"""Interpret exact-head CI evidence for one canonical dependency change.

Cluster 5 introduces a coverage-oriented path that separates three propositions:

* successful exact-head runtime workflow/job authority;
* static changed-dependency consumption;
* stronger static direct changed-package exercise.

Static consumption may be established by direct requirements installation or by a typed
project-environment selection/membership composition. Direct exercise additionally
requires a package invocation ordered after supported consumption in the same static job.
Neither proposition is correlated to runtime step execution in this cluster.

The legacy ``evaluate_dependency_ci_exercise`` path is retained temporarily so ordinary
application/CLI orchestration can migrate in Cluster 6 without destabilizing the accepted
requirements behavior during this cluster.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

from ..dependency.change import DependencyVersionChange
from ..dependency.environment import DependencySourceContext
from ..github.actions import WorkflowJob, WorkflowRun
from ..github.repository import (
    RepositoryFileEvidence,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)
from .consumption import StaticDependencyConsumptionEvidence
from .workflow_commands import (
    DirectPackageInvocationEvidence,
    WorkflowStaticDependencyEvidence,
    inspect_workflow_commands,
    inspect_workflow_dependency_evidence,
)


type DependencyCIExerciseState = Literal[
    "supported_not_correlated",
    "no_successful_ci",
    "unresolved",
]
type DependencyCICoverageState = DependencyCIExerciseState
type StaticCIEvidenceState = Literal["supported", "not_established", "unresolved"]


@dataclass(frozen=True, slots=True)
class WorkflowDependencyExerciseInput:
    """Runtime run/jobs plus exact static definition and optional typed consumptions.

    ``external_consumptions`` is used by the new Cluster-5 coverage path for already
    composed project-environment evidence. The legacy evaluator ignores it.
    """

    run: WorkflowRun
    jobs: tuple[WorkflowJob, ...]
    definition: RepositoryFileEvidence
    external_consumptions: tuple[StaticDependencyConsumptionEvidence, ...] = ()


@dataclass(frozen=True, slots=True)
class WorkflowDependencyExerciseResult:
    """Legacy workflow-scoped combined install→invocation result."""

    workflow_name: str
    workflow_path: str
    state: DependencyCIExerciseState
    reason: str
    detail: str
    install_command: str | None = None
    execution_command: str | None = None


@dataclass(frozen=True, slots=True)
class DependencyCIExerciseResult:
    """Legacy aggregate CI exercise result retained through Cluster 5."""

    state: DependencyCIExerciseState
    reason: str
    detail: str
    workflows: tuple[WorkflowDependencyExerciseResult, ...]


@dataclass(frozen=True, slots=True)
class WorkflowDependencyCoverageResult:
    """Workflow-scoped runtime/static evidence with consumption/exercise separated."""

    workflow_name: str
    workflow_path: str
    state: DependencyCICoverageState
    reason: str
    detail: str
    consumption_state: StaticCIEvidenceState
    consumption_reason: str
    consumption_detail: str
    direct_exercise_state: StaticCIEvidenceState
    direct_exercise_reason: str
    direct_exercise_detail: str
    consumption_command: str | None = None
    execution_command: str | None = None
    consumptions: tuple[StaticDependencyConsumptionEvidence, ...] = ()
    invocations: tuple[DirectPackageInvocationEvidence, ...] = ()


@dataclass(frozen=True, slots=True)
class DependencyCICoverageResult:
    """Aggregate CI coverage evidence preserving heterogeneous workflow results."""

    state: DependencyCICoverageState
    reason: str
    detail: str
    workflows: tuple[WorkflowDependencyCoverageResult, ...]


def evaluate_dependency_ci_coverage(
    dependency: DependencyVersionChange,
    workflow_inputs: Sequence[WorkflowDependencyExerciseInput],
    *,
    source_contexts: Sequence[DependencySourceContext],
) -> DependencyCICoverageResult:
    """Classify CI dependency coverage without manufacturing runtime correlation.

    The strongest result requires successful exact-head runtime CI plus at least one
    supported static changed-dependency consumption. Direct package exercise is recorded
    independently and is not required for coverage support.
    """

    if not workflow_inputs:
        return DependencyCICoverageResult(
            state="no_successful_ci",
            reason="no_exact_head_workflows",
            detail="No pull-request workflow runs were available for the exact head SHA.",
            workflows=(),
        )

    results = tuple(
        _evaluate_workflow_dependency_coverage(
            dependency,
            workflow_input,
            source_contexts=source_contexts,
        )
        for workflow_input in workflow_inputs
    )

    supported = next(
        (result for result in results if result.state == "supported_not_correlated"),
        None,
    )
    if supported is not None:
        return DependencyCICoverageResult(
            state="supported_not_correlated",
            reason="successful_exact_head_ci_with_static_dependency_consumption",
            detail=(
                f"Successful exact-head CI evidence exists for workflow "
                f"{supported.workflow_name!r}, and its exact static definition contains "
                "supported changed-dependency consumption. The static consuming "
                "declaration is not correlated to runtime job/step execution or success."
            ),
            workflows=results,
        )

    has_successful_job = any(
        job.status == "completed" and job.conclusion == "success"
        for workflow_input in workflow_inputs
        for job in workflow_input.jobs
    )
    if not has_successful_job:
        return DependencyCICoverageResult(
            state="no_successful_ci",
            reason="no_successful_exact_head_jobs",
            detail="No completed successful exact-head job was available.",
            workflows=results,
        )

    return DependencyCICoverageResult(
        state="unresolved",
        reason="dependency_consumption_not_established",
        detail=(
            "Successful exact-head CI exists, but the admitted static evidence does not "
            "establish changed-dependency consumption in a readable CI environment."
        ),
        workflows=results,
    )


def _evaluate_workflow_dependency_coverage(
    dependency: DependencyVersionChange,
    workflow_input: WorkflowDependencyExerciseInput,
    *,
    source_contexts: Sequence[DependencySourceContext],
) -> WorkflowDependencyCoverageResult:
    run = workflow_input.run
    definition = workflow_input.definition
    workflow_path = definition.path

    successful_jobs = tuple(
        job
        for job in workflow_input.jobs
        if job.status == "completed" and job.conclusion == "success"
    )
    runtime_success = (
        bool(successful_jobs)
        and run.status == "completed"
        and run.conclusion == "success"
    )

    if isinstance(definition, UnavailableRepositoryFile):
        return WorkflowDependencyCoverageResult(
            workflow_name=run.name,
            workflow_path=workflow_path,
            state="no_successful_ci" if not successful_jobs else "unresolved",
            reason=(
                "no_successful_jobs"
                if not successful_jobs
                else "workflow_definition_unavailable"
            ),
            detail=(
                "The workflow had no completed successful job record."
                if not successful_jobs
                else definition.detail
            ),
            consumption_state="unresolved",
            consumption_reason="workflow_definition_unavailable",
            consumption_detail=definition.detail,
            direct_exercise_state="unresolved",
            direct_exercise_reason="workflow_definition_unavailable",
            direct_exercise_detail=definition.detail,
        )

    assert isinstance(definition, RepositoryTextFile)
    if definition.revision != run.head_sha:
        detail = "Workflow definition revision did not match the run head SHA."
        return WorkflowDependencyCoverageResult(
            workflow_name=run.name,
            workflow_path=workflow_path,
            state="no_successful_ci" if not successful_jobs else "unresolved",
            reason=("no_successful_jobs" if not successful_jobs else "workflow_definition_revision_mismatch"),
            detail=(
                "The workflow had no completed successful job record."
                if not successful_jobs
                else detail
            ),
            consumption_state="unresolved",
            consumption_reason="workflow_definition_revision_mismatch",
            consumption_detail=detail,
            direct_exercise_state="unresolved",
            direct_exercise_reason="workflow_definition_revision_mismatch",
            direct_exercise_detail=detail,
        )

    static = inspect_workflow_dependency_evidence(
        definition,
        source_contexts=source_contexts,
        package=dependency.package,
        normalized_package=dependency.normalized_package,
        external_consumptions=workflow_input.external_consumptions,
    )
    consumption_state, consumption_reason, consumption_detail, selected_consumption = (
        _classify_static_consumption(static)
    )
    exercise_state, exercise_reason, exercise_detail, selected_invocation = (
        _classify_direct_exercise(static, consumption_state)
    )

    if not successful_jobs:
        return _coverage_result(
            run,
            workflow_path,
            state="no_successful_ci",
            reason="no_successful_jobs",
            detail="The workflow had no completed successful job record.",
            static=static,
            consumption_state=consumption_state,
            consumption_reason=consumption_reason,
            consumption_detail=consumption_detail,
            exercise_state=exercise_state,
            exercise_reason=exercise_reason,
            exercise_detail=exercise_detail,
            selected_consumption=selected_consumption,
            selected_invocation=selected_invocation,
        )

    if not runtime_success:
        return _coverage_result(
            run,
            workflow_path,
            state="unresolved",
            reason="workflow_not_successful",
            detail=(
                "A completed successful job exists, but the workflow run was not "
                f"completed-successful; conclusion was {run.conclusion!r}."
            ),
            static=static,
            consumption_state=consumption_state,
            consumption_reason=consumption_reason,
            consumption_detail=consumption_detail,
            exercise_state=exercise_state,
            exercise_reason=exercise_reason,
            exercise_detail=exercise_detail,
            selected_consumption=selected_consumption,
            selected_invocation=selected_invocation,
        )

    if consumption_state == "supported":
        return _coverage_result(
            run,
            workflow_path,
            state="supported_not_correlated",
            reason="successful_ci_with_static_dependency_consumption",
            detail=(
                "The exact-head workflow/run has successful runtime evidence and its "
                "static definition contains supported changed-dependency consumption. "
                "Static job/step execution is not correlated to runtime evidence."
            ),
            static=static,
            consumption_state=consumption_state,
            consumption_reason=consumption_reason,
            consumption_detail=consumption_detail,
            exercise_state=exercise_state,
            exercise_reason=exercise_reason,
            exercise_detail=exercise_detail,
            selected_consumption=selected_consumption,
            selected_invocation=selected_invocation,
        )

    return _coverage_result(
        run,
        workflow_path,
        state="unresolved",
        reason="static_dependency_consumption_not_supported",
        detail=(
            "The workflow has successful exact-head runtime evidence, but static "
            "changed-dependency consumption is not established."
        ),
        static=static,
        consumption_state=consumption_state,
        consumption_reason=consumption_reason,
        consumption_detail=consumption_detail,
        exercise_state=exercise_state,
        exercise_reason=exercise_reason,
        exercise_detail=exercise_detail,
        selected_consumption=selected_consumption,
        selected_invocation=selected_invocation,
    )


def _classify_static_consumption(
    static: WorkflowStaticDependencyEvidence,
) -> tuple[
    StaticCIEvidenceState,
    str,
    str,
    StaticDependencyConsumptionEvidence | None,
]:
    supported = next(
        (item for item in static.consumptions if item.state == "supported"),
        None,
    )
    if supported is not None:
        return "supported", supported.reason, supported.detail, supported

    unresolved = next(
        (item for item in static.consumptions if item.state == "unresolved"),
        None,
    )
    if unresolved is not None:
        return "unresolved", unresolved.reason, unresolved.detail, unresolved

    if static.problems:
        problem = static.problems[0]
        return "unresolved", problem.reason, problem.detail, None

    not_established = next(
        (item for item in static.consumptions if item.state == "not_established"),
        None,
    )
    if not_established is not None:
        return (
            "not_established",
            not_established.reason,
            not_established.detail,
            not_established,
        )

    return (
        "not_established",
        "static_dependency_consumption_not_observed",
        "No admitted static changed-dependency consumption declaration was established.",
        None,
    )


def _classify_direct_exercise(
    static: WorkflowStaticDependencyEvidence,
    consumption_state: StaticCIEvidenceState,
) -> tuple[
    StaticCIEvidenceState,
    str,
    str,
    DirectPackageInvocationEvidence | None,
]:
    supported_consumptions = tuple(
        item for item in static.consumptions if item.state == "supported"
    )
    for consumption in supported_consumptions:
        location = (consumption.step_source_index, consumption.segment_index)
        later_invocation = next(
            (
                invocation
                for invocation in static.invocations
                if invocation.job_key == consumption.job_key
                and location
                < (invocation.step_source_index, invocation.segment_index)
            ),
            None,
        )
        if later_invocation is not None:
            return (
                "supported",
                "direct_package_invocation_after_consumption",
                (
                    "The static job directly invokes the changed package after a "
                    "supported dependency-consumption declaration. Runtime execution "
                    "is not established."
                ),
                later_invocation,
            )

    if consumption_state == "unresolved":
        return (
            "unresolved",
            "direct_exercise_prerequisite_unresolved",
            "Direct exercise cannot be established while static consumption is unresolved.",
            None,
        )

    if supported_consumptions and static.invocations:
        return (
            "not_established",
            "direct_invocation_not_after_supported_consumption",
            (
                "Direct package invocation is visible, but no invocation is ordered "
                "after supported consumption in the same static job."
            ),
            static.invocations[0],
        )

    return (
        "not_established",
        "direct_package_exercise_not_observed",
        (
            "No admitted direct changed-package invocation is ordered after supported "
            "static dependency consumption in the same job."
        ),
        None,
    )


def _coverage_result(
    run: WorkflowRun,
    workflow_path: str,
    *,
    state: DependencyCICoverageState,
    reason: str,
    detail: str,
    static: WorkflowStaticDependencyEvidence,
    consumption_state: StaticCIEvidenceState,
    consumption_reason: str,
    consumption_detail: str,
    exercise_state: StaticCIEvidenceState,
    exercise_reason: str,
    exercise_detail: str,
    selected_consumption: StaticDependencyConsumptionEvidence | None,
    selected_invocation: DirectPackageInvocationEvidence | None,
) -> WorkflowDependencyCoverageResult:
    return WorkflowDependencyCoverageResult(
        workflow_name=run.name,
        workflow_path=workflow_path,
        state=state,
        reason=reason,
        detail=detail,
        consumption_state=consumption_state,
        consumption_reason=consumption_reason,
        consumption_detail=consumption_detail,
        direct_exercise_state=exercise_state,
        direct_exercise_reason=exercise_reason,
        direct_exercise_detail=exercise_detail,
        consumption_command=(
            selected_consumption.command if selected_consumption is not None else None
        ),
        execution_command=(
            selected_invocation.command if selected_invocation is not None else None
        ),
        consumptions=static.consumptions,
        invocations=static.invocations,
    )


# ---------------------------------------------------------------------------
# Legacy Cluster-4-and-earlier evaluator, retained until Cluster 6 migration.
# ---------------------------------------------------------------------------

def evaluate_dependency_ci_exercise(
    dependency: DependencyVersionChange,
    workflow_inputs: Sequence[WorkflowDependencyExerciseInput],
    *,
    direct_requirements_install_path: str | None,
) -> DependencyCIExerciseResult:
    """Classify the accepted legacy direct-requirements exercise path."""

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
    """Combine one workflow's runtime authority with its legacy exact static definition."""

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
                "the legacy CI rule. Generic dependency evidence paths were not "
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
    "DependencyCICoverageResult",
    "DependencyCICoverageState",
    "DependencyCIExerciseResult",
    "DependencyCIExerciseState",
    "StaticCIEvidenceState",
    "WorkflowDependencyCoverageResult",
    "WorkflowDependencyExerciseInput",
    "WorkflowDependencyExerciseResult",
    "evaluate_dependency_ci_coverage",
    "evaluate_dependency_ci_exercise",
)
