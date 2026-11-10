#!/usr/bin/env python3
"""One synthetic counterexample, reusing run.py unchanged; stdout only."""

import argparse
import hashlib
import importlib.util
import io
import json
from contextlib import redirect_stdout
from datetime import datetime, timezone
from pathlib import Path
import re
import sqlite3
import sys
from unittest.mock import patch

sys.dont_write_bytecode = True

EXPECTED = [
    {"id": "P1", "depends_on_path": ["P1", "I1"]},
    {"id": "P2", "depends_on_path": ["P2", "P1", "I1"]},
]
PREDICTED_SWAP = [
    {"id": "P1", "depends_on_path": ["P1", "I1"]},
    {"id": "U1", "depends_on_path": ["U1", "P1", "I1"]},
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def derive_swap(raw):
    lines = raw.decode("utf-8").split("\n")
    rows = [(i, json.loads(line)) for i, line in enumerate(lines) if line]
    matches = [(i, row) for i, row in rows if row["id"] == "E3"]
    require(len(matches) == 1, "ONE_E3_REQUIRED")
    index, before = matches[0]
    require((before["record_type"], before["relation"], before["from"], before["to"])
            == ("edge", "depends_on", "P2", "P1"), "BASE_RELATION_CHANGED")
    after = dict(before, **{"from": "U1"})
    lines[index] = json.dumps(after, ensure_ascii=False, separators=(",", ":"))
    derived = "\n".join(lines).encode("utf-8")
    derived_rows = [json.loads(line) for line in derived.decode("utf-8").split("\n") if line]
    differences = [(a["id"], key) for (_, a), b in zip(rows, derived_rows)
                   for key in a if a[key] != b[key]]
    require(len(rows) == len(derived_rows) and differences == [("E3", "from")],
            "ONLY_E3_FROM_MAY_CHANGE")
    return derived, {"record_id": "E3", "line": index + 1, "field": "from",
                     "before": "P2", "after": "U1",
                     "preserved": "All other record fields and all other input lines"}


def observe(baseline, fixture, raw, name):
    # Supply bytes at the existing read boundary, never by rewriting the fixture.
    # This also runs the ORIGINAL seven expectations in run.main(), unchanged.
    read_bytes = Path.read_bytes

    def input_bytes(path):
        return raw if path.resolve() == fixture else read_bytes(path)

    output = io.StringIO()
    with patch.object(baseline.Path, "read_bytes", input_bytes), redirect_stdout(output):
        exit_code = baseline.main()
    report = json.loads(output.getvalue())
    require(report["fixture_sha256"] == digest(raw), "SUPPLIED_INPUT_HASH_MISMATCH")
    nodes, edges = report["input_counts"]["nodes"], report["input_counts"]["edges"]
    records = [json.loads(line) for line in raw.decode("utf-8").split("\n") if line]
    ids = {r["id"] for r in records if r["record_type"] == "node"}
    endpoints_exist = all(r["from"] in ids and r["to"] in ids
                          for r in records if r["record_type"] == "edge")
    expected_ids = {r["id"] for r in EXPECTED}
    file_ids = {r["id"] for r in report["file_candidates"]}
    sqlite_ids = {r["id"] for r in report["sqlite_candidates"]}
    # Each path/line points to a baseline location. Identify the actual snapshot
    # explicitly so a derived E3 is never presented as unchanged source content.
    bundle = report["evidence_bundle"]
    for record in bundle["records"] + bundle["relations"]:
        record["source_ref"].update(input_variant=name, input_sha256=digest(raw),
                                    path_role="baseline location; use variant and hash for content identity")
    return {
        "variant": name,
        "input_sha256": digest(raw),
        "input_accepted_by_original_loader": True,
        "input_counts": {"nodes": nodes, "edges": edges},
        "referential_integrity": {
            "all_endpoints_exist": endpoints_exist,
            "sqlite_query_completed": True,
            "observation_scope": "Original sqlite_query enabled foreign_keys and completed inserts/queries; no separate foreign_key_check or failure-case test.",
        },
        "complete_evidence_bundle_equal": report["checks"]["complete_evidence_bundle_equal"],
        "file_candidates": report["file_candidates"],
        "sqlite_candidates": report["sqlite_candidates"],
        "file_matches_known_answer": report["file_candidates"] == EXPECTED,
        "sqlite_matches_known_answer": report["sqlite_candidates"] == EXPECTED,
        "file_missing": sorted(expected_ids - file_ids),
        "file_extra": sorted(file_ids - expected_ids),
        "sqlite_missing": sorted(expected_ids - sqlite_ids),
        "sqlite_extra": sorted(sqlite_ids - expected_ids),
        "original_run_py_result": report["result"],
        "original_run_py_exit_code": exit_code,
        "original_run_py_checks": report["checks"],
        "original_run_py_executed_at_utc": report["executed_at_utc"],
        "evidence_bundle": bundle,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-source-commit", help="Caller-verified commit for fixture/run.py, not for this new script")
    args = parser.parse_args()
    if args.base_source_commit:
        require(re.fullmatch(r"[0-9a-f]{40}", args.base_source_commit), "FULL_COMMIT_REQUIRED")
    script = Path(__file__).resolve()
    fixture, runner = script.with_name("fixture.jsonl"), script.with_name("run.py")
    raw, runner_bytes = fixture.read_bytes(), runner.read_bytes()
    spec = importlib.util.spec_from_file_location("correction_baseline", runner)
    baseline = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(baseline)
    control = observe(baseline, fixture, raw, "baseline")
    require(control["original_run_py_result"] == "PASS"
            and control["file_matches_known_answer"] and control["sqlite_matches_known_answer"],
            "BASELINE_NOT_CONFIRMED; no swap executed")
    derived, transformation = derive_swap(raw)
    swapped = observe(baseline, fixture, derived, "E3_from_P2_to_U1")
    false_checks = {name for name, value in swapped["original_run_py_checks"].items() if not value}
    expected_observation = (
        swapped["complete_evidence_bundle_equal"]
        and swapped["file_candidates"] == swapped["sqlite_candidates"] == PREDICTED_SWAP
        and not swapped["file_matches_known_answer"] and not swapped["sqlite_matches_known_answer"]
        and swapped["original_run_py_result"] == "FAIL" and swapped["original_run_py_exit_code"] == 1
        and false_checks == {"expected_candidates_and_paths", "expected_context_records"}
        and swapped["input_counts"] == control["input_counts"] == {"nodes": 6, "edges": 4}
        and swapped["referential_integrity"]["all_endpoints_exist"]
    )
    require(fixture.read_bytes() == raw and runner.read_bytes() == runner_bytes,
            "BASE_FILES_CHANGED_DURING_COMPARISON")
    result = {
        "experiment_id": "SQLITE-CORRECTION-RELATION-SWAP-001", "synthetic": True,
        "observation": "EXPECTED_COUNTEREXAMPLE_OBSERVED" if expected_observation else "UNEXPECTED_OBSERVATION",
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version.split()[0], "sqlite": sqlite3.sqlite_version,
        "base_source_commit_supplied_by_caller": args.base_source_commit,
        "source_revision_policy": "Caller supplies verified base commit; no Git/network lookup. Hashes identify executed bytes. Script revision is separate.",
        "fixture_sha256": digest(raw), "runner_sha256": digest(runner_bytes),
        "probe_sha256": digest(script.read_bytes()), "derived_input_sha256": digest(derived),
        "transformation": transformation, "known_answer": EXPECTED,
        "prediction_before_observation": PREDICTED_SWAP,
        "variants": [control, swapped], "base_files_unchanged": True,
        "limits": [
            "An observed counterexample is not correct retrieval: swapped candidates disagree with the case author's known answer.",
            "Both routes share parsing/packaging and the same supplied relations. Original expectations remain unchanged.",
            "E3 scope text intentionally still describes P2: this one-field swap is not a general semantic-error test suite.",
            "No automatic language understanding, model calls, Human success appraisal, or real-life-effect evidence.",
        ],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if expected_observation else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, sqlite3.Error) as exc:
        print(json.dumps({"observation": "COMPARISON_ERROR", "error": str(exc)}, ensure_ascii=False))
        raise SystemExit(2)
