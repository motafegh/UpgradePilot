"""Prepare and execute frozen independent local interface canaries, never case comparison.

Preparation loads only the named owned instance, measures short/near-envelope and late/
report requests using synthetic native/source material, retains full rendering/configuration
and unloads it. Execution requires a separately inspected, hash-bound batch freeze. Each
assignment is fresh, serial and limited to six calls, with no retry beyond the trial's
already frozen correction allowance. Raw requests/responses remain owner-only outside Git.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from dataclasses import asdict
from pathlib import Path

from experiments.investigator_model_interface import (
    REQUEST_PRESENTATION,
    ModelLimits,
    SDKBinding,
    StatelessInvestigatorModel,
    digest,
    import_isolated_sdk,
    measure_input,
    prediction_configuration,
    private_write,
    run_model_trial,
)
from experiments.investigator_workspace_adapter import InvestigatorAssignment
from experiments.investigator_workspace_trial import (
    TrialLimits,
    pack_input,
    protocol_definition,
)
from upgradepilot.dependency.change import (
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.workspace.native_capture import NativeInvestigationCapture
from upgradepilot.workspace.native_representation import json_bytes
from upgradepilot.workspace.source_access import (
    RetainedSourceCatalog,
    RetainedSourceFile,
    RetainedSourceScope,
)

PADDING = "Independent capacity calibration text; no source or action authority.\n"
CANDIDATES = (
    "google/gemma-4-12b",
    "qwen3.8-27b-ud",
    "gemma-4-e2b-it",
    "gemma-4-e4b-it-ud",
    "mimo-v2.6-distill-qwen-9b",
    "qwen3.5-9b-ud",
)
CODE_FILES = (
    Path("experiments/investigator_model_interface.py"),
    Path("experiments/qualify_investigator_model_interface.py"),
    Path("experiments/investigator_workspace_trial.py"),
    Path("experiments/investigator_workspace_adapter.py"),
)


def code_hashes():
    return {str(p): digest(p.read_bytes()) for p in CODE_FILES}


def observe_owned_backend(output):
    """Retain only allowlisted process settings; never emit an entire command line.

    LM Studio's internal process arguments contain an ephemeral credential. It is not
    needed for this SDK path and must never enter stdout, receipts or a subprocess API.
    The app-generated temporary template is copied while the owned model is loaded.
    """
    command = r"""$items = @(Get-CimInstance Win32_Process -Filter "name = 'llama-server.exe'");
