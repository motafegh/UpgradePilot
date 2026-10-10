"""Durable encoded publication proofs, deliberately before combined native reconstruction.

Normal native capture supplies the material fixture; modified bytes and opaque intent
records isolate storage boundaries, not semantic acceptance or a lifecycle producer path.
Real SQLite/process controls distinguish rollback, conflict, unconfirmed acknowledgement,
retained history and validated online backup. No power-loss/device claim is made.
"""

from __future__ import annotations

import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from dataclasses import FrozenInstanceError, replace
from hashlib import sha256
from pathlib import Path
from unittest.mock import patch

from test_workspace_native_reconstruction import captured_case

from upgradepilot.workspace.checkpoint_revision import (
    CheckpointRevision,
    CheckpointStorageError,
    UnconfirmedPublication,
)
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_boundary import (
    CapturedNativeRecord,
    encode_native_boundary,
)
from upgradepilot.workspace.native_representation import json_bytes


_INTERRUPT_CHILD = r"""
import json, os, signal, sqlite3, sys
from pathlib import Path
from unittest.mock import patch
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget, read_native_boundary
from upgradepilot.workspace.checkpoint_revision import CheckpointRevision
from upgradepilot.workspace.checkpoint_store import CheckpointStore
target = ExactInvestigationTarget(**json.loads(sys.argv[3]))
boundary = read_native_boundary(Path(sys.argv[2]).read_bytes(), expected_target=target)
stage, revision_id, predecessor = sys.argv[4:]
predecessor = predecessor or None
real_connect = sqlite3.connect
def terminate():
    os.kill(os.getpid(), signal.SIGKILL)
class Interrupted(sqlite3.Connection):
    def execute(self, sql, parameters=()):
        if stage == 'before_begin' and sql == 'BEGIN IMMEDIATE': terminate()
        if stage == 'before_commit' and sql == 'COMMIT': terminate()
        result = super().execute(sql, parameters)
        checks = {
            'after_payload': 'INSERT INTO payloads',
            'after_record': 'INSERT INTO records',
            'after_reference': 'INSERT INTO record_inputs',
            'after_revision': 'INSERT INTO revisions',
            'after_membership': 'INSERT INTO revision_members',
            'after_head': 'UPDATE heads',
        }
        if stage in checks and sql.startswith(checks[stage]): terminate()
        if stage == 'after_commit' and sql == 'COMMIT': terminate()
        return result
def connect(*args, **kwargs):
    return real_connect(*args, factory=Interrupted, **kwargs)
with patch('sqlite3.connect', connect):
    store = CheckpointStore.open(Path(sys.argv[1]))
    receipt = store.publish(CheckpointRevision('main', revision_id, predecessor, boundary))
    if stage == 'after_ack':
        print(json.dumps({'revision_id': receipt.revision_id, 'digest': receipt.revision_digest}), flush=True)
        terminate()
    raise AssertionError('interruption point was not exercised')
"""

_WRITER_CHILD = r"""
import json, sys
from pathlib import Path
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget, read_native_boundary
from upgradepilot.workspace.checkpoint_revision import CheckpointRevision, CheckpointStorageError
from upgradepilot.workspace.checkpoint_store import CheckpointStore
target = ExactInvestigationTarget(**json.loads(sys.argv[3]))
boundary = read_native_boundary(Path(sys.argv[2]).read_bytes(), expected_target=target)
store = CheckpointStore.open(Path(sys.argv[1]), busy_timeout_ms=3000)
print('ready', flush=True)
sys.stdin.readline()
try:
    receipt = store.publish(CheckpointRevision('main', sys.argv[4], 'initial', boundary))
    print('published:' + receipt.revision_id, flush=True)
except CheckpointStorageError as error:
    print(error.reason, flush=True)
"""

_OFFLINE_CHILD = r"""
import json, socket, sys
from pathlib import Path
from unittest.mock import patch
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.checkpoint_revision import CheckpointStorageError
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget, encode_native_boundary
from upgradepilot.github.repository import GitHubRepositoryClient
from upgradepilot.upstream.support_drop import evaluate_support_drop_runtime
from upgradepilot.ci.dependency_state import evaluate_runtime_dependency_state
from upgradepilot.maintainer_action import synthesize_maintainer_action
forbidden_prefixes = (
    'upgradepilot.github.', 'upgradepilot.pypi.', 'upgradepilot.ci.',
    'upgradepilot.impact.', 'upgradepilot.target.', 'upgradepilot.upstream.',
    'upgradepilot.dependency.', 'upgradepilot.investigation',
    'upgradepilot.maintainer_action', 'upgradepilot.report_projection',
    'upgradepilot.workspace.native_projection', 'upgradepilot.workspace.native_codecs',
    'requests.', 'httpx.', 'openai.',
)
def guard(frame, event, arg):
    if event == 'call':
        module = frame.f_globals.get('__name__') or ''
        if module.startswith(forbidden_prefixes) and not frame.f_code.co_name.startswith('__'):
            raise RuntimeError('forbidden storage re-entry: ' + module + '.' + frame.f_code.co_name)
target = ExactInvestigationTarget(**json.loads(sys.argv[2]))
sys.setprofile(guard)
with patch.object(socket.socket, 'connect', side_effect=AssertionError('network forbidden')):
    if len(sys.argv) in (5, 6):
        try:
            operation = sys.argv[5] if len(sys.argv) == 6 else 'read'
            store = CheckpointStore.open(Path(sys.argv[1]), read_only=operation != 'publish')
            if operation == 'read':
                store.read_revision('main', 'second', expected_target=target)
            else:
                from upgradepilot.workspace.checkpoint_revision import CheckpointRevision
                from upgradepilot.workspace.native_boundary import read_native_boundary
                boundary = read_native_boundary(Path(sys.argv[3]).read_bytes(), expected_target=target)
                revision = CheckpointRevision('main', 'third', 'second', boundary)
                if operation == 'inspect': store.inspect_publication(revision)
                elif operation == 'publish': store.publish(revision)
                else: raise AssertionError('unknown storage control')
        except CheckpointStorageError as error:
            assert error.reason == sys.argv[4], error
            result = {'refusal': error.reason}
        else: raise AssertionError('cold inconsistency was accepted')
    else:
        store = CheckpointStore.open(Path(sys.argv[1]), read_only=True)
        restored = store.read_revision('main', 'second', expected_target=target)
        status = store.inspect_publication(restored.revision)
        backup = store.backup(Path(sys.argv[3]))
        copied = CheckpointStore.open(Path(sys.argv[3]), read_only=True).read_revision('main', 'second', expected_target=target)
        assert restored == copied
        assert backup.revision_count == 2
        data = encode_native_boundary(copied.revision.boundary)
        result = {'digest': __import__('hashlib').sha256(data).hexdigest(), 'status': status}
sys.setprofile(None)
blocked = 0
for call in (
    lambda: GitHubRepositoryClient.get_exact_head_text_file(None, None, None),
    lambda: evaluate_support_drop_runtime(None),
    lambda: evaluate_runtime_dependency_state(None, None, None, source_contexts=()),
    lambda: synthesize_maintainer_action(None),
):
    sys.setprofile(guard)
    try: call()
    except RuntimeError as error:
        assert str(error).startswith('forbidden storage re-entry:'), error
        blocked += 1
    finally: sys.setprofile(None)
assert blocked == 4
result['blocked'] = blocked
print(json.dumps(result))
"""


class WorkspaceCheckpointStoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.boundary = captured_case()[2]
        cls.target_json = json.dumps(
            json.loads(encode_native_boundary(cls.boundary))["target"]
        )

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="upgradepilot-store-proof-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.store = CheckpointStore.create(self.root / "store")
        self.initial = CheckpointRevision("main", "initial", None, self.boundary)

    def _next(self, *, revision_id="second", boundary=None, predecessor="initial"):
        return CheckpointRevision(
            "main", revision_id, predecessor, boundary or self.boundary
        )

    def _read(self, revision_id="initial", store=None):
        return (store or self.store).read_revision(
            "main", revision_id, expected_target=self.boundary.target
        )

    def _database(self):
        return sqlite3.connect(
            self.store.directory / "workspace.sqlite3", isolation_level=None
        )

    def _assert_reason(self, reason, call):
        with self.assertRaises(CheckpointStorageError) as raised:
            call()
        self.assertEqual(raised.exception.reason, reason)
        return raised.exception

    def _fresh_ids(self, boundary=None, suffix="new"):
        boundary = boundary or self.boundary
        ids = {r.record_id: r.record_id + suffix for r in boundary.records}
        return replace(
            boundary,
            records=tuple(
                replace(
                    r,
                    record_id=ids[r.record_id],
                    input_record_ids=tuple(ids[i] for i in r.input_record_ids),
                )
                for r in boundary.records
            ),
        )

    def _damage(self, table, statement, values=()):
        # Test-only damage bypasses immutable triggers; restore the exact catalog afterward
        # so content/reference controls must detect corruption independently of schema checks.
        with self._database() as db:
            triggers = list(
                db.execute(
                    "SELECT name,sql FROM sqlite_schema WHERE type='trigger' AND tbl_name=?",
                    (table,),
                )
            )
            for name, _ in triggers:
                db.execute(f'DROP TRIGGER "{name}"')
            db.execute(statement, values)
            for _, sql in triggers:
                db.execute(sql)

    def test_missing_head_distinguishes_absent_and_damaged_lineage(self):
        with self.subTest(state="no head and no revisions"):
            self._assert_reason("missing_checkpoint_revision", self._read)

        self.store.publish(self.initial)
        with self.subTest(state="valid lineage, selected revision absent"):
            self._assert_reason(
                "missing_checkpoint_revision", lambda: self._read("unpublished")
            )

        self._damage("heads", "DELETE FROM heads")
        for selected in ("initial", "unpublished"):
            with self.subTest(
                state="retained revisions without head", selected=selected
            ):
                self._assert_reason(
                    "invalid_checkpoint_storage", lambda: self._read(selected)
                )

    def test_retained_views_membership_payloads_and_lineage_scope_are_immutable(self):
        receipt = self.store.publish(self.initial)
        view = self._read()
        self.store.publish(self._next())
        self.assertEqual(receipt.revision_digest, self.initial.digest())
        self.assertEqual(view.revision, self.initial)
        self.assertEqual(view.excluded_successor_ids, ())
        later_view = self._read()
        self.assertEqual(later_view.excluded_successor_ids, ("second",))
        self.assertEqual(later_view.revision, view.revision)
        with self.assertRaises(FrozenInstanceError):
            view.revision.revision_id = "mutated"
        with self._database() as db:
            self.assertEqual(
                db.execute("SELECT count(*) FROM records").fetchone()[0], 11
            )
            self.assertEqual(
                db.execute("SELECT count(*) FROM revision_members").fetchone()[0], 22
            )
            for table in (
                "records",
                "payloads",
                "revisions",
                "revision_members",
                "record_inputs",
            ):
                with self.assertRaises(sqlite3.IntegrityError):
                    db.execute(f"DELETE FROM {table}")
        other = replace(self.initial, lineage_id="other")
        self.store.publish(other)
        with self._database() as db:
            self.assertEqual(
                db.execute("SELECT count(*) FROM records").fetchone()[0], 22
            )

    def test_new_record_identity_shares_payload_without_cross_lineage_deduplication(
        self,
    ):
        self.store.publish(self.initial)
        with self._database() as db:
            before = db.execute("SELECT count(*) FROM payloads").fetchone()[0]
        fresh = self._fresh_ids()
        self.store.publish(self._next(boundary=fresh))
        self.assertEqual(self._read("second").revision.boundary, fresh)
        with self._database() as db:
            self.assertEqual(
                db.execute("SELECT count(*) FROM payloads").fetchone()[0], before
            )
            self.assertEqual(
                db.execute("SELECT count(*) FROM records").fetchone()[0], 22
            )

    def test_stale_and_root_predecessors_conflict_without_changing_history(self):
        self.store.publish(self.initial)
        self.store.publish(self._next())
        error = self._assert_reason(
            "publication_conflict",
            lambda: self.store.publish(self._next(revision_id="loser")),
        )
        self.assertEqual((error.expected, error.actual), ("initial", "second"))
        self._assert_reason(
            "publication_conflict",
            lambda: self.store.publish(replace(self.initial, revision_id="root2")),
        )
        self.assertEqual(
            self.store.inspect_publication(self._next(revision_id="loser")),
            "not_published",
        )
        self.assertEqual(self._read("second").revision, self._next())

    def test_absent_publication_requires_coherent_lineage(self):
        self.assertEqual(self.store.inspect_publication(self.initial), "not_published")
        self.store.publish(self.initial)
        self.store.publish(self._next())
        absent = self._next(revision_id="third", predecessor="second")
        self.assertEqual(self.store.inspect_publication(absent), "not_published")
        variants = (
            ("heads", "DELETE FROM heads"),
            ("heads", "UPDATE heads SET revision_id='missing'"),
            (
                "revisions",
                "UPDATE revisions SET predecessor_id='second' WHERE revision_id='initial'",
            ),
        )
        for index, (table, sql) in enumerate(variants):
            with self.subTest(damage=sql):
                directory = self.root / ("absent-lineage-" + str(index))
                self.store.backup(directory)
                original = self.store
                self.store = CheckpointStore.open(directory)
                try:
                    self._damage(table, sql)
                    self._assert_reason(
                        "invalid_checkpoint_storage",
                        lambda: self.store.inspect_publication(absent),
                    )
                finally:
                    self.store = original

    def test_absent_publication_validates_staged_revision(self):
        damaged = replace(
            self.boundary,
            records=(replace(self.boundary.records[0], payload_digest="wrong"),)
            + self.boundary.records[1:],
        )
        variants = (
            (replace(self.initial, lineage_id=""), "invalid_revision"),
            (replace(self.initial, revision_id=""), "invalid_revision"),
            (replace(self.initial, predecessor_id="initial"), "invalid_revision"),
            (replace(self.initial, boundary=damaged), "invalid_revision"),
            (
                replace(self.initial, boundary=replace(self.boundary, records=())),
                "storage_resource_limit",
            ),
        )
        for revision, reason in variants:
            with self.subTest(reason=reason, revision_id=revision.revision_id):
                self._assert_reason(
                    reason, lambda: self.store.inspect_publication(revision)
                )
        self.assertEqual(self.store.inspect_publication(self.initial), "not_published")

    def test_absent_publication_refuses_invalid_head_material(self):
        self.store.publish(self.initial)
        self.store.publish(self._next())
        absent = self._next(revision_id="third", predecessor="second")
        variants = (
            (
                "revisions",
                "UPDATE revisions SET digest='damaged-head' WHERE revision_id='second'",
                (),
            ),
            (
                "payloads",
                "UPDATE payloads SET body=? WHERE digest=?",
                (b"damaged-head-material", self.boundary.records[0].payload_digest),
            ),
        )
        for index, (table, sql, values) in enumerate(variants):
            with self.subTest(damage=table):
                directory = self.root / ("absent-head-material-" + str(index))
                self.store.backup(directory)
                original = self.store
                self.store = CheckpointStore.open(directory)
                try:
                    self._damage(table, sql, values)
                    if table == "revisions":
                        # A coherent selected A remains inspectable despite B's bad digest.
                        self.assertEqual(
                            self.store.inspect_publication(self.initial), "published"
                        )
                    self._assert_reason(
                        "invalid_checkpoint_storage",
                        lambda: self.store.inspect_publication(absent),
                    )
                finally:
                    self.store = original

    def test_successor_refuses_corrupt_retained_history_with_intact_head(self):
        # Distinct IDs AND payloads isolate A's material from B's shared storage closure.
        fresh = self._fresh_ids()
        records = []
        for record in fresh.records:
            body = record.payload + b" "
            records.append(
                replace(record, payload=body, payload_digest=sha256(body).hexdigest())
            )
        second = self._next(boundary=replace(fresh, records=tuple(records)))
        third = replace(second, revision_id="third", predecessor_id="second")
        self.store.publish(self.initial)
        self.store.publish(second)
        variants = (
            (
                "revisions",
                "UPDATE revisions SET digest='damaged' WHERE revision_id='initial'",
                (),
            ),
            (
                "payloads",
                "UPDATE payloads SET body=? WHERE digest=?",
                (b"damaged", self.boundary.records[0].payload_digest),
            ),
            (
                "records",
                "UPDATE records SET metadata=? WHERE record_id=?",
                (b"{}", self.boundary.records[0].record_id),
            ),
            (
                "record_inputs",
                "DELETE FROM record_inputs WHERE record_id=?",
                (self.boundary.records[1].record_id,),
            ),
            (
                "revision_members",
                "DELETE FROM revision_members WHERE revision_id='initial' AND position=0",
                (),
            ),
        )
        for index, (table, sql, values) in enumerate(variants):
            with self.subTest(damage=table):
                directory = self.root / ("historical-damage-" + str(index))
                self.store.backup(directory)
                original = self.store
                self.store = CheckpointStore.open(directory)
                try:
                    self._damage(table, sql, values)
                    self.assertEqual(self._read("second").revision, second)
                    self.assertEqual(
                        self.store.inspect_publication(second), "published"
                    )
                    self._assert_reason("invalid_checkpoint_storage", self._read)
                    with self._database() as db:
                        before = tuple(
                            db.execute(f"SELECT count(*) FROM {name}").fetchone()[0]
                            for name in (
                                "revisions",
                                "records",
                                "payloads",
                                "revision_members",
                                "record_inputs",
                            )
                        )
                    self._assert_reason(
                        "invalid_checkpoint_storage", lambda: self.store.publish(third)
                    )
                    self.assertEqual(self._read("second").head_revision_id, "second")
                    self.assertEqual(
                        self.store.inspect_publication(third), "not_published"
                    )
                    with self._database() as db:
                        after = tuple(
                            db.execute(f"SELECT count(*) FROM {name}").fetchone()[0]
                            for name in (
                                "revisions",
                                "records",
                                "payloads",
                                "revision_members",
                                "record_inputs",
                            )
                        )
                    self.assertEqual(after, before)
                    # Refusal is scoped to the lineage being extended, not unrelated history.
                    other = replace(self.initial, lineage_id="unaffected")
                    self.store.publish(other)
                    self.assertEqual(self.store.inspect_publication(other), "published")
                finally:
                    self.store = original

    def test_failed_create_sqlite_full_cleans_only_exclusively_created_files(self):
        directory = self.root / "failed-create"
        directory.mkdir(mode=0o700)
        sentinel = directory / "retained-user-file"
        sentinel.write_bytes(b"keep")
        real_connect = sqlite3.connect
        initialized_tables = []
        sqlite_failures = []

        class InitializationFull(sqlite3.Connection):
            def execute(self, sql, parameters=()):
                if sql.startswith("CREATE TABLE records"):
                    # Real engine exhaustion after the first table was created in the transaction.
                    pages = super().execute("PRAGMA page_count").fetchone()[0]
                    super().execute(f"PRAGMA max_page_count={pages}")
                try:
                    result = super().execute(sql, parameters)
                except sqlite3.Error as error:
                    sqlite_failures.append(error.sqlite_errorcode)
                    raise
                if sql.startswith("CREATE TABLE"):
                    initialized_tables.append(sql)
                return result

        with patch(
            "sqlite3.connect",
            lambda *a, **k: real_connect(*a, factory=InitializationFull, **k),
        ):
            self._assert_reason(
                "storage_full", lambda: CheckpointStore.create(directory)
            )
        self.assertEqual(len(initialized_tables), 1)
        self.assertEqual(sqlite_failures, [sqlite3.SQLITE_FULL])
        self.assertEqual(list(directory.iterdir()), [sentinel])
        self.assertEqual(sentinel.read_bytes(), b"keep")
        retried = CheckpointStore.create(directory)
        retried.publish(self.initial)
        self.assertEqual(self._read(store=retried).revision, self.initial)

    def test_failed_create_after_commit_cleans_new_store_and_preserves_existing_store(
        self,
    ):
        directory = self.root / "failed-verification"
        with patch(
            "upgradepilot.workspace.checkpoint_store._verify_schema",
            side_effect=CheckpointStorageError("controlled_validation", "fail"),
        ):
            self._assert_reason(
                "controlled_validation", lambda: CheckpointStore.create(directory)
            )
        self.assertEqual(list(directory.iterdir()), [])
        CheckpointStore.create(directory)
        self.store.publish(self.initial)
        self._assert_reason(
            "store_already_exists", lambda: CheckpointStore.create(self.store.directory)
        )
        self.assertEqual(self._read().revision, self.initial)

    def test_create_refuses_preexisting_sidecars_without_touching_them(self):
        for suffix in ("-wal", "-shm"):
            with self.subTest(suffix=suffix):
                directory = self.root / ("preexisting" + suffix)
                directory.mkdir(mode=0o700)
                sidecar = directory / ("workspace.sqlite3" + suffix)
                sidecar.write_bytes(b"existing-host-file")
                self._assert_reason(
                    "store_already_exists", lambda: CheckpointStore.create(directory)
                )
                self.assertEqual(list(directory.iterdir()), [sidecar])
                self.assertEqual(sidecar.read_bytes(), b"existing-host-file")

    def test_cold_absence_and_historical_publication_refusals_keep_guards_active(self):
        self.store.publish(self.initial)
        self.store.publish(self._next())
        data = self.root / "staged.json"
        data.write_bytes(encode_native_boundary(self.boundary))
        variants = (
            ("inspect", "heads", "DELETE FROM heads"),
            (
                "publish",
                "revisions",
                "UPDATE revisions SET digest='damaged' WHERE revision_id='initial'",
            ),
        )
        for operation, table, sql in variants:
            with self.subTest(operation=operation):
                directory = self.root / ("cold-audit-" + operation)
                self.store.backup(directory)
                original = self.store
                self.store = CheckpointStore.open(directory)
                try:
                    self._damage(table, sql)
                finally:
                    self.store = original
                child = subprocess.run(
                    [
                        sys.executable,
                        "-c",
                        _OFFLINE_CHILD,
                        str(directory),
                        self.target_json,
                        str(data),
                        "invalid_checkpoint_storage",
                        operation,
                    ],
                    capture_output=True,
                    text=True,
                    timeout=20,
                )
                self.assertEqual(child.returncode, 0, child.stderr)
                self.assertEqual(
                    json.loads(child.stdout),
                    {"blocked": 4, "refusal": "invalid_checkpoint_storage"},
                )

    def test_duplicate_revision_and_changed_record_identity_are_refused(self):
        self.store.publish(self.initial)
        self._assert_reason(
            "invalid_revision",
            lambda: self.store.publish(self._next(revision_id="initial")),
        )
        record = self.boundary.records[0]
        for name, value in (
            ("owner", "substituted-owner"),
            ("producer_method", "changed"),
            ("retention_gaps", ("different",)),
        ):
            with self.subTest(field=name):
                changed = replace(
                    self.boundary,
                    records=(replace(record, **{name: value}),)
                    + self.boundary.records[1:],
                )
                self._assert_reason(
                    "immutable_identity_conflict",
                    lambda: self.store.publish(self._next(boundary=changed)),
                )
        self.assertEqual(self._read().revision, self.initial)
        self.store.publish(self._next())
        self._assert_reason(
            "immutable_identity_conflict",
            lambda: self.store.publish(
                self._next(revision_id="initial", predecessor="second")
            ),
        )

    def test_payload_digest_identity_collision_refuses_even_with_valid_boundary_digest(
        self,
    ):
        self.store.publish(self.initial)
        record = self.boundary.records[0]
        self._damage(
            "payloads",
            "UPDATE payloads SET body=? WHERE lineage_id=? AND digest=?",
            (b"substituted", "main", record.payload_digest),
        )
        self._assert_reason("invalid_checkpoint_storage", self._read)
        self._assert_reason(
            "invalid_checkpoint_storage", lambda: self.store.publish(self._next())
        )

    def test_missing_scope_cycle_and_dangling_material_refuse_before_publication(self):
        root = self.boundary.records[0]
        variants = (
            replace(self.boundary, records=self.boundary.records[1:]),
            replace(
                self.boundary,
                records=(
                    replace(
                        root, input_record_ids=(self.boundary.records[1].record_id,)
                    ),
                )
                + self.boundary.records[1:],
            ),
            replace(
                self.boundary,
                records=(replace(root, target=replace(root.target, head_sha="other")),)
                + self.boundary.records[1:],
            ),
        )
        for boundary in variants:
            with self.subTest(boundary=boundary.records[0].family):
                self._assert_reason(
                    "invalid_revision",
                    lambda: self.store.publish(
                        replace(self.initial, boundary=boundary)
                    ),
                )
        self.assertEqual(self.store.inspect_publication(self.initial), "not_published")

    def test_target_change_cannot_silently_rebase_lineage(self):
        self.store.publish(self.initial)
        target = replace(self.boundary.target, head_sha="other-head")
        changed = self._fresh_ids(
            replace(
                self.boundary,
                target=target,
                records=tuple(replace(r, target=target) for r in self.boundary.records),
            )
        )
        self._assert_reason(
            "wrong_target", lambda: self.store.publish(self._next(boundary=changed))
        )
        self._assert_reason(
            "wrong_target",
            lambda: self.store.read_revision("main", "initial", expected_target=target),
        )
        self.assertEqual(self._read().revision, self.initial)

    def test_unsupported_native_versions_are_retained_without_decoder_dispatch(self):
        records = tuple(
            replace(r, codec_version=999, producer_version="future-semantic")
            for r in self.boundary.records
        )
        revision = replace(
            self.initial, boundary=replace(self.boundary, records=records)
        )
        self.store.publish(revision)
        self.assertEqual(self._read().revision, revision)

    def test_schema_refusal_and_catalog_damage_do_not_auto_initialize_or_migrate(self):
        self.store.publish(self.initial)
        for pragma, value in (("user_version", 99), ("application_id", 123)):
            with self.subTest(pragma=pragma), self._database() as db:
                original = db.execute(f"PRAGMA {pragma}").fetchone()[0]
                db.execute(f"PRAGMA {pragma}={value}")
                self._assert_reason(
                    "unsupported_storage_schema",
                    lambda: CheckpointStore.open(self.store.directory),
                )
                self.assertEqual(db.execute(f"PRAGMA {pragma}").fetchone()[0], value)
                db.execute(f"PRAGMA {pragma}={original}")
        with self._database() as db:
            db.execute("DROP TRIGGER immutable_records_update")
        self._assert_reason(
            "invalid_checkpoint_storage",
            lambda: CheckpointStore.open(self.store.directory),
        )
        self._assert_reason(
            "store_already_exists", lambda: CheckpointStore.create(self.store.directory)
        )

    def test_store_location_permissions_and_missing_database_are_explicit(self):
        self._assert_reason(
            "unsupported_store_location",
            lambda: CheckpointStore.create(
                Path(__file__).resolve().parents[1] / "forbidden-store"
            ),
        )
        public = self.root / "public"
        public.mkdir(mode=0o755)
        self._assert_reason(
            "unsupported_store_location", lambda: CheckpointStore.create(public)
        )
        link = self.root / "linked"
        link.symlink_to(self.store.directory, target_is_directory=True)
        self._assert_reason(
            "unsupported_store_location", lambda: CheckpointStore.open(link)
        )
        missing = self.root / "missing"
        missing.mkdir(mode=0o700)
        self._assert_reason("storage_io_error", lambda: CheckpointStore.open(missing))
        self.assertFalse((missing / "workspace.sqlite3").exists())
        self._assert_reason(
            "unsupported_storage_settings",
            lambda: CheckpointStore.open(self.store.directory, busy_timeout_ms=5001),
        )

    def test_required_settings_are_verified_and_silent_fallback_refused(self):
        with self.store._connection() as db:
            self.assertEqual(db.execute("PRAGMA journal_mode").fetchone(), ("wal",))
            self.assertEqual(db.execute("PRAGMA synchronous").fetchone(), (2,))
            self.assertEqual(db.execute("PRAGMA foreign_keys").fetchone(), (1,))
            self.assertEqual(db.execute("PRAGMA busy_timeout").fetchone(), (1000,))
        real_connect = sqlite3.connect

        class Fallback(sqlite3.Connection):
            def execute(self, sql, parameters=()):
                return super().execute(
                    "PRAGMA synchronous=OFF"
                    if sql == "PRAGMA synchronous=FULL"
                    else sql,
                    parameters,
                )

        with patch(
            "sqlite3.connect", lambda *a, **k: real_connect(*a, factory=Fallback, **k)
        ):
            self._assert_reason(
                "unsupported_storage_settings",
                lambda: CheckpointStore.open(self.store.directory),
            )

    def test_bounded_actual_busy_and_read_only_refusal_preserve_previous_head(self):
        self.store.publish(self.initial)
        with self._database() as writer:
            writer.execute("BEGIN IMMEDIATE")
            fast = CheckpointStore.open(self.store.directory, busy_timeout_ms=10)
            self._assert_reason("storage_busy", lambda: fast.publish(self._next()))
            writer.execute("ROLLBACK")
        reader = CheckpointStore.open(self.store.directory, read_only=True)
        self._assert_reason("storage_read_only", lambda: reader.publish(self._next()))
        with reader._connection() as db:
            with self.assertRaises(sqlite3.OperationalError) as raised:
                db.execute("INSERT INTO heads VALUES ('forbidden','missing')")
            self.assertEqual(
                raised.exception.sqlite_errorcode & 255, sqlite3.SQLITE_READONLY
            )
        self.assertEqual(self._read().revision, self.initial)

    def test_actual_sqlite_full_rolls_back_all_unpublished_material(self):
        self.store.publish(self.initial)
        fresh = self._fresh_ids()
        body = json_bytes({"capacity_control": "x" * (2 * 1024 * 1024)})
        fresh = replace(
            fresh,
            records=(
                replace(
                    fresh.records[0],
                    payload=body,
                    payload_digest=sha256(body).hexdigest(),
                ),
            )
            + fresh.records[1:],
        )
        real_connect = sqlite3.connect

        class Full(sqlite3.Connection):
            def execute(self, sql, parameters=()):
                if sql == "BEGIN IMMEDIATE":
                    pages = super().execute("PRAGMA page_count").fetchone()[0]
                    super().execute(f"PRAGMA max_page_count={pages}")
                return super().execute(sql, parameters)

        with patch(
            "sqlite3.connect", lambda *a, **k: real_connect(*a, factory=Full, **k)
        ):
            self._assert_reason(
                "storage_full", lambda: self.store.publish(self._next(boundary=fresh))
            )
        self.assertEqual(self._read().revision, self.initial)
        with self._database() as db:
            self.assertEqual(
                db.execute("SELECT count(*) FROM records").fetchone()[0], 11
            )
            self.assertEqual(
                db.execute("SELECT count(*) FROM revisions").fetchone()[0], 1
            )

    def test_unconfirmed_commit_and_lost_acknowledgement_require_identity_reconciliation(
        self,
    ):
        self.store.publish(self.initial)
        real_connect = sqlite3.connect

        class CommitError(sqlite3.Connection):
            def execute(self, sql, parameters=()):
                if sql == "COMMIT":
                    raise sqlite3.OperationalError(
                        "controlled commit acknowledgement error"
                    )
                return super().execute(sql, parameters)

        with patch(
            "sqlite3.connect",
            lambda *a, **k: real_connect(*a, factory=CommitError, **k),
        ):
            with self.assertRaises(UnconfirmedPublication) as raised:
                self.store.publish(self._next())
        self.assertEqual(raised.exception.revision_id, "second")
        self.assertEqual(self.store.inspect_publication(self._next()), "not_published")
        with patch(
            "upgradepilot.workspace.checkpoint_store.PublicationReceipt",
            side_effect=RuntimeError("lost ack"),
        ):
            with self.assertRaises(UnconfirmedPublication):
                self.store.publish(self._next())
        self.assertEqual(self.store.inspect_publication(self._next()), "published")
        self._assert_reason(
            "publication_conflict", lambda: self.store.publish(self._next())
        )
        inconsistent = replace(self._next(), boundary=self._fresh_ids())
        self._assert_reason(
            "immutable_identity_conflict",
            lambda: self.store.inspect_publication(inconsistent),
        )

    def test_real_process_interruptions_leave_only_previous_or_complete_successor(self):
        self.store.publish(self.initial)
        stages = (
            "before_begin",
            "after_payload",
            "after_record",
            "after_reference",
            "after_revision",
            "after_membership",
            "after_head",
            "before_commit",
            "after_commit",
            "after_ack",
        )
        for stage in stages:
            with self.subTest(stage=stage):
                directory = self.root / stage
                store = CheckpointStore.create(directory)
                store.publish(self.initial)
                successor = self._next(boundary=self._fresh_ids(suffix=stage))
                first = successor.boundary.records[0]
                new_body = first.payload + b" "
                successor = replace(
                    successor,
                    boundary=replace(
                        successor.boundary,
                        records=(
                            replace(
                                first,
                                payload=new_body,
                                payload_digest=sha256(new_body).hexdigest(),
                            ),
                        )
                        + successor.boundary.records[1:],
                    ),
                )
                data = self.root / (stage + ".json")
                data.write_bytes(encode_native_boundary(successor.boundary))
                child = subprocess.run(
                    [
                        sys.executable,
                        "-c",
                        _INTERRUPT_CHILD,
                        str(directory),
                        str(data),
                        self.target_json,
                        stage,
                        "second",
                        "initial",
                    ],
                    capture_output=True,
                    text=True,
                    timeout=15,
                )
                self.assertEqual(child.returncode, -9, child.stderr)
                published = stage in ("after_commit", "after_ack")
                self.assertEqual(
                    store.inspect_publication(successor),
                    "published" if published else "not_published",
                )
                self.assertEqual(
                    store.read_revision(
                        "main", "initial", expected_target=self.boundary.target
                    ).revision,
                    self.initial,
                )
                receipt = store.backup(self.root / (stage + "-backup"))
                self.assertEqual(receipt.revision_count, 2 if published else 1)
                if stage == "after_ack":
                    self.assertEqual(
                        json.loads(child.stdout)["digest"], successor.digest()
                    )

    def test_intent_publication_survives_termination_without_inventing_observation(
        self,
    ):
        # Opaque host-created intent fixture: storage retains these bytes; lifecycle codec,
        # capability admission/execution and combined native recovery are deliberately absent.
        body = json_bytes({"attempt_id": "controlled-attempt", "completion": "unknown"})
        intent = CapturedNativeRecord(
            "intent-record",
            "host_attempt",
            "workspace.host",
            1,
            self.boundary.target,
            (self.boundary.records[0].record_id,),
            body,
            sha256(body).hexdigest(),
            "recorded",
            "controlled-host-intent",
            None,
            ("producer_version_unavailable",),
        )
        revision = replace(
            self.initial,
            boundary=replace(self.boundary, records=self.boundary.records + (intent,)),
        )
        for stage in ("before_commit", "after_commit"):
            with self.subTest(stage=stage):
                store = CheckpointStore.create(self.root / (stage + "-intent"))
                data = self.root / (stage + "-intent.json")
                data.write_bytes(encode_native_boundary(revision.boundary))
                child = subprocess.run(
                    [
                        sys.executable,
                        "-c",
                        _INTERRUPT_CHILD,
                        str(store.directory),
                        str(data),
                        self.target_json,
                        stage,
                        "initial",
                        "",
                    ],
                    capture_output=True,
                    text=True,
                    timeout=15,
                )
                self.assertEqual(child.returncode, -9, child.stderr)
                if stage == "after_commit":
                    recovered = store.read_revision(
                        "main", "initial", expected_target=self.boundary.target
                    )
                    self.assertEqual(
                        recovered.revision.boundary.records[-1].payload, body
                    )
                    self.assertEqual(store.inspect_publication(revision), "published")
                else:
                    self.assertEqual(
                        store.inspect_publication(revision), "not_published"
                    )

    def test_two_real_writers_one_successor_and_one_conflict(self):
        self.store.publish(self.initial)
        data = self.root / "writers.json"
        data.write_bytes(encode_native_boundary(self.boundary))
        children = [
            subprocess.Popen(
                [
                    sys.executable,
                    "-c",
                    _WRITER_CHILD,
                    str(self.store.directory),
                    str(data),
                    self.target_json,
                    identity,
                ],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            for identity in ("writer-a", "writer-b")
        ]
        try:
            for child in children:
                self.assertEqual(child.stdout.readline().strip(), "ready")
            for child in children:
                child.stdin.write("go\n")
                child.stdin.flush()
            results = []
            for child in children:
                out, err = child.communicate(timeout=15)
                self.assertEqual(child.returncode, 0, err)
                results.append(out.strip())
            self.assertEqual(
                sum(value.startswith("published:") for value in results), 1, results
            )
            self.assertEqual(results.count("publication_conflict"), 1, results)
        finally:
            for child in children:
                if child.poll() is None:
                    child.kill()
                    child.wait()
        self.assertEqual(
            self.store.backup(self.root / "writers-backup").revision_count, 2
        )

    def test_damaged_metadata_references_membership_header_and_head_are_refused(self):
        variants = (
            (
                "records",
                "UPDATE records SET metadata=? WHERE record_id=?",
                (b"{}", self.boundary.records[0].record_id),
            ),
            (
                "record_inputs",
                "DELETE FROM record_inputs WHERE record_id=?",
                (self.boundary.records[1].record_id,),
            ),
            ("revision_members", "DELETE FROM revision_members WHERE position=0", ()),
            ("revisions", "UPDATE revisions SET digest='wrong'", ()),
            ("heads", "UPDATE heads SET revision_id='missing'", ()),
        )
        self.store.publish(self.initial)
        for index, (table, sql, args) in enumerate(variants):
            with self.subTest(table=table):
                copy = self.root / ("damaged-" + str(index))
                self.store.backup(copy)
                original = self.store
                self.store = CheckpointStore.open(copy)
                try:
                    self._damage(table, sql, args)
                    with self.assertRaises(CheckpointStorageError):
                        self._read()
                    with self.assertRaises(CheckpointStorageError):
                        self.store.backup(self.root / ("refused-backup-" + str(index)))
                    self.assertFalse(
                        (
                            self.root
                            / ("refused-backup-" + str(index))
                            / "workspace.sqlite3"
                        ).exists()
                    )
                finally:
                    self.store = original

    def test_backup_validates_every_revision_and_restores_explicit_earlier_loss(self):
        self.store.publish(self.initial)
        self.store.publish(self._next())
        self.store.publish(self._next(revision_id="third", predecessor="second"))
        backup = self.root / "backup"
        receipt = self.store.backup(backup)
        self.assertEqual(receipt.revision_count, 3)
        self.assertEqual(receipt.lineage_heads, (("main", "third"),))
        restored = CheckpointStore.open(backup, read_only=True)
        self.assertEqual(self._read("third", restored), self._read("third"))
        earlier = self._read("initial", restored)
        self.assertEqual(earlier.excluded_successor_ids, ("second", "third"))
        self._assert_reason("store_already_exists", lambda: self.store.backup(backup))
        self.assertEqual(self._read("third").revision.revision_id, "third")
        self._damage(
            "revisions",
            "UPDATE revisions SET digest='damaged-historical' WHERE revision_id='initial'",
        )
        self._assert_reason(
            "invalid_checkpoint_storage",
            lambda: self.store.backup(self.root / "bad-history"),
        )
        # Unaffected latest material remains inspectable; whole-history backup must refuse.
        self.assertEqual(self._read("third").revision.revision_id, "third")

    def test_backup_includes_uncheckpointed_wal_and_does_not_replace_source(self):
        self.store.publish(self.initial)
        with self._database() as held:
            held.execute("PRAGMA wal_autocheckpoint=0")
            held.execute("BEGIN")
            held.execute("SELECT count(*) FROM revisions").fetchone()
            self.store.publish(self._next())
            self.assertTrue((self.store.directory / "workspace.sqlite3-wal").exists())
            receipt = self.store.backup(self.root / "wal-backup")
            self.assertEqual(receipt.revision_count, 2)
            self.assertEqual(self._read("second").revision, self._next())

    def test_backup_failure_keeps_source_and_removes_only_new_destination(self):
        self.store.publish(self.initial)
        with patch.object(
            CheckpointStore,
            "_validate_catalog",
            side_effect=CheckpointStorageError("controlled_validation", "fail"),
        ):
            self._assert_reason(
                "controlled_validation",
                lambda: self.store.backup(self.root / "failed-backup"),
            )
        self.assertFalse((self.root / "failed-backup" / "workspace.sqlite3").exists())
        self.assertEqual(self._read().revision, self.initial)
        self._assert_reason(
            "store_already_exists", lambda: self.store.backup(self.store.directory)
        )
        self.assertEqual(self._read().revision, self.initial)

    def test_cold_backup_restore_inspection_is_guarded_without_native_reconstruction(
        self,
    ):
        self.store.publish(self.initial)
        self.store.publish(self._next())
        child = subprocess.run(
            [
                sys.executable,
                "-c",
                _OFFLINE_CHILD,
                str(self.store.directory),
                self.target_json,
                str(self.root / "cold-backup"),
            ],
            capture_output=True,
            text=True,
            timeout=20,
        )
        self.assertEqual(child.returncode, 0, child.stderr)
        result = json.loads(child.stdout)
        self.assertEqual(
            result["digest"], sha256(encode_native_boundary(self.boundary)).hexdigest()
        )
        self.assertEqual((result["status"], result["blocked"]), ("published", 4))

    def test_actual_filesystem_read_only_publication_has_no_successor(self):
        import os

        if os.geteuid() == 0:
            self.skipTest("Root bypasses the filesystem permission control.")
        self.store.publish(self.initial)
        path = self.store.directory / "workspace.sqlite3"
        path.chmod(0o400)
        try:
            self._assert_reason(
                "storage_read_only", lambda: self.store.publish(self._next())
            )
            self.assertEqual(
                self.store.inspect_publication(self._next()), "not_published"
            )
        finally:
            path.chmod(0o600)

    def test_oversized_storage_body_is_refused_before_body_allocation(self):
        self.store.publish(self.initial)
        digest = self.boundary.records[0].payload_digest
        self._damage(
            "payloads",
            "UPDATE payloads SET body=zeroblob(2097152) WHERE digest=?",
            (digest,),
        )
        real_connect = sqlite3.connect
        body_reads = []

        class BoundedRead(sqlite3.Connection):
            def execute(self, sql, parameters=()):
                if sql.startswith("SELECT body FROM payloads"):
                    body_reads.append(sql)
                return super().execute(sql, parameters)

        with patch(
            "upgradepilot.workspace.checkpoint_store.MAX_NATIVE_JSON_BYTES", 1024 * 1024
        ):
            with patch(
                "sqlite3.connect",
                lambda *a, **k: real_connect(*a, factory=BoundedRead, **k),
            ):
                self._assert_reason("storage_resource_limit", self._read)
        self.assertEqual(body_reads, [])

    def test_cold_storage_schema_material_and_reference_refusals_keep_guards_active(
        self,
    ):
        self.store.publish(self.initial)
        self.store.publish(self._next())
        variants = (
            (
                "revisions",
                "UPDATE revisions SET digest='wrong' WHERE revision_id='second'",
                (),
                "invalid_checkpoint_storage",
            ),
            (
                "payloads",
                "DELETE FROM payloads WHERE digest=?",
                (self.boundary.records[0].payload_digest,),
                "missing_checkpoint_material",
            ),
            (
                "records",
                "DELETE FROM records WHERE record_id=?",
                (self.boundary.records[0].record_id,),
                "missing_checkpoint_material",
            ),
            (
                "record_inputs",
                "DELETE FROM record_inputs WHERE record_id=?",
                (self.boundary.records[1].record_id,),
                "invalid_checkpoint_storage",
            ),
            (
                "heads",
                "UPDATE heads SET revision_id='missing'",
                (),
                "invalid_checkpoint_storage",
            ),
            ("schema", "PRAGMA user_version=99", (), "unsupported_storage_schema"),
        )
        for index, (table, sql, values, reason) in enumerate(variants):
            with self.subTest(table=table):
                directory = self.root / ("cold-refusal-" + str(index))
                self.store.backup(directory)
                original = self.store
                self.store = CheckpointStore.open(directory)
                try:
                    self._damage(table, sql, values)
                finally:
                    self.store = original
                child = subprocess.run(
                    [
                        sys.executable,
                        "-c",
                        _OFFLINE_CHILD,
                        str(directory),
                        self.target_json,
                        str(self.root / "unused-backup"),
                        reason,
                    ],
                    capture_output=True,
                    text=True,
                    timeout=20,
                )
                self.assertEqual(child.returncode, 0, child.stderr)
                self.assertEqual(
                    json.loads(child.stdout), {"blocked": 4, "refusal": reason}
                )

    def test_broken_lineage_and_undeclared_orphan_rows_block_publication_and_backup(
        self,
    ):
        self.store.publish(self.initial)
        self.store.publish(self._next())
        variants = (
            (
                "revisions",
                "UPDATE revisions SET predecessor_id='second' WHERE revision_id='initial'",
                (),
            ),
            (
                "revisions",
                "UPDATE revisions SET predecessor_id='missing' WHERE revision_id='second'",
                (),
            ),
            ("heads", "DELETE FROM heads", ()),
        )
        for index, (table, sql, values) in enumerate(variants):
            with self.subTest(table=table, index=index):
                directory = self.root / ("broken-history-" + str(index))
                self.store.backup(directory)
                original = self.store
                self.store = CheckpointStore.open(directory)
                try:
                    self._damage(table, sql, values)
                    with self.assertRaises(CheckpointStorageError):
                        self.store.publish(
                            self._next(revision_id="third", predecessor="second")
                        )
                    with self.assertRaises(CheckpointStorageError):
                        self.store.backup(self.root / ("broken-backup-" + str(index)))
                finally:
                    self.store = original
        with self._database() as db:
            db.execute(
                "INSERT INTO payloads VALUES ('main','orphan',?)", (b"undeclared",)
            )
        self._assert_reason(
            "invalid_checkpoint_storage",
            lambda: self.store.backup(self.root / "orphan-backup"),
        )

    def test_damaged_sqlite_file_refuses_without_creating_replacement(self):
        self.store.publish(self.initial)
        path = self.store.directory / "workspace.sqlite3"
        path.write_bytes(b"controlled corruption")
        self._assert_reason(
            "invalid_checkpoint_storage",
            lambda: CheckpointStore.open(self.store.directory),
        )
        self.assertEqual(path.read_bytes(), b"controlled corruption")


if __name__ == "__main__":
    unittest.main()
