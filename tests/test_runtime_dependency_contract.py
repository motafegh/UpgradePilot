"""Protect deliberate runtime dependency bounds recorded by architecture decisions."""

from __future__ import annotations

import tomllib
import unittest
from importlib.metadata import version
from pathlib import Path

from packaging.version import Version


class RuntimeDependencyContractTests(unittest.TestCase):
    def test_packaging_dependency_uses_the_accepted_26x_bound(self) -> None:
        repository_root = Path(__file__).resolve().parents[1]
        document = tomllib.loads(
            (repository_root / "pyproject.toml").read_text(encoding="utf-8")
        )

        self.assertEqual(
            document["project"]["dependencies"],
            [
                "requests>=2.32,<3",
                "packaging>=26.2,<27",
            ],
        )

    def test_installed_packaging_version_satisfies_the_accepted_bound(self) -> None:
        installed = Version(version("packaging"))

        self.assertGreaterEqual(installed, Version("26.2"))
        self.assertLess(installed, Version("27"))


if __name__ == "__main__":
    unittest.main()
