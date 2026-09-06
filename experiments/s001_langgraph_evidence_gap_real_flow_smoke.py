#!/usr/bin/env python3
"""Run the real public S001 evidence-gap responsibility through the LangGraph experiment.

This is experiment/evaluation support, not UpgradePilot product-runtime integration.

The smoke deliberately reuses the normal product-owned S001 investigation result and starts the
LangGraph turn from its preserved pre-target Python-support assessment::

    normal public S001 product investigation
    -> real PublicPullRequestInvestigation
    -> LangGraph start input
    -> real local EvidenceGapPlanner model invocation
    -> deterministic current authority snapshot + admission control
    -> exact authorized GitHub pyproject.toml read
    -> target-Python interpretation
    -> deterministic LangGraph conclusion
    -> compare graph semantic result with the normal product path at the same immutable head

The normal product investigation already performs its own target-file read before returning. The
LangGraph smoke intentionally performs a second exact read through the experiment effect boundary,
using the preserved pre-target assessment as the graph baseline. This proves the real LangGraph
orchestration seam without changing product runtime.

Run from the repository root in the normal WSL virtual environment. S001 is public, so isolate
ambient GitHub credentials and GitHub proxy variables for this one process as required by
``ENVIRONMENT.md`` / ``SECURITY.md``::

    env \
      -u GITHUB_TOKEN \
      -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY \
      -u http_proxy -u https_proxy -u all_proxy \
      python -m experiments.s001_langgraph_evidence_gap_real_flow_smoke
"""

from __future__ import annotations

from dataclasses import asdict
import json
from pathlib import Path
import time

from experiments.langgraph.evidence_gap_ordinary_python_control_adapters import (
    OrdinaryPythonEvidenceGapAuthorityAdapter,
    OrdinaryPythonEvidenceGapPlannerAdapter,
)
from experiments.langgraph.evidence_gap_workflow import (
    EvidenceGapLangGraphActionProposal,
    EvidenceGapLangGraphAuthorityRejection,
    EvidenceGapLangGraphAuthoritySnapshot,
    EvidenceGapLangGraphAuthorizedAction,
    EvidenceGapLangGraphBaseline,
    EvidenceGapLangGraphOperationalFailure,
    EvidenceGapLangGraphResult,
    EvidenceGapLangGraphStartInput,
    build_evidence_gap_langgraph,
)
from experiments.local_evidence_gap_planner import (
    EVIDENCE_GAP_MODEL_ID,
    LocalEvidenceGapPlanner,
)
from upgradepilot.github.repository import GitHubRepositoryClient
from upgradepilot.impact.python_support import (
    PythonSupportDropImpactAssessment,
    PythonSupportDropInvestigationSelection,
)
from upgradepilot.investigation import (
    PublicPullRequestInvestigation,
    investigate_public_pull_request,
)
from upgradepilot.target.python import TargetPythonDeclaration


_REPOSITORY = "pydantic/pydantic"
_PR_NUMBER = 13432
_EXPECTED_ACTION_ID = "acquire_exact_target_python_declaration"
_EXPECTED_NODE_PATH = ("plan", "authorize", "investigate", "conclude")
_PLANNING_QUESTION = (
    "What additional admitted investigation, if any, is useful for determining whether the "
    "established upstream Python-support drop intersects the target declaration?"
)
_OUTPUT_PATH = Path("/tmp/upgradepilot-s001-langgraph-evidence-gap-real-flow-smoke.json")


