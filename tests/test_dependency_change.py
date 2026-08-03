"""Test modern PR-wide dependency-change comparison contracts."""

from __future__ import annotations

import unittest

from upgradepilot.dependency.change import (
    DependencyChangeProblem,
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
    ExtractedDependencyVersionChange,
    compare_extracted_dependency_changes,
)


def _extracted(
    package: str = "pytest",
    normalized_package: str = "pytest",
    old_version: str = "9.0.2",
    proposed_version: str = "9.0.3",
    path: str = "requirements-dev.txt",
) -> ExtractedDependencyVersionChange:
    return ExtractedDependencyVersionChange(
        package=package,
        normalized_package=normalized_package,
        old_version=old_version,
        proposed_version=proposed_version,
        source_evidence=DependencyChangeSourceEvidence(
            path=path,
            file_format="exact_requirement",
            extraction_method="changed_file_patch",
        ),
    )


class DependencyChangeTests(unittest.TestCase):
    def test_one_extracted_change_becomes_trusted_dependency_change(self) -> None:
        result = compare_extracted_dependency_changes((_extracted(),))

        self.assertIsInstance(result, DependencyVersionChange)
        assert isinstance(result, DependencyVersionChange)
        self.assertEqual(result.package, "pytest")
        self.assertEqual(result.old_version, "9.0.2")
        self.assertEqual(result.proposed_version, "9.0.3")
        self.assertEqual(len(result.source_evidence), 1)

    def test_matching_sources_are_combined_without_duplicate_fact_identity(self) -> None:
        result = compare_extracted_dependency_changes(
            (
                _extracted(path="requirements-dev.txt"),
                ExtractedDependencyVersionChange(
                    package="pytest",
                    normalized_package="pytest",
                    old_version="9.0.2",
                    proposed_version="9.0.3",
                    source_evidence=DependencyChangeSourceEvidence(
                        path="uv.lock",
                        file_format="uv_lock",
                        extraction_method="exact_base_head_files",
                    ),
                ),
            )
        )

        self.assertIsInstance(result, DependencyVersionChange)
        assert isinstance(result, DependencyVersionChange)
        self.assertEqual(len(result.source_evidence), 2)

    def test_different_packages_are_explicitly_ambiguous(self) -> None:
        result = compare_extracted_dependency_changes(
            (_extracted(), _extracted(package="pluggy", normalized_package="pluggy"))
        )

        self.assertIsInstance(result, DependencyChangeProblem)
        assert isinstance(result, DependencyChangeProblem)
        self.assertEqual(result.reason, "multiple_dependency_version_changes")

    def test_conflicting_transitions_are_explicit(self) -> None:
        result = compare_extracted_dependency_changes(
            (_extracted(), _extracted(proposed_version="9.1.0", path="uv.lock"))
        )

        self.assertIsInstance(result, DependencyChangeProblem)
        assert isinstance(result, DependencyChangeProblem)
        self.assertEqual(result.reason, "conflicting_dependency_version_changes")

    def test_source_problem_stops_comparison(self) -> None:
        problem = DependencyChangeProblem(
            reason="missing_dependency_patch",
            detail="patch missing",
        )
        self.assertEqual(compare_extracted_dependency_changes((problem,)).reason, "missing_dependency_patch")


if __name__ == "__main__":
    unittest.main()
