"""CLI for the host adapter. All input data is JSON/TOML; no target code is executed."""

from __future__ import annotations

import argparse
import json
import sys
from contextlib import contextmanager
from pathlib import Path

from .checks import reference_checks
from .contracts import ReadMark, Request, Result, Snapshot, SourceInput, json_loads
from .review import (active, add_tree, bundle, code_digest, event, finish, ingest, load_run,
                     mark_read, pause, resume, snapshots, start, verified_sources)
from .sources import local_path, read_coverage


def incoming(name: str, model):
    text = sys.stdin.read() if name == "-" else Path(name).read_text(encoding="utf-8")
    return model.from_dict(json_loads(text))


def emit(value):
    if hasattr(value, "to_dict"):
        value = value.to_dict()
    print(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False))


@contextmanager
def exclusive(root: Path):
    # POSIX advisory locking releases on process exit, including an interrupted command.
    try:
        import fcntl
    except ImportError as exc:
        raise ValueError("this CLI adapter requires a POSIX runtime") from exc
    with local_path(root, ".writer-lock").open("a+b") as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise ValueError("another command owns this run; use one writer per run") from exc
        try:
            yield
        finally:
            fcntl.flock(stream, fcntl.LOCK_UN)


def parser():
    cli = argparse.ArgumentParser(description=__doc__)
    sub = cli.add_subparsers(dest="command", required=True)
    init = sub.add_parser("start", help="create a new run outside the source repository")
    init.add_argument("--run", type=Path, required=True)
    init.add_argument("--profile", type=Path, required=True)
    init.add_argument("--request", required=True)
    init.add_argument("--tree", required=True)
    init.add_argument("--tool-commit", required=True)
    for name in ("ingest", "mark-read", "add-tree", "finish"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--run", type=Path, required=True)
        cmd.add_argument("--input", default="-", help="JSON filename or - for stdin")
    for name in ("status", "pause", "resume", "bundle", "show", "check-link", "note"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--run", type=Path, required=True)
        if name == "pause":
            cmd.add_argument("--reason", required=True)
        elif name == "resume":
            cmd.add_argument("--authority", required=True)
        elif name == "bundle":
            cmd.add_argument("--out", type=Path, required=True)
        elif name == "show":
            cmd.add_argument("--source-id", required=True)
            cmd.add_argument("--start", type=int, default=1)
            cmd.add_argument("--end", type=int)
        elif name == "check-link":
            cmd.add_argument("--source-id", required=True)
            cmd.add_argument("--href", required=True)
        elif name == "note":
            cmd.add_argument("--kind", choices=("fetch-failed", "scope-note", "correction", "verification-note"), required=True)
            cmd.add_argument("--detail", required=True)
    schema = sub.add_parser("schema")
    schema.add_argument("model", choices=("request", "snapshot", "source", "read", "result"))
    sub.add_parser("digest")
    return cli


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        if args.command == "schema":
            model = {"request": Request, "snapshot": Snapshot, "source": SourceInput,
                     "read": ReadMark, "result": Result}[args.model]
            emit(model.json_schema())
            return 0
        if args.command == "digest":
            emit({"tool_code_sha256": code_digest()})
            return 0
        if args.command == "start":
            emit(start(args.run, args.profile, incoming(args.request, Request),
                       incoming(args.tree, Snapshot), args.tool_commit))
            return 0
        with exclusive(args.run):
            if args.command == "ingest":
                emit({"source_id": ingest(args.run, incoming(args.input, SourceInput))})
            elif args.command == "mark-read":
                mark_read(args.run, incoming(args.input, ReadMark))
                emit({"reading": "host declaration recorded; comprehension not machine-proven"})
            elif args.command == "add-tree":
                add_tree(args.run, incoming(args.input, Snapshot))
                emit({"snapshot": "registered"})
            elif args.command == "pause":
                pause(args.run, args.reason)
                emit({"state": "paused"})
            elif args.command == "resume":
                resume(args.run, args.authority)
                emit({"state": "active"})
            elif args.command == "note":
                active(args.run)
                if not args.detail.strip():
                    raise ValueError("event detail is required")
                event(args.run, args.kind, args.detail)
                emit({"event": "recorded"})
            elif args.command == "finish":
                validation = finish(args.run, incoming(args.input, Result))
                emit(validation)
                return 0 if validation.passed else 1
            elif args.command == "bundle":
                emit(bundle(args.run, args.out))
            else:
                run = load_run(args.run)
                sources = verified_sources(args.run, run)
                if args.command == "status":
                    emit({"run": run.to_dict(), "sources": [{"source_id": s.source_id,
                          "lines": s.line_count, "reading": read_coverage(s)} for s in sources.sources]})
                elif args.command == "check-link":
                    if not any(s.source_id == args.source_id for s in sources.sources):
                        raise ValueError("origin must be a verified source")
                    checks = reference_checks(args.href, args.source_id, snapshots(args.run, run))
                    emit([c.to_dict() for c in checks])
                    return 1 if any(c.status == "fail" for c in checks) else 0
                elif args.command == "show":
                    source = next((s for s in sources.sources if s.source_id == args.source_id), None)
                    if source is None:
                        raise ValueError("unknown source")
                    if source.line_count == 0 and args.start == 1 and args.end is None:
                        print("Verified empty UTF-8 blob; no source lines.")
                        return 0
                    end = source.line_count if args.end is None else args.end
                    if args.start < 1 or end < args.start or end > source.line_count:
                        raise ValueError("invalid display range")
                    lines = local_path(args.run, f"objects/{source.blob_sha}").read_bytes().decode("utf-8").splitlines()
                    for number in range(args.start, end + 1):
                        print(f"{number}: {lines[number - 1]}")
        return 0
    except (ValueError, OSError, KeyError) as exc:
        print(json.dumps({"error": type(exc).__name__, "detail": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
