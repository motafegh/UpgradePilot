"""Composed publication/recovery proof before normal host integration.

Native fixtures come from the real controlled producer sequence. Lifecycle records here
are declared boundary stimuli, not claims that a product Investigator executed them.
Children recover only from a store/selection, under independently exercised re-entry guards.
"""

from __future__ import annotations

import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from dataclasses import asdict, replace
from hashlib import sha256
from pathlib import Path
from unittest.mock import patch

from test_workspace_native_reconstruction import (
    _RECOVERY_CONTROLS,
    _RECOVERY_GUARD,
    captured_case,
    independent_native_values,
)

from upgradepilot.workspace.checkpoint_revision import (
    CheckpointRevision,
    CheckpointStorageError,
    UnconfirmedPublication,
)
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.lifecycle_boundary import (
    CapturedLifecycleHistory,
    capture_lifecycle_record,
    encode_lifecycle_history,
    encode_lifecycle_record,
    reconstruct_lifecycle_history,
)
from upgradepilot.workspace.lifecycle_records import (
    AttributedProposal,
    CapabilityObservation,
    CapabilityRequest,
    ConsumerView,
    DiscoveryObjective,
    EvaluationOutcome,
    ExecutionAttempt,
    InvestigationNeed,
    LifecycleMethodIdentity,
    ObservableUse,
    ProceduralTermination,
    RequestAdmission,
    StoppingProposal,
)
from upgradepilot.workspace.native_boundary import encode_native_boundary
from upgradepilot.workspace.native_representation import (
    NativeReconstructionError,
    json_bytes,
)

_COLD_CHILD = (
    _RECOVERY_GUARD
    + r"""
from dataclasses import asdict
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.checkpoint_revision import CheckpointStorageError
from upgradepilot.workspace.lifecycle_boundary import reconstruct_lifecycle_history
selection = json.loads(sys.argv[2])
target = ExactInvestigationTarget(**selection['target'])
result = {}
sys.setprofile(guard)
with patch.object(socket.socket, 'connect', side_effect=AssertionError('network forbidden')):
    try:
        store = CheckpointStore.open(Path(sys.argv[1]), read_only=True)
        stored = store.read_revision('main', selection['revision_id'], expected_target=target)
    except CheckpointStorageError as error:
        result['storage_refusal'] = error.reason
    else:
        revision = stored.revision
        result['revision_digest'] = revision.digest()
        result['excluded'] = list(stored.excluded_successor_ids)
        result['retention'] = stored.lifecycle_recovery_status
        result['ci'] = independent_native_values(reconstruct_ci_projection(revision.boundary, expected_target=target))
        result['python'] = independent_native_values(reconstruct_python_support_projection(revision.boundary, expected_target=target))
        if revision.lifecycle_history is not None:
            bases = {revision.revision_id: revision.boundary}
            for item in revision.lifecycle_history.records:
                if item.basis_revision_id not in bases:
                    bases[item.basis_revision_id] = store.read_revision('main', item.basis_revision_id, expected_target=target).revision.boundary
            try:
                values = reconstruct_lifecycle_history(revision.lifecycle_history, bases=bases)
            except NativeReconstructionError as error:
                result['lifecycle_refusal'] = error.reason
            else:
                result['lifecycle'] = [
                    {'id': item.capture.record_id, 'basis': item.capture.basis_revision_id,
                     'native': list(item.capture.native_record_ids),
                     'predecessors': list(item.capture.predecessor_record_ids),
                     'method': asdict(item.capture.method), 'kind': type(item.value).__name__,
                     'value': asdict(item.value)} for item in values
                ]
    with socket.socket() as connection:
        try: connection.connect(('127.0.0.1', 9))
        except AssertionError as error:
            assert str(error) == 'network forbidden', error
            result['blocked_network'] = 1
        else: raise AssertionError('inactive network guard')
"""
    + _RECOVERY_CONTROLS
)


