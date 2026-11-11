#!/usr/bin/env python3
"""One synthetic quarantine/re-query/release experiment; stdout only."""

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


def require(condition, message):
    if not condition:
        raise ValueError(message)


def inspect_candidate(evidence, observation, bundle, reference, expected_metadata):
    record_check = evidence.compare_records(bundle, reference)
    metadata = evidence.source_metadata(bundle)
    nodes = {row["id"]: row for row in bundle["records"]}
    checks = {
        "input_matches_requested_V2": observation["input_sha256"] == REQUIRED_V2_SHA256,
        "query_routes_agree": observation["complete_evidence_bundle_equal"],
        "original_query_checks_pass": observation["original_run_py_exit_code"] == 0
            and len(observation["original_run_py_checks"]) == 7
            and all(observation["original_run_py_checks"].values()),
        "candidate_paths_preserved": bundle["review_candidates"] == evidence.EXPECTED_CANDIDATES,
        "records_match_fixed_V2": record_check["matches_reference_records"],
        "source_metadata_preserved": metadata == expected_metadata and all(
            ref["input_variant"] == "V2" and ref["input_sha256"] == REQUIRED_V2_SHA256
            for ref in metadata.values()),
        "correction_target_preserved": bundle["correction_id"] == "C1"
                                       and bundle["corrected_interpretation_id"] == "I1",
        "proposals_remain_unadopted": all(nodes.get(key, {}).get("status") == "proposed_not_adopted"
                                          for key in ("P1", "P2")),
    }
    return {"eligible": all(checks.values()), "checks": checks,
            "record_check": record_check,
            "reason_codes": [key for key, value in checks.items() if not value]}


