"""Prepare a source-bound runtime freeze, or explicitly activate its six-slot diagnostic.

Both entry points are local-only and separately operated. `prepare_runtime` loads the
single intended point to measure complete requests without prediction. `execute` accepts
only that verified freeze plus its explicit activation hash, runs the cancellation and
report-reference probes first, and withholds all later work on a hard failure. Semantic
grading is offline source review; this module never supplies or scores expected answers.

Neither CLI mode is invoked by offline packet preparation or by the test suite. Runtime
ownership/backend checks reuse the existing qualifier; unknown usage is never zero.
"""

from __future__ import annotations

import argparse
import json
import time
from dataclasses import asdict, replace
from copy import deepcopy
from contextlib import contextmanager
from pathlib import Path

from experiments.investigator_model_interface import (
    ModelLimits, SDKBinding, StatelessInvestigatorModel, digest, fields,
    finalize_owned_runtime, import_isolated_sdk, private_write,
    measure_input, request_presentation, SUPPLIED_REQUEST_PRESENTATION,
)
from experiments.investigator_run_control import MonotonicDeadline, problem_text
from experiments.investigator_supplied_evidence import SuppliedEvidenceLimits, SuppliedEvidenceTrial
from experiments.prepare_investigator_supplied_evidence import (
    PREPARATION_CODE, prepare_recipe, read_recipes, selection_inventory, verify_prepared_packets,
)
from experiments.qualify_investigator_model_interface import (
    canary_assignment, observe_owned_backend, validate_loaded_backend,
)
from upgradepilot.workspace.native_representation import json_bytes

REFERENCE_PROFILE = Path.home() / ".local/share/upgradepilot/investigator-runs/semantic-comparison-2026-10-18-reference-v2/gemma12-preflight/profile.json"
REFERENCE_PROFILE_SHA256 = "793bed85004fe1567c0d567155051e5887a893749e9c6d45c277e40065ff9531"
FREEZE_FORMAT = "investigator-supplied-evidence-runtime-freeze/2"
CAPACITY_PROFILE_FORMAT = "investigator-supplied-evidence-capacity-profile/1"
CONTEXT = 36864
CAPACITY_IDENTIFIER = "up-supplied-capacity-gemma12-36864-v1"
ROLES = ("probe-cancel", "probe-report", "packet-a", "packet-b", "packet-c", "packet-d")
INPUT_CAPS = dict(zip(ROLES, (4096, 4096, 24000, 9000, 27000, 9000), strict=True))
CEILINGS = {
    "attempts": 6, "input_tokens": 77192, "generated_tokens": 49152,
    "prediction_seconds": 4200, "finalization_seconds": 360,
    "batch_seconds": 4800, "preparation_seconds": 1200, "admission_units": 340,
}


def source_hashes():
    return {path: digest(Path(path).read_bytes()) for path in (
        *PREPARATION_CODE, "experiments/qualify_investigator_model_interface.py",
        "experiments/run_investigator_supplied_evidence.py",
    )}


def sdk_source_identity(sdk):
    root = Path(sdk.__file__).parent
    return {name: digest((root / name).read_bytes()) for name in (
        "sync_api.py", "json_api.py", "sdk_api.py", "_ws_thread.py", "_ws_impl.py",
    )}


def reference_profile():
    """Immutable 32k parent; never presented as qualification of the new point."""
    if digest(REFERENCE_PROFILE.read_bytes()) != REFERENCE_PROFILE_SHA256:
        raise ValueError("intended retained deployment profile unavailable/drifted; no substitute")
    return json.loads(REFERENCE_PROFILE.read_bytes())


def capacity_load_request(parent):
    """Prospective request only; contains no purported new observations."""
    requested = deepcopy(parent["requested_load"])
    requested["contextLength"] = CONTEXT
    return {"model_key": parent["model_key"], "identifier": CAPACITY_IDENTIFIER,
        "requested_load": requested}


