"""Trusted, bounded source/native delivery through the canonical Workspace seam.

``WorkspaceEvidenceAccess`` is an in-process consumer interface, not a model runner.
Trusted composition installs its method and frozen catalog/scope. Consumers request
source pages or native views; the host checks present material/method bindings and retains
what was actually delivered. Native projections stay offline and do not re-evaluate facts.
Usage receipts are observational accounting; canonical history remains host-owned.
"""

from __future__ import annotations

from dataclasses import dataclass

from .lifecycle_host import InvestigationWorkspaceHost, WorkspaceHostError
from .lifecycle_records import (
    LifecycleMethodIdentity,
    ViewDelivery,
)
from .native_projection import reconstruct_ci_projection
from .native_representation import json_bytes, parse_json
from .source_access import (
    SOURCE_VIEW_REPRESENTATION,
    RetainedSourceCatalog,
    read_source_delivery,
    source_reference_was_delivered,
)

NATIVE_VIEW_REPRESENTATION = "workspace-native-view/1"
_INITIAL_FAMILIES = (
    "investigation_inputs",
    "ci_inputs",
    "ci_coverage",
    "runtime_dependency_state",
)


@dataclass(frozen=True, slots=True)
class ViewAccessReceipt:
    operation: str
    outcome: str
    delivery_id: str | None
    delivered_bytes: int
    examined_files: int
    examined_lines: int
    detail: str


