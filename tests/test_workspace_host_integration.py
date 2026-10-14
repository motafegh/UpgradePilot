"""Production orchestration proof plus disclosed generic/defensive lifecycle controls.

Normal cases use real native producers/evaluators with controlled provider/semantic ports.
Generic delayed delivery/capability controls establish the host contract, not new native
semantic coverage. Fresh readers receive only store and exact selection, never the oracle.
"""

import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from dataclasses import asdict, replace
from pathlib import Path
from unittest.mock import Mock, patch

from test_workspace_lifecycle_publication import _COLD_CHILD
from test_workspace_native_reconstruction import (
    captured_case,
    independent_native_values,
)

from upgradepilot.github.api import GitHubAcquisitionError
from upgradepilot.github.repository import RepositoryTextFile, UnavailableRepositoryFile
from upgradepilot.impact.python_support import (
    evaluate_python_support_drop_impact,
    select_python_support_drop_investigation,
)
from upgradepilot.workspace.checkpoint_revision import (
    CheckpointRevision,
    CheckpointStorageError,
    UnconfirmedPublication,
)
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.lifecycle_host import (
    CapabilityResult,
    ExecutionAuthority,
    HostCapability,
    InvestigationWorkspaceHost,
    WorkspaceHostError,
)
from upgradepilot.workspace.lifecycle_records import (
    CapabilityObservation,
    CapabilityRequest,
    DiscoveryObjective,
    EvaluationOutcome,
    ExecutionAttempt,
    ExecutionInterruption,
    InvestigationNeed,
    LifecycleMethodIdentity,
    ProceduralTermination,
    RequestAdmission,
    decode_lifecycle_value,
    encode_lifecycle_value,
)
from upgradepilot.workspace.material_validity import validate_current_material_basis
from upgradepilot.workspace.native_capture import NativeInvestigationCapture
from upgradepilot.workspace.native_projection import (
    reconstruct_python_support_projection,
)
from upgradepilot.workspace.native_representation import NativeReconstructionError
from upgradepilot.workspace.repository_read_capability import (
    restore_repository_observation,
)

_NORMAL_KILL = r"""
import os,signal,sys
from pathlib import Path
from test_workspace_native_reconstruction import captured_case
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost
store=CheckpointStore.open(Path(sys.argv[1]))
host=InvestigationWorkspaceHost(store=store,lineage_id='main')
stage=sys.argv[2]
real_publish=store.publish
def publish(revision):
    kinds=[record.kind for record in revision.lifecycle_history.records]
    latest=kinds[-1] if kinds else None
    if stage=='before_intent' and latest=='execution_attempt': os.kill(os.getpid(),signal.SIGKILL)
    receipt=real_publish(revision)
    if ((stage=='after_intent' and latest=='execution_attempt')
        or (stage=='after_observation' and latest=='capability_observation')
        or (stage=='after_evaluation' and latest=='evaluation_outcome')):
        os.kill(os.getpid(),signal.SIGKILL)
    return receipt
store.publish=publish
def entered(h): Path(sys.argv[3]).write_text('provider entered')
captured_case(workspace_host=host,before_target_read=entered)
raise AssertionError('kill point not reached')
"""

# unittest discovery adds tests to the parent sys.path, not the child's environment.
# Carry that fixture directory explicitly; never add checkout source for installed proof.
_CHILD_ENV = dict(
    os.environ,
    PYTHONPATH=os.pathsep.join(
        [str(Path(__file__).resolve().parent)]
        + ([os.environ["PYTHONPATH"]] if os.environ.get("PYTHONPATH") else [])
    ),
)


# Extend the independently exercised guarded reader with real host restoration. Its
# only inputs remain the store and exact selection; it obtains original bases there.
_COLD_HOST_CHILD = _COLD_CHILD.replace(
    "values = reconstruct_lifecycle_history(revision.lifecycle_history, bases=bases)",
    """values = reconstruct_lifecycle_history(revision.lifecycle_history, bases=bases)
                from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost, WorkspaceHostError
                from upgradepilot.workspace.lifecycle_records import ExecutionAttempt, RequestAdmission
                restored = InvestigationWorkspaceHost(lineage_id=revision.lineage_id)
                restored.restore(stored, bases=bases)
                result['attempt_states'] = {
                    item.capture.record_id: restored.attempt_completion(item.capture.record_id)
                    for item in values if isinstance(item.value, ExecutionAttempt)
                }
                result['historical_admission_refusals'] = 0
                for item in values:
                    if isinstance(item.value, RequestAdmission) and item.value.outcome == 'admitted':
                        try: restored.execute_admission(item.capture.record_id)
                        except WorkspaceHostError as error:
                            assert error.reason == 'historical_or_consumed_admission', error
                            result['historical_admission_refusals'] += 1
                        else: raise AssertionError('recovered admission granted execution')""",
)


class WorkspaceHostIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _, _, cls.boundary, _, _ = captured_case()

    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="upgradepilot-host-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.store = CheckpointStore.create(self.root / "store", schema_version=2)
        self.host = InvestigationWorkspaceHost(store=self.store, lineage_id="main")
        self.method = LifecycleMethodIdentity(
            "controlled.capability",
            "read_exact_scope",
            "1",
            None,
            "control/1",
            None,
            (),
        )
        self.handler = Mock(
            return_value=CapabilityResult(
                "scoped_negative", "Only this exact scope was checked."
            )
        )
        self.capability = HostCapability(
            "inspect_scope",
            self.method,
            frozenset({"repository_read"}),
            lambda scope: scope == "Cargo.lock",
            self.handler,
        )
        self.authority = ExecutionAuthority(
            self.boundary.target,
            frozenset({"inspect_scope"}),
            frozenset({"repository_read"}),
        )

    def _generic_request(self):
        self.host.configure(authority=self.authority, capabilities=(self.capability,))
        self.host.initialize(self.boundary)
        root = next(
            item.record_id
            for item in self.boundary.records
            if item.family == "python_support_pre_assessment"
        )
        purpose = self.host.add_purpose(
            DiscoveryObjective(
                "Inspect scoped material",
                "Cargo.lock",
                "Controlled protocol pressure",
                "Not a production Rust capability",
            ),
            native_record_ids=(root,),
        )
        return self.host.request_capability(purpose, "inspect_scope", "Cargo.lock")

    def _values(self, kind):
        return [
            (record, value)
            for record, value in self.host.inspect_lifecycle()
            if isinstance(value, kind)
        ]

    def _stored(self):
        return self.store.read_revision(
            "main", self.host.current.revision_id, expected_target=self.boundary.target
        )

    def _cold(self, store=None):
        store = store or self.store
        with sqlite3.connect(store.directory / "workspace.sqlite3") as db:
            revision_id = db.execute(
                "SELECT revision_id FROM heads WHERE lineage_id='main'"
            ).fetchone()[0]
        selection = json.dumps(
            {"revision_id": revision_id, "target": asdict(self.boundary.target)}
        )
        child = subprocess.run(
            [sys.executable, "-c", _COLD_HOST_CHILD, str(store.directory), selection],
            check=False,
            env=_CHILD_ENV,
            capture_output=True,
            text=True,
            timeout=30,
        )
        self.assertEqual(child.returncode, 0, child.stderr)
        result = json.loads(child.stdout)
        self.assertEqual(result["blocked_controls"], 4)
        self.assertEqual(result["blocked_network"], 1)
        return result

    def test_normal_selected_read_publishes_intent_before_provider_and_native_reassessment_once(
        self,
    ):
        def before_read(h):
            stored = self._stored()
            kinds = [
                record.kind for record in stored.revision.lifecycle_history.records
            ]
            self.assertEqual(kinds[-1], "execution_attempt")
            projection = reconstruct_python_support_projection(
                stored.revision.boundary, expected_target=self.boundary.target
            )
            self.assertIsNone(projection.target_python_source)
            self.assertIsNone(projection.impact_result)
            self.assertEqual(
                projection.pre_investigation_result.applicability.state, "unresolved"
            )

        with patch(
            "upgradepilot.investigation.evaluate_python_support_drop_impact",
            wraps=evaluate_python_support_drop_impact,
        ) as evaluator:
            h, result, boundary, ci, python = captured_case(
                workspace_host=self.host, before_target_read=before_read
            )
        self.assertEqual(evaluator.call_count, 2)
        self.assertEqual(
            self._values(InvestigationNeed)[0][0].method.owner, "impact.python_support"
        )
        h.repository_client.get_exact_head_text_file.assert_called_once_with(
            h.identity, "pyproject.toml"
        )
        self.assertEqual(result.workspace_revision, self.host.current)
        self.assertEqual(boundary, self.host.current.boundary)
        observed = self._values(CapabilityObservation)
        self.assertEqual(len(observed), 1)
        self.assertEqual(observed[0][1].outcome, "observed")
        self.assertEqual(observed[0][0].codec_version, 2)
        self.assertIn(
            "provider_method_unavailable", observed[0][0].method.retention_gaps
        )
        self.assertEqual(
            restore_repository_observation(observed[0][1]),
            h.repository_client.get_exact_head_text_file.return_value,
        )
        evaluated = self._values(EvaluationOutcome)
        self.assertEqual(evaluated[-1][1].outcome, "evaluated")
        self.assertEqual(evaluated[-1][0].method.owner, "impact.python_support")
        self.assertEqual(
            self.host.current_validity(evaluated[-1][0].record_id).status, "valid"
        )
        self.assertEqual(
            self._values(ProceduralTermination)[-1][1].outcome, "completed"
        )
        recovered = self._cold()
        self.assertEqual(recovered["ci"], independent_native_values(ci))
        self.assertEqual(recovered["python"], independent_native_values(python))
        self.assertEqual(
            [item["kind"] for item in recovered["lifecycle"]],
            [type(value).__name__ for _, value in self.host.inspect_lifecycle()],
        )
        backup = self.root / "backup"
        self.store.backup(backup)
        self.assertEqual(
            self._cold(CheckpointStore.open(backup, read_only=True))["revision_digest"],
            result.workspace_revision.digest(),
        )

    def test_normal_available_unresolved_and_unavailable_results_preserve_native_meanings(
        self,
    ):
        for variant, expected in (
            ("overlap", "observed"),
            ("unresolved", "observed"),
            ("unavailable", "problem"),
            ("empty", "empty"),
        ):
            with self.subTest(variant=variant):
                store = CheckpointStore.create(self.root / variant, schema_version=2)
                host = InvestigationWorkspaceHost(store=store, lineage_id="main")
                h, result, _, _, python = captured_case(
                    python_variant=variant, workspace_host=host
                )
                history = host.inspect_lifecycle()
                observation = next(
                    value
                    for _, value in history
                    if isinstance(value, CapabilityObservation)
                )
                self.assertEqual(observation.outcome, expected)
                self.assertIsNone(
                    select_python_support_drop_investigation(
                        result.python_support_drop_impact_result
                    )
                )
                h.repository_client.get_exact_head_text_file.assert_called_once()
                self.assertEqual(
                    self._cold(store)["python"], independent_native_values(python)
                )

    def test_normal_no_candidate_and_dependency_problem_preserve_unperformed_branches(
        self,
    ):
        for options in ({"python_variant": "no_claim"}, {"dependency_problem": True}):
            with self.subTest(options=options):
                host = InvestigationWorkspaceHost()
                h, result, _, _, _ = captured_case(workspace_host=host, **options)
                h.repository_client.get_exact_head_text_file.assert_not_called()
                self.assertFalse(
                    any(
                        isinstance(value, ExecutionAttempt)
                        for _, value in host.inspect_lifecycle()
                    )
                )
                self.assertIsNotNone(result.workspace_revision)
                self.assertEqual(host.inspect_lifecycle()[-1][1].outcome, "completed")

    def test_exact_repository_adapter_keeps_empty_inaccessible_and_http_failure_distinct(
        self,
    ):
        from upgradepilot.workspace.repository_read_capability import (
            repository_read_capability,
        )

        h, _, _, _, _ = captured_case()
        adapter = repository_read_capability(h.identity, h.repository_client)
        request = CapabilityRequest("purpose", adapter.name, "docs/readme.md")
        for source, outcome in (
            (
                RepositoryTextFile(
                    h.identity.repository, request.scope, h.identity.head_sha, ""
                ),
                "empty",
            ),
            (
                UnavailableRepositoryFile(
                    h.identity.repository,
                    request.scope,
                    h.identity.head_sha,
                    "not_found_or_inaccessible",
                    "No stronger absence claim",
                ),
                "problem",
            ),
        ):
            h.repository_client.get_exact_head_text_file.return_value = source
            result = adapter.execute(request)
            self.assertEqual(result.outcome, outcome)
            self.assertEqual(
                restore_repository_observation(
                    CapabilityObservation(
                        "attempt",
                        result.outcome,
                        request.scope,
                        result.detail,
                        result.representation,
                        result.retained_content,
                    )
                ),
                source,
            )
        h.repository_client.get_exact_head_text_file.side_effect = (
            GitHubAcquisitionError("safe failure", reason="timeout")
        )
        failed = adapter.execute(request)
        self.assertEqual(failed.outcome, "problem")
        self.assertEqual(failed.value.reason, "timeout")
        h.repository_client.get_exact_head_text_file.side_effect = None
        h.repository_client.get_exact_head_text_file.return_value = RepositoryTextFile(
            h.identity.repository, "other.md", h.identity.head_sha, "other"
        )
        with self.assertRaises(ValueError):
            adapter.execute(request)

    def test_generic_host_admits_scope_and_effects_without_python_policy(self):
        request_id = self._generic_request()
        admission = self.host.admit_request(request_id)
        observation, result = self.host.execute_admission(admission)
        self.assertEqual(result.outcome, "scoped_negative")
        self.assertEqual(
            self.host.lifecycle_value(observation).outcome, "scoped_negative"
        )
        self.handler.assert_called_once_with(
            CapabilityRequest(
                self.host.lifecycle_value(request_id).purpose_id,
                "inspect_scope",
                "Cargo.lock",
            )
        )
        recovered = self._cold()
        self.assertEqual(recovered["lifecycle"][-1]["value"]["scope"], "Cargo.lock")
        self.assertNotIn("python", recovered["lifecycle"][-1]["method"]["owner"])

    def test_current_execution_authority_is_rechecked_after_admission(self):
        request_id = self._generic_request()
        admission = self.host.admit_request(request_id)
        for authority, capability, reason in (
            (None, self.capability, "current_execution_authority_unavailable"),
            (
                replace(self.authority, effects=frozenset()),
                self.capability,
                "effects_not_authorized",
            ),
            (
                replace(
                    self.authority,
                    target=replace(self.boundary.target, head_sha="f" * 40),
                ),
                self.capability,
                "current_execution_authority_unavailable",
            ),
            (
                self.authority,
                replace(self.capability, method=replace(self.method, version="2")),
                "capability_method_changed",
            ),
            (
                self.authority,
                replace(self.capability, accepts_scope=lambda scope: False),
                "capability_scope_changed",
            ),
        ):
            with self.subTest(reason=reason):
                self.host.configure(authority=authority, capabilities=(capability,))
                with self.assertRaises(WorkspaceHostError) as caught:
                    self.host.execute_admission(admission)
                self.assertEqual(caught.exception.reason, reason)
        self.handler.assert_not_called()
        self.assertFalse(self._values(ExecutionAttempt))

    def test_request_rejection_and_missing_capability_do_not_execute(self):
        request_id = self._generic_request()
        self.host.configure(
            authority=replace(self.authority, capabilities=frozenset()), capabilities=()
        )
        admission = self.host.admit_request(request_id)
        self.assertEqual(self.host.lifecycle_value(admission).outcome, "rejected")
        with self.assertRaises(WorkspaceHostError):
            self.host.execute_admission(admission)
        self.handler.assert_not_called()

    def test_failed_intent_publication_blocks_normal_provider_execution_and_retry(self):
        real_publish = self.store.publish

        def refuse_intent(revision):
            if (
                revision.lifecycle_history.records
                and revision.lifecycle_history.records[-1].kind == "execution_attempt"
            ):
                raise CheckpointStorageError(
                    "storage_busy", "Controlled before-intent publication failure"
                )
            return real_publish(revision)

        calls = []
        with (
            patch.object(self.store, "publish", side_effect=refuse_intent),
            self.assertRaises(CheckpointStorageError),
        ):
            captured_case(
                workspace_host=self.host,
                before_target_read=lambda h: calls.append("provider"),
            )
        self.assertEqual(calls, [])
        with self.assertRaises(WorkspaceHostError) as caught:
            self.host.terminate(
                "run", "failed", "cannot continue without reconciliation"
            )
        self.assertEqual(caught.exception.reason, "publication_reconciliation_required")
        self.assertNotIn(
            "ExecutionAttempt", [item["kind"] for item in self._cold()["lifecycle"]]
        )

    def test_unknown_completion_and_completed_problem_are_separate_and_never_auto_retried(
        self,
    ):
        request_id = self._generic_request()
        self.handler.side_effect = RuntimeError(
            "do not retain arbitrary exception text"
        )
        with self.assertRaises(RuntimeError):
            self.host.execute_admission(self.host.admit_request(request_id))
        attempt = self._values(ExecutionAttempt)[0][0].record_id
        self.assertEqual(self.host.attempt_completion(attempt), "completion_unknown")
        self.assertEqual(
            self._values(ExecutionInterruption)[0][1].problem_kind, "RuntimeError"
        )
        self.assertFalse(self._values(CapabilityObservation))
        admission = self.host.admit_request(request_id)
        self.assertEqual(self.host.lifecycle_value(admission).outcome, "rejected")
        self.handler.assert_called_once()
        with self.assertRaises(WorkspaceHostError):
            self.host.ingest_observation(
                attempt, CapabilityResult("problem", "not independently reconciled")
            )
        self.assertIn(
            "ExecutionInterruption",
            [item["kind"] for item in self._cold()["lifecycle"]],
        )

    def test_duplicate_observation_is_idempotent_but_contradictory_content_refuses(
        self,
    ):
        request_id = self._generic_request()
        observation_id, result = self.host.execute_admission(
            self.host.admit_request(request_id)
        )
        attempt_id = self.host.lifecycle_value(observation_id).attempt_id
        revision = self.host.current.revision_id
        self.assertEqual(
            self.host.ingest_observation(attempt_id, result), observation_id
        )
        self.assertEqual(self.host.current.revision_id, revision)
        with self.assertRaises(WorkspaceHostError) as caught:
            self.host.ingest_observation(
                attempt_id, replace(result, outcome="observed", detail="Contradiction")
            )
        self.assertEqual(caught.exception.reason, "contradictory_duplicate_observation")
        self.assertEqual(self.host.current.revision_id, revision)
        with self.assertRaises(WorkspaceHostError):
            self.host.execute_admission(self._values(RequestAdmission)[0][0].record_id)

    def test_unrelated_progress_keeps_original_basis_valid_but_material_scope_head_method_changes_do_not(
        self,
    ):
        request_id = self._generic_request()
        record = self.host._records[request_id]
        basis = self.host._bases[record.basis_revision_id]
        earlier = self.host.current.revision_id
        progress = replace(
            self.boundary,
            records=tuple(
                replace(item, record_id=item.record_id + "progress")
                if item.family == "runtime_dependency_state"
                else item
                for item in self.boundary.records
            ),
        )
        self.host.publish_native_progress(progress)
        self.assertNotEqual(earlier, self.host.current.revision_id)
        self.assertEqual(self.host.current_validity(request_id).status, "valid")
        recorded_method = record.method
        self.assertEqual(
            self.host._records[request_id].basis_revision_id, record.basis_revision_id
        )
        current_records = {item.record_id: item for item in progress.records}
        # Defensive same-ID metadata substitution tests comparison, not a publishable state.
        premise_id = next(
            identity
            for identity in current_records
            if current_records[identity].family == "upstream_support_drop"
        )
        changed = replace(
            progress,
            records=tuple(
                replace(item, producer_method="changed_method")
                if item.record_id == premise_id
                else item
                for item in progress.records
            ),
        )
        cases = (
            (changed, "Cargo.lock", recorded_method, True, "stale"),
            (
                replace(progress, target=replace(progress.target, head_sha="f" * 40)),
                "Cargo.lock",
                recorded_method,
                True,
                "stale",
            ),
            (progress, "other.lock", recorded_method, True, "stale"),
            (
                progress,
                "Cargo.lock",
                replace(recorded_method, version="2"),
                True,
                "stale",
            ),
            (progress, "Cargo.lock", None, True, "unsupported"),
            (progress, "Cargo.lock", recorded_method, False, "unsupported"),
        )
        for current, scope, method, available, status in cases:
            with self.subTest(scope=scope, method=method, available=available):
                self.assertEqual(
                    validate_current_material_basis(
                        record,
                        basis,
                        current,
                        original_scope="Cargo.lock",
                        current_scope=scope,
                        current_method=method,
                        capability_available=available,
                    ).status,
                    status,
                )

    def test_material_changes_block_delayed_native_evaluation_without_rewriting_history(
        self,
    ):
        request_id = self._generic_request()
        observation, _ = self.host.execute_admission(
            self.host.admit_request(request_id)
        )
        original_records = self.host.current.lifecycle_history.records
        changed = replace(
            self.boundary,
            records=tuple(
                replace(item, record_id=item.record_id + "changed")
                if item.family == "python_support_post_assessment"
                else item
                for item in self.boundary.records
            ),
        )
        self.host.publish_native_progress(changed)
        self.assertEqual(self.host.current_validity(observation).status, "valid")
        self.host.configure(
            authority=self.authority,
            capabilities=(
                replace(self.capability, method=replace(self.method, version="2")),
            ),
            methods=(self.method,),
        )
        callback = Mock()
        evaluated = self.host.evaluate_native(
            observation, method=self.method, evaluate=callback
        )
        self.assertEqual(self.host.lifecycle_value(evaluated).outcome, "stale")
        callback.assert_not_called()
        self.assertEqual(
            self.host.current.lifecycle_history.records[: len(original_records)],
            original_records,
        )

    def test_normal_native_evaluator_failure_retains_returned_source_and_failed_evaluation(
        self,
    ):
        calls = 0

        def evaluator(*args):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise ValueError("Controlled native owner failure")
            return evaluate_python_support_drop_impact(*args)

        with (
            patch(
                "upgradepilot.investigation.evaluate_python_support_drop_impact",
                side_effect=evaluator,
            ),
            self.assertRaises(ValueError),
        ):
            captured_case(workspace_host=self.host)
        observation = self._values(CapabilityObservation)[0][1]
        self.assertIsInstance(
            restore_repository_observation(observation), RepositoryTextFile
        )
        self.assertEqual(self._values(EvaluationOutcome)[-1][1].outcome, "failed")
        recovered = self._cold()
        self.assertEqual(
            next(
                item
                for item in recovered["lifecycle"]
                if item["kind"] == "EvaluationOutcome"
            )["value"]["outcome"],
            "failed",
        )
        self.assertFalse(self._values(ProceduralTermination))

    def test_views_proposals_use_and_unsupported_conflict_or_adequacy_never_grant_truth(
        self,
    ):
        self._generic_request()
        ids = tuple(item.record_id for item in self.boundary.records)
        view = self.host.prepare_view(
            "future.local.investigator",
            (ids[0],),
            selection_limit="One native record; remainder omitted.",
        )
        self.assertEqual(view.native_records, (self.boundary.records[0],))
        stored_view = self.host.lifecycle_value(view.view_id)
        self.assertEqual(stored_view.omitted_native_ids, ids[1:])
        with self.assertRaises(NativeReconstructionError):
            self.host.record_use(view.view_id, (ids[1],), receipt="False use claim")
        self.host.record_use(
            view.view_id,
            (ids[0],),
            receipt="Observed adapter delivery; no hidden examination claim",
        )
        proposal = self.host.propose(
            view.view_id,
            "domain proposition",
            "Conflicting attributed claim",
            (ids[1],),
        )
        evaluated = self.host.evaluate_proposal(proposal)
        self.assertEqual(self.host.lifecycle_value(evaluated).outcome, "unsupported")
        self.assertEqual(
            self.host.lifecycle_value(proposal).cited_native_ids, (ids[1],)
        )
        self.assertIn(ids[0], self.host._records[proposal].native_record_ids)
        stopping = self.host.propose_stop(
            "run", "Generated procedural stopping proposal"
        )
        self.assertEqual(
            self.host.lifecycle_value(self.host.evaluate_proposal(stopping)).outcome,
            "unsupported",
        )
        self.host.terminate("run", "limit_exhausted", "Budget endpoint, not adequacy")
        self.assertEqual(
            self._values(ProceduralTermination)[-1][1].outcome, "limit_exhausted"
        )
        with self.assertRaises(WorkspaceHostError):
            self.host.add_purpose(
                RequestAdmission("fake", "admitted", "fake", "self authority"),
                native_record_ids=(),
            )

    def test_restored_admissions_and_unknown_attempts_have_no_current_execution_authority(
        self,
    ):
        request_id = self._generic_request()
        admission = self.host.admit_request(request_id)
        restored = InvestigationWorkspaceHost(store=self.store, lineage_id="main")
        restored.restore(self._stored(), bases=self.host._bases)
        restored.configure(authority=self.authority, capabilities=(self.capability,))
        with self.assertRaises(WorkspaceHostError) as caught:
            restored.execute_admission(admission)
        self.assertEqual(caught.exception.reason, "historical_or_consumed_admission")
        self.handler.assert_not_called()
        # A separate explicit fresh admission is required; this control performs no effect.
        self.assertEqual(
            restored.lifecycle_value(restored.admit_request(request_id)).outcome,
            "admitted",
        )

    def test_schema1_refuses_host_publication_without_migration_or_execution(self):
        legacy = CheckpointStore.create(self.root / "legacy")
        host = InvestigationWorkspaceHost(store=legacy, lineage_id="main")
        with self.assertRaises(CheckpointStorageError):
            host.initialize(self.boundary)
        self.assertIsNone(host.current)
        with sqlite3.connect(legacy.directory / "workspace.sqlite3") as db:
            self.assertEqual(db.execute("PRAGMA user_version").fetchone(), (1,))
            self.assertEqual(
                db.execute("SELECT count(*) FROM revisions").fetchone(), (0,)
            )

    def test_multiple_admissions_cannot_execute_the_same_request_twice(self):
        request = self._generic_request()
        first = self.host.admit_request(request)
        second = self.host.admit_request(request)
        self.host.execute_admission(first)
        with self.assertRaises(WorkspaceHostError) as caught:
            self.host.execute_admission(second)
        self.assertEqual(
            caught.exception.reason, "request_already_attempted_no_automatic_retry"
        )
        self.handler.assert_called_once()

    def test_changed_material_or_effect_contract_blocks_current_use_and_evaluation(
        self,
    ):
        request = self._generic_request()
        observation, _ = self.host.execute_admission(self.host.admit_request(request))
        self.host.configure(
            authority=self.authority,
            capabilities=(
                replace(self.capability, effects=frozenset({"external_write"})),
            ),
        )
        self.assertEqual(self.host.current_validity(observation).status, "stale")
        self.host.configure(
            authority=self.authority,
            capabilities=(self.capability,),
            methods=(self.method,),
        )
        delayed_request = self.host.request_capability(
            self.host.lifecycle_value(request).purpose_id, "inspect_scope", "Cargo.lock"
        )
        _, _, changed, _, _ = captured_case(python_variant="overlap")
        self.host.publish_native_progress(changed)
        self.assertEqual(
            self.host.current_validity(observation).reasons, ("material_changed",)
        )
        callback = Mock()
        evaluation = self.host.evaluate_native(
            observation, method=self.method, evaluate=callback
        )
        self.assertEqual(self.host.lifecycle_value(evaluation).outcome, "stale")
        callback.assert_not_called()
        rejection = self.host.admit_request(delayed_request)
        self.assertEqual(self.host.lifecycle_value(rejection).outcome, "rejected")
        self.assertEqual(
            self.host.lifecycle_value(rejection).detail, "material_changed"
        )
        self.assertEqual(
            self.host._records[rejection].basis_revision_id,
            self.host._records[delayed_request].basis_revision_id,
        )
        self._stored()

    def test_authority_withdrawn_during_intent_publication_retains_known_non_execution(
        self,
    ):
        request = self._generic_request()
        admission = self.host.admit_request(request)
        real_publish = self.store.publish

        def withdraw(revision):
            receipt = real_publish(revision)
            if revision.lifecycle_history.records[-1].kind == "execution_attempt":
                self.host.configure(
                    authority=replace(self.authority, effects=frozenset()),
                    capabilities=(self.capability,),
                )
            return receipt

        with (
            patch.object(self.store, "publish", side_effect=withdraw),
            self.assertRaises(WorkspaceHostError),
        ):
            self.host.execute_admission(admission)
        self.handler.assert_not_called()
        attempt = self._values(ExecutionAttempt)[0][0].record_id
        self.assertEqual(self.host.attempt_completion(attempt), "not_started")
        self.assertEqual(
            self._values(ExecutionInterruption)[0][1].completion, "not_started"
        )
        self.assertEqual(set(self._cold()["attempt_states"].values()), {"not_started"})

    def test_unconfirmed_intent_acknowledgement_grants_no_execution_or_retry(self):
        request = self._generic_request()
        admission = self.host.admit_request(request)
        real_publish = self.store.publish

        def lose_receipt(revision):
            receipt = real_publish(revision)
            if revision.lifecycle_history.records[-1].kind == "execution_attempt":
                raise UnconfirmedPublication(revision.lineage_id, revision.revision_id)
            return receipt

        with (
            patch.object(self.store, "publish", side_effect=lose_receipt),
            self.assertRaises(UnconfirmedPublication),
        ):
            self.host.execute_admission(admission)
        self.handler.assert_not_called()
        self.assertEqual(
            set(self._cold()["attempt_states"].values()), {"completion_unknown"}
        )
        with self.assertRaises(WorkspaceHostError):
            self.host.execute_admission(admission)

    def test_unrelated_competing_head_is_publication_refusal_not_material_staleness(
        self,
    ):
        request = self._generic_request()
        admission = self.host.admit_request(request)
        record = self.host._records[request]
        original = self.host._bases[record.basis_revision_id]
        real_publish = self.store.publish

        def competing_progress(revision):
            receipt = real_publish(revision)
            if revision.lifecycle_history.records[-1].kind == "execution_attempt":
                real_publish(
                    CheckpointRevision(
                        "main",
                        "competing-progress",
                        revision.revision_id,
                        revision.boundary,
                        revision.lifecycle_history,
                    )
                )
            return receipt

        with (
            patch.object(self.store, "publish", side_effect=competing_progress),
            self.assertRaises(WorkspaceHostError) as caught,
        ):
            self.host.execute_admission(admission)
        self.assertEqual(
            caught.exception.reason, "publication_head_changed_before_execution"
        )
        self.handler.assert_not_called()
        current = self.store.read_revision(
            "main", "competing-progress", expected_target=self.boundary.target
        )
        validity = validate_current_material_basis(
            record,
            original,
            current.revision.boundary,
            original_scope="Cargo.lock",
            current_scope="Cargo.lock",
            current_method=record.method,
        )
        self.assertEqual(validity.status, "valid")

    def test_withdrawn_native_method_returns_unsupported_without_invoking_owner(self):
        request = self._generic_request()
        observation, _ = self.host.execute_admission(self.host.admit_request(request))
        callback = Mock()
        evaluation = self.host.evaluate_native(
            observation, method=self.method, evaluate=callback
        )
        self.assertEqual(self.host.lifecycle_value(evaluation).outcome, "unsupported")
        callback.assert_not_called()

    def test_actual_normal_process_interruption_preserves_intent_observation_and_native_boundaries(
        self,
    ):
        for stage in (
            "before_intent",
            "after_intent",
            "after_observation",
            "after_evaluation",
        ):
            with self.subTest(stage=stage):
                store = CheckpointStore.create(self.root / stage, schema_version=2)
                marker = self.root / (stage + ".provider")
                child = subprocess.run(
                    [
                        sys.executable,
                        "-c",
                        _NORMAL_KILL,
                        str(store.directory),
                        stage,
                        str(marker),
                    ],
                    check=False,
                    env=_CHILD_ENV,
                    capture_output=True,
                    text=True,
                    timeout=30,
                )
                self.assertEqual(child.returncode, -9, child.stderr)
                recovered = self._cold(store)
                kinds = [item["kind"] for item in recovered["lifecycle"]]
                self.assertEqual(
                    marker.exists(), stage in {"after_observation", "after_evaluation"}
                )
                self.assertEqual("ExecutionAttempt" in kinds, stage != "before_intent")
                self.assertEqual(
                    "CapabilityObservation" in kinds,
                    stage in {"after_observation", "after_evaluation"},
                )
                self.assertEqual(
                    "EvaluationOutcome" in kinds, stage == "after_evaluation"
                )
                self.assertNotIn("ProceduralTermination", kinds)
                if stage == "after_intent":
                    self.assertEqual(
                        set(recovered["attempt_states"].values()),
                        {"completion_unknown"},
                    )
                if stage in {"after_observation", "after_evaluation"}:
                    self.assertEqual(
                        set(recovered["attempt_states"].values()), {"observed"}
                    )
                self.assertGreater(recovered["historical_admission_refusals"], 0)

    def test_partial_capture_does_not_claim_completed_or_rebind_an_earlier_snapshot(
        self,
    ):
        inputs = reconstruct_python_support_projection(
            self.boundary, expected_target=self.boundary.target
        ).inputs
        capture = NativeInvestigationCapture()
        capture.start(
            inputs.pull_request,
            inputs.changed_files,
            inputs.dependency_result,
            inputs.source_contexts,
        )
        partial = capture.partial_snapshot()
        self.assertTrue(
            all(
                item.outcome == "not_evaluated"
                for item in partial.records
                if item.family != "investigation_inputs"
            )
        )
        with self.assertRaisesRegex(ValueError, "No completed normal investigation"):
            capture.snapshot()
        self.assertEqual(capture.partial_snapshot(), partial)
        capture.complete()
        self.assertEqual(capture.snapshot(), partial)

    def test_observation_version_support_preserves_v1_and_requires_complete_v2_fields(
        self,
    ):
        legacy = CapabilityObservation(
            "attempt", "empty", "scope", "No retained content in v1"
        )
        kind, version, payload = encode_lifecycle_value(legacy)
        self.assertEqual(version, 1)
        self.assertEqual(
            set(json.loads(payload)["fields"]),
            {"attempt_id", "outcome", "scope", "detail"},
        )
        self.assertIsNone(
            decode_lifecycle_value(kind, version, payload).retained_content
        )
        retained = replace(legacy, representation="bounded-text/1", retained_content="")
        kind, version, payload = encode_lifecycle_value(retained)
        self.assertEqual(version, 2)
        self.assertEqual(decode_lifecycle_value(kind, version, payload), retained)
        missing = json.loads(payload)
        del missing["fields"]["retained_content"]
        with self.assertRaises(NativeReconstructionError):
            decode_lifecycle_value(kind, 2, json.dumps(missing).encode())
        with self.assertRaisesRegex(
            NativeReconstructionError, "unsupported_lifecycle_codec"
        ):
            decode_lifecycle_value(kind, 3, payload)


if __name__ == "__main__":
    unittest.main()
