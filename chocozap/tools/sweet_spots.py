#!/usr/bin/env python3
"""Read-only Sweet Spot validation and derived views. Python 3.9+, stdlib only."""
import argparse
import csv
import hashlib
import io
import json
import math
import re
import sys
import unittest
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCOPES = {"current", "historical", "unspecified"}
KINDS = {"observation", "update", "reaffirmation", "unspecified"}
CSV_FIELDS = [
    "graph_date", "date_basis", "observed_date", "reported_date", "created_at",
    "record_id", "observation_id", "machine", "label", "mode", "round",
    "condition", "kg", "report_kind", "reference_scope", "origin",
    "source_refs", "correction_refs", "previous_ref",
]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, ensure_ascii=True, sort_keys=True,
                      separators=(",", ":"), allow_nan=False)


def check_id(value, where):
    require(isinstance(value, str) and
            re.fullmatch(r"[A-Za-z0-9_-]+", value) is not None,
            where + ": expected a nonempty stable ID")


def check_date(value, where):
    if value is None:
        return
    require(isinstance(value, str), where + ": expected ISO date or null")
    try:
        require(date.fromisoformat(value).isoformat() == value,
                where + ": expected YYYY-MM-DD")
    except ValueError as exc:
        raise ValueError(where + ": invalid ISO date") from exc


def check_weight(value, where):
    require(type(value) in (int, float) and math.isfinite(value) and value >= 0,
            where + ": expected finite, nonnegative numeric kg")


def check_timestamp(value, where):
    require(isinstance(value, str), where + ": expected a timestamp with timezone")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(where + ": invalid timestamp") from exc
    require(parsed.tzinfo is not None, where + ": timezone is required")
    return parsed


def observations(record):
    return record.get("spots", []) + record.get("sequences", [])


def effective(record, observation, field):
    return observation[field] if field in observation else record.get(field)


def condition_key(item):
    return canonical([item.get("machine"), item.get("label") if not item.get("machine") else None,
                      item.get("mode"), item.get("round"), item.get("condition", {})])


def indices(data):
    records, entities = {}, {}
    for record in data["records"]:
        rid = record["id"]
        records[rid] = record
        for item in observations(record):
            entities[rid + "/" + item["id"]] = ("observation", record, item)
        for item in record.get("visits", []):
            entities[rid + "/" + item["id"]] = ("visit", record, item)
        for sid, source in record["sources"].items():
            entities[rid + "/" + sid] = ("source", record, source)
        for item in record.get("corrections", []):
            entities[rid + "/" + item["id"]] = ("correction", record, item)
    return records, entities


