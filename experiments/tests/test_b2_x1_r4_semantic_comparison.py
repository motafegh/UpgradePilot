"""Controlled framework-neutral semantic comparison for R4-A and native R4-B.

The same bounded scenario is executed through each implementation and then projected onto the
common R4 semantic surface. Internal classes/topology are intentionally not compared.
"""

from __future__ import annotations

import unittest
from unittest.mock import Mock

from experiments.b2_x1_evidence_gap_admission import (
    AdmittedInvestigationAction,
    EvidenceGapAdmissionProblem,
    EvidenceGapAdmissionState,
    admit_selected_investigation_action,
    build_target_python_declaration_action,
)
from experiments.b2_x1_evidence_gap_planner import EvidenceGapDecision
from experiments.b2_x1_evidence_gap_transition import (
    EvidenceGapInvestigationState,
    run_evidence_gap_transition,
)
from experiments.b2_x1_r4_semantic_comparison import (
    project_r4a_admission_rejection,
    project_r4a_transition,
    project_r4b_result,
)
from experiments.langgraph.evidence_gap_workflow import (
    EvidenceGapLangGraphActionProposal,
    EvidenceGapLangGraphAuthoritySnapshot,
    EvidenceGapLangGraphBaseline,
    EvidenceGapLangGraphNoAction,
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
_TARGET_FILE = RepositoryTextFile(
    repository=_REPOSITORY,
    path="pyproject.toml",
    revision=_REVISION,
    content='[project]\nname = "demo"\nrequires-python = ">=3.10"\n',
)


class R4SemanticComparisonTests(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = build_evidence_gap_langgraph()
        self.r4b_authority = R4AControlAuthorityAdapter()

    def test_no_action_semantics_match(self) -> None:
        decision = EvidenceGapDecision(
            decision_kind="QUESTION_SETTLED",
            action_id=None,
            explanation="The bounded planning question is already settled.",
        )
        r4a_trace = run_evidence_gap_transition(_r4a_state(), decision)

        planner = Mock()
        planner.plan.return_value = EvidenceGapLangGraphNoAction(
            decision_kind="QUESTION_SETTLED",
            explanation=decision.explanation,
        )
        authority_supplier = Mock(side_effect=AssertionError("authority snapshot must not run"))
        authority = Mock(side_effect=AssertionError("authority evaluation must not run"))
        repository_reader = Mock()
        r4b_result = self.graph.invoke(
            {"start_input": _r4b_start_input()},
            context={
                "planner": planner,
                "authority_snapshot_supplier": authority_supplier,
                "authority": authority,
                "repository_reader": repository_reader,
            },
        )["final_result"]

        repository_reader.get_exact_commit_text_file.assert_not_called()
        self.assertEqual(project_r4a_transition(r4a_trace), project_r4b_result(r4b_result))

    def test_fresh_t2_consumed_action_rejection_semantics_match(self) -> None:
        decision = _r4a_action_decision()
        r4a_state = _r4a_state(consumed_actions=(_ACTION_ID,))
        admission = admit_selected_investigation_action(
            _r4a_admission_state(consumed_actions=(_ACTION_ID,)),
            decision,
        )
        self.assertIsInstance(admission, EvidenceGapAdmissionProblem)
        assert isinstance(admission, EvidenceGapAdmissionProblem)

        planner = Mock()
        planner.plan.return_value = _r4b_action_proposal()
        repository_reader = Mock()
        r4b_result = self.graph.invoke(
            {"start_input": _r4b_start_input(consumed_actions=())},
            context={
                "planner": planner,
                "authority_snapshot_supplier": Mock(
                    return_value=_r4b_authority_snapshot(
                        consumed_actions=(_ACTION_ID,),
                    )
                ),
                "authority": self.r4b_authority,
                "repository_reader": repository_reader,
            },
        )["final_result"]

        repository_reader.get_exact_commit_text_file.assert_not_called()
        self.assertEqual(
            project_r4a_admission_rejection(r4a_state, decision, admission),
            project_r4b_result(r4b_result),
        )

    def test_authorized_semantic_success_semantics_match(self) -> None:
        decision = _r4a_action_decision()
        admission = admit_selected_investigation_action(
            _r4a_admission_state(),
            decision,
        )
        self.assertIsInstance(admission, AdmittedInvestigationAction)
        assert isinstance(admission, AdmittedInvestigationAction)

        r4a_reader = Mock()
        r4a_reader.get_exact_commit_text_file.return_value = _TARGET_FILE
        r4a_trace = run_evidence_gap_transition(
            _r4a_state(),
            decision,
            admitted_action=admission,
            repository_client=r4a_reader,
        )

        r4b_reader = Mock()
        r4b_reader.get_exact_commit_text_file.return_value = _TARGET_FILE
        planner = Mock()
        planner.plan.return_value = _r4b_action_proposal()
        r4b_result = self.graph.invoke(
            {"start_input": _r4b_start_input()},
            context={
                "planner": planner,
                "authority_snapshot_supplier": Mock(return_value=_r4b_authority_snapshot()),
                "authority": self.r4b_authority,
                "repository_reader": r4b_reader,
            },
        )["final_result"]

        r4a_reader.get_exact_commit_text_file.assert_called_once_with(
            _REPOSITORY,
            _REVISION,
            "pyproject.toml",
        )
        r4b_reader.get_exact_commit_text_file.assert_called_once_with(
            _REPOSITORY,
            _REVISION,
            "pyproject.toml",
        )
        self.assertEqual(project_r4a_transition(r4a_trace), project_r4b_result(r4b_result))

    def test_expected_repository_failure_semantics_match(self) -> None:
        decision = _r4a_action_decision()
        admission = admit_selected_investigation_action(
            _r4a_admission_state(),
            decision,
        )
        self.assertIsInstance(admission, AdmittedInvestigationAction)
        assert isinstance(admission, AdmittedInvestigationAction)

        r4a_reader = Mock()
        r4a_reader.get_exact_commit_text_file.side_effect = GitHubAcquisitionError(
            "GitHub repository-file acquisition timed out.",
            reason="timeout",
        )
        r4a_trace = run_evidence_gap_transition(
            _r4a_state(),
            decision,
            admitted_action=admission,
            repository_client=r4a_reader,
        )

        r4b_reader = Mock()
        r4b_reader.get_exact_commit_text_file.side_effect = GitHubAcquisitionError(
            "GitHub repository-file acquisition timed out.",
            reason="timeout",
        )
        planner = Mock()
        planner.plan.return_value = _r4b_action_proposal()
        r4b_result = self.graph.invoke(
            {"start_input": _r4b_start_input()},
            context={
                "planner": planner,
                "authority_snapshot_supplier": Mock(return_value=_r4b_authority_snapshot()),
                "authority": self.r4b_authority,
                "repository_reader": r4b_reader,
            },
        )["final_result"]

        r4a_reader.get_exact_commit_text_file.assert_called_once()
        r4b_reader.get_exact_commit_text_file.assert_called_once()
        self.assertEqual(project_r4a_transition(r4a_trace), project_r4b_result(r4b_result))


def _r4a_state(
    *,
    consumed_actions: tuple[str, ...] = (),
    remaining_investigations: int = 1,
) -> EvidenceGapInvestigationState:
    return EvidenceGapInvestigationState(
        python_support_assessment=_assessment(),
        consumed_actions=consumed_actions,
        remaining_investigations=remaining_investigations,
    )


def _r4a_admission_state(
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


def _r4a_action_decision() -> EvidenceGapDecision:
    return EvidenceGapDecision(
        decision_kind="ACTION_SELECTED",
        action_id=_ACTION_ID,
        explanation="Acquire the exact target Python declaration.",
    )


def _r4b_start_input(
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


def _r4b_authority_snapshot(
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


def _r4b_action_proposal() -> EvidenceGapLangGraphActionProposal:
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
