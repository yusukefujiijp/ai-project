import unittest

from ark_harness.checks import reference_checks
from ark_harness.contracts import Evidence, LineRange, ReadMark, Result
from ark_harness.review import finish, ingest, load_run, mark_read
from test_review import ReviewFixture
from test_sources import FIXTURE, snapshot, source


class CheckTests(ReviewFixture, unittest.TestCase):
    def test_unread_required_method_blocks_completion(self):
        self.populate(read=False)
        validation = finish(self.run_root, self.result())
        self.assertFalse(validation.passed)
        self.assertEqual(load_run(self.run_root).state, "active")

    def test_citation_outside_declared_reading_fails(self):
        self.populate()
        result = self.result()
        result.findings[0].evidence[0].lines = LineRange(start=2, end=4)
        self.assertFalse(finish(self.run_root, result).passed)

    def test_partial_result_can_preserve_missing_required_source(self):
        sid = ingest(self.run_root, source())
        mark_read(self.run_root, ReadMark(source_id=sid, ranges=[LineRange(start=1, end=1)],
                                        reviewer="test", note="one line available for this result"))
        validation = finish(self.run_root, self.result(outcome="partial"))
        self.assertTrue(validation.passed)
        self.assertEqual(load_run(self.run_root).state, "partial")
        self.assertTrue(any(c.code == "required-read" and c.status == "warning" for c in validation.checks))

    def test_wrong_run_identity_blocks_completion(self):
        self.populate()
        result = self.result()
        result.run_id = "some-other-run"
        self.assertFalse(finish(self.run_root, result).passed)

    def test_main_drift_is_explicit_not_silent_repin(self):
        self.populate()
        result = self.result()
        result.end_ref_commit = "b" * 40
        result.ref_change_assessment = "report remains about the starting snapshot; newer changes not reviewed"
        validation = finish(self.run_root, result)
        self.assertTrue(validation.passed)
        self.assertTrue(any(c.code == "main-drift" and c.status == "warning" for c in validation.checks))

    def test_fixed_history_not_resolved_against_main(self):
        checks = reference_checks("https://github.com/example/repository/blob/" + "a" * 40 + "/README.md",
                                  FIXTURE["commit"] + ":README.md", {FIXTURE["commit"]: snapshot()})
        self.assertEqual(checks[0].status, "not-checked")

    def test_relative_paths_fragments_and_missing_targets(self):
        snapshots = {FIXTURE["commit"]: snapshot()}
        origin = FIXTURE["commit"] + ":repository-reviews/README.md"
        checks = reference_checks("../README.md#meaning", origin, snapshots)
        self.assertEqual([c.status for c in checks], ["pass", "not-checked"])
        self.assertEqual(reference_checks("missing.md", origin, snapshots)[0].status, "fail")
        self.assertEqual(reference_checks("../../escape", origin, snapshots)[0].status, "fail")

    def test_unknown_result_fields_do_not_silently_disappear(self):
        self.populate()
        with self.assertRaises(ValueError):
            Result.from_dict(self.result().to_dict() | {"new_schema_meaning": True})


if __name__ == "__main__":
    unittest.main()
