"""Focused tests for the EvidenceGapPlanner model-observation and decision boundary.

These tests stop before model/provider invocation and deterministic action execution. They prove
that request projection exposes the justified reasoning fields, keeps trusted execution authority
out of the model payload, and enforces the structured decision shape.
"""

from __future__ import annotations

import unittest

from experiments.evidence_gap_planner_model_boundary import (
    EVIDENCE_GAP_DECISION_JSON_SCHEMA,
    EvidenceGapActionDescriptor,
    EvidenceGapDecision,
    EvidenceGapDependencyTransition,
    EvidenceGapPlannerContext,
    EvidenceGapPlanningBudget,
    PlanningEvidence,
    PlanningEvidenceFact,
    evidence_gap_decision_from_mapping,
    render_evidence_gap_planner_request,
)
from upgradepilot.impact.applicability import PropositionAssessment


_TARGET_PROPOSITION = "exact_target_python_declaration_established"
_ACTION_ID = "acquire_exact_target_python_declaration"


class EvidenceGapPlannerBoundaryTests(unittest.TestCase):
    def test_request_projection_contains_only_evidence_refined_boundary(self) -> None:
        request = render_evidence_gap_planner_request(_context())
        context_payload = request["context"]
        assert isinstance(context_payload, dict)

        self.assertEqual(set(context_payload), {"planning_question","dependency_transition","propositions","planning_evidence","consumed_actions","planning_budget","allowed_actions"})
        self.assertEqual(context_payload["dependency_transition"], {"normalized_package":"soupsieve","old_version":"2.6","proposed_version":"2.8.4"})
        action = context_payload["allowed_actions"][0]  # type: ignore[index]
        self.assertEqual(set(action), {"action_id","purpose","target_proposition","evidence_yield"})  # type: ignore[arg-type]
        request_keys = _nested_mapping_keys(request)
        for hidden_name in ("repository","pull_number","revision","path","required_proposition_state","required_evidence_coverage","mutation_class","result_families","cost_class","attempted_actions","remaining_steps","hard_constraints","untrusted_evidence_notes"):
            self.assertNotIn(hidden_name, request_keys)

    def test_structured_planning_evidence_preserves_witness_path_without_raw_source(self) -> None:
        request = render_evidence_gap_planner_request(_context())
        context_payload = request["context"]
        assert isinstance(context_payload, dict)
        planning_evidence = context_payload["planning_evidence"]
        assert isinstance(planning_evidence, list)
        evidence = planning_evidence[0]
        facts = {fact["name"]: fact["value"] for fact in evidence["facts"]}
        self.assertEqual(facts["consumption_state"], "supported")
        self.assertEqual(facts["reachability_kind"], "transitive")
        self.assertEqual(facts["witness_path"], ["mkdocs-llmstxt","beautifulsoup4","soupsieve"])

    def test_action_decision_requires_action_id(self) -> None:
        with self.assertRaises(ValueError):
            evidence_gap_decision_from_mapping({"decision_kind":"ACTION_SELECTED","action_id":None,"explanation":"Acquire evidence."})

    def test_no_action_decision_rejects_action_id(self) -> None:
        with self.assertRaises(ValueError):
            evidence_gap_decision_from_mapping({"decision_kind":"QUESTION_SETTLED","action_id":_ACTION_ID,"explanation":"Already settled."})

    def test_extra_output_field_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            evidence_gap_decision_from_mapping({"decision_kind":"ACTION_SELECTED","action_id":_ACTION_ID,"explanation":"Acquire evidence.","repository":"evil/project"})

    def test_schema_is_closed_to_extra_fields(self) -> None:
        self.assertFalse(EVIDENCE_GAP_DECISION_JSON_SCHEMA["additionalProperties"])


def _context() -> EvidenceGapPlannerContext:
    return EvidenceGapPlannerContext(
        planning_question="What bounded investigation should run next?",
        dependency_transition=EvidenceGapDependencyTransition(normalized_package="soupsieve",old_version="2.6",proposed_version="2.8.4"),
        propositions=(PropositionAssessment(key=_TARGET_PROPOSITION,state="unresolved",evidence_coverage="insufficient",evidence_owner="target.python",detail="Target declaration remains unresolved."),),
        planning_evidence=(PlanningEvidence(evidence_kind="ci_dependency_consumption",summary="Static transitive CI consumption is supported without runtime compatibility proof.",facts=(PlanningEvidenceFact(name="consumption_state",value="supported"),PlanningEvidenceFact(name="reachability_kind",value="transitive"),PlanningEvidenceFact(name="witness_path",value=("mkdocs-llmstxt","beautifulsoup4","soupsieve")))),),
        consumed_actions=(),
        planning_budget=EvidenceGapPlanningBudget(remaining_investigations=1),
        allowed_actions=(EvidenceGapActionDescriptor(action_id=_ACTION_ID,purpose="Acquire the exact target Python declaration.",target_proposition=_TARGET_PROPOSITION,evidence_yield="Exact target declaration evidence."),),
    )


def _nested_mapping_keys(value: object) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, item in value.items():
            if isinstance(key, str):
                keys.add(key)
            keys.update(_nested_mapping_keys(item))
    elif isinstance(value, list):
        for item in value:
            keys.update(_nested_mapping_keys(item))
    return keys


if __name__ == "__main__":
    unittest.main()
