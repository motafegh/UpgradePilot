"""Controlled semantic comparison for ordinary-Python and LangGraph evidence-gap implementations.

The same bounded scenario is executed through each implementation and then projected onto the
common semantic surface. Internal classes/topology are intentionally not compared.
"""

from __future__ import annotations

import unittest
from unittest.mock import Mock

from experiments.evidence_gap_action_admission import (
    AdmittedInvestigationAction,
    EvidenceGapAdmissionProblem,
    EvidenceGapAdmissionState,
    admit_selected_investigation_action,
    build_target_python_declaration_action,
)
from experiments.evidence_gap_planner_model_boundary import EvidenceGapDecision
from experiments.evidence_gap_investigation_transition import (
    EvidenceGapInvestigationState,
    run_evidence_gap_transition,
)
from experiments.evidence_gap_implementation_semantic_comparison import (
    project_langgraph_result,
    project_ordinary_python_admission_rejection,
    project_ordinary_python_transition,
)
from experiments.langgraph.evidence_gap_workflow import (
    EvidenceGapLangGraphActionProposal,
    EvidenceGapLangGraphAuthoritySnapshot,
    EvidenceGapLangGraphBaseline,
    EvidenceGapLangGraphNoAction,
    EvidenceGapLangGraphStartInput,
    build_evidence_gap_langgraph,
)
from experiments.langgraph.evidence_gap_ordinary_python_control_adapters import (
    OrdinaryPythonEvidenceGapAuthorityAdapter,
)
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
_TARGET_FILE = RepositoryTextFile(
    repository=_REPOSITORY,
    path="pyproject.toml",
    revision=_REVISION,
    content='[project]\nname = "demo"\nrequires-python = ">=3.10"\n',
)


