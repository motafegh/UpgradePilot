#!/usr/bin/env python3
"""Run the current R4-A3 planner against real S001 product-derived context.

This is experiment support code, not UpgradePilot product runtime code.

The smoke uses the normal public S001 investigation path, the current real-flow composition seam,
and the current ``LocalEvidenceGapPlanner`` implementation::

    pydantic/pydantic#13432
    -> investigate_public_pull_request(...)
    -> compose_pre_target_python_support_planner_context(...)
    -> LocalEvidenceGapPlanner.decide(...)
    -> untrusted EvidenceGapDecision OR typed invocation problem
    -> optional A2 deterministic admission for ACTION_SELECTED
    -> no capability execution

The purpose is to observe one real local-model planner decision after the A1/A2/A3 mocked proof
and the real product-flow composition proof.  A technically valid but semantically poor decision
is still useful smoke evidence and does not make the script fail.  Provider/structured-output
failure is persisted as typed evidence and returns a non-zero exit code.

Run from the repository root as a module so ``experiments.*`` imports resolve from the project
root.  S001 is public, so isolate ambient GitHub credentials/proxies as documented in
``ENVIRONMENT.md`` when needed::

    env \
      -u GITHUB_TOKEN \
      -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY \
      -u http_proxy -u https_proxy -u all_proxy \
      python -m experiments.b2_x1_s001_real_flow_a3_smoke
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
from experiments.b2_x1_evidence_gap_planner import (
    EvidenceGapDecision,
    render_evidence_gap_planner_request,
)
from upgradepilot.impact.python_support import PythonSupportDropInvestigationSelection
from upgradepilot.investigation import investigate_public_pull_request


_REPOSITORY = "pydantic/pydantic"
_PR_NUMBER = 13432
_OUTPUT_PATH = Path("/tmp/upgradepilot-b2-x1-r4-s001-real-flow-a3-smoke.json")
_EXPECTED_ACTION_ID = "acquire_exact_target_python_declaration"
_PLANNING_QUESTION = (
    "What additional admitted investigation, if any, is useful for determining whether the "
    "established upstream Python-support drop intersects the target declaration?"
)


def run_smoke() -> dict[str, object]:
    """Acquire real S001 state, invoke A3 once, and preserve the non-executed result."""

    investigation = investigate_public_pull_request(
        _REPOSITORY,
        _PR_NUMBER,
        token=None,
    )
    context = compose_pre_target_python_support_planner_context(
        investigation,
        planning_question=_PLANNING_QUESTION,
    )
    rendered_request = render_evidence_gap_planner_request(context)

    started = time.perf_counter()
    result = LocalEvidenceGapPlanner().decide(context)
    elapsed = time.perf_counter() - started

    common: dict[str, object] = {
        "kind": "b2_x1_r4_s001_real_flow_a3_smoke",
        "model": EVIDENCE_GAP_MODEL_ID,
        "case": {
            "repository": investigation.pull_request.repository,
            "pull_number": investigation.pull_request.number,
            "head_revision": investigation.pull_request.head_sha,
        },
        "elapsed_seconds": elapsed,
        "planner_request": rendered_request,
        "capability_executed": False,
    }

    if isinstance(result, EvidenceGapModelInvocationProblem):
        return {
            **common,
            "outcome": "invocation_problem",
            "invocation_problem": asdict(result),
            "decision": None,
            "basic_expectation_match": False,
            "admission": None,
        }

    if not isinstance(result, EvidenceGapDecision):
        raise TypeError(f"Unsupported A3 smoke result type: {type(result)!r}")

    admission_payload: dict[str, object] | None = None
    if result.decision_kind == "ACTION_SELECTED":
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
                remaining_investigations=(
                    context.planning_budget.remaining_investigations
                ),
                actions=(action,),
            ),
            result,
        )
        if isinstance(admission, AdmittedInvestigationAction):
            admission_payload = {
                "kind": "admitted_action",
                "action_id": admission.action.action_id,
                "explanation": admission.explanation,
            }
        elif isinstance(admission, EvidenceGapAdmissionProblem):
            admission_payload = {
                "kind": "admission_problem",
                **asdict(admission),
            }
        else:
            raise TypeError(f"Unsupported admission result type: {type(admission)!r}")

    return {
        **common,
        "outcome": "decision",
        "invocation_problem": None,
        "decision": asdict(result),
        "basic_expectation_match": (
            result.decision_kind == "ACTION_SELECTED"
            and result.action_id == _EXPECTED_ACTION_ID
        ),
        "admission": admission_payload,
    }


def main() -> int:
    """Persist and print one real-flow A3 smoke result without executing a capability."""

    output = run_smoke()
    _OUTPUT_PATH.write_text(
        json.dumps(output, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    print(f"case: {_REPOSITORY}#{_PR_NUMBER}")
    print(f"model: {EVIDENCE_GAP_MODEL_ID}")
    print(f"outcome: {output['outcome']}")
    print(f"elapsed_seconds: {output['elapsed_seconds']:.3f}")

    if output["outcome"] == "invocation_problem":
        problem = output["invocation_problem"]
        assert isinstance(problem, dict)
        print(f"invocation_problem_reason: {problem['reason']}")
        print(f"invocation_problem_detail: {problem['detail']}")
        print("capability_executed: False")
        print(f"output: {_OUTPUT_PATH}")
        return 1

    decision = output["decision"]
    assert isinstance(decision, dict)
    print(f"decision_kind: {decision['decision_kind']}")
    print(f"action_id: {decision['action_id']}")
    print(f"explanation: {decision['explanation']}")
    print(f"basic_expectation_match: {output['basic_expectation_match']}")

    admission = output["admission"]
    if isinstance(admission, dict):
        print(f"admission_kind: {admission['kind']}")
        if "action_id" in admission:
            print(f"admission_action_id: {admission['action_id']}")
    else:
        print("admission_kind: not_applicable_no_tool")

    print("capability_executed: False")
    print(f"output: {_OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
