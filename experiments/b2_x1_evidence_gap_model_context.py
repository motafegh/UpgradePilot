"""Candidate model-visible context projection for the B2/X1 EvidenceGapPlanner.

This module is experiment support code, not UpgradePilot product runtime code.

R2 narrows the trusted state that the model actually needs to reason about the next evidence
gap. Historical Phase-3 request code remains intact as consumed evidence; this module expresses
the post-research candidate context contract without serializing whole product/experiment objects.

The ownership split is deliberate::

    trusted PlannerEvaluationCase
    + trusted DependencyVersionChange
    -> build_evidence_gap_model_context(...)
    -> compact model-visible context

The model may see trusted identity, transition, proposition state, bounded action history/budget,
and the reasoning-relevant subset of each admitted action. It does not receive evaluator/oracle
metadata, raw evidence channels, verbose hard-constraint strings, or deterministic action locator
fields that it neither owns nor needs to echo.

R3 separately owns the candidate structured decision/output and deterministic admission contract.
This module therefore does not freeze the historical AgentPlanResult JSON schema as part of R2.
"""

from __future__ import annotations

import json

from experiments.b2_x1_phase3b_harness import PlannerEvaluationCase
from upgradepilot.dependency.change import DependencyVersionChange


def build_evidence_gap_model_context(
    case: PlannerEvaluationCase,
    dependency_change: DependencyVersionChange,
) -> dict[str, object]:
    """Project one trusted planning turn into the exact R2 model-visible context.

    The projection is intentionally explicit. Adding a field to ``InvestigationSnapshot`` or
    ``DependencyVersionChange`` does not make that field model-visible automatically; future
    additions must earn visibility through the EvidenceGapPlanner responsibility.

    Deterministic owners remain authoritative even when one of their values is visible here.
    In particular, repository/revision identity and action metadata are context, not values the
    model is permitted to redefine or use as execution authorization.
    """

    snapshot = case.snapshot

    return {
        "planning_question": case.planning_question,
        "case_identity": {
            "repository": snapshot.repository,
            "pull_number": snapshot.pull_number,
            "revision": snapshot.revision,
        },
        "dependency_transition": {
            "package": dependency_change.package,
            "old_version": dependency_change.old_version,
            "proposed_version": dependency_change.proposed_version,
        },
        "propositions": [
            {
                "key": proposition.key,
                "state": proposition.state,
                "evidence_coverage": proposition.evidence_coverage,
                "detail": proposition.detail,
            }
            for proposition in snapshot.propositions
        ],
        "attempted_actions": [
            {
                "action_id": attempt.action_id,
                "outcome": attempt.outcome,
            }
            for attempt in snapshot.attempted_actions
        ],
        "remaining_budget": {
            "remaining_steps": snapshot.remaining_steps,
        },
        "allowed_actions": [
            {
                "action_id": action.action_id,
                "purpose": action.purpose,
                "target_proposition": action.target_proposition,
                "required_precondition": {
                    "proposition_state": action.required_proposition_state,
                    "evidence_coverage": action.required_evidence_coverage,
                },
                "cost_class": action.cost_class,
                "mutation_class": action.mutation_class,
                "result_families": list(action.result_families),
            }
            for action in snapshot.allowed_actions
        ],
    }


def render_evidence_gap_model_context_json(
    case: PlannerEvaluationCase,
    dependency_change: DependencyVersionChange,
) -> str:
    """Return stable model-context JSON for inspection, hashing, and later replay."""

    return json.dumps(
        build_evidence_gap_model_context(case, dependency_change),
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )


__all__ = (
    "build_evidence_gap_model_context",
    "render_evidence_gap_model_context_json",
)