class EvidenceGapImplementationSemanticComparisonTests(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = build_evidence_gap_langgraph()
        self.langgraph_authority = OrdinaryPythonEvidenceGapAuthorityAdapter()

    def test_no_action_semantics_match(self) -> None:
        decision = EvidenceGapDecision(
            decision_kind="QUESTION_SETTLED",
            action_id=None,
            explanation="The bounded planning question is already settled.",
        )
        ordinary_python_trace = run_evidence_gap_transition(
            _ordinary_python_state(),
            decision,
        )

        planner = Mock()
        planner.plan.return_value = EvidenceGapLangGraphNoAction(
            decision_kind="QUESTION_SETTLED",
            explanation=decision.explanation,
        )
        authority_supplier = Mock(side_effect=AssertionError("authority snapshot must not run"))
        authority = Mock(side_effect=AssertionError("authority evaluation must not run"))
        repository_reader = Mock()
        langgraph_result = self.graph.invoke(
            {"start_input": _langgraph_start_input()},
            context={
                "planner": planner,
                "authority_snapshot_supplier": authority_supplier,
                "authority": authority,
                "repository_reader": repository_reader,
            },
        )["final_result"]

        repository_reader.get_exact_commit_text_file.assert_not_called()
        self.assertEqual(
            project_ordinary_python_transition(ordinary_python_trace),
            project_langgraph_result(langgraph_result),
        )

    def test_fresh_t2_consumed_action_rejection_semantics_match(self) -> None:
        decision = _ordinary_python_action_decision()
        ordinary_python_state = _ordinary_python_state(consumed_actions=(_ACTION_ID,))
        admission = admit_selected_investigation_action(
            _ordinary_python_admission_state(consumed_actions=(_ACTION_ID,)),
            decision,
        )
        self.assertIsInstance(admission, EvidenceGapAdmissionProblem)
        assert isinstance(admission, EvidenceGapAdmissionProblem)

        planner = Mock()
        planner.plan.return_value = _langgraph_action_proposal()
        repository_reader = Mock()
        langgraph_result = self.graph.invoke(
            {"start_input": _langgraph_start_input(consumed_actions=())},
            context={
                "planner": planner,
                "authority_snapshot_supplier": Mock(
                    return_value=_langgraph_authority_snapshot(
                        consumed_actions=(_ACTION_ID,),
                    )
                ),
                "authority": self.langgraph_authority,
                "repository_reader": repository_reader,
            },
        )["final_result"]

        repository_reader.get_exact_commit_text_file.assert_not_called()
        self.assertEqual(
            project_ordinary_python_admission_rejection(
                ordinary_python_state,
                decision,
                admission,
            ),
            project_langgraph_result(langgraph_result),
        )

    def test_authorized_semantic_success_semantics_match(self) -> None:
        decision = _ordinary_python_action_decision()
        admission = admit_selected_investigation_action(
            _ordinary_python_admission_state(),
            decision,
        )
        self.assertIsInstance(admission, AdmittedInvestigationAction)
        assert isinstance(admission, AdmittedInvestigationAction)

        ordinary_python_reader = Mock()
        ordinary_python_reader.get_exact_commit_text_file.return_value = _TARGET_FILE
        ordinary_python_trace = run_evidence_gap_transition(
            _ordinary_python_state(),
            decision,
            admitted_action=admission,
            repository_client=ordinary_python_reader,
        )

        langgraph_reader = Mock()
        langgraph_reader.get_exact_commit_text_file.return_value = _TARGET_FILE
        planner = Mock()
        planner.plan.return_value = _langgraph_action_proposal()
        langgraph_result = self.graph.invoke(
            {"start_input": _langgraph_start_input()},
            context={
                "planner": planner,
                "authority_snapshot_supplier": Mock(
                    return_value=_langgraph_authority_snapshot()
                ),
                "authority": self.langgraph_authority,
                "repository_reader": langgraph_reader,
            },
        )["final_result"]

        ordinary_python_reader.get_exact_commit_text_file.assert_called_once_with(
            _REPOSITORY,
            _REVISION,
            "pyproject.toml",
        )
        langgraph_reader.get_exact_commit_text_file.assert_called_once_with(
            _REPOSITORY,
            _REVISION,
            "pyproject.toml",
        )
        self.assertEqual(
            project_ordinary_python_transition(ordinary_python_trace),
            project_langgraph_result(langgraph_result),
        )

    def test_expected_repository_failure_semantics_match(self) -> None:
        decision = _ordinary_python_action_decision()
        admission = admit_selected_investigation_action(
            _ordinary_python_admission_state(),
            decision,
        )
        self.assertIsInstance(admission, AdmittedInvestigationAction)
        assert isinstance(admission, AdmittedInvestigationAction)

        ordinary_python_reader = Mock()
        ordinary_python_reader.get_exact_commit_text_file.side_effect = GitHubAcquisitionError(
            "GitHub repository-file acquisition timed out.",
            reason="timeout",
        )
        ordinary_python_trace = run_evidence_gap_transition(
            _ordinary_python_state(),
            decision,
            admitted_action=admission,
            repository_client=ordinary_python_reader,
        )

        langgraph_reader = Mock()
        langgraph_reader.get_exact_commit_text_file.side_effect = GitHubAcquisitionError(
            "GitHub repository-file acquisition timed out.",
            reason="timeout",
        )
        planner = Mock()
        planner.plan.return_value = _langgraph_action_proposal()
        langgraph_result = self.graph.invoke(
            {"start_input": _langgraph_start_input()},
            context={
                "planner": planner,
                "authority_snapshot_supplier": Mock(
                    return_value=_langgraph_authority_snapshot()
                ),
                "authority": self.langgraph_authority,
                "repository_reader": langgraph_reader,
            },
        )["final_result"]

        ordinary_python_reader.get_exact_commit_text_file.assert_called_once()
        langgraph_reader.get_exact_commit_text_file.assert_called_once()
        self.assertEqual(
            project_ordinary_python_transition(ordinary_python_trace),
            project_langgraph_result(langgraph_result),
        )


def _ordinary_python_state(
    *,
    consumed_actions: tuple[str, ...] = (),
    remaining_investigations: int = 1,
) -> EvidenceGapInvestigationState:
    return EvidenceGapInvestigationState(
        python_support_assessment=_assessment(),
        consumed_actions=consumed_actions,
        remaining_investigations=remaining_investigations,
    )


def _ordinary_python_admission_state(
    *,
    consumed_actions: tuple[str, ...] = (),
    remaining_investigations: int = 1,
) -> EvidenceGapAdmissionState:
    assessment = _assessment()
    return EvidenceGapAdmissionState(
        repository=_REPOSITORY,
        revision=_REVISION,
        propositions=_assessment_propositions(assessment),
        consumed_actions=consumed_actions,
        remaining_investigations=remaining_investigations,
        actions=(build_target_python_declaration_action(_REPOSITORY, _REVISION),),
    )


def _ordinary_python_action_decision() -> EvidenceGapDecision:
    return EvidenceGapDecision(
        decision_kind="ACTION_SELECTED",
        action_id=_ACTION_ID,
        explanation="Acquire the exact target Python declaration.",
    )


def _langgraph_start_input(
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


def _langgraph_authority_snapshot(
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


def _langgraph_action_proposal() -> EvidenceGapLangGraphActionProposal:
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


def _assessment_propositions(
    assessment: PythonSupportDropImpactAssessment,
):
    return tuple(
        proposition
        for path in assessment.applicability.paths
        for proposition in path.propositions
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
