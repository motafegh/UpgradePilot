"""Test Cluster-5 CI coverage with consumption and direct exercise separated."""

from __future__ import annotations

import unittest

from upgradepilot.ci.consumption import compose_project_environment_consumption
from upgradepilot.ci.dependency_exercise import (
    WorkflowDependencyCoverageInput,
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
from upgradepilot.dependency.uv_reachability import UvSelectedRootReachability
from upgradepilot.dependency.workflow_context import EffectiveWorkingDirectory
from upgradepilot.github.actions import WorkflowJob, WorkflowRun
from upgradepilot.github.repository import RepositoryTextFile, UnavailableRepositoryFile

_REPOSITORY = "example/project"
_HEAD_SHA = "a" * 40
_WORKFLOW_PATH = ".github/workflows/ci.yml"
_CHECKOUT = "actions/checkout@v4"


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
    project_environment_consumptions=(),
    path: str = _WORKFLOW_PATH,
) -> WorkflowDependencyCoverageInput:
    selected_run = run or _run()
    return WorkflowDependencyCoverageInput(
        run=selected_run,
        jobs=jobs if jobs is not None else (_job(run_id=selected_run.run_id),),
        definition=_definition(content, path=path),
        project_environment_consumptions=tuple(project_environment_consumptions),
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


def _uv_observation_and_declaration(
    *,
    package_scope: str = "all_workspace_packages",
) -> tuple[ProjectEnvironmentSelectionObservation, ProjectEnvironmentSelectionDeclaration]:
    declaration = ProjectEnvironmentSelectionDeclaration(
        manager="uv",
        operation="sync",
        segment_index=0,
        project_root=None,
        selectors=(DependencyGroupSelector("docs"),),
        package_scope=package_scope,  # type: ignore[arg-type]
    )
    command = (
        "uv sync --all-packages --group docs"
        if package_scope == "all_workspace_packages"
        else "uv sync --group docs"
    )
    observation = ProjectEnvironmentSelectionObservation(
        state="observed",
        reason="project_environment_selection_declared",
        detail="docs selected",
        step_source_index=0,
        command=command,
        project_file_path="pyproject.toml",
        working_directory=_root_workdir(),
        declarations=(declaration,),
    )
    return observation, declaration


def _s001_consumption():
    observation, declaration = _uv_observation_and_declaration()
    reachability = UvSelectedRootReachability(
        state="reachable",
        reason="uv_selected_root_transitive_reachability",
        detail="SoupSieve is transitively reachable from the selected docs root.",
        normalized_package="soupsieve",
        project_root=None,
        lock_file_path="uv.lock",
        selectors=declaration.selectors,
        reachability_kind="transitive",
        witness_root="mkdocs-llmstxt",
        witness_path=("mkdocs-llmstxt", "beautifulsoup4", "soupsieve"),
    )
    return compose_project_environment_consumption(
        workflow_path=_WORKFLOW_PATH,
        workflow_revision=_HEAD_SHA,
        job_key="docs",
        observation=observation,
        declaration=declaration,
        dependency_evidence=reachability,
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
        dependency_evidence=membership,
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
    def test_no_workflow_inputs_is_no_successful_ci(self) -> None:
        dependency, contexts = _requirement_dependency()

        result = evaluate_dependency_ci_coverage(
            dependency,
            (),
            source_contexts=contexts,
        )

        self.assertEqual(result.state, "no_successful_ci")
        self.assertEqual(result.reason, "no_exact_head_workflows")
        self.assertEqual(result.workflows, ())

    def test_no_successful_job_precedes_unavailable_definition(self) -> None:
        dependency, contexts = _requirement_dependency()
        definition = UnavailableRepositoryFile(
            repository=_REPOSITORY,
            path=_WORKFLOW_PATH,
            revision=_HEAD_SHA,
            reason="path_not_found",
            detail="The exact workflow definition was unavailable.",
        )

        result = evaluate_dependency_ci_coverage(
            dependency,
            (
                WorkflowDependencyCoverageInput(
                    run=_run(),
                    jobs=(),
                    definition=definition,
                ),
            ),
            source_contexts=contexts,
        )

        self.assertEqual(result.state, "no_successful_ci")
        workflow_result = result.workflows[0]
        self.assertEqual(workflow_result.state, "no_successful_ci")
        self.assertEqual(workflow_result.reason, "no_successful_jobs")
        self.assertEqual(
            workflow_result.consumption_reason,
            "workflow_definition_unavailable",
        )

    def test_successful_job_with_unavailable_definition_is_unresolved(self) -> None:
        dependency, contexts = _requirement_dependency()
        definition = UnavailableRepositoryFile(
            repository=_REPOSITORY,
            path=_WORKFLOW_PATH,
            revision=_HEAD_SHA,
            reason="path_not_found",
            detail="The exact workflow definition was unavailable.",
        )

        result = evaluate_dependency_ci_coverage(
            dependency,
            (
                WorkflowDependencyCoverageInput(
                    run=_run(),
                    jobs=(_job(),),
                    definition=definition,
                ),
            ),
            source_contexts=contexts,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.workflows[0].state, "unresolved")
        self.assertEqual(
            result.workflows[0].reason,
            "workflow_definition_unavailable",
        )

    def test_successful_job_with_non_successful_run_is_unresolved(self) -> None:
        dependency, contexts = _requirement_dependency()
        workflow = f"""jobs:
  test:
    steps:
      - uses: {_CHECKOUT}
      - run: pip install -r requirements-dev.txt
"""
        failed_run = _run(conclusion="failure")

        result = evaluate_dependency_ci_coverage(
            dependency,
            [
                _input(
                    workflow,
                    run=failed_run,
                    jobs=(_job(run_id=failed_run.run_id),),
                )
            ],
            source_contexts=contexts,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.workflows[0].state, "unresolved")
        self.assertEqual(result.workflows[0].reason, "workflow_not_successful")

    def test_requirements_install_supports_consumption_without_direct_exercise(self) -> None:
        dependency, contexts = _requirement_dependency()
        workflow = f"""jobs:
  test:
    steps:
      - uses: {_CHECKOUT}
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
        workflow = f"""jobs:
  test:
    steps:
      - uses: {_CHECKOUT}
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

    def test_direct_invocation_before_consumption_is_not_direct_exercise(self) -> None:
        dependency, contexts = _requirement_dependency()
        workflow = f"""jobs:
  test:
    steps:
      - uses: {_CHECKOUT}
      - run: |
          pytest tests
          pip install -r requirements-dev.txt
"""

        result = evaluate_dependency_ci_coverage(
            dependency,
            [_input(workflow)],
            source_contexts=contexts,
        )

        workflow_result = result.workflows[0]
        self.assertEqual(workflow_result.consumption_state, "supported")
        self.assertEqual(workflow_result.direct_exercise_state, "not_established")
        self.assertEqual(
            workflow_result.direct_exercise_reason,
            "direct_invocation_not_after_supported_consumption",
        )

    def test_multiple_static_jobs_no_longer_destroy_supported_consumption(self) -> None:
        dependency, contexts = _requirement_dependency()
        workflow = f"""jobs:
  unit:
    steps:
      - uses: {_CHECKOUT}
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
      - run: uv sync --all-packages --group docs
      - run: uv run mkdocs build
  lint:
    steps:
      - run: ruff check .
"""

        result = evaluate_dependency_ci_coverage(
            dependency,
            [
                _input(
                    workflow,
                    project_environment_consumptions=(_s001_consumption(),),
                )
            ],
            source_contexts=contexts,
        )

        self.assertEqual(result.state, "supported_not_correlated")
        workflow_result = result.workflows[0]
        self.assertEqual(workflow_result.consumption_state, "supported")
        self.assertEqual(workflow_result.direct_exercise_state, "not_established")
        consumption = workflow_result.consumptions[0]
        self.assertEqual(consumption.source_path, "uv.lock")
        self.assertEqual(consumption.reachability_kind, "transitive")
        self.assertEqual(
            consumption.witness_path,
            ("mkdocs-llmstxt", "beautifulsoup4", "soupsieve"),
        )

    def test_uv_conditional_candidate_remains_unresolved_consumption(self) -> None:
        observation, declaration = _uv_observation_and_declaration(package_scope="bound_project")
        reachability = UvSelectedRootReachability(
            state="unresolved",
            reason="uv_selected_root_conditional_candidate_unresolved",
            detail="Candidate depends on an unevaluated marker.",
            normalized_package="soupsieve",
            project_root=None,
            lock_file_path="uv.lock",
            selectors=declaration.selectors,
            conditional_candidate_root="mkdocs-llmstxt",
            conditional_candidate_path=(
                "mkdocs-llmstxt",
                "beautifulsoup4",
                "soupsieve",
            ),
            unresolved_conditions=(
                "edge marker to 'soupsieve': python_version >= '3.12'",
            ),
        )

        consumption = compose_project_environment_consumption(
            workflow_path=_WORKFLOW_PATH,
            workflow_revision=_HEAD_SHA,
            job_key="docs",
            observation=observation,
            declaration=declaration,
            dependency_evidence=reachability,
        )

        self.assertEqual(consumption.state, "unresolved")
        self.assertIsNone(consumption.reachability_kind)
        self.assertEqual(consumption.witness_path, ())
        self.assertEqual(
            consumption.conditional_candidate_path,
            ("mkdocs-llmstxt", "beautifulsoup4", "soupsieve"),
        )
        self.assertEqual(consumption.unresolved_conditions, reachability.unresolved_conditions)

    def test_uv_bound_project_not_established_maps_without_strengthening(self) -> None:
        observation, declaration = _uv_observation_and_declaration(package_scope="bound_project")
        reachability = UvSelectedRootReachability(
            state="not_established",
            reason="uv_selected_root_reachability_not_established",
            detail="Complete bounded selected-root domain had no target path.",
            normalized_package="soupsieve",
            project_root=None,
            lock_file_path="uv.lock",
            selectors=declaration.selectors,
        )

        consumption = compose_project_environment_consumption(
            workflow_path=_WORKFLOW_PATH,
            workflow_revision=_HEAD_SHA,
            job_key="docs",
            observation=observation,
            declaration=declaration,
            dependency_evidence=reachability,
        )

        self.assertEqual(consumption.state, "not_established")
        self.assertEqual(consumption.reason, "selected_uv_root_reachability_not_established")

    def test_uv_not_established_cannot_be_rebound_to_all_workspace_scope(self) -> None:
        observation, declaration = _uv_observation_and_declaration()
        reachability = UvSelectedRootReachability(
            state="not_established",
            reason="uv_selected_root_reachability_not_established",
            detail="Synthetic bounded negative evidence.",
            normalized_package="soupsieve",
            project_root=None,
            lock_file_path="uv.lock",
            selectors=declaration.selectors,
        )

        with self.assertRaisesRegex(ValueError, "all-workspace scope"):
            compose_project_environment_consumption(
                workflow_path=_WORKFLOW_PATH,
                workflow_revision=_HEAD_SHA,
                job_key="docs",
                observation=observation,
                declaration=declaration,
                dependency_evidence=reachability,
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
            [
                _input(
                    workflow,
                    project_environment_consumptions=(consumption,),
                )
            ],
            source_contexts=contexts,
        )

        self.assertEqual(result.state, "unresolved")
        workflow_result = result.workflows[0]
        self.assertEqual(workflow_result.consumption_state, "not_established")
        self.assertEqual(
            workflow_result.consumption_reason,
            "selected_environment_membership_not_established",
        )
        self.assertEqual(workflow_result.consumptions[0].source_path, "pyproject.toml")
        self.assertEqual(workflow_result.direct_exercise_state, "not_established")

    def test_no_successful_ci_remains_separate_from_supported_static_consumption(self) -> None:
        dependency, contexts = _uv_dependency()
        workflow = """jobs:
  docs:
    steps:
      - run: uv sync --all-packages --group docs
"""
        failed_run = _run(conclusion="failure")

        result = evaluate_dependency_ci_coverage(
            dependency,
            [
                _input(
                    workflow,
                    run=failed_run,
                    jobs=(_job(conclusion="failure"),),
                    project_environment_consumptions=(_s001_consumption(),),
                )
            ],
            source_contexts=contexts,
        )

        self.assertEqual(result.state, "no_successful_ci")
        self.assertEqual(result.workflows[0].state, "no_successful_ci")
        self.assertEqual(result.workflows[0].consumption_state, "supported")

    def test_project_environment_consumption_from_other_workflow_revision_is_rejected(
        self,
    ) -> None:
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
            reachability_kind=consumption.reachability_kind,
            witness_path=consumption.witness_path,
            conditional_candidate_path=consumption.conditional_candidate_path,
            unresolved_conditions=consumption.unresolved_conditions,
        )
        workflow = """jobs:
  docs:
    steps:
      - run: uv sync --all-packages --group docs
"""

        result = evaluate_dependency_ci_coverage(
            dependency,
            [
                _input(
                    workflow,
                    project_environment_consumptions=(mismatched,),
                )
            ],
            source_contexts=contexts,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.workflows[0].consumption_state, "unresolved")
        self.assertEqual(
            result.workflows[0].consumption_reason,
            "project_environment_consumption_workflow_identity_mismatch",
        )

    def test_supported_workflow_wins_without_erasing_weaker_workflow(self) -> None:
        dependency, contexts = _requirement_dependency()
        supported = f"""jobs:
  test:
    steps:
      - uses: {_CHECKOUT}
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
