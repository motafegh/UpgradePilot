"""Host-only checkpoint adapters; Investigator values never import this module."""

import sqlite3

from experiments.workspace_checkpoint_stores import (
    StalePublication,
    StoreBusy,
    StoreDamaged,
    open_store,
)
from experiments.workspace_investigator_seam import CheckpointUnavailable
from experiments.workspace_revision_representation import (
    decode_checkpoint,
    encode_checkpoint,
)


class MemoryCheckpoints:
    """Encoded memory baseline exercises recovery through the same declared closure."""

    def __init__(self):
        self.data = None

    def load(self):
        return None if self.data is None else decode_checkpoint(self.data)

    def save(self, revision, expected):
        old = self.load()
        if (-1 if old is None else old.number) != expected:
            return False
        self.data = encode_checkpoint(revision)
        return True


class SQLiteCheckpoints:
    """Provisional WAL/FULL store, translating publication contention for the host."""

    def __init__(self, root, *, create=False):
        self.store = open_store("sqlite-wal", root, create=create)

    def load(self):
        try:
            outcome = self.store.recover()
        except (StoreDamaged, StoreBusy, OSError, ValueError, sqlite3.Error) as error:
            raise CheckpointUnavailable("Historical checkpoint unavailable") from error
        if outcome.rejected:
            # Historical fallback is inspectable through the store; this sketch refuses
            # active continuation rather than silently selecting a damaged current head.
            raise CheckpointUnavailable(
                "Damaged current checkpoint: inspection requires explicit fallback"
            )
        return outcome.revision

    def save(self, revision, expected):
        try:
            self.store.publish(encode_checkpoint(revision), expected=expected)
        except StalePublication:
            return False
        except (StoreDamaged, StoreBusy, OSError, ValueError, sqlite3.Error) as error:
            raise CheckpointUnavailable("Checkpoint publication unconfirmed") from error
        return True

    def close(self):
        self.store.close()
