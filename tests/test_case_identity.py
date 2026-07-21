from copy import deepcopy
import json
import unittest

from pydantic import ValidationError

from upgradepilot.case_identity import (
    ChangedFileEvidence,
    DependencyChange,
    InitialCaseRecord,
    PullRequestSnapshotIdentity,
    build_initial_case_record,
)


BASE_SHA = "652a61ce4f9d7d76eaada31535807a485ece0e21"
HEAD_SHA = "aa2dc024d33f61cdef50bf1973ab5adf0a974f5a"


def _real_m1_case() -> dict[str, object]:
    return {
        "repository": " pydantic/pydantic ",
        "pr_number": 13432,
        "base_sha": BASE_SHA.upper(),
        "head_sha": HEAD_SHA.upper(),
        "dependency": " soupsieve ",
        "old_version": " 2.6 ",
        "new_version": " 2.8.4 ",
        "changed_files": [" uv.lock "],
    }


class BuildInitialCaseRecordTests(unittest.TestCase):
    def test_builds_nested_record_from_real_m1_case_without_mutating_raw_input(self) -> None:
        raw_case = _real_m1_case()
        original_raw_case = deepcopy(raw_case)

        result = build_initial_case_record(raw_case)

        self.assertIsInstance(result, InitialCaseRecord)
        self.assertEqual(result.snapshot_identity.repository, "pydantic/pydantic")
        self.assertEqual(result.snapshot_identity.pr_number, 13432)
        self.assertEqual(result.snapshot_identity.base_sha, BASE_SHA)
        self.assertEqual(result.snapshot_identity.head_sha, HEAD_SHA)
        self.assertEqual(result.dependency_change.dependency, "soupsieve")
        self.assertEqual(result.dependency_change.old_version, "2.6")
        self.assertEqual(result.dependency_change.new_version, "2.8.4")
        self.assertEqual(result.changed_file_evidence.paths, ("uv.lock",))
        self.assertEqual(raw_case, original_raw_case)

    def test_rejects_missing_head_sha(self) -> None:
        raw_case = _real_m1_case()
        del raw_case["head_sha"]

        with self.assertRaises(ValidationError) as raised:
            build_initial_case_record(raw_case)

        finding = raised.exception.errors(include_url=False)[0]
        self.assertEqual(finding["loc"], ("head_sha",))
        self.assertEqual(finding["type"], "missing")

    def test_rejects_malformed_head_sha_without_returning_a_partial_record(self) -> None:
        raw_case = _real_m1_case()
        raw_case["head_sha"] = "not-a-full-sha"

        with self.assertRaises(ValidationError) as raised:
            build_initial_case_record(raw_case)

        findings = raised.exception.errors(include_url=False)
        head_sha_findings = [
            finding for finding in findings if finding["loc"] == ("head_sha",)
        ]

        self.assertEqual(len(head_sha_findings), 1)
        self.assertEqual(head_sha_findings[0]["type"], "value_error")
        self.assertIn(
            "head_sha must be exactly 40 hexadecimal characters",
            head_sha_findings[0]["msg"],
        )

    def test_rejects_non_integer_pr_number_without_coercion(self) -> None:
        for invalid_pr_number in ("13432", True):
            with self.subTest(pr_number=invalid_pr_number):
                raw_case = _real_m1_case()
                raw_case["pr_number"] = invalid_pr_number

                with self.assertRaises(ValidationError) as raised:
                    build_initial_case_record(raw_case)

                finding = raised.exception.errors(include_url=False)[0]
                self.assertEqual(finding["loc"], ("pr_number",))
                self.assertEqual(finding["type"], "int_type")

    def test_rejects_unknown_top_level_field(self) -> None:
        raw_case = _real_m1_case()
        raw_case["unexpected"] = "value"

        with self.assertRaises(ValidationError) as raised:
            build_initial_case_record(raw_case)

        finding = raised.exception.errors(include_url=False)[0]
        self.assertEqual(finding["loc"], ("unexpected",))
        self.assertEqual(finding["type"], "extra_forbidden")

    def test_rejects_repository_outside_basic_owner_name_form(self) -> None:
        for invalid_repository in (
            "pydantic",
            "/pydantic",
            "pydantic/",
            "organization/team/repository",
        ):
            with self.subTest(repository=invalid_repository):
                raw_case = _real_m1_case()
                raw_case["repository"] = invalid_repository

                with self.assertRaises(ValidationError) as raised:
                    build_initial_case_record(raw_case)

                finding = raised.exception.errors(include_url=False)[0]
                self.assertEqual(finding["loc"], ("repository",))
                self.assertEqual(finding["type"], "value_error")

    def test_rejects_non_positive_pr_number(self) -> None:
        for invalid_pr_number in (0, -1):
            with self.subTest(pr_number=invalid_pr_number):
                raw_case = _real_m1_case()
                raw_case["pr_number"] = invalid_pr_number

                with self.assertRaises(ValidationError) as raised:
                    build_initial_case_record(raw_case)

                finding = raised.exception.errors(include_url=False)[0]
                self.assertEqual(finding["loc"], ("pr_number",))
                self.assertIn("positive integer", finding["msg"])

    def test_rejects_empty_dependency_or_version_after_trimming(self) -> None:
        for field_name in ("dependency", "old_version", "new_version"):
            with self.subTest(field=field_name):
                raw_case = _real_m1_case()
                raw_case[field_name] = "   "

                with self.assertRaises(ValidationError) as raised:
                    build_initial_case_record(raw_case)

                finding = raised.exception.errors(include_url=False)[0]
                self.assertEqual(finding["loc"], (field_name,))
                self.assertIn("must not be empty", finding["msg"])

    def test_rejects_equal_versions_after_normalization(self) -> None:
        raw_case = _real_m1_case()
        raw_case["old_version"] = " 2.8.4 "
        raw_case["new_version"] = "2.8.4"

        with self.assertRaises(ValidationError) as raised:
            build_initial_case_record(raw_case)

        finding = raised.exception.errors(include_url=False)[0]
        self.assertEqual(finding["loc"], ())
        self.assertEqual(finding["type"], "value_error")
        self.assertIn("old_version and new_version must differ", finding["msg"])

    def test_rejects_empty_changed_file_collection(self) -> None:
        raw_case = _real_m1_case()
        raw_case["changed_files"] = []

        with self.assertRaises(ValidationError) as raised:
            build_initial_case_record(raw_case)

        finding = raised.exception.errors(include_url=False)[0]
        self.assertEqual(finding["loc"], ("changed_files",))
        self.assertIn("at least one path", finding["msg"])

    def test_rejects_empty_normalized_changed_file_path(self) -> None:
        raw_case = _real_m1_case()
        raw_case["changed_files"] = ["   "]

        with self.assertRaises(ValidationError) as raised:
            build_initial_case_record(raw_case)

        finding = raised.exception.errors(include_url=False)[0]
        self.assertEqual(finding["loc"], ("changed_files",))
        self.assertEqual(finding["type"], "value_error")

    def test_identifies_duplicate_changed_file_path_after_normalization(self) -> None:
        raw_case = _real_m1_case()
        raw_case["changed_files"] = ["uv.lock", " uv.lock "]

        with self.assertRaises(ValidationError) as raised:
            build_initial_case_record(raw_case)

        finding = raised.exception.errors(include_url=False)[0]
        self.assertEqual(finding["loc"], ("changed_files",))
        self.assertEqual(finding["type"], "value_error")
        self.assertIn(
            "duplicate changed file path after normalization: uv.lock",
            finding["msg"],
        )

    def test_preserves_changed_file_order_without_aliasing_the_raw_list(self) -> None:
        raw_case = _real_m1_case()
        raw_paths = [" uv.lock ", " docs/plugins/algolia.py "]
        raw_case["changed_files"] = raw_paths

        result = build_initial_case_record(raw_case)
        raw_paths.append("later-added.py")

        self.assertEqual(
            result.changed_file_evidence.paths,
            ("uv.lock", "docs/plugins/algolia.py"),
        )

    def test_preserves_non_sha_casing_while_canonicalizing_shas(self) -> None:
        raw_case = _real_m1_case()
        raw_case["repository"] = " Owner/Repository "
        raw_case["dependency"] = " SomePackage "
        raw_case["old_version"] = " V1 "
        raw_case["new_version"] = " V2 "
        raw_case["changed_files"] = [" Src/Module.py "]

        result = build_initial_case_record(raw_case)

        self.assertEqual(result.snapshot_identity.repository, "Owner/Repository")
        self.assertEqual(result.snapshot_identity.base_sha, BASE_SHA)
        self.assertEqual(result.snapshot_identity.head_sha, HEAD_SHA)
        self.assertEqual(result.dependency_change.dependency, "SomePackage")
        self.assertEqual(result.dependency_change.old_version, "V1")
        self.assertEqual(result.dependency_change.new_version, "V2")
        self.assertEqual(result.changed_file_evidence.paths, ("Src/Module.py",))

    def test_serializes_nested_record_to_machine_readable_json(self) -> None:
        result = build_initial_case_record(_real_m1_case())

        serialized = json.loads(result.model_dump_json())

        self.assertEqual(
            serialized,
            {
                "snapshot_identity": {
                    "repository": "pydantic/pydantic",
                    "pr_number": 13432,
                    "base_sha": BASE_SHA,
                    "head_sha": HEAD_SHA,
                },
                "dependency_change": {
                    "dependency": "soupsieve",
                    "old_version": "2.6",
                    "new_version": "2.8.4",
                },
                "changed_file_evidence": {"paths": ["uv.lock"]},
            },
        )


