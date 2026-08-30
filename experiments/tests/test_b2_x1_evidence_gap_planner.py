"""Focused tests for the R4-A evidence-refined planner model boundary.

These tests intentionally stop before model/provider invocation and deterministic action
execution.  They prove that the new request projection exposes the R2-approved reasoning fields,
keeps trusted execution authority out of the model payload, and enforces the R3 decision shape.
"""

from __future__ import annotations

import json
import unittest

from experiments.b2_x1_evidence_gap_planner import (
    EVIDENCE_GAP_DECISION_JSON_SCHEMA,
    EvidenceGapActionDescriptor,
    EvidenceGapDecision,
    EvidenceGapDependencyTransition,
    EvidenceGapPlannerContext,
    EvidenceGapPlanningBudget,
    EvidenceGapPlanningEvidence,
    EvidenceGapPlanningEvidenceFact,
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

        self.assertEqual(
            set(context_payload),
            {
                "planning_question",
                "dependency_transition",
                "propositions",
                "planning_evidence",
                "consumed_actions",
                "planning_budget",
                "allowed_actions",
            },
        )

        dependency = context_payload["dependency_transition"]
        self.assertEqual(
            dependency,
            {
                "normalized_package": "soupsieve",
                "old_version": "2.6",
                "proposed_version": "2.8.4",
            },
        )

        action = context_payload["allowed_actions"][0]  # type: ignore[index]
        self.assertEqual(
            set(action),  # type: ignore[arg-type]
            {"action_id", "purpose", "target_proposition", "evidence_yield"},
        )

        serialized = json.dumps(request, sort_keys=True)
        for hidden_name in (
            "repository",
            "pull_number",
            "revision",
            "path",
            "required_proposition_state",
            "required_evidence_coverage",
            "mutation_class",
            "result_families",
            "cost_class",
            "attempted_actions",
            "remaining_steps",
            "hard_constraints",
            "untrusted_evidence_notes",
        ):
            self.assertNotIn(hidden_name, serialized)

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
        self.assertEqual(
            facts["witness_path"],
            ["mkdocs-llmstxt", "beautifulsoup4", "soupsieve"],
        )
        self.assertNotIn("workflow_yaml", evidence)
        self.assertNotIn("raw_command", evidence)

    def test_context_rejects_action_target_absent_from_propositions(self) -> None:
        with self.assertRaisesRegex(ValueError, "target proposition"):
            EvidenceGapPlannerContext(
                planning_question="What useful investigation, if any, should run?",
                dependency_transition=_transition(),
                propositions=(
                    PropositionAssessment(
                        key="different_proposition",
                        state="unresolved",
                        evidence_coverage="insufficient",
                        evidence_owner="target.python",
                        detail="A different unresolved proposition.",
                    ),
                ),
                planning_evidence=(),
                consumed_actions=(),
                planning_budget=EvidenceGapPlanningBudget(
                    remaining_investigations=1
                ),
                allowed_actions=(_action_descriptor(),),
            )

    def test_context_rejects_consumed_action_that_is_still_offered(self) -> None:
        with self.assertRaisesRegex(ValueError, "consumed action"):
            _context(consumed_actions=(_ACTION_ID,))

    def test_action_selected_requires_action_id(self) -> None:
        with self.assertRaisesRegex(ValueError, "action_id"):
            EvidenceGapDecision(
                decision_kind="ACTION_SELECTED",
                action_id=None,
                explanation="The action would add discriminating evidence.",
            )

    def test_no_tool_decision_requires_null_action_id(self) -> None:
        with self.assertRaisesRegex(ValueError, "no-tool"):
            EvidenceGapDecision(
                decision_kind="QUESTION_SETTLED",
                action_id=_ACTION_ID,
                explanation="The bounded question is already sufficiently settled.",
            )

    def test_strict_mapping_parser_accepts_action_selected(self) -> None:
        decision = evidence_gap_decision_from_mapping(
            {
                "decision_kind": "ACTION_SELECTED",
                "action_id": _ACTION_ID,
                "explanation": "The target declaration is the discriminating missing evidence.",
            }
        )

        self.assertEqual(decision.action_id, _ACTION_ID)
        self.assertEqual(decision.decision_kind, "ACTION_SELECTED")

    def test_strict_mapping_parser_accepts_no_tool_kind(self) -> None:
        decision = evidence_gap_decision_from_mapping(
            {
                "decision_kind": "NO_JUSTIFIED_INVESTIGATION_IDENTIFIED",
                "action_id": None,
                "explanation": "The question remains non-final but no useful action is identified.",
            }
        )

        self.assertIsNone(decision.action_id)

    def test_strict_mapping_parser_rejects_extra_authority_field(self) -> None:
        raw: dict[str, object] = {
            "decision_kind": "ACTION_SELECTED",
            "action_id": _ACTION_ID,
            "explanation": "Acquire the missing exact declaration.",
            "target_proposition": _TARGET_PROPOSITION,
        }

        with self.assertRaisesRegex(ValueError, "fields differed"):
            evidence_gap_decision_from_mapping(raw)

    def test_output_schema_is_exact_three_field_shape(self) -> None:
        self.assertIs(EVIDENCE_GAP_DECISION_JSON_SCHEMA["additionalProperties"], False)
        self.assertEqual(
            EVIDENCE_GAP_DECISION_JSON_SCHEMA["required"],
            ["decision_kind", "action_id", "explanation"],
        )
        properties = EVIDENCE_GAP_DECISION_JSON_SCHEMA["properties"]
        assert isinstance(properties, dict)
        self.assertEqual(
            set(properties),
            {"decision_kind", "action_id", "explanation"},
        )


def _transition() -> EvidenceGapDependencyTransition:
    return EvidenceGapDependencyTransition(
        normalized_package="soupsieve",
        old_version="2.6",
        proposed_version="2.8.4",
    )


def _target_proposition() -> PropositionAssessment:
    return PropositionAssessment(
        key=_TARGET_PROPOSITION,
        state="unresolved",
        evidence_coverage="insufficient",
        evidence_owner="target.python",
        detail="The exact target Python declaration has not yet been acquired.",
    )


def _action_descriptor() -> EvidenceGapActionDescriptor:
    return EvidenceGapActionDescriptor(
        action_id=_ACTION_ID,
        purpose=(
            "Acquire the exact target Python declaration needed to advance the unresolved "
            "Python-support question."
        ),
        target_proposition=_TARGET_PROPOSITION,
        evidence_yield=(
            "Exact target Python declaration evidence or a typed target-declaration problem."
        ),
    )


def _planning_evidence() -> EvidenceGapPlanningEvidence:
    return EvidenceGapPlanningEvidence(
        evidence_kind="ci_dependency_consumption",
        summary=(
            "The exact-head docs environment has static transitive reachability to the changed "
            "dependency; this is not runtime compatibility proof."
        ),
        facts=(
            EvidenceGapPlanningEvidenceFact(
                name="consumption_state",
                value="supported",
            ),
            EvidenceGapPlanningEvidenceFact(
                name="reachability_kind",
                value="transitive",
            ),
            EvidenceGapPlanningEvidenceFact(
                name="witness_path",
                value=("mkdocs-llmstxt", "beautifulsoup4", "soupsieve"),
            ),
            EvidenceGapPlanningEvidenceFact(
                name="direct_exercise_established",
                value=False,
            ),
        ),
    )


def _context(
    *,
    consumed_actions: tuple[str, ...] = (),
) -> EvidenceGapPlannerContext:
    return EvidenceGapPlannerContext(
        planning_question=(
            "What additional admitted investigation, if any, is useful for determining whether "
            "the established upstream Python-support drop intersects the target declaration?"
        ),
        dependency_transition=_transition(),
        propositions=(_target_proposition(),),
        planning_evidence=(_planning_evidence(),),
        consumed_actions=consumed_actions,
        planning_budget=EvidenceGapPlanningBudget(remaining_investigations=1),
        allowed_actions=(_action_descriptor(),),
    )


if __name__ == "__main__":
    unittest.main()
