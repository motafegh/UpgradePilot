"""Interpret exact-head CI evidence for one pinned dependency change.

Purpose of this file
--------------------
Earlier modules acquire and validate facts:

* ``dependency_change.py`` identifies one supported pinned dependency update;
* ``github_actions.py`` supplies exact-head workflow runs and jobs;
* ``github_repository.py`` supplies exact-revision workflow text or explicit
  unavailability;
* ``workflow_commands.py`` decides whether the supported direct install/invoke
  command pattern is visible.

This module combines those already-validated facts into a bounded CI-authority
classification. It performs no HTTP requests and does not parse raw GitHub JSON.

Meaning of the three statuses
-----------------------------
* ``sufficient``: at least one successful exact-head workflow satisfies the current
  direct install-and-invoke rule;
* ``insufficient``: the evidence positively shows that required successful execution
  evidence is absent, such as no exact-head workflows or no successful jobs;
* ``unresolved``: relevant CI exists, but unavailable or unsupported evidence prevents
  the current rule from proving direct dependency exercise.

A ``sufficient`` result is deliberately narrow. It proves one CI path exercised the
changed dependency under the supported rule. It does not prove complete test coverage,
upgrade safety, compatibility, or that the pull request should be merged.

Typical execution flow
----------------------
1. ``cli.py`` builds one ``WorkflowAuthorityInput`` per workflow run.
2. ``evaluate_ci_authority`` assesses every workflow independently.
3. If any assessment is sufficient, the overall result is sufficient.
4. Otherwise, absence of every successful exact-head job is insufficient.
5. Remaining cases are unresolved because successful CI exists but direct exercise
   was not proven.
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

# ``Literal`` defines the complete public status vocabulary for both per-workflow and
# overall results. Callers need not accept arbitrary strings.
type CIAuthorityStatus = Literal["sufficient", "insufficient", "unresolved"]


@dataclass(frozen=True, slots=True)
class WorkflowAuthorityInput:
    """All validated evidence needed to assess one workflow execution.

    ``run`` and ``jobs`` come from ``github_actions.py``. ``definition`` comes from
    ``github_repository.py`` and is intentionally a union: exact workflow text may be
    available or explicitly unavailable. Grouping these records prevents the evaluator
    from accidentally mixing jobs or definitions belonging to different runs.
    """

    run: WorkflowRun
    jobs: tuple[WorkflowJob, ...]
    definition: RepositoryFileEvidence


@dataclass(frozen=True, slots=True)
class WorkflowAuthorityAssessment:
    """Transparent interpretation result for one workflow run.

    The record keeps the workflow identity, stable reason, human detail, and any
    command strings actually observed. Preserving partial command evidence makes an
    unresolved result inspectable instead of reducing it to a bare status.
    """

    workflow_name: str
    workflow_path: str
    status: CIAuthorityStatus
    reason: str
    detail: str
    install_command: str | None = None
    execution_command: str | None = None


@dataclass(frozen=True, slots=True)
class CIAuthorityResult:
    """Overall CI-authority classification plus every workflow assessment.

    The overall status summarizes the current rule, while ``workflows`` preserves the
    full evidence trail. A sufficient workflow does not erase unresolved or failed
    workflows; all assessments remain available to ``cli.py`` for presentation.
    """

    status: CIAuthorityStatus
    reason: str
    detail: str
    workflows: tuple[WorkflowAuthorityAssessment, ...]


def evaluate_ci_authority(
    dependency: PinnedDependencyChange,
    workflow_inputs: Sequence[WorkflowAuthorityInput],
) -> CIAuthorityResult:
    """Classify what all current exact-head CI evidence proves.

    Goal:
        Apply the first deterministic authority rule across every acquired workflow
        while preserving per-workflow reasons.

    Why ``Sequence`` is accepted:
        The evaluator only needs ordered iteration. A tuple from ``cli.py`` is normal,
        but tests or other callers may provide another sequence type.

    Overall decision order matters:
        1. no workflows is a positive absence and therefore insufficient;
        2. any sufficient workflow establishes the existential rule;
        3. no successful job anywhere is insufficient;
        4. otherwise successful CI exists, but exercise remains unresolved.
    """

    if not workflow_inputs:
        return CIAuthorityResult(
            status="insufficient",
            reason="no_exact_head_workflows",
            detail="No pull-request workflow runs were available for the exact head SHA.",
            workflows=(),
        )

    # Assess every workflow before selecting the overall status so the final result can
    # retain transparent reasons for successful, failed, and unresolved paths.
    assessments = tuple(
        _assess_workflow(dependency, workflow_input)
        for workflow_input in workflow_inputs
    )

    # The first authority rule is existential: one proven CI path is enough to say that
    # exact-head CI exercised the dependency. ``next(..., None)`` stops at the first
    # sufficient assessment without constructing another list.
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

    # The nested generator checks all jobs across all workflow inputs lazily. ``any``
    # stops as soon as one completed-successful job is found.
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

    # At least one successful job exists, so evidence is not simply absent. However,
    # no workflow met the supported direct command rule, making the honest state
    # unresolved rather than insufficient or sufficient.
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
    """Apply the current authority rule to one workflow evidence bundle.

    Goal:
        Decide whether this single run is successful, has a successful job, has an
        exact matching workflow definition, and contains the supported commands.

    The function is private because callers should normally use the overall evaluator,
    which preserves cross-workflow decision semantics.
    """

    # Local names shorten repeated field access and make the evidence relationships
    # easier to read during the ordered checks below.
    run = workflow_input.run
    definition = workflow_input.definition
    workflow_path = definition.path

    # An unavailable definition is not evidence of a failed workflow or absent command.
    # The command question cannot be answered, so the result is unresolved.
    if isinstance(definition, UnavailableRepositoryFile):
        return WorkflowAuthorityAssessment(
            workflow_name=run.name,
            workflow_path=workflow_path,
            status="unresolved",
            reason="workflow_definition_unavailable",
            detail=definition.detail,
        )

    # ``RepositoryFileEvidence`` has only two union members. After returning from the
    # unavailable branch, this assertion documents and narrows the remaining type for
    # readers and type checkers. It also protects the invariant at runtime.
    assert isinstance(definition, RepositoryTextFile)

    # Exact workflow text from another commit must not be attached to this run, even
    # if the path and contents otherwise look plausible.
    if definition.revision != run.head_sha:
        return WorkflowAuthorityAssessment(
            workflow_name=run.name,
            workflow_path=workflow_path,
            status="unresolved",
            reason="workflow_definition_revision_mismatch",
            detail="Workflow definition revision did not match the run head SHA.",
        )

    # Filter once into an immutable tuple so the following checks and command rule use
    # a clear set of completed-successful jobs.
    successful_jobs = tuple(
        job
        for job in workflow_input.jobs
        if job.status == "completed" and job.conclusion == "success"
    )

    # A non-successful workflow positively fails the execution requirement; this is
    # insufficient evidence rather than an unsupported interpretation.
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

    # Only after revision and execution success are established do we inspect workflow
    # commands. The keyword arguments identify the exact changed file and package from
    # ``PinnedDependencyChange``.
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
