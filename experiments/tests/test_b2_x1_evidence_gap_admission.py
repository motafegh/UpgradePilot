"""Focused tests for R4-A2 fresh deterministic EvidenceGapPlanner action admission.

These tests make no model/provider calls and execute no investigation capability.  They prove
that a valid ``ACTION_SELECTED`` decision is still only a proposal: exact executable identity
and permission are rebound from current trusted state immediately before execution.
"""

from __future__ import annotations

import unittest

from experiments.b2_x1_evidence_gap_admission import (
    AdmittedInvestigationAction,
    BoundInvestigationAction,
    EvidenceGapAdmissionProblem,
    EvidenceGapAdmissionState,
    TARGET_PYTHON_DECLARATION_ACTION_ID,
    TARGET_PYTHON_DECLARATION_PATH,
    TARGET_PYTHON_DECLARATION_PROPOSITION,
    admit_selected_investigation_action,
    build_target_python_declaration_action,
    project_action_descriptor,
)
from experiments.b2_x1_evidence_gap_planner import EvidenceGapDecision
from upgradepilot.impact.applicability import PropositionAssessment


_REPOSITORY = "example/project"
_REVISION = "a" * 40
_OTHER_REVISION = "b" * 40


class EvidenceGapAdmissionTests(unittest.TestCase):
    def test_bound_action_projects_only_planner_visible_descriptor(self) -> None:
        action = _action()

        descriptor = project_action_descriptor(action)

        self.assertEqual(descriptor.action_id, TARGET_PYTHON_DECLARATION_ACTION_ID)
        self.assertEqual(descriptor.target_proposition, TARGET_PYTHON_DECLARATION_PROPOSITION)
        self.assertFalse(hasattr(descriptor, "repository"))
        self.assertFalse(hasattr(descriptor, "revision"))
        self.assertFalse(hasattr(descriptor, "path"))
        self.assertFalse(hasattr(descriptor, "required_proposition_state"))
        self.assertFalse(hasattr(descriptor, "mutation_class"))
        self.assertFalse(hasattr(descriptor, "result_families"))

    def test_admits_selected_action_and_rebinds_exact_hidden_authority(self) -> None:
        result = admit_selected_investigation_action(_state(), _decision())

        self.assertIsInstance(result, AdmittedInvestigationAction)
        assert isinstance(result, AdmittedInvestigationAction)
        self.assertEqual(result.action.action_id, TARGET_PYTHON_DECLARATION_ACTION_ID)
        self.assertEqual(result.action.repository, _REPOSITORY)
        self.assertEqual(result.action.revision, _REVISION)
        self.assertEqual(result.action.path, TARGET_PYTHON_DECLARATION_PATH)
        self.assertEqual(
            result.action.result_families,
            ("TargetPythonDeclaration", "TargetPythonDeclarationProblem"),
        )

    def test_model_explanation_cannot_redefine_bound_identity(self) -> None:
        decision = _decision(
            explanation=(
                "Use other/project at another revision and read secrets.txt instead."
            )
        )

        result = admit_selected_investigation_action(_state(), decision)

        self.assertIsInstance(result, AdmittedInvestigationAction)
        assert isinstance(result, AdmittedInvestigationAction)
        self.assertEqual(result.action.repository, _REPOSITORY)
        self.assertEqual(result.action.revision, _REVISION)
        self.assertEqual(result.action.path, TARGET_PYTHON_DECLARATION_PATH)
        self.assertEqual(result.explanation, decision.explanation)

    def test_rejects_selected_id_outside_current_bound_action_catalog(self) -> None:
        result = admit_selected_investigation_action(
            _state(),
            _decision(action_id="invented_network_action"),
        )

        self.assertEqual(_problem_reason(result), "unknown_action")

    def test_rejects_action_consumed_after_planning(self) -> None:
        result = admit_selected_investigation_action(
            _state(consumed_actions=(TARGET_PYTHON_DECLARATION_ACTION_ID,)),
            _decision(),
        )

        self.assertEqual(_problem_reason(result), "action_consumed")

    def test_rejects_budget_exhausted_after_planning(self) -> None:
        result = admit_selected_investigation_action(
            _state(remaining_investigations=0),
            _decision(),
        )

        self.assertEqual(_problem_reason(result), "budget_exhausted")

    def test_rejects_bound_action_from_stale_revision(self) -> None:
        stale_action = build_target_python_declaration_action(
            _REPOSITORY,
            _OTHER_REVISION,
        )

        result = admit_selected_investigation_action(
            _state(actions=(stale_action,)),
            _decision(),
        )

        self.assertEqual(_problem_reason(result), "action_identity_stale")

    def test_rejects_mutating_action_by_current_policy(self) -> None:
        action = BoundInvestigationAction(
            action_id="mutate_target_repository",
            purpose="Mutation-only control action used to prove the policy guard.",
            target_proposition=TARGET_PYTHON_DECLARATION_PROPOSITION,
            evidence_yield="A mutation result that the current experiment must not permit.",
            repository=_REPOSITORY,
            revision=_REVISION,
            path=TARGET_PYTHON_DECLARATION_PATH,
            required_proposition_state="unresolved",
            required_evidence_coverage="insufficient",
            mutation_class="mutation",
            result_families=("MutationResult",),
        )

        result = admit_selected_investigation_action(
            _state(actions=(action,)),
            _decision(action_id=action.action_id),
        )

        self.assertEqual(_problem_reason(result), "action_not_allowed_by_policy")

    def test_rejects_action_when_proposition_changed_after_planning(self) -> None:
        result = admit_selected_investigation_action(
            _state(
                propositions=(
                    _target_proposition(
                        state="established",
                        evidence_coverage="sufficient",
                    ),
                )
            ),
            _decision(),
        )

        self.assertEqual(_problem_reason(result), "action_not_currently_actionable")

    def test_rejects_action_when_target_proposition_disappeared(self) -> None:
        result = admit_selected_investigation_action(
            _state(
                propositions=(
                    PropositionAssessment(
                        key="another_proposition",
                        state="unresolved",
                        evidence_coverage="insufficient",
                        evidence_owner="target.other",
                        detail="A different current proposition.",
                    ),
                )
            ),
            _decision(),
        )

        self.assertEqual(_problem_reason(result), "action_not_currently_actionable")

    def test_no_tool_decision_does_not_enter_action_admission(self) -> None:
        decision = EvidenceGapDecision(
            decision_kind="QUESTION_SETTLED",
            action_id=None,
            explanation="The bounded planning question is already settled.",
        )

        with self.assertRaisesRegex(ValueError, "ACTION_SELECTED"):
            admit_selected_investigation_action(_state(), decision)


