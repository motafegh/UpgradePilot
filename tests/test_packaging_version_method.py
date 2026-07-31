"""Test PEP 440 parsing and crossed-release ordering for Step 3."""

from __future__ import annotations

import unittest

from packaging.version import Version

from upgradepilot.packaging_method import (
    OrderedCrossedReleaseVersions,
    PackagingVersionProblem,
    ParsedDependencyReleaseInterval,
    order_crossed_release_versions,
    parse_dependency_release_interval,
)
from upgradepilot.upstream_interval import DependencyReleaseInterval


def _interval(
    old_version: str = "2.6",
    proposed_version: str = "2.8.4",
) -> DependencyReleaseInterval:
    return DependencyReleaseInterval(
        package="friendly-bard",
        normalized_package="friendly-bard",
        old_version=old_version,
        proposed_version=proposed_version,
    )


class DependencyReleaseIntervalMethodTests(unittest.TestCase):
    def test_forward_interval_preserves_raw_and_parsed_versions(self) -> None:
        interval = _interval()

        result = parse_dependency_release_interval(interval)

        self.assertIsInstance(result, ParsedDependencyReleaseInterval)
        assert isinstance(result, ParsedDependencyReleaseInterval)
        self.assertIs(result.interval, interval)
        self.assertEqual(result.old_version, Version("2.6"))
        self.assertEqual(result.proposed_version, Version("2.8.4"))
        self.assertEqual(result.interval.old_version, "2.6")
        self.assertEqual(result.interval.proposed_version, "2.8.4")

    def test_invalid_old_version_is_explicit(self) -> None:
        result = parse_dependency_release_interval(_interval(old_version="not-a-version"))

        self.assertIsInstance(result, PackagingVersionProblem)
        assert isinstance(result, PackagingVersionProblem)
        self.assertEqual(result.state, "invalid_python_package_version")
        self.assertEqual(result.release_version, "not-a-version")

    def test_invalid_proposed_version_is_explicit(self) -> None:
        result = parse_dependency_release_interval(
            _interval(proposed_version="not-a-version")
        )

        self.assertIsInstance(result, PackagingVersionProblem)
        assert isinstance(result, PackagingVersionProblem)
        self.assertEqual(result.state, "invalid_python_package_version")
        self.assertEqual(result.release_version, "not-a-version")

    def test_pep440_equivalent_bounds_are_not_a_change(self) -> None:
        result = parse_dependency_release_interval(
            _interval(old_version="1.0", proposed_version="1.0.0")
        )

        self.assertIsInstance(result, PackagingVersionProblem)
        assert isinstance(result, PackagingVersionProblem)
        self.assertEqual(result.state, "equivalent_python_package_versions")

    def test_backwards_interval_is_explicit(self) -> None:
        result = parse_dependency_release_interval(
            _interval(old_version="2.8.4", proposed_version="2.6")
        )

        self.assertIsInstance(result, PackagingVersionProblem)
        assert isinstance(result, PackagingVersionProblem)
        self.assertEqual(result.state, "dependency_version_not_forward")

    def test_prerelease_to_final_is_valid_pep440_forward_ordering(self) -> None:
        result = parse_dependency_release_interval(
            _interval(old_version="2.8.4rc1", proposed_version="2.8.4")
        )

        self.assertIsInstance(result, ParsedDependencyReleaseInterval)
        assert isinstance(result, ParsedDependencyReleaseInterval)
        self.assertLess(result.old_version, result.proposed_version)


class CrossedReleaseOrderingMethodTests(unittest.TestCase):
    def setUp(self) -> None:
        parsed = parse_dependency_release_interval(_interval())
        assert isinstance(parsed, ParsedDependencyReleaseInterval)
        self.interval = parsed

    def test_unsorted_crossed_releases_are_ordered_and_raw_values_preserved(self) -> None:
        result = order_crossed_release_versions(
            self.interval,
            ("2.8.4", "2.7", "2.8.3", "2.8"),
        )

        self.assertIsInstance(result, OrderedCrossedReleaseVersions)
        assert isinstance(result, OrderedCrossedReleaseVersions)
        self.assertEqual(
            result.ordered_raw_versions,
            ("2.7", "2.8", "2.8.3", "2.8.4"),
        )
        self.assertEqual(
            result.ordered_versions,
            (
                Version("2.7"),
                Version("2.8"),
                Version("2.8.3"),
                Version("2.8.4"),
            ),
        )
        self.assertEqual(
            tuple(zip(result.ordered_raw_versions, result.ordered_versions)),
            (
                ("2.7", Version("2.7")),
                ("2.8", Version("2.8")),
                ("2.8.3", Version("2.8.3")),
                ("2.8.4", Version("2.8.4")),
            ),
        )

    def test_old_bound_is_excluded(self) -> None:
        result = order_crossed_release_versions(
            self.interval,
            ("2.6", "2.7", "2.8.4"),
        )

        self.assertIsInstance(result, PackagingVersionProblem)
        assert isinstance(result, PackagingVersionProblem)
        self.assertEqual(result.state, "crossed_release_outside_interval")
        self.assertEqual(result.release_version, "2.6")

    def test_release_before_old_bound_is_rejected(self) -> None:
        result = order_crossed_release_versions(
            self.interval,
            ("2.5", "2.7", "2.8.4"),
        )

        self.assertIsInstance(result, PackagingVersionProblem)
        assert isinstance(result, PackagingVersionProblem)
        self.assertEqual(result.state, "crossed_release_outside_interval")
        self.assertEqual(result.release_version, "2.5")

    def test_release_after_proposed_bound_is_rejected(self) -> None:
        result = order_crossed_release_versions(
            self.interval,
            ("2.7", "2.8.4", "2.9"),
        )

        self.assertIsInstance(result, PackagingVersionProblem)
        assert isinstance(result, PackagingVersionProblem)
        self.assertEqual(result.state, "crossed_release_outside_interval")
        self.assertEqual(result.release_version, "2.9")

    def test_invalid_crossed_release_is_explicit(self) -> None:
        result = order_crossed_release_versions(
            self.interval,
            ("2.7", "not-a-version", "2.8.4"),
        )

        self.assertIsInstance(result, PackagingVersionProblem)
        assert isinstance(result, PackagingVersionProblem)
        self.assertEqual(result.state, "invalid_crossed_release_version")
        self.assertEqual(result.release_version, "not-a-version")

    def test_pep440_equivalent_crossed_release_identities_are_rejected(self) -> None:
        result = order_crossed_release_versions(
            self.interval,
            ("2.7", "2.8", "2.8.0", "2.8.4"),
        )

        self.assertIsInstance(result, PackagingVersionProblem)
        assert isinstance(result, PackagingVersionProblem)
        self.assertEqual(result.state, "equivalent_crossed_release_versions")

    def test_exact_raw_proposed_release_is_required(self) -> None:
        result = order_crossed_release_versions(
            self.interval,
            ("2.7", "2.8", "2.8.4.0"),
        )

        self.assertIsInstance(result, PackagingVersionProblem)
        assert isinstance(result, PackagingVersionProblem)
        self.assertEqual(result.state, "proposed_release_missing")


if __name__ == "__main__":
    unittest.main()
