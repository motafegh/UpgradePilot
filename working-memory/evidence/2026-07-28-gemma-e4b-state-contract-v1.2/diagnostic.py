#!/usr/bin/env python3
"""State-contract v1.2 evidence harness for the bounded Gemma E4B diagnostic.

This is dated diagnostic code under working-memory, not UpgradePilot product code.
It reuses the preserved v1.1 harness and changes only the authorized semantic
contract, deterministic domain validator, and frozen diagnostic oracles.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[2]
RESULT_RECORD = REPO_ROOT / "working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.2-diagnostic-result.md"
V1_1_ROOT = ROOT.parent / "2026-07-28-gemma-e4b-state-contract-v1.1"
V1_1_HARNESS = V1_1_ROOT / "diagnostic.py"

spec = importlib.util.spec_from_file_location("upgradepilot_v1_1", V1_1_HARNESS)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not load prior harness: {V1_1_HARNESS}")
v1_1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v1_1)
base = v1_1.base

BASE_SCHEMA = copy.deepcopy(v1_1.BASE_SCHEMA)
BASE_SYSTEM_PROMPT = v1_1.SYSTEM_PROMPT_V1_1
LMS_EXE = os.environ.get("LMS_EXE", base.LMS_EXE)

V1_2_ADDITION = (
    " Category and weak-change contract version 1.2: "
    "Use compatibility_assurance only when the source explicitly assures continued "
    "compatibility, backward compatibility, drop-in replacement behavior, or absence "
    "of required migration. The word compatibility by itself is not an assurance. "
    "An explicit adjustment to compatibility-related behavior is an "
    "interface_or_behavior_change, not a compatibility_assurance. "
    "Use changed_unspecified only when the source explicitly states that an interface "
    "or behavior changed, the changed subject or scope is identifiable, and the "
    "direction or effect is not stated. changed_unspecified means only that a change "
    "occurred; it does not imply improvement, regression, breaking behavior, "
    "compatibility, migration impact, or safety. "
    "Use resolved when the minimum explicit source meaning can be represented "
    "responsibly; resolved does not mean the evidence is sufficient, safe, compatible, "
    "or actionable. Use unresolved when no supported category and change-state pair "
    "can represent the minimum meaning without invention. "
    "A support_boundary_change must explicitly state support_added or support_dropped; "
    "otherwise return unresolved."
)
SYSTEM_PROMPT_V1_2 = BASE_SYSTEM_PROMPT + V1_2_ADDITION

PAIR_MATRIX: dict[str, set[str]] = {
    "fix_or_remediation": {"fixed"},
    "compatibility_assurance": {"compatibility_assured"},
    "support_boundary_change": {"support_added", "support_dropped"},
    "interface_or_behavior_change": {
        "deprecated", "removed", "future_removal", "changed_unspecified"
    },
}

GATE_A_CASE = {
    "id": "A_exact_compatibility_behavior_adjustment",
    "text": "Compatibility behavior was adjusted for older environments.",
    "expected_state": "resolved",
    "expected": [("interface_or_behavior_change", "changed_unspecified")],
    "critical": True,
}
GATE_B_CASES = [
    {
        "id": "B_generic_behavior_change",
        "text": "Request retry behavior changed for slow networks.",
        "expected_state": "resolved",
        "expected": [("interface_or_behavior_change", "changed_unspecified")],
        "critical": True,
    },
    {
        "id": "C_explicit_compatibility_assurance",
        "text": (
            "This release remains backward compatible with the previous patch release "
            "and requires no migration."
        ),
        "expected_state": "resolved",
        "expected": [("compatibility_assurance", "compatibility_assured")],
        "critical": True,
    },
    {
        "id": "D_genuinely_unresolved_relevance",
        "text": "Older environments may be affected.",
        "expected_state": "unresolved",
        "expected": [],
        "critical": True,
    },
    {
        "id": "E_support_direction_missing",
        "text": "Python version support policy changed in this release.",
        "expected_state": "unresolved",
        "expected": [],
        "critical": True,
    },
    {
        "id": "F_no_decision_relevant_claim",
        "text": "Documentation examples were reorganized and several spelling errors were corrected.",
        "expected_state": "no_decision_relevant_claim",
        "expected": [],
        "critical": False,
    },
]
GATE_C_CASE = {
    "id": "G_conflicting_support",
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


def canonical_hash(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def configure() -> None:
    base.ROOT = ROOT
    base.SYSTEM_PROMPT = SYSTEM_PROMPT_V1_2
    base.SCHEMA = copy.deepcopy(BASE_SCHEMA)
    base.validate_structure = validate_structure_v1_2


def validate_pair_matrix(value: Any) -> list[str]:
    if not isinstance(value, dict):
        return ["category/change-state matrix requires an object"]
    claims = value.get("claims")
    if not isinstance(claims, list):
        return ["category/change-state matrix requires a claims array"]
    errors: list[str] = []
    for index, claim in enumerate(claims):
        if not isinstance(claim, dict):
            continue
        category = claim.get("category")
        change_state = claim.get("change_state")
        allowed = PAIR_MATRIX.get(category)
        if allowed is None:
            errors.append(f"claim {index} has unsupported category {category!r}")
        elif change_state not in allowed:
            errors.append(
                f"claim {index} pair {category!r}/{change_state!r} is invalid; "
                f"allowed={sorted(allowed)}"
            )
    return errors


def validate_structure_v1_2(value: Any, source_text: str) -> list[str]:
    return v1_1.validate_structure_v1_1(value, source_text) + validate_pair_matrix(value)


def freeze() -> None:
    previous_schema = json.loads((V1_1_ROOT / "schema.json").read_text(encoding="utf-8"))
    if previous_schema != BASE_SCHEMA:
        raise RuntimeError("v1.1 schema differs from imported schema")
    base.write_json(ROOT / "schema.json", BASE_SCHEMA)
    base.write_text(ROOT / "system-prompt-v1.1.txt", BASE_SYSTEM_PROMPT + "\n")
    base.write_text(ROOT / "state-contract-v1.2-addition.txt", V1_2_ADDITION.lstrip() + "\n")
    base.write_text(ROOT / "system-prompt-v1.2.txt", SYSTEM_PROMPT_V1_2 + "\n")
    base.write_json(
        ROOT / "category-change-state-matrix.json",
        {key: sorted(value) for key, value in PAIR_MATRIX.items()},
    )
    base.write_json(
        ROOT / "frozen-diagnostic-cases.json",
        {"gate_a": GATE_A_CASE, "gate_b": GATE_B_CASES, "gate_c": GATE_C_CASE},
    )
    base.write_json(
        ROOT / "frozen-variable-comparison.json",
        {
            "prompt_version": "1.2",
            "v1_1_prompt_sha256": hashlib.sha256(BASE_SYSTEM_PROMPT.encode()).hexdigest(),
            "v1_2_addition_sha256": hashlib.sha256(V1_2_ADDITION.encode()).hexdigest(),
            "v1_2_prompt_sha256": hashlib.sha256(SYSTEM_PROMPT_V1_2.encode()).hexdigest(),
            "v1_1_schema_sha256": canonical_hash(previous_schema),
            "v1_2_schema_sha256": canonical_hash(BASE_SCHEMA),
            "schema_equal": previous_schema == BASE_SCHEMA,
            "model": base.MODEL,
            "temperature": 0,
            "seed": 0,
            "max_tokens": 512,
            "stream": False,
            "endpoint": f"{base.BASE_URL}/v1/chat/completions",
            "changed_variables": [
                "v1.2 category and changed_unspecified prompt semantics",
                "deterministic category/change-state matrix",
                "revised ambiguity oracle and contrast cases",
            ],
            "unchanged_variables": [
                "Gemma E4B model and Q4_K_XL quantization",
                "4096 context and load configuration",
                "parallelism 1",
                "Flash Attention and GPU KV-cache placement",
                "four-state v1.1 semantics",
                "claim categories and change-state vocabulary",
                "flat JSON Schema",
                "temperature 0 and seed 0",
                "512-token output budget",
                "non-streaming endpoint",
                "source grounding",
                "no Instructor or retry layer",
            ],
        },
    )


def self_test() -> None:
    source = "Synthetic source."
    valid = {
        "state": "resolved",
        "claims": [{
            "category": "interface_or_behavior_change",
            "subject": "synthetic",
            "change_state": "changed_unspecified",
            "source_quote": source,
        }],
        "unresolved_reasons": [],
    }
    invalid = copy.deepcopy(valid)
    invalid["claims"][0]["category"] = "compatibility_assurance"
    valid_errors = validate_structure_v1_2(valid, source)
    invalid_errors = validate_structure_v1_2(invalid, source)
    result = {
        "valid_errors": valid_errors,
        "invalid_errors": invalid_errors,
        "passed": not valid_errors and bool(invalid_errors),
    }
    base.write_json(ROOT / "validator-self-test.json", result)
    if not result["passed"]:
        raise RuntimeError("validator self-test failed")


def loaded_instances() -> list[dict[str, str]]:
    payload = base.get_json(f"{base.BASE_URL}/api/v1/models")
    models = payload if isinstance(payload, list) else payload.get("models", [])
    result: list[dict[str, str]] = []
    for model in models:
        if not isinstance(model, dict):
            continue
        for instance in model.get("loaded_instances", []) or []:
            if isinstance(instance, dict):
                result.append({
                    "model_key": str(model.get("key")),
                    "instance_id": str(instance.get("id")),
                })
    return result


def preflight() -> None:
    evidence: dict[str, Any] = {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "repo_root": str(REPO_ROOT),
        "python": sys.executable,
        "lms_exe": LMS_EXE,
        "lms_exe_exists": Path(LMS_EXE).exists(),
        "base_url": base.BASE_URL,
    }
    try:
        evidence["loaded_instances"] = loaded_instances()
        evidence["server_reachable"] = True
    except Exception as exc:
        evidence["server_reachable"] = False
        evidence["server_error"] = repr(exc)
        base.write_json(ROOT / "preflight.json", evidence)
        raise
    base.write_json(ROOT / "preflight.json", evidence)
    if not evidence["lms_exe_exists"]:
        raise RuntimeError(f"LM Studio CLI not found: {LMS_EXE}")
    if evidence["loaded_instances"]:
        raise RuntimeError(f"Refusing to run while another model is loaded: {evidence['loaded_instances']}")


def run_gate_a() -> int:
    results: list[dict[str, Any]] = []
    for repetition in (1, 2, 3):
        result = base.run_one(GATE_A_CASE, repetition, "state-contract-v1.2-gate-a")
        results.append(result)
        if not result["pass"]:
            base.write_json(ROOT / "gate-a-summary.json", {
                "completed": False,
                "passed": False,
                "stop_reason": f"Gate A failed at repetition {repetition}",
                "results": results,
            })
            return 2
    base.write_json(ROOT / "gate-a-summary.json", {
        "completed": True,
        "passed": True,
        "required_passes": 3,
        "observed_passes": 3,
        "stop_reason": None,
        "results": results,
    })
    return 0


def require_passed(path: Path, gate: str) -> None:
    if not path.exists():
        raise RuntimeError(f"{gate} evidence does not exist")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("passed") is not True:
        raise RuntimeError(f"{gate} did not pass")


def run_gate_b() -> int:
    require_passed(ROOT / "gate-a-summary.json", "Gate A")
    results: list[dict[str, Any]] = []
    for case in GATE_B_CASES:
        result = base.run_one(case, 1, "state-contract-v1.2-gate-b")
        results.append(result)
        if not result["pass"]:
            base.write_json(ROOT / "gate-b-summary.json", {
                "completed": False,
                "passed": False,
                "stop_reason": f"Gate B failed at {case['id']}",
                "results": results,
            })
            return 2
    base.write_json(ROOT / "gate-b-summary.json", {
        "completed": True,
        "passed": True,
        "stop_reason": None,
        "results": results,
    })
    return 0


def run_gate_c() -> int:
    require_passed(ROOT / "gate-b-summary.json", "Gate B")
    result = base.run_one(GATE_C_CASE, 1, "state-contract-v1.2-gate-c")
    base.write_json(ROOT / "gate-c-summary.json", {
        "completed": bool(result["pass"]),
        "passed": bool(result["pass"]),
        "stop_reason": (
            "Authorized v1.2 stop line reached" if result["pass"]
            else "Gate C conflict case failed"
        ),
        "results": [result],
    })
    return 0 if result["pass"] else 2


def read_json_if_exists(path: Path, default: Any) -> Any:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def format_rows(summary: dict[str, Any]) -> str:
    results = summary.get("results", [])
    if not results:
        return "| — | not run | — | — | — |\n"
    rows = ["| Case | Pass | State | Claims | Reasons |", "|---|---|---|---:|---:|"]
    for result in results:
        inner = result.get("inner") or {}
        rows.append(
            f"| `{result.get('case_id')}` | {bool(result.get('pass'))} | "
            f"`{inner.get('state')}` | {len(inner.get('claims', []) or [])} | "
            f"{len(inner.get('unresolved_reasons', []) or [])} |"
        )
    return "\n".join(rows) + "\n"


def first_failure(*summaries: dict[str, Any]) -> str:
    for summary in summaries:
        for result in summary.get("results", []):
            if not result.get("pass"):
                errors = (
                    list(result.get("structure_errors", []))
                    + list(result.get("semantic_errors", []))
                    + list(result.get("runtime_errors", []))
                )
                return f"`{result.get('case_id')}`: " + ("; ".join(errors) or "unspecified failure")
    return "None within the executed gates."


def report() -> None:
    gate_a = read_json_if_exists(ROOT / "gate-a-summary.json", {"passed": False, "results": []})
    gate_b = read_json_if_exists(ROOT / "gate-b-summary.json", {"passed": False, "results": []})
    gate_c = read_json_if_exists(ROOT / "gate-c-summary.json", {"passed": False, "results": []})
    test_exit = (ROOT / "product-tests.exit-code.txt").read_text().strip() if (ROOT / "product-tests.exit-code.txt").exists() else "missing"
    test_output = ""
    for candidate in (ROOT / "product-tests.stdout.txt", ROOT / "product-tests.stderr.txt"):
        if candidate.exists():
            test_output += candidate.read_text(encoding="utf-8", errors="replace") + "\n"
    match = re.search(r"Ran\s+(\d+)\s+tests?", test_output)
    test_count = match.group(1) if match else "unknown"

    if gate_a.get("passed") is not True:
        outcome = "Gate A failed"
    elif gate_b.get("passed") is not True:
        outcome = "Gate A passed; Gate B failed"
    elif gate_c.get("passed") is not True:
        outcome = "Gates A and B passed; Gate C failed"
    else:
        outcome = "Gates A, B, and C passed"

    text = f"""# B2 Gemma E4B State-Contract v1.2 Diagnostic Result