def observed_capacity_profile(parent, identity, backend):
    """Validate the sole declared delta, then retain actual observed identity/backend.

    The projection below is an expectation against the immutable parent, not an edited
    observation. Only context and the instance label may differ; full load/template,
    placement, cache and model checks stay with the existing qualifier. The returned
    profile uses the actual arguments, never the projected parent's observations.
    """
    expected = deepcopy(parent)
    expected["initial_identity"]["model"].update(
        contextLength=CONTEXT, identifier=CAPACITY_IDENTIFIER,
    )
    load_fields = expected["initial_identity"]["load"]["fields"]
    context_fields = [item for item in load_fields if item["key"] == "llm.load.contextLength"]
    if len(context_fields) != 1:
        raise ValueError("parent load has no unique context field")
    context_fields[0]["value"] = CONTEXT
    expected["backend_observation"]["flags"]["ctx-size"] = str(CONTEXT)
    validate_loaded_backend(expected, identity, backend)
    if identity["load"] != expected["initial_identity"]["load"]:
        raise ValueError("capacity load changed outside the declared context delta")
    return {
        "format": CAPACITY_PROFILE_FORMAT,
        **capacity_load_request(parent),
        "parent_reference_profile_sha256": REFERENCE_PROFILE_SHA256,
        "context": identity["model"]["contextLength"], "output_tokens": 8192,
        "initial_identity": identity, "backend_observation": backend,
        "prediction_configuration": deepcopy(parent["prediction_configuration"]),
        "prediction_base_sha256": parent["prediction_base_sha256"],
        "tokenizer_policy": deepcopy(parent["tokenizer_policy"]),
        "request_presentation": SUPPLIED_REQUEST_PRESENTATION,
        "code_sha256": source_hashes(),
        "qualification": "actual loaded identity/backend only; packet fit is separately frozen; inference unqualified",
    }


def asset_stats(profile):
    """Cheap current checks at inherited asset paths; explicitly not a new full hash."""
    expected = profile["backend_observation"]
    result = {}
    for role, name in (("backend", expected["executable"]), ("model", expected["flags"]["model"])):
        name = name.strip('"')
        if len(name) < 3 or name[1:3] != ":\\":
            raise ValueError("unsupported inherited Windows asset path")
        path = Path("/mnt/" + name[0].lower() + name[2:].replace("\\", "/"))
        stat = path.stat()
        result[role] = {"path": str(path), "bytes": stat.st_size, "mtime_ns": stat.st_mtime_ns,
            "check": "current stat at inherited asset path; not a fresh full-content hash"}
    return result


def private_root(output):
    allowed = Path.home() / ".local/share/upgradepilot/investigator-runs"
    if not output.is_absolute() or not output.resolve().is_relative_to(allowed.resolve()):
        raise ValueError("output must be a fresh durable Investigator retention root")
    output.mkdir(mode=0o700, parents=False, exist_ok=False)


@contextmanager
def bounded_client(sdk, receipt_path, cleanup):
    """Reserve ten seconds for client release after up to fifty for owned unload."""
    previous_timeout = sdk.get_sync_api_timeout()
    sdk.set_sync_api_timeout(600)
    try:
        client = sdk.Client("127.0.0.1:18080")
    except BaseException:
        sdk.set_sync_api_timeout(previous_timeout)
        raise
    primary = failure = traceback = None
    try:
        client.__enter__()
        yield client
    except BaseException as error:
        primary = error
        raise
    finally:
        started = time.monotonic()
        try:
            with MonotonicDeadline(10, label="SDK client release").enforce():
                client.__exit__(None, None, None)
            cleanup["confirmed"] = True
        except BaseException as error:
            failure, traceback = error, error.__traceback__
            cleanup.update(confirmed=False, problem=problem_text(error))
        cleanup["elapsed_seconds"] = time.monotonic() - started
        sdk.set_sync_api_timeout(previous_timeout)
        try:
            private_write(receipt_path, json_bytes(cleanup))
        except BaseException as error:
            cleanup["receipt_problem"] = problem_text(error)
            if failure is None:
                failure, traceback = error, error.__traceback__
        if failure is not None:
            if primary is not None:
                primary.add_note("SDK client release: " + problem_text(failure))
            else:
                raise failure.with_traceback(traceback)


