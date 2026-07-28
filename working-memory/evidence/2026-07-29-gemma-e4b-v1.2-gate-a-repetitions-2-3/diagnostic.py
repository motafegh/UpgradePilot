#!/usr/bin/env python3
"""Run Gemma E4B state-contract v1.2 Gate A repetitions 2 and 3.

This is dated evidence code, not UpgradePilot product code. It delegates each
model request and all semantic validation to the accepted completion-recovery
harness, then relocates and labels the resulting evidence as repetitions 2 and
3. Each repetition receives a separate clean-resource preflight and model
load/unload lifecycle through run.sh.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[2]
RESULT_RECORD = (
    REPO_ROOT
    / "working-memory/2026-07-29_B2-gemma-e4b-v1.2-gate-a-repetitions-2-3-result.md"
)
PRIOR_HARNESS = (
    ROOT.parent
    / "2026-07-29-gemma-e4b-v1.2-completion-recovery"
    / "diagnostic.py"
)
ACCEPTED_REPETITION_1_COMMIT = "154d83a3ad0741dc60262f0deaafed07d0536669"
ACCEPTED_REPETITION_1_EVIDENCE = (
    "evidence/2026-07-29-gemma-e4b-v1.2-completion-recovery-load-flag-correction/"
)
GPU_USED_MAX_MIB = 2000
GPU_FREE_MIN_MIB = 6000
REPETITIONS = (2, 3)
SUMMARY_PATH = ROOT / "gate-a-repetitions-summary.json"

spec = importlib.util.spec_from_file_location(
    "upgradepilot_completion_recovery_for_gate_a", PRIOR_HARNESS
)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not load accepted completion-recovery harness: {PRIOR_HARNESS}")
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)

# Redirect all inherited dated-harness outputs into this new immutable bundle.
prior.ROOT = ROOT
prior.RESULT_RECORD = RESULT_RECORD
prior.v1_2.ROOT = ROOT
prior.base.ROOT = ROOT

base = prior.base
v1_2 = prior.v1_2
CASE = dict(prior.CASE)
LMS_EXE = os.environ.get("LMS_EXE", prior.LMS_EXE)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


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
    prior.configure()


def freeze() -> None:
    """Freeze the accepted repetition-1 request and validator without changes."""

    configure()
    prior.freeze()
    path = ROOT / "frozen-variable-comparison.json"
    value = read_json(path, {})
    value["gate_operation"] = "state-contract v1.2 Gate A repetitions 2 and 3"
    value["accepted_repetition_1"] = {
        "commit": ACCEPTED_REPETITION_1_COMMIT,
        "evidence": ACCEPTED_REPETITION_1_EVIDENCE,
        "result": "complete_correct",
    }
    value["historical_recovery_change"] = "max_tokens 512 -> 1024"
    value["changed_variables_from_accepted_repetition_1"] = []
    value["repetitions"] = list(REPETITIONS)
    value["required_preload_gpu_band_per_repetition"] = {
        "memory_used_mib_max": GPU_USED_MAX_MIB,
        "memory_free_mib_min": GPU_FREE_MIN_MIB,
        "loaded_models_required": 0,
    }
    write_json(path, value)
    write_json(
        ROOT / "gate-a-plan.json",
        {
            "accepted_repetition_1_commit": ACCEPTED_REPETITION_1_COMMIT,
            "case": CASE,
            "repetitions": list(REPETITIONS),
            "stop_on_first_failure": True,
            "gate_b_included": False,
            "instructor_used": False,
            "retries": 0,
        },
    )


def self_test() -> None:
    configure()
    prior.self_test()
    inherited = read_json(ROOT / "recovery-validator-self-test.json", {})
    inherited["gate"] = "state-contract-v1.2-gate-a"
    inherited["repetitions"] = list(REPETITIONS)
    write_json(ROOT / "gate-a-validator-self-test.json", inherited)
    if not inherited.get("passed"):
        raise RuntimeError("Gate A validator self-test failed")


def query_gpu(repetition: int) -> dict[str, float]:
    command = [
        "nvidia-smi",
        "--query-gpu=memory.total,memory.used,memory.free,utilization.gpu,temperature.gpu",
        "--format=csv,noheader,nounits",
    ]
    completed = subprocess.run(command, text=True, capture_output=True, check=False)
    write_json(
        ROOT / f"gpu-preflight-command-r{repetition}.json",
        {
            "command": command,
            "exit_code": completed.returncode,
            "stdout": completed.stdout,
            "stderr": completed.stderr,
        },
    )
    if completed.returncode != 0:
        raise RuntimeError(f"nvidia-smi preflight failed: {completed.stderr.strip()}")
    first_line = next(
        (line.strip() for line in completed.stdout.splitlines() if line.strip()), ""
    )
    parts = [part.strip() for part in first_line.split(",")]
    if len(parts) != 5:
        raise RuntimeError(f"Unexpected nvidia-smi output: {first_line!r}")
    total, used, free, utilization, temperature = (float(part) for part in parts)
    return {
        "memory_total_mib": total,
        "memory_used_mib": used,
        "memory_free_mib": free,
        "utilization_percent": utilization,
        "temperature_c": temperature,
    }


def preflight(repetition: int) -> None:
    configure()
    evidence: dict[str, Any] = {
        "captured_at": utc_now(),
        "gate": "state-contract-v1.2-gate-a",
        "repetition": repetition,
        "repo_root": str(REPO_ROOT),
        "python": sys.executable,
        "lms_exe": LMS_EXE,
        "lms_exe_exists": Path(LMS_EXE).exists(),
        "base_url": base.BASE_URL,
        "required_gpu_band": {
            "memory_used_mib_max": GPU_USED_MAX_MIB,
            "memory_free_mib_min": GPU_FREE_MIN_MIB,
        },
    }
    failures: list[str] = []
    try:
        evidence["loaded_instances"] = v1_2.loaded_instances()
        evidence["server_reachable"] = True
    except Exception as exc:
        evidence["loaded_instances"] = []
        evidence["server_reachable"] = False
        evidence["server_error"] = repr(exc)
        failures.append("LM Studio server is not reachable")
    try:
        evidence["gpu"] = query_gpu(repetition)
    except Exception as exc:
        evidence["gpu_error"] = repr(exc)
        failures.append("GPU state could not be measured")

    if not evidence["lms_exe_exists"]:
        failures.append(f"LM Studio CLI not found: {LMS_EXE}")
    if evidence.get("loaded_instances"):
        failures.append(f"another LM Studio model is loaded: {evidence['loaded_instances']}")
    gpu = evidence.get("gpu")
    if isinstance(gpu, dict):
        if gpu["memory_used_mib"] > GPU_USED_MAX_MIB:
            failures.append(
                f"GPU used {gpu['memory_used_mib']:.0f} MiB exceeds {GPU_USED_MAX_MIB} MiB"
            )
        if gpu["memory_free_mib"] < GPU_FREE_MIN_MIB:
            failures.append(
                f"GPU free {gpu['memory_free_mib']:.0f} MiB is below {GPU_FREE_MIN_MIB} MiB"
            )
    evidence["passed"] = not failures
    evidence["failures"] = failures
    write_json(ROOT / f"preflight-r{repetition}.json", evidence)
    if failures:
        raise RuntimeError("; ".join(failures))


def run_repetition(repetition: int) -> None:
    """Run the unchanged accepted request/validator and relabel its evidence."""

    if repetition not in REPETITIONS:
        raise ValueError(f"Unsupported repetition: {repetition}")

    summary = read_json(
        SUMMARY_PATH,
        {
            "gate": "state-contract-v1.2-gate-a",
            "accepted_repetition_1": {
                "commit": ACCEPTED_REPETITION_1_COMMIT,
                "evidence": ACCEPTED_REPETITION_1_EVIDENCE,
                "pass": True,
            },
            "results": [],
        },
    )
    if any(item.get("repetition") == repetition for item in summary.get("results", [])):
        raise RuntimeError(f"Repetition {repetition} already exists and will not be overwritten")

    temporary_id = f"{CASE['id']}__completion_recovery_r1"
    temporary_dir = ROOT / "runs" / temporary_id
    temporary_summary = ROOT / "completion-recovery-summary.json"
    if temporary_dir.exists() or temporary_summary.exists():
        raise RuntimeError("Temporary inherited evidence already exists and will not be overwritten")

    prior.run_once()
    inherited = read_json(temporary_summary, {})
    inherited_results = inherited.get("results", [])
    if len(inherited_results) != 1:
        raise RuntimeError("Inherited completion-recovery harness did not produce one result")

    result = dict(inherited_results[0])
    final_id = f"{CASE['id']}__gate_a_r{repetition}"
    final_dir = ROOT / "runs" / final_id
    if final_dir.exists():
        raise RuntimeError(f"Final repetition directory already exists: {final_dir}")
    temporary_dir.rename(final_dir)
    temporary_summary.unlink()

    result.update(
        {
            "run_id": final_id,
            "phase": "state-contract-v1.2-gate-a-repetitions",
            "case_id": CASE["id"],
            "repetition": repetition,
        }
    )
    write_json(final_dir / "validation.json", result)

    results = list(summary.get("results", []))
    results.append(result)
    results.sort(key=lambda item: item.get("repetition", 0))
    current_pass = all(bool(item.get("pass")) for item in results)
    completed = {item.get("repetition") for item in results}
    gate_complete = set(REPETITIONS).issubset(completed)
    gate_passed = gate_complete and current_pass

    if not result.get("pass"):
        classification = f"gate_a_stopped_at_repetition_{repetition}"
        stop_reason = "First Gate A failure reached the mandatory stop line"
    elif gate_passed:
        classification = "gate_a_3_of_3_passed"
        stop_reason = "Gate A completed; independent review required before Gate B"
    else:
        classification = f"gate_a_repetition_{repetition}_passed"
        stop_reason = "Continue only with the next authorized Gate A repetition"

    summary.update(
        {
            "updated_at": utc_now(),
            "results": results,
            "current_repetitions_passed": current_pass,
            "gate_complete": gate_complete,
            "gate_passed": gate_passed,
            "classification": classification,
            "stop_reason": stop_reason,
        }
    )
    write_json(SUMMARY_PATH, summary)
    print(f"GATE_A {classification} {final_id}", flush=True)


def result_passed(repetition: int) -> bool:
    summary = read_json(SUMMARY_PATH, {"results": []})
    return any(
        item.get("repetition") == repetition and bool(item.get("pass"))
        for item in summary.get("results", [])
    )


def report() -> None:
    summary = read_json(
        SUMMARY_PATH,
        {
            "classification": "not_run",
            "gate_complete": False,
            "gate_passed": False,
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

    sections: list[str] = []
    for result in summary.get("results", []):
        repetition = result.get("repetition")
        preflight_result = read_json(ROOT / f"preflight-r{repetition}.json", {})
        gpu = preflight_result.get("gpu", {})
        usage = result.get("usage") if isinstance(result.get("usage"), dict) else {}
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
        sections.append(
            f"""## Repetition {repetition}

