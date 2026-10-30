import json
import re
import tempfile
import unittest
from pathlib import Path

from ark_harness.contracts import (LineRange, ReadMark, Request, Snapshot, SourceInput,
                                   TreeEntry, json_loads, repo_path)
from ark_harness.sources import (build_source, check_mark, covers, git_blob_sha,
                                 local_path, read_coverage)

FIXTURE = json.loads((Path(__file__).parent / "fixtures/repository-review.json").read_text())
ADAPTER = Path(__file__).resolve().parents[1] / "adapters/chatgpt-work/README.md"
EXAMPLE_START = "<!-- ark-harness:request-example:start -->"
EXAMPLE_END = "<!-- ark-harness:request-example:end -->"


def published_request(text):
    """Read the public example itself, refusing ambiguous or absent boundaries."""
    if text.count(EXAMPLE_START) != 1 or text.count(EXAMPLE_END) != 1:
        raise ValueError("request example needs exactly one start/end marker")
    start = text.index(EXAMPLE_START) + len(EXAMPLE_START)
    end = text.index(EXAMPLE_END)
    if end < start:
        raise ValueError("request example markers are reversed")
    match = re.fullmatch(r"\s*\x60{3}json\n(.*?)\n\x60{3}\s*", text[start:end], re.DOTALL)
    if match is None:
        raise ValueError("request example must contain one JSON fence")
    return Request.from_dict(json_loads(match.group(1)))


def snapshot(commit=None, files=None):
    files = FIXTURE["files"] if files is None else files
    return Snapshot(schema_version=1, repository=FIXTURE["repository"],
                    commit=commit or FIXTURE["commit"], tree_sha=FIXTURE["tree_sha"], truncated=False,
                    entries=[TreeEntry(path=p, type="blob", mode="100644", sha=git_blob_sha(t.encode()),
                                       size=len(t.encode())) for p, t in files.items()])


def source(path="README.md", content=None, commit=None):
    original = FIXTURE["files"][path]
    return SourceInput(schema_version=1, repository=FIXTURE["repository"],
                       commit=commit or FIXTURE["commit"], path=path, blob_sha=git_blob_sha(original.encode()),
                       content=original if content is None else content, role="subject", purpose="synthetic test")


