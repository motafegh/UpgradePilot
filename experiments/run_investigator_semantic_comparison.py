"""Execute the frozen development comparison after all interface points qualify.

Start at execute_comparison. The manifest binds common inputs, code, exact protocols,
review obligations and the separately frozen canaries before any prediction. Every
assignment has a fresh host and explicit stateless model requests. This runner retains
original reports/failures/accounting; it never grades semantics or acquires evidence.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from experiments.investigator_model_interface import (
    ModelLimits,
    SDKBinding,
    StatelessInvestigatorModel,
    digest,
    fields,
    import_isolated_sdk,
    private_write,
    run_model_trial,
)
from experiments.investigator_workspace_adapter import InvestigatorAssignment
from experiments.investigator_workspace_trial import (
    REFERENCE_SCHEMA_POLICY,
    TrialLimits,
    protocol_definition,
)
from experiments.qualify_investigator_model_interface import (
    code_hashes,
    observe_owned_backend,
    validate_loaded_backend,
)
from experiments.qualify_investigator_workspace import verify_retained_inputs
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
from upgradepilot.workspace.native_representation import json_bytes
from upgradepilot.workspace.source_access import read_source_catalog


def comparison_code_hashes():
    paths = (
        Path(__file__),
        Path("experiments/qualify_investigator_workspace.py"),
    )
    return code_hashes() | {
        str(p.relative_to(Path.cwd()) if p.is_absolute() else p): digest(p.read_bytes())
        for p in paths
    }


def load_case_assignment(qualification, case_id, treatment, max_native_bytes):
    """Read the exact native boundary, without the preparation's interaction history."""
    index, case = next(
        (n, c)
        for n, c in enumerate(qualification["cases"], 1)
        if c["case_id"] == case_id
    )
    target = ExactInvestigationTarget(**case["target"])
    directory = Path(qualification["local_root"]) / f"case-{index}"
    revision = (
        CheckpointStore.open(directory / "checkpoint", read_only=True)
        .read_revision(case["lineage_id"], case["revision_id"], expected_target=target)
        .revision
    )
    if revision.digest() != case["checkpoint_digest"]:
        raise ValueError("common checkpoint drift")
    catalog = read_source_catalog(
        (directory / "common-sources.json").read_bytes(), expected_target=target
    )
    if catalog.identity != case["catalog_id"]:
        raise ValueError("common source-catalog drift")
    return InvestigatorAssignment(
        revision.boundary, catalog, treatment, max_native_bytes=max_native_bytes
    )


def validate_schedule(assignments, model_keys, case_ids):
    triples = [(a["model_key"], a["case_id"], a["treatment"]) for a in assignments]
    expected = {
        (m, c, t) for m in model_keys for c in case_ids for t in ("raw", "structured")
    }
    if (
        len(model_keys) != 3
        or len(set(model_keys)) != 3
        or len(case_ids) != 2
        or len(set(case_ids)) != 2
        or len(triples) != 12
        or set(triples) != expected
        or len({a["id"] for a in assignments}) != 12
    ):
        raise ValueError("incomplete/duplicate semantic schedule")
    firsts = {
        (m, c): next(t for mm, cc, t in triples if (mm, cc) == (m, c))
        for m in model_keys
        for c in case_ids
    }
    if sum(t == "raw" for t in firsts.values()) != 3 or any(
        sorted(firsts[m, c] for c in case_ids) != ["raw", "structured"]
        for m in model_keys
    ):
        raise ValueError("unbalanced treatment-first schedule")
    if sorted(sum(firsts[m, c] == "raw" for m in model_keys) for c in case_ids) != [
        1,
        2,
    ]:
        raise ValueError("unbalanced per-case treatment-first schedule")


def validate_case_balance(assignments, case_ids, balance):
    """The immutable manifest names which case receives each inverse orientation."""
    firsts = {}
    for row in assignments:
        firsts.setdefault((row["model_key"], row["case_id"]), row["treatment"])
    if balance.get(
        "format"
    ) != "investigator-semantic-treatment-first-balance/1" or balance.get(
        "raw_first_by_case"
    ) != {
        c: sum(t == "raw" for (_, case), t in firsts.items() if case == c)
        for c in case_ids
    }:
        raise ValueError("named-case treatment-first balance mismatch")


