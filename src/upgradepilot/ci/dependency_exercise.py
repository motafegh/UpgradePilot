"""Interpret exact-head CI evidence for one canonical dependency change.

This boundary combines two evidence families without conflating them:

* runtime GitHub Actions evidence can establish that an exact-head workflow/run had
  completed-successful run/job records;
* the exact-head static workflow definition can establish an ordered dependency install
  declaration and direct package invocation under the bounded CI rule.

Cluster 5 intentionally does **not** correlate those static steps to runtime step
records. Therefore the strongest current state is ``supported_not_correlated`` rather
than ``proven``. The result does not establish that the matched static commands executed
or succeeded, nor does it establish complete coverage, compatibility, safety, or a
maintainer decision.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

from ..dependency.change import DependencyVersionChange
from ..github.actions import WorkflowJob, WorkflowRun
from ..github.repository import (
    RepositoryFileEvidence,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)
from .workflow_commands import inspect_workflow_commands

type DependencyCIExerciseState = Literal[
    "supported_not_correlated",
    "no_successful_ci",
    "unresolved",
]


@dataclass(frozen=True, slots=True)
class WorkflowDependencyExerciseInput:
    """Runtime run/jobs plus the exact static definition for one workflow path."""

    run: WorkflowRun
    jobs: tuple[WorkflowJob, ...]
    definition: RepositoryFileEvidence


@dataclass(frozen=True, slots=True)
class WorkflowDependencyExerciseResult:
    """Workflow-scoped result preserving runtime/static evidence boundaries."""

    workflow_name: str
    workflow_path: str
    state: DependencyCIExerciseState
    reason: str
    detail: str
    install_command: str | None = None
    execution_command: str | None = None


@dataclass(frozen=True, slots=True)
class DependencyCIExerciseResult:
    """Aggregate CI support state for one dependency change."""

    state: DependencyCIExerciseState
    reason: str
    detail: str
    workflows: tuple[WorkflowDependencyExerciseResult, ...]


def evaluate_dependency_ci_exercise(
    dependency: DependencyVersionChange,
    workflow_inputs: Sequence[WorkflowDependencyExerciseInput],
    *,
    direct_requirements_install_path: str | None,
) -> DependencyCIExerciseResult:
    """Classify current CI support without claiming static↔runtime correlation."""

    if not workflow_inputs:
        return DependencyCIExerciseResult(
            state="no_successful_ci",
            reason="no_exact_head_workflows",
            detail="No pull-request workflow runs were available for the exact head SHA.",
            workflows=(),
        )

    results = tuple(
        _evaluate_workflow_dependency_exercise(
            dependency,
            workflow_input,
            direct_requirements_install_path=direct_requirements_install_path,
        )
        for workflow_input in workflow_inputs
    )

    supported = next(
        (result for result in results if result.state == "supported_not_correlated"),
        None,
    )
    if supported is not None:
        assert direct_requirements_install_path is not None
        return DependencyCIExerciseResult(
            state="supported_not_correlated",
            reason="successful_exact_head_ci_with_static_dependency_path",
            detail=(
                f"Successful exact-head CI evidence exists for workflow "
                f"{supported.workflow_name!r}, and its exact-head static definition "
                f"declares installation from {direct_requirements_install_path!r} before "
                f"a direct invocation of {dependency.package!r}. The matched static "
                "commands are not correlated to runtime step execution or success."
            ),
            workflows=results,
        )

    has_successful_job = any(
        job.status == "completed" and job.conclusion == "success"
        for workflow_input in workflow_inputs
        for job in workflow_input.jobs
    )
    if not has_successful_job:
        return DependencyCIExerciseResult(
            state="no_successful_ci",
            reason="no_successful_exact_head_jobs",
            detail="No completed successful exact-head job was available.",
            workflows=results,
        )

    return DependencyCIExerciseResult(
        state="unresolved",
        reason="dependency_exercise_not_established",
        detail=(
            "Successful exact-head CI exists, but the admitted evidence does not "
            "establish a sufficiently bounded static dependency path or correlate such "
            "a path to successful runtime steps."
        ),
        workflows=results,
    )


def _evaluate_workflow_dependency_exercise(
    dependency: DependencyVersionChange,
    workflow_input: WorkflowDependencyExerciseInput,
    *,
    direct_requirements_install_path: str | None,
) -> WorkflowDependencyExerciseResult:
    """Combine one workflow's runtime authority with its exact static definition."""

    run = workflow_input.run
    definition = workflow_input.definition
    workflow_path = definition.path

    successful_jobs = tuple(
        job
        for job in workflow_input.jobs
        if job.status == "completed" and job.conclusion == "success"
    )
    if not successful_jobs:
        return WorkflowDependencyExerciseResult(
            workflow_name=run.name,
            workflow_path=workflow_path,
            state="no_successful_ci",
            reason="no_successful_jobs",
            detail="The workflow had no completed successful job record.",
        )

    if run.status != "completed" or run.conclusion != "success":
        return WorkflowDependencyExerciseResult(
            workflow_name=run.name,
            workflow_path=workflow_path,
            state="unresolved",
            reason="workflow_not_successful",
            detail=(
                "A completed successful job exists, but the workflow run was not "
                f"completed-successful; conclusion was {run.conclusion!r}."
            ),
        )

    if isinstance(definition, UnavailableRepositoryFile):
        return WorkflowDependencyExerciseResult(
            workflow_name=run.name,
            workflow_path=workflow_path,
            state="unresolved",
            reason="workflow_definition_unavailable",
            detail=definition.detail,
        )

    assert isinstance(definition, RepositoryTextFile)
    if definition.revision != run.head_sha:
        return WorkflowDependencyExerciseResult(
            workflow_name=run.name,
            workflow_path=workflow_path,
            state="unresolved",
            reason="workflow_definition_revision_mismatch",
            detail="Workflow definition revision did not match the run head SHA.",
        )

    if direct_requirements_install_path is None:
        return WorkflowDependencyExerciseResult(
            workflow_name=run.name,
            workflow_path=workflow_path,
            state="unresolved",
            reason="direct_requirements_install_path_unavailable",
            detail=(
                "No explicit direct-requirements installation path was supplied for "
                "the current CI rule. Generic dependency evidence paths were not "
                "treated as installation declarations."
            ),
        )

    commands = inspect_workflow_commands(
        definition,
        source_file=direct_requirements_install_path,
        package=dependency.package,
        normalized_package=dependency.normalized_package,
    )
    if commands.status == "unresolved":
        return WorkflowDependencyExerciseResult(
            workflow_name=run.name,
            workflow_path=workflow_path,
            state="unresolved",
            reason=commands.reason,
            detail=commands.detail,
            install_command=commands.install_command,
            execution_command=commands.execution_command,
        )

    # Runtime success and static path recognition are deliberately kept as separate
    # premises. Without explicit static↔runtime correlation we can say the evidence
    # supports the path, but not that these exact static commands ran successfully.
    return WorkflowDependencyExerciseResult(
        workflow_name=run.name,
        workflow_path=workflow_path,
        state="supported_not_correlated",
        reason="successful_ci_with_ordered_static_dependency_path",
        detail=(
            "The exact-head workflow/run has successful runtime evidence and its static "
            "definition declares an ordered direct dependency install and package "
            "invocation. The static declarations are not correlated to runtime steps."
        ),
        install_command=commands.install_command,
        execution_command=commands.execution_command,
    )


__all__ = (
    "DependencyCIExerciseResult",
    "DependencyCIExerciseState",
    "WorkflowDependencyExerciseInput",
    "WorkflowDependencyExerciseResult",
    "evaluate_dependency_ci_exercise",
)
