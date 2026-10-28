"""Strict, versioned dataclass contracts. Standard library only; prose stays flexible."""

from __future__ import annotations

import json
import re
import types
from dataclasses import MISSING, asdict, dataclass, field, fields
from pathlib import PurePosixPath
from typing import Annotated, Literal, Union, get_args, get_origin, get_type_hints


@dataclass(frozen=True)
class Rule:
    pattern: str | None = None
    minimum: int | None = None
    nonblank: bool = False
    path: bool = False


def repo_path(value: str) -> str:
    if (not value or value.startswith("/") or "\\" in value
            or any(ord(c) < 32 or ord(c) == 127 for c in value)
            or any(part in ("", ".", "..") for part in value.split("/"))
            or str(PurePosixPath(value)) != value):
        raise ValueError("path must be a canonical relative POSIX path")
    return value


Sha1 = Annotated[str, Rule(pattern=r"[0-9a-f]{40}")]
Sha256 = Annotated[str, Rule(pattern=r"[0-9a-f]{64}")]
Text = Annotated[str, Rule(nonblank=True)]
Repository = Annotated[str, Rule(pattern=r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+")]
RepoPath = Annotated[str, Rule(path=True)]
Nonnegative = Annotated[int, Rule(minimum=0)]
Positive = Annotated[int, Rule(minimum=1)]


def json_loads(text: str):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    def invalid(value):
        raise ValueError(f"non-JSON number: {value}")

    return json.loads(text, object_pairs_hook=unique, parse_constant=invalid)


def _value(annotation, value):
    origin, args = get_origin(annotation), get_args(annotation)
    if origin is Annotated:
        value = _value(args[0], value)
        for rule in args[1:]:
            if rule.pattern is not None and re.fullmatch(rule.pattern, value) is None:
                raise ValueError("value does not match required pattern")
            if rule.minimum is not None and value < rule.minimum:
                raise ValueError("value is below minimum")
            if rule.nonblank and not value.strip():
                raise ValueError("value must not be blank")
            if rule.path:
                repo_path(value)
        return value
    if origin is Literal:
        if not any(type(value) is type(option) and value == option for option in args):
            raise ValueError(f"expected one of {args}")
        return value
    if origin in (types.UnionType, Union):
        for option in args:
            try:
                return _value(option, value)
            except (ValueError, TypeError):
                pass
        raise ValueError("value does not match union")
    if origin is list:
        if type(value) is not list:
            raise ValueError("expected list")
        return [_value(args[0], item) for item in value]
    if origin is dict:
        if type(value) is not dict:
            raise ValueError("expected object")
        return {_value(args[0], key): _value(args[1], item) for key, item in value.items()}
    if isinstance(annotation, type) and issubclass(annotation, Contract):
        if isinstance(value, annotation):
            return value
        return annotation.from_dict(value)
    if type(value) is not annotation:
        raise ValueError(f"expected {annotation.__name__}; coercion is disabled")
    return value


def _schema(annotation):
    origin, args = get_origin(annotation), get_args(annotation)
    if origin is Annotated:
        result = _schema(args[0])
        for rule in args[1:]:
            if rule.pattern is not None:
                result["pattern"] = "^(?:" + rule.pattern + ")$"
            if rule.minimum is not None:
                result["minimum"] = rule.minimum
            if rule.nonblank:
                result["pattern"] = r"\S"
            if rule.path:
                result["description"] = "Canonical relative POSIX path; semantic path validation also applies"
        return result
    if origin is Literal:
        return {"enum": list(args), "type": _schema(type(args[0]))["type"]}
    if origin in (types.UnionType, Union):
        return {"anyOf": [_schema(a) for a in args]}
    if origin is list:
        return {"type": "array", "items": _schema(args[0])}
    if origin is dict:
        return {"type": "object", "additionalProperties": _schema(args[1])}
    if isinstance(annotation, type) and issubclass(annotation, Contract):
        return annotation.json_schema()
    return {"type": {str: "string", int: "integer", bool: "boolean", type(None): "null"}[annotation]}


@dataclass(kw_only=True)
class Contract:
    def __post_init__(self):
        hints = get_type_hints(type(self), include_extras=True)
        for item in fields(self):
            try:
                setattr(self, item.name, _value(hints[item.name], getattr(self, item.name)))
            except (ValueError, TypeError) as exc:
                raise ValueError(f"{type(self).__name__}.{item.name}: {exc}") from exc
        self.check()

    def check(self):
        pass

    @classmethod
    def from_dict(cls, value):
        if type(value) is not dict:
            raise ValueError(f"{cls.__name__} requires an object")
        known = {f.name for f in fields(cls)}
        if set(value) - known:
            raise ValueError(f"{cls.__name__}: unknown fields: {sorted(set(value) - known)}")
        try:
            return cls(**value)
        except TypeError as exc:
            raise ValueError(f"{cls.__name__}: missing or invalid fields") from exc

    def to_dict(self):
        return asdict(self)

    @classmethod
    def json_schema(cls):
        hints = get_type_hints(cls, include_extras=True)
        return {"title": cls.__name__, "type": "object", "additionalProperties": False,
                "properties": {f.name: _schema(hints[f.name]) for f in fields(cls)},
                "required": [f.name for f in fields(cls) if f.default is MISSING and f.default_factory is MISSING],
                "$comment": "Transport shape only. Cross-field and semantic validation is owned by contracts.py and checks.py."}


@dataclass(kw_only=True)
class RequiredSource(Contract):
    path: RepoPath
    read: Literal["full", "related"] = "full"


@dataclass(kw_only=True)
class Request(Contract):
    schema_version: Literal[1]
    repository: Repository
    ref: Text = "main"
    purpose: Text
    scope: Literal["focused", "repository-wide"]
    paths: list[RepoPath] = field(default_factory=list)
    required_sources: list[RequiredSource] = field(default_factory=list)
    repository_writes: Literal[False] = False
    execute_target_code: Literal[False] = False
    output_intent: Text

    def check(self):
        if self.scope == "focused" and not self.paths:
            raise ValueError("focused review requires named paths")
        if len(set(self.paths)) != len(self.paths):
            raise ValueError("duplicate scope path")
        if len({s.path for s in self.required_sources}) != len(self.required_sources):
            raise ValueError("duplicate required source")


@dataclass(kw_only=True)
class Profile(Contract):
    schema_version: Literal[1]
    profile_id: Literal["repository-review"]
    repository: Repository
    default_ref: Text
    review_entry: RepoPath
    review_method: RepoPath
    adapter: Literal["chatgpt-work"]
    repository_writes: Literal[False]
    execute_target_code: Literal[False]


@dataclass(kw_only=True)
class TreeEntry(Contract):
    path: RepoPath
    mode: Literal["040000", "100644", "100755", "120000", "160000"]
    type: Literal["tree", "blob", "commit"]
    sha: Sha1
    size: Nonnegative | None = None

    def check(self):
        expected = "tree" if self.mode == "040000" else "commit" if self.mode == "160000" else "blob"
        if self.type != expected:
            raise ValueError("tree mode/type mismatch")


@dataclass(kw_only=True)
class Snapshot(Contract):
    schema_version: Literal[1]
    repository: Repository
    commit: Sha1
    tree_sha: Sha1
    truncated: Literal[False]
    entries: list[TreeEntry]

    def check(self):
        if len({e.path for e in self.entries}) != len(self.entries):
            raise ValueError("duplicate tree path")


@dataclass(kw_only=True)
class SourceInput(Contract):
    schema_version: Literal[1]
    repository: Repository
    commit: Sha1
    path: RepoPath
    blob_sha: Sha1
    content: str
    role: Literal["instruction", "method", "subject", "dependency", "history"]
    purpose: Text


@dataclass(kw_only=True)
class LineRange(Contract):
    start: Positive
    end: Positive

    def check(self):
        if self.end < self.start:
            raise ValueError("reversed line range")


@dataclass(kw_only=True)
class ReadMark(Contract):
    source_id: Text
    ranges: list[LineRange]
    reviewer: Text
    note: Text


@dataclass(kw_only=True)
class SourceRecord(Contract):
    source_id: Text
    repository: Repository
    commit: Sha1
    path: RepoPath
    blob_sha: Sha1
    sha256: Sha256
    byte_count: Nonnegative
    line_count: Nonnegative
    role: Literal["instruction", "method", "subject", "dependency", "history"]
    purpose: Text
    read_marks: list[ReadMark] = field(default_factory=list)


@dataclass(kw_only=True)
class SourceIndex(Contract):
    schema_version: Literal[1] = 1
    sources: list[SourceRecord] = field(default_factory=list)


@dataclass(kw_only=True)
class Evidence(Contract):
    source_id: Text
    lines: LineRange
    supports: Text


@dataclass(kw_only=True)
class Finding(Contract):
    id: Text
    statement: Text
    certainty: Literal["confirmed", "candidate", "unknown"]
    temporal: Literal["snapshot", "historical", "current-human"]
    evidence: list[Evidence] = field(default_factory=list)


@dataclass(kw_only=True)
class Output(Contract):
    path: RepoPath
    media_type: Text
    sha256: Sha256
    role: Literal["primary", "supporting"]

    def check(self):
        if not self.path.startswith("deliverables/"):
            raise ValueError("output must be under deliverables/")


@dataclass(kw_only=True)
class Result(Contract):
    schema_version: Literal[1]
    run_id: Text
    snapshot_commit: Sha1
    end_ref_commit: Sha1
    ref_change_assessment: Text
    outcome: Literal["complete", "partial"]
    summary: Text
    findings: list[Finding]
    limitations: list[Text]
    remaining: list[Text]
    outputs: list[Output]
    semantic_review: Text

    def check(self):
        if len({f.id for f in self.findings}) != len(self.findings):
            raise ValueError("duplicate finding id")
        if len({o.path for o in self.outputs}) != len(self.outputs):
            raise ValueError("duplicate output path")
        if sum(o.role == "primary" for o in self.outputs) != 1:
            raise ValueError("exactly one primary output is required")
        if self.outcome == "partial" and not self.remaining:
            raise ValueError("partial result requires resumption/remaining work")


@dataclass(kw_only=True)
class Run(Contract):
    schema_version: Literal[1] = 1
    run_id: Text
    started_at: Text
    updated_at: Text
    repository: Repository
    snapshot_commit: Sha1
    tool_commit: Sha1
    tool_code_sha256: Sha256
    environment: dict[str, str]
    state: Literal["active", "paused", "complete", "partial"] = "active"
    checkpoint_note: str = ""
    immutable_files: dict[RepoPath, Sha256]


@dataclass(kw_only=True)
class Check(Contract):
    code: Text
    status: Literal["pass", "fail", "not-checked", "warning"]
    detail: Text


@dataclass(kw_only=True)
class Validation(Contract):
    schema_version: Literal[1] = 1
    checked_at: Text
    passed: bool
    result_sha256: Sha256
    checks: list[Check]
