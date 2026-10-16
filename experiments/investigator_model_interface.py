"""Stateless LM Studio binding for the experiment-owned Workspace trial.

Start at StatelessInvestigatorModel: pack -> measure the complete rendered request ->
SDK prediction -> exact visible response -> existing strict adapter admission. Product
Workspace/source authority stays with investigator_workspace_adapter. No model loading,
case selection, output repair or automatic retries live here.

The pinned optional SDK 1.5.0 drops newer server fields in its high-level config reader
and cannot set enableThinking through its public prediction config. SDKBinding uses its
existing typed RPC/prediction channel, retaining raw configuration and scalar usage while
filtering reasoning fragments before any artifact is written. This small version-specific
binding fails on unsupported shapes; it does not install/patch the SDK or switch transports.
"""

from __future__ import annotations

import hashlib
import importlib.metadata
import json
import os
import sys
import time
from copy import deepcopy
from dataclasses import dataclass, replace
from pathlib import Path

from experiments.investigator_workspace_trial import (
    PackedInput,
    pack_input,
    run_scripted_trial,
)
from upgradepilot.workspace.native_representation import json_bytes

REFERENCE_POLICY = "current-complete-stateless-request/1"
WIRE_INSTRUCTION = """Return exactly one JSON object, without markdown or commentary.
For phase investigate return {\"tool\": an offered name, \"arguments\": its schema object}.
For phase report return the entire report_schema object. All state is explicit in this
request. Only typed evidence references inside the included complete events are eligible
for notes or report citations now; omitted events and earlier requests grant no memory.
Use read_trial_event or re-read sources to recover omitted evidence before citing it.
"""


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def private_write(path: Path, content: bytes):
    """Never overwrite prior request/result evidence or expose it through Git defaults."""
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "wb") as stream:
        stream.write(content)


def fields(config: dict) -> dict:
    values = config["fields"]
    result = {item["key"]: item["value"] for item in values}
    if len(result) != len(values):
        raise ValueError("ambiguous duplicate server configuration field")
    return result


@dataclass(frozen=True)
class ModelLimits:
    context: int
    generated_per_call: int = 8192
    input_total: int = 524288
    generated_total: int = 131072
    calls: int = 6
    margin: int = 256
    seconds: int = 14400

    def __post_init__(self):
        if any(type(value) is not int or value < 1 for value in vars(self).values()):
            raise ValueError("model limits must be positive integers")
        if self.context <= self.generated_per_call + self.margin:
            raise ValueError("no model input capacity after generation reserve")


@dataclass(frozen=True)
class MeasuredInput:
    packed: PackedInput
    messages: dict
    rendered: str
    token_ids_sha256: str
    tokens: int
    configuration: dict


def measure_input(binding, packed: PackedInput, configuration: dict) -> MeasuredInput:
    body = json.loads(packed.content)
    # The whole packed object (including exact escaped event bytes) is a single user
    # message. There is no server-side prior-response ID or implicit conversation.
    messages = {
        "messages": [
            {"role": "system", "content": body["system"] + "\n" + WIRE_INSTRUCTION},
            {"role": "user", "content": packed.content.decode("utf-8")},
        ]
    }
    rendered = binding.render(messages, configuration)
    if not rendered or packed.content.decode("utf-8") not in rendered:
        raise ValueError("rendered request lost or transformed complete packed input")
    for reference in packed.reference_ids:
        if reference not in rendered:
            raise ValueError("rendered request lost an eligible evidence reference")
    tokens = binding.tokenize(rendered)
    if not tokens or any(type(t) is not int or t < 0 for t in tokens):
        raise ValueError("invalid actual tokenizer result")
    return MeasuredInput(
        packed,
        messages,
        rendered,
        digest(json_bytes(tokens)),
        len(tokens),
        configuration,
    )