def delivery(candidate, bundle):
    # This is the ONLY route into the downstream evidence slot.
    # Diagnostic mismatch text is never placed in verified_evidence.
    return {
        "state": "READY" if candidate["eligible"] else "WITHHELD",
        "verified_evidence": bundle if candidate["eligible"] else None,
        "reason_codes": candidate["reason_codes"],
        "meaning": "READY means exact synthetic source agreement, not semantic truth or action authorization.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-source-commit", help="Caller-verified commit for fixture and four existing Python files")
    args = parser.parse_args()
    if args.base_source_commit:
        require(re.fullmatch(r"[0-9a-f]{40}", args.base_source_commit), "FULL_COMMIT_REQUIRED")
    script = Path(__file__).resolve()
    names = ("fixture.jsonl", "run.py", "check_relation_swap.py", "check_snapshot_version.py",
             "check_evidence_snapshot.py")
    paths = {name: script.with_name(name) for name in names}
    originals = {name: path.read_bytes() for name, path in paths.items()}
    spec = importlib.util.spec_from_file_location("recovery_snapshot_tools", paths["check_snapshot_version.py"])
    snapshot = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(snapshot)
    evidence = snapshot.load_module(paths["check_evidence_snapshot.py"], "recovery_evidence_tools")
    observer = snapshot.load_module(paths["check_relation_swap.py"], "recovery_observer")
    baseline = snapshot.load_module(paths["run.py"], "recovery_baseline")
    digest, encode = observer.digest, evidence.canonical_json
    v1 = originals["fixture.jsonl"]
    require(digest(v1) == snapshot.V1_SHA256, "BASE_FIXTURE_CHANGED")
    require(snapshot.REQUIRED_V2_SHA256 == evidence.REQUIRED_V2_SHA256 == REQUIRED_V2_SHA256,
            "REQUIRED_VERSION_CONTRACT_CHANGED")
    required_v2_bytes, transformation = snapshot.derive_v2(v1)
    require(digest(required_v2_bytes) == REQUIRED_V2_SHA256, "FIXED_V2_HASH_MISMATCH")
    frozen_reference = encode({row["id"]: row for row in
        (json.loads(line) for line in required_v2_bytes.decode("utf-8").split("\n") if line)})
    required_c1 = json.loads(frozen_reference)["C1"]["text"]
    old_c1 = next(json.loads(line)["text"] for line in v1.decode("utf-8").split("\n")
                  if line and json.loads(line)["id"] == "C1")
    require(required_c1 == old_c1 + snapshot.APPEND_TEXT, "C1_VERSION_DELTA_CHANGED")
    fixed_at = datetime.now(timezone.utc).isoformat()
    input_version = snapshot.assess_version(required_v2_bytes, required_v2_bytes, digest)
    prediction = {
        "initial": "Both routes agree; 9 records match fixed V2",
        "injected_copy": "Only C1.text mismatches; source metadata and paths stay unchanged",
        "after_detection": "WITHHELD; verified_evidence is null",
        "recovery": "One re-query per route; 9 records match fixed V2",
        "final": "READY; full C1 correction, P1/P2 paths and unadopted status preserved",
    }
    stages = [{"stage": "input_version", "verdict": input_version["verdict"],
               "required_sha256": REQUIRED_V2_SHA256}]

    # Initial pair through unchanged run.main(): each route runs once.
    # The relation/version/evidence comparison entrypoints are not invoked.
    initial = observer.observe(baseline, paths["fixture.jsonl"], required_v2_bytes, "V2")
    snapshot.attach_provenance(initial, args.base_source_commit, transformation)
    normal = initial["evidence_bundle"]
    normal_frozen = encode(normal)
    expected_metadata = evidence.source_metadata(normal)
    initial_check = inspect_candidate(evidence, initial, normal, frozen_reference, expected_metadata)
    require(initial_check["eligible"], "INITIAL_RETRIEVAL_NOT_CONFIRMED; no mutation or recovery")
    stages.append({"stage": "initial_retrieval", "candidate_check": initial_check})

    stale = json.loads(normal_frozen)
    c1 = next(row for row in stale["records"] if row["id"] == "C1")
    require(c1["text"] == required_c1, "INITIAL_C1_CHANGED")
    c1["text"] = old_c1
    restored_copy = json.loads(encode(stale))
    next(row for row in restored_copy["records"] if row["id"] == "C1")["text"] = required_c1
    require(encode(restored_copy) == normal_frozen and old_c1 != required_c1,
            "ONLY_C1_TEXT_MAY_CHANGE")
    rejected = inspect_candidate(evidence, initial, stale, frozen_reference, expected_metadata)
    issues = rejected["record_check"]["issues"]
    require(not rejected["eligible"] and rejected["reason_codes"] == ["records_match_fixed_V2"]
            and len(issues) == 1 and issues[0]["id"] == "C1" and issues[0]["fields"] == ["text"],
            "EXPECTED_C1_MISMATCH_NOT_DETECTED; no recovery")
    before_recovery = delivery(rejected, stale)
    require(before_recovery["state"] == "WITHHELD" and before_recovery["verified_evidence"] is None,
            "UNVERIFIED_OUTPUT_REACHED_DOWNSTREAM")
    stages.append({"stage": "mismatch_detection", "candidate_check": rejected,
                   "diagnostic_only": True, "affected_record_ids": ["C1"],
                   "other_source_records_matched": 8,
                   "rejected_bundle_sha256": digest(encode(stale).encode("utf-8"))})
    stages.append({"stage": "withhold_unverified_evidence", "downstream": before_recovery})

    # Exactly one recovery attempt. There is no retry loop or alternative source.
    recovery, recovery_check, recovery_error = None, None, None
    downstream = dict(before_recovery)
    stages.append({"stage": "requery_fixed_V2", "attempt": 1, "maximum_attempts": 1,
                   "input_sha256": digest(required_v2_bytes)})
    try:
        recovery = observer.observe(baseline, paths["fixture.jsonl"], required_v2_bytes, "V2")
        snapshot.attach_provenance(recovery, args.base_source_commit, transformation)
        recovery_check = inspect_candidate(evidence, recovery, recovery["evidence_bundle"],
                                           frozen_reference, expected_metadata)
        downstream = delivery(recovery_check, recovery["evidence_bundle"])
        stages.append({"stage": "recovery_validation", "candidate_check": recovery_check})
    except Exception as exc:
        # Keep the delivery slot empty even if recovery cannot produce a report.
        recovery_error = {"type": type(exc).__name__, "message": str(exc)}
        downstream = {"state": "WITHHELD", "verified_evidence": None,
                      "reason_codes": ["recovery_error"], "error": recovery_error}
        stages.append({"stage": "recovery_validation", "error": recovery_error})
    stages.append({"stage": "return_eligibility", "state": downstream["state"],
                   "verified_evidence_present": downstream["verified_evidence"] is not None,
                   "reason_codes": downstream["reason_codes"]})
    completed = recovery is not None
    released = downstream["state"] == "READY"
    checks = {
        "input_version_matched": input_version["verdict"] == "MATCH",
        "mismatch_detected_before_recovery": rejected["reason_codes"] == ["records_match_fixed_V2"],
        "rejected_copy_withheld": before_recovery["state"] == "WITHHELD"
                                  and before_recovery["verified_evidence"] is None,
        "recovery_records_match": bool(recovery_check and recovery_check["eligible"]
            and recovery_check["record_check"]["checked"] == recovery_check["record_check"]["matched"] == 9),
        "returned_bundle_matches_normal": released and encode(downstream["verified_evidence"]) == normal_frozen,
        "normal_output_retained": encode(normal) == normal_frozen,
    }
    require(all(path.read_bytes() == originals[name] for name, path in paths.items()),
            "BASE_FILES_CHANGED_DURING_EXPERIMENT")
    result = {
        "experiment_id": "SQLITE-CORRECTION-EVIDENCE-RECOVERY-001", "synthetic": True,
        "observation": "EXPECTED_BOUNDED_RECOVERY_OBSERVED" if all(checks.values()) else "RECOVERY_NOT_CONFIRMED",
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version.split()[0], "sqlite": sqlite3.sqlite_version,
        "platform": platform.system(), "machine": platform.machine(),
        "base_source_commit_supplied_by_caller": args.base_source_commit,
        "source_revision_policy": "Caller-verified base commit; recovery is a re-query of frozen synthetic V2, not a GitHub/latest/authenticity check",
        "base_file_sha256": {name: digest(raw) for name, raw in originals.items()},
        "probe_sha256": digest(script.read_bytes()),
        "required_input": {"version": "V2", "sha256": REQUIRED_V2_SHA256,
                           "bytes": len(required_v2_bytes), "fixed_at_utc": fixed_at},
        "input_transformation": transformation,
        "output_transformation": {"stage": "shared post-query output copy", "id": "C1", "field": "text",
                                  "before": required_c1, "after": old_c1, "all_other_fields_preserved": True},
        "prediction_before_observation": prediction, "stages": stages, "checks": checks,
        "query_observations": {
            "initial": {key: value for key, value in initial.items() if key != "evidence_bundle"},
            "recovery": {key: value for key, value in recovery.items() if key != "evidence_bundle"}
                        if completed else None,
        },
        "search_execution": {
            "initial": {"pair_calls": 1, "file_completed": 1, "sqlite_completed": 1},
            "recovery": {"pair_calls": 1, "file_completed": 1 if completed else None,
                         "sqlite_completed": 1 if completed else None},
            "maximum_pair_calls": 2, "recovery_attempts": 1,
            "failure_count_policy": "null means a failed paired call did not report which route completed",
        },
        "bundle_sha256": {"normal": digest(normal_frozen.encode("utf-8")),
                          "rejected": digest(encode(stale).encode("utf-8")),
                          "returned": digest(encode(downstream["verified_evidence"]).encode("utf-8")) if released else None},
        "bundle_hash_serialization": "UTF-8 JSON, sort_keys=True, ensure_ascii=False, compact separators, no final LF",
        "downstream": downstream, "base_files_unchanged": True,
        "limits": [
            "Only the observed injected-text mismatch followed by successful bounded recovery was exercised; persistent mismatch/error branches remain untested.",
            "One shared output copy was changed after correct retrieval, not an observed SQLite/cache defect or two independent failures.",
            "The downstream slot is a local experiment contract, not an installed AI integration or an information-flow security boundary.",
            "No Human re-explanation was an input to this synthetic workflow; reduced Human burden in actual use was not measured.",
            "READY denotes agreement with the declared synthetic source, not source authenticity, semantic understanding, current intent, adoption, or action authority.",
            "No GitHub refresh, operational repair, independent AI evaluation, Human success appraisal, or real-life-effect evidence.",
        ],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, sqlite3.Error) as exc:
        print(json.dumps({"observation": "EXPERIMENT_ERROR", "state": "WITHHELD",
                          "verified_evidence": None, "error": str(exc)}, ensure_ascii=False))
        raise SystemExit(2)