def run_smoke() -> dict[str, object]:
    """Execute one real S001 LangGraph turn and return bounded diagnostic evidence."""

    investigation = investigate_public_pull_request(
        _REPOSITORY,
        _PR_NUMBER,
        token=None,
    )
    _require_real_s001_pre_target_state(investigation)

    start_input = EvidenceGapLangGraphStartInput(
        investigation=investigation,
        planning_question=_PLANNING_QUESTION,
    )
    graph = build_evidence_gap_langgraph()
    runtime_context = {
        "planner": OrdinaryPythonEvidenceGapPlannerAdapter(LocalEvidenceGapPlanner()),
        "authority_snapshot_supplier": _current_authority_snapshot,
        "authority": OrdinaryPythonEvidenceGapAuthorityAdapter(),
        "repository_reader": GitHubRepositoryClient(token=None),
    }

    observed_nodes: list[str] = []
    final_result: EvidenceGapLangGraphResult | None = None
    started = time.perf_counter()
    for update in graph.stream(
        {"start_input": start_input},
        context=runtime_context,
        stream_mode="updates",
    ):
        if not isinstance(update, dict):
            raise TypeError(
                "LangGraph updates stream returned an unsupported event shape."
            )
        for node_name, node_update in update.items():
            observed_nodes.append(node_name)
            if node_name == "conclude" and isinstance(node_update, dict):
                candidate = node_update.get("final_result")
                if isinstance(candidate, EvidenceGapLangGraphResult):
                    final_result = candidate
    graph_elapsed_seconds = time.perf_counter() - started

    if final_result is None:
        raise RuntimeError(
            "LangGraph stream completed without exposing the final result from conclude."
        )

    planner = final_result.planner_outcome
    authority = final_result.execution_authority_outcome
    investigation_outcome = final_result.investigation_outcome

    product_target_result_match = (
        investigation_outcome == investigation.target_python_result
    )
    product_final_assessment_match = (
        final_result.python_support_assessment
        == investigation.python_support_drop_impact_result
    )
    expected_node_path_match = tuple(observed_nodes) == _EXPECTED_NODE_PATH

    semantic_success = (
        final_result.outcome_kind == "semantic_result"
        and isinstance(planner, EvidenceGapLangGraphActionProposal)
        and planner.action_id == _EXPECTED_ACTION_ID
        and isinstance(authority, EvidenceGapLangGraphAuthorizedAction)
        and authority.action_id == _EXPECTED_ACTION_ID
        and isinstance(investigation_outcome, TargetPythonDeclaration)
        and final_result.executed_action_id == _EXPECTED_ACTION_ID
        and final_result.remaining_investigations == 0
        and final_result.consumed_actions == (_EXPECTED_ACTION_ID,)
    )

    basic_expectation_match = (
        semantic_success
        and expected_node_path_match
        and product_target_result_match
        and product_final_assessment_match
    )

    return {
        "kind": "s001_langgraph_evidence_gap_real_flow_smoke",
        "model": EVIDENCE_GAP_MODEL_ID,
        "case": {
            "repository": investigation.pull_request.repository,
            "pull_number": investigation.pull_request.number,
            "head_revision": investigation.pull_request.head_sha,
        },
        "workflow_input": {
            "planning_question": start_input.planning_question,
            "consumed_actions": start_input.consumed_actions,
            "remaining_investigations": start_input.remaining_investigations,
            "continuation_status": start_input.continuation_status,
            "pre_target_assessment_state": (
                investigation.python_support_drop_pre_investigation_result.applicability.state
            ),
        },
        "normal_product_path_used": True,
        "product_path_target_result_before_graph": (
            asdict(investigation.target_python_result)
            if investigation.target_python_result is not None
            else None
        ),
        "graph_started_from_preserved_pre_target_assessment": True,
        "graph_elapsed_seconds": graph_elapsed_seconds,
        "observed_node_path": observed_nodes,
        "expected_node_path_match": expected_node_path_match,
        "planner_outcome": asdict(planner),
        "authority_outcome": asdict(authority) if authority is not None else None,
        "investigation_outcome": (
            asdict(investigation_outcome)
            if investigation_outcome is not None
            else None
        ),
        "final": {
            "outcome_kind": final_result.outcome_kind,
            "executed_action_id": final_result.executed_action_id,
            "remaining_investigations": final_result.remaining_investigations,
            "consumed_actions": final_result.consumed_actions,
            "continuation_status": final_result.continuation_status,
            "target_relevance_state": (
                final_result.python_support_assessment.target_relevance.state
                if final_result.python_support_assessment.target_relevance is not None
                else None
            ),
            "applicability_state": final_result.python_support_assessment.applicability.state,
        },
        "product_target_result_match": product_target_result_match,
        "product_final_assessment_match": product_final_assessment_match,
        "basic_expectation_match": basic_expectation_match,
    }


