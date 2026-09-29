from __future__ import annotations

import unittest

from upgradepilot.ci.executable_selection import establish_executable_selection
from upgradepilot.ci.workflow_runtime_correlation import correlate_workflow_runtime
from upgradepilot.github.actions import WorkflowJob, WorkflowRun, WorkflowStep
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.workflow_command_analysis import analyze_run_step_commands
from upgradepilot.github.workflow_definition import (
    RunStepDefinition,
    StepsJobDefinition,
    WorkflowDefinition,
    parse_workflow_definition,
)


_REVISION = "a" * 40


def _source(content: str) -> RepositoryTextFile:
    return RepositoryTextFile(
        repository="example/project",
        path=".github/workflows/ci.yml",
        revision=_REVISION,
        content=content.lstrip(),
    )


def _run() -> WorkflowRun:
    return WorkflowRun(
        run_id=1001,
        workflow_id=2001,
        name="CI",
        event="pull_request",
        head_sha=_REVISION,
        status="completed",
        conclusion="success",
        run_attempt=1,
    )


def _runtime_step(
    number: int,
    name: str,
    *,
    conclusion: str = "success",
) -> WorkflowStep:
    return WorkflowStep(
        number=number,
        name=name,
        status="completed",
        conclusion=conclusion,
    )


def _runtime_job(*steps: WorkflowStep) -> WorkflowJob:
    return WorkflowJob(
        job_id=3001,
        run_id=1001,
        name="Tests",
        head_sha=_REVISION,
        status="completed",
        conclusion="success",
        steps=steps,
    )


def _static(
    source: RepositoryTextFile,
) -> tuple[WorkflowDefinition, StepsJobDefinition, RunStepDefinition]:
    workflow = parse_workflow_definition(source)
    assert isinstance(workflow, WorkflowDefinition)
    job = workflow.jobs[0]
    assert isinstance(job, StepsJobDefinition)
    run_steps = tuple(
        step for step in job.steps if isinstance(step, RunStepDefinition)
    )
    assert run_steps
    return workflow, job, run_steps[-1]


def _python_occurrence(
    workflow: WorkflowDefinition,
    job: StepsJobDefinition,
    step: RunStepDefinition,
):
    analysis = analyze_run_step_commands(workflow, job, step)
    assert analysis.state == "analyzable"
    matches = tuple(
        item
        for item in analysis.command_occurrences
        if item.executable.literal_value in {
            "python",
            "./.venv/bin/python",
        }
    )
    assert len(matches) == 1
    return matches[0]


class ExecutableSelectionEvidenceTests(unittest.TestCase):
    def test_explicit_path_needs_no_path_provenance(self) -> None:
        source = _source(
            """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Install
        run: ./.venv/bin/python -m pip install demo
"""
        )
        workflow, job, step = _static(source)
        occurrence = _python_occurrence(workflow, job, step)

        result = establish_executable_selection(
            workflow,
            job,
            step,
            occurrence,
        )

        self.assertEqual(result.state, "established")
        self.assertEqual(result.source, "explicit_path")
        self.assertEqual(result.environment_reference, "./.venv/bin/python")

    def test_successful_adjacent_setup_python_establishes_bare_python_relation(self) -> None:
        source = _source(
            """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"
      - name: Install
        run: python -m pip install demo
"""
        )
        workflow, job, step = _static(source)
        occurrence = _python_occurrence(workflow, job, step)
        correlation = correlate_workflow_runtime(
            source,
            _run(),
            (
                _runtime_job(
                    _runtime_step(1, "Set up Python"),
                    _runtime_step(2, "Install"),
                ),
            ),
        )

        result = establish_executable_selection(
            workflow,
            job,
            step,
            occurrence,
            correlation=correlation,
        )

        self.assertEqual(result.state, "established")
        self.assertEqual(result.source, "setup_python_path")
        self.assertEqual(result.executable, "python")
        self.assertEqual(result.provider_step_source_index, 0)
        assert result.environment_reference is not None
        self.assertIn("actions/setup-python@v6", result.environment_reference)

    def test_setup_python_update_environment_false_does_not_establish_path(self) -> None:
        source = _source(
            """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"
          update-environment: false
      - name: Install
        run: python -m pip install demo
"""
        )
        workflow, job, step = _static(source)
        occurrence = _python_occurrence(workflow, job, step)
        correlation = correlate_workflow_runtime(
            source,
            _run(),
            (
                _runtime_job(
                    _runtime_step(1, "Set up Python"),
                    _runtime_step(2, "Install"),
                ),
            ),
        )

        result = establish_executable_selection(
            workflow,
            job,
            step,
            occurrence,
            correlation=correlation,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(
            result.reason,
            "setup_python_update_environment_disabled",
        )

    def test_failed_setup_python_runtime_step_does_not_establish_path(self) -> None:
        source = _source(
            """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Set up Python
        uses: actions/setup-python@v6
      - name: Install
        run: python -m pip install demo
"""
        )
        workflow, job, step = _static(source)
        occurrence = _python_occurrence(workflow, job, step)
        correlation = correlate_workflow_runtime(
            source,
            _run(),
            (
                _runtime_job(
                    _runtime_step(1, "Set up Python", conclusion="failure"),
                    _runtime_step(2, "Install"),
                ),
            ),
        )

        result = establish_executable_selection(
            workflow,
            job,
            step,
            occurrence,
            correlation=correlation,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(
            result.reason,
            "setup_python_runtime_execution_not_supported",
        )

    def test_intervening_user_step_prevents_first_setup_python_path_relation(self) -> None:
        source = _source(
            """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Set up Python
        uses: actions/setup-python@v6
      - name: Other
        run: echo other
      - name: Install
        run: python -m pip install demo
"""
        )
        workflow, job, step = _static(source)
        occurrence = _python_occurrence(workflow, job, step)

        result = establish_executable_selection(
            workflow,
            job,
            step,
            occurrence,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(
            result.reason,
            "setup_python_adjacent_predecessor_missing",
        )

    def test_command_local_path_assignment_supersedes_setup_python_relation(self) -> None:
        source = _source(
            """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Set up Python
        uses: actions/setup-python@v6
      - name: Install
        run: PATH=/other/bin python -m pip install demo
"""
        )
        workflow, job, step = _static(source)
        occurrence = _python_occurrence(workflow, job, step)

        result = establish_executable_selection(
            workflow,
            job,
            step,
            occurrence,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "command_local_path_override")

    def test_prior_command_in_same_step_keeps_bare_python_unresolved(self) -> None:
        source = _source(
            """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Set up Python
        uses: actions/setup-python@v6
      - name: Install
        run: |
          source .venv/bin/activate
          python -m pip install demo
"""
        )
        workflow, job, step = _static(source)
        occurrence = _python_occurrence(workflow, job, step)

        result = establish_executable_selection(
            workflow,
            job,
            step,
            occurrence,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "bare_python_not_first_process_in_step")


if __name__ == "__main__":
    unittest.main()
