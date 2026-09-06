"""Focused tests for the evidence-gap investigation transition/update/trace seam.

The tests keep model selection and deterministic action admission outside this responsibility.
They prove that one already-valid branch produces the accepted immutable state update and a
replayable trace while reusing existing target/domain owners.
"""

from __future__ import annotations

import unittest
from unittest.mock import Mock

from experiments.evidence_gap_action_admission import (
    AdmittedInvestigationAction,
    build_target_python_declaration_action,
)
from experiments.evidence_gap_planner_model_boundary import EvidenceGapDecision
from experiments.evidence_gap_investigation_transition import (
    EvidenceGapInvestigationState,
    replay_evidence_gap_transition,
    run_evidence_gap_transition,
)
from upgradepilot.dependency.change import DependencyVersionChange
from upgradepilot.github.api import GitHubAcquisitionError, GitHubResponseError
from upgradepilot.github.pull_request import PullRequestIdentity
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.impact.python_support import (
    build_python_support_drop_impact_candidate,
    evaluate_python_support_drop_impact,
)
from upgradepilot.upstream.claim import GroundedPythonSupportDropClaim
from upgradepilot.upstream.interval import DependencyReleaseInterval


_REPOSITORY = "example/project"
_REVISION = "b" * 40
_ACTION_ID = "acquire_exact_target_python_declaration"


class EvidenceGapTransitionTests(unittest.TestCase):
    def test_valid_target_result_updates_domain_consumes_action_spends_budget_and_replays(
        self,
    ) -> None:
        client = Mock()
        client.get_exact_commit_text_file.return_value = RepositoryTextFile(
            repository=_REPOSITORY,
            path="pyproject.toml",
            revision=_REVISION,
            content='[project]\nname = "demo"\nrequires-python = ">=3.8"\n',
        )

        trace = run_evidence_gap_transition(
            _state(),
            _action_decision(),
            admitted_action=_admitted_action(),
            repository_client=client,
        )

        client.get_exact_commit_text_file.assert_called_once_with(
            _REPOSITORY,
            _REVISION,
            "pyproject.toml",
        )
        self.assertIsNotNone(trace.execution_result)
        self.assertIsNone(trace.operational_failure)
        self.assertEqual(trace.after_state.remaining_investigations, 0)
        self.assertEqual(trace.after_state.consumed_actions, (_ACTION_ID,))
        self.assertEqual(trace.after_state.continuation_status, "ACTIVE")
        self.assertIsNotNone(trace.after_state.python_support_assessment.target_relevance)
        assert trace.after_state.python_support_assessment.target_relevance is not None
        self.assertEqual(
            trace.after_state.python_support_assessment.target_relevance.state,
            "declared_python_overlap",
        )
        self.assertEqual(replay_evidence_gap_transition(trace), trace.after_state)

    def test_typed_target_problem_is_valid_semantic_result_and_consumes_action(self) -> None:
        client = Mock()
        client.get_exact_commit_text_file.return_value = RepositoryTextFile(
            repository=_REPOSITORY,
            path="pyproject.toml",
            revision=_REVISION,
            content='[project]\nname = "demo"\n',
        )

        trace = run_evidence_gap_transition(
            _state(),
            _action_decision(),
            admitted_action=_admitted_action(),
            repository_client=client,
        )

        self.assertIsNotNone(trace.execution_result)
        assert trace.execution_result is not None
        self.assertEqual(trace.execution_result.state, "requires_python_absent")
        self.assertIsNone(trace.operational_failure)
        self.assertEqual(trace.after_state.remaining_investigations, 0)
        self.assertEqual(trace.after_state.consumed_actions, (_ACTION_ID,))
        relevance = trace.after_state.python_support_assessment.target_relevance
        self.assertIsNotNone(relevance)
        assert relevance is not None
        self.assertEqual(relevance.state, "target_declaration_unresolved")
        self.assertEqual(replay_evidence_gap_transition(trace), trace.after_state)

    def test_timeout_spends_budget_without_consuming_or_changing_domain_state(self) -> None:
        client = Mock()
        client.get_exact_commit_text_file.side_effect = GitHubAcquisitionError(
            "GitHub repository-file acquisition timed out.",
            reason="timeout",
        )
        before = _state()

        trace = run_evidence_gap_transition(
            before,
            _action_decision(),
            admitted_action=_admitted_action(),
            repository_client=client,
        )

        self.assertIsNone(trace.execution_result)
        self.assertIsNotNone(trace.operational_failure)
        assert trace.operational_failure is not None
        self.assertEqual(trace.operational_failure.exception_type, "GitHubAcquisitionError")
        self.assertEqual(trace.operational_failure.reason, "timeout")
        self.assertEqual(trace.after_state.remaining_investigations, 0)
        self.assertEqual(trace.after_state.consumed_actions, ())
        self.assertEqual(
            trace.after_state.python_support_assessment,
            before.python_support_assessment,
        )
        self.assertEqual(replay_evidence_gap_transition(trace), trace.after_state)

    def test_untrusted_provider_response_is_operational_failure_not_domain_evidence(self) -> None:
        client = Mock()
        client.get_exact_commit_text_file.side_effect = GitHubResponseError(
            "GitHub repository-file response could not be trusted."
        )
        before = _state()

        trace = run_evidence_gap_transition(
            before,
            _action_decision(),
            admitted_action=_admitted_action(),
            repository_client=client,
        )

        self.assertIsNone(trace.execution_result)
        self.assertIsNotNone(trace.operational_failure)
        assert trace.operational_failure is not None
        self.assertEqual(trace.operational_failure.exception_type, "GitHubResponseError")
        self.assertIsNone(trace.operational_failure.reason)
        self.assertEqual(trace.after_state.remaining_investigations, 0)
        self.assertEqual(trace.after_state.consumed_actions, ())
        self.assertEqual(
            trace.after_state.python_support_assessment,
            before.python_support_assessment,
        )

    def test_no_action_decisions_change_only_the_bounded_continuation_status(self) -> None:
        cases = (
            ("QUESTION_SETTLED", "SETTLED"),
            (
                "KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY",
                "OUTSIDE_CURRENT_BOUNDARY",
            ),
            (
                "NO_JUSTIFIED_INVESTIGATION_IDENTIFIED",
                "NO_JUSTIFIED_INVESTIGATION",
            ),
        )

        for decision_kind, expected_status in cases:
            with self.subTest(decision_kind=decision_kind):
                before = _state()
                decision = EvidenceGapDecision(
                    decision_kind=decision_kind,  # type: ignore[arg-type]
                    action_id=None,
                    explanation="No investigation action should execute in this bounded turn.",
                )

                trace = run_evidence_gap_transition(before, decision)

                self.assertIsNone(trace.admitted_action)
                self.assertIsNone(trace.execution_result)
                self.assertIsNone(trace.operational_failure)
                self.assertEqual(trace.after_state.continuation_status, expected_status)
                self.assertEqual(
                    trace.after_state.remaining_investigations,
                    before.remaining_investigations,
                )
                self.assertEqual(trace.after_state.consumed_actions, before.consumed_actions)
                self.assertEqual(
                    trace.after_state.python_support_assessment,
                    before.python_support_assessment,
                )
                self.assertEqual(replay_evidence_gap_transition(trace), trace.after_state)

    def test_action_transition_requires_prior_a2_admission(self) -> None:
        with self.assertRaisesRegex(ValueError, "admitted action"):
            run_evidence_gap_transition(
                _state(),
                _action_decision(),
                repository_client=Mock(),
            )

    def test_terminal_no_action_state_cannot_enter_another_transition(self) -> None:
        settled = EvidenceGapInvestigationState(
            python_support_assessment=_assessment(),
            consumed_actions=(),
            remaining_investigations=1,
            continuation_status="SETTLED",
        )

        with self.assertRaisesRegex(ValueError, "ACTIVE"):
            run_evidence_gap_transition(
                settled,
                EvidenceGapDecision(
                    decision_kind="QUESTION_SETTLED",
                    action_id=None,
                    explanation="Already terminal for this bounded planner loop.",
                ),
            )


