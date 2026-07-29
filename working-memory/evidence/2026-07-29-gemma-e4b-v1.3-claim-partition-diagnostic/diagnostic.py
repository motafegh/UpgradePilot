#!/usr/bin/env python3
"""Run the bounded Gemma E4B v1.3 claim-partition diagnostic.

This is dated experiment evidence, not UpgradePilot product code. It reuses the
accepted v1.2 completion-recovery harness and appends only the selected claim-
partition instruction. The exact failed compatibility-assurance source and
one-claim oracle remain frozen.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[2]
RESULT_RECORD = (
    REPO_ROOT
    / "working-memory/2026-07-29_B2-gemma-e4b-v1.3-claim-partition-diagnostic-result.md"
)
PRIOR_HARNESS = (
    ROOT.parent
    / "2026-07-29-gemma-e4b-v1.2-completion-recovery"
    / "diagnostic.py"
)
REVIEW_COMMIT = "58bfd87212c6f261c64f6807b090a982f7a726e4"
FAILED_EVIDENCE_COMMIT = "8e703c86b9da824268119e9437af4eb0ac2c4d8e"
SUMMARY_PATH = ROOT / "claim-partition-summary.json"
REPETITIONS = (1, 2, 3)

spec = importlib.util.spec_from_file_location(
    "upgradepilot_completion_recovery_for_claim_partition", PRIOR_HARNESS
)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not load prior completion-recovery harness: {PRIOR_HARNESS}")
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)

prior.ROOT = ROOT
prior.RESULT_RECORD = RESULT_RECORD
prior.v1_2.ROOT = ROOT
prior.base.ROOT = ROOT

base = prior.base
v1_2 = prior.v1_2
LMS_EXE = os.environ.get("LMS_EXE", prior.LMS_EXE)
ORIGINAL_CONFIGURE = prior.configure
BASE_V1_2_PROMPT = v1_2.SYSTEM_PROMPT_V1_2

CASE: dict[str, Any] = {
    "id": "C_explicit_compatibility_assurance",
    "text": (
        "This release remains backward compatible with the previous patch release "
        "and requires no migration."
    ),
    "expected_state": "resolved",
    "expected": [("compatibility_assurance", "compatibility_assured")],
    "critical": True,
}

V1_3_ADDITION = (
    " Claim partition contract version 1.3: "
    "Emit one claim per distinct supported category and change-state proposition, "
    "not one claim per clause or phrase. When multiple clauses in one source span "
    "jointly support the same proposition, combine them into one claim. "
    "Backward compatible and requires no migration jointly express one "
    "compatibility_assurance with change_state compatibility_assured. "
    "Absence of required migration is never a support_boundary_change. "
    "Do not emit an extra claim merely to restate evidence that supports an already "
    "represented proposition. Before returning JSON, ensure every claim uses a valid "
    "category/change-state pair."
)
SYSTEM_PROMPT_V1_3 = BASE_V1_2_PROMPT + V1_3_ADDITION


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def configure() -> None:
    """Apply only the selected v1.3 prompt addition to the inherited harness."""

    v1_2.SYSTEM_PROMPT_V1_2 = SYSTEM_PROMPT_V1_3
    ORIGINAL_CONFIGURE()
    base.SYSTEM_PROMPT = SYSTEM_PROMPT_V1_3


# The inherited run_once/freeze functions resolve configure through module globals.
prior.configure = configure


def freeze() -> None:
    prior.CASE = copy.deepcopy(CASE)
    configure()
    prior.freeze()

    (ROOT / "claim-partition-contract-v1.3-addition.txt").write_text(
        V1_3_ADDITION.lstrip() + "\n", encoding="utf-8"
    )
    (ROOT / "system-prompt-v1.3.txt").write_text(
        SYSTEM_PROMPT_V1_3 + "\n", encoding="utf-8"
    )
    write_json(ROOT / "frozen-claim-partition-case.json", CASE)

    comparison_path = ROOT / "frozen-variable-comparison.json"
    comparison = read_json(comparison_path, {})
    comparison.update(
        {
            "operation": "state-contract v1.3 claim-partition diagnostic",
            "review_commit": REVIEW_COMMIT,
            "failed_evidence_commit": FAILED_EVIDENCE_COMMIT,
            "v1_2_prompt_sha256": hashlib.sha256(
                BASE_V1_2_PROMPT.encode("utf-8")
            ).hexdigest(),
            "v1_3_addition_sha256": hashlib.sha256(
                V1_3_ADDITION.encode("utf-8")
            ).hexdigest(),
            "v1_3_prompt_sha256": hashlib.sha256(
                SYSTEM_PROMPT_V1_3.encode("utf-8")
            ).hexdigest(),
            "schema_sha256": canonical_hash(base.SCHEMA),
            "case": CASE,
            "repetitions": list(REPETITIONS),
            "changed_variables_from_v1_2_gate_b": [
                "append claim-partition contract v1.3"
            ],
            "unchanged_variables": [
                "Gemma E4B model and Q4_K_XL quantization",
                "4096 context and load configuration",
                "parallelism 1",
                "Flash Attention and GPU KV-cache placement",
                "v1.2 state, category, weak-change, and grounding semantics",
                "flat JSON Schema",
                "category/change-state matrix",
                "exact compatibility-assurance source and one-claim oracle",
                "max_tokens 1024",
                "temperature 0 and seed 0",
                "non-streaming endpoint",
                "no Instructor and no retries",
            ],
        }
    )
    write_json(comparison_path, comparison)


def self_test() -> None:
    configure()
    valid = {
        "state": "resolved",
        "claims": [
            {
                "category": "compatibility_assurance",
                "subject": "backward compatibility and migration requirement",
                "change_state": "compatibility_assured",
                "source_quote": CASE["text"],
            }
        ],
        "unresolved_reasons": [],
    }
    invalid = copy.deepcopy(valid)
    invalid["claims"].append(
        {
            "category": "support_boundary_change",
            "subject": "migration requirement",
            "change_state": "compatibility_assured",
            "source_quote": CASE["text"],
        }
    )

    valid_structure = v1_2.validate_structure_v1_2(valid, CASE["text"])
    valid_semantics = base.validate_semantics(CASE, valid)
    invalid_structure = v1_2.validate_structure_v1_2(invalid, CASE["text"])
    payload = {
        "valid_structure_errors": valid_structure,
        "valid_semantic_errors": valid_semantics,
        "invalid_structure_errors": invalid_structure,
        "passed": (
            not valid_structure
            and not valid_semantics
            and any("support_boundary_change" in item for item in invalid_structure)
        ),
    }
    write_json(ROOT / "claim-partition-validator-self-test.json", payload)
    if not payload["passed"]:
        raise RuntimeError("v1.3 claim-partition validator self-test failed")


def preflight() -> None:
    configure()
    prior.preflight()


def run_repetition(repetition: int) -> dict[str, Any]:
    if repetition not in REPETITIONS:
        raise ValueError(f"Unsupported repetition: {repetition}")

    prior.CASE = copy.deepcopy(CASE)
    configure()

    temporary_id = f"{CASE['id']}__completion_recovery_r1"
    temporary_dir = ROOT / "runs" / temporary_id
    temporary_summary = ROOT / "completion-recovery-summary.json"
    if temporary_dir.exists() or temporary_summary.exists():
        raise RuntimeError("Temporary inherited evidence exists and will not be overwritten")

    prior.run_once()
    inherited = read_json(temporary_summary, {})
    inherited_results = inherited.get("results", [])
    if len(inherited_results) != 1:
        raise RuntimeError("Inherited harness did not produce exactly one result")

    result = dict(inherited_results[0])
    final_id = f"{CASE['id']}__claim_partition_r{repetition}"
    final_dir = ROOT / "runs" / final_id
    if final_dir.exists():
        raise RuntimeError(f"Final repetition evidence exists: {final_dir}")
    temporary_dir.rename(final_dir)
    temporary_summary.unlink()

    structure_errors = list(result.get("structure_errors", []))
    semantic_evaluated = not structure_errors
    result.update(
        {
            "run_id": final_id,
            "phase": "state-contract-v1.3-claim-partition",
            "repetition": repetition,
            "semantic_evaluated": semantic_evaluated,
            "semantic_pass": (
                bool(result.get("semantic_pass")) if semantic_evaluated else None
            ),
        }
    )
    write_json(final_dir / "validation.json", result)
    print(
        f"CLAIM_PARTITION {result.get('classification')} {final_id}", flush=True
    )
    return result


def run_all() -> int:
    if SUMMARY_PATH.exists():
        raise RuntimeError("Claim-partition summary already exists")

    results: list[dict[str, Any]] = []
    for repetition in REPETITIONS:
        result = run_repetition(repetition)
        results.append(result)
        if not result.get("pass"):
            write_json(
                SUMMARY_PATH,
                {
                    "completed": False,
                    "passed": False,
                    "classification": f"stopped_at_repetition_{repetition}",
                    "stop_reason": (
                        "First v1.3 claim-partition failure reached the mandatory stop line"
                    ),
                    "results": results,
                },
            )
            return 2

    write_json(
        SUMMARY_PATH,
        {
            "completed": True,
            "passed": True,
            "classification": "claim_partition_3_of_3_passed",
            "stop_reason": (
                "v1.3 claim-partition diagnostic completed; independent review required"
            ),
            "results": results,
        },
    )
    return 0


def format_result(result: dict[str, Any]) -> str:
    usage = result.get("usage") if isinstance(result.get("usage"), dict) else {}
    details = (
        usage.get("completion_tokens_details")
        if isinstance(usage.get("completion_tokens_details"), dict)
        else {}
    )
    inner = result.get("inner")
    inner_text = (
        json.dumps(inner, indent=2, ensure_ascii=False)
        if inner is not None
        else "not produced"
    )
    errors = (
        list(result.get("runtime_errors", []))
        + list(result.get("structure_errors", []))
        + list(result.get("semantic_errors", []))
    )
    if result.get("exception"):
        errors.append(f"{result.get('exception_type')}: {result.get('exception')}")
    error_text = "\n".join(f"- {item}" for item in errors) if errors else "- none"
    return f"""## Repetition {result.get('repetition')}

