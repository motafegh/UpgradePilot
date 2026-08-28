"""Focused deterministic tests for the accepted B2/X1 Phase-3B request harness.

No model/provider call is made here. The tests protect three bounded responsibilities:

- reconstruct the real protected S001 decision from the accepted protocol;
- construct the minimum development action/STOP pair needed for an early local-model smoke;
- keep evaluator-only metadata unable to influence planner-facing request bytes.

Runtime execution remains a separate local evidence gate when the admitted WSL environment is
available.
"""

from __future__ import annotations

from dataclasses import replace
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from experiments.b2_x1_phase3b_harness import (
    ACCEPTED_PROTOCOL_BLOB_SHA,
    ACCEPTED_PROTOCOL_ID,
    D_A1_CASE_KEY,
    D_A1_PLANNING_QUESTION,
    D_S004_CASE_KEY,
    D_S004_PLANNING_QUESTION,
    PlannerDecisionOracle,
    S001_CASE_KEY,
    S001_PLANNING_QUESTION,
    S001_REQUIRED_GIT_BLOBS,
    build_development_a1_smoke_case,
    build_development_s004_stop_case,
    build_s001_protected_case,
    render_planner_request,
    render_planner_request_json,
    validate_s001_required_source_identities,
)
from experiments.b2_x1_planner_contract import (
    AGENT_PLAN_RESULT_JSON_SCHEMA,
    TARGET_PYTHON_DECLARATION_ACTION_ID,
    TARGET_PYTHON_DECLARATION_PATH,
    TARGET_PYTHON_DECLARATION_PROPOSITION,
)

_REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


