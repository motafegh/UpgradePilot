"""Test Cluster-5 CI coverage with consumption and direct exercise separated."""

from __future__ import annotations

import unittest

from upgradepilot.ci.consumption import compose_project_environment_consumption
from upgradepilot.ci.dependency_exercise import (
    WorkflowDependencyExerciseInput,
    evaluate_dependency_ci_coverage,
)
from upgradepilot.dependency.change import (
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.dependency.environment import (
    PyprojectOptionalExtraDependencyContext,
    RequirementsFileDependencyContext,
    UvLockDependencyContext,
)
from upgradepilot.dependency.environment_membership import (
    evaluate_project_source_environment_membership,
)
from upgradepilot.dependency.environment_selection import (
    DependencyGroupSelector,
    OptionalExtraSelector,
    ProjectEnvironmentSelectionDeclaration,
    ProjectEnvironmentSelectionObservation,
)
from upgradepilot.dependency.uv_membership import UvSelectedEnvironmentMembership
from upgradepilot.dependency.workflow_context import EffectiveWorkingDirectory
from upgradepilot.github.actions import WorkflowJob, WorkflowRun
from upgradepilot.github.repository import RepositoryTextFile

_REPOSITORY = "example/project"
_HEAD_SHA = "a" * 40
_WORKFLOW_PATH = ".github/workflows/ci.yml"


def _run(
    *,
    run_id: int = 1001,
    name: str = "CI",
    conclusion: str | None = "success",
) -> WorkflowRun:
    return WorkflowRun(
        run_id=run_id,
        workflow_id=2000 + run_id,
        name=name,
        event="pull_request",
        head_sha=_HEAD_SHA,
        status="completed",
        conclusion=conclusion,
        run_attempt=1,
    )


def _job(
    *,
    run_id: int = 1001,
    job_id: int = 3001,
    name: str = "test",
    conclusion: str | None = "success",
) -> WorkflowJob:
    return WorkflowJob(
        job_id=job_id,
        run_id=run_id,
        name=name,
        head_sha=_HEAD_SHA,
        status="completed",
        conclusion=conclusion,
        steps=(),
    )


def _definition(content: str, *, path: str = _WORKFLOW_PATH) -> RepositoryTextFile:
    return RepositoryTextFile(
        repository=_REPOSITORY,
        path=path,
        revision=_HEAD_SHA,
        content=content,
    )


def _input(
    content: str,
    *,
    run: WorkflowRun | None = None,
    jobs: tuple[WorkflowJob, ...] | None = None,
    external_consumptions=(),
    path: str = _WORKFLOW_PATH,
) -> WorkflowDependencyExerciseInput:
    selected_run = run or _run()
    return WorkflowDependencyExerciseInput(
        run=selected_run,
        jobs=jobs if jobs is not None else (_job(run_id=selected_run.run_id),),
        definition=_definition(content, path=path),
        external_consumptions=tuple(external_consumptions),
    )


def _requirement_dependency():
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


def _uv_dependency():
    evidence = DependencyChangeSourceEvidence(
        path="uv.lock",
        file_format="uv_lock",
        extraction_method="exact_base_head_files",
    )
    dependency = DependencyVersionChange(
        package="soupsieve",
        normalized_package="soupsieve",
        old_version="2.6",
        proposed_version="2.8.4",
        source_evidence=(evidence,),
    )
    context = UvLockDependencyContext(
        repository=_REPOSITORY,
        revision=_HEAD_SHA,
        normalized_package="soupsieve",
        source_evidence=evidence,
    )
    return dependency, (context,)


def _root_workdir() -> EffectiveWorkingDirectory:
    return EffectiveWorkingDirectory(
        state="repository_root",
        source="repository_root",
        path=None,
        raw=None,
    )


def _s001_consumption():
    declaration = ProjectEnvironmentSelectionDeclaration(
        manager="uv",
        operation="sync",
        segment_index=0,
        project_root=None,
        selectors=(DependencyGroupSelector("docs"),),
    )
    observation = ProjectEnvironmentSelectionObservation(
        state="observed",
        reason="project_environment_selection_declared",
        detail="docs selected",
        step_source_index=0,
        command="uv sync --group docs",
        project_file_path="pyproject.toml",
        working_directory=_root_workdir(),
        declarations=(declaration,),
    )
    membership = UvSelectedEnvironmentMembership(
        state="member",
        reason="uv_selected_environment_transitive_member",
        detail="Soup Sieve is transitively reachable from docs.",
        normalized_package="soupsieve",
        project_file_path="pyproject.toml",
        lock_file_path="uv.lock",
        selectors=declaration.selectors,
        membership_kind="transitive",
        witness_root="mkdocs-llmstxt",
        witness_path=("mkdocs-llmstxt", "beautifulsoup4", "soupsieve"),
    )
    return compose_project_environment_consumption(
        workflow_path=_WORKFLOW_PATH,
        workflow_revision=_HEAD_SHA,
        job_key="docs",
        observation=observation,
        declaration=declaration,
        membership=membership,
    )


def _s011_context_and_consumption():
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
    declaration = ProjectEnvironmentSelectionDeclaration(
        manager="pip",
        operation="install",
        segment_index=0,
        project_root=None,
        selectors=(OptionalExtraSelector("dev"),),
    )
    observation = ProjectEnvironmentSelectionObservation(
        state="observed",
        reason="project_environment_selection_declared",
        detail="dev selected",
        step_source_index=0,
        command='pip install -e ".[dev]"',
        project_file_path="pyproject.toml",
        working_directory=_root_workdir(),
        declarations=(declaration,),
    )
    membership = evaluate_project_source_environment_membership(context, declaration)
    consumption = compose_project_environment_consumption(
        workflow_path=_WORKFLOW_PATH,
        workflow_revision=_HEAD_SHA,
        job_key="test",
        observation=observation,
        declaration=declaration,
        membership=membership,
    )
    dependency = DependencyVersionChange(
        package="numpy",
        normalized_package="numpy",
        old_version="1.26.4",
        proposed_version="2.4.6",
        source_evidence=(evidence,),
    )
    return dependency, (context,), consumption


class DependencyCICoverageTests(unittest.TestCase):
    def test_requirements_install_supports_consumption_without_direct_exercise(self) -> None:
        dependency, contexts = _requirement_dependency()
        workflow = """jobs:
  test:
    steps:
      - run: pip install -r requirements-dev.txt
"""

        result = evaluate_dependency_ci_coverage(
            dependency,
            [_input(workflow)],
            source_contexts=contexts,
        )

        self.assertEqual(result.state, "supported_not_correlated")
        workflow_result = result.workflows[0]
        self.assertEqual(workflow_result.consumption_state, "supported")
        self.assertEqual(workflow_result.direct_exercise_state, "not_established")
        self.assertIsNotNone(workflow_result.consumption_command)
        self.assertIsNone(workflow_result.execution_command)

    def test_requirements_install_then_direct_invocation_supports_both_axes(self) -> None:
        dependency, contexts = _requirement_dependency()
        workflow = """jobs:
  test:
    steps:
      - run: |
          pip install -r requirements-dev.txt
          pytest tests
"""

        result = evaluate_dependency_ci_coverage(
            dependency,
            [_input(workflow)],
            source_contexts=contexts,
        )

        workflow_result = result.workflows[0]
        self.assertEqual(workflow_result.consumption_state, "supported")
        self.assertEqual(workflow_result.direct_exercise_state, "supported")
        self.assertIsNotNone(workflow_result.execution_command)

    def test_multiple_static_jobs_no_longer_destroy_supported_consumption(self) -> None:
        dependency, contexts = _requirement_dependency()
        workflow = """jobs:
  unit:
    steps:
      - run: pip install -r requirements-dev.txt
  lint:
    steps:
      - run: ruff check .
"""

        result = evaluate_dependency_ci_coverage(
            dependency,
            [_input(workflow)],
            source_contexts=contexts,
        )

        self.assertEqual(result.state, "supported_not_correlated")
        self.assertEqual(result.workflows[0].consumption_state, "supported")

    def test_s001_shape_supports_consumption_without_direct_soupsieve_exercise(self) -> None:
        dependency, contexts = _uv_dependency()
        workflow = """jobs:
  docs:
    steps:
      - run: uv sync --group docs
      - run: uv run mkdocs build
  lint:
    steps:
      - run: ruff check .
"""

        result = evaluate_dependency_ci_coverage(
            dependency,
            [_input(workflow, external_consumptions=(_s001_consumption(),))],
            source_contexts=contexts,
        )

        self.assertEqual(result.state, "supported_not_correlated")
        workflow_result = result.workflows[0]
        self.assertEqual(workflow_result.consumption_state, "supported")
        self.assertEqual(workflow_result.direct_exercise_state, "not_established")
        self.assertEqual(
            workflow_result.consumptions[0].witness_path,
            ("mkdocs-llmstxt", "beautifulsoup4", "soupsieve"),
        )

    def test_s011_dev_selection_does_not_become_mlx_consumption(self) -> None:
        dependency, contexts, consumption = _s011_context_and_consumption()
        workflow = """jobs:
  test:
    steps:
      - run: pip install -e ".[dev]"
      - run: pytest
"""

        result = evaluate_dependency_ci_coverage(
            dependency,
            [_input(workflow, external_consumptions=(consumption,))],
            source_contexts=contexts,
        )

        self.assertEqual(result.state, "unresolved")
        workflow_result = result.workflows[0]
        self.assertEqual(workflow_result.consumption_state, "not_established")
        self.assertEqual(
            workflow_result.consumption_reason,
            "selected_environment_membership_not_established",
        )
        self.assertEqual(workflow_result.direct_exercise_state, "not_established")

    def test_no_successful_ci_remains_separate_from_supported_static_consumption(self) -> None:
        dependency, contexts = _uv_dependency()
        workflow = """jobs:
  docs:
    steps:
      - run: uv sync --group docs
"""
        failed_run = _run(conclusion="failure")

        result = evaluate_dependency_ci_coverage(
            dependency,
            [
                _input(
                    workflow,
                    run=failed_run,
                    jobs=(_job(conclusion="failure"),),
                    external_consumptions=(_s001_consumption(),),
                )
            ],
            source_contexts=contexts,
        )

        self.assertEqual(result.state, "no_successful_ci")
        self.assertEqual(result.workflows[0].state, "no_successful_ci")
        self.assertEqual(result.workflows[0].consumption_state, "supported")

    def test_external_consumption_from_other_workflow_revision_is_rejected(self) -> None:
        dependency, contexts = _uv_dependency()
        consumption = _s001_consumption()
        mismatched = type(consumption)(
            state=consumption.state,
            mechanism=consumption.mechanism,
            normalized_package=consumption.normalized_package,
            workflow_path=consumption.workflow_path,
            workflow_revision="c" * 40,
            job_key=consumption.job_key,
            step_source_index=consumption.step_source_index,
            segment_index=consumption.segment_index,
            command=consumption.command,
            reason=consumption.reason,
            detail=consumption.detail,
            source_path=consumption.source_path,
            membership_kind=consumption.membership_kind,
            witness_path=consumption.witness_path,
        )
        workflow = """jobs:
  docs:
    steps:
      - run: uv sync --group docs
"""

        result = evaluate_dependency_ci_coverage(
            dependency,
            [_input(workflow, external_consumptions=(mismatched,))],
            source_contexts=contexts,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.workflows[0].consumption_state, "unresolved")
        self.assertEqual(
            result.workflows[0].consumption_reason,
            "external_consumption_workflow_identity_mismatch",
        )

    def test_supported_workflow_wins_without_erasing_weaker_workflow(self) -> None:
        dependency, contexts = _requirement_dependency()
        supported = """jobs:
  test:
    steps:
      - run: pip install -r requirements-dev.txt
"""
        weak = """jobs:
  test:
    steps:
      - run: python -V
"""
        second_run = _run(run_id=1002, name="Other")

        result = evaluate_dependency_ci_coverage(
            dependency,
            [
                _input(supported),
                _input(
                    weak,
                    run=second_run,
                    jobs=(_job(run_id=1002, job_id=3002),),
                    path=".github/workflows/other.yml",
                ),
            ],
            source_contexts=contexts,
        )

        self.assertEqual(result.state, "supported_not_correlated")
        self.assertEqual(len(result.workflows), 2)
        self.assertEqual(result.workflows[0].consumption_state, "supported")
        self.assertEqual(result.workflows[1].consumption_state, "not_established")


if __name__ == "__main__":
    unittest.main()
