"""Test Step 2 path eligibility and file-level exact-requirement extraction."""

from __future__ import annotations

import unittest

from upgradepilot.dependency_change import (
    DependencyChangeEvidenceProblem,
    ExtractedDependencyVersionChange,
)
from upgradepilot.exact_requirement_change import (
    extract_exact_requirement_changes,
    is_admitted_requirements_file,
    is_exact_requirement_file,
)
from upgradepilot.github_client import ChangedFile


def _record(
    patch: str | None,
    *,
    filename: str = "requirements-dev.txt",
    status: str = "modified",
    additions: int = 1,
    deletions: int = 1,
) -> ChangedFile:
    """Build one validated changed-file record with controlled evidence."""

    return ChangedFile(
        filename=filename,
        status=status,
        additions=additions,
        deletions=deletions,
        changes=additions + deletions,
        patch=patch,
    )


class ExactRequirementPathTests(unittest.TestCase):
    """Protect dependency-evidence admission and the narrower CI source role."""

    def test_accepts_conventional_descriptive_and_nested_paths(self) -> None:
        accepted = (
            "requirements.txt",
            "requirements-dev.txt",
            "requirements_test.in",
            "requirements.docs.txt",
            "constraints-ci.in",
            "constraints_python310.txt",
            "backend/requirements.txt",
            "docs/requirements.txt",
            "config/requirements/test.txt",
            "services/api/requirements/prod.in",
            "constraints/python/py310.txt",
        )

        for path in accepted:
            with self.subTest(path=path):
                self.assertTrue(is_exact_requirement_file(path))

    def test_distinguishes_requirements_family_from_constraints_family(self) -> None:
        requirements_paths = (
            "requirements.txt",
            "requirements-dev.txt",
            "backend/requirements.in",
            "config/requirements/test.txt",
            "services/api/requirements/prod.in",
        )
        constraints_paths = (
            "constraints.txt",
            "constraints-ci.in",
            "config/constraints/base.txt",
            "constraints/python/py310.txt",
        )

        for path in requirements_paths:
            with self.subTest(path=path):
                self.assertTrue(is_exact_requirement_file(path))
                self.assertTrue(is_admitted_requirements_file(path))

        for path in constraints_paths:
            with self.subTest(path=path):
                self.assertTrue(is_exact_requirement_file(path))
                self.assertFalse(is_admitted_requirements_file(path))

    def test_rejects_arbitrary_or_non_normalized_paths(self) -> None:
        rejected = (
            "README.txt",
            "dependency-list.txt",
            "docs/example.txt",
            "examples/dependency.in",
            "my-requirements-example.md",
            "requirements_notes.md",
            "/requirements.txt",
            "requirements//base.txt",
            "requirements/../base.txt",
            "Requirements/base.txt",
        )

        for path in rejected:
            with self.subTest(path=path):
                self.assertFalse(is_exact_requirement_file(path))
                self.assertFalse(is_admitted_requirements_file(path))


class ExactRequirementExtractionTests(unittest.TestCase):
    """Protect the file-level result and shared problem vocabulary."""

    def test_extracts_one_file_level_change_with_source_evidence(self) -> None:
        result = extract_exact_requirement_changes(
            _record("-pytest==9.0.2\n+pytest==9.0.3")
        )

        self.assertIsInstance(result, ExtractedDependencyVersionChange)
        assert isinstance(result, ExtractedDependencyVersionChange)
        self.assertEqual(result.package, "pytest")
        self.assertEqual(result.normalized_package, "pytest")
        self.assertEqual(result.old_version, "9.0.2")
        self.assertEqual(result.proposed_version, "9.0.3")
        self.assertEqual(result.source_evidence.path, "requirements-dev.txt")
        self.assertEqual(result.source_evidence.file_format, "exact_requirement")
        self.assertEqual(
            result.source_evidence.extraction_method,
            "changed_file_patch",
        )

    def test_rejects_ineligible_path_before_interpreting_patch_text(self) -> None:
        result = extract_exact_requirement_changes(
            _record(
                "-pytest==9.0.2\n+pytest==9.0.3",
                filename="docs/example.txt",
            )
        )

        self.assertEqual(
            result,
            DependencyChangeEvidenceProblem(
                reason="no_supported_dependency_file",
                detail=(
                    "Path 'docs/example.txt' is not an admitted conventional "
                    "requirements or constraints file."
                ),
            ),
        )

    def test_missing_patch_uses_shared_problem_code(self) -> None:
        result = extract_exact_requirement_changes(_record(None))

        self.assertIsInstance(result, DependencyChangeEvidenceProblem)
        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "missing_dependency_patch")
        self.assertEqual(result.source_evidence[0].path, "requirements-dev.txt")

    def test_incomplete_patch_uses_shared_problem_code(self) -> None:
        result = extract_exact_requirement_changes(
            _record(
                "-pytest==9.0.2\n+pytest==9.0.3",
                additions=2,
                deletions=1,
            )
        )

        self.assertIsInstance(result, DependencyChangeEvidenceProblem)
        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "incomplete_dependency_patch")

    def test_range_change_is_unsupported_requirement_format(self) -> None:
        result = extract_exact_requirement_changes(
            _record("-pytest>=9.0.2\n+pytest>=9.0.3")
        )

        self.assertIsInstance(result, DependencyChangeEvidenceProblem)
        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "unsupported_requirement_format")

    def test_non_modified_source_uses_shared_status_problem(self) -> None:
        result = extract_exact_requirement_changes(
            _record(
                "-pytest==9.0.2\n+pytest==9.0.3",
                status="renamed",
            )
        )

        self.assertIsInstance(result, DependencyChangeEvidenceProblem)
        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "unsupported_dependency_file_status")

    def test_multiple_exact_transitions_are_explicit(self) -> None:
        result = extract_exact_requirement_changes(
            _record(
                "-pytest==9.0.2\n"
                "+pytest==9.0.3\n"
                "-pluggy==1.5.0\n"
                "+pluggy==1.6.0",
                additions=2,
                deletions=2,
            )
        )

        self.assertIsInstance(result, DependencyChangeEvidenceProblem)
        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "multiple_dependency_version_changes")

    def test_different_package_identities_are_not_paired(self) -> None:
        result = extract_exact_requirement_changes(
            _record("-pytest==9.0.2\n+pluggy==1.6.0")
        )

        self.assertIsInstance(result, DependencyChangeEvidenceProblem)
        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "multiple_dependency_version_changes")


if __name__ == "__main__":
    unittest.main()
