"""Focused tests for the product-output to EvidenceGapPlanner composition seam.

These tests use the actual UpgradePilot domain/result types that the normal product flow returns.
They do not call GitHub or LM Studio. Their responsibility is narrower: prove that already-owned
product semantics are projected into ``EvidenceGapPlannerContext`` without exposing exact source
or action authority and without inventing a first-match CI policy.
"""

from __future__ import annotations

from dataclasses import replace
import json
import unittest

from experiments.evidence_gap_product_planner_composition import (
    compose_pre_target_python_support_planner_context,
)
from experiments.evidence_gap_planner_model_boundary import render_evidence_gap_planner_request
from upgradepilot.ci.consumption import StaticDependencyConsumptionEvidence
from upgradepilot.ci.dependency_exercise import (
    DependencyCICoverageResult,
    WorkflowDependencyCoverageResult,
)
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


_PLANNING_QUESTION = (
    "What additional admitted investigation, if any, is useful for determining whether the "
    "established upstream Python-support drop intersects the target declaration?"
)
_ACTION_ID = "acquire_exact_target_python_declaration"
_HEAD_SHA = "b" * 40


class EvidenceGapRealStateCompositionTests(unittest.TestCase):
    def test_composition_reuses_product_transition_propositions_and_all_supported_ci_consumptions(
        self,
    ) -> None:
        context = compose_pre_target_python_support_planner_context(
            _investigation(),
            planning_question=_PLANNING_QUESTION,
        )

        self.assertEqual(context.dependency_transition.normalized_package, "soupsieve")
        self.assertEqual(context.dependency_transition.old_version, "2.6")
        self.assertEqual(context.dependency_transition.proposed_version, "2.8.4")
        self.assertEqual(
            tuple(item.key for item in context.propositions),
            (
                "upstream_python_support_drop_crossed",
                "exact_target_python_declaration_established",
                "declared_python_range_intersects_dropped_line",
            ),
        )

        # Preserve every supported product-owned consumption. The unresolved third record below
        # must not be promoted to supported planning evidence by the adapter.
        self.assertEqual(len(context.planning_evidence), 2)
        witnesses = []
        for evidence in context.planning_evidence:
            facts = {fact.name: fact.value for fact in evidence.facts}
            self.assertEqual(facts["consumption_state"], "supported")
            self.assertEqual(facts["mechanism"], "project_environment")
            self.assertFalse(facts["direct_exercise_established"])
            witnesses.append(facts["witness_path"])

        self.assertEqual(
            witnesses,
            [
                ("mkdocs-llmstxt", "beautifulsoup4", "soupsieve"),
                ("beautifulsoup4", "soupsieve"),
            ],
        )

        self.assertEqual(len(context.allowed_actions), 1)
        self.assertEqual(context.allowed_actions[0].action_id, _ACTION_ID)
        self.assertEqual(
            context.allowed_actions[0].target_proposition,
            "exact_target_python_declaration_established",
        )

    def test_rendered_context_keeps_exact_source_and_action_authority_hidden(self) -> None:
        request = render_evidence_gap_planner_request(
            compose_pre_target_python_support_planner_context(
                _investigation(),
                planning_question=_PLANNING_QUESTION,
            )
        )
        rendered = json.dumps(request, sort_keys=True)

        for hidden_value in (
            "pydantic/pydantic",
            _HEAD_SHA,
            "pyproject.toml",
            ".github/workflows/docs.yml",
            "uv sync --all-packages --group docs",
            "uv.lock",
        ):
            self.assertNotIn(hidden_value, rendered)

        self.assertIn("mkdocs-llmstxt", rendered)
        self.assertIn("beautifulsoup4", rendered)
        self.assertIn("soupsieve", rendered)

    def test_consumed_or_budget_blocked_action_is_not_offered_pre_call(self) -> None:
        consumed = compose_pre_target_python_support_planner_context(
            _investigation(),
            planning_question=_PLANNING_QUESTION,
            consumed_actions=(_ACTION_ID,),
        )
        exhausted = compose_pre_target_python_support_planner_context(
            _investigation(),
            planning_question=_PLANNING_QUESTION,
            remaining_investigations=0,
        )

        self.assertEqual(consumed.allowed_actions, ())
        self.assertEqual(exhausted.allowed_actions, ())
        self.assertEqual(consumed.consumed_actions, (_ACTION_ID,))
        self.assertEqual(exhausted.planning_budget.remaining_investigations, 0)

    def test_composition_rejects_selector_that_no_longer_matches_bound_action_contract(self) -> None:
        investigation = _investigation()
        selection = investigation.python_support_drop_investigation_selection
        assert selection is not None
        mismatched = replace(selection, path="requirements.txt")

        with self.assertRaisesRegex(ValueError, "no longer matches"):
            compose_pre_target_python_support_planner_context(
                replace(
                    investigation,
                    python_support_drop_investigation_selection=mismatched,
                ),
                planning_question=_PLANNING_QUESTION,
            )


