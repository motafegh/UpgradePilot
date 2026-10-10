"""Publication-order regression for checkpoint lineage coherence classification."""

from __future__ import annotations

import sqlite3
import tempfile
import unittest
from pathlib import Path

from test_workspace_native_reconstruction import captured_case

from upgradepilot.workspace.checkpoint_revision import (
    CheckpointRevision,
    CheckpointStorageError,
)
from upgradepilot.workspace.checkpoint_store import CheckpointStore


class WorkspaceCheckpointPublicationCoherenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.boundary = captured_case()[2]

    def setUp(self):
        temporary = tempfile.TemporaryDirectory(
            prefix="upgradepilot-publication-coherence-"
        )
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.store = CheckpointStore.create(self.root / "store")
        self.initial = CheckpointRevision("main", "initial", None, self.boundary)

    def _assert_reason(self, reason: str, call) -> CheckpointStorageError:
        with self.assertRaises(CheckpointStorageError) as raised:
            call()
        self.assertEqual(raised.exception.reason, reason)
        return raised.exception

    def test_headless_retained_lineage_refuses_before_predecessor_conflict(self):
        self.store.publish(self.initial)
        with sqlite3.connect(
            self.store.directory / "workspace.sqlite3", isolation_level=None
        ) as database:
            database.execute("DELETE FROM heads WHERE lineage_id='main'")

        successor = CheckpointRevision("main", "second", "initial", self.boundary)
        self._assert_reason(
            "invalid_checkpoint_storage", lambda: self.store.publish(successor)
        )

        with sqlite3.connect(
            self.store.directory / "workspace.sqlite3", isolation_level=None
        ) as database:
            self.assertEqual(
                database.execute(
                    "SELECT revision_id,predecessor_id FROM revisions "
                    "WHERE lineage_id='main' ORDER BY revision_id"
                ).fetchall(),
                [("initial", None)],
            )

    def test_nonexistent_predecessor_on_empty_lineage_remains_conflict(self):
        staged = CheckpointRevision("main", "second", "initial", self.boundary)
        error = self._assert_reason(
            "publication_conflict", lambda: self.store.publish(staged)
        )
        self.assertEqual((error.expected, error.actual), ("initial", None))


if __name__ == "__main__":
    unittest.main()
