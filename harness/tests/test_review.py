import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
import zipfile
from unittest.mock import patch
from pathlib import Path

from ark_harness.__main__ import main as cli_main
from ark_harness.contracts import Evidence, Finding, LineRange, Output, ReadMark, Request, Result, SourceInput
from ark_harness.review import add_tree, bundle, finish, ingest, load_run, mark_read, pause, resume, start, verified_sources
from ark_harness.sources import json_bytes, read_coverage, sha256
from test_sources import FIXTURE, snapshot, source


class ReviewFixture:
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.run_root = self.root / "run"
        self.profile = self.root / "profile.toml"
        self.profile.write_text('''schema_version = 1
profile_id = "repository-review"
repository = "example/repository"
default_ref = "main"
review_entry = "repository-reviews/README.md"
review_method = "repository-reviews/review-prompt.md"
adapter = "chatgpt-work"
repository_writes = false
execute_target_code = false
''')
        self.request = Request(schema_version=1, repository=FIXTURE["repository"], purpose="synthetic lifecycle",
                               scope="focused", paths=["README.md"], output_intent="HTML and minimal evidence")
        self.run = start(self.run_root, self.profile, self.request, snapshot(), "f" * 40)

    def cli(self, *args, input_bytes=None):
        env = os.environ.copy()
        env["PYTHONPATH"] = str(Path(__file__).resolve().parents[1] / "src")
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        return subprocess.run([sys.executable, "-B", "-m", "ark_harness", *args],
                              input=input_bytes, env=env, capture_output=True, timeout=15)

    def business_files(self):
        # Lock acquisition can create .writer-lock; it is not a source or lifecycle record.
        return {str(p.relative_to(self.run_root)): p.read_bytes()
                for p in self.run_root.rglob("*") if p.is_file() and p.name != ".writer-lock"}

    def populate(self, read=True):
        for path in FIXTURE["files"]:
            sid = ingest(self.run_root, source(path))
            if read:
                mark_read(self.run_root, ReadMark(source_id=sid,
                    ranges=[LineRange(start=1, end=len(FIXTURE["files"][path].splitlines()))],
                    reviewer="unit-test actor", note="synthetic fixture reading declaration"))

    def result(self, outcome="complete"):
        path = self.run_root / "deliverables/review.html"
        path.write_text("<!doctype html><html lang='ja'><title>Fixture</title><p>架空の検査結果</p></html>")
        return Result(schema_version=1, run_id=self.run.run_id, snapshot_commit=self.run.snapshot_commit,
            end_ref_commit=self.run.snapshot_commit, ref_change_assessment="synthetic ref unchanged",
            outcome=outcome, summary="fixture result; not an actual review", findings=[Finding(id="F1",
            statement="fixture first line", certainty="confirmed", temporal="snapshot",
            evidence=[Evidence(source_id=f"{self.run.snapshot_commit}:README.md", lines=LineRange(start=1,end=1), supports="fixture")])],
            limitations=["no real AI semantic evaluation"], remaining=[] if outcome == "complete" else ["read remaining required sources"],
            outputs=[Output(path="deliverables/review.html", media_type="text/html", sha256=sha256(path.read_bytes()), role="primary")],
            semantic_review="synthetic fixture only")


