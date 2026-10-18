"""Bounded, model-free trial driver and protocol freeze for Workspace Investigators.

run_scripted_trial supplies exact packed bytes to a trusted scripted consumer; it has no
model transport. Original responses, input bytes, whole-event omissions, failed attempts
and conservative operation charges are retained. Future inference needs a separately
qualified transport/deployment, actual token measurements and its own activation.
"""

from __future__ import annotations

import hashlib
import time
from copy import deepcopy
from dataclasses import asdict, dataclass
from pathlib import Path

from experiments.investigator_workspace_adapter import (
    CONTRACT,
    KINDS,
    REFERENCE,
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

REFERENCE_SCHEMA_POLICY = "investigator-request-local-reference-schema/1"


def closed_reference_array(pairs):
    """Select exact delivered typed pairs, never a kind/ID Cartesian product.

    Packing supplies trusted producer metadata. Text in observations or prior requests
    is deliberately not parsed to create options. The adapter still owns admission.
    """
    groups = {}
    identities = {}
    for pair in pairs:
        if (
            type(pair) is not tuple
            or len(pair) != 2
            or pair[0] not in KINDS
            or type(pair[1]) is not str
            or not pair[1]
            or identities.get(pair[1], pair[0]) != pair[0]
        ):
            raise ValueError("invalid or ambiguous trusted reference metadata")
        kind, identity = pair
        identities[identity] = kind
        groups.setdefault(kind, set()).add(identity)
    schema = {"type": "array", "maxItems": 128}
    if not groups:
        return {**schema, "maxItems": 0, "items": deepcopy(REFERENCE)}
    schema["items"] = {
        "anyOf": [
            {
                "type": "object",
                "properties": {
                    "kind": {"type": "string", "enum": [kind]},
                    "id": {"type": "string", "enum": sorted(groups[kind])},
                },
                "required": ["kind", "id"],
                "additionalProperties": False,
            }
            for kind in sorted(groups)
        ]
    }
    return schema


@dataclass(frozen=True)
class PackedInput:
    content: bytes
    reference_pairs: frozenset[tuple[str, str]]
    omitted_event_ids: tuple[str, ...]

    @property
    def reference_ids(self):
        return frozenset(identity for _, identity in self.reference_pairs)


def trial_budget_observation(limits, charges, seconds_remaining):
    """Expose driver-owned allowance before the next invocation, not evidence.

    Model token/call facts are joined by StatelessInvestigatorModel.pack. No counter
    comes from the model's notes or omitted history. Completion costs are disclosed;
    only the existing termination unit is reserved by enforcement.
    """
    return {
        "format": "investigator-budget-observation/1",
        "trial_limits": asdict(limits),
        "trial_remaining": {
            "invocations_including_this_request": limits.consumer_turns
            - charges.get("consumer_invocation_attempts", 0),
            "operation_units": limits.operations
            - charges.get("admission_operations", 0),
            "observation_bytes": limits.observation_bytes
            - charges.get("observation_bytes", 0),
            "corrections": limits.corrections - charges.get("corrections", 0),
            "terminal_corrections": limits.terminal_corrections
            - charges.get("terminal_corrections", 0),
            "seconds_at_snapshot": round(max(0, seconds_remaining), 3),
        },
        "operation_charges": {
            "tools": TOOL_CHARGES,
            "report_base": 4,
            "per_unique_report_reference": 1,
            "termination_reserved": 1,
        },
        "completion": (
            "Remaining invocations include this response. Finish and report need separate "
            "invocations. Preserve finish=3, report=4+unique references and termination=1 "
            "operation units. Only termination is enforced as reserved; other remaining "
            "capacity is not all discovery capacity. No automatic finish or adequacy proof."
        ),
        "model": None,
        "limit": "Runner control metadata, not source evidence or citation authority. Time is sampled; actual admission still applies.",
    }


def protocol_definition(
    assignment: InvestigatorAssignment, limits: TrialLimits
) -> dict:
    """Exact prompts/schemas/packing/charging; context tokens are not inferred from bytes."""
    return {
        "contract": CONTRACT,
        "reference_schema_policy": REFERENCE_SCHEMA_POLICY,
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
        "budget_observation": trial_budget_observation(limits, {}, limits.seconds),
        "tool_charges": TOOL_CHARGES,
        "report_charge": "4 + unique typed evidence references; malformed wire costs 1",
        "charging": "Conservative admission units; every request charged, early refusals not refunded; termination reserves 1.",
        "packing": "Exact newest whole events that fit; chronological rendering; explicit omitted IDs/bytes/hashes; no text truncation.",
        "measurement_limit": "Byte envelope only. Actual tokenizer/chat template/context/output/reasoning reserve qualification is still required.",
    }


def pack_input(
    protocol: dict, history: list[AdapterEvent], phase: str, capacity: int
) -> PackedInput:
    """Keep newest whole request/result pairs; only delivered refs grant visibility.

    Original UTF8 request intent is separate from returned observation content. Omitted
    pairs retain each component's bytes/hash; unavailable legacy intent stays explicit.
    Showing a proposed reference in prior intent does not make it eligible evidence.
    """
    selected = []

    def render(events):
        pairs = frozenset(pair for event in events for pair in event.reference_pairs)
        citations = closed_reference_array(pairs)
        report_schema = deepcopy(protocol["report_schema"])
        report_schema["properties"]["claims"]["items"]["properties"]["evidence"] = (
            citations
        )
        report_schema["properties"]["recommendation_evidence"] = citations
        tools = deepcopy(protocol["tools"]) if phase == "investigate" else {}
        if "record_note" in tools:
            tools["record_note"]["properties"]["evidence"] = citations
        ids = {e.event_id for e in events}
        omitted = [
            {
                "event_id": e.event_id,
                "bytes": len(e.content),
                "sha256": hashlib.sha256(e.content).hexdigest(),
                "request_bytes": len(e.request_text.encode())
                if e.request_text is not None
                else None,
                "request_sha256": hashlib.sha256(e.request_text.encode()).hexdigest()
                if e.request_text is not None
                else None,
            }
            for e in history
            if e.event_id not in ids
        ]
        body = {
            "contract": CONTRACT,
            "reference_schema_policy": REFERENCE_SCHEMA_POLICY,
            "system": protocol["system"],
            "task": protocol["task"],
            "phase": phase,
            "tools": tools,
            "report_schema": report_schema,
            "budget_observation": protocol["budget_observation"],
            "events": [
                {
                    "event_id": e.event_id,
                    "typed_citation_available": bool(e.reference_pairs),
                    "request_text": e.request_text,
                    "content": e.content.decode(),
                }
                for e in events
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
        content, frozenset(r for e in selected for r in e.reference_pairs), omitted
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
    assignment: InvestigatorAssignment,
    consumer,
    *,
    limits=None,
    clock=time.monotonic,
    reference_visibility="cumulative_script",
    input_packer=pack_input,
) -> ScriptedTrialResult:
    """consumer receives PackedInput and returns exact tool/report JSON bytes.

    This callback is a trusted local script, not a model plugin or untrusted executable.
    Errors yield visible bounded corrections; originals remain distinct from accepted
    attribution. A report is not accepted solely because the callback returned JSON.
    """
    if reference_visibility not in {"cumulative_script", "current_request"}:
        raise ValueError("unknown reference visibility policy")
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
        "report_refusals": [],
        "model_calls": 0,
        "model_tokens": None,
        "native_producer_calls": 0,
        "assignment_composition_seconds": assignment.composition_seconds,
        "assignment_composition_publications": 2,
        "consumer_response_bytes": 0,
        "reference_visibility": reference_visibility,
    }
    started = clock()
    publication = termination = problem = None
    outcome = "limit_exhausted"
    interruption = interruption_traceback = None
    try:
        for _ in range(limits.consumer_turns):
            elapsed = clock() - started
            if (
                elapsed >= limits.seconds
                or charges["admission_operations"] + 1 >= limits.operations
            ):
                break
            report_phase = assignment.ready
            request_protocol = {
                **protocol,
                "budget_observation": trial_budget_observation(
                    limits, charges, limits.seconds - elapsed
                ),
            }
            packed = input_packer(
                request_protocol,
                history,
                "report" if report_phase else "investigate",
                limits.packed_input_bytes,
            )
            inputs.append(packed)
            # Scripts may remember prior inputs. Stateless inference cannot: only
            # references in this exact request may authorize notes/report citations.
            if reference_visibility == "current_request":
                visible = set(packed.reference_ids)
            else:
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
                    # Retain the last refusal even when no following model request
                    # exists to carry its correction event. Originals stay separate.
                    charges["report_refusals"].append(
                        {"consumer_attempt": len(responses), "detail": str(error)}
                    )
                    if charges["terminal_corrections"] >= limits.terminal_corrections:
                        raise
                    charges["terminal_corrections"] += 1
                    try:
                        request_text = response.decode("utf-8")
                    except UnicodeDecodeError:
                        request_text = None
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
                        request_text,
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
    except BaseException as error:  # retain interruption, then terminate and re-raise it
        outcome, problem = "failed", f"{type(error).__name__}: {error}"
        if not isinstance(error, Exception):
            interruption, interruption_traceback = error, error.__traceback__
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
    except BaseException as error:  # secondary storage failure never erases prediction cause
        charges["termination_problem"] = f"{type(error).__name__}: {error}"
        outcome, problem = "failed", problem or f"termination publication failed: {error}"
        if not isinstance(error, Exception) and interruption is None:
            interruption, interruption_traceback = error, error.__traceback__
    charges["elapsed_seconds"] = clock() - started
    charges["access_receipts"] = [asdict(r) for r in assignment.access.receipts]
    result = ScriptedTrialResult(
        outcome,
        tuple(responses),
        tuple(inputs),
        publication,
        termination,
        charges,
        problem,
    )
    # Orchestration can retain the procedural failure even when control-flow
    # interruption must escape. It is never a canonical successful observation.
    assignment.last_trial_result = result
    if interruption is not None:
        raise interruption.with_traceback(interruption_traceback)
    return result


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
