from __future__ import annotations

import unittest

from upgradepilot.ci.dependency_exercise import (
    WorkflowDependencyCoverageInput,
    evaluate_dependency_ci_coverage,
)
from upgradepilot.dependency.change import (
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.dependency.environment import RequirementsFileDependencyContext
from upgradepilot.github.actions import WorkflowJob, WorkflowRun, WorkflowStep
from upgradepilot.github.repository import RepositoryTextFile

_REPOSITORY = "example/project"
_HEAD_SHA = "a" * 40
_WORKFLOW_PATH = ".github/workflows/ci.yml"


def _dependency_and_contexts() -> tuple[
    DependencyVersionChange,
    tuple[RequirementsFileDependencyContext, ...],
]:
    evidence = DependencyChangeSourceEvidence(
        path="requirements-dev.txt",
        file_format="exact_requirement",
        extraction_method="changed_file_patch",
    )
    dependency = DependencyVersionChange(
        package="pytest",
        normalized_package="pytest",
        old_version="9.0.2",
        proposed_version="9.0.3",
        source_evidence=(evidence,),
    )
    context = RequirementsFileDependencyContext(
        repository=_REPOSITORY,
        revision=_HEAD_SHA,
        normalized_package="pytest",
        source_evidence=evidence,
    )
    return dependency, (context,)


def _run() -> WorkflowRun:
    return WorkflowRun(
        run_id=1001,
        workflow_id=2001,
        name="CI",
        event="pull_request",
        head_sha=_HEAD_SHA,
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


def _job(
    steps: tuple[WorkflowStep, ...],
    *,
    name: str = "Tests",
) -> WorkflowJob:
    return WorkflowJob(
        job_id=3001,
        run_id=1001,
        name=name,
        head_sha=_HEAD_SHA,
        status="completed",
        conclusion="success",
        steps=steps,
    )


def _input(
    workflow: str,
    steps: tuple[WorkflowStep, ...],
    *,
    runtime_job_name: str = "Tests",
) -> WorkflowDependencyCoverageInput:
    return WorkflowDependencyCoverageInput(
        run=_run(),
        jobs=(_job(steps, name=runtime_job_name),),
        definition=RepositoryTextFile(
            repository=_REPOSITORY,
            path=_WORKFLOW_PATH,
            revision=_HEAD_SHA,
            content=workflow.lstrip(),
        ),
    )


class RuntimeCorrelatedDependencyCoverageTests(unittest.TestCase):
    def test_successful_consuming_step_strengthens_coverage_to_runtime_correlated(self) -> None:
        dependency, contexts = _dependency_and_contexts()
        workflow = """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4
      - name: Install test dependencies
        run: pip install -r requirements-dev.txt
"""

        result = evaluate_dependency_ci_coverage(
            dependency,
            (
                _input(
                    workflow,
                    (
                        _step(1, "Set up job"),
                        _step(2, "Check out repository"),
                        _step(4, "Install test dependencies"),
                        _step(9, "Post Check out repository"),
                        _step(10, "Complete job"),
                    ),
                ),
            ),
            source_contexts=contexts,
        )

        self.assertEqual(result.state, "supported_runtime_correlated")
        workflow_result = result.workflows[0]
        self.assertEqual(workflow_result.state, "supported_runtime_correlated")
        self.assertEqual(workflow_result.consumption_state, "supported")
        self.assertEqual(workflow_result.runtime_consumption_state, "supported")
        self.assertEqual(workflow_result.direct_exercise_state, "not_established")
        self.assertEqual(
            workflow_result.runtime_direct_exercise_state,
            "not_established",
        )
        self.assertIsNotNone(workflow_result.runtime_correlation)
        assert workflow_result.runtime_correlation is not None
        self.assertEqual(workflow_result.runtime_correlation.state, "correlated")

    def test_direct_exercise_axis_is_separately_runtime_correlated(self) -> None:
        dependency, contexts = _dependency_and_contexts()
        workflow = """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4
      - name: Install test dependencies
        run: pip install -r requirements-dev.txt
      - name: Exercise pytest
        run: pytest tests
"""

        result = evaluate_dependency_ci_coverage(
            dependency,
            (
                _input(
                    workflow,
                    (
                        _step(1, "Set up job"),
                        _step(2, "Check out repository"),
                        _step(3, "Install test dependencies"),
                        _step(4, "Exercise pytest"),
                        _step(9, "Post Check out repository"),
                        _step(10, "Complete job"),
                    ),
                ),
            ),
            source_contexts=contexts,
        )

        workflow_result = result.workflows[0]
        self.assertEqual(result.state, "supported_runtime_correlated")
        self.assertEqual(workflow_result.direct_exercise_state, "supported")
        self.assertEqual(workflow_result.runtime_direct_exercise_state, "supported")

    def test_correlated_skipped_consuming_step_does_not_become_positive_execution(self) -> None:
        dependency, contexts = _dependency_and_contexts()
        workflow = """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4
      - name: Install test dependencies
        if: ${{ false }}
        run: pip install -r requirements-dev.txt
"""

        result = evaluate_dependency_ci_coverage(
            dependency,
            (
                _input(
                    workflow,
                    (
                        _step(1, "Set up job"),
                        _step(2, "Check out repository"),
                        _step(
                            3,
                            "Install test dependencies",
                            conclusion="skipped",
                        ),
                        _step(8, "Post Check out repository"),
                        _step(9, "Complete job"),
                    ),
                ),
            ),
            source_contexts=contexts,
        )

        workflow_result = result.workflows[0]
        self.assertEqual(result.state, "unresolved")
        self.assertEqual(
            result.reason,
            "correlated_dependency_consumption_execution_not_successful",
        )
        self.assertEqual(workflow_result.runtime_consumption_state, "not_established")
        self.assertEqual(workflow_result.runtime_correlation.state, "correlated")

    def test_continue_on_error_success_is_not_treated_as_unmasked_success(self) -> None:
        dependency, contexts = _dependency_and_contexts()
        workflow = """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4
      - name: Install test dependencies
        continue-on-error: true
        run: pip install -r requirements-dev.txt
"""

        result = evaluate_dependency_ci_coverage(
            dependency,
            (
                _input(
                    workflow,
                    (
                        _step(1, "Set up job"),
                        _step(2, "Check out repository"),
                        _step(3, "Install test dependencies"),
                        _step(8, "Post Check out repository"),
                        _step(9, "Complete job"),
                    ),
                ),
            ),
            source_contexts=contexts,
        )

        workflow_result = result.workflows[0]
        self.assertEqual(result.state, "unresolved")
        self.assertEqual(
            result.reason,
            "correlated_dependency_consumption_execution_unresolved",
        )
        self.assertEqual(workflow_result.runtime_consumption_state, "unresolved")
        self.assertIn("continue-on-error", workflow_result.runtime_consumption_detail)

    def test_unbridgeable_static_shape_preserves_supported_not_correlated_fallback(self) -> None:
        dependency, contexts = _dependency_and_contexts()
        workflow = """
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements-dev.txt
"""

        result = evaluate_dependency_ci_coverage(
            dependency,
            (
                _input(
                    workflow,
                    (),
                    runtime_job_name="test",
                ),
            ),
            source_contexts=contexts,
        )

        workflow_result = result.workflows[0]
        self.assertEqual(result.state, "supported_not_correlated")
        self.assertEqual(workflow_result.consumption_state, "supported")
        self.assertEqual(workflow_result.runtime_consumption_state, "unresolved")
        self.assertIsNotNone(workflow_result.runtime_correlation)
        assert workflow_result.runtime_correlation is not None
        self.assertEqual(
            workflow_result.runtime_correlation.reason,
            "static_job_name_missing",
        )


if __name__ == "__main__":
    unittest.main()
