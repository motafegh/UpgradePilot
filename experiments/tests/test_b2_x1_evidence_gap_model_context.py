"""Focused deterministic tests for the R2 EvidenceGapPlanner model-visible context.

These tests do not call a model/provider. They protect the field-level projection decision:
trusted state needed for evidence-gap reasoning is visible, while evaluator/oracle data, raw
untrusted channels, verbose policy text, and action-owned locator metadata remain outside the
model context.
"""

from __future__ import annotations

from dataclasses import replace
import json
import unittest

from experiments.b2_x1_evidence_gap_model_context import (
    build_evidence_gap_model_context,
    render_evidence_gap_model_context_json,
)
from experiments.b2_x1_phase3b_harness import (
    build_development_a1_smoke_case,
    build_development_s004_stop_case,
    build_s001_protected_case,
)
from experiments.b2_x1_planner_contract import (
    AttemptedInvestigationAction,
    TARGET_PYTHON_DECLARATION_ACTION_ID,
)
from upgradepilot.dependency.change import DependencyVersionChange


def _dependency_change(
    package: str,
    old_version: str,
    proposed_version: str,
) -> DependencyVersionChange:
    """Build only the trusted transition fields needed by this projection test."""

    return DependencyVersionChange(
        package=package,
        normalized_package=package.lower(),
        old_version=old_version,
        proposed_version=proposed_version,
        source_evidence=(),
    )


class EvidenceGapModelContextTests(unittest.TestCase):
    def test_s001_context_carries_exact_r2_fields_and_structured_transition(self) -> None:
        case = build_s001_protected_case()
        context = build_evidence_gap_model_context(
            case,
            _dependency_change("soupsieve", "2.6", "2.8.4"),
        )

        self.assertEqual(
            tuple(context),
            (
                "planning_question",
                "case_identity",
                "dependency_transition",
                "propositions",
                "attempted_actions",
                "remaining_budget",
                "allowed_actions",
            ),
        )
        self.assertEqual(
            context["case_identity"],
            {
                "repository": "pydantic/pydantic",
                "pull_number": 13432,
                "revision": "aa2dc024d33f61cdef50bf1973ab5adf0a974f5a",
            },
        )
        self.assertEqual(
            context["dependency_transition"],
            {
                "package": "soupsieve",
                "old_version": "2.6",
                "proposed_version": "2.8.4",
            },
        )

        propositions = context["propositions"]
        assert isinstance(propositions, list)
        self.assertTrue(propositions)
        self.assertEqual(
            tuple(propositions[0]),
            ("key", "state", "evidence_coverage", "detail"),
        )
        self.assertNotIn("evidence_owner", propositions[0])

        actions = context["allowed_actions"]
        assert isinstance(actions, list)
        self.assertEqual(len(actions), 1)
        action = actions[0]
        self.assertEqual(action["action_id"], TARGET_PYTHON_DECLARATION_ACTION_ID)
        self.assertEqual(
            tuple(action),
            (
                "action_id",
                "purpose",
                "target_proposition",
                "required_precondition",
                "cost_class",
                "mutation_class",
                "result_families",
            ),
        )
        self.assertNotIn("repository", action)
        self.assertNotIn("revision", action)
        self.assertNotIn("path", action)

    def test_real_s004_no_tool_state_renders_without_action_or_raw_context_leakage(self) -> None:
        case = build_development_s004_stop_case()
        context = build_evidence_gap_model_context(
            case,
            _dependency_change("pytest", "9.0.2", "9.0.3"),
        )

        self.assertEqual(context["allowed_actions"], [])
        self.assertEqual(context["attempted_actions"], [])
        self.assertEqual(context["remaining_budget"], {"remaining_steps": 1})
        self.assertEqual(
            context["dependency_transition"],
            {
                "package": "pytest",
                "old_version": "9.0.2",
                "proposed_version": "9.0.3",
            },
        )

        rendered = render_evidence_gap_model_context_json(
            case,
            _dependency_change("pytest", "9.0.2", "9.0.3"),
        )
        self.assertNotIn(case.evaluation_case_key, rendered)
        self.assertNotIn("oracle", rendered)
        self.assertNotIn("expected_state", rendered)
        self.assertNotIn("hard_constraints", rendered)
        self.assertNotIn("untrusted_evidence_notes", rendered)
        self.assertNotIn("evidence_owner", rendered)

    def test_attempt_history_is_typed_system_state_without_prose_memory(self) -> None:
        case = build_development_a1_smoke_case()
        repeated_snapshot = replace(
            case.snapshot,
            attempted_actions=(
                AttemptedInvestigationAction(
                    action_id=TARGET_PYTHON_DECLARATION_ACTION_ID,
                    outcome="problem",
                ),
            ),
        )
        repeated_case = replace(case, snapshot=repeated_snapshot)

        context = build_evidence_gap_model_context(
            repeated_case,
            _dependency_change("example-dependency", "1.0", "2.0"),
        )

        self.assertEqual(
            context["attempted_actions"],
            [
                {
                    "action_id": TARGET_PYTHON_DECLARATION_ACTION_ID,
                    "outcome": "problem",
                }
            ],
        )
        self.assertNotIn("reason", context["attempted_actions"][0])
        self.assertNotIn("detail", context["attempted_actions"][0])

    def test_dependency_product_metadata_is_projected_not_serialized_wholesale(self) -> None:
        case = build_development_a1_smoke_case()
        dependency_change = DependencyVersionChange(
            package="Example_Dependency",
            normalized_package="example-dependency",
            old_version="1.0",
            proposed_version="2.0",
            source_evidence=(),
            limitations=("product-owned limitation not needed for this planner turn",),
        )

        context = build_evidence_gap_model_context(case, dependency_change)
        transition = context["dependency_transition"]
        assert isinstance(transition, dict)

        self.assertEqual(
            transition,
            {
                "package": "Example_Dependency",
                "old_version": "1.0",
                "proposed_version": "2.0",
            },
        )
        self.assertNotIn("normalized_package", transition)
        self.assertNotIn("source_evidence", transition)
        self.assertNotIn("limitations", transition)

    def test_rendered_context_is_stable_json(self) -> None:
        case = build_s001_protected_case()
        dependency_change = _dependency_change("soupsieve", "2.6", "2.8.4")

        first = render_evidence_gap_model_context_json(case, dependency_change)
        second = render_evidence_gap_model_context_json(case, dependency_change)

        self.assertEqual(first, second)
        decoded = json.loads(first)
        self.assertEqual(decoded["dependency_transition"]["proposed_version"], "2.8.4")
        self.assertEqual(decoded["case_identity"]["repository"], "pydantic/pydantic")


if __name__ == "__main__":  # pragma: no cover - convenience for direct local execution.
    unittest.main()
