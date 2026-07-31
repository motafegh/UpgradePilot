"""Test PR-wide comparison of source-specific dependency extraction results.

These tests begin after source-specific parsing. They construct typed file-level results
directly so failures isolate comparison, conflict detection, and evidence aggregation
rather than requirements syntax, GitHub patch acquisition, or future ``uv.lock`` parsing.
"""

from __future__ import annotations

import unittest

from upgradepilot.dependency_change import (
    DependencyChangeEvidenceProblem,
    DependencyFileEvidence,
    DependencyVersionChange,
    ExtractedDependencyVersionChange,
    compare_extracted_dependency_changes,
)


def _evidence(path: str) -> DependencyFileEvidence:
    """Build one patch-derived exact-requirement source record."""

    return DependencyFileEvidence(
        path=path,
        file_format="exact_requirement",
        extraction_method="changed_file_patch",
    )


def _change(
    path: str,
    *,
    package: str = "pytest",
    normalized_package: str = "pytest",
    old_version: str = "9.0.2",
    proposed_version: str = "9.0.3",
) -> ExtractedDependencyVersionChange:
    """Build one file-level extracted transition with controlled identity."""

    return ExtractedDependencyVersionChange(
        package=package,
        normalized_package=normalized_package,
        old_version=old_version,
        proposed_version=proposed_version,
        source_evidence=_evidence(path),
    )


class DependencyChangeComparisonTests(unittest.TestCase):
    """Protect the B2 exactly-one-transition comparison rule."""

    def test_no_results_has_no_supported_dependency_file(self) -> None:
        """An empty comparison input cannot establish a dependency transition."""

        result = compare_extracted_dependency_changes(())

        self.assertEqual(
            result,
            DependencyChangeEvidenceProblem(
                reason="no_supported_dependency_file",
                detail=(
                    "No extracted dependency version change or recognized dependency-file "
                    "problem was available for PR-wide comparison."
                ),
            ),
        )

    def test_one_extracted_change_becomes_pr_wide_trusted(self) -> None:
        """One unopposed file-level result should become the trusted shared record."""

        extracted = _change("requirements-dev.txt")

        result = compare_extracted_dependency_changes((extracted,))

        self.assertIsInstance(result, DependencyVersionChange)
        assert isinstance(result, DependencyVersionChange)
        self.assertEqual(result.package, "pytest")
        self.assertEqual(result.normalized_package, "pytest")
        self.assertEqual(result.old_version, "9.0.2")
        self.assertEqual(result.proposed_version, "9.0.3")
        self.assertEqual(result.source_evidence, (extracted.source_evidence,))
        self.assertEqual(result.limitations, ())

    def test_equivalent_changes_combine_all_source_evidence(self) -> None:
        """Equivalent normalized identity and exact strings should aggregate sources."""

        first = _change(
            "requirements.txt",
            package="My_Package",
            normalized_package="my-package",
            old_version="1.0.0",
            proposed_version="1.1.0",
        )
        second = _change(
            "constraints/production.txt",
            package="my-package",
            normalized_package="my-package",
            old_version="1.0.0",
            proposed_version="1.1.0",
        )

        result = compare_extracted_dependency_changes((first, second))

        self.assertIsInstance(result, DependencyVersionChange)
        assert isinstance(result, DependencyVersionChange)
        self.assertEqual(result.package, "My_Package")
        self.assertEqual(result.normalized_package, "my-package")
        self.assertEqual(result.old_version, "1.0.0")
        self.assertEqual(result.proposed_version, "1.1.0")
        self.assertEqual(
            result.source_evidence,
            (first.source_evidence, second.source_evidence),
        )

    def test_conflicting_transitions_for_one_package_are_explicit(self) -> None:
        """One package with different exact version transitions must not be merged."""

        first = _change("requirements.txt")
        second = _change(
            "requirements-dev.txt",
            proposed_version="9.0.4",
        )

        result = compare_extracted_dependency_changes((first, second))

        self.assertIsInstance(result, DependencyChangeEvidenceProblem)
        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "conflicting_dependency_version_changes")
        self.assertEqual(
            result.source_evidence,
            (first.source_evidence, second.source_evidence),
        )

    def test_several_package_changes_are_explicit(self) -> None:
        """B2 must abstain rather than choose among different changed packages."""

        pytest_change = _change("requirements-dev.txt")
        pluggy_change = _change(
            "constraints-ci.in",
            package="pluggy",
            normalized_package="pluggy",
            old_version="1.5.0",
            proposed_version="1.6.0",
        )

        result = compare_extracted_dependency_changes(
            (pytest_change, pluggy_change)
        )

        self.assertIsInstance(result, DependencyChangeEvidenceProblem)
        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "multiple_dependency_version_changes")
        self.assertEqual(
            result.source_evidence,
            (pytest_change.source_evidence, pluggy_change.source_evidence),
        )

    def test_recognized_problem_blocks_a_convenient_change(self) -> None:
        """Malformed admitted evidence must not be ignored beside a valid extraction."""

        valid = _change("requirements-dev.txt")
        malformed_evidence = _evidence("constraints-ci.in")
        malformed = DependencyChangeEvidenceProblem(
            reason="malformed_dependency_file",
            detail="The admitted dependency file could not be interpreted safely.",
            source_evidence=(malformed_evidence,),
        )

        result = compare_extracted_dependency_changes((valid, malformed))

        self.assertEqual(
            result,
            DependencyChangeEvidenceProblem(
                reason="malformed_dependency_file",
                detail="The admitted dependency file could not be interpreted safely.",
                source_evidence=(valid.source_evidence, malformed_evidence),
            ),
        )


if __name__ == "__main__":
    unittest.main()