def validate_data(data):
    require(isinstance(data, dict) and data.get("schema_version") == 2,
            "schema_version must be 2; migrate v1 rather than treating visits as reports")
    require(isinstance(data.get("timezone"), str) and data["timezone"],
            "timezone is required")
    require(isinstance(data.get("records"), list), "records must be an array")
    record_ids = set()
    sessions, entries, snapshots = {}, {}, {}
    total = 0
    for record in data["records"]:
        require(isinstance(record, dict), "each record must be an object")
        rid = record.get("id")
        check_id(rid, "record.id")
        require(rid not in record_ids, "duplicate record ID: " + rid)
        record_ids.add(rid)
        require(isinstance(record.get("reporter"), str) and record["reporter"],
                rid + ": reporter is required")
        for field in ("observed_date", "reported_date"):
            require(field in record, rid + ": " + field + " must be explicit (null allowed)")
            check_date(record[field], rid + "/" + field)
        require(record.get("reference_scope") in SCOPES, rid + ": invalid reference_scope")
        if record.get("created_at") is not None:
            try:
                timestamp = datetime.fromisoformat(record["created_at"].replace("Z", "+00:00"))
                require(timestamp.tzinfo is not None, rid + ": created_at needs a timezone")
            except (ValueError, AttributeError) as exc:
                raise ValueError(rid + ": invalid created_at") from exc
        sources = record.get("sources")
        require(isinstance(sources, dict) and sources, rid + ": sources must be a nonempty object")
        local_ids = set()
        for sid, source in sources.items():
            check_id(sid, rid + "/source")
            require(isinstance(source, dict) and isinstance(source.get("text"), str),
                    rid + "/" + sid + ": source.text must be a string")
            if "reported_date" in source:
                check_date(source["reported_date"], rid + "/" + sid + "/reported_date")
            local_ids.add(sid)

        def source_ref(value, where):
            require(isinstance(value, str) and value in sources,
                    where + ": unresolved source " + str(value))

        if record.get("date_source") is not None:
            source_ref(record["date_source"], rid + "/date_source")
        require(isinstance(record.get("spots"), list), rid + ": spots must be an array")
        for key in ("sequences", "corrections", "feedback", "transitions", "visits"):
            require(isinstance(record.get(key, []), list), rid + ": " + key + " must be an array")
        obs_by_id = {}
        for origin in ("spots", "sequences"):
            for obs in record.get(origin, []):
                require(isinstance(obs, dict), rid + ": observation must be an object")
                oid = obs.get("id")
                check_id(oid, rid + "/observation.id")
                loc = rid + "/" + oid
                require(oid not in local_ids, loc + ": duplicate local ID")
                local_ids.add(oid)
                obs_by_id[oid] = obs
                source_ref(obs.get("source"), loc)
                require(isinstance(obs.get("machine") or obs.get("label"), str),
                        loc + ": machine or original label is required")
                for key in ("machine", "label", "mode"):
                    require(obs.get(key) is None or
                            (isinstance(obs[key], str) and bool(obs[key].strip())),
                            loc + ": invalid " + key)
                if "condition" in obs:
                    require(isinstance(obs["condition"], dict), loc + ": condition must be an object")
                require(obs.get("report_kind", "unspecified") in KINDS,
                        loc + ": invalid report_kind")
                require(effective(record, obs, "reference_scope") in SCOPES,
                        loc + ": invalid reference_scope")
                for key in ("observed_date", "reported_date"):
                    if key in obs:
                        check_date(obs[key], loc + "/" + key)
                observed = effective(record, obs, "observed_date")
                reported = effective(record, obs, "reported_date")
                require(not (observed and reported and observed > reported),
                        loc + ": observation cannot follow its report date")
                for key, value in obs.items():
                    if key.endswith("_source") and value is not None:
                        source_ref(value, loc + "/" + key)
                if origin == "spots":
                    check_weight(obs.get("kg"), loc)
                else:
                    weights = obs.get("kg_sequence")
                    require(isinstance(weights, list) and weights, loc + ": empty/invalid sequence")
                    for weight in weights:
                        check_weight(weight, loc)
                total += 1
        local_sessions = set()
        for visit in record.get("visits", []):
            require(isinstance(visit, dict), rid + ": visit must be an object")
            vid = visit.get("id")
            check_id(vid, rid + "/visit.id")
            loc = rid + "/" + vid
            require(vid not in local_ids, loc + ": duplicate local ID")
            local_ids.add(vid)
            session = visit.get("session_id")
            check_id(session, loc + "/session_id")
            require(session not in local_sessions, loc + ": repeated session within one report")
            local_sessions.add(session)
            require("visit_date" in visit and visit["visit_date"] is not None,
                    loc + ": visit_date is required")
            check_date(visit["visit_date"], loc + "/visit_date")
            require("location" in visit and (visit["location"] is None or
                    isinstance(visit["location"], str) and visit["location"].strip()),
                    loc + ": location must be a name or null")
            require("entered_at" in visit, loc + ": entered_at must be explicit (null allowed)")
            entered = (check_timestamp(visit["entered_at"], loc + "/entered_at")
                       if visit["entered_at"] is not None else None)
            as_of = check_timestamp(visit.get("as_of"), loc + "/as_of")
            require(visit["visit_date"] <= as_of.date().isoformat(), loc + ": visit follows snapshot")
            require(entered is None or entered <= as_of, loc + ": entry follows snapshot")
            require(entered is None or entered.date().isoformat() == visit["visit_date"],
                    loc + ": entry date differs from visit_date")
            require(not record["reported_date"] or as_of.date().isoformat() <= record["reported_date"],
                    loc + ": snapshot follows report date")
            require("exited_at" in visit, loc + ": exited_at must be explicit (null allowed)")
            exited = (check_timestamp(visit["exited_at"], loc + "/exited_at")
                      if visit["exited_at"] is not None else None)
            status = visit.get("status")
            require(status in {"exited", "ongoing", "exit_unknown"}, loc + ": invalid visit status")
            require(exited is None or status == "exited",
                    loc + ": status conflicts with exit timestamp")
            require(exited is None or (exited <= as_of and
                    (entered <= exited if entered else visit["visit_date"] <= exited.date().isoformat())),
                    loc + ": exit outside entry/snapshot interval")
            for key in ("source", "as_of_source"):
                source_ref(visit.get(key), loc + "/" + key)
            for key, value in visit.items():
                if key.endswith("_source"):
                    source_ref(value, loc + "/" + key)
            if status == "ongoing":
                source_ref(visit.get("status_source"), loc + "/status_source")
            identity = (visit["visit_date"], visit["location"], entered)
            prior = sessions.get(session, identity)
            require(all(a is None or b is None or a == b for a, b in zip(prior, identity)),
                    loc + ": session identity changed; reconcile the source record")
            sessions[session] = tuple(a if a is not None else b for a, b in zip(prior, identity))
            if visit["location"] is not None and entered is not None:
                entry_key = (visit["location"], entered)
                require(entry_key not in entries or entries[entry_key] == session,
                        loc + ": same arrival has multiple session IDs")
                entries[entry_key] = session
            snapshot_key = (session, as_of)
            state = (exited, status)
            require(snapshot_key not in snapshots or snapshots[snapshot_key] == state,
                    loc + ": conflicting states at the same snapshot time")
            snapshots[snapshot_key] = state
        chains = defaultdict(list)
        correction_ids = set()
        for correction in record.get("corrections", []):
            require(isinstance(correction, dict), rid + ": correction must be an object")
            cid = correction.get("id")
            check_id(cid, rid + "/correction.id")
            loc = rid + "/" + cid
            require(cid not in local_ids, loc + ": duplicate local ID")
            local_ids.add(cid)
            correction_ids.add(cid)
            require(correction.get("target") in obs_by_id, loc + ": unresolved correction target")
            require(isinstance(correction.get("field"), str) and correction["field"] != "id",
                    loc + ": invalid correction field")
            require("from" in correction and "to" in correction, loc + ": from/to required")
            for key in ("source", "previous_source"):
                source_ref(correction.get(key), loc + "/" + key)
            if "reported_date" in correction:
                check_date(correction["reported_date"], loc + "/reported_date")
            chain = chains[(correction["target"], correction["field"])]
            if chain:
                require(chain[-1]["to"] == correction["from"], loc + ": broken correction chain")
            chain.append(correction)
        for (target, field), chain in chains.items():
            require(obs_by_id[target].get(field) == chain[-1]["to"],
                    rid + "/" + target + ": current value differs from final correction")
            source_field = {"kg": "source", "kg_sequence": "source",
                            "machine": "machine_source"}.get(field)
            if source_field:
                require(obs_by_id[target].get(source_field) == chain[-1]["source"],
                        rid + "/" + target + ": corrected value needs its current source")
        for feedback in record.get("feedback", []):
            require(isinstance(feedback, dict), rid + ": feedback must be an object")
            source_ref(feedback.get("source"), rid + "/feedback")
            if feedback.get("about") is not None:
                require(feedback["about"] in set(obs_by_id) | correction_ids,
                        rid + "/feedback: unresolved about")
        seqs = {o["id"]: o for o in record.get("sequences", [])}
        transitions = set()
        for transition in record.get("transitions", []):
            require(isinstance(transition, dict), rid + ": transition must be an object")
            pair = (transition.get("from"), transition.get("to"))
            require(pair[0] in seqs and pair[1] in seqs and pair[0] != pair[1],
                    rid + ": transition must join distinct local sequences")
            require(pair not in transitions, rid + ": duplicate transition")
            transitions.add(pair)
            source_ref(transition.get("source"), rid + "/transition")
            require(transition.get("at") == "to_sweet_spot" and
                    seqs[pair[1]].get("sweet_spot_source") is not None,
                    rid + ": transition requires a confirmed target Sweet Spot")
            left, right = seqs[pair[0]].get("machine"), seqs[pair[1]].get("machine")
            require(not (left and right and left != right), rid + ": transition crosses machines")
        if record.get("start_time") is not None:
            start = record["start_time"]
            require(isinstance(start, dict) and isinstance(start.get("time"), str) and
                    re.fullmatch(r"(?:[01][0-9]|2[0-3]):[0-5][0-9]", start["time"]),
                    rid + ": invalid start_time")
            source_ref(start.get("source"), rid + "/start_time")
            require("approximate" not in start or type(start["approximate"]) is bool,
                    rid + ": approximate must be boolean")

    for session in sessions:
        states = sorted((as_of, state) for (sid, as_of), state in snapshots.items() if sid == session)
        has_exit = False
        for _, (exited, status) in states:
            require(not has_exit or status == "exited",
                    session + ": later snapshot loses known exit; reconcile the source record")
            has_exit = has_exit or status == "exited"
    _, entities = indices(data)
    links = {}
    for ref, (kind, record, obs) in entities.items():
        if kind != "observation" or not obs.get("previous_ref"):
            continue
        previous = obs["previous_ref"]
        require(previous in entities and entities[previous][0] == "observation",
                ref + ": unresolved previous_ref")
        require(previous != ref, ref + ": self-referencing previous_ref")
        _, prior_record, prior = entities[previous]
        require(condition_key(obs) == condition_key(prior), ref + ": previous_ref changes condition")
        a = effective(record, obs, "reported_date") or effective(record, obs, "observed_date")
        b = effective(prior_record, prior, "reported_date") or effective(prior_record, prior, "observed_date")
        require(not (a and b and b > a), ref + ": previous_ref points forward in reference order")
        if obs.get("report_kind") == "reaffirmation":
            def kg(item):
                return item.get("kg", item.get("kg_sequence", [None])[0])
            require(kg(obs) == kg(prior), ref + ": reaffirmation differs from previous value")
        links[ref] = previous
    for ref in links:
        seen = set()
        while ref in links:
            require(ref not in seen, ref + ": cyclic previous_ref")
            seen.add(ref)
            ref = links[ref]
    return {"records": len(data["records"]), "observations": total,
            "visits": len(sessions)}


