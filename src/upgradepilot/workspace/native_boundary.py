"""Immutable encoded native capture boundary and storage-independent inspection.

``read_native_boundary`` validates format, exact target, digests and reference closure.
It does not dispatch native decoders. Thus unsupported unrelated codecs remain inspectable;
``native_projection`` separately refuses the affected typed consumer. These functions are
for admitted host capture/storage, not authentication of arbitrary imported checkpoints.
This boundary has no publication/continuation promise until the persistence owner proves it.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from typing import Literal

from ..dependency.change import DependencyChangeProblem, DependencyVersionChange
from ..github.pull_request import PullRequestIdentity
from .native_representation import (
    NativeReconstructionError,
    json_bytes,
    object_fields,
    parse_json,
)


@dataclass(frozen=True, slots=True)
class ExactInvestigationTarget:
    repository: str
    pull_number: int
    base_sha: str
    head_sha: str
    normalized_package: str | None
    old_version: str | None
    proposed_version: str | None


def exact_investigation_target(
    pull_request: PullRequestIdentity,
    dependency: DependencyVersionChange | DependencyChangeProblem,
) -> ExactInvestigationTarget:
    transition = isinstance(dependency, DependencyVersionChange)
    return ExactInvestigationTarget(
        pull_request.repository,
        pull_request.number,
        pull_request.base_sha,
        pull_request.head_sha,
        dependency.normalized_package if transition else None,
        dependency.old_version if transition else None,
        dependency.proposed_version if transition else None,
    )


@dataclass(frozen=True, slots=True)
class CapturedNativeRecord:
    """Scoped identity is separate from payload digest and from material references."""

    record_id: str
    family: str
    owner: str
    codec_version: int
    target: ExactInvestigationTarget
    input_record_ids: tuple[str, ...]
    payload: bytes
    payload_digest: str
    outcome: Literal["recorded", "not_evaluated"]
    producer_method: str | None
    producer_version: str | None
    retention_gaps: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class CapturedNativeBoundary:
    target: ExactInvestigationTarget
    records: tuple[CapturedNativeRecord, ...]


_TARGET_FIELDS = (
    "repository",
    "pull_number",
    "base_sha",
    "head_sha",
    "normalized_package",
    "old_version",
    "proposed_version",
)
_RECORD_FIELDS = (
    "record_id",
    "family",
    "owner",
    "codec_version",
    "target",
    "input_record_ids",
    "payload",
    "payload_digest",
    "outcome",
    "producer_method",
    "producer_version",
    "retention_gaps",
)


def _invalid(detail: str) -> NativeReconstructionError:
    return NativeReconstructionError("invalid_native_material", detail)


def _target_object(target: ExactInvestigationTarget) -> dict[str, object]:
    return {name: getattr(target, name) for name in _TARGET_FIELDS}


def _read_target(value: object) -> ExactInvestigationTarget:
    fields = object_fields(value, _TARGET_FIELDS)
    for name in ("repository", "base_sha", "head_sha"):
        if type(fields[name]) is not str or not fields[name]:
            raise _invalid(f"Invalid exact target {name}.")
    if type(fields["pull_number"]) is not int or fields["pull_number"] <= 0:
        raise _invalid("Invalid pull-request number.")
    transition = [
        fields[name]
        for name in ("normalized_package", "old_version", "proposed_version")
    ]
    if not (
        all(item is None for item in transition)
        or all(type(item) is str and item for item in transition)
    ):
        raise _invalid("Dependency transition must be complete or explicitly absent.")
    return ExactInvestigationTarget(**fields)


def _strings(value: object) -> tuple[str, ...]:
    if type(value) is not list or any(
        type(item) is not str or not item for item in value
    ):
        raise _invalid("Expected an ordered string array.")
    return tuple(value)


def _payload_text(payload: bytes) -> str:
    try:
        return payload.decode("utf-8")
    except UnicodeError as error:
        raise _invalid(
            "Native boundary format 1 requires UTF-8 encoded payloads."
        ) from error


def _payload_bytes(payload: str) -> bytes:
    try:
        return payload.encode("utf-8")
    except UnicodeError as error:
        raise _invalid(
            "Native boundary payload contains invalid UTF-8 text."
        ) from error


def validate_native_boundary(
    boundary: CapturedNativeBoundary, *, expected_target: ExactInvestigationTarget
) -> dict[str, CapturedNativeRecord]:
    """Validate one complete encoded boundary before any native projection is exposed."""

    _read_target(_target_object(boundary.target))
    if boundary.target != expected_target:
        raise NativeReconstructionError(
            "wrong_target", "Retained boundary belongs to another exact target."
        )
    records: dict[str, CapturedNativeRecord] = {}
    ids: set[str] = set()
    for record in boundary.records:
        for name in ("record_id", "family", "owner", "payload_digest"):
            if type(getattr(record, name)) is not str or not getattr(record, name):
                raise _invalid(f"Invalid record {name}.")
        if type(record.codec_version) is not int or record.codec_version < 1:
            raise _invalid("Invalid codec version declaration.")
        if record.outcome not in ("recorded", "not_evaluated"):
            raise _invalid("Invalid retained evaluation outcome.")
        for value in (record.input_record_ids, record.retention_gaps):
            if type(value) is not tuple or any(
                type(item) is not str or not item for item in value
            ):
                raise _invalid("Invalid immutable reference/gap sequence.")
        for value in (record.producer_method, record.producer_version):
            if value is not None and (type(value) is not str or not value):
                raise _invalid("Invalid retained method metadata.")
        if record.target != boundary.target:
            raise NativeReconstructionError(
                "wrong_target", "Record is outside the declared exact target."
            )
        if not record.record_id or record.record_id in ids or record.family in records:
            raise _invalid("Duplicate record identity or native family.")
        if (
            type(record.payload) is not bytes
            or sha256(record.payload).hexdigest() != record.payload_digest
        ):
            raise _invalid(f"Corrupted native payload {record.family!r}.")
        if len(set(record.input_record_ids)) != len(record.input_record_ids):
            raise _invalid("Duplicate material reference.")
        records[record.family] = record
        ids.add(record.record_id)
    for record in boundary.records:
        if any(
            reference not in ids or reference == record.record_id
            for reference in record.input_record_ids
        ):
            raise NativeReconstructionError(
                "missing_native_material",
                f"Broken material closure for {record.family!r}.",
            )
    # A reference cycle has no grounded input boundary; reject rather than merging histories.
    by_id = {record.record_id: record for record in boundary.records}
    completed: set[str] = set()

    def visit(record_id: str, ancestors: frozenset[str]) -> None:
        if record_id in completed:
            return
        if record_id in ancestors:
            raise _invalid("Cyclic material references.")
        if len(ancestors) > 64:
            raise _invalid("Material reference depth exceeds supported inspection.")
        for reference in by_id[record_id].input_record_ids:
            visit(reference, ancestors | {record_id})
        completed.add(record_id)

    for record_id in by_id:
        visit(record_id, frozenset())
    return records


def encode_native_boundary(boundary: CapturedNativeBoundary) -> bytes:
    validate_native_boundary(boundary, expected_target=boundary.target)
    return json_bytes(
        {
            "format_version": 1,
            "target": _target_object(boundary.target),
            "records": [
                {
                    "record_id": record.record_id,
                    "family": record.family,
                    "owner": record.owner,
                    "codec_version": record.codec_version,
                    "target": _target_object(record.target),
                    "input_record_ids": list(record.input_record_ids),
                    "payload": _payload_text(record.payload),
                    "payload_digest": record.payload_digest,
                    "outcome": record.outcome,
                    "producer_method": record.producer_method,
                    "producer_version": record.producer_version,
                    "retention_gaps": list(record.retention_gaps),
                }
                for record in boundary.records
            ],
        }
    )


def read_native_boundary(
    payload: bytes, *, expected_target: ExactInvestigationTarget
) -> CapturedNativeBoundary:
    fields = object_fields(parse_json(payload), ("format_version", "target", "records"))
    if type(fields["format_version"]) is not int or fields["format_version"] != 1:
        raise NativeReconstructionError(
            "unsupported_capture_format", "No supported native boundary format."
        )
    target = _read_target(fields["target"])
    if type(fields["records"]) is not list:
        raise _invalid("Missing native record array.")
    records = []
    for value in fields["records"]:
        item = object_fields(value, _RECORD_FIELDS)
        for name in ("record_id", "family", "owner", "payload_digest"):
            if type(item[name]) is not str or not item[name]:
                raise _invalid(f"Invalid record {name}.")
        for name in ("producer_method", "producer_version"):
            if item[name] is not None and (
                type(item[name]) is not str or not item[name]
            ):
                raise _invalid(f"Invalid record {name}.")
        if type(item["codec_version"]) is not int or item["codec_version"] < 1:
            raise _invalid("Invalid codec version declaration.")
        if (
            item["outcome"] not in ("recorded", "not_evaluated")
            or type(item["payload"]) is not str
        ):
            raise _invalid("Invalid retained outcome/payload.")
        records.append(
            CapturedNativeRecord(
                record_id=item["record_id"],
                family=item["family"],
                owner=item["owner"],
                codec_version=item["codec_version"],
                target=_read_target(item["target"]),
                input_record_ids=_strings(item["input_record_ids"]),
                payload=_payload_bytes(item["payload"]),
                payload_digest=item["payload_digest"],
                outcome=item["outcome"],
                producer_method=item["producer_method"],
                producer_version=item["producer_version"],
                retention_gaps=_strings(item["retention_gaps"]),
            )
        )
    boundary = CapturedNativeBoundary(target, tuple(records))
    validate_native_boundary(boundary, expected_target=expected_target)
    return boundary
