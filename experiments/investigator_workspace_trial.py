"""Bounded, model-free trial driver and protocol freeze for Workspace Investigators.

run_scripted_trial supplies exact packed bytes to a trusted scripted consumer; it has no
model transport. Original responses, input bytes, whole-event omissions, failed attempts
and conservative operation charges are retained. Future inference needs a separately
qualified transport/deployment, actual token measurements and its own activation.
"""

from __future__ import annotations

import hashlib
import time
from dataclasses import asdict, dataclass
from pathlib import Path

from experiments.investigator_workspace_adapter import (
    CONTRACT,
    REPORT_SCHEMA,
    SYSTEM_PROMPT,
    AdapterEvent,
    InvestigatorAssignment,
    decode_object,
    validate_shape,
)
from upgradepilot.workspace.checkpoint_revision import CheckpointStorageError
from upgradepilot.workspace.native_representation import json_bytes
from upgradepilot.workspace.source_access import MAX_SOURCE_VIEW_BYTES


@dataclass(frozen=True)
class TrialLimits:
    consumer_turns: int = 16
    operations: int = 48
    observation_bytes: int = 8 * 1024 * 1024
    packed_input_bytes: int = 128 * 1024
    seconds: int = 14400
    corrections: int = 2
    terminal_corrections: int = 1

    def __post_init__(self):
        for name, value in asdict(self).items():
            if type(value) is not int or value < (0 if "corrections" in name else 1):
                raise ValueError("invalid trial limit: " + name)
        if self.consumer_turns < 2 or self.operations < 2:
            raise ValueError("trial cannot reserve finish/report and termination")


# Admission charges bound all normal dispatch/read/publication attempts, including early
# refusals; they are not claims those operations executed. Actual access receipts/history
# are retained separately. One unit is reserved for final procedural termination.
TOOL_CHARGES = {
    "list_sources": 4,
    "list_paths": 4,
    "read_source": 4,
    "search_sources": 4,
    "resolve_source": 4,
    "read_native": 4,
    "read_native_page": 4,
    "record_note": 1,
    "read_trial_event": 3,
    "finish_investigation": 3,
}


@dataclass(frozen=True)
class PackedInput:
    content: bytes
    reference_ids: frozenset[str]
    omitted_event_ids: tuple[str, ...]


def protocol_definition(
    assignment: InvestigatorAssignment, limits: TrialLimits
) -> dict:
    """Exact prompts/schemas/packing/charging; context tokens are not inferred from bytes."""
    return {
        "contract": CONTRACT,
        "system": SYSTEM_PROMPT,
        "task": {
            "target": asdict(assignment.host.current.boundary.target),
            "goal": "Investigate update-relevant evidence, uncertainty and justified next work.",
            "source_universe": assignment.access.catalog.identity,
            "limit": "Only retained capture; no installed compatibility or action permission implied.",
        },
        "tools": assignment.tools(),
        "report_schema": REPORT_SCHEMA,
        "offering": {
            "source_ids": assignment.access.source_ids,
            "native_families": assignment.access.native_families,
            "max_native_bytes": assignment.access.max_native_bytes,
        },
        "limits": asdict(limits),
        "tool_charges": TOOL_CHARGES,
        "report_charge": "4 + unique typed evidence references; malformed wire costs 1",
        "charging": "Conservative admission units; every request charged, early refusals not refunded; termination reserves 1.",
        "packing": "Exact newest whole events that fit; chronological rendering; explicit omitted IDs/bytes/hashes; no text truncation.",
        "measurement_limit": "Byte envelope only. Actual tokenizer/chat template/context/output/reasoning reserve qualification is still required.",
    }


def pack_input(
    protocol: dict, history: list[AdapterEvent], phase: str, capacity: int
) -> PackedInput:
    selected = []

    def render(events):
        ids = {e.event_id for e in events}
        omitted = [
            {
                "event_id": e.event_id,
                "bytes": len(e.content),
                "sha256": hashlib.sha256(e.content).hexdigest(),
            }
            for e in history
            if e.event_id not in ids
        ]
        body = {
            "contract": CONTRACT,
            "system": protocol["system"],
            "task": protocol["task"],
            "phase": phase,
            "tools": protocol["tools"] if phase == "investigate" else {},
            "report_schema": protocol["report_schema"],
            "events": [
                {"event_id": e.event_id, "content": e.content.decode()} for e in events
            ],
            "omitted_events": omitted,
        }
        return json_bytes(body), tuple(e["event_id"] for e in omitted)

    for event in reversed(history):
        candidate = [event] + selected
        if len(render(candidate)[0]) <= capacity:
            selected = candidate
    content, omitted = render(selected)
    if len(content) > capacity:
        raise ValueError(
            "fixed prompt/tool/schema/omission metadata exceeds input byte envelope"
        )
    return PackedInput(
        content, frozenset(r for e in selected for r in e.reference_ids), omitted
    )


