"""Adapt the ordinary-Python evidence-gap control into LangGraph workflow contracts.

The LangGraph workflow must not depend directly on ordinary-Python planner/admission
representations. This module is the explicit comparison bridge: it translates between
LangGraph-owned workflow contracts and the already-proven ordinary-Python control implementation
when holding planner and authority semantics constant improves the comparison.

These adapters are experiment/evaluation code, not product runtime code.
"""

from __future__ import annotations

from typing import Protocol

from experiments.evidence_gap_action_admission import (
    AdmittedInvestigationAction,
    EvidenceGapAdmissionProblem,
    EvidenceGapAdmissionState,
    admit_selected_investigation_action,
    build_target_python_declaration_action,
)
from experiments.evidence_gap_product_planner_composition import (
    compose_pre_target_python_support_planner_context,
)
from experiments.local_evidence_gap_planner import (
    EvidenceGapModelInvocationProblem,
    EvidenceGapModelInvocationResult,
)
from experiments.evidence_gap_planner_model_boundary import (
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


class OrdinaryPythonEvidenceGapPlannerControl(Protocol):
    """Small control-seam protocol implemented by the existing local ordinary-Python planner."""

    def decide(
        self,
        context: EvidenceGapPlannerContext,
    ) -> EvidenceGapModelInvocationResult: ...


class OrdinaryPythonEvidenceGapPlannerAdapter:
    """Map the ordinary-Python bounded planner seam into LangGraph planner outcomes."""

    def __init__(self, planner: OrdinaryPythonEvidenceGapPlannerControl) -> None:
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
        return _planner_outcome_from_ordinary_python_control(result)


class OrdinaryPythonEvidenceGapAuthorityAdapter:
    """Use ordinary-Python admission as a deterministic control oracle for LangGraph outcomes."""

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
                    "current product investigation selection no longer matches the ordinary-Python control action contract."
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
            raise TypeError("ordinary-Python admission returned an unsupported result.")

        action = result.action
        return EvidenceGapLangGraphAuthorizedAction(
            action_id=action.action_id,
            repository=action.repository,
            revision=action.revision,
            path=action.path,
            explanation=result.explanation,
        )


def _planner_outcome_from_ordinary_python_control(
    result: EvidenceGapModelInvocationResult,
) -> EvidenceGapLangGraphPlannerOutcome:
    if isinstance(result, EvidenceGapModelInvocationProblem):
        return EvidenceGapLangGraphProviderProblem(
            reason=result.reason,
            detail=result.detail,
        )

    if not isinstance(result, EvidenceGapDecision):
        raise TypeError("ordinary-Python planner returned an unsupported result.")

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
    "OrdinaryPythonEvidenceGapAuthorityAdapter",
    "OrdinaryPythonEvidenceGapPlannerAdapter",
    "OrdinaryPythonEvidenceGapPlannerControl",
)
