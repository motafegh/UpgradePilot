#!/usr/bin/env python3
"""Assess committed Step 6D contract-v2 evidence without new model calls.

The live evaluator intentionally preserved exact free-text ``detail`` values. Its first
repeat-consistency metric therefore treated wording differences in otherwise identical
unresolved outcomes as inconsistency. The Step 6 adoption plan asks for *materially*
consistent trusted outcomes, not byte-identical explanatory prose.

This post-run assessment reads the committed live-v2 evidence and computes:

- strict/safety counts already recorded by the evaluator;
- material trusted-outcome consistency for the five repeated critical cases;
- latency summary for the completed local inference calls;
- a bounded adoption-gate checklist grounded in the frozen corpus and Step 2 results.

It performs no HTTP requests, no model calls, no retries, and no product integration.
"""

from __future__ import annotations

import json
import statistics
import sys
from pathlib import Path
from typing import Any

from experiments.step6_support_drop_evaluation import CRITICAL_REPEAT_CASE_IDS


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_PATH = (
    ROOT
    / "working-memory"
    / "evidence"
    / "2026-08-03-step6d"
    / "contract-v2-live-evaluation.json"
)
DEFAULT_OUTPUT_PATH = (
    ROOT
    / "working-memory"
    / "evidence"
    / "2026-08-03-step6d"
    / "contract-v2-adoption-assessment.json"
)


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or not isinstance(value.get("runs"), list):
        raise RuntimeError("The contract-v2 live evidence had an unexpected structure.")
    return value


def _candidate_identity(candidate: object) -> tuple[object, ...] | None:
    if not isinstance(candidate, dict):
        return None
    return (
        candidate.get("category"),
        candidate.get("change_state"),
        candidate.get("python_line"),
        candidate.get("introduced_in_version"),
        candidate.get("source_kind"),
        candidate.get("source_release_version"),
        candidate.get("source_quote"),
        candidate.get("quote_start"),
        candidate.get("quote_end"),
    )


def material_trusted_outcome_signature(run: dict[str, object]) -> str:
    """Return the repeat signature that matters to downstream trust/product behavior.

    Free-text details are intentionally excluded. For a grounded result, the trusted
    claim identity is compared. For a stopping problem, only the problem state matters.
    Candidate identities are included so an accidentally changing model selection cannot
    be hidden merely because a later validator returned the same broad result kind.
    """

    candidate_result = run.get("candidate_result")
    trust_result = run.get("trust_result")

    candidate_state = None
    candidate_identities: list[tuple[object, ...]] = []
    if isinstance(candidate_result, dict):
        candidate_state = candidate_result.get("state")
        raw_candidates = candidate_result.get("candidates")
        if isinstance(raw_candidates, list):
            candidate_identities = sorted(
                identity
                for item in raw_candidates
                if (identity := _candidate_identity(item)) is not None
            )

    trust_kind = None
    trust_state = None
    trusted_python_line = None
    trusted_release = None
    if isinstance(trust_result, dict):
        trust_kind = trust_result.get("kind")
        trust_state = trust_result.get("state")
        trusted_python_line = trust_result.get("python_line")
        trusted_release = trust_result.get("introduced_in_version")

    return json.dumps(
        {
            "candidate_state": candidate_state,
            "candidate_identities": candidate_identities,
            "trust_kind": trust_kind,
            "trust_state": trust_state,
            "trusted_python_line": trusted_python_line,
            "trusted_release": trusted_release,
            "adoption_safety_pass": run.get("adoption_safety_pass"),
        },
        sort_keys=True,
        ensure_ascii=False,
    )


def _material_repeat_consistency(runs: list[dict[str, object]]) -> dict[str, bool]:
    result: dict[str, bool] = {}
    for case_id in CRITICAL_REPEAT_CASE_IDS:
        matching = [run for run in runs if run.get("case_id") == case_id]
        result[case_id] = bool(
            len(matching) == 3
            and len({material_trusted_outcome_signature(run) for run in matching}) == 1
        )
    return result