```text
finish reason: {result.get('finish_reason')}
completion tokens: {usage.get('completion_tokens')}
reasoning tokens: {details.get('reasoning_tokens')}
latency seconds: {result.get('total_latency_seconds')}
classification: {result.get('classification')}
structure pass: {result.get('structure_pass')}
semantic evaluated: {result.get('semantic_evaluated')}
semantic pass: {result.get('semantic_pass')}
```

```json
{inner_text}
```

Errors:

{error_text}
"""


def report() -> None:
    summary = read_json(
        SUMMARY_PATH,
        {
            "completed": False,
            "passed": False,
            "classification": "not_run",
            "results": [],
        },
    )
    test_exit = (
        (ROOT / "product-tests.exit-code.txt").read_text(encoding="utf-8").strip()
        if (ROOT / "product-tests.exit-code.txt").exists()
        else "missing"
    )
    test_output = ""
    for path in (ROOT / "product-tests.stdout.txt", ROOT / "product-tests.stderr.txt"):
        if path.exists():
            test_output += path.read_text(encoding="utf-8", errors="replace") + "\n"
    match = re.search(r"Ran\s+(\d+)\s+tests?", test_output)
    test_count = match.group(1) if match else "unknown"
    result_sections = "\n".join(
        format_result(item) for item in summary.get("results", [])
    ) or "No repetition completed."

    text = f"""# B2 Gemma E4B v1.3 Claim-Partition Diagnostic Result

