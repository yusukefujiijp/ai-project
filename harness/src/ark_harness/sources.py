"""Exact UTF-8 source ingestion and local evidence storage. No network calls."""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from .contracts import LineRange, ReadMark, Snapshot, SourceInput, SourceRecord, json_loads, repo_path


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def json_bytes(value) -> bytes:
    if hasattr(value, "to_dict"):
        value = type(value).from_dict(value.to_dict()).to_dict()
    return (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")


def local_path(root: Path, relative: str) -> Path:
    repo_path(relative)
    root = root.resolve()
    path = root
    for part in relative.split("/"):
        path = path / part
        if path.is_symlink():
            raise ValueError(f"symlink is not allowed in run storage: {relative}")
    if not path.resolve().is_relative_to(root):
        raise ValueError("path escapes run directory")
    return path


def atomic_bytes(path: Path, data: bytes) -> None:
    if path.is_symlink():
        raise ValueError("refusing to replace a symlink")
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".ark-write-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def write_json(root: Path, name: str, value) -> None:
    atomic_bytes(local_path(root, name), json_bytes(value))


def read_model(root: Path, name: str, model):
    return model.from_dict(json_loads(local_path(root, name).read_text(encoding="utf-8")))


def merged_ranges(ranges: list[LineRange]) -> list[tuple[int, int]]:
    merged: list[tuple[int, int]] = []
    for r in sorted(ranges, key=lambda item: (item.start, item.end)):
        if merged and r.start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], r.end))
        else:
            merged.append((r.start, r.end))
    return merged


def read_coverage(record: SourceRecord) -> str:
    if not record.read_marks:
        return "not-declared"
    ranges = merged_ranges([r for mark in record.read_marks for r in mark.ranges])
    if record.line_count == 0 or ranges == [(1, record.line_count)]:
        return "full-declared"
    return "partial-declared"


def covers(record: SourceRecord, lines: LineRange) -> bool:
    return any(start <= lines.start <= lines.end <= end for start, end in
               merged_ranges([r for mark in record.read_marks for r in mark.ranges]))


def check_mark(record: SourceRecord, mark: ReadMark) -> None:
    if mark.source_id != record.source_id:
        raise ValueError("read mark source identity mismatch")
    if record.line_count and not mark.ranges:
        raise ValueError("nonempty source needs explicit read ranges")
    if any(r.end > record.line_count for r in mark.ranges):
        raise ValueError("read range exceeds source")


def build_source(snapshot: Snapshot, incoming: SourceInput) -> tuple[SourceRecord, bytes]:
    if incoming.repository != snapshot.repository or incoming.commit != snapshot.commit:
        raise ValueError("source repository/commit differs from snapshot")
    entry = next((e for e in snapshot.entries if e.path == incoming.path), None)
    if entry is None:
        raise ValueError("source path is absent from the supplied complete snapshot")
    if entry.type != "blob" or entry.mode not in ("100644", "100755"):
        raise ValueError("only regular UTF-8 blobs are supported; symlinks/submodules are not followed")
    data = incoming.content.encode("utf-8")
    if incoming.blob_sha != entry.sha or git_blob_sha(data) != entry.sha:
        raise ValueError("Git blob mismatch: partial, normalized or different content is not a full source")
    if entry.size is not None and len(data) != entry.size:
        raise ValueError("source byte count differs from tree")
    record = SourceRecord(
        source_id=f"{incoming.commit}:{incoming.path}", repository=incoming.repository,
        commit=incoming.commit, path=incoming.path, blob_sha=incoming.blob_sha,
        sha256=sha256(data), byte_count=len(data), line_count=len(incoming.content.splitlines()),
        role=incoming.role, purpose=incoming.purpose,
    )
    return record, data


def verify_source(root: Path, snapshot: Snapshot, record: SourceRecord) -> None:
    data = local_path(root, f"objects/{record.blob_sha}").read_bytes()
    rebuilt, _ = build_source(snapshot, SourceInput(
        schema_version=1, repository=record.repository, commit=record.commit,
        path=record.path, blob_sha=record.blob_sha, content=data.decode("utf-8"),
        role=record.role, purpose=record.purpose,
    ))
    for key in ("source_id", "sha256", "byte_count", "line_count"):
        if getattr(rebuilt, key) != getattr(record, key):
            raise ValueError(f"source record mismatch: {record.path}: {key}")
    for mark in record.read_marks:
        check_mark(record, mark)
