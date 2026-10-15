"""Synchronous host authority and immutable lifecycle publication, independent of domains.

Start at InvestigationWorkspaceHost: trusted composition registers capabilities/methods,
while consumers submit typed requests and attributed proposals against registered purposes.
Native/domain owners supply genuine needs; trusted composition admits discovery objectives.
Admission and durable
attempt intent precede capability execution. Native evaluators keep semantic ownership.
Current material validity is checked separately from conditional predecessor publication.

Without a store, identical CheckpointRevision values form volatile in-process publication;
there is no durability promise or automatic filesystem choice. With an explicitly supplied
schema-2 CheckpointStore, acknowledgement precedes execution. Recovery/inspection never
installs authority; restored admissions cannot be executed as live admission receipts.
"""

from collections.abc import Callable, Mapping
from dataclasses import dataclass, replace
from typing import Literal
from uuid import uuid4

from .checkpoint_revision import CheckpointRevision, StoredCheckpoint
from .checkpoint_store import CheckpointStore
from .lifecycle_boundary import (
    CapturedLifecycleHistory,
    CapturedLifecycleRecord,
    capture_lifecycle_record,
    reconstruct_lifecycle_history,
)
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
    ProceduralTermination,
    RequestAdmission,
    StoppingProposal,
)
from .material_validity import (
    MaterialBasisValidity,
    native_material_closure,
    validate_current_material_basis,
)
from .native_boundary import (
    CapturedNativeBoundary,
    CapturedNativeRecord,
    ExactInvestigationTarget,
    validate_native_boundary,
)
from .native_representation import json_bytes


class WorkspaceHostError(ValueError):
    def __init__(self, reason: str) -> None:
        self.reason = reason
        super().__init__(reason)


@dataclass(frozen=True, slots=True)
class ExecutionAuthority:
    target: ExactInvestigationTarget
    capabilities: frozenset[str]
    effects: frozenset[str]


@dataclass(frozen=True, slots=True)
class CapabilityResult:
    outcome: Literal["observed", "empty", "scoped_negative", "problem"]
    detail: str
    value: object = None
    representation: str | None = None
    retained_content: str | None = None


@dataclass(frozen=True, slots=True)
class HostCapability:
    """Installed by trusted composition, never by a request/proposal or retained file."""

    name: str
    method: LifecycleMethodIdentity
    effects: frozenset[str]
    accepts_scope: Callable[[str], bool]
    execute: Callable[[CapabilityRequest], CapabilityResult]


@dataclass(frozen=True, slots=True)
class WorkspaceConsumerView:
    view_id: str
    revision_id: str
    target: ExactInvestigationTarget
    native_records: tuple[CapturedNativeRecord, ...]


_HOST_METHOD = LifecycleMethodIdentity(
    "workspace.host",
    "InvestigationWorkspaceHost",
    "1",
    None,
    "synchronous-lifecycle/1",
    None,
    (),
)


def _capability_identity(capability: HostCapability) -> LifecycleMethodIdentity:
    # The installed effects contract is material too: retaining just a method name could
    # conceal a changed capability under the same registry key. Preserve supplied config.
    return replace(
        capability.method,
        configuration=json_bytes(
            {
                "declared_configuration": capability.method.configuration,
                "effects": sorted(capability.effects),
            }
        ).decode("utf-8"),
    )


