"""Protect universal-lock marker boundaries in uv membership reasoning."""

from __future__ import annotations

import unittest

from upgradepilot.dependency.change import DependencyChangeSourceEvidence
from upgradepilot.dependency.environment import UvLockDependencyContext
from upgradepilot.dependency.environment_selection import (
    DependencyGroupSelector,
    ProjectEnvironmentSelectionDeclaration,
)
from upgradepilot.dependency.uv_membership import evaluate_uv_selected_environment_membership
from upgradepilot.github.repository import RepositoryTextFile

_REPOSITORY = "example/project"
_REVISION = "a" * 40


def _file(path: str, content: str) -> RepositoryTextFile:
    """Build strong exact text evidence without provider transport metadata."""

    return RepositoryTextFile(
        repository=_REPOSITORY,
        path=path,
        revision=_REVISION,
        content=content,
    )


class UvUniversalLockBoundaryTests(unittest.TestCase):
    def test_resolution_scoped_package_cannot_prove_unconditional_membership(self) -> None:
        project = _file(
            "pyproject.toml",
            '''[project]
name = "demo"
[dependency-groups]
docs = ["conditional-package"]
''',
        )
        lock = _file(
            "uv.lock",
            '''version = 1
revision = 3
[[package]]
name = "demo"
source = { editable = "." }
[package.dev-dependencies]
docs = [{ name = "conditional-package" }]
[[package]]
name = "conditional-package"
version = "1.0"
source = { registry = "https://pypi.org/simple" }
resolution-markers = ["python_full_version >= '3.12'"]
''',
        )
        context = UvLockDependencyContext(
            repository=_REPOSITORY,
            revision=_REVISION,
            normalized_package="conditional-package",
            source_evidence=DependencyChangeSourceEvidence(
                path="uv.lock",
                file_format="uv_lock",
                extraction_method="exact_base_head_files",
            ),
        )
        declaration = ProjectEnvironmentSelectionDeclaration(
            manager="uv",
            operation="sync",
            segment_index=0,
            project_root=None,
            selectors=(DependencyGroupSelector("docs"),),
        )

        result = evaluate_uv_selected_environment_membership(
            context,
            declaration,
            project_file=project,
            lock_file=lock,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(
            result.reason,
            "uv_membership_conditional_or_forked_path_unresolved",
        )


if __name__ == "__main__":
    unittest.main()
