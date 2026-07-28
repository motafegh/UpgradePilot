#!/usr/bin/env python3
"""Run the frozen Gemma E4B state-contract v1.2 Gates B and C."""

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
RESULT_RECORD = REPO_ROOT / "working-memory/2026-07-29_B2-gemma-e4b-v1.2-gates-b-c-result.md"
PRIOR_HARNESS = ROOT.parent / "2026-07-29-gemma-e4b-v1.2-completion-recovery" / "diagnostic.py"
GATE_A_REVIEW_COMMIT = "e9e3f0a6ba9480f334ec43835c5f9d76677332f8"
GATE_A_EVIDENCE_COMMIT = "bb32fcd1c3858a9a88811efd6d42a9278dc5fa58"
SUMMARY_B = ROOT / "gate-b-summary.json"
SUMMARY_C = ROOT / "gate-c-summary.json"

spec = importlib.util.spec_from_file_location("upgradepilot_recovery_for_gates_bc", PRIOR_HARNESS)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not load prior harness: {PRIOR_HARNESS}")
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)

prior.ROOT = ROOT
prior.RESULT_RECORD = RESULT_RECORD
prior.v1_2.ROOT = ROOT
prior.base.ROOT = ROOT
base = prior.base
v1_2 = prior.v1_2
LMS_EXE = os.environ.get("LMS_EXE", prior.LMS_EXE)
GATE_B_CASES = [copy.deepcopy(case) for case in v1_2.GATE_B_CASES]
GATE_C_CASE = copy.deepcopy(v1_2.GATE_C_CASE)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def read_json(path: Path, default: Any) -> Any:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def configure() -> None:
    prior.configure()


def freeze() -> None:
    configure()
    prior.freeze()
    path = ROOT / "frozen-variable-comparison.json"
    value = read_json(path, {})
    value.update({
        "gate_operation": "state-contract v1.2 Gates B and C",
        "gate_a_review_commit": GATE_A_REVIEW_COMMIT,
        "gate_a_evidence_commit": GATE_A_EVIDENCE_COMMIT,
        "changed_variables_from_accepted_gate_a": [],
        "max_tokens": 1024,
        "gate_b_cases": GATE_B_CASES,
        "gate_c_case": GATE_C_CASE,
        "stop_on_first_failure": True,
        "gate_c_requires_gate_b_pass": True,
        "instructor_used": False,
        "retries": 0,
    })
    write_json(path, value)
    write_json(ROOT / "gates-b-c-plan.json", {
        "gate_a_review_commit": GATE_A_REVIEW_COMMIT,
        "gate_a_evidence_commit": GATE_A_EVIDENCE_COMMIT,
        "gate_b_cases": GATE_B_CASES,
        "gate_c_case": GATE_C_CASE,
        "stop_on_first_failure": True,
        "gate_c_requires_gate_b_pass": True,
    })


def self_test() -> None:
    configure()
    prior.self_test()
    result = read_json(ROOT / "recovery-validator-self-test.json", {})
    result.update({"gate": "state-contract-v1.2-gates-b-c", "gate_b_case_count": 5, "gate_c_case_count": 1})
    write_json(ROOT / "gates-b-c-validator-self-test.json", result)
    if not result.get("passed"):
        raise RuntimeError("Gates B/C validator self-test failed")


def preflight() -> None:
    configure()
    prior.preflight()


def run_case(case: dict[str, Any], gate: str, ordinal: int) -> dict[str, Any]:
    configure()
    prior.CASE = copy.deepcopy(case)
    temporary_id = f"{case['id']}__completion_recovery_r1"
    temporary_dir = ROOT / "runs" / temporary_id
    temporary_summary = ROOT / "completion-recovery-summary.json"
    if temporary_dir.exists() or temporary_summary.exists():
        raise RuntimeError("Temporary inherited evidence exists and will not be overwritten")

    prior.run_once()
    inherited = read_json(temporary_summary, {})
    results = inherited.get("results", [])
    if len(results) != 1:
        raise RuntimeError("Inherited harness did not produce exactly one result")

    result = dict(results[0])
    final_id = f"{case['id']}__{gate}_r1"
    final_dir = ROOT / "runs" / final_id
    if final_dir.exists():
        raise RuntimeError(f"Final evidence exists and will not be overwritten: {final_dir}")
    temporary_dir.rename(final_dir)
    temporary_summary.unlink()
    result.update({"run_id": final_id, "phase": f"state-contract-v1.2-{gate}", "gate": gate, "ordinal": ordinal})
    write_json(final_dir / "validation.json", result)
    print(f"{gate.upper()} {result.get('classification')} {final_id}", flush=True)
    return result


def run_gate_b() -> int:
    if SUMMARY_B.exists():
        raise RuntimeError("Gate B summary already exists")
    results: list[dict[str, Any]] = []
    for ordinal, case in enumerate(GATE_B_CASES, start=1):
        result = run_case(case, "gate_b", ordinal)
        results.append(result)
        if not result.get("pass"):
            write_json(SUMMARY_B, {"completed": False, "passed": False, "stop_reason": f"Gate B failed at {case['id']}", "results": results})
            return 2
    write_json(SUMMARY_B, {"completed": True, "passed": True, "stop_reason": None, "results": results})
    return 0


def run_gate_c() -> int:
    gate_b = read_json(SUMMARY_B, {})
    if gate_b.get("passed") is not True:
        raise RuntimeError("Gate B has not passed; Gate C is not authorized")
    if SUMMARY_C.exists():
        raise RuntimeError("Gate C summary already exists")
    result = run_case(GATE_C_CASE, "gate_c", 1)
    write_json(SUMMARY_C, {
        "completed": bool(result.get("pass")),
        "passed": bool(result.get("pass")),
        "stop_reason": "Authorized v1.2 stop line reached" if result.get("pass") else "Gate C conflicting-support case failed",
        "results": [result],
    })
    return 0 if result.get("pass") else 2


