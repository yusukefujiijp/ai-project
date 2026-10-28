"""One-writer local lifecycle. Host invokes tools, interprets evidence and persists deliverables."""

from __future__ import annotations

import platform
import tomllib
import uuid
import zipfile
from pathlib import Path

from . import __version__
from .checks import validate_result
from .contracts import Profile, ReadMark, Request, Result, Run, Snapshot, SourceIndex, SourceInput, Validation
from .sources import (atomic_bytes, build_source, check_mark, json_bytes, local_path, now,
                      read_model, sha256, verify_source, write_json)


def code_digest() -> str:
    root = Path(__file__).parent
    records = {p.name: sha256(p.read_bytes()) for p in sorted(root.glob("*.py"))}
    return sha256(json_bytes(records))


def event(root: Path, kind: str, detail: str) -> None:
    # A compact operational event, never a full conversation/tool dump or reasoning transcript.
    import json
    with local_path(root, "events.jsonl").open("a", encoding="utf-8") as stream:
        stream.write(json.dumps({"at": now(), "kind": kind, "detail": detail}, ensure_ascii=False) + "\n")


def start(root: Path, profile_path: Path, request: Request, snapshot: Snapshot, tool_commit: str) -> Run:
    root = root.absolute()
    repository_root = Path(__file__).resolve().parents[3]
    if root.resolve().is_relative_to(repository_root):
        raise ValueError("run directory must be outside the harness source repository")
    profile = Profile.from_dict(tomllib.loads(profile_path.read_text(encoding="utf-8")))
    if request.repository != profile.repository or snapshot.repository != request.repository:
        raise ValueError("request/profile/snapshot repository mismatch")
    # Validate everything, including tool identity, before claiming a new directory.
    payloads = {"request.json": json_bytes(request), "profile.json": json_bytes(profile), "tree.json": json_bytes(snapshot)}
    run = Run(run_id=str(uuid.uuid4()), started_at=now(), updated_at=now(),
              repository=request.repository, snapshot_commit=snapshot.commit, tool_commit=tool_commit,
              tool_code_sha256=code_digest(), environment={"python": platform.python_version(),
              "validation": "stdlib-dataclasses", "ark_harness": __version__},
              immutable_files={name: sha256(data) for name, data in payloads.items()})
    root.mkdir(parents=True, exist_ok=False)
    for name, data in payloads.items():
        atomic_bytes(local_path(root, name), data)
    write_json(root, "sources.json", SourceIndex())
    write_json(root, "run.json", run)
    (root / "deliverables").mkdir()
    event(root, "start", f"{request.repository}@{snapshot.commit}")
    return run


def load_run(root: Path) -> Run:
    run = read_model(root, "run.json", Run)
    if code_digest() != run.tool_code_sha256:
        raise ValueError("harness code differs from this run; use its recorded version")
    for path, expected in run.immutable_files.items():
        if sha256(local_path(root, path).read_bytes()) != expected:
            raise ValueError(f"immutable run file changed: {path}")
    return run


def snapshots(root: Path, run: Run) -> dict[str, Snapshot]:
    result = {}
    for path in run.immutable_files:
        if path == "tree.json" or path.startswith("trees/"):
            snap = read_model(root, path, Snapshot)
            if snap.repository != run.repository:
                raise ValueError("snapshot repository mismatch")
            result[snap.commit] = snap
    if run.snapshot_commit not in result:
        raise ValueError("primary snapshot is missing")
    return result


def verified_sources(root: Path, run: Run) -> SourceIndex:
    sources = read_model(root, "sources.json", SourceIndex)
    if len({s.source_id for s in sources.sources}) != len(sources.sources):
        raise ValueError("duplicate source identity")
    trees = snapshots(root, run)
    for source in sources.sources:
        if source.commit not in trees:
            raise ValueError("source snapshot is not registered")
        verify_source(root, trees[source.commit], source)
    return sources


def active(root: Path) -> Run:
    run = load_run(root)
    if run.state != "active":
        raise ValueError(f"run is {run.state}; mutation requires an active run")
    return run


def add_tree(root: Path, snapshot: Snapshot) -> None:
    run = active(root)
    if snapshot.repository != run.repository:
        raise ValueError("historical snapshot repository mismatch")
    existing = snapshots(root, run).get(snapshot.commit)
    if existing:
        if existing != snapshot:
            raise ValueError("same commit has conflicting snapshot data")
        return
    path = f"trees/{snapshot.commit}.json"
    write_json(root, path, snapshot)
    run.immutable_files[path] = sha256(json_bytes(snapshot))
    run.updated_at = now()
    write_json(root, "run.json", run)
    event(root, "add-tree", snapshot.commit)


