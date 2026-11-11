#!/usr/bin/env python3
"""One synthetic all-path query comparison; memory and stdout only."""

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import re
import sqlite3
import sys

sys.dont_write_bytecode = True

VARIANT = "V2_BRANCH_001"
REQUIRED_V2_SHA256 = "47f6663c6d19512ecec057add2ecbeee91b0e3d9ad8f93f7b3f84ce4f46de909"
E5 = {
    "schema_version": 1, "case_id": "SQLITE-CORRECTION-001", "synthetic": True,
    "record_type": "edge", "id": "E5", "relation": "depends_on", "from": "P2", "to": "I1",
    "evidence": "synthetic_fixture_author_declaration; not independent validation",
    "scope": "P2 also uses I1 directly as a premise in this synthetic variant",
}
EXPECTED_PATHS = (
    ("P1", ("P1", "I1"), ("E2",)),
    ("P2", ("P2", "I1"), ("E5",)),
    ("P2", ("P2", "P1", "I1"), ("E3", "E2")),
)
EXPECTED_NODES = {"S1", "I1", "P1", "P2", "C1"}
EXPECTED_EDGES = {"E1", "E2", "E3", "E4", "E5"}
SOURCE = "sandbox/sqlite-correction/fixture.jsonl"
SCRIPT_SOURCE = "sandbox/sqlite-correction/check_dependency_paths.py"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def prepare_input(v1, snapshot, baseline, commit, code_hash):
    require(digest(v1) == snapshot.V1_SHA256, "BASE_FIXTURE_CHANGED")
    v2, v2_change = snapshot.derive_v2(v1)
    require(digest(v2) == REQUIRED_V2_SHA256 == snapshot.REQUIRED_V2_SHA256,
            "FIXED_V2_HASH_MISMATCH")
    addition = encode(E5) + b"\n"
    derived = v2 + addition
    lines = derived.splitlines(keepends=True)
    require(v2.endswith(b"\n") and len(lines) == 11 and b"".join(lines[:10]) == v2
            and lines[10] == addition, "ONLY_SPECIFIED_E5_MAY_BE_APPENDED")
    # Keep the original strict 6-node/4-edge loader intact. It sees only V2.
    nodes, edges = baseline.load_fixture(b"".join(lines[:10]))
    added = json.loads(lines[10], object_pairs_hook=baseline.unique_object,
                       parse_constant=baseline.reject_constant)
    require(added == E5 and added["id"] not in nodes and added["id"] not in edges
            and added["from"] in nodes and added["to"] in nodes, "INVALID_E5_EXTENSION")
    edges[added["id"]] = added
    require(len(nodes) == 6 and len(edges) == 5, "INVALID_DERIVED_COUNTS")
    original = {row["id"]: row for row in (json.loads(line) for line in lines)}
    for index, line in enumerate(lines, 1):
        identifier = json.loads(line)["id"]
        record = (nodes if identifier in nodes else edges)[identifier]
        record["source_ref"] = {
            "record_id": identifier, "input_variant": VARIANT,
            "input_sha256": digest(derived), "input_line": index,
            "origin": "generated_relation" if identifier == "E5" else "derived_baseline_record",
            "baseline_path": None if identifier == "E5" else SOURCE,
            "baseline_line": None if identifier == "E5" else index,
            "base_source_commit_supplied_by_caller": commit,
        }
        if identifier == "E5":
            record["source_ref"].update(definition_path=SCRIPT_SOURCE, definition_code_sha256=code_hash)
    provenance = {
        "baseline": {"path": SOURCE, "sha256": digest(v1), "bytes": len(v1),
                     "commit_supplied_by_caller": commit},
        "parent_input": {"variant": "V2", "sha256": digest(v2), "bytes": len(v2),
                         "transformation": v2_change},
        "input": {"variant": VARIANT, "sha256": digest(derived), "bytes": len(derived),
                  "nodes": 6, "edges": 5},
        "transformation": {"operation": "append_one_generated_E5_line", "record": E5,
                           "serialization": "UTF-8 JSON; ensure_ascii=False; sort_keys=True; compact separators; final LF",
                           "preserved": "All ten V2 lines and fields, byte for byte"},
    }
    frozen_reference = encode(original)
    frozen_metadata = encode({key: row["source_ref"] for key, row in (nodes | edges).items()})
    return derived, nodes, edges, provenance, frozen_reference, frozen_metadata


