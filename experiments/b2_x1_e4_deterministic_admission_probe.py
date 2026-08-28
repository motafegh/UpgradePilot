"""Test deterministic admission on the exact successful E4.2 planner proposal.

E4.2 already produced a schema-valid, correct S001 action choice. E4.3 does not call GitHub or
LM Studio again. It replays that exact untrusted model result against reconstructed trusted state
and the existing ``admit_agent_plan(...)`` owner.

The E4.2 schema intentionally asked the model for only ``action_id`` + ``explanation``. Trusted
action metadata that the old planner contract also asks the model to echo (target proposition and
result families) is rebound deterministically from the trusted action descriptor before admission.
This keeps the experiment focused on admission rather than on redundant model repetition.

Checks::

    observed E4.2 correct proposal + current trusted state
    -> should admit the exact read-only action

    counterfactual unknown action id + same trusted state
    -> should reject as unknown_action

    observed correct proposal + stale/non-actionable trusted target proposition
    -> should reject as target_proposition_not_actionable

No capability is executed in any branch.
"""

from __future__ import annotations

from dataclasses import asdict, replace
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

from experiments.b2_x1_planner_contract import (
    AdmittedInvestigationAction,
    AdmittedNoToolDisposition,
    AgentPlanResult,
    InvestigationSnapshot,
    PlanAdmissionProblem,
    TARGET_PYTHON_DECLARATION_ACTION_ID,
    TARGET_PYTHON_DECLARATION_PROPOSITION,
    admit_agent_plan,
    build_target_python_declaration_action,
)
from upgradepilot.impact.applicability import PropositionAssessment

_REPOSITORY = "pydantic/pydantic"
_PR_NUMBER = 13432
_REVISION = "aa2dc024d33f61cdef50bf1973ab5adf0a974f5a"
_E4_2_OUTPUT_PATH = Path("/tmp/upgradepilot-b2-x1-e4-json-schema-binding.json")
_OUTPUT_PATH = Path("/tmp/upgradepilot-b2-x1-e4-deterministic-admission.json")
_UNKNOWN_ACTION_ID = "invented_untrusted_action"


def _load_e4_2_replay() -> tuple[dict[str, Any], dict[str, Any], str]:
    """Load and validate the exact successful E4.2 evidence record."""

    try:
        raw = _E4_2_OUTPUT_PATH.read_bytes()
    except FileNotFoundError as exc:
        raise RuntimeError(
            "E4.3 requires the successful E4.2 evidence file at "
            f"{_E4_2_OUTPUT_PATH}."
        ) from exc

    try:
        document = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError("E4.2 replay evidence is not valid JSON.") from exc
    if not isinstance(document, dict):
        raise RuntimeError("E4.2 replay evidence must be one JSON object.")

    expected_flags = {
        "kind": "b2_x1_e4_json_schema_binding_probe",
        "closed_action_catalog_supplied": True,
        "json_schema_supplied": True,
        "deterministic_admission_applied": False,
        "capability_executed": False,
        "raw_upstream_text_supplied_to_planner": False,
        "github_acquisition_performed": False,
        "support_drop_model_reexecuted": False,
        "expected_action_id_selected": True,
    }
    for field, expected in expected_flags.items():
        if document.get(field) != expected:
            raise RuntimeError(
                f"E4.2 replay field {field!r} differs from the successful control result."
            )

    planner_input = document.get("planner_input")
    parsed_model_content = document.get("parsed_model_content")
    if not isinstance(planner_input, dict):
        raise RuntimeError("E4.2 replay contains no usable planner_input object.")
    if not isinstance(parsed_model_content, dict):
        raise RuntimeError("E4.2 replay contains no usable parsed_model_content object.")

    if planner_input.get("repository") != _REPOSITORY:
        raise RuntimeError("E4.2 replay repository differs from S001.")
    if planner_input.get("pull_number") != _PR_NUMBER:
        raise RuntimeError("E4.2 replay pull number differs from S001.")
    if planner_input.get("revision") != _REVISION:
        raise RuntimeError("E4.2 replay revision differs from S001.")
    if planner_input.get("remaining_investigation_steps") != 1:
        raise RuntimeError("E4.2 replay step budget differs from the accepted decision point.")

    if parsed_model_content.get("action_id") != TARGET_PYTHON_DECLARATION_ACTION_ID:
        raise RuntimeError("E4.2 replay did not preserve the accepted action ID.")
    explanation = parsed_model_content.get("explanation")
    if not isinstance(explanation, str) or not explanation.strip():
        raise RuntimeError("E4.2 replay explanation is missing or empty.")

    return planner_input, parsed_model_content, sha256(raw).hexdigest()


def _propositions_from_payload(payload: object) -> tuple[PropositionAssessment, ...]:
    if not isinstance(payload, list) or not payload:
        raise RuntimeError("E4.2 replay propositions are missing or empty.")

    propositions: list[PropositionAssessment] = []
    for index, item in enumerate(payload):
        if not isinstance(item, dict):
            raise RuntimeError(f"E4.2 replay proposition {index} is not an object.")
        try:
            proposition = PropositionAssessment(
                key=item["key"],
                state=item["state"],
                evidence_coverage=item["evidence_coverage"],
                evidence_owner=item["evidence_owner"],
                detail=item["detail"],
            )
        except KeyError as exc:
            raise RuntimeError(
                f"E4.2 replay proposition {index} is missing field {exc.args[0]!r}."
            ) from exc
        propositions.append(proposition)

    return tuple(propositions)


