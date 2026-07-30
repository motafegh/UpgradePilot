"""Test the shared dependency-change records before parser migration.

These tests isolate the Step 1 contract layer. They do not parse requirements files,
acquire GitHub content, interpret ``uv.lock``, or change the existing CLI path.
"""

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError

from upgradepilot.dependency_change import (
    DEPENDENCY_CHANGE_PROBLEM_CODES,
    DependencyChangeEvidenceProblem,
    DependencyFileEvidence,
    DependencyVersionChange,
    ExtractedDependencyVersionChange,
)


class DependencyChangeContractTests(unittest.TestCase):
    """Protect the meaning and immutability of the new shared records."""

    def test_file_evidence_preserves_path_method_and_exact_file_identity(self) -> None:
        """Structured evidence should retain both immutable repository-file versions."""

        evidence = DependencyFileEvidence(
            path="uv.lock",
            file_format="uv_lock",
            extraction_method="exact_base_head_files",
            base_revision="652a61ce4f9d7d76eaada31535807a485ece0e21",
            base_blob_sha="b4a68ab725de337889d50d5374ac0f05db7fb484",
            base_byte_count=606_307,
            head_revision="aa2dc024d33f61cdef50bf1973ab5adf0a974f5a",
            head_blob_sha="def33fe05d78ab851ce91a33db5bc55a439873a1",
            head_byte_count=606_313,
        )

        self.assertEqual(evidence.path, "uv.lock")
        self.assertEqual(evidence.file_format, "uv_lock")
        self.assertEqual(evidence.extraction_method, "exact_base_head_files")
        self.assertEqual(evidence.base_byte_count, 606_307)
        self.assertEqual(evidence.head_byte_count, 606_313)

    def test_extracted_change_is_tied_to_one_source_but_not_pr_wide_trust(self) -> None:
        """One file-level observation should keep exactly one source evidence record."""

        evidence = DependencyFileEvidence(
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
        """A PR-wide trusted change should preserve all supporting evidence immutably."""

        requirement_evidence = DependencyFileEvidence(
            path="requirements-dev.txt",
            file_format="exact_requirement",
            extraction_method="changed_file_patch",
        )
        lock_evidence = DependencyFileEvidence(
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

        self.assertEqual(
            change.source_evidence,
            (requirement_evidence, lock_evidence),
        )
        self.assertEqual(change.limitations, ("dependency role not established",))

        with self.assertRaises(FrozenInstanceError):
            setattr(change, "package", "pluggy")

        with self.assertRaises(AttributeError):
            change.source_evidence.append(requirement_evidence)  # type: ignore[attr-defined]

    def test_problem_uses_one_explicit_immutable_vocabulary(self) -> None:
        """Problem reasons should come from the architecture's exact stable vocabulary."""

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
                "version_unchanged",
                "multiple_dependency_version_changes",
                "conflicting_dependency_version_changes",
            ),
        )

        evidence = DependencyFileEvidence(
            path="uv.lock",
            file_format="uv_lock",
            extraction_method="exact_base_head_files",
        )
        problem = DependencyChangeEvidenceProblem(
            reason="ambiguous_uv_lock_package_records",
            detail="A repeated package group changed and cannot be paired safely.",
            source_evidence=(evidence,),
        )

        self.assertEqual(problem.reason, "ambiguous_uv_lock_package_records")
        self.assertEqual(problem.source_evidence, (evidence,))


if __name__ == "__main__":
    unittest.main()
