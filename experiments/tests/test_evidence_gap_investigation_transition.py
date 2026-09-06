"""Focused tests for the bounded investigation transition, state consequence, and replay seam.

The assertions are unchanged from the previous coordinate-named proof owner; only the module
identity and imports move to responsibility-first names.
"""

from __future__ import annotations

import unittest
from unittest.mock import Mock

from experiments.evidence_gap_action_admission import (
    AdmittedInvestigationAction,
    build_target_python_declaration_action,
)
from experiments.evidence_gap_investigation_transition import (
    EvidenceGapInvestigationState,
    EvidenceGapOperationalFailure,
    replay_evidence_gap_transition,
    run_evidence_gap_transition,
)
from experiments.evidence_gap_planner_model_boundary import EvidenceGapDecision
from upgradepilot.github.api import GitHubAcquisitionError
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.impact.python_support import (
    build_python_support_drop_impact_candidate,
    evaluate_python_support_drop_impact,
)
from upgradepilot.target.python import TargetPythonDeclaration
from upgradepilot.upstream.claim import GroundedPythonSupportDropClaim
from upgradepilot.upstream.interval import DependencyReleaseInterval
from upgradepilot.dependency.change import DependencyVersionChange
from upgradepilot.github.pull_request import PullRequestIdentity


_REPOSITORY = "example/project"
_REVISION = "b" * 40
_ACTION_ID = "acquire_exact_target_python_declaration"


class EvidenceGapTransitionTests(unittest.TestCase):
    def test_no_action_settles_without_repository_effect(self) -> None:
        repository_client = Mock()
        decision = EvidenceGapDecision(
            decision_kind="QUESTION_SETTLED",
            action_id=None,
            explanation="The bounded question is settled.",
        )
        trace = run_evidence_gap_transition(
            _state(),
            decision,
            repository_client=repository_client,
        )
        repository_client.get_exact_commit_text_file.assert_not_called()
        self.assertEqual(trace.after_state.continuation_status, "SETTLED")
        self.assertEqual(replay_evidence_gap_transition(trace), trace.after_state)

    def test_semantic_result_consumes_action_spends_budget_and_replays(self) -> None:
        repository_client = Mock()
        repository_client.get_exact_commit_text_file.return_value = RepositoryTextFile(
            repository=_REPOSITORY,
            path="pyproject.toml",
            revision=_REVISION,
            content='[project]\nrequires-python = ">=3.10"\n',
        )
        decision, admitted = _admitted_action()
        trace = run_evidence_gap_transition(
            _state(),
            decision,
            admitted_action=admitted,
            repository_client=repository_client,
        )
        self.assertIsInstance(trace.execution_result, TargetPythonDeclaration)
        self.assertEqual(trace.after_state.consumed_actions, (_ACTION_ID,))
        self.assertEqual(trace.after_state.remaining_investigations, 0)
        self.assertEqual(replay_evidence_gap_transition(trace), trace.after_state)

    def test_operational_failure_spends_budget_without_consuming_action(self) -> None:
        repository_client = Mock()
        repository_client.get_exact_commit_text_file.side_effect = GitHubAcquisitionError(
            "timeout",
            reason="timeout",
        )
        decision, admitted = _admitted_action()
        trace = run_evidence_gap_transition(
            _state(),
            decision,
            admitted_action=admitted,
            repository_client=repository_client,
        )
        self.assertIsInstance(trace.operational_failure, EvidenceGapOperationalFailure)
        self.assertEqual(trace.after_state.consumed_actions, ())
        self.assertEqual(trace.after_state.remaining_investigations, 0)
        self.assertEqual(replay_evidence_gap_transition(trace), trace.after_state)


def _admitted_action() -> tuple[EvidenceGapDecision, AdmittedInvestigationAction]:
    decision = EvidenceGapDecision(
        decision_kind="ACTION_SELECTED",
        action_id=_ACTION_ID,
        explanation="Acquire exact target declaration.",
    )
    admitted = AdmittedInvestigationAction(
        action=build_target_python_declaration_action(_REPOSITORY, _REVISION),
        explanation=decision.explanation,
    )
    return decision, admitted


def _state() -> EvidenceGapInvestigationState:
    pull_request = PullRequestIdentity(
        repository=_REPOSITORY,
        number=1,
        title="Bump soupsieve",
        state="open",
        merged=False,
        author="dependabot[bot]",
        base_ref="main",
        base_sha="a" * 40,
        head_ref="dependabot/soupsieve",
        head_sha=_REVISION,
        changed_files=1,
    )
    dependency = DependencyVersionChange(
        package="soupsieve",
        normalized_package="soupsieve",
        old_version="2.6",
        proposed_version="2.8.4",
        source_evidence=(),
    )
    claim = GroundedPythonSupportDropClaim(
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
    assessment = evaluate_python_support_drop_impact(
        build_python_support_drop_impact_candidate(pull_request, dependency, claim)
    )
    return EvidenceGapInvestigationState(
        python_support_assessment=assessment,
        consumed_actions=(),
        remaining_investigations=1,
    )


if __name__ == "__main__":
    unittest.main()
