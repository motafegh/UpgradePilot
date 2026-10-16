"""Offline qualification against a declared retained common-input bundle.

Run as python -m experiments.qualify_investigator_workspace --help. This is a mechanical
experiment, not a model evaluation. The generic script selects the first discovered source
path, reads a page and (structured arm only) native material/pages, then publishes an
explicitly unresolved laboratory report. Its choices are not case-specific model hints.
Raw inputs/requests remain in the owner-only output directory; the public summary contains
identities/counts/hashes only. Nothing restores the preparation's demonstration history.
"""

from __future__ import annotations

import argparse
import json
import socket
import subprocess
import sys
import time
from contextlib import ExitStack
from dataclasses import asdict
from hashlib import sha256
from pathlib import Path
from unittest.mock import patch

import requests

from experiments.investigator_workspace_adapter import InvestigatorAssignment
from experiments.investigator_workspace_trial import (
    mechanical_manifest,
    run_scripted_trial,
)
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
from upgradepilot.workspace.native_representation import json_bytes
from upgradepilot.workspace.source_access import read_source_catalog


def verify_retained_inputs(qualification: dict) -> dict:
    root = Path(qualification["local_root"]).resolve()
    if (
        qualification["format"] != "qualified-common-investigator-input-snapshot/1"
        or not root.is_absolute()
    ):
        raise ValueError("unsupported qualification inventory")
    for item in qualification["files"]:
        path = (root / item["path"]).resolve()
        if not path.is_relative_to(root):
            raise ValueError("inventory path escapes bundle")
        content = path.read_bytes()
        if (
            len(content) != item["bytes"]
            or sha256(content).hexdigest() != item["sha256"]
        ):
            raise ValueError("retained artifact size/hash mismatch: " + item["path"])
    manifest = json.loads((root / "manifest.json").read_bytes())
    if (
        sha256((root / "manifest.json").read_bytes()).hexdigest()
        != qualification["preparation_manifest_sha256"]
    ):
        raise ValueError("preparation manifest identity mismatch")
    repository = Path(__file__).resolve().parents[1]
    for relative, digest in manifest["product_source_sha256"].items():
        path = (repository / relative).resolve()
        if (
            not path.is_relative_to(repository / "src/upgradepilot")
            or sha256(path.read_bytes()).hexdigest() != digest
        ):
            raise ValueError("preparation product code differs: " + relative)
    return manifest


class GenericMechanicalConsumer:
    """Stateful test consumer using only the actual packed input, with no expected answers."""

    def __init__(self, treatment):
        self.treatment, self.step = treatment, 0
        self.evidence = {}
        self.latest = {}

    def __call__(self, packed):
        body = json.loads(packed.content)
        for event in body["events"]:
            observation = json.loads(event["content"])
            if "tool" in observation:
                self.latest[observation["tool"]] = observation
            for ref in observation.get("evidence", []):
                self.evidence[ref["id"]] = ref
        if body["phase"] == "report":
            return json_bytes(
                {
                    "summary": "Mechanical scripted traversal only; no dependency recommendation established.",
                    "claims": [
                        {
                            "statement": "Retained material was delivered; interpretation is unassessed.",
                            "status": "unresolved",
                            "evidence": list(self.evidence.values()),
                            "missing_observation": "Semantic and independent usefulness evaluation",
                        }
                    ],
                    "conditions": [],
                    "unexamined": [
                        "All substantive compatibility and action questions"
                    ],
                    "recommendation": "No substantive recommendation from mechanical qualification.",
                    "recommendation_status": "unresolved",
                    "recommendation_evidence": [],
                    "recommendation_missing_observation": "A separately qualified Investigator and semantic review",
                    "stopping_reason": "Generic scripted interface check complete; adequacy unsupported.",
                }
            )
        self.step += 1
        tool, arguments = "finish_investigation", {}
        if self.step == 1:
            tool = "list_sources"
        elif self.step == 2:
            scopes = json.loads(self.latest["list_sources"]["content"])["payload"][
                "sources"
            ]
            tool, arguments = "list_paths", {"source_id": scopes[0]["source_id"]}
        elif self.step == 3:
            paths = json.loads(self.latest["list_paths"]["content"])["payload"]["items"]
            tool, arguments = (
                "read_source",
                {
                    "source_id": paths[0]["source_id"],
                    "path": paths[0]["path"],
                    "line_count": 1,
                },
            )
        elif self.step == 4 and self.treatment == "structured":
            tool, arguments = (
                "read_native",
                {"families": ["ci_coverage", "runtime_dependency_state"]},
            )
        elif self.step == 5 and self.treatment == "structured":
            native = json.loads(self.latest["read_native"]["content"])
            if native["omitted"]:
                tool, arguments = (
                    "read_native_page",
                    {
                        "record_id": native["omitted"][0]["record_id"],
                        "character_count": 256,
                    },
                )
        return json_bytes({"tool": tool, "arguments": arguments})