**Date:** 2026-07-28  
**Operation:** Execute the selected state-contract v1.2 category and ambiguity-boundary diagnostic through its stop condition  
**Selected diagnostic:** [`2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md`](2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md)  
**Prior result:** [`2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md`](2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md)  
**Raw evidence:** [`evidence/2026-07-28-gemma-e4b-state-contract-v1.2/`](evidence/2026-07-28-gemma-e4b-state-contract-v1.2/)  
**Result classification:** {outcome}; independent review pending; no model or product adoption

## Compact result

```text
Gate A passed: {gate_a.get('passed')}
Gate B passed: {gate_b.get('passed')}
Gate C passed: {gate_c.get('passed')}
product-test exit: {test_exit}
product-test count: {test_count}
```

## Gate A

{format_rows(gate_a)}
## Gate B

{format_rows(gate_b)}
## Gate C

{format_rows(gate_c)}
## First failure

{first_failure(gate_a, gate_b, gate_c)}

## Frozen change

The diagnostic changed only the v1.2 category and `changed_unspecified` prompt
semantics, the deterministic category/change-state matrix, and the revised frozen
oracles. The model, quantization, context, runtime configuration, endpoint, flat
schema, temperature, seed, output budget, grounding rule, and no-Instructor/no-retry
boundary remained frozen. Exact hashes are in `frozen-variable-comparison.json`.

