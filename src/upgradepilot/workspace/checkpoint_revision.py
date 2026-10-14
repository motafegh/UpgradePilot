"""Immutable publication inputs and receipts, independent of SQLite/native evaluators.

The host stages an explicit revision identity before publication so a lost acknowledgement
can be reconciled by that identity. Material comes from ``native_capture``; retaining it
does not grant capability execution or turn a historical assessment into current authority.
``checkpoint_store`` owns atomic publication and encoded inspection. Native projection
from a durable checkpoint is a separate integration responsibility.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256

from .lifecycle_boundary import CapturedLifecycleHistory, encode_lifecycle_history
from .native_boundary import CapturedNativeBoundary, encode_native_boundary
from .native_representation import MAX_NATIVE_JSON_BYTES, json_bytes


class CheckpointStorageError(ValueError):
    """Refusal without automatic merge, migration, acquisition or external retry."""

    def __init__(self, reason: str, detail: str) -> None:
        self.reason = reason
        self.detail = detail
        super().__init__(f"{reason}: {detail}")


class PublicationConflict(CheckpointStorageError):
    def __init__(self, expected: str | None, actual: str | None) -> None:
        self.expected = expected
        self.actual = actual
        super().__init__(
            "publication_conflict", "Lineage head differs from predecessor."
        )


class UnconfirmedPublication(CheckpointStorageError):
    """Commit was attempted; inspect this identity before deciding what happened.

    This says nothing about exactly-once external effects and grants no retry authority.
    Even a commit error is conservatively unconfirmed until the store can be inspected.
    """

    def __init__(self, lineage_id: str, revision_id: str) -> None:
        self.lineage_id = lineage_id
        self.revision_id = revision_id
        super().__init__(
            "unconfirmed_publication", "Reconcile the staged revision identity."
        )


@dataclass(frozen=True, slots=True)
class CheckpointRevision:
    lineage_id: str
    revision_id: str
    predecessor_id: str | None
    boundary: CapturedNativeBoundary
    lifecycle_history: CapturedLifecycleHistory | None = None

    def digest(self) -> str:
        """Bind header identity to the complete ordered encoded material, not its truth."""
        for value in (self.lineage_id, self.revision_id):
            if type(value) is not str or not value or len(value) > 256:
                raise CheckpointStorageError(
                    "invalid_revision", "Invalid revision identity."
                )
        if self.predecessor_id is not None and (
            type(self.predecessor_id) is not str
            or not self.predecessor_id
            or len(self.predecessor_id) > 256
            or self.predecessor_id == self.revision_id
        ):
            raise CheckpointStorageError(
                "invalid_revision", "Invalid predecessor identity."
            )
        native = encode_native_boundary(self.boundary)
        identity = {
            "lineage_id": self.lineage_id,
            "revision_id": self.revision_id,
            "predecessor_id": self.predecessor_id,
            "boundary_digest": sha256(native).hexdigest(),
        }
        # Missing history is the original native-only format, not an empty recovered run.
        # Preserve that exact digest contract for existing schema-1/native-only revisions.
        if self.lifecycle_history is not None:
            lifecycle = encode_lifecycle_history(self.lifecycle_history)
            if len(native) + len(lifecycle) > MAX_NATIVE_JSON_BYTES:
                raise CheckpointStorageError(
                    "storage_resource_limit", "Composed revision exceeds read capacity."
                )
            identity["format_version"] = 2
            identity["lifecycle_digest"] = sha256(lifecycle).hexdigest()
        return sha256(json_bytes(identity)).hexdigest()


@dataclass(frozen=True, slots=True)
class PublicationReceipt:
    lineage_id: str
    revision_id: str
    revision_digest: str


@dataclass(frozen=True, slots=True)
class StoredCheckpoint:
    """Selected historical boundary and explicit exclusion of later published progress."""

    revision: CheckpointRevision
    head_revision_id: str
    excluded_successor_ids: tuple[str, ...]

    @property
    def lifecycle_recovery_status(self) -> str:
        """Retention only; this does not assert codec support or current resume authority."""
        return "not_retained" if self.revision.lifecycle_history is None else "retained"


@dataclass(frozen=True, slots=True)
class BackupReceipt:
    revision_count: int
    lineage_heads: tuple[tuple[str, str], ...]
