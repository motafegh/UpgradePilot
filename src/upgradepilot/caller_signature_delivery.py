"""Application delivery and historical opening for the explicit source-only profile.

``investigate_and_deliver_caller_signature`` composes the normal acquisition stages
with report generation and lifecycle publication. Its outcome separates producer,
presentation and publication problems so the CLI can apply shell policy. An exact
unacknowledged publication is inspected once, without retrying a capability.

``open_caller_signature_checkpoint`` reads the selected immutable boundary and any
supported retained report. It never generates a report or installs execution authority.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .caller_signature.acquisition import AcquisitionSession
from .github.api import GitHubAcquisitionError, GitHubResponseError
from .github.identity import UpgradePilotInputError
from .investigation import investigate_caller_signature_progress
from .report import InvestigationReport
from .report_file import ReportValidationError, decode_report, encode_report
from .report_projection import project_caller_signature_report
from .workspace.checkpoint_revision import CheckpointRevision, CheckpointStorageError, StoredCheckpoint
from .workspace.checkpoint_store import CheckpointStore
from .workspace.lifecycle_boundary import CapturedLifecycleRecord, reconstruct_lifecycle_history
from .workspace.lifecycle_host import InvestigationWorkspaceHost
from .workspace.lifecycle_records import (
    InvestigationNeed, LifecycleMethodIdentity, ViewDelivery, decode_lifecycle_value,
)
from .workspace.native_projection import (
    CallerSignatureNativeProjection, reconstruct_caller_signature_projection,
)
from .workspace.native_representation import NativeReconstructionError

REPORT_REPRESENTATION = "upgradepilot-investigation-report/schema1"
REPORT_METHOD = LifecycleMethodIdentity(
    "report.projection", "report_projection.project_caller_signature_report", "1",
    None, REPORT_REPRESENTATION, None,
    ("Source-only profile; local comparisons grant no runtime or maintainer-action permission.",),
)
type DeliveryStage = Literal["input", "acquisition", "response", "analysis", "report", "publication"]
type PublicationInspection = Literal["not_attempted", "published", "not_published", "unknown"]


@dataclass(frozen=True)
class DeliveryProblem:
    stage: DeliveryStage
    reason: str
    detail: str


@dataclass(frozen=True)
class CallerSignatureDelivery:
    report: InvestigationReport | None
    last_acknowledged_revision: CheckpointRevision | None
    attempted_revision: CheckpointRevision | None
    attempt_status: PublicationInspection
    problems: tuple[DeliveryProblem, ...]

    @property
    def recoverable_revision(self) -> CheckpointRevision | None:
        if self.attempt_status == "published":
            return self.attempted_revision
        return self.last_acknowledged_revision


def _publication_handoff(host: InvestigationWorkspaceHost, report: InvestigationReport | None,
                         problems: tuple[DeliveryProblem, ...] | list[DeliveryProblem]) -> CallerSignatureDelivery:
    attempted = host.unacknowledged_revision
    status: PublicationInspection = "not_attempted"
    if attempted is not None:
        status = "unknown"
        assert host.store is not None
        try:
            status = host.store.inspect_publication(attempted)
        except Exception:
            # Failed inspection cannot establish absence or permission to retry.
            pass
    return CallerSignatureDelivery(report, host.current, attempted, status, tuple(problems))


def _failure(stage: DeliveryStage, error: Exception) -> DeliveryProblem:
    # Arbitrary worker/filesystem exceptions may contain private environment data.
    # Typed public reasons are useful without copying arbitrary exception messages.
    reason = getattr(error, "reason", type(error).__name__)
    public_errors = (GitHubAcquisitionError, GitHubResponseError, UpgradePilotInputError,
                     NativeReconstructionError, CheckpointStorageError, ReportValidationError)
    detail = str(error) if isinstance(error, public_errors) else f"{stage} operation failed ({reason})."
    return DeliveryProblem(stage, reason, detail)


def investigate_and_deliver_caller_signature(
    repository: str, pull_number: int, *, session: AcquisitionSession,
    host: InvestigationWorkspaceHost,
    expected_base: str | None = None, expected_head: str | None = None,
) -> CallerSignatureDelivery:
    """Run each producer once, publish the exact report, then return earned handoff.

    Optional expected revisions reach the existing PR-prefix guard before changed
    files or source work. None preserves ordinary unguarded acquisition; this
    application does not fetch a second prefix or reinterpret mismatched evidence.
    """
    problems = []
    try:
        revision = investigate_caller_signature_progress(
            repository, pull_number, session=session, workspace_host=host,
            expected_base=expected_base, expected_head=expected_head,
        )
    except Exception as error:
        if host.publication_blocked:
            stage = "publication"
        elif isinstance(error, UpgradePilotInputError):
            stage = "input"
        elif isinstance(error, GitHubAcquisitionError):
            stage = "acquisition"
        elif isinstance(error, GitHubResponseError):
            stage = "response"
        else:
            # Installed attempt identities distinguish worker failures from earlier
            # source composition failures without copying a second phase tracker.
            history = host.current.lifecycle_history if host.current else None
            analysis_started = history is not None and any(
                record.kind == "execution_attempt" and record.method.owner == "caller_signature.analysis"
                for record in history.records
            )
            stage = "analysis" if analysis_started else "acquisition"
        return _publication_handoff(host, None, (_failure(stage, error),))

    try:
        native = reconstruct_caller_signature_projection(revision.boundary, expected_target=revision.boundary.target)
        if native.sources and native.sources.acquisition.state == "failed":
            problems.append(DeliveryProblem("acquisition", "source_acquisition_failed",
                                           "Source acquisition aborted with retained progress and recorded problems."))
        if native.comparison and native.comparison.state != "completed":
            problems.append(DeliveryProblem("analysis", native.comparison.reason or native.comparison.state,
                                           "Bounded source analysis did not complete."))
        report = project_caller_signature_report(revision.boundary, auth_mode=session.auth_mode)
        encoded = encode_report(report)
        # Producer execution is finished. Install only the trusted report consumer,
        # withdrawing capability authority before presentation publication.
        host.configure(authority=None, capabilities=(), methods=(REPORT_METHOD,))
        ids = tuple(record.record_id for record in revision.boundary.records)
        purpose = host.add_purpose(
            InvestigationNeed("report_delivery", "Deliver the exact source-profile report.", revision.revision_id),
            native_record_ids=ids,
        )
        view = host.prepare_view("caller-signature-report", ids, selection_limit="Complete actual native basis, including unperformed branches.")
        host.deliver_view(purpose, view.view_id, representation=REPORT_REPRESENTATION,
                          content=encoded.decode("utf-8"), method=REPORT_METHOD)
    except Exception as error:
        stage = "publication" if host.publication_blocked else "report"
        problems.append(_failure(stage, error))
        return _publication_handoff(host, None, problems)
    return _publication_handoff(host, report, problems)


@dataclass(frozen=True)
class OpenedCallerSignatureCheckpoint:
    selected: StoredCheckpoint
    native: CallerSignatureNativeProjection
    report: InvestigationReport | None


def retained_report_presence(revision: CheckpointRevision) -> bool:
    """Describe a confirmed boundary's delivery presence without regenerating it."""
    if revision.lifecycle_history is None:
        return False
    return any(
        isinstance(value := decode_lifecycle_value(record.kind, record.codec_version, record.payload), ViewDelivery)
        and _is_report_delivery(record, value)
        for record in revision.lifecycle_history.records if record.kind == "view_delivery"
    )


