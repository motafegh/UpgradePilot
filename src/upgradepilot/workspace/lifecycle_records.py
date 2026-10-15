"""Fixed representations for retained investigation interactions, never execution policy.

The host captures these attributed values through lifecycle_boundary; reconstruction uses
only this closed table. Request/admission/attempt/observation/evaluation are distinct facts.
An admission in history grants no current capability authority, and a termination or stop
proposal is not an adequacy assessment. Native conclusions remain native record references.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, cast

from .native_representation import (
    Either,
    LiteralValues,
    NativeReconstructionError,
    NativeValueCodec,
    RecordLayout,
    RecordRef,
    SequenceOf,
)


@dataclass(frozen=True, slots=True)
class LifecycleMethodIdentity:
    owner: str
    method: str | None
    version: str | None
    model: str | None
    contract: str | None
    configuration: str | None
    retention_gaps: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class DiscoveryObjective:
    question: str
    scope: str
    decision_relevance: str
    coverage_limit: str


@dataclass(frozen=True, slots=True)
class InvestigationNeed:
    proposition_key: str
    discriminator: str
    scope: str


@dataclass(frozen=True, slots=True)
class CapabilityRequest:
    purpose_id: str
    capability: str
    scope: str


@dataclass(frozen=True, slots=True)
class RequestAdmission:
    request_id: str
    outcome: Literal["admitted", "rejected"]
    policy_id: str
    detail: str


@dataclass(frozen=True, slots=True)
class ExecutionAttempt:
    admission_id: str
    state: Literal["intent_recorded", "started", "completion_unknown"]


@dataclass(frozen=True, slots=True)
class CapabilityObservation:
    """Outcome under the admitted request scope; detail retains actual coverage limits."""

    attempt_id: str
    outcome: Literal["observed", "empty", "scoped_negative", "problem"]
    scope: str
    detail: str
    representation: str | None = None
    retained_content: str | None = None


@dataclass(frozen=True, slots=True)
class ExecutionInterruption:
    """Interrupted intent: external completion unknown, or execution known not started."""

    attempt_id: str
    problem_kind: str
    completion: Literal["unknown", "not_started"] = "unknown"


@dataclass(frozen=True, slots=True)
class EvaluationOutcome:
    subject_id: str
    outcome: Literal["evaluated", "unsupported", "failed", "stale"]
    native_assessment_id: str | None
    detail: str


@dataclass(frozen=True, slots=True)
class ConsumerView:
    consumer: str
    delivered_native_ids: tuple[str, ...]
    omitted_native_ids: tuple[str, ...]
    selection_limit: str


@dataclass(frozen=True, slots=True)
class ObservableUse:
    view_id: str
    native_ids: tuple[str, ...]
    receipt: str


@dataclass(frozen=True, slots=True)
class AttributedProposal:
    view_id: str
    subject: str
    statement: str
    cited_native_ids: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ProceduralTermination:
    run_id: str
    outcome: Literal["completed", "interrupted", "limit_exhausted", "failed"]
    detail: str


@dataclass(frozen=True, slots=True)
class StoppingProposal:
    run_id: str
    explanation: str


type LifecycleValue = (
    DiscoveryObjective
    | InvestigationNeed
    | CapabilityRequest
    | RequestAdmission
    | ExecutionAttempt
    | CapabilityObservation
    | ExecutionInterruption
    | EvaluationOutcome
    | ConsumerView
    | ObservableUse
    | AttributedProposal
    | ProceduralTermination
    | StoppingProposal
)


_OPTIONAL_TEXT = Either((str, type(None)))
_STRINGS = SequenceOf(str)
_METHOD = RecordLayout(
    "lifecycle_method",
    LifecycleMethodIdentity,
    (
        ("owner", str),
        ("method", _OPTIONAL_TEXT),
        ("version", _OPTIONAL_TEXT),
        ("model", _OPTIONAL_TEXT),
        ("contract", _OPTIONAL_TEXT),
        ("configuration", _OPTIONAL_TEXT),
        ("retention_gaps", _STRINGS),
    ),
)
_LAYOUTS = (
    RecordLayout(
        "discovery_objective",
        DiscoveryObjective,
        (
            ("question", str),
            ("scope", str),
            ("decision_relevance", str),
            ("coverage_limit", str),
        ),
    ),
    RecordLayout(
        "investigation_need",
        InvestigationNeed,
        (("proposition_key", str), ("discriminator", str), ("scope", str)),
    ),
    RecordLayout(
        "capability_request",
        CapabilityRequest,
        (("purpose_id", str), ("capability", str), ("scope", str)),
    ),
    RecordLayout(
        "request_admission",
        RequestAdmission,
        (
            ("request_id", str),
            ("outcome", LiteralValues(("admitted", "rejected"))),
            ("policy_id", str),
            ("detail", str),
        ),
    ),
    RecordLayout(
        "execution_attempt",
        ExecutionAttempt,
        (
            ("admission_id", str),
            (
                "state",
                LiteralValues(("intent_recorded", "started", "completion_unknown")),
            ),
        ),
    ),
    RecordLayout(
        "capability_observation",
        CapabilityObservation,
        (
            ("attempt_id", str),
            (
                "outcome",
                LiteralValues(("observed", "empty", "scoped_negative", "problem")),
            ),
            ("scope", str),
            ("detail", str),
        ),
    ),
    RecordLayout(
        "execution_interruption",
        ExecutionInterruption,
        (
            ("attempt_id", str),
            ("problem_kind", str),
            ("completion", LiteralValues(("unknown", "not_started"))),
        ),
    ),
    RecordLayout(
        "evaluation_outcome",
        EvaluationOutcome,
        (
            ("subject_id", str),
            ("outcome", LiteralValues(("evaluated", "unsupported", "failed", "stale"))),
            ("native_assessment_id", _OPTIONAL_TEXT),
            ("detail", str),
        ),
    ),
    RecordLayout(
        "consumer_view",
        ConsumerView,
        (
            ("consumer", str),
            ("delivered_native_ids", _STRINGS),
            ("omitted_native_ids", _STRINGS),
            ("selection_limit", str),
        ),
    ),
    RecordLayout(
        "observable_use",
        ObservableUse,
        (("view_id", str), ("native_ids", _STRINGS), ("receipt", str)),
    ),
    RecordLayout(
        "attributed_proposal",
        AttributedProposal,
        (
            ("view_id", str),
            ("subject", str),
            ("statement", str),
            ("cited_native_ids", _STRINGS),
        ),
    ),
    RecordLayout(
        "procedural_termination",
        ProceduralTermination,
        (
            ("run_id", str),
            (
                "outcome",
                LiteralValues(
                    ("completed", "interrupted", "limit_exhausted", "failed")
                ),
            ),
            ("detail", str),
        ),
    ),
    RecordLayout(
        "stopping_proposal", StoppingProposal, (("run_id", str), ("explanation", str))
    ),
)
_CODEC = NativeValueCodec((_METHOD,) + _LAYOUTS)
_BY_KIND = {layout.variant: layout for layout in _LAYOUTS}
_BY_TYPE = {layout.constructor: layout.variant for layout in _LAYOUTS}

# Observation v1 keeps its exact four-field layout. V2 additionally retains actual
# capability output with a declared non-executing representation; it grants no truth.
_OBSERVATION_V2 = RecordLayout(
    "capability_observation",
    CapabilityObservation,
    next(
        layout.fields
        for layout in _LAYOUTS
        if layout.variant == "capability_observation"
    )
    + (("representation", _OPTIONAL_TEXT), ("retained_content", _OPTIONAL_TEXT)),
)
_CODEC_V2 = NativeValueCodec((_OBSERVATION_V2,))


def encode_method_identity(method: LifecycleMethodIdentity) -> bytes:
    return _CODEC.encode(method, RecordRef("lifecycle_method"))


def decode_method_identity(data: bytes) -> LifecycleMethodIdentity:
    return cast(
        LifecycleMethodIdentity, _CODEC.decode(data, RecordRef("lifecycle_method"))
    )


def encode_lifecycle_value(value: LifecycleValue) -> tuple[str, int, bytes]:
    kind = _BY_TYPE.get(type(value))
    if kind is None:
        raise NativeReconstructionError(
            "unsupported_lifecycle_codec", "Unknown lifecycle value."
        )
    if isinstance(value, CapabilityObservation) and (
        value.representation is not None or value.retained_content is not None
    ):
        return kind, 2, _CODEC_V2.encode(value, RecordRef(kind))
    return kind, 1, _CODEC.encode(value, RecordRef(kind))


def decode_lifecycle_value(kind: str, version: int, payload: bytes) -> LifecycleValue:
    if kind == "capability_observation" and version == 2:
        return cast(LifecycleValue, _CODEC_V2.decode(payload, RecordRef(kind)))
    if version != 1 or kind not in _BY_KIND:
        raise NativeReconstructionError(
            "unsupported_lifecycle_codec", "No supported lifecycle kind/version."
        )
    return cast(LifecycleValue, _CODEC.decode(payload, RecordRef(kind)))


def lifecycle_predecessors(value: LifecycleValue) -> tuple[str, ...]:
    """Representation-owned causal edges; the host still owns current admission."""
    match value:
        case CapabilityRequest(purpose_id=reference):
            return (reference,)
        case RequestAdmission(request_id=reference):
            return (reference,)
        case ExecutionAttempt(admission_id=reference):
            return (reference,)
        case CapabilityObservation(attempt_id=reference):
            return (reference,)
        case ExecutionInterruption(attempt_id=reference):
            return (reference,)
        case EvaluationOutcome(subject_id=reference):
            return (reference,)
        case ObservableUse(view_id=reference) | AttributedProposal(view_id=reference):
            return (reference,)
        case _:
            return ()
