#!/usr/bin/env python3
"""Run one real S001 planner decision through the R4-A4 transition seam.

This is experiment support code, not UpgradePilot product runtime code.  It extends the existing
real S001 A3 path by applying exactly one already-admitted planner branch::

    normal S001 product investigation
    -> preserved pre-target Python-support assessment
    -> real-flow planner composition
    -> local A3 EvidenceGapDecision
    -> fresh A2 deterministic admission
    -> A4 exact target-file acquisition and domain update
    -> immutable transition trace
    -> deterministic replay comparison

The normal product investigation currently continues through its own target-file acquisition
before returning.  This probe deliberately starts A4 from the preserved pre-investigation
assessment and performs a new exact-file read through the experiment seam.  It therefore proves
the real S001 A4 transition boundary, not product-runtime orchestration integration.

Run from the repository root as a module.  S001 is public, so isolate ambient GitHub credentials
and proxies as documented in ``ENVIRONMENT.md``::

    env \
      -u GITHUB_TOKEN \
      -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY \
      -u http_proxy -u https_proxy -u all_proxy \
      python -m experiments.b2_x1_s001_real_flow_a4_transition
"""

from __future__ import annotations

from dataclasses import asdict
import json
from pathlib import Path
import time

from experiments.b2_x1_evidence_gap_admission import (
    AdmittedInvestigationAction,
    EvidenceGapAdmissionProblem,
    EvidenceGapAdmissionState,
    admit_selected_investigation_action,
    build_target_python_declaration_action,
)
from experiments.b2_x1_evidence_gap_composition import (
    compose_pre_target_python_support_planner_context,
)
from experiments.b2_x1_evidence_gap_model import (
    EVIDENCE_GAP_MODEL_ID,
    EvidenceGapModelInvocationProblem,
    LocalEvidenceGapPlanner,
)
from experiments.b2_x1_evidence_gap_planner import EvidenceGapDecision
from experiments.b2_x1_evidence_gap_transition import (
    EvidenceGapInvestigationState,
    replay_evidence_gap_transition,
    run_evidence_gap_transition,
)
from upgradepilot.github.repository import GitHubRepositoryClient
from upgradepilot.impact.python_support import (
    PythonSupportDropImpactAssessment,
    PythonSupportDropInvestigationSelection,
)
from upgradepilot.investigation import investigate_public_pull_request


_REPOSITORY = "pydantic/pydantic"
_PR_NUMBER = 13432
_OUTPUT_PATH = Path("/tmp/upgradepilot-b2-x1-r4-s001-real-flow-a4-transition.json")
_EXPECTED_ACTION_ID = "acquire_exact_target_python_declaration"
_PLANNING_QUESTION = (
    "What additional admitted investigation, if any, is useful for determining whether the "
    "established upstream Python-support drop intersects the target declaration?"
)


