#!/usr/bin/env python3
"""One synthetic correction case; stdout only; standard library; no network."""

import hashlib
import json
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

CASE = "SQLITE-CORRECTION-001"
SOURCE = "sandbox/sqlite-correction/fixture.jsonl"
COMMON = {"schema_version", "case_id", "synthetic", "record_type", "id"}
FIELDS = {
    "node": {"kind", "speaker", "text", "occurred_at", "recorded_at", "scope", "status"},
    "edge": {"relation", "from", "to", "evidence", "scope"},
}


class InputError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise InputError(message)


def unique_object(pairs):
    obj = {}
    for key, value in pairs:
        require(key not in obj, "DUPLICATE_JSON_KEY: " + key)
        obj[key] = value
    return obj


def reject_constant(value):
    raise InputError("NON_JSON_CONSTANT: " + value)


def load_fixture(raw):
    nodes, edges, ids = {}, {}, set()
    for number, line in enumerate(raw.decode("utf-8").splitlines(), 1):
        require(bool(line.strip()), f"EMPTY_JSONL_LINE: {number}")
        record = json.loads(line, object_pairs_hook=unique_object,
                            parse_constant=reject_constant)
        require(isinstance(record, dict), f"OBJECT_REQUIRED: line {number}")
        if (record.get("record_type") == "withdrawal"
                or record.get("kind") == "withdrawal"
                or record.get("relation") in ("withdraws", "revokes")
                or record.get("status") == "withdrawn"):
            raise InputError(f"UNSUPPORTED_WITHDRAWAL: line {number}")
        kind = record.get("record_type")
        require(isinstance(kind, str) and kind in FIELDS, f"UNSUPPORTED_RECORD_TYPE: line {number}")
        require(set(record) == COMMON | FIELDS[kind],
                f"UNSUPPORTED_OR_MISSING_FIELDS: line {number}")
        require(type(record["schema_version"]) is int and record["schema_version"] == 1,
                "UNSUPPORTED_SCHEMA_VERSION")
        require(record["case_id"] == CASE and record["synthetic"] is True,
                "THIS_RUNNER_ACCEPTS_ONLY_ITS_SYNTHETIC_CASE")
        for key in (COMMON | FIELDS[kind]) - {"schema_version", "synthetic"}:
            require(isinstance(record[key], str) and bool(record[key].strip()),
                    f"NONEMPTY_STRING_REQUIRED: line {number}, field {key}")
        identifier = record["id"]
        require(re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]{0,63}", identifier) is not None,
                "INVALID_ID: " + identifier)
        require(identifier not in ids, "DUPLICATE_ID: " + identifier)
        ids.add(identifier)
        if kind == "node":
            require(record["kind"] in {"source", "interpretation", "proposal", "correction"},
                    "UNSUPPORTED_NODE_KIND: " + identifier)
            require(record["speaker"] in {"fictional_human", "fictional_ai"},
                    "UNSUPPORTED_SPEAKER: " + identifier)
            require(record["status"] in {"reported_in_synthetic_case", "candidate_not_adopted",
                                         "proposed_not_adopted"},
                    "UNSUPPORTED_STATUS: " + identifier)
        else:
            require(record["relation"] in {"based_on", "depends_on", "corrects"},
                    "UNSUPPORTED_RELATION: " + identifier)
        record["source_ref"] = {"path": SOURCE, "line": number, "record_id": identifier}
        (nodes if kind == "node" else edges)[identifier] = record
    for edge in edges.values():
        require(edge["from"] in nodes and edge["to"] in nodes,
                "DANGLING_REFERENCE: " + edge["id"])
    require(set(nodes) == {"S1", "I1", "P1", "P2", "C1", "U1"}
            and set(edges) == {"E1", "E2", "E3", "E4"}, "UNSUPPORTED_CASE_SHAPE")
    require(nodes["C1"]["kind"] == "correction"
            and nodes["C1"]["speaker"] == "fictional_human", "INVALID_CORRECTION_SOURCE")
    return nodes, edges


def package(target, paths, records, relations):
    return {
        "correction_id": "C1",
        "corrected_interpretation_id": target,
        "review_candidates": [
            {"id": key, "depends_on_path": paths[key]} for key in sorted(paths)
        ],
        "records": sorted(records, key=lambda r: r["id"]),
        "relations": sorted(relations, key=lambda r: r["id"]),
        "coverage": "Recorded relations in this synthetic snapshot only; semantic missing edges remain unknown.",
        "authority": "Review candidates only; no adoption, cancellation, execution, or real Human state change.",
    }


def file_query(nodes, edges):
    corrections = [e for e in edges.values()
                   if e["relation"] == "corrects" and e["from"] == "C1"]
    require(len(corrections) == 1, "ONE_CORRECTION_TARGET_REQUIRED")
    target = corrections[0]["to"]
    paths, pending = {target: [target]}, [target]
    while pending:
        parent = pending.pop(0)
        for edge in sorted(edges.values(), key=lambda e: e["id"]):
            child = edge["from"]
            if edge["relation"] == "depends_on" and edge["to"] == parent and child not in paths:
                paths[child] = [child] + paths[parent]
                pending.append(child)
    selected = set(paths) | {"C1"}
    while True:
        extra = {e["to"] for e in edges.values()
                 if e["relation"] == "based_on" and e["from"] in selected}
        if extra <= selected:
            break
        selected |= extra
    proposals = {key: path for key, path in paths.items() if nodes[key]["kind"] == "proposal"}
    return package(target, proposals, [nodes[key] for key in selected],
                   [e for e in edges.values() if e["from"] in selected and e["to"] in selected])


