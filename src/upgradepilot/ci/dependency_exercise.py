"""Interpret exact-head CI evidence for one canonical dependency change.

The coverage path keeps four propositions distinct:

* successful exact-head runtime workflow/job authority;
* static changed-dependency consumption;
* stronger static direct changed-package exercise;
* bounded correlation from those static job/step locations to factual runtime steps.

Static consumption may be established by direct requirements installation or by a typed
project-environment selection/membership composition. Direct exercise additionally requires
a package invocation ordered after supported consumption in the same static job. Runtime
correlation can strengthen either static proposition only when the owning user-defined run
step is safely matched to a completed-successful runtime step without continue-on-error
masking. It still does not prove exact resolved versions, wheel selection, or compatibility.
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
from ..github.workflow_definition import RunStepDefinition
from .consumption import StaticDependencyConsumptionEvidence
from .workflow_commands import (
    DirectPackageInvocationEvidence,
    StaticWorkflowDependencyProblem,
    WorkflowStaticDependencyEvidence,
    inspect_workflow_dependency_evidence,
)
from .workflow_runtime_correlation import (
    WorkflowRuntimeCorrelationResult,
    WorkflowRuntimeStepCorrelation,
    correlate_workflow_runtime,
)


type DependencyCICoverageState = Literal[
    "supported_runtime_correlated",
    "supported_not_correlated",
    "no_successful_ci",
    "unresolved",
]
type StaticCIEvidenceState = Literal["supported", "not_established", "unresolved"]
type RuntimeCIEvidenceState = Literal["supported", "not_established", "unresolved"]


@dataclass(frozen=True, slots=True)
class WorkflowDependencyCoverageInput:
    """Runtime run/jobs plus exact static definition and project-environment consumptions.

    Direct-requirements consumption is derived from typed source contexts by the static
    workflow owner. ``project_environment_consumptions`` carries the separately composed
    R3→dependency-domain→R5 evidence needed by this workflow's coverage classification.
    """

    run: WorkflowRun
    jobs: tuple[WorkflowJob, ...]
    definition: RepositoryFileEvidence
    project_environment_consumptions: tuple[StaticDependencyConsumptionEvidence, ...] = ()


@dataclass(frozen=True, slots=True)
class WorkflowDependencyCoverageResult:
    """Workflow-scoped static/runtime evidence with proof axes kept explicit."""

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
    runtime_consumption_state: RuntimeCIEvidenceState
    runtime_consumption_reason: str
    runtime_consumption_detail: str
    runtime_direct_exercise_state: RuntimeCIEvidenceState
    runtime_direct_exercise_reason: str
    runtime_direct_exercise_detail: str
    runtime_correlation: WorkflowRuntimeCorrelationResult | None = None
    consumption_command: str | None = None
    execution_command: str | None = None
    consumptions: tuple[StaticDependencyConsumptionEvidence, ...] = ()
    invocations: tuple[DirectPackageInvocationEvidence, ...] = ()
    problems: tuple[StaticWorkflowDependencyProblem, ...] = ()


@dataclass(frozen=True, slots=True)
class DependencyCICoverageResult:
    """Aggregate CI coverage evidence preserving heterogeneous workflow results."""

    state: DependencyCICoverageState
    reason: str
    detail: str
    workflows: tuple[WorkflowDependencyCoverageResult, ...]


def evaluate_dependency_ci_coverage(
    dependency: DependencyVersionChange,
    workflow_inputs: Sequence[WorkflowDependencyCoverageInput],
    *,
    source_contexts: Sequence[DependencySourceContext],
) -> DependencyCICoverageResult:
    """Classify CI dependency coverage without inflating the correlation claim.

    ``supported_runtime_correlated`` means at least one supported static dependency-
    consumption step was deterministically matched to an exact-attempt runtime step that
    GitHub reports completed successfully, with no statically visible continue-on-error
    masking. It does not mean the dependency version, wheel, or behavior was proven.
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

    runtime_correlated = next(
        (result for result in results if result.state == "supported_runtime_correlated"),
        None,
    )
    if runtime_correlated is not None:
        return DependencyCICoverageResult(
            state="supported_runtime_correlated",
            reason="successful_exact_head_ci_with_runtime_correlated_dependency_consumption",
            detail=(
                f"Workflow {runtime_correlated.workflow_name!r} contains supported static "
                "changed-dependency consumption whose owning user-defined run step is "
                "correlated to a completed-successful runtime step for the exact run attempt."
            ),
            workflows=results,
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
                "declaration is not safely correlated to successful runtime step execution."
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

    runtime_execution_unresolved = next(
        (
            result
            for result in results
            if result.reason
            in {
                "correlated_dependency_consumption_execution_not_successful",
                "correlated_dependency_consumption_execution_unresolved",
            }
        ),
        None,
    )
    if runtime_execution_unresolved is not None:
        return DependencyCICoverageResult(
            state="unresolved",
            reason=runtime_execution_unresolved.reason,
            detail=runtime_execution_unresolved.detail,
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
    workflow_input: WorkflowDependencyCoverageInput,
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
            runtime_consumption_state="unresolved",
            runtime_consumption_reason="workflow_definition_unavailable",
            runtime_consumption_detail=definition.detail,
            runtime_direct_exercise_state="unresolved",
            runtime_direct_exercise_reason="workflow_definition_unavailable",
            runtime_direct_exercise_detail=definition.detail,
        )

    assert isinstance(definition, RepositoryTextFile)
    if definition.revision != run.head_sha:
        detail = "Workflow definition revision did not match the run head SHA."
        return WorkflowDependencyCoverageResult(
            workflow_name=run.name,
            workflow_path=workflow_path,
            state="no_successful_ci" if not successful_jobs else "unresolved",
            reason=(
                "no_successful_jobs"
                if not successful_jobs
                else "workflow_definition_revision_mismatch"
            ),
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
            runtime_consumption_state="unresolved",
            runtime_consumption_reason="workflow_definition_revision_mismatch",
            runtime_consumption_detail=detail,
            runtime_direct_exercise_state="unresolved",
            runtime_direct_exercise_reason="workflow_definition_revision_mismatch",
            runtime_direct_exercise_detail=detail,
        )

    static = inspect_workflow_dependency_evidence(
        definition,
        source_contexts=source_contexts,
        package=dependency.package,
        normalized_package=dependency.normalized_package,
        project_environment_consumptions=(
            workflow_input.project_environment_consumptions
        ),
    )
    consumption_state, consumption_reason, consumption_detail, selected_consumption = (
        _classify_static_consumption(static)
    )
    exercise_state, exercise_reason, exercise_detail, selected_invocation = (
        _classify_direct_exercise(static, consumption_state)
    )

    correlation = correlate_workflow_runtime(
        definition,
        run,
        workflow_input.jobs,
    )
    (
        runtime_consumption_state,
        runtime_consumption_reason,
        runtime_consumption_detail,
    ) = _classify_runtime_step_execution(
        correlation,
        static_state=consumption_state,
        locations=_supported_consumption_locations(static),
        evidence_label="dependency consumption",
    )
    (
        runtime_exercise_state,
        runtime_exercise_reason,
        runtime_exercise_detail,
    ) = _classify_runtime_step_execution(
        correlation,
        static_state=exercise_state,
        locations=_supported_direct_exercise_locations(static),
        evidence_label="direct package exercise",
    )

    common_runtime = {
        "runtime_consumption_state": runtime_consumption_state,
        "runtime_consumption_reason": runtime_consumption_reason,
        "runtime_consumption_detail": runtime_consumption_detail,
        "runtime_direct_exercise_state": runtime_exercise_state,
        "runtime_direct_exercise_reason": runtime_exercise_reason,
        "runtime_direct_exercise_detail": runtime_exercise_detail,
        "runtime_correlation": correlation,
    }

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
            **common_runtime,
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
            **common_runtime,
        )

    if consumption_state == "supported":
        if correlation.state != "correlated":
            return _coverage_result(
                run,
                workflow_path,
                state="supported_not_correlated",
                reason="successful_ci_with_static_dependency_consumption",
                detail=(
                    "The exact-head workflow/run has successful runtime evidence and its "
                    "static definition contains supported changed-dependency consumption, "
                    "but the bounded static↔runtime bridge could not safely correlate the "
                    f"workflow: {correlation.reason}."
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
                **common_runtime,
            )

        if runtime_consumption_state == "supported":
            return _coverage_result(
                run,
                workflow_path,
                state="supported_runtime_correlated",
                reason="successful_ci_with_runtime_correlated_dependency_consumption",
                detail=(
                    "The exact-head workflow/run has successful runtime evidence, and at "
                    "least one supported static changed-dependency consumption step is "
                    "correlated to a completed-successful runtime step without visible "
                    "continue-on-error masking."
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
                **common_runtime,
            )

        runtime_reason = (
            "correlated_dependency_consumption_execution_unresolved"
            if runtime_consumption_state == "unresolved"
            else "correlated_dependency_consumption_execution_not_successful"
        )
        return _coverage_result(
            run,
            workflow_path,
            state="unresolved",
            reason=runtime_reason,
            detail=runtime_consumption_detail,
            static=static,
            consumption_state=consumption_state,
            consumption_reason=consumption_reason,
            consumption_detail=consumption_detail,
            exercise_state=exercise_state,
            exercise_reason=exercise_reason,
            exercise_detail=exercise_detail,
            selected_consumption=selected_consumption,
            selected_invocation=selected_invocation,
            **common_runtime,
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
        **common_runtime,
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
                    "is classified separately."
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


def _supported_consumption_locations(
    static: WorkflowStaticDependencyEvidence,
) -> tuple[tuple[str, int], ...]:
    return _deduplicated_step_locations(
        (item.job_key, item.step_source_index)
        for item in static.consumptions
        if item.state == "supported"
    )


def _supported_direct_exercise_locations(
    static: WorkflowStaticDependencyEvidence,
) -> tuple[tuple[str, int], ...]:
    supported_consumptions = tuple(
        item for item in static.consumptions if item.state == "supported"
    )
    return _deduplicated_step_locations(
        (invocation.job_key, invocation.step_source_index)
        for invocation in static.invocations
        if any(
            consumption.job_key == invocation.job_key
            and (consumption.step_source_index, consumption.segment_index)
            < (invocation.step_source_index, invocation.segment_index)
            for consumption in supported_consumptions
        )
    )


def _deduplicated_step_locations(
    locations: Sequence[tuple[str, int]] | object,
) -> tuple[tuple[str, int], ...]:
    # Accept any finite iterable internally while preserving first-observed static order.
    seen: set[tuple[str, int]] = set()
    result: list[tuple[str, int]] = []
    for location in locations:  # type: ignore[union-attr]
        if location in seen:
            continue
        seen.add(location)
        result.append(location)
    return tuple(result)


def _classify_runtime_step_execution(
    correlation: WorkflowRuntimeCorrelationResult,
    *,
    static_state: StaticCIEvidenceState,
    locations: tuple[tuple[str, int], ...],
    evidence_label: str,
) -> tuple[RuntimeCIEvidenceState, str, str]:
    if static_state == "unresolved":
        return (
            "unresolved",
            f"static_{evidence_label.replace(' ', '_')}_unresolved",
            f"Runtime {evidence_label} cannot be strengthened while static evidence is unresolved.",
        )
    if static_state != "supported" or not locations:
        return (
            "not_established",
            f"static_{evidence_label.replace(' ', '_')}_not_supported",
            f"No supported static {evidence_label} location is available for runtime correlation.",
        )
    if correlation.state != "correlated":
        return (
            "unresolved",
            "workflow_runtime_correlation_unresolved",
            (
                f"Static {evidence_label} exists, but workflow runtime correlation is "
                f"unresolved: {correlation.reason}: {correlation.detail}"
            ),
        )

    unresolved_detail: str | None = None
    observed_non_success: list[str] = []
    for job_key, step_source_index in locations:
        step_correlation = _find_correlated_step(
            correlation,
            job_key=job_key,
            step_source_index=step_source_index,
        )
        if step_correlation is None:
            unresolved_detail = (
                f"Correlated workflow did not retain static location {job_key!r} step "
                f"{step_source_index}."
            )
            continue

        static_step = step_correlation.static_step
        if not isinstance(static_step, RunStepDefinition):
            unresolved_detail = (
                f"Static {evidence_label} location {job_key!r} step {step_source_index} "
                "did not resolve to a run step."
            )
            continue

        continue_on_error = static_step.continue_on_error
        if continue_on_error is not None and (
            continue_on_error.contains_expression
            or continue_on_error.text.strip().casefold() != "false"
        ):
            unresolved_detail = (
                f"Static {evidence_label} step {job_key!r}/{step_source_index} has "
                "continue-on-error semantics that prevent treating runtime conclusion "
                "success as an unmasked successful outcome."
            )
            continue

        runtime_step = step_correlation.runtime_step
        if runtime_step.status == "completed" and runtime_step.conclusion == "success":
            return (
                "supported",
                f"runtime_correlated_{evidence_label.replace(' ', '_')}_step_succeeded",
                (
                    f"Static {evidence_label} step {job_key!r}/{step_source_index} is "
                    f"correlated to runtime step {runtime_step.number} and GitHub reports "
                    "completed/success."
                ),
            )

        observed_non_success.append(
            (
                f"{job_key!r}/{step_source_index} -> runtime step {runtime_step.number} "
                f"status={runtime_step.status!r}, conclusion={runtime_step.conclusion!r}"
            )
        )

    if unresolved_detail is not None:
        return (
            "unresolved",
            f"runtime_{evidence_label.replace(' ', '_')}_interpretation_unresolved",
            unresolved_detail,
        )

    return (
        "not_established",
        f"runtime_correlated_{evidence_label.replace(' ', '_')}_step_not_successful",
        (
            f"Correlated {evidence_label} step(s) were available, but none had an "
            "admissible completed/success result: "
            + "; ".join(observed_non_success)
        ),
    )


def _find_correlated_step(
    correlation: WorkflowRuntimeCorrelationResult,
    *,
    job_key: str,
    step_source_index: int,
) -> WorkflowRuntimeStepCorrelation | None:
    for job in correlation.jobs:
        if job.static_job.key != job_key:
            continue
        return next(
            (
                step
                for step in job.steps
                if step.static_step.source_index == step_source_index
            ),
            None,
        )
    return None


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
    runtime_consumption_state: RuntimeCIEvidenceState,
    runtime_consumption_reason: str,
    runtime_consumption_detail: str,
    runtime_direct_exercise_state: RuntimeCIEvidenceState,
    runtime_direct_exercise_reason: str,
    runtime_direct_exercise_detail: str,
    runtime_correlation: WorkflowRuntimeCorrelationResult,
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
        runtime_consumption_state=runtime_consumption_state,
        runtime_consumption_reason=runtime_consumption_reason,
        runtime_consumption_detail=runtime_consumption_detail,
        runtime_direct_exercise_state=runtime_direct_exercise_state,
        runtime_direct_exercise_reason=runtime_direct_exercise_reason,
        runtime_direct_exercise_detail=runtime_direct_exercise_detail,
        runtime_correlation=runtime_correlation,
        consumption_command=(
            selected_consumption.command if selected_consumption is not None else None
        ),
        execution_command=(
            selected_invocation.command if selected_invocation is not None else None
        ),
        consumptions=static.consumptions,
        invocations=static.invocations,
        problems=static.problems,
    )


__all__ = (
    "DependencyCICoverageResult",
    "DependencyCICoverageState",
    "RuntimeCIEvidenceState",
    "StaticCIEvidenceState",
    "WorkflowDependencyCoverageInput",
    "WorkflowDependencyCoverageResult",
    "evaluate_dependency_ci_coverage",
)