def _snapshot_from_replay(planner_input: dict[str, Any]) -> InvestigationSnapshot:
    action = build_target_python_declaration_action(_REPOSITORY, _REVISION)
    return InvestigationSnapshot(
        case_key="e4-3-s001-admission",
        repository=_REPOSITORY,
        pull_number=_PR_NUMBER,
        revision=_REVISION,
        propositions=_propositions_from_payload(planner_input.get("propositions")),
        attempted_actions=(),
        allowed_actions=(action,),
        remaining_steps=1,
    )


def _plan_from_minimal_model_result(
    parsed_model_content: dict[str, Any],
    *,
    selected_action_id: str | None = None,
) -> AgentPlanResult:
    """Bind trusted action metadata around the model's minimal action choice."""

    action = build_target_python_declaration_action(_REPOSITORY, _REVISION)
    action_id = (
        parsed_model_content["action_id"]
        if selected_action_id is None
        else selected_action_id
    )
    if not isinstance(action_id, str) or not action_id.strip():
        raise RuntimeError("E4.3 action replay requires a non-empty selected action ID.")

    explanation = parsed_model_content["explanation"]
    assert isinstance(explanation, str)

    return AgentPlanResult(
        state="choose_action",
        selected_action_id=action_id,
        target_proposition=action.target_proposition,
        reason=explanation,
        expected_result_categories=action.result_families,
        limitations=(),
    )


def _admission_record(result: object) -> dict[str, Any]:
    if isinstance(result, AdmittedInvestigationAction):
        return {
            "kind": "admitted_action",
            "result": asdict(result),
        }
    if isinstance(result, AdmittedNoToolDisposition):
        return {
            "kind": "admitted_no_tool",
            "result": asdict(result),
        }
    if isinstance(result, PlanAdmissionProblem):
        return {
            "kind": "admission_problem",
            "reason": result.reason,
            "detail": result.detail,
            "result": asdict(result),
        }
    raise TypeError(f"Unsupported admission result type: {type(result)!r}")


def _stale_snapshot(snapshot: InvestigationSnapshot) -> InvestigationSnapshot:
    propositions = tuple(
        replace(
            proposition,
            state="established",
            evidence_coverage="sufficient",
            detail=(
                "Counterfactual E4.3 stale-state control: the exact target Python "
                "declaration is now already established."
            ),
        )
        if proposition.key == TARGET_PYTHON_DECLARATION_PROPOSITION
        else proposition
        for proposition in snapshot.propositions
    )
    return replace(snapshot, propositions=propositions)


def run_probe() -> dict[str, Any]:
    """Replay E4.2 and test existing deterministic admission without another model call."""

    planner_input, parsed_model_content, e4_2_sha256 = _load_e4_2_replay()
    snapshot = _snapshot_from_replay(planner_input)
    observed_plan = _plan_from_minimal_model_result(parsed_model_content)

    observed_admission = admit_agent_plan(snapshot, observed_plan)

    unknown_action_plan = _plan_from_minimal_model_result(
        parsed_model_content,
        selected_action_id=_UNKNOWN_ACTION_ID,
    )
    unknown_action_admission = admit_agent_plan(snapshot, unknown_action_plan)

    stale_snapshot = _stale_snapshot(snapshot)
    stale_state_admission = admit_agent_plan(stale_snapshot, observed_plan)

    return {
        "kind": "b2_x1_e4_deterministic_admission_probe",
        "comparison_basis": "exact_persisted_e4_2_result_plus_existing_deterministic_admission",
        "e4_2_replay_path": str(_E4_2_OUTPUT_PATH),
        "e4_2_replay_sha256": e4_2_sha256,
        "observed_model_result": parsed_model_content,
        "trusted_snapshot": asdict(snapshot),
        "observed_admission": _admission_record(observed_admission),
        "unknown_action_counterfactual": {
            "selected_action_id": _UNKNOWN_ACTION_ID,
            "admission": _admission_record(unknown_action_admission),
        },
        "stale_state_counterfactual": {
            "target_proposition_state": "established",
            "target_proposition_evidence_coverage": "sufficient",
            "admission": _admission_record(stale_state_admission),
        },
        "model_called": False,
        "github_acquisition_performed": False,
        "capability_executed": False,
        "deterministic_admission_applied": True,
        "minimal_model_output_rebound_to_trusted_action_metadata": True,
    }


def main() -> int:
    output = run_probe()
    _OUTPUT_PATH.write_text(
        json.dumps(output, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    observed = output["observed_admission"]
    unknown = output["unknown_action_counterfactual"]["admission"]
    stale = output["stale_state_counterfactual"]["admission"]

    print(f"case: {_REPOSITORY}#{_PR_NUMBER}")
    print("comparison_basis: exact persisted E4.2 result + deterministic admission")
    print(f"e4_2_replay_sha256: {output['e4_2_replay_sha256']}")
    print("model_called: False")
    print(f"observed_admission: {observed['kind']}")
    print(
        "unknown_action_counterfactual: "
        f"{unknown['kind']} | {unknown.get('reason')}"
    )
    print(
        "stale_state_counterfactual: "
        f"{stale['kind']} | {stale.get('reason')}"
    )
    print("capability_executed: False")
    print(f"output: {_OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
