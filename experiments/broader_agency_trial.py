"""Common trial history/resources and two investigation policies, experiment only.

Workspace observations are source truth; model notes/stage artifacts are candidate
interpretations. Report shape and citation existence are mechanical proof only.
The provider owns wire rendering, instance binding, usage and private receipts.
"""

from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass
from typing import Protocol

from .broader_agency_workspace import TOOL_GUIDE, SourceWorkspace, digest, strict_json


def object_schema(properties, required=None):
    return {
        "type": "object",
        "properties": properties,
        "required": list(properties) if required is None else required,
        "additionalProperties": False,
    }


STRING = {"type": "string"}
STRINGS = {"type": "array", "items": STRING}
CLAIM_SCHEMA = object_schema(
    {"statement": STRING, "citations": STRINGS, "status": STRING}
)
CLAIMS = {"type": "array", "items": CLAIM_SCHEMA}
REPORT_SCHEMA = object_schema(
    {
        "summary": STRING,
        "claims": CLAIMS,
        "recommendation": STRING,
        "conditions": STRINGS,
        "unexamined": STRINGS,
        "stopping_reason": STRING,
    }
)
STAGE_SCHEMA = object_schema(
    {"summary": STRING, "claims": CLAIMS, "conditions": STRINGS, "unexamined": STRINGS}
)
TOOL_ARGUMENTS = {
    "list_sources": object_schema({}),
    "list_paths": object_schema(
        {"source_id": STRING, "prefix": STRING, "offset": {"type": "integer"}},
        ["source_id"],
    ),
    "read_source": object_schema(
        {
            "source_id": STRING,
            "path": STRING,
            "start_line": {"type": "integer"},
            "line_count": {"type": "integer"},
        },
        ["source_id", "path"],
    ),
    "search_sources": object_schema(
        {
            "query": STRING,
            "source_id": STRING,
            "path_prefix": STRING,
            "offset": {"type": "integer"},
        },
        ["query"],
    ),
    "record_note": object_schema({"text": STRING, "citations": STRINGS}, ["text"]),
    "read_trial_event": object_schema(
        {"event_id": STRING, "offset": {"type": "integer"}}, ["event_id"]
    ),
    "finish_investigation": object_schema({}),
}
TOOL_ARGUMENTS["read_observation"] = TOOL_ARGUMENTS["read_source"]
TOOLS = tuple(
    {
        "type": "function",
        "function": {
            "name": name,
            "description": name.replace("_", " ") + "; see common tool guide",
            "parameters": schema,
        },
    }
    for name, schema in TOOL_ARGUMENTS.items()
)
FIXED_STAGES = (
    ("interpret upstream changes", 3),
    ("localize consumer use", 3),
    ("assess conditions, environment and CI coverage", 4),
    ("synthesize provisional advice", 1),
    ("challenge advice against counterevidence and assumptions", 1),
)


@dataclass(frozen=True)
class TrialLimits:
    calls: int = 16
    input_tokens: int = 245_760
    output_tokens: int = 32_768
    tool_operations: int = 48
    source_bytes: int = 8 * 1024 * 1024
    seconds: int = 1200
    action_output: int = 1024
    final_output: int = 4096
    corrections: int = 2


@dataclass(frozen=True)
class ModelRequest:
    system: str
    user: str
    output_reserve: int
    phase: str = "investigate"
    history: tuple = ()
    tools: tuple = ()
    response_schema: dict | None = None


@dataclass(frozen=True)
class MeasuredRequest:
    input_tokens: int
    context_tokens: int
    request_sha256: str
    deployment_identity: str


@dataclass(frozen=True)
class ModelReply:
    text: str
    input_tokens: int
    output_tokens: int
    reasoning_tokens: int | None
    deployment_identity: str
    truncated: bool = False
    tool_calls: tuple | None = None


class TrialProvider(Protocol):
    def measure(self, request: ModelRequest) -> MeasuredRequest: ...
    def predict(
        self, request: ModelRequest, measurement: MeasuredRequest, timeout: float
    ) -> ModelReply: ...


def request_identity(request: ModelRequest) -> str:
    return digest(asdict(request))


