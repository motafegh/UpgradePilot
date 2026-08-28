#!/usr/bin/env python3
"""Probe the smallest useful no-tool planner disposition on three frozen development cases.

E3/E4 established the first action path incrementally:

    typed state
    -> correct reasoning
    + trusted action descriptor
    -> exact action binding
    + JSON Schema
    -> machine-readable shape
    + deterministic admission
    -> execution-time trusted-state containment

The remaining large semantic difference from the earlier strict planner result is no-tool state.
A plain ``action_id = null`` cannot tell these situations apart::

    stop
        the bounded planning question is sufficiently settled / no further justified work

    defer
        a useful next responsibility is known, but it is outside the admitted action catalog
        or current support boundary

    unresolved
        evidence remains insufficient/conflicted and no supported action or known outside
        capability is justified

E5 uses the already-accepted Phase-3 development controls for exactly those meanings:
``d-s004-stop``, ``d-s006-defer``, and ``d-conflict``.  It adds only a small strict structured
output with ``disposition`` + ``explanation``.  No GitHub acquisition, capability execution,
product mutation, deterministic admission, or protected scoring occurs here.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import time
from typing import Any, Literal

import requests


_DEFAULT_BASE_URL = "http://127.0.0.1:12345"
_DEFAULT_MODEL = "gemma-4-e4b-it-ud"
_OUTPUT_PATH = Path("/tmp/upgradepilot-b2-x1-e5-no-tool-dispositions.json")
_MODEL_LIST_TIMEOUT_SECONDS = 15.0
_REQUEST_TIMEOUT_SECONDS = 180.0
_MAX_COMPLETION_TOKENS = 700

NoToolDisposition = Literal["stop", "defer", "unresolved"]

_SYSTEM_PROMPT = """You are assisting with a bounded software-upgrade investigation.

Use only the supplied planning question and typed investigation state. No executable action is
available in these cases. Return the no-tool disposition that best matches the state:

- stop: the planning question is sufficiently settled, or no further justified work remains for
  that question.
- defer: a material unresolved proposition remains and a useful next responsibility/capability
  can be identified, but it is outside the currently admitted action catalog/support boundary.
- unresolved: evidence remains insufficient or conflicted and the state does not justify a
  supported action, a known outside capability, or a settled conclusion.

