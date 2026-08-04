"""Test Step 5A conversion from PyPI release keys to crossed-release evidence."""

from __future__ import annotations

import unittest
from datetime import datetime, timezone

from upgradepilot.pypi.release import PackageReleaseIndexEvidence
from upgradepilot.upstream.interval import DependencyReleaseInterval
from upgradepilot.upstream.interval_evidence import (
    CrossedReleaseIndexSelectionProblem,
    SelectedCrossedReleaseIndex,
    select_crossed_release_index,
)

_NOW = datetime(2026, 8, 2, 12, 0, tzinfo=timezone.utc)
_REPOSITORY = "facelessuser/soupsieve"


def _interval(
    *,
    package: str = "soupsieve",
    normalized_package: str = "soupsieve",
    old_version: str = "2.6",
    proposed_version: str = "2.8.4",
) -> DependencyReleaseInterval:
    return DependencyReleaseInterval(
        package=package,
        normalized_package=normalized_package,
        old_version=old_version,
        proposed_version=proposed_version,
    )


def _index(
    *release_versions: str,
    normalized_package: str = "soupsieve",
) -> PackageReleaseIndexEvidence:
    return PackageReleaseIndexEvidence(
        requested_package="soupsieve",
        normalized_package=normalized_package,
        published_name="soupsieve",
        source_url="https://pypi.org/pypi/soupsieve/json",
        retrieved_at=_NOW,
        last_serial=12345,
        release_versions=tuple(release_versions),
    )


class UpstreamIntervalAcquisitionTests(unittest.TestCase):
    """Protect old-exclusive selection, exact raw identity, and honest exclusions."""

    def test_s001_shaped_release_set_becomes_ordered_crossed_index(self) -> None:
        result = select_crossed_release_index(
            _interval(),
            _REPOSITORY,
            _index(
                "2.9",
                "2.8.4",
                "2.6",
                "2.8.3",
                "2.8",
                "2.7",
                "2.8.2",
                "2.5",
            ),
        )

        self.assertIsInstance(result, SelectedCrossedReleaseIndex)
        assert isinstance(result, SelectedCrossedReleaseIndex)
        self.assertEqual(
            result.evidence.ordered_versions,
            ("2.7", "2.8", "2.8.2", "2.8.3", "2.8.4"),
        )
        self.assertNotIn("2.6", result.evidence.ordered_versions)
        self.assertNotIn("2.9", result.evidence.ordered_versions)

    def test_source_identity_and_retrieval_evidence_are_preserved(self) -> None:
        source = _index("2.6", "2.7", "2.8.4")
        result = select_crossed_release_index(_interval(), _REPOSITORY, source)
        self.assertIsInstance(result, SelectedCrossedReleaseIndex)
        assert isinstance(result, SelectedCrossedReleaseIndex)
        self.assertIs(result.source_index, source)
        self.assertEqual(result.evidence.repository, _REPOSITORY)
        self.assertEqual(result.evidence.interval, _interval())
        self.assertEqual(result.evidence.source_url, source.source_url)
        self.assertEqual(result.evidence.retrieved_at, _NOW)

    def test_non_pep440_project_keys_are_preserved_as_ignored(self) -> None:
        result = select_crossed_release_index(
            _interval(),
            _REPOSITORY,
            _index("legacy-final", "2.6", "2.7", "2.8.4"),
        )
        self.assertIsInstance(result, SelectedCrossedReleaseIndex)
        assert isinstance(result, SelectedCrossedReleaseIndex)
        self.assertEqual(result.evidence.ordered_versions, ("2.7", "2.8.4"))
        self.assertEqual(result.ignored_non_pep440_versions, ("legacy-final",))

    def test_exact_raw_proposed_release_must_exist(self) -> None:
        result = select_crossed_release_index(
            _interval(),
            _REPOSITORY,
            _index("2.6", "2.7", "2.8", "2.8.3"),
        )
        self.assertIsInstance(result, CrossedReleaseIndexSelectionProblem)
        assert isinstance(result, CrossedReleaseIndexSelectionProblem)
        self.assertEqual(result.state, "release_index_unusable")
        self.assertIsNotNone(result.method_problem)
        assert result.method_problem is not None
        self.assertEqual(result.method_problem.state, "proposed_release_missing")

    def test_pep440_equivalent_selected_release_keys_are_not_collapsed(self) -> None:
        result = select_crossed_release_index(
            _interval(),
            _REPOSITORY,
            _index("2.6", "2.7", "2.8.4", "2.8.4.0"),
        )
        self.assertIsInstance(result, CrossedReleaseIndexSelectionProblem)
        assert isinstance(result, CrossedReleaseIndexSelectionProblem)
        self.assertEqual(result.state, "release_index_unusable")
        self.assertIsNotNone(result.method_problem)
        assert result.method_problem is not None
        self.assertEqual(result.method_problem.state, "equivalent_crossed_release_versions")

    def test_release_index_package_must_match_dependency_interval(self) -> None:
        result = select_crossed_release_index(
            _interval(),
            _REPOSITORY,
            _index("2.6", "2.8.4", normalized_package="other-package"),
        )
        self.assertIsInstance(result, CrossedReleaseIndexSelectionProblem)
        assert isinstance(result, CrossedReleaseIndexSelectionProblem)
        self.assertEqual(result.state, "identity_mismatch")
        self.assertIsNone(result.method_problem)

    def test_invalid_dependency_interval_remains_method_unresolved(self) -> None:
        result = select_crossed_release_index(
            _interval(old_version="not-a-version"),
            _REPOSITORY,
            _index("2.7", "2.8.4"),
        )
        self.assertIsInstance(result, CrossedReleaseIndexSelectionProblem)
        assert isinstance(result, CrossedReleaseIndexSelectionProblem)
        self.assertEqual(result.state, "dependency_interval_unresolved")
        self.assertIsNotNone(result.method_problem)
        assert result.method_problem is not None
        self.assertEqual(result.method_problem.state, "invalid_python_package_version")

    def test_wrong_public_argument_types_are_rejected(self) -> None:
        with self.assertRaises(TypeError):
            select_crossed_release_index(
                "not-an-interval",  # type: ignore[arg-type]
                _REPOSITORY,
                _index("2.8.4"),
            )
        with self.assertRaises(TypeError):
            select_crossed_release_index(
                _interval(),
                _REPOSITORY,
                "not-an-index",  # type: ignore[arg-type]
            )

    def test_malformed_repository_locator_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            select_crossed_release_index(
                _interval(),
                "not-a-repository",
                _index("2.6", "2.8.4"),
            )


if __name__ == "__main__":
    unittest.main()
