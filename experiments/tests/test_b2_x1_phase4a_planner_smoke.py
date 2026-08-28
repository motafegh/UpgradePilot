"""Offline tests for the first B2/X1 Phase-4A local planner smoke runner.

These tests never contact LM Studio. They protect the request/response/admission plumbing so a
later live smoke can distinguish transport/model behavior from local harness-shape defects.
"""

from __future__ import annotations

import json
import unittest
from unittest.mock import patch

from experiments.b2_x1_phase3b_harness import (
    build_development_a1_smoke_case,
    build_development_s004_stop_case,
)
from experiments.b2_x1_phase4a_planner_smoke import (
    DEFAULT_MODEL,
    build_lmstudio_payload,
    parse_structured_plan,
    run_development_decision,
)
from experiments.b2_x1_planner_contract import (
    AdmittedInvestigationAction,
    AdmittedNoToolDisposition,
    TARGET_PYTHON_DECLARATION_ACTION_ID,
    TARGET_PYTHON_DECLARATION_PROPOSITION,
)


def _outer_response(inner: dict[str, object]) -> dict[str, object]:
    return {
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": json.dumps(inner, separators=(",", ":"), sort_keys=True),
                }
            }
        ]
    }


def _a1_plan_mapping() -> dict[str, object]:
    return {
        "state": "choose_action",
        "selected_action_id": TARGET_PYTHON_DECLARATION_ACTION_ID,
        "target_proposition": TARGET_PYTHON_DECLARATION_PROPOSITION,
        "reason": "The exact target declaration is the remaining discriminating evidence gap.",
        "expected_result_categories": [
            "TargetPythonDeclaration",
            "TargetPythonDeclarationProblem",
        ],
        "limitations": [
            "This action does not establish compatibility or upgrade safety."
        ],
    }


def _s004_stop_mapping() -> dict[str, object]:
    return {
        "state": "stop",
        "selected_action_id": None,
        "target_proposition": "decision_critical_contradiction_or_gap_present",
        "reason": "The bounded authority question is already sufficiently settled.",
        "expected_result_categories": [],
        "limitations": [],
    }


class Phase4APlannerSmokeOfflineTests(unittest.TestCase):
    def test_payload_uses_strict_schema_and_excludes_evaluator_metadata(self) -> None:
        case = build_development_a1_smoke_case()
        payload = build_lmstudio_payload(case, model=DEFAULT_MODEL)

        self.assertEqual(payload["model"], DEFAULT_MODEL)
        self.assertEqual(payload["temperature"], 0)
        self.assertEqual(payload["seed"], 0)
        self.assertIs(payload["stream"], False)

        response_format = payload["response_format"]
        assert isinstance(response_format, dict)
        schema_wrapper = response_format["json_schema"]
        assert isinstance(schema_wrapper, dict)
        self.assertIs(schema_wrapper["strict"], True)

        messages = payload["messages"]
        assert isinstance(messages, list)
        user_content = messages[1]["content"]  # type: ignore[index]
        assert isinstance(user_content, str)
        decoded = json.loads(user_content)
        self.assertEqual(
            tuple(decoded),
            ("planning_question", "snapshot"),
        )
        self.assertNotIn("case_key", decoded["snapshot"])

        serialized = json.dumps(payload, sort_keys=True)
        self.assertNotIn(case.evaluation_case_key, serialized)
        self.assertNotIn("expected_state", serialized)
        self.assertNotIn("expected_action_id", serialized)
        self.assertNotIn("baseline_relationship", serialized)
        self.assertNotIn("oracle", serialized)

    def test_stop_payload_has_no_admitted_action_but_keeps_remaining_budget(self) -> None:
        case = build_development_s004_stop_case()
        payload = build_lmstudio_payload(case, model=DEFAULT_MODEL)

        messages = payload["messages"]
        assert isinstance(messages, list)
        decoded = json.loads(messages[1]["content"])  # type: ignore[index]
        snapshot = decoded["snapshot"]
        self.assertEqual(snapshot["allowed_actions"], [])
        self.assertEqual(snapshot["remaining_steps"], 1)

    def test_parses_schema_valid_choose_action_without_granting_authority(self) -> None:
        plan, raw = parse_structured_plan(_outer_response(_a1_plan_mapping()))

        self.assertEqual(plan.state, "choose_action")
        self.assertEqual(plan.selected_action_id, TARGET_PYTHON_DECLARATION_ACTION_ID)
        self.assertEqual(plan.target_proposition, TARGET_PYTHON_DECLARATION_PROPOSITION)
        self.assertEqual(json.loads(raw), _a1_plan_mapping())

    def test_development_action_decision_is_admitted_after_parsing(self) -> None:
        case = build_development_a1_smoke_case()

        with patch(
            "experiments.b2_x1_phase4a_planner_smoke.post_completion",
            return_value=(_outer_response(_a1_plan_mapping()), 0.25),
        ):
            decision = run_development_decision(
                case,
                repetition=1,
                base_url="http://127.0.0.1:12345",
                model=DEFAULT_MODEL,
            )

        self.assertEqual(decision.plan.state, "choose_action")
        self.assertEqual(decision.admission_kind, "admitted_action")
        self.assertIsInstance(decision.admission, AdmittedInvestigationAction)
        self.assertTrue(decision.basic_expectation_match)
        self.assertEqual(decision.elapsed_seconds, 0.25)

    def test_development_stop_decision_admits_no_tool_execution(self) -> None:
        case = build_development_s004_stop_case()

        with patch(
            "experiments.b2_x1_phase4a_planner_smoke.post_completion",
            return_value=(_outer_response(_s004_stop_mapping()), 0.1),
        ):
            decision = run_development_decision(
                case,
                repetition=1,
                base_url="http://127.0.0.1:12345",
                model=DEFAULT_MODEL,
            )

        self.assertEqual(decision.plan.state, "stop")
        self.assertEqual(decision.admission_kind, "admitted_no_tool")
        self.assertIsInstance(decision.admission, AdmittedNoToolDisposition)
        self.assertTrue(decision.basic_expectation_match)
        self.assertEqual(decision.elapsed_seconds, 0.1)

    def test_malformed_lmstudio_envelope_is_rejected(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "no usable first choice"):
            parse_structured_plan({"choices": []})


if __name__ == "__main__":
    unittest.main()
