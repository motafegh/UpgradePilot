"""Framework-neutral semantic projection for bounded R4 implementation comparison.

This module is experiment/evaluation support. It does not define product runtime state and it does
not require R4-A and R4-B to share internal classes, topology, or trace representation. Instead it
projects each implementation's observable result into the small semantic surface that the R4
comparison actually cares about.

The projection is intentionally suitable for later R4-C use as well: comparison should normalize
accepted behavior, not force one implementation's architecture onto another.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from experiments.b2_x1_evidence_gap_admission import EvidenceGapAdmissionProblem
from experiments.b2_x1_evidence_gap_planner import EvidenceGapDecision
from experiments.b2_x1_evidence_gap_transition import (
    EvidenceGapInvestigationState,
    EvidenceGapTransitionTrace,
)
from experiments.langgraph.evidence_gap_workflow import (
    EvidenceGapLangGraphActionProposal,
    EvidenceGapLangGraphAuthorityRejection,
    EvidenceGapLangGraphAuthorizedAction,
    EvidenceGapLangGraphNoAction,
    EvidenceGapLangGraphOperationalFailure,
    EvidenceGapLangGraphProviderProblem,
    EvidenceGapLangGraphResult,
)


EvidenceGapComparisonPlannerOutcome = Literal[
    "ACTION_SELECTED",
    "QUESTION_SETTLED",
    "KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY",
    "NO_JUSTIFIED_INVESTIGATION_IDENTIFIED",
    "PROVIDER_PROBLEM",
]
EvidenceGapComparisonAuthorityStatus = Literal[
    "NOT_REQUIRED",
    "AUTHORIZED",
    "REJECTED",
]
EvidenceGapComparisonOutcomeKind = Literal[
    "no_action",
    "provider_problem",
    "authority_rejected",
    "semantic_result",
    "operational_failure",
]


@dataclass(frozen=True, slots=True)
class EvidenceGapSemanticProjection:
    """Small common semantic surface used to compare R4 implementations."""

    planner_outcome: EvidenceGapComparisonPlannerOutcome
    action_id: str | None
    authority_status: EvidenceGapComparisonAuthorityStatus
    authority_reason: str | None
    external_effect_attempted: bool
    outcome_kind: EvidenceGapComparisonOutcomeKind
    remaining_investigations: int
    consumed_actions: tuple[str, ...]
    continuation_status: str
    investigation_semantic_state: str | None
    target_relevance_state: str | None
    applicability_state: str
    operational_failure_type: str | None
    operational_failure_reason: str | None


def project_r4a_transition(
    trace: EvidenceGapTransitionTrace,
) -> EvidenceGapSemanticProjection:
    """Project one completed R4-A transition into the common comparison surface."""

    after = trace.after_state
    planner_outcome = trace.decision.decision_kind
    if planner_outcome == "ACTION_SELECTED":
        assert trace.admitted_action is not None
        action_id = trace.admitted_action.action.action_id
        authority_status: EvidenceGapComparisonAuthorityStatus = "AUTHORIZED"
        external_effect_attempted = True
        if trace.execution_result is not None:
            outcome_kind: EvidenceGapComparisonOutcomeKind = "semantic_result"
            investigation_semantic_state = trace.execution_result.state
            failure_type = None
            failure_reason = None
        else:
            assert trace.operational_failure is not None
            outcome_kind = "operational_failure"
            investigation_semantic_state = None
            failure_type = trace.operational_failure.exception_type
            failure_reason = trace.operational_failure.reason
    else:
        action_id = None
        authority_status = "NOT_REQUIRED"
        external_effect_attempted = False
        outcome_kind = "no_action"
        investigation_semantic_state = None
        failure_type = None
        failure_reason = None

    return _projection(
        planner_outcome=planner_outcome,
        action_id=action_id,
        authority_status=authority_status,
        authority_reason=None,
        external_effect_attempted=external_effect_attempted,
        outcome_kind=outcome_kind,
        state=after,
        investigation_semantic_state=investigation_semantic_state,
        operational_failure_type=failure_type,
        operational_failure_reason=failure_reason,
    )


def project_r4a_admission_rejection(
    state: EvidenceGapInvestigationState,
    decision: EvidenceGapDecision,
    problem: EvidenceGapAdmissionProblem,
) -> EvidenceGapSemanticProjection:
    """Project an R4-A action proposal rejected at the fresh admission boundary."""

    if decision.decision_kind != "ACTION_SELECTED":
        raise ValueError("R4-A admission rejection comparison requires ACTION_SELECTED.")
    if decision.action_id != problem.action_id:
        raise ValueError("R4-A decision and admission problem action ids must match.")

    return _projection(
        planner_outcome="ACTION_SELECTED",
        action_id=problem.action_id,
        authority_status="REJECTED",
        authority_reason=problem.reason,
        external_effect_attempted=False,
        outcome_kind="authority_rejected",
        state=state,
        investigation_semantic_state=None,
        operational_failure_type=None,
        operational_failure_reason=None,
    )


def project_r4b_result(
    result: EvidenceGapLangGraphResult,
) -> EvidenceGapSemanticProjection:
    """Project one completed native R4-B graph result into the common comparison surface."""

    planner = result.planner_outcome
    if isinstance(planner, EvidenceGapLangGraphActionProposal):
        planner_outcome: EvidenceGapComparisonPlannerOutcome = "ACTION_SELECTED"
        action_id = planner.action_id
    elif isinstance(planner, EvidenceGapLangGraphNoAction):
        planner_outcome = planner.decision_kind
        action_id = None
    elif isinstance(planner, EvidenceGapLangGraphProviderProblem):
        planner_outcome = "PROVIDER_PROBLEM"
        action_id = None
    else:
        raise TypeError("unsupported R4-B planner outcome for comparison.")

    authority = result.execution_authority_outcome
    if authority is None:
        authority_status: EvidenceGapComparisonAuthorityStatus = "NOT_REQUIRED"
        authority_reason = None
    elif isinstance(authority, EvidenceGapLangGraphAuthorizedAction):
        authority_status = "AUTHORIZED"
        authority_reason = None
    elif isinstance(authority, EvidenceGapLangGraphAuthorityRejection):
        authority_status = "REJECTED"
        authority_reason = authority.reason
    else:
        raise TypeError("unsupported R4-B authority outcome for comparison.")

    investigation_semantic_state = None
    failure_type = None
    failure_reason = None
    investigation = result.investigation_outcome
    if isinstance(investigation, EvidenceGapLangGraphOperationalFailure):
        failure_type = investigation.exception_type
        failure_reason = investigation.reason
    elif investigation is not None:
        investigation_semantic_state = investigation.state

    assessment = result.python_support_assessment
    relevance = assessment.target_relevance
    return EvidenceGapSemanticProjection(
        planner_outcome=planner_outcome,
        action_id=action_id,
        authority_status=authority_status,
        authority_reason=authority_reason,
        external_effect_attempted=result.outcome_kind in {
            "semantic_result",
            "operational_failure",
        },
        outcome_kind=result.outcome_kind,
        remaining_investigations=result.remaining_investigations,
        consumed_actions=result.consumed_actions,
        continuation_status=result.continuation_status,
        investigation_semantic_state=investigation_semantic_state,
        target_relevance_state=relevance.state if relevance is not None else None,
        applicability_state=assessment.applicability.state,
        operational_failure_type=failure_type,
        operational_failure_reason=failure_reason,
    )


def _projection(
    *,
    planner_outcome: EvidenceGapComparisonPlannerOutcome,
    action_id: str | None,
    authority_status: EvidenceGapComparisonAuthorityStatus,
    authority_reason: str | None,
    external_effect_attempted: bool,
    outcome_kind: EvidenceGapComparisonOutcomeKind,
    state: EvidenceGapInvestigationState,
    investigation_semantic_state: str | None,
    operational_failure_type: str | None,
    operational_failure_reason: str | None,
) -> EvidenceGapSemanticProjection:
    assessment = state.python_support_assessment
    relevance = assessment.target_relevance
    return EvidenceGapSemanticProjection(
        planner_outcome=planner_outcome,
        action_id=action_id,
        authority_status=authority_status,
        authority_reason=authority_reason,
        external_effect_attempted=external_effect_attempted,
        outcome_kind=outcome_kind,
        remaining_investigations=state.remaining_investigations,
        consumed_actions=state.consumed_actions,
        continuation_status=state.continuation_status,
        investigation_semantic_state=investigation_semantic_state,
        target_relevance_state=relevance.state if relevance is not None else None,
        applicability_state=assessment.applicability.state,
        operational_failure_type=operational_failure_type,
        operational_failure_reason=operational_failure_reason,
    )


__all__ = (
    "EvidenceGapSemanticProjection",
    "project_r4a_admission_rejection",
    "project_r4a_transition",
    "project_r4b_result",
)
