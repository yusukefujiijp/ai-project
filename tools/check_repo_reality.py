#!/usr/bin/env python3
"""Minimal Reality Court for ai-project.

Checks only repository facts that can be read from the checked-out tree.
It does not judge Human meaning, theology, Human Seal, or canonical intent.
"""

from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

REQUIRED_FILES = (
    "README.md",
    "CURRENT_BOARD.md",
    "tools/check_repo_reality.py",
    ".github/workflows/reality-check.yml",
)

BOARD_REQUIRED_KEYS = (
    "board_version",
    "board_status",
    "repository",
    "canonical_branch",
    "reality_base_commit",
    "last_verified",
    "review_scope",
    "current_gate",
    "next_action_id",
)

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
META_RE = re.compile(r"^([A-Za-z0-9_.-]+):\s*(.*?)\s*$")


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: str
    line: int
    message: str

    def render(self) -> str:
        where = self.path if self.line <= 0 else f"{self.path}:{self.line}"
        return f"[{self.severity}] {self.code} {where} — {self.message}"


def read_utf8(path: Path) -> tuple[str | None, str | None]:
    try:
        return path.read_text(encoding="utf-8"), None
    except UnicodeDecodeError as exc:
        return None, f"not valid UTF-8: {exc}"
    except OSError as exc:
        return None, str(exc)


def front_matter(text: str) -> tuple[dict[str, str], dict[str, int]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, {}
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return {}, {}
    data: dict[str, str] = {}
    positions: dict[str, int] = {}
    for i in range(1, end):
        match = META_RE.match(lines[i])
        if not match:
            continue
        key, value = match.groups()
        data[key] = value.strip().strip('"').strip("'").strip("`")
        positions[key] = i + 1
    return data, positions


def outside_fences(text: str) -> list[tuple[int, str]]:
    visible: list[tuple[int, str]] = []
    in_fence = False
    fence = ""
    for number, line in enumerate(text.splitlines(), 1):
        match = FENCE_RE.match(line)
        if match:
            token = match.group(1)
            if not in_fence:
                in_fence, fence = True, token
            elif token == fence:
                in_fence, fence = False, ""
            continue
        if not in_fence:
            visible.append((number, line))
    return visible


def clean_target(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("<") and ">" in raw:
        return raw[1 : raw.index(">")].strip()
    if " " in raw:
        first, rest = raw.split(" ", 1)
        if rest.lstrip().startswith(('"', "'", "(")):
            raw = first
    return raw.strip()


def external_or_anchor(target: str) -> bool:
    lower = target.lower()
    return (
        not target
        or target.startswith("#")
        or lower.startswith(("http://", "https://", "mailto:", "tel:", "data:"))
    )


def resolved_target(root: Path, source: Path, target: str) -> Path | None:
    target = unquote(target).split("#", 1)[0].split("?", 1)[0]
    if not target:
        return None
    candidate = root / target.lstrip("/") if target.startswith("/") else source.parent / target
    return candidate.resolve()


def within(root: Path, path: Path) -> bool:
    try:
        path.relative_to(root.resolve())
        return True
    except ValueError:
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Check minimal ai-project repository reality.")
    parser.add_argument("--strict", action="store_true", help="Promote warnings to errors.")
    args = parser.parse_args()

    root = Path.cwd().resolve()
    findings: list[Finding] = []

    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            findings.append(Finding("ERROR", "REQUIRED_FILE_MISSING", rel, 0, "required Court surface is missing"))

    markdown_files = sorted(path for path in root.rglob("*.md") if ".git" not in path.parts)
    texts: dict[Path, str] = {}

    for path in markdown_files:
        rel = path.relative_to(root).as_posix()
        text, error = read_utf8(path)
        if error:
            findings.append(Finding("ERROR", "UTF8_FAILURE", rel, 0, error))
            continue
        assert text is not None
        texts[path] = text

        if path.name.lower() == "readme.md" and not text.strip():
            findings.append(Finding("ERROR", "EMPTY_README", rel, 0, "README is empty or whitespace-only"))

        meta, positions = front_matter(text)
        canonical_path = meta.get("canonical_path")
        if canonical_path and not any(ch in canonical_path for ch in "{}<>"):
            if not (root / canonical_path.lstrip("/")).exists():
                findings.append(Finding("WARN", "CANONICAL_PATH_MISSING", rel, positions.get("canonical_path", 0), canonical_path))

    board_path = root / "CURRENT_BOARD.md"
    board_text = texts.get(board_path)
    if board_text is not None:
        board, positions = front_matter(board_text)
        for key in BOARD_REQUIRED_KEYS:
            if not board.get(key):
                findings.append(Finding("ERROR", "BOARD_METADATA_MISSING", "CURRENT_BOARD.md", positions.get(key, 0), key))

    root_text = texts.get(root / "README.md")
    if root_text is not None and "CURRENT_BOARD.md" not in root_text:
        findings.append(Finding("WARN", "ROOT_BOARD_ROUTE_MISSING", "README.md", 0, "Root README does not yet route to CURRENT_BOARD.md"))

    for source, text in texts.items():
        rel = source.relative_to(root).as_posix()
        for line_no, line in outside_fences(text):
            for match in LINK_RE.finditer(line):
                target = clean_target(match.group(1))
                if external_or_anchor(target):
                    continue
                resolved = resolved_target(root, source, target)
                if resolved is None:
                    continue
                if not within(root, resolved):
                    findings.append(Finding("WARN", "LINK_ESCAPES_REPO", rel, line_no, target))
                elif not resolved.exists():
                    findings.append(Finding("WARN", "INTERNAL_LINK_MISSING", rel, line_no, target))

    if args.strict:
        findings = [Finding("ERROR" if item.severity == "WARN" else item.severity, item.code, item.path, item.line, item.message) for item in findings]

    findings.sort(key=lambda item: (item.severity != "ERROR", item.path, item.line, item.code))
    errors = [item for item in findings if item.severity == "ERROR"]
    warnings = [item for item in findings if item.severity == "WARN"]

    for item in findings:
        print(item.render())

    print()
    print(f"REALITY_COURT_STATUS: {'PASS' if not errors else 'FAIL'}")
    print(f"head_commit: {os.environ.get('GITHUB_SHA', 'LOCAL_OR_UNKNOWN')}")
    print(f"markdown_files: {len(markdown_files)}")
    print(f"errors: {len(errors)}")
    print(f"warnings: {len(warnings)}")
    print(f"strict_mode: {args.strict}")

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