def validate_shape(value, schema, path="$"):
    kind = schema["type"]
    if kind == "object":
        if not isinstance(value, dict):
            raise ValueError(f"{path}: expected object")
        missing = set(schema["required"]) - set(value)
        extra = set(value) - set(schema["properties"])
        if missing or extra:
            raise ValueError(
                f"{path}: missing {sorted(missing)}, extra {sorted(extra)}"
            )
        for key, item in value.items():
            validate_shape(item, schema["properties"][key], f"{path}.{key}")
    elif kind == "array":
        if not isinstance(value, list):
            raise ValueError(f"{path}: expected array")
        for index, item in enumerate(value):
            validate_shape(item, schema["items"], f"{path}[{index}]")
    elif kind == "string" and not isinstance(value, str):
        raise ValueError(f"{path}: expected string")
    elif kind == "integer" and type(value) is not int:
        raise ValueError(f"{path}: expected integer")


def decode_actions(reply: ModelReply, event_id: str):
    notes = ""
    if reply.tool_calls is not None:
        raw = list(reply.tool_calls)
        if not raw:
            return [], notes  # tool-free assistant readiness, separately finalized
    else:
        value = strict_json(reply.text)
        if not isinstance(value, dict):
            raise ValueError("$: expected tool/arguments object or actions array")
        if set(value) - {"tool", "arguments", "actions", "notes"}:
            raise ValueError("$: unknown action fields; notes is optional")
        notes = value.get("notes", "")
        if not isinstance(notes, str) or len(notes) > 2400:
            raise ValueError("$.notes: expected text <=2400 characters")
        if "actions" in value:
            if (
                set(value) - {"actions", "notes"}
                or not isinstance(value["actions"], list)
                or not value["actions"]
            ):
                raise ValueError("$.actions: expected nonempty action array")
            raw = value["actions"]
        else:
            raw = [{k: v for k, v in value.items() if k != "notes"}]
    actions = []
    ids = set()
    for index, item in enumerate(raw):
        if (
            not isinstance(item, dict)
            or set(item) - {"tool", "arguments", "id"}
            or not {"tool", "arguments"} <= set(item)
        ):
            raise ValueError(f"$.actions[{index}]: expected tool/arguments")
        name = item["tool"]
        if name not in TOOL_ARGUMENTS:
            raise ValueError(
                f"$.tool: unsupported {name!r}; allowed {list(TOOL_ARGUMENTS)}"
            )
        validate_shape(item["arguments"], TOOL_ARGUMENTS[name], "$.arguments")
        call_id = item.get("id", f"{event_id}-tool-{index + 1}")
        if not isinstance(call_id, str) or not call_id or call_id in ids:
            raise ValueError("$.id: missing or duplicate tool-call ID")
        ids.add(call_id)
        actions.append({"id": call_id, "tool": name, "arguments": item["arguments"]})
    return actions, notes


def _directory(events, included):
    return [
        {
            "event_id": e["event_id"],
            "phase": e["phase"],
            "actions": [
                {
                    "tool": c["tool"],
                    "scope": {
                        k: v
                        for k, v in c["arguments"].items()
                        if k
                        in {
                            "query",
                            "source_id",
                            "path",
                            "path_prefix",
                            "offset",
                            "start_line",
                            "line_count",
                            "event_id",
                        }
                    },
                }
                for c in e.get("actions", [])
            ],
            "error": e.get("error"),
            "omitted": e["event_id"] not in included,
        }
        for e in events
    ]


def _pack(provider, base, events, remaining_input):
    """Measure full packet first; pack only whole event pairs if pressure requires it."""

    def candidate(selected):
        included = {e["event_id"] for e in selected}
        request = ModelRequest(
            user=json.dumps(
                {**base["user"], "event_directory": _directory(events, included)},
                ensure_ascii=False,
            ),
            history=tuple(selected),
            **base["request"],
        )
        measured = provider.measure(request)
        if (
            type(measured.input_tokens) is not int
            or measured.input_tokens < 0
            or type(measured.context_tokens) is not int
            or measured.context_tokens <= 0
            or measured.request_sha256 != request_identity(request)
        ):
            raise ValueError("invalid capacity counts or request identity")
        fits = (
            measured.input_tokens + request.output_reserve <= measured.context_tokens
            and measured.input_tokens <= remaining_input
        )
        return request, measured, fits

    request, measured, fits = candidate(events)
    selected = list(events)
    if not fits and events:
        selected = [events[-1]]
        request, measured, fits = candidate(selected)
        if fits:
            for event in reversed(events[:-1]):
                wanted = [event, *selected]
                trial_request, trial_measured, trial_fits = candidate(wanted)
                if trial_fits:
                    selected, request, measured = wanted, trial_request, trial_measured
    included = [e["event_id"] for e in selected]
    omitted = [e["event_id"] for e in events if e["event_id"] not in included]
    return (
        request,
        measured,
        fits,
        {
            "included_event_ids": included,
            "omitted_event_ids": omitted,
            "packed": bool(omitted),
        },
    )