def read_qualified_matrix(freeze):
    """All selected points must finish the newly bound matrix; no arm fallback."""
    spec = freeze["interface_qualification"]
    content = Path(spec["freeze_path"]).read_bytes()
    if digest(content) != spec["freeze_sha256"]:
        raise ValueError("qualification freeze drift")
    qualification = json.loads(content)
    if (
        qualification.get("format") != "investigator-interface-canary-freeze/2"
        or qualification.get("reference_schema_policy") != REFERENCE_SCHEMA_POLICY
        or freeze.get("reference_schema_policy") != REFERENCE_SCHEMA_POLICY
    ):
        raise ValueError("qualification reference contract mismatch")
    if qualification["code_sha256"] != code_hashes():
        raise ValueError("qualification belongs to different source")
    rows = json.loads((Path(spec["results_root"]) / "summary.json").read_bytes())[
        "assignments"
    ]
    wanted = {a["id"]: a for a in qualification["assignments"]}
    if (
        len(rows) != len(wanted)
        or [r["assignment"] for r in rows] != qualification["assignments"]
        or any(
            r["assignment"] != wanted[r["assignment"]["id"]]
            or r["disposition"] != "qualified"
            or not r.get("usage_complete")
            or r.get("outcome") != "completed"
            for r in rows
        )
    ):
        raise ValueError(
            "required interface matrix did not qualify; semantic batch withheld"
        )
    if qualification["deployments"] != freeze["deployments"]:
        raise ValueError("qualification profile/configuration mismatch")
    root = Path(spec["results_root"])
    for row in rows:
        verified = verify_call_artifacts(root / row["assignment"]["id"])
        if verified != (
            row["model_attempts"],
            row["known_input_tokens"],
            row["known_generated_tokens"],
        ):
            raise ValueError("qualification accounting/receipt mismatch")
    return rows


def verify_call_artifacts(directory):
    """Recheck retained actual usage/configuration, without rerunning a prediction."""
    receipts = sorted(directory.glob("call-*.receipt.json"))
    if not receipts:
        raise ValueError("missing qualification call artifacts")
    inputs = generated = 0
    for number, path in enumerate(receipts, 1):
        if path.name != f"call-{number:02}.receipt.json":
            raise ValueError("noncontiguous qualification call artifacts")
        prefix = directory / f"call-{number:02}"
        read = lambda suffix, prefix=prefix: Path(str(prefix) + suffix).read_bytes()
        request = json.loads(read(".request.json"))
        receipt = json.loads(path.read_bytes())
        meta = json.loads(read(".metadata.json"))
        stats = receipt["usage"]
        requested = fields(request["configuration"]["layers"][0]["config"])
        applied = fields(meta["predictionConfig"])
        if (
            receipt["outcome"] != "returned"
            or not receipt["complete_response_received"]
            or receipt["request_sha256"] != digest(json_bytes(request))
            or request["packed_input_sha256"] != digest(read(".packed-input.json"))
            or request["rendered_sha256"] != digest(read(".rendered.txt"))
            or request.get("reference_schema_policy") != REFERENCE_SCHEMA_POLICY
            or request["derived_schema_sha256"]
            != digest(json_bytes(requested["llm.prediction.structured"]["jsonSchema"]))
            or any(applied.get(k) != v for k, v in requested.items())
            or meta["modelInfo"]["instanceReference"]
            != request["identity"]["model"]["instanceReference"]
            or stats != meta["stats"]
            or any(
                type(stats.get(k)) is not int or stats[k] < 0
                for k in (
                    "promptTokensCount",
                    "predictedTokensCount",
                    "totalTokensCount",
                )
            )
            or stats["promptTokensCount"] != request["rendered_tokens"]
            or stats["promptTokensCount"] + stats["predictedTokensCount"]
            != stats["totalTokensCount"]
            or read(".visible-response.txt") != read(".visible-fragments.txt")
            or receipt["visible_fragments_sha256"]
            != digest(read(".visible-fragments.txt"))
        ):
            raise ValueError("qualification call artifact/configuration mismatch")
        inputs += stats["promptTokensCount"]
        generated += stats["predictedTokensCount"]
    return len(receipts), inputs, generated