def package_paths(target, paths, records, relations):
    # A list retains every path. Do not collapse rows by proposal ID.
    return {
        "correction_id": "C1", "corrected_interpretation_id": target,
        "review_paths": [{"proposal_id": key, "node_path": list(node_path), "edge_path": list(edge_path)}
                         for key, node_path, edge_path in sorted(paths)],
        "records": sorted(records, key=lambda row: row["id"]),
        "relations": sorted(relations, key=lambda row: row["id"]),
        "coverage": "All recorded simple depends_on paths in this one synthetic variant; missing semantic relations remain unknown.",
        "authority": "Review only; no adoption, cancellation, execution, or current Human intent inferred.",
        "evidence_independence": "P2's two paths converge on the same I1; not two independent supporting sources.",
    }


def file_query(nodes, edges):
    corrections = [edge for edge in edges.values()
                   if edge["relation"] == "corrects" and edge["from"] == "C1"]
    require(len(corrections) == 1, "ONE_CORRECTION_TARGET_REQUIRED")
    target = corrections[0]["to"]
    reverse, based_on = defaultdict(list), defaultdict(list)
    for edge in sorted(edges.values(), key=lambda row: row["id"]):
        if edge["relation"] == "depends_on":
            reverse[edge["to"]].append(edge)
        elif edge["relation"] == "based_on":
            based_on[edge["from"]].append(edge["to"])
    pending, paths = [(target, (target,), ())], []
    while pending:
        current, node_path, edge_path = pending.pop()
        if nodes[current]["kind"] == "proposal" and nodes[current]["status"] == "proposed_not_adopted":
            paths.append((current, node_path, edge_path))
        for edge in reverse[current]:
            child = edge["from"]
            if child not in node_path:
                pending.append((child, (child,) + node_path, (edge["id"],) + edge_path))
    selected = {target, "C1"} | {key for _, path, _ in paths for key in path}
    pending = list(selected)
    while pending:
        for key in based_on[pending.pop()]:
            if key not in selected:
                selected.add(key)
                pending.append(key)
    return package_paths(target, paths, [nodes[key] for key in selected],
                         [edge for edge in edges.values()
                          if edge["from"] in selected and edge["to"] in selected])


def open_database(nodes, edges):
    db = sqlite3.connect(":memory:")
    try:
        db.execute("PRAGMA foreign_keys = ON")
        db.execute("PRAGMA temp_store = MEMORY")
        db.executescript("""
            CREATE TABLE nodes(id TEXT PRIMARY KEY, kind TEXT NOT NULL, status TEXT NOT NULL, payload TEXT NOT NULL);
            CREATE TABLE edges(id TEXT PRIMARY KEY, relation TEXT NOT NULL,
                source_id TEXT REFERENCES nodes(id), target_id TEXT REFERENCES nodes(id), payload TEXT NOT NULL);
        """)
        with db:
            db.executemany("INSERT INTO nodes VALUES (?, ?, ?, ?)",
                           [(row["id"], row["kind"], row["status"], encode(row).decode("utf-8")) for row in nodes.values()])
            db.executemany("INSERT INTO edges VALUES (?, ?, ?, ?, ?)",
                           [(row["id"], row["relation"], row["from"], row["to"], encode(row).decode("utf-8"))
                            for row in edges.values()])
        db.execute("PRAGMA query_only = ON")
        return db
    except Exception:
        db.close()
        raise