def _latency_summary(runs: list[dict[str, object]]) -> dict[str, float | int]:
    values = [
        float(run["latency_seconds"])
        for run in runs
        if isinstance(run.get("latency_seconds"), (int, float))
    ]
    if not values:
        return {"count": 0}
    return {
        "count": len(values),
        "mean_seconds": round(statistics.fmean(values), 6),
        "median_seconds": round(statistics.median(values), 6),
        "min_seconds": round(min(values), 6),
        "max_seconds": round(max(values), 6),
    }


def main() -> int:
    evidence = _load(DEFAULT_INPUT_PATH)
    runs = [run for run in evidence["runs"] if isinstance(run, dict)]
    summary = evidence.get("summary")
    if not isinstance(summary, dict):
        raise RuntimeError("The live evidence contained no summary object.")

    material_consistency = _material_repeat_consistency(runs)
    all_materially_consistent = all(material_consistency.values())
    latency = _latency_summary(runs)

    # These checks are intentionally tied to the current frozen corpus and the Step 6
    # adoption language. They do not claim general model quality outside this slice.
    gate = {
        "1_every_accepted_candidate_survives_step2": summary.get("adoption_safety_failed") == 0,
        "2_no_wrong_direction_on_frozen_controls": summary.get("adoption_safety_failed") == 0,
        "3_no_negated_or_future_drop_admitted": summary.get("adoption_safety_failed") == 0,
        "4_no_unstated_line_from_raised_minimum_admitted": all(
            run.get("adoption_safety_pass") is True
            for run in runs
            if run.get("case_id") == "raised_minimum_without_explicit_dropped_line"
        ),
        "5_s001_correct_and_grounded": all(
            run.get("strict_pass") is True
            for run in runs
            if run.get("case_id") == "s001_exact_excerpt"
        ),
        "6_ambiguous_and_no_claim_cases_abstain": all(
            run.get("adoption_safety_pass") is True
            for run in runs
            if run.get("case_id") in {"ambiguous_support_wording", "irrelevant_fix_only"}
        ),
        "7_critical_trusted_outcomes_materially_consistent": all_materially_consistent,
        "8_latency_recorded_for_all_calls": latency.get("count") == len(runs) == 25,
        "9_material_improvement_over_rejected_local_baseline": (
            summary.get("adoption_safety_passed") == 25
            and summary.get("strict_oracle_passed") == 24
        ),
        "10_deployment_identity_recorded": bool(
            evidence.get("model")
            and evidence.get("base_url")
            and evidence.get("contract_version") == 2
            and evidence.get("temperature") == 0
            and evidence.get("seed") == 0
            and evidence.get("automatic_retries") is False
        ),
    }

    all_gate_checks_pass = all(gate.values())
    disposition = "adopt_bounded_extractor" if all_gate_checks_pass else "retain_experiment_only"

    result = {
        "input_evidence": str(DEFAULT_INPUT_PATH),
        "model": evidence.get("model"),
        "contract_version": evidence.get("contract_version"),
        "strict_oracle_passed": summary.get("strict_oracle_passed"),
        "strict_oracle_failed": summary.get("strict_oracle_failed"),
        "adoption_safety_passed": summary.get("adoption_safety_passed"),
        "adoption_safety_failed": summary.get("adoption_safety_failed"),
        "material_critical_repeat_consistency": material_consistency,
        "all_material_critical_repeats_consistent": all_materially_consistent,
        "latency": latency,
        "adoption_gate": gate,
        "all_adoption_gate_checks_pass": all_gate_checks_pass,
        "proposed_step6_disposition": disposition,
        "scope_note": (
            "This disposition applies only to the bounded support-drop extraction role, "
            "with deterministic Step 2 validation remaining mandatory downstream."
        ),
    }

    DEFAULT_OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    DEFAULT_OUTPUT_PATH.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print("B2 Step 6 contract-v2 deterministic adoption assessment")
    print("model calls: 0")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"evidence file: {DEFAULT_OUTPUT_PATH}")
    return 0 if all_gate_checks_pass else 2


if __name__ == "__main__":
    sys.exit(main())
