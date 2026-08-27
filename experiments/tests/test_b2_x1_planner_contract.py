from __future__ import annotations

import unittest

from experiments.b2_x1_planner_contract import (
    AdmittedInvestigationAction,
    AdmittedNoToolDisposition,
    AgentPlanResult,
    AllowedInvestigationAction,
    AttemptedInvestigationAction,
    InvestigationActionArguments,
    InvestigationSnapshot,
    PlanAdmissionProblem,
    TARGET_PYTHON_DECLARATION_ACTION_ID,
    TARGET_PYTHON_DECLARATION_PATH,
    TARGET_PYTHON_DECLARATION_PROPOSITION,
    admit_agent_plan,
    build_target_python_declaration_action,
)
from upgradepilot.impact.applicability import PropositionAssessment

_REPOSITORY = "example/project"
_REVISION = "a" * 40
_OTHER_REVISION = "b" * 40


class PlannerAdmissionContractTests(unittest.TestCase):
    def test_admits_exact_read_only_target_python_action(self) -> None:
        snapshot = _snapshot()

        result = admit_agent_plan(snapshot, _target_action_plan())

        self.assertIsInstance(result, AdmittedInvestigationAction)
        assert isinstance(result, AdmittedInvestigationAction)
        self.assertEqual(result.action.action_id, TARGET_PYTHON_DECLARATION_ACTION_ID)
        self.assertEqual(result.arguments.repository, _REPOSITORY)
        self.assertEqual(result.arguments.revision, _REVISION)
        self.assertEqual(result.arguments.path, TARGET_PYTHON_DECLARATION_PATH)

    def test_rejects_action_outside_trusted_catalog(self) -> None:
        snapshot = _snapshot()
        plan = _target_action_plan(selected_action_id="invented_network_action")

        result = admit_agent_plan(snapshot, plan)

        self.assertEqual(_problem_reason(result), "unknown_action")

    def test_rejects_model_selected_repository(self) -> None:
        snapshot = _snapshot()
        plan = _target_action_plan(
            arguments=InvestigationActionArguments(
                repository="other/project",
                revision=_REVISION,
                path=TARGET_PYTHON_DECLARATION_PATH,
            )
        )

        result = admit_agent_plan(snapshot, plan)

        self.assertEqual(_problem_reason(result), "action_arguments_mismatch")

    def test_rejects_model_selected_revision(self) -> None:
        snapshot = _snapshot()
        plan = _target_action_plan(
            arguments=InvestigationActionArguments(
                repository=_REPOSITORY,
                revision=_OTHER_REVISION,
                path=TARGET_PYTHON_DECLARATION_PATH,
            )
        )

        result = admit_agent_plan(snapshot, plan)

        self.assertEqual(_problem_reason(result), "action_arguments_mismatch")

    def test_rejects_arbitrary_repository_path(self) -> None:
        snapshot = _snapshot()
        plan = _target_action_plan(
            arguments=InvestigationActionArguments(
                repository=_REPOSITORY,
                revision=_REVISION,
                path="secrets.txt",
            )
        )

        result = admit_agent_plan(snapshot, plan)

        self.assertEqual(_problem_reason(result), "action_arguments_mismatch")

    def test_rejects_mutating_catalog_action(self) -> None:
        read_only = build_target_python_declaration_action(_REPOSITORY, _REVISION)
        mutating = AllowedInvestigationAction(
            action_id=read_only.action_id,
            purpose=read_only.purpose,
            target_proposition=read_only.target_proposition,
            repository=read_only.repository,
            revision=read_only.revision,
            path=read_only.path,
            required_proposition_state=read_only.required_proposition_state,
            required_evidence_coverage=read_only.required_evidence_coverage,
            mutation_class="mutation",
            result_families=read_only.result_families,
            cost_class=read_only.cost_class,
        )
        snapshot = _snapshot(allowed_actions=(mutating,))

        result = admit_agent_plan(snapshot, _target_action_plan())

        self.assertEqual(_problem_reason(result), "action_not_read_only")

    def test_rejects_blind_repeat(self) -> None:
        snapshot = _snapshot(
            attempted_actions=(
                AttemptedInvestigationAction(
                    action_id=TARGET_PYTHON_DECLARATION_ACTION_ID,
                    outcome="problem",
                ),
            )
        )

        result = admit_agent_plan(snapshot, _target_action_plan())

        self.assertEqual(_problem_reason(result), "action_already_attempted")

    def test_rejects_action_when_step_budget_is_exhausted(self) -> None:
        snapshot = _snapshot(remaining_steps=0)

        result = admit_agent_plan(snapshot, _target_action_plan())

        self.assertEqual(_problem_reason(result), "budget_exhausted")

    def test_rejects_action_after_target_proposition_is_established(self) -> None:
        snapshot = _snapshot(
            propositions=(
                _target_proposition(state="established", evidence_coverage="sufficient"),
            )
        )

        result = admit_agent_plan(snapshot, _target_action_plan())

        self.assertEqual(_problem_reason(result), "target_proposition_not_actionable")

    def test_rejects_target_proposition_substitution(self) -> None:
        snapshot = _snapshot()
        plan = _target_action_plan(target_proposition="some_other_question")

        result = admit_agent_plan(snapshot, plan)

        self.assertEqual(_problem_reason(result), "target_proposition_mismatch")

    def test_rejects_catalog_action_bound_to_another_revision(self) -> None:
        stale_action = build_target_python_declaration_action(
            _REPOSITORY,
            _OTHER_REVISION,
        )
        snapshot = _snapshot(allowed_actions=(stale_action,))

        result = admit_agent_plan(
            snapshot,
            _target_action_plan(
                arguments=InvestigationActionArguments(
                    repository=_REPOSITORY,
                    revision=_OTHER_REVISION,
                    path=TARGET_PYTHON_DECLARATION_PATH,
                )
            ),
        )

        self.assertEqual(_problem_reason(result), "action_identity_mismatch")

    def test_stop_admits_no_tool_execution(self) -> None:
        snapshot = _snapshot()
        plan = AgentPlanResult(
            state="stop",
            selected_action_id=None,
            arguments=None,
            target_proposition=TARGET_PYTHON_DECLARATION_PROPOSITION,
            reason="No further admitted evidence is useful for this bounded question.",
            expected_result_categories=(),
            limitations=("Stopping does not establish compatibility.",),
        )

        result = admit_agent_plan(snapshot, plan)

        self.assertIsInstance(result, AdmittedNoToolDisposition)
        assert isinstance(result, AdmittedNoToolDisposition)
        self.assertEqual(result.state, "stop")

    def test_defer_admits_no_tool_execution(self) -> None:
        snapshot = _snapshot()
        plan = AgentPlanResult(
            state="defer",
            selected_action_id=None,
            arguments=None,
            target_proposition=TARGET_PYTHON_DECLARATION_PROPOSITION,
            reason="The remaining question is outside the admitted action catalog.",
            expected_result_categories=(),
            limitations=("Deferred evidence remains unresolved.",),
        )

        result = admit_agent_plan(snapshot, plan)

        self.assertIsInstance(result, AdmittedNoToolDisposition)
        assert isinstance(result, AdmittedNoToolDisposition)
        self.assertEqual(result.state, "defer")

    def test_no_tool_disposition_cannot_smuggle_action_arguments(self) -> None:
        snapshot = _snapshot()
        plan = AgentPlanResult(
            state="stop",
            selected_action_id=TARGET_PYTHON_DECLARATION_ACTION_ID,
            arguments=_target_arguments(),
            target_proposition=TARGET_PYTHON_DECLARATION_PROPOSITION,
            reason="Stop.",
            expected_result_categories=(),
            limitations=(),
        )

        result = admit_agent_plan(snapshot, plan)

        self.assertEqual(_problem_reason(result), "invalid_plan_shape")

    def test_choose_action_requires_arguments(self) -> None:
        snapshot = _snapshot()
        plan = AgentPlanResult(
            state="choose_action",
            selected_action_id=TARGET_PYTHON_DECLARATION_ACTION_ID,
            arguments=None,
            target_proposition=TARGET_PYTHON_DECLARATION_PROPOSITION,
            reason="Acquire the missing exact target declaration.",
            expected_result_categories=(
                "TargetPythonDeclaration",
                "TargetPythonDeclarationProblem",
            ),
            limitations=(),
        )

        result = admit_agent_plan(snapshot, plan)

        self.assertEqual(_problem_reason(result), "invalid_plan_shape")

    def test_unsupported_plan_state_is_not_admitted(self) -> None:
        snapshot = _snapshot()
        plan = AgentPlanResult(
            state="execute_everything",
            selected_action_id=None,
            arguments=None,
            target_proposition=TARGET_PYTHON_DECLARATION_PROPOSITION,
            reason="Attempt to widen authority.",
            expected_result_categories=(),
            limitations=(),
        )

        result = admit_agent_plan(snapshot, plan)

        self.assertEqual(_problem_reason(result), "invalid_plan_shape")



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