Explain the decision briefly. Do not execute anything and do not invent an action.
"""

_OUTPUT_SCHEMA: dict[str, object] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["disposition", "explanation"],
    "properties": {
        "disposition": {
            "type": "string",
            "enum": ["stop", "defer", "unresolved"],
        },
        "explanation": {"type": "string", "minLength": 1},
    },
}


@dataclass(frozen=True, slots=True)
class NoToolCase:
    case_key: str
    repository: str
    pull_number: int
    revision: str
    planning_question: str
    propositions: tuple[dict[str, str], ...]
    expected_disposition: NoToolDisposition


def _cases() -> tuple[NoToolCase, ...]:
    """Return the three accepted development controls needed for no-tool semantics."""

    return (
        NoToolCase(
            case_key="d-s004-stop",
            repository="googlefonts/glyphsLib",
            pull_number=1145,
            revision="f3cda8a94600e58d27f1bc17c99b7693718b6350",
            planning_question=(
                "Does the current bounded evidence state require any further investigation to "
                "answer whether the pytest update has an unresolved decision-critical authority gap?"
            ),
            propositions=(
                {
                    "key": "direct_pytest_development_role_established",
                    "state": "established",
                    "evidence_coverage": "sufficient",
                },
                {
                    "key": "changed_requirements_installed_by_owning_test_path",
                    "state": "established",
                    "evidence_coverage": "sufficient",
                },
                {
                    "key": "exact_head_relevant_pytest_ci_established",
                    "state": "established",
                    "evidence_coverage": "sufficient",
                },
                {
                    "key": "official_drop_in_bugfix_status_established",
                    "state": "established",
                    "evidence_coverage": "sufficient",
                },
                {
                    "key": "decision_critical_contradiction_or_gap_present",
                    "state": "refuted",
                    "evidence_coverage": "sufficient",
                },
            ),
            expected_disposition="stop",
        ),
        NoToolCase(
            case_key="d-s006-defer",
            repository="eduardoklosowski/qldebugger",
            pull_number=27,
            revision="a454b47b8e483dffc825a3c9998f38e7634ec93b",
            planning_question=(
                "What supported next investigation, if any, can establish whether the mapped "
                "Pydantic exception-semantic change produces an observable difference on the "
                "exact target branch?"
            ),
            propositions=(
                {
                    "key": "upstream_validator_typeerror_semantic_change_established",
                    "state": "established",
                    "evidence_coverage": "sufficient",
                },
                {
                    "key": "target_affected_validator_branch_established",
                    "state": "established",
                    "evidence_coverage": "sufficient",
                },
                {
                    "key": "visible_evidence_exercises_affected_branch",
                    "state": "refuted",
                    "evidence_coverage": "sufficient",
                },
                {
                    "key": "cross_version_target_exception_behavior_established",
                    "state": "unresolved",
                    "evidence_coverage": "insufficient",
                },
                {
                    "key": "discriminating_two_version_check_identified",
                    "state": "established",
                    "evidence_coverage": "sufficient",
                },
            ),
            expected_disposition="defer",
        ),
        NoToolCase(
            case_key="d-conflict",
            repository="example/conflicted-ci",
            pull_number=107,
            revision="7" * 40,
            planning_question=(
                "What planning disposition is supported for the dependency-CI coverage question "
                "when the trusted evidence remains genuinely conflicted and no admitted action "
                "or identified outside capability resolves it?"
            ),
            propositions=(
                {
                    "key": "dependency_ci_coverage_established",
                    "state": "conflicted",
                    "evidence_coverage": "sufficient",
                },
            ),
            expected_disposition="unresolved",
        ),
    )


def _local_session() -> requests.Session:
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


def _parse_content(raw_content: str) -> dict[str, str]:
    try:
        parsed = json.loads(raw_content)
    except json.JSONDecodeError as exc:
        raise RuntimeError("E5 structured content was not valid JSON.") from exc
    if not isinstance(parsed, dict) or set(parsed) != {"disposition", "explanation"}:
        raise RuntimeError("E5 structured content had an unexpected object shape.")
    disposition = parsed["disposition"]
    explanation = parsed["explanation"]
    if disposition not in {"stop", "defer", "unresolved"}:
        raise RuntimeError(f"E5 disposition was unsupported: {disposition!r}")
    if not isinstance(explanation, str) or not explanation.strip():
        raise RuntimeError("E5 explanation was empty or non-text.")
    return {"disposition": disposition, "explanation": explanation}


def _run_case(
    session: requests.Session,
    case: NoToolCase,
) -> dict[str, object]:
    planner_input = {
        "planning_question": case.planning_question,
        "repository": case.repository,
        "pull_number": case.pull_number,
        "revision": case.revision,
        "propositions": list(case.propositions),
        "allowed_actions": [],
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
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "upgradepilot_b2_x1_e5_no_tool_disposition",
                "strict": True,
                "schema": _OUTPUT_SCHEMA,
            },
        },
        "temperature": 0,
        "seed": 0,
        "max_tokens": _MAX_COMPLETION_TOKENS,
        "stream": False,
    }

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
    raw_content = _extract_text_completion(outer)
    parsed = _parse_content(raw_content)

    return {
        "case_key": case.case_key,
        "planner_input": planner_input,
        "expected_disposition": case.expected_disposition,
        "parsed_model_content": parsed,
        "raw_model_content": raw_content,
        "expectation_match": parsed["disposition"] == case.expected_disposition,
        "elapsed_seconds": elapsed,
    }


def main() -> int:
    session = _local_session()
    model_ids = _available_model_ids(session, _DEFAULT_BASE_URL)
    if _DEFAULT_MODEL not in model_ids:
        raise RuntimeError(
            f"Expected model {_DEFAULT_MODEL!r} is not currently exposed by LM Studio; "
            f"available IDs: {model_ids!r}"
        )

    results = [_run_case(session, case) for case in _cases()]
    output = {
        "kind": "b2_x1_e5_no_tool_disposition_probe",
        "model": _DEFAULT_MODEL,
        "temperature": 0,
        "seed": 0,
        "development_cases_only": True,
        "protected_scoring": False,
        "github_acquisition_performed": False,
        "capability_executed": False,
        "deterministic_admission_applied": False,
        "result_shape": ["disposition", "explanation"],
        "cases": results,
    }
    _OUTPUT_PATH.write_text(
        json.dumps(output, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    print(f"no-tool cases: {len(results)}")
    for result in results:
        print(
            f"{result['case_key']}: expected={result['expected_disposition']} "
            f"observed={result['parsed_model_content']['disposition']} "
            f"match={result['expectation_match']} "
            f"elapsed={result['elapsed_seconds']:.3f}s"
        )
        print(f"  explanation: {result['parsed_model_content']['explanation']}")
    print("capability_executed: False")
    print(f"output: {_OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
