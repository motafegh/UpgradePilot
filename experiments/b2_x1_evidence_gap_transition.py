"""Experiment-owned R4-A4 transition/update/trace seam for ``EvidenceGapPlanner``.

This module starts after the R4-A2 authority boundary.  It does not decide which action should
run and it does not re-authorize model output.  It applies one already-valid planner branch:

    no-action decision
    -> lifecycle transition only

    ACTION_SELECTED + AdmittedInvestigationAction
    -> exact product-owned acquisition
    -> existing target/domain interpretation
    -> immutable next investigation state
    -> deterministic transition trace

The first action path intentionally supports only the one currently admitted real capability,
``acquire_exact_target_python_declaration``.  A generic executor registry is deferred until a
second real action demonstrates that such an abstraction is useful.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Literal

from experiments.b2_x1_evidence_gap_admission import (
    AdmittedInvestigationAction,
    TARGET_PYTHON_DECLARATION_ACTION_ID,
)
from experiments.b2_x1_evidence_gap_planner import EvidenceGapDecision
from upgradepilot.github.api import GitHubAcquisitionError, GitHubResponseError
from upgradepilot.github.repository import GitHubRepositoryClient
from upgradepilot.impact.python_support import (
    PythonSupportDropImpactAssessment,
    evaluate_python_support_drop_impact,
)
from upgradepilot.target.python import TargetPythonEvidence, interpret_target_python_declaration
from upgradepilot.target.relevance import evaluate_target_python_relevance


EvidenceGapContinuationStatus = Literal[
    "ACTIVE",
    "SETTLED",
    "OUTSIDE_CURRENT_BOUNDARY",
    "NO_JUSTIFIED_INVESTIGATION",
]

OperationalFailureType = Literal[
    "GitHubAcquisitionError",
    "GitHubResponseError",
]


@dataclass(frozen=True, slots=True)
class EvidenceGapInvestigationState:
    """Small evolving trusted state for the bounded R4-A planner loop."""

    python_support_assessment: PythonSupportDropImpactAssessment
    consumed_actions: tuple[str, ...]
    remaining_investigations: int
    continuation_status: EvidenceGapContinuationStatus = "ACTIVE"

    def __post_init__(self) -> None:
        if not isinstance(self.python_support_assessment, PythonSupportDropImpactAssessment):
            raise TypeError(
                "python_support_assessment must be PythonSupportDropImpactAssessment."
            )
        if type(self.remaining_investigations) is not int or self.remaining_investigations < 0:
            raise ValueError("remaining_investigations must be a non-negative integer.")
        if len(set(self.consumed_actions)) != len(self.consumed_actions):
            raise ValueError("consumed action ids must be unique.")
        for action_id in self.consumed_actions:
            if not isinstance(action_id, str) or not action_id or action_id != action_id.strip():
                raise ValueError("consumed action ids must be non-empty trimmed text.")
        if self.continuation_status not in {
            "ACTIVE",
            "SETTLED",
            "OUTSIDE_CURRENT_BOUNDARY",
            "NO_JUSTIFIED_INVESTIGATION",
        }:
            raise ValueError("continuation_status is unsupported.")


@dataclass(frozen=True, slots=True)
class EvidenceGapOperationalFailure:
    """Expected external acquisition failure before valid semantic target evidence exists."""

    exception_type: OperationalFailureType
    detail: str
    reason: str | None = None
    status_code: int | None = None

    def __post_init__(self) -> None:
        if self.exception_type not in {"GitHubAcquisitionError", "GitHubResponseError"}:
            raise ValueError("exception_type is unsupported.")
        if not isinstance(self.detail, str) or not self.detail or self.detail != self.detail.strip():
            raise ValueError("operational failure detail must be non-empty trimmed text.")
        if self.reason is not None and (
            not isinstance(self.reason, str)
            or not self.reason
            or self.reason != self.reason.strip()
        ):
            raise ValueError("operational failure reason must be trimmed text or None.")
        if self.status_code is not None and type(self.status_code) is not int:
            raise ValueError("operational failure status_code must be int or None.")


@dataclass(frozen=True, slots=True)
class EvidenceGapTransitionTrace:
    """Deterministic record of one bounded A4 transition.

    The trace stores the actual small immutable before/after states.  It also stores the model
    decision, exact admitted action when one existed, and either the valid semantic execution
    result or the expected operational failure.  No-action decisions have neither execution
    result nor operational failure.
    """

    before_state: EvidenceGapInvestigationState
    decision: EvidenceGapDecision
    admitted_action: AdmittedInvestigationAction | None
    execution_result: TargetPythonEvidence | None
    operational_failure: EvidenceGapOperationalFailure | None
    after_state: EvidenceGapInvestigationState

    def __post_init__(self) -> None:
        if self.decision.decision_kind == "ACTION_SELECTED":
            if self.admitted_action is None:
                raise ValueError("action transition trace requires an admitted action.")
            if self.decision.action_id != self.admitted_action.action.action_id:
                raise ValueError("trace decision/action identity must match.")
            if (self.execution_result is None) == (self.operational_failure is None):
                raise ValueError(
                    "action transition trace requires exactly one result or operational failure."
                )
            return

        if self.admitted_action is not None:
            raise ValueError("no-action transition trace must not contain an admitted action.")
        if self.execution_result is not None or self.operational_failure is not None:
            raise ValueError("no-action transition trace must not contain an execution outcome.")


def run_evidence_gap_transition(
    state: EvidenceGapInvestigationState,
    decision: EvidenceGapDecision,
    *,
    admitted_action: AdmittedInvestigationAction | None = None,
    repository_client: GitHubRepositoryClient | None = None,
) -> EvidenceGapTransitionTrace:
    """Apply one already-valid planner branch and return its immutable trace.

    ``ACTION_SELECTED`` must already have passed R4-A2 admission.  No-action decisions bypass
    capability execution entirely.  The function intentionally does not run another planner turn.
    """

    _require_active_state(state)

    if decision.decision_kind != "ACTION_SELECTED":
        if admitted_action is not None:
            raise ValueError("no-action decision must not supply an admitted action.")
        after_state = _state_after_no_action_decision(state, decision)
        return EvidenceGapTransitionTrace(
            before_state=state,
            decision=decision,
            admitted_action=None,
            execution_result=None,
            operational_failure=None,
            after_state=after_state,
        )

    if admitted_action is None:
        raise ValueError("ACTION_SELECTED transition requires an admitted action.")
    if repository_client is None:
        raise ValueError("ACTION_SELECTED transition requires a repository client.")
    if decision.action_id != admitted_action.action.action_id:
        raise ValueError("decision action_id must match the admitted action.")
    if admitted_action.action.action_id != TARGET_PYTHON_DECLARATION_ACTION_ID:
        raise ValueError("the current A4 seam supports only the target-Python action.")
    if admitted_action.action.action_id in state.consumed_actions:
        raise ValueError("an already-consumed action cannot enter A4 execution.")
    if state.remaining_investigations <= 0:
        raise ValueError("A4 execution requires remaining investigation budget.")

    action = admitted_action.action
    try:
        repository_evidence = repository_client.get_exact_commit_text_file(
            action.repository,
            action.revision,
            action.path,
        )
    except GitHubAcquisitionError as exc:
        failure = EvidenceGapOperationalFailure(
            exception_type="GitHubAcquisitionError",
            detail=str(exc),
            reason=exc.reason,
            status_code=exc.status_code,
        )
        after_state = _state_after_operational_failure(state)
        return EvidenceGapTransitionTrace(
            before_state=state,
            decision=decision,
            admitted_action=admitted_action,
            execution_result=None,
            operational_failure=failure,
            after_state=after_state,
        )
    except GitHubResponseError as exc:
        failure = EvidenceGapOperationalFailure(
            exception_type="GitHubResponseError",
            detail=str(exc),
        )
        after_state = _state_after_operational_failure(state)
        return EvidenceGapTransitionTrace(
            before_state=state,
            decision=decision,
            admitted_action=admitted_action,
            execution_result=None,
            operational_failure=failure,
            after_state=after_state,
        )

    target_result = interpret_target_python_declaration(repository_evidence)
    after_state = _state_after_semantic_result(
        state,
        action_id=action.action_id,
        target_result=target_result,
    )
    return EvidenceGapTransitionTrace(
        before_state=state,
        decision=decision,
        admitted_action=admitted_action,
        execution_result=target_result,
        operational_failure=None,
        after_state=after_state,
    )


def replay_evidence_gap_transition(
    trace: EvidenceGapTransitionTrace,
) -> EvidenceGapInvestigationState:
    """Reproduce the deterministic state transition without LM Studio or GitHub I/O.

    Replay consumes the recorded decision and execution outcome.  It does not re-execute the
    external provider boundary.  Callers can compare the returned state with ``trace.after_state``
    to prove transition equivalence.
    """

    if trace.decision.decision_kind != "ACTION_SELECTED":
        return _state_after_no_action_decision(trace.before_state, trace.decision)

    assert trace.admitted_action is not None
    if trace.execution_result is not None:
        return _state_after_semantic_result(
            trace.before_state,
            action_id=trace.admitted_action.action.action_id,
            target_result=trace.execution_result,
        )

    assert trace.operational_failure is not None
    return _state_after_operational_failure(trace.before_state)


def _state_after_semantic_result(
    state: EvidenceGapInvestigationState,
    *,
    action_id: str,
    target_result: TargetPythonEvidence,
) -> EvidenceGapInvestigationState:
    assessment = state.python_support_assessment
    target_relevance = evaluate_target_python_relevance(
        assessment.candidate.upstream_claim,
        target_result,
    )
    next_assessment = evaluate_python_support_drop_impact(
        assessment.candidate,
        target_relevance,
    )
    return replace(
        state,
        python_support_assessment=next_assessment,
        consumed_actions=state.consumed_actions + (action_id,),
        remaining_investigations=state.remaining_investigations - 1,
    )


def _state_after_operational_failure(
    state: EvidenceGapInvestigationState,
) -> EvidenceGapInvestigationState:
    return replace(
        state,
        remaining_investigations=state.remaining_investigations - 1,
    )


def _state_after_no_action_decision(
    state: EvidenceGapInvestigationState,
    decision: EvidenceGapDecision,
) -> EvidenceGapInvestigationState:
    continuation_by_decision: dict[str, EvidenceGapContinuationStatus] = {
        "QUESTION_SETTLED": "SETTLED",
        "KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY": "OUTSIDE_CURRENT_BOUNDARY",
        "NO_JUSTIFIED_INVESTIGATION_IDENTIFIED": "NO_JUSTIFIED_INVESTIGATION",
    }
    try:
        continuation_status = continuation_by_decision[decision.decision_kind]
    except KeyError as exc:
        raise ValueError("no-action state transition requires a no-action decision.") from exc
    return replace(state, continuation_status=continuation_status)


def _require_active_state(state: EvidenceGapInvestigationState) -> None:
    if state.continuation_status != "ACTIVE":
        raise ValueError("only ACTIVE investigation state may enter another A4 transition.")


__all__ = (
    "EvidenceGapContinuationStatus",
    "EvidenceGapInvestigationState",
    "EvidenceGapOperationalFailure",
    "EvidenceGapTransitionTrace",
    "replay_evidence_gap_transition",
    "run_evidence_gap_transition",
)
