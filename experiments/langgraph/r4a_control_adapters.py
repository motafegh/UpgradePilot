"""Narrow R4-A comparison/control adapters for the R4-B LangGraph experiment.

The LangGraph workflow must not depend directly on R4-A planner/admission representations. This
module is the only intended bridge: it translates between R4-B-owned workflow contracts and the
already-proven R4-A control implementation where holding semantics constant improves comparison.

These adapters are experiment/evaluation code, not product runtime code.
"""

from __future__ import annotations

from typing import Protocol

from experiments.b2_x1_evidence_gap_admission import (
    AdmittedInvestigationAction,
    EvidenceGapAdmissionProblem,
    EvidenceGapAdmissionState,
    admit_selected_investigation_action,
    build_target_python_declaration_action,
)
from experiments.b2_x1_evidence_gap_composition import (
    compose_pre_target_python_support_planner_context,
)
from experiments.b2_x1_evidence_gap_model import (
    EvidenceGapModelInvocationProblem,
    EvidenceGapModelInvocationResult,
)
from experiments.b2_x1_evidence_gap_planner import (
    EvidenceGapDecision,
    EvidenceGapPlannerContext,
)
from experiments.langgraph.evidence_gap_workflow import (
    EvidenceGapLangGraphActionProposal,
    EvidenceGapLangGraphAuthorityOutcome,
    EvidenceGapLangGraphAuthorityRejection,
    EvidenceGapLangGraphAuthoritySnapshot,
    EvidenceGapLangGraphAuthorizedAction,
    EvidenceGapLangGraphNoAction,
    EvidenceGapLangGraphPlannerOutcome,
    EvidenceGapLangGraphProviderProblem,
    EvidenceGapLangGraphStartInput,
)


class R4APlannerControl(Protocol):
    """Small control-seam protocol implemented by the existing local R4-A planner."""

    def decide(
        self,
        context: EvidenceGapPlannerContext,
    ) -> EvidenceGapModelInvocationResult: ...


class R4AControlPlannerAdapter:
    """Map the existing R4-A bounded planner seam into R4-B planner outcomes."""

    def __init__(self, planner: R4APlannerControl) -> None:
        self._planner = planner

    def plan(
        self,
        start_input: EvidenceGapLangGraphStartInput,
    ) -> EvidenceGapLangGraphPlannerOutcome:
        context = compose_pre_target_python_support_planner_context(
            start_input.investigation,
            planning_question=start_input.planning_question,
            consumed_actions=start_input.consumed_actions,
            remaining_investigations=start_input.remaining_investigations,
        )
        result = self._planner.decide(context)
        return _planner_outcome_from_r4a(result)


class R4AControlAuthorityAdapter:
    """Use R4-A admission as a hidden deterministic oracle, then return R4-B outcomes."""

    def authorize(
        self,
        snapshot: EvidenceGapLangGraphAuthoritySnapshot,
        proposal: EvidenceGapLangGraphActionProposal,
    ) -> EvidenceGapLangGraphAuthorityOutcome:
        baseline = snapshot.baseline
        assessment = baseline.python_support_assessment
        candidate = assessment.candidate

        actions = ()
        selection = snapshot.current_selection
        if selection is not None:
            action = build_target_python_declaration_action(
                selection.repository,
                selection.revision,
            )
            if (
                selection.kind != action.action_id
                or selection.path != action.path
                or selection.proposition_key != action.target_proposition
            ):
                raise ValueError(
                    "current product investigation selection no longer matches the control action contract."
                )
            actions = (action,)

        admission_state = EvidenceGapAdmissionState(
            repository=candidate.target_repository,
            revision=candidate.target_revision,
            propositions=_assessment_propositions(assessment),
            consumed_actions=baseline.consumed_actions,
            remaining_investigations=baseline.remaining_investigations,
            actions=actions,
        )
        control_decision = EvidenceGapDecision(
            decision_kind="ACTION_SELECTED",
            action_id=proposal.action_id,
            explanation=proposal.explanation,
        )
        result = admit_selected_investigation_action(
            admission_state,
            control_decision,
        )

        if isinstance(result, EvidenceGapAdmissionProblem):
            return EvidenceGapLangGraphAuthorityRejection(
                reason=result.reason,
                action_id=result.action_id,
                detail=result.detail,
            )

        if not isinstance(result, AdmittedInvestigationAction):
            raise TypeError("R4-A admission returned an unsupported result.")

        action = result.action
        return EvidenceGapLangGraphAuthorizedAction(
            action_id=action.action_id,
            repository=action.repository,
            revision=action.revision,
            path=action.path,
            explanation=result.explanation,
        )


def _planner_outcome_from_r4a(
    result: EvidenceGapModelInvocationResult,
) -> EvidenceGapLangGraphPlannerOutcome:
    if isinstance(result, EvidenceGapModelInvocationProblem):
        return EvidenceGapLangGraphProviderProblem(
            reason=result.reason,
            detail=result.detail,
        )

    if not isinstance(result, EvidenceGapDecision):
        raise TypeError("R4-A planner returned an unsupported result.")

    if result.decision_kind == "ACTION_SELECTED":
        assert result.action_id is not None
        return EvidenceGapLangGraphActionProposal(
            action_id=result.action_id,
            explanation=result.explanation,
        )

    return EvidenceGapLangGraphNoAction(
        decision_kind=result.decision_kind,
        explanation=result.explanation,
    )


def _assessment_propositions(assessment):
    return tuple(
        proposition
        for path in assessment.applicability.paths
        for proposition in path.propositions
    )


__all__ = (
    "R4AControlAuthorityAdapter",
    "R4AControlPlannerAdapter",
    "R4APlannerControl",
)
