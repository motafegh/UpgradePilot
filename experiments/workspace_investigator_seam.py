"""Experiment-only typed Investigator seam; no storage engine or native truth owner.

START HERE: read -> request -> host admission -> start -> observe -> native bridge.
This host retains interaction/binding history and explicit unsupported outcomes. Callers
cannot supply admission, evaluator truth or permission. CheckpointPort is host-internal;
restoration is historical until explicit current-policy validation. Full trace retention
is a disclosed experiment choice, not a product retention policy or migration codec.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from types import MappingProxyType
from typing import Protocol

from experiments.workspace_revision_representation import PublishedRevision, TraceRecord


def json_bytes(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False).encode()


def payload(record):
    return None if record.payload is None else json.loads(record.payload)


def _text(value):
    if type(value) is not str or not value:
        raise ValueError("Explicit nonempty string required")


@dataclass(frozen=True, slots=True)
class RevisionRef:
    lineage: str
    number: int
    target: str

    def __post_init__(self):
        _text(self.lineage)
        _text(self.target)
        if type(self.number) is not int or self.number < 0:
            raise ValueError("Revision number must be a nonnegative integer")


@dataclass(frozen=True, slots=True)
class Binding:
    slot: str
    record_id: str

    def __post_init__(self):
        _text(self.slot)
        _text(self.record_id)


@dataclass(frozen=True, slots=True)
class AcquisitionRequest:
    request_id: str
    revision: RevisionRef
    basis: tuple[Binding, ...]
    capability: str
    scope: str
    method: str
    discriminator: str

    def __post_init__(self):
        for name in ("request_id", "capability", "scope", "method", "discriminator"):
            _text(getattr(self, name))
        if not self.request_id.startswith("investigator:"):
            raise ValueError("Investigator identity must not impersonate host records")
        if type(self.revision) is not RevisionRef or type(self.basis) is not tuple:
            raise ValueError("Typed revision and immutable basis required")
        if (
            not self.basis
            or len(self.basis) > 64
            or any(type(item) is not Binding for item in self.basis)
        ):
            raise ValueError("Explicit bounded material bindings required")
        if len({item.slot for item in self.basis}) != len(self.basis):
            raise ValueError("Repeated material slot")


def encode_request(request: AcquisitionRequest) -> bytes:
    """Transport envelope has no authority, store identity or execution result fields."""
    return json_bytes(asdict(request))


def decode_request(data: bytes) -> AcquisitionRequest:
    """Bounded, non-executing strict parser; Python and wire share typed admission."""
    if type(data) is not bytes or len(data) > 65_536:
        raise ValueError("Request envelope exceeds bounded bytes")

    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("Repeated envelope field")
            result[key] = value
        return result

    item = json.loads(data, object_pairs_hook=unique)
    if type(item) is not dict or set(item) != set(
        AcquisitionRequest.__dataclass_fields__
    ):
        raise ValueError("Unknown/missing request fields; authority cannot be supplied")
    if type(item["revision"]) is not dict or set(item["revision"]) != {
        "lineage",
        "number",
        "target",
    }:
        raise ValueError("Exact revision envelope required")
    basis = item["basis"]
    if (
        type(basis) is not list
        or not 0 < len(basis) <= 64
        or any(
            type(entry) is not dict or set(entry) != {"slot", "record_id"}
            for entry in basis
        )
    ):
        raise ValueError("Exact bounded material bindings required")
    return AcquisitionRequest(
        **{
            key: value
            for key, value in item.items()
            if key not in ("revision", "basis")
        },
        revision=RevisionRef(**item["revision"]),
        basis=tuple(Binding(**entry) for entry in basis),
    )


@dataclass(frozen=True, slots=True)
class HostPolicy:
    """Current host authority, supplied independently of historical checkpoints."""

    target: str
    method: str
    capabilities: frozenset[str]
    authorized: bool
    scope: str
    discriminator: str


@dataclass(frozen=True, slots=True)
class Outcome:
    status: str
    records: tuple[str, ...] = ()
    detail: str = ""


@dataclass(frozen=True, slots=True)
class Projection:
    revision: RevisionRef
    view_id: str
    delivered: tuple[TraceRecord, ...]
    omitted_but_addressable: tuple[str, ...]
    basis: tuple[Binding, ...]
    method: str
    capabilities: tuple[str, ...]
    continuation: str
    adequacy: str = "unsupported_no_admitted_evaluator"


def encode_projection(view: Projection) -> bytes:
    """Lossless disclosed UTF-8 projection for the scripted wire consumer.

    This does not hydrate native domain objects or establish examination/evaluation.
    A transport-specific response decoder is outside this in-process sketch.
    """
    return json_bytes(
        {
            "revision": asdict(view.revision),
            "view_id": view.view_id,
            "delivered": [
                {
                    "id": item.record_id,
                    "owner": item.owner,
                    "kind": item.kind,
                    "scope": item.scope,
                    "content": None if item.payload is None else item.payload.decode(),
                    "material_references": item.dependencies,
                    "gap": item.gap,
                }
                for item in view.delivered
            ],
            "omitted_but_addressable": view.omitted_but_addressable,
            "basis": [asdict(item) for item in view.basis],
            "method": view.method,
            "capabilities": view.capabilities,
            "continuation": view.continuation,
            "adequacy": view.adequacy,
        }
    )


class CheckpointUnavailable(Exception):
    """Host publication/recovery could not be confirmed; never an execution result."""


class CheckpointPort(Protocol):
    """Private host persistence; its implementation never reaches Investigator values."""

    def load(self) -> PublishedRevision | None: ...
    def save(self, revision: PublishedRevision, expected: int) -> bool: ...


class WorkspaceHost:
    """Small lifecycle sketch; a host-controlled registry owns scopes and bindings.

    `seed`, `rebind`, `retain_evidence` and `publish_evaluation` are host/native bridge
    operations, not Investigator permissions. InvestigatorPort exposes read/request/
    propose only; start/observe stand in for a separate admitted capability driver.
    """

    def __init__(self, port: CheckpointPort, policy: HostPolicy):
        self.port = port
        self.policy = policy
        self.revision = port.load()
        self.active = False  # Recovery and even fresh creation grant no authority.

    @property
    def ref(self):
        revision = self.revision
        return RevisionRef(revision.lineage, revision.number, revision.target.decode())

    @property
    def state(self):
        return payload(self.revision.records[f"workspace:state:{self.revision.number}"])

    @property
    def basis(self):
        return tuple(
            Binding(key, value) for key, value in sorted(self.state["bindings"].items())
        )

    def seed(self, records, bindings, *, lineage="offline-seam"):
        if self.revision is not None:
            raise ValueError(
                "Existing lineage cannot be reseeded or rebound to a target"
            )
        context = TraceRecord(
            "workspace:context:0",
            "experiment.host",
            "basis",
            self.policy.target,
            json_bytes([]),
        )
        return self._publish(
            (*records, context),
            {
                "bindings": {**bindings, "context": context.record_id},
                "evidence": [],
                "need_status": "material_non_final",
            },
            lineage=lineage,
        )

    def refresh(self):
        self.revision = self.port.load()
        self.active = False
        return Outcome("historical_only")

    def continue_current(self):
        self.active = False
        if self.policy.target != self.ref.target:
            return Outcome("target_changed")
        if not self.policy.authorized:
            return Outcome("authority_unavailable")
        for binding in self.basis:
            if self.revision.records[binding.record_id].payload is None:
                return Outcome("missing_material_content", (binding.record_id,))
        self.active = True
        return Outcome("current_bindings_validated")

    def _publish(self, additions, state=None, *, lineage=None):
        old = self.revision
        number = 0 if old is None else old.number + 1
        records = {} if old is None else dict(old.records)
        for record in additions:
            previous = records.get(record.record_id)
            if previous is not None and previous != record:
                raise ValueError("Immutable record identity/content/scope collision")
            if record.kind == "source_text" and any(
                other.kind == "source_text"
                and other.scope == record.scope
                and other.payload != record.payload
                for other in records.values()
            ):
                raise ValueError("Exact source scope/content collision")
            records[record.record_id] = record
        next_state = state if state is not None else self.state
        state_record = TraceRecord(
            f"workspace:state:{number}",
            "experiment.host",
            "state",
            self.policy.target if old is None else self.ref.target,
            json_bytes(next_state),
            tuple(records),
        )
        records[state_record.record_id] = state_record
        revision = PublishedRevision(
            lineage if old is None else old.lineage,
            number,
            None if old is None else old.number,
            self.policy.target.encode() if old is None else old.target,
            (state_record.record_id,),
            MappingProxyType(records),
            tuple(record.record_id for record in additions) + (state_record.record_id,),
        )
        try:
            saved = self.port.save(revision, -1 if old is None else old.number)
        except CheckpointUnavailable:
            self.active = False
            return Outcome(
                "publication_unconfirmed",
                detail="Inspect/refresh historical state, then explicitly revalidate; no implicit retry",
            )
        if not saved:
            self.active = False
            return Outcome(
                "publication_conflict",
                detail="Refresh and revalidate; no implicit retry",
            )
        self.revision = revision
        return Outcome("published", tuple(record.record_id for record in additions))

    def _event(self, kind, values, dependencies=()):
        return TraceRecord(
            f"workspace:{kind}:{self.revision.number + 1}",
            "experiment.host",
            kind,
            self.ref.target,
            json_bytes(values),
            tuple(dependencies),
        )

    def _problem(self, status, values, dependencies=()):
        record = self._event("problem", {"status": status, **values}, dependencies)
        outcome = self._publish((record,))
        return (
            Outcome(status, (record.record_id,))
            if outcome.status == "published"
            else outcome
        )

    def read(self, record_ids: tuple[str, ...]) -> Projection | Outcome:
        if len(set(record_ids)) != len(record_ids) or any(
            key not in self.revision.records
            or self.revision.records[key].kind == "state"
            for key in record_ids
        ):
            return self._problem(
                "unknown_or_repeated_reference", {"requested": record_ids}
            )
        ref = self.ref
        basis = self.basis
        delivered = tuple(self.revision.records[key] for key in record_ids)
        omitted = tuple(
            sorted(
                key
                for key, record in self.revision.records.items()
                if record.kind != "state" and key not in record_ids
            )
        )
        view = self._event(
            "view",
            {
                "revision": asdict(ref),
                "delivered": record_ids,
                "omitted_but_addressable": omitted,
                "examined_or_used": "unknown",
                "basis": [asdict(item) for item in basis],
                "method": self.policy.method,
            },
            record_ids,
        )
        outcome = self._publish((view,))
        if outcome.status != "published":
            return outcome
        return Projection(
            ref,
            view.record_id,
            delivered,
            omitted,
            basis,
            self.policy.method,
            tuple(sorted(self.policy.capabilities)),
            "current"
            if self.active
            and self.policy.authorized
            and self.policy.target == self.ref.target
            else "historical_only",
        )

    def _validate(self, request):
        if (
            request.revision.target != self.ref.target
            or self.policy.target != self.ref.target
        ):
            return "target_changed"
        if (
            request.revision.lineage != self.ref.lineage
            or request.revision.number > self.ref.number
        ):
            return "unknown_revision"
        if request.method != self.policy.method:
            return "method_changed"
        if request.capability not in self.policy.capabilities:
            return "capability_unavailable"
        if not self.active or not self.policy.authorized:
            return "current_authority_unavailable"
        if request.basis != self.basis:
            return "material_basis_changed"
        original = payload(
            self.revision.records[f"workspace:state:{request.revision.number}"]
        )
        if {item.slot: item.record_id for item in request.basis} != original[
            "bindings"
        ]:
            return "basis_not_in_original_revision"
        if any(
            self.revision.records[item.record_id].payload is None
            for item in request.basis
        ):
            return "missing_material_content"
        if self.state["need_status"] != "material_non_final":
            return "no_current_material_need"
        if (
            request.scope != self.policy.scope
            or request.discriminator != self.policy.discriminator
        ):
            return "request_meaning_or_scope_rejected"
        return "valid"

    def request(
        self, request: AcquisitionRequest, *, principal="scripted-investigator"
    ):
        if type(request) is not AcquisitionRequest:
            raise ValueError("Only a typed attributed request is accepted")
        previous = self.revision.records.get(request.request_id)
        encoded = encode_request(request)
        if previous is not None:
            if previous.payload != encoded:
                return self._problem(
                    "identity_content_collision", {"request_id": request.request_id}
                )
            return Outcome("duplicate_request", (request.request_id,))
        status = self._validate(request)
        record = TraceRecord(
            request.request_id,
            principal,
            "request",
            self.ref.target,
            encoded,
            tuple(item.record_id for item in request.basis),
        )
        admission = self._event(
            "admission",
            {
                "request_id": request.request_id,
                "status": "admitted" if status == "valid" else status,
                "method": self.policy.method,
                "principal": principal,
            },
            (record.record_id,),
        )
        outcome = self._publish((record, admission))
        return (
            Outcome(
                "admitted" if status == "valid" else status,
                (record.record_id, admission.record_id),
            )
            if outcome.status == "published"
            else outcome
        )

    def _request(self, request_id):
        record = self.revision.records.get(request_id)
        return (
            None
            if record is None or record.kind != "request"
            else decode_request(record.payload)
        )

    def start(self, request_id):
        request = self._request(request_id)
        if request is None:
            return self._problem("unknown_request", {"request_id": request_id})
        attempt_id = f"attempt:{request_id}"
        if attempt_id in self.revision.records:
            completed = f"completion:{request_id}" in self.revision.records
            return Outcome(
                "already_completed"
                if completed
                else "completion_unknown_no_auto_retry",
                (attempt_id,),
            )
        admissions = [
            record
            for record in self.revision.records.values()
            if record.kind == "admission"
            and payload(record)["request_id"] == request_id
        ]
        status = self._validate(request)
        if status != "valid" or not any(
            payload(item)["status"] == "admitted" for item in admissions
        ):
            return self._problem(
                status if status != "valid" else "request_not_admitted",
                {"request_id": request_id},
                (request_id,),
            )
        attempt = TraceRecord(
            attempt_id,
            "experiment.host",
            "attempt",
            self.ref.target,
            json_bytes(
                {
                    "request_id": request_id,
                    "completion": "unknown",
                    "retry_permission": None,
                    "admission_id": admissions[0].record_id,
                    "started_revision": asdict(self.ref),
                    "basis": [asdict(item) for item in request.basis],
                    "method": self.policy.method,
                    "capability": request.capability,
                    "scope": request.scope,
                    "current_host_authorization_checked": True,
                }
            ),
            (request_id, admissions[0].record_id),
        )
        return self._publish((attempt,))

    def observe(self, request_id, result: TraceRecord):
        request = self._request(request_id)
        attempt_id = f"attempt:{request_id}"
        if request is None or attempt_id not in self.revision.records:
            return self._problem("no_admitted_attempt", {"request_id": request_id})
        completion_id = f"completion:{request_id}"
        if completion_id in self.revision.records:
            completion = payload(self.revision.records[completion_id])
            if completion.get("result_id") is None:
                return self._problem(
                    "completion_already_recorded", {"request_id": request_id}
                )
            previous = self.revision.records[completion["result_id"]]
            if previous == result:
                return Outcome("duplicate_delivery", (result.record_id, completion_id))
            return self._problem(
                "identity_content_collision",
                {"request_id": request_id, "result_id": result.record_id},
            )
        status = self._validate(request)
        previous = self.revision.records.get(result.record_id)
        same_scope = [
            record
            for record in self.revision.records.values()
            if record.kind == "source_text" and record.scope == result.scope
        ]
        duplicate_known = previous == result or any(
            record.owner == result.owner
            and record.kind == result.kind
            and record.payload == result.payload
            and record.dependencies == result.dependencies
            for record in same_scope
        )
        if duplicate_known and status in {
            "no_current_material_need",
            "material_basis_changed",
        }:
            # A separately admitted attempt can acknowledge already-retained exact data
            # historically; this cannot reopen a need or create additional support.
            status = "valid"
        if (
            previous is not None
            and previous != result
            or any(record.payload != result.payload for record in same_scope)
        ):
            status = "identity_content_collision"
        elif (
            result.kind != "source_text"
            or result.owner != "upgradepilot.github.repository"
            or result.scope != request.scope
            or result.payload is None
            or result.dependencies
            or result.record_id.startswith(
                ("workspace:", "attempt:", "completion:", "proposal:", "investigator:")
            )
        ):
            status = "result_identity_or_meaning_rejected"
        if status != "valid":
            return self._problem(
                status,
                {
                    "request_id": request_id,
                    "rejected_result": {
                        "id": result.record_id,
                        "owner": result.owner,
                        "scope": result.scope,
                        "content": None
                        if result.payload is None
                        else result.payload.decode(),
                    },
                },
                (request_id, attempt_id),
            )
        completion = TraceRecord(
            completion_id,
            "experiment.host",
            "observation",
            self.ref.target,
            json_bytes(
                {
                    "request_id": request_id,
                    "result_id": result.record_id,
                    "original_revision": asdict(request.revision),
                    "method": request.method,
                    "admitted_after_revalidation_at": asdict(self.ref),
                    "delivery_role": "duplicate_known_evidence"
                    if duplicate_known
                    else "new_observation",
                }
            ),
            (request_id, attempt_id, result.record_id),
        )
        state = (
            self.state
            if duplicate_known
            else {
                **self.state,
                "evidence": self.state["evidence"]
                + [
                    {
                        "id": result.record_id,
                        "role": "target_source",
                        "candidate": {b.slot: b.record_id for b in request.basis}[
                            "candidate"
                        ],
                    }
                ],
                "need_status": "owner_revalidation_required",
            }
        )
        outcome = self._publish((result, completion), state)
        return (
            Outcome(
                "duplicate_delivery" if duplicate_known else "observation_admitted",
                (result.record_id, completion_id),
            )
            if outcome.status == "published"
            else outcome
        )

    def attempt_problem(self, request_id, code, *, completion_known):
        """Capability failure is a problem, never a negative domain observation."""
        attempt_id = f"attempt:{request_id}"
        if attempt_id not in self.revision.records:
            return self._problem("no_admitted_attempt", {"request_id": request_id})
        _text(code)
        completion_id = f"completion:{request_id}"
        if completion_id in self.revision.records:
            return Outcome("already_completed", (completion_id,))
        values = {
            "request_id": request_id,
            "problem": code,
            "completion": "failed" if completion_known else "unknown",
            "result_id": None,
            "retry_permission": None,
        }
        if completion_known:
            record = TraceRecord(
                completion_id,
                "experiment.host",
                "attempt_problem",
                self.ref.target,
                json_bytes(values),
                (request_id, attempt_id),
            )
        else:
            record = self._event("attempt_problem", values, (request_id, attempt_id))
        return self._publish((record,))

    def propose(
        self, proposal_id, revision, basis, view_id, citations, claim, *, method=None
    ):
        """Attributed semantic proposal; general semantic evaluation remains unavailable."""
        if not proposal_id.startswith("proposal:") or type(claim) is not str:
            raise ValueError("Proposal attribution/claim required")
        view = self.revision.records.get(view_id)
        method = (
            (None if view is None else payload(view).get("method"))
            if method is None
            else method
        )
        if not self.active or not self.policy.authorized:
            return self._problem(
                "current_authority_unavailable", {"proposal_id": proposal_id}
            )
        if (
            self.policy.target != self.ref.target
            or method != self.policy.method
            or revision.number > self.ref.number
            or revision.target != self.ref.target
            or revision.lineage != self.ref.lineage
            or basis != self.basis
        ):
            return self._problem("proposal_basis_changed", {"proposal_id": proposal_id})
        if (
            view is None
            or view.kind != "view"
            or payload(view)["revision"] != asdict(revision)
            or payload(view)["basis"] != [asdict(item) for item in basis]
            or payload(view)["method"] != method
            or any(key not in payload(view)["delivered"] for key in citations)
        ):
            return self._problem(
                "citation_not_delivered_in_view", {"proposal_id": proposal_id}
            )
        proposal = TraceRecord(
            proposal_id,
            "scripted-investigator",
            "proposal",
            self.ref.target,
            json_bytes(
                {
                    "claim": claim,
                    "revision": asdict(revision),
                    "citations": citations,
                    "examined_or_used": "consumer_asserted",
                    "basis": [asdict(item) for item in basis],
                    "method": method,
                }
            ),
            (view_id, *citations, *(item.record_id for item in basis)),
        )
        if proposal_id in self.revision.records:
            if self.revision.records[proposal_id] == proposal:
                return Outcome("duplicate_proposal", (proposal_id,))
            return self._problem(
                "identity_content_collision", {"proposal_id": proposal_id}
            )
        evaluation = self._event(
            "proposal_evaluation",
            {
                "proposal_id": proposal_id,
                "status": "unsupported_no_admitted_evaluator",
                "assessment": None,
            },
            (proposal_id,),
        )
        outcome = self._publish((proposal, evaluation))
        return (
            Outcome(
                "proposal_retained_evaluation_unsupported",
                (proposal_id, evaluation.record_id),
            )
            if outcome.status == "published"
            else outcome
        )

    def rebind(self, slot, record):
        """Trusted fixture/native-owner update, never a consumer-supplied premise edit."""
        state = {
            **self.state,
            "bindings": {**self.state["bindings"], slot: record.record_id},
        }
        return self._publish((record,), state)

    def retain_evidence(self, record, *, role, candidate):
        state = {
            **self.state,
            "evidence": self.state["evidence"]
            + [{"id": record.record_id, "role": role, "candidate": candidate}],
        }
        additions = [record]
        if (
            role == "counterevidence"
            and candidate == self.state["bindings"]["candidate"]
        ):
            relevant = sorted(
                {
                    item["id"]
                    for item in state["evidence"]
                    if item["candidate"] == candidate
                }
            )
            context = self._event("context", relevant, relevant)
            additions.append(context)
            state = {
                **state,
                "bindings": {**state["bindings"], "context": context.record_id},
                "need_status": "owner_revalidation_required",
            }
        return self._publish(additions, state)

    def evaluation_inputs(self):
        """Host selects all owner-relevant inputs, including omitted counterevidence/gaps."""
        candidate = self.state["bindings"]["candidate"]
        selected = {
            item["id"]
            for item in self.state["evidence"]
            if item["candidate"] == candidate
        }
        return tuple(self.revision.records[key] for key in sorted(selected))

    def publish_evaluation(
        self, records, *, status, need_status="owner_revalidation_required"
    ):
        if not self.active or not self.policy.authorized:
            return self._problem(
                "current_authority_unavailable", {"operation": "native_evaluation"}
            )
        inputs = self.evaluation_inputs()
        event = self._event(
            "domain_evaluation",
            {
                "status": status,
                "basis": [asdict(item) for item in self.basis],
                "selected_inputs": [item.record_id for item in inputs],
                "adequacy": "unsupported_no_admitted_evaluator",
                "method": self.policy.method,
                "capabilities": sorted(self.policy.capabilities),
                "next_need_status": need_status,
            },
            tuple(item.record_id for item in inputs)
            + tuple(item.record_id for item in records),
        )
        return self._publish(
            (*records, event), {**self.state, "need_status": need_status}
        )

    def evaluation_basis_status(self, evaluation_id):
        item = payload(self.revision.records[evaluation_id])
        same = item["basis"] == [asdict(binding) for binding in self.basis] and item[
            "selected_inputs"
        ] == [record.record_id for record in self.evaluation_inputs()]
        same = (
            same
            and item["method"] == self.policy.method
            and item["capabilities"] == sorted(self.policy.capabilities)
            and self.policy.target == self.ref.target
        )
        return "unchanged_declared_basis" if same else "requires_owner_revalidation"


class InvestigatorPort:
    """Consumer surface: reading and attributed proposals/requests only.

    Capability driver callbacks, native truth, policy edits, publication and recovery
    stay with WorkspaceHost. Python access control here is a responsibility sketch,
    not isolation from hostile code running in the same process.
    """

    def __init__(self, host: WorkspaceHost):
        self._host = host

    def read(self, record_ids: tuple[str, ...]):
        return self._host.read(record_ids)

    def request(self, request: AcquisitionRequest):
        return self._host.request(request)

    def request_bytes(self, envelope: bytes):
        return self.request(decode_request(envelope))

    def propose(self, proposal_id, view: Projection, citations, claim):
        return self._host.propose(
            proposal_id,
            view.revision,
            view.basis,
            view.view_id,
            citations,
            claim,
            method=view.method,
        )