def sqlite_query(nodes, edges):
    db = open_database(nodes, edges)
    try:
        targets = db.execute("SELECT target_id FROM edges WHERE relation = 'corrects' AND source_id = ?", ("C1",)).fetchall()
        require(len(targets) == 1, "ONE_CORRECTION_TARGET_REQUIRED")
        target = targets[0][0]
        rows = db.execute("""
            WITH RECURSIVE affected(id, node_path, edge_path) AS (
                SELECT ?, ?, ''
                UNION ALL
                SELECT e.source_id, e.source_id || '/' || a.node_path,
                       e.id || CASE WHEN a.edge_path = '' THEN '' ELSE '/' || a.edge_path END
                FROM edges e JOIN affected a ON e.target_id = a.id
                WHERE e.relation = 'depends_on'
                  AND instr('/' || a.node_path || '/', '/' || e.source_id || '/') = 0
            )
            SELECT a.id, a.node_path, a.edge_path FROM affected a JOIN nodes n ON n.id = a.id
            WHERE n.kind = 'proposal' AND n.status = 'proposed_not_adopted'
            ORDER BY a.id, a.node_path, a.edge_path
        """, (target, target)).fetchall()
        paths = [(key, tuple(node_path.split("/")), tuple(edge_path.split("/")))
                 for key, node_path, edge_path in rows]
        seed = sorted({target, "C1"} | {key for _, path, _ in paths for key in path})
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
            f"SELECT payload FROM edges WHERE source_id IN ({placeholders}) AND target_id IN ({placeholders}) ORDER BY id",
            selected + selected)]
        return package_paths(target, paths, records, relations)
    finally:
        db.close()


