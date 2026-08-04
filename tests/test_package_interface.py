"""Protect the intentionally small UpgradePilot package-root surface."""

from __future__ import annotations

import unittest

import upgradepilot


class PackageInterfaceTests(unittest.TestCase):
    def test_package_import_has_no_accidental_public_facade(self) -> None:
        self.assertEqual(upgradepilot.__all__, ())

    def test_internal_contracts_are_imported_from_owning_modules(self) -> None:
        from upgradepilot.dependency.change import DependencyVersionChange
        from upgradepilot.github.changelog import GitHubChangelogPathClient
        from upgradepilot.github.pull_request import GitHubPullRequestClient
        from upgradepilot.target.relevance import evaluate_target_python_relevance
        from upgradepilot.upstream.claim import validate_support_drop_candidates

        self.assertIsNotNone(DependencyVersionChange)
        self.assertIsNotNone(GitHubChangelogPathClient)
        self.assertIsNotNone(GitHubPullRequestClient)
        self.assertIsNotNone(evaluate_target_python_relevance)
        self.assertIsNotNone(validate_support_drop_candidates)

    def test_removed_legacy_dependency_symbols_are_not_package_attributes(self) -> None:
        for name in (
            "PinnedDependencyChange",
            "UnsupportedDependencyChange",
            "DependencyChangeResult",
            "extract_pinned_dependency_change",
        ):
            with self.subTest(name=name):
                self.assertFalse(hasattr(upgradepilot, name))


if __name__ == "__main__":
    unittest.main()
