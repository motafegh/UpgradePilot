"""Known-case interpretation-only development with preselected neutral sources.

Selectors name frozen source windows, not answers. They are never injected into
Fixed/Agent policies. Save the packet coverage review before inference; adequate
source delivery does not fill absent runtime facts or establish compatibility.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict
from pathlib import Path

from .broader_agency_local import LocalJSONActionProvider
from .broader_agency_pilot import code_identities
from .broader_agency_trial import TrialLimits, run_investigation_trial
from .broader_agency_workspace import SourceDocument, SourceWorkspace, digest


def save(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def run(corpus_path, selections_path, identity_path, destination):
    import lmstudio as lms

    bundle = json.loads(corpus_path.read_text())
    selections = json.loads(selections_path.read_text())
    if selections["corpus_sha256"] != digest(bundle):
        raise ValueError("selected corpus changed")
    if len(selections["cases"]) != 2:
        raise ValueError("exactly two known development packets selected")
    identity = json.loads(identity_path.read_text())
    limits = TrialLimits(
        calls=2,
        corrections=1,
        seconds=3600,
        action_output=8192,
        final_output=8192,
        output_tokens=16384,
        input_tokens=524288,
    )
    destination.mkdir(parents=True, exist_ok=False)
    (destination / "driver-source.py").write_bytes(Path(__file__).read_bytes())
    save(
        destination / "freeze.json",
        {
            "label": "interpretation-only known-case development; not F/A comparison",
            "code": code_identities(),
            "driver_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "selections_sha256": hashlib.sha256(
                selections_path.read_bytes()
            ).hexdigest(),
            "corpus_sha256": digest(bundle),
            "maximum_attempts": 4,
            "evidence_contract_version": 2,
            "limits": asdict(limits),
        },
    )
    save(destination / "packet-selection.json", selections)
    with (Path("/mnt/f/LLM") / identity["path"]).open("rb") as stream:
        if hashlib.file_digest(stream, "sha256").hexdigest() != identity["gguf_sha256"]:
            raise ValueError("model asset changed")
    lms.set_sync_api_timeout(1800)
    with lms.Client("127.0.0.1:18080") as client:
        if client.llm.list_loaded():
            raise RuntimeError("shared GPU occupied; foreign instances preserved")
        model = client.llm.load_new_instance(
            identity["key"],
            "broader-agency-interpretation-only-20261007",
            ttl=None,
            config={
                "contextLength": 32768,
                "gpu": {"ratio": 0.45},
                "gpuStrictVramCap": True,
                "offloadKVCacheToGpu": True,
                "flashAttention": True,
            },
        )
        provider = None
        try:
            info = model.get_info().to_dict()
            if any(
                info[k] != identity[v]
                for k, v in (
                    ("modelKey", "key"),
                    ("path", "path"),
                    ("sizeBytes", "size_bytes"),
                )
            ):
                raise ValueError("deployment identity mismatch")
            provider = LocalJSONActionProvider(
                model,
                lms.Chat.from_history,
                interface="compatible-tools",
                reasoning="server-default-accounted",
                request_timeout_seconds=1800,
            )
            save(destination / "deployment.json", provider.configuration())
            prepared, measurements = [], []
            for selection in selections["cases"]:
                item = next(
                    c
                    for c in bundle["cases"]
                    if c["task"]["case_id"] == selection["case_id"]
                )
                workspace = SourceWorkspace(
                    [SourceDocument(**d) for d in item["documents"]], item["sources"]
                )
                if workspace.identity != item["corpus_sha256"]:
                    raise ValueError("case identity changed")

                class CapacityPreview:
                    def measure(self, request, case_id=item["task"]["case_id"]):
                        actual = provider.measure(request)
                        measurements.append(
                            {
                                **asdict(actual),
                                "case_id": case_id,
                                "output_reserve": request.output_reserve,
                                "fits": actual.input_tokens + request.output_reserve
                                <= actual.context_tokens,
                            }
                        )
                        # Stop during preparation, before the inference boundary.
                        raise ValueError("preparation-only measurement; no inference")

                run_investigation_trial(
                    item["task"],
                    workspace,
                    "interpretation",
                    CapacityPreview(),
                    limits=limits,
                    contract_version=2,
                    provided_evidence=selection["observations"],
                )
                prepared.append((selection, item, workspace))
            save(
                destination / "capacity-preflight.json",
                {
                    "measurements": measurements,
                    "inference_attempts": 0,
                    "all_fit": len(measurements) == 2
                    and all(m["fits"] for m in measurements),
                },
            )
            if len(measurements) != 2 or not all(m["fits"] for m in measurements):
                raise ValueError("interpretation packets do not fit; no inference")
            for selection, item, workspace in prepared:
                result = run_investigation_trial(
                    item["task"],
                    workspace,
                    "interpretation",
                    provider,
                    limits=limits,
                    contract_version=2,
                    provided_evidence=selection["observations"],
                )
                save(destination / (selection["case_id"] + ".json"), result)
                save(
                    destination / "private-provider-receipts.json",
                    provider.private_receipts,
                )
                print(
                    json.dumps(
                        {
                            "case_id": result["case_id"],
                            "outcome": result["outcome"],
                            "counters": result["counters"],
                            "elapsed_seconds": result["elapsed_seconds"],
                        }
                    ),
                    flush=True,
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
    for name in ("corpus", "selections", "identity", "destination"):
        parser.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args()
    run(args.corpus, args.selections, args.identity, args.destination)