## Restoration and validation

Load, unload, snapshots, logs, product-test output, repository status, and evidence
hashes are preserved in the raw evidence directory. `MEMORY.md` was not modified by
the runner; independent review must update the sole live-state owner.
"""
    RESULT_RECORD.write_text(text, encoding="utf-8")
    (ROOT / "result-record.sha256").write_text(
        f"{sha256_file(RESULT_RECORD)}  {RESULT_RECORD.name}\n", encoding="utf-8"
    )


def manifest() -> None:
    excluded = {"MANIFEST.sha256", "manifest-verification.txt"}
    paths = sorted(path for path in ROOT.rglob("*") if path.is_file() and path.name not in excluded)
    lines = [f"{sha256_file(path)}  {path.relative_to(ROOT).as_posix()}" for path in paths]
    (ROOT / "MANIFEST.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")
    verification = []
    for line in lines:
        expected, relative = line.split("  ", 1)
        actual = sha256_file(ROOT / relative)
        verification.append(f"{'OK' if expected == actual else 'FAIL'}  {relative}")
    passed = all(item.startswith("OK  ") for item in verification)
    (ROOT / "manifest-verification.txt").write_text(
        "\n".join(verification) + f"\n\nverified={passed}\ncount={len(lines)}\n",
        encoding="utf-8",
    )
    if not passed:
        raise RuntimeError("manifest verification failed")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("freeze")
    sub.add_parser("self-test")
    sub.add_parser("preflight")
    sub.add_parser("gate-a")
    sub.add_parser("gate-b")
    sub.add_parser("gate-c")
    sub.add_parser("report")
    sub.add_parser("manifest")
    snapshot = sub.add_parser("snapshot")
    snapshot.add_argument("label")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    configure()
    if args.command == "freeze":
        freeze(); print("v1.2 contract frozen"); return 0
    if args.command == "self-test":
        freeze(); self_test(); print("validator self-test passed"); return 0
    if args.command == "preflight":
        freeze(); preflight(); print("preflight passed"); return 0
    if args.command == "gate-a":
        return run_gate_a()
    if args.command == "gate-b":
        return run_gate_b()
    if args.command == "gate-c":
        return run_gate_c()
    if args.command == "report":
        report(); print(RESULT_RECORD); return 0
    if args.command == "manifest":
        manifest(); print("manifest verified"); return 0
    if args.command == "snapshot":
        return base.capture_snapshot(args.label)
    raise AssertionError(args.command)


if __name__ == "__main__":
    sys.exit(main())