class SDKBinding:
    """Pinned installed SDK channel; one fresh explicit history for every prediction.

    Raw RPC is needed to retain the applied template/advanced load settings. The same
    predictionConfigStack is supplied to rendering and prediction. Success metadata is
    intercepted before SDK 1.5.0 discards unknown fields; reasoning text is never retained.
    """

    def __init__(self, model, sdk):
        self.model, self.sdk = model, sdk

    def raw_load(self):
        from lmstudio._sdk_models import LlmRpcGetLoadConfigParameter

        parameter = LlmRpcGetLoadConfigParameter._from_api_dict(
            {"specifier": self.specifier}
        )
        return self.model._session.remote_call("getLoadConfig", parameter)

    @property
    def specifier(self):
        return {"type": "query", "query": {"identifier": self.model.identifier}}

    def identity(self):
        return {"model": self.model.get_info().to_dict(), "load": self.raw_load()}

    def render(self, messages, configuration):
        from lmstudio._sdk_models import LlmRpcApplyPromptTemplateParameter

        chat = self.sdk.Chat.from_history(messages)
        parameter = LlmRpcApplyPromptTemplateParameter._from_api_dict(
            {
                "specifier": self.specifier,
                "history": chat._get_history_for_prediction(),
                "predictionConfigStack": configuration,
                "opts": {},
            }
        )
        return self.model._session.remote_call("applyPromptTemplate", parameter)[
            "formatted"
        ]

    def tokenize(self, rendered):
        return list(self.model.tokenize(rendered))

    def predict(self, measured, timeout):
        from lmstudio.json_api import ChatResponseEndpoint
        from lmstudio.sync_api import PredictionStream

        class CapturedEndpoint(ChatResponseEndpoint):
            metadata = None
            reasoning_observed = False

            def iter_message_events(endpoint, contents):
                if contents and contents.get("type") == "fragment":
                    fragment = contents["fragment"]
                    if fragment.get("reasoningType") not in (None, "none"):
                        endpoint.reasoning_observed = True
                        # Do not pass hidden content to the SDK's accumulated result.
                        return
                if contents and contents.get("type") == "success":
                    endpoint.metadata = {
                        key: contents[key]
                        for key in (
                            "stats",
                            "modelInfo",
                            "loadModelConfig",
                            "predictionConfig",
                        )
                    }
                yield from super().iter_message_events(contents)

        self.sdk.set_sync_api_timeout(timeout)
        endpoint = CapturedEndpoint(
            self.model.identifier,
            self.sdk.Chat.from_history(measured.messages),
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        )
        endpoint.creation_params["predictionConfigStack"] = measured.configuration
        with PredictionStream(
            self.model._session._create_channel(endpoint), endpoint
        ) as stream:
            result = stream.wait_for_result()
        if endpoint.metadata is None:
            raise ValueError(
                "prediction ended without actual configuration/usage receipt"
            )
        return (
            result.content.encode("utf-8"),
            endpoint.metadata,
            endpoint.reasoning_observed,
        )


def import_isolated_sdk(site: Path):
    """Explicit optional SDK selection; process-local proxy exclusion, no global changes."""
    sys.path.append(str(site.resolve(strict=True)))
    if importlib.metadata.version("lmstudio") != "1.5.0":
        raise ValueError("this qualified binding requires isolated lmstudio==1.5.0")
    import lmstudio

    if not Path(lmstudio.__file__).resolve().is_relative_to(site.resolve()):
        raise ValueError("another SDK shadowed the selected isolated installation")
    for key in (
        "HTTP_PROXY",
        "HTTPS_PROXY",
        "ALL_PROXY",
        "http_proxy",
        "https_proxy",
        "all_proxy",
    ):
        os.environ.pop(key, None)
    os.environ["NO_PROXY"] = "127.0.0.1,localhost,::1"
    return lmstudio


