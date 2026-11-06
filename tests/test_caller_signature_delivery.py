"""Normal explicit CLI delivery with actual clients and controlled HTTP responses.

The existing acquisition control supplies a genuine old/proposed source pair.
These checks exercise application, installed worker, report, lifecycle/store and
offline CLI together. Faults target publication acknowledgement and consumer
delivery independently of source-comparison outcomes.
"""
from __future__ import annotations

import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch

import test_caller_signature_source_acquisition as acquisition_controls

from upgradepilot.cli import main
from upgradepilot.report_file import read_report, encode_report, ReportValidationError
from upgradepilot.workspace.checkpoint_revision import CheckpointStorageError, UnconfirmedPublication
from upgradepilot.workspace.checkpoint_store import CheckpointStore

_COLD_OPEN = r'''
import ast, os, socket, sys
from unittest.mock import patch
from upgradepilot.cli import main
from upgradepilot.caller_signature.correspondence import discover_source_candidates
from upgradepilot.caller_signature.analysis import compare_arguments
from upgradepilot.maintainer_action import synthesize_maintainer_action
blocked_names = {
    'acquire_dependency_inputs', 'collect_source_progress', 'run_source_analysis',
    'produce_source_analysis', 'discover_source_candidates', 'compare_arguments',
    'extract_python_source', 'analyze_python_bindings', 'synthesize_maintainer_action',
    'project_caller_signature_report', 'project_investigation_report',
}
def guard(frame, event, arg):
    if event == 'call':
        module = frame.f_globals.get('__name__', '')
        name = frame.f_code.co_name
        if ((module.startswith('upgradepilot.') and name in blocked_names)
            or (module == 'ast' and name == 'parse')
            or (module == 'os' and name == 'getenv')):
            raise AssertionError('forbidden cold-open operation ' + module + '.' + name)
sys.setprofile(guard)
with patch.object(socket.socket, 'connect', side_effect=AssertionError('network forbidden')):
    result = main(sys.argv[1:])
    # Discriminating controls prove the guard actually rejects re-entry.
    for forbidden in (
        lambda: ast.parse('pass'), lambda: os.getenv('GITHUB_TOKEN'),
        lambda: discover_source_candidates(None, None, None),
        lambda: compare_arguments(None, None, None),
        lambda: synthesize_maintainer_action(None),
    ):
        # Python clears a profile hook when it raises. Rearm each control.
        sys.setprofile(guard)
        try: forbidden()
        except AssertionError as error:
            assert str(error).startswith('forbidden cold-open operation '), error
        else: raise AssertionError('inactive cold-open guard')
sys.setprofile(None)
raise SystemExit(result)
'''


class CallerSignatureDeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="upgradepilot-delivery-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.store_path = self.root / "store"
        self.report_path = self.root / "report.json"

    def run_cli(self, arguments):
        output = io.StringIO()
        with redirect_stdout(output):
            code = main(arguments)
        return code, output.getvalue()

    def live(self, *, proposed_missing=False, save=True, durable=True, forwarded=True,
             guard_arguments=(), target_object_id_length=40):
        identity, session, requests = acquisition_controls.NativeSourceClientCompositionTests().controlled_transport(
            proposed_missing=proposed_missing, forwarded=forwarded,
            target_object_id_length=target_object_id_length,
        )
        arguments = [identity.repository, str(identity.number), "--evidence-profile", "caller-signature", *guard_arguments]
        if durable:
            arguments += ["--workspace-store", str(self.store_path)]
        if save:
            arguments += ["--save-report", str(self.report_path)]
        with patch("upgradepilot.cli.AcquisitionSession", return_value=session), patch("socket.socket.connect", side_effect=AssertionError("live network forbidden")):
            code, output = self.run_cli(arguments)
        return code, output, requests

    def revision_id(self, output):
        return next(line.removeprefix("Confirmed revision: ") for line in output.splitlines() if line.startswith("Confirmed revision: "))

    def cold(self, revision_id, *extra):
        child = subprocess.run(
            [sys.executable, "-c", _COLD_OPEN, "--open-workspace", str(self.store_path),
             "--revision", revision_id, *extra],
            cwd=self.root, env=dict(os.environ, PYTHONPATH=os.pathsep.join(str(Path(p).absolute()) for p in sys.path if p)),
            capture_output=True, text=True, timeout=45,
        )
        self.assertEqual(child.returncode, 0, child.stdout + child.stderr)
        return child.stdout

    def test_normal_cli_report_source_and_exact_workspace_open(self):
        code, output, requests = self.live()
        self.assertEqual(code, 0, output)
        self.assertEqual(len(requests), 23)
        report = read_report(self.report_path)
        self.assertEqual(report.action.state, "abstain")
        candidates = [a for a in report.assessments if a.assessment_id.startswith("caller-signature-comparison-")]
        self.assertEqual({a.state for a in candidates}, {"bound", "rejected"})
        self.assertEqual(len(candidates), 2)
        analysis = next(a for a in report.assessments if a.assessment_id == "caller-signature-analysis")
        self.assertIn("1", [f.value for f in analysis.facts if f.name == "distinct_roots"])
        self.assertTrue(all(a.status == "not_evaluated" for a in report.assessments if a.assessment_id in {"ci", "runtime"}))
        retained = next(s for s in report.sources if s.retention == "retained_text" and any(f.name == "path" and f.value == "demo/_core.py" for f in s.identity))
        revision_id = self.revision_id(output)
        from upgradepilot.caller_signature import worker
        from upgradepilot.caller_signature_delivery import open_caller_signature_checkpoint
        opened = open_caller_signature_checkpoint(CheckpointStore.open(self.store_path, read_only=True), revision_id)
        self.assertEqual(Path(opened.native.comparison.worker_module_origin).resolve(), Path(worker.__file__).resolve())
        with patch("upgradepilot.cli.AcquisitionSession", side_effect=AssertionError("acquisition forbidden")), patch("upgradepilot.cli.os.getenv", side_effect=AssertionError("credentials forbidden")), patch("upgradepilot.report_projection.synthesize_maintainer_action", side_effect=AssertionError("synthesis forbidden")):
            code, reopened = self.run_cli(["--open-workspace", str(self.store_path), "--revision", revision_id])
            self.assertEqual(code, 0, reopened)
            self.assertIn(report.report_id, reopened)
            code, source = self.run_cli(["--open-workspace", str(self.store_path), "--revision", revision_id, "--show-source", retained.source_id])
            self.assertEqual(code, 0, source)
            self.assertIn(retained.content, source)
        restored = self.cold(revision_id)
        self.assertIn(report.report_id, restored)
        self.assertIn("report: True", restored)
        self.assertIn(retained.content, self.cold(revision_id, "--show-source", retained.source_id))

    def test_matching_cli_guards_preserve_comparisons_sources_and_request_allocation(self):
        """Exercise the real CLI/application/clients/worker, including absent guards.

        Uppercase and individual guards must reach the same native comparison;
        supplying a guard must not add another prefix or change source work.
        """
        from upgradepilot.caller_signature_delivery import open_caller_signature_checkpoint
        cases = (
            ("unguarded", (), 40),
            ("both", ("--expected-base", "B"*40, "--expected-head", "A"*40), 40),
            ("base", ("--expected-base", "b"*40), 40),
            ("head", ("--expected-head", "a"*40), 40),
            ("sha256", ("--expected-base", "B"*64, "--expected-head", "A"*64), 64),
        )
        reference = None
        for label, arguments, size in cases:
            with self.subTest(label=label):
                self.store_path = self.root / f"{label}-store"
                self.report_path = self.root / f"{label}-report.json"
                code, output, requests = self.live(guard_arguments=arguments, target_object_id_length=size)
                self.assertEqual(code, 0, output)
                self.assertEqual(len(requests), 23)
                # The normal changed-file client rechecks PR identity after its
                # paginated diff read. Guarding must preserve that protection.
                self.assertEqual(sum(r.url.endswith("/pulls/1145") for r in requests), 2)
                report = read_report(self.report_path)
                comparisons = tuple(a for a in report.assessments if a.assessment_id.startswith("caller-signature-comparison-"))
                self.assertEqual({a.state for a in comparisons}, {"bound", "rejected"})
                if size == 40:
                    # New observations have distinct times and native snapshot IDs.
                    # Compare original text plus deterministic native facts/paths/
                    # premises/admission/work, not byte identity of timed envelopes.
                    sources = tuple(replace(source, retrieved_at=None,
                        identity=tuple(f for f in source.identity if f.name != "acquisition_snapshot_at"))
                        for source in report.sources if source.kind != "producer_assessment")
                    opened = open_caller_signature_checkpoint(
                        CheckpointStore.open(self.store_path, read_only=True), self.revision_id(output))
                    native = opened.native
                    evidence = (comparisons, sources, report.production_limits, report.action,
                        native.sources.catalog, native.sources.modules, native.sources.analysis_limits,
                        native.sources.acquisition.transport.limits, native.comparison.result)
                    if reference is None:
                        reference = evidence
                    else:
                        self.assertEqual(evidence, reference)
                else:
                    self.assertIn("a"*64, [fact.value for fact in report.identity])

    def test_cli_revision_mismatch_stops_after_one_charged_pr_observation(self):
        for flag in ("--expected-base", "--expected-head"):
            with self.subTest(flag=flag):
                identity, session, dispatched = acquisition_controls.NativeSourceClientCompositionTests().controlled_transport()
                self.store_path = self.root / (flag.removeprefix("--") + "-store")
                with patch("upgradepilot.cli.AcquisitionSession", return_value=session), \
                     patch("socket.socket.connect", side_effect=AssertionError("network forbidden")), \
                     patch("upgradepilot.investigation.collect_source_progress") as sources, \
                     patch("upgradepilot.investigation.run_source_analysis") as worker:
                    code, output = self.run_cli([identity.repository, str(identity.number),
                        "--evidence-profile", "caller-signature", "--workspace-store", str(self.store_path),
                        "--save-report", str(self.report_path), flag, "f"*40])
                self.assertEqual(code, 3, output)
                self.assertEqual((len(dispatched), session.github_requests, session.provider_requests), (1, 1, 1))
                self.assertTrue(dispatched[0].url.endswith("/pulls/1145"))
                sources.assert_not_called()
                worker.assert_not_called()
                self.assertIn("no confirmed revision", output)
                self.assertFalse(self.report_path.exists())
                receipt = CheckpointStore.open(self.store_path).backup(self.root / flag.removeprefix("--"))
                self.assertEqual(receipt.revision_count, 0)

    def test_application_delivery_forwards_individual_guards_before_source_work(self):
        from upgradepilot.caller_signature_delivery import investigate_and_deliver_caller_signature
        from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost
        for keyword in ("expected_base", "expected_head"):
            with self.subTest(keyword=keyword):
                identity, session, dispatched = acquisition_controls.NativeSourceClientCompositionTests().controlled_transport()
                host = InvestigationWorkspaceHost()
                with patch("socket.socket.connect", side_effect=AssertionError("network forbidden")):
                    outcome = investigate_and_deliver_caller_signature(identity.repository, identity.number,
                        session=session, host=host, **{keyword: "f"*40})
                self.assertEqual((len(dispatched), session.github_requests), (1, 1))
                self.assertIsNone(outcome.recoverable_revision)
                self.assertIsNone(outcome.report)
                self.assertEqual([(p.stage, p.reason) for p in outcome.problems], [("acquisition", "ValueError")])

    def test_guard_argument_errors_precede_credentials_sessions_and_offline_reads(self):
        for flag in ("--expected-base", "--expected-head"):
            cases = [
                ["owner/target", "1", "--evidence-profile", "caller-signature", flag, value]
                for value in ("main", "a"*39, "a"*41, "a"*63, "g"*40, " " + "a"*40, "a"*40 + "\n")
            ]
            cases += [
                ["owner/target", "1", "--github-auth", "token-env", flag, "a"*40],
                ["--open-report", "missing.json", flag, "a"*40],
                ["--open-workspace", "missing", "--revision", "x", flag, "a"*40],
                ["--open-report", "missing.json", "--evidence-profile", "caller-signature", flag, "a"*40],
            ]
            for arguments in cases:
                with self.subTest(arguments=arguments), \
                     patch("upgradepilot.cli.AcquisitionSession") as session, \
                     patch("upgradepilot.cli.os.getenv") as getenv, \
                     patch("upgradepilot.cli.read_report") as report, \
                     patch("upgradepilot.cli._open_workspace") as workspace, redirect_stderr(io.StringIO()):
                    with self.assertRaises(SystemExit) as caught:
                        self.run_cli(arguments)
                    self.assertEqual(caught.exception.code, 2)
                    session.assert_not_called()
                    getenv.assert_not_called()
                    report.assert_not_called()
                    workspace.assert_not_called()

    def test_analysis_failure_offers_exact_source_only_cold_recovery(self):
        with patch("upgradepilot.investigation.run_source_analysis", side_effect=RuntimeError("controlled analysis failure")) as worker:
            code, output, requests = self.live()
        self.assertEqual(code, 10, output)
        self.assertEqual(worker.call_count, 1)
        self.assertEqual(len(requests), 23)
        self.assertFalse(self.report_path.exists())
        revision_id = self.revision_id(output)
        restored = self.cold(revision_id)
        self.assertIn("retained report/action absent", restored)
        self.assertIn("comparison: False; report: False", restored)
        file_id = next(line.split()[2] for line in restored.splitlines() if line.startswith("Retained file:"))
        self.assertIn("BEGIN LITERAL SOURCE TEXT", self.cold(revision_id, "--show-source", file_id))

    def test_partial_acquisition_is_successful_delivery_with_honest_coverage(self):
        code, output, _ = self.live(proposed_missing=True, forwarded=False)
        self.assertEqual(code, 0, output)
        report = read_report(self.report_path)
        coverage = next(a for a in report.assessments if a.assessment_id == "caller-signature-coverage")
        self.assertEqual(coverage.state, "partial")
        self.assertEqual(report.action.state, "abstain")
        self.assertIn("unavailable", self.report_path.read_text())

    def test_unsupported_dependency_delivers_explained_non_evaluation(self):
        from upgradepilot.dependency.change import DependencyChangeProblem
        from upgradepilot.investigation_inputs import acquire_dependency_inputs
        def unsupported(*args, **kwargs):
            inputs = acquire_dependency_inputs(*args, **kwargs)
            return replace(inputs, dependency=DependencyChangeProblem(
                "no_supported_dependency_file", "Controlled unsupported declaration."), source_contexts=())
        with patch("upgradepilot.investigation.acquire_dependency_inputs", side_effect=unsupported), patch("upgradepilot.investigation.run_source_analysis") as worker:
            code, output, requests = self.live()
        self.assertEqual(code, 0, output)
        worker.assert_not_called()
        self.assertEqual(len(requests), 3)
        report = read_report(self.report_path)
        self.assertEqual(next(a for a in report.assessments if a.assessment_id == "dependency").state, "unsupported")
        self.assertIn(report.report_id, self.cold(self.revision_id(output)))

    def test_external_save_failure_preserves_workspace_report_delivery(self):
        self.report_path.write_text("existing")
        code, output, _ = self.live()
        self.assertEqual(code, 5, output)
        self.assertEqual(self.report_path.read_text(), "existing")
        self.assertIn("report: True", self.cold(self.revision_id(output)))

    def test_report_projection_failure_preserves_comparison_and_no_report(self):
        with patch("upgradepilot.caller_signature_delivery.project_caller_signature_report", side_effect=ValueError("controlled projection failure")):
            code, output, _ = self.live()
        self.assertEqual(code, 8, output)
        self.assertFalse(self.report_path.exists())
        self.assertIn("comparison: True; report: False", self.cold(self.revision_id(output)))

    def test_lost_report_acknowledgement_is_inspected_without_retry(self):
        real_publish = CheckpointStore.publish
        attempted = []
        def lose_receipt(store, revision):
            receipt = real_publish(store, revision)
            if revision.lifecycle_history.records and revision.lifecycle_history.records[-1].kind == "view_delivery":
                attempted.append(revision)
                raise UnconfirmedPublication(revision.lineage_id, revision.revision_id)
            return receipt
        with patch.object(CheckpointStore, "publish", lose_receipt):
            code, output, requests = self.live()
        self.assertEqual(code, 11, output)
        self.assertEqual(len(attempted), 1)
        self.assertEqual(len(requests), 23)
        self.assertIn("exact inspection: published", output)
        self.assertEqual(self.revision_id(output), attempted[0].revision_id)
        self.assertIn("report: True", self.cold(attempted[0].revision_id))

    def test_failed_acknowledgement_inspection_preserves_unknown_and_predecessor(self):
        real_publish = CheckpointStore.publish
        attempted = []
        def lose_receipt(store, revision):
            receipt = real_publish(store, revision)
            if revision.lifecycle_history.records and revision.lifecycle_history.records[-1].kind == "view_delivery":
                attempted.append(revision)
                raise UnconfirmedPublication(revision.lineage_id, revision.revision_id)
            return receipt
        with patch.object(CheckpointStore, "publish", lose_receipt), patch.object(CheckpointStore, "inspect_publication", side_effect=CheckpointStorageError("storage_io_error", "controlled inspection failure")):
            code, output, requests = self.live()
        self.assertEqual(code, 11, output)
        self.assertEqual(len(requests), 23)
        self.assertIn("exact inspection: unknown", output)
        self.assertEqual(self.revision_id(output), attempted[0].predecessor_id)
        self.assertIn("report: False", self.cold(self.revision_id(output)))
        self.assertIn("report: True", self.cold(attempted[0].revision_id))

    def test_known_failed_report_publication_preserves_predecessor(self):
        real_publish = CheckpointStore.publish
        def fail_delivery(store, revision):
            if revision.lifecycle_history.records and revision.lifecycle_history.records[-1].kind == "view_delivery":
                raise CheckpointStorageError("storage_full", "controlled full disk")
            return real_publish(store, revision)
        with patch.object(CheckpointStore, "publish", fail_delivery):
            code, output, _ = self.live()
        self.assertEqual(code, 11, output)
        self.assertIn("exact inspection: not_published", output)
        self.assertIn("comparison: True; report: False", self.cold(self.revision_id(output)))

    def test_volatile_delivery_and_preinitialization_failure_have_earned_handoffs(self):
        code, output, _ = self.live(durable=False)
        self.assertEqual(code, 0, output)
        self.assertIn("volatile-only", output)
        self.assertNotIn("Open confirmed revision:", output)
        from upgradepilot.github.api import GitHubAcquisitionError
        with patch("upgradepilot.investigation.acquire_dependency_inputs", side_effect=GitHubAcquisitionError("offline", reason="transport_error")):
            code, output, requests = self.live(save=False)
        self.assertEqual(code, 3, output)
        self.assertEqual(requests, [])
        self.assertIn("no confirmed revision", output)
        self.assertNotIn("Open confirmed revision:", output)

    def test_offline_argument_conflicts_fail_before_clients_or_credentials(self):
        for extra in (["--github-auth", "anonymous"], ["--evidence-profile", "caller-signature"],
                      ["owner/target", "1"], ["--save-report", "x"], ["--workspace-store", "x"],
                      ["--open-report", "x"]):
            with self.subTest(extra=extra), patch("upgradepilot.cli.AcquisitionSession") as client, patch("upgradepilot.cli.os.getenv") as getenv, redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as caught:
                    self.run_cli(["--open-workspace", str(self.store_path), "--revision", "x", *extra])
                self.assertEqual(caught.exception.code, 2)
                client.assert_not_called()
                getenv.assert_not_called()

    def test_missing_selected_revision_has_no_fallback(self):
        self.live()
        code, output = self.run_cli(["--open-workspace", str(self.store_path), "--revision", "absent"])
        self.assertEqual(code, 9, output)
        self.assertIn("missing_checkpoint_revision", output)

    def test_report_reader_refuses_unadmitted_comparison_states(self):
        self.live()
        report = read_report(self.report_path)
        for state in ("compatible", "safe", "tested"):
            assessments = tuple(replace(a, state=state) if a.assessment_id.startswith("caller-signature-comparison-") else a
                                for a in report.assessments)
            with self.subTest(state=state), self.assertRaises(ReportValidationError):
                encode_report(replace(report, assessments=assessments))
        code, output = self.run_cli(["--open-report", str(self.report_path)])
        self.assertEqual(code, 0, output)
        self.assertIn(report.report_id, output)

    def test_render_failure_preserves_the_retained_report(self):
        with patch("upgradepilot.cli.render_investigation_report", side_effect=ValueError("controlled render failure")):
            code, output, _ = self.live()
        self.assertEqual(code, 8, output)
        self.assertIn("report: True", self.cold(self.revision_id(output)))

    def test_report_encoding_capacity_refusal_preserves_evidence(self):
        with patch("upgradepilot.report_file.MAX_REPORT_BYTES", 1024):
            code, output, _ = self.live()
        self.assertEqual(code, 8, output)
        self.assertFalse(self.report_path.exists())
        self.assertIn("comparison: True; report: False", self.cold(self.revision_id(output)))

    def test_competing_publication_never_switches_to_the_competing_head(self):
        real_publish = CheckpointStore.publish
        attempted = []
        def conflict(store, revision):
            if revision.lifecycle_history.records and revision.lifecycle_history.records[-1].kind == "view_delivery":
                attempted.append(revision)
                real_publish(store, replace(revision, revision_id="competing-report"))
            return real_publish(store, revision)
        with patch.object(CheckpointStore, "publish", conflict):
            code, output, requests = self.live()
        self.assertEqual(code, 11, output)
        self.assertEqual(len(requests), 23)
        self.assertEqual(len(attempted), 1)
        self.assertEqual(self.revision_id(output), attempted[0].predecessor_id)
        self.assertIn("exact inspection: not_published", output)
        restored = self.cold(self.revision_id(output))
        self.assertIn("Later revisions excluded: 1", restored)
        self.assertIn("report: False", restored)

    def test_preexecution_head_conflict_is_publication_failure_without_pending_write(self):
        real_publish = CheckpointStore.publish
        def advance_after_intent(store, revision):
            receipt = real_publish(store, revision)
            if revision.lifecycle_history.records and revision.lifecycle_history.records[-1].kind == "execution_attempt":
                real_publish(store, replace(revision, revision_id="competing-before-execution", predecessor_id=revision.revision_id))
            return receipt
        with patch.object(CheckpointStore, "publish", advance_after_intent):
            code, output, requests = self.live()
        self.assertEqual(code, 11, output)
        self.assertEqual(len(requests), 3)
        self.assertIn("publication_head_changed_before_execution", output)
        self.assertNotIn("Publication attempt:", output)
        self.assertIn("Later revisions excluded: 1", self.cold(self.revision_id(output)))

    def test_fixed_workspace_consumer_offers_native_sources_and_comparison_pages(self):
        from upgradepilot.caller_signature_delivery import open_caller_signature_checkpoint
        from upgradepilot.workspace.consumer_access import WorkspaceEvidenceAccess
        from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost
        from upgradepilot.workspace.lifecycle_records import InvestigationNeed, ViewDelivery
        _, output, _ = self.live()
        store = CheckpointStore.open(self.store_path)
        opened = open_caller_signature_checkpoint(store, self.revision_id(output))
        revision = opened.selected.revision
        host = InvestigationWorkspaceHost(store=store, lineage_id=revision.lineage_id)
        bases = {r.basis_revision_id: store.read_revision(revision.lineage_id, r.basis_revision_id,
                  expected_target=revision.boundary.target).revision.boundary for r in revision.lifecycle_history.records}
        host.restore(opened.selected, bases=bases)
        access = WorkspaceEvidenceAccess(host, opened.native.sources.catalog,
            native_families=("caller_signature_sources", "caller_signature_comparison"), max_native_bytes=4096)
        host.configure(authority=None, capabilities=(), methods=(access.method,))
        ids = tuple(r.record_id for r in revision.boundary.records)
        purpose = host.add_purpose(InvestigationNeed("source_review", "Inspect retained evidence.", access.scope), native_record_ids=ids)
        delivery = access.native_view(purpose, ("caller_signature_sources", "caller_signature_comparison"))
        value = host.lifecycle_value(delivery)
        self.assertIsInstance(value, ViewDelivery)
        payload = json.loads(value.retained_content)
        self.assertTrue(payload["omitted"])
        record_id = next(r.record_id for r in revision.boundary.records if r.family == "caller_signature_comparison")
        page = access.native_page(purpose, record_id, character_count=100)
        page_content = json.loads(host.lifecycle_value(page).retained_content)
        original = next(r.payload.decode() for r in revision.boundary.records if r.record_id == record_id)
        self.assertEqual(page_content["text"], original[:100])

    def test_unsupported_retained_report_method_refuses_without_fallback(self):
        from upgradepilot.caller_signature_delivery import REPORT_METHOD, REPORT_REPRESENTATION, open_caller_signature_checkpoint
        from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost
        from upgradepilot.workspace.lifecycle_records import InvestigationNeed
        _, output, _ = self.live()
        original_id = self.revision_id(output)
        store = CheckpointStore.open(self.store_path)
        opened = open_caller_signature_checkpoint(store, original_id)
        revision = opened.selected.revision
        host = InvestigationWorkspaceHost(store=store, lineage_id=revision.lineage_id)
        bases = {r.basis_revision_id: store.read_revision(revision.lineage_id, r.basis_revision_id,
                  expected_target=revision.boundary.target).revision.boundary for r in revision.lifecycle_history.records}
        host.restore(opened.selected, bases=bases)
        unsupported = replace(REPORT_METHOD, version="999")
        host.configure(authority=None, capabilities=(), methods=(unsupported,))
        ids = tuple(r.record_id for r in revision.boundary.records)
        purpose = host.add_purpose(InvestigationNeed("report", "Controlled unsupported delivery.", "report"), native_record_ids=ids)
        view = host.prepare_view("report", ids, selection_limit="Controlled complete native basis.")
        host.deliver_view(purpose, view.view_id, representation=REPORT_REPRESENTATION,
                          content=encode_report(opened.report).decode(), method=unsupported)
        code, output = self.run_cli(["--open-workspace", str(self.store_path), "--revision", host.current.revision_id])
        self.assertEqual(code, 9, output)
        self.assertIn("unsupported_report_projection", output)
        self.assertIn(opened.report.report_id, self.cold(original_id))

    def test_unknown_report_representation_is_unsupported_rather_than_absent(self):
        from upgradepilot.caller_signature_delivery import REPORT_METHOD, open_caller_signature_checkpoint
        from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost
        from upgradepilot.workspace.lifecycle_records import InvestigationNeed
        _, output, _ = self.live()
        store = CheckpointStore.open(self.store_path)
        opened = open_caller_signature_checkpoint(store, self.revision_id(output))
        revision = opened.selected.revision
        host = InvestigationWorkspaceHost(store=store, lineage_id=revision.lineage_id)
        bases = {r.basis_revision_id: store.read_revision(revision.lineage_id, r.basis_revision_id,
                  expected_target=revision.boundary.target).revision.boundary for r in revision.lifecycle_history.records}
        host.restore(opened.selected, bases=bases)
        host.configure(authority=None, capabilities=(), methods=(REPORT_METHOD,))
        ids = tuple(r.record_id for r in revision.boundary.records)
        purpose = host.add_purpose(InvestigationNeed("report", "Controlled future encoding.", "report"), native_record_ids=ids)
        view = host.prepare_view("report", ids, selection_limit="Controlled complete native basis.")
        host.deliver_view(purpose, view.view_id, representation="upgradepilot-investigation-report/schema999",
                          content=encode_report(opened.report).decode(), method=REPORT_METHOD)
        code, output = self.run_cli(["--open-workspace", str(self.store_path), "--revision", host.current.revision_id])
        self.assertEqual(code, 9, output)
        self.assertIn("unsupported_report_projection", output)


if __name__ == "__main__":
    unittest.main()
