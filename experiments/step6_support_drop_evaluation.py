#!/usr/bin/env python3
"""Score the Step 6 support-drop extractor against the frozen semantic corpus.

This is experiment code, not UpgradePilot product runtime code.

Step 6C proved that one S001 case can travel through the complete local semantic
boundary. Step 6D asks a different question: whether the same bounded deployment behaves
correctly across the frozen positive, negative, ambiguous, adversarial/noisy, and repeated
critical controls required by the Step 6 plan.

The model remains responsible only for semantic selection:

- candidate state;
- explicit Python X.Y line;
- crossed release that introduces the claim;
- deterministic source-line ID.

Dependency identity, category/direction, source authority, exact source quote, and quote
offsets remain deterministic. Automatic retries remain disabled.
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from experiments.step6_support_drop_smoke import (
    CORPUS_PATH,
    DEFAULT_BASE_URL,
    DEFAULT_MODEL,
    MAX_COMPLETION_TOKENS,
    SYSTEM_PROMPT,
    _available_model_ids,
    _candidate_result_from_model,
    _indexed_source_lines,
    _parse_inner_content,
    _post_completion,
    _python_line_tokens,
    _smoke_authority,
    _trust_result_summary,
)
from upgradepilot.upstream_claim import (
    CandidateUpstreamClaimResult,
    GroundedPythonSupportDropClaim,
    UpstreamSupportDropClaimProblem,
    validate_support_drop_candidates,
)


DEFAULT_OUTPUT_PATH = Path("/tmp/upgradepilot-step6d-support-drop-evaluation.json")
CRITICAL_REPEAT_CASE_IDS = (
    "support_added_control",
    "negated_drop_control",
    "future_drop_control",
    "raised_minimum_without_explicit_dropped_line",
    "s001_exact_excerpt",
)
TOTAL_CRITICAL_TRIALS = 3


def _load_corpus() -> tuple[dict[str, object], tuple[dict[str, object], ...]]:
    corpus = json.loads(CORPUS_PATH.read_text(encoding="utf-8"))
    context = corpus.get("context")
    cases = corpus.get("cases")
    if not isinstance(context, dict) or not isinstance(cases, list):
        raise RuntimeError("The frozen Step 6 corpus had an unexpected structure.")
    typed_cases = tuple(case for case in cases if isinstance(case, dict))
    if len(typed_cases) != len(cases):
        raise RuntimeError("The frozen Step 6 corpus contained a non-object case.")
    return context, typed_cases


def _evaluation_response_schema(
    context: dict[str, object],
    source_text: str,
) -> dict[str, object]:
    """Build a strict selection schema, including true no-Python controls."""

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
        # A source with no explicit Python X.Y token cannot legally produce a candidate.
        candidates_schema["maxItems"] = 0

    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "state": {
                "type": "string",
                "enum": ["candidates_available", "no_relevant_claim", "unresolved"],
            },
            "candidates": candidates_schema,
            "detail": {"type": "string"},
        },
        "required": ["state", "candidates", "detail"],
    }


def _evaluation_request_payload(
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
        "Extract only the bounded current Python support-drop candidate described by the system rules. "
        "Use an empty detail string when no explanation is needed."
    )
    return {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "upgradepilot_step6_support_drop_evaluation",
                "strict": True,
                "schema": _evaluation_response_schema(context, source_text),
            },
        },
        "temperature": 0,
        "seed": 0,
        "max_tokens": MAX_COMPLETION_TOKENS,
        "stream": False,
    }


def _planned_runs(
    cases: tuple[dict[str, object], ...],
) -> tuple[tuple[dict[str, object], int], ...]:
    """Run every case once, then repeat the decision-critical controls twice."""

    runs: list[tuple[dict[str, object], int]] = [(case, 1) for case in cases]
    by_id = {str(case["id"]): case for case in cases}
    missing = set(CRITICAL_REPEAT_CASE_IDS) - set(by_id)
    if missing:
        raise RuntimeError(
            "Frozen corpus is missing required critical repeat cases: "
            + ", ".join(sorted(missing))
        )
    for repetition in range(2, TOTAL_CRITICAL_TRIALS + 1):
        for case_id in CRITICAL_REPEAT_CASE_IDS:
            runs.append((by_id[case_id], repetition))
    return tuple(runs)


def _candidate_signature(candidate: object) -> tuple[str, str, str] | None:
    python_line = getattr(candidate, "python_line", None)
    introduced = getattr(candidate, "introduced_in_version", None)
    quote = getattr(candidate, "source_quote", None)
    if not all(isinstance(item, str) for item in (python_line, introduced, quote)):
        return None
    return python_line, introduced, quote


def _semantic_oracle_errors(
    case: dict[str, object],
    candidate_result: CandidateUpstreamClaimResult,
) -> list[str]:
    """Compare meaning while treating candidate ordering as non-semantic."""

    errors: list[str] = []
    expected_state = str(case["expected_candidate_state"])
    if candidate_result.state != expected_state:
        errors.append(
            f"candidate state was {candidate_result.state!r}; expected {expected_state!r}"
        )

    expected_candidates = case.get("candidates")
    if not isinstance(expected_candidates, list):
        raise RuntimeError(f"Case {case.get('id')!r} had an invalid candidate oracle.")

    expected_signatures = sorted(
        (
            str(candidate["python_line"]),
            str(candidate["introduced_in_version"]),
            str(candidate["source_quote"]),
        )
        for candidate in expected_candidates
        if isinstance(candidate, dict)
    )
    actual_signatures = sorted(
        signature
        for candidate in candidate_result.candidates
        if (signature := _candidate_signature(candidate)) is not None
    )
    if actual_signatures != expected_signatures:
        errors.append(
            f"candidate identities were {actual_signatures!r}; expected {expected_signatures!r}"
        )
    return errors


def _trust_matches_oracle(case: dict[str, object], result: object) -> bool:
    expected = str(case["expected_validator_state"])
    if expected == "grounded":
        if not isinstance(result, GroundedPythonSupportDropClaim):
            return False
        expected_candidates = case["candidates"]
        if not isinstance(expected_candidates, list) or len(expected_candidates) != 1:
            return False
        oracle = expected_candidates[0]
        return (
            isinstance(oracle, dict)
            and result.python_line == str(oracle["python_line"])
            and result.introduced_in_version == str(oracle["introduced_in_version"])
        )
    return isinstance(result, UpstreamSupportDropClaimProblem) and result.state == expected


def _diagnostic_flags(
    case: dict[str, object],
    candidate_result: CandidateUpstreamClaimResult,
) -> dict[str, bool]:
    expected_candidates = case["candidates"]
    assert isinstance(expected_candidates, list)
    expected_has_candidates = bool(expected_candidates)
    actual_has_candidates = bool(candidate_result.candidates)

    expected_python = sorted(
        str(item["python_line"])
        for item in expected_candidates
        if isinstance(item, dict)
    )
    actual_python = sorted(item.python_line for item in candidate_result.candidates)
    expected_release = sorted(
        str(item["introduced_in_version"])
        for item in expected_candidates
        if isinstance(item, dict)
    )
    actual_release = sorted(
        item.introduced_in_version for item in candidate_result.candidates
    )
    expected_quotes = sorted(
        str(item["source_quote"])
        for item in expected_candidates
        if isinstance(item, dict)
    )
    actual_quotes = sorted(item.source_quote for item in candidate_result.candidates)

    return {
        "state_mismatch": candidate_result.state != str(case["expected_candidate_state"]),
        "false_positive": not expected_has_candidates and actual_has_candidates,
        "false_negative": expected_has_candidates and not actual_has_candidates,
        "wrong_python_line": actual_has_candidates and actual_python != expected_python,
        "wrong_introduced_release": actual_has_candidates and actual_release != expected_release,
        "wrong_source_selection": actual_has_candidates and actual_quotes != expected_quotes,
    }


def _outcome_signature(run: dict[str, object]) -> str:
    if not run.get("mapping_pass"):
        return "mapping_failure"
    candidate_result = run.get("candidate_result")
    trust_result = run.get("trust_result")
    return json.dumps(
        {
            "candidate_result": candidate_result,
            "trust_result": trust_result,
            "semantic_pass": run.get("semantic_pass"),
        },
        sort_keys=True,
        ensure_ascii=False,
    )


def _write_output(path: Path, value: dict[str, object]) -> None:
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
        os.environ.get("UPGRADEPILOT_STEP6D_OUTPUT", str(DEFAULT_OUTPUT_PATH))
    )

    context, cases = _load_corpus()
    planned = _planned_runs(cases)
    evidence: dict[str, object] = {
        "started_at": datetime.now(timezone.utc).isoformat(),
        "base_url": base_url,
        "model": model,
        "automatic_retries": False,
        "temperature": 0,
        "seed": 0,
        "max_completion_tokens": MAX_COMPLETION_TOKENS,
        "corpus_path": str(CORPUS_PATH),
        "case_count": len(cases),
        "planned_run_count": len(planned),
        "critical_repeat_case_ids": CRITICAL_REPEAT_CASE_IDS,
        "critical_trials_per_case": TOTAL_CRITICAL_TRIALS,
        "runs": [],
    }

    print("B2 Step 6D support-drop semantic evaluation")
    print("control plane: WSL")
    print(f"LM Studio base URL: {base_url}")
    print(f"model: {model}")
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
        _write_output(output_path, evidence)
        print(f"EVALUATION STOP: model inventory failed: {type(exc).__name__}: {exc}")
        return 2

    evidence["available_model_ids"] = available_ids
    if model not in available_ids:
        evidence.update(
            {
                "completed": False,
                "stop_reason": "selected_model_unavailable",
            }
        )
        _write_output(output_path, evidence)
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

        payload = _evaluation_request_payload(context, case, model)
        run["request"] = payload
        try:
            outer, elapsed = _post_completion(base_url, payload)
        except Exception as exc:
            run.update(
                {
                    "transport_pass": False,
                    "pass": False,
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
            inner = _parse_inner_content(outer)
            run["structured_content"] = inner
            run["structured_json_pass"] = True
            candidate_result = _candidate_result_from_model(context, source_text, inner)
            run["candidate_result"] = asdict(candidate_result)
            run["mapping_pass"] = True
        except Exception as exc:
            run.update(
                {
                    "structured_json_pass": False,
                    "mapping_pass": False,
                    "semantic_pass": False,
                    "trust_oracle_pass": False,
                    "pass": False,
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

        semantic_errors = _semantic_oracle_errors(case, candidate_result)
        flags = _diagnostic_flags(case, candidate_result)
        run["semantic_errors"] = semantic_errors
        run["diagnostic_flags"] = flags
        run["semantic_pass"] = not semantic_errors

        authority = _smoke_authority(context, source_text)
        trust_result = validate_support_drop_candidates(authority, candidate_result)
        run["trust_result"] = _trust_result_summary(trust_result)
        run["trust_oracle_pass"] = _trust_matches_oracle(case, trust_result)
        run["finish_pass"] = finish_reason != "length"
        run["pass"] = bool(
            run["semantic_pass"]
            and run["trust_oracle_pass"]
            and run["finish_pass"]
        )
        runs.append(run)

        status = "PASS" if run["pass"] else "FAIL"
        print(
            f"  {status} {elapsed:.3f}s finish={finish_reason!r} "
            f"state={candidate_result.state!r} trust={run['trust_result']}"
        )
        if semantic_errors:
            for error in semantic_errors:
                print(f"    semantic: {error}")

    evidence["runs"] = runs
    evidence["completed_at"] = datetime.now(timezone.utc).isoformat()
    evidence["completed"] = not transport_stop and len(runs) == len(planned)
    if transport_stop:
        evidence["stop_reason"] = "completion_transport_failure"

    passed = sum(1 for run in runs if run.get("pass") is True)
    failed = len(runs) - passed
    semantic_passed = sum(1 for run in runs if run.get("semantic_pass") is True)
    trust_passed = sum(1 for run in runs if run.get("trust_oracle_pass") is True)

    repeat_consistency: dict[str, bool] = {}
    for case_id in CRITICAL_REPEAT_CASE_IDS:
        matching = [run for run in runs if run["case_id"] == case_id]
        if len(matching) == TOTAL_CRITICAL_TRIALS:
            repeat_consistency[case_id] = len(
                {_outcome_signature(run) for run in matching}
            ) == 1
        else:
            repeat_consistency[case_id] = False

    summary = {
        "completed": evidence["completed"],
        "runs_completed": len(runs),
        "runs_planned": len(planned),
        "passed": passed,
        "failed": failed,
        "semantic_passed": semantic_passed,
        "trust_oracle_passed": trust_passed,
        "critical_repeat_consistency": repeat_consistency,
        "all_critical_repeats_consistent": all(repeat_consistency.values()),
        "all_runs_pass": bool(evidence["completed"] and failed == 0),
    }
    evidence["summary"] = summary
    _write_output(output_path, evidence)

    print("\nSTEP 6D SUMMARY")
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print(f"evidence file: {output_path}")

    if summary["all_runs_pass"]:
        print("\nSTEP 6D EVALUATION: COMPLETE / ALL RUNS PASS")
        return 0
    if evidence["completed"]:
        print("\nSTEP 6D EVALUATION: COMPLETE / FAILURES RECORDED")
        return 2
    print("\nSTEP 6D EVALUATION: INCOMPLETE")
    return 2


if __name__ == "__main__":
    sys.exit(main())
