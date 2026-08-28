"""Test the smallest trusted action-binding control on the real S001 planner state.

E3 showed that the adopted model can identify the correct missing evidence proposition from the
real typed S001 pre-investigation state without a closed action catalog, JSON Schema, or
deterministic admission.  E4.1 changes exactly one planning capability: the model now receives
the existing trusted action descriptor for acquiring the exact target Python declaration.

The experiment remains observation-only::

    real S001 product investigation
    -> small typed proposition projection
    -> one trusted pre-bound action descriptor
    -> minimally constrained LM Studio response
    -> record only; execute nothing

No provider structured-output schema and no deterministic admission are used here.  The purpose
is to observe whether closed trusted action binding converts E3's correct conceptual next step
into an exact action-id selection without crediting heavier controls for that effect.
"""

from __future__ import annotations

from dataclasses import asdict
import json
import os
from pathlib import Path
import time
from typing import Any

import requests

from experiments.b2_x1_e2_s001_state_origin_probe import proposition_projection
from experiments.b2_x1_planner_contract import (
    TARGET_PYTHON_DECLARATION_ACTION_ID,
    build_target_python_declaration_action,
)
from upgradepilot.impact.python_support import PythonSupportDropImpactAssessment
from upgradepilot.investigation import investigate_public_pull_request

_REPOSITORY = "pydantic/pydantic"
_PR_NUMBER = 13432
_DEFAULT_BASE_URL = "http://127.0.0.1:12345"
_DEFAULT_MODEL = "gemma-4-e4b-it-ud"
_OUTPUT_PATH = Path("/tmp/upgradepilot-b2-x1-e4-closed-action-binding.json")
_MODEL_LIST_TIMEOUT_SECONDS = 15.0
_REQUEST_TIMEOUT_SECONDS = 180.0
_MAX_COMPLETION_TOKENS = 900

_PLANNING_QUESTION = (
    "Given the current evidence about this dependency update, what is the single most useful "
    "next investigation step, if any, for determining whether the upstream Python 3.8 support "
    "drop affects the target project's exact declared Python range?"
)

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


def run_probe() -> dict[str, object]:
    """Acquire real S001 state, add one trusted action descriptor, and record one proposal."""

    investigation = investigate_public_pull_request(
        _REPOSITORY,
        _PR_NUMBER,
        token=os.getenv("GITHUB_TOKEN"),
    )
    assessment = investigation.python_support_drop_pre_investigation_result
    if not isinstance(assessment, PythonSupportDropImpactAssessment):
        raise RuntimeError(
            "Real S001 product path did not retain the expected pre-investigation assessment."
        )

    propositions = proposition_projection(assessment)
    action = build_target_python_declaration_action(
        investigation.pull_request.repository,
        investigation.pull_request.head_sha,
    )

    planner_input = {
        "planning_question": _PLANNING_QUESTION,
        "repository": investigation.pull_request.repository,
        "pull_number": investigation.pull_request.number,
        "revision": investigation.pull_request.head_sha,
        "propositions": [asdict(item) for item in propositions],
        "allowed_actions": [asdict(action)],
        "remaining_investigation_steps": 1,
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

    deterministic_selection = investigation.python_support_drop_investigation_selection

    return {
        "kind": "b2_x1_e4_closed_action_binding_probe",
        "model": _DEFAULT_MODEL,
        "temperature": 0,
        "seed": 0,
        "elapsed_seconds": elapsed,
        "planner_input": planner_input,
        "raw_model_content": raw_model_content,
        "expected_action_id": TARGET_PYTHON_DECLARATION_ACTION_ID,
        "expected_action_id_mentioned": (
            TARGET_PYTHON_DECLARATION_ACTION_ID in raw_model_content
        ),
        "deterministic_baseline": (
            None if deterministic_selection is None else asdict(deterministic_selection)
        ),
        "capability_executed": False,
        "closed_action_catalog_supplied": True,
        "json_schema_supplied": False,
        "deterministic_admission_applied": False,
        "raw_upstream_text_supplied": False,
    }


def main() -> int:
    output = run_probe()
    _OUTPUT_PATH.write_text(
        json.dumps(output, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    print(f"case: {_REPOSITORY}#{_PR_NUMBER}")
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
