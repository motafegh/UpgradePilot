"""Bounded local-model request/response seam for the B2/X1 ``EvidenceGapPlanner``.

This module is experiment support code, not UpgradePilot product runtime code.

R4-A1 owns the model-visible context projection and strict ``EvidenceGapDecision`` parser.
R4-A2 owns fresh deterministic action rebinding/admission. R4-A3 adds only the local-model
transport boundary between them::

    EvidenceGapPlannerContext
    -> explicit planner request projection
    -> one LM Studio OpenAI-compatible structured-output request
    -> provider envelope validation
    -> strict EvidenceGapDecision parsing
    -> EvidenceGapDecision OR EvidenceGapModelProblem

The provider/model never receives hidden executable action authority. A valid model decision
remains untrusted semantic output and still requires the R4-A2 deterministic admission boundary
before any selected investigation may execute.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Callable, Literal, Mapping

import requests
from requests import Response
from requests.exceptions import RequestException

from experiments.b2_x1_evidence_gap_planner import (
    EvidenceGapDecision,
    EvidenceGapPlannerContext,
    evidence_gap_decision_from_mapping,
    render_evidence_gap_planner_request,
)


LM_STUDIO_BASE_URL = "http://127.0.0.1:12345"
# Reuse the already-deployed local model for this bounded experiment. This does not extend
# ADR-0006's product adoption decision to the planner responsibility.
EVIDENCE_GAP_MODEL_ID = "gemma-4-e4b-it-ud"
REQUEST_TIMEOUT_SECONDS = 180.0
MAX_COMPLETION_TOKENS = 512

EvidenceGapModelProblemReason = Literal[
    "provider_request_failed",
    "provider_http_error",
    "provider_response_malformed",
    "completion_truncated",
    "structured_output_invalid",
]

SYSTEM_PROMPT = """You are UpgradePilot's bounded EvidenceGapPlanner.

Your only responsibility is to decide whether one currently offered investigation action should
be selected for the supplied planning question, or whether no action should execute now.

