"""Measured, stateless local JSON-action interface for the agency pilot.

The native chat API exposes reasoning control and total/reasoning usage. Tools
are described in ordinary prompt text and dispatched by our trial runner, not
by LM Studio integrations. This explicit alternate interface avoids claiming a
native-function-call comparison. SDK rendering is measured with a 64-token
allowance and checked against actual provider usage on every response.
"""

from __future__ import annotations

from dataclasses import asdict

from upgradepilot.upstream.support_drop_extractor import build_lm_studio_session

from .broader_agency_trial import (
    MeasuredRequest,
    ModelReply,
    ModelRequest,
    request_identity,
)
from .broader_agency_workspace import digest, strict_json


class LocalJSONActionProvider:
    def __init__(self, model, chat_factory, *, reasoning="off", temperature=0.2):
        self.model = model
        self.chat_factory = chat_factory
        self.reasoning = reasoning
        self.temperature = temperature
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
            "interface": "native-stateless-chat-with-text-JSON-actions-v1",
            "endpoint": "http://127.0.0.1:18080/api/v1/chat",
            "model": self.initial_info,
            "load_config": self.initial_load,
            "reasoning": self.reasoning,
            "temperature": self.temperature,
            "accounting": "SDK default prompt-template tokenizer + 64 token allowance; per-response native stats cross-check",
            "template_control_limit": "SDK apply_prompt_template uses default prediction stack, whereas native request explicitly sets reasoning; allowance is not a claim of exact native rendering",
        }

    def _check_deployment(self):
        info = self.model.get_info().to_dict()
        if (
            info["instanceReference"] != self.deployment_identity
            or self.model.get_load_config().to_dict() != self.initial_load
        ):
            raise ValueError("loaded deployment changed")

    def measure(self, request: ModelRequest) -> MeasuredRequest:
        self._check_deployment()
        chat = self.chat_factory(
            {
                "messages": [
                    {"role": "system", "content": request.system},
                    {"role": "user", "content": request.user},
                ]
            }
        )
        rendered = self.model.apply_prompt_template(chat)
        count = len(self.model.tokenize(rendered)) + 64
        return MeasuredRequest(
            count,
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
        payload = {
            "model": self.identifier,
            "input": request.user,
            "system_prompt": request.system,
            "reasoning": self.reasoning,
            "temperature": self.temperature,
            "max_output_tokens": request.output_reserve,
            "store": False,
            "stream": False,
        }
        # Timeout and frame cap also bound malformed/provider failure handling.
        with self.session.post(
            "http://127.0.0.1:18080/api/v1/chat",
            json=payload,
            timeout=min(timeout, 60),
            stream=True,
        ) as response:
            raw = bytearray()
            for chunk in response.iter_content(65536):
                raw.extend(chunk)
                if len(raw) > 1_048_576:
                    raise ValueError("provider frame exceeds 1 MiB")
            receipt = {
                "request_sha256": request_identity(request),
                "measurement": asdict(measurement),
                "payload": payload,
                "status": response.status_code,
                "body": raw.decode("utf-8"),
            }
            self.private_receipts.append(receipt)
            if response.status_code != 200:
                raise ValueError(f"local provider HTTP {response.status_code}")
        outer = strict_json(receipt["body"])
        if outer.get("model_instance_id") != self.identifier:
            raise ValueError("provider returned another model instance")
        stats = outer["stats"]
        fields = ("input_tokens", "total_output_tokens", "reasoning_output_tokens")
        if any(type(stats.get(key)) is not int or stats[key] < 0 for key in fields):
            raise ValueError("missing/invalid native usage stats")
        if self.reasoning == "off" and stats["reasoning_output_tokens"] != 0:
            raise ValueError("requested reasoning-off not observed")
        messages = [
            part["content"] for part in outer["output"] if part["type"] == "message"
        ]
        if len(messages) != 1:
            raise ValueError("expected exactly one native message")
        self._check_deployment()
        return ModelReply(
            messages[0],
            stats["input_tokens"],
            stats["total_output_tokens"],
            stats["reasoning_output_tokens"],
            self.deployment_identity,
            stats["total_output_tokens"] >= request.output_reserve,
        )

    def harmless_probe(self) -> dict:
        """Exercise actual JSON action, a tool response and final report; no source."""
        requests = [
            ModelRequest(
                'Return exactly {"tool":"echo","arguments":{"text":"capacity-canary"},"notes":""}.',
                "Harmless local interface probe; no source or secrets.",
                256,
            ),
            ModelRequest(
                'The tool returned {"text":"capacity-canary"}. Return exactly {"acknowledged":"capacity-canary"}.',
                "Acknowledge the supplied tool result, no other action.",
                256,
            ),
        ]
        outcomes = []
        for request in requests:
            measured = self.measure(request)
            if measured.input_tokens + request.output_reserve > measured.context_tokens:
                raise ValueError("probe cannot fit")
            reply = self.predict(request, measured, 60)
            if reply.input_tokens > measured.input_tokens or reply.truncated:
                raise ValueError("probe accounting/truncation problem")
            parsed = strict_json(reply.text)
            outcomes.append(
                {
                    "measurement": asdict(measured),
                    "usage": {
                        "input": reply.input_tokens,
                        "output": reply.output_tokens,
                        "reasoning": reply.reasoning_tokens,
                    },
                    "reply_sha256": digest(parsed),
                }
            )
            expected = (
                {"tool": "echo", "arguments": {"text": "capacity-canary"}, "notes": ""}
                if len(outcomes) == 1
                else {"acknowledged": "capacity-canary"}
            )
            if parsed != expected:
                raise ValueError("probe JSON/tool follow-up differs")
        return {
            "outcome": "passed",
            "probes": outcomes,
            "native_function_call_support": "not_tested; explicit text JSON-action interface",
        }
