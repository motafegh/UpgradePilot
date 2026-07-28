#!/usr/bin/env python3
"""One-response completion-recovery diagnostic for Gemma E4B state contract v1.2.

This is dated evidence code under working-memory, not UpgradePilot product code.
It preserves the frozen v1.2 semantic contract and changes only max_tokens from
512 to 1024 while adding explicit truncation and GPU-baseline classification.
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
    / "working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-result.md"
)
V1_2_ROOT = ROOT.parent / "2026-07-28-gemma-e4b-state-contract-v1.2"
V1_2_HARNESS = V1_2_ROOT / "diagnostic.py"

spec = importlib.util.spec_from_file_location("upgradepilot_v1_2", V1_2_HARNESS)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not load prior v1.2 harness: {V1_2_HARNESS}")
v1_2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v1_2)

# Redirect the imported dated harness to this new evidence directory before use.
v1_2.ROOT = ROOT
base = v1_2.base
LMS_EXE = os.environ.get("LMS_EXE", v1_2.LMS_EXE)
CASE = dict(v1_2.GATE_A_CASE)
MAX_TOKENS = 1024
GPU_USED_MAX_MIB = 2000
GPU_FREE_MIN_MIB = 6000


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def configure() -> None:
    v1_2.configure()


def freeze() -> None:
    configure()
    v1_2.freeze()
    comparison_path = ROOT / "frozen-variable-comparison.json"
    comparison = json.loads(comparison_path.read_text(encoding="utf-8"))
    comparison["recovery_operation"] = "v1.2 completion recovery"
    comparison["prior_max_tokens"] = comparison.get("max_tokens")
    comparison["max_tokens"] = MAX_TOKENS
    comparison["changed_variables"] = ["max_tokens 512 -> 1024"]
    comparison["unchanged_variables"] = [
        "Gemma E4B model and Q4_K_XL quantization",
        "4096 context and load configuration",
        "parallelism 1",
        "Flash Attention and GPU KV-cache placement",
        "state-contract v1.2 complete prompt",
        "flat JSON Schema",
        "category/change-state matrix",
        "exact ambiguity source and revised oracle",
        "temperature 0 and seed 0",
        "non-streaming endpoint",
        "source grounding",
        "no Instructor or retry layer",
    ]
    comparison["required_preload_gpu_band"] = {
        "memory_used_mib_max": GPU_USED_MAX_MIB,
        "memory_free_mib_min": GPU_FREE_MIN_MIB,
    }
    base.write_json(comparison_path, comparison)
    base.write_json(ROOT / "frozen-recovery-case.json", CASE)


def self_test() -> None:
    configure()
    v1_2.self_test()
    valid = {
        "state": "resolved",
        "claims": [
            {
                "category": "interface_or_behavior_change",
                "subject": "compatibility behavior for older environments",
                "change_state": "changed_unspecified",
                "source_quote": CASE["text"],
            }
        ],
        "unresolved_reasons": [],
    }
    errors = v1_2.validate_structure_v1_2(valid, CASE["text"])
    semantic_errors = base.validate_semantics(CASE, valid)
    payload = {
        "structure_errors": errors,
        "semantic_errors": semantic_errors,
        "passed": not errors and not semantic_errors,
    }
    base.write_json(ROOT / "recovery-validator-self-test.json", payload)
    if not payload["passed"]:
        raise RuntimeError("completion-recovery validator self-test failed")


def query_gpu() -> dict[str, float]:
    command = [
        "nvidia-smi",
        "--query-gpu=memory.total,memory.used,memory.free,utilization.gpu,temperature.gpu",
        "--format=csv,noheader,nounits",
    ]
    completed = subprocess.run(command, text=True, capture_output=True, check=False)
    evidence = {
        "command": command,
        "exit_code": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }
    base.write_json(ROOT / "gpu-preflight-command.json", evidence)
    if completed.returncode != 0:
        raise RuntimeError(f"nvidia-smi preflight failed: {completed.stderr.strip()}")
    first_line = next((line.strip() for line in completed.stdout.splitlines() if line.strip()), "")
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


def preflight() -> None:
    configure()
    evidence: dict[str, Any] = {
        "captured_at": utc_now(),
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
        evidence["gpu"] = query_gpu()
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
    base.write_json(ROOT / "preflight.json", evidence)
    if failures:
        raise RuntimeError("; ".join(failures))


def run_once() -> int:
    configure()
    run_id = f"{CASE['id']}__completion_recovery_r1"
    run_dir = ROOT / "runs" / run_id
    payload = base.request_payload(CASE["text"], max_tokens=MAX_TOKENS)
    prompt_identity = {
        "system_prompt_sha256": hashlib.sha256(base.SYSTEM_PROMPT.encode()).hexdigest(),
        "schema_sha256": hashlib.sha256(
            json.dumps(base.SCHEMA, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
        "request_sha256": hashlib.sha256(
            json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
    }
    base.write_json(run_dir / "request.json", payload)
    base.write_text(run_dir / "source.txt", CASE["text"])
    result: dict[str, Any] = {
        "run_id": run_id,
        "phase": "state-contract-v1.2-completion-recovery",
        "case_id": CASE["id"],
        "repetition": 1,
        "started_at": utc_now(),
        "model": base.MODEL,
        "temperature": 0,
        "seed": 0,
        "max_tokens": MAX_TOKENS,
        "stream": False,
        "prompt_identity": prompt_identity,
        "first_token_latency_seconds": None,
        "first_token_latency_note": "Unavailable because the required request is non-streaming.",
        "runtime_errors": [],
        "structure_errors": [],
        "semantic_errors": [],
    }
    try:
        raw, elapsed = base.post_completion(payload, timeout=360.0)
        raw_text = raw.decode("utf-8", errors="replace")
        base.write_text(run_dir / "outer-response.raw.json", raw_text)
        outer = json.loads(raw)
        base.write_json(run_dir / "outer-response.json", outer)

        choices = outer.get("choices")
        if not isinstance(choices, list) or not choices or not isinstance(choices[0], dict):
            raise ValueError("outer response has no usable first choice")
        choice = choices[0]
        finish_reason = choice.get("finish_reason")
        message = choice.get("message")
        if not isinstance(message, dict):
            raise TypeError("outer response message is not an object")
        content = message.get("content")
        usage = outer.get("usage")
        result.update(
            {
                "completed_at": utc_now(),
                "total_latency_seconds": round(elapsed, 6),
                "finish_reason": finish_reason,
                "usage": usage,
                "content_type": type(content).__name__,
                "content_length": len(content) if isinstance(content, str) else None,
            }
        )

        if isinstance(content, str):
            base.write_text(run_dir / "inner-content.raw.txt", content)
        if finish_reason == "length":
            result["classification"] = "truncation"
            result["runtime_errors"].append(
                "finish_reason was length; completion budget exhausted before a complete structured result"
            )
            if not isinstance(content, str) or not content.strip():
                result["runtime_errors"].append("assistant structured content was empty")
            result["pass"] = False
        elif not isinstance(content, str):
            result["classification"] = "invalid_outer_content"
            result["runtime_errors"].append("assistant structured content was not text")
            result["pass"] = False
        elif not content.strip():
            result["classification"] = "empty_content"
            result["runtime_errors"].append("assistant structured content was empty")
            result["pass"] = False
        else:
            inner = json.loads(content)
            base.write_json(run_dir / "inner-content.json", inner)
            structure_errors = v1_2.validate_structure_v1_2(inner, CASE["text"])
            semantic_errors = base.validate_semantics(CASE, inner) if not structure_errors else []
            result.update(
                {
                    "inner": inner,
                    "structure_errors": structure_errors,
                    "semantic_errors": semantic_errors,
                    "structure_pass": not structure_errors,
                    "semantic_pass": not semantic_errors,
                    "classification": (
                        "complete_correct"
                        if not structure_errors and not semantic_errors
                        else "complete_semantic_or_contract_failure"
                    ),
                    "pass": not structure_errors and not semantic_errors,
                }
            )
    except Exception as exc:
        result.update(
            {
                "completed_at": utc_now(),
                "classification": "request_or_parse_failure",
                "pass": False,
                "exception_type": type(exc).__name__,
                "exception": str(exc),
            }
        )

    base.write_json(run_dir / "validation.json", result)
    base.write_json(
        ROOT / "completion-recovery-summary.json",
        {
            "completed": True,
            "passed": bool(result.get("pass")),
            "classification": result.get("classification"),
            "stop_reason": "Authorized one-response completion-recovery stop line reached",
            "results": [result],
        },
    )
    print(f"RECOVERY {result.get('classification')} {run_id}", flush=True)
    return 0


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def report() -> None:
    summary = read_json(
        ROOT / "completion-recovery-summary.json",
        {"passed": False, "classification": "not_run", "results": []},
    )
    result = summary.get("results", [{}])[0] if summary.get("results") else {}
    preflight_result = read_json(ROOT / "preflight.json", {})
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
    gpu = preflight_result.get("gpu", {})
    classification = summary.get("classification", "not_run")
    errors = (
        list(result.get("runtime_errors", []))
        + list(result.get("structure_errors", []))
        + list(result.get("semantic_errors", []))
    )
    if result.get("exception"):
        errors.append(f"{result.get('exception_type')}: {result.get('exception')}")
    error_text = "\n".join(f"- {item}" for item in errors) if errors else "- none"
    inner = result.get("inner")
    inner_text = json.dumps(inner, indent=2, ensure_ascii=False) if inner is not None else "not produced"

    text = f"""# B2 Gemma E4B v1.2 Completion-Recovery Result