_PUBLISH_CHILD = r"""
import json, os, signal, sqlite3, sys
from pathlib import Path
from unittest.mock import patch
from upgradepilot.workspace.checkpoint_revision import CheckpointRevision
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget, read_native_boundary
from upgradepilot.workspace.lifecycle_boundary import CapturedLifecycleHistory, read_lifecycle_record
from upgradepilot.workspace.native_representation import json_bytes
target = ExactInvestigationTarget(**json.loads(sys.argv[3]))
packet = json.loads(Path(sys.argv[2]).read_bytes())
boundary = read_native_boundary(packet['native'].encode(), expected_target=target)
history = CapturedLifecycleHistory(tuple(read_lifecycle_record(json_bytes(item)) for item in packet['history']['records']))
stage = sys.argv[4]
real_connect = sqlite3.connect
class Interrupted(sqlite3.Connection):
    def execute(self, sql, parameters=()):
        if stage == 'before_commit' and sql == 'COMMIT': os.kill(os.getpid(), signal.SIGKILL)
        result = super().execute(sql, parameters)
        if ((stage == 'after_record' and sql.startswith('INSERT INTO lifecycle_records'))
            or (stage == 'after_member' and sql.startswith('INSERT INTO revision_lifecycle_members'))
            or (stage == 'after_head' and sql.startswith('UPDATE heads'))
            or (stage == 'after_commit' and sql == 'COMMIT')):
            os.kill(os.getpid(), signal.SIGKILL)
        return result
with patch('sqlite3.connect', lambda *a, **k: real_connect(*a, factory=Interrupted, **k)):
    store = CheckpointStore.open(Path(sys.argv[1]))
    store.publish(CheckpointRevision('main', 'later', 'original', boundary, history))
    raise AssertionError('interruption was not exercised')
"""


class WorkspaceLifecyclePublicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _, _, cls.original_native, cls.original_ci, cls.original_python = (
            captured_case()
        )
        _, _, cls.later_native, cls.later_ci, cls.later_python = captured_case(
            python_variant="overlap"
        )

    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="upgradepilot-lifecycle-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.store = CheckpointStore.create(self.root / "store", schema_version=2)
        self.method = LifecycleMethodIdentity(
            "workspace.host", "controlled-boundary", "1", None, "lifecycle-1", None, ()
        )
        native = {
            record.family: record.record_id for record in self.original_native.records
        }
        self.initial_values = (
            (
                "need",
                InvestigationNeed(
                    "exact_target_python_declaration_established",
                    "read exact declaration",
                    "pyproject.toml",
                ),
            ),
            (
                "request",
                CapabilityRequest("need", "read_exact_declaration", "pyproject.toml"),
            ),
            (
                "admission",
                RequestAdmission(
                    "request", "admitted", "public-read-only", "Bounded host admission."
                ),
            ),
            ("attempt", ExecutionAttempt("admission", "intent_recorded")),
            (
                "view",
                ConsumerView(
                    "investigator",
                    (native["python_support_pre_assessment"],),
                    (native["investigation_inputs"],),
                    "Declared subset; other coverage unknown.",
                ),
            ),
            (
                "use",
                ObservableUse(
                    "view",
                    (native["python_support_pre_assessment"],),
                    "Recorded delivery operation receipt.",
                ),
            ),
            (
                "proposal",
                AttributedProposal(
                    "view",
                    "Python exposure",
                    "Attributed claim, not evaluated truth.",
                    (native["investigation_inputs"],),
                ),
            ),
            (
                "discovery",
                DiscoveryObjective(
                    "What relevant changes exist?",
                    "crossed interval",
                    "Review coverage",
                    "Bounded discovery; no completeness claim.",
                ),
            ),
        )
        self.initial_history = CapturedLifecycleHistory(
            tuple(
                capture_lifecycle_record(
                    identity,
                    "original",
                    value,
                    native_record_ids=(
                        native["investigation_inputs"],
                        native["python_support_pre_assessment"],
                    ),
                    method=self.method,
                )
                for identity, value in self.initial_values
            )
        )
        self.initial = CheckpointRevision(
            "main", "original", None, self.original_native, self.initial_history
        )
        later = {
            record.family: record.record_id for record in self.later_native.records
        }
        evaluator = replace(
            self.method,
            owner="impact.python_support",
            method="evaluate_python_support_drop_impact",
        )
        missing_method = LifecycleMethodIdentity(
            "semantic.adequacy", None, None, None, None, None, ("method_not_admitted",)
        )
        self.later_values = (
            (
                "observation",
                CapabilityObservation(
                    "attempt",
                    "observed",
                    "pyproject.toml",
                    "Exact retained target declaration.",
                ),
                self.method,
            ),
            (
                "assessment",
                EvaluationOutcome(
                    "observation",
                    "evaluated",
                    later["python_support_post_assessment"],
                    "Retained native conclusion.",
                ),
                evaluator,
            ),
            (
                "finish",
                ProceduralTermination(
                    "mechanism-run", "completed", "Procedural completion only."
                ),
                self.method,
            ),
            (
                "stop",
                StoppingProposal("mechanism-run", "Attributed stopping proposal."),
                self.method,
            ),
            (
                "adequacy",
                EvaluationOutcome(
                    "stop", "unsupported", None, "No admitted adequacy evaluator."
                ),
                missing_method,
            ),
        )
        additions = tuple(
            capture_lifecycle_record(
                identity,
                "later",
                value,
                native_record_ids=(
                    later["target_python"],
                    later["python_support_post_assessment"],
                ),
                method=method,
            )
            for identity, value, method in self.later_values
        )
        self.later = CheckpointRevision(
            "main",
            "later",
            "original",
            self.later_native,
            CapturedLifecycleHistory(self.initial_history.records + additions),
        )

    def _read(self, revision_id="original", store=None):
        return (store or self.store).read_revision(
            "main", revision_id, expected_target=self.original_native.target
        )

    def _assert_reason(self, reason, operation):
        with self.assertRaises(CheckpointStorageError) as raised:
            operation()
        self.assertEqual(raised.exception.reason, reason)

    def _cold(self, store, revision_id):
        selection = {
            "revision_id": revision_id,
            "target": asdict(self.original_native.target),
        }
        child = subprocess.run(
            [
                sys.executable,
                "-c",
                _COLD_CHILD,
                str(store.directory),
                json.dumps(selection),
            ],
            check=False,
            env=dict(
                os.environ,
                PYTHONPATH=os.pathsep.join(
                    [str(Path(__file__).parent)]
                    + (
                        [os.environ["PYTHONPATH"]]
                        if os.environ.get("PYTHONPATH")
                        else []
                    )
                ),
            ),
            capture_output=True,
            text=True,
            timeout=30,
        )
        self.assertEqual(child.returncode, 0, child.stderr)
        value = json.loads(child.stdout)
        self.assertEqual(value["blocked_controls"], 4)
        self.assertEqual(value["blocked_network"], 1)
        return value

    def _expected_history(self, revision):
        # Values supplied before encoding are the oracle, not decoded values or a live cache
        # sent to the child. This independent renderer preserves every declared field.
        originals = {identity: value for identity, value in self.initial_values}
        originals.update({identity: value for identity, value, _ in self.later_values})
        return json.loads(
            json.dumps(
                [
                    {
                        "id": record.record_id,
                        "basis": record.basis_revision_id,
                        "native": list(record.native_record_ids),
                        "predecessors": list(record.predecessor_record_ids),
                        "method": asdict(record.method),
                        "kind": type(originals[record.record_id]).__name__,
                        "value": asdict(originals[record.record_id]),
                    }
                    for record in revision.lifecycle_history.records
                ]
            )
        )

    def test_composed_history_native_meanings_and_original_bases_survive_cold_backup(
        self,
    ):
        self.store.publish(self.initial)
        self.store.publish(self.later)
        self.assertEqual(self._read().revision, self.initial)
        self.assertEqual(self._read("later").revision, self.later)
        self.assertEqual(self._read().excluded_successor_ids, ("later",))
        backup = self.root / "backup"
        self.assertEqual(self.store.backup(backup).revision_count, 2)
        copied = CheckpointStore.open(backup, read_only=True)
        for store in (self.store, copied):
            for revision, ci, support in (
                (self.initial, self.original_ci, self.original_python),
                (self.later, self.later_ci, self.later_python),
            ):
                with self.subTest(
                    store=store.directory.name, revision=revision.revision_id
                ):
                    recovered = self._cold(store, revision.revision_id)
                    self.assertEqual(recovered["revision_digest"], revision.digest())
                    self.assertEqual(recovered["ci"], independent_native_values(ci))
                    self.assertEqual(
                        recovered["python"], independent_native_values(support)
                    )
                    self.assertEqual(
                        recovered["lifecycle"], self._expected_history(revision)
                    )
                    self.assertEqual(recovered["retention"], "retained")

    def test_native_only_digest_and_schema1_remain_unchanged_without_fake_history(self):
        old = CheckpointRevision("main", "original", None, self.original_native)
        expected = sha256(
            json_bytes(
                {
                    "lineage_id": "main",
                    "revision_id": "original",
                    "predecessor_id": None,
                    "boundary_digest": sha256(
                        encode_native_boundary(self.original_native)
                    ).hexdigest(),
                }
            )
        ).hexdigest()
        legacy = CheckpointStore.create(self.root / "legacy")
        legacy.publish(old)
        self.assertEqual(old.digest(), expected)
        self.assertEqual(
            self._read(store=legacy).lifecycle_recovery_status, "not_retained"
        )
        self.assertEqual(self._cold(legacy, "original")["retention"], "not_retained")
        with legacy._connection() as db:
            self.assertEqual(db.execute("PRAGMA user_version").fetchone(), (1,))
        self._assert_reason(
            "unsupported_storage_schema", lambda: legacy.publish(self.later)
        )
        self.assertEqual(self._read(store=legacy).revision, old)
        with legacy._connection() as db:
            self.assertEqual(db.execute("PRAGMA user_version").fetchone(), (1,))

    def test_explicit_empty_history_is_not_missing_and_cannot_be_downgraded(self):
        empty = replace(self.initial, lifecycle_history=CapturedLifecycleHistory(()))
        self.assertNotEqual(
            empty.digest(), replace(empty, lifecycle_history=None).digest()
        )
        self.store.publish(empty)
        self.assertEqual(self._read().lifecycle_recovery_status, "retained")
        self._assert_reason(
            "invalid_revision",
            lambda: self.store.publish(
                CheckpointRevision("main", "later", "original", self.original_native)
            ),
        )

    def test_broken_original_native_basis_forward_refs_and_cycles_refuse_atomically(
        self,
    ):
        changes = (
            replace(
                self.initial_history.records[0], native_record_ids=("not-in-basis",)
            ),
            replace(self.initial_history.records[0], basis_revision_id="later"),
            replace(
                self.initial_history.records[0], predecessor_record_ids=("request",)
            ),
            replace(self.initial_history.records[0], predecessor_record_ids=("need",)),
        )
        for number, changed in enumerate(changes):
            with self.subTest(control=number):
                store = CheckpointStore.create(
                    self.root / str(number), schema_version=2
                )
                revision = replace(
                    self.initial,
                    lifecycle_history=CapturedLifecycleHistory(
                        (changed,) + self.initial_history.records[1:]
                    ),
                )
                self._assert_reason(
                    "invalid_checkpoint_storage",
                    lambda store=store, revision=revision: store.publish(revision),
                )
                with store._connection() as db:
                    for table in ("revisions", "records", "lifecycle_records", "heads"):
                        self.assertEqual(
                            db.execute(f"SELECT count(*) FROM {table}").fetchone()[0], 0
                        )

    def test_basis_membership_cannot_silently_move_to_later_native_values(self):
        self.store.publish(self.initial)
        last = self.later.lifecycle_history.records[-1]
        changed = replace(last, basis_revision_id="original")
        bad = replace(
            self.later,
            lifecycle_history=CapturedLifecycleHistory(
                self.initial_history.records
                + self.later.lifecycle_history.records[
                    len(self.initial_history.records) : -1
                ]
                + (changed,)
            ),
        )
        self._assert_reason(
            "invalid_checkpoint_storage", lambda: self.store.publish(bad)
        )
        self.assertEqual(self._read().head_revision_id, "original")

    def test_history_loss_rewrite_identity_collision_and_stale_publication_refuse(self):
        self.store.publish(self.initial)
        for bad in (
            replace(
                self.later,
                lifecycle_history=CapturedLifecycleHistory(
                    self.initial_history.records[:-1]
                ),
            ),
            replace(self.later, lifecycle_history=None),
        ):
            self._assert_reason(
                "invalid_revision", lambda bad=bad: self.store.publish(bad)
            )
        changed = replace(
            self.initial_history.records[0],
            method=replace(self.method, method="changed"),
        )
        bad = replace(
            self.later,
            lifecycle_history=CapturedLifecycleHistory(
                (changed,) + self.later.lifecycle_history.records[1:]
            ),
        )
        self._assert_reason("invalid_revision", lambda: self.store.publish(bad))
        collision = replace(
            self.initial_history.records[-1],
            record_id=self.later_native.records[0].record_id,
        )
        bad = replace(
            self.later,
            lifecycle_history=CapturedLifecycleHistory(
                self.later.lifecycle_history.records + (collision,)
            ),
        )
        self._assert_reason(
            "immutable_identity_conflict", lambda: self.store.publish(bad)
        )
        self.store.publish(self.later)
        self._assert_reason(
            "publication_conflict",
            lambda: self.store.publish(replace(self.later, revision_id="stale")),
        )

    def test_unknown_lifecycle_codec_blocks_typed_history_not_native_inspection(self):
        unknown = replace(self.initial_history.records[-1], codec_version=99)
        revision = replace(
            self.initial,
            lifecycle_history=CapturedLifecycleHistory(
                self.initial_history.records[:-1] + (unknown,)
            ),
        )
        self.store.publish(revision)
        recovered = self._cold(self.store, "original")
        self.assertEqual(recovered["lifecycle_refusal"], "unsupported_lifecycle_codec")
        self.assertEqual(recovered["ci"], independent_native_values(self.original_ci))
        self.assertEqual(
            recovered["python"], independent_native_values(self.original_python)
        )

    def test_rejected_admission_payload_reference_substitution_and_false_use_refuse_typed_history(
        self,
    ):
        bases = {"original": self.original_native}
        cases = []
        rejection = capture_lifecycle_record(
            "admission",
            "original",
            RequestAdmission("request", "rejected", "public-read-only", "Refused."),
            native_record_ids=(),
            method=self.method,
        )
        cases.append(
            CapturedLifecycleHistory(
                self.initial_history.records[:2]
                + (rejection,)
                + self.initial_history.records[3:]
            )
        )
        request = self.initial_history.records[1]
        body = json_bytes(
            {
                "variant": "capability_request",
                "fields": {
                    "purpose_id": "discovery",
                    "capability": "read_exact_declaration",
                    "scope": "pyproject.toml",
                },
            }
        )
        substitution = replace(
            request, payload=body, payload_digest=sha256(body).hexdigest()
        )
        cases.append(
            CapturedLifecycleHistory(
                (self.initial_history.records[0], substitution)
                + self.initial_history.records[2:]
            )
        )
        native = self.initial_history.records[0].native_record_ids
        false_use = capture_lifecycle_record(
            "use",
            "original",
            ObservableUse("view", (native[0],), "receipt"),
            native_record_ids=native,
            method=self.method,
        )
        cases.append(
            CapturedLifecycleHistory(
                self.initial_history.records[:5]
                + (false_use,)
                + self.initial_history.records[6:]
            )
        )
        for history in cases:
            with (
                self.subTest(control=history.records[1].payload),
                self.assertRaises(NativeReconstructionError),
            ):
                reconstruct_lifecycle_history(history, bases=bases)

    def test_schema2_catalog_record_and_header_corruption_refuse_without_migration(
        self,
    ):
        self.store.publish(self.initial)
        database = self.store.directory / "workspace.sqlite3"
        with sqlite3.connect(database) as db:
            db.execute("DROP TRIGGER immutable_lifecycle_records_update")
        self._assert_reason(
            "invalid_checkpoint_storage",
            lambda: CheckpointStore.open(self.store.directory),
        )
        with sqlite3.connect(database) as db:
            db.execute(
                "CREATE TRIGGER immutable_lifecycle_records_update BEFORE UPDATE ON lifecycle_records BEGIN SELECT RAISE(ABORT, 'immutable checkpoint material'); END"
            )
            db.execute("PRAGMA user_version=99")
        self._assert_reason(
            "unsupported_storage_schema",
            lambda: CheckpointStore.open(self.store.directory),
        )
        with sqlite3.connect(database) as db:
            self.assertEqual(db.execute("PRAGMA user_version").fetchone(), (99,))
            db.execute("PRAGMA user_version=2")
        self.assertEqual(self._read().revision, self.initial)

    def test_orphan_lifecycle_material_blocks_validated_backup(self):
        self.store.publish(self.initial)
        record = replace(self.initial_history.records[-1], record_id="orphan")
        body = encode_lifecycle_record(record)
        with self.store._connection() as db:
            db.execute(
                "INSERT INTO lifecycle_records VALUES (?,?,?,?)",
                ("main", "orphan", body, sha256(body).hexdigest()),
            )
        self._assert_reason(
            "invalid_checkpoint_storage",
            lambda: self.store.backup(self.root / "bad-backup"),
        )
        self.assertEqual(self._read().revision, self.initial)

    def test_commit_without_acknowledgement_reconciles_the_whole_composed_identity(
        self,
    ):
        self.store.publish(self.initial)
        real_connect = sqlite3.connect

        class LostAcknowledgement(sqlite3.Connection):
            def execute(self, sql, parameters=()):
                result = super().execute(sql, parameters)
                if sql == "COMMIT":
                    raise RuntimeError("receipt lost")
                return result

        with (
            patch(
                "sqlite3.connect",
                lambda *a, **k: real_connect(*a, factory=LostAcknowledgement, **k),
            ),
            self.assertRaises(UnconfirmedPublication),
        ):
            self.store.publish(self.later)
        self.assertEqual(self.store.inspect_publication(self.later), "published")
        self.assertEqual(self._read("later").revision, self.later)

    def test_actual_process_interruption_does_not_publish_torn_native_lifecycle_state(
        self,
    ):
        packet = self.root / "staging.json"
        packet.write_bytes(
            json_bytes(
                {
                    "native": encode_native_boundary(self.later_native).decode(),
                    "history": json.loads(
                        encode_lifecycle_history(self.later.lifecycle_history)
                    ),
                }
            )
        )
        target = json.dumps(asdict(self.original_native.target))
        for stage in (
            "after_record",
            "after_member",
            "after_head",
            "before_commit",
            "after_commit",
        ):
            with self.subTest(stage=stage):
                store = CheckpointStore.create(self.root / stage, schema_version=2)
                store.publish(self.initial)
                child = subprocess.run(
                    [
                        sys.executable,
                        "-c",
                        _PUBLISH_CHILD,
                        str(store.directory),
                        str(packet),
                        target,
                        stage,
                    ],
                    check=False,
                    capture_output=True,
                    text=True,
                    timeout=30,
                )
                self.assertEqual(child.returncode, -9, child.stderr)
                selected = "later" if stage == "after_commit" else "original"
                recovered = self._cold(store, selected)
                revision = self.later if selected == "later" else self.initial
                self.assertEqual(recovered["revision_digest"], revision.digest())
                self.assertEqual(
                    recovered["lifecycle"], self._expected_history(revision)
                )
                if selected == "original":
                    self._assert_reason(
                        "missing_checkpoint_revision",
                        lambda store=store: self._read("later", store),
                    )

    def test_scope_raw_input_and_stop_cannot_become_native_evaluation(self):
        self.store.publish(self.initial)
        bases = {"original": self.original_native, "later": self.later_native}
        native = {item.family: item.record_id for item in self.later_native.records}
        controls = (
            (
                "observation",
                CapabilityObservation(
                    "attempt", "observed", "other-file", "Wrong scope."
                ),
                self.method,
            ),
            (
                "assessment",
                EvaluationOutcome(
                    "observation",
                    "evaluated",
                    native["investigation_inputs"],
                    "Input is not an assessment.",
                ),
                replace(self.method, owner="investigation"),
            ),
            (
                "adequacy",
                EvaluationOutcome(
                    "stop",
                    "evaluated",
                    native["python_support_post_assessment"],
                    "Domain conclusion is not canonical adequacy.",
                ),
                replace(self.method, owner="impact.python_support"),
            ),
        )
        for identity, value, method in controls:
            with self.subTest(identity=identity):
                replacement = capture_lifecycle_record(
                    identity,
                    "later",
                    value,
                    native_record_ids=tuple(native.values()),
                    method=method,
                )
                history = CapturedLifecycleHistory(
                    tuple(
                        replacement if record.record_id == identity else record
                        for record in self.later.lifecycle_history.records
                    )
                )
                with self.assertRaises(NativeReconstructionError):
                    reconstruct_lifecycle_history(history, bases=bases)

    def test_extra_authority_missing_fields_and_import_tags_refuse_typed_payload(self):
        request = self.initial_history.records[1]
        original = json.loads(request.payload)
        controls = (
            dict(original, fields=dict(original["fields"], admitted=True)),
            dict(
                original,
                fields={
                    key: value
                    for key, value in original["fields"].items()
                    if key != "scope"
                },
            ),
            dict(original, variant="os.system"),
        )
        for value in controls:
            with self.subTest(value=value):
                body = json_bytes(value)
                modified = replace(
                    request, payload=body, payload_digest=sha256(body).hexdigest()
                )
                history = CapturedLifecycleHistory(
                    (self.initial_history.records[0], modified)
                    + self.initial_history.records[2:]
                )
                with self.assertRaises(NativeReconstructionError):
                    reconstruct_lifecycle_history(
                        history, bases={"original": self.original_native}
                    )

    def test_composed_read_budget_refuses_before_lifecycle_allocation(self):
        self.store.publish(self.initial)
        with self.store._connection() as db:
            native_size = db.execute(
                "SELECT sum(length(r.metadata)+length(p.body)) FROM revision_members m "
                "JOIN records r USING(lineage_id,record_id) JOIN payloads p "
                "ON p.lineage_id=r.lineage_id AND p.digest=r.payload_digest "
                "WHERE m.lineage_id='main' AND m.revision_id='original'"
            ).fetchone()[0]
            target_size = db.execute("SELECT length(target) FROM revisions").fetchone()[
                0
            ]
            lifecycle_size = db.execute(
                "SELECT sum(length(body)) FROM lifecycle_records"
            ).fetchone()[0]
        real_read = self.store._bounded_blob

        def refuse_lifecycle_allocation(connection, query, identity):
            if "FROM lifecycle_records" in query:
                raise AssertionError("oversized lifecycle body was allocated")
            return real_read(connection, query, identity)

        with (
            patch(
                "upgradepilot.workspace.checkpoint_store.MAX_NATIVE_JSON_BYTES",
                native_size + target_size + lifecycle_size - 1,
            ),
            patch.object(self.store, "_bounded_blob", refuse_lifecycle_allocation),
        ):
            self._assert_reason("storage_resource_limit", self._read)

    def test_original_basis_budget_refuses_before_ancestor_allocation(self):
        self.store.publish(self.initial)
        self.store.publish(self.later)
        with self.store._connection() as db:
            sizes = {}
            for revision_id in ("original", "later"):
                native = db.execute(
                    "SELECT length(r.metadata),length(p.body) FROM revision_members m "
                    "JOIN records r USING(lineage_id,record_id) JOIN payloads p "
                    "ON p.lineage_id=r.lineage_id AND p.digest=r.payload_digest "
                    "WHERE m.lineage_id='main' AND m.revision_id=?",
                    (revision_id,),
                ).fetchall()
                target = db.execute(
                    "SELECT length(target) FROM revisions WHERE revision_id=?",
                    (revision_id,),
                ).fetchone()[0]
                lifecycle = db.execute(
                    "SELECT length(r.body) FROM revision_lifecycle_members m "
                    "JOIN lifecycle_records r USING(lineage_id,record_id) "
                    "WHERE m.lineage_id='main' AND m.revision_id=?",
                    (revision_id,),
                ).fetchall()
                sizes[revision_id] = (
                    target
                    + sum(metadata + body for metadata, body in native)
                    + sum(body for (body,) in lifecycle)
                )
        budget = sum(sizes.values()) - 1
        self.assertLess(sizes["later"] + 1024, budget)
        real_read = self.store._bounded_blob

        def refuse_ancestor_allocation(connection, query, identity):
            if "FROM revisions" in query and identity == ("main", "original"):
                raise AssertionError("oversized original-basis closure was allocated")
            return real_read(connection, query, identity)

        with (
            patch(
                "upgradepilot.workspace.checkpoint_store.MAX_NATIVE_JSON_BYTES", budget
            ),
            patch.object(self.store, "_bounded_blob", refuse_ancestor_allocation),
        ):
            self._assert_reason("storage_resource_limit", lambda: self._read("later"))

    def test_damaged_history_never_falls_back_to_native_only(self):
        self.store.publish(self.initial)
        for index, (table, statement, parameters) in enumerate(
            (
                (
                    "lifecycle_records",
                    "UPDATE lifecycle_records SET body=? WHERE record_id='need'",
                    (b"{}",),
                ),
                (
                    "lifecycle_records",
                    "DELETE FROM lifecycle_records WHERE record_id='need'",
                    (),
                ),
                ("revision_lifecycle", "DELETE FROM revision_lifecycle", ()),
            )
        ):
            with self.subTest(table=table, statement=statement):
                backup = self.root / ("damage-" + str(index))
                self.store.backup(backup)
                with sqlite3.connect(backup / "workspace.sqlite3") as db:
                    triggers = tuple(
                        db.execute(
                            "SELECT name,sql FROM sqlite_schema WHERE type='trigger' AND tbl_name=?",
                            (table,),
                        )
                    )
                    for name, _ in triggers:
                        db.execute(f"DROP TRIGGER {name}")
                    db.execute(statement, parameters)
                    for _, sql in triggers:
                        db.execute(sql)
                reader = CheckpointStore.open(backup, read_only=True)
                with self.assertRaises(CheckpointStorageError):
                    self._read(store=reader)


if __name__ == "__main__":
    unittest.main()
