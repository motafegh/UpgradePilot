"""Compare scheduled versus model-directed investigation over the same sources.

run_investigation_trial owns fresh trial state, limits and control. A provider
measures each fully rendered request before inference and returns usage plus a
single JSON action. SourceWorkspace owns exact source access; no semantic grader
or target execution is embedded here. Raw traces are saved only by the local CLI.
"""

from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass
from typing import Protocol

from .broader_agency_workspace import TOOL_GUIDE, SourceWorkspace, digest, strict_json


@dataclass(frozen=True)
class TrialLimits:
    calls: int = 16
    input_tokens: int = 49_152
    output_tokens: int = 16_384
    tool_operations: int = 48
    source_bytes: int = 8 * 1024 * 1024
    seconds: int = 1200
    action_output: int = 1024
    final_output: int = 1536


@dataclass(frozen=True)
class ModelRequest:
    system: str
    user: str
    output_reserve: int


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
    reasoning_tokens: int
    deployment_identity: str
    truncated: bool = False


class TrialProvider(Protocol):
    def measure(self, request: ModelRequest) -> MeasuredRequest: ...
    def predict(
        self, request: ModelRequest, measurement: MeasuredRequest, timeout: float
    ) -> ModelReply: ...


FIXED_STAGES = (
    "interpret upstream changes",
    "localize consumer use",
    "assess conditions, environment and CI coverage",
    "synthesize provisional advice",
    "challenge advice and finish the report",
)


def request_identity(request: ModelRequest) -> str:
    return digest(asdict(request))


def decode_action(text: str) -> dict:
    value = strict_json(text)
    if not isinstance(value, dict) or set(value) != {"tool", "arguments", "notes"}:
        raise ValueError("expected tool/arguments/notes object")
    if not isinstance(value["tool"], str) or not isinstance(value["arguments"], dict):
        raise ValueError("invalid tool/action arguments")
    if not isinstance(value["notes"], str) or len(value["notes"]) > 2400:
        raise ValueError("invalid or oversized cumulative notes")
    if value["tool"] == "finish_report":
        report = value["arguments"]
        keys = {
            "summary",
            "claims",
            "recommendation",
            "conditions",
            "unexamined",
            "stopping_reason",
        }
        if set(report) != keys or not all(
            isinstance(report[k], str)
            for k in ("summary", "recommendation", "stopping_reason")
        ):
            raise ValueError("invalid report fields")
        if not all(
            isinstance(report[k], list) and all(isinstance(s, str) for s in report[k])
            for k in ("conditions", "unexamined")
        ):
            raise ValueError("invalid report conditions/scope")
        if not isinstance(report["claims"], list):
            raise ValueError("invalid report claims")
        for claim in report["claims"]:
            if not isinstance(claim, dict) or set(claim) != {
                "statement",
                "citations",
                "status",
            }:
                raise ValueError("invalid claim fields")
            if (
                not isinstance(claim["statement"], str)
                or not isinstance(claim["status"], str)
                or not isinstance(claim["citations"], list)
                or not all(isinstance(c, str) for c in claim["citations"])
            ):
                raise ValueError("invalid claim values")
    return value