def assess(bundle, frozen_reference, frozen_metadata):
    reference, metadata = json.loads(frozen_reference), json.loads(frozen_metadata)
    rows = bundle["records"] + bundle["relations"]
    ids = [row["id"] for row in rows]
    expected_ids = EXPECTED_NODES | EXPECTED_EDGES
    issues = []
    for row in rows:
        raw = {key: value for key, value in row.items() if key != "source_ref"}
        expected = reference.get(row["id"], {})
        fields = sorted(key for key in raw.keys() | expected.keys() if raw.get(key) != expected.get(key)
                        or (key in raw) != (key in expected))
        if fields:
            issues.append({"id": row["id"], "fields": fields})
    paths = [(row["proposal_id"], tuple(row["node_path"]), tuple(row["edge_path"])) for row in bundle["review_paths"]]
    missing = sorted((Counter(EXPECTED_PATHS) - Counter(paths)).elements())
    extra = sorted((Counter(paths) - Counter(EXPECTED_PATHS)).elements())
    valid_paths = True
    for key, node_path, edge_path in paths:
        valid_paths &= bool(node_path) and node_path[0] == key and node_path[-1] == "I1"
        valid_paths &= len(node_path) == len(set(node_path)) and len(edge_path) == len(node_path) - 1
        for index, edge_id in enumerate(edge_path):
            edge = reference.get(edge_id, {})
            valid_paths &= (edge.get("relation"), edge.get("from"), edge.get("to")) == (
                "depends_on", node_path[index], node_path[index + 1])
    actual_nodes = {row["id"]: row for row in bundle["records"]}
    checks = {
        "candidate_ids_match": {key for key, _, _ in paths} == {"P1", "P2"},
        "all_paths_match_fixed_expectation": not missing and not extra,
        "no_duplicate_paths": len(paths) == len(set(paths)),
        "paths_follow_named_edges": bool(valid_paths),
        "context_node_ids_match": set(actual_nodes) == EXPECTED_NODES,
        "context_edge_ids_match": {row["id"] for row in bundle["relations"]} == EXPECTED_EDGES,
        "ten_unique_source_records": len(ids) == len(set(ids)) == 10 and set(ids) == expected_ids,
        "all_original_fields_match": not issues,
        "source_metadata_matches": all(row["source_ref"] == metadata.get(row["id"]) for row in rows),
        "full_V2_C1_retained": actual_nodes.get("C1", {}).get("text") == reference["C1"]["text"],
        "day_one_scope_retained": actual_nodes.get("S1", {}).get("scope") == "Day 1 only",
        "proposals_remain_unadopted": all(actual_nodes.get(key, {}).get("status") == "proposed_not_adopted" for key in ("P1", "P2")),
        "correction_target_preserved": (bundle["correction_id"], bundle["corrected_interpretation_id"]) == ("C1", "I1"),
    }
    return {"checks": checks, "matches_fixed_expectation": all(checks.values()),
            "missing_paths": missing, "extra_paths": extra, "record_issues": issues,
            "checked_records": len(ids), "bundle_sha256": digest(encode(bundle))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-source-commit", required=True, help="Caller-verified source commit; no network lookup")
    args = parser.parse_args()
    require(re.fullmatch(r"[0-9a-f]{40}", args.base_source_commit), "FULL_COMMIT_REQUIRED")
    script = Path(__file__).resolve()
    names = ("fixture.jsonl", "run.py", "check_relation_swap.py", "check_snapshot_version.py",
             "check_evidence_snapshot.py", "check_evidence_recovery.py")
    originals = {name: script.with_name(name).read_bytes() for name in names}
    spec = importlib.util.spec_from_file_location("paths_snapshot_tools", script.with_name("check_snapshot_version.py"))
    snapshot = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(snapshot)
    baseline = snapshot.load_module(script.with_name("run.py"), "paths_baseline_tools")
    code_hash = digest(script.read_bytes())
    derived, nodes, edges, provenance, reference, metadata = prepare_input(
        originals["fixture.jsonl"], snapshot, baseline, args.base_source_commit, code_hash)
    fixed_at = datetime.now(timezone.utc).isoformat()
    input_frozen = encode({"nodes": nodes, "edges": edges})
    reports, bundles, calls = {}, {}, {"file": 0, "sqlite": 0}
    for name, query in (("file", file_query), ("sqlite", sqlite_query)):
        # Equal independent copies of the same parsed input; no previous main() calls.
        supplied = json.loads(input_frozen)
        calls[name] += 1
        bundles[name] = query(supplied["nodes"], supplied["edges"])
        require(encode(supplied) == input_frozen, "QUERY_MODIFIED_INPUT: " + name)
        reports[name] = assess(bundles[name], reference, metadata)
    equal = bundles["file"] == bundles["sqlite"]
    retained = all(script.with_name(name).read_bytes() == raw for name, raw in originals.items())
    require(retained, "BASE_FILES_CHANGED")
    passed = equal and all(report["matches_fixed_expectation"] for report in reports.values())
    output = {
        "experiment_id": "SQLITE-CORRECTION-DEPENDENCY-PATHS-001", "synthetic": True,
        "observation": "EXPECTED_ALL_PATHS_OBSERVED" if passed else "ALL_PATHS_NOT_CONFIRMED",
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version.split()[0], "sqlite": sqlite3.sqlite_version,
        "platform": platform.system(), "machine": platform.machine(),
        "base_source_commit_supplied_by_caller": args.base_source_commit,
        "base_file_sha256": {name: digest(raw) for name, raw in originals.items()},
        "probe_sha256": code_hash, "provenance": provenance,
        "fixed_before_search": {"at_utc": fixed_at, "input_sha256": digest(derived),
            "reference_sha256": digest(reference), "metadata_sha256": digest(metadata),
            "expected_paths": EXPECTED_PATHS, "expected_nodes": sorted(EXPECTED_NODES),
            "expected_edges": sorted(EXPECTED_EDGES)},
        "search_execution": calls, "complete_evidence_bundle_equal": equal,
        "routes": reports, "evidence_bundles": bundles, "base_files_unchanged": retained,
        "limits": [
            "One author-declared E5, shared loader/formatter/checker; not independent semantic verification.",
            "Two P2 paths converge on I1; path count does not establish evidence independence or greater confidence.",
            "Only this fixed simple-path input was exercised; no cycle, scalability, performance, or repeated-failure trials.",
            "Commit is caller-verified provenance, not automatic latest-main or authenticity verification.",
            "No AI integration, Human success appraisal, actual workload reduction, or adoption decision established.",
        ],
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, sqlite3.Error) as exc:
        print(json.dumps({"observation": "EXPERIMENT_ERROR", "error": str(exc)}, ensure_ascii=False))
        raise SystemExit(2)
