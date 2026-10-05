"""Source-only API proposals for the declared-source experiment, never findings.

The producer maps every retained section; the model selects line references;
the decoder reconstructs evidence. Shape and reference checks do not adjudicate
meaning. Frozen prompt/schema assets stay with their preparation record.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Protocol

import requests

from upgradepilot.dependency.versioning import (
    PackagingVersionProblem,
    order_crossed_release_versions,
    parse_dependency_release_interval,
)
from upgradepilot.upstream.interval import DependencyReleaseInterval
from upgradepilot.upstream.support_drop_extractor import build_lm_studio_session

from .api_change_source_acquisition import AcquisitionProblem, DeclaredReleaseWindow
from .api_release_window_manifest import release_window_manifest

ROLE = "source-only-api-change-v1"
ASSETS = Path(__file__).resolve().parents[1] / (
    "working-memory/evidence/2026-10-05-api-interpretation-preparation"
)
MAX_RESPONSE_BYTES = 262_144
# Includes reasoning and structured output. The failed 1536-token pilot remains
# reproducible through explicit request settings and saved method identities.
OUTPUT_TOKENS = 8192
LOCAL_ENDPOINT = "http://127.0.0.1:18080/v1/chat/completions"
LOCAL_MODEL = "gemma-4-e4b-it-ud"


def text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def packet_hash(packet: object) -> str:
    return text_hash(
        json.dumps(packet, sort_keys=True, ensure_ascii=False, allow_nan=False)
    )


def strict_json(text: str, *, max_bytes: int = MAX_RESPONSE_BYTES) -> object:
    """Bound before parsing and reject duplicate keys/nonfinite JSON numbers."""
    if len(text.encode("utf-8")) > max_bytes:
        raise ValueError("JSON byte limit exceeded")

    def object_pairs(pairs):
        value = {}
        for key, item in pairs:
            if key in value:
                raise ValueError("duplicate JSON key")
            value[key] = item
        return value

    def invalid_constant(value):
        raise ValueError("nonfinite JSON number")

    return json.loads(
        text, object_pairs_hook=object_pairs, parse_constant=invalid_constant
    )


def source_input_from_projection(upstream: dict, interval: dict) -> dict:
    """Map an acquired projection, also used to check independently saved input.

    Complete sections and incomplete candidates share a text-map operation;
    neither source eligibility nor duplicate ambiguity is upgraded by mapping.
    Acquisition owns full-file verification. This boundary checks retained text,
    offsets and source relationships needed for exact downstream citations.
    """
    complete = upstream.get("state") == "available"
    examination = upstream.get("section_examination", {})
    context = upstream.get("source_context", {})
    if context.get("interval") is not None and context["interval"] != interval:
        raise ValueError("source interval differs from dependency interval")
    identity_owner = upstream if complete else examination
    identity = {
        "repository": identity_owner.get("repository"),
        "revision": identity_owner.get("revision"),
        "path": identity_owner.get("path"),
        "full_source_sha256": identity_owner.get(
            "sha256" if complete else "full_source_sha256"
        ),
        "source_basis": upstream.get("basis") if complete else context.get("basis"),
    }
    candidates = upstream["sections"] if complete else examination.get("candidates", [])
    required = (
        upstream["versions"] if complete else examination.get("required_versions", [])
    )
    if required:
        # Projection/save is a serialized boundary. Reuse the version owner so
        # a rewritten dependency interval cannot relabel an old complete window.
        native_interval = DependencyReleaseInterval(
            **{
                key: interval[key]
                for key in (
                    "package",
                    "normalized_package",
                    "old_version",
                    "proposed_version",
                )
            }
        )
        if interval != asdict(native_interval):
            raise ValueError("unsupported dependency interval shape/bounds")
        parsed = parse_dependency_release_interval(native_interval)
        if isinstance(parsed, PackagingVersionProblem) or isinstance(
            order_crossed_release_versions(parsed, required), PackagingVersionProblem
        ):
            raise ValueError("required releases differ from dependency interval")
    if complete and (
        len(candidates) != len(required)
        or len(set(required)) != len(required)
        or {c["version"] for c in candidates} != set(required)
    ):
        raise ValueError("complete sections differ from required releases")
    if any(c["version"] not in required for c in candidates):
        raise ValueError("candidate release outside required window")
    sections = []
    omitted = []
    retained = [c for c in candidates if c.get("text")]
    for candidate in candidates:
        if not candidate.get("text"):
            omitted.append({k: v for k, v in candidate.items() if k != "text"})
    for index, candidate in enumerate(
        sorted(retained, key=lambda c: c["start_offset"]), 1
    ):
        text = candidate["text"]
        start, end = candidate["start_offset"], candidate["end_offset"]
        line = candidate["start_line"]
        if (
            type(start) is not int
            or type(end) is not int
            or type(line) is not int
            or start < 0
            or line < 1
            or end != start + len(text)
            or candidate["sha256"] != text_hash(text)
        ):
            raise ValueError("retained source range/hash mismatch")
        if any(not isinstance(v, str) or not v for v in identity.values()):
            raise ValueError("retained text lacks exact source identity/basis")
        section_id = f"S{index}"
        offset = start
        lines = []
        for number, line_text in enumerate(text.splitlines(keepends=True), 1):
            lines.append(
                {
                    "line_id": f"{section_id}:L{number}",
                    "source_line_number": line + number - 1,
                    "start_offset": offset,
                    "end_offset": offset + len(line_text),
                    "text": line_text,
                }
            )
            offset += len(line_text)
        sections.append(
            {
                "section_id": section_id,
                "release_version": candidate["version"],
                "source_identity": identity,
                "start_line": line,
                "start_offset": start,
                "end_offset": end,
                "text": text,
                "sha256": candidate["sha256"],
                "lines": lines,
            }
        )
    return {
        "role_version": ROLE,
        "interval": interval,
        "source_identity": identity,
        "source_coverage": {
            "complete_window_eligible": complete
            and upstream.get("complete_window_eligible") is True,
            "acquisition_coverage": upstream.get("coverage"),
            "required_versions": list(required),
            "supplied_versions": list(
                dict.fromkeys(s["release_version"] for s in sections)
            ),
            "missing_or_unsupported_versions": list(
                examination.get("missing_or_unsupported_versions", [])
            ),
            "ambiguous_versions": list(examination.get("ambiguous_versions", [])),
            "issues": list(examination.get("issues", [])),
            "text_omission_reason": examination.get("text_omission_reason"),
            "max_characters": examination.get("max_characters"),
            "omitted_candidates": omitted,
            "acquisition_problem": None
            if complete
            else {k: upstream.get(k) for k in ("stage", "reason", "detail")},
        },
        "sections": sections,
    }


def frozen_contract() -> tuple[str, str, dict, dict]:
    """Load the two frozen producer assets; evaluation answers never enter here."""
    manifest = json.loads((ASSETS / "freeze-manifest.json").read_text())
    assets = {}
    hashes = {}
    for name in ("prompt-template-v1.md", "output-schema-v1.json"):
        raw = (ASSETS / name).read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if digest != manifest["files"][name]["sha256"]:
            raise ValueError("frozen producer asset changed")
        assets[name] = raw.decode("utf-8")
        hashes[name] = digest
    blocks = re.findall(r"```text\n(.*?)\n```", assets["prompt-template-v1.md"], re.S)
    if len(blocks) != 2:
        raise ValueError("unexpected frozen prompt layout")
    return blocks[0], blocks[1], json.loads(assets["output-schema-v1.json"]), hashes


@dataclass(frozen=True)
class InterpretationRequest:
    source_input: dict
    payload: dict
    method: dict


def prepare_request(
    source_input: dict, *, max_output_tokens: int = OUTPUT_TOKENS
) -> InterpretationRequest:
    if type(max_output_tokens) is not int or max_output_tokens < 1:
        raise ValueError("output token budget must be a positive integer")
    system, user_template, schema, hashes = frozen_contract()
    # Send each source character once. Offsets/hashes belong to the retained map,
    # not model work; compact labelled lines preserve all available source text.
    rendered_sections = [
        {
            "section_id": section["section_id"],
            "release_version": section["release_version"],
            "lines": [
                {"line_id": line["line_id"], "text": line["text"]}
                for line in section["lines"]
            ],
        }
        for section in source_input["sections"]
    ]
    user = user_template.format(
        package_and_dependency_interval=json.dumps(
            source_input["interval"], ensure_ascii=False
        ),
        declared_source_basis_and_exact_source_identity=json.dumps(
            source_input["source_identity"], ensure_ascii=False
        ),
        required_supplied_missing_ambiguous_releases_and_source_limits=json.dumps(
            source_input["source_coverage"], ensure_ascii=False
        ),
        all_available_sections_in_source_order_with_release_context_and_line_ids=json.dumps(
            rendered_sections, ensure_ascii=False
        ),
    )
    payload = {
        "model": LOCAL_MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": ROLE.replace("-", "_"),
                "strict": True,
                "schema": schema,
            },
        },
        "temperature": 0,
        "seed": 0,
        "max_tokens": max_output_tokens,
        "stream": False,
    }
    return InterpretationRequest(
        source_input,
        payload,
        {
            "role_version": ROLE,
            "renderer_version": 1,
            "asset_sha256": hashes,
            "input_sha256": packet_hash(source_input),
            "request_sha256": packet_hash(payload),
            "interpreter_code_sha256": hashlib.sha256(
                Path(__file__).read_bytes()
            ).hexdigest(),
            "model": LOCAL_MODEL,
            "temperature": 0,
            "seed": 0,
            "max_output_tokens": max_output_tokens,
        },
    )


def validate_shape(value: object, schema: dict) -> None:
    """Interpret only the shape keywords used by the frozen schema.

    This small trial decoder avoids maintaining a second semantic field table.
    A new schema version requires reviewing this decoder's supported keywords.
    """
    allowed = {
        "$schema",
        "title",
        "type",
        "additionalProperties",
        "properties",
        "required",
        "items",
        "minItems",
        "maxItems",
        "minLength",
        "maxLength",
        "enum",
    }
    if set(schema) - allowed:
        raise ValueError("unsupported frozen schema keyword")
    types = schema["type"]
    types = [types] if isinstance(types, str) else types
    actual = {dict: "object", list: "array", str: "string", type(None): "null"}.get(
        type(value)
    )
    if actual not in types:
        raise ValueError("wrong output type")
    if "enum" in schema and value not in schema["enum"]:
        raise ValueError("unknown output enum")
    if actual == "object":
        properties = schema["properties"]
        if set(schema["required"]) - value.keys() or value.keys() - properties.keys():
            raise ValueError("missing or extra output fields")
        for key, item in value.items():
            validate_shape(item, properties[key])
    elif actual == "array":
        if (
            not schema.get("minItems", 0)
            <= len(value)
            <= schema.get("maxItems", len(value))
        ):
            raise ValueError("output array size")
        for item in value:
            validate_shape(item, schema["items"])
    elif actual == "string":
        if (
            not schema.get("minLength", 0)
            <= len(value)
            <= schema.get("maxLength", len(value))
        ):
            raise ValueError("output string size")


class GroundingError(ValueError):
    """A syntactically valid reference does not recover supplied source."""


def recover_spans(spans: list, source_input: dict) -> list:
    lookup = {
        line["line_id"]: (section, index)
        for section in source_input["sections"]
        for index, line in enumerate(section["lines"])
    }
    evidence = []
    for span in spans:
        try:
            start_section, start = lookup[span["start_line_id"]]
            end_section, end = lookup[span["end_line_id"]]
        except KeyError as exc:
            raise GroundingError("source line ID absent") from exc
        if start_section is not end_section or start > end:
            raise GroundingError("cross-section or reversed source span")
        lines = start_section["lines"][start : end + 1]
        quote = "".join(line["text"] for line in lines)
        evidence.append(
            {
                "source_identity": start_section["source_identity"],
                "reported_in_version": start_section["release_version"],
                "section_id": start_section["section_id"],
                "start_line": lines[0]["source_line_number"],
                "end_line": lines[-1]["source_line_number"],
                "start_offset": lines[0]["start_offset"],
                "end_offset": lines[-1]["end_offset"],
                "quote": quote,
                "quote_sha256": text_hash(quote),
            }
        )
    return evidence


def decode_proposals(output: object, source_input: dict, *, schema: dict) -> dict:
    """Validate with the exact request schema, then recover producer-owned text."""
    validate_shape(output, schema)
    for observation in output["observations"]:
        needs_reason = (
            observation["kind"] == "unclear"
            or observation["assertion"] == "uncertain"
            or observation["subject"] is None
            or observation["timing"] == "unspecified"
        )
        if needs_reason and not (observation["reason"] or "").strip():
            raise ValueError("uncertainty needs a nonblank reason")
    if any(not item["reason"].strip() for item in output["unassessed"]):
        raise ValueError("unassessed needs a nonblank reason")
    return {
        key: [
            {**item, "evidence": recover_spans(item["source_spans"], source_input)}
            for item in output[key]
        ]
        for key in ("observations", "unassessed")
    }


@dataclass(frozen=True)
class ProviderReply:
    content: str | None = None
    finish_reason: str | None = "stop"
    problem: tuple[str, str] | None = None


class InterpretationProvider(Protocol):
    identity: dict

    def complete(self, request: InterpretationRequest) -> ProviderReply: ...


@dataclass(frozen=True)
class RequestCapacityEvidence:
    """Caller-measured accounting, bound to this exact request and deployment.

    Counts must include chat template and schema overhead. This record does not
    itself measure tokens or attest that the caller's measurement is authentic.
    The subsequent live-evaluation owner supplies and verifies that evidence.
    """

    request_sha256: str
    model: str
    deployment_identity: str
    tokenizer_identity: str
    template_identity: str
    accounting_method: str
    effective_context_tokens: int
    input_tokens: int
    reserved_output_tokens: int


class LocalInterpretationProvider:
    """One direct loopback request, only after request-bound capacity evidence."""

    def __init__(
        self,
        *,
        capacity: RequestCapacityEvidence | None = None,
        session=None,
        response_observer=None,
    ):
        self.capacity = capacity
        self.session = session if session is not None else build_lm_studio_session()
        self.session.trust_env = False
        # Evaluation can retain a bounded HTTP frame privately and inspect usage.
        # The observer supplies no output correction or admission authority.
        self.response_observer = response_observer
        self.identity = {
            "kind": "local_lm_studio",
            "endpoint": LOCAL_ENDPOINT,
            "capacity": vars(capacity) if capacity is not None else None,
        }

    def complete(self, request: InterpretationRequest) -> ProviderReply:
        capacity = self.capacity
        if capacity is None:
            return ProviderReply(
                problem=("context_problem", "effective_capacity_unverified")
            )
        if (
            capacity.request_sha256 != packet_hash(request.payload)
            or capacity.model != request.payload["model"]
            or any(
                not isinstance(v, str) or not v.strip()
                for v in (
                    capacity.deployment_identity,
                    capacity.tokenizer_identity,
                    capacity.template_identity,
                    capacity.accounting_method,
                )
            )
            or any(
                type(v) is not int or v < 1
                for v in (
                    capacity.effective_context_tokens,
                    capacity.input_tokens,
                    capacity.reserved_output_tokens,
                )
            )
            or capacity.reserved_output_tokens < request.payload["max_tokens"]
        ):
            return ProviderReply(
                problem=("context_problem", "capacity_identity_or_accounting_mismatch")
            )
        if (
            capacity.input_tokens + capacity.reserved_output_tokens
            > capacity.effective_context_tokens
        ):
            return ProviderReply(
                problem=("context_problem", "input_and_output_reserve_exceed_context")
            )
        try:
            with self.session.post(
                LOCAL_ENDPOINT,
                json=request.payload,
                timeout=180,
                allow_redirects=False,
                stream=True,
            ) as response:
                chunks = bytearray()
                for chunk in response.iter_content(chunk_size=8192):
                    chunks.extend(chunk)
                    if len(chunks) > MAX_RESPONSE_BYTES:
                        return ProviderReply(
                            problem=("provider_problem", "response_byte_limit")
                        )
                if self.response_observer is not None:
                    self.response_observer(response.status_code, bytes(chunks))
                if response.status_code != 200:
                    return ProviderReply(
                        problem=(
                            "provider_problem",
                            f"http_status_{response.status_code}",
                        )
                    )
                outer = strict_json(chunks.decode("utf-8"))
            choices = outer["choices"]
            if not isinstance(choices, list) or len(choices) != 1:
                raise ValueError("unexpected choices")
            choice = choices[0]
            message = choice["message"]
            if message.get("refusal") or message.get("tool_calls"):
                return ProviderReply(
                    problem=("provider_problem", "refusal_or_tool_output")
                )
            if not isinstance(message["content"], str):
                raise ValueError("missing structured content")
            return ProviderReply(message["content"], choice["finish_reason"])
        except requests.RequestException as exc:
            return ProviderReply(problem=("provider_problem", type(exc).__name__))
        except (ValueError, KeyError, TypeError, AttributeError, RecursionError):
            return ProviderReply(
                problem=("provider_problem", "malformed_provider_envelope")
            )


def interpret_projection(
    upstream: dict, interval: dict, provider: InterpretationProvider
) -> dict:
    """Preserve scope on failure; no partial candidates, retries or semantic vote."""
    try:
        source_input = source_input_from_projection(upstream, interval)
    except (ValueError, KeyError, TypeError, AttributeError):
        return {
            **_result_envelope(None),
            "state": "input_problem",
            "problem": {
                "stage": "input_problem",
                "reason": "invalid_source_relationships",
            },
        }
    return interpret_source_input(source_input, provider)


def _result_envelope(source_input: dict | None) -> dict:
    return {
        "role_version": ROLE,
        "source_input": source_input,
        "method": None,
        "observations": [],
        "unassessed": [],
        "problem": None,
    }


def interpret_source_input(
    source_input: dict,
    provider: InterpretationProvider,
    *,
    max_output_tokens: int = OUTPUT_TOKENS,
) -> dict:
    """Interpret a producer-validated map; calibration never becomes acquisition.

    Ordinary callers enter through interpret_acquired_source/interpret_projection.
    The evaluation adapter independently checks its frozen calibration maps and
    labels their weaker/constructed scope before entering this shared mechanism.
    """
    packet = _result_envelope(source_input)

    def fail(stage, reason):
        return {**packet, "state": stage, "problem": {"stage": stage, "reason": reason}}

    if not packet["source_input"]["sections"]:
        return fail("input_problem", "no_retained_source_text")
    try:
        request = prepare_request(
            packet["source_input"], max_output_tokens=max_output_tokens
        )
    except (OSError, ValueError, KeyError):
        return fail("contract_problem", "frozen_producer_assets_invalid")
    packet["method"] = {**request.method, "provider": provider.identity}
    try:
        reply = provider.complete(request)
    except Exception as exc:
        # A provider failure must not erase the independently acquired branches.
        return fail("provider_problem", type(exc).__name__)
    if reply.problem:
        return fail(*reply.problem)
    if reply.finish_reason != "stop":
        return fail(
            "provider_problem",
            "output_truncated"
            if reply.finish_reason == "length"
            else "unexpected_finish_reason",
        )
    try:
        proposals = decode_proposals(
            strict_json(reply.content),
            request.source_input,
            schema=request.payload["response_format"]["json_schema"]["schema"],
        )
    except GroundingError as exc:
        return fail("grounding_problem", str(exc))
    except (ValueError, TypeError, AttributeError, RecursionError):
        return fail("contract_problem", "invalid_structured_output")
    return {
        **packet,
        **proposals,
        "state": "observations_returned"
        if proposals["observations"]
        else "no_observations_returned",
    }


def interpret_acquired_source(
    source: DeclaredReleaseWindow | AcquisitionProblem,
    interval: dict,
    provider: InterpretationProvider,
) -> dict:
    return interpret_projection(release_window_manifest(source), interval, provider)