class SourceTests(unittest.TestCase):
    def test_published_request_example_matches_parser_and_detects_h1(self):
        text = ADAPTER.read_text(encoding="utf-8")
        request = published_request(text)
        self.assertFalse(request.repository_writes)
        self.assertFalse(request.execute_target_code)
        self.assertEqual(request.ref, "main")
        for path in ("harness", "repository-reviews"):
            with self.subTest(path=path):
                legacy = text.replace(f'"{path}"', f'"{path}/"', 1)
                self.assertNotEqual(legacy, text)
                with self.assertRaisesRegex(ValueError, "Request.paths"):
                    published_request(legacy)

    def test_published_request_example_rejects_missing_or_ambiguous_markers(self):
        text = ADAPTER.read_text(encoding="utf-8")
        reversed_markers = (text.replace(EXAMPLE_START, "MARKER_SWAP", 1)
                           .replace(EXAMPLE_END, EXAMPLE_START, 1)
                           .replace("MARKER_SWAP", EXAMPLE_END, 1))
        for malformed in (text.replace(EXAMPLE_START, "", 1), text.replace(EXAMPLE_END, "", 1),
                          text + EXAMPLE_START, text + EXAMPLE_END, reversed_markers):
            with self.subTest(markers=malformed.count(EXAMPLE_START)), self.assertRaises(ValueError):
                published_request(malformed)

    def test_exact_bytes_and_reading_are_separate(self):
        record, data = build_source(snapshot(), source())
        self.assertEqual(data, FIXTURE["files"]["README.md"].encode())
        self.assertEqual(read_coverage(record), "not-declared")
        mark = ReadMark(source_id=record.source_id, ranges=[LineRange(start=1, end=1), LineRange(start=3, end=3)],
                        reviewer="test", note="middle not read")
        check_mark(record, mark)
        record.read_marks.append(mark)
        self.assertEqual(read_coverage(record), "partial-declared")
        self.assertFalse(covers(record, LineRange(start=1, end=3)))
        record.read_marks.append(ReadMark(source_id=record.source_id, ranges=[LineRange(start=2, end=2)],
                                           reviewer="test", note="remaining line"))
        self.assertEqual(read_coverage(record), "full-declared")

    def test_eof_does_not_hide_missing_middle(self):
        with self.assertRaisesRegex(ValueError, "blob mismatch"):
            build_source(snapshot(), source(content="First line\nEOF\n"))

    def test_ref_mix_rejected(self):
        with self.assertRaisesRegex(ValueError, "commit"):
            build_source(snapshot(), source(commit="3" * 40))

    def test_utf8_and_crlf_are_exact(self):
        body = "原本\r\n二行目\r\n"
        snap = snapshot(files={"日本語.md": body})
        incoming = SourceInput(schema_version=1, repository=FIXTURE["repository"], commit=FIXTURE["commit"],
            path="日本語.md", blob_sha=git_blob_sha(body.encode()), content=body, role="subject", purpose="encoding test")
        record, data = build_source(snap, incoming)
        self.assertEqual(data, body.encode())
        self.assertEqual(record.line_count, 2)
        incoming.content = body.replace("\r\n", "\n")
        with self.assertRaises(ValueError):
            build_source(snap, incoming)

    def test_truncated_and_duplicate_tree_rejected(self):
        data = snapshot().to_dict()
        data["truncated"] = True
        with self.assertRaises(ValueError):
            Snapshot.from_dict(data)
        data["truncated"] = False
        data["entries"].append(data["entries"][0])
        with self.assertRaises(ValueError):
            Snapshot.from_dict(data)

    def test_paths_and_symlinks(self):
        for path in ("harness", "repository-reviews"):
            self.assertEqual(repo_path(path), path)
        for path in ("../escape", "/absolute", "a/../b", "a//b", "a\\b", "a\nb", "./a",
                     "harness/", "repository-reviews/"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                repo_path(path)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "link").symlink_to(root.parent, target_is_directory=True)
            with self.assertRaises(ValueError):
                local_path(root, "link/escape")
        snap = snapshot()
        snap.entries[0].mode = "120000"
        with self.assertRaisesRegex(ValueError, "symlinks"):
            build_source(snap, source())

    def test_strict_json_types_and_unknown_versions(self):
        base = dict(schema_version=1, repository="example/repository", purpose="test", scope="focused",
                    paths=["README.md"], output_intent="report")
        for patch in ({"schema_version": True}, {"schema_version": "1"}, {"schema_version": 2},
                      {"repository_writes": 0}, {"repository_writes": True}, {"unexpected": "value"}):
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                Request.from_dict(base | patch)
        for invalid in ('{"a":1,"a":2}', '{"a":NaN}', '{"a":Infinity}'):
            with self.assertRaises(ValueError):
                json_loads(invalid)

    def test_read_range_bounds(self):
        record, _ = build_source(snapshot(), source())
        with self.assertRaises(ValueError):
            check_mark(record, ReadMark(source_id=record.source_id, ranges=[LineRange(start=1, end=4)],
                                       reviewer="test", note="invalid"))
        with self.assertRaises(ValueError):
            LineRange(start=3, end=2)

    def test_empty_blob_can_have_an_explicit_read_declaration(self):
        body = ""
        snap = snapshot(files={"empty.md": body})
        record, _ = build_source(snap, SourceInput(schema_version=1, repository=FIXTURE["repository"],
            commit=FIXTURE["commit"], path="empty.md", blob_sha=git_blob_sha(b""), content=body,
            role="subject", purpose="empty fixture"))
        mark = ReadMark(source_id=record.source_id, ranges=[], reviewer="test", note="verified empty body")
        check_mark(record, mark)
        record.read_marks.append(mark)
        self.assertEqual(read_coverage(record), "full-declared")

    def test_generated_schema_exposes_required_fields_and_version(self):
        schema = Request.json_schema()
        self.assertEqual(schema["properties"]["schema_version"], {"enum": [1], "type": "integer"})
        self.assertIn("scope", schema["required"])
        self.assertFalse(schema["additionalProperties"])
        self.assertIn("anyOf", TreeEntry.json_schema()["properties"]["size"])


if __name__ == "__main__":
    unittest.main()