def run_probe() -> dict[str, object]:
    """Execute and preserve one real S001 A3 -> A2 -> A4 transition."""

    investigation = investigate_public_pull_request(
        _REPOSITORY,
        _PR_NUMBER,
        token=None,
    )
    context = compose_pre_target_python_support_planner_context(
        investigation,
        planning_question=_PLANNING_QUESTION,
    )

    pre_target_assessment = investigation.python_support_drop_pre_investigation_result
    if not isinstance(pre_target_assessment, PythonSupportDropImpactAssessment):
        raise RuntimeError("Real S001 state lost the pre-target Python-support assessment.")

    before_state = EvidenceGapInvestigationState(
        python_support_assessment=pre_target_assessment,
        consumed_actions=context.consumed_actions,
        remaining_investigations=context.planning_budget.remaining_investigations,
    )

    started = time.perf_counter()
    decision = LocalEvidenceGapPlanner().decide(context)
    planner_elapsed_seconds = time.perf_counter() - started

    common: dict[str, object] = {
        "kind": "b2_x1_r4_s001_real_flow_a4_transition",
        "model": EVIDENCE_GAP_MODEL_ID,
        "case": {
            "repository": investigation.pull_request.repository,
            "pull_number": investigation.pull_request.number,
            "head_revision": investigation.pull_request.head_sha,
        },
        "planner_elapsed_seconds": planner_elapsed_seconds,
        "normal_product_path_used": True,
        "product_path_target_result_before_a4_probe": (
            type(investigation.target_python_result).__name__
            if investigation.target_python_result is not None
            else None
        ),
        "a4_started_from_preserved_pre_target_assessment": True,
    }

    if isinstance(decision, EvidenceGapModelInvocationProblem):
        return {
            **common,
            "outcome": "invocation_problem",
            "decision": None,
            "invocation_problem": asdict(decision),
            "admission": None,
            "capability_executed": False,
            "transition_trace": None,
            "replay_equivalent": False,
            "basic_expectation_match": False,
        }
    if not isinstance(decision, EvidenceGapDecision):
        raise TypeError(f"Unsupported planner result type: {type(decision)!r}")

    if decision.decision_kind != "ACTION_SELECTED":
        trace = run_evidence_gap_transition(before_state, decision)
        replayed_after_state = replay_evidence_gap_transition(trace)
        return {
            **common,
            "outcome": "no_action_transition",
            "decision": asdict(decision),
            "invocation_problem": None,
            "admission": None,
            "capability_executed": False,
            "transition_trace": asdict(trace),
            "replayed_after_state": asdict(replayed_after_state),
            "replay_equivalent": replayed_after_state == trace.after_state,
            "basic_expectation_match": False,
        }

    selection = investigation.python_support_drop_investigation_selection
    if not isinstance(selection, PythonSupportDropInvestigationSelection):
        raise RuntimeError(
            "Real S001 state lost the expected deterministic Python-support selection."
        )
    action = build_target_python_declaration_action(
        selection.repository,
        selection.revision,
    )
    admission = admit_selected_investigation_action(
        EvidenceGapAdmissionState(
            repository=investigation.pull_request.repository,
            revision=investigation.pull_request.head_sha,
            propositions=context.propositions,
            consumed_actions=context.consumed_actions,
            remaining_investigations=context.planning_budget.remaining_investigations,
            actions=(action,),
        ),
        decision,
    )
    if isinstance(admission, EvidenceGapAdmissionProblem):
        return {
            **common,
            "outcome": "admission_problem",
            "decision": asdict(decision),
            "invocation_problem": None,
            "admission": asdict(admission),
            "capability_executed": False,
            "transition_trace": None,
            "replay_equivalent": False,
            "basic_expectation_match": False,
        }
    if not isinstance(admission, AdmittedInvestigationAction):
        raise TypeError(f"Unsupported admission result type: {type(admission)!r}")

    trace = run_evidence_gap_transition(
        before_state,
        decision,
        admitted_action=admission,
        repository_client=GitHubRepositoryClient(token=None),
    )
    replayed_after_state = replay_evidence_gap_transition(trace)
    replay_equivalent = replayed_after_state == trace.after_state
    semantic_execution_succeeded = trace.execution_result is not None

    return {
        **common,
        "outcome": (
            "semantic_result" if semantic_execution_succeeded else "operational_failure"
        ),
        "decision": asdict(decision),
        "invocation_problem": None,
        "admission": {
            "kind": "admitted_action",
            "action_id": admission.action.action_id,
            "explanation": admission.explanation,
        },
        "capability_executed": True,
        "transition_trace": asdict(trace),
        "replayed_after_state": asdict(replayed_after_state),
        "replay_equivalent": replay_equivalent,
        "basic_expectation_match": (
            decision.action_id == _EXPECTED_ACTION_ID
            and semantic_execution_succeeded
            and replay_equivalent
        ),
    }


def main() -> int:
    """Persist the exact trace and print a compact interpretation of the live result."""

    output = run_probe()
    _OUTPUT_PATH.write_text(
        # The in-memory trace deliberately retains typed packaging.Version and datetime
        # evidence.  The diagnostic JSON renders those established value objects as text;
        # replay equivalence is checked against the typed in-memory states before this step.
        json.dumps(output, indent=2, sort_keys=True, default=str),
        encoding="utf-8",
    )

    print(f"case: {_REPOSITORY}#{_PR_NUMBER}")
    print(f"model: {EVIDENCE_GAP_MODEL_ID}")
    print(f"outcome: {output['outcome']}")
    print(f"planner_elapsed_seconds: {output['planner_elapsed_seconds']:.3f}")

    decision = output["decision"]
    if isinstance(decision, dict):
        print(f"decision_kind: {decision['decision_kind']}")
        print(f"action_id: {decision['action_id']}")

    admission = output["admission"]
    if isinstance(admission, dict):
        print(f"admission_kind: {admission.get('kind', 'admission_problem')}")
        print(f"admission_action_id: {admission.get('action_id')}")

    print(f"capability_executed: {output['capability_executed']}")
    print(f"replay_equivalent: {output['replay_equivalent']}")
    print(f"basic_expectation_match: {output['basic_expectation_match']}")

    trace = output["transition_trace"]
    if isinstance(trace, dict):
        before_state = trace["before_state"]
        after_state = trace["after_state"]
        assert isinstance(before_state, dict)
        assert isinstance(after_state, dict)
        execution_result = trace["execution_result"]
        operational_failure = trace["operational_failure"]
        print(
            "execution_result_state: "
            f"{execution_result.get('state') if isinstance(execution_result, dict) else None}"
        )
        print(
            "operational_failure_type: "
            f"{operational_failure.get('exception_type') if isinstance(operational_failure, dict) else None}"
        )
        print(
            "remaining_investigations: "
            f"{before_state['remaining_investigations']} -> "
            f"{after_state['remaining_investigations']}"
        )
        print(
            "consumed_actions: "
            f"{before_state['consumed_actions']} -> {after_state['consumed_actions']}"
        )
        print(
            "applicability_state: "
            f"{before_state['python_support_assessment']['applicability']['state']} -> "
            f"{after_state['python_support_assessment']['applicability']['state']}"
        )

    print(f"output: {_OUTPUT_PATH}")
    return 0 if output["basic_expectation_match"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
