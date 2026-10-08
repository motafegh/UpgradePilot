"""Disposable revision/retention comparison; no production Workspace or persistence.

Trace records contain immutable payload bytes and explicit material dependencies. Native
payloads retain every inspected dataclass field/type; lifecycle payloads are simulations.
Neither this graph nor its JSON reader evaluates evidence or hydrates trusted native types.
Read the experiment corpus for capture ownership, and the runner for measurements.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping
from dataclasses import dataclass, fields, is_dataclass, replace
from datetime import datetime
from types import MappingProxyType

from packaging.version import Version


def encode_fields(value: object) -> bytes:
    """Pinned experiment encoding, not a stable native migration/rehydration codec."""

    def encode(item):
        if is_dataclass(item) and not isinstance(item, type):
            return {
                "type": f"{type(item).__module__}.{type(item).__qualname__}",
                "fields": {
                    field.name: encode(getattr(item, field.name))
                    for field in fields(item)
                },
            }
        if isinstance(item, tuple):
            return {"tuple": [encode(element) for element in item]}
        if isinstance(item, list):
            return [encode(element) for element in item]
        if isinstance(item, dict) and all(type(key) is str for key in item):
            return {key: encode(element) for key, element in item.items()}
        if isinstance(item, (datetime, Version)):
            return {"type": type(item).__name__, "value": str(item)}
        if item is None or type(item) in (str, int, bool):
            return item
        raise TypeError(f"Uninspected payload type: {type(item).__name__}")

    return json.dumps(encode(value), sort_keys=True, ensure_ascii=False).encode("utf-8")


@dataclass(frozen=True, slots=True)
class TraceRecord:
    record_id: str
    owner: str
    kind: str
    scope: str
    payload: bytes | None
    dependencies: tuple[str, ...] = ()
    gap: str | None = None

    def __post_init__(self):
        for value in (self.record_id, self.owner, self.kind, self.scope):
            if type(value) is not str or not value:
                raise ValueError("Record identity/owner/kind/scope must be explicit")
        if type(self.dependencies) is not tuple or any(
            type(value) is not str or not value for value in self.dependencies
        ):
            raise ValueError("Material references must be immutable named identities")
        if self.payload is not None and type(self.payload) is not bytes:
            raise ValueError("Payload must be immutable bytes")
        if (self.payload is None) != (self.gap is not None):
            raise ValueError(
                "Missing content requires an explicit gap, retained content has none"
            )
        if self.gap is not None and (type(self.gap) is not str or not self.gap):
            raise ValueError("Gap reason must be explicit")

    @property
    def digest(self):
        return (
            None if self.payload is None else hashlib.sha256(self.payload).hexdigest()
        )


@dataclass(frozen=True, slots=True)
class PublishedRevision:
    lineage: str
    number: int
    predecessor: int | None
    target: bytes
    roots: tuple[str, ...]
    records: Mapping[str, TraceRecord]
    triggering_records: tuple[str, ...] = ()


def material_closure(revision: PublishedRevision) -> tuple[str, ...]:
    """Follow declared material edges; completeness of their declaration is an oracle duty."""
    visited = set()
    pending = list(revision.roots)
    while pending:
        key = pending.pop()
        if key in visited:
            continue
        if key not in revision.records:
            raise ValueError(f"Broken material reference: {key}")
        visited.add(key)
        pending.extend(revision.records[key].dependencies)
    return tuple(sorted(visited))


def retention_gaps(revision: PublishedRevision) -> dict[str, str]:
    return {
        key: revision.records[key].gap
        for key in material_closure(revision)
        if revision.records[key].gap is not None
    }


def _admit(existing, additions):
    updates = {}
    for record in additions:
        previous = updates.get(record.record_id, existing.get(record.record_id))
        if previous is not None and previous != record:
            raise ValueError(f"Identity/content/scope collision: {record.record_id}")
        updates[record.record_id] = record
    if any(record.kind == "source_text" for record in updates.values()):
        exact_sources = {
            record.scope: record
            for record in existing.values()
            if record.kind == "source_text"
        }
        for record in updates.values():
            if record.kind != "source_text":
                continue
            previous = exact_sources.get(record.scope)
            if previous is not None and previous.payload != record.payload:
                raise ValueError(
                    f"Exact source identity/content collision: {record.scope}"
                )
            exact_sources[record.scope] = record
    return updates


def _freeze(lineage, number, target, roots, records, triggers=()):
    frozen = PublishedRevision(
        lineage,
        number,
        number - 1 if number else None,
        target,
        tuple(roots),
        MappingProxyType(records),
        tuple(triggers),
    )
    closure = set(material_closure(frozen))
    # Discardable diagnostic edits do not become material history dependencies.
    return replace(
        frozen, triggering_records=tuple(key for key in triggers if key in closure)
    )


class ImmutableSuccessorHistory:
    """Build successors by copying the record index, sharing immutable payloads."""

    def __init__(self, target: bytes, lineage: str = "offline-comparison"):
        self.history = [_freeze(lineage, 0, target, (), {})]

    def publish(self, additions, roots):
        previous = self.history[-1]
        updates = _admit(previous.records, additions)
        records = dict(previous.records)
        records.update(updates)
        revision = _freeze(
            previous.lineage,
            previous.number + 1,
            previous.target,
            roots,
            records,
            tuple(updates),
        )
        self.history.append(revision)
        return revision


class MutableDraftHistory:
    """Stage index edits; freeze publication and roll back invalid drafts.

    Old revisions never expose the draft dictionary. It is intentionally single-threaded;
    transaction/locking and crash publication belong to later research.
    """

    def __init__(self, target: bytes, lineage: str = "offline-comparison"):
        self.draft = {}
        self.pending = {}
        self.history = [_freeze(lineage, 0, target, (), {})]

    def stage(self, additions):
        """Unpublished drafts are not canonical revisions or recoverable checkpoints."""
        updates = _admit(self.draft, additions)
        self.draft.update(updates)
        self.pending.update(updates)

    def publish_pending(self, roots):
        previous = self.history[-1]
        try:
            revision = _freeze(
                previous.lineage,
                previous.number + 1,
                previous.target,
                roots,
                dict(self.draft),
                tuple(self.pending),
            )
        except ValueError:
            self.draft = dict(previous.records)
            self.pending.clear()
            raise
        self.history.append(revision)
        self.pending.clear()
        return revision

    def publish(self, additions, roots):
        self.stage(additions)
        return self.publish_pending(roots)


def encode_checkpoint(revision: PublishedRevision) -> bytes:
    """Encode only the declared closure, not every unreferenced record in memory."""
    records = []
    for key in material_closure(revision):
        record = revision.records[key]
        records.append(
            {
                "id": key,
                "owner": record.owner,
                "kind": record.kind,
                "scope": record.scope,
                "payload": None
                if record.payload is None
                else record.payload.decode("utf-8"),
                "dependencies": list(record.dependencies),
                "gap": record.gap,
                "digest": record.digest,
            }
        )
    body = {
        "schema": "experiment.workspace-material-closure",
        "version": 1,
        "native_encoding": "pinned-tagged-fields-v1-no-rehydration",
        "lineage": revision.lineage,
        "revision": revision.number,
        "predecessor": revision.predecessor,
        "triggering_records": list(revision.triggering_records),
        "target": revision.target.decode("utf-8"),
        "roots": list(revision.roots),
        "records": records,
    }
    return json.dumps(body, sort_keys=True, ensure_ascii=False).encode("utf-8")


def decode_checkpoint(data: bytes) -> PublishedRevision:
    """In-memory structural round trip only; no external calls or trusted-object import."""
    body = json.loads(data)
    if (
        body["schema"] != "experiment.workspace-material-closure"
        or type(body["version"]) is not int
        or body["version"] != 1
    ):
        raise ValueError("Unsupported experiment schema")
    if body["native_encoding"] != "pinned-tagged-fields-v1-no-rehydration":
        raise ValueError("Unsupported native encoding")
    number = body["revision"]
    if (
        type(number) is not int
        or number < 0
        or (number and type(body["predecessor"]) is not int)
        or body["predecessor"] != (number - 1 if number else None)
    ):
        raise ValueError("Invalid revision lineage")
    records = {}
    for entry in body["records"]:
        record = TraceRecord(
            entry["id"],
            entry["owner"],
            entry["kind"],
            entry["scope"],
            None if entry["payload"] is None else entry["payload"].encode("utf-8"),
            tuple(entry["dependencies"]),
            entry["gap"],
        )
        if record.record_id in records or record.digest != entry["digest"]:
            raise ValueError("Duplicate record or payload digest mismatch")
        records[record.record_id] = record
    _admit({}, records.values())
    revision = _freeze(
        body["lineage"],
        number,
        body["target"].encode("utf-8"),
        body["roots"],
        records,
        tuple(body["triggering_records"]),
    )
    if revision.triggering_records != tuple(body["triggering_records"]):
        raise ValueError("Broken material trigger reference")
    if set(material_closure(revision)) != set(records):
        raise ValueError("Checkpoint contains undeclared material")
    return revision


def affected_dependents(
    revision: PublishedRevision, changed_ids: set[str]
) -> tuple[str, ...]:
    """Experiment dependency invalidation, not semantic reevaluation/staleness adjudication."""
    affected = set(changed_ids)
    while True:
        more = {
            key
            for key in material_closure(revision)
            if set(revision.records[key].dependencies) & affected
        } - affected
        if not more:
            return tuple(sorted(affected - changed_ids))
        affected.update(more)
