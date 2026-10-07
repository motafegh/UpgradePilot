"""Saved-packet decoding contrast, separate from case-policy evaluation.

Private receipts retain requests/reasoning; the summary exposes only mechanism,
format and usage facts. No result changes the main provider or repairs old trials.
Run with the LM Studio SDK environment and PYTHONPATH=.:src.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from dataclasses import replace
from pathlib import Path

from .broader_agency_local import LocalJSONActionProvider
from .broader_agency_trial import ModelRequest, object_schema, validate_shape
from .broader_agency_workspace import SourceDocument, SourceWorkspace, strict_json


def save(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def comparable(config):
    fields = (
        "interface",
        "endpoint",
        "load_config",
        "reasoning",
        "reasoning_control",
        "temperature",
        "request_timeout_seconds",
        "accounting",
        "template_control_limit",
        "structured_path",
    )
    return {k: config[k] for k in fields} | {
        "model": {
            k: v
            for k, v in config["model"].items()
            if k not in {"identifier", "instanceReference"}
        }
    }


def candidate_check(text, schema, workspace=None):
    try:
        candidate = strict_json(text)
        validate_shape(candidate, schema)
        missing = workspace.validate_citations(candidate) if workspace else []
        return {
            "shape_valid": True,
            "missing_references": missing,
            "semantic_review": "not_performed",
        }
    except (ValueError, KeyError, TypeError) as error:
        return {
            "shape_valid": False,
            "problem": str(error),
            "semantic_review": "not_performed",
        }


def run(prior, corpus_path, identity_path, destination):
    import lmstudio as lms  # Only the selected local runtime needs this dependency.

    destination.mkdir(parents=True, exist_ok=False)
    (destination / "driver-source.py").write_bytes(Path(__file__).read_bytes())
    receipts = json.loads((prior / "private-provider-receipts.json").read_text())
    trial = json.loads((prior / "2-fixed.json").read_text())
    bundle = json.loads(corpus_path.read_text())
    case = bundle["cases"][1]
    workspace = SourceWorkspace(
        [SourceDocument(**d) for d in case["documents"]], case["sources"]
    )
    selected = []
    for index in (55, 66):
        original = receipts[index - 1]
        event = next(
            e
            for e in trial["trace"]
            if e["measurement"]["request_sha256"] == original["request_sha256"]
        )
        request = ModelRequest(**event["request"])
        selected.append((index, request, original))
    freeze = {
        "source_receipt_sha256": hashlib.sha256(
            (prior / "private-provider-receipts.json").read_bytes()
        ).hexdigest(),
        "corpus_sha256": workspace.identity,
        "order": [
            [55, "structured"],
            [55, "unconstrained"],
            [66, "unconstrained"],
            [66, "structured"],
        ],
        "maximum_attempts": 4,
        "conditional_replication_attempts": 2,
        "driver_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    save(destination / "freeze.json", freeze)
    identity = json.loads(identity_path.read_text())
    model_path = Path("/mnt/f/LLM") / identity["path"]
    with model_path.open("rb") as stream:
        observed = hashlib.file_digest(stream, "sha256").hexdigest()
    if observed != identity["gguf_sha256"]:
        raise ValueError("model asset changed")
    lms.set_sync_api_timeout(1800)
    results, provider = [], None
    with lms.Client("127.0.0.1:18080") as client:
        if client.llm.list_loaded():
            raise RuntimeError("shared GPU occupied; foreign instances preserved")
        model = client.llm.load_new_instance(
            identity["key"],
            "broader-agency-empty-output-20261007",
            ttl=None,
            config={
                "contextLength": 32768,
                "gpu": {"ratio": 0.45},
                "gpuStrictVramCap": True,
                "offloadKVCacheToGpu": True,
                "flashAttention": True,
            },
        )
        try:
            provider = LocalJSONActionProvider(
                model,
                lms.Chat.from_history,
                interface="compatible-tools",
                reasoning="server-default-accounted",
                request_timeout_seconds=1800,
            )
            old = json.loads((prior / "deployment-freeze.json").read_text())
            if comparable(provider.configuration()) != comparable(old):
                raise ValueError("loaded/provider configuration changed")
            save(destination / "deployment.json", provider.configuration())

            def call(label, request, schema, original=None):
                measurement = provider.measure(request)
                if (
                    measurement.input_tokens + request.output_reserve
                    > measurement.context_tokens
                ):
                    raise ValueError("diagnostic request does not fit")
                began = time.monotonic()
                row = {"label": label}
                try:
                    reply = provider.predict(request, measurement, 1800)
                    receipt = provider.private_receipts[-1]
                    if original:
                        expected = dict(original["payload"])
                        actual = dict(receipt["payload"])
                        expected["model"] = actual["model"]
                        if request.response_schema is None:
                            expected.pop("response_format", None)
                        if actual != expected:
                            raise ValueError(
                                "saved payload changed beyond selected variable"
                            )
                    body = strict_json(receipt["body"])
                    message = body["choices"][0]["message"]
                    row.update(
                        visible_characters=len(reply.text),
                        tool_calls=len(reply.tool_calls or ()),
                        reasoning_present=bool(message.get("reasoning_content")),
                        finish=body["choices"][0].get("finish_reason"),
                        input_tokens=reply.input_tokens,
                        output_tokens=reply.output_tokens,
                        reasoning_tokens=reply.reasoning_tokens,
                        truncated=reply.truncated,
                        fit_verified=reply.input_tokens <= measurement.input_tokens
                        and reply.input_tokens + reply.output_tokens <= 32768,
                        validation=candidate_check(
                            reply.text, schema, workspace if original else None
                        ),
                    )
                except Exception as error:  # noqa: BLE001 - preserve failures without retry
                    row["problem"] = f"{type(error).__name__}: {error}"
                finally:
                    row["elapsed_seconds"] = round(time.monotonic() - began, 3)
                    results.append(row)
                    save(
                        destination / "private-provider-receipts.json",
                        provider.private_receipts,
                    )
                    save(
                        destination / "summary.json",
                        {"results": results, "authority_change": False},
                    )
                    print(json.dumps(row), flush=True)

            for index, variant in freeze["order"]:
                _, request, original = next(r for r in selected if r[0] == index)
                call(
                    f"saved-{index}-{variant}",
                    request
                    if variant == "structured"
                    else replace(request, response_schema=None),
                    request.response_schema,
                    original,
                )
            changed = any(
                len(pair) == 2
                and all("visible_characters" in r for r in pair)
                and bool(pair[0]["visible_characters"])
                != bool(pair[1]["visible_characters"])
                for index in (55, 66)
                for pair in [
                    [r for r in results if r["label"].startswith(f"saved-{index}-")]
                ]
            )
            if changed:
                schema = object_schema(
                    {
                        "current_state": {"type": "string"},
                        "removal_timing": {"type": "string"},
                    }
                )
                control = ModelRequest(
                    "Interpret only the supplied change record. Return a JSON object with current_state and removal_timing strings.",
                    "The API is supported now. Deprecation has been announced. Removal is proposed for a future date that has not been assigned.",
                    8192,
                    phase="controlled-structured-replication",
                    response_schema=schema,
                )
                save(
                    destination / "replication-freeze.json",
                    {
                        "label": "separate controlled structured-task replication",
                        "order": ["structured", "unconstrained"],
                        "maximum_attempts": 2,
                        "mechanism_only": True,
                    },
                )
                for variant in ("structured", "unconstrained"):
                    call(
                        f"control-{variant}",
                        control
                        if variant == "structured"
                        else replace(control, response_schema=None),
                        schema,
                    )
        finally:
            if provider:
                save(
                    destination / "private-provider-receipts.json",
                    provider.private_receipts,
                )
                provider.close()
            model.unload()
            save(
                destination / "closure.json",
                {
                    "owned_instance_unloaded": True,
                    "attempts": len(provider.private_receipts) if provider else 0,
                },
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prior", type=Path, required=True)
    parser.add_argument("--corpus", type=Path, required=True)
    parser.add_argument("--identity", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    args = parser.parse_args()
    run(args.prior, args.corpus, args.identity, args.destination)