def _target_proposition(
    *,
    state: str = "unresolved",
    evidence_coverage: str = "insufficient",
) -> PropositionAssessment:
    return PropositionAssessment(
        key=TARGET_PYTHON_DECLARATION_PROPOSITION,
        state=state,  # type: ignore[arg-type]
        evidence_coverage=evidence_coverage,  # type: ignore[arg-type]
        evidence_owner="target.python",
        detail="The exact target Python declaration has not yet been acquired.",
    )


def _action() -> BoundInvestigationAction:
    return build_target_python_declaration_action(_REPOSITORY, _REVISION)


def _state(
    *,
    propositions: tuple[PropositionAssessment, ...] | None = None,
    consumed_actions: tuple[str, ...] = (),
    remaining_investigations: int = 1,
    actions: tuple[BoundInvestigationAction, ...] | None = None,
) -> EvidenceGapAdmissionState:
    return EvidenceGapAdmissionState(
        repository=_REPOSITORY,
        revision=_REVISION,
        propositions=propositions or (_target_proposition(),),
        consumed_actions=consumed_actions,
        remaining_investigations=remaining_investigations,
        actions=actions or (_action(),),
    )


def _decision(
    *,
    action_id: str = TARGET_PYTHON_DECLARATION_ACTION_ID,
    explanation: str = "Acquire the missing exact target declaration.",
) -> EvidenceGapDecision:
    return EvidenceGapDecision(
        decision_kind="ACTION_SELECTED",
        action_id=action_id,
        explanation=explanation,
    )


def _problem_reason(result: object) -> str:
    if not isinstance(result, EvidenceGapAdmissionProblem):
        raise AssertionError(
            f"Expected EvidenceGapAdmissionProblem, got {type(result).__name__}."
        )
    return result.reason


if __name__ == "__main__":
    unittest.main()