def sqlite_query(nodes, edges):
    db = sqlite3.connect(":memory:")
    try:
        db.execute("PRAGMA foreign_keys = ON")
        db.execute("PRAGMA temp_store = MEMORY")
        db.executescript("""
            CREATE TABLE nodes(id TEXT PRIMARY KEY, kind TEXT NOT NULL, payload TEXT NOT NULL);
            CREATE TABLE edges(id TEXT PRIMARY KEY, relation TEXT NOT NULL,
                source_id TEXT REFERENCES nodes(id), target_id TEXT REFERENCES nodes(id),
                payload TEXT NOT NULL);
        """)
        with db:
            db.executemany("INSERT INTO nodes VALUES (?, ?, ?)",
                           [(r["id"], r["kind"], json.dumps(r, ensure_ascii=False)) for r in nodes.values()])
            db.executemany("INSERT INTO edges VALUES (?, ?, ?, ?, ?)",
                           [(e["id"], e["relation"], e["from"], e["to"], json.dumps(e, ensure_ascii=False))
                            for e in edges.values()])
        db.execute("PRAGMA query_only = ON")
        targets = db.execute("SELECT target_id FROM edges WHERE relation = 'corrects' AND source_id = ?",
                             ("C1",)).fetchall()
        require(len(targets) == 1, "ONE_CORRECTION_TARGET_REQUIRED")
        target = targets[0][0]
        rows = db.execute("""
            WITH RECURSIVE affected(id, path) AS (
                SELECT ?, ?
                UNION ALL
                SELECT e.source_id, e.source_id || '/' || a.path
                FROM edges e JOIN affected a ON e.target_id = a.id
                WHERE e.relation = 'depends_on'
                  AND instr('/' || a.path || '/', '/' || e.source_id || '/') = 0
            )
            SELECT a.id, a.path, n.kind FROM affected a JOIN nodes n ON n.id = a.id
            ORDER BY a.id, a.path
        """, (target, target)).fetchall()
        seed = sorted({row[0] for row in rows} | {"C1"})
        placeholders = ",".join("?" for _ in seed)
        selected = [row[0] for row in db.execute(f"""
            WITH RECURSIVE context(id) AS (
                SELECT id FROM nodes WHERE id IN ({placeholders})
                UNION
                SELECT e.target_id FROM edges e JOIN context c ON e.source_id = c.id
                WHERE e.relation = 'based_on'
            ) SELECT id FROM context ORDER BY id
        """, seed)]
        placeholders = ",".join("?" for _ in selected)
        records = [json.loads(row[0]) for row in db.execute(
            f"SELECT payload FROM nodes WHERE id IN ({placeholders}) ORDER BY id", selected)]
        relations = [json.loads(row[0]) for row in db.execute(
            f"SELECT payload FROM edges WHERE source_id IN ({placeholders}) "
            f"AND target_id IN ({placeholders}) ORDER BY id", selected + selected)]
        return package(target, {key: path.split("/") for key, path, kind in rows if kind == "proposal"},
                       records, relations)
    finally:
        db.close()


def main():
    runner = Path(__file__).resolve()
    raw = runner.with_name("fixture.jsonl").read_bytes()
    nodes, edges = load_fixture(raw)
    file_result = file_query(nodes, edges)
    sql_result = sqlite_query(nodes, edges)
    checks = {
        "complete_evidence_bundle_equal": file_result == sql_result,
        "expected_candidates_and_paths": sql_result["review_candidates"] == [
            {"id": "P1", "depends_on_path": ["P1", "I1"]},
            {"id": "P2", "depends_on_path": ["P2", "P1", "I1"]}],
        "expected_context_records": {r["id"] for r in sql_result["records"]}
                                    == {"S1", "I1", "P1", "P2", "C1"},
        "expected_context_relations": {e["id"] for e in sql_result["relations"]}
                                      == {"E1", "E2", "E3", "E4"},
        "correction_targets_interpretation": sql_result["corrected_interpretation_id"] == "I1",
        "source_scope_preserved": nodes["S1"]["scope"] == "Day 1 only",
        "proposals_remain_unadopted": all(nodes[key]["status"] == "proposed_not_adopted"
                                          for key in ("P1", "P2", "U1")),
    }
    output = {
        "case_id": CASE, "synthetic": True,
        "result": "PASS" if all(checks.values()) else "FAIL",
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version.split()[0], "sqlite": sqlite3.sqlite_version,
        "fixture_sha256": hashlib.sha256(raw).hexdigest(),
        "runner_sha256": hashlib.sha256(runner.read_bytes()).hexdigest(),
        "source_revision_policy": "Exact local input bytes identified above; no automatic latest-main claim.",
        "input_counts": {"nodes": len(nodes), "edges": len(edges)},
        "checks": checks,
        "file_candidates": file_result["review_candidates"],
        "sqlite_candidates": sql_result["review_candidates"],
        "not_reached": sorted(set(nodes) - {r["id"] for r in sql_result["records"]}),
        "evidence_bundle": sql_result,
        "limits": ["One hand-authored case, shared parser and output packaging; not independent semantic verification.",
                   "No performance, persistence, concurrency, withdrawal, or real-life-effect validation.",
                   "U1 not reached means no path in this snapshot, not proof of universal irrelevance."],
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (InputError, UnicodeError, json.JSONDecodeError, OSError, sqlite3.Error) as exc:
        print(json.dumps({"result": "ERROR", "error": str(exc)}, ensure_ascii=False))
        raise SystemExit(2)
