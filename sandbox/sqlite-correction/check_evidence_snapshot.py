#!/usr/bin/env python3
"""One synthetic stale-output comparison after one V2 search per route."""

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

REQUIRED_V2_SHA256 = "47f6663c6d19512ecec057add2ecbeee91b0e3d9ad8f93f7b3f84ce4f46de909"
EXPECTED_RECORD_IDS = {"C1", "I1", "P1", "P2", "S1"}
EXPECTED_RELATION_IDS = {"E1", "E2", "E3", "E4"}
EXPECTED_CANDIDATES = [
    {"id": "P1", "depends_on_path": ["P1", "I1"]},
    {"id": "P2", "depends_on_path": ["P2", "P1", "I1"]},
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical_json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def compare_records(bundle, frozen_reference):
    # Read expected content from the pre-search V2 input, never from the output.
    reference = json.loads(frozen_reference)
    issues, checked, matched = [], 0, 0
    for group, expected_ids in (("records", EXPECTED_RECORD_IDS), ("relations", EXPECTED_RELATION_IDS)):
        ids = [row["id"] for row in bundle[group]]
        if len(ids) != len(set(ids)):
            issues.append({"group": group, "problem": "duplicate_id"})
        if set(ids) != expected_ids:
            issues.append({"group": group, "problem": "unexpected_record_set",
                           "missing": sorted(expected_ids - set(ids)),
                           "extra": sorted(set(ids) - expected_ids)})
        for row in bundle[group]:
            checked += 1
            identifier = row["id"]
            expected = reference.get(identifier)
            # source_ref is derived metadata and is evaluated separately.
            actual = {key: value for key, value in row.items() if key != "source_ref"}
            if expected is None:
                issues.append({"id": identifier, "problem": "unknown_source_record"})
            elif actual == expected:
                matched += 1
            else:
                fields = sorted(key for key in set(actual) | set(expected)
                                if key not in actual or key not in expected or actual[key] != expected[key])
                issues.append({"id": identifier, "problem": "record_content_mismatch", "fields": fields,
                               "expected_values": {key: expected.get(key) for key in fields},
                               "actual_values": {key: actual.get(key) for key in fields}})
    return {"matches_reference_records": not issues, "checked": checked,
            "matched": matched, "issues": issues,
            "comparison_scope": "Raw fields of the 5 expected nodes and 4 edges, by ID; source_ref checked separately"}


def source_metadata(bundle):
    return {row["id"]: row["source_ref"] for row in bundle["records"] + bundle["relations"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-source-commit", help="Caller-verified commit for fixture and the three existing Python files")
    args = parser.parse_args()
    if args.base_source_commit:
        require(re.fullmatch(r"[0-9a-f]{40}", args.base_source_commit), "FULL_COMMIT_REQUIRED")
    script = Path(__file__).resolve()
    names = ("fixture.jsonl", "run.py", "check_relation_swap.py", "check_snapshot_version.py")
    paths = {name: script.with_name(name) for name in names}
    originals = {name: path.read_bytes() for name, path in paths.items()}
    spec = importlib.util.spec_from_file_location("evidence_snapshot_tools", paths["check_snapshot_version.py"])
    snapshot = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(snapshot)
    observer = snapshot.load_module(paths["check_relation_swap.py"], "evidence_observer")
    baseline = snapshot.load_module(paths["run.py"], "evidence_baseline")
    digest = observer.digest
    v1 = originals["fixture.jsonl"]
    require(digest(v1) == snapshot.V1_SHA256, "BASE_FIXTURE_CHANGED")
    require(snapshot.REQUIRED_V2_SHA256 == REQUIRED_V2_SHA256, "REQUIRED_VERSION_CONTRACT_CHANGED")
    required_v2_bytes, input_transformation = snapshot.derive_v2(v1)
    require(digest(required_v2_bytes) == REQUIRED_V2_SHA256, "FIXED_V2_HASH_MISMATCH")
    # Freeze the independent source records and required input BEFORE querying.
    frozen_reference = canonical_json({row["id"]: row for row in
        (json.loads(line) for line in required_v2_bytes.decode("utf-8").split("\n") if line)})
    reference = json.loads(frozen_reference)
    old_c1 = next(json.loads(line)["text"] for line in v1.decode("utf-8").split("\n")
                  if line and json.loads(line)["id"] == "C1")
    required_c1 = reference["C1"]["text"]
    require(required_c1 == old_c1 + snapshot.APPEND_TEXT, "C1_VERSION_DELTA_CHANGED")
    fixed_at = datetime.now(timezone.utc).isoformat()
    prediction = {
        "one_V2_search_per_route": "both routes match; original seven checks all true",
        "both_outputs_input_version": "MATCH",
        "both_outputs_candidates": EXPECTED_CANDIDATES,
        "both_outputs_source_metadata": "identical, declares V2",
        "normal_reference_match": True, "stale_reference_match": False,
        "stale_mismatch_fields": [{"id": "C1", "fields": ["text"]}],
    }

    observation = observer.observe(baseline, paths["fixture.jsonl"], required_v2_bytes, "V2")
    require(observation["original_run_py_result"] == "PASS"
            and observation["original_run_py_exit_code"] == 0
            and len(observation["original_run_py_checks"]) == 7
            and all(observation["original_run_py_checks"].values())
            and observation["file_candidates"] == observation["sqlite_candidates"] == EXPECTED_CANDIDATES,
            "NORMAL_V2_RETRIEVAL_NOT_CONFIRMED; no output mutation performed")
    snapshot.attach_provenance(observation, args.base_source_commit, input_transformation)
    normal = observation["evidence_bundle"]
    normal_frozen = canonical_json(normal)
    normal_check = compare_records(normal, frozen_reference)
    require(normal_check["matches_reference_records"], "NORMAL_OUTPUT_ALREADY_DIFFERS_FROM_SOURCE")

    # Simulate a post-query packaging/cache error in ONE common output copy.
    # No SQL result, input byte sequence, database, or saved file is rewritten.
    stale = json.loads(normal_frozen)
    matches = [row for row in stale["records"] if row["id"] == "C1"]
    require(len(matches) == 1 and matches[0]["text"] == required_c1, "OUTPUT_C1_CHANGED")
    matches[0]["text"] = old_c1
    changes = [(a["id"], key) for a, b in zip(normal["records"], stale["records"])
               for key in set(a) | set(b) if a.get(key) != b.get(key)]
    require(changes == [("C1", "text")]
            and len(normal["records"]) == len(stale["records"])
            and {key: value for key, value in normal.items() if key != "records"}
                == {key: value for key, value in stale.items() if key != "records"},
            "ONLY_OUTPUT_C1_TEXT_MAY_CHANGE")
    stale_check = compare_records(stale, frozen_reference)
    version_check = snapshot.assess_version(required_v2_bytes, required_v2_bytes, digest)
    normal_metadata = source_metadata(normal)
    variants = []
    for name, bundle, record_check in (("normal_V2_output", normal, normal_check),
                                       ("output_C1_text_reverted_to_V1", stale, stale_check)):
        metadata = source_metadata(bundle)
        variants.append({
            "variant": name, "input_sha256": digest(required_v2_bytes),
            "input_version_check": version_check,
            "candidates_and_paths_preserved": bundle["review_candidates"] == EXPECTED_CANDIDATES,
            "source_metadata_preserved": metadata == normal_metadata,
            "source_metadata_declares_required_V2": all(
                ref["input_variant"] == "V2" and ref["input_sha256"] == REQUIRED_V2_SHA256
                for ref in metadata.values()),
            "reference_record_check": record_check,
            "bundle_sha256": digest(canonical_json(bundle).encode("utf-8")),
            "evidence_bundle": bundle,
        })
    checks = {
        "input_matches_fixed_V2": version_check["verdict"] == "MATCH",
        "candidate_paths_and_metadata_preserved": all(v["candidates_and_paths_preserved"]
            and v["source_metadata_preserved"] and v["source_metadata_declares_required_V2"] for v in variants),
        "normal_records_match_source": normal_check["matches_reference_records"]
                                       and normal_check["checked"] == normal_check["matched"] == 9,
        "stale_C1_text_mismatch_detected": not stale_check["matches_reference_records"]
            and stale_check["checked"] == 9 and stale_check["matched"] == 8
            and len(stale_check["issues"]) == 1 and stale_check["issues"][0]["id"] == "C1"
            and stale_check["issues"][0]["fields"] == ["text"],
        "normal_output_retained": canonical_json(normal) == normal_frozen,
    }
    require(all(path.read_bytes() == originals[name] for name, path in paths.items()),
            "BASE_FILES_CHANGED_DURING_COMPARISON")
    result = {
        "experiment_id": "SQLITE-CORRECTION-EVIDENCE-SNAPSHOT-001", "synthetic": True,
        "observation": "EXPECTED_EVIDENCE_MISMATCH_OBSERVED" if all(checks.values()) else "UNEXPECTED_OBSERVATION",
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version.split()[0], "sqlite": sqlite3.sqlite_version,
        "platform": platform.system(), "machine": platform.machine(),
        "base_source_commit_supplied_by_caller": args.base_source_commit,
        "source_revision_policy": "Caller-verified base commit; no Git/network lookup; new probe revision identified separately by hash",
        "base_file_sha256": {name: digest(raw) for name, raw in originals.items()},
        "probe_sha256": digest(script.read_bytes()),
        "required_input": {"version": "V2", "sha256": REQUIRED_V2_SHA256,
                           "bytes": len(required_v2_bytes), "fixed_at_utc": fixed_at},
        "input_transformation": input_transformation,
        "output_transformation": {"stage": "common output copy after successful queries",
            "record_id": "C1", "field": "text", "before": required_c1, "after": old_c1,
            "preserved": "All other fields, relations, counts, candidates, paths, and V2 source metadata"},
        "output_hash_serialization": "UTF-8 JSON, sort_keys=True, ensure_ascii=False, compact separators, no final LF",
        "prediction_before_observation": prediction,
        "original_query": {key: value for key, value in observation.items() if key != "evidence_bundle"},
        "checks": checks, "variants": variants,
        "search_executions": {"V2": {"file": 1, "sqlite": 1}, "V1": {"file": 0, "sqlite": 0}},
        "base_files_unchanged": True,
        "limits": [
            "The stale text was deliberately injected into a shared post-query copy; no SQLite defect or independent two-route failure was observed.",
            "Correct input identity and unchanged source metadata do not attest to the returned record content.",
            "Exact source-record comparison is not authenticity, semantic truth, completeness of unregistered relations, or appropriate current advice.",
            "The matcher uses the known synthetic V2 source and expected IDs; it does not discover missing context or infer Human meaning.",
            "No production output gate, live cache, independent AI, Human success appraisal, or real-life-effect measurement.",
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
