"""Reusable CI evidence for successful user-step and exact-command execution.

Static/runtime workflow correlation establishes identity only. Runtime-strengthening eligibility
establishes only whether a parsed command shape may inherit step-level success. This module
composes those independent facts into reusable execution assessments without learning any
dependency or package-manager semantics.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..github.workflow_command_location import StaticCommandLocation
from ..github.workflow_definition import RunStepDefinition
from .runtime_strengthening import (
    RuntimeStrengthenableCommandOccurrence,
    classify_runtime_strengthening_eligibility,
)
from .workflow_runtime_correlation import (
    WorkflowRuntimeCorrelationResult,
    WorkflowRuntimeStepCorrelation,
)


type RuntimeExecutionState = Literal["supported", "not_established", "unresolved"]
type CorrelatedStepExecutionBasis = Literal[
    "supported",
    "continue_on_error_unresolved",
    "runtime_non_success",
]
type ExactCommandExecutionBasis = Literal[
    "supported",
    "eligibility_ineligible",
    "eligibility_unresolved",
    "workflow_correlation_unresolved",
    "step_correlation_unresolved",
    "continue_on_error_unresolved",
    "runtime_non_success",
]


@dataclass(frozen=True, slots=True)
class CorrelatedStepExecutionAssessment:
    """Execution assessment for one already-correlated GitHub user step."""

    state: RuntimeExecutionState
    basis: CorrelatedStepExecutionBasis
    reason: str
    detail: str
    correlation: WorkflowRuntimeStepCorrelation


@dataclass(frozen=True, slots=True)
class ExactCommandExecutionAssessment:
    """Execution assessment for one exact parsed command occurrence."""

    state: RuntimeExecutionState
    basis: ExactCommandExecutionBasis
    reason: str
    detail: str
    workflow_path: str | None
    workflow_revision: str | None
    job_key: str
    step_source_index: int
    command_location: StaticCommandLocation | None
    step_execution: CorrelatedStepExecutionAssessment | None = None

    @property
    def runtime_status(self) -> str | None:
        if self.step_execution is None:
            return None
        return self.step_execution.correlation.runtime_step.status

    @property
    def runtime_conclusion(self) -> str | None:
        if self.step_execution is None:
            return None
        return self.step_execution.correlation.runtime_step.conclusion

    @property
    def runtime_step_number(self) -> int | None:
        if self.step_execution is None:
            return None
        return self.step_execution.correlation.runtime_step.number


def assess_correlated_step_execution(
    correlation: WorkflowRuntimeStepCorrelation,
) -> CorrelatedStepExecutionAssessment:
    """Interpret one correlated user step without attributing success to inner commands."""

    static_step = correlation.static_step
    runtime_step = correlation.runtime_step
    continue_on_error = static_step.continue_on_error

    if continue_on_error is not None and (
        continue_on_error.contains_expression
        or continue_on_error.text.strip().casefold() != "false"
    ):
        return CorrelatedStepExecutionAssessment(
            state="unresolved",
            basis="continue_on_error_unresolved",
            reason="correlated_step_continue_on_error_unresolved",
            detail=(
                f"Runtime step {runtime_step.number} is correlated to static user step "
                f"{static_step.source_index}, but continue-on-error semantics mask the "
                "positive interpretation of the runtime conclusion."
            ),
            correlation=correlation,
        )

    if runtime_step.status == "completed" and runtime_step.conclusion == "success":
        return CorrelatedStepExecutionAssessment(
            state="supported",
            basis="supported",
            reason="correlated_step_execution_supported",
            detail=(
                f"Runtime step {runtime_step.number} is correlated to static user step "
                f"{static_step.source_index}, and GitHub reports status='completed', "
                "conclusion='success' without visible continue-on-error masking."
            ),
            correlation=correlation,
        )

    return CorrelatedStepExecutionAssessment(
        state="not_established",
        basis="runtime_non_success",
        reason="correlated_step_execution_not_successful",
        detail=(
            f"Runtime step {runtime_step.number} is correlated to static user step "
            f"{static_step.source_index}; GitHub factually reports "
            f"status={runtime_step.status!r}, conclusion={runtime_step.conclusion!r}. "
            "Positive user-step execution is therefore not established."
        ),
        correlation=correlation,
    )


def assess_exact_command_execution(
    candidate: RuntimeStrengthenableCommandOccurrence,
    *,
    correlation: WorkflowRuntimeCorrelationResult,
) -> ExactCommandExecutionAssessment:
    """Assess whether exact command execution follows from correlation plus static structure."""

    eligibility = classify_runtime_strengthening_eligibility(candidate)
    if eligibility.state == "ineligible":
        return _command_assessment(
            candidate,
            state="not_established",
            basis="eligibility_ineligible",
            reason=eligibility.reason,
            detail=eligibility.detail,
        )
    if eligibility.state == "unresolved":
        return _command_assessment(
            candidate,
            state="unresolved",
            basis="eligibility_unresolved",
            reason=eligibility.reason,
            detail=eligibility.detail,
        )

    if correlation.state != "correlated":
        return _command_assessment(
            candidate,
            state="unresolved",
            basis="workflow_correlation_unresolved",
            reason="workflow_runtime_correlation_unresolved",
            detail=(
                "The exact command is structurally eligible, but the bounded workflow "
                f"runtime bridge is unavailable: {correlation.reason}: {correlation.detail}"
            ),
        )

    step_correlation = _find_correlated_step(
        correlation,
        job_key=candidate.job_key,
        step_source_index=candidate.step_source_index,
    )
    if step_correlation is None:
        return _command_assessment(
            candidate,
            state="unresolved",
            basis="step_correlation_unresolved",
            reason="exact_command_owning_step_correlation_missing",
            detail=(
                f"The workflow bridge is correlated, but command occurrence "
                f"{candidate.job_key!r}/{candidate.step_source_index} has no retained "
                "owning runtime-step correlation."
            ),
        )

    if not isinstance(step_correlation.static_step, RunStepDefinition):
        return _command_assessment(
            candidate,
            state="unresolved",
            basis="step_correlation_unresolved",
            reason="exact_command_static_step_not_run_step",
            detail=(
                f"Command occurrence {candidate.job_key!r}/{candidate.step_source_index} "
                "did not resolve to a static run step."
            ),
        )

    step_execution = assess_correlated_step_execution(step_correlation)
    if step_execution.state == "supported":
        source_order = (
            candidate.command_location.source_order
            if candidate.command_location is not None
            else "unknown"
        )
        return _command_assessment(
            candidate,
            state="supported",
            basis="supported",
            reason="exact_command_execution_supported",
            detail=(
                f"Exact eligible command occurrence {candidate.job_key!r}/"
                f"{candidate.step_source_index} at source order {source_order} is owned by "
                f"runtime step {step_correlation.runtime_step.number}, whose unmasked "
                "completed-successful execution supports this bounded command occurrence."
            ),
            step_execution=step_execution,
        )

    return _command_assessment(
        candidate,
        state=step_execution.state,
        basis=step_execution.basis,
        reason=step_execution.reason,
        detail=step_execution.detail,
        step_execution=step_execution,
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


def _command_assessment(
    candidate: RuntimeStrengthenableCommandOccurrence,
    *,
    state: RuntimeExecutionState,
    basis: ExactCommandExecutionBasis,
    reason: str,
    detail: str,
    step_execution: CorrelatedStepExecutionAssessment | None = None,
) -> ExactCommandExecutionAssessment:
    return ExactCommandExecutionAssessment(
        state=state,
        basis=basis,
        reason=reason,
        detail=detail,
        workflow_path=candidate.workflow_path,
        workflow_revision=candidate.workflow_revision,
        job_key=candidate.job_key,
        step_source_index=candidate.step_source_index,
        command_location=candidate.command_location,
        step_execution=step_execution,
    )


__all__ = (
    "CorrelatedStepExecutionAssessment",
    "CorrelatedStepExecutionBasis",
    "ExactCommandExecutionAssessment",
    "ExactCommandExecutionBasis",
    "RuntimeExecutionState",
    "assess_correlated_step_execution",
    "assess_exact_command_execution",
)
