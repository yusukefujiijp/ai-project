import json
import os
import subprocess
import sys
import tempfile
import unittest
import zipfile
from unittest.mock import patch
from pathlib import Path

from ark_harness.contracts import Evidence, Finding, LineRange, Output, ReadMark, Request, Result
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
    def test_ingest_is_idempotent_preserves_read_marks(self):
        self.populate()
        ingest(self.run_root, source())
        records = verified_sources(self.run_root, load_run(self.run_root)).sources
        self.assertEqual(len(records), len(FIXTURE["files"]))
        self.assertTrue(all(read_coverage(s) == "full-declared" for s in records))

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
        env = os.environ.copy()
        env["PYTHONPATH"] = str(Path(__file__).resolve().parents[1] / "src")
        with (self.run_root / ".writer-lock").open("a+b") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            result = subprocess.run([sys.executable, "-m", "ark_harness", "note", "--run", str(self.run_root),
                "--kind", "fetch-failed", "--detail", "unavailable source"], env=env, text=True, capture_output=True)
            self.assertEqual(result.returncode, 2)
            self.assertIn("another command", result.stderr)

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