def reviewer_identity(path):
    body = json.loads(path.read_bytes())
    expected = {"packet-a": 6, "packet-b": 4, "packet-c": 6, "packet-d": 4}
    if (
        body.get("format") != "investigator-source-aware-review-protocol/1"
        or {label: len(items) for label, items in body["obligations"].items()} != expected
        or not body.get("reviewer") or not body.get("materiality")
        or any(not item.get("id") or not item.get("criterion") or not item.get("source_locators")
            for items in body["obligations"].values() for item in items)
    ):
        raise ValueError("complete separately frozen source-review obligations required")
    # Only the path/hash enters the freeze. Neither this body nor any reviewer prose
    # is passed to new_trial, protocol construction, packing or model rendering.
    return {"path": str(path.resolve()), "sha256": digest(path.read_bytes())}


def new_trial(role, preparation, qualification, recipes):
    if role.startswith("probe-"):
        assignment = canary_assignment("structured")
        requests = [json_bytes({"tool": "read_source", "arguments": {
            "source_id": "canary", "path": path, "line_count": 1,
        }}) for path in ("probe.txt", "requirements.txt")]
        trial = SuppliedEvidenceTrial(
            assignment, requests, case_label=role,
            limits=SuppliedEvidenceLimits(reads=2, references=2, operations=18, seconds=300),
        )
        trial.prepare()
        return trial
    recipe = next(item for item in recipes["cases"] if item["label"] == role)
    trial = prepare_recipe(qualification, recipe)
    expected = next(item for item in preparation["cases"] if item["label"] == role)
    if digest(json_bytes(selection_inventory(trial))) != expected["selection_inventory_sha256"]:
        raise ValueError("actual fresh packet differs from frozen source selections")
    return trial


def model_limits(role, *, seconds=None):
    probe = role.startswith("probe-")
    return ModelLimits(
        context=CONTEXT, generated_per_call=8192, generated_total=8192,
        input_total=INPUT_CAPS[role], calls=1,
        seconds=seconds or (300 if probe else 900),
        prediction_seconds=1 if role == "probe-cancel" else (300 if probe else 900),
        finalization_seconds=50,
    )


def load_owned(client, profile):
    if client.llm.list_loaded():
        raise ValueError("pre-existing model; no implicit unload")
    downloaded = next(m for m in client.llm.list_downloaded() if m.model_key == profile["model_key"])
    return downloaded.load_new_instance(
        instance_identifier=profile["identifier"], config=profile["requested_load"], ttl=3600,
    )


def validate_owned(binding, profile, output):
    output.mkdir(mode=0o700)
    identity = binding.identity()
    validate_loaded_backend(profile, identity, observe_owned_backend(output))
    if identity["load"] != profile["initial_identity"]["load"]:
        raise ValueError("loaded settings differ from retained intended point")
    return identity


