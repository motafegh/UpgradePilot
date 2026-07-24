"""Evaluate whether exact-head CI directly exercised one dependency change.

This is deterministic interpretation over already validated evidence. The first
rule is deliberately narrow: one successful exact-head workflow must contain one
statically readable job whose commands install the changed requirements file and
directly invoke the changed package. Indirect tox/script paths remain unresolved.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

from .dependency_change import PinnedDependencyChange
from .github_actions import WorkflowJob, WorkflowRun
from .github_repository import (
    RepositoryFileEvidence,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)
from .workflow_commands import inspect_workflow_commands

type CIAuthorityStatus = Literal["sufficient", "insufficient", "unresolved"]


@dataclass(frozen=True, slots=True)
class WorkflowAuthorityInput:
    """Validated runtime and workflow-definition evidence for one run."""

    run: WorkflowRun
    jobs: tuple[WorkflowJob, ...]
    definition: RepositoryFileEvidence


@dataclass(frozen=True, slots=True)
class WorkflowAuthorityAssessment:
    """Bounded authority interpretation for one workflow run."""

    workflow_name: str
    workflow_path: str
    status: CIAuthorityStatus
    reason: str
    detail: str
    install_command: str | None = None
    execution_command: str | None = None


@dataclass(frozen=True, slots=True)
class CIAuthorityResult:
    """Overall authority result with transparent per-workflow reasons."""

    status: CIAuthorityStatus
    reason: str
    detail: str
    workflows: tuple[WorkflowAuthorityAssessment, ...]


def evaluate_ci_authority(
    dependency: PinnedDependencyChange,
    workflow_inputs: Sequence[WorkflowAuthorityInput],
) -> CIAuthorityResult:
    """Classify what the current exact-head CI evidence proves.

    One sufficient workflow proves that at least one CI path exercised the
    dependency. It does not prove complete coverage, upgrade safety, or a merge
    recommendation.
    """

    if not workflow_inputs:
        return CIAuthorityResult(
            status="insufficient",
            reason="no_exact_head_workflows",
            detail="No pull-request workflow runs were available for the exact head SHA.",
            workflows=(),
        )

    assessments = tuple(
        _assess_workflow(dependency, workflow_input)
        for workflow_input in workflow_inputs
    )
    sufficient = next(
        (item for item in assessments if item.status == "sufficient"),
        None,
    )
    if sufficient is not None:
        return CIAuthorityResult(
            status="sufficient",
            reason="exact_head_dependency_exercised",
            detail=(
                f"Workflow {sufficient.workflow_name!r} installed "
                f"{dependency.source_file!r} and directly invoked "
                f"{dependency.package!r} in successful exact-head CI."
            ),
            workflows=assessments,
        )

    has_successful_job = any(
        job.status == "completed" and job.conclusion == "success"
        for workflow_input in workflow_inputs
        for job in workflow_input.jobs
    )
    if not has_successful_job:
        return CIAuthorityResult(
            status="insufficient",
            reason="no_successful_exact_head_jobs",
            detail="No completed successful exact-head job could establish exercise.",
            workflows=assessments,
        )

    return CIAuthorityResult(
        status="unresolved",
        reason="dependency_exercise_not_proven",
        detail=(
            "Successful exact-head CI exists, but the current rule could not prove "
            "that it installed and directly invoked the changed dependency."
        ),
        workflows=assessments,
    )


def _assess_workflow(
    dependency: PinnedDependencyChange,
    workflow_input: WorkflowAuthorityInput,
) -> WorkflowAuthorityAssessment:
    """Apply the first deterministic authority rule to one workflow."""

    run = workflow_input.run
    definition = workflow_input.definition
    workflow_path = definition.path

    if isinstance(definition, UnavailableRepositoryFile):
        return WorkflowAuthorityAssessment(
            workflow_name=run.name,
            workflow_path=workflow_path,
            status="unresolved",
            reason="workflow_definition_unavailable",
            detail=definition.detail,
        )

    assert isinstance(definition, RepositoryTextFile)
    if definition.revision != run.head_sha:
        return WorkflowAuthorityAssessment(
            workflow_name=run.name,
            workflow_path=workflow_path,
            status="unresolved",
            reason="workflow_definition_revision_mismatch",
            detail="Workflow definition revision did not match the run head SHA.",
        )

    successful_jobs = tuple(
        job
        for job in workflow_input.jobs
        if job.status == "completed" and job.conclusion == "success"
    )
    if run.status != "completed" or run.conclusion != "success":
        return WorkflowAuthorityAssessment(
            workflow_name=run.name,
            workflow_path=workflow_path,
            status="insufficient",
            reason="workflow_not_successful",
            detail=f"Workflow conclusion was {run.conclusion!r}, not success.",
        )
    if not successful_jobs:
        return WorkflowAuthorityAssessment(
            workflow_name=run.name,
            workflow_path=workflow_path,
            status="insufficient",
            reason="no_successful_jobs",
            detail="The workflow had no completed successful job record.",
        )

    commands = inspect_workflow_commands(
        definition.content,
        source_file=dependency.source_file,
        package=dependency.package,
        normalized_package=dependency.normalized_package,
    )
    if commands.status == "unresolved":
        return WorkflowAuthorityAssessment(
            workflow_name=run.name,
            workflow_path=workflow_path,
            status="unresolved",
            reason=commands.reason,
            detail=commands.detail,
            install_command=commands.install_command,
            execution_command=commands.execution_command,
        )

    return WorkflowAuthorityAssessment(
        workflow_name=run.name,
        workflow_path=workflow_path,
        status="sufficient",
        reason=commands.reason,
        detail=(
            "A successful exact-head workflow job installs the changed requirements "
            "file and directly invokes the changed package."
        ),
        install_command=commands.install_command,
        execution_command=commands.execution_command,
    )
