"""Store fault/isolation proof; no product recovery or native-codec adoption claim."""

from __future__ import annotations

import json
import sqlite3
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch

from experiments.workspace_checkpoint_stores import (
    MAX_CHECKPOINT_BYTES,
    PHASES,
    STORE_KINDS,
    FileCheckpointStore,
    StalePublication,
    StoreDamaged,
    bounded_json,
    canonical_json,
    open_store,
    validate_checkpoint,
)
from experiments.workspace_checkpoint_trials import (
    DAMAGE_MODES,
    backup_trial,
    cadence_trial,
    contention_trial,
    damage_trial,
    injected_failure_trial,
    kill_trial,
    race_trial,
    reader_trial,
    run,
    seed_store,
    sqlite_full_trial,
    storage_benchmark,
    successor_history,
    trace_history,
    wal_backup_negative_control,
)
from experiments.workspace_revision_representation import encode_checkpoint


class WorkspaceCheckpointStoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.history = trace_history()

    def test_store_recovery_retains_native_bytes_gaps_and_observation_before_evaluation(
        self,
    ):
        for kind in STORE_KINDS:
            with (
                self.subTest(kind=kind),
                tempfile.TemporaryDirectory() as temporary,
                seed_store(kind, Path(temporary) / "store", self.history) as store,
            ):
                self.assertEqual(
                    encode_checkpoint(store.recover().revision),
                    encode_checkpoint(self.history.history[-1]),
                )
                revision = successor_history(self.history)
                store.publish(encode_checkpoint(revision), expected=4)
                recovered = store.recover()
                self.assertEqual(
                    encode_checkpoint(recovered.revision), encode_checkpoint(revision)
                )
                self.assertEqual(
                    json.loads(
                        recovered.revision.records["observation:recorded"].payload
                    )["evaluation"],
                    "not_attempted",
                )
                self.assertIn("method:missing", recovered.summary()["retention_gaps"])
                unknown = json.loads(
                    recovered.revision.records["attempt:unknown"].payload
                )
                self.assertEqual(unknown["outcome"], "completion_unknown")
                self.assertIsNone(unknown["retry_permission"])

    def test_sigkill_boundaries_distinguish_publication_from_acknowledgement(self):
        for kind in STORE_KINDS:
            for phase in PHASES:
                with self.subTest(kind=kind, phase=phase):
                    result = kill_trial(kind, phase, self.history)
                    self.assertEqual(result["exit_code"], -9)
                    committed = phase in ("after_publish", "before_ack", "acknowledged")
                    self.assertEqual(
                        result["recovered_revision"], 5 if committed else 4
                    )
                    self.assertEqual(result["ack_seen"], phase == "acknowledged")
                    self.assertFalse(result["fallback"])

    def test_corrupt_missing_and_invalid_content_is_rejected_with_explicit_fallback(
        self,
    ):
        for kind in STORE_KINDS:
            for mode in DAMAGE_MODES:
                with self.subTest(kind=kind, mode=mode):
                    result = damage_trial(kind, mode, self.history)
                    self.assertTrue(result["publication_refused"])
                    self.assertTrue(result["rejected"])
                    if mode not in ("store_version", "catalog_damage"):
                        self.assertTrue(result["fallback"])
                        self.assertEqual(result["latest_declared"], 4)
                        self.assertEqual(result["lost_published_revisions"], [4])
                    else:
                        self.assertIsNone(result["recovered_revision"])

    def test_two_process_publishers_and_duplicate_inputs_cannot_both_advance(self):
        for kind in STORE_KINDS:
            for duplicate in (False, True):
                with self.subTest(kind=kind, duplicate=duplicate):
                    result = race_trial(kind, self.history, duplicate=duplicate)
                    self.assertEqual(
                        sorted(row["status"] for row in result["writers"]),
                        ["StalePublication", "published"],
                    )
                    self.assertEqual(result["recovered_revision"], 5)

    def test_reader_snapshot_and_writer_lock_behaviors_are_explicit(self):
        for kind in STORE_KINDS:
            with self.subTest(kind=kind):
                result = reader_trial(kind, self.history)
                self.assertEqual(result["reader"]["held"]["recovered_revision"], 4)
                self.assertEqual(result["post_release_revision"], 5)
                self.assertEqual(
                    contention_trial(kind, self.history)["status"], "bounded_busy"
                )

    def test_storage_refusal_rolls_back_before_publish_and_is_uncertain_after_publish(
        self,
    ):
        for kind in STORE_KINDS:
            for phase in (
                "after_partial_content_write",
                "before_publish",
                "before_ack",
            ):
                with self.subTest(kind=kind, phase=phase):
                    result = injected_failure_trial(kind, phase, self.history)
                    self.assertFalse(result["acknowledged"])
                    self.assertEqual(
                        result["recovered_revision"], 5 if phase == "before_ack" else 4
                    )

    def test_real_sqlite_full_and_read_only_refusal_leave_published_state_intact(self):
        for kind in ("sqlite-delete", "sqlite-wal"):
            with self.subTest(kind=kind):
                self.assertEqual(
                    sqlite_full_trial(kind, self.history)["engine_error"], "SQLITE_FULL"
                )
                with (
                    tempfile.TemporaryDirectory() as temporary,
                    seed_store(kind, Path(temporary) / "store", self.history) as store,
                ):
                    store.close()
                    store._writer = sqlite3.connect(
                        store.path.as_uri() + "?mode=ro", uri=True, isolation_level=None
                    )
                    with self.assertRaisesRegex(sqlite3.OperationalError, "readonly"):
                        store.publish(
                            encode_checkpoint(successor_history(self.history)),
                            expected=4,
                        )
                    store.close()
                    self.assertEqual(store.recover().revision.number, 4)

    def test_supported_backups_preserve_all_history_after_original_removal(self):
        for kind in STORE_KINDS:
            with self.subTest(kind=kind):
                result = backup_trial(kind, self.history)
                self.assertTrue(result["all_history_byte_equal"])
                self.assertTrue(result["original_removed"])
                self.assertEqual(result["recovered_revision"], 4)
        self.assertTrue(wal_backup_negative_control(self.history)["rejected"])

    def test_checkpoint_cadence_discloses_unpublished_loss_instead_of_claiming_durability(
        self,
    ):
        for kind in STORE_KINDS:
            with self.subTest(kind=kind):
                self.assertEqual(
                    cadence_trial(kind, self.history, 1)["uncheckpointed_updates_lost"],
                    0,
                )
                self.assertEqual(
                    cadence_trial(kind, self.history, 4)["uncheckpointed_updates_lost"],
                    3,
                )

    def test_recovery_does_not_call_provider_model_or_native_evaluator(self):
        for kind in STORE_KINDS:
            with (
                self.subTest(kind=kind),
                tempfile.TemporaryDirectory() as temporary,
                seed_store(kind, Path(temporary) / "store", self.history) as store,
                patch(
                    "requests.sessions.Session.request",
                    side_effect=AssertionError("HTTP"),
                ),
                patch(
                    "upgradepilot.upstream.support_drop_extractor.LocalSupportDropExtractor.extract",
                    side_effect=AssertionError("model"),
                ),
                patch(
                    "upgradepilot.ci.dependency_state.evaluate_runtime_dependency_state",
                    side_effect=AssertionError("native evaluator"),
                ),
                patch(
                    "upgradepilot.target.relevance.evaluate_target_python_relevance",
                    side_effect=AssertionError("target evaluator"),
                ),
            ):
                recovered = store.recover()
                self.assertEqual(recovered.revision.number, 4)

    def test_publication_refuses_target_lineage_and_same_identity_native_overwrite(
        self,
    ):
        for kind in STORE_KINDS:
            with (
                self.subTest(kind=kind),
                tempfile.TemporaryDirectory() as temporary,
                seed_store(kind, Path(temporary) / "store", self.history) as store,
            ):
                revision = successor_history(self.history)
                for changed in (
                    replace(revision, target=b'{"target":"different"}'),
                    replace(revision, lineage="different"),
                ):
                    with self.assertRaisesRegex(StoreDamaged, "Target/lineage"):
                        store.publish(encode_checkpoint(changed), expected=4)
                records = dict(revision.records)
                records["ci:runtime"] = replace(
                    records["ci:runtime"], payload=b"altered native result"
                )
                with self.assertRaisesRegex(
                    StoreDamaged, "Immutable historical record"
                ):
                    store.publish(
                        encode_checkpoint(replace(revision, records=records)),
                        expected=4,
                    )
                with self.assertRaises(StalePublication):
                    store.publish(encode_checkpoint(revision), expected=3)
                self.assertEqual(store.recover().revision.number, 4)

    def test_storage_envelope_rejects_duplicate_keys_bounds_and_metadata_coercion(self):
        with self.assertRaises(StoreDamaged):
            bounded_json(b'{"schema":1,"schema":2}')
        with self.assertRaises(StoreDamaged):
            bounded_json(b" " * (MAX_CHECKPOINT_BYTES + 1))
        with self.assertRaises(StoreDamaged):
            bounded_json(b"[" * 129 + b"]" * 129)
        for mutate in (
            lambda body: body.update(lineage=17),
            lambda body: body.update(extra="undeclared"),
            lambda body: body.update(predecessor=True),
        ):
            body = json.loads(encode_checkpoint(self.history.history[-1]))
            mutate(body)
            with self.assertRaises(StoreDamaged):
                validate_checkpoint(canonical_json(body))

    def test_identity_guard_survives_disappearance_from_the_current_closure(self):
        prior = self.history.history[-1]
        dropped = replace(
            prior,
            number=5,
            predecessor=4,
            roots=tuple(key for key in prior.roots if key != "annotation"),
            records={
                key: record
                for key, record in prior.records.items()
                if key != "annotation"
            },
            triggering_records=(),
        )
        records = dict(dropped.records)
        records["annotation"] = replace(
            prior.records["annotation"], payload=b"changed historical identity"
        )
        changed = replace(
            dropped,
            number=6,
            predecessor=5,
            roots=dropped.roots + ("annotation",),
            records=records,
            triggering_records=("annotation",),
        )
        for kind in STORE_KINDS:
            with (
                self.subTest(kind=kind),
                tempfile.TemporaryDirectory() as temporary,
                seed_store(kind, Path(temporary) / "store", self.history) as store,
            ):
                # This narrowed closure is a negative identity control, not a claim
                # that dropping material product history is an admitted retention policy.
                store.publish(encode_checkpoint(dropped), expected=4)
                with self.assertRaisesRegex(
                    StoreDamaged, "Immutable.*identity/content collision"
                ):
                    store.publish(encode_checkpoint(changed), expected=5)
                unchanged = dict(dropped.records)
                unchanged["annotation"] = prior.records["annotation"]
                store.publish(
                    encode_checkpoint(replace(changed, records=unchanged)), expected=5
                )
                self.assertEqual(
                    store.recover().revision.records["annotation"],
                    prior.records["annotation"],
                )

    def test_missing_store_is_not_silently_initialized_and_abandoned_content_is_ignored(
        self,
    ):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for kind in STORE_KINDS:
                with self.assertRaises(StoreDamaged):
                    open_store(kind, root / kind)
            with seed_store("files", root / "files", self.history) as store:
                self.assertIsInstance(store, FileCheckpointStore)
                (store.root / "content-unpublished.json").write_bytes(
                    encode_checkpoint(successor_history(self.history))
                )
                self.assertEqual(store.recover().revision.number, 4)
                self.assertFalse(store.recover().rejected)

    def test_volume_measurement_preserves_unknown_io_and_independent_restore_equality(
        self,
    ):
        with patch(
            "experiments.workspace_checkpoint_trials._io_write_bytes", return_value=None
        ):
            for kind in STORE_KINDS:
                with self.subTest(kind=kind):
                    result = storage_benchmark(
                        kind, self.history.history[-1], copies=1, repeats=1, updates=1
                    )
                    self.assertIsNone(result["kernel_accounted_write_bytes"])
                    self.assertGreater(
                        result["logical_retained_value_bytes_added"]["median"], 0
                    )
                    self.assertEqual(result["starting_material_records"], 36)

    def test_later_trial_failure_preserves_completed_evidence_families(self):
        with (
            tempfile.TemporaryDirectory() as temporary,
            patch(
                "experiments.workspace_checkpoint_trials.kill_trial",
                return_value={"test_only": "completed earlier family"},
            ),
            patch(
                "experiments.workspace_checkpoint_trials.damage_trial",
                side_effect=AssertionError("injected later failure"),
            ),
        ):
            output = Path(temporary) / "evidence"
            with self.assertRaisesRegex(AssertionError, "injected later failure"):
                run(output, repeats=1)
            saved = json.loads((output / "results.json").read_bytes())
            self.assertEqual(saved["status"], "failed")
            self.assertEqual(saved["phase"], "damage_trials")
            self.assertEqual(len(saved["kill_trials"]), 21)
            self.assertIn("injected later failure", saved["failure"])

    def test_sql_partial_stage_hook_follows_the_fresh_uncommitted_record(self):
        for kind in ("sqlite-delete", "sqlite-wal"):
            with (
                self.subTest(kind=kind),
                tempfile.TemporaryDirectory() as temporary,
                seed_store(kind, Path(temporary) / "store", self.history) as store,
            ):
                observed = []

                def inspect_stage(phase, store=store, observed=observed):
                    if phase == "after_partial_content_write":
                        self.assertIsNotNone(
                            store._writer.execute(
                                "SELECT id FROM records WHERE id='observation:recorded'"
                            ).fetchone()
                        )
                        self.assertEqual(store.recover().revision.number, 4)
                        observed.append(phase)

                store.publish(
                    encode_checkpoint(successor_history(self.history)),
                    expected=4,
                    hook=inspect_stage,
                )
                self.assertEqual(observed, ["after_partial_content_write"])
                self.assertEqual(store.recover().revision.number, 5)


if __name__ == "__main__":
    unittest.main()
