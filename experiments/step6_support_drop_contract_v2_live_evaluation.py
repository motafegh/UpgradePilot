#!/usr/bin/env python3
"""Run the Step 6D live semantic evaluation with contract v2.

This experiment keeps the frozen corpus/oracle and the existing Step 2 trust boundary
unchanged. It changes only the model-facing representation demonstrated by the offline
replay to be non-redundant:

- the model returns candidate selections;
- ``candidates_available`` is derived mechanically from candidate presence;
- only the zero-candidate distinction (unresolved vs no relevant claim) remains semantic.

Two scores are reported deliberately:

1. strict oracle score — preserves the frozen exact state classification;
2. adoption-safety score — requires exact positive candidates and safe abstention for
   every zero-candidate oracle case, because both no-support-drop and candidate-unresolved
   stop target-Python activation in the current product data flow.

Automatic retries are disabled. This is experiment code, not product runtime code.
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from experiments.step6_support_drop_contract_v2 import (
    CONTRACT_VERSION,
    SYSTEM_PROMPT_V2,
    candidate_result_from_v2_selection,
)
from experiments.step6_support_drop_evaluation import (
    CRITICAL_REPEAT_CASE_IDS,
    TOTAL_CRITICAL_TRIALS,
    _diagnostic_flags,
    _load_corpus,
    _outcome_signature,
    _planned_runs,
    _semantic_oracle_errors,
    _trust_matches_oracle,
)
from experiments.step6_support_drop_smoke import (
    DEFAULT_BASE_URL,
    DEFAULT_MODEL,
    MAX_COMPLETION_TOKENS,
    _available_model_ids,
    _indexed_source_lines,
    _parse_inner_content,
    _post_completion,
    _python_line_tokens,
    _smoke_authority,
    _trust_result_summary,
)
from upgradepilot.upstream.claim import (
    UpstreamSupportDropClaimProblem,
    validate_support_drop_candidates,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_PATH = (
    ROOT
    / "working-memory"
    / "evidence"
    / "2026-08-03-step6d"
    / "contract-v2-live-evaluation.json"
)
_SAFE_ABSTENTION_STATES = {"no_support_drop_claim", "candidate_unresolved"}


def _response_schema(
    context: dict[str, object],
    source_text: str,
) -> dict[str, object]:
    crossed_versions = [str(item) for item in context["crossed_versions"]]
    line_ids = [
        line_id
        for line_id, line, _, _ in _indexed_source_lines(source_text)
        if line
    ]
    python_lines = list(_python_line_tokens(source_text))
    if not line_ids:
        raise RuntimeError("The evaluation source contained no selectable source lines.")

    candidate_properties: dict[str, object] = {
        "python_line": (
            {"type": "string", "enum": python_lines}
            if python_lines
            else {"type": "string"}
        ),
        "introduced_in_version": {
            "type": "string",
            "enum": crossed_versions,
        },
        "source_line_id": {"type": "string", "enum": line_ids},
    }
    candidates_schema: dict[str, object] = {
        "type": "array",
        "items": {
            "type": "object",
            "additionalProperties": False,
            "properties": candidate_properties,
            "required": [
                "python_line",
                "introduced_in_version",
                "source_line_id",
            ],
        },
    }
    if not python_lines:
        candidates_schema["maxItems"] = 0

    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "candidates": candidates_schema,
            "unresolved_if_no_candidates": {"type": "boolean"},
            "detail": {"type": "string"},
        },
        "required": ["candidates", "unresolved_if_no_candidates", "detail"],
    }


def _request_payload(
    context: dict[str, object],
    case: dict[str, object],
    model: str,
) -> dict[str, object]:
    source_text = str(case["text"])
    rendered_lines = "\n".join(
        f"{line_id} | {line}"
        for line_id, line, _, _ in _indexed_source_lines(source_text)
    )
    python_tokens = _python_line_tokens(source_text)
    rendered_python_tokens = ", ".join(python_tokens) if python_tokens else "none"

    user_prompt = (
        "Trusted extraction context:\n"
        f"package: {context['package']}\n"
        f"old_version: {context['old_version']}\n"
        f"proposed_version: {context['proposed_version']}\n"
        "crossed_release_versions: "
        + ", ".join(str(item) for item in context["crossed_versions"])
        + "\n"
        f"explicit_python_line_tokens: {rendered_python_tokens}\n\n"
        "Untrusted release text with deterministic source-line IDs:\n"
        "--- BEGIN RELEASE TEXT ---\n"
        f"{rendered_lines}\n"
        "--- END RELEASE TEXT ---\n\n"
        "Return only the bounded current Python support-drop selection described by "
        "the system rules."
    )
    return {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT_V2},
            {"role": "user", "content": user_prompt},
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "upgradepilot_step6_support_drop_contract_v2",
                "strict": True,
                "schema": _response_schema(context, source_text),
            },
        },
        "temperature": 0,
        "seed": 0,
        "max_tokens": MAX_COMPLETION_TOKENS,
        "stream": False,
    }


def _adoption_safety_errors(
    case: dict[str, object],
    candidate_result: object,
    trust_result: object,
) -> list[str]:
    """Score the Step 6 adoption gate without erasing strict diagnostic differences."""

    expected_candidates = case.get("candidates")
    if not isinstance(expected_candidates, list):
        raise RuntimeError(f"Case {case.get('id')!r} had an invalid candidate oracle.")

    actual_candidates = getattr(candidate_result, "candidates", None)
    if not isinstance(actual_candidates, tuple):
        return ["candidate result did not expose a candidate tuple"]

    if expected_candidates:
        strict = _semantic_oracle_errors(case, candidate_result)
        if strict:
            return strict
        if not _trust_matches_oracle(case, trust_result):
            return ["trusted result did not match the frozen positive/multiple-claim oracle"]
        return []

    errors: list[str] = []
    if actual_candidates:
        errors.append("zero-candidate oracle case produced one or more candidates")
    if not isinstance(trust_result, UpstreamSupportDropClaimProblem):
        errors.append("zero-candidate oracle case produced a grounded claim")
    elif trust_result.state not in _SAFE_ABSTENTION_STATES:
        errors.append(
            f"zero-candidate oracle case stopped as {trust_result.state!r}, not a safe abstention state"
        )
    return errors


def _write_json(path: Path, value: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False, default=str) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    base_url = os.environ.get(
        "UPGRADEPILOT_LM_STUDIO_BASE_URL",
        DEFAULT_BASE_URL,
    ).rstrip("/")
    model = os.environ.get("UPGRADEPILOT_LM_STUDIO_MODEL", DEFAULT_MODEL)
    output_path = Path(
        os.environ.get("UPGRADEPILOT_STEP6D_V2_OUTPUT", str(DEFAULT_OUTPUT_PATH))
    )

    context, cases = _load_corpus()
    planned = _planned_runs(cases)
    evidence: dict[str, object] = {
        "started_at": datetime.now(timezone.utc).isoformat(),
        "contract_version": CONTRACT_VERSION,
        "base_url": base_url,
        "model": model,
        "automatic_retries": False,
        "temperature": 0,
        "seed": 0,
        "max_completion_tokens": MAX_COMPLETION_TOKENS,
        "case_count": len(cases),
        "planned_run_count": len(planned),
        "critical_repeat_case_ids": CRITICAL_REPEAT_CASE_IDS,
        "critical_trials_per_case": TOTAL_CRITICAL_TRIALS,
        "runs": [],
    }

    print("B2 Step 6D contract-v2 live semantic evaluation")
    print("control plane: WSL")
    print(f"LM Studio base URL: {base_url}")
    print(f"model: {model}")
    print(f"contract version: {CONTRACT_VERSION}")
    print(f"frozen cases: {len(cases)}")
    print(f"planned model calls: {len(planned)}")
    print(f"evidence file: {output_path}")
    print()

    try:
        available_ids = _available_model_ids(base_url)
    except Exception as exc:
        evidence.update(
            {
                "completed": False,
                "stop_reason": "model_inventory_failure",
                "exception_type": type(exc).__name__,
                "exception": str(exc),
            }
        )
        _write_json(output_path, evidence)
        print(f"EVALUATION STOP: model inventory failed: {type(exc).__name__}: {exc}")
        return 2

    evidence["available_model_ids"] = available_ids
    if model not in available_ids:
        evidence.update({"completed": False, "stop_reason": "selected_model_unavailable"})
        _write_json(output_path, evidence)
        print(f"EVALUATION STOP: selected model {model!r} is unavailable")
        return 2

    runs: list[dict[str, object]] = []
    transport_stop = False

    for case, repetition in planned:
        case_id = str(case["id"])
        source_text = str(case["text"])
        run: dict[str, object] = {
            "case_id": case_id,
            "repetition": repetition,
            "critical_repeat": case_id in CRITICAL_REPEAT_CASE_IDS,
            "started_at": datetime.now(timezone.utc).isoformat(),
        }
        print(f"RUN {case_id} r{repetition}")

        payload = _request_payload(context, case, model)
        run["request"] = payload
        try:
            outer, elapsed = _post_completion(base_url, payload)
        except Exception as exc:
            run.update(
                {
                    "transport_pass": False,
                    "strict_pass": False,
                    "adoption_safety_pass": False,
                    "exception_type": type(exc).__name__,
                    "exception": str(exc),
                }
            )
            runs.append(run)
            print(f"  TRANSPORT FAIL: {type(exc).__name__}: {exc}")
            transport_stop = True
            break

        run["transport_pass"] = True
        run["latency_seconds"] = round(elapsed, 6)
        run["outer_response"] = outer
        choices = outer.get("choices")
        first_choice = (
            choices[0]
            if isinstance(choices, list)
            and choices
            and isinstance(choices[0], dict)
            else {}
        )
        finish_reason = first_choice.get("finish_reason")
        run["finish_reason"] = finish_reason
        run["usage"] = outer.get("usage")

        try:
            selection = _parse_inner_content(outer)
            run["structured_selection"] = selection
            run["structured_json_pass"] = True
            candidate_result = candidate_result_from_v2_selection(
                context,
                source_text,
                selection,
            )
            run["candidate_result"] = asdict(candidate_result)
            run["mapping_pass"] = True
        except Exception as exc:
            run.update(
                {
                    "structured_json_pass": False,
                    "mapping_pass": False,
                    "strict_semantic_pass": False,
                    "strict_trust_pass": False,
                    "strict_pass": False,
                    "adoption_safety_pass": False,
                    "exception_type": type(exc).__name__,
                    "exception": str(exc),
                }
            )
            runs.append(run)
            print(
                f"  FAIL {elapsed:.3f}s finish={finish_reason!r} "
                f"mapping={type(exc).__name__}: {exc}"
            )
            continue

        strict_errors = _semantic_oracle_errors(case, candidate_result)
        flags = _diagnostic_flags(case, candidate_result)
        run["strict_semantic_errors"] = strict_errors
        run["diagnostic_flags"] = flags
        run["strict_semantic_pass"] = not strict_errors

        authority = _smoke_authority(context, source_text)
        trust_result = validate_support_drop_candidates(authority, candidate_result)
        run["trust_result"] = _trust_result_summary(trust_result)
        run["strict_trust_pass"] = _trust_matches_oracle(case, trust_result)
        run["finish_pass"] = finish_reason != "length"
        run["strict_pass"] = bool(
            run["strict_semantic_pass"]
            and run["strict_trust_pass"]
            and run["finish_pass"]
        )

        safety_errors = _adoption_safety_errors(case, candidate_result, trust_result)
        run["adoption_safety_errors"] = safety_errors
        run["adoption_safety_pass"] = bool(not safety_errors and run["finish_pass"])
        runs.append(run)

        strict_status = "PASS" if run["strict_pass"] else "FAIL"
        safety_status = "PASS" if run["adoption_safety_pass"] else "FAIL"
        print(
            f"  strict={strict_status} safety={safety_status} {elapsed:.3f}s "
            f"finish={finish_reason!r} state={candidate_result.state!r} "
            f"trust={run['trust_result']}"
        )
        for error in strict_errors:
            print(f"    strict: {error}")
        for error in safety_errors:
            print(f"    safety: {error}")

    evidence["runs"] = runs
    evidence["completed_at"] = datetime.now(timezone.utc).isoformat()
    evidence["completed"] = not transport_stop and len(runs) == len(planned)
    if transport_stop:
        evidence["stop_reason"] = "completion_transport_failure"

    strict_passed = sum(1 for run in runs if run.get("strict_pass") is True)
    safety_passed = sum(1 for run in runs if run.get("adoption_safety_pass") is True)

    strict_repeat_consistency: dict[str, bool] = {}
    safety_repeat_consistency: dict[str, bool] = {}
    for case_id in CRITICAL_REPEAT_CASE_IDS:
        matching = [run for run in runs if run["case_id"] == case_id]
        if len(matching) == TOTAL_CRITICAL_TRIALS:
            strict_repeat_consistency[case_id] = len(
                {_outcome_signature(run) for run in matching}
            ) == 1
            safety_repeat_consistency[case_id] = len(
                {
                    json.dumps(
                        {
                            "candidate_result": run.get("candidate_result"),
                            "adoption_safety_pass": run.get("adoption_safety_pass"),
                        },
                        sort_keys=True,
                        ensure_ascii=False,
                    )
                    for run in matching
                }
            ) == 1
        else:
            strict_repeat_consistency[case_id] = False
            safety_repeat_consistency[case_id] = False

    summary = {
        "contract_version": CONTRACT_VERSION,
        "completed": evidence["completed"],
        "runs_completed": len(runs),
        "runs_planned": len(planned),
        "strict_oracle_passed": strict_passed,
        "strict_oracle_failed": len(runs) - strict_passed,
        "adoption_safety_passed": safety_passed,
        "adoption_safety_failed": len(runs) - safety_passed,
        "strict_critical_repeat_consistency": strict_repeat_consistency,
        "safety_critical_repeat_consistency": safety_repeat_consistency,
        "all_strict_critical_repeats_consistent": all(strict_repeat_consistency.values()),
        "all_safety_critical_repeats_consistent": all(safety_repeat_consistency.values()),
        "strict_all_runs_pass": bool(evidence["completed"] and strict_passed == len(runs)),
        "adoption_safety_all_runs_pass": bool(
            evidence["completed"] and safety_passed == len(runs)
        ),
    }
    evidence["summary"] = summary
    _write_json(output_path, evidence)

    print("\nSTEP 6D CONTRACT-V2 LIVE SUMMARY")
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print(f"evidence file: {output_path}")

    if not evidence["completed"]:
        print("\nSTEP 6D CONTRACT-V2 LIVE: INCOMPLETE")
        return 2
    if summary["adoption_safety_all_runs_pass"]:
        print("\nSTEP 6D CONTRACT-V2 LIVE: COMPLETE / ADOPTION-SAFETY GATE PASSED")
        return 0
    print("\nSTEP 6D CONTRACT-V2 LIVE: COMPLETE / SAFETY FAILURES RECORDED")
    return 2


if __name__ == "__main__":
    sys.exit(main())
