"""Focused tests for the local EvidenceGapPlanner model request/response seam.

These tests use a mocked HTTP boundary. They prove request construction, local-provider failure
classification, strict structured-output parsing, and preservation of the existing model-visible
context boundary. They do not establish live LM Studio/model behavior or planner semantic quality.
"""

from __future__ import annotations

import json
import unittest
from unittest.mock import Mock

from requests.exceptions import Timeout

from experiments.local_evidence_gap_planner import (
    EVIDENCE_GAP_MODEL_ID,
    LM_STUDIO_BASE_URL,
    MAX_COMPLETION_TOKENS,
    REQUEST_TIMEOUT_SECONDS,
    EvidenceGapModelInvocationProblem,
    LocalEvidenceGapPlanner,
    build_lm_studio_session,
)
from experiments.evidence_gap_planner_model_boundary import (
    EvidenceGapActionDescriptor,
    EvidenceGapDecision,
    EvidenceGapDependencyTransition,
    EvidenceGapPlannerContext,
    EvidenceGapPlanningBudget,
    PlanningEvidence,
    PlanningEvidenceFact,
)
from upgradepilot.impact.applicability import PropositionAssessment


_TARGET_PROPOSITION = "exact_target_python_declaration_established"
_ACTION_ID = "acquire_exact_target_python_declaration"


def _response(
    decision: object,
    *,
    status: int = 200,
    finish_reason: str = "stop",
) -> Mock:
    response = Mock()
    response.status_code = status
    response.json.return_value = {
        "choices": [
            {
                "finish_reason": finish_reason,
                "message": {"content": json.dumps(decision)},
            }
        ]
    }
    return response


class EvidenceGapModelTests(unittest.TestCase):
    def test_request_uses_bounded_context_and_strict_schema(self) -> None:
        post = Mock(
            return_value=_response(
                {
                    "decision_kind": "ACTION_SELECTED",
                    "action_id": _ACTION_ID,
                    "explanation": "The exact target declaration is the next useful evidence gap.",
                }
            )
        )

        result = LocalEvidenceGapPlanner(post=post).decide(_context())

        self.assertIsInstance(result, EvidenceGapDecision)
        post.assert_called_once()
        args, kwargs = post.call_args
        self.assertEqual(args, (f"{LM_STUDIO_BASE_URL}/v1/chat/completions",))
        self.assertEqual(kwargs["timeout"], REQUEST_TIMEOUT_SECONDS)

        payload = kwargs["json"]
        self.assertEqual(payload["model"], EVIDENCE_GAP_MODEL_ID)
        self.assertEqual(payload["temperature"], 0)
        self.assertEqual(payload["seed"], 0)
        self.assertEqual(payload["max_tokens"], MAX_COMPLETION_TOKENS)
        self.assertFalse(payload["stream"])

        response_format = payload["response_format"]
        self.assertEqual(response_format["type"], "json_schema")
        self.assertTrue(response_format["json_schema"]["strict"])
        schema = response_format["json_schema"]["schema"]
        self.assertEqual(
            set(schema["properties"]),
            {"decision_kind", "action_id", "explanation"},
        )

        user_content = payload["messages"][1]["content"]
        self.assertIn('"planning_question"', user_content)
        self.assertIn('"planning_evidence"', user_content)
        self.assertIn('"allowed_actions"', user_content)
        self.assertNotIn('"repository"', user_content)
        self.assertNotIn('"revision"', user_content)
        self.assertNotIn('"path"', user_content)
        self.assertNotIn('"result_families"', user_content)
        self.assertNotIn('"mutation_class"', user_content)

    def test_valid_action_selection_maps_to_evidence_gap_decision(self) -> None:
        post = Mock(
            return_value=_response(
                {
                    "decision_kind": "ACTION_SELECTED",
                    "action_id": _ACTION_ID,
                    "explanation": "Acquire the exact target declaration.",
                }
            )
        )

        result = LocalEvidenceGapPlanner(post=post).decide(_context())

        self.assertIsInstance(result, EvidenceGapDecision)
        assert isinstance(result, EvidenceGapDecision)
        self.assertEqual(result.decision_kind, "ACTION_SELECTED")
        self.assertEqual(result.action_id, _ACTION_ID)

    def test_valid_no_action_selection_maps_to_evidence_gap_decision(self) -> None:
        post = Mock(
            return_value=_response(
                {
                    "decision_kind": "NO_JUSTIFIED_INVESTIGATION_IDENTIFIED",
                    "action_id": None,
                    "explanation": "No useful admitted or specific outside-boundary investigation remains.",
                }
            )
        )

        result = LocalEvidenceGapPlanner(post=post).decide(_no_action_context())

        self.assertIsInstance(result, EvidenceGapDecision)
        assert isinstance(result, EvidenceGapDecision)
        self.assertEqual(
            result.decision_kind,
            "NO_JUSTIFIED_INVESTIGATION_IDENTIFIED",
        )
        self.assertIsNone(result.action_id)

    def test_timeout_is_typed_provider_problem_and_not_retried(self) -> None:
        post = Mock(side_effect=Timeout("slow"))

        result = LocalEvidenceGapPlanner(post=post).decide(_context())

        self.assertEqual(_problem_reason(result), "provider_request_failed")
        post.assert_called_once()

    def test_unsuccessful_http_status_is_provider_http_problem(self) -> None:
        post = Mock(return_value=_response({}, status=503))

        result = LocalEvidenceGapPlanner(post=post).decide(_context())

        self.assertEqual(_problem_reason(result), "provider_http_error")

    def test_malformed_outer_json_is_provider_response_problem(self) -> None:
        response = Mock()
        response.status_code = 200
        response.json.side_effect = ValueError("bad outer")

        result = LocalEvidenceGapPlanner(post=Mock(return_value=response)).decide(_context())

        self.assertEqual(_problem_reason(result), "provider_response_malformed")

    def test_missing_provider_choice_is_provider_response_problem(self) -> None:
        response = Mock()
        response.status_code = 200
        response.json.return_value = {"choices": []}

        result = LocalEvidenceGapPlanner(post=Mock(return_value=response)).decide(_context())

        self.assertEqual(_problem_reason(result), "provider_response_malformed")

    def test_missing_message_content_is_provider_response_problem(self) -> None:
        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "choices": [{"finish_reason": "stop", "message": {}}]
        }

        result = LocalEvidenceGapPlanner(post=Mock(return_value=response)).decide(_context())

        self.assertEqual(_problem_reason(result), "provider_response_malformed")

    def test_completion_length_stop_is_typed_truncation_problem(self) -> None:
        post = Mock(
            return_value=_response(
                {
                    "decision_kind": "ACTION_SELECTED",
                    "action_id": _ACTION_ID,
                    "explanation": "Incomplete decision.",
                },
                finish_reason="length",
            )
        )

        result = LocalEvidenceGapPlanner(post=post).decide(_context())

        self.assertEqual(_problem_reason(result), "completion_truncated")

    def test_malformed_inner_json_is_structured_output_problem(self) -> None:
        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "choices": [
                {
                    "finish_reason": "stop",
                    "message": {"content": "not-json"},
                }
            ]
        }

        result = LocalEvidenceGapPlanner(post=Mock(return_value=response)).decide(_context())

        self.assertEqual(_problem_reason(result), "structured_output_invalid")

    def test_schema_shaped_but_semantically_invalid_decision_is_structured_output_problem(self) -> None:
        post = Mock(
            return_value=_response(
                {
                    "decision_kind": "QUESTION_SETTLED",
                    "action_id": _ACTION_ID,
                    "explanation": "Attempt to combine a no-action decision with an action ID.",
                }
            )
        )

        result = LocalEvidenceGapPlanner(post=post).decide(_context())

        self.assertEqual(_problem_reason(result), "structured_output_invalid")

    def test_extra_model_authority_field_is_structured_output_problem(self) -> None:
        post = Mock(
            return_value=_response(
                {
                    "decision_kind": "ACTION_SELECTED",
                    "action_id": _ACTION_ID,
                    "explanation": "Attempt to widen authority.",
                    "path": "secrets.txt",
                }
            )
        )

        result = LocalEvidenceGapPlanner(post=post).decide(_context())

        self.assertEqual(_problem_reason(result), "structured_output_invalid")

    def test_loopback_session_ignores_ambient_proxy_configuration(self) -> None:
        with build_lm_studio_session() as session:
            self.assertFalse(session.trust_env)


