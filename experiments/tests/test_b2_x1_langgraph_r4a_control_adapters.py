"""Offline mapping proof for the R4-A control adapters used by the R4-B LangGraph experiment."""

from __future__ import annotations

import unittest
from unittest.mock import Mock

from experiments.b2_x1_evidence_gap_model import EvidenceGapModelInvocationProblem
from experiments.b2_x1_evidence_gap_planner import EvidenceGapDecision
from experiments.langgraph.evidence_gap_workflow import (
    EvidenceGapLangGraphActionProposal,
    EvidenceGapLangGraphNoAction,
    EvidenceGapLangGraphProviderProblem,
    EvidenceGapLangGraphStartInput,
)
from experiments.langgraph.r4a_control_adapters import R4AControlPlannerAdapter
from upgradepilot.dependency.change import DependencyVersionChange
from upgradepilot.github.pull_request import PullRequestIdentity
from upgradepilot.impact.python_support import (
    build_python_support_drop_impact_candidate,
    evaluate_python_support_drop_impact,
    select_python_support_drop_investigation,
)
from upgradepilot.investigation import PublicPullRequestInvestigation
from upgradepilot.upstream.claim import GroundedPythonSupportDropClaim
from upgradepilot.upstream.interval import DependencyReleaseInterval


_REPOSITORY = "example/project"
_REVISION = "b" * 40
_ACTION_ID = "acquire_exact_target_python_declaration"
_PLANNING_QUESTION = "What bounded investigation, if any, should run now?"


class R4AControlPlannerAdapterTests(unittest.TestCase):
    def test_action_decision_maps_to_r4b_action_proposal(self) -> None:
        control = Mock()
        control.decide.return_value = EvidenceGapDecision(
            decision_kind="ACTION_SELECTED",
            action_id=_ACTION_ID,
            explanation="Acquire the exact target Python declaration.",
        )

        result = R4AControlPlannerAdapter(control).plan(_start_input())

        self.assertIsInstance(result, EvidenceGapLangGraphActionProposal)
        assert isinstance(result, EvidenceGapLangGraphActionProposal)
        self.assertEqual(result.action_id, _ACTION_ID)

    def test_no_action_decision_maps_to_r4b_no_action(self) -> None:
        control = Mock()
        control.decide.return_value = EvidenceGapDecision(
            decision_kind="QUESTION_SETTLED",
            action_id=None,
            explanation="The bounded question is settled.",
        )

        result = R4AControlPlannerAdapter(control).plan(_start_input())

        self.assertIsInstance(result, EvidenceGapLangGraphNoAction)
        assert isinstance(result, EvidenceGapLangGraphNoAction)
        self.assertEqual(result.decision_kind, "QUESTION_SETTLED")

    def test_provider_problem_maps_to_r4b_provider_problem(self) -> None:
        control = Mock()
        control.decide.return_value = EvidenceGapModelInvocationProblem(
            reason="provider_request_failed",
            detail="The controlled provider request failed.",
        )

        result = R4AControlPlannerAdapter(control).plan(_start_input())

        self.assertIsInstance(result, EvidenceGapLangGraphProviderProblem)
        assert isinstance(result, EvidenceGapLangGraphProviderProblem)
        self.assertEqual(result.reason, "provider_request_failed")


def _start_input() -> EvidenceGapLangGraphStartInput:
    return EvidenceGapLangGraphStartInput(
        investigation=_investigation(),
        planning_question=_PLANNING_QUESTION,
    )


def _investigation() -> PublicPullRequestInvestigation:
    pull_request = PullRequestIdentity(
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
        build_python_support_drop_impact_candidate(
            pull_request,
            dependency,
            claim,
        )
    )
    selection = select_python_support_drop_investigation(assessment)
    assert selection is not None
    return PublicPullRequestInvestigation(
        pull_request=pull_request,
        changed_files=(),
        dependency_result=dependency,
        target_python_result=None,
        workflow_evidence=(),
        ci_coverage_result=None,
        package_result=None,
        upstream_repository_result=None,
        python_support_drop_pre_investigation_result=assessment,
        python_support_drop_investigation_selection=selection,
        python_support_drop_impact_result=assessment,
    )


if __name__ == "__main__":
    unittest.main()
