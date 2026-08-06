from __future__ import annotations

import unittest

from upgradepilot.package_identity import normalize_package_name
from upgradepilot.repository_path import repository_relative_parts


class PackageIdentityTests(unittest.TestCase):
    def test_pep503_normalization_collapses_separator_runs_and_case(self) -> None:
        self.assertEqual(normalize_package_name("Foo._-BAR"), "foo-bar")

    def test_normalization_preserves_non_separator_text(self) -> None:
        self.assertEqual(normalize_package_name("zope.interface"), "zope-interface")


class RepositoryPathTests(unittest.TestCase):
    def test_valid_repository_relative_path_preserves_components(self) -> None:
        self.assertEqual(
            repository_relative_parts("docs/src/CHANGELOG.md"),
            ("docs", "src", "CHANGELOG.md"),
        )

    def test_rejects_absolute_backslash_empty_and_traversal_paths(self) -> None:
        invalid = (
            "",
            "/requirements.txt",
            "dir\\requirements.txt",
            "dir//requirements.txt",
            "./requirements.txt",
            "dir/../requirements.txt",
        )
        for path in invalid:
            with self.subTest(path=path):
                self.assertIsNone(repository_relative_parts(path))


if __name__ == "__main__":
    unittest.main()