def _admission_charge(assignment, content, report_phase):
    try:
        item = decode_object(content)
        if report_phase:
            validate_shape(item, REPORT_SCHEMA)
            refs = item["recommendation_evidence"] + [
                r for c in item["claims"] for r in c["evidence"]
            ]
            return 4 + len({(r["kind"], r["id"]) for r in refs})
        if set(item) != {"tool", "arguments"} or item["tool"] not in assignment.tools():
            return 1
        validate_shape(item["arguments"], assignment.tools()[item["tool"]])
        return TOOL_CHARGES[item["tool"]]
    except (ValueError, TypeError, KeyError):
        return 1


def _observation_reserve(assignment, content):
    """Bound encoded observations before backend work; unused reservation is released.

    JSON escaping can expand retained bytes by up to six. Fixed overhead covers typed
    references and envelopes. This is conservative capacity admission, not measured cost.
    """
    try:
        tool = decode_object(content).get("tool")
        if tool in ("read_native", "read_native_page"):
            return 6 * assignment.access.max_native_bytes + 8192
        if tool in (
            "list_sources",
            "list_paths",
            "read_source",
            "search_sources",
            "resolve_source",
        ):
            return 6 * MAX_SOURCE_VIEW_BYTES + 8192
        return 128 * 1024 if tool == "read_trial_event" else 8192
    except (ValueError, TypeError):
        return 8192


@dataclass(frozen=True)
class ScriptedTrialResult:
    outcome: str
    original_responses: tuple[bytes | None, ...]
    packed_inputs: tuple[PackedInput, ...]
    report_publication: dict | None
    termination_id: str | None
    charges: dict
    problem: str | None


