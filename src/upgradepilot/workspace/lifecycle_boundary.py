"""Immutable encoded lifecycle closure composed with versioned native checkpoints.

capture_lifecycle_record retains an attributed value and its original basis. Storage validates
encoded identity/reference closure without running native or semantic evaluators. Separately,
reconstruct_lifecycle_history checks supported typed representations and causal relationships.
Neither function supplies present execution authority, semantic support, or adequacy.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from hashlib import sha256

from .lifecycle_records import (
    AttributedProposal,
    CapabilityObservation,
    CapabilityRequest,
    ConsumerView,
    DiscoveryObjective,
    EvaluationOutcome,
    ExecutionAttempt,
    ExecutionInterruption,
    InvestigationNeed,
    LifecycleMethodIdentity,
    LifecycleValue,
    ObservableUse,
    RequestAdmission,
    StoppingProposal,
    decode_lifecycle_value,
    decode_method_identity,
    encode_lifecycle_value,
    encode_method_identity,
    lifecycle_predecessors,
)
from .native_boundary import CapturedNativeBoundary
from .native_representation import (
    NativeReconstructionError,
    json_bytes,
    object_fields,
    parse_json,
)

MAX_LIFECYCLE_RECORDS = 4096

# Initial typed evaluation links admit assessment-bearing roots from the supported native
# ledger. Raw inputs/requests cannot become an assessment merely by sharing an owner label.
# Broader native/adequacy families need their own tested codec/support expansion.
_NATIVE_ASSESSMENT_FAMILIES = frozenset(
    {
        "ci_coverage",
        "runtime_dependency_state",
        "upstream_authority",
        "upstream_support_drop",
        "python_support_pre_assessment",
        "target_relevance",
        "python_support_post_assessment",
    }
)


@dataclass(frozen=True, slots=True)
class CapturedLifecycleRecord:
    record_id: str
    basis_revision_id: str
    native_record_ids: tuple[str, ...]
    predecessor_record_ids: tuple[str, ...]
    kind: str
    codec_version: int
    payload: bytes
    payload_digest: str
    method: LifecycleMethodIdentity


@dataclass(frozen=True, slots=True)
class CapturedLifecycleHistory:
    """Ordered cumulative history; an explicit empty history differs from missing history."""

    records: tuple[CapturedLifecycleRecord, ...]


@dataclass(frozen=True, slots=True)
class ReconstructedLifecycleRecord:
    capture: CapturedLifecycleRecord
    value: LifecycleValue


def _invalid(detail: str) -> NativeReconstructionError:
    return NativeReconstructionError("invalid_lifecycle_material", detail)


def _text(value: object) -> str:
    if type(value) is not str or not value or len(value) > 4096:
        raise _invalid("Invalid lifecycle identity/label.")
    return value


def _ids(value: object, *, encoded: bool = False) -> tuple[str, ...]:
    if (
        type(value) is not (list if encoded else tuple)
        or len(value) > MAX_LIFECYCLE_RECORDS
    ):
        raise _invalid("Invalid lifecycle reference sequence.")
    values = tuple(_text(item) for item in value)
    if len(set(values)) != len(values):
        raise _invalid("Duplicate lifecycle reference.")
    return values


def capture_lifecycle_record(
    record_id: str,
    basis_revision_id: str,
    value: LifecycleValue,
    *,
    native_record_ids: tuple[str, ...],
    method: LifecycleMethodIdentity,
) -> CapturedLifecycleRecord:
    kind, version, body = encode_lifecycle_value(value)
    record = CapturedLifecycleRecord(
        record_id,
        basis_revision_id,
        native_record_ids,
        lifecycle_predecessors(value),
        kind,
        version,
        body,
        sha256(body).hexdigest(),
        method,
    )
    encode_lifecycle_record(record)
    return record


def encode_lifecycle_record(record: CapturedLifecycleRecord) -> bytes:
    for value in (record.record_id, record.basis_revision_id, record.kind):
        _text(value)
    _ids(record.native_record_ids)
    _ids(record.predecessor_record_ids)
    if type(record.codec_version) is not int or record.codec_version < 1:
        raise _invalid("Invalid lifecycle codec declaration.")
    if (
        type(record.payload) is not bytes
        or sha256(record.payload).hexdigest() != record.payload_digest
    ):
        raise _invalid("Corrupted lifecycle payload.")
    # Check bounds/JSON without dispatching a declared, possibly unsupported kind/codec.
    parse_json(record.payload)
    method = parse_json(encode_method_identity(record.method))
    if not record.method.owner or any(not gap for gap in record.method.retention_gaps):
        raise _invalid("Invalid retained method owner/gap.")
    return json_bytes(
        {
            "record_id": record.record_id,
            "basis_revision_id": record.basis_revision_id,
            "native_record_ids": list(record.native_record_ids),
            "predecessor_record_ids": list(record.predecessor_record_ids),
            "kind": record.kind,
            "codec_version": record.codec_version,
            "payload": record.payload.decode("utf-8"),
            "payload_digest": record.payload_digest,
            "method": method,
        }
    )


def read_lifecycle_record(data: bytes) -> CapturedLifecycleRecord:
    fields = object_fields(
        parse_json(data),
        (
            "record_id",
            "basis_revision_id",
            "native_record_ids",
            "predecessor_record_ids",
            "kind",
            "codec_version",
            "payload",
            "payload_digest",
            "method",
        ),
    )
    if type(fields["payload"]) is not str:
        raise _invalid("Lifecycle payload must be UTF-8 text.")
    record = CapturedLifecycleRecord(
        fields["record_id"],
        fields["basis_revision_id"],
        _ids(fields["native_record_ids"], encoded=True),
        _ids(fields["predecessor_record_ids"], encoded=True),
        fields["kind"],
        fields["codec_version"],
        fields["payload"].encode("utf-8"),
        fields["payload_digest"],
        decode_method_identity(json_bytes(fields["method"])),
    )
    encode_lifecycle_record(record)
    return record


def encode_lifecycle_history(history: CapturedLifecycleHistory) -> bytes:
    if (
        type(history.records) is not tuple
        or len(history.records) > MAX_LIFECYCLE_RECORDS
    ):
        raise _invalid("Unsupported lifecycle history size.")
    return json_bytes(
        {
            "format_version": 1,
            "records": [
                parse_json(encode_lifecycle_record(record))
                for record in history.records
            ],
        }
    )


def validate_lifecycle_history(
    history: CapturedLifecycleHistory,
    *,
    bases: Mapping[str, CapturedNativeBoundary],
) -> None:
    """Validate declared retained bases, not their present validity or semantic truth.

    Storage supplies only the selected revision and its exact-target ancestors from its own
    snapshot. A basis reference cannot point to a future revision or another lineage.
    """
    encode_lifecycle_history(history)
    prior: set[str] = set()
    native_ids = {
        record.record_id for boundary in bases.values() for record in boundary.records
    }
    target = next(iter(bases.values())).target if bases else None
    if any(boundary.target != target for boundary in bases.values()):
        raise _invalid("Lifecycle bases have different exact targets.")
    for record in history.records:
        if record.record_id in prior or record.record_id in native_ids:
            raise _invalid("Colliding lifecycle/native identity.")
        boundary = bases.get(record.basis_revision_id)
        if boundary is None:
            raise _invalid("Missing or non-ancestor lifecycle basis revision.")
        available = {item.record_id for item in boundary.records}
        if not set(record.native_record_ids) <= available:
            raise _invalid("Native references are outside the original basis revision.")
        if not set(record.predecessor_record_ids) <= prior:
            raise _invalid("Missing, forward or cyclic lifecycle predecessor.")
        prior.add(record.record_id)


def reconstruct_lifecycle_history(
    history: CapturedLifecycleHistory,
    *,
    bases: Mapping[str, CapturedNativeBoundary],
) -> tuple[ReconstructedLifecycleRecord, ...]:
    """Expose supported typed history; no capability, native evaluation or policy calls."""
    validate_lifecycle_history(history, bases=bases)
    prior: dict[str, LifecycleValue] = {}
    result = []
    for record in history.records:
        value = decode_lifecycle_value(
            record.kind, record.codec_version, record.payload
        )
        if lifecycle_predecessors(value) != record.predecessor_record_ids:
            raise _invalid(
                "Typed causal references disagree with the encoded envelope."
            )
        parent = (
            prior.get(record.predecessor_record_ids[0])
            if record.predecessor_record_ids
            else None
        )
        if isinstance(value, CapabilityRequest) and not isinstance(
            parent, (InvestigationNeed, DiscoveryObjective)
        ):
            raise _invalid(
                "A capability request needs an objective or investigation need."
            )
        if isinstance(value, RequestAdmission) and not isinstance(
            parent, CapabilityRequest
        ):
            raise _invalid("Admission has no retained request.")
        if isinstance(value, ExecutionAttempt) and (
            not isinstance(parent, RequestAdmission) or parent.outcome != "admitted"
        ):
            raise _invalid(
                "An attempt cannot derive from rejected or absent admission."
            )
        if isinstance(value, CapabilityObservation) and not isinstance(
            parent, ExecutionAttempt
        ):
            raise _invalid("Observation has no retained execution attempt.")
        if isinstance(value, CapabilityObservation):
            admission = prior[parent.admission_id]
            request = prior[admission.request_id]
            if value.scope != request.scope:
                raise _invalid("Observation has another admitted request scope.")
            if (value.representation is None) != (value.retained_content is None):
                raise _invalid(
                    "Retained capability content needs its representation identity."
                )
        if isinstance(value, ExecutionInterruption) and not isinstance(
            parent, ExecutionAttempt
        ):
            raise _invalid("Interruption has no retained execution attempt.")
        if isinstance(value, EvaluationOutcome):
            if not isinstance(
                parent,
                (
                    CapabilityObservation,
                    AttributedProposal,
                    InvestigationNeed,
                    StoppingProposal,
                ),
            ):
                raise _invalid("Evaluation has no retained subject.")
            if isinstance(parent, StoppingProposal) and value.outcome == "evaluated":
                raise _invalid(
                    "This codec has no admitted canonical adequacy assessment."
                )
            if (value.outcome == "evaluated") != (
                value.native_assessment_id is not None
            ):
                raise _invalid(
                    "Evaluation outcome and native assessment presence disagree."
                )
            if value.native_assessment_id is not None:
                native = {
                    item.record_id: item
                    for item in bases[record.basis_revision_id].records
                }
                assessment = native.get(value.native_assessment_id)
                if (
                    value.native_assessment_id not in record.native_record_ids
                    or assessment is None
                    or assessment.outcome != "recorded"
                    or assessment.owner != record.method.owner
                    or assessment.family not in _NATIVE_ASSESSMENT_FAMILIES
                ):
                    raise _invalid(
                        "Native assessment is outside the recorded evaluator basis."
                    )
        if isinstance(value, ConsumerView):
            _ids(value.delivered_native_ids)
            _ids(value.omitted_native_ids)
            if set(value.delivered_native_ids) & set(value.omitted_native_ids):
                raise _invalid("View marks the same material delivered and omitted.")
            if not set(value.delivered_native_ids + value.omitted_native_ids) <= set(
                record.native_record_ids
            ):
                raise _invalid("View material is outside its retained basis.")
        if isinstance(value, (ObservableUse, AttributedProposal)):
            if not isinstance(parent, ConsumerView):
                raise _invalid("Use/proposal has no retained view.")
            references = (
                value.native_ids
                if isinstance(value, ObservableUse)
                else value.cited_native_ids
            )
            _ids(references)
            if not set(references) <= set(record.native_record_ids):
                raise _invalid("Use/citations are outside the retained basis.")
            if isinstance(value, ObservableUse) and not set(references) <= set(
                parent.delivered_native_ids
            ):
                raise _invalid("Observable use cannot claim undelivered material.")
        prior[record.record_id] = value
        result.append(ReconstructedLifecycleRecord(record, value))
    return tuple(result)