**Date:** 2026-07-29  
**Operation:** Recover one complete state-contract v1.2 response under the required GPU baseline  
**Selected review:** [`2026-07-28_B2-gemma-e4b-v1.2-truncation-and-resource-baseline-review.md`](2026-07-28_B2-gemma-e4b-v1.2-truncation-and-resource-baseline-review.md)  
**Raw evidence:** [`evidence/2026-07-29-gemma-e4b-v1.2-completion-recovery/`](evidence/2026-07-29-gemma-e4b-v1.2-completion-recovery/)  
**Result classification:** {classification}; independent review pending; no model or product adoption

## Compact result

```text
preflight passed: {preflight_result.get('passed')}
pre-load GPU used: {gpu.get('memory_used_mib')} MiB
pre-load GPU free: {gpu.get('memory_free_mib')} MiB
finish reason: {result.get('finish_reason')}
completion tokens: {(result.get('usage') or {}).get('completion_tokens') if isinstance(result.get('usage'), dict) else None}
classification: {classification}
semantic pass: {result.get('semantic_pass')}
product-test exit: {test_exit}
product-test count: {test_count}
```

## Frozen change

Only the request completion budget changed:

```text
max_tokens: 512 -> 1024
```

The Gemma model, quantization, 4096 context, load configuration, v1.2 prompt,
flat schema, category/change-state matrix, exact source and oracle, temperature,
seed, endpoint, grounding, and no-Instructor/no-retry boundary remained frozen.

## Structured result

```json
{inner_text}
```

## Errors or stop classification

{error_text}

## Restoration and validation

Load, resource snapshots, request, outer response, reasoning/logs, validation,
unload, product-test output, repository status, and hashes are preserved in the
evidence directory. `MEMORY.md` was not modified by the runner; independent
review must update the sole live-state owner.
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
    sub.add_parser("preflight")
    sub.add_parser("run")
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
        print("v1.2 completion-recovery contract frozen")
        return 0
    if args.command == "self-test":
        freeze()
        self_test()
        print("completion-recovery validator self-test passed")
        return 0
    if args.command == "preflight":
        freeze()
        preflight()
        print("completion-recovery preflight passed")
        return 0
    if args.command == "run":
        return run_once()
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
