"""Test the smallest trusted action-binding control by replaying exact E3 S001 state.

E3 showed that the adopted model can identify the correct missing evidence proposition from the
real typed S001 pre-investigation state without a closed action catalog, JSON Schema, or
deterministic admission. E4.1 changes exactly one planner-facing capability: the model now
receives the existing trusted action descriptor for acquiring the exact target Python
declaration.

A controlled comparison requires the *same* state that E3 used. Therefore E4.1 deliberately
replays the successful E3 evidence file instead of reacquiring the whole public S001 product
pipeline::

    exact persisted E3 planner input
    -> validate S001 identity / E3 boundary facts
    -> add one trusted pre-bound action descriptor
    -> minimally constrained LM Studio response
    -> record only; execute nothing

This avoids contaminating the E3→E4 comparison with GitHub rate limits, fresh provider state, or
a second pass through the already-adopted support-drop semantic model. No provider structured-
output schema and no deterministic admission are used here.
"""

from __future__ import annotations

from dataclasses import asdict
from hashlib import sha256
import json
from pathlib import Path
import time
from typing import Any

import requests

from experiments.b2_x1_planner_contract import (
    TARGET_PYTHON_DECLARATION_ACTION_ID,
    TARGET_PYTHON_DECLARATION_PATH,
    TARGET_PYTHON_DECLARATION_PROPOSITION,
    build_target_python_declaration_action,
)

_REPOSITORY = "pydantic/pydantic"
_PR_NUMBER = 13432
_REVISION = "aa2dc024d33f61cdef50bf1973ab5adf0a974f5a"
_DEFAULT_BASE_URL = "http://127.0.0.1:12345"
_DEFAULT_MODEL = "gemma-4-e4b-it-ud"
_E3_OUTPUT_PATH = Path("/tmp/upgradepilot-b2-x1-e3-minimal-s001-planner.json")
_OUTPUT_PATH = Path("/tmp/upgradepilot-b2-x1-e4-closed-action-binding.json")
_MODEL_LIST_TIMEOUT_SECONDS = 15.0
_REQUEST_TIMEOUT_SECONDS = 180.0
_MAX_COMPLETION_TOKENS = 900

_SYSTEM_PROMPT = """You are assisting with a software-upgrade investigation.

Use only the supplied investigation state and supplied allowed actions. Select at most one
allowed action when it is useful for answering the planning question, or say that no action is
useful. If you select an action, name its exact action_id and explain why it is the useful next
step. Do not execute anything.
"""


def _local_session() -> requests.Session:
    """Use the accepted proxy-independent localhost boundary for LM Studio traffic."""

    session = requests.Session()
    session.trust_env = False
    return session


def _available_model_ids(
    session: requests.Session,
    base_url: str,
) -> tuple[str, ...]:
    response = session.get(
        f"{base_url}/v1/models",
        timeout=_MODEL_LIST_TIMEOUT_SECONDS,
    )
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, dict) or not isinstance(payload.get("data"), list):
        raise RuntimeError("LM Studio /v1/models returned an unexpected response shape.")

    ids: list[str] = []
    for item in payload["data"]:
        if isinstance(item, dict) and isinstance(item.get("id"), str):
            ids.append(item["id"])
    return tuple(ids)


def _extract_text_completion(outer: dict[str, Any]) -> str:
    choices = outer.get("choices")
    if (
        not isinstance(choices, list)
        or not choices
        or not isinstance(choices[0], dict)
    ):
        raise RuntimeError("LM Studio response contained no usable first choice.")
    message = choices[0].get("message")
    if not isinstance(message, dict) or not isinstance(message.get("content"), str):
        raise RuntimeError("LM Studio first choice contained no textual message content.")
    return message["content"]


def _load_e3_replay() -> tuple[dict[str, object], dict[str, object], str]:
    """Load and validate the exact successful E3 record used as E4.1's control state."""

    try:
        raw = _E3_OUTPUT_PATH.read_bytes()
    except FileNotFoundError as exc:
        raise RuntimeError(
            "E4.1 requires the successful E3 evidence file at "
            f"{_E3_OUTPUT_PATH}; rerun E3 only if that evidence file is genuinely absent."
        ) from exc

    try:
        document = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError("E3 replay evidence is not valid JSON.") from exc
    if not isinstance(document, dict):
        raise RuntimeError("E3 replay evidence must be one JSON object.")

    if document.get("kind") != "b2_x1_e3_minimal_s001_planner_probe":
        raise RuntimeError("E4.1 replay source is not the expected E3 experiment record.")
    if document.get("capability_executed") is not False:
        raise RuntimeError("E3 replay record unexpectedly reports capability execution.")
    if document.get("closed_action_catalog_supplied") is not False:
        raise RuntimeError("E3 replay record already contained a closed action catalog.")
    if document.get("json_schema_supplied") is not False:
        raise RuntimeError("E3 replay record already contained JSON Schema output control.")
    if document.get("deterministic_admission_applied") is not False:
        raise RuntimeError("E3 replay record already applied deterministic admission.")
    if document.get("raw_upstream_text_supplied") is not False:
        raise RuntimeError("E3 replay record unexpectedly supplied raw upstream text.")

    planner_input = document.get("planner_input")
    if not isinstance(planner_input, dict):
        raise RuntimeError("E3 replay record contains no usable planner_input object.")

    if planner_input.get("repository") != _REPOSITORY:
        raise RuntimeError("E3 replay repository identity differs from S001.")
    if planner_input.get("pull_number") != _PR_NUMBER:
        raise RuntimeError("E3 replay pull-request identity differs from S001.")
    if planner_input.get("revision") != _REVISION:
        raise RuntimeError("E3 replay revision differs from the accepted S001 head.")
    if planner_input.get("remaining_investigation_steps") != 1:
        raise RuntimeError("E3 replay step budget differs from the accepted E3 decision point.")

    planning_question = planner_input.get("planning_question")
    propositions = planner_input.get("propositions")
    if not isinstance(planning_question, str) or not planning_question.strip():
        raise RuntimeError("E3 replay planning question is missing or empty.")
    if not isinstance(propositions, list) or not propositions:
        raise RuntimeError("E3 replay propositions are missing or empty.")

    deterministic_baseline = document.get("deterministic_baseline")
    if not isinstance(deterministic_baseline, dict):
        raise RuntimeError("E3 replay record contains no deterministic baseline selection.")
    expected_baseline = {
        "kind": TARGET_PYTHON_DECLARATION_ACTION_ID,
        "repository": _REPOSITORY,
        "revision": _REVISION,
        "path": TARGET_PYTHON_DECLARATION_PATH,
        "proposition_key": TARGET_PYTHON_DECLARATION_PROPOSITION,
    }
    for field, expected in expected_baseline.items():
        if deterministic_baseline.get(field) != expected:
            raise RuntimeError(
                f"E3 deterministic baseline field {field!r} differs from expected S001 state."
            )

    return planner_input, deterministic_baseline, sha256(raw).hexdigest()