def prepare_runtime(sdk, preparation_root, reviewer_path, output):
    """Separately authorized zero-generation load/render/fit; never calls predict()."""
    preparation = verify_prepared_packets(preparation_root)
    review = reviewer_identity(reviewer_path)
    parent = reference_profile()
    requested = capacity_load_request(parent)
    qualification = json.loads(Path(preparation["qualified_input_path"]).read_bytes())
    recipes = read_recipes(preparation_root / "packet-recipes.json")
    private_root(output)
    started = time.monotonic()
    freeze = {
        "format": FREEZE_FORMAT, "activation": "requires_explicit_matching_freeze_hash",
        "preparation_root": str(preparation_root.resolve()),
        "preparation_sha256": digest((preparation_root / "preparation.json").read_bytes()),
        "reference_profile_sha256": REFERENCE_PROFILE_SHA256,
        "code_sha256": source_hashes(), "reviewer": review,
        "sdk_source_sha256": sdk_source_identity(sdk),
        "non_prediction_rpc_idle_seconds": 600,
        "asset_stats": asset_stats(parent),
        "capacity_contract": {"context": CONTEXT, "input_caps": INPUT_CAPS},
        "ceilings": CEILINGS, "roles": list(ROLES),
        "cancellation_probe": {"required": True, "prediction_deadline_seconds": 1,
            "pass": "deadline failure with terminal protocol, known usage and channel release; then fresh callback only"},
        "fit": {}, "prediction_attempts": 0,
    }
    private_write(output / "preflight-intent.json", json_bytes({
        **freeze, "format": "investigator-supplied-evidence-runtime-preflight-intent/1",
    }))
    private_write(output / "reference-profile.json", json_bytes(parent))
    private_write(output / "capacity-load-request.json", json_bytes(requested))
    with bounded_client(sdk, output / "client-cleanup.json", {}) as client:
        model = None
        try:
            with MonotonicDeadline(1140, label="zero-generation load/fit").enforce():
                model = load_owned(client, requested)
                binding = SDKBinding(model, sdk, parent["tokenizer_policy"], finalization_seconds=50)
                identity = binding.identity()
                private_write(output / "actual-identity.json", json_bytes(identity))
                backend_root = output / "backend"
                backend_root.mkdir(mode=0o700)
                backend = observe_owned_backend(backend_root)
                private_write(output / "actual-backend.json", json_bytes(backend))
                profile = observed_capacity_profile(parent, identity, backend)
                profile_bytes = json_bytes(profile)
                private_write(output / "capacity-profile.json", profile_bytes)
                freeze.update(identity=identity, capacity_profile_sha256=digest(profile_bytes))
                for role in ROLES:
                    trial = new_trial(role, preparation, qualification, recipes)
                    consumer = StatelessInvestigatorModel(
                        binding, profile["prediction_configuration"], model_limits(role), output / role,
                    )
                    packed = trial.pack(consumer)
                    measured = measure_input(binding, packed, profile["prediction_configuration"])
                    private_write(consumer.directory / "fit-packed-input.json", packed.content)
                    private_write(consumer.directory / "fit-rendered.txt", measured.rendered.encode())
                    freeze["fit"][role] = {
                        "request_presentation": request_presentation(json.loads(packed.content)),
                        "rendered_tokens": measured.tokens,
                        "rendered_sha256": digest(measured.rendered.encode()),
                        "packed_sha256": digest(packed.content),
                        "token_ids_sha256": measured.token_ids_sha256,
                        "reference_pairs": sorted(packed.reference_pairs),
                        "omitted_events": packed.omitted_event_ids,
                        "input_cap_met": measured.tokens <= model_limits(role).input_total,
                        "context_reserve_met": measured.tokens + 8192 + 256 <= CONTEXT,
                    }
                    # Persist failed measurements before withholding. Tokenization of
                    # complete input is not neural prediction and needs no truncation.
                    private_write(consumer.directory / "fit-measurement.json", json_bytes(freeze["fit"][role]))
                    freeze["fit"][role]["preparation_termination_id"] = trial.assignment.host.terminate(
                        trial.assignment.host.lineage_id, "interrupted",
                        "Zero-generation fit only; no report prediction/publication attempted.",
                    )
        finally:
            if model is not None:
                finalize_owned_runtime(model, client.llm.list_loaded, output / "cleanup.json",
                    seconds=min(50, max(.001, 1190 - (time.monotonic() - started))))
    freeze["preparation_elapsed_seconds"] = time.monotonic() - started
    if freeze["preparation_elapsed_seconds"] >= 1200:
        raise ValueError("zero-generation preparation ceiling exceeded")
    private_write(output / "runtime-preflight.json", json_bytes({
        **freeze, "format": "investigator-supplied-evidence-runtime-preflight/1",
        "admission": "measurement_only; not_an_executable_freeze",
    }))
    if not all(fit["input_cap_met"] and fit["context_reserve_met"] for fit in freeze["fit"].values()):
        raise ValueError("complete packet exceeds declared input/context limits; measurements retained, no freeze")
    private_write(output / "freeze.json", json_bytes(freeze))
    return freeze


