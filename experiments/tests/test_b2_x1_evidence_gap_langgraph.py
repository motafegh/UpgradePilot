"""Focused offline proof for the native R4-B LangGraph EvidenceGapPlanner workflow.

These tests never contact LM Studio or GitHub. They exercise R4-B-owned workflow contracts. The
existing R4-A deterministic admission implementation is used only through the explicit control
adapter, so the graph tests can hold authority semantics constant without importing R4-A state or
result representations into the LangGraph workflow contract.
"""

from __future__ import annotations

import unittest
from unittest.mock import Mock

from experiments.langgraph.evidence_gap_workflow import (
    EvidenceGapLangGraphActionProposal,
    EvidenceGapLangGraphAuthoritySnapshot,
    EvidenceGapLangGraphBaseline,
    EvidenceGapLangGraphNoAction,
    EvidenceGapLangGraphOperationalFailure,
    EvidenceGapLangGraphStartInput,
    build_evidence_gap_langgraph,
)
from experiments.langgraph.r4a_control_adapters import R4AControlAuthorityAdapter
from upgradepilot.dependency.change import DependencyVersionChange
from upgradepilot.github.api import GitHubAcquisitionError
from upgradepilot.github.pull_request import PullRequestIdentity
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.impact.python_support import (
    PythonSupportDropImpactAssessment,
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
_PLANNING_QUESTION = (
    "What additional admitted investigation, if any, is useful for determining whether the "
    "established upstream Python-support drop intersects the target declaration?"
)


class EvidenceGapLangGraphTests(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = build_evidence_gap_langgraph()
        self.authority = R4AControlAuthorityAdapter()

    def test_no_action_routes_directly_to_conclude_without_authority_or_repository_effect(self) -> None:
        start_input = _start_input()
        planner = Mock()
        planner.plan.return_value = EvidenceGapLangGraphNoAction(
            decision_kind="QUESTION_SETTLED",
            explanation="The bounded planning question is already settled.",
        )
        authority_supplier = Mock(side_effect=AssertionError("authority snapshot must not run"))
        authority = Mock(side_effect=AssertionError("authority evaluation must not run"))
        repository_reader = Mock()

        output = self.graph.invoke(
            {"start_input": start_input},
            context={
                "planner": planner,
                "authority_snapshot_supplier": authority_supplier,
                "authority": authority,
                "repository_reader": repository_reader,
            },
        )
        result = output["final_result"]

        authority_supplier.assert_not_called()
        authority.authorize.assert_not_called()
        repository_reader.get_exact_commit_text_file.assert_not_called()
        self.assertEqual(result.outcome_kind, "no_action")
        self.assertEqual(result.continuation_status, "SETTLED")
        self.assertEqual(result.remaining_investigations, 1)
        self.assertEqual(result.consumed_actions, ())
        self.assertIsNone(result.executed_action_id)

    def test_fresh_t2_consumption_rejects_model_proposal_and_preserves_t2_baseline(self) -> None:
        start_input = _start_input(consumed_actions=())
        planner = Mock()
        planner.plan.return_value = _action_proposal()
        authority_snapshot = _authority_snapshot(
            consumed_actions=(_ACTION_ID,),
            remaining_investigations=1,
        )
        authority_supplier = Mock(return_value=authority_snapshot)
        repository_reader = Mock()

        output = self.graph.invoke(
            {"start_input": start_input},
            context={
                "planner": planner,
                "authority_snapshot_supplier": authority_supplier,
                "authority": self.authority,
                "repository_reader": repository_reader,
            },
        )
        result = output["final_result"]

        authority_supplier.assert_called_once_with(start_input)
        repository_reader.get_exact_commit_text_file.assert_not_called()
        self.assertEqual(result.outcome_kind, "authority_rejected")
        assert result.execution_authority_outcome is not None
        self.assertEqual(result.execution_authority_outcome.reason, "action_consumed")
        self.assertEqual(result.consumed_actions, (_ACTION_ID,))
        self.assertEqual(result.remaining_investigations, 1)
        self.assertIsNone(result.executed_action_id)

    def test_authorized_semantic_result_executes_once_consumes_action_spends_budget_and_updates_domain(self) -> None:
        start_input = _start_input()
        planner = Mock()
        planner.plan.return_value = _action_proposal()
        authority_supplier = Mock(return_value=_authority_snapshot())
        repository_reader = Mock()
        repository_reader.get_exact_commit_text_file.return_value = RepositoryTextFile(
            repository=_REPOSITORY,
            path="pyproject.toml",
            revision=_REVISION,
            content='[project]\nname = "demo"\nrequires-python = ">=3.10"\n',
        )

        output = self.graph.invoke(
            {"start_input": start_input},
            context={
                "planner": planner,
                "authority_snapshot_supplier": authority_supplier,
                "authority": self.authority,
                "repository_reader": repository_reader,
            },
        )
        result = output["final_result"]

        repository_reader.get_exact_commit_text_file.assert_called_once_with(
            _REPOSITORY,
            _REVISION,
            "pyproject.toml",
        )
        self.assertEqual(result.outcome_kind, "semantic_result")
        self.assertEqual(result.executed_action_id, _ACTION_ID)
        self.assertEqual(result.remaining_investigations, 0)
        self.assertEqual(result.consumed_actions, (_ACTION_ID,))
        self.assertIsNotNone(result.python_support_assessment.target_relevance)
        assert result.python_support_assessment.target_relevance is not None
        self.assertEqual(
            result.python_support_assessment.target_relevance.state,
            "outside_declared_python_range",
        )
        self.assertEqual(
            result.python_support_assessment.applicability.state,
            "established_not_applicable",
        )

    def test_expected_repository_failure_spends_budget_without_consuming_action_or_changing_domain(self) -> None:
        start_input = _start_input()
        planner = Mock()
        planner.plan.return_value = _action_proposal()
        authority_snapshot = _authority_snapshot()
        authority_supplier = Mock(return_value=authority_snapshot)
        repository_reader = Mock()
        repository_reader.get_exact_commit_text_file.side_effect = GitHubAcquisitionError(
            "GitHub repository-file acquisition timed out.",
            reason="timeout",
        )

        output = self.graph.invoke(
            {"start_input": start_input},
            context={
                "planner": planner,
                "authority_snapshot_supplier": authority_supplier,
                "authority": self.authority,
                "repository_reader": repository_reader,
            },
        )
        result = output["final_result"]

        self.assertEqual(result.outcome_kind, "operational_failure")
        self.assertEqual(result.executed_action_id, _ACTION_ID)
        self.assertEqual(result.remaining_investigations, 0)
        self.assertEqual(result.consumed_actions, ())
        self.assertEqual(
            result.python_support_assessment,
            authority_snapshot.baseline.python_support_assessment,
        )
        self.assertIsInstance(
            result.investigation_outcome,
            EvidenceGapLangGraphOperationalFailure,
        )
        assert isinstance(
            result.investigation_outcome,
            EvidenceGapLangGraphOperationalFailure,
        )
        self.assertEqual(result.investigation_outcome.reason, "timeout")


def _start_input(
    *,
    consumed_actions: tuple[str, ...] = (),
    remaining_investigations: int = 1,
) -> EvidenceGapLangGraphStartInput:
    return EvidenceGapLangGraphStartInput(
        investigation=_investigation(),
        planning_question=_PLANNING_QUESTION,
        consumed_actions=consumed_actions,
        remaining_investigations=remaining_investigations,
    )


def _authority_snapshot(
    *,
    consumed_actions: tuple[str, ...] = (),
    remaining_investigations: int = 1,
) -> EvidenceGapLangGraphAuthoritySnapshot:
    assessment = _assessment()
    selection = select_python_support_drop_investigation(assessment)
    assert selection is not None
    return EvidenceGapLangGraphAuthoritySnapshot(
        baseline=EvidenceGapLangGraphBaseline(
            python_support_assessment=assessment,
            consumed_actions=consumed_actions,
            remaining_investigations=remaining_investigations,
        ),
        current_selection=selection,
    )


def _action_proposal() -> EvidenceGapLangGraphActionProposal:
    return EvidenceGapLangGraphActionProposal(
        action_id=_ACTION_ID,
        explanation="Acquire the exact target Python declaration.",
    )


def _investigation() -> PublicPullRequestInvestigation:
    pull_request = _pull_request()
    dependency = _dependency()
    assessment = evaluate_python_support_drop_impact(
        build_python_support_drop_impact_candidate(
            pull_request,
            dependency,
            _claim(),
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


def _assessment() -> PythonSupportDropImpactAssessment:
    return evaluate_python_support_drop_impact(
        build_python_support_drop_impact_candidate(
            _pull_request(),
            _dependency(),
            _claim(),
        )
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
