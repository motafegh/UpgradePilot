"""Interpret exact-head CI evidence for one canonical dependency change.

This module answers one narrow question: whether an admitted successful exact-head CI
path consumed the changed dependency and exercised the changed package under a selected
deterministic rule. It does not establish complete coverage, compatibility, safety, or
a maintainer decision.

The current rule supports only an explicitly supplied direct-requirements path together
with visible ``pip -r`` installation and direct changed-package invocation. Generic
dependency evidence paths are never promoted into CI-consumption proof.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

from .dependency_change import DependencyVersionChange
from .github_actions import WorkflowJob, WorkflowRun
from .github_repository import (
    RepositoryFileEvidence,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)
from .workflow_commands import inspect_workflow_commands


type DependencyCIExerciseState = Literal[
    "proven",
    "no_successful_ci",
    "unresolved",
]


@dataclass(frozen=True, slots=True)
class WorkflowDependencyExerciseInput:
    """Validated run, job, and exact workflow-definition evidence for one run."""

    run: WorkflowRun
    jobs: tuple[WorkflowJob, ...]
    definition: RepositoryFileEvidence


@dataclass(frozen=True, slots=True)
class WorkflowDependencyExerciseResult:
    """Transparent dependency-exercise interpretation for one workflow run."""

    workflow_name: str
    workflow_path: str
    state: DependencyCIExerciseState
    reason: str
    detail: str
    install_command: str | None = None
    execution_command: str | None = None


@dataclass(frozen=True, slots=True)
class DependencyCIExerciseResult:
    """Overall CI dependency-exercise state plus every workflow result."""

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
    """Classify what exact-head CI proves about dependency exercise.

    State meanings are exact:

    * ``proven`` — one successful exact-head path satisfies an admitted consumption and
      package-exercise rule;
    * ``no_successful_ci`` — no completed successful exact-head job is available;
    * ``unresolved`` — at least one successful job exists, but no admitted rule proves
      dependency consumption and package exercise.

    The keyword-only requirements path is source-specific operational evidence. It is
    never inferred from ``dependency.source_evidence``.
    """

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

    proven = next(
        (result for result in results if result.state == "proven"),
        None,
    )
    if proven is not None:
        assert direct_requirements_install_path is not None
        return DependencyCIExerciseResult(
            state="proven",
            reason="exact_head_dependency_exercised",
            detail=(
                f"Workflow {proven.workflow_name!r} installed "
                f"{direct_requirements_install_path!r} and directly invoked "
                f"{dependency.package!r} in successful exact-head CI."
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
        reason="dependency_exercise_not_proven",
        detail=(
            "Successful exact-head CI exists, but no admitted rule proved that it "
            "consumed and exercised the changed dependency."
        ),
        workflows=results,
    )


def _evaluate_workflow_dependency_exercise(
    dependency: DependencyVersionChange,
    workflow_input: WorkflowDependencyExerciseInput,
    *,
    direct_requirements_install_path: str | None,
) -> WorkflowDependencyExerciseResult:
    """Apply the current direct-requirements rule to one workflow bundle."""

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
                "the current CI command rule. Dependency evidence paths were not "
                "treated as installation proof."
            ),
        )

    commands = inspect_workflow_commands(
        definition.content,
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

    return WorkflowDependencyExerciseResult(
        workflow_name=run.name,
        workflow_path=workflow_path,
        state="proven",
        reason=commands.reason,
        detail=(
            "A successful exact-head workflow job installs the explicitly supplied "
            "requirements file and directly invokes the changed package."
        ),
        install_command=commands.install_command,
        execution_command=commands.execution_command,
    )
