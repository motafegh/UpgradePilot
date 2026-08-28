#!/usr/bin/env python3
"""Observe minimally constrained planner behavior on the real S001 typed product state.

This experiment intentionally sits *before* the previously designed strict planner contract.
Its purpose is behavioral observation, not capability execution or product integration.

Real flow::

    pydantic/pydantic#13432
    -> investigate_public_pull_request(...)
    -> retained pre-target-declaration Python-support assessment
    -> small typed proposition projection
    -> minimally constrained LM Studio prompt
    -> raw natural-language proposal only

The model is deliberately NOT given the closed action catalog, pre-bound action arguments,
planner JSON Schema, deterministic admission rules, evaluator oracle, or raw upstream changelog
text.  It is asked what investigation it would perform next and why.  No proposed action is
executed.

This gives E3 a baseline for later incremental-constraint comparisons: what does the adopted
model naturally infer from the real typed evidence state before guardrails shape its answer?
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
from upgradepilot.impact.python_support import PythonSupportDropImpactAssessment
from upgradepilot.investigation import investigate_public_pull_request

_REPOSITORY = "pydantic/pydantic"
_PR_NUMBER = 13432
_DEFAULT_BASE_URL = "http://127.0.0.1:12345"
_DEFAULT_MODEL = "gemma-4-e4b-it-ud"
_OUTPUT_PATH = Path("/tmp/upgradepilot-b2-x1-e3-minimal-s001-planner.json")
_MODEL_LIST_TIMEOUT_SECONDS = 15.0
_REQUEST_TIMEOUT_SECONDS = 180.0
_MAX_COMPLETION_TOKENS = 900

_PLANNING_QUESTION = (
    "Given the current evidence about this dependency update, what is the single most useful "
    "next investigation step, if any, for determining whether the upstream Python 3.8 support "
    "drop affects the target project's exact declared Python range?"
)

_SYSTEM_PROMPT = """You are assisting with a software-upgrade investigation.

Use only the supplied investigation state. Propose at most one next investigation step, or say
that no further investigation is useful. Explain what evidence the step would obtain and why it
would help answer the planning question. Do not execute anything.
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
    """Acquire real S001 state, project it, and obtain one non-executed model proposal."""

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
    planner_input = {
        "planning_question": _PLANNING_QUESTION,
        "repository": investigation.pull_request.repository,
        "pull_number": investigation.pull_request.number,
        "revision": investigation.pull_request.head_sha,
        "propositions": [asdict(item) for item in propositions],
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
        "kind": "b2_x1_e3_minimal_s001_planner_probe",
        "model": _DEFAULT_MODEL,
        "temperature": 0,
        "seed": 0,
        "elapsed_seconds": elapsed,
        "planner_input": planner_input,
        "raw_model_content": raw_model_content,
        "deterministic_baseline": (
            None if deterministic_selection is None else asdict(deterministic_selection)
        ),
        "capability_executed": False,
        "closed_action_catalog_supplied": False,
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
    print("raw_model_content:")
    print(output["raw_model_content"])
    print("capability_executed: False")
    print(f"output: {_OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
