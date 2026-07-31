"""Interpret exact-head CI evidence for one canonical dependency change.

The current CI rule remains intentionally narrow: one successful exact-head workflow
must visibly install one explicitly supplied requirements file and directly invoke the
changed package. The dependency identity is format-independent; the requirements path
is separate source-specific input. Generic dependency evidence paths are never selected
as installation proof.
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


type CIAuthorityStatus = Literal["sufficient", "insufficient", "unresolved"]


@dataclass(frozen=True, slots=True)
class WorkflowAuthorityInput:
    """Validated run, job, and exact workflow-definition evidence for one run."""

    run: WorkflowRun
    jobs: tuple[WorkflowJob, ...]
    definition: RepositoryFileEvidence


@dataclass(frozen=True, slots=True)
class WorkflowAuthorityAssessment:
    """Transparent interpretation result for one workflow run."""

    workflow_name: str
    workflow_path: str
    status: CIAuthorityStatus
    reason: str
    detail: str
    install_command: str | None = None
    execution_command: str | None = None


@dataclass(frozen=True, slots=True)
class CIAuthorityResult:
    """Overall CI-authority classification plus every workflow assessment."""

    status: CIAuthorityStatus
    reason: str
    detail: str
    workflows: tuple[WorkflowAuthorityAssessment, ...]


def evaluate_ci_authority(
    dependency: DependencyVersionChange,
    workflow_inputs: Sequence[WorkflowAuthorityInput],
    *,
    direct_requirements_install_path: str | None,
) -> CIAuthorityResult:
    """Classify what exact-head CI proves under the current direct requirements rule.

    ``dependency`` supplies canonical package identity only. The keyword-only
    ``direct_requirements_install_path`` must be established independently by the
    caller. ``None`` means the current command rule has no admitted source-specific
    installation input; successful CI therefore remains unresolved rather than using a
    path from ``dependency.source_evidence``.

    Overall decision order remains the validated legacy order:

    1. no workflows is insufficient;
    2. any sufficient workflow establishes the existential rule;
    3. no successful job anywhere is insufficient;
    4. otherwise successful CI exists but dependency exercise is unresolved.
    """

    if not workflow_inputs:
        return CIAuthorityResult(
            status="insufficient",
            reason="no_exact_head_workflows",
            detail="No pull-request workflow runs were available for the exact head SHA.",
            workflows=(),
        )

    assessments = tuple(
        _assess_workflow(
            dependency,
            workflow_input,
            direct_requirements_install_path=direct_requirements_install_path,
        )
        for workflow_input in workflow_inputs
    )

    sufficient = next(
        (item for item in assessments if item.status == "sufficient"),
        None,
    )
    if sufficient is not None:
        # A sufficient assessment can only be produced after the private evaluator
        # receives a concrete explicit path.
        assert direct_requirements_install_path is not None
        return CIAuthorityResult(
            status="sufficient",
            reason="exact_head_dependency_exercised",
            detail=(
                f"Workflow {sufficient.workflow_name!r} installed "
                f"{direct_requirements_install_path!r} and directly invoked "
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
    dependency: DependencyVersionChange,
    workflow_input: WorkflowAuthorityInput,
    *,
    direct_requirements_install_path: str | None,
) -> WorkflowAuthorityAssessment:
    """Apply the current direct requirements rule to one workflow bundle."""

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

    if direct_requirements_install_path is None:
        return WorkflowAuthorityAssessment(
            workflow_name=run.name,
            workflow_path=workflow_path,
            status="unresolved",
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
            "A successful exact-head workflow job installs the explicitly supplied "
            "requirements file and directly invokes the changed package."
        ),
        install_command=commands.install_command,
        execution_command=commands.execution_command,
    )
