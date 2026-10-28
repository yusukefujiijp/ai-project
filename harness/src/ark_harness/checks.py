"""Bounded deterministic checks. Meaning and host authorization remain human/AI judgments."""

from __future__ import annotations

import posixpath
from pathlib import Path
from urllib.parse import unquote, urlsplit

from .contracts import Check, Profile, Request, Result, Run, Snapshot, SourceIndex, Validation
from .sources import covers, json_bytes, local_path, now, read_coverage, sha256


def reference_checks(href: str, origin_id: str, snapshots: dict[str, Snapshot]) -> list[Check]:
    """Check a supplied file reference. Fragments and external URLs are explicitly unverified."""
    commit, origin = origin_id.split(":", 1)
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc:
        parts = unquote(parsed.path).strip("/").split("/", 4)
        if parsed.scheme != "https" or parsed.netloc != "github.com" or len(parts) < 5 or parts[2] != "blob":
            return [Check(code="link", status="not-checked", detail=f"external/unsupported URL: {href}")]
        repository, commit, target = "/".join(parts[:2]), parts[3], parts[4]
        snap = snapshots.get(commit)
        if snap is None or snap.repository != repository:
            return [Check(code="link", status="not-checked", detail=f"unpinned or unavailable historical snapshot: {href}")]
    else:
        snap = snapshots.get(commit)
        target = posixpath.normpath(posixpath.join(posixpath.dirname(origin), unquote(parsed.path))) if parsed.path else origin
    if snap is None:
        return [Check(code="link", status="not-checked", detail="origin snapshot unavailable")]
    if target.startswith("/") or target == ".." or target.startswith("../") or "\\" in target:
        return [Check(code="link", status="fail", detail=f"reference escapes repository: {href}")]
    exists = any(e.path == target for e in snap.entries)
    result = [Check(code="link-path", status="pass" if exists else "fail", detail=f"{commit}:{target}")]
    if parsed.fragment:
        result.append(Check(code="link-fragment", status="not-checked", detail=f"fragment semantics not checked: {parsed.fragment}"))
    return result


def validate_result(root: Path, request: Request, profile: Profile, run: Run,
                    sources: SourceIndex, result: Result) -> Validation:
    checks: list[Check] = []

    def check(code, condition, detail, failure="fail"):
        checks.append(Check(code=code, status="pass" if condition else failure, detail=detail))

    check("identity", result.run_id == run.run_id and result.snapshot_commit == run.snapshot_commit,
          "result must name this run and its primary snapshot")
    index = {s.source_id: s for s in sources.sources}
    required = {s.path: s.read for s in request.required_sources}
    required[profile.review_entry] = "full"
    required[profile.review_method] = "full"
    for path, mode in required.items():
        source = index.get(f"{run.snapshot_commit}:{path}")
        valid = source is not None and read_coverage(source) != "not-declared"
        if mode == "full":
            valid = valid and read_coverage(source) == "full-declared"
        check("required-read", valid, f"{path}: required {mode}; declarations are not proof of comprehension",
              "warning" if result.outcome == "partial" else "fail")
    for finding in result.findings:
        check("finding-evidence", finding.certainty == "unknown" or bool(finding.evidence), finding.id)
        for evidence in finding.evidence:
            source = index.get(evidence.source_id)
            check("citation", source is not None and covers(source, evidence.lines),
                  f"{finding.id}: {evidence.source_id}: {evidence.lines.start}-{evidence.lines.end}")
    for output in result.outputs:
        try:
            actual = sha256(local_path(root, output.path).read_bytes())
            check("output", actual == output.sha256, output.path)
        except (OSError, ValueError) as exc:
            check("output", False, f"{output.path}: {exc}")
    check("remaining", result.outcome != "complete" or not result.remaining,
          "complete means the requested review scope is closed, not every unknown is resolved")
    checks.append(Check(code="main-drift", status="pass" if result.end_ref_commit == run.snapshot_commit else "warning",
                        detail=result.ref_change_assessment))
    checks.extend([
        Check(code="semantic-review", status="not-checked", detail="Host-authored assessment: " + result.semantic_review),
        Check(code="write-enforcement", status="not-checked", detail="This package has no GitHub write API; host-wide read-only capability enforcement is not established"),
        Check(code="external-links", status="not-checked", detail="No external URLs, all Markdown forms or rendered output are automatically tested"),
    ])
    return Validation(checked_at=now(), passed=not any(c.status == "fail" for c in checks),
                      result_sha256=sha256(json_bytes(result)), checks=checks)
