from copy import deepcopy
import unittest

from upgradepilot.case_identity import InitialCaseRecord, build_initial_case_record


class BuildInitialCaseRecordTests(unittest.TestCase):
    def test_builds_nested_record_from_real_m1_case_without_mutating_raw_input(self) -> None:
        raw_case = {
            "repository": " pydantic/pydantic ",
            "pr_number": 13432,
            "base_sha": "652A61CE4F9D7D76EAADA31535807A485ECE0E21",
            "head_sha": "AA2DC024D33F61CDEF50BF1973AB5ADF0A974F5A",
            "dependency": " soupsieve ",
            "old_version": " 2.6 ",
            "new_version": " 2.8.4 ",
            "changed_files": [" uv.lock "],
        }
        original_raw_case = deepcopy(raw_case)

        result = build_initial_case_record(raw_case)

        self.assertIsInstance(result, InitialCaseRecord)
        self.assertEqual(result.snapshot_identity.repository, "pydantic/pydantic")
        self.assertEqual(result.snapshot_identity.pr_number, 13432)
        self.assertEqual(
            result.snapshot_identity.base_sha,
            "652a61ce4f9d7d76eaada31535807a485ece0e21",
        )
        self.assertEqual(
            result.snapshot_identity.head_sha,
            "aa2dc024d33f61cdef50bf1973ab5adf0a974f5a",
        )
        self.assertEqual(result.dependency_change.dependency, "soupsieve")
        self.assertEqual(result.dependency_change.old_version, "2.6")
        self.assertEqual(result.dependency_change.new_version, "2.8.4")
        self.assertEqual(result.changed_file_evidence.paths, ("uv.lock",))
        self.assertEqual(raw_case, original_raw_case)


if __name__ == "__main__":
    unittest.main()
