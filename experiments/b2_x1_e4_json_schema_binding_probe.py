"""Test JSON Schema as a machine-readable output control on exact E4.1 planner state.

E4.1 already showed that the adopted model can bind its correct S001 reasoning to the exact
trusted action ID when given one closed action descriptor. E4.2 keeps that successful planner
input fixed and changes only the provider output contract::

    exact persisted E4.1 planner_input
    + same system prompt / model / temperature / seed
    + strict JSON Schema response_format
    -> parse machine-readable result
    -> record only; execute nothing

The schema deliberately does not encode the expected action ID as an enum. It requires only the
machine-readable equivalent of the E4.1 free-form answer: ``action_id`` as string-or-null plus a
non-empty ``explanation``. Deterministic admission is still absent.
"""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import time
from typing import Any

import requests

from experiments.b2_x1_planner_contract import TARGET_PYTHON_DECLARATION_ACTION_ID

_REPOSITORY = "pydantic/pydantic"
_PR_NUMBER = 13432
_REVISION = "aa2dc024d33f61cdef50bf1973ab5adf0a974f5a"
_DEFAULT_BASE_URL = "http://127.0.0.1:12345"
_DEFAULT_MODEL = "gemma-4-e4b-it-ud"
_E4_1_OUTPUT_PATH = Path("/tmp/upgradepilot-b2-x1-e4-closed-action-binding.json")
_OUTPUT_PATH = Path("/tmp/upgradepilot-b2-x1-e4-json-schema-binding.json")
_MODEL_LIST_TIMEOUT_SECONDS = 15.0
_REQUEST_TIMEOUT_SECONDS = 180.0
_MAX_COMPLETION_TOKENS = 900

_SYSTEM_PROMPT = """You are assisting with a software-upgrade investigation.

Use only the supplied investigation state and supplied allowed actions. Select at most one
allowed action when it is useful for answering the planning question, or say that no action is
useful. If you select an action, name its exact action_id and explain why it is the useful next
step. Do not execute anything.
"""

_OUTPUT_SCHEMA: dict[str, object] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["action_id", "explanation"],
    "properties": {
        "action_id": {
            "anyOf": [
                {"type": "string", "minLength": 1},
                {"type": "null"},
            ]
        },
        "explanation": {"type": "string", "minLength": 1},
    },
}


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


def _load_e4_1_replay() -> tuple[dict[str, object], str]:
    """Load and validate the successful E4.1 record whose planner input must stay fixed."""

    try:
        raw = _E4_1_OUTPUT_PATH.read_bytes()
    except FileNotFoundError as exc:
        raise RuntimeError(
            "E4.2 requires the successful E4.1 evidence file at "
            f"{_E4_1_OUTPUT_PATH}."
        ) from exc

    try:
        document = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError("E4.1 replay evidence is not valid JSON.") from exc
    if not isinstance(document, dict):
        raise RuntimeError("E4.1 replay evidence must be one JSON object.")

    expected_flags = {
        "kind": "b2_x1_e4_closed_action_binding_probe",
        "closed_action_catalog_supplied": True,
        "json_schema_supplied": False,
        "deterministic_admission_applied": False,
        "capability_executed": False,
        "raw_upstream_text_supplied_to_planner": False,
        "github_acquisition_performed": False,
        "support_drop_model_reexecuted": False,
        "expected_action_id_mentioned": True,
    }
    for field, expected in expected_flags.items():
        if document.get(field) != expected:
            raise RuntimeError(
                f"E4.1 replay field {field!r} differs from the successful control result."
            )

    planner_input = document.get("planner_input")
    if not isinstance(planner_input, dict):
        raise RuntimeError("E4.1 replay record contains no usable planner_input object.")
    if planner_input.get("repository") != _REPOSITORY:
        raise RuntimeError("E4.1 replay repository differs from S001.")
    if planner_input.get("pull_number") != _PR_NUMBER:
        raise RuntimeError("E4.1 replay pull number differs from S001.")
    if planner_input.get("revision") != _REVISION:
        raise RuntimeError("E4.1 replay revision differs from S001.")

    allowed_actions = planner_input.get("allowed_actions")
    if not isinstance(allowed_actions, list) or len(allowed_actions) != 1:
        raise RuntimeError("E4.1 replay must contain exactly one trusted allowed action.")
    action = allowed_actions[0]
    if not isinstance(action, dict):
        raise RuntimeError("E4.1 replay action descriptor is malformed.")
    if action.get("action_id") != TARGET_PYTHON_DECLARATION_ACTION_ID:
        raise RuntimeError("E4.1 replay action identity differs from the accepted S001 action.")

    return planner_input, sha256(raw).hexdigest()


def _parse_schema_content(raw_content: str) -> dict[str, object]:
    try:
        parsed = json.loads(raw_content)
    except json.JSONDecodeError as exc:
        raise RuntimeError("JSON-Schema planner content was not valid JSON.") from exc
    if not isinstance(parsed, dict):
        raise RuntimeError("JSON-Schema planner content was not a JSON object.")
    if set(parsed) != {"action_id", "explanation"}:
        raise RuntimeError("JSON-Schema planner content contained unexpected fields.")
    action_id = parsed["action_id"]
    explanation = parsed["explanation"]
    if action_id is not None and not isinstance(action_id, str):
        raise RuntimeError("JSON-Schema planner action_id was not string-or-null.")
    if not isinstance(explanation, str) or not explanation.strip():
        raise RuntimeError("JSON-Schema planner explanation was empty or non-text.")
    return parsed


def run_probe() -> dict[str, object]:
    """Replay exact E4.1 input and add only provider JSON Schema structured output."""

    planner_input, e4_1_sha256 = _load_e4_1_replay()

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
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "upgradepilot_b2_x1_e4_action_binding",
                "strict": True,
                "schema": _OUTPUT_SCHEMA,
            },
        },
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
    parsed_model_content = _parse_schema_content(raw_model_content)

    return {
        "kind": "b2_x1_e4_json_schema_binding_probe",
        "model": _DEFAULT_MODEL,
        "temperature": 0,
        "seed": 0,
        "elapsed_seconds": elapsed,
        "comparison_basis": "exact_persisted_e4_1_planner_input_plus_json_schema_only",
        "e4_1_replay_path": str(_E4_1_OUTPUT_PATH),
        "e4_1_replay_sha256": e4_1_sha256,
        "planner_input": planner_input,
        "raw_model_content": raw_model_content,
        "parsed_model_content": parsed_model_content,
        "expected_action_id": TARGET_PYTHON_DECLARATION_ACTION_ID,
        "expected_action_id_selected": (
            parsed_model_content["action_id"] == TARGET_PYTHON_DECLARATION_ACTION_ID
        ),
        "capability_executed": False,
        "closed_action_catalog_supplied": True,
        "json_schema_supplied": True,
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
    print("comparison_basis: exact persisted E4.1 planner input + JSON Schema only")
    print(f"e4_1_replay_sha256: {output['e4_1_replay_sha256']}")
    print("github_acquisition_performed: False")
    print("support_drop_model_reexecuted: False")
    print(f"model: {_DEFAULT_MODEL}")
    print(f"elapsed_seconds: {output['elapsed_seconds']:.3f}")
    print(f"expected_action_id_selected: {output['expected_action_id_selected']}")
    print("raw_model_content:")
    print(output["raw_model_content"])
    print("capability_executed: False")
    print(f"output: {_OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
