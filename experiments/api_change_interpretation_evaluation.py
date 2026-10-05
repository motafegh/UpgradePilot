"""Measured local evaluation of the frozen source-only development inputs.

No semantic oracle runs here. Calibration is explicitly weaker than ordinary
acquisition. Requests, HTTP frames and unreviewed results stay under ignored
.tmp/; reviewed public outcomes belong to the cycle evidence owner. The optional
LM Studio SDK is evaluation tooling, not a product/project dependency.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from dataclasses import asdict
from importlib.metadata import version
from pathlib import Path

from .api_change_interpretation import (
    ASSETS,
    LOCAL_MODEL,
    OUTPUT_TOKENS,
    ROLE,
    LocalInterpretationProvider,
    RequestCapacityEvidence,
    interpret_source_input,
    packet_hash,
    prepare_request,
    source_input_from_projection,
    strict_json,
    text_hash,
)
from .api_change_interpretation_trial import (
    PACKET_KIND,
    dependency_interval,
    read_saved_trial,
    save_trial,
)

ROOT = Path(__file__).resolve().parents[1]
HISTORICAL_CONTEXT = (
    ROOT
    / "working-memory/evidence/2026-10-04-ordered-scoped-bindings/live-pr-context.json"
)


def calibration_source_input(item: dict, ordinary_context: dict) -> dict:
    """Verify frozen source maps without giving calibration acquired authority."""
    if item["role_version"] != ROLE:
        raise ValueError("unexpected calibration role")
    scope = item["scope"]
    sections = item["sections"]
    for index, section in enumerate(sections, 1):
        text = section["text"]
        if section["section_id"] != f"S{index}" or section["sha256"] != text_hash(text):
            raise ValueError("calibration section identity/hash mismatch")
        offset = section["start_offset"]
        expected_lines = []
        for number, line in enumerate(text.splitlines(keepends=True), 1):
            expected_lines.append(
                {
                    "line_id": f"S{index}:L{number}",
                    "source_line_number": section["start_line"] + number - 1,
                    "start_offset": offset,
                    "end_offset": offset + len(line),
                    "text": line,
                }
            )
            offset += len(line)
        if section["lines"] != expected_lines or offset != section["end_offset"]:
            raise ValueError("calibration line map/range mismatch")
    if scope["mode"] == "acquired_window":
        normal = source_input_from_projection(
            ordinary_context["upstream"],
            dependency_interval(ordinary_context["dependency"]),
        )
        if len(normal["sections"]) != len(sections):
            raise ValueError("frozen acquisition differs from retained ordinary source")
        for actual, frozen in zip(normal["sections"], sections, strict=True):
            if any(
                actual[key] != frozen[key]
                for key in (
                    "text",
                    "lines",
                    "sha256",
                    "release_version",
                    "start_offset",
                    "end_offset",
                    "start_line",
                    "section_id",
                )
            ) or any(
                actual["source_identity"][key] != frozen["source_identity"][key]
                for key in actual["source_identity"]
            ):
                raise ValueError("frozen acquisition source identity/map mismatch")
        return normal
    if scope["complete_window_eligible"]:
        raise ValueError("calibration cannot claim complete ordinary acquisition")
    return {
        "role_version": ROLE,
        "interval": {
            "package": None,
            "old_version": None,
            "proposed_version": None,
            "scope": "source-only calibration; no target dependency interval supplied",
        },
        "source_identity": {
            "input_mode": scope["mode"],
            "section_source_identities": [s["source_identity"] for s in sections],
        },
        "source_coverage": scope,
        "sections": sections,
    }


def measured_capacity(
    request, model, chat_factory, *, template_identity: str
) -> tuple[RequestCapacityEvidence, dict]:
    """Use the loaded model's own template/tokenizer; account schema separately.

    The SDK represents structured output as prediction configuration, distinct
    from chat text. Tokenizing the complete response-format JSON supplies an
    additional conservative schema allowance, not a claimed exact server prompt.
    Provider-reported prompt usage is checked against this allowance after each
    call; disagreement stops the batch rather than silently trusting the estimate.
    """
    info = model.get_info().to_dict()
    if info["identifier"] != LOCAL_MODEL or info["modelKey"] != LOCAL_MODEL:
        raise ValueError("loaded model differs from maintained pilot")
    formatted = model.apply_prompt_template(
        chat_factory({"messages": request.payload["messages"]})
    )
    chat_tokens = len(model.tokenize(formatted))
    schema_tokens = len(
        model.tokenize(
            json.dumps(
                request.payload["response_format"], sort_keys=True, ensure_ascii=False
            )
        )
    )
    capacity = RequestCapacityEvidence(
        request_sha256=packet_hash(request.payload),
        model=LOCAL_MODEL,
        deployment_identity=info["instanceReference"],
        tokenizer_identity=f"{info['modelKey']}:{info['path']}:{info['instanceReference']}",
        template_identity=template_identity,
        accounting_method="loaded-model SDK chat template/tokenization plus SDK-tokenized full response-format JSON allowance; provider usage cross-check",
        effective_context_tokens=model.get_context_length(),
        input_tokens=chat_tokens + schema_tokens,
        reserved_output_tokens=OUTPUT_TOKENS,
    )
    return capacity, {
        "chat_template_tokens": chat_tokens,
        "schema_token_allowance": schema_tokens,
        "formatted_chat_sha256": text_hash(formatted),
        "fits": capacity.input_tokens + OUTPUT_TOKENS
        <= capacity.effective_context_tokens,
    }


def prepare_evaluation(
    output: Path, model, chat_factory, *, template_identity: str
) -> tuple[list, dict, dict]:
    """Freeze all request/code/input identities before any model prediction."""
    output.mkdir(parents=True, exist_ok=False)
    freeze = json.loads((ASSETS / "freeze-manifest.json").read_text())
    for name, record in freeze["files"].items():
        raw = (ASSETS / name).read_bytes()
        if (
            len(raw) != record["bytes"]
            or hashlib.sha256(raw).hexdigest() != record["sha256"]
        ):
            raise ValueError("prepared development artifact changed")
    inputs = json.loads((ASSETS / "source-inputs-v1.json").read_text())["inputs"]
    context = json.loads(HISTORICAL_CONTEXT.read_text())
    cases = []
    for item in inputs:
        source_input = calibration_source_input(item, context)
        request = prepare_request(source_input)
        if source_input["sections"]:
            capacity, counts = measured_capacity(
                request, model, chat_factory, template_identity=template_identity
            )
        else:
            capacity, counts = None, {"fits": False, "no_inference_control": True}
        cases.append(
            {
                "input_id": item["input_id"],
                "source_input": source_input,
                "request": request,
                "capacity": capacity,
                "counts": counts,
            }
        )
        (output / f"{item['input_id']}-request.json").write_text(
            json.dumps(request.payload, ensure_ascii=False)
        )
    manifest = {
        "role_version": ROLE,
        "model_outputs_seen": False,
        "source_inputs_sha256": hashlib.sha256(
            (ASSETS / "source-inputs-v1.json").read_bytes()
        ).hexdigest(),
        "evaluation_expectations_sha256": hashlib.sha256(
            (ASSETS / "evaluation-cases-v1.json").read_bytes()
        ).hexdigest(),
        "historical_context_sha256": hashlib.sha256(
            HISTORICAL_CONTEXT.read_bytes()
        ).hexdigest(),
        "code_sha256": {
            name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
            for name in (
                "experiments/api_change_interpretation.py",
                "experiments/api_change_interpretation_trial.py",
                "experiments/api_change_interpretation_evaluation.py",
                "src/upgradepilot/upstream/support_drop_extractor.py",
            )
        },
        "requests": [
            {
                "input_id": c["input_id"],
                "method": c["request"].method,
                "capacity": asdict(c["capacity"]) if c["capacity"] else None,
                "counts": c["counts"],
            }
            for c in cases
        ],
        "review_class": "frozen assisted development; semantic review pending; no independent acceptance",
    }
    (output / "before-inference.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return cases, manifest, context


def execute_evaluation(cases: list, output: Path, model, context: dict) -> dict:
    """One serial pass, with local raw retention and no semantic scoring/retry."""
    results = []
    if not cases[0]["counts"]["fits"]:
        summary = {
            "state": "capacity_problem",
            "reason": "full_acquired_window_does_not_fit",
            "inference_attempts": 0,
            "results": [],
        }
        (output / "results.json").write_text(json.dumps(summary, indent=2) + "\n")
        return summary
    for case in cases:
        capacity = case["capacity"]
        if capacity is not None and (
            model.get_info().to_dict()["instanceReference"]
            != capacity.deployment_identity
            or model.get_context_length() != capacity.effective_context_tokens
        ):
            raise ValueError("deployment changed after capacity freeze")
        observed = {}

        def capture(status, raw):
            (output / f"{case['input_id']}-http-response.bin").write_bytes(raw)
            observed["http_status"] = status
            try:
                envelope = strict_json(raw.decode("utf-8"))
                observed["usage"] = envelope.get("usage")
                observed["finish_reason"] = envelope.get("choices", [{}])[0].get(
                    "finish_reason"
                )
            except (
                ValueError,
                KeyError,
                TypeError,
                AttributeError,
                IndexError,
                RecursionError,
            ):
                observed["envelope_problem"] = True

        provider = LocalInterpretationProvider(
            capacity=capacity, response_observer=capture
        )
        start = time.monotonic()
        result = interpret_source_input(case["source_input"], provider)
        usage = observed.get("usage") or {}
        prompt_tokens = usage.get("prompt_tokens")
        accounting_mismatch = (
            capacity is not None
            and type(prompt_tokens) is int
            and prompt_tokens > capacity.input_tokens
        )
        record = {
            "input_id": case["input_id"],
            "elapsed_seconds": round(time.monotonic() - start, 3),
            "inference_attempted": capacity is not None and case["counts"]["fits"],
            "provider": observed,
            "capacity_accounting_mismatch": accounting_mismatch,
            "interpretation": result,
            "semantic_review": "pending",
        }
        (output / f"{case['input_id']}-result.json").write_text(
            json.dumps(record, indent=2, ensure_ascii=False) + "\n"
        )
        results.append(record)
        if (
            case["source_input"]["source_coverage"].get("acquisition_coverage")
            is not None
        ):
            body = {
                "artifact_kind": PACKET_KIND,
                "packet_version": 1,
                "proof": "historical ordinary acquisition plus real model proposal; no semantic acceptance",
                "context": context,
                "interpretation": result,
            }
            packet = {**body, "packet_sha256": packet_hash(body)}
            path = output / f"{case['input_id']}-saved-trial.json"
            save_trial(packet, path)
            if packet_hash(read_saved_trial(path)) != packet_hash(packet):
                raise ValueError("live proposal saved recovery differs")
            record["saved_recovery_equal"] = True
        print(
            json.dumps(
                {
                    "input_id": case["input_id"],
                    "state": result["state"],
                    "observations": len(result["observations"]),
                    "elapsed_seconds": record["elapsed_seconds"],
                    "finish_reason": observed.get("finish_reason"),
                    "accounting_mismatch": accounting_mismatch,
                }
            ),
            flush=True,
        )
        if accounting_mismatch or observed.get("http_status", 200) >= 400:
            break
    state = "development_execution_finished"
    if any(r["capacity_accounting_mismatch"] for r in results):
        state = "capacity_accounting_problem"
    elif results[-1]["provider"].get("http_status", 200) >= 400:
        state = "provider_problem"
    summary = {
        "state": state,
        "inference_attempts": sum(r["inference_attempted"] for r in results),
        "results": results,
        "semantic_acceptance": False,
    }
    (output / "results.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n"
    )
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sdk-site", type=Path, help="optional isolated SDK site-packages"
    )
    parser.add_argument(
        "--name", required=True, help="new local run name; existing runs are preserved"
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="execute after all capacity/request identities are frozen",
    )
    args = parser.parse_args()
    if not re.fullmatch(r"[a-zA-Z0-9_-]{1,80}", args.name):
        parser.error("name must contain only letters, digits, underscore or hyphen")
    if args.sdk_site:
        sys.path.append(str(args.sdk_site.resolve()))
    for key in (
        "HTTP_PROXY",
        "HTTPS_PROXY",
        "ALL_PROXY",
        "http_proxy",
        "https_proxy",
        "all_proxy",
    ):
        os.environ.pop(key, None)
    os.environ["NO_PROXY"] = "127.0.0.1,localhost,::1"
    import lmstudio as lms

    lms.set_sync_api_timeout(30)
    output = ROOT / ".tmp/api-interpretation-live" / args.name
    with lms.Client("127.0.0.1:18080") as client:
        loaded = [m for m in client.llm.list_loaded() if m.identifier == LOCAL_MODEL]
        if len(loaded) != 1:
            raise ValueError(
                "exactly one maintained pilot instance must already be loaded"
            )
        model = loaded[0]
        load_config = model.get_load_config().to_dict()
        # Fingerprint actual template behaviour on a fixed probe, without
        # assuming an earlier load receipt still describes the current instance.
        probe = lms.Chat.from_history(
            {
                "messages": [
                    {"role": "system", "content": "Template identity probe."},
                    {"role": "user", "content": "Probe only; no prediction."},
                ]
            }
        )
        template_identity = packet_hash(
            {
                "deployment": model.get_info().to_dict()["instanceReference"],
                "load_config": load_config,
                "formatted_probe_sha256": text_hash(model.apply_prompt_template(probe)),
            }
        )
        cases, _manifest, context = prepare_evaluation(
            output, model, lms.Chat.from_history, template_identity=template_identity
        )
        runtime = {
            name: version(name)
            for name in ("lmstudio", "requests", "packaging", "httpx", "anyio")
        }
        (output / "runtime.json").write_text(
            json.dumps(
                {
                    "packages": runtime,
                    "model": model.get_info().to_dict(),
                    "load_config": load_config,
                    "template_identity_basis": "actual loaded-instance config and SDK-applied fixed chat probe",
                    "template_identity": template_identity,
                },
                indent=2,
            )
            + "\n"
        )
        print(
            json.dumps(
                {
                    "prepared": len(cases),
                    "fit_inputs": sum(c["counts"]["fits"] for c in cases),
                    "output": str(output),
                }
            ),
            flush=True,
        )
        if args.execute:
            summary = execute_evaluation(cases, output, model, context)
            return 1 if summary["state"] != "development_execution_finished" else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
