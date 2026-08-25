"""R6 transfer regression for project-source environment evidence (S011 shape)."""

from __future__ import annotations

import unittest

from upgradepilot.ci.workflow_commands import (
    WorkflowProjectEnvironmentSource,
    derive_project_environment_consumptions,
)
from upgradepilot.dependency.change import DependencyChangeSourceEvidence
from upgradepilot.dependency.environment import PyprojectOptionalExtraDependencyContext
from upgradepilot.github.repository import RepositoryTextFile

_REPOSITORY = "example/project"
_HEAD_SHA = "a" * 40


class R6ProjectSourceWorkflowIntegrationTests(unittest.TestCase):
    def test_s011_dev_selection_does_not_become_mlx_consumption_without_prebuilt_membership(self) -> None:
        workflow = RepositoryTextFile(
            repository=_REPOSITORY,
            path=".github/workflows/test.yml",
            revision=_HEAD_SHA,
            content='''name: test
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: pip install -e ".[dev]"
      - run: pytest
''',
        )
        project = RepositoryTextFile(
            repository=_REPOSITORY,
            path="pyproject.toml",
            revision=_HEAD_SHA,
            content='''[project.optional-dependencies]
mlx = ["numpy"]
dev = ["pytest"]
''',
        )
        evidence = DependencyChangeSourceEvidence(
            path="pyproject.toml",
            file_format="pyproject_optional_extra",
            extraction_method="exact_base_head_files",
        )
        context = PyprojectOptionalExtraDependencyContext(
            repository=_REPOSITORY,
            revision=_HEAD_SHA,
            normalized_package="numpy",
            source_evidence=evidence,
            extra="mlx",
        )

        consumptions = derive_project_environment_consumptions(
            workflow,
            sources=(
                WorkflowProjectEnvironmentSource(
                    context=context,
                    project_file=project,
                ),
            ),
            normalized_package="numpy",
        )

        self.assertEqual(len(consumptions), 1)
        consumption = consumptions[0]
        self.assertEqual(consumption.command, 'pip install -e ".[dev]"')
        self.assertEqual(consumption.state, "not_established")
        self.assertEqual(
            consumption.reason,
            "selected_environment_membership_not_established",
        )
        self.assertEqual(consumption.source_path, "pyproject.toml")
        self.assertEqual(consumption.witness_path, ())


if __name__ == "__main__":
    unittest.main()
