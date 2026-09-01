"""Compose real UpgradePilot product outputs into the bounded B2/X1 planner context.

This module is experiment support code, not UpgradePilot product runtime code.

The current R4 live path must stop hand-reconstructing S001 planner facts.  This seam therefore
accepts the normal ``PublicPullRequestInvestigation`` result for the existing pre-target Python-
support-drop responsibility and only projects semantics that are already owned elsewhere::

    PublicPullRequestInvestigation
    -> product-owned dependency transition
    -> product-owned PropositionAssessment state
    -> selected product-owned CI consumption evidence
    -> current deterministic investigation selection
    -> EvidenceGapPlannerContext

It does not parse lockfiles/workflows, normalize package identity, derive reachability, establish
CI consumption, establish proposition truth, or define exact action authority.  Exact source and
action identity remains hidden from the model and is recovered later through deterministic
admission.
"""

from __future__ import annotations

from experiments.b2_x1_evidence_gap_admission import (
    build_target_python_declaration_action,
    project_action_descriptor,
)
from experiments.b2_x1_evidence_gap_planner import (
    EvidenceGapPlannerContext,
    EvidenceGapPlanningBudget,
    EvidenceGapDependencyTransition,
    PlanningEvidence,
    PlanningEvidenceFact,
)
from upgradepilot.ci.dependency_exercise import DependencyCICoverageResult
from upgradepilot.dependency.change import DependencyVersionChange
from upgradepilot.impact.python_support import (
    PythonSupportDropImpactAssessment,
    PythonSupportDropInvestigationSelection,
)
from upgradepilot.investigation import PublicPullRequestInvestigation


_CI_PLANNING_EVIDENCE_KIND = "ci_dependency_consumption"


def compose_pre_target_python_support_planner_context(
    investigation: PublicPullRequestInvestigation,
    *,
    planning_question: str,
    consumed_actions: tuple[str, ...] = (),
    remaining_investigations: int = 1,
) -> EvidenceGapPlannerContext:
    """Project one real pre-target Python-support investigation into the A1 context.

    ``planning_question``, consumed history, and budget remain orchestration inputs rather than
    product evidence.  The dependency transition, proposition state, CI evidence, and current
    investigation selection are reused from their existing product owners.
    """

    dependency = investigation.dependency_result
    if not isinstance(dependency, DependencyVersionChange):
        raise ValueError(
            "planner composition requires an established DependencyVersionChange."
        )

    assessment = investigation.python_support_drop_pre_investigation_result
    if not isinstance(assessment, PythonSupportDropImpactAssessment):
        raise ValueError(
            "planner composition requires the product pre-target Python-support assessment."
        )
    if assessment.target_relevance is not None:
        raise ValueError(
            "pre-target planner composition requires an assessment before target relevance."
        )
    if assessment.candidate.dependency != dependency:
        raise ValueError(
            "planner composition dependency must match the product impact candidate."
        )

    selection = investigation.python_support_drop_investigation_selection
    if not isinstance(selection, PythonSupportDropInvestigationSelection):
        raise ValueError(
            "planner composition requires the current product Python-support investigation selection."
        )

    propositions = tuple(
        proposition
        for path in assessment.applicability.paths
        for proposition in path.propositions
    )

    action = _bound_action_for_selection(selection)
    offer_action = (
        remaining_investigations > 0
        and action.action_id not in consumed_actions
    )

    return EvidenceGapPlannerContext(
        planning_question=planning_question,
        dependency_transition=EvidenceGapDependencyTransition(
            normalized_package=dependency.normalized_package,
            old_version=dependency.old_version,
            proposed_version=dependency.proposed_version,
        ),
        propositions=propositions,
        planning_evidence=_project_supported_ci_consumption_evidence(
            investigation.ci_coverage_result
        ),
        consumed_actions=consumed_actions,
        planning_budget=EvidenceGapPlanningBudget(
            remaining_investigations=remaining_investigations
        ),
        allowed_actions=(project_action_descriptor(action),) if offer_action else (),
    )


def _bound_action_for_selection(
    selection: PythonSupportDropInvestigationSelection,
):
    """Rebind the product selector output to the existing exact A2 action definition."""

    action = build_target_python_declaration_action(
        selection.repository,
        selection.revision,
    )
    if (
        selection.kind != action.action_id
        or selection.path != action.path
        or selection.proposition_key != action.target_proposition
    ):
        raise ValueError(
            "product investigation selection no longer matches the bound target-Python action contract."
        )
    return action


def _project_supported_ci_consumption_evidence(
    coverage: DependencyCICoverageResult | None,
) -> tuple[PlanningEvidence, ...]:
    """Project every supported product-owned CI consumption without re-interpreting it.

    The current real S001 verifier intentionally preserves every supported consumption rather
    than choosing an arbitrary first match.  This projection follows the same evidence rule.
    Exact workflow/source paths, commands, revisions, and raw source remain model-hidden.
    """

    if coverage is None:
        return ()

    projected: list[PlanningEvidence] = []
    for workflow in coverage.workflows:
        for consumption in workflow.consumptions:
            if consumption.state != "supported":
                continue

            facts: list[PlanningEvidenceFact] = [
                PlanningEvidenceFact(
                    name="consumption_state",
                    value=consumption.state,
                ),
                PlanningEvidenceFact(
                    name="mechanism",
                    value=consumption.mechanism,
                ),
            ]
            if consumption.reachability_kind is not None:
                facts.append(
                    PlanningEvidenceFact(
                        name="reachability_kind",
                        value=consumption.reachability_kind,
                    )
                )
            if consumption.witness_path:
                facts.append(
                    PlanningEvidenceFact(
                        name="witness_path",
                        value=consumption.witness_path,
                    )
                )
            facts.append(
                PlanningEvidenceFact(
                    name="direct_exercise_established",
                    value=workflow.direct_exercise_state == "supported",
                )
            )

            projected.append(
                PlanningEvidence(
                    evidence_kind=_CI_PLANNING_EVIDENCE_KIND,
                    summary=(
                        "Product-owned exact-head CI evidence establishes one supported static "
                        "changed-dependency consumption. Static consumption does not by itself "
                        "establish runtime execution, runtime dependency use, or compatibility."
                    ),
                    facts=tuple(facts),
                )
            )

    return tuple(projected)


__all__ = ("compose_pre_target_python_support_planner_context",)