class InvestigationWorkspaceHost:
    def __init__(
        self,
        *,
        store: CheckpointStore | None = None,
        lineage_id: str | None = None,
    ) -> None:
        self.store = store
        self.lineage_id = lineage_id or uuid4().hex
        self.current: CheckpointRevision | None = None
        self._bases: dict[str, CapturedNativeBoundary] = {}
        self._values: dict[str, LifecycleValue] = {}
        self._records: dict[str, CapturedLifecycleRecord] = {}
        self._capabilities: dict[str, HostCapability] = {}
        self._methods: tuple[LifecycleMethodIdentity, ...] = (_HOST_METHOD,)
        self._authority: ExecutionAuthority | None = None
        self._live_admissions: set[str] = set()
        self._publication_blocked = False
        self._configured = False

    def configure(
        self,
        *,
        authority: ExecutionAuthority | None,
        capabilities: tuple[HostCapability, ...],
        methods: tuple[LifecycleMethodIdentity, ...] = (),
    ) -> None:
        """Trusted present bindings; no request, file or recovered record can install them."""
        if len({item.name for item in capabilities}) != len(capabilities):
            raise WorkspaceHostError("duplicate_capability_registration")
        self._authority = authority
        self._capabilities = {item.name: item for item in capabilities}
        self._methods = (_HOST_METHOD,) + methods
        self._configured = True

    def bind_native_callers(
        self,
        *,
        authority: ExecutionAuthority,
        capabilities: tuple[HostCapability, ...],
        methods: tuple[LifecycleMethodIdentity, ...],
    ) -> None:
        """Install the normal composition's narrow defaults, preserving explicit policy."""
        if not self._configured:
            self.configure(
                authority=authority, capabilities=capabilities, methods=methods
            )

    def lifecycle_value(self, identity: str) -> LifecycleValue:
        self._required_current()
        if identity not in self._values:
            raise WorkspaceHostError("unknown_lifecycle_reference")
        return self._values[identity]

    def initialize(self, boundary: CapturedNativeBoundary) -> None:
        if self.current is not None:
            raise WorkspaceHostError("host_already_initialized")
        self._publish(boundary, ())

    def restore(
        self,
        stored: StoredCheckpoint,
        *,
        bases: Mapping[str, CapturedNativeBoundary],
    ) -> None:
        """Explicit historical installation; no capability execution, authority or retry."""
        if self.current is not None or stored.revision.lineage_id != self.lineage_id:
            raise WorkspaceHostError("wrong_host_lineage")
        if stored.revision.lifecycle_history is None:
            raise WorkspaceHostError("lifecycle_not_retained")
        selected_bases = dict(bases)
        selected_bases[stored.revision.revision_id] = stored.revision.boundary
        decoded = reconstruct_lifecycle_history(
            stored.revision.lifecycle_history, bases=selected_bases
        )
        self.current = stored.revision
        self._bases = selected_bases
        self._records = {item.capture.record_id: item.capture for item in decoded}
        self._values = {item.capture.record_id: item.value for item in decoded}
        self._authority = None
        self._live_admissions.clear()

    def _required_current(self) -> CheckpointRevision:
        if self._publication_blocked:
            raise WorkspaceHostError("publication_reconciliation_required")
        if self.current is None:
            raise WorkspaceHostError("host_not_initialized")
        return self.current

    def _publish(
        self,
        boundary: CapturedNativeBoundary,
        events: tuple[
            tuple[LifecycleValue, tuple[str, ...], LifecycleMethodIdentity, str | None],
            ...,
        ],
    ) -> tuple[str, ...]:
        if self._publication_blocked:
            raise WorkspaceHostError("publication_reconciliation_required")
        target = self.current.boundary.target if self.current else boundary.target
        validate_native_boundary(boundary, expected_target=target)
        # Volatile and durable publication share immutable identity/reference semantics.
        retained = {
            item.record_id: item
            for basis in self._bases.values()
            for item in basis.records
        }
        if any(
            item.record_id in retained and retained[item.record_id] != item
            for item in boundary.records
        ):
            raise WorkspaceHostError("immutable_native_identity_conflict")
        revision_id = uuid4().hex
        additions = tuple(
            capture_lifecycle_record(
                uuid4().hex,
                basis or revision_id,
                value,
                native_record_ids=references,
                method=method,
            )
            for value, references, method, basis in events
        )
        previous = (
            self.current.lifecycle_history.records
            if self.current and self.current.lifecycle_history
            else ()
        )
        history = CapturedLifecycleHistory(previous + additions)
        bases = dict(self._bases, **{revision_id: boundary})
        decoded = reconstruct_lifecycle_history(history, bases=bases)
        revision = CheckpointRevision(
            self.lineage_id,
            revision_id,
            self.current.revision_id if self.current else None,
            boundary,
            history,
        )
        revision.digest()
        if self.store is not None:
            try:
                self.store.publish(revision)
            except BaseException:
                # Even a lost receipt cannot authorize the next external effect.
                self._publication_blocked = True
                raise
        self.current = revision
        self._bases = bases
        self._records = {item.capture.record_id: item.capture for item in decoded}
        self._values = {item.capture.record_id: item.value for item in decoded}
        return tuple(item.record_id for item in additions)

    def publish_native_progress(self, boundary: CapturedNativeBoundary) -> None:
        self._required_current()
        self._publish(boundary, ())

    def _append(
        self,
        value: LifecycleValue,
        references: tuple[str, ...],
        *,
        method: LifecycleMethodIdentity = _HOST_METHOD,
        basis: str | None = None,
        boundary: CapturedNativeBoundary | None = None,
    ) -> str:
        current = self._required_current()
        return self._publish(
            boundary or current.boundary, ((value, references, method, basis),)
        )[0]

    def add_purpose(
        self,
        value: InvestigationNeed | DiscoveryObjective,
        *,
        native_record_ids: tuple[str, ...],
        method: LifecycleMethodIdentity = _HOST_METHOD,
    ) -> str:
        """Register an owner-supplied/admitted purpose, not classify a model suggestion.

        A future model adapter may submit an attributed proposal; it must not expose this
        trusted registration operation as a way to fabricate a non-final proposition.
        """
        if not isinstance(value, (InvestigationNeed, DiscoveryObjective)):
            raise WorkspaceHostError("invalid_purpose")
        return self._append(value, native_record_ids, method=method)

    def request_capability(self, purpose_id: str, capability: str, scope: str) -> str:
        if not isinstance(
            self.lifecycle_value(purpose_id), (InvestigationNeed, DiscoveryObjective)
        ):
            raise WorkspaceHostError("request_without_registered_purpose")
        purpose = self._records[purpose_id]
        installed = self._capabilities.get(capability)
        method = (
            _capability_identity(installed)
            if installed
            else LifecycleMethodIdentity(
                "workspace.host",
                None,
                None,
                None,
                None,
                None,
                ("capability_not_installed",),
            )
        )
        return self._append(
            CapabilityRequest(purpose_id, capability, scope),
            purpose.native_record_ids,
            method=method,
            basis=purpose.basis_revision_id,
        )

    def _request_for(self, identity: str) -> tuple[str, CapabilityRequest] | None:
        value = self.lifecycle_value(identity)
        if isinstance(value, CapabilityRequest):
            return identity, value
        if isinstance(value, RequestAdmission):
            return self._request_for(value.request_id)
        if isinstance(value, ExecutionAttempt):
            return self._request_for(value.admission_id)
        if isinstance(value, (CapabilityObservation, ExecutionInterruption)):
            return self._request_for(value.attempt_id)
        if isinstance(value, EvaluationOutcome):
            return self._request_for(value.subject_id)
        return None

    def current_validity(
        self, identity: str, *, scope: str | None = None
    ) -> MaterialBasisValidity:
        current = self._required_current()
        self.lifecycle_value(identity)
        record = self._records[identity]
        request = self._request_for(identity)
        available = True
        value_at_boundary = self._values[identity]
        original_scope = (
            value_at_boundary.scope
            if isinstance(value_at_boundary, (InvestigationNeed, DiscoveryObjective))
            else None
        )
        method = record.method if record.method in self._methods else None
        if request is not None:
            request_id, value = request
            original_scope = value.scope
            capability = self._capabilities.get(value.capability)
            available = capability is not None
            if capability is not None:
                if _capability_identity(capability) != self._records[request_id].method:
                    return MaterialBasisValidity(
                        "stale", ("capability_method_changed",)
                    )
                if not capability.accepts_scope(value.scope):
                    return MaterialBasisValidity("stale", ("capability_scope_changed",))
                if isinstance(
                    value_at_boundary,
                    (
                        CapabilityRequest,
                        ExecutionAttempt,
                        CapabilityObservation,
                        ExecutionInterruption,
                    ),
                ):
                    method = _capability_identity(capability)
        return validate_current_material_basis(
            record,
            self._bases[record.basis_revision_id],
            current.boundary,
            original_scope=original_scope,
            current_scope=scope if scope is not None else original_scope,
            current_method=method,
            capability_available=available,
        )

    def _execution_refusal(self, request_id: str) -> str | None:
        request = self.lifecycle_value(request_id)
        if not isinstance(request, CapabilityRequest):
            return "not_a_capability_request"
        current = self._required_current()
        authority = self._authority
        capability = self._capabilities.get(request.capability)
        if authority is None or authority.target != current.boundary.target:
            return "current_execution_authority_unavailable"
        if capability is None or request.capability not in authority.capabilities:
            return "capability_not_authorized"
        if not capability.effects <= authority.effects:
            return "effects_not_authorized"
        validity = self.current_validity(request_id)
        return None if validity.status == "valid" else validity.reasons[0]

    def admit_request(self, request_id: str) -> str:
        request = self.lifecycle_value(request_id)
        if not isinstance(request, CapabilityRequest):
            raise WorkspaceHostError("not_a_capability_request")
        refusal = self._execution_refusal(request_id)
        if any(
            isinstance(value, ExecutionAttempt)
            and self._request_for(identity)[0] == request_id
            for identity, value in self._values.items()
        ):
            refusal = "request_already_attempted_no_automatic_retry"
        record = self._records[request_id]
        admission = self._append(
            RequestAdmission(
                request_id,
                "rejected" if refusal else "admitted",
                "present-host-effects/1",
                refusal
                or "Exact capability/scope/material admitted under present host authority.",
            ),
            record.native_record_ids,
            basis=record.basis_revision_id,
        )
        if refusal is None:
            self._live_admissions.add(admission)
        return admission

    def execute_admission(self, admission_id: str) -> tuple[str, CapabilityResult]:
        admission = self.lifecycle_value(admission_id)
        if (
            not isinstance(admission, RequestAdmission)
            or admission.outcome != "admitted"
        ):
            raise WorkspaceHostError("request_not_admitted")
        if admission_id not in self._live_admissions:
            raise WorkspaceHostError("historical_or_consumed_admission")
        refusal = self._execution_refusal(admission.request_id)
        if refusal:
            raise WorkspaceHostError(refusal)
        if any(
            isinstance(value, ExecutionAttempt)
            and self._request_for(identity)[0] == admission.request_id
            for identity, value in self._values.items()
        ):
            raise WorkspaceHostError("request_already_attempted_no_automatic_retry")
        self._live_admissions.remove(admission_id)
        request = self._values[admission.request_id]
        assert isinstance(request, CapabilityRequest)
        capability = self._capabilities[request.capability]
        original = self._records[admission.request_id]
        attempt_id = self._append(
            ExecutionAttempt(admission_id, "intent_recorded"),
            original.native_record_ids,
            method=_capability_identity(capability),
        )
        if self.store is not None:
            current = self._required_current()
            try:
                selected = self.store.read_revision(
                    self.lineage_id,
                    current.revision_id,
                    expected_target=current.boundary.target,
                )
            except BaseException:
                self._publication_blocked = True
                raise
            if selected.head_revision_id != current.revision_id:
                # A concurrency refusal is not a material-staleness assessment or an
                # invitation to merge/retry. Reconciliation remains explicit.
                self._publication_blocked = True
                raise WorkspaceHostError("publication_head_changed_before_execution")
        refusal = self._execution_refusal(admission.request_id)
        if refusal:
            self._append(
                ExecutionInterruption(attempt_id, refusal, "not_started"),
                original.native_record_ids,
                method=self._records[attempt_id].method,
                basis=self._records[attempt_id].basis_revision_id,
            )
            raise WorkspaceHostError(refusal)
        try:
            result = capability.execute(request)
            if not isinstance(result, CapabilityResult):
                raise WorkspaceHostError("invalid_capability_result")
        except BaseException as error:
            self._append(
                ExecutionInterruption(attempt_id, type(error).__name__),
                original.native_record_ids,
                method=_capability_identity(capability),
                basis=self._records[attempt_id].basis_revision_id,
            )
            raise
        observation_id = self.ingest_observation(attempt_id, result)
        return observation_id, result

    def ingest_observation(self, attempt_id: str, result: CapabilityResult) -> str:
        request = self._request_for(attempt_id)
        if request is None or not isinstance(
            self._values[attempt_id], ExecutionAttempt
        ):
            raise WorkspaceHostError("observation_without_attempt")
        for value in self._values.values():
            if (
                isinstance(value, ExecutionInterruption)
                and value.attempt_id == attempt_id
            ):
                raise WorkspaceHostError(
                    "attempt_not_executed"
                    if value.completion == "not_started"
                    else "unknown_completion_requires_explicit_reconciliation"
                )
        record = self._records[attempt_id]
        observation = CapabilityObservation(
            attempt_id,
            result.outcome,
            request[1].scope,
            result.detail,
            result.representation,
            result.retained_content,
        )
        for identity, value in self._values.items():
            if (
                isinstance(value, CapabilityObservation)
                and value.attempt_id == attempt_id
            ):
                if value != observation:
                    raise WorkspaceHostError("contradictory_duplicate_observation")
                return identity
        return self._append(
            observation,
            record.native_record_ids,
            method=record.method,
            basis=record.basis_revision_id,
        )

    def evaluate_native(
        self,
        observation_id: str,
        *,
        method: LifecycleMethodIdentity,
        evaluate: Callable[[], tuple[CapturedNativeBoundary, str]],
    ) -> str:
        """Invoke an explicitly admitted native owner once, retaining its actual basis.

        The composition callback supplies that owner's full inputs independently of any
        model citations. Host bookkeeping never substitutes a semantic/adequacy evaluator.
        """
        if not isinstance(self.lifecycle_value(observation_id), CapabilityObservation):
            raise WorkspaceHostError("native_evaluation_without_observation")
        record = self._records[observation_id]
        validity = self.current_validity(observation_id)
        if validity.status != "valid" or method not in self._methods:
            outcome = "stale" if validity.status == "stale" else "unsupported"
            return self._append(
                EvaluationOutcome(
                    observation_id,
                    outcome,
                    None,
                    ",".join(validity.reasons) or "native_method_unavailable",
                ),
                record.native_record_ids,
                method=method,
                basis=record.basis_revision_id,
            )
        try:
            boundary, assessment_id = evaluate()
        except BaseException:
            self._append(
                EvaluationOutcome(
                    observation_id,
                    "failed",
                    None,
                    "Native owner failed; no assessment invented.",
                ),
                record.native_record_ids,
                method=method,
                basis=record.basis_revision_id,
            )
            raise
        references = native_material_closure(boundary, (assessment_id,))
        return self._append(
            EvaluationOutcome(
                observation_id,
                "evaluated",
                assessment_id,
                "Retained native result; no stronger host interpretation.",
            ),
            references,
            method=method,
            boundary=boundary,
        )

    def prepare_view(
        self, consumer: str, native_record_ids: tuple[str, ...], *, selection_limit: str
    ) -> WorkspaceConsumerView:
        current = self._required_current()
        available = {item.record_id: item for item in current.boundary.records}
        if (
            len(set(native_record_ids)) != len(native_record_ids)
            or not set(native_record_ids) <= available.keys()
        ):
            raise WorkspaceHostError("view_material_unavailable")
        omitted = tuple(
            identity for identity in available if identity not in native_record_ids
        )
        view_id = self._append(
            ConsumerView(consumer, native_record_ids, omitted, selection_limit),
            tuple(available),
        )
        return WorkspaceConsumerView(
            view_id,
            self._required_current().revision_id,
            current.boundary.target,
            tuple(available[identity] for identity in native_record_ids),
        )

    def record_use(
        self, view_id: str, native_record_ids: tuple[str, ...], *, receipt: str
    ) -> str:
        """Retain an observable adapter receipt; model self-report is not such a receipt.

        Even a valid receipt proves only its recorded delivery/use event, never hidden
        examination, reasoning, semantic support or adequacy.
        """
        self.lifecycle_value(view_id)
        record = self._records[view_id]
        return self._append(
            ObservableUse(view_id, native_record_ids, receipt),
            native_record_ids,
            basis=record.basis_revision_id,
        )

    def propose(
        self,
        view_id: str,
        subject: str,
        statement: str,
        cited_native_ids: tuple[str, ...],
    ) -> str:
        view = self.lifecycle_value(view_id)
        record = self._records[view_id]
        if not isinstance(view, ConsumerView):
            raise WorkspaceHostError("proposal_without_view")
        references = tuple(dict.fromkeys(view.delivered_native_ids + cited_native_ids))
        return self._append(
            AttributedProposal(view_id, subject, statement, cited_native_ids),
            references,
            basis=record.basis_revision_id,
        )

    def evaluate_proposal(self, proposal_id: str) -> str:
        if not isinstance(
            self.lifecycle_value(proposal_id), (AttributedProposal, StoppingProposal)
        ):
            raise WorkspaceHostError("not_an_attributed_or_stopping_proposal")
        record = self._records[proposal_id]
        return self._append(
            EvaluationOutcome(
                proposal_id,
                "unsupported",
                None,
                "No admitted semantic proposal/conflict/adequacy evaluator.",
            ),
            record.native_record_ids,
            basis=record.basis_revision_id,
        )

    def propose_stop(self, run_id: str, explanation: str) -> str:
        return self._append(StoppingProposal(run_id, explanation), ())

    def terminate(
        self,
        run_id: str,
        outcome: Literal["completed", "interrupted", "limit_exhausted", "failed"],
        detail: str,
    ) -> str:
        return self._append(ProceduralTermination(run_id, outcome, detail), ())

    def inspect_lifecycle(
        self,
    ) -> tuple[tuple[CapturedLifecycleRecord, LifecycleValue], ...]:
        self._required_current()
        return tuple(
            (self._records[identity], value) for identity, value in self._values.items()
        )

    def attempt_completion(
        self, attempt_id: str
    ) -> Literal["observed", "completion_unknown", "not_started"]:
        if not isinstance(self.lifecycle_value(attempt_id), ExecutionAttempt):
            raise WorkspaceHostError("not_an_execution_attempt")
        if any(
            isinstance(value, ExecutionInterruption)
            and value.attempt_id == attempt_id
            and value.completion == "not_started"
            for value in self._values.values()
        ):
            return "not_started"
        return (
            "observed"
            if any(
                isinstance(value, CapabilityObservation)
                and value.attempt_id == attempt_id
                for value in self._values.values()
            )
            else "completion_unknown"
        )
