#!/usr/bin/env python3
"""Prove the R4 planner composition seam against the normal real S001 product path.

This probe performs the existing public S001 investigation, composes the returned typed product
state into ``EvidenceGapPlannerContext``, renders the A1 request, and stops before the new A3
planner invocation.

The normal product investigation already uses UpgradePilot's adopted bounded local semantic
extractor for upstream support-drop evidence. Therefore this probe may use LM Studio through
that existing product responsibility. It does *not* call ``LocalEvidenceGapPlanner`` and does
not obtain or execute a new EvidenceGapPlanner decision.

Run from the repository root as a module so the repository root remains the Python import root::

    python -m experiments.b2_x1_s001_real_flow_composition_probe

Do not invoke this file as ``python experiments/b2_x1_s001_real_flow_composition_probe.py``;
that makes ``experiments/`` the script import root and breaks this module's ``experiments.*``
imports. S001 is public, so the proof should not inherit an ambient GitHub token or proxy merely
by accident; use the process-local isolation command recorded in ``ENVIRONMENT.md`` when needed.
"""

from __future__ import annotations

import json
from pathlib import Path

from experiments.b2_x1_evidence_gap_composition import (
    compose_pre_target_python_support_planner_context,
)
from experiments.b2_x1_evidence_gap_planner import render_evidence_gap_planner_request
from upgradepilot.investigation import investigate_public_pull_request


_REPOSITORY = "pydantic/pydantic"
_PR_NUMBER = 13432
_OUTPUT_PATH = Path("/tmp/upgradepilot-b2-x1-r4-s001-real-flow-composition.json")
_EXPECTED_TRANSITION = ("soupsieve", "2.6", "2.8.4")
_EXPECTED_PROPOSITIONS = (
    "upstream_python_support_drop_crossed",
    "exact_target_python_declaration_established",
    "declared_python_range_intersects_dropped_line",
)
_EXPECTED_WITNESS = ("mkdocs-llmstxt", "beautifulsoup4", "soupsieve")
_EXPECTED_ACTION_ID = "acquire_exact_target_python_declaration"
_PLANNING_QUESTION = (
    "What additional admitted investigation, if any, is useful for determining whether the "
    "established upstream Python-support drop intersects the target declaration?"
)


def run_probe() -> dict[str, object]:
    """Run normal S001 product acquisition and prove the bounded composition result."""

    investigation = investigate_public_pull_request(
        _REPOSITORY,
        _PR_NUMBER,
        token=None,
    )
    context = compose_pre_target_python_support_planner_context(
        investigation,
        planning_question=_PLANNING_QUESTION,
    )
    request = render_evidence_gap_planner_request(context)

    transition = (
        context.dependency_transition.normalized_package,
        context.dependency_transition.old_version,
        context.dependency_transition.proposed_version,
    )
    if transition != _EXPECTED_TRANSITION:
        raise AssertionError(
            f"real S001 transition differed: expected {_EXPECTED_TRANSITION!r}, got {transition!r}"
        )

    proposition_keys = tuple(item.key for item in context.propositions)
    if proposition_keys != _EXPECTED_PROPOSITIONS:
        raise AssertionError(
            "real S001 product propositions differed from the current pre-target contract: "
            f"{proposition_keys!r}"
        )

    witness_paths = tuple(
        fact.value
        for evidence in context.planning_evidence
        for fact in evidence.facts
        if fact.name == "witness_path"
    )
    if _EXPECTED_WITNESS not in witness_paths:
        raise AssertionError(
            "real S001 planner evidence did not preserve the expected product-owned CI witness."
        )

    action_ids = tuple(item.action_id for item in context.allowed_actions)
    if action_ids != (_EXPECTED_ACTION_ID,):
        raise AssertionError(
            f"real S001 allowed action projection differed: {action_ids!r}"
        )

    serialized_request = json.dumps(request, sort_keys=True)
    hidden_values = (
        investigation.pull_request.repository,
        investigation.pull_request.head_sha,
        "pyproject.toml",
        "uv.lock",
        "uv sync",
    )
    leaked = tuple(value for value in hidden_values if value in serialized_request)
    if leaked:
        raise AssertionError(
            f"real S001 A1 request exposed hidden source/action authority: {leaked!r}"
        )

    return {
        "kind": "b2_x1_r4_s001_real_flow_composition_probe",
        "case": {
            "repository": investigation.pull_request.repository,
            "pull_number": investigation.pull_request.number,
            "head_revision": investigation.pull_request.head_sha,
        },
        "product_transition": {
            "normalized_package": transition[0],
            "old_version": transition[1],
            "proposed_version": transition[2],
        },
        "product_proposition_keys": list(proposition_keys),
        "projected_ci_witness_paths": [
            list(item) for item in witness_paths if isinstance(item, tuple)
        ],
        "projected_action_ids": list(action_ids),
        "planner_request": request,
        "findings": {
            "normal_product_path_used": True,
            "product_semantic_extractor_may_use_existing_local_model": True,
            "new_a3_planner_invoked": False,
            "expected_s001_transition_preserved": True,
            "expected_product_propositions_preserved": True,
            "expected_ci_witness_preserved": True,
            "hidden_source_action_authority_absent_from_request": True,
        },
    }


def main() -> int:
    output = run_probe()
    _OUTPUT_PATH.write_text(
        json.dumps(output, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    print(f"case: {_REPOSITORY}#{_PR_NUMBER}")
    print("normal_product_path_used: True")
    print("new_a3_planner_invoked: False")
    print("expected_s001_transition_preserved: True")
    print("expected_product_propositions_preserved: True")
    print("expected_ci_witness_preserved: True")
    print("hidden_source_action_authority_absent_from_request: True")
    print(f"output: {_OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