def verify_freeze(path, expected_hash):
    if digest(path.read_bytes()) != expected_hash:
        raise ValueError("runtime freeze hash mismatch")
    freeze = json.loads(path.read_bytes())
    if (
        freeze["format"] != FREEZE_FORMAT or freeze["ceilings"] != CEILINGS
        or freeze["activation"] != "requires_explicit_matching_freeze_hash"
        or freeze["roles"] != list(ROLES) or freeze["code_sha256"] != source_hashes()
        or freeze["reference_profile_sha256"] != REFERENCE_PROFILE_SHA256
        or set(freeze["fit"]) != set(ROLES) or freeze["prediction_attempts"] != 0
        or freeze["cancellation_probe"]["prediction_deadline_seconds"] != 1
        or freeze["cancellation_probe"]["required"] is not True
        or not 0 <= freeze["preparation_elapsed_seconds"] < 1200
        or freeze["non_prediction_rpc_idle_seconds"] != 600
        or freeze.get("capacity_contract") != {"context": CONTEXT, "input_caps": INPUT_CAPS}
    ):
        raise ValueError("unsupported/drifted/incomplete diagnostic freeze")
    profile_bytes = (path.parent / "capacity-profile.json").read_bytes()
    if digest(profile_bytes) != freeze.get("capacity_profile_sha256"):
        raise ValueError("observed capacity profile identity drift")
    profile = json.loads(profile_bytes)
    parent = reference_profile()
    if profile != observed_capacity_profile(parent, freeze["identity"], profile["backend_observation"]):
        raise ValueError("observed capacity profile differs from its declared inheritance")
    for role, fit in freeze["fit"].items():
        if fit.get("request_presentation") != SUPPLIED_REQUEST_PRESENTATION:
            raise ValueError("supplied presentation identity drift; fresh fit required")
        if not 0 < fit["rendered_tokens"] <= model_limits(role).input_total or fit["omitted_events"]:
            raise ValueError("complete actual request fit not established")
        if (not fit["input_cap_met"] or not fit["context_reserve_met"]
            or fit["rendered_tokens"] + 8192 + 256 > CONTEXT):
            raise ValueError("required input/context fit gate failed")
        if not fit.get("preparation_termination_id"):
            raise ValueError("preflight host terminal publication unconfirmed")
        for filename, key in (("fit-packed-input.json", "packed_sha256"), ("fit-rendered.txt", "rendered_sha256")):
            if digest((path.parent / role / filename).read_bytes()) != fit[key]:
                raise ValueError("retained actual fit artifact drift")
    if reviewer_identity(Path(freeze["reviewer"]["path"])) != freeze["reviewer"]:
        raise ValueError("review protocol drift")
    root = Path(freeze["preparation_root"])
    if digest((root / "preparation.json").read_bytes()) != freeze["preparation_sha256"]:
        raise ValueError("offline preparation identity drift")
    preparation = verify_prepared_packets(root)
    if asset_stats(reference_profile()) != freeze["asset_stats"]:
        raise ValueError("intended model/backend asset stat changed; fresh disposition required")
    return freeze, preparation


def probe_passed(role, trial, consumer):
    if len(consumer.receipts) != 1 or not consumer.usage_complete:
        return False
    receipt = consumer.receipts[0]
    if role == "probe-cancel":
        control = receipt.get("control") or {}
        if not (
            trial.result.outcome == "failed" and receipt["outcome"] == "failed"
            and "PredictionDeadlineExceeded" in receipt.get("problem", "")
            and control.get("cancellation_requested") and control.get("terminal_received")
            and control.get("channel_released") and not control.get("secondary_problems")
            and control.get("receive_ownership", {}).get("receiver_stopped") is True
        ):
            return False
        metadata = json.loads((consumer.directory / "call-01.metadata.json").read_bytes())
        request = json.loads((consumer.directory / "call-01.request.json").read_bytes())
        return (
            metadata["modelInfo"]["instanceReference"] == consumer.identity["model"]["instanceReference"]
            and all(fields(metadata["predictionConfig"]).get(key) == value
                for key, value in fields(request["configuration"]["layers"][0]["config"]).items())
            and consumer.binding.identity() == consumer.identity
        )
    return (
        trial.result.outcome == "completed" and receipt["outcome"] == "returned"
        and bool(trial.result.report_publication["citation_ids"])
    )