def format_result(result: dict[str, Any]) -> str:
    usage = result.get("usage") if isinstance(result.get("usage"), dict) else {}
    details = usage.get("completion_tokens_details") if isinstance(usage.get("completion_tokens_details"), dict) else {}
    inner = result.get("inner")
    inner_text = json.dumps(inner, indent=2, ensure_ascii=False) if inner is not None else "not produced"
    errors = list(result.get("runtime_errors", [])) + list(result.get("structure_errors", [])) + list(result.get("semantic_errors", []))
    if result.get("exception"):
        errors.append(f"{result.get('exception_type')}: {result.get('exception')}")
    error_text = "\n".join(f"- {item}" for item in errors) if errors else "- none"
    return f"""### `{result.get('case_id')}`

```text
finish reason: {result.get('finish_reason')}
completion tokens: {usage.get('completion_tokens')}
reasoning tokens: {details.get('reasoning_tokens')}
latency seconds: {result.get('total_latency_seconds')}
classification: {result.get('classification')}
structure pass: {result.get('structure_pass')}
semantic pass: {result.get('semantic_pass')}
```

```json
{inner_text}
```

Errors:

{error_text}
"""


def report() -> None:
    gate_b = read_json(SUMMARY_B, {"passed": False, "results": []})
    gate_c = read_json(SUMMARY_C, {"passed": False, "results": []})
    test_exit = (ROOT / "product-tests.exit-code.txt").read_text(encoding="utf-8").strip() if (ROOT / "product-tests.exit-code.txt").exists() else "missing"
    test_output = ""
    for path in (ROOT / "product-tests.stdout.txt", ROOT / "product-tests.stderr.txt"):
        if path.exists():
            test_output += path.read_text(encoding="utf-8", errors="replace") + "\n"
    match = re.search(r"Ran\s+(\d+)\s+tests?", test_output)
    test_count = match.group(1) if match else "unknown"
    outcome = "Gate B failed or did not complete" if gate_b.get("passed") is not True else ("Gate B passed; Gate C failed or did not complete" if gate_c.get("passed") is not True else "Gates B and C passed")
    gate_b_text = "\n".join(format_result(item) for item in gate_b.get("results", [])) or "No Gate B case completed."
    gate_c_text = "\n".join(format_result(item) for item in gate_c.get("results", [])) or "Gate C was not run."
    text = f"""# B2 Gemma E4B State-Contract v1.2 Gates B and C Result

**Date:** 2026-07-29  
**Operation:** Execute the frozen v1.2 contrast suite and, conditionally, the conflicting-support case  
**Gate A review:** commit `{GATE_A_REVIEW_COMMIT}`  
**Gate A evidence:** commit `{GATE_A_EVIDENCE_COMMIT}`  
**Raw evidence:** [`evidence/2026-07-29-gemma-e4b-v1.2-gates-b-c/`](evidence/2026-07-29-gemma-e4b-v1.2-gates-b-c/)  
**Result classification:** {outcome}; independent review pending; no model or product adoption

## Compact result

```text
Gate B completed: {gate_b.get('completed')}
Gate B passed: {gate_b.get('passed')}
Gate B stop reason: {gate_b.get('stop_reason')}
Gate C completed: {gate_c.get('completed')}
Gate C passed: {gate_c.get('passed')}
Gate C stop reason: {gate_c.get('stop_reason')}
product-test exit: {test_exit}
product-test count: {test_count}
```

## Gate B

{gate_b_text}

## Gate C

{gate_c_text}

## Frozen boundary

The model, quantization, context, runtime configuration, v1.2 prompt, flat schema,
category/change-state matrix, frozen source cases and oracles, `max_tokens=1024`,
temperature, seed, endpoint, grounding, no-Instructor boundary, and no-retry
boundary remained frozen from the independently accepted Gate A run.

## Restoration and review boundary

Load, snapshots, requests, responses, reasoning/logs, validation, unload, product
tests, repository status, hashes, and manifest verification are preserved.
`MEMORY.md` was not modified. Stop and push the first result for independent
review before broader evaluation or product integration.
"""
    RESULT_RECORD.write_text(text, encoding="utf-8")
    (ROOT / "result-record.sha256").write_text(f"{sha256_file(RESULT_RECORD)}  {RESULT_RECORD.name}\n", encoding="utf-8")


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
    (ROOT / "manifest-verification.txt").write_text("\n".join(verification) + f"\n\nverified={passed}\ncount={len(lines)}\n", encoding="utf-8")
    if not passed:
        raise RuntimeError("manifest verification failed")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("freeze", "self-test", "preflight", "gate-b", "gate-c", "report", "manifest"):
        sub.add_parser(name)
    snapshot = sub.add_parser("snapshot")
    snapshot.add_argument("label")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    configure()
    if args.command == "freeze": freeze(); print("v1.2 Gates B/C contract frozen"); return 0
    if args.command == "self-test": freeze(); self_test(); print("v1.2 Gates B/C validator self-test passed"); return 0
    if args.command == "preflight": freeze(); preflight(); print("v1.2 Gates B/C preflight passed"); return 0
    if args.command == "gate-b": return run_gate_b()
    if args.command == "gate-c": return run_gate_c()
    if args.command == "report": report(); print(RESULT_RECORD); return 0
    if args.command == "manifest": manifest(); print("manifest verified"); return 0
    if args.command == "snapshot": return base.capture_snapshot(args.label)
    raise AssertionError(args.command)


if __name__ == "__main__":
    sys.exit(main())