def run_scripted_trial(
    assignment: InvestigatorAssignment, consumer, *, limits=None, clock=time.monotonic
) -> ScriptedTrialResult:
    """consumer receives PackedInput and returns exact tool/report JSON bytes.

    This callback is a trusted local script, not a model plugin or untrusted executable.
    Errors yield visible bounded corrections; originals remain distinct from accepted
    attribution. A report is not accepted solely because the callback returned JSON.
    """
    limits = TrialLimits() if limits is None else limits
    if assignment.events or assignment.notes or assignment.ready:
        raise ValueError("trial requires a fresh assignment")
    protocol = protocol_definition(assignment, limits)
    history, inputs, responses = [], [], []
    visible = set()
    charges = {
        "consumer_invocation_attempts": 0,
        "admission_operations": 0,
        "tool_requests": 0,
        "observation_bytes": 0,
        "packed_input_bytes": 0,
        "corrections": 0,
        "terminal_corrections": 0,
        "model_calls": 0,
        "model_tokens": None,
        "native_producer_calls": 0,
        "assignment_composition_seconds": assignment.composition_seconds,
        "assignment_composition_publications": 2,
        "consumer_response_bytes": 0,
    }
    started = clock()
    publication = termination = problem = None
    outcome = "limit_exhausted"
    try:
        for _ in range(limits.consumer_turns):
            if (
                clock() - started >= limits.seconds
                or charges["admission_operations"] + 1 >= limits.operations
            ):
                break
            report_phase = assignment.ready
            packed = pack_input(
                protocol,
                history,
                "report" if report_phase else "investigate",
                limits.packed_input_bytes,
            )
            inputs.append(packed)
            visible.update(packed.reference_ids)
            charges["packed_input_bytes"] += len(packed.content)
            charges["consumer_invocation_attempts"] += 1
            responses.append(
                None
            )  # retain an attempted call even if the callback fails
            response = consumer(packed)
            if type(response) is not bytes:
                raise ValueError("scripted consumer must return exact bytes")
            responses[-1] = response
            charges["consumer_response_bytes"] += len(response)
            cost = _admission_charge(assignment, response, report_phase)
            if charges["admission_operations"] + cost + 1 > limits.operations:
                charges["admission_operations"] += 1
                problem = "operation admission refused before dispatch"
                break
            if (
                charges["observation_bytes"]
                + (8192 if report_phase else _observation_reserve(assignment, response))
                > limits.observation_bytes
            ):
                charges["admission_operations"] += 1
                problem = "observation capacity admission refused before dispatch"
                break
            charges["admission_operations"] += cost
            if clock() - started >= limits.seconds:
                problem = "deadline reached after consumer return; no dispatch"
                break
            if report_phase:
                try:
                    publication = assignment.publish_report(
                        response, visible=frozenset(visible)
                    )
                    outcome = "completed"
                    break
                except CheckpointStorageError:
                    raise
                except ValueError as error:
                    if charges["terminal_corrections"] >= limits.terminal_corrections:
                        raise
                    charges["terminal_corrections"] += 1
                    event = AdapterEvent(
                        f"report-error-{len(responses)}",
                        json_bytes(
                            {
                                "outcome": "refused",
                                "detail": str(error),
                                "instruction": "Return a complete corrected report; do not edit the original.",
                            }
                        ),
                        (),
                        "refused",
                        0,
                        (),
                    )
            else:
                charges["tool_requests"] += 1
                event = assignment.invoke(response, visible=frozenset(visible))
            history.append(event)
            charges["observation_bytes"] += len(event.content)
            if charges["observation_bytes"] > limits.observation_bytes:
                problem = "observation byte budget exceeded; result retained, not delivered in another input"
                break
            if event.outcome == "failed":
                outcome, problem = (
                    "failed",
                    "adapter/publication failure; no automatic retry",
                )
                break
            if event.outcome == "refused":
                charges["corrections"] += 1
                if charges["corrections"] > limits.corrections:
                    outcome = "failed"
                    break
        else:
            problem = "consumer turn budget exhausted"
    except Exception as error:  # noqa: BLE001 - callback failures are retained trial outcomes
        outcome, problem = "failed", f"{type(error).__name__}: {error}"
    if outcome != "failed" and clock() - started >= limits.seconds:
        outcome, problem = (
            "limit_exhausted",
            "deadline reached; any completed work remains retained",
        )
    try:
        charges["admission_operations"] += 1
        termination = assignment.host.terminate(
            assignment.host.lineage_id,
            outcome,
            problem or "Scripted procedural result; adequacy remains unsupported.",
        )
    except Exception as error:  # noqa: BLE001 - retain failed/unconfirmed terminal publication
        outcome, problem = "failed", f"termination publication failed: {error}"
    charges["elapsed_seconds"] = clock() - started
    charges["access_receipts"] = [asdict(r) for r in assignment.access.receipts]
    return ScriptedTrialResult(
        outcome,
        tuple(responses),
        tuple(inputs),
        publication,
        termination,
        charges,
        problem,
    )


def mechanical_manifest(
    assignment: InvestigatorAssignment, *, limits=None, input_inventory=None
):
    """A protocol artifact, explicitly withheld from inference; no runnable placeholders."""
    protocol = protocol_definition(assignment, limits or TrialLimits())
    code = {
        str(path): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in (
            Path(__file__),
            Path(__file__).with_name("investigator_workspace_adapter.py"),
        )
    }
    return {
        "format": "investigator-mechanical-manifest/1",
        "inference_admitted": False,
        "withheld_reason": "Actual deployment/tokenizer/template/fit and model-interface qualification pending; no model transport in this driver.",
        "required_deployment_fields": [
            "gguf_files_sizes_sha256",
            "repository_revision",
            "runtime_backend_versions",
            "context_tokens",
            "actual_gpu_weight_offload",
            "kv_cache_placement",
            "chat_template_content_sha256",
            "reasoning_configuration",
            "generation_reserve",
            "qualified_input_token_measurements",
        ],
        "deployment": None,
        "protocol": protocol,
        "protocol_sha256": hashlib.sha256(json_bytes(protocol)).hexdigest(),
        "code_sha256": code,
        "input_inventory": input_inventory,
        "lineage_id": assignment.host.lineage_id,
        "limit": "Model-free mechanical evidence; no semantic, adequacy or usefulness result.",
    }
