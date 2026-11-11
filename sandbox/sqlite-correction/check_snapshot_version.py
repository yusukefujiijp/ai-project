#!/usr/bin/env python3
"""One synthetic version comparison; reuse existing searches; stdout only."""

import argparse
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path
import platform
import re
import sqlite3
import sys

sys.dont_write_bytecode = True

# Fixed before the comparison, not learned from the input being assessed.
V1_SHA256 = "aa5c4e9b446fc79a158b9f0525cd69062fe7f4de3c89cc8049802f7c861193b5"
REQUIRED_V2_SHA256 = "47f6663c6d19512ecec057add2ecbeee91b0e3d9ad8f93f7b3f84ce4f46de909"
ORIGINAL_C1 = "その日だけの希望だった。常に静かな作業を好むという意味ではない。"
APPEND_TEXT = "次の相談では、その日の希望を確かめてください。"
EXPECTED_CANDIDATES = [
    {"id": "P1", "depends_on_path": ["P1", "I1"]},
    {"id": "P2", "depends_on_path": ["P2", "P1", "I1"]},
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def derive_v2(raw):
    lines = raw.decode("utf-8").split("\n")
    rows = [(i, json.loads(line)) for i, line in enumerate(lines) if line]
    matches = [(i, row) for i, row in rows if row["id"] == "C1"]
    require(len(matches) == 1, "ONE_C1_REQUIRED")
    index, before = matches[0]
    require((before["record_type"], before["kind"], before["speaker"], before["text"])
            == ("node", "correction", "fictional_human", ORIGINAL_C1), "BASE_C1_CHANGED")
    after = dict(before, text=ORIGINAL_C1 + APPEND_TEXT)
    derived_lines = list(lines)
    derived_lines[index] = json.dumps(after, ensure_ascii=False, separators=(",", ":"))
    derived = "\n".join(derived_lines).encode("utf-8")
    derived_rows = [json.loads(line) for line in derived_lines if line]
    require(len(rows) == len(derived_rows) == 10, "RECORD_COUNT_CHANGED")
    for (i, row), new in zip(rows, derived_rows):
        require(new == (after if i == index else row), "UNEXPECTED_FIELD_CHANGE")
        require(i == index or lines[i] == derived_lines[i], "OTHER_LINE_CHANGED")
    return derived, {
        "operation": "append_to_C1_text", "record_id": "C1", "line": index + 1,
        "field": "text", "appended_text": APPEND_TEXT,
        "before": ORIGINAL_C1, "after": ORIGINAL_C1 + APPEND_TEXT,
        "serialization": "Only C1 line: UTF-8 JSON, ensure_ascii=False, compact separators; retain key order and final LF",
        "preserved": "Every other field, relation, input line, and record count",
        "synthetic_only": True,
    }


def assess_version(raw, required_bytes, digest):
    actual_hash = digest(raw)
    if required_bytes is None:
        return {
            "required_version": None, "required_sha256": None,
            "actual_sha256": actual_hash, "matches_required_bytes": None,
            "matches_required_hash": None, "verdict": "UNKNOWN_REQUIREMENT",
            "reason": "An input hash identifies bytes but supplies no requested-version information.",
        }
    # The requirement is frozen V2; never replace it with the observed input.
    require(digest(required_bytes) == REQUIRED_V2_SHA256, "REQUIREMENT_CHANGED")
    bytes_match = raw == required_bytes
    hash_match = actual_hash == REQUIRED_V2_SHA256
    return {
        "required_version": "V2", "required_sha256": REQUIRED_V2_SHA256,
        "actual_sha256": actual_hash, "matches_required_bytes": bytes_match,
        "matches_required_hash": hash_match,
        "verdict": "MATCH" if bytes_match and hash_match else "MISMATCH",
    }


def attach_provenance(observation, commit, transformation):
    for record in observation["evidence_bundle"]["records"] + observation["evidence_bundle"]["relations"]:
        record["source_ref"].update(
            base_source_commit_supplied_by_caller=commit,
            baseline_sha256=V1_SHA256,
            transformation_id=observation["variant"],
            transformation=transformation,
        )


def payload_without_source_refs(observation):
    bundle = json.loads(json.dumps(observation["evidence_bundle"], ensure_ascii=False))
    for record in bundle["records"] + bundle["relations"]:
        record.pop("source_ref")
    return bundle


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-source-commit", help="Caller-verified commit for fixture/run.py/check_relation_swap.py")
    args = parser.parse_args()
    if args.base_source_commit:
        require(re.fullmatch(r"[0-9a-f]{40}", args.base_source_commit), "FULL_COMMIT_REQUIRED")
    script = Path(__file__).resolve()
    fixture, runner, helper = (script.with_name(name) for name in
                               ("fixture.jsonl", "run.py", "check_relation_swap.py"))
    originals = {path: path.read_bytes() for path in (fixture, runner, helper)}
    observer = load_module(helper, "snapshot_observer")
    baseline = load_module(runner, "snapshot_baseline")
    digest = observer.digest
    v1 = originals[fixture]
    require(digest(v1) == V1_SHA256, "BASE_FIXTURE_CHANGED; do not retarget the requirement")
    # Freeze immutable V2 bytes and verify their predeclared hash BEFORE any search.
    required_v2_bytes, transformation = derive_v2(v1)
    require(digest(required_v2_bytes) == REQUIRED_V2_SHA256, "FIXED_V2_HASH_MISMATCH")
    required_fixed_at = datetime.now(timezone.utc).isoformat()
    transformations = {"V1": {"operation": "identity", "synthetic_only": True},
                       "V2": transformation}
    prediction = {
        "both_versions_original_seven_checks": "all true",
        "both_versions_both_routes_candidates": EXPECTED_CANDIDATES,
        "required_V2_input_V2": "MATCH", "required_V2_input_V1": "MISMATCH",
        "no_requirement_input_V2": "UNKNOWN_REQUIREMENT",
    }

    # One V1/V2 pair only. Each call uses run.main() once: file + SQLite + 7 checks.
    v1_observation = observer.observe(baseline, fixture, v1, "V1")
    v2_observation = observer.observe(baseline, fixture, required_v2_bytes, "V2")
    observations = [v1_observation, v2_observation]
    for observation in observations:
        attach_provenance(observation, args.base_source_commit,
                          transformations[observation["variant"]])

    # The third condition reuses V2; there is no third search or database.
    version_conditions = [
        {"condition": "required_V2_input_V2", "reuses_search": "V2",
         **assess_version(required_v2_bytes, required_v2_bytes, digest)},
        {"condition": "required_V2_input_V1", "reuses_search": "V1",
         **assess_version(v1, required_v2_bytes, digest)},
        {"condition": "no_requirement_input_V2", "reuses_search": "V2",
         **assess_version(required_v2_bytes, None, digest)},
    ]
    earlier = payload_without_source_refs(v1_observation)
    later = payload_without_source_refs(v2_observation)
    earlier_c1 = next(r for r in earlier["records"] if r["id"] == "C1")
    later_c1 = next(r for r in later["records"] if r["id"] == "C1")
    c1_texts = {"V1": earlier_c1["text"], "V2": later_c1["text"]}
    expected_later = json.loads(json.dumps(earlier, ensure_ascii=False))
    next(r for r in expected_later["records"] if r["id"] == "C1")["text"] = ORIGINAL_C1 + APPEND_TEXT
    checks = {
        "both_searches_and_original_expectations_pass": all(
            o["original_run_py_result"] == "PASS" and o["original_run_py_exit_code"] == 0
            and len(o["original_run_py_checks"]) == 7 and all(o["original_run_py_checks"].values())
            and o["input_counts"] == {"nodes": 6, "edges": 4}
            and o["file_candidates"] == o["sqlite_candidates"] == EXPECTED_CANDIDATES
            for o in observations),
        "each_version_full_bundle_equal_between_routes": all(
            o["complete_evidence_bundle_equal"] for o in observations),
        "returned_c1_matches_each_version": c1_texts == {"V1": ORIGINAL_C1, "V2": ORIGINAL_C1 + APPEND_TEXT},
        "returned_payload_differs_only_in_c1_text": later == expected_later,
        "three_version_verdicts_as_predicted": [v["verdict"] for v in version_conditions]
                                             == ["MATCH", "MISMATCH", "UNKNOWN_REQUIREMENT"],
    }
    require(all(path.read_bytes() == raw for path, raw in originals.items()),
            "BASE_FILES_CHANGED_DURING_COMPARISON")
    result = {
        "experiment_id": "SQLITE-CORRECTION-SNAPSHOT-VERSION-001", "synthetic": True,
        "observation": "EXPECTED_VERSION_DISTINCTION_OBSERVED" if all(checks.values()) else "UNEXPECTED_OBSERVATION",
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version.split()[0], "sqlite": sqlite3.sqlite_version,
        "platform": platform.system(), "machine": platform.machine(),
        "base_source_commit_supplied_by_caller": args.base_source_commit,
        "source_revision_policy": "Caller-verified base commit; no Git/network lookup. V2 is derived in memory, not a saved fixture or main revision.",
        "fixture_sha256": digest(v1), "runner_sha256": digest(originals[runner]),
        "observer_sha256": digest(originals[helper]), "probe_sha256": digest(script.read_bytes()),
        "required_version": {"version": "V2", "sha256": REQUIRED_V2_SHA256,
                             "byte_length": len(required_v2_bytes), "fixed_at_utc": required_fixed_at},
        "input_byte_lengths": {"V1": len(v1), "V2": len(required_v2_bytes)},
        "transformations": transformations, "prediction_before_observation": prediction,
        "checks": checks, "variants": observations, "version_conditions": version_conditions,
        "returned_c1_texts": c1_texts, "base_files_unchanged": True,
        "search_executions": {"V1": {"file": 1, "sqlite": 1}, "V2": {"file": 1, "sqlite": 1}},
        "limits": [
            "Observed distinction is not a single PASS for search correctness, version match, and current advice.",
            "Matching declared bytes/hash proves neither latest main, source authenticity, nor semantic validity.",
            "Both versions are synthetic. The appended sentence is not an actual Human statement or execution authority.",
            "Original seven checks accept both versions; the separate fixed requirement detects V1 mismatch.",
            "Metadata verdicts reuse two completed searches. No persistent index, revision history, permission, or concurrency test.",
            "No Human success appraisal, independent AI understanding, or real-life-effect measurement.",
        ],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, sqlite3.Error) as exc:
        print(json.dumps({"observation": "COMPARISON_ERROR", "error": str(exc)}, ensure_ascii=False))
        raise SystemExit(2)