def ingest(root: Path, incoming: SourceInput) -> str:
    run = active(root)
    trees = snapshots(root, run)
    if incoming.commit not in trees:
        raise ValueError("register this commit's complete tree before ingesting sources")
    record, data = build_source(trees[incoming.commit], incoming)
    sources = verified_sources(root, run)
    previous = next((s for s in sources.sources if s.source_id == record.source_id), None)
    if previous:
        if previous.sha256 != record.sha256:
            raise ValueError("conflicting source content")
        return previous.source_id
    atomic_bytes(local_path(root, f"objects/{record.blob_sha}"), data)
    sources.sources.append(record)
    write_json(root, "sources.json", sources)
    event(root, "ingest", record.source_id)
    return record.source_id


def mark_read(root: Path, mark: ReadMark) -> None:
    run = active(root)
    sources = verified_sources(root, run)
    record = next((s for s in sources.sources if s.source_id == mark.source_id), None)
    if record is None:
        raise ValueError("cannot declare reading of an unverified source")
    check_mark(record, mark)
    record.read_marks.append(mark)
    write_json(root, "sources.json", sources)
    event(root, "read-declared", mark.source_id)


def pause(root: Path, reason: str) -> None:
    if not reason.strip():
        raise ValueError("pause reason is required")
    run = active(root)
    verified_sources(root, run)
    run.state, run.checkpoint_note, run.updated_at = "paused", reason, now()
    write_json(root, "run.json", run)
    event(root, "pause", reason)


def resume(root: Path, authority: str) -> None:
    if not authority.strip():
        raise ValueError("host must state the currently valid resumption authority")
    run = load_run(root)
    if run.state != "paused":
        raise ValueError("only a paused run can resume")
    verified_sources(root, run)
    run.state, run.checkpoint_note, run.updated_at = "active", authority, now()
    write_json(root, "run.json", run)
    event(root, "resume", authority)


def finish(root: Path, result: Result) -> Validation:
    run = active(root)
    sources = verified_sources(root, run)
    request = read_model(root, "request.json", Request)
    profile = read_model(root, "profile.json", Profile)
    validation = validate_result(root, request, profile, run, sources, result)
    write_json(root, "result.json", result)
    write_json(root, "validation.json", validation)
    if validation.passed:
        run.state, run.updated_at = result.outcome, now()
        write_json(root, "run.json", run)
    event(root, "finish" if validation.passed else "validation-failed", result.summary)
    return validation


def bundle(root: Path, destination: Path) -> dict:
    run = load_run(root)
    if run.state not in ("complete", "partial"):
        raise ValueError("only a validated complete/partial review can be bundled")
    sources = verified_sources(root, run)
    result = read_model(root, "result.json", Result)
    if result.outcome != run.state:
        raise ValueError("run state differs from the validated outcome")
    prior = read_model(root, "validation.json", Validation)
    fresh = validate_result(root, read_model(root, "request.json", Request),
                            read_model(root, "profile.json", Profile), run, sources, result)
    if not prior.passed or not fresh.passed or prior.result_sha256 != fresh.result_sha256:
        raise ValueError("result/output changed after validation; bundle refused")
    if destination.resolve().is_relative_to(root.resolve()):
        raise ValueError("bundle destination must be outside the run directory")
    if destination.resolve().is_relative_to(Path(__file__).resolve().parents[3]):
        raise ValueError("bundle destination must be outside the harness source repository")
    destination.parent.mkdir(parents=True, exist_ok=True)
    names = sorted(set(run.immutable_files) | {"run.json", "sources.json", "result.json", "validation.json", "events.jsonl"}
                   | {o.path for o in result.outputs})
    # Object cache is deliberately excluded; originals remain referenced by commit/path/blob.
    with destination.open("xb") as stream:
        with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for name in names:
                archive.writestr(name, local_path(root, name).read_bytes())
    with zipfile.ZipFile(destination) as archive:
        if archive.testzip() is not None or sorted(archive.namelist()) != names:
            raise ValueError("bundle readback failed")
        for name in names:
            if archive.read(name) != local_path(root, name).read_bytes():
                raise ValueError(f"bundle member differs: {name}")
    return {"path": str(destination), "sha256": sha256(destination.read_bytes()),
            "members": len(names), "readback_verified": True, "durable_save": "not-performed-by-python"}