def visit_rows(data):
    """Latest reported snapshot per session; never count report or spot IDs as visits."""
    groups = defaultdict(list)
    for record in data["records"]:
        for visit in record.get("visits", []):
            groups[visit["session_id"]].append((record, visit))
    rows = []
    for session, candidates in groups.items():
        last = max(check_timestamp(v["as_of"], "as_of") for _, v in candidates)
        current = [(r, v) for r, v in candidates if check_timestamp(v["as_of"], "as_of") == last]
        record, visit = sorted(current, key=lambda pair: (pair[0]["id"], pair[1]["id"]))[0]
        merged = dict(visit)
        for _, prior in sorted(candidates, key=lambda pair: check_timestamp(pair[1]["as_of"], "as_of"), reverse=True):
            for field in ("entered_at", "exited_at", "location"):
                if merged[field] is None and prior[field] is not None:
                    merged[field] = prior[field]
        entered = check_timestamp(merged["entered_at"], "entered_at") if merged["entered_at"] else None
        exited = check_timestamp(merged["exited_at"], "exited_at") if merged["exited_at"] else None
        refs = sorted(r["id"] + "/" + v["id"] for r, v in candidates)
        rows.append({
            "session_id": session, "visit_date": visit["visit_date"],
            "location": merged["location"], "entered_at": merged["entered_at"],
            "exited_at": merged["exited_at"], "status": visit["status"],
            "as_of": visit["as_of"],
            "duration_minutes": (exited - entered).total_seconds() / 60 if entered and exited else None,
            "evidence_refs": refs,
            "source_refs": sorted({r["id"] + "/" + value for r, v in candidates
                                   for key, value in v.items()
                                   if key == "source" or key.endswith("_source")}),
        })
    return sorted(rows, key=lambda r: (r["visit_date"], r["entered_at"] or "", r["session_id"]))