```text
preflight passed: {preflight_result.get('passed')}
pre-load GPU used: {gpu.get('memory_used_mib')} MiB
pre-load GPU free: {gpu.get('memory_free_mib')} MiB
finish reason: {result.get('finish_reason')}
completion tokens: {usage.get('completion_tokens')}
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
        )

    sections_text = "\n".join(sections) if sections else "No repetitions were completed."
    text = f"""# B2 Gemma E4B v1.2 Gate A Repetitions 2 and 3 Result

**Date:** 2026-07-29  
**Operation:** Complete the two remaining identical Gate A repetitions under separately verified clean pre-load baselines  
**Accepted repetition 1:** commit `{ACCEPTED_REPETITION_1_COMMIT}`  
**Raw evidence:** [`evidence/2026-07-29-gemma-e4b-v1.2-gate-a-repetitions-2-3/`](evidence/2026-07-29-gemma-e4b-v1.2-gate-a-repetitions-2-3/)  
**Result classification:** {summary.get('classification')}; independent review pending; no model or product adoption

## Gate summary

```text
accepted repetition 1: passed
gate complete: {summary.get('gate_complete')}
gate passed: {summary.get('gate_passed')}
stop reason: {summary.get('stop_reason')}
product-test exit: {test_exit}
product-test count: {test_count}
```

The model, quantization, load configuration, v1.2 prompt, flat schema,
category/change-state matrix, source, oracle, `max_tokens=1024`, temperature,
seed, endpoint, grounding, no-Instructor boundary, and no-retry boundary remained
frozen from the independently accepted repetition-1 run.

{sections_text}

## Restoration and review boundary

Each attempted repetition has separate preflight, load, snapshots, request,
response, reasoning/logs, validation, unload, and restoration evidence. Product
tests, repository status, hashes, and manifest verification are preserved.

`MEMORY.md` was not modified. Stop and push this first result for independent
review before Gate B, broader evaluation, Qwen, Instructor, or product integration.
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
    lines = [f"{sha256_file(path)}  {path.relative_to(ROOT).as_posix()}" for path in paths]
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
    preflight_parser = sub.add_parser("preflight")
    preflight_parser.add_argument("repetition", type=int, choices=REPETITIONS)
    run_parser = sub.add_parser("run")
    run_parser.add_argument("repetition", type=int, choices=REPETITIONS)
    status_parser = sub.add_parser("result-passed")
    status_parser.add_argument("repetition", type=int, choices=REPETITIONS)
    sub.add_parser("report")
    sub.add_parser("manifest")
    snapshot_parser = sub.add_parser("snapshot")
    snapshot_parser.add_argument("label")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    configure()
    if args.command == "freeze":
        freeze()
        print("v1.2 Gate A repetition contract frozen")
        return 0
    if args.command == "self-test":
        freeze()
        self_test()
        print("v1.2 Gate A validator self-test passed")
        return 0
    if args.command == "preflight":
        freeze()
        preflight(args.repetition)
        print(f"Gate A repetition {args.repetition} preflight passed")
        return 0
    if args.command == "run":
        run_repetition(args.repetition)
        return 0
    if args.command == "result-passed":
        return 0 if result_passed(args.repetition) else 1
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
