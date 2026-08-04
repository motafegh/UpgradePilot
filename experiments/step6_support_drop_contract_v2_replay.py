#!/usr/bin/env python3
"""Replay the committed Step 6D Gemma outputs under semantic contract v2.

This experiment performs no HTTP requests and makes no new model calls. It reuses the
exact 25 structured model outputs preserved by the first Step 6D run and changes only the
contract interpretation that was shown to be redundant:

- candidate presence now derives ``candidates_available`` mechanically;
- the historical state choice is preserved only for zero-candidate outputs, where the
  no-relevant versus unresolved distinction is genuinely semantic.

The replay therefore answers one narrow counterfactual question before a new live model
run is justified: how much of the original 14/25 result was caused solely by duplicated
state encoding?
"""

from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path
from typing import Any

from experiments.step6_support_drop_contract_v2 import (
    CONTRACT_VERSION,
    candidate_result_from_v2_selection,
    selection_from_v1_structured_output,
)
from experiments.step6_support_drop_evaluation import (
    CRITICAL_REPEAT_CASE_IDS,
    TOTAL_CRITICAL_TRIALS,
    _diagnostic_flags,
    _load_corpus,
    _outcome_signature,
    _semantic_oracle_errors,
    _trust_matches_oracle,
)
from experiments.step6_support_drop_smoke import (
    _smoke_authority,
    _trust_result_summary,
)
from upgradepilot.upstream.claim import validate_support_drop_candidates


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_PATH = (
    ROOT
    / "working-memory"
    / "evidence"
    / "2026-08-03-step6d"
    / "support-drop-evaluation.json"
)
DEFAULT_OUTPUT_PATH = Path("/tmp/upgradepilot-step6d-contract-v2-replay.json")