def _is_report_delivery(record: CapturedLifecycleRecord, value: ViewDelivery) -> bool:
    # Future report encodings are present-but-unsupported, not absent. Recognition
    # never dispatches a decoder named by retained content.
    return value.representation.startswith("upgradepilot-investigation-report/") or (
        record.method.owner == REPORT_METHOD.owner and record.method.method == REPORT_METHOD.method
    )


def open_caller_signature_checkpoint(store: CheckpointStore, revision_id: str) -> OpenedCallerSignatureCheckpoint:
    """Decode one explicit source checkpoint and its historical report delivery.

    Stored identities are local selection, not authentication. Typed lifecycle
    reconstruction checks causal links against original ancestor bases. Report
    support is fixed by installed method identity and schema; it is never dispatched
    using a function name supplied by the file.
    """
    selected = store.read_selected_revision(revision_id)
    revision = selected.revision
    native = reconstruct_caller_signature_projection(revision.boundary, expected_target=revision.boundary.target)
    reports = []
    if revision.lifecycle_history is not None:
        bases = {revision.revision_id: revision.boundary}
        for record in revision.lifecycle_history.records:
            if record.basis_revision_id not in bases:
                bases[record.basis_revision_id] = store.read_revision(
                    revision.lineage_id, record.basis_revision_id,
                    expected_target=revision.boundary.target,
                ).revision.boundary
        for item in reconstruct_lifecycle_history(revision.lifecycle_history, bases=bases):
            value, record = item.value, item.capture
            if isinstance(value, ViewDelivery) and _is_report_delivery(record, value):
                if record.method != REPORT_METHOD or value.representation != REPORT_REPRESENTATION:
                    raise NativeReconstructionError("unsupported_report_projection", "No installed report delivery support.")
                if set(record.native_record_ids) != {r.record_id for r in revision.boundary.records}:
                    raise NativeReconstructionError("invalid_report_basis", "Report does not cover the selected native boundary.")
                report = decode_report(value.retained_content.encode("utf-8"))
                identity = {f.name: f.value for f in report.identity}
                target = revision.boundary.target
                expected = dict(repository=target.repository, pull_number=str(target.pull_number),
                                base_sha=target.base_sha, head_sha=target.head_sha)
                if any(identity.get(k) != v for k, v in expected.items()):
                    raise NativeReconstructionError("wrong_target", "Retained report target differs from selected revision.")
                reports.append(report)
    if len(reports) > 1:
        raise NativeReconstructionError("ambiguous_report_delivery", "Multiple report deliveries require explicit selection support.")
    return OpenedCallerSignatureCheckpoint(selected, native, reports[0] if reports else None)