def run_probe() -> dict[str, object]:
    """Replay exact E3 state, add one trusted action descriptor, and record one proposal."""

    e3_input, deterministic_baseline, e3_sha256 = _load_e3_replay()

    action = build_target_python_declaration_action(_REPOSITORY, _REVISION)
    planner_input = {
        "planning_question": e3_input["planning_question"],
        "repository": e3_input["repository"],
        "pull_number": e3_input["pull_number"],
        "revision": e3_input["revision"],
        "propositions": e3_input["propositions"],
        "allowed_actions": [asdict(action)],
        "remaining_investigation_steps": e3_input["remaining_investigation_steps"],
    }

    payload: dict[str, object] = {
        "model": _DEFAULT_MODEL,
        "messages": [
            {"role": "system", "content": _SYSTEM_PROMPT},
            {
                "role": "user",
                "content": json.dumps(
                    planner_input,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                ),
            },
        ],
        "temperature": 0,
        "seed": 0,
        "max_tokens": _MAX_COMPLETION_TOKENS,
        "stream": False,
    }

    session = _local_session()
    model_ids = _available_model_ids(session, _DEFAULT_BASE_URL)
    if _DEFAULT_MODEL not in model_ids:
        raise RuntimeError(
            f"Expected model {_DEFAULT_MODEL!r} is not currently exposed by LM Studio; "
            f"available IDs: {model_ids!r}"
        )

    started = time.perf_counter()
    response = session.post(
        f"{_DEFAULT_BASE_URL}/v1/chat/completions",
        json=payload,
        timeout=_REQUEST_TIMEOUT_SECONDS,
    )
    elapsed = time.perf_counter() - started
    if not response.ok:
        raise RuntimeError(
            f"LM Studio returned HTTP {response.status_code}: {response.text}"
        )

    outer = response.json()
    if not isinstance(outer, dict):
        raise RuntimeError("LM Studio completion response was not a JSON object.")
    raw_model_content = _extract_text_completion(outer)

    return {
        "kind": "b2_x1_e4_closed_action_binding_probe",
        "model": _DEFAULT_MODEL,
        "temperature": 0,
        "seed": 0,
        "elapsed_seconds": elapsed,
        "comparison_basis": "exact_persisted_e3_planner_input_plus_one_trusted_action_descriptor",
        "e3_replay_path": str(_E3_OUTPUT_PATH),
        "e3_replay_sha256": e3_sha256,
        "planner_input": planner_input,
        "raw_model_content": raw_model_content,
        "expected_action_id": TARGET_PYTHON_DECLARATION_ACTION_ID,
        "expected_action_id_mentioned": (
            TARGET_PYTHON_DECLARATION_ACTION_ID in raw_model_content
        ),
        "deterministic_baseline": deterministic_baseline,
        "capability_executed": False,
        "closed_action_catalog_supplied": True,
        "json_schema_supplied": False,
        "deterministic_admission_applied": False,
        "raw_upstream_text_supplied_to_planner": False,
        "github_acquisition_performed": False,
        "support_drop_model_reexecuted": False,
    }


def main() -> int:
    output = run_probe()
    _OUTPUT_PATH.write_text(
        json.dumps(output, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    print(f"case: {_REPOSITORY}#{_PR_NUMBER}")
    print("comparison_basis: exact persisted E3 planner input + one trusted action")
    print(f"e3_replay_sha256: {output['e3_replay_sha256']}")
    print("github_acquisition_performed: False")
    print("support_drop_model_reexecuted: False")
    print(f"model: {_DEFAULT_MODEL}")
    print(f"elapsed_seconds: {output['elapsed_seconds']:.3f}")
    print(
        "expected_action_id_mentioned: "
        f"{output['expected_action_id_mentioned']}"
    )
    print("raw_model_content:")
    print(output["raw_model_content"])
    print("capability_executed: False")
    print(f"output: {_OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