def _target_proposition() -> PropositionAssessment:
    return PropositionAssessment(
        key=_TARGET_PROPOSITION,
        state="unresolved",
        evidence_coverage="insufficient",
        evidence_owner="target.python",
        detail="The exact target Python declaration has not yet been acquired.",
    )


def _planning_evidence() -> PlanningEvidence:
    return PlanningEvidence(
        evidence_kind="ci_dependency_consumption",
        summary=(
            "The exact-head docs environment has static transitive reachability to the changed "
            "dependency; this is not runtime compatibility proof."
        ),
        facts=(
            PlanningEvidenceFact(name="consumption_state", value="supported"),
            PlanningEvidenceFact(name="reachability_kind", value="transitive"),
            PlanningEvidenceFact(
                name="witness_path",
                value=("mkdocs-llmstxt", "beautifulsoup4", "soupsieve"),
            ),
        ),
    )


def _action() -> EvidenceGapActionDescriptor:
    return EvidenceGapActionDescriptor(
        action_id=_ACTION_ID,
        purpose="Acquire the exact target Python declaration.",
        target_proposition=_TARGET_PROPOSITION,
        evidence_yield=(
            "Exact target Python declaration evidence or a typed target-declaration problem."
        ),
    )


def _context() -> EvidenceGapPlannerContext:
    return EvidenceGapPlannerContext(
        planning_question=(
            "What additional admitted investigation, if any, is useful for determining whether "
            "the established upstream Python-support drop intersects the target declaration?"
        ),
        dependency_transition=EvidenceGapDependencyTransition(
            normalized_package="soupsieve",
            old_version="2.6",
            proposed_version="2.8.4",
        ),
        propositions=(_target_proposition(),),
        planning_evidence=(_planning_evidence(),),
        consumed_actions=(),
        planning_budget=EvidenceGapPlanningBudget(remaining_investigations=1),
        allowed_actions=(_action(),),
    )


def _no_action_context() -> EvidenceGapPlannerContext:
    return EvidenceGapPlannerContext(
        planning_question="Is another admitted investigation useful for this bounded question?",
        dependency_transition=EvidenceGapDependencyTransition(
            normalized_package="soupsieve",
            old_version="2.6",
            proposed_version="2.8.4",
        ),
        propositions=(
            PropositionAssessment(
                key="decision_critical_gap_present",
                state="refuted",
                evidence_coverage="sufficient",
                evidence_owner="investigation.stopping",
                detail="No decision-critical evidence gap remains for the bounded question.",
            ),
        ),
        planning_evidence=(),
        consumed_actions=(),
        planning_budget=EvidenceGapPlanningBudget(remaining_investigations=1),
        allowed_actions=(),
    )


def _problem_reason(result: object) -> str:
    if not isinstance(result, EvidenceGapModelInvocationProblem):
        raise AssertionError(
            f"Expected EvidenceGapModelInvocationProblem, got {type(result).__name__}."
        )
    return result.reason


if __name__ == "__main__":
    unittest.main()
