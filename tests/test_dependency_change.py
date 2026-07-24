"""Tests for the exact pinned dependency-change interpretation boundary.

These tests supply already validated ``ChangedFile`` records. They therefore
exercise deterministic extraction and abstention behavior, not GitHub I/O.
"""

from __future__ import annotations

import unittest

from upgradepilot.dependency_change import (
    PinnedDependencyChange,
    UnsupportedDependencyChange,
    extract_pinned_dependency_change,
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
    """Build one trusted changed-file record with focused test variations."""

    return ChangedFile(
        filename=filename,
        status=status,
        additions=additions,
        deletions=deletions,
        changes=additions + deletions,
        patch=patch,
    )


class DependencyChangeTests(unittest.TestCase):
    """Protect supported extraction and explicit unsupported outcomes."""

    def test_extracts_supported_exact_pinned_change(self) -> None:
        result = extract_pinned_dependency_change(
            [
                _record(
                    "@@ -62,7 +62,7 @@ pyflakes==3.4.0\n"
                    " pygments==2.19.2\n"
                    "-pytest==9.0.2\n"
                    "+pytest==9.0.3"
                )
            ]
        )

        self.assertIsInstance(result, PinnedDependencyChange)
        # The unittest assertion proves runtime behavior; this assertion also
        # narrows the result union for type-aware readers and tools below.
        assert isinstance(result, PinnedDependencyChange)
        self.assertEqual(result.package, "pytest")
        self.assertEqual(result.old_version, "9.0.2")
        self.assertEqual(result.proposed_version, "9.0.3")
        self.assertEqual(result.source_file, "requirements-dev.txt")

    def test_missing_patch_is_explicitly_unsupported(self) -> None:
        result = extract_pinned_dependency_change([_record(None)])

        self.assertEqual(
            result,
            UnsupportedDependencyChange(
                reason="missing_patch_evidence",
                detail=(
                    "No usable patch evidence was available for requirements-dev.txt."
                ),
            ),
        )

    def test_range_change_is_outside_exact_pin_support(self) -> None:
        result = extract_pinned_dependency_change(
            [_record("-pytest>=9.0.2\n+pytest>=9.0.3")]
        )

        self.assertIsInstance(result, UnsupportedDependencyChange)
        assert isinstance(result, UnsupportedDependencyChange)
        self.assertEqual(result.reason, "no_supported_pinned_change")

    def test_different_package_names_are_unsupported(self) -> None:
        result = extract_pinned_dependency_change(
            [_record("-pytest==9.0.2\n+pluggy==1.6.0")]
        )

        self.assertIsInstance(result, UnsupportedDependencyChange)
        assert isinstance(result, UnsupportedDependencyChange)
        self.assertEqual(result.reason, "package_mismatch")

    def test_multiple_pinned_changes_are_ambiguous(self) -> None:
        result = extract_pinned_dependency_change(
            [
                _record(
                    "-pytest==9.0.2\n"
                    "+pytest==9.0.3\n"
                    "-pluggy==1.5.0\n"
                    "+pluggy==1.6.0",
                    additions=2,
                    deletions=2,
                )
            ]
        )

        self.assertIsInstance(result, UnsupportedDependencyChange)
        assert isinstance(result, UnsupportedDependencyChange)
        self.assertEqual(result.reason, "ambiguous_pinned_changes")

    def test_patch_count_disagreement_is_incomplete_evidence(self) -> None:
        result = extract_pinned_dependency_change(
            [
                _record(
                    "-pytest==9.0.2\n+pytest==9.0.3",
                    additions=2,
                    deletions=1,
                )
            ]
        )

        self.assertIsInstance(result, UnsupportedDependencyChange)
        assert isinstance(result, UnsupportedDependencyChange)
        self.assertEqual(result.reason, "incomplete_patch_evidence")


if __name__ == "__main__":
    unittest.main()