def _current_authority_snapshot(
    start_input: EvidenceGapLangGraphStartInput,
) -> EvidenceGapLangGraphAuthoritySnapshot:
    """Re-derive the T2 graph snapshot from the current real investigation object.

    The current experiment has no independent durable/concurrent orchestration store. The supplier
    is nevertheless invoked only after the planner outcome, so authority uses the current product
    selection and the current orchestration budget/history rather than trusting model output as
    execution authority. A future concurrent state owner would belong behind this supplier rather
    than in the model contract.
    """

    investigation = start_input.investigation
    assessment = investigation.python_support_drop_pre_investigation_result
    selection = investigation.python_support_drop_investigation_selection
    if not isinstance(assessment, PythonSupportDropImpactAssessment):
        raise RuntimeError(
            "Real S001 lost the required pre-target Python-support assessment at T2."
        )
    if not isinstance(selection, PythonSupportDropInvestigationSelection):
        raise RuntimeError(
            "Real S001 lost the deterministic target-Python investigation selection at T2."
        )
    if (
        selection.repository != investigation.pull_request.repository
        or selection.revision != investigation.pull_request.head_sha
    ):
        raise RuntimeError(
            "Real S001 target-Python selection no longer matches the current pull-request identity."
        )

    return EvidenceGapLangGraphAuthoritySnapshot(
        baseline=EvidenceGapLangGraphBaseline(
            python_support_assessment=assessment,
            consumed_actions=start_input.consumed_actions,
            remaining_investigations=start_input.remaining_investigations,
            continuation_status=start_input.continuation_status,
        ),
        current_selection=selection,
    )


def _require_real_s001_pre_target_state(
    investigation: PublicPullRequestInvestigation,
) -> None:
    if not isinstance(
        investigation.python_support_drop_pre_investigation_result,
        PythonSupportDropImpactAssessment,
    ):
        raise RuntimeError(
            "Real S001 product flow did not establish the pre-target Python-support assessment."
        )
    if not isinstance(
        investigation.python_support_drop_investigation_selection,
        PythonSupportDropInvestigationSelection,
    ):
        raise RuntimeError(
            "Real S001 product flow did not establish the target-Python investigation selection."
        )
    if investigation.target_python_result is None:
        raise RuntimeError(
            "Real S001 normal product path did not establish target-Python evidence for comparison."
        )
    if investigation.python_support_drop_impact_result is None:
        raise RuntimeError(
            "Real S001 normal product path did not establish the final impact assessment for comparison."
        )


def main() -> int:
    output = run_smoke()
    _OUTPUT_PATH.write_text(
        json.dumps(output, indent=2, sort_keys=True, default=str),
        encoding="utf-8",
    )

    print(f"case: {_REPOSITORY}#{_PR_NUMBER}")
    print(f"model: {EVIDENCE_GAP_MODEL_ID}")
    print(f"outcome: {output['final']['outcome_kind']}")
    print(f"graph_elapsed_seconds: {output['graph_elapsed_seconds']:.3f}")
    print(f"observed_node_path: {output['observed_node_path']}")

    planner = output["planner_outcome"]
    if isinstance(planner, dict):
        print(f"planner_outcome_type: {type(planner).__name__}")
        print(f"planner_action_id: {planner.get('action_id')}")

    authority = output["authority_outcome"]
    if isinstance(authority, dict):
        if "reason" in authority:
            print(f"authority_status: rejected:{authority['reason']}")
        else:
            print("authority_status: authorized")
            print(f"authority_action_id: {authority.get('action_id')}")
            print(f"authority_repository: {authority.get('repository')}")
            print(f"authority_revision: {authority.get('revision')}")
            print(f"authority_path: {authority.get('path')}")

    investigation_outcome = output["investigation_outcome"]
    if isinstance(investigation_outcome, dict):
        print(f"investigation_state: {investigation_outcome.get('state')}")
        print(f"requires_python: {investigation_outcome.get('requires_python')}")

    final = output["final"]
    assert isinstance(final, dict)
    print(f"target_relevance_state: {final['target_relevance_state']}")
    print(f"applicability_state: {final['applicability_state']}")
    print(f"remaining_investigations: {final['remaining_investigations']}")
    print(f"consumed_actions: {final['consumed_actions']}")
    print(f"product_target_result_match: {output['product_target_result_match']}")
    print(f"product_final_assessment_match: {output['product_final_assessment_match']}")
    print(f"expected_node_path_match: {output['expected_node_path_match']}")
    print(f"basic_expectation_match: {output['basic_expectation_match']}")
    print(f"output: {_OUTPUT_PATH}")

    return 0 if output["basic_expectation_match"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
