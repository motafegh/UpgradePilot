"""Offline real-packet preparation and maximum-reference publication proof.

This CLI never imports/constructs an SDK client, loads a model or predicts. It verifies
the retained common input qualification, applies an explicit allowlisted source recipe
to fresh hosts, and retains complete packets/receipts and structural feasibility results.
The output is preparation evidence, deliberately not an inference-admission freeze.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict
from pathlib import Path

from experiments.investigator_model_interface import digest, private_write
from experiments.investigator_supplied_evidence import (
    SUPPLIED_EVIDENCE_PROTOCOL,
    SuppliedEvidenceLimits,
    SuppliedEvidenceTrial,
    mechanical_report,
)
from experiments.qualify_investigator_workspace import verify_retained_inputs
from experiments.run_investigator_semantic_comparison import load_case_assignment
from upgradepilot.workspace.native_representation import json_bytes

PREPARATION_FORMAT = "investigator-supplied-evidence-offline-preparation/1"
RECIPE_FORMAT = "investigator-supplied-evidence-recipes/1"
PREPARATION_CODE = (
    "experiments/investigator_run_control.py",
    "experiments/investigator_model_interface.py",
    "experiments/investigator_supplied_evidence.py",
    "experiments/investigator_workspace_trial.py",
    "experiments/investigator_workspace_adapter.py",
    "experiments/prepare_investigator_supplied_evidence.py",
    "experiments/run_investigator_semantic_comparison.py",
    "experiments/qualify_investigator_workspace.py",
)


def read_recipes(path):
    """Only this allowlisted inventory reaches packet construction; no reviewer file."""
    body = json.loads(path.read_bytes())
    if set(body) != {"format", "cases"} or body["format"] != RECIPE_FORMAT:
        raise ValueError("unsupported packet recipe inventory")
    labels = []
    for case in body["cases"]:
        if set(case) != {"label", "case_id", "source_pair", "requests"}:
            raise ValueError("unexpected recipe fields; reviewer material is not model input")
        if type(case["source_pair"]) is not bool or not re.fullmatch(r"packet-[a-z]", case["label"]):
            raise ValueError("invalid recipe task or opaque label")
        labels.append(case["label"])
    if labels != ["packet-a", "packet-b", "packet-c", "packet-d"]:
        raise ValueError("diagnostic requires exactly the declared ordered four packets")
    return body


def prepare_recipe(qualification, recipe, *, limits=None):
    assignment = load_case_assignment(qualification, recipe["case_id"], "structured", 65536)
    trial = SuppliedEvidenceTrial(
        assignment, [json_bytes(item) for item in recipe["requests"]],
        case_label=recipe["label"], source_pair=recipe["source_pair"], limits=limits,
    )
    trial.prepare()
    return trial


def verify_prepared_packets(root):
    """Recheck immutable preparation retention/source, without loading or predicting."""
    manifest = json.loads((root / "preparation.json").read_bytes())
    index = json.loads((root / "retention-index.json").read_bytes())
    if ((root / "retention-index.json").stat().st_mode & 0o777) != 0o600:
        raise ValueError("preparation retention-index mode drift")
    if set(manifest["code_sha256"]) != set(PREPARATION_CODE):
        raise ValueError("unexpected preparation source inventory")
    if manifest["format"] != PREPARATION_FORMAT or manifest["admission"] != "offline_preparation_only; not_a_prediction_freeze":
        raise ValueError("unsupported offline preparation")
    expected = {item["path"] for item in index["files"]}
    actual = {str(path.relative_to(root)) for path in root.rglob("*") if path.is_file()}
    if actual != expected | {"retention-index.json"}:
        raise ValueError("preparation retention membership drift")
    if any((path.stat().st_mode & 0o777) != 0o700 for path in [root, *[p for p in root.rglob("*") if p.is_dir()]]):
        raise ValueError("preparation directory mode drift")
    for item in index["files"]:
        path = (root / item["path"]).resolve()
        if not path.is_relative_to(root.resolve()):
            raise ValueError("retention path escapes root")
        if path.stat().st_size != item["bytes"] or digest(path.read_bytes()) != item["sha256"] or (path.stat().st_mode & 0o777) != 0o600:
            raise ValueError("preparation file identity/mode drift")
    for path, expected_hash in manifest["code_sha256"].items():
        if digest(Path(path).read_bytes()) != expected_hash:
            raise ValueError("preparation source drift; create a new version, not an old-root repair")
    qualification_path = Path(manifest["qualified_input_path"])
    if digest(qualification_path.read_bytes()) != manifest["qualified_input_sha256"]:
        raise ValueError("original qualified input identity drift")
    verify_retained_inputs(json.loads(qualification_path.read_bytes()))
    return manifest


def selection_inventory(trial):
    """Freeze concrete source/payload selections separately from fresh delivery IDs.

    Source descriptors and native records come from actual authoritative deliveries.
    No strings are normalized to hide drift. Fresh host revision/delivery/reference IDs
    remain in the exact packet and mapping artifacts; their owner is the new host.
    """
    result = []
    for request, event in zip(trial.requests, trial.assignment.events, strict=False):
        item = json.loads(request)
        delivery = json.loads(json.loads(event.content)["content"])
        if item["tool"] == "read_source":
            payload = delivery["payload"]
            selection = {
                "request": item,
                "catalog_id": delivery["catalog_id"],
                "file": payload["file"],
                "start_line": payload["start_line"],
                "delivered_lines": len(payload["lines"]),
                "selected_lines_sha256": digest(json_bytes(payload["lines"])),
                "source_reference": payload["reference"],
            }
        else:
            if delivery["omitted"]:
                raise ValueError("incomplete required native material")
            selection = {
                "request": item,
                "source_universe": delivery["source_universe"],
                "native_records": [
                    {
                        "record_id": record["record_id"],
                        "family": record["family"],
                        "payload_digest": record["payload_digest"],
                        "complete_record_sha256": digest(json_bytes(record)),
                    }
                    for record in delivery["native_records"]
                ],
            }
        result.append(selection)
    return result


def prepare_packets(qualification_path, recipes_path, output):
    qualification = json.loads(qualification_path.read_bytes())
    original = verify_retained_inputs(qualification)
    recipes = read_recipes(recipes_path)
    allowed = Path.home() / ".local/share/upgradepilot/investigator-runs"
    if not output.is_absolute() or not output.resolve().is_relative_to(allowed.resolve()):
        raise ValueError("preparation output must be a fresh durable Investigator retention root")
    output.mkdir(mode=0o700, parents=False, exist_ok=False)
    private_write(output / "qualified-inputs.json", qualification_path.read_bytes())
    private_write(output / "packet-recipes.json", recipes_path.read_bytes())
    manifest = {
        "format": PREPARATION_FORMAT,
        "protocol": SUPPLIED_EVIDENCE_PROTOCOL,
        "admission": "offline_preparation_only; not_a_prediction_freeze",
        "qualified_input_path": str(qualification_path.resolve()),
        "qualified_input_sha256": digest(qualification_path.read_bytes()),
        "recipes_sha256": digest(recipes_path.read_bytes()),
        "limits": asdict(SuppliedEvidenceLimits()),
        "code_sha256": {path: digest(Path(path).read_bytes()) for path in PREPARATION_CODE},
        "product_source_sha256": original["product_source_sha256"],
        "fresh_identity_policy": {
            "fixed": "target/catalog/source descriptors/native record payloads/selection inventory",
            "fresh": "Workspace host lineage/revisions/deliveries and laboratory typed reference IDs, minted by the actual new host",
            "dispatch": "Bind exact actual rendered bytes and current local references; never reuse these terminated feasibility hosts.",
        },
        "remaining_admission_requirements": [
            "Current owned runtime and retained intended deployment identity",
            "Zero-generation actual rendering/tokenizer and complete packet input fit",
            "New source-bound deployment/freeze identity and reviewer obligations",
            "Explicit bounded prediction activation and applicable probes",
        ],
        "cases": [],
    }
    for recipe in recipes["cases"]:
        directory = output / recipe["label"]
        directory.mkdir(mode=0o700)
        trial = prepare_recipe(qualification, recipe)
        packed = trial.pack()
        selections = selection_inventory(trial)
        private_write(directory / "packed-input.json", packed.content)
        private_write(directory / "protocol.json", json_bytes(trial.protocol()))
        private_write(directory / "selection-inventory.json", json_bytes(selections))
        private_write(directory / "reference-map.json", json_bytes([
            asdict(reference) for reference in trial.assignment.references.values()
        ]))
        private_write(directory / "delivery-events.json", json_bytes([
            asdict(event) | {"content": event.content.decode()}
            for event in trial.assignment.events
        ]))
        result = trial.run(mechanical_report)
        private_write(directory / "feasibility-response.json", result.original_responses[0])
        private_write(directory / "feasibility-result.json", json_bytes({
            "outcome": result.outcome, "problem": result.problem,
            "charges": result.charges, "publication": result.report_publication,
            "termination_id": result.termination_id,
            "semantic_acceptance": "not_evaluated; mechanical_script_only",
        }))
        if (
            result.outcome != "completed" or result.termination_id is None
            or len(result.report_publication["citation_ids"]) != len(packed.reference_pairs)
            or result.charges["admission_operations"] > trial.limits.operations
        ):
            raise ValueError("offline maximum-reference feasibility failed; no inference")
        manifest["cases"].append({
            **{key: recipe[key] for key in ("label", "case_id", "source_pair")},
            "target": asdict(trial.assignment.host.current.boundary.target),
            "catalog_id": trial.assignment.access.catalog.identity,
            "setup_reads": len(recipe["requests"]),
            "eligible_references": len(packed.reference_pairs),
            "packed_bytes": len(packed.content),
            "selection_inventory_sha256": digest(json_bytes(selections)),
            "required_material_event_ids": [event.event_id for event in trial.assignment.events],
            "feasibility_units": result.charges["admission_operations"],
            "feasibility_outcome": result.outcome,
            "semantic_acceptance": "not_evaluated",
        })
        private_write(output / (recipe["label"] + ".checkpoint.json"), json_bytes(manifest["cases"][-1]))
    private_write(output / "preparation.json", json_bytes(manifest))
    files = [
        {"path": str(path.relative_to(output)), "bytes": path.stat().st_size,
         "sha256": digest(path.read_bytes()), "mode": oct(path.stat().st_mode & 0o777)}
        for path in sorted(output.rglob("*")) if path.is_file()
    ]
    if any(item["mode"] != "0o600" for item in files):
        raise ValueError("private retention mode drift")
    private_write(output / "retention-index.json", json_bytes({"files": files, "excludes_self": True}))
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--qualification", type=Path, required=True)
    parser.add_argument("--recipes", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = prepare_packets(args.qualification, args.recipes, args.output)
    print(json.dumps({"admission": result["admission"], "cases": result["cases"]}, indent=2))


if __name__ == "__main__":
    main()