**Date:** 2026-07-29  
**Operation:** Test the selected claim-partition rule against the exact failed compatibility-assurance case  
**Selected review:** [`2026-07-29_B2-gemma-e4b-v1.2-gate-b-compatibility-claim-partition-review.md`](2026-07-29_B2-gemma-e4b-v1.2-gate-b-compatibility-claim-partition-review.md)  
**Raw evidence:** [`evidence/2026-07-29-gemma-e4b-v1.3-claim-partition-diagnostic/`](evidence/2026-07-29-gemma-e4b-v1.3-claim-partition-diagnostic/)  
**Result classification:** {summary.get('classification')}; independent review pending; no model or product adoption

## Compact result

```text
completed: {summary.get('completed')}
passed: {summary.get('passed')}
stop reason: {summary.get('stop_reason')}
product-test exit: {test_exit}
product-test count: {test_count}
```

## Only semantic-contract change

The v1.3 addition defines one claim per distinct supported category/change-state
proposition and requires the backward-compatibility and no-migration clauses to be
represented as one compatibility assurance. The schema, taxonomy, source, oracle,
model, runtime configuration, and deterministic validators remain frozen.

{result_sections}

## Restoration and review boundary

Load, snapshots, requests, responses, reasoning/logs, validation, unload, product
tests, repository status, hashes, and manifest verification are preserved.
`MEMORY.md` was not modified by the runner. Stop and push the first result for
independent review before resuming Gate B or comparing another model.
"""
    RESULT_RECORD.write_text(text, encoding="utf-8")
    (ROOT / "result-record.sha256").write_text(
        f"{sha256_file(RESULT_RECORD)}  {RESULT_RECORD.name}\n", encoding="utf-8"
    )


def manifest() -> None:
    excluded = {"MANIFEST.sha256", "manifest-verification.txt"}
    paths = sorted(
        path for path in ROOT.rglob("*") if path.is_file() and path.name not in excluded
    )
    lines = [
        f"{sha256_file(path)}  {path.relative_to(ROOT).as_posix()}" for path in paths
    ]
    (ROOT / "MANIFEST.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")
    verification: list[str] = []
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
    sub.add_parser("run-all")
    sub.add_parser("report")
    sub.add_parser("manifest")
    snapshot = sub.add_parser("snapshot")
    snapshot.add_argument("label")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    configure()
    if args.command == "freeze":
        freeze()
        print("v1.3 claim-partition contract frozen")
        return 0
    if args.command == "self-test":
        freeze()
        self_test()
        print("v1.3 claim-partition validator self-test passed")
        return 0
    if args.command == "preflight":
        freeze()
        preflight()
        print("v1.3 claim-partition preflight passed")
        return 0
    if args.command == "run-all":
        return run_all()
    if args.command == "report":
        report()
        print(RESULT_RECORD)
        return 0
    if args.command == "manifest":
        manifest()
        print("manifest verified")
        return 0
    if args.command == "snapshot":
        return base.capture_snapshot(args.label)
    raise AssertionError(args.command)


if __name__ == "__main__":
    sys.exit(main())
