"""SQLite-selected cold native recovery for the admitted CI/Python material closure.

Normal controlled acquisition supplies native oracles; a new process receives only a
host-owned store and explicit revision/target selection. No material JSON or live native
values cross that recovery boundary. Reuse the JSON-native proof's actual-entry guard,
then distinguish storage refusal from native refusal and compare complete projections.
This composition proof adds no lifecycle/report/continuation or untrusted-import API.
"""

from __future__ import annotations

import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from dataclasses import fields, replace
from hashlib import sha256
from pathlib import Path

from test_workspace_checkpoint_store import _INTERRUPT_CHILD
from test_workspace_native_reconstruction import (
    _RECOVERY_CONTROLS,
    _RECOVERY_GUARD,
    altered_record,
    captured_case,
    captured_project_case,
    independent_native_values,
    rebound_claim,
    replaced_values,
    retained_values,
    unevaluated_families,
)

from upgradepilot.workspace.checkpoint_revision import CheckpointRevision
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_boundary import encode_native_boundary
from upgradepilot.workspace.native_codecs import FAMILY_CONTRACTS
from upgradepilot.workspace.native_projection import (
    reconstruct_ci_projection,
    reconstruct_python_support_projection,
)


_DURABLE_RECOVERY_CHILD = (
    _RECOVERY_GUARD
    + r"""
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.checkpoint_revision import CheckpointStorageError
from upgradepilot.workspace.native_boundary import encode_native_boundary
selection = json.loads(sys.argv[2])
target = ExactInvestigationTarget(**selection['target'])
sys.setprofile(guard)
with patch.object(socket.socket, 'connect', side_effect=AssertionError('network forbidden')):
    result = {}
    try:
        store = CheckpointStore.open(Path(sys.argv[1]), read_only=True)
        stored = store.read_revision(selection['lineage_id'], selection['revision_id'], expected_target=target)
    except CheckpointStorageError as error:
        result['storage_refusal'] = error.reason
    else:
        revision = stored.revision
        boundary = revision.boundary
        result['checkpoint'] = {
            'lineage_id': revision.lineage_id, 'revision_id': revision.revision_id,
            'predecessor_id': revision.predecessor_id, 'head_revision_id': stored.head_revision_id,
            'excluded_successor_ids': list(stored.excluded_successor_ids),
            'revision_digest': revision.digest(),
            'boundary_digest': __import__('hashlib').sha256(encode_native_boundary(boundary)).hexdigest(),
            'publication_status': store.inspect_publication(revision),
        }
        for name, reconstruct in (('ci', reconstruct_ci_projection), ('python', reconstruct_python_support_projection)):
            try:
                projection = reconstruct(boundary, expected_target=target)
            except NativeReconstructionError as error:
                result[name + '_refusal'] = error.reason
            else:
                result[name] = independent_native_values(projection)
    # Actual attempted entry verifies that the network guard is active on every path.
    with socket.socket() as connection:
        try: connection.connect(('127.0.0.1', 9))
        except AssertionError as error:
            assert str(error) == 'network forbidden', error
            result['blocked_network'] = 1
        else: raise AssertionError('network guard was inactive')
"""
    + _RECOVERY_CONTROLS
)


class WorkspaceCheckpointReconstructionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _, _, cls.boundary, cls.expected_ci, cls.expected_python = captured_case()

    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="upgradepilot-durable-native-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.sequence = 0

    def _publish(self, boundary):
        self.sequence += 1
        store = CheckpointStore.create(self.root / str(self.sequence))
        revision = CheckpointRevision("main", "initial", None, boundary)
        store.publish(revision)
        return store, revision

    def _cold(self, store, *, revision_id="initial", target=None, lineage_id="main"):
        target = target or self.boundary.target
        selection = {
            "lineage_id": lineage_id,
            "revision_id": revision_id,
            "target": {
                field.name: getattr(target, field.name) for field in fields(target)
            },
        }
        database = store.directory / "workspace.sqlite3"
        before = sha256(database.read_bytes()).hexdigest()
        child = subprocess.run(
            [
                sys.executable,
                "-c",
                _DURABLE_RECOVERY_CHILD,
                str(store.directory),
                json.dumps(selection),
            ],
            # Discovery changes only the parent's sys.path. Propagate the test oracle
            # explicitly; retain tests-only PYTHONPATH for installed product execution.
            env=dict(
                os.environ,
                PYTHONPATH=os.pathsep.join(
                    [
                        str(Path(__file__).resolve().parent),
                        os.environ.get("PYTHONPATH", ""),
                    ]
                ),
            ),
            capture_output=True,
            text=True,
            timeout=20,
        )
        self.assertEqual(child.returncode, 0, child.stderr)
        self.assertEqual(sha256(database.read_bytes()).hexdigest(), before)
        result = json.loads(child.stdout)
        self.assertEqual(result["blocked_controls"], 4)
        self.assertEqual(result["blocked_network"], 1)
        return result

    def _assert_reconstructed(
        self,
        store,
        revision,
        *,
        expected_ci=None,
        expected_python=None,
        refusals=None,
        head=None,
        excluded=(),
    ):
        boundary = revision.boundary
        result = self._cold(
            store, revision_id=revision.revision_id, target=boundary.target
        )
        expected = {
            "checkpoint": {
                "lineage_id": revision.lineage_id,
                "revision_id": revision.revision_id,
                "predecessor_id": revision.predecessor_id,
                "head_revision_id": head or revision.revision_id,
                "excluded_successor_ids": list(excluded),
                "revision_digest": revision.digest(),
                "boundary_digest": sha256(encode_native_boundary(boundary)).hexdigest(),
                "publication_status": "published",
            },
            "blocked_controls": 4,
            "blocked_network": 1,
        }
        for name, reconstruct, supplied in (
            ("ci", reconstruct_ci_projection, expected_ci),
            ("python", reconstruct_python_support_projection, expected_python),
        ):
            if name in (refusals or {}):
                expected[name + "_refusal"] = refusals[name]
            else:
                value = (
                    supplied
                    if supplied is not None
                    else reconstruct(boundary, expected_target=boundary.target)
                )
                expected[name] = independent_native_values(value)
        self.assertEqual(result, expected)

    def _assert_storage_refusal(self, store, reason, **selection):
        self.assertEqual(
            self._cold(store, **selection),
            {"storage_refusal": reason, "blocked_controls": 4, "blocked_network": 1},
        )

    @staticmethod
    def _damage(store, table, sql, values=()):
        # Controlled corruption restores exact trigger DDL: schema refusal cannot hide
        # missing/corrupt material and reference validation at the combined boundary.
        with sqlite3.connect(
            store.directory / "workspace.sqlite3", isolation_level=None
        ) as db:
            triggers = list(
                db.execute(
                    "SELECT name,sql FROM sqlite_schema WHERE type='trigger' AND tbl_name=?",
                    (table,),
                )
            )
            for name, _ in triggers:
                db.execute(f'DROP TRIGGER "{name}"')
            db.execute(sql, values)
            for _, ddl in triggers:
                db.execute(ddl)

    def test_normal_capture_complete_native_values_survive_store_and_validated_backup(
        self,
    ):
        for command, python, problem in (
            ("positive", "outside", False),
            ("dry_run", "overlap", False),
            ("ambient", "unresolved", False),
            ("positive", "unavailable", False),
            ("positive", "no_claim", False),
            ("positive", "outside", True),
        ):
            with self.subTest(
                command=command, python=python, dependency_problem=problem
            ):
                _, _, boundary, ci, support = captured_case(
                    command_variant=command,
                    python_variant=python,
                    dependency_problem=problem,
                )
                self.assertEqual(len(boundary.records), 11)
                store, revision = self._publish(boundary)
                self._assert_reconstructed(
                    store, revision, expected_ci=ci, expected_python=support
                )
                destination = self.root / (str(self.sequence) + "-backup")
                self.assertEqual(store.backup(destination).revision_count, 1)
                copied = CheckpointStore.open(destination, read_only=True)
                self._assert_reconstructed(
                    copied, revision, expected_ci=ci, expected_python=support
                )

    def test_acquired_project_bundles_survive_durable_native_reconstruction(self):
        for kind, unavailable, second_context in (
            ("uv", False, False),
            ("extra", False, False),
            ("group", False, False),
            ("uv", True, False),
            ("uv", False, True),
        ):
            with self.subTest(
                kind=kind, unavailable=unavailable, contexts=second_context
            ):
                boundary, original = captured_project_case(
                    kind, unavailable=unavailable, second_context=second_context
                )
                store, revision = self._publish(boundary)
                ci = reconstruct_ci_projection(
                    boundary, expected_target=boundary.target
                )
                self.assertEqual(ci.ci_coverage_result, original.ci_coverage_result)
                self._assert_reconstructed(store, revision, expected_ci=ci)

    def test_every_coherent_not_evaluated_prefix_remains_historical_intermediate(self):
        families = tuple(FAMILY_CONTRACTS)
        python_fields = {
            "upstream_authority": ("upstream_interval_result",),
            "upstream_support_drop": ("upstream_support_drop_result",),
            "python_support_pre_assessment": ("pre_investigation_result",),
            "python_support_selection": ("investigation_selection",),
            "target_python": ("target_python_source", "target_python_result"),
            "target_relevance": ("target_python_relevance_result",),
            "python_support_post_assessment": ("impact_result",),
        }
        for count in range(1, len(families) + 1):
            with self.subTest(recorded_prefix=count):
                remaining = families[count:]
                boundary = unevaluated_families(self.boundary, remaining)
                ci = replace(
                    self.expected_ci,
                    workflow_inputs=()
                    if "ci_inputs" in remaining
                    else self.expected_ci.workflow_inputs,
                    ci_coverage_result=None
                    if "ci_coverage" in remaining
                    else self.expected_ci.ci_coverage_result,
                    runtime_dependency_state_result=None
                    if "runtime_dependency_state" in remaining
                    else self.expected_ci.runtime_dependency_state_result,
                )
                support = replace(
                    self.expected_python,
                    **{
                        field: None
                        for family in remaining
                        for field in python_fields.get(family, ())
                    },
                )
                store, revision = self._publish(boundary)
                self._assert_reconstructed(
                    store, revision, expected_ci=ci, expected_python=support
                )

    def test_explicit_earlier_revision_and_backup_do_not_invent_later_progress(self):
        store, initial = self._publish(self.boundary)
        destination = self.root / "earlier-backup"
        store.backup(destination)
        _, _, newer, ci, support = captured_case(python_variant="overlap")
        successor = CheckpointRevision("main", "second", "initial", newer)
        store.publish(successor)
        self._assert_reconstructed(
            store,
            initial,
            expected_ci=self.expected_ci,
            expected_python=self.expected_python,
            head="second",
            excluded=("second",),
        )
        self._assert_reconstructed(
            store, successor, expected_ci=ci, expected_python=support
        )
        copied = CheckpointStore.open(destination, read_only=True)
        self._assert_reconstructed(
            copied,
            initial,
            expected_ci=self.expected_ci,
            expected_python=self.expected_python,
        )
        self._assert_storage_refusal(
            copied, "missing_checkpoint_revision", revision_id="second"
        )

    def test_combined_reconstruction_reads_committed_wal_and_validated_backup(self):
        store, _ = self._publish(self.boundary)
        _, _, boundary, ci, support = captured_case(python_variant="overlap")
        successor = CheckpointRevision("main", "second", "initial", boundary)
        with sqlite3.connect(
            store.directory / "workspace.sqlite3", isolation_level=None
        ) as held:
            held.execute("PRAGMA wal_autocheckpoint=0")
            held.execute("BEGIN")
            held.execute("SELECT count(*) FROM revisions").fetchone()
            store.publish(successor)
            self.assertTrue((store.directory / "workspace.sqlite3-wal").exists())
            self._assert_reconstructed(
                store, successor, expected_ci=ci, expected_python=support
            )
            destination = self.root / "wal-backup"
            self.assertEqual(store.backup(destination).revision_count, 2)
            self._assert_reconstructed(
                CheckpointStore.open(destination, read_only=True),
                successor,
                expected_ci=ci,
                expected_python=support,
            )

    def test_every_root_unsupported_codec_or_semantic_version_preserves_unaffected_projection(
        self,
    ):
        self.assertEqual(len(FAMILY_CONTRACTS), 11)
        for family in FAMILY_CONTRACTS:
            for field, value, reason in (
                ("codec_version", 999, "unsupported_native_codec"),
                (
                    "producer_version",
                    "unadmitted",
                    "unsupported_native_semantic_version",
                ),
            ):
                with self.subTest(family=family, version=field):
                    boundary = altered_record(self.boundary, family, **{field: value})
                    affected = (
                        ("ci", "python")
                        if family == "investigation_inputs"
                        else ("ci",)
                        if family.startswith("ci_")
                        or family == "runtime_dependency_state"
                        else ("python",)
                    )
                    store, revision = self._publish(boundary)
                    self._assert_reconstructed(
                        store,
                        revision,
                        expected_ci=self.expected_ci,
                        expected_python=self.expected_python,
                        refusals=dict.fromkeys(affected, reason),
                    )

    def test_every_declared_input_edge_substitution_is_refused_after_valid_publication(
        self,
    ):
        records = {record.family: record for record in self.boundary.records}
        edges = [
            (family, name)
            for family, contract in FAMILY_CONTRACTS.items()
            for name in contract.inputs
        ]
        self.assertEqual(len(edges), 18)
        for family, input_name in edges:
            with self.subTest(family=family, input=input_name):
                is_ci = family.startswith("ci_") or family == "runtime_dependency_state"
                alternate = "upstream_authority" if is_ci else "ci_inputs"
                record = records[family]
                boundary = altered_record(
                    self.boundary,
                    family,
                    input_record_ids=tuple(
                        records[alternate].record_id
                        if ref == records[input_name].record_id
                        else ref
                        for ref in record.input_record_ids
                    ),
                )
                store, revision = self._publish(boundary)
                self._assert_reconstructed(
                    store,
                    revision,
                    expected_ci=self.expected_ci,
                    expected_python=self.expected_python,
                    refusals={"ci" if is_ci else "python": "missing_native_material"},
                )

    def test_valid_digest_decoded_material_bindings_are_checked_after_sqlite_read(self):
        values = retained_values(self.boundary)
        inputs = values["investigation_inputs"]
        context = inputs["source_contexts"][0]
        changed_inputs = dict(
            inputs,
            source_contexts=(
                replace(
                    context,
                    source_evidence=replace(
                        context.source_evidence, path="substituted.txt"
                    ),
                ),
            ),
        )
        context_case = replaced_values(
            self.boundary, investigation_inputs=changed_inputs
        )
        claim = values["upstream_support_drop"]
        grounding = claim.source_evidence[0]
        claim_case = rebound_claim(
            self.boundary,
            replace(
                claim,
                source_evidence=(
                    replace(
                        grounding,
                        source=replace(grounding.source, path="other/CHANGELOG.md"),
                    ),
                ),
            ),
        )
        pending = unevaluated_families(
            self.boundary,
            ("target_python", "target_relevance", "python_support_post_assessment"),
        )
        selection_case = replaced_values(
            pending,
            python_support_selection=replace(
                values["python_support_selection"], path="other/pyproject.toml"
            ),
        )
        source = replace(
            self.expected_python.target_python_source, path="other/pyproject.toml"
        )
        target = replace(self.expected_python.target_python_result, path=source.path)
        relevance = replace(
            self.expected_python.target_python_relevance_result, target_evidence=target
        )
        source_case = replaced_values(
            self.boundary,
            target_python={"source": source, "result": target},
            target_relevance=relevance,
            python_support_post_assessment=replace(
                self.expected_python.impact_result, target_relevance=relevance
            ),
        )
        missing_case = replaced_values(
            self.boundary, target_python={"source": None, "result": None}
        )
        project, _ = captured_project_case("uv")
        workflow = retained_values(project)["ci_inputs"][0]
        bundle = workflow.project_environment_sources[0]
        project_case = replaced_values(
            project,
            ci_inputs=(
                replace(
                    workflow,
                    project_environment_sources=(
                        replace(
                            bundle,
                            lock_file=replace(bundle.lock_file, path="other/uv.lock"),
                        ),
                    ),
                ),
            ),
        )
        for name, boundary, affected, reason in (
            (
                "dependency_provenance",
                context_case,
                ("ci", "python"),
                "invalid_native_material",
            ),
            ("claim_authority", claim_case, ("python",), "invalid_native_material"),
            (
                "selection_pre_basis",
                selection_case,
                ("python",),
                "invalid_native_material",
            ),
            ("selected_source", source_case, ("python",), "invalid_native_material"),
            (
                "recorded_empty_acquisition",
                missing_case,
                ("python",),
                "missing_native_material",
            ),
            ("project_lock_locator", project_case, ("ci",), "invalid_native_material"),
        ):
            with self.subTest(binding=name):
                store, revision = self._publish(boundary)
                self._assert_reconstructed(
                    store, revision, refusals=dict.fromkeys(affected, reason)
                )

    def test_retained_owner_conclusion_is_preserved_without_fresh_semantic_derivation(
        self,
    ):
        post = self.expected_python.impact_result
        historical = replace(
            post,
            applicability=replace(
                post.applicability,
                state="conflicted",
                detail="Retained historical owner conclusion.",
            ),
        )
        boundary = replaced_values(
            self.boundary, python_support_post_assessment=historical
        )
        store, revision = self._publish(boundary)
        # Constructed admitted-boundary control, not semantic correctness/authentication.
        self._assert_reconstructed(
            store,
            revision,
            expected_ci=self.expected_ci,
            expected_python=replace(self.expected_python, impact_result=historical),
        )

    def test_missing_terminal_native_root_refuses_only_its_projection(self):
        boundary = replace(
            self.boundary,
            records=tuple(
                record
                for record in self.boundary.records
                if record.family != "python_support_post_assessment"
            ),
        )
        store, revision = self._publish(boundary)
        self._assert_reconstructed(
            store,
            revision,
            expected_ci=self.expected_ci,
            refusals={"python": "missing_native_material"},
        )

    def test_storage_integrity_schema_target_and_selection_refuse_before_native_recovery(
        self,
    ):
        store, _ = self._publish(self.boundary)
        variants = (
            ("schema", "PRAGMA user_version=99", (), "unsupported_storage_schema"),
            (
                "revisions",
                "UPDATE revisions SET digest='damaged'",
                (),
                "invalid_checkpoint_storage",
            ),
            (
                "payloads",
                "UPDATE payloads SET body=? WHERE digest=?",
                (b"damaged", self.boundary.records[0].payload_digest),
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
                "revision_members",
                "DELETE FROM revision_members WHERE position=0",
                (),
                "invalid_checkpoint_storage",
            ),
            ("heads", "DELETE FROM heads", (), "missing_checkpoint_revision"),
            (
                "heads",
                "UPDATE heads SET revision_id='missing'",
                (),
                "invalid_checkpoint_storage",
            ),
        )
        for index, (table, sql, values, reason) in enumerate(variants):
            with self.subTest(damage=table, sql=sql):
                destination = self.root / ("storage-damage-" + str(index))
                store.backup(destination)
                damaged = CheckpointStore.open(destination)
                self._damage(damaged, table, sql, values)
                self._assert_storage_refusal(damaged, reason)
        self._assert_storage_refusal(
            store,
            "wrong_target",
            target=replace(self.boundary.target, head_sha="different-head"),
        )
        self._assert_storage_refusal(
            store, "missing_checkpoint_revision", revision_id="unpublished"
        )
        self._assert_storage_refusal(
            store, "missing_checkpoint_revision", lineage_id="other"
        )

    def test_actual_pre_and_postcommit_interruption_reconstructs_only_declared_progress(
        self,
    ):
        _, _, boundary, ci, support = captured_case(python_variant="overlap")
        successor = CheckpointRevision("main", "second", "initial", boundary)
        for stage in ("before_commit", "after_commit"):
            with self.subTest(stage=stage):
                store, initial = self._publish(self.boundary)
                publisher_input = self.root / (stage + ".json")
                publisher_input.write_bytes(encode_native_boundary(boundary))
                target = json.dumps(
                    {
                        field.name: getattr(boundary.target, field.name)
                        for field in fields(boundary.target)
                    }
                )
                child = subprocess.run(
                    [
                        sys.executable,
                        "-c",
                        _INTERRUPT_CHILD,
                        str(store.directory),
                        str(publisher_input),
                        target,
                        stage,
                        "second",
                        "initial",
                    ],
                    capture_output=True,
                    text=True,
                    timeout=20,
                )
                self.assertEqual(child.returncode, -9, child.stderr)
                publisher_input.unlink()
                if stage == "before_commit":
                    self._assert_reconstructed(
                        store,
                        initial,
                        expected_ci=self.expected_ci,
                        expected_python=self.expected_python,
                    )
                    self._assert_storage_refusal(
                        store, "missing_checkpoint_revision", revision_id="second"
                    )
                else:
                    self._assert_reconstructed(
                        store, successor, expected_ci=ci, expected_python=support
                    )
                    self._assert_reconstructed(
                        store,
                        initial,
                        expected_ci=self.expected_ci,
                        expected_python=self.expected_python,
                        head="second",
                        excluded=("second",),
                    )


if __name__ == "__main__":
    unittest.main()
