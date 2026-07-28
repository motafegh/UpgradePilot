#!/usr/bin/env python3
"""Prompt state-contract v1.1 diagnostic for the Gemma E4B clear-fix smoke.

This wrapper deliberately reuses the first observed-run harness. It changes only the
system prompt's state-selection contract and deterministic cross-field validation,
then executes Gate A and conditionally Gate B from the dated diagnostic record.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
PRIOR_ROOT = ROOT.parent / "2026-07-28-gemma-e4b"
PRIOR_HARNESS = PRIOR_ROOT / "evaluate.py"

spec = importlib.util.spec_from_file_location("prior_gemma_evidence", PRIOR_HARNESS)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not load prior harness: {PRIOR_HARNESS}")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)

BASE_SYSTEM_PROMPT = base.SYSTEM_PROMPT
STATE_CONTRACT_V1_1 = (
    " State selection contract version 1.1: Select exactly one result state using "
    "these meanings and relationships. Use resolved when the source explicitly "
    "supports one or more decision-relevant grounded claims and no material ambiguity "
    "or conflict remains; return one or more claims and zero unresolved reasons. Use "
    "no_decision_relevant_claim when the source contains no supported "
    "decision-relevant claim; return zero claims and zero unresolved reasons. Use "
    "unresolved when potentially relevant meaning cannot be responsibly resolved "
    "because the source is ambiguous, incomplete, or outside the supported vocabulary; "
    "return zero accepted claims and one or more unresolved reasons. Use conflicting "
    "when the source contains materially opposing grounded claims that cannot "
    "responsibly be collapsed into one meaning; return multiple grounded conflicting "
    "claims and one or more conflict reasons."
)
SYSTEM_PROMPT_V1_1 = BASE_SYSTEM_PROMPT + STATE_CONTRACT_V1_1

BASE_VALIDATE_STRUCTURE = base.validate_structure
BASE_SCHEMA = copy.deepcopy(base.SCHEMA)

CLEAR_FIX = copy.deepcopy(base.SYNTHETIC_CASES[0])
NO_RELEVANT_CLAIM = copy.deepcopy(base.SYNTHETIC_CASES[1])
AMBIGUOUS = copy.deepcopy(base.SYNTHETIC_CASES[9])
CONFLICTING = {
    "id": "K_conflicting_support",
    "text": (
        "This release adds Python 3.13 support. "
        "This release drops Python 3.13 support."
    ),
    "expected_state": "conflicting",
    "expected": [
        ("support_boundary_change", "support_added"),
        ("support_boundary_change", "support_dropped"),
    ],
    "critical": True,
}
GATE_B_CASES = [NO_RELEVANT_CLAIM, AMBIGUOUS, CONFLICTING]


def canonical_hash(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def validate_state_invariant(value: Any) -> list[str]:
    """Enforce the state/claims/reasons relationships outside model control."""

    if not isinstance(value, dict):
        return ["state invariant cannot evaluate a non-object result"]
    state = value.get("state")
    claims = value.get("claims")
    reasons = value.get("unresolved_reasons")
    if not isinstance(claims, list) or not isinstance(reasons, list):
        return ["state invariant requires claims and unresolved_reasons arrays"]

    errors: list[str] = []
    if state == "resolved":
        if len(claims) < 1:
            errors.append("resolved requires one or more accepted claims")
        if reasons:
            errors.append("resolved requires zero unresolved reasons")
    elif state == "no_decision_relevant_claim":
        if claims:
            errors.append("no_decision_relevant_claim requires zero claims")
        if reasons:
            errors.append("no_decision_relevant_claim requires zero unresolved reasons")
    elif state == "unresolved":
        if claims:
            errors.append("unresolved requires zero accepted claims")
        if len(reasons) < 1:
            errors.append("unresolved requires one or more unresolved reasons")
    elif state == "conflicting":
        if len(claims) < 2:
            errors.append("conflicting requires multiple grounded conflicting claims")
        if len(reasons) < 1:
            errors.append("conflicting requires one or more conflict reasons")
    return errors


def validate_structure_v1_1(value: Any, source_text: str) -> list[str]:
    return BASE_VALIDATE_STRUCTURE(value, source_text) + validate_state_invariant(value)


def freeze_contract() -> None:
    prior_schema = json.loads((PRIOR_ROOT / "schema.json").read_text(encoding="utf-8"))
    if prior_schema != BASE_SCHEMA:
        raise RuntimeError("Prior frozen schema and imported harness schema differ")
    if CLEAR_FIX["text"] != (
        "This release fixes a crash when parsing empty configuration files."
    ):
        raise RuntimeError("The Gate A clear-fix source changed")

    base.write_json(ROOT / "schema.json", BASE_SCHEMA)
    base.write_text(ROOT / "system-prompt-v1.0.txt", BASE_SYSTEM_PROMPT + "\n")
    base.write_text(ROOT / "state-contract-v1.1-addition.txt", STATE_CONTRACT_V1_1.lstrip() + "\n")
    base.write_text(ROOT / "system-prompt-v1.1.txt", SYSTEM_PROMPT_V1_1 + "\n")
    base.write_json(ROOT / "gate-a-case.json", CLEAR_FIX)
    base.write_json(ROOT / "gate-b-cases.json", GATE_B_CASES)
    base.write_json(
        ROOT / "frozen-variable-comparison.json",
        {
            "prompt_version": "1.1",
            "base_prompt_sha256": hashlib.sha256(BASE_SYSTEM_PROMPT.encode()).hexdigest(),
            "state_contract_addition_sha256": hashlib.sha256(
                STATE_CONTRACT_V1_1.encode()
            ).hexdigest(),
            "prompt_v1_1_sha256": hashlib.sha256(
                SYSTEM_PROMPT_V1_1.encode()
            ).hexdigest(),
            "prior_schema_sha256": canonical_hash(prior_schema),
            "diagnostic_schema_sha256": canonical_hash(BASE_SCHEMA),
            "schema_equal": prior_schema == BASE_SCHEMA,
            "model": base.MODEL,
            "source_equal": True,
            "temperature": 0,
            "seed": 0,
            "max_tokens": 512,
            "stream": False,
            "endpoint": f"{base.BASE_URL}/v1/chat/completions",
            "changed_variables": [
                "explicit four-state system-prompt semantics",
                "deterministic state/claims/reasons invariant",
            ],
            "unchanged_variables": [
                "model and quantization",
                "load configuration",
                "4096 context",
                "parallelism 1",
                "Flash Attention and GPU KV-cache placement",
                "Gate A source sentence",
                "authority boundary",
                "claim categories",
                "change states",
                "flat JSON Schema",
                "temperature 0",
                "seed 0",
                "maximum output budget 512",
                "non-streaming endpoint",
                "base shape and grounding validator",
            ],
        },
    )


def configure_reused_harness() -> None:
    base.ROOT = ROOT
    base.SYSTEM_PROMPT = SYSTEM_PROMPT_V1_1
    base.SCHEMA = copy.deepcopy(BASE_SCHEMA)
    base.validate_structure = validate_structure_v1_1


def run_gate_a() -> int:
    freeze_contract()
    configure_reused_harness()
    results: list[dict[str, Any]] = []
    for repetition in (1, 2, 3):
        result = base.run_one(CLEAR_FIX, repetition, "state-contract-v1.1-gate-a")
        results.append(result)
        if not result["pass"]:
            base.write_json(
                ROOT / "gate-a-summary.json",
                {
                    "completed": False,
                    "passed": False,
                    "stop_reason": f"Gate A failed at repetition {repetition}",
                    "results": results,
                },
            )
            return 2
    base.write_json(
        ROOT / "gate-a-summary.json",
        {
            "completed": True,
            "passed": True,
            "stop_reason": None,
            "required_passes": 3,
            "observed_passes": 3,
            "results": results,
        },
    )
    return 0


def run_gate_b() -> int:
    freeze_contract()
    configure_reused_harness()
    gate_a_path = ROOT / "gate-a-summary.json"
    if not gate_a_path.exists():
        raise RuntimeError("Gate B cannot run before Gate A evidence exists")
    gate_a = json.loads(gate_a_path.read_text(encoding="utf-8"))
    if gate_a.get("passed") is not True or gate_a.get("observed_passes") != 3:
        raise RuntimeError("Gate B cannot run because Gate A did not pass three of three")

    results: list[dict[str, Any]] = []
    for case in GATE_B_CASES:
        result = base.run_one(case, 1, "state-contract-v1.1-gate-b")
        results.append(result)
        if not result["pass"]:
            base.write_json(
                ROOT / "gate-b-summary.json",
                {
                    "completed": False,
                    "passed": False,
                    "stop_reason": f"Gate B failed at {case['id']}",
                    "results": results,
                },
            )
            return 2
    base.write_json(
        ROOT / "gate-b-summary.json",
        {
            "completed": True,
            "passed": True,
            "stop_reason": "Diagnostic stop line reached before broader corpus",
            "results": results,
        },
    )
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    snapshot = subparsers.add_parser("snapshot")
    snapshot.add_argument("label")
    subparsers.add_parser("freeze")
    subparsers.add_parser("gate-a")
    subparsers.add_parser("gate-b")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "snapshot":
        configure_reused_harness()
        return base.capture_snapshot(args.label)
    if args.command == "freeze":
        freeze_contract()
        print("state contract v1.1 frozen")
        return 0
    if args.command == "gate-a":
        return run_gate_a()
    if args.command == "gate-b":
        return run_gate_b()
    raise AssertionError(args.command)


if __name__ == "__main__":
    sys.exit(main())