def qualify(qualification: dict, output: Path) -> dict:
    started = time.monotonic()
    manifest = verify_retained_inputs(qualification)
    output.mkdir(mode=0o700, parents=True, exist_ok=False)
    root = Path(qualification["local_root"])
    public = {
        "format": "investigator-workspace-mechanical-qualification/1",
        "scope": "Scripted mechanical integration; no model inference or semantic outcome",
        "preparation_manifest_sha256": qualification["preparation_manifest_sha256"],
        "retained_artifacts_verified": len(qualification["files"]),
        "unchanged_product_hashes": len(manifest["product_source_sha256"]),
        "assignments": [],
        "shared_preparation_public_get_operations": qualification["execution"][
            "public_get_operations"
        ],
        "preparation_cost_scope": "Earlier common preparation, charged once separately; no reacquisition in this qualification.",
    }
    blocked_names = {
        "analyze_dependency_change",
        "evaluate_dependency_ci_coverage",
        "evaluate_runtime_dependency_state",
        "investigate_public_pull_request",
        "build_lm_studio_session",
    }
    guard_hits = []

    def guard(frame, event, arg):
        if event == "call" and frame.f_code.co_name in blocked_names:
            guard_hits.append(frame.f_code.co_name)
            raise AssertionError("producer/model execution forbidden")

    previous_profile = sys.getprofile()
    with ExitStack() as stack:
        forbidden = [
            stack.enter_context(
                patch.object(
                    owner,
                    name,
                    side_effect=AssertionError("network/target execution forbidden"),
                )
            )
            for owner, name in (
                (socket.socket, "connect"),
                (requests.Session, "request"),
                (subprocess, "Popen"),
            )
        ]
        sys.setprofile(guard)
        try:
            for number, case in enumerate(qualification["cases"], 1):
                read_started = time.monotonic()
                target = ExactInvestigationTarget(**case["target"])
                directory = root / f"case-{number}"
                stored = CheckpointStore.open(
                    directory / "checkpoint", read_only=True
                ).read_revision(
                    case["lineage_id"], case["revision_id"], expected_target=target
                )
                if stored.revision.digest() != case["checkpoint_digest"]:
                    raise ValueError("checkpoint identity mismatch")
                catalog = read_source_catalog(
                    (directory / "common-sources.json").read_bytes(),
                    expected_target=target,
                )
                if catalog.identity != case["catalog_id"]:
                    raise ValueError("source catalog identity mismatch")
                input_read_seconds = time.monotonic() - read_started
                pair = []
                for treatment in ("raw", "structured"):
                    assignment = InvestigatorAssignment(
                        stored.revision.boundary,
                        catalog,
                        treatment,
                        max_native_bytes=4096,
                    )
                    # Fresh assignment retains no views/proposals from the qualification checkpoint.
                    if len(assignment.host.current.lifecycle_history.records) != 1:
                        raise AssertionError("preparation interaction history leaked")
                    result = run_scripted_trial(
                        assignment, GenericMechanicalConsumer(treatment)
                    )
                    if (
                        result.outcome != "completed"
                        or result.report_publication["evaluation"] != "unsupported"
                    ):
                        raise AssertionError(
                            f"mechanical trial failed: {result.problem}"
                        )
                    artifact = {
                        "manifest": mechanical_manifest(
                            assignment, input_inventory=qualification["files"]
                        ),
                        "charges": result.charges,
                        "report_publication": result.report_publication,
                        "termination_id": result.termination_id,
                        "termination": asdict(
                            assignment.host.lifecycle_value(result.termination_id)
                        ),
                        "responses_hex": [
                            r.hex() if r is not None else None
                            for r in result.original_responses
                        ],
                        "inputs_hex": [p.content.hex() for p in result.packed_inputs],
                        "events": [
                            asdict(e)
                            | {
                                "content": e.content.hex(),
                                "access_receipts": [
                                    asdict(r) for r in e.access_receipts
                                ],
                            }
                            for e in assignment.events
                        ],
                    }
                    path = output / f"case-{number}-{treatment}.json"
                    with path.open("xb") as stream:
                        path.chmod(0o600)
                        stream.write(json_bytes(artifact))
                    source_read = next(
                        json.loads(e.content)
                        for e in assignment.events
                        if json.loads(e.content).get("tool") == "read_source"
                    )
                    item = {
                        "case_id": case["case_id"],
                        "treatment": treatment,
                        "outcome": result.outcome,
                        "catalog_id": catalog.identity,
                        "target": case["target"],
                        "lineage_id": assignment.host.lineage_id,
                        "artifact_sha256": sha256(path.read_bytes()).hexdigest(),
                        "protocol_sha256": artifact["manifest"]["protocol_sha256"],
                        "raw_page_sha256": sha256(
                            source_read["content"].encode()
                        ).hexdigest(),
                        "consumer_turns": result.charges[
                            "consumer_invocation_attempts"
                        ],
                        "charged_operations": result.charges["admission_operations"],
                        "observation_bytes": result.charges["observation_bytes"],
                        "input_bytes": result.charges["packed_input_bytes"],
                        "consumer_response_bytes": result.charges[
                            "consumer_response_bytes"
                        ],
                        "assignment_composition_seconds": assignment.composition_seconds,
                        "scripted_elapsed_seconds": result.charges["elapsed_seconds"],
                        "shared_case_input_read_seconds": input_read_seconds,
                        "citation_count": len(
                            result.report_publication["citation_ids"]
                        ),
                        "evaluation": result.report_publication["evaluation"],
                        "inference_admitted": False,
                    }
                    public["assignments"].append(item)
                    pair.append(item)
                if (
                    pair[0]["raw_page_sha256"] != pair[1]["raw_page_sha256"]
                    or pair[0]["lineage_id"] == pair[1]["lineage_id"]
                ):
                    raise AssertionError("raw fidelity or assignment isolation failed")
        finally:
            sys.setprofile(previous_profile)
        if guard_hits or any(mock.call_count for mock in forbidden):
            raise AssertionError("forbidden execution attempted")
    verify_retained_inputs(qualification)
    public["forbidden_execution_attempts"] = 0
    public["model_calls"] = 0
    public["native_producer_calls"] = 0
    public["retained_bundle_unchanged"] = True
    public["private_output_directory"] = str(output.resolve())
    public["qualification_elapsed_seconds"] = time.monotonic() - started
    return public


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--qualification", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    args = parser.parse_args()
    summary = qualify(json.loads(args.qualification.read_bytes()), args.output)
    with args.summary.open("x") as stream:
        stream.write(json.dumps(summary, indent=2) + "\n")
    print(
        json.dumps(
            {
                "assignments": len(summary["assignments"]),
                "model_calls": 0,
                "summary": str(args.summary),
            }
        )
    )


if __name__ == "__main__":
    main()