def visit_summary(data, month=None):
    rows = [r for r in visit_rows(data) if month is None or r["visit_date"].startswith(month + "-")]
    durations = [r["duration_minutes"] for r in rows if r["duration_minutes"] is not None]
    return {
        "visit_count": len(rows), "exited_count": sum(r["status"] == "exited" for r in rows),
        "timed_stay_count": len(durations),
        "ongoing_at_report_count": sum(r["status"] == "ongoing" for r in rows),
        "exit_unknown_count": sum(r["status"] == "exit_unknown" for r in rows),
        "completed_stay_minutes": sum(durations) if durations else None,
        "mean_completed_stay_minutes": sum(durations) / len(durations) if durations else None,
        "visits": rows,
        "note": "Reported visits only. Status is as of each source report; stay is not exercise time."
    }


def flatten(data, date_basis="reported"):
    field = date_basis + "_date"
    rows = []
    for record in data["records"]:
        rid = record["id"]
        for origin in ("spots", "sequences"):
            for obs in record.get(origin, []):
                if origin == "sequences" and not obs.get("sweet_spot_source"):
                    continue
                source_ids = {value for key, value in obs.items()
                              if (key == "source" or key.endswith("_source")) and value}
                corrections = [c for c in record.get("corrections", [])
                               if c["target"] == obs["id"]]
                row = {
                    "graph_date": effective(record, obs, field), "date_basis": date_basis,
                    "observed_date": effective(record, obs, "observed_date"),
                    "reported_date": effective(record, obs, "reported_date"),
                    "created_at": record.get("created_at"),
                    "record_id": rid, "observation_id": obs["id"],
                    "machine": obs.get("machine"), "label": obs.get("label"),
                    "mode": obs.get("mode"), "round": obs.get("round"),
                    "condition": obs.get("condition", {}),
                    "kg": obs["kg"] if origin == "spots" else obs["kg_sequence"][0],
                    "report_kind": obs.get("report_kind", "unspecified"),
                    "reference_scope": effective(record, obs, "reference_scope"),
                    "origin": "spot" if origin == "spots" else "confirmed_sequence_start",
                    "source_refs": [rid + "/" + sid for sid in sorted(source_ids)],
                    "correction_refs": [rid + "/" + c["id"] for c in corrections],
                    "previous_ref": obs.get("previous_ref"),
                }
                rows.append(row)
    return sorted(rows, key=lambda r: (r["graph_date"] is None, r["graph_date"] or "",
                                      r["record_id"], r["observation_id"]))


def latest(data):
    groups = defaultdict(list)
    for row in flatten(data):
        if row["reference_scope"] == "current":
            row = dict(row)
            row["reference_date"] = row["reported_date"] or row["observed_date"]
            row["reference_date_basis"] = ("reported" if row["reported_date"] else
                                           "observed" if row["observed_date"] else "unknown")
            groups[condition_key(row)].append(row)
    result = []
    for key in sorted(groups):
        rows = groups[key]
        dated = [r for r in rows if r["reference_date"]]
        undated = [r for r in rows if not r["reference_date"]]
        last = max((r["reference_date"] for r in dated), default=None)
        candidates = [r for r in dated if r["reference_date"] == last] + undated
        weights = {r["kg"] for r in candidates}
        status = ("chronology_incomplete" if undated else
                  "conflicting_same_date" if len(weights) > 1 else "resolved")
        result.append({
            "machine": rows[0]["machine"], "label": rows[0]["label"],
            "mode": rows[0]["mode"], "round": rows[0]["round"],
            "condition": rows[0]["condition"], "status": status,
            "kg": next(iter(weights)) if len(weights) == 1 and not undated else None,
            "reference_date": last, "candidates": candidates,
        })
    return result