def _load_v1_evidence(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or not isinstance(value.get("runs"), list):
        raise RuntimeError("The Step 6D evidence file had an unexpected structure.")
    return value


def _case_index() -> tuple[dict[str, object], dict[str, dict[str, object]]]:
    context, cases = _load_corpus()
    return context, {str(case["id"]): case for case in cases}


def _replay_one(
    context: dict[str, object],
    case: dict[str, object],
    historical: dict[str, Any],
) -> dict[str, object]:
    replay: dict[str, object] = {
        "case_id": str(case["id"]),
        "repetition": historical.get("repetition"),
        "critical_repeat": historical.get("critical_repeat"),
        "historical_pass": historical.get("pass"),
        "historical_mapping_pass": historical.get("mapping_pass"),
        "historical_semantic_pass": historical.get("semantic_pass"),
        "historical_trust_oracle_pass": historical.get("trust_oracle_pass"),
        "historical_finish_reason": historical.get("finish_reason"),
        "historical_structured_content": historical.get("structured_content"),
    }

    structured = historical.get("structured_content")
    if not isinstance(structured, dict):
        replay.update(
            {
                "replay_pass": False,
                "exception_type": "MissingStructuredContent",
                "exception": "Historical run contained no structured model content.",
            }
        )
        return replay

    try:
        selection = selection_from_v1_structured_output(structured)
        replay["contract_v2_selection"] = selection
        source_text = str(case["text"])
        candidate_result = candidate_result_from_v2_selection(
            context,
            source_text,
            selection,
        )
        replay["candidate_result"] = asdict(candidate_result)
        replay["mapping_pass"] = True

        semantic_errors = _semantic_oracle_errors(case, candidate_result)
        replay["semantic_errors"] = semantic_errors
        replay["diagnostic_flags"] = _diagnostic_flags(case, candidate_result)
        replay["semantic_pass"] = not semantic_errors

        authority = _smoke_authority(context, source_text)
        trust_result = validate_support_drop_candidates(authority, candidate_result)
        replay["trust_result"] = _trust_result_summary(trust_result)
        replay["trust_oracle_pass"] = _trust_matches_oracle(case, trust_result)
        replay["finish_pass"] = historical.get("finish_reason") != "length"
        replay["replay_pass"] = bool(
            replay["semantic_pass"]
            and replay["trust_oracle_pass"]
            and replay["finish_pass"]
        )
    except Exception as exc:
        replay.update(
            {
                "mapping_pass": False,
                "semantic_pass": False,
                "trust_oracle_pass": False,
                "replay_pass": False,
                "exception_type": type(exc).__name__,
                "exception": str(exc),
            }
        )

    return replay


def _failure_class(run: dict[str, object]) -> str:
    if run.get("mapping_pass") is not True:
        return "mapping_failure"
    flags = run.get("diagnostic_flags")
    if isinstance(flags, dict):
        if flags.get("false_positive"):
            return "false_positive"
        if flags.get("false_negative"):
            return "false_negative"
        if flags.get("wrong_python_line"):
            return "wrong_python_line"
        if flags.get("wrong_introduced_release"):
            return "wrong_introduced_release"
        if flags.get("wrong_source_selection"):
            return "wrong_source_selection"
        if flags.get("state_mismatch"):
            return "zero_candidate_state_mismatch"
    if run.get("trust_oracle_pass") is not True:
        return "trust_oracle_mismatch"
    if run.get("finish_pass") is not True:
        return "finish_failure"
    return "other_semantic_failure"


def _write_json(path: Path, value: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False, default=str) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    input_path = DEFAULT_INPUT_PATH
    output_path = DEFAULT_OUTPUT_PATH

    print("B2 Step 6D contract-v2 offline replay")
    print("model calls: 0")
    print(f"historical evidence: {input_path}")
    print(f"output: {output_path}")
    print()

    evidence = _load_v1_evidence(input_path)
    context, cases = _case_index()
    historical_runs = evidence["runs"]
    assert isinstance(historical_runs, list)

    replay_runs: list[dict[str, object]] = []
    for historical in historical_runs:
        if not isinstance(historical, dict):
            raise RuntimeError("Historical evidence contained a non-object run.")
        case_id = str(historical.get("case_id"))
        case = cases.get(case_id)
        if case is None:
            raise RuntimeError(f"Historical run referenced unknown case {case_id!r}.")
        replay = _replay_one(context, case, historical)
        replay_runs.append(replay)
        status = "PASS" if replay.get("replay_pass") else "FAIL"
        derived = replay.get("candidate_result")
        state = derived.get("state") if isinstance(derived, dict) else None
        print(f"{status} {case_id} r{historical.get('repetition')} state={state!r}")
        for error in replay.get("semantic_errors", []):
            print(f"  semantic: {error}")

    passed = sum(1 for run in replay_runs if run.get("replay_pass") is True)
    failed = len(replay_runs) - passed
    historical_passed = sum(
        1 for run in historical_runs if isinstance(run, dict) and run.get("pass") is True
    )
    rescued = sum(
        1
        for old, new in zip(historical_runs, replay_runs)
        if isinstance(old, dict)
        and old.get("pass") is not True
        and new.get("replay_pass") is True
    )

    failure_classes: dict[str, int] = {}
    for run in replay_runs:
        if run.get("replay_pass") is True:
            continue
        key = _failure_class(run)
        failure_classes[key] = failure_classes.get(key, 0) + 1

    repeat_consistency: dict[str, bool] = {}
    for case_id in CRITICAL_REPEAT_CASE_IDS:
        matching = [run for run in replay_runs if run["case_id"] == case_id]
        if len(matching) == TOTAL_CRITICAL_TRIALS:
            repeat_consistency[case_id] = len(
                {_outcome_signature(run) for run in matching}
            ) == 1
        else:
            repeat_consistency[case_id] = False

    summary = {
        "contract_version": CONTRACT_VERSION,
        "counterfactual_replay": True,
        "new_model_calls": 0,
        "historical_runs": len(historical_runs),
        "historical_passed": historical_passed,
        "replay_passed": passed,
        "replay_failed": failed,
        "historical_failures_rescued": rescued,
        "failure_classes": failure_classes,
        "critical_repeat_consistency": repeat_consistency,
        "all_critical_repeats_consistent": all(repeat_consistency.values()),
    }
    result = {
        "input_evidence": str(input_path),
        "contract_version": CONTRACT_VERSION,
        "method": (
            "Offline deterministic replay of historical structured model outputs; "
            "candidate-bearing v1 states are ignored and candidates_available is derived "
            "from candidate presence. Zero-candidate v1 state choices are preserved."
        ),
        "runs": replay_runs,
        "summary": summary,
    }
    _write_json(output_path, result)

    print("\nSTEP 6D CONTRACT-V2 REPLAY SUMMARY")
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print(f"output: {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