def prediction_configuration(raw_load, *, output_tokens=8192):
    """Freeze the actual loaded template, explicit reasoning-off and overflow refusal."""
    template = deepcopy(fields(raw_load)["llm.load.promptTemplate"])
    if not template.get("jinjaPromptTemplate", {}).get("template"):
        raise ValueError("actual loaded template content is unavailable")
    # The installed server's load record omits stopStrings, while its prediction
    # schema requires them. Freeze an explicit no-extra-stop policy rather than
    # inventing a delimiter or mutating the retained original load receipt.
    template.setdefault("stopStrings", [])
    return {
        "layers": [
            {
                "layerName": "apiOverride",
                "config": {
                    "fields": [
                        {"key": "llm.prediction.promptTemplate", "value": template},
                        {
                            "key": "llm.prediction.reasoning.enableThinking",
                            "value": False,
                        },
                        {"key": "llm.prediction.temperature", "value": 0.2},
                        {
                            "key": "llm.prediction.maxPredictedTokens",
                            "value": {"checked": True, "value": output_tokens},
                        },
                        {
                            "key": "llm.prediction.contextOverflowPolicy",
                            "value": "stopAtLimit",
                        },
                    ]
                },
            }
        ]
    }


class StatelessInvestigatorModel:
    """Trusted trial callback with actual usage/capacity and request-local references.

    The caller freezes identity/configuration/batch before constructing this callback and
    first calls prepare() without inference for inspection. Receipts are written before
    prediction; failures/unknown usage consume an attempt and stop the assignment.
    The ordinary adapter parser handles the exact visible bytes without salvage.
    """

    def __init__(
        self, binding, configuration, limits, directory, *, clock=time.monotonic
    ):
        self.binding, self.configuration, self.limits = (
            binding,
            deepcopy(configuration),
            limits,
        )
        prediction_fields = fields(self.configuration["layers"][0]["config"])
        if prediction_fields["llm.prediction.maxPredictedTokens"] != {
            "checked": True,
            "value": limits.generated_per_call,
        }:
            raise ValueError(
                "prediction generation ceiling differs from admitted reserve"
            )
        self.configuration_sha256 = digest(json_bytes(self.configuration))
        self.identity = binding.identity()
        self.directory = Path(directory)
        self.directory.mkdir(mode=0o700, parents=True, exist_ok=False)
        self.clock, self.started = clock, clock()
        self.receipts = []
        self.input_tokens = self.output_tokens = 0
        self.usage_complete = True

    def prepare(self, packed):
        if digest(json_bytes(self.configuration)) != self.configuration_sha256:
            raise ValueError("prediction configuration changed since freeze")
        if self.binding.identity() != self.identity:
            raise ValueError("deployment changed since freeze")
        measured = measure_input(self.binding, packed, self.configuration)
        if (
            measured.tokens + self.limits.generated_per_call + self.limits.margin
            > self.limits.context
        ):
            raise ValueError(
                "rendered input plus generation reserve/margin exceeds context"
            )
        return measured

    def pack(self, protocol, history, phase, capacity):
        """Newest whole events; token overflow removes whole events, never source text.

        Whole-event omission metadata remains explicit. Fixed prompt overflow refuses.
        Each candidate is measured with the actual loaded tokenizer and frozen template.
        """
        while True:
            packed = pack_input(protocol, history, phase, capacity)
            try:
                self.prepare(packed)
                return packed
            except ValueError as error:
                if "exceeds context" not in str(error):
                    raise
                # Byte packing is monotone enough for admission only: reducing it may
                # discard more than the maximal token pack. No optimal-packing claim.
                if not json.loads(packed.content)["events"]:
                    raise ValueError("fixed rendered prompt cannot fit") from error
                capacity = min(capacity - 1, len(packed.content) - 1)

    def __call__(self, packed):
        measured = self.prepare(packed)
        remaining = self.limits.seconds - (self.clock() - self.started)
        if (
            not self.usage_complete
            or len(self.receipts) >= self.limits.calls
            or remaining <= 0
            or self.input_tokens + measured.tokens > self.limits.input_total
            or self.output_tokens + self.limits.generated_per_call
            > self.limits.generated_total
        ):
            raise ValueError("model budget refuses prediction before dispatch")
        number = len(self.receipts) + 1
        prefix = self.directory / f"call-{number:02}"
        request = {
            "messages": measured.messages,
            "configuration": self.configuration,
            "reference_policy": REFERENCE_POLICY,
            "references": sorted(packed.reference_ids),
            "omitted_events": packed.omitted_event_ids,
            "rendered_tokens": measured.tokens,
            "token_ids_sha256": measured.token_ids_sha256,
            "rendered_sha256": digest(measured.rendered.encode()),
            "identity": self.identity,
        }
        private_write(prefix.with_suffix(".request.json"), json_bytes(request))
        private_write(prefix.with_suffix(".rendered.txt"), measured.rendered.encode())
        receipt = {
            "attempt": number,
            "request_sha256": digest(json_bytes(request)),
            "usage": None,
            "outcome": "attempted",
        }
        usage_validated = False
        self.receipts.append(receipt)
        started = self.clock()
        try:
            content, metadata, reasoning = self.binding.predict(
                measured, min(1800, remaining)
            )
            private_write(prefix.with_suffix(".visible-response.txt"), content)
            private_write(prefix.with_suffix(".metadata.json"), json_bytes(metadata))
            if digest(json_bytes(self.configuration)) != self.configuration_sha256:
                raise ValueError("prediction configuration changed during call")
            stats = metadata["stats"]
            receipt.update(usage=stats, reasoning_fragment_observed=reasoning)
            values = [
                stats.get(k)
                for k in (
                    "promptTokensCount",
                    "predictedTokensCount",
                    "totalTokensCount",
                )
            ]
            if any(type(v) is not int or v < 0 for v in values):
                raise ValueError("missing/invalid actual model usage")
            prompt, generated, total = values
            self.input_tokens += prompt
            self.output_tokens += generated
            usage_validated = True
            if total != prompt + generated or prompt != measured.tokens:
                raise ValueError(
                    "actual prompt usage differs from fully rendered tokenizer measurement"
                )
            if (
                metadata["modelInfo"]["instanceReference"]
                != self.identity["model"]["instanceReference"]
            ):
                raise ValueError("response came from another model instance")
            applied = fields(metadata["predictionConfig"])
            for setting in self.configuration["layers"][0]["config"]["fields"]:
                if applied.get(setting["key"]) != setting["value"]:
                    raise ValueError(
                        "requested prediction setting not applied: " + setting["key"]
                    )
            if self.binding.identity() != self.identity:
                raise ValueError("deployment changed during prediction")
            if reasoning:
                raise ValueError(
                    "reasoning-off request produced reasoning fragments; content discarded"
                )
            if (
                stats["stopReason"] not in {"eosFound", "stopStringFound"}
                or generated >= self.limits.generated_per_call
                or prompt + generated + self.limits.margin > self.limits.context
            ):
                raise ValueError(
                    "generation incomplete, exhausted or outside context envelope"
                )
            if not content.strip():
                raise ValueError("empty visible model response")
            receipt["outcome"] = "returned"
            return content
        except Exception as error:
            self.usage_complete = usage_validated
            receipt.update(outcome="failed", problem=f"{type(error).__name__}: {error}")
            raise
        finally:
            receipt["elapsed_seconds"] = self.clock() - started
            private_write(prefix.with_suffix(".receipt.json"), json_bytes(receipt))


def run_model_trial(assignment, model, *, limits, protocol=None):
    """Use the existing admission/accounting engine with request-local evidence only."""

    def pack(default_protocol, history, phase, capacity):
        return model.pack(protocol or default_protocol, history, phase, capacity)

    result = run_scripted_trial(
        assignment,
        model,
        limits=limits,
        reference_visibility="current_request",
        input_packer=pack,
    )
    charges = dict(result.charges)
    charges.update(
        model_calls=len(model.receipts),
        model_tokens={"input": model.input_tokens, "generated": model.output_tokens}
        if model.usage_complete
        else None,
        model_usage_complete=model.usage_complete,
        # SDK may report total generated usage without a separate reasoning count.
        # Do not turn absence of reasoning fragments into zero reasoning tokens.
        reasoning_tokens=None,
    )
    return replace(result, charges=charges)