def _snapshot(
    *,
    propositions: tuple[PropositionAssessment, ...] | None = None,
    attempted_actions: tuple[AttemptedInvestigationAction, ...] = (),
    allowed_actions: tuple[AllowedInvestigationAction, ...] | None = None,
    remaining_steps: int = 1,
) -> InvestigationSnapshot:
    return InvestigationSnapshot(
        repository=_REPOSITORY,
        pull_number=17,
        revision=_REVISION,
        propositions=propositions or (_target_proposition(),),
        attempted_actions=attempted_actions,
        allowed_actions=allowed_actions
        or (build_target_python_declaration_action(_REPOSITORY, _REVISION),),
        remaining_steps=remaining_steps,
    )


def _target_arguments() -> InvestigationActionArguments:
    return InvestigationActionArguments(
        repository=_REPOSITORY,
        revision=_REVISION,
        path=TARGET_PYTHON_DECLARATION_PATH,
    )


def _target_action_plan(
    *,
    selected_action_id: str = TARGET_PYTHON_DECLARATION_ACTION_ID,
    arguments: InvestigationActionArguments | None = None,
    target_proposition: str = TARGET_PYTHON_DECLARATION_PROPOSITION,
) -> AgentPlanResult:
    return AgentPlanResult(
        state="choose_action",
        selected_action_id=selected_action_id,
        arguments=arguments or _target_arguments(),
        target_proposition=target_proposition,
        reason="Acquire the missing exact target declaration.",
        expected_result_categories=(
            "TargetPythonDeclaration",
            "TargetPythonDeclarationProblem",
        ),
        limitations=("The action cannot establish runtime compatibility.",),
    )


def _problem_reason(result: object) -> str:
    self_result = result
    if not isinstance(self_result, PlanAdmissionProblem):
        raise AssertionError(f"Expected PlanAdmissionProblem, got {type(result).__name__}.")
    return self_result.reason


if __name__ == "__main__":
    unittest.main()
