"""Prove the Cycle 2 single-traversal static workflow evidence seam."""

from __future__ import annotations

import unittest
from unittest.mock import patch

from upgradepilot.ci.workflow_commands import (
    WorkflowProjectEnvironmentSource,
    inspect_workflow_dependency_evidence,
)
from upgradepilot.dependency.change import DependencyChangeSourceEvidence
from upgradepilot.dependency.environment import PyprojectOptionalExtraDependencyContext
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.workflow_command_analysis import analyze_run_step_commands

_REPOSITORY = "example/project"
_REVISION = "a" * 40
_WORKFLOW_PATH = ".github/workflows/ci.yml"


def _workflow(content: str) -> RepositoryTextFile:
    return RepositoryTextFile(
        repository=_REPOSITORY,
        path=_WORKFLOW_PATH,
        revision=_REVISION,
        content=content,
    )


def _project_source() -> WorkflowProjectEnvironmentSource:
    evidence = DependencyChangeSourceEvidence(
        path="pyproject.toml",
        file_format="pyproject_optional_extra",
        extraction_method="exact_base_head_files",
    )
    context = PyprojectOptionalExtraDependencyContext(
        repository=_REPOSITORY,
        revision=_REVISION,
        normalized_package="demo",
        source_evidence=evidence,
        extra="dev",
    )
    return WorkflowProjectEnvironmentSource(
        context=context,
        project_file=RepositoryTextFile(
            repository=_REPOSITORY,
            path="pyproject.toml",
            revision=_REVISION,
            content='[project]\nname = "example"\n[project.optional-dependencies]\ndev = ["demo==1"]\n',
        ),
    )


class SinglePassWorkflowStaticEvidenceTests(unittest.TestCase):
    def test_project_environment_uses_one_shared_analysis_for_run_step(self) -> None:
        source = _project_source()
        workflow = _workflow(
            """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -e \".[dev]\"
"""
        )

        with patch(
            "upgradepilot.ci.workflow_commands.analyze_run_step_commands",
            wraps=analyze_run_step_commands,
        ) as analyze:
            result = inspect_workflow_dependency_evidence(
                workflow,
                source_contexts=(source.context,),
                package="demo",
                normalized_package="demo",
                project_environment_sources=(source,),
            )

        self.assertEqual(analyze.call_count, 1)
        project_consumptions = tuple(
            item
            for item in result.consumptions
            if item.mechanism == "project_environment"
        )
        self.assertEqual(len(project_consumptions), 1)
        consumption = project_consumptions[0]
        self.assertEqual(consumption.state, "supported")
        self.assertEqual(
            consumption.reason,
            "selected_project_environment_contains_changed_dependency",
        )
        self.assertIsNotNone(consumption.command_location)
        self.assertEqual(result.problems, ())

    def test_project_environment_input_modes_cannot_be_mixed(self) -> None:
        source = _project_source()
        workflow = _workflow(
            """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -e \".[dev]\"
"""
        )

        first = inspect_workflow_dependency_evidence(
            workflow,
            source_contexts=(source.context,),
            package="demo",
            normalized_package="demo",
            project_environment_sources=(source,),
        ).consumptions[0]

        with self.assertRaisesRegex(ValueError, "mutually exclusive"):
            inspect_workflow_dependency_evidence(
                workflow,
                source_contexts=(source.context,),
                package="demo",
                normalized_package="demo",
                project_environment_sources=(source,),
                project_environment_consumptions=(first,),
            )


if __name__ == "__main__":
    unittest.main()
