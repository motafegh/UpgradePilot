"""Test deterministic dependency-change interpretation without GitHub I/O.

Purpose of this test file
-------------------------
``dependency_change.py`` receives already validated ``ChangedFile`` records and
must decide whether they prove one exact ``package==old`` to ``package==new``
transition. These tests construct those trusted records directly so they isolate
interpretation from acquisition.

The suite protects both the supported path and several honest abstention paths:
missing patch evidence, unsupported requirement syntax, package mismatch, ambiguous
multiple changes, and incomplete patch evidence.

Because no raw JSON or network collaborator appears here, failures point to the
extraction rule itself rather than GitHub transport or response parsing.
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
    """Build one trusted file record while varying only the evidence under test.

    ``patch`` remains positional because it is the main varied input. The remaining
    fields are keyword-only, making exceptional test conditions such as altered
    counts or status explicit at the call site.

    ``changes`` is derived from additions plus deletions so fixture metadata stays
    internally consistent unless a test intentionally varies another invariant.
    """

    return ChangedFile(
        filename=filename,
        status=status,
        additions=additions,
        deletions=deletions,
        changes=additions + deletions,
        patch=patch,
    )


class DependencyChangeTests(unittest.TestCase):
    """Protect supported extraction and explicit unsupported classifications."""

    def test_extracts_supported_exact_pinned_change(self) -> None:
        """One complete exact-pin replacement should produce trusted change identity."""

        # The hunk also contains an unchanged context line. The extractor must ignore
        # context and use only removed/added exact-pin lines as candidates.
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

        # ``assertIsInstance`` is the unittest assertion reported by the runner.
        self.assertIsInstance(result, PinnedDependencyChange)

        # The plain assertion additionally narrows the union for type-aware readers
        # and tools, allowing the following package/version attributes to be accessed.
        assert isinstance(result, PinnedDependencyChange)
        self.assertEqual(result.package, "pytest")
        self.assertEqual(result.old_version, "9.0.2")
        self.assertEqual(result.proposed_version, "9.0.3")
        self.assertEqual(result.source_file, "requirements-dev.txt")

    def test_missing_patch_is_explicitly_unsupported(self) -> None:
        """A valid file record without patch text must preserve missing evidence."""

        result = extract_pinned_dependency_change([_record(None)])

        # Dataclass value equality checks the complete expected result, including both
        # stable reason and human-readable detail, rather than only its class.
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
        """Version ranges must not be misread as supported exact pins."""

        result = extract_pinned_dependency_change(
            [_record("-pytest>=9.0.2\n+pytest>=9.0.3")]
        )

        self.assertIsInstance(result, UnsupportedDependencyChange)
        assert isinstance(result, UnsupportedDependencyChange)

        # The result is unsupported—not malformed—because the complete patch uses a
        # valid dependency form outside the current exact ``==`` grammar.
        self.assertEqual(result.reason, "no_supported_pinned_change")

    def test_different_package_names_are_unsupported(self) -> None:
        """Removed and added pins must normalize to the same package identity."""

        result = extract_pinned_dependency_change(
            [_record("-pytest==9.0.2\n+pluggy==1.6.0")]
        )

        self.assertIsInstance(result, UnsupportedDependencyChange)
        assert isinstance(result, UnsupportedDependencyChange)
        self.assertEqual(result.reason, "package_mismatch")

    def test_multiple_pinned_changes_are_ambiguous(self) -> None:
        """The extractor must abstain instead of choosing among multiple updates."""

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

        # Selecting one pair heuristically would contaminate later CI analysis, so
        # multiple complete candidates must remain explicitly ambiguous.
        self.assertEqual(result.reason, "ambiguous_pinned_changes")

    def test_patch_count_disagreement_is_incomplete_evidence(self) -> None:
        """Visible patch lines must agree with GitHub's independent edit counts."""

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

        # The visible patch appears simple, but metadata says another addition exists.
        # This protects the invariant that potentially truncated evidence is not trusted.
        self.assertEqual(result.reason, "incomplete_patch_evidence")


if __name__ == "__main__":
    unittest.main()
