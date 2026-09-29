from __future__ import annotations

import unittest

from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.workflow_definition import (
    RunStepDefinition,
    StepsJobDefinition,
    WorkflowDefinition,
    parse_workflow_definition,
)
from upgradepilot.github.workflow_environment import observe_workflow_environment_value


def _workflow(content: str) -> tuple[WorkflowDefinition, StepsJobDefinition, RunStepDefinition]:
    source = RepositoryTextFile(
        repository="example/project",
        path=".github/workflows/ci.yml",
        revision="a" * 40,
        content=content.lstrip(),
    )
    workflow = parse_workflow_definition(source)
    assert isinstance(workflow, WorkflowDefinition)
    job = workflow.jobs[0]
    assert isinstance(job, StepsJobDefinition)
    step = job.steps[0]
    assert isinstance(step, RunStepDefinition)
    return workflow, job, step


class WorkflowEnvironmentValueTests(unittest.TestCase):
    def test_step_literal_wins_over_job_and_workflow_declarations(self) -> None:
        workflow, job, step = _workflow(
            """
env:
  MODE: workflow
jobs:
  test:
    runs-on: ubuntu-latest
    env:
      MODE: job
    steps:
      - env:
          MODE: step
        run: echo ok
"""
        )

        result = observe_workflow_environment_value(workflow, job, step, "MODE")

        self.assertEqual(result.state, "established")
        self.assertEqual(result.value, "step")
        self.assertEqual(result.source_scope, "step")
        self.assertEqual(
            [(item.scope, item.disposition) for item in result.inspected_scopes],
            [("step", "decisive")],
        )

    def test_dynamic_step_value_blocks_literal_lower_scopes(self) -> None:
        workflow, job, step = _workflow(
            """
env:
  MODE: workflow
jobs:
  test:
    runs-on: ubuntu-latest
    env:
      MODE: job
    steps:
      - env:
          MODE: ${{ matrix.mode }}
        run: echo ok
"""
        )

        result = observe_workflow_environment_value(workflow, job, step, "MODE")

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.source_scope, "step")
        self.assertEqual(result.reason, "environment_variable_value_dynamic")
        self.assertEqual(len(result.inspected_scopes), 1)

    def test_job_literal_is_selected_only_after_step_non_declaration(self) -> None:
        workflow, job, step = _workflow(
            """
env:
  MODE: workflow
jobs:
  test:
    runs-on: ubuntu-latest
    env:
      MODE: job
    steps:
      - env:
          OTHER: step
        run: echo ok
"""
        )

        result = observe_workflow_environment_value(workflow, job, step, "MODE")

        self.assertEqual(result.state, "established")
        self.assertEqual(result.value, "job")
        self.assertEqual(result.source_scope, "job")
        self.assertEqual(
            [(item.scope, item.disposition) for item in result.inspected_scopes],
            [("step", "not_declared"), ("job", "decisive")],
        )

    def test_no_declaration_does_not_claim_process_absence(self) -> None:
        workflow, job, step = _workflow(
            """
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: echo ok
"""
        )

        result = observe_workflow_environment_value(
            workflow,
            job,
            step,
            "PIP_DRY_RUN",
        )

        self.assertEqual(result.state, "not_declared")
        self.assertIsNone(result.value)
        self.assertIsNone(result.source_scope)
        self.assertEqual(
            [item.scope for item in result.inspected_scopes],
            ["step", "job", "workflow"],
        )
        self.assertIn("does not establish absence", result.detail)


if __name__ == "__main__":
    unittest.main()
