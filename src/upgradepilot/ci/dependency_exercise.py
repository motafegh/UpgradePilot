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
from .runtime_strengthening import (
    RuntimeStrengtheningCandidate,
    candidate_from_consumption,
    candidate_from_direct_exercise,
    classify_runtime_strengthening_eligibility,
)
from .static_command_order import relate_invocation_after_consumption
from .workflow_commands import (
    DirectPackageInvocationEvidence,
    StaticWorkflowDependencyProblem,
    WorkflowProjectEnvironmentSource,
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
type _RuntimeStrengtheningBasis = Literal[
    "supported",
    "eligibility_ineligible",
    "eligibility_unresolved",
    "workflow_correlation_unresolved",
    "step_correlation_unresolved",
    "continue_on_error_unresolved",
    "runtime_non_success",
]
type _RuntimeStrengtheningDisposition = Literal[
    "supported",
    "static_fallback",
    "broader_unresolved",
]


@dataclass(frozen=True, slots=True)
class _RuntimeStrengtheningCandidateResult:
    state: RuntimeCIEvidenceState
    basis: _RuntimeStrengtheningBasis
    reason: str
    detail: str
    runtime_status: str | None = None
    runtime_conclusion: str | None = None
    runtime_step_number: int | None = None


@dataclass(frozen=True, slots=True)
class _RuntimeStrengtheningAggregate:
    state: RuntimeCIEvidenceState
    disposition: _RuntimeStrengtheningDisposition
    reason: str
    detail: str
    candidates: tuple[_RuntimeStrengtheningCandidateResult, ...] = ()


@dataclass(frozen=True, slots=True)
class WorkflowDependencyCoverageInput:
    """Runtime run/jobs plus exact static definition and project-environment sources.

    The normal production path supplies exact ``project_environment_sources`` so the static
    workflow owner can derive direct requirements, project-environment consumption, and
    package invocation in one traversal. ``project_environment_consumptions`` remains only as
    a temporary Cycle 2 compatibility seam for focused synthetic tests.
    """

    run: WorkflowRun
    jobs: tuple[WorkflowJob, ...]
    definition: RepositoryFileEvidence
    project_environment_sources: tuple[WorkflowProjectEnvironmentSource, ...] = ()
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
        project_environment_sources=workflow_input.project_environment_sources,
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
    runtime_consumption = _classify_runtime_strengthening(
        correlation,
        static_state=consumption_state,
        candidates=_supported_consumption_candidates(static),
        evidence_label="dependency consumption",
    )
    runtime_exercise = _classify_runtime_strengthening(
        correlation,
        static_state=exercise_state,
        candidates=_supported_direct_exercise_candidates(static),
        evidence_label="direct package exercise",
    )

    common_runtime = {
        "runtime_consumption_state": runtime_consumption.state,
        "runtime_consumption_reason": runtime_consumption.reason,
        "runtime_consumption_detail": runtime_consumption.detail,
        "runtime_direct_exercise_state": runtime_exercise.state,
        "runtime_direct_exercise_reason": runtime_exercise.reason,
        "runtime_direct_exercise_detail": runtime_exercise.detail,
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
        if runtime_consumption.state == "supported":
            return _coverage_result(
                run,
                workflow_path,
                state="supported_runtime_correlated",
                reason="successful_ci_with_runtime_correlated_dependency_consumption",
                detail=(
                    "The exact-head workflow/run has successful runtime evidence, and at "
                    "least one exact eligible static changed-dependency consumption "
                    "occurrence earns bounded Runtime-Correlated Support."
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

        if runtime_consumption.disposition == "static_fallback":
            return _coverage_result(
                run,
                workflow_path,
                state="supported_not_correlated",
                reason="successful_ci_with_static_dependency_consumption",
                detail=runtime_consumption.detail,
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
            if runtime_consumption.state == "unresolved"
            else "correlated_dependency_consumption_execution_not_successful"
        )
        return _coverage_result(
            run,
            workflow_path,
            state="unresolved",
            reason=runtime_reason,
            detail=runtime_consumption.detail,
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
    observed_invocations = tuple(
        item for item in static.invocations if item.state == "observed"
    )

    unresolved_relation: DirectPackageInvocationEvidence | None = None
    for consumption in supported_consumptions:
        for invocation in observed_invocations:
            relation = relate_invocation_after_consumption(consumption, invocation)
            if relation == "ordered_after":
                return (
                    "supported",
                    "direct_package_invocation_after_consumption",
                    (
                        "The static job directly invokes the changed package after a "
                        "supported dependency-consumption declaration. Runtime execution "
                        "is classified separately."
                    ),
                    invocation,
                )
            if relation == "unresolved" and unresolved_relation is None:
                unresolved_relation = invocation

    if consumption_state == "unresolved":
        return (
            "unresolved",
            "direct_exercise_prerequisite_unresolved",
            "Direct exercise cannot be established while static consumption is unresolved.",
            None,
        )

    unresolved_target = _first_relevant_unresolved_invocation(
        supported_consumptions,
        static.invocations,
    )
    if unresolved_relation is not None or unresolved_target is not None:
        selected = unresolved_relation or unresolved_target
        return (
            "unresolved",
            "direct_invocation_order_or_target_unresolved",
            (
                "A direct package invocation candidate is visible after, or may be after, "
                "supported consumption, but its package target or same-step static ordering "
                "cannot be established within the bounded rule."
            ),
            selected,
        )

    if supported_consumptions and observed_invocations:
        return (
            "not_established",
            "direct_invocation_not_after_supported_consumption",
            (
                "Direct package invocation is visible, but no invocation is ordered "
                "after supported consumption in the same static job."
            ),
            observed_invocations[0],
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


def _first_relevant_unresolved_invocation(
    supported_consumptions: tuple[StaticDependencyConsumptionEvidence, ...],
    invocations: tuple[DirectPackageInvocationEvidence, ...],
) -> DirectPackageInvocationEvidence | None:
    for invocation in invocations:
        if invocation.state != "unresolved":
            continue
        for consumption in supported_consumptions:
            relation = relate_invocation_after_consumption(consumption, invocation)
            if relation in {"ordered_after", "unresolved"}:
                return invocation
    return None


def _supported_consumption_candidates(
    static: WorkflowStaticDependencyEvidence,
) -> tuple[RuntimeStrengtheningCandidate, ...]:
    return _deduplicated_runtime_candidates(
        candidate_from_consumption(item)
        for item in static.consumptions
        if item.state == "supported"
    )


def _supported_direct_exercise_candidates(
    static: WorkflowStaticDependencyEvidence,
) -> tuple[RuntimeStrengtheningCandidate, ...]:
    supported_consumptions = tuple(
        item for item in static.consumptions if item.state == "supported"
    )
    return _deduplicated_runtime_candidates(
        candidate_from_direct_exercise(invocation)
        for invocation in static.invocations
        if invocation.state == "observed"
        and any(
            relate_invocation_after_consumption(consumption, invocation)
            == "ordered_after"
            for consumption in supported_consumptions
        )
    )


def _deduplicated_runtime_candidates(
    candidates: Sequence[RuntimeStrengtheningCandidate] | object,
) -> tuple[RuntimeStrengtheningCandidate, ...]:
    seen: set[tuple[object, ...]] = set()
    result: list[RuntimeStrengtheningCandidate] = []
    for candidate in candidates:  # type: ignore[union-attr]
        key = (
            candidate.workflow_path,
            candidate.workflow_revision,
            candidate.job_key,
            candidate.step_source_index,
            candidate.command_location,
            candidate.proposition_kind,
        )
        if key in seen:
            continue
        seen.add(key)
        result.append(candidate)
    return tuple(result)


def _classify_runtime_strengthening(
    correlation: WorkflowRuntimeCorrelationResult,
    *,
    static_state: StaticCIEvidenceState,
    candidates: tuple[RuntimeStrengtheningCandidate, ...],
    evidence_label: str,
) -> _RuntimeStrengtheningAggregate:
    if static_state == "unresolved":
        return _RuntimeStrengtheningAggregate(
            state="unresolved",
            disposition="broader_unresolved",
            reason=f"static_{evidence_label.replace(' ', '_')}_unresolved",
            detail=(
                f"Runtime {evidence_label} cannot be strengthened while static evidence "
                "itself is unresolved."
            ),
        )
    if static_state != "supported" or not candidates:
        return _RuntimeStrengtheningAggregate(
            state="not_established",
            disposition="broader_unresolved",
            reason=f"static_{evidence_label.replace(' ', '_')}_not_supported",
            detail=(
                f"No supported exact static {evidence_label} occurrence is available for "
                "runtime strengthening."
            ),
        )

    if correlation.state != "correlated":
        detail = (
            f"Supported static {evidence_label} exists, but the bounded workflow runtime "
            f"bridge is unavailable: {correlation.reason}: {correlation.detail}"
        )
        candidate_results = tuple(
            _RuntimeStrengtheningCandidateResult(
                state="unresolved",
                basis="workflow_correlation_unresolved",
                reason="workflow_runtime_correlation_unresolved",
                detail=detail,
            )
            for _ in candidates
        )
        return _RuntimeStrengtheningAggregate(
            state="unresolved",
            disposition="static_fallback",
            reason="workflow_runtime_correlation_unresolved",
            detail=detail,
            candidates=candidate_results,
        )

    results = tuple(
        _classify_runtime_strengthening_candidate(
            candidate,
            correlation=correlation,
            evidence_label=evidence_label,
        )
        for candidate in candidates
    )

    supported = next((item for item in results if item.state == "supported"), None)
    if supported is not None:
        return _RuntimeStrengtheningAggregate(
            state="supported",
            disposition="supported",
            reason=supported.reason,
            detail=supported.detail,
            candidates=results,
        )

    material_runtime = next(
        (
            item
            for item in results
            if item.basis
            in {
                "step_correlation_unresolved",
                "continue_on_error_unresolved",
                "runtime_non_success",
            }
        ),
        None,
    )
    if material_runtime is not None:
        state: RuntimeCIEvidenceState = (
            "unresolved"
            if any(item.state == "unresolved" for item in results)
            else "not_established"
        )
        return _RuntimeStrengtheningAggregate(
            state=state,
            disposition="broader_unresolved",
            reason=material_runtime.reason,
            detail=_runtime_candidate_result_summary(results),
            candidates=results,
        )

    if any(item.state == "unresolved" for item in results):
        unresolved = next(item for item in results if item.state == "unresolved")
        return _RuntimeStrengtheningAggregate(
            state="unresolved",
            disposition="static_fallback",
            reason=unresolved.reason,
            detail=_runtime_candidate_result_summary(results),
            candidates=results,
        )

    not_established = results[0]
    return _RuntimeStrengtheningAggregate(
        state="not_established",
        disposition="static_fallback",
        reason=not_established.reason,
        detail=_runtime_candidate_result_summary(results),
        candidates=results,
    )


def _classify_runtime_strengthening_candidate(
    candidate: RuntimeStrengtheningCandidate,
    *,
    correlation: WorkflowRuntimeCorrelationResult,
    evidence_label: str,
) -> _RuntimeStrengtheningCandidateResult:
    eligibility = classify_runtime_strengthening_eligibility(candidate)

    if eligibility.state == "ineligible":
        return _RuntimeStrengtheningCandidateResult(
            state="not_established",
            basis="eligibility_ineligible",
            reason=eligibility.reason,
            detail=eligibility.detail,
        )

    if eligibility.state == "unresolved":
        return _RuntimeStrengtheningCandidateResult(
            state="unresolved",
            basis="eligibility_unresolved",
            reason=eligibility.reason,
            detail=eligibility.detail,
        )

    step_correlation = _find_correlated_step(
        correlation,
        job_key=candidate.job_key,
        step_source_index=candidate.step_source_index,
    )
    if step_correlation is None:
        return _RuntimeStrengtheningCandidateResult(
            state="unresolved",
            basis="step_correlation_unresolved",
            reason="runtime_strengthening_exact_step_missing",
            detail=(
                f"The workflow bridge is correlated, but exact eligible {evidence_label} "
                f"occurrence {candidate.job_key!r}/{candidate.step_source_index} has no "
                "retained owning runtime-step correlation."
            ),
        )

    static_step = step_correlation.static_step
    if not isinstance(static_step, RunStepDefinition):
        return _RuntimeStrengtheningCandidateResult(
            state="unresolved",
            basis="step_correlation_unresolved",
            reason="runtime_strengthening_static_step_not_run_step",
            detail=(
                f"Exact eligible {evidence_label} occurrence "
                f"{candidate.job_key!r}/{candidate.step_source_index} did not resolve to "
                "a static run step."
            ),
        )

    runtime_step = step_correlation.runtime_step
    continue_on_error = static_step.continue_on_error
    if continue_on_error is not None and (
        continue_on_error.contains_expression
        or continue_on_error.text.strip().casefold() != "false"
    ):
        return _RuntimeStrengtheningCandidateResult(
            state="unresolved",
            basis="continue_on_error_unresolved",
            reason="runtime_strengthening_continue_on_error_unresolved",
            detail=(
                f"Exact eligible {evidence_label} occurrence "
                f"{candidate.job_key!r}/{candidate.step_source_index} is owned by runtime "
                f"step {runtime_step.number}, but continue-on-error semantics mask the "
                "positive interpretation of the step conclusion."
            ),
            runtime_status=runtime_step.status,
            runtime_conclusion=runtime_step.conclusion,
            runtime_step_number=runtime_step.number,
        )

    if runtime_step.status == "completed" and runtime_step.conclusion == "success":
        source_order = (
            candidate.command_location.source_order
            if candidate.command_location is not None
            else "unknown"
        )
        return _RuntimeStrengtheningCandidateResult(
            state="supported",
            basis="supported",
            reason=f"runtime_correlated_{evidence_label.replace(' ', '_')}_supported",
            detail=(
                f"Exact eligible static {evidence_label} occurrence "
                f"{candidate.job_key!r}/{candidate.step_source_index} at source order "
                f"{source_order} is owned by runtime step {runtime_step.number}, and GitHub "
                "reports status='completed', conclusion='success' without visible "
                "continue-on-error masking."
            ),
            runtime_status=runtime_step.status,
            runtime_conclusion=runtime_step.conclusion,
            runtime_step_number=runtime_step.number,
        )

    return _RuntimeStrengtheningCandidateResult(
        state="not_established",
        basis="runtime_non_success",
        reason=f"runtime_correlated_{evidence_label.replace(' ', '_')}_not_successful",
        detail=(
            f"Exact eligible static {evidence_label} occurrence "
            f"{candidate.job_key!r}/{candidate.step_source_index} is owned by runtime step "
            f"{runtime_step.number}; GitHub factually reports status={runtime_step.status!r}, "
            f"conclusion={runtime_step.conclusion!r}. Positive Runtime-Correlated Support "
            "is therefore not established. This does not attribute the runtime outcome to "
            "the dependency command itself."
        ),
        runtime_status=runtime_step.status,
        runtime_conclusion=runtime_step.conclusion,
        runtime_step_number=runtime_step.number,
    )


def _runtime_candidate_result_summary(
    results: tuple[_RuntimeStrengtheningCandidateResult, ...],
) -> str:
    return "; ".join(item.detail for item in results)


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
