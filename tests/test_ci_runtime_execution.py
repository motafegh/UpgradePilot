from __future__ import annotations

import unittest

from upgradepilot.ci.runtime_execution import (
    assess_correlated_step_execution,
    assess_exact_command_execution,
)
from upgradepilot.ci.runtime_strengthening import RuntimeStrengtheningCandidate
from upgradepilot.ci.workflow_runtime_correlation import correlate_workflow_runtime
from upgradepilot.github.actions import WorkflowJob, WorkflowRun, WorkflowStep
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.workflow_command_analysis import CommandSourceSpan
from upgradepilot.github.workflow_command_location import StaticCommandLocation


_REPOSITORY = "example/project"
_REVISION = "a" * 40
_PATH = ".github/workflows/ci.yml"


def _source(content: str) -> RepositoryTextFile:
    return RepositoryTextFile(
        repository=_REPOSITORY,
        path=_PATH,
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


def _step(
    number: int,
    name: str,
    *,
    status: str = "completed",
    conclusion: str | None = "success",
) -> WorkflowStep:
    return WorkflowStep(
        number=number,
        name=name,
        status=status,
        conclusion=conclusion,
    )


def _job(steps: tuple[WorkflowStep, ...]) -> WorkflowJob:
    return WorkflowJob(
        job_id=3001,
        run_id=1001,
        name="Tests",
        head_sha=_REVISION,
        status="completed",
        conclusion="success",
        steps=steps,
    )


def _location(source_order: int = 0) -> StaticCommandLocation:
    return StaticCommandLocation(
        source_span=CommandSourceSpan(
            start_byte=0,
            end_byte=10,
            start_line=0,
            start_column=0,
            end_line=0,
            end_column=10,
        ),
        source_order=source_order,
    )


def _candidate(
    *,
    step_source_index: int = 0,
    structural_context: tuple[str, ...] = ("straightforward_top_level",),
    whole_step_relation: str | None = "sole_ordinary_top_level_command",
) -> RuntimeStrengtheningCandidate:
    return RuntimeStrengtheningCandidate(
        proposition_kind="dependency_consumption",
        workflow_path=_PATH,
        workflow_revision=_REVISION,
        job_key="test",
        step_source_index=step_source_index,
        command_location=_location(),
        structural_context=structural_context,  # type: ignore[arg-type]
        whole_step_relation=whole_step_relation,  # type: ignore[arg-type]
        execution_profile="github_builtin_bash",
    )


class CorrelatedStepExecutionTests(unittest.TestCase):
    def test_run_and_uses_steps_share_unmasked_success_interpretation(self) -> None:
        correlation = correlate_workflow_runtime(
            _source(
                """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/setup-python@v6
      - run: python -m unittest
"""
            ),
            _run(),
            (
                _job(
                    (
                        _step(1, "Run actions/setup-python@v6"),
                        _step(2, "Run python -m unittest"),
                    )
                ),
            ),
        )

        self.assertEqual(correlation.state, "correlated")
        self.assertEqual(
            [assess_correlated_step_execution(item).state for item in correlation.jobs[0].steps],
            ["supported", "supported"],
        )

    def test_continue_on_error_prevents_positive_step_interpretation(self) -> None:
        correlation = correlate_workflow_runtime(
            _source(
                """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Allowed failure
        continue-on-error: true
        run: python -m unittest
"""
            ),
            _run(),
            (_job((_step(1, "Allowed failure"),)),),
        )

        assessment = assess_correlated_step_execution(correlation.jobs[0].steps[0])

        self.assertEqual(assessment.state, "unresolved")
        self.assertEqual(assessment.basis, "continue_on_error_unresolved")

    def test_failed_runtime_step_is_factual_not_established(self) -> None:
        correlation = correlate_workflow_runtime(
            _source(
                """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Run tests
        run: python -m unittest
"""
            ),
            _run(),
            (_job((_step(1, "Run tests", conclusion="failure"),)),),
        )

        assessment = assess_correlated_step_execution(correlation.jobs[0].steps[0])

        self.assertEqual(assessment.state, "not_established")
        self.assertEqual(assessment.basis, "runtime_non_success")
        self.assertEqual(assessment.correlation.runtime_step.conclusion, "failure")


class ExactCommandExecutionTests(unittest.TestCase):
    def test_sole_eligible_command_in_successful_step_is_supported(self) -> None:
        correlation = correlate_workflow_runtime(
            _source(
                """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Install
        run: pip install -r requirements.txt
"""
            ),
            _run(),
            (_job((_step(1, "Install"),)),),
        )

        assessment = assess_exact_command_execution(
            _candidate(),
            correlation=correlation,
        )

        self.assertEqual(assessment.state, "supported")
        self.assertEqual(assessment.basis, "supported")
        self.assertEqual(assessment.runtime_step_number, 1)

    def test_ineligible_command_does_not_inherit_successful_step(self) -> None:
        correlation = correlate_workflow_runtime(
            _source(
                """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Conditional install
        run: |
          if false; then
            pip install -r requirements.txt
          fi
"""
            ),
            _run(),
            (_job((_step(1, "Conditional install"),)),),
        )

        assessment = assess_exact_command_execution(
            _candidate(
                structural_context=("conditional",),
                whole_step_relation=None,
            ),
            correlation=correlation,
        )

        self.assertEqual(assessment.state, "not_established")
        self.assertEqual(assessment.basis, "eligibility_ineligible")

    def test_unresolved_later_command_remains_unresolved_after_step_success(self) -> None:
        correlation = correlate_workflow_runtime(
            _source(
                """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Install then report
        run: |
          echo ready
          pip install -r requirements.txt
"""
            ),
            _run(),
            (_job((_step(1, "Install then report"),)),),
        )

        assessment = assess_exact_command_execution(
            _candidate(
                structural_context=("linear_chain",),
                whole_step_relation=None,
            ),
            correlation=correlation,
        )

        self.assertEqual(assessment.state, "unresolved")
        self.assertEqual(assessment.basis, "eligibility_unresolved")


if __name__ == "__main__":
    unittest.main()