def _investigation() -> PublicPullRequestInvestigation:
    pull_request = _pull_request()
    dependency = _dependency()
    candidate = build_python_support_drop_impact_candidate(
        pull_request,
        dependency,
        _claim(),
    )
    assessment = evaluate_python_support_drop_impact(candidate)
    selection = select_python_support_drop_investigation(assessment)
    assert selection is not None

    return PublicPullRequestInvestigation(
        pull_request=pull_request,
        changed_files=(),
        dependency_result=dependency,
        target_python_result=None,
        workflow_evidence=(),
        ci_coverage_result=_coverage(),
        package_result=None,
        upstream_repository_result=None,
        python_support_drop_pre_investigation_result=assessment,
        python_support_drop_investigation_selection=selection,
        python_support_drop_impact_result=assessment,
    )


def _pull_request() -> PullRequestIdentity:
    return PullRequestIdentity(
        repository="pydantic/pydantic",
        number=13432,
        title="Bump soupsieve",
        state="open",
        merged=False,
        author="dependabot[bot]",
        base_ref="main",
        base_sha="a" * 40,
        head_ref="dependabot/soupsieve",
        head_sha=_HEAD_SHA,
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


def _coverage() -> DependencyCICoverageResult:
    docs = _consumption(
        command="uv sync --all-packages --group docs",
        witness_path=("mkdocs-llmstxt", "beautifulsoup4", "soupsieve"),
        segment_index=0,
    )
    docs_upload = _consumption(
        command="uv sync --group docs-upload",
        witness_path=("beautifulsoup4", "soupsieve"),
        segment_index=1,
    )
    unresolved = StaticDependencyConsumptionEvidence(
        state="unresolved",
        mechanism="project_environment",
        normalized_package="soupsieve",
        workflow_path=".github/workflows/docs.yml",
        workflow_revision=_HEAD_SHA,
        job_key="docs",
        step_source_index=3,
        segment_index=2,
        command="uv sync --group conditional-docs",
        reason="conditional_marker_unresolved",
        detail="A conditional candidate path remains unresolved.",
        source_path="uv.lock",
        conditional_candidate_path=("conditional-root", "soupsieve"),
        unresolved_conditions=("python_version < '3.12'",),
    )

    workflow = WorkflowDependencyCoverageResult(
        workflow_name="Docs",
        workflow_path=".github/workflows/docs.yml",
        state="supported_not_correlated",
        reason="successful_exact_head_ci_with_static_dependency_consumption",
        detail="Controlled supported CI coverage result.",
        consumption_state="supported",
        consumption_reason="static_dependency_consumption_supported",
        consumption_detail="Controlled supported static consumption.",
        direct_exercise_state="not_established",
        direct_exercise_reason="direct_package_invocation_not_established",
        direct_exercise_detail="No direct package invocation was established.",
        consumptions=(docs, docs_upload, unresolved),
    )
    return DependencyCICoverageResult(
        state="supported_not_correlated",
        reason="successful_exact_head_ci_with_static_dependency_consumption",
        detail="Controlled aggregate CI coverage result.",
        workflows=(workflow,),
    )


def _consumption(
    *,
    command: str,
    witness_path: tuple[str, ...],
    segment_index: int,
) -> StaticDependencyConsumptionEvidence:
    return StaticDependencyConsumptionEvidence(
        state="supported",
        mechanism="project_environment",
        normalized_package="soupsieve",
        workflow_path=".github/workflows/docs.yml",
        workflow_revision=_HEAD_SHA,
        job_key="docs",
        step_source_index=3,
        segment_index=segment_index,
        command=command,
        reason="selected_uv_roots_reach_changed_dependency",
        detail="Controlled supported transitive consumption.",
        source_path="uv.lock",
        reachability_kind="transitive",
        witness_path=witness_path,
    )


if __name__ == "__main__":
    unittest.main()