def qualification_artifact_index(root):
    """Bind all qualification originals; index/receipt live outside this closed root."""
    result = []
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError("qualification artifact symlink")
        if path.is_file():
            content = path.read_bytes()
            result.append(
                {
                    "path": str(path.relative_to(root)),
                    "bytes": len(content),
                    "sha256": digest(content),
                }
            )
    return result


def create_admission_receipt(freeze_path, expected_hash):
    """Append the observed gate result without modifying either pre-run freeze."""
    freeze, _ = verify_freeze(freeze_path, expected_hash)
    disposition, problem = "permitted", None
    try:
        read_qualified_matrix(freeze)
    except (ValueError, OSError, KeyError, TypeError) as error:
        disposition, problem = "withheld", str(error)
    spec = freeze["admission_receipt"]
    index = qualification_artifact_index(
        Path(freeze["interface_qualification"]["results_root"])
    )
    private_write(Path(spec["index_path"]), json_bytes(index))
    receipt = {
        "format": "investigator-semantic-admission/1",
        "semantic_freeze_sha256": expected_hash,
        "qualification_freeze_sha256": freeze["interface_qualification"][
            "freeze_sha256"
        ],
        "qualification_artifact_index_sha256": digest(json_bytes(index)),
        "disposition": disposition,
        "problem": problem,
    }
    private_write(Path(spec["path"]), json_bytes(receipt))
    return receipt


def require_qualification(freeze, expected_hash):
    """Recheck exact current results and the append-only receipt before semantic load."""
    read_qualified_matrix(freeze)
    spec = freeze["admission_receipt"]
    receipt = json.loads(Path(spec["path"]).read_bytes())
    index_bytes = Path(spec["index_path"]).read_bytes()
    if (
        receipt.get("format") != "investigator-semantic-admission/1"
        or receipt.get("disposition") != "permitted"
        or receipt.get("semantic_freeze_sha256") != expected_hash
        or receipt.get("qualification_freeze_sha256")
        != freeze["interface_qualification"]["freeze_sha256"]
        or receipt.get("qualification_artifact_index_sha256") != digest(index_bytes)
        or json.loads(index_bytes)
        != qualification_artifact_index(
            Path(freeze["interface_qualification"]["results_root"])
        )
    ):
        raise ValueError("qualification admission receipt/artifact mismatch")


def verify_freeze(path, expected_hash):
    content = path.read_bytes()
    if digest(content) != expected_hash:
        raise ValueError("semantic freeze hash mismatch")
    freeze = json.loads(content)
    if freeze["format"] != "investigator-semantic-comparison-freeze/2":
        raise ValueError("unsupported semantic freeze")
    if freeze.get("reference_schema_policy") != REFERENCE_SCHEMA_POLICY:
        raise ValueError("semantic reference contract mismatch")
    if freeze["code_sha256"] != comparison_code_hashes():
        raise ValueError("semantic source drift")
    validate_schedule(
        freeze["assignments"],
        [d["model_key"] for d in freeze["deployments"]],
        freeze["case_ids"],
    )
    validate_case_balance(
        freeze["assignments"], freeze["case_ids"], freeze["treatment_first_balance"]
    )
    for item in freeze["bound_files"]:
        if digest(Path(item["path"]).read_bytes()) != item["sha256"]:
            raise ValueError(
                "bound contract/profile/review/input drift: " + item["path"]
            )
    for item in freeze["immutable_files"]:
        observed = Path(item["path"]).stat()
        if (
            observed.st_size != item["bytes"]
            or observed.st_mtime_ns != item["mtime_ns"]
        ):
            raise ValueError("hashed model/runtime file changed")
    qualification = json.loads(Path(freeze["input_qualification_path"]).read_bytes())
    verify_retained_inputs(qualification)
    return freeze, qualification