class TrustedContractTests(unittest.TestCase):
    def test_snapshot_identity_rejects_direct_strict_type_violation(self) -> None:
        with self.assertRaises(ValidationError) as raised:
            PullRequestSnapshotIdentity(
                repository="pydantic/pydantic",
                pr_number="13432",  # type: ignore[arg-type]
                base_sha=BASE_SHA,
                head_sha=HEAD_SHA,
            )

        finding = raised.exception.errors(include_url=False)[0]
        self.assertEqual(finding["loc"], ("pr_number",))
        self.assertEqual(finding["type"], "int_type")

    def test_dependency_change_rejects_equal_versions_when_built_directly(self) -> None:
        with self.assertRaises(ValidationError) as raised:
            DependencyChange(
                dependency="soupsieve",
                old_version="2.8.4",
                new_version="2.8.4",
            )

        finding = raised.exception.errors(include_url=False)[0]
        self.assertEqual(finding["loc"], ())
        self.assertIn("must differ", finding["msg"])

    def test_changed_file_evidence_requires_an_immutable_tuple(self) -> None:
        with self.assertRaises(ValidationError) as raised:
            ChangedFileEvidence(paths=["uv.lock"])  # type: ignore[arg-type]

        finding = raised.exception.errors(include_url=False)[0]
        self.assertEqual(finding["loc"], ("paths",))
        self.assertEqual(finding["type"], "tuple_type")

    def test_trusted_models_are_frozen(self) -> None:
        result = build_initial_case_record(_real_m1_case())

        with self.assertRaises(ValidationError) as raised:
            result.snapshot_identity.repository = "other/repository"

        finding = raised.exception.errors(include_url=False)[0]
        self.assertEqual(finding["loc"], ("repository",))
        self.assertEqual(finding["type"], "frozen_instance")


if __name__ == "__main__":
    unittest.main()
