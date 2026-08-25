"""R6 pressure: S005 tox-mediated lock use must not become direct uv command evidence."""

from __future__ import annotations

import unittest

from upgradepilot.ci.workflow_commands import (
    WorkflowProjectEnvironmentSource,
    derive_project_environment_consumptions,
)
from upgradepilot.dependency.change import DependencyChangeSourceEvidence
from upgradepilot.dependency.environment import UvLockDependencyContext
from upgradepilot.github.repository import RepositoryTextFile

_REPOSITORY = "PennLINC/ModelArrayIO"
_HEAD_SHA = "b590cfe93fbe49235f0f68d2b87102672f8a0aa0"


class R6S005MediatedUvBoundaryTests(unittest.TestCase):
    def test_tox_latest_command_does_not_manufacture_direct_uv_reachability(self) -> None:
        workflow = RepositoryTextFile(
            repository=_REPOSITORY,
            path=".github/workflows/tests.yml",
            revision=_HEAD_SHA,
            content='''name: tests
jobs:
  py312-latest:
    runs-on: ubuntu-latest
    steps:
      - run: tox -e py312-latest
''',
        )
        project = RepositoryTextFile(
            repository=_REPOSITORY,
            path="pyproject.toml",
            revision=_HEAD_SHA,
            content='''[project.optional-dependencies]
test = ["pytest>=8", "pytest-cov>=5", "pytest-xdist>=3", "pytest-env>=1.0"]
''',
        )
        lock = RepositoryTextFile(
            repository=_REPOSITORY,
            path="uv.lock",
            revision=_HEAD_SHA,
            content='''version = 1
revision = 3
[[package]]
name = "modelarrayio"
source = { editable = "." }
[package.optional-dependencies]
test = [{ name = "pytest" }]
[[package]]
name = "pytest"
version = "9.1.1"
source = { registry = "https://pypi.org/simple" }
''',
        )
        evidence = DependencyChangeSourceEvidence(
            path="uv.lock",
            file_format="uv_lock",
            extraction_method="exact_base_head_files",
        )
        source = WorkflowProjectEnvironmentSource(
            context=UvLockDependencyContext(
                repository=_REPOSITORY,
                revision=_HEAD_SHA,
                normalized_package="pytest",
                source_evidence=evidence,
            ),
            project_file=project,
            lock_file=lock,
        )

        consumptions = derive_project_environment_consumptions(
            workflow,
            sources=(source,),
            normalized_package="pytest",
        )

        self.assertEqual(consumptions, ())
        # S005's real evidence is mediated by tox's uv-venv-lock-runner. Supporting that
        # proposition requires a separate tox/runner owner; R4 must not infer it from a tox
        # command as though the workflow had directly selected uv roots.


if __name__ == "__main__":
    unittest.main()