def fingerprint(data, evidence):
    _, entities = indices(data)
    payload = []
    for ref in sorted(evidence):
        require(ref in entities, "unresolved evidence: " + str(ref))
        kind, record, item = entities[ref]
        source_ids = set()
        for obj in (item, record):
            for key, value in obj.items():
                if (key == "source" or key.endswith("_source")) and isinstance(value, str):
                    source_ids.add(value)
        corrections = []
        if kind == "observation":
            corrections = [c for c in record.get("corrections", []) if c["target"] == item["id"]]
            for correction in corrections:
                source_ids.update([correction["source"], correction["previous_source"]])
        payload.append({
            "ref": ref, "kind": kind, "value": item,
            "record_context": {key: record.get(key) for key in
                               ("observed_date", "reported_date", "date_basis", "reference_scope")},
            "sources": {sid: record["sources"][sid] for sid in sorted(source_ids)},
            "corrections": corrections,
        })
    return hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest()


def validate_analyses(data, analyses):
    require(isinstance(analyses, dict) and analyses.get("schema_version") == 1 and
            analyses.get("data_schema_version") == 2, "invalid analyses schema")
    require(isinstance(analyses.get("findings"), list), "findings must be an array")
    ids = set()
    for finding in analyses["findings"]:
        require(isinstance(finding, dict), "finding must be an object")
        fid = finding.get("id")
        check_id(fid, "finding.id")
        require(fid not in ids, "duplicate finding ID: " + fid)
        ids.add(fid)
        require(finding.get("status") in {"active", "superseded", "withdrawn"},
                fid + ": invalid status")
        require(finding.get("as_of") is not None, fid + ": as_of is required")
        check_date(finding["as_of"], fid + "/as_of")
        for field in ("kind", "claim"):
            require(isinstance(finding.get(field), str) and finding[field],
                    fid + ": " + field + " is required")
        for field in ("evidence", "reasoning", "limits", "review_when"):
            values = finding.get(field)
            require(isinstance(values, list) and values and
                    all(isinstance(v, str) and v for v in values),
                    fid + ": nonempty " + field + " array is required")
        require(len(set(finding["evidence"])) == len(finding["evidence"]),
                fid + ": duplicate evidence")
        require(isinstance(finding.get("revisions"), list) and finding["revisions"],
                fid + ": revisions are required")
        for revision in finding["revisions"]:
            require(isinstance(revision, dict) and revision.get("on") and revision.get("reason"),
                    fid + ": each revision needs on and reason")
            check_date(revision["on"], fid + "/revision")
        expected = fingerprint(data, finding["evidence"])
        actual = finding.get("evidence_fingerprint", "")
        require(isinstance(actual, str) and re.fullmatch(r"[0-9a-f]{64}", actual),
                fid + ": invalid evidence_fingerprint")
        if finding["status"] == "active":
            require(actual == expected, fid + ": evidence changed; review analysis before refreshing fingerprint")
    return {"findings": len(ids), "evidence_state": "unchanged",
            "note": "Fingerprints check cited inputs, not correctness or current applicability."}


def csv_text(rows):
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, CSV_FIELDS, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        values = {}
        for field in CSV_FIELDS:
            value = row.get(field)
            if isinstance(value, list):
                value = ";".join(value)
            elif isinstance(value, dict):
                value = json.dumps(value, ensure_ascii=False, sort_keys=True)
            if isinstance(value, str) and value.startswith(("=", "+", "-", "@", "\t", "\r")):
                value = "'" + value
            values[field] = "" if value is None else value
        writer.writerow(values)
    return out.getvalue()


def load_json(path):
    def no_duplicates(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, "duplicate JSON key: " + key)
            result[key] = value
        return result
    with Path(path).open(encoding="utf-8") as stream:
        return json.load(stream, object_pairs_hook=no_duplicates,
                         parse_constant=lambda value: (_ for _ in ()).throw(
                             ValueError("nonfinite JSON value: " + value)))


def fixture():
    return {"schema_version": 2, "timezone": "Asia/Tokyo", "records": [{
        "id": "r1", "reporter": "test", "observed_date": "2026-01-01",
        "reported_date": "2026-01-02", "reference_scope": "current",
        "created_at": "2026-01-02T00:00:00Z",
        "sources": {"s1": {"text": "synthetic test only"}},
        "spots": [{"id": "o1", "machine": "test", "mode": "両手",
                   "kg": 20, "source": "s1"}],
    }]}