def run_investigation_trial(
    case,
    workspace: SourceWorkspace,
    method,
    provider: TrialProvider,
    *,
    limits=None,
    clock=time.monotonic,
):
    limits = TrialLimits() if limits is None else limits
    if method not in {"fixed", "agent"}:
        raise ValueError("method must be fixed or agent")
    if limits.calls < 2 or limits.output_tokens < 2 * limits.final_output:
        raise ValueError("limits cannot reserve report plus one correction")
    started = clock()
    counters = dict.fromkeys(
        (
            "calls",
            "input_tokens",
            "output_tokens",
            "reasoning_tokens",
            "tool_operations",
            "source_bytes",
            "corrections",
        ),
        0,
    )
    trace, events, artifacts = [], [], []
    latest_note = None
    report = None
    outcome = "call_budget_exhausted"
    deployment = None
    stage_index = stage_used = 0
    flex = max(0, limits.calls - 14)  # 12 scheduled work calls + two report calls
    early_artifact = False
    report_mode = False
    correction_phase = None
    report_corrections = 0
    unknown_usage = False
    packet = workspace.update_packet()
    while counters["calls"] < limits.calls:
        remaining = limits.seconds - (clock() - started)
        if remaining <= 0:
            outcome = "time_budget_exhausted"
            break
        output_left = limits.output_tokens - counters["output_tokens"]
        if (
            limits.calls - counters["calls"] <= 2
            or output_left < 2 * limits.final_output + limits.action_output
        ):
            report_mode = True
        if method == "fixed" and stage_index >= len(FIXED_STAGES):
            report_mode = True
        phase = (
            "report"
            if report_mode
            else "stage"
            if method == "fixed"
            and (early_artifact or stage_used >= FIXED_STAGES[stage_index][1] - 1)
            else "investigate"
        )
        if correction_phase is not None and not report_mode:
            phase = correction_phase
        elif report_mode and correction_phase != "report":
            correction_phase = None
        stage = (
            "terminal report"
            if phase == "report"
            else FIXED_STAGES[stage_index][0]
            if method == "fixed"
            else "choose useful investigation; signal finish_investigation when justified"
        )
        reserve = limits.final_output if phase == "report" else limits.action_output
        if output_left < reserve:
            outcome = "output_budget_exhausted"
            break
        schema = (
            REPORT_SCHEMA
            if phase == "report"
            else STAGE_SCHEMA
            if phase == "stage"
            else None
        )
        instruction = stage
        if schema:
            instruction += (
                "; return the schema object DIRECTLY, no tool wrapper or Markdown"
            )
        base = {
            "request": {
                "system": "Investigate a dependency update for a maintainer. "
                + TOOL_GUIDE,
                "output_reserve": reserve,
                "phase": phase,
                "tools": TOOLS if phase == "investigate" else (),
                "response_schema": schema,
            },
            "user": {
                "task": case,
                "sources": workspace.sources,
                "update_packet": packet,
                "instruction": instruction,
                "schema": schema,
                "latest_nonempty_model_note": latest_note,
                "fixed_stage_artifacts": artifacts if method == "fixed" else [],
                "remaining_calls": limits.calls - counters["calls"],
                "remaining_output_tokens": output_left,
                "correction": events[-1].get("error")
                if correction_phase and events
                else None,
            },
        }
        event_id = f"event-{len(trace) + 1:03d}"
        event = {"event_id": event_id, "phase": phase, "stage": stage}
        trace.append(event)
        public = {
            "event_id": event_id,
            "phase": phase,
            "assistant": "",
            "actions": [],
            "results": [],
        }
        try:
            request, measured, fits, packing = _pack(
                provider, base, events, limits.input_tokens - counters["input_tokens"]
            )
            event.update(
                request=asdict(request), measurement=asdict(measured), packing=packing
            )
            if not fits:
                outcome = (
                    "input_budget_exhausted"
                    if measured.input_tokens
                    > limits.input_tokens - counters["input_tokens"]
                    else "request_capacity_exceeded"
                )
                break
            if deployment is not None and deployment != measured.deployment_identity:
                raise ValueError("deployment changed within trial")
            deployment = measured.deployment_identity
            remaining = limits.seconds - (clock() - started)
            if remaining <= 0:
                outcome = "time_budget_exhausted"
                break
            counters["calls"] += 1
            if method == "fixed" and phase != "report":
                if correction_phase:
                    flex -= 1
                else:
                    stage_used += 1
            reply = provider.predict(request, measured, remaining)
            event["reply"] = asdict(reply)
            public["assistant"] = reply.text
            for key in ("input_tokens", "output_tokens"):
                value = getattr(reply, key)
                if type(value) is not int or value < 0:
                    raise ValueError("invalid provider usage")
                counters[key] += value
            if type(reply.reasoning_tokens) is not int or reply.reasoning_tokens < 0:
                unknown_usage = True
                outcome = "provider_reasoning_usage_unknown"
                break
            counters["reasoning_tokens"] += reply.reasoning_tokens
            if (
                reply.deployment_identity != deployment
                or reply.input_tokens > measured.input_tokens
                or reply.output_tokens > reserve
                or reply.reasoning_tokens > reply.output_tokens
            ):
                outcome = "provider_accounting_or_identity_mismatch"
                break
            if clock() - started > limits.seconds:
                outcome = "time_budget_exhausted"
                break
            if reply.truncated:
                outcome = "output_truncated"
                break
            correction_phase = None
            try:
                if phase in {"stage", "report"}:
                    value = strict_json(reply.text)
                    validate_shape(value, schema)
                    missing = workspace.validate_citations(value)
                    if missing:
                        raise ValueError(
                            "$.claims.citations: nonexistent retained references "
                            + repr(missing)
                        )
                    public["artifact"] = value
                    if phase == "report":
                        report = value
                        outcome = (
                            "completed_after_recovery_ungraded"
                            if counters["corrections"]
                            else "completed_ungraded"
                        )
                        break
                    artifacts.append(
                        {
                            "stage": stage,
                            "event_id": event_id,
                            "artifact": value,
                            "complete": True,
                        }
                    )
                    flex += max(0, FIXED_STAGES[stage_index][1] - stage_used)
                    stage_index += 1
                    stage_used = 0
                    early_artifact = False
                else:
                    actions, note = decode_actions(reply, event_id)
                    public["actions"] = actions
                    if note:
                        latest_note = {
                            "text": note,
                            "citations": [],
                            "event_id": event_id,
                        }
                    if not actions:
                        if method == "agent":
                            report_mode = True
                        else:
                            early_artifact = True
                    for index, action in enumerate(actions):
                        if counters["tool_operations"] >= limits.tool_operations:
                            event["not_dispatched"] = actions[index:]
                            outcome = "tool_budget_exhausted"
                            break
                        counters["tool_operations"] += 1
                        name, args = action["tool"], action["arguments"]
                        if name == "finish_investigation":
                            result = {
                                "ready": True,
                                "scope": "this stage"
                                if method == "fixed"
                                else "this investigation",
                            }
                            if method == "agent":
                                report_mode = True
                            else:
                                early_artifact = True
                        elif name == "record_note":
                            if len(args["text"]) > 2400:
                                result = {
                                    "tool_problem": "text exceeds 2400 characters"
                                }
                            elif workspace.validate_citations(
                                {"claims": [{"citations": args.get("citations", [])}]}
                            ):
                                raise ValueError(
                                    "$.record_note.citations: nonexistent retained reference"
                                )
                            else:
                                if args["text"]:
                                    latest_note = {**args, "event_id": event_id}
                                result = {
                                    "stored": bool(args["text"]),
                                    "empty_did_not_erase": not bool(args["text"]),
                                }
                        elif name == "read_trial_event":
                            earlier = next(
                                (
                                    e
                                    for e in events
                                    if e["event_id"] == args["event_id"]
                                ),
                                None,
                            )
                            offset = args.get("offset", 0)
                            if earlier is None or type(offset) is not int or offset < 0:
                                result = {
                                    "tool_problem": "unknown prior event or invalid offset",
                                    "event_id": args["event_id"],
                                    "offset": offset,
                                }
                            else:
                                text = json.dumps(earlier, ensure_ascii=False)
                                page = text[offset : offset + 2400]
                                result = {
                                    "event_id": args["event_id"],
                                    "offset": offset,
                                    "total_characters": len(text),
                                    "returned_characters": len(page),
                                    "content": page,
                                    "next_offset": offset + len(page)
                                    if offset + len(page) < len(text)
                                    else None,
                                    "omissions": [],
                                }
                        else:
                            result = workspace.invoke(name, args)
                        result = {
                            **result,
                            "trial_event_id": event_id,
                            "tool_call_id": action["id"],
                        }
                        public["results"].append(
                            {"id": action["id"], "tool": name, "result": result}
                        )
                        counters["source_bytes"] += len(
                            json.dumps(result, ensure_ascii=False).encode()
                        )
                        if counters["source_bytes"] > limits.source_bytes:
                            event["not_dispatched"] = actions[index + 1 :]
                            outcome = "source_byte_budget_exhausted"
                            break
                    if outcome in {
                        "tool_budget_exhausted",
                        "source_byte_budget_exhausted",
                    }:
                        event["public_event"] = public
                        events.append(public)
                        break
            except (ValueError, TypeError, KeyError) as error:
                public["error"] = {
                    "failed_event_id": event_id,
                    "problem": str(error),
                    "allowed_contract": schema
                    if schema
                    else {"tools": TOOL_ARGUMENTS, "notes": "optional text <=2400"},
                    "meaning_review": "not performed",
                }
                # Complete pending native pairs with visible errors; never leave
                # an assistant request unmatched in a later compatible message.
                answered = {r["id"] for r in public["results"]}
                if reply.tool_calls is not None and not public["actions"]:
                    public["actions"] = [
                        a
                        for a in reply.tool_calls
                        if isinstance(a, dict) and {"id", "tool", "arguments"} <= set(a)
                    ]
                for action in public["actions"]:
                    if action["id"] not in answered:
                        public["results"].append(
                            {
                                "id": action["id"],
                                "tool": action["tool"],
                                "result": {
                                    "format_problem": public["error"],
                                    "not_executed": True,
                                },
                            }
                        )
                can_correct = (
                    counters["corrections"] < limits.corrections
                    and counters["calls"] < limits.calls
                    and (phase != "report" or report_corrections < 1)
                )
                if method == "fixed" and phase != "report":
                    can_correct = can_correct and flex > 0
                if can_correct:
                    counters["corrections"] += 1
                    report_corrections += int(phase == "report")
                    correction_phase = phase
                elif phase == "stage":
                    artifacts.append(
                        {
                            "stage": stage,
                            "event_id": event_id,
                            "artifact": None,
                            "complete": False,
                            "problem": str(error),
                        }
                    )
                    stage_index += 1
                    stage_used = 0
                    early_artifact = False
                else:
                    outcome = (
                        "report_contract_problem"
                        if phase == "report"
                        else "action_contract_problem"
                    )
                    event["public_event"] = public
                    events.append(public)
                    break
            event["public_event"] = public
            events.append(public)
        except Exception as error:  # noqa: BLE001 - preserve provider failures without retry
            event["problem"] = f"{type(error).__name__}: {error}"
            outcome = "provider_or_capacity_problem"
            break
    if trace and "reply" in trace[-1] and "public_event" not in trace[-1]:
        trace[-1]["public_event"] = public
    return {
        "case_id": case["case_id"],
        "method": method,
        "corpus_sha256": workspace.identity,
        "limits": asdict(limits),
        "outcome": outcome,
        "report": report,
        "fixed_stage_artifacts": artifacts,
        "counters": counters,
        "usage_complete": not unknown_usage and not any("problem" in e for e in trace),
        "elapsed_seconds": round(clock() - started, 3),
        "trace": trace,
        "semantic_review": "not_performed",
    }
