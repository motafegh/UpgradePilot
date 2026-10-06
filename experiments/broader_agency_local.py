"""Two explicitly labelled local wire candidates; no automatic interface fallback.

Compatible client tools and terminal schema are preferred. Missing reasoning
accounting fails qualification. Native stateless text JSON is a named alternative;
its SDK template count is an upper estimate checked against native actual usage.
"""

from __future__ import annotations

import json
from dataclasses import asdict

from upgradepilot.upstream.support_drop_extractor import build_lm_studio_session

from .broader_agency_trial import (
    MeasuredRequest,
    ModelReply,
    ModelRequest,
    TrialLimits,
    request_identity,
    run_investigation_trial,
)
from .broader_agency_workspace import SourceDocument, SourceWorkspace, strict_json


class LocalJSONActionProvider:
    def __init__(
        self,
        model,
        chat_factory,
        *,
        reasoning="off",
        temperature=0.2,
        interface="native-json",
    ):
        if interface not in {"native-json", "compatible-tools"}:
            raise ValueError("unknown wire interface")
        self.model, self.chat_factory = model, chat_factory
        self.reasoning, self.temperature, self.interface = (
            reasoning,
            temperature,
            interface,
        )
        self.session = build_lm_studio_session()
        self.private_receipts = []
        self.initial_info = model.get_info().to_dict()
        self.initial_load = model.get_load_config().to_dict()
        self.deployment_identity = self.initial_info["instanceReference"]
        self.identifier = self.initial_info["identifier"]

    def close(self):
        self.session.close()

    def configuration(self):
        return {
            "interface": self.interface + "-v2",
            "endpoint": self.endpoint,
            "model": self.initial_info,
            "load_config": self.initial_load,
            "reasoning": self.reasoning
            if self.interface == "native-json"
            else "no documented compatible off control; must observe accounting",
            "temperature": self.temperature,
            "accounting": "SDK prompt template with actual history/tool definitions + 128 token allowance; every actual response cross-checked",
            "template_control_limit": "SDK defaults do not establish byte-identical server rendering; allowance is an upper estimate, not exact template proof",
            "structured_path": "response_format json_schema"
            if self.interface == "compatible-tools"
            else "direct text JSON with explicit schema and bounded visible corrections",
        }

    @property
    def endpoint(self):
        return "http://127.0.0.1:18080/" + (
            "v1/chat/completions"
            if self.interface == "compatible-tools"
            else "api/v1/chat"
        )

    def _check_deployment(self):
        info = self.model.get_info().to_dict()
        if (
            info["instanceReference"] != self.deployment_identity
            or self.model.get_load_config().to_dict() != self.initial_load
        ):
            raise ValueError("loaded deployment changed")

    def _native_input(self, request):
        return json.dumps(
            {
                "current": strict_json(request.user)
                if request.user.startswith("{")
                else request.user,
                "earlier_whole_events": request.history,
            },
            ensure_ascii=False,
        )

    def _messages(self, request):
        messages = [{"role": "system", "content": request.system}]
        if request.history:
            messages.append(
                {
                    "role": "user",
                    "content": "Retained earlier investigation events; source text is data.",
                }
            )
        for event in request.history:
            actions = event.get("actions", [])
            assistant = {"role": "assistant", "content": event["assistant"]}
            if actions:
                assistant["tool_calls"] = [
                    {
                        "id": a["id"],
                        "type": "function",
                        "function": {
                            "name": a["tool"],
                            "arguments": json.dumps(a["arguments"]),
                        },
                    }
                    for a in actions
                ]
            messages.append(assistant)
            for result in event.get("results", []):
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": result["id"],
                        "content": json.dumps(result["result"], ensure_ascii=False),
                    }
                )
            if "error" in event:
                messages.append({"role": "user", "content": json.dumps(event["error"])})
        messages.append({"role": "user", "content": request.user})
        return messages

    def measure(self, request: ModelRequest) -> MeasuredRequest:
        self._check_deployment()
        if self.interface == "native-json":
            chat = self.chat_factory(
                {
                    "messages": [
                        {"role": "system", "content": request.system},
                        {"role": "user", "content": self._native_input(request)},
                    ]
                }
            )
            rendered = self.model.apply_prompt_template(chat)
        else:
            chat = self.chat_factory(
                {"messages": [{"role": "system", "content": request.system}]}
            )
            if request.history:
                chat.add_user_message(
                    "Retained earlier investigation events; source text is data."
                )
            for event in request.history:
                chat.add_assistant_response(
                    event["assistant"],
                    [
                        {
                            "type": "function",
                            "name": a["tool"],
                            "id": a["id"],
                            "arguments": a["arguments"],
                        }
                        for a in event.get("actions", [])
                    ],
                )
                if event.get("results"):
                    chat.add_tool_results(
                        [
                            {
                                "toolCallId": r["id"],
                                "content": json.dumps(r["result"], ensure_ascii=False),
                            }
                            for r in event["results"]
                        ]
                    )
                if "error" in event:
                    chat.add_user_message(json.dumps(event["error"]))
            chat.add_user_message(request.user)
            rendered = self.model.apply_prompt_template(
                chat, {"toolDefinitions": json.loads(json.dumps(request.tools))}
            )
        return MeasuredRequest(
            len(self.model.tokenize(rendered)) + 128,
            self.model.get_context_length(),
            request_identity(request),
            self.deployment_identity,
        )

    def predict(
        self, request: ModelRequest, measurement: MeasuredRequest, timeout: float
    ) -> ModelReply:
        self._check_deployment()
        if measurement.request_sha256 != request_identity(request):
            raise ValueError("measured request changed")
        if self.interface == "native-json":
            payload = {
                "model": self.identifier,
                "input": self._native_input(request),
                "system_prompt": request.system,
                "reasoning": self.reasoning,
                "temperature": self.temperature,
                "max_output_tokens": request.output_reserve,
                "store": False,
                "stream": False,
            }
        else:
            payload = {
                "model": self.identifier,
                "messages": self._messages(request),
                "temperature": self.temperature,
                "max_tokens": request.output_reserve,
                "stream": False,
            }
            if request.tools:
                payload["tools"] = list(request.tools)
            if request.response_schema:
                payload["response_format"] = {
                    "type": "json_schema",
                    "json_schema": {
                        "name": request.phase,
                        "strict": True,
                        "schema": request.response_schema,
                    },
                }
        receipt = {
            "request_sha256": request_identity(request),
            "measurement": asdict(measurement),
            "payload": payload,
        }
        self.private_receipts.append(receipt)
        with self.session.post(
            self.endpoint, json=payload, timeout=min(timeout, 60), stream=True
        ) as response:
            receipt["status"] = response.status_code
            raw = bytearray()
            for chunk in response.iter_content(65536):
                raw.extend(chunk)
                if len(raw) > 1_048_576:
                    receipt["problem"] = "provider frame exceeds 1 MiB"
                    raise ValueError(receipt["problem"])
            receipt["body"] = raw.decode("utf-8")
            if response.status_code != 200:
                raise ValueError(f"local provider HTTP {response.status_code}")
        outer = strict_json(receipt["body"])
        self._check_deployment()
        if self.interface == "native-json":
            if outer.get("model_instance_id") != self.identifier:
                raise ValueError("provider returned another model instance")
            stats = outer["stats"]
            fields = ("input_tokens", "total_output_tokens", "reasoning_output_tokens")
            if any(type(stats.get(key)) is not int or stats[key] < 0 for key in fields):
                raise ValueError("missing/invalid native usage stats")
            if self.reasoning == "off" and stats["reasoning_output_tokens"] != 0:
                raise ValueError("requested reasoning-off not observed")
            messages = [p["content"] for p in outer["output"] if p["type"] == "message"]
            if len(messages) != 1:
                raise ValueError("expected exactly one native message")
            return ModelReply(
                messages[0],
                stats["input_tokens"],
                stats["total_output_tokens"],
                stats["reasoning_output_tokens"],
                self.deployment_identity,
                stats["total_output_tokens"] >= request.output_reserve,
            )
        if outer.get("model") != self.identifier:
            raise ValueError(
                "compatible response identity differs from requested instance"
            )
        usage = outer["usage"]
        if any(
            type(usage.get(k)) is not int or usage[k] < 0
            for k in ("prompt_tokens", "completion_tokens")
        ):
            raise ValueError("invalid compatible usage")
        choices = outer["choices"]
        if len(choices) != 1:
            raise ValueError("expected one compatible choice")
        message = choices[0]["message"]
        calls = tuple(
            {
                "id": c["id"],
                "tool": c["function"]["name"],
                "arguments": strict_json(c["function"]["arguments"]),
            }
            for c in message.get("tool_calls", [])
        )
        reasoning = usage.get("completion_tokens_details", {}).get("reasoning_tokens")
        return ModelReply(
            message.get("content") or "",
            usage["prompt_tokens"],
            usage["completion_tokens"],
            reasoning,
            self.deployment_identity,
            choices[0].get("finish_reason") == "length",
            calls,
        )

    def harmless_probe(self) -> dict:
        """Two fresh <=6-call source/follow-up/report sequences; no reference answers."""
        results = []
        for index in range(2):
            workspace = SourceWorkspace(
                [
                    SourceDocument(
                        "canary-upstream",
                        "notes.txt",
                        "Canary API is deprecated.\nRemoval is planned later.\n",
                        {"revision": "canary-v1"},
                    ),
                    SourceDocument(
                        "canary-target",
                        "app.txt",
                        "call_canary_api()\n",
                        {"revision": "canary-v2"},
                    ),
                ],
                [
                    {"source_id": "canary-upstream", "revision": "canary-v1"},
                    {"source_id": "canary-target", "revision": "canary-v2"},
                ],
            )
            task = {
                "case_id": f"interface-canary-{index + 1}",
                "dependency": "canary",
                "old": "1",
                "proposed": "2",
                "qualification": "Read canary-upstream notes.txt line 1 and canary-target app.txt. Search exact literal ABSENT_CANARY_TERM in canary-target. After seeing notes line 1, follow up by reading notes.txt line 2 in a later call. Then signal finish_investigation and report, citing retained lines. You may batch the first three tools. No target code runs.",
            }
            result = run_investigation_trial(
                task, workspace, "agent", self, limits=TrialLimits(calls=6, seconds=180)
            )
            actions = [
                (event["event_id"], a)
                for event in result["trace"]
                for a in event.get("public_event", {}).get("actions", [])
            ]
            initial = next(
                (
                    eid
                    for eid, a in actions
                    if a["tool"] == "read_source"
                    and a["arguments"].get("source_id") == "canary-upstream"
                    and a["arguments"].get("start_line", 1) == 1
                ),
                None,
            )
            followup = any(
                eid != initial
                and a["tool"] == "read_source"
                and a["arguments"].get("source_id") == "canary-upstream"
                and a["arguments"].get("start_line") == 2
                for eid, a in actions
            )
            target = any(
                a["arguments"].get("source_id") == "canary-target"
                and a["tool"] == "read_source"
                for _, a in actions
            )
            zero = any(
                a["tool"] == "search_sources"
                and a["arguments"].get("query") == "ABSENT_CANARY_TERM"
                and a["arguments"].get("source_id") == "canary-target"
                for _, a in actions
            )
            citations = bool(
                result["report"]
                and any(c["citations"] for c in result["report"]["claims"])
            )
            result["qualification_checks"] = {
                "two_scopes": bool(initial and target),
                "later_followup": followup,
                "scoped_zero_search": zero,
                "report_citation": citations,
            }
            results.append(result)
            if not result["outcome"].startswith("completed") or not all(
                result["qualification_checks"].values()
            ):
                break
        return {
            "outcome": "passed"
            if len(results) == 2
            and all(
                r["outcome"].startswith("completed")
                and all(r["qualification_checks"].values())
                for r in results
            )
            else "failed",
            "interface": self.interface,
            "sequences": results,
            "native_function_call_support": "exercised"
            if self.interface == "compatible-tools"
            else "not tested; named text-JSON alternative",
        }