def execute_comparison(sdk, freeze_path, expected_hash, output):
    freeze, qualification = verify_freeze(freeze_path, expected_hash)
    require_qualification(
        freeze, expected_hash
    )  # Before model loading/output creation.
    output.mkdir(mode=0o700, parents=True, exist_ok=False)
    private_write(output / "executed-freeze.json", freeze_path.read_bytes())
    rows = []
    limits = TrialLimits(**freeze["trial_limits"])
    with sdk.Client("127.0.0.1:18080") as client:
        if client.llm.list_loaded():
            raise ValueError("pre-existing model; no implicit unload")
        for spec in freeze["assignments"]:
            deployment = next(
                d for d in freeze["deployments"] if d["model_key"] == spec["model_key"]
            )
            profile = json.loads(Path(deployment["profile_path"]).read_bytes())
            assignment = load_case_assignment(
                qualification,
                spec["case_id"],
                spec["treatment"],
                freeze["max_native_bytes"],
            )
            protocol = protocol_definition(assignment, limits)
            expected_protocol = freeze["protocol_sha256"][spec["case_id"]][
                spec["treatment"]
            ]
            if digest(json_bytes(protocol)) != expected_protocol:
                raise ValueError("actual initial protocol differs from frozen contract")
            model = None
            try:
                download = next(
                    m
                    for m in client.llm.list_downloaded()
                    if m.model_key == spec["model_key"]
                )
                model = download.load_new_instance(
                    # The frozen public identifier is part of native model identity.
                    # Unload/load gives fresh instanceReference/state with that label.
                    instance_identifier=profile["identifier"],
                    config=profile["requested_load"],
                    ttl=3600,
                )
                binding = SDKBinding(model, sdk, profile["tokenizer_policy"])
                identity = binding.identity()
                backend_dir = output / (spec["id"] + "-backend")
                backend_dir.mkdir(mode=0o700)
                validate_loaded_backend(
                    profile, identity, observe_owned_backend(backend_dir)
                )
                if identity["load"] != profile["initial_identity"]["load"]:
                    raise ValueError("semantic load differs from qualified profile")
                consumer = StatelessInvestigatorModel(
                    binding,
                    profile["prediction_configuration"],
                    ModelLimits(**freeze["model_limits"]),
                    output / spec["id"],
                )
                result = run_model_trial(
                    assignment, consumer, limits=limits, protocol=protocol
                )
                record = {
                    "assignment": spec,
                    "outcome": result.outcome,
                    "problem": result.problem,
                    "charges": result.charges,
                    "report_publication": result.report_publication,
                    "termination_id": result.termination_id,
                    "events": [
                        asdict(e) | {"content": e.content.decode()}
                        for e in assignment.events
                    ],
                    "model_receipts": consumer.receipts,
                    "lineage_id": assignment.host.lineage_id,
                    "semantic_acceptance": "not_evaluated; separate source-to-claim review required",
                }
                private_write(
                    consumer.directory / "assignment.json", json_bytes(record)
                )
                rows.append(
                    {
                        k: record[k]
                        for k in ("assignment", "outcome", "problem", "charges")
                    }
                )
                private_write(
                    output / (spec["id"] + ".checkpoint.json"), json_bytes(rows[-1])
                )
                print(
                    json.dumps(
                        {
                            "assignment": spec["id"],
                            "outcome": result.outcome,
                            "calls": len(consumer.receipts),
                        }
                    ),
                    flush=True,
                )
                if not consumer.usage_complete:
                    raise ValueError(
                        "unknown usage; remaining batch withheld, no rerun"
                    )
            finally:
                if model is not None:
                    model.unload()
    private_write(output / "summary.json", json_bytes({"assignments": rows}))
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sdk-site", type=Path, required=True)
    parser.add_argument("--freeze", type=Path, required=True)
    parser.add_argument("--expected-freeze-sha256", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    sdk = import_isolated_sdk(args.sdk_site)
    execute_comparison(sdk, args.freeze, args.expected_freeze_sha256, args.output)


if __name__ == "__main__":
    main()