Rules:
- Treat the supplied context as the complete model-visible planning state for this turn.
- Select only an action_id that appears in allowed_actions.
- Do not invent repository paths, commands, tools, evidence, actions, or hidden execution details.
- Do not decide compatibility, safety, merge readiness, or maintainer action.
- QUESTION_SETTLED means the bounded planning question is sufficiently settled by the supplied state.
- KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY means a specific useful investigation is known but is not available in the current allowed action boundary.
- NO_JUSTIFIED_INVESTIGATION_IDENTIFIED means the question may remain non-final, but no useful current or specific outside-boundary investigation is identified.
- A selected action is only a proposal; deterministic code separately decides whether it is still authorized at execution time.
- Return only JSON conforming to the supplied schema.
"""

HttpPost = Callable[..., Response]


@dataclass(frozen=True, slots=True)
class EvidenceGapModelProblem:
    """Provider/structured-output failure before a usable planner decision exists."""

    reason: EvidenceGapModelProblemReason
    detail: str

    def __post_init__(self) -> None:
        if self.reason not in {
            "provider_request_failed",
            "provider_http_error",
            "provider_response_malformed",
            "completion_truncated",
            "structured_output_invalid",
        }:
            raise ValueError("evidence-gap model problem reason is unsupported.")
        if (
            not isinstance(self.detail, str)
            or not self.detail
            or self.detail != self.detail.strip()
        ):
            raise ValueError(
                "evidence-gap model problem detail must be non-empty trimmed text."
            )


type EvidenceGapModelResult = EvidenceGapDecision | EvidenceGapModelProblem


def build_lm_studio_session() -> requests.Session:
    """Return a loopback LM Studio session that ignores ambient proxy configuration.

    The experiment has the same local-transport security requirement as the adopted support-drop
    adapter, but product integration is not authorized, so this experiment keeps its transport
    helper local rather than creating a new product-level provider abstraction.
    """

    session = requests.Session()
    session.trust_env = False
    return session


def _post_without_ambient_proxy(*args: object, **kwargs: object) -> Response:
    with build_lm_studio_session() as session:
        return session.post(*args, **kwargs)


class LocalEvidenceGapPlanner:
    """Generate one untrusted ``EvidenceGapDecision`` through local LM Studio inference."""

    def __init__(self, *, post: HttpPost | None = None) -> None:
        self._post = post or _post_without_ambient_proxy

    def decide(self, context: EvidenceGapPlannerContext) -> EvidenceGapModelResult:
        if not isinstance(context, EvidenceGapPlannerContext):
            raise TypeError("context must be EvidenceGapPlannerContext.")

        payload = _request_payload(context)

        try:
            response = self._post(
                f"{LM_STUDIO_BASE_URL}/v1/chat/completions",
                json=payload,
                timeout=REQUEST_TIMEOUT_SECONDS,
            )
        except RequestException as exc:
            return _problem(
                "provider_request_failed",
                f"The local planner provider request failed: {type(exc).__name__}.",
            )
        except Exception as exc:
            return _problem(
                "provider_request_failed",
                f"The local planner provider call failed: {type(exc).__name__}.",
            )

        status_code = getattr(response, "status_code", None)
        if type(status_code) is not int or not 200 <= status_code < 300:
            rendered_status = status_code if type(status_code) is int else "unknown"
            return _problem(
                "provider_http_error",
                f"LM Studio returned an unsuccessful HTTP status: {rendered_status}.",
            )

        try:
            outer = response.json()
        except Exception as exc:
            return _problem(
                "provider_response_malformed",
                f"LM Studio returned malformed outer JSON: {type(exc).__name__}.",
            )

        if not isinstance(outer, dict):
            return _problem(
                "provider_response_malformed",
                "LM Studio response was not a JSON object.",
            )

        if _finish_reason(outer) == "length":
            return _problem(
                "completion_truncated",
                "LM Studio stopped because the completion length limit was reached.",
            )

        try:
            message_content = _provider_message_content(outer)
        except ValueError as exc:
            return _problem(
                "provider_response_malformed",
                f"LM Studio response envelope was unusable: {exc}",
            )

        try:
            structured = _structured_message_mapping(message_content)
            return evidence_gap_decision_from_mapping(structured)
        except (TypeError, ValueError, json.JSONDecodeError) as exc:
            return _problem(
                "structured_output_invalid",
                f"LM Studio planner output could not be mapped safely: {exc}",
            )


def _request_payload(context: EvidenceGapPlannerContext) -> dict[str, object]:
    rendered = render_evidence_gap_planner_request(context)
    context_payload = rendered["context"]
    output_schema = rendered["output_schema"]

    # ``render_evidence_gap_planner_request`` is the explicit authority/context projection owner.
    # The provider adapter serializes that already-bounded observation; it does not rediscover or
    # widen the model-visible field set.
    user_prompt = (
        "Current EvidenceGapPlanner context (JSON):\n"
        + json.dumps(context_payload, sort_keys=True, separators=(",", ":"))
        + "\n\nReturn one decision for this exact bounded context."
    )

    return {
        "model": EVIDENCE_GAP_MODEL_ID,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "upgradepilot_evidence_gap_decision_v1",
                "strict": True,
                "schema": output_schema,
            },
        },
        "temperature": 0,
        "seed": 0,
        "max_tokens": MAX_COMPLETION_TOKENS,
        "stream": False,
    }


def _provider_message_content(outer: Mapping[str, Any]) -> str:
    """Recover textual model content from the provider envelope only."""

    choices = outer.get("choices")
    if (
        not isinstance(choices, list)
        or not choices
        or not isinstance(choices[0], dict)
    ):
        raise ValueError("The provider response contained no usable first choice.")

    message = choices[0].get("message")
    if not isinstance(message, dict) or not isinstance(message.get("content"), str):
        raise ValueError("The first provider choice contained no textual message content.")
    return message["content"]


def _structured_message_mapping(message_content: str) -> Mapping[str, Any]:
    """Decode the model-owned structured content without granting semantic authority."""

    structured = json.loads(message_content)
    if not isinstance(structured, dict):
        raise ValueError("Structured planner content was not a JSON object.")
    return structured


def _finish_reason(outer: Mapping[str, Any]) -> str | None:
    choices = outer.get("choices")
    if (
        isinstance(choices, list)
        and choices
        and isinstance(choices[0], dict)
        and isinstance(choices[0].get("finish_reason"), str)
    ):
        return choices[0]["finish_reason"]
    return None


def _problem(
    reason: EvidenceGapModelProblemReason,
    detail: str,
) -> EvidenceGapModelProblem:
    return EvidenceGapModelProblem(reason=reason, detail=detail)


__all__ = (
    "EVIDENCE_GAP_MODEL_ID",
    "LM_STUDIO_BASE_URL",
    "MAX_COMPLETION_TOKENS",
    "REQUEST_TIMEOUT_SECONDS",
    "EvidenceGapModelProblem",
    "EvidenceGapModelProblemReason",
    "EvidenceGapModelResult",
    "LocalEvidenceGapPlanner",
    "build_lm_studio_session",
)