def _state() -> EvidenceGapInvestigationState:
    return EvidenceGapInvestigationState(
        python_support_assessment=_assessment(),
        consumed_actions=(),
        remaining_investigations=1,
    )


def _assessment():
    return evaluate_python_support_drop_impact(
        build_python_support_drop_impact_candidate(
            _pull_request(),
            _dependency(),
            _claim(),
        )
    )


def _action_decision() -> EvidenceGapDecision:
    return EvidenceGapDecision(
        decision_kind="ACTION_SELECTED",
        action_id=_ACTION_ID,
        explanation="Acquire the exact target Python declaration.",
    )


def _admitted_action() -> AdmittedInvestigationAction:
    decision = _action_decision()
    return AdmittedInvestigationAction(
        action=build_target_python_declaration_action(_REPOSITORY, _REVISION),
        explanation=decision.explanation,
    )


def _pull_request() -> PullRequestIdentity:
    return PullRequestIdentity(
        repository=_REPOSITORY,
        number=1,
        title="Bump dependency",
        state="open",
        merged=False,
        author="dependabot[bot]",
        base_ref="main",
        base_sha="a" * 40,
        head_ref="dependabot/dependency",
        head_sha=_REVISION,
        changed_files=1,
    )


def _dependency() -> DependencyVersionChange:
    return DependencyVersionChange(
        package="soupsieve",
        normalized_package="soupsieve",
        old_version="2.6",
        proposed_version="2.8.4",
        source_evidence=(),
    )


def _claim() -> GroundedPythonSupportDropClaim:
    return GroundedPythonSupportDropClaim(
        python_line="3.8",
        introduced_in_version="2.8",
        interval=DependencyReleaseInterval(
            package="soupsieve",
            normalized_package="soupsieve",
            old_version="2.6",
            proposed_version="2.8.4",
        ),
        source_evidence=(),
    )


if __name__ == "__main__":
    unittest.main()