$safe = @($items | ForEach-Object {
  $line = $_.CommandLine; $flags = @{};
  foreach ($flag in @('n-gpu-layers','ctx-size','parallel','batch-size','ubatch-size','cache-type-k','cache-type-v','flash-attn','model','chat-template-file')) {
    $match = [regex]::Match($line, '--' + $flag + '\s+(.+?)(?=\s+--|$)');
    if ($match.Success) { $flags[$flag] = $match.Groups[1].Value }
  }
  [pscustomobject]@{executable=$_.ExecutablePath; flags=$flags; cpu_kv=$line.Contains('--no-kv-offload')}
}); ConvertTo-Json -InputObject $safe -Depth 5 -Compress"""
    result = subprocess.run(
        [
            "/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe",
            "-NoProfile",
            "-Command",
            command,
        ],
        check=True,
        capture_output=True,
        timeout=30,
    )
    entries = json.loads(result.stdout)
    if len(entries) != 1:
        raise ValueError("cannot identify a single owned backend process")
    observation = entries[0]
    name = observation["flags"]["chat-template-file"].strip('"')
    source = Path("/mnt/" + name[0].lower() + name[2:].replace("\\", "/"))
    allowed = Path("/mnt/c/Users/lenovo/.cache/lm-studio/.internal/temp")
    if not source.resolve().is_relative_to(allowed):
        raise ValueError(
            "backend template is outside the expected generated-template directory"
        )
    content = source.read_bytes()
    private_write(output / "backend-template.jinja", content)
    observation["backend_template_sha256"] = digest(content)
    private_write(output / "backend-observation.json", json_bytes(observation))
    return observation


def validate_batch_freeze(freeze):
    """Arm selection/order and every assignment are explicit before any SDK load/call."""
    if (
        freeze["format"] != "investigator-interface-canary-freeze/1"
        or not freeze["preflight_inspected"]
        or not freeze["inference_admitted"]
        or freeze["later_semantic_comparison_admitted"]
    ):
        raise ValueError("unsupported or uninspected inference freeze")
    keys = [item["model_key"] for item in freeze["deployments"]]
    assignments = freeze["assignments"]
    triples = [(a["model_key"], a["treatment"], a["sequence"]) for a in assignments]
    expected = {
        (key, treatment, sequence)
        for key in keys
        for treatment in ("raw", "structured")
        for sequence in (1, 2)
    }
    if (
        len(keys) != freeze["deployment_count"]
        or len(set(keys)) != len(keys)
        or not set(keys).issubset(CANDIDATES)
        or len(triples) != len(expected)
        or set(triples) != expected
        or len({a["id"] for a in assignments}) != len(assignments)
        or freeze["calls_per_sequence"] > 6
        or freeze["calls_per_sequence"] < 2
        or freeze["max_model_calls"] != freeze["calls_per_sequence"] * len(assignments)
        or freeze["prior_spent_calls"] + freeze["max_model_calls"]
        > freeze["cycle_call_ceiling"]
        or [a["model_key"] for a in assignments]
        != [key for key in keys for _ in range(4)]
    ):
        raise ValueError("deployment/assignment/order/budget freeze is inconsistent")


def validate_loaded_backend(profile, identity, observation):
    """A registry alias/load receipt alone does not bind the actual GGUF or placement."""
    expected = profile["backend_observation"]
    for key in ("executable", "cpu_kv", "backend_template_sha256"):
        if observation[key] != expected[key]:
            raise ValueError("actual backend/template/cache changed since preflight")
    for key, value in expected["flags"].items():
        if key != "chat-template-file" and observation["flags"].get(key) != value:
            raise ValueError("actual model file/backend placement changed: " + key)
    for key, value in profile["initial_identity"]["model"].items():
        if key != "instanceReference" and identity["model"].get(key) != value:
            raise ValueError("actual model identity changed: " + key)


def assess_canary(assignment, sequence, result):
    """Completion alone cannot qualify a model that skipped the required interface work."""
    expected = (
        [
            "read_source",
            "search_sources",
            "read_source",
            "finish_investigation",
        ]
        if sequence == 1
        else [
            "read_native" if assignment.treatment == "structured" else "read_source",
            "read_source",
            "read_source" if assignment.treatment == "structured" else "search_sources",
            "finish_investigation",
        ]
    )
    # A refused request remains charged/retained but cannot replace a required read.
    # The frozen sixth call permits one correction without erasing its original.
    observations = [
        json.loads(e.content) for e in assignment.events if e.outcome != "refused"
    ]
    if (
        result.outcome != "completed"
        or [e.get("tool") for e in observations] != expected
    ):
        return "withheld", "required canary sequence did not complete"
    if sequence == 1 and [e["outcome"] for e in observations][1:3] != [
        "scoped_negative",
        "empty",
    ]:
        return "withheld", "scoped zero/empty distinctions not exercised"
    if sequence == 2 and observations[1]["outcome"] != "problem":
        return "withheld", "missing-source problem not exercised"
    positive = 0 if assignment.treatment == "raw" or sequence == 1 else 2
    if observations[positive]["outcome"] != "observed" or not observations[
        positive
    ].get("evidence"):
        return "withheld", "positive source read did not deliver evidence"
    if not result.report_publication["reference_mapping"]:
        return "withheld", "report cited no eligible evidence"
    return (
        "qualified",
        "bounded synthetic interface sequence completed; no semantic acceptance",
    )


def canary_assignment(treatment):
    """Explicit synthetic capture; no retained case answers, acquisition or target work."""
    pull = PullRequestIdentity(
        "qualification/synthetic",
        1,
        "Interface canary",
        "open",
        False,
        "canary",
        "base",
        "a" * 40,
        "head",
        "b" * 40,
        1,
    )
    change = DependencyVersionChange(
        "canary-package",
        "canary-package",
        "1.0",
        "1.1",
        (
            DependencyChangeSourceEvidence(
                "requirements.txt", "exact_requirement", "changed_file_patch"
            ),
        ),
    )
    capture = NativeInvestigationCapture()
    capture.start(
        pull, (ChangedFile("requirements.txt", "modified", 1, 1, 2, ""),), change, ()
    )
    boundary = capture.partial_snapshot()
    catalog = RetainedSourceCatalog(
        (
            RetainedSourceScope(
                "canary",
                pull.repository,
                pull.head_sha,
                "repository_text",
                "Synthetic interface canary",
                "No real compatibility claim",
            ),
        ),
        (
            RetainedSourceFile(
                "canary", "probe.txt", "Synthetic retained marker: interface-ready.\n"
            ),
            RetainedSourceFile("canary", "empty.txt", ""),
            RetainedSourceFile("canary", "requirements.txt", "canary-package==1.1\n"),
        ),
        target=boundary.target,
    )
    return InvestigatorAssignment(boundary, catalog, treatment, max_native_bytes=4096)


def canary_protocol(assignment, sequence, padding_count):
    protocol = protocol_definition(assignment, TrialLimits(consumer_turns=6))
    if sequence == 1:
        actions = (
            'read_source with source_id="canary", path="probe.txt"; search_sources in canary for exactly '
            '"NO_SUCH_CANARY_MARKER_91"; read_source with source_id=canary, path=empty.txt; '
            "finish_investigation; final report"
        )
    else:
        first = (
            'read_native families=["ci_coverage"]'
            if assignment.treatment == "structured"
            else 'read_source with source_id="canary", path="probe.txt"'
        )
        third = (
            'read_source with source_id="canary", path="probe.txt"'
            if assignment.treatment == "structured"
            else 'search_sources in canary for exactly "NO_SUCH_CANARY_MARKER_91"'
        )
        actions = f"{first}; read_source with source_id=canary, path=missing.txt; {third}; finish_investigation; final report"
    protocol["task"]["goal"] = (
        "INDEPENDENT SYNTHETIC INTERFACE CANARY. Perform five required steps, "
        "with at most six responses including any correction. Perform "
        f'these steps in order, one per response: {actions}. Use source_id="canary" and path '
        "without the source prefix. Follow the actual tool schemas. In the final report cite "
        "at least one currently visible delivered typed reference, retain uncertainty about "
        "runtime/compatibility, and distinguish scoped zero, empty and missing-file outcomes. "
        "A zero-match search does NOT replace the separate empty-file read. An empty or "
        "missing-file result counts as an attempted step; continue to the next listed step. "
        "Do not finish before all three requested evidence operations have been attempted "
        "in order. Read the included events to determine the next step; do not repeat a "
        "completed operation. Keep the final report concise, at most 350 words, with every "
        "required schema field and no invented compatibility conclusion. "
        "This tests interface completion, not real dependency reasoning."
    )
    protocol["task"]["capacity_calibration"] = PADDING * padding_count
    return protocol


def representative_inputs(binding, configuration, treatment, sequence, padding_count):
    assignment = canary_assignment(treatment)
    protocol = canary_protocol(assignment, sequence, padding_count)
    history = []
    shapes = []
    # Real adapter events over synthetic retained inputs, not fabricated delivery JSON.
    requests = [
        ("read_source", {"source_id": "canary", "path": "probe.txt"}),
        (
            "search_sources",
            {"source_id": "canary", "query": "NO_SUCH_CANARY_MARKER_91"},
        ),
        ("read_source", {"source_id": "canary", "path": "empty.txt"}),
        ("read_source", {"source_id": "canary", "path": "missing.txt"}),
    ]
    if treatment == "structured":
        requests.append(("read_native", {"families": ["ci_coverage"]}))
    for label in ("initial", "late", "report"):
        if label == "late":
            for tool, arguments in requests:
                history.append(
                    assignment.invoke(
                        json_bytes({"tool": tool, "arguments": arguments})
                    )
                )
        phase = "report" if label == "report" else "investigate"
        packed = pack_input(protocol, history, phase, 128 * 1024)
        measured = measure_input(binding, packed, configuration)
        shapes.append((label, measured))
    return protocol, shapes


def prepare_profile(
    sdk,
    model_key,
    identifier,
    requested,
    output,
    tokenizer_policy,
    output_tokens=8192,
    prediction_base=None,
):
    output.mkdir(mode=0o700, parents=True, exist_ok=False)
    for path in CODE_FILES:
        private_write(output / path.name, path.read_bytes())
    with sdk.Client("127.0.0.1:18080") as client:
        if client.llm.list_loaded():
            raise ValueError(
                "preparation requires no pre-existing loaded instance; no implicit unload"
            )
        download = next(
            m for m in client.llm.list_downloaded() if m.model_key == model_key
        )
        model = None
        try:
            model = download.load_new_instance(
                instance_identifier=identifier, config=requested, ttl=3600
            )
            binding = SDKBinding(model, sdk, tokenizer_policy)
            identity = binding.identity()
            backend = observe_owned_backend(output)
            configuration = prediction_configuration(
                identity["load"],
                output_tokens=output_tokens,
                applied_base=prediction_base,
            )
            profile = {
                "format": "investigator-interface-profile/1",
                "model_key": model_key,
                "identifier": identifier,
                "requested_load": requested,
                "initial_identity": identity,
                "prediction_configuration": configuration,
                "context": model.get_context_length(),
                "output_tokens": output_tokens,
                "request_presentation": REQUEST_PRESENTATION,
                "prediction_base_sha256": digest(json_bytes(prediction_base))
                if prediction_base is not None
                else None,
                "measurements": [],
                "padding_count": 0,
                "code_sha256": code_hashes(),
                "qualification": "preflight only; no inference or semantic outcome",
                "backend_observation": backend,
                "tokenizer_policy": tokenizer_policy,
            }
            if profile["context"] != requested["contextLength"]:
                raise ValueError("requested context not applied")
            # About 19k calibration tokens plus fixed input. The same padding is used
            # for both treatments; all final shapes are measured, never byte-estimated.
            per_unit = len(binding.tokenize(PADDING * 100)) / 100
            padding = max(1, int(18000 / per_unit))
            for sequence, count in ((1, 0), (2, padding)):
                for treatment in ("raw", "structured"):
                    protocol, shapes = representative_inputs(
                        binding, configuration, treatment, sequence, count
                    )
                    private_write(
                        output / f"{treatment}-{sequence}.protocol.json",
                        json_bytes(protocol),
                    )
                    for label, measurement in shapes:
                        if (
                            measurement.tokens + output_tokens + 256
                            > profile["context"]
                        ):
                            raise ValueError(
                                "representative complete input/reserve cannot fit"
                            )
                        name = f"{treatment}-{sequence}-{label}"
                        private_write(
                            output / f"{name}.rendered.txt",
                            measurement.rendered.encode(),
                        )
                        private_write(
                            output / f"{name}.packed.json", measurement.packed.content
                        )
                        profile["measurements"].append(
                            {
                                "shape": name,
                                "input_tokens": measurement.tokens,
                                "references": sorted(measurement.packed.reference_ids),
                                "omitted_event_ids": measurement.packed.omitted_event_ids,
                                "rendered_sha256": digest(
                                    measurement.rendered.encode()
                                ),
                                "token_ids_sha256": measurement.token_ids_sha256,
                            }
                        )
            profile["padding_count"] = padding
            private_write(output / "profile.json", json_bytes(profile))
            return profile
        except Exception as error:
            private_write(
                output / "preparation-failure.json",
                json_bytes(
                    {
                        "error": f"{type(error).__name__}: {error}",
                        "model_key": model_key,
                        "requested_load": requested,
                        "inference_calls": 0,
                    }
                ),
            )
            raise
        finally:
            if model is not None:
                model.unload()


def execute_frozen(sdk, freeze_path, expected_hash, output):
    content = freeze_path.read_bytes()
    if digest(content) != expected_hash:
        raise ValueError("batch freeze hash mismatch")
    freeze = json.loads(content)
    validate_batch_freeze(freeze)
    if freeze["code_sha256"] != code_hashes():
        raise ValueError("code changed after freeze")
    for item in freeze["immutable_files"]:
        stat = Path(item["path"]).stat()
        if stat.st_size != item["bytes"] or stat.st_mtime_ns != item["mtime_ns"]:
            raise ValueError("hashed local asset/runtime changed before inference")
    output.mkdir(mode=0o700, parents=True, exist_ok=False)
    summaries = []
    output_tokens = freeze.get("per_sequence", {}).get(
        "per_call_generation_reserve", 8192
    )
    with sdk.Client("127.0.0.1:18080") as client:
        if client.llm.list_loaded():
            raise ValueError("pre-existing loaded models; no implicit unload")
        for deployment in freeze["deployments"]:
            path = Path(deployment["profile_path"])
            data = path.read_bytes()
            if digest(data) != deployment["profile_sha256"]:
                raise ValueError("profile changed")
            profile = json.loads(data)
            if profile["model_key"] != deployment["model_key"]:
                raise ValueError("profile belongs to another selected deployment")
            if profile.get("output_tokens", 8192) != output_tokens:
                raise ValueError("profile generation reserve differs from freeze")
            model = None
            try:
                download = next(
                    m
                    for m in client.llm.list_downloaded()
                    if m.model_key == profile["model_key"]
                )
                model = download.load_new_instance(
                    instance_identifier=profile["identifier"],
                    config=profile["requested_load"],
                    ttl=3600,
                )
                binding = SDKBinding(model, sdk, profile["tokenizer_policy"])
                identity = binding.identity()
                observed_path = output / (
                    str(freeze["deployments"].index(deployment)) + "-backend"
                )
                observed_path.mkdir(mode=0o700)
                validate_loaded_backend(
                    profile, identity, observe_owned_backend(observed_path)
                )
                # New instance IDs are expected; load/template settings must be identical.
                if identity["load"] != profile["initial_identity"]["load"]:
                    raise ValueError(
                        "applied load/template differs from inspected profile"
                    )
                for assignment_spec in freeze["assignments"]:
                    if assignment_spec["model_key"] != profile["model_key"]:
                        continue
                    treatment, sequence = (
                        assignment_spec["treatment"],
                        assignment_spec["sequence"],
                    )
                    assignment = canary_assignment(treatment)
                    protocol = canary_protocol(
                        assignment,
                        sequence,
                        0 if sequence == 1 else profile["padding_count"],
                    )
                    model_consumer = StatelessInvestigatorModel(
                        binding,
                        profile["prediction_configuration"],
                        ModelLimits(
                            context=profile["context"],
                            calls=freeze["calls_per_sequence"],
                            generated_per_call=output_tokens,
                            generated_total=freeze["calls_per_sequence"]
                            * output_tokens,
                        ),
                        output / assignment_spec["id"],
                    )

                    result = run_model_trial(
                        assignment,
                        model_consumer,
                        limits=TrialLimits(consumer_turns=freeze["calls_per_sequence"]),
                        protocol=protocol,
                    )
                    disposition, reason = assess_canary(assignment, sequence, result)
                    record = {
                        "assignment": assignment_spec,
                        "outcome": result.outcome,
                        "problem": result.problem,
                        "trial_charges": result.charges,
                        "model_attempts": len(model_consumer.receipts),
                        "known_input_tokens": model_consumer.input_tokens,
                        "known_generated_tokens": model_consumer.output_tokens,
                        "usage_complete": model_consumer.usage_complete,
                        "reasoning_tokens": None,
                        "report_publication": result.report_publication,
                        "events": [
                            asdict(e) | {"content": e.content.decode()}
                            for e in assignment.events
                        ],
                        "identity": identity,
                        "disposition": disposition,
                        "disposition_reason": reason,
                    }
                    private_write(
                        model_consumer.directory / "assignment.json", json_bytes(record)
                    )
                    summaries.append(
                        {
                            k: record[k]
                            for k in (
                                "assignment",
                                "outcome",
                                "problem",
                                "model_attempts",
                                "known_input_tokens",
                                "known_generated_tokens",
                                "usage_complete",
                                "reasoning_tokens",
                                "disposition",
                                "disposition_reason",
                            )
                        }
                    )
                    private_write(
                        output / f"{assignment_spec['id']}.summary.json",
                        json_bytes(summaries[-1]),
                    )
                    if disposition != "qualified" and not freeze.get(
                        "continue_independent_sequences_after_failure", False
                    ):
                        break
            except Exception as error:  # noqa: BLE001 - preserve each independent deployment failure
                # A broken load/profile prevents this deployment's calls, not the
                # independent candidates. Preserve it without an implicit fallback.
                private_write(
                    output
                    / f"deployment-{freeze['deployments'].index(deployment)}-failure.json",
                    json_bytes(
                        {
                            "model_key": deployment["model_key"],
                            "error": f"{type(error).__name__}: {error}",
                            "disposition": "withheld",
                            "semantic_comparison_runs": 0,
                        }
                    ),
                )
            finally:
                if model is not None:
                    model.unload()
    completed_ids = {item["assignment"]["id"] for item in summaries}
    for assignment in freeze["assignments"]:
        if assignment["id"] not in completed_ids:
            summaries.append(
                {
                    "assignment": assignment,
                    "disposition": "withheld_before_call",
                    "disposition_reason": "earlier canary withheld this deployment",
                    "model_attempts": 0,
                }
            )
    private_write(
        output / "summary.json",
        json_bytes({"assignments": summaries, "semantic_comparison_runs": 0}),
    )
    return summaries


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sdk-site", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model", choices=CANDIDATES)
    parser.add_argument("--identifier")
    parser.add_argument("--load-config", type=Path)
    parser.add_argument("--tokenizer-policy", type=Path)
    parser.add_argument("--output-tokens", type=int, default=8192)
    parser.add_argument("--prediction-base", type=Path)
    parser.add_argument("--execute-freeze", type=Path)
    parser.add_argument("--expected-freeze-sha256")
    args = parser.parse_args()
    sdk = import_isolated_sdk(args.sdk_site)
    sdk.set_sync_api_timeout(600)
    if args.execute_freeze:
        try:
            result = execute_frozen(
                sdk, args.execute_freeze, args.expected_freeze_sha256, args.output
            )
        except Exception as error:
            if args.output.exists():
                private_write(
                    args.output / "execution-failure.json",
                    json_bytes(
                        {
                            "error": f"{type(error).__name__}: {error}",
                            "freeze": str(args.execute_freeze),
                            "semantic_comparison_runs": 0,
                        }
                    ),
                )
            raise
        print(json.dumps(result))
    else:
        if not (
            args.model
            and args.identifier
            and args.load_config
            and args.tokenizer_policy
        ):
            parser.error(
                "preparation needs model/identifier/load-config/tokenizer-policy"
            )
        profile = prepare_profile(
            sdk,
            args.model,
            args.identifier,
            json.loads(args.load_config.read_bytes()),
            args.output,
            json.loads(args.tokenizer_policy.read_bytes()),
            args.output_tokens,
            json.loads(args.prediction_base.read_bytes())
            if args.prediction_base
            else None,
        )
        print(
            json.dumps(
                {
                    "model": profile["model_key"],
                    "shapes": len(profile["measurements"]),
                    "min_tokens": min(
                        m["input_tokens"] for m in profile["measurements"]
                    ),
                    "max_tokens": max(
                        m["input_tokens"] for m in profile["measurements"]
                    ),
                    "inference_calls": 0,
                }
            )
        )


if __name__ == "__main__":
    main()