@dataclass(frozen=True, init=False)
class WorkspaceEvidenceAccess:
    """One assignment's adapter; source universe and method identity are fixed at entry."""

    host: InvestigationWorkspaceHost
    catalog: RetainedSourceCatalog
    source_ids: tuple[str, ...]
    native_families: tuple[str, ...]
    max_native_bytes: int
    scope: str
    method: LifecycleMethodIdentity
    _receipts: list[ViewAccessReceipt]

    def __init__(
        self,
        host: InvestigationWorkspaceHost,
        catalog: RetainedSourceCatalog,
        *,
        source_ids: tuple[str, ...] | None = None,
        native_families: tuple[str, ...] = _INITIAL_FAMILIES,
        max_native_bytes: int = 256 * 1024,
    ):
        if host.current is None or catalog.target != host.current.boundary.target:
            raise ValueError(
                "Source catalog is not bound to this exact Workspace target."
            )
        object.__setattr__(self, "host", host)
        object.__setattr__(self, "catalog", catalog)
        object.__setattr__(
            self,
            "source_ids",
            tuple(source_ids)
            if source_ids is not None
            else tuple(scope.source_id for scope in catalog.scopes),
        )
        if not set(self.source_ids) <= {scope.source_id for scope in catalog.scopes}:
            raise ValueError("Source access scope is outside the frozen catalog.")
        if not set(native_families) <= set(_INITIAL_FAMILIES) or len(
            set(native_families)
        ) != len(native_families):
            raise ValueError("Unsupported native offering.")
        if (
            type(max_native_bytes) is not int
            or not 4096 <= max_native_bytes <= 1024 * 1024
        ):
            raise ValueError("Unsupported native view capacity.")
        object.__setattr__(self, "native_families", tuple(native_families))
        object.__setattr__(self, "max_native_bytes", max_native_bytes)
        object.__setattr__(self, "scope", "frozen-sources:" + catalog.identity)
        object.__setattr__(
            self,
            "method",
            LifecycleMethodIdentity(
                "workspace.consumer_access",
                "WorkspaceEvidenceAccess",
                "1",
                None,
                "bounded-workspace-access/1",
                json_bytes(
                    {
                        "catalog": catalog.identity,
                        "sources": self.source_ids,
                        "native_families": native_families,
                        "max_native_bytes": max_native_bytes,
                    }
                ).decode(),
                (
                    "Source capture labels retain their original strength; no semantic or adequacy evaluation.",
                ),
            ),
        )
        object.__setattr__(self, "_receipts", [])

    @property
    def receipts(self) -> tuple[ViewAccessReceipt, ...]:
        return tuple(self._receipts)

    def _guard(self, purpose_id: str) -> None:
        purpose = self.host.validate_view_access(purpose_id, method=self.method)
        if purpose.scope != self.scope:
            raise WorkspaceHostError("source_universe_outside_admitted_purpose")

    def _deliver(
        self,
        purpose_id,
        operation,
        content,
        native_ids=(),
        *,
        outcome="observed",
        work=(0, 0),
    ) -> str:
        view = self.host.prepare_view(
            "workspace-evidence-consumer",
            native_ids,
            selection_limit="Only the actual bounded payload is delivered; references and omissions do not imply examination or support.",
        )
        delivery_id = self.host.deliver_view(
            purpose_id,
            view.view_id,
            representation=SOURCE_VIEW_REPRESENTATION
            if operation.startswith("source:")
            else NATIVE_VIEW_REPRESENTATION,
            content=content.decode(),
            method=self.method,
        )
        self._receipts.append(
            ViewAccessReceipt(
                operation,
                outcome,
                delivery_id,
                len(content),
                *work,
                "Actual delivery; no hidden use or semantic support inferred.",
            )
        )
        return delivery_id

    def source_view(self, purpose_id: str, operation: str, arguments: dict) -> str:
        label = "source:" + (
            operation if type(operation) is str and len(operation) <= 80 else "invalid"
        )
        work = (0, 0)
        try:
            self._guard(purpose_id)
            if type(operation) is not str or len(operation) > 80:
                raise WorkspaceHostError("invalid_source_operation")
            if type(arguments) is not dict:
                raise WorkspaceHostError("invalid_source_arguments")
            source = arguments.get("source_id")
            # A global query on a restricted source menu must not leak other scopes.
            if source is not None and source not in self.source_ids:
                raise WorkspaceHostError("source_not_offered")
            if set(self.source_ids) != {
                scope.source_id for scope in self.catalog.scopes
            }:
                if source is None:
                    raise WorkspaceHostError("restricted_access_requires_exact_source")
                if operation == "resolve":
                    raise WorkspaceHostError(
                        "reference_resolution_outside_exact_source_scope"
                    )
            result = self.catalog.query(operation, arguments)
            work = (result.examined_files, result.examined_lines)
            return self._deliver(
                purpose_id,
                label,
                result.content,
                outcome=result.outcome,
                work=(result.examined_files, result.examined_lines),
            )
        except Exception as error:
            self._receipts.append(
                ViewAccessReceipt(
                    label, "refused", None, 0, *work, type(error).__name__
                )
            )
            raise

    def native_view(self, purpose_id: str, families: tuple[str, ...]) -> str:
        try:
            self._guard(purpose_id)
            if (
                type(families) is not tuple
                or not families
                or len(set(families)) != len(families)
                or not set(families) <= set(self.native_families)
            ):
                raise WorkspaceHostError("native_family_not_offered")
            current = self.host.current
            assert current is not None
            reconstruct_ci_projection(
                current.boundary, expected_target=current.boundary.target
            )
            selected = [
                record
                for record in current.boundary.records
                if record.family in families
            ]
            items = []
            ids = []
            omitted = []
            for record in selected:
                item = {
                    "record_id": record.record_id,
                    "family": record.family,
                    "owner": record.owner,
                    "outcome": record.outcome,
                    "codec_version": record.codec_version,
                    "producer_method": record.producer_method,
                    "producer_version": record.producer_version,
                    "retention_gaps": record.retention_gaps,
                    "input_record_ids": record.input_record_ids,
                    "payload_digest": record.payload_digest,
                    "payload": parse_json(record.payload),
                }
                if len(json_bytes(items + [item])) > self.max_native_bytes - 2048:
                    omitted.append(
                        {
                            "record_id": record.record_id,
                            "family": record.family,
                            "reason": "native_view_capacity",
                            "page_access": "native_page",
                        }
                    )
                else:
                    items.append(item)
                    ids.append(record.record_id)
            content = json_bytes(
                {
                    "format": NATIVE_VIEW_REPRESENTATION,
                    "target_revision": current.revision_id,
                    "source_universe": self.catalog.identity,
                    "native_records": items,
                    "omitted": omitted,
                    "limit": "Only selected native material; no general applicability, adequacy or action permission.",
                }
            )
            if len(content) > self.max_native_bytes:
                raise WorkspaceHostError("native_view_capacity")
            return self._deliver(purpose_id, "native:view", content, tuple(ids))
        except Exception as error:
            self._receipts.append(
                ViewAccessReceipt(
                    "native:view", "refused", None, 0, 0, 0, type(error).__name__
                )
            )
            raise

    def propose_source(
        self,
        purpose_id: str,
        delivery_id: str,
        subject: str,
        statement: str,
        reference: str,
    ) -> tuple[str, str]:
        """Submit an attributed source proposal with a delivered-reference relationship.

        This closes the source/native reference seam without inventing a native evidence
        record or evaluator. Search-only/undelivered references are refused before proposal
        publication; accepted citations still do not establish semantic truth.
        """
        try:
            self._guard(purpose_id)
            delivery = self.host.lifecycle_value(delivery_id)
            if (
                not isinstance(delivery, ViewDelivery)
                or delivery.representation != SOURCE_VIEW_REPRESENTATION
            ):
                raise WorkspaceHostError("proposal_without_source_delivery")
            content = delivery.retained_content.encode()
            if read_source_delivery(content)[
                "catalog_id"
            ] != self.catalog.identity or not source_reference_was_delivered(
                reference, content
            ):
                raise WorkspaceHostError("source_reference_not_delivered")
            if self.host.current_validity(delivery_id).status != "valid":
                raise WorkspaceHostError("source_delivery_stale_or_unsupported")
            proposal = self.host.propose(delivery.view_id, subject, statement, ())
            citation = self.host.cite_delivery(
                proposal, delivery_id, reference, method=self.method
            )
            self._receipts.append(
                ViewAccessReceipt(
                    "proposal:source",
                    "proposed",
                    delivery_id,
                    0,
                    0,
                    0,
                    "Attributed proposal/citation only; no semantic evaluation.",
                )
            )
            return proposal, citation
        except Exception as error:
            self._receipts.append(
                ViewAccessReceipt(
                    "proposal:source", "refused", None, 0, 0, 0, type(error).__name__
                )
            )
            raise

    def native_page(
        self,
        purpose_id: str,
        record_id: str,
        *,
        start_character: int = 0,
        character_count: int = 4096,
    ) -> str:
        try:
            self._guard(purpose_id)
            if (
                type(start_character) is not int
                or start_character < 0
                or type(character_count) is not int
                or not 1 <= character_count <= 4096
            ):
                raise WorkspaceHostError("invalid_native_page")
            current = self.host.current
            assert current is not None
            reconstruct_ci_projection(
                current.boundary, expected_target=current.boundary.target
            )
            record = next(
                (
                    r
                    for r in current.boundary.records
                    if r.record_id == record_id and r.family in self.native_families
                ),
                None,
            )
            if record is None:
                raise WorkspaceHostError("native_reference_unavailable")
            text = record.payload.decode()
            if start_character >= len(text):
                raise WorkspaceHostError("native_page_outside_payload")
            end = min(len(text), start_character + character_count)
            content = json_bytes(
                {
                    "format": NATIVE_VIEW_REPRESENTATION,
                    "record_id": record_id,
                    "family": record.family,
                    "payload_digest": record.payload_digest,
                    "start_character": start_character,
                    "text": text[start_character:end],
                    "next_character": end if end < len(text) else None,
                    "partial_payload": start_character != 0 or end != len(text),
                    "limit": "Exact retained UTF-8 JSON text page; a partial page is not a complete native record.",
                }
            )
            return self._deliver(purpose_id, "native:page", content, (record_id,))
        except Exception as error:
            self._receipts.append(
                ViewAccessReceipt(
                    "native:page", "refused", None, 0, 0, 0, type(error).__name__
                )
            )
            raise
