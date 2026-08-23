"""Test the shared dependency-change evidence contracts."""

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError

from upgradepilot.dependency.change import (
    DEPENDENCY_CHANGE_PROBLEM_CODES,
    DependencyChangeProblem,
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
    ExtractedDependencyVersionChange,
)


class DependencyChangeContractTests(unittest.TestCase):
    """Protect the meaning and immutability of the shared dependency records."""

    def test_source_evidence_preserves_path_format_and_extraction_method(self) -> None:
        evidence = DependencyChangeSourceEvidence(
            path="uv.lock",
            file_format="uv_lock",
            extraction_method="exact_base_head_files",
        )

        self.assertEqual(evidence.path, "uv.lock")
        self.assertEqual(evidence.file_format, "uv_lock")
        self.assertEqual(evidence.extraction_method, "exact_base_head_files")

    def test_pyproject_optional_extra_is_an_exact_file_evidence_format(self) -> None:
        evidence = DependencyChangeSourceEvidence(
            path="pyproject.toml",
            file_format="pyproject_optional_extra",
            extraction_method="exact_base_head_files",
        )

        self.assertEqual(evidence.file_format, "pyproject_optional_extra")
        self.assertEqual(evidence.path, "pyproject.toml")

    def test_extracted_change_is_tied_to_one_source_but_not_pr_wide_trust(self) -> None:
        evidence = DependencyChangeSourceEvidence(
            path="requirements-dev.txt",
            file_format="exact_requirement",
            extraction_method="changed_file_patch",
        )
        extracted = ExtractedDependencyVersionChange(
            package="pytest",
            normalized_package="pytest",
            old_version="9.0.2",
            proposed_version="9.0.3",
            source_evidence=evidence,
        )

        self.assertEqual(extracted.source_evidence, evidence)
        self.assertEqual(extracted.old_version, "9.0.2")
        self.assertEqual(extracted.proposed_version, "9.0.3")

    def test_trusted_change_combines_sources_and_cannot_be_mutated(self) -> None:
        requirement_evidence = DependencyChangeSourceEvidence(
            path="requirements-dev.txt",
            file_format="exact_requirement",
            extraction_method="changed_file_patch",
        )
        lock_evidence = DependencyChangeSourceEvidence(
            path="uv.lock",
            file_format="uv_lock",
            extraction_method="exact_base_head_files",
        )
        change = DependencyVersionChange(
            package="pytest",
            normalized_package="pytest",
            old_version="9.0.2",
            proposed_version="9.0.3",
            source_evidence=(requirement_evidence, lock_evidence),
            limitations=("dependency role not established",),
        )

        self.assertEqual(change.source_evidence, (requirement_evidence, lock_evidence))
        self.assertEqual(change.limitations, ("dependency role not established",))

        with self.assertRaises(FrozenInstanceError):
            setattr(change, "package", "pluggy")

        with self.assertRaises(AttributeError):
            change.source_evidence.append(requirement_evidence)  # type: ignore[attr-defined]

    def test_problem_uses_one_explicit_immutable_vocabulary(self) -> None:
        self.assertEqual(
            DEPENDENCY_CHANGE_PROBLEM_CODES,
            (
                "no_supported_dependency_file",
                "missing_dependency_patch",
                "incomplete_dependency_patch",
                "unsupported_requirement_format",
                "unsupported_dependency_file_status",
                "dependency_file_unavailable",
                "dependency_file_too_large",
                "malformed_dependency_file",
                "invalid_dependency_record",
                "unsupported_uv_lock_schema",
                "unsupported_uv_lock_structural_change",
                "ambiguous_uv_lock_package_records",
                "unsupported_pyproject_optional_dependency_change",
                "ambiguous_pyproject_dependency_records",
                "version_unchanged",
                "multiple_dependency_version_changes",
                "conflicting_dependency_version_changes",
            ),
        )

        evidence = DependencyChangeSourceEvidence(
            path="pyproject.toml",
            file_format="pyproject_optional_extra",
            extraction_method="exact_base_head_files",
        )
        problem = DependencyChangeProblem(
            reason="unsupported_pyproject_optional_dependency_change",
            detail="The change also moved the dependency across extras.",
            source_evidence=(evidence,),
        )

        self.assertEqual(
            problem.reason,
            "unsupported_pyproject_optional_dependency_change",
        )
        self.assertEqual(problem.source_evidence, (evidence,))


if __name__ == "__main__":
    unittest.main()