def run_investigation_trial(
    case: dict,
    workspace: SourceWorkspace,
    method: str,
    provider: TrialProvider,
    *,
    limits: TrialLimits = TrialLimits(),
    clock=time.monotonic,
) -> dict:
    """Return engineering outcome/trace; even completed reports are ungraded advice.

    Notebook replacement is model-owned memory, shared between arms. The latest
    tool page and cumulative notes enter the next request; full prior text remains
    in the private trace, with re-reading through exact source IDs always possible.
    No automatic transcript trimming or oracle-derived summary occurs.
    """
    if method not in {"fixed", "agent"}:
        raise ValueError("method must be fixed or agent")
    if limits.calls < 2 or limits.output_tokens < limits.final_output:
        raise ValueError("limits cannot reserve final output")
    started = clock()
    counters = {
        "calls": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "reasoning_tokens": 0,
        "tool_operations": 0,
        "source_bytes": 0,
    }
    notes = ""
    last_result = None
    trace = []
    report = None
    outcome = "call_budget_exhausted"
    deployment = None
    for index in range(limits.calls):
        remaining = limits.seconds - (clock() - started)
        if remaining <= 0:
            outcome = "time_budget_exhausted"
            break
        remaining_output = limits.output_tokens - counters["output_tokens"]
        final = index == limits.calls - 1 or remaining_output <= limits.final_output
        stage = (
            FIXED_STAGES[min(index // 4, 2) if index < 12 else 3 if index < 14 else 4]
            if method == "fixed"
            else "choose the most useful investigation, or finish when justified"
        )
        if final:
            stage = "finish_report now, retaining unexamined scope and unresolved conditions"
        reserve = min(
            limits.final_output if final else limits.action_output,
            remaining_output if final else remaining_output - limits.final_output,
        )
        if reserve <= 0:
            outcome = "output_budget_exhausted"
            break
        request = ModelRequest(
            "You investigate a dependency update for a maintainer. " + TOOL_GUIDE,
            json.dumps(
                {
                    "task": case,
                    "sources": workspace.sources,
                    "instruction": stage,
                    "cumulative_notes": notes,
                    "last_tool_result": last_result,
                    "remaining_calls": limits.calls - index,
                    "finish_allowed": final or method == "agent" or index >= 14,
                },
                ensure_ascii=False,
            ),
            reserve,
        )
        event = {"index": index + 1, "stage": stage, "request": asdict(request)}
        trace.append(event)
        try:
            measured = provider.measure(request)
            event["measurement"] = asdict(measured)
            if (
                type(measured.input_tokens) is not int
                or measured.input_tokens < 0
                or type(measured.context_tokens) is not int
                or measured.context_tokens <= 0
            ):
                raise ValueError("invalid capacity counts")
            if measured.request_sha256 != request_identity(request):
                raise ValueError("capacity evidence belongs to another request")
            if measured.input_tokens + reserve > measured.context_tokens:
                outcome = "request_capacity_exceeded"
                break
            if counters["input_tokens"] + measured.input_tokens > limits.input_tokens:
                outcome = "input_budget_exhausted"
                break
            if deployment is not None and measured.deployment_identity != deployment:
                raise ValueError("deployment changed within trial")
            deployment = measured.deployment_identity
            remaining = limits.seconds - (clock() - started)
            if remaining <= 0:
                outcome = "time_budget_exhausted"
                break
            counters["calls"] += 1
            reply = provider.predict(request, measured, remaining)
            event["reply"] = asdict(reply)
            for key in ("input_tokens", "output_tokens", "reasoning_tokens"):
                value = getattr(reply, key)
                if type(value) is not int or value < 0:
                    raise ValueError("invalid provider usage")
                counters[key] += value
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
            action = decode_action(reply.text)
            event["action"] = action
            notes = action["notes"]
            if action["tool"] == "finish_report":
                if method == "fixed" and index < 14 and not final:
                    last_result = {
                        "tool_problem": "fixed workflow finishes in its challenge/report stage"
                    }
                    event["tool_result"] = last_result
                    continue
                report = action["arguments"]
                missing = workspace.validate_citations(report)
                event["unknown_citations"] = missing
                outcome = "report_citation_problem" if missing else "completed_ungraded"
                break
            if final:
                outcome = "final_report_missing"
                break
            if counters["tool_operations"] >= limits.tool_operations:
                outcome = "tool_budget_exhausted"
                break
            counters["tool_operations"] += 1
            last_result = workspace.invoke(action["tool"], action["arguments"])
            event["tool_result"] = last_result
            returned_bytes = len(json.dumps(last_result, ensure_ascii=False).encode())
            counters["source_bytes"] += returned_bytes
            if counters["source_bytes"] > limits.source_bytes:
                outcome = "source_byte_budget_exhausted"
                break
        except Exception as error:
            event["problem"] = f"{type(error).__name__}: {error}"
            outcome = "provider_or_action_problem"
            break
    return {
        "case_id": case["case_id"],
        "method": method,
        "corpus_sha256": workspace.identity,
        "limits": asdict(limits),
        "outcome": outcome,
        "report": report,
        "counters": counters,
        "elapsed_seconds": round(clock() - started, 3),
        "trace": trace,
        "semantic_review": "not_performed",
    }
