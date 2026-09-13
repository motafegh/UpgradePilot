"""Protect deliberate runtime dependency bounds recorded by architecture decisions."""

from __future__ import annotations

import tomllib
import unittest
from importlib.metadata import version
from pathlib import Path

from packaging.version import Version


class RuntimeDependencyContractTests(unittest.TestCase):
    def test_runtime_dependencies_use_the_accepted_bounds(self) -> None:
        repository_root = Path(__file__).resolve().parents[1]
        document = tomllib.loads(
            (repository_root / "pyproject.toml").read_text(encoding="utf-8")
        )

        self.assertEqual(
            document["project"]["dependencies"],
            [
                "requests>=2.32,<3",
                "packaging>=26.2,<27",
                "PyYAML>=6.0.3,<7",
                "tree-sitter==0.25.0",
                "tree-sitter-bash==0.25.1",
                "tree-sitter-pwsh==0.38.1",
                "tree-sitter-batch==0.11.1",
            ],
        )

    def test_installed_packaging_version_satisfies_the_accepted_bound(self) -> None:
        installed = Version(version("packaging"))

        self.assertGreaterEqual(installed, Version("26.2"))
        self.assertLess(installed, Version("27"))

    def test_installed_pyyaml_version_satisfies_the_accepted_bound(self) -> None:
        installed = Version(version("PyYAML"))

        self.assertGreaterEqual(installed, Version("6.0.3"))
        self.assertLess(installed, Version("7"))

    def test_installed_tree_sitter_stack_matches_characterized_versions(self) -> None:
        expected = {
            "tree-sitter": "0.25.0",
            "tree-sitter-bash": "0.25.1",
            "tree-sitter-pwsh": "0.38.1",
            "tree-sitter-batch": "0.11.1",
        }

        self.assertEqual(
            {distribution: version(distribution) for distribution in expected},
            expected,
        )


if __name__ == "__main__":
    unittest.main()