class RegressionTests(unittest.TestCase):
    def visit_fixture(self):
        data = fixture()
        data["records"][0]["visits"] = [
            {"id": "v1", "session_id": "session1", "location": "test gym",
             "visit_date": "2026-01-01",
             "entered_at": "2026-01-01T18:00+09:00", "exited_at": "2026-01-01T19:10+09:00",
             "status": "exited", "as_of": "2026-01-02T08:00+09:00",
             "source": "s1", "as_of_source": "s1"},
            {"id": "v2", "session_id": "session2", "location": "test gym",
             "visit_date": "2026-01-02",
             "entered_at": "2026-01-02T07:30+09:00", "exited_at": None,
             "status": "ongoing", "as_of": "2026-01-02T08:00+09:00",
             "source": "s1", "as_of_source": "s1", "status_source": "s1"},
        ]
        return data

    def test_visits_do_not_create_weight_observations_or_complete_open_stays(self):
        data = self.visit_fixture()
        self.assertEqual(validate_data(data)["visits"], 2)
        self.assertEqual(flatten(data), flatten(fixture()))
        self.assertEqual(latest(data), latest(fixture()))
        summary = visit_summary(data)
        self.assertEqual(summary["visit_count"], 2)
        self.assertEqual(summary["completed_stay_minutes"], 70)
        self.assertEqual(summary["mean_completed_stay_minutes"], 70)
        self.assertIsNone(summary["visits"][1]["duration_minutes"])
        self.assertEqual(summary["ongoing_at_report_count"], 1)

    def test_later_screenshot_updates_session_without_counting_again(self):
        data = self.visit_fixture()
        record = json.loads(json.dumps(data["records"][0]))
        record.update(id="r2", spots=[], reported_date="2026-01-03")
        for visit in record["visits"]:
            visit["as_of"] = "2026-01-03T09:00+09:00"
        record["visits"][1].update(exited_at="2026-01-02T08:10+09:00", status="exited")
        data["records"].append(record)
        self.assertEqual(validate_data(data)["visits"], 2)
        summary = visit_summary(data)
        self.assertEqual(summary["visit_count"], 2)
        self.assertEqual(summary["completed_stay_minutes"], 110)
        self.assertEqual(summary["ongoing_at_report_count"], 0)
        self.assertEqual(len(flatten(data)), 1)

    def test_duplicate_arrivals_conflicting_snapshots_and_regression_rejected(self):
        for case in ("identity", "conflict", "regression"):
            data = self.visit_fixture()
            record = json.loads(json.dumps(data["records"][0]))
            record.update(id="r2", spots=[])
            if case == "identity":
                record["visits"][0]["session_id"] = "duplicate"
            elif case == "conflict":
                record["visits"][0]["exited_at"] = "2026-01-01T19:20+09:00"
            else:
                record["visits"][0].update(as_of="2026-01-02T09:00+09:00",
                                          exited_at=None, status="exit_unknown")
            data["records"].append(record)
            with self.assertRaises(ValueError):
                validate_data(data)

    def test_missing_exit_is_not_ongoing_without_human_source(self):
        data = self.visit_fixture()
        visit = data["records"][0]["visits"][1]
        del visit["status_source"]
        with self.assertRaises(ValueError):
            validate_data(data)
        visit["status"] = "exit_unknown"
        validate_data(data)
        self.assertEqual(visit_summary(data)["ongoing_at_report_count"], 0)
        self.assertIsNone(visit_summary(data)["visits"][1]["duration_minutes"])

    def test_short_visit_report_needs_no_clock_or_location(self):
        data = self.visit_fixture()
        visit = data["records"][0]["visits"][1]
        visit.update(entered_at=None, exited_at=None, location=None, status="exited")
        validate_data(data)
        summary = visit_summary(data)
        self.assertEqual(summary["visit_count"], 2)
        self.assertEqual(summary["exited_count"], 2)
        self.assertEqual(summary["timed_stay_count"], 1)
        self.assertIsNone(summary["visits"][1]["duration_minutes"])

    def test_invalid_visit_time_and_changed_evidence(self):
        for field, value in (("entered_at", "2026-01-01T18:00"),
                             ("exited_at", "2026-01-01T17:00+09:00"),
                             ("as_of", "2026-01-03T08:00+09:00")):
            data = self.visit_fixture()
            data["records"][0]["visits"][0][field] = value
            with self.assertRaises(ValueError):
                validate_data(data)
        data = self.visit_fixture()
        original = fingerprint(data, ["r1/v1"])
        data["records"][0]["visits"][0]["exited_at"] = "2026-01-01T19:20+09:00"
        self.assertNotEqual(fingerprint(data, ["r1/v1"]), original)

    def test_fixture(self):
        self.assertEqual(validate_data(fixture())["observations"], 1)

    def test_sequence_start_only_and_repeats_preserved(self):
        data = fixture()
        seq = {"id": "o2", "machine": "test", "mode": "片手", "source": "s1",
               "kg_sequence": [10, 10, 5], "sweet_spot_source": "s1"}
        data["records"][0]["sequences"] = [seq]
        validate_data(data)
        self.assertEqual([r["kg"] for r in flatten(data)], [20, 10])
        self.assertEqual(seq["kg_sequence"], [10, 10, 5])
        del seq["sweet_spot_source"]
        self.assertEqual(len(flatten(data)), 1)

    def test_unknown_date_not_imputed(self):
        data = fixture()
        data["records"][0]["observed_date"] = None
        self.assertIsNone(flatten(data, "observed")[0]["graph_date"])
        self.assertEqual(flatten(data, "reported")[0]["graph_date"], "2026-01-02")

    def test_explicit_observation_null_overrides_default(self):
        data = fixture()
        data["records"][0]["spots"][0]["reported_date"] = None
        self.assertIsNone(flatten(data)[0]["reported_date"])

    def test_unknown_mode_is_separate(self):
        data = fixture()
        data["records"][0]["spots"].append(
            {"id": "o2", "machine": "test", "kg": 30, "source": "s1"})
        self.assertEqual(len(latest(data)), 2)

    def test_historical_and_save_time_do_not_override_current(self):
        data = fixture()
        old = json.loads(json.dumps(data["records"][0]))
        old.update(id="r2", observed_date="2025-12-01", reported_date="2026-02-01",
                   created_at="2026-03-01T00:00:00Z", reference_scope="historical")
        old["spots"][0]["kg"] = 50
        data["records"].append(old)
        self.assertEqual(latest(data)[0]["kg"], 20)

    def test_same_date_conflict_is_not_array_order(self):
        data = fixture()
        data["records"][0]["spots"].append(
            {"id": "o2", "machine": "test", "mode": "両手", "kg": 30, "source": "s1"})
        result = latest(data)[0]
        self.assertEqual(result["status"], "conflicting_same_date")
        self.assertIsNone(result["kg"])

    def test_undated_candidate_blocks_false_latest(self):
        data = fixture()
        data["records"][0]["spots"][0].update(observed_date=None, reported_date=None)
        self.assertEqual(latest(data)[0]["status"], "chronology_incomplete")
        self.assertIsNone(latest(data)[0]["kg"])

    def test_correction_is_not_a_new_point(self):
        data = fixture()
        record = data["records"][0]
        record["sources"]["s2"] = {"text": "correction", "reported_date": "2026-02-01"}
        record["spots"][0].update(kg=25, source="s2")
        record["corrections"] = [{"id": "c1", "target": "o1", "field": "kg",
                                  "from": 20, "to": 25, "previous_source": "s1", "source": "s2"}]
        validate_data(data)
        rows = flatten(data)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["kg"], 25)
        self.assertEqual(rows[0]["reported_date"], "2026-01-02")

    def test_duplicate_id_and_dangling_source_rejected(self):
        data = fixture()
        data["records"][0]["spots"].append(dict(data["records"][0]["spots"][0]))
        with self.assertRaises(ValueError):
            validate_data(data)
        data = fixture()
        data["records"][0]["spots"][0]["source"] = "missing"
        with self.assertRaises(ValueError):
            validate_data(data)

    def test_bool_and_nonfinite_weight_rejected(self):
        for value in (True, float("nan"), float("inf"), -1):
            data = fixture()
            data["records"][0]["spots"][0]["kg"] = value
            with self.assertRaises(ValueError):
                validate_data(data)

    def test_previous_ref_must_match_condition(self):
        data = fixture()
        data["records"][0]["spots"].append(
            {"id": "o2", "machine": "test", "mode": "片手", "kg": 10,
             "source": "s1", "previous_ref": "r1/o1"})
        with self.assertRaises(ValueError):
            validate_data(data)

    def test_fingerprint_tracks_cited_inputs_not_unrelated_additions(self):
        data = fixture()
        original = fingerprint(data, ["r1/o1"])
        data["records"][0]["spots"].append(
            {"id": "o2", "machine": "other", "kg": 15, "source": "s1"})
        self.assertEqual(fingerprint(data, ["r1/o1"]), original)
        data["records"][0]["spots"][0]["kg"] = 25
        self.assertNotEqual(fingerprint(data, ["r1/o1"]), original)

    def test_reaffirmation_is_not_deduplicated(self):
        data = fixture()
        second = dict(data["records"][0]["spots"][0], id="o2",
                      report_kind="reaffirmation", previous_ref="r1/o1")
        data["records"][0]["spots"].append(second)
        validate_data(data)
        self.assertEqual(len(flatten(data)), 2)
        self.assertEqual(latest(data)[0]["kg"], 20)

    def test_save_time_never_decides_latest(self):
        data = fixture()
        second = json.loads(json.dumps(data["records"][0]))
        second.update(id="r2", observed_date="2026-01-03", reported_date="2026-01-03",
                      created_at="2026-01-03T00:00:00Z")
        second["spots"][0]["kg"] = 30
        data["records"][0]["created_at"] = "2027-01-01T00:00:00Z"
        data["records"].append(second)
        self.assertEqual(latest(data)[0]["kg"], 30)

    def test_round_and_setup_are_separate_conditions(self):
        data = fixture()
        record = data["records"][0]
        record["spots"].append(dict(record["spots"][0], id="o2", round=2))
        record["spots"].append(dict(record["spots"][0], id="o3", condition={"seat": 3}))
        validate_data(data)
        self.assertEqual(len(latest(data)), 3)

    def test_broken_correction_chain_rejected(self):
        data = fixture()
        record = data["records"][0]
        record["spots"][0]["kg"] = 30
        record["corrections"] = [
            {"id": "c1", "target": "o1", "field": "kg", "from": 10,
             "to": 20, "source": "s1", "previous_source": "s1"},
            {"id": "c2", "target": "o1", "field": "kg", "from": 25,
             "to": 30, "source": "s1", "previous_source": "s1"}]
        with self.assertRaises(ValueError):
            validate_data(data)

    def test_transition_needs_confirmed_target(self):
        data = fixture()
        record = data["records"][0]
        record["sequences"] = [
            {"id": "q1", "machine": "test", "mode": "両手",
             "kg_sequence": [20, 15], "source": "s1", "sweet_spot_source": "s1"},
            {"id": "q2", "machine": "test", "mode": "片手",
             "kg_sequence": [10, 5], "source": "s1"}]
        record["transitions"] = [{"from": "q1", "to": "q2",
                                  "at": "to_sweet_spot", "source": "s1"}]
        with self.assertRaises(ValueError):
            validate_data(data)
        record["sequences"][1]["sweet_spot_source"] = "s1"
        validate_data(data)

    def test_previous_ref_cycle_rejected(self):
        data = fixture()
        record = data["records"][0]
        record["spots"][0]["previous_ref"] = "r1/o2"
        record["spots"].append(dict(record["spots"][0], id="o2", previous_ref="r1/o1"))
        with self.assertRaises(ValueError):
            validate_data(data)

    def test_invalid_date_rejected(self):
        data = fixture()
        data["records"][0]["observed_date"] = "2026-02-30"
        with self.assertRaises(ValueError):
            validate_data(data)

    def test_analysis_detects_changed_or_missing_evidence(self):
        data = fixture()
        finding = {"id": "a1", "as_of": "2026-01-02", "status": "active",
                   "kind": "descriptive", "claim": "test", "evidence": ["r1/o1"],
                   "reasoning": ["test"], "limits": ["test"], "review_when": ["test"],
                   "revisions": [{"on": "2026-01-02", "reason": "test"}],
                   "evidence_fingerprint": fingerprint(data, ["r1/o1"])}
        analyses = {"schema_version": 1, "data_schema_version": 2, "findings": [finding]}
        validate_analyses(data, analyses)
        data["records"][0]["spots"][0]["kg"] = 25
        with self.assertRaises(ValueError):
            validate_analyses(data, analyses)
        finding["evidence"] = ["r1/missing"]
        with self.assertRaises(ValueError):
            validate_analyses(data, analyses)

    def test_csv_roundtrip_and_formula_safety(self):
        data = fixture()
        data["records"][0]["spots"][0]["machine"] = "=danger"
        row = next(csv.DictReader(io.StringIO(csv_text(flatten(data)))))
        self.assertEqual(row["machine"], "'=danger")
        self.assertEqual(float(row["kg"]), 20)
        self.assertEqual(row["observed_date"], "2026-01-01")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=ROOT / "sweet-spots.json")
    parser.add_argument("--analyses", type=Path, default=ROOT / "analyses.json")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("validate")
    commands.add_parser("latest")
    visits_parser = commands.add_parser("visits")
    visits_parser.add_argument("--month", help="YYYY-MM; filter by entry date")
    commands.add_parser("self-test")
    for name in ("history", "csv"):
        sub = commands.add_parser(name)
        sub.add_argument("--machine")
        sub.add_argument("--mode")
        sub.add_argument("--date-basis", choices=("observed", "reported"), default="reported")
        sub.add_argument("--dated-only", action="store_true")
        if name == "csv":
            sub.add_argument("--output", type=Path)
    sub = commands.add_parser("fingerprint")
    sub.add_argument("--ref", dest="refs", action="append", required=True)
    args = parser.parse_args(argv)
    if args.command == "self-test":
        result = unittest.TextTestRunner(verbosity=2).run(
            unittest.defaultTestLoader.loadTestsFromTestCase(RegressionTests))
        return 0 if result.wasSuccessful() else 1
    try:
        data = load_json(args.data)
        summary = validate_data(data)
        if args.command == "validate":
            result = {**summary, **validate_analyses(data, load_json(args.analyses)),
                      "confirmed_sweet_spot_rows": len(flatten(data))}
        elif args.command == "latest":
            result = latest(data)
        elif args.command == "visits":
            if args.month is not None:
                check_date(args.month + "-01", "month")
            result = visit_summary(data, args.month)
        elif args.command == "fingerprint":
            result = {"evidence": args.refs, "evidence_fingerprint": fingerprint(data, args.refs)}
        else:
            rows = [row for row in flatten(data, args.date_basis)
                    if (args.machine is None or row["machine"] == args.machine)
                    and (args.mode is None or row["mode"] == args.mode)
                    and (not args.dated_only or row["graph_date"] is not None)]
            if args.command == "csv":
                output = csv_text(rows)
                if args.output:
                    with args.output.open("x", encoding="utf-8", newline="") as stream:
                        stream.write(output)
                else:
                    sys.stdout.write(output)
                return 0
            result = rows
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
        return 0
    except (ValueError, OSError, TypeError, KeyError) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