class ReviewTests(ReviewFixture, unittest.TestCase):
    def test_cli_large_source_file_and_stdin_preserve_exact_bytes(self):
        line = '日本語 "quote" \\backslash $(literal-only) \x60literal-only\x60\r\n'
        body = line * (1024 * 1024 // len(line.encode("utf-8")) + 1) + "末尾改行なし"
        snap = snapshot(files=FIXTURE["files"] | {"transport.md": body})
        entry = next(e for e in snap.entries if e.path == "transport.md")
        incoming = SourceInput(schema_version=1, repository=snap.repository, commit=snap.commit,
            path=entry.path, blob_sha=entry.sha, content=body, role="subject", purpose="synthetic transport")
        payload = json_bytes(incoming)
        self.assertGreater(len(payload), 1024 * 1024)
        input_path = self.root / "source-input.json"
        input_path.write_bytes(payload)
        for mode in ("file", "stdin"):
            with self.subTest(mode=mode):
                root = self.root / ("transport-" + mode)
                start(root, self.profile, self.request, snap, "f" * 40)
                result = self.cli("ingest", "--run", str(root), "--input",
                                  str(input_path) if mode == "file" else "-",
                                  input_bytes=payload if mode == "stdin" else None)
                self.assertEqual(result.returncode, 0, result.stderr)
                records = verified_sources(root, load_run(root)).sources
                self.assertEqual(len(records), 1)
                record = records[0]
                self.assertEqual(json.loads(result.stdout)["source_id"], record.source_id)
                self.assertEqual((root / "objects" / record.blob_sha).read_bytes(), body.encode("utf-8"))
                self.assertEqual(record.byte_count, len(body.encode("utf-8")))
                self.assertEqual(record.sha256, sha256(body.encode("utf-8")))
                self.assertEqual(read_coverage(record), "not-declared")

    def test_cli_start_uses_separate_files_and_rejects_double_stdin(self):
        request_path, tree_path = self.root / "request-input.json", self.root / "tree-input.json"
        request_path.write_bytes(json_bytes(self.request))
        tree_path.write_bytes(json_bytes(snapshot()))
        root = self.root / "cli-start"
        result = self.cli("start", "--run", str(root), "--profile", str(self.profile),
            "--request", str(request_path), "--tree", str(tree_path), "--tool-commit", "f" * 40)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(load_run(root).snapshot_commit, FIXTURE["commit"])
        invalid_root = self.root / "double-stdin"
        rejected = self.cli("start", "--run", str(invalid_root), "--profile", str(self.profile),
            "--request", "-", "--tree", "-", "--tool-commit", "f" * 40,
            input_bytes=json_bytes(self.request))
        self.assertEqual(rejected.returncode, 2, rejected.stderr)
        self.assertIn("JSONDecodeError", json.loads(rejected.stderr)["error"])
        self.assertFalse(invalid_root.exists())

    def test_cli_malformed_source_json_does_not_ingest(self):
        self.populate()
        before = self.business_files()
        result = self.cli("ingest", "--run", str(self.run_root), "--input", "-",
                          input_bytes=b'{"schema_version":')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(self.business_files(), before)

    def assert_closed_run(self, outcome):
        self.populate()
        result = self.result(outcome=outcome)
        self.assertTrue(finish(self.run_root, result).passed)
        before = self.business_files()
        commands = [
            (("resume", "--authority", "synthetic authorization"), None),
            (("pause", "--reason", "cannot pause a closed run"), None),
            (("ingest", "--input", "-"), json_bytes(source())),
            (("finish", "--input", "-"), json_bytes(result)),
        ]
        for (command, *args), payload in commands:
            with self.subTest(outcome=outcome, command=command):
                rejected = self.cli(command, "--run", str(self.run_root), *args, input_bytes=payload)
                self.assertEqual(rejected.returncode, 2, rejected.stderr)
                detail = json.loads(rejected.stderr)["detail"]
                self.assertIn("only a paused run" if command == "resume" else "mutation requires", detail)
                self.assertEqual(self.business_files(), before)
                self.assertEqual(load_run(self.run_root).state, outcome)

    def test_cli_complete_run_cannot_reopen(self):
        self.assert_closed_run("complete")

    def test_cli_partial_run_cannot_reopen_but_can_bundle(self):
        self.assert_closed_run("partial")
        destination = self.root / "partial.zip"
        result = self.cli("bundle", "--run", str(self.run_root), "--out", str(destination))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)["readback_verified"])
        with zipfile.ZipFile(destination) as archive:
            self.assertEqual(json.loads(archive.read("run.json"))["state"], "partial")
            self.assertFalse(any(name.startswith("objects/") for name in archive.namelist()))

    def test_cli_nonterminal_run_cannot_bundle_or_resume_active(self):
        self.populate()
        before = self.business_files()
        rejected = self.cli("resume", "--run", str(self.run_root), "--authority", "synthetic authorization")
        self.assertEqual(rejected.returncode, 2)
        self.assertIn("only a paused run", json.loads(rejected.stderr)["detail"])
        self.assertEqual(self.business_files(), before)
        for state in ("active", "paused"):
            with self.subTest(state=state):
                if state == "paused":
                    pause(self.run_root, "synthetic checkpoint")
                before = self.business_files()
                destination = self.root / (state + ".zip")
                rejected = self.cli("bundle", "--run", str(self.run_root), "--out", str(destination))
                self.assertEqual(rejected.returncode, 2)
                self.assertIn("complete/partial", json.loads(rejected.stderr)["detail"])
                self.assertFalse(destination.exists())
                self.assertEqual(self.business_files(), before)

    def test_cli_missing_cache_blocks_status_and_resume_without_changing_paused_state(self):
        self.populate()
        pause(self.run_root, "synthetic checkpoint")
        record = verified_sources(self.run_root, load_run(self.run_root)).sources[0]
        missing = self.run_root / "objects" / record.blob_sha
        missing.unlink()
        before = self.business_files()
        for args in (("status",), ("resume", "--authority", "synthetic authorization")):
            with self.subTest(command=args[0]):
                rejected = self.cli(args[0], "--run", str(self.run_root), *args[1:])
                self.assertEqual(rejected.returncode, 2)
                self.assertEqual(json.loads(rejected.stderr)["error"], "FileNotFoundError")
                self.assertEqual(self.business_files(), before)
                self.assertEqual(load_run(self.run_root).state, "paused")
                self.assertFalse(missing.exists())

    def test_cli_missing_cache_is_not_repaired_by_ingest_or_bypassed_by_partial(self):
        self.populate()
        partial = self.result(outcome="partial")
        record = verified_sources(self.run_root, load_run(self.run_root)).sources[0]
        missing = self.run_root / "objects" / record.blob_sha
        missing.unlink()
        before = self.business_files()
        commands = [
            (("status",), None),
            (("show", "--source-id", record.source_id), None),
            (("ingest", "--input", "-"), json_bytes(source(record.path))),
            (("finish", "--input", "-"), json_bytes(partial)),
        ]
        for (command, *args), payload in commands:
            with self.subTest(command=command):
                rejected = self.cli(command, "--run", str(self.run_root), *args, input_bytes=payload)
                self.assertEqual(rejected.returncode, 2)
                self.assertEqual(json.loads(rejected.stderr)["error"], "FileNotFoundError")
                self.assertEqual(self.business_files(), before)
                self.assertEqual(load_run(self.run_root).state, "active")
                self.assertFalse(missing.exists())

    def test_cli_finish_codes_and_written_results_stay_distinct(self):
        self.populate(read=False)
        proposed = self.result()
        rejected = self.cli("finish", "--run", str(self.run_root), "--input", "-",
                            input_bytes=json_bytes(proposed))
        self.assertEqual(rejected.returncode, 1, rejected.stderr)
        self.assertEqual(load_run(self.run_root).state, "active")
        self.assertEqual(json.loads((self.run_root / "result.json").read_bytes()), proposed.to_dict())
        validation = json.loads((self.run_root / "validation.json").read_bytes())
        self.assertEqual(json.loads(rejected.stdout), validation)
        self.assertTrue(any(check["status"] == "fail" for check in validation["checks"]))
        before = self.business_files()
        malformed = self.cli("finish", "--run", str(self.run_root), "--input", "-", input_bytes=b"{")
        self.assertEqual(malformed.returncode, 2)
        self.assertEqual(self.business_files(), before)
        self.populate()
        partial = self.result(outcome="partial")
        accepted = self.cli("finish", "--run", str(self.run_root), "--input", "-",
                            input_bytes=json_bytes(partial))
        self.assertEqual(accepted.returncode, 0, accepted.stderr)
        self.assertEqual(load_run(self.run_root).state, "partial")
        self.assertEqual(json.loads((self.run_root / "result.json").read_bytes()), partial.to_dict())
        self.assertEqual(json.loads(accepted.stdout), json.loads((self.run_root / "validation.json").read_bytes()))
        self.assertFalse(any(check["status"] == "fail" for check in json.loads(accepted.stdout)["checks"]))

    def test_ingest_is_idempotent_preserves_read_marks(self):
        self.populate()
        ingest(self.run_root, source())
        records = verified_sources(self.run_root, load_run(self.run_root)).sources
        self.assertEqual(len(records), len(FIXTURE["files"]))
        self.assertTrue(all(read_coverage(s) == "full-declared" for s in records))

    def test_lost_finish_response_does_not_mean_the_operation_was_undone(self):
        self.populate()
        proposed = self.result(outcome="partial")
        input_path = self.root / "result-input.json"
        input_path.write_bytes(json_bytes(proposed))
        errors = io.StringIO()
        # Inject failure at the response boundary, after the real finish has written its records.
        with patch("ark_harness.__main__.emit", side_effect=BrokenPipeError("synthetic response loss")), \
             patch("sys.stderr", errors):
            code = cli_main(["finish", "--run", str(self.run_root), "--input", str(input_path)])
        self.assertEqual(code, 2)
        self.assertEqual(json.loads(errors.getvalue())["error"], "BrokenPipeError")
        status = self.cli("status", "--run", str(self.run_root))
        self.assertEqual(status.returncode, 0, status.stderr)
        self.assertEqual(json.loads(status.stdout)["run"]["state"], "partial")
        self.assertEqual(json.loads((self.run_root / "result.json").read_bytes()), proposed.to_dict())
        validation = json.loads((self.run_root / "validation.json").read_bytes())
        self.assertFalse(any(check["status"] == "fail" for check in validation["checks"]))
        # Inspect and bundle the accepted result; do not repeat finish on a closed run.
        receipt = bundle(self.run_root, self.root / "after-response-loss.zip")
        self.assertTrue(receipt["readback_verified"])

    def test_pause_blocks_mutation_and_resume_checks_authority(self):
        self.populate()
        pause(self.run_root, "process checkpoint")
        with self.assertRaises(ValueError):
            ingest(self.run_root, source())
        with self.assertRaises(ValueError):
            resume(self.run_root, "")
        resume(self.run_root, "original request remains authorized")
        self.assertEqual(load_run(self.run_root).state, "active")

    def test_resume_detects_corrupt_object(self):
        self.populate()
        pause(self.run_root, "checkpoint")
        record = verified_sources(self.run_root, load_run(self.run_root)).sources[0]
        (self.run_root / "objects" / record.blob_sha).write_bytes(b"changed")
        with self.assertRaises(ValueError):
            resume(self.run_root, "still authorized")
        self.assertEqual(load_run(self.run_root).state, "paused")

    def test_immutable_request_detected(self):
        (self.run_root / "request.json").write_text("{}")
        with self.assertRaisesRegex(ValueError, "immutable"):
            load_run(self.run_root)

    def test_complete_html_and_readback_bundle(self):
        self.populate()
        self.assertTrue(finish(self.run_root, self.result()).passed)
        receipt = bundle(self.run_root, self.root / "review.zip")
        self.assertTrue(receipt["readback_verified"])
        with zipfile.ZipFile(receipt["path"]) as archive:
            self.assertIn("deliverables/review.html", archive.namelist())
            self.assertFalse(any(p.startswith("objects/") for p in archive.namelist()))
        with self.assertRaises(FileExistsError):
            bundle(self.run_root, self.root / "review.zip")

    def test_changed_output_refuses_archive(self):
        self.populate()
        finish(self.run_root, self.result())
        (self.run_root / "deliverables/review.html").write_text("changed after validation")
        with self.assertRaisesRegex(ValueError, "changed"):
            bundle(self.run_root, self.root / "changed.zip")

    def test_historical_snapshot_keeps_own_version(self):
        historical = "a" * 40
        add_tree(self.run_root, snapshot(commit=historical))
        sid = ingest(self.run_root, source(commit=historical))
        self.assertTrue(sid.startswith(historical))
        self.assertEqual(load_run(self.run_root).snapshot_commit, FIXTURE["commit"])

    def test_cli_resume_in_fresh_process(self):
        self.populate()
        pause(self.run_root, "process-boundary test")
        env = os.environ.copy()
        env["PYTHONPATH"] = str(Path(__file__).resolve().parents[1] / "src")
        result = subprocess.run([sys.executable, "-m", "ark_harness", "resume", "--run", str(self.run_root),
                                 "--authority", "existing test authority"], env=env, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(load_run(self.run_root).state, "active")

    def test_changed_tool_code_requires_recorded_version(self):
        with patch("ark_harness.review.code_digest", return_value="0" * 64):
            with self.assertRaisesRegex(ValueError, "code differs"):
                load_run(self.run_root)

    def test_concurrent_cli_writer_is_rejected(self):
        import fcntl
        self.populate()
        before = self.business_files()
        source_id = f"{self.run.snapshot_commit}:README.md"
        with (self.run_root / ".writer-lock").open("a+b") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            for args in (("note", "--kind", "fetch-failed", "--detail", "unavailable source"),
                         ("status",), ("show", "--source-id", source_id)):
                with self.subTest(command=args[0]):
                    result = self.cli(args[0], "--run", str(self.run_root), *args[1:])
                    self.assertEqual(result.returncode, 2)
                    self.assertIn("another command", json.loads(result.stderr)["detail"])
                    self.assertEqual(self.business_files(), before)

    def test_new_run_cannot_overwrite_existing_checkpoint(self):
        with self.assertRaises(FileExistsError):
            start(self.run_root, self.profile, self.request, snapshot(), "f" * 40)

    def test_source_repository_cannot_be_run_storage(self):
        forbidden = Path(__file__).resolve().parents[2] / "harness-forbidden-run"
        with self.assertRaisesRegex(ValueError, "outside"):
            start(forbidden, self.profile, self.request, snapshot(), "f" * 40)
        self.assertFalse(forbidden.exists())


if __name__ == "__main__":
    unittest.main()
