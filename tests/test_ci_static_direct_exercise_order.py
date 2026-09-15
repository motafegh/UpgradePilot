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
from upgradepilot.github.actions import WorkflowJob, WorkflowRun
from upgradepilot.github.repository import RepositoryTextFile

_HEAD_SHA = "a" * 40
_PATH = ".github/workflows/ci.yml"


def _dependency_and_context() -> tuple[
    DependencyVersionChange,
    tuple[RequirementsFileDependencyContext, ...],
]:
    source_evidence = DependencyChangeSourceEvidence(
        path="requirements-dev.txt",
        file_format="exact_requirement",
        extraction_method="changed_file_patch",
    )
    dependency = DependencyVersionChange(
        package="pytest",
        normalized_package="pytest",
        old_version="9.0.2",
        proposed_version="9.0.3",
        source_evidence=(source_evidence,),
    )
    context = RequirementsFileDependencyContext(
        repository="example/project",
        revision=_HEAD_SHA,
        normalized_package="pytest",
        source_evidence=source_evidence,
    )
    return dependency, (context,)


def _workflow_input(content: str) -> WorkflowDependencyCoverageInput:
    run = WorkflowRun(
        run_id=1001,
        workflow_id=2001,
        name="CI",
        event="pull_request",
        head_sha=_HEAD_SHA,
        status="completed",
        conclusion="success",
        run_attempt=1,
    )
    job = WorkflowJob(
        job_id=3001,
        run_id=1001,
        name="test",
        head_sha=_HEAD_SHA,
        status="completed",
        conclusion="success",
        steps=(),
    )
    definition = RepositoryTextFile(
        repository="example/project",
        path=_PATH,
        revision=_HEAD_SHA,
        content=content,
    )
    return WorkflowDependencyCoverageInput(
        run=run,
        jobs=(job,),
        definition=definition,
    )


class DirectExerciseStaticOrderingTests(unittest.TestCase):
    def test_clean_same_step_linear_order_supports_direct_exercise(self) -> None:
        dependency, contexts = _dependency_and_context()
        workflow = """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: |
          pip install -r requirements-dev.txt
          pytest tests
"""

        result = evaluate_dependency_ci_coverage(
            dependency,
            (_workflow_input(workflow),),
            source_contexts=contexts,
        )

        workflow_result = result.workflows[0]
        self.assertEqual(workflow_result.consumption_state, "supported")
        self.assertEqual(workflow_result.direct_exercise_state, "supported")
        self.assertEqual(
            workflow_result.direct_exercise_reason,
            "direct_package_invocation_after_consumption",
        )

    def test_short_circuit_source_order_is_unresolved_not_supported(self) -> None:
        dependency, contexts = _dependency_and_context()
        workflow = """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements-dev.txt && pytest tests
"""

        result = evaluate_dependency_ci_coverage(
            dependency,
            (_workflow_input(workflow),),
            source_contexts=contexts,
        )

        workflow_result = result.workflows[0]
        self.assertEqual(workflow_result.consumption_state, "supported")
        self.assertEqual(workflow_result.direct_exercise_state, "unresolved")
        self.assertEqual(
            workflow_result.direct_exercise_reason,
            "direct_invocation_order_or_target_unresolved",
        )


if __name__ == "__main__":
    unittest.main()