def execute(sdk, freeze_path, expected_hash, activation_hash, output):
    """One frozen cohort, no retries/resume or semantic feedback between attempts."""
    if activation_hash != expected_hash:
        raise ValueError("explicit matching runtime-freeze activation required before model loading")
    freeze, preparation = verify_freeze(freeze_path, expected_hash)
    if sdk_source_identity(sdk) != freeze["sdk_source_sha256"]:
        raise ValueError("installed SDK source differs from the runtime freeze")
    profile = json.loads((freeze_path.parent / "capacity-profile.json").read_bytes())
    root = Path(freeze["preparation_root"])
    qualification = json.loads(Path(preparation["qualified_input_path"]).read_bytes())
    recipes = read_recipes(root / "packet-recipes.json")
    private_root(output)
    private_write(output / "executed-freeze.json", freeze_path.read_bytes())
    rows = [{"role": role, "execution": "unattempted", "semantic_acceptance": "not_evaluated"} for role in ROLES]
    spent = {"input": 0, "generated": 0, "operations": 0, "prediction_seconds": 0,
        "finalization_seconds": 0, "known_usage_attempts": 0, "unknown_usage_attempts": 0}
    batch_started = None
    failure = traceback = None
    client_cleanup = {}
    try:
        with bounded_client(sdk, output / "client-cleanup.json", client_cleanup) as client:
            model = None
            try:
                with MonotonicDeadline(1140, label="diagnostic model load").enforce():
                    model = load_owned(client, profile)
                    binding = SDKBinding(model, sdk, profile["tokenizer_policy"], finalization_seconds=50)
                    validate_owned(binding, profile, output / "backend")
                for row in rows:
                    role = row["role"]
                    row["preparation"] = "started"
                    row["preparation_operation_reservation"] = 18 if role.startswith("probe-") else 76
                    remaining = 4800 if batch_started is None else 4800 - (time.monotonic() - batch_started)
                    if remaining <= 60:
                        raise ValueError("batch deadline refuses another prediction")
                    with MonotonicDeadline(min(240, remaining - 60), label="fresh packet/dispatch preparation").enforce():
                        trial = new_trial(role, preparation, qualification, recipes)
                        limits = model_limits(role, seconds=min(model_limits(role).seconds, int(remaining - 60)))
                        consumer = StatelessInvestigatorModel(binding, profile["prediction_configuration"], limits, output / role)
                        packed = trial.pack(consumer)
                        measured = consumer.prepare(packed)
                        if measured.tokens > limits.input_total:
                            raise ValueError("actual fresh request fit exceeds input cap; no packet omission")
                        private_write(consumer.directory / "reference-map.json", json_bytes([
                            asdict(reference) for reference in trial.assignment.references.values()
                        ]))
                    row["preparation"] = "completed"
                    if batch_started is None:
                        batch_started = time.monotonic()
                    consumer.limits = replace(consumer.limits, seconds=min(
                        consumer.limits.seconds, int(batch_started + 4800 - 60 - consumer.started)
                    ))
                    # Immutable per-model reservation precedes actual dispatch. A missing
                    # result/receipt becomes an orphan attempt; this fresh output cannot resume.
                    row.update(execution="attempt_reserved", rendered_tokens=measured.tokens,
                        reserved_generated_tokens=8192, reserved_input_tokens=limits.input_total)
                    private_write(output / (role + ".reservation.json"), json_bytes(row))
                    interrupted = interrupted_traceback = None
                    try:
                        result = trial.run(consumer)
                    except BaseException as error:
                        interrupted, interrupted_traceback = error, error.__traceback__
                        result = trial.result
                    finally:
                        if consumer.receipts:
                            receipt = consumer.receipts[0]
                            row.update(model_receipts=consumer.receipts, usage_complete=consumer.usage_complete)
                            if not consumer.usage_complete:
                                row["unknown_usage_reservation"] = {"input": limits.input_total, "generated": 8192}
                                spent["unknown_usage_attempts"] += 1
                            else:
                                spent["input"] += consumer.input_tokens
                                spent["generated"] += consumer.output_tokens
                                spent["known_usage_attempts"] += 1
                            spent["prediction_seconds"] += receipt.get("prediction_elapsed_seconds") or 0
                            if trial.result is not None:
                                spent["finalization_seconds"] += trial.result.charges["total_finalization_elapsed_seconds"]
                        spent["operations"] += trial.charges["admission_operations"]
                    row["prediction_attempts"] = len(consumer.receipts)
                    if result is not None:
                        row.update(execution=result.outcome, problem=result.problem,
                            charges=result.charges, termination_id=result.termination_id,
                            report_publication=result.report_publication)
                    else:
                        row.update(execution="failed_before_prediction", problem=problem_text(interrupted))
                    private_write(output / (role + ".result.json"), json_bytes(row))
                    if interrupted is not None:
                        raise interrupted.with_traceback(interrupted_traceback)
                    if not consumer.receipts:
                        raise ValueError("no prediction receipt; later cohort withheld")
                    if not consumer.usage_complete:
                        raise ValueError("unknown usage; whole remaining cohort withheld")
                    if any(spent[key] > CEILINGS[limit] for key, limit in (
                        ("input", "input_tokens"), ("generated", "generated_tokens"),
                        ("operations", "admission_units"), ("prediction_seconds", "prediction_seconds"),
                        ("finalization_seconds", "finalization_seconds"),
                    )):
                        raise ValueError("aggregate resource ceiling reached; no further prediction")
                    if role.startswith("probe-"):
                        if not probe_passed(role, trial, consumer):
                            raise ValueError("required probe failed; semantic cohort withheld without retry")
                    elif result.outcome != "completed" or consumer.blocked:
                        raise ValueError("hard interface/control/publication failure; later cases withheld")
            except BaseException as error:
                failure, traceback = error, error.__traceback__
            finally:
                if model is not None:
                    try:
                        finalizing = time.monotonic()
                        remaining_batch = 60 if batch_started is None else 4800 - (finalizing - batch_started)
                        finalize_owned_runtime(model, client.llm.list_loaded, output / "cleanup.json",
                            seconds=min(50, max(.001, remaining_batch - 10), max(.001, 350 - spent["finalization_seconds"])))
                    except BaseException as error:
                        if failure is None:
                            failure, traceback = error, error.__traceback__
                        else:
                            failure.add_note("Runtime cleanup: " + problem_text(error))
                    finally:
                        spent["finalization_seconds"] += time.monotonic() - finalizing
                if batch_started is not None and time.monotonic() - batch_started >= 4800 and failure is None:
                    failure = ValueError("batch elapsed ceiling exceeded; no acceptance")
            if failure is not None:
                raise failure.with_traceback(traceback)
    except BaseException as error:
        failure, traceback = error, error.__traceback__
    spent["finalization_seconds"] += client_cleanup.get("elapsed_seconds", 0)
    if failure is None and (spent["finalization_seconds"] > 360 or (batch_started is not None and time.monotonic() - batch_started >= 4800)):
        failure = ValueError("finalization/batch ceiling exceeded; no acceptance")
    summary = {"rows": rows, "measured_known_usage": spent,
        "problem": problem_text(failure) if failure else None,
        "batch_elapsed_seconds": time.monotonic() - batch_started if batch_started else 0,
        "semantic_acceptance": "not_evaluated; offline frozen source review required"}
    try:
        private_write(output / "summary.json", json_bytes(summary))
    except BaseException as error:
        if failure is None:
            failure, traceback = error, error.__traceback__
        else:
            failure.add_note("Summary persistence: " + problem_text(error))
    if failure is not None:
        raise failure.with_traceback(traceback)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("prepare-runtime", "execute"))
    parser.add_argument("--sdk-site", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--preparation", type=Path)
    parser.add_argument("--reviewer-protocol", type=Path)
    parser.add_argument("--freeze", type=Path)
    parser.add_argument("--freeze-sha256")
    parser.add_argument("--activate-freeze-sha256")
    args = parser.parse_args()
    if args.mode == "prepare-runtime":
        if args.preparation is None or args.reviewer_protocol is None:
            parser.error("runtime preparation needs actual offline preparation and reviewer protocol")
        sdk = import_isolated_sdk(args.sdk_site)
        result = prepare_runtime(sdk, args.preparation, args.reviewer_protocol, args.output)
        print(json.dumps({"freeze_sha256": digest((args.output / "freeze.json").read_bytes()), "prediction_attempts": result["prediction_attempts"]}))
    else:
        if args.freeze is None or not args.freeze_sha256 or args.activate_freeze_sha256 != args.freeze_sha256:
            parser.error("execution requires actual freeze path/hash and explicit matching activation hash")
        sdk = import_isolated_sdk(args.sdk_site)
        result = execute(sdk, args.freeze, args.freeze_sha256, args.activate_freeze_sha256, args.output)
        print(json.dumps({"attempts": len(result["rows"]), "semantic_acceptance": result["semantic_acceptance"]}))


if __name__ == "__main__":
    main()