class Phase3BRequestHarnessTests(unittest.TestCase):
    def test_accepted_s001_source_identity_subset_matches_checkout(self) -> None:
        problems = validate_s001_required_source_identities(_REPOSITORY_ROOT)

        self.assertEqual(problems, ())
        self.assertEqual(ACCEPTED_PROTOCOL_ID, "b2-x1-phase3a-v2")
        self.assertEqual(
            S001_REQUIRED_GIT_BLOBS["plans/B2_X1_PHASE3_EVALUATION_PROTOCOL.md"],
            ACCEPTED_PROTOCOL_BLOB_SHA,
        )

    def test_identity_validation_fails_closed_when_required_sources_are_missing(self) -> None:
        with TemporaryDirectory() as directory:
            problems = validate_s001_required_source_identities(Path(directory))

        self.assertEqual(len(problems), len(S001_REQUIRED_GIT_BLOBS))
        self.assertTrue(all(problem.observed_blob_sha is None for problem in problems))

    def test_reconstructs_real_s001_multi_proposition_state_in_frozen_order(self) -> None:
        case = build_s001_protected_case()

        self.assertEqual(case.evaluation_case_key, S001_CASE_KEY)
        self.assertEqual(case.planning_question, S001_PLANNING_QUESTION)
        self.assertEqual(case.snapshot.repository, "pydantic/pydantic")
        self.assertEqual(case.snapshot.pull_number, 13432)
        self.assertEqual(
            case.snapshot.revision,
            "aa2dc024d33f61cdef50bf1973ab5adf0a974f5a",
        )
        self.assertEqual(
            tuple(proposition.key for proposition in case.snapshot.propositions),
            (
                "dependency_change_established",
                "upstream_python_support_drop_established",
                TARGET_PYTHON_DECLARATION_PROPOSITION,
                "declared_python_range_intersects_dropped_line",
                "selected_environment_dependency_consumption_established",
            ),
        )
        self.assertEqual(
            tuple(proposition.state for proposition in case.snapshot.propositions),
            ("established", "established", "unresolved", "unresolved", "established"),
        )

    def test_s001_action_locator_and_result_semantics_remain_prebound(self) -> None:
        case = build_s001_protected_case()

        self.assertEqual(len(case.snapshot.allowed_actions), 1)
        action = case.snapshot.allowed_actions[0]
        self.assertEqual(action.action_id, TARGET_PYTHON_DECLARATION_ACTION_ID)
        self.assertEqual(action.target_proposition, TARGET_PYTHON_DECLARATION_PROPOSITION)
        self.assertEqual(action.repository, case.snapshot.repository)
        self.assertEqual(action.revision, case.snapshot.revision)
        self.assertEqual(action.path, TARGET_PYTHON_DECLARATION_PATH)
        self.assertEqual(action.mutation_class, "read_only")
        self.assertEqual(
            action.result_families,
            ("TargetPythonDeclaration", "TargetPythonDeclarationProblem"),
        )

    def test_development_a1_smoke_is_the_minimal_choose_action_control(self) -> None:
        case = build_development_a1_smoke_case()

        self.assertEqual(case.evaluation_case_key, D_A1_CASE_KEY)
        self.assertEqual(case.planning_question, D_A1_PLANNING_QUESTION)
        self.assertEqual(case.snapshot.repository, "example/project")
        self.assertEqual(case.snapshot.pull_number, 7)
        self.assertEqual(case.snapshot.revision, "b" * 40)
        self.assertEqual(len(case.snapshot.propositions), 1)
        proposition = case.snapshot.propositions[0]
        self.assertEqual(proposition.key, TARGET_PYTHON_DECLARATION_PROPOSITION)
        self.assertEqual(proposition.state, "unresolved")
        self.assertEqual(proposition.evidence_coverage, "insufficient")
        self.assertEqual(len(case.snapshot.allowed_actions), 1)
        self.assertEqual(
            case.snapshot.allowed_actions[0].action_id,
            TARGET_PYTHON_DECLARATION_ACTION_ID,
        )
        self.assertEqual(case.oracle.expected_state, "choose_action")
        self.assertEqual(case.oracle.expected_action_id, TARGET_PYTHON_DECLARATION_ACTION_ID)
        self.assertIsNone(case.oracle.baseline_relationship)

    def test_development_s004_is_real_no_tool_stop_control(self) -> None:
        case = build_development_s004_stop_case()

        self.assertEqual(case.evaluation_case_key, D_S004_CASE_KEY)
        self.assertEqual(case.planning_question, D_S004_PLANNING_QUESTION)
        self.assertEqual(case.snapshot.repository, "googlefonts/glyphsLib")
        self.assertEqual(case.snapshot.pull_number, 1145)
        self.assertEqual(
            case.snapshot.revision,
            "f3cda8a94600e58d27f1bc17c99b7693718b6350",
        )
        self.assertEqual(case.snapshot.allowed_actions, ())
        self.assertEqual(case.snapshot.remaining_steps, 1)
        self.assertEqual(
            tuple(proposition.state for proposition in case.snapshot.propositions),
            ("established", "established", "established", "established", "refuted"),
        )
        self.assertEqual(case.oracle.expected_state, "stop")
        self.assertIsNone(case.oracle.expected_action_id)
        self.assertEqual(
            case.oracle.target_proposition,
            "decision_critical_contradiction_or_gap_present",
        )
        self.assertIsNone(case.oracle.baseline_relationship)

    def test_development_cases_use_same_oracle_isolating_renderer(self) -> None:
        for case in (
            build_development_a1_smoke_case(),
            build_development_s004_stop_case(),
        ):
            request = render_planner_request(case)
            snapshot = request["snapshot"]
            assert isinstance(snapshot, dict)

            self.assertNotIn("case_key", snapshot)
            rendered = render_planner_request_json(case)
            self.assertNotIn(case.evaluation_case_key, rendered)
            self.assertNotIn("expected_state", rendered)
            self.assertNotIn("expected_action_id", rendered)
            self.assertNotIn("baseline_relationship", rendered)

    def test_renderer_exposes_only_admitted_top_level_request_fields(self) -> None:
        request = render_planner_request(build_s001_protected_case())

        self.assertEqual(
            tuple(request),
            ("task", "planning_question", "snapshot", "output_schema"),
        )
        self.assertEqual(request["planning_question"], S001_PLANNING_QUESTION)
        self.assertEqual(request["output_schema"], AGENT_PLAN_RESULT_JSON_SCHEMA)

        snapshot = request["snapshot"]
        assert isinstance(snapshot, dict)
        self.assertNotIn("case_key", snapshot)
        self.assertEqual(snapshot["repository"], "pydantic/pydantic")
        self.assertEqual(snapshot["pull_number"], 13432)
        self.assertEqual(snapshot["remaining_steps"], 1)

    def test_evaluator_case_keys_and_oracle_do_not_influence_model_facing_request(self) -> None:
        case = build_s001_protected_case()
        original = render_planner_request_json(case)

        # Deliberately make evaluator-only metadata maximally revealing. If the renderer is
        # correctly layered, none of these changes can affect the model-facing bytes.
        altered_snapshot = replace(case.snapshot, case_key="protected-secret-stop-answer")
        altered_case = replace(
            case,
            evaluation_case_key="protected-secret-defer-answer",
            snapshot=altered_snapshot,
            oracle=PlannerDecisionOracle(
                expected_state="stop",
                expected_action_id=None,
                target_proposition="different_hidden_oracle_target",
                baseline_relationship="non_comparative",
            ),
        )

        self.assertEqual(render_planner_request_json(altered_case), original)
        self.assertNotIn(S001_CASE_KEY, original)
        self.assertNotIn("protected-secret", original)
        self.assertNotIn("baseline_relationship", original)
        self.assertNotIn("expected_state", original)
        self.assertNotIn("oracle", original)

    def test_renderer_preserves_proposition_order_and_prebound_action_fields(self) -> None:
        request = render_planner_request(build_s001_protected_case())
        snapshot = request["snapshot"]
        assert isinstance(snapshot, dict)

        propositions = snapshot["propositions"]
        assert isinstance(propositions, list)
        self.assertEqual(
            [item["key"] for item in propositions],  # type: ignore[index]
            [
                "dependency_change_established",
                "upstream_python_support_drop_established",
                TARGET_PYTHON_DECLARATION_PROPOSITION,
                "declared_python_range_intersects_dropped_line",
                "selected_environment_dependency_consumption_established",
            ],
        )

        actions = snapshot["allowed_actions"]
        assert isinstance(actions, list)
        self.assertEqual(len(actions), 1)
        action = actions[0]
        self.assertEqual(action["action_id"], TARGET_PYTHON_DECLARATION_ACTION_ID)
        self.assertEqual(action["repository"], "pydantic/pydantic")
        self.assertEqual(
            action["revision"],
            "aa2dc024d33f61cdef50bf1973ab5adf0a974f5a",
        )
        self.assertEqual(action["path"], TARGET_PYTHON_DECLARATION_PATH)

    def test_renderer_returns_schema_copy_not_mutable_global_authority(self) -> None:
        request = render_planner_request(build_s001_protected_case())
        schema = request["output_schema"]
        assert isinstance(schema, dict)

        schema["additionalProperties"] = True

        self.assertIs(AGENT_PLAN_RESULT_JSON_SCHEMA["additionalProperties"], False)

    def test_canonical_json_render_is_stable_and_parseable(self) -> None:
        case = build_s001_protected_case()

        first = render_planner_request_json(case)
        second = render_planner_request_json(case)

        self.assertEqual(first, second)
        decoded = json.loads(first)
        self.assertEqual(decoded["planning_question"], S001_PLANNING_QUESTION)
        self.assertNotIn("case_key", decoded["snapshot"])


if __name__ == "__main__":  # pragma: no cover - convenience for direct local execution.
    unittest.main()
