"""Native source/comparison material joins, publication and fixed cold recovery."""
from contextlib import ExitStack
from dataclasses import replace
from datetime import UTC, datetime
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from unittest import TestCase
from unittest.mock import patch

from test_source_correspondence import material
from upgradepilot.caller_signature import source_evidence as se
from upgradepilot.caller_signature.evidence import AnalysisLimits, MeasuredDuration
from upgradepilot.caller_signature.source_codec import decode_sources, encode_sources
from upgradepilot.caller_signature.worker import run_source_analysis
from upgradepilot.dependency.change import DependencyChangeSourceEvidence, DependencyVersionChange
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.github.tag import GitHubTagCommitEvidence, GitHubTagRepositoryRedirect
from upgradepilot.pypi.release import PackageReleaseEvidence, ProjectUrlCandidate
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost
from upgradepilot.workspace.native_boundary import CapturedNativeBoundary
from upgradepilot.workspace.native_capture import NativeInvestigationCapture
from upgradepilot.workspace.native_projection import reconstruct_caller_signature_projection, reconstruct_ci_projection
from upgradepilot.workspace.native_representation import NativeReconstructionError, json_bytes, parse_json
from upgradepilot.workspace.source_access import RetainedSourceCatalog


def controlled_sources(*, limits=None, full=False, source_texts=None):
    texts = source_texts or ("from vendor import send\nsend(option=1)\n",
        "def send(*, option=None):\n pass\n", "def send():\n pass\n")
    catalog, modules = material(*texts)
    catalog = RetainedSourceCatalog(tuple(replace(s, revision={"old": "c" * 40, "new": "d" * 40}.get(s.source_id, s.revision)) for s in catalog.scopes), catalog.files, target=catalog.target)
    scopes = {s.source_id: s for s in catalog.scopes}
    declaration = se.SourceDependencyDeclaration("owner/target@" + "a" * 40 + ":requirements.txt", "line:1", "vendor==1.0", "vendor", "==1.0", (), None, "requirements")
    target_files, requests = [], []
    now = datetime(2026, 11, 2, tzinfo=UTC)
    for file in catalog.files:
        scope = scopes[file.source_id]
        size, digest = len(file.content.encode()), sha256(file.content.encode()).hexdigest()
        if file.source_id == "target":
            target_files.append(se.SourceFileReceipt(f"{scope.repository}@{scope.revision}:{file.path}", digest, size))
        else:
            module = next(m for m in modules if m.source_id == file.source_id)
            request = se.ModuleSourceRequest(module.package, module.version, module.module, module.role, None)
            association, tags = None, ()
            if full:
                link = ProjectUrlCandidate("Source", "https://github.com/" + scope.repository)
                release = PackageReleaseEvidence(module.package, module.package, module.version, module.package, module.version,
                    "https://pypi.org/pypi/vendor/" + module.version + "/json", now, 1, (), (link,))
                provenance = se.SourcePublisherInspection("source_unavailable", "Controlled missing registry publisher", None, ())
                association = se.PackageSourceAssociation(release, scope.repository, (link,), (), provenance, "exact_release_publisher_declared_repository")
                tags = (GitHubTagCommitEvidence(scope.repository, module.version, "refs/tags/" + module.version, "commit", scope.revision, scope.revision, (), now),)
            requests.append(se.ModuleSourceReceipt(request, "module_examined", None, scope.repository, scope.revision, file.path, digest, size,
                "exact_release_publisher_declared_repository", "source_unavailable", (se.SourceTagCommit(module.version, scope.revision),),
                se.SourceDependencyMetadata(module.package, module.version, "https://pypi.org/pypi/vendor/" + module.version + "/json", (), ()), (),
                association, tags, () if full else ("full_association_observations_not_retained", "full_tag_observations_not_retained")))
    target = se.TargetSourceReceipt(catalog.target.repository, catalog.target.head_sha, "b" * 40, 1, False,
        tuple(target_files), (declaration,), (), (), (), (), sum(f.utf8_bytes for f in target_files), ("source_only_not_execution",))
    receipt = se.SourceAcquisitionReceipt("native_observation" if full else "controlled_observation", "complete", now, target,
        tuple(requests), (), (), (), (), (), (), (), se.SourceAcquisitionWork((("vendor", "1.0"), ("vendor", "2.0")), 2, sum(r.utf8_bytes for r in requests)),
        None, (), ("transport_receipt_unavailable",))
    return se.CallerSignatureSources(catalog, modules, limits or AnalysisLimits(), receipt)


def started_capture(source):
    target = source.catalog.target
    identity = PullRequestIdentity(target.repository, target.pull_number, "controlled dependency change", "open", False,
        "author", "main", target.base_sha, "upgrade", target.head_sha, 1)
    change = DependencyVersionChange(target.normalized_package, target.normalized_package, target.old_version, target.proposed_version,
        (DependencyChangeSourceEvidence("requirements.txt", "exact_requirement", "changed_file_patch"),))
    capture = NativeInvestigationCapture()
    capture.start(identity, (ChangedFile("requirements.txt", "modified", 1, 1, 2, None),), change, ())
    return capture


def altered(boundary, family, **changes):
    return replace(boundary, records=tuple(replace(r, **changes) if r.family == family else r for r in boundary.records))


class CallerSignatureWorkspaceTests(TestCase):
    def moved_sources(self, *, verified=True):
        source = controlled_sources(full=True)
        first, second = source.acquisition.module_requests
        tag = first.request.version
        redirect = GitHubTagRepositoryRedirect("old/vendor", tag, 123, f"/repositories/123/git/ref/tags/{tag}")
        move = se.SourceRepositoryMove(redirect, "owner/vendor", verified)
        link = ProjectUrlCandidate("Source", "https://github.com/old/vendor")
        association = replace(first.association, repository="old/vendor", declarations=(link,),
                              release=replace(first.association.release, project_urls=(link,)))
        paths = [(f"/repos/old/vendor/git/ref/tags/{tag}", 301), ("/repositories/123", 200)]
        if verified:
            paths.extend((("/repos/owner/vendor", 200), (f"/repos/owner/vendor/git/ref/tags/{tag}", 200)))
        events = tuple(se.SourceRequestEvent("source", "api.github.com", path, number, number, 10, status, "received", None)
                       for number, (path, status) in enumerate(paths, 1))
        limits = se.SourceAcquisitionLimits(50, 100, 8 * 1024 * 1024, 32 * 1024 * 1024,
            MeasuredDuration.from_seconds(180.0, "acquisition_limit"), 24, 16, 4)
        transport = se.SourceTransportReceipt(limits, "anonymous", len(events), len(events), 10 * len(events),
            MeasuredDuration.from_seconds(.1, "acquisition_elapsed"),
            "cooperative_monotonic_checks_and_bounded_socket_timeouts", (), events, "none", ())
        first = replace(first, association=association, repository_move=move)
        receipt = replace(source.acquisition, module_requests=(first, second), transport=transport, retention_gaps=())
        if verified:
            return replace(source, acquisition=receipt)
        first = replace(first, state="unavailable", repository="old/vendor", revision=None, path=None,
            problem=se.SourceProblem("adapter_acquisition", "transport_error", "Canonical identity request failed"),
            tags=(), tag_commits=(), sha256=None, utf8_bytes=None)
        return replace(source, catalog=None, modules=(), acquisition=replace(receipt, state="partial", module_requests=(first,)))

    def test_move_version_round_trips_with_prior_format_and_comparison(self):
        source = self.moved_sources()
        capture = started_capture(source)
        with tempfile.TemporaryDirectory() as tmp:
            store = CheckpointStore.create(Path(tmp) / "store", schema_version=2)
            host = InvestigationWorkspaceHost(store=store, lineage_id="control")
            host.initialize(capture.partial_snapshot())
            revisions = []
            run = run_source_analysis(source.analysis_input())
            for captured in (controlled_sources(full=True), self.moved_sources(verified=False), source):
                capture.capture_caller_signature_sources(captured)
                if captured is source:
                    capture.capture_caller_signature_comparison(run)
                host.publish_native_progress(capture.partial_snapshot())
                revisions.append(host.current.revision_id)
            with ExitStack() as stack:
                for hook in ("requests.sessions.Session.request", "ast.parse", "upgradepilot.caller_signature.worker.run_source_analysis"):
                    stack.enter_context(patch(hook, side_effect=AssertionError("Producer invoked during recovery")))
                reader = CheckpointStore.open(store.directory, read_only=True)
                target = source.catalog.target
                for revision, version, state in zip(revisions, (1, 2, 2), (None, False, True), strict=True):
                    boundary = reader.read_revision("control", revision, expected_target=target).revision.boundary
                    restored = reconstruct_caller_signature_projection(boundary, expected_target=target)
                    record = next(r for r in boundary.records if r.family == "caller_signature_sources")
                    self.assertEqual((record.codec_version, record.producer_version), (version, str(version)))
                    move = restored.sources.acquisition.module_requests[0].repository_move
                    self.assertEqual(move.verified if move else None, state)
                    if state is True:
                        self.assertEqual(restored.sources.catalog.files, source.catalog.files)
                        self.assertEqual(restored.comparison, run)

    def test_move_reader_refuses_broken_identity_tag_and_file_joins(self):
        source = self.moved_sources()
        first, second = source.acquisition.module_requests
        move = first.repository_move
        payload = encode_sources(source, version=2)
        with self.assertRaises(ValueError):
            decode_sources(payload)
        for changed in (
            replace(first, repository_move=replace(move, redirect=replace(move.redirect, repository_id=124))),
            replace(first, association=replace(first.association, repository="other/vendor")),
            replace(first, repository_move=replace(move, canonical_repository="other/vendor")),
            replace(first, repository_move=replace(move, verified=False)),
            replace(first, tags=(replace(first.tags[0], tag_ref="refs/tags/9.0"),)),
            replace(first, revision="e" * 40), replace(first, sha256="0" * 64),
        ):
            with self.subTest(changed=changed), self.assertRaises(ValueError):
                encode_sources(replace(source, acquisition=replace(source.acquisition,
                    module_requests=(changed, second))), version=2)

    def test_full_observations_and_historical_gaps_remain_distinct(self):
        for full in (False, True):
            source = controlled_sources(full=full)
            restored = decode_sources(encode_sources(source))
            self.assertEqual(restored.catalog.identity, source.catalog.identity)
            self.assertEqual(restored.acquisition, source.acquisition)
        source = controlled_sources()
        with self.assertRaisesRegex(ValueError, "full source association"):
            encode_sources(replace(source, acquisition=replace(source.acquisition, origin="native_observation")))

    def test_source_text_receipt_transition_and_association_substitutions_refuse(self):
        source = controlled_sources(full=True)
        receipts = source.acquisition.module_requests
        changes = (replace(receipts[0], sha256="0" * 64),
                   replace(receipts[0], revision="e" * 40),
                   replace(receipts[0], request=replace(receipts[0].request, version="99")),
                   replace(receipts[0], association=replace(receipts[0].association, repository="other/project")))
        for changed in changes:
            with self.subTest(changed=changed.request.version), self.assertRaises(ValueError):
                encode_sources(replace(source, acquisition=replace(source.acquisition, module_requests=(changed, *receipts[1:]))))

    def test_physical_request_costs_and_timeout_recovery_links_remain_exact(self):
        source = controlled_sources()
        limits = se.SourceAcquisitionLimits(50, 100, 8 * 1024 * 1024, 32 * 1024 * 1024,
            MeasuredDuration.from_seconds(180.0, "acquisition_limit"), 24, 16, 2)
        events = (se.SourceRequestEvent("source", "pypi.org", "/pypi/vendor/1/json", 0, 1, 0, None, "failed", "transport_error"),
                  se.SourceRequestEvent("source", "pypi.org", "/pypi/vendor/1/json", 0, 2, 10, 200, "received", None))
        transport = se.SourceTransportReceipt(limits, "anonymous", 0, 2, 10, MeasuredDuration.from_seconds(.1, "acquisition_elapsed"),
            "cooperative_monotonic_checks_and_bounded_socket_timeouts", (), events, "pypi-get-timeout-once/1",
            (se.SourceRetryDecision(1, 2, "timeout_before_response", "dispatched"),))
        def captured(value):
            return replace(source, acquisition=replace(source.acquisition, transport=value))
        restored = decode_sources(encode_sources(captured(transport)))
        self.assertEqual(restored.acquisition.transport, transport)
        for changed in (replace(transport, provider_requests=1), replace(transport, decoded_body_bytes=0),
                        replace(transport, retry_decisions=(se.SourceRetryDecision(2, None, "timeout_before_response", "not_dispatched"),))):
            with self.assertRaises(ValueError):
                encode_sources(captured(changed))

    def test_capture_placeholders_source_progress_and_completed_comparison(self):
        source = controlled_sources()
        capture = started_capture(source)
        initial = capture.partial_snapshot()
        projection = reconstruct_caller_signature_projection(initial, expected_target=initial.target)
        self.assertIsNone(projection.sources)
        self.assertIsNone(projection.comparison)
        pending = next(r for r in initial.records if r.family == "caller_signature_comparison")
        capture.capture_caller_signature_sources(source)
        progress = capture.partial_snapshot()
        projection = reconstruct_caller_signature_projection(progress, expected_target=initial.target)
        self.assertEqual(projection.sources.catalog.identity, source.catalog.identity)
        self.assertIsNone(projection.comparison)
        current = next(r for r in progress.records if r.family == "caller_signature_comparison")
        self.assertNotEqual(pending.record_id, current.record_id)
        run = run_source_analysis(source.analysis_input())
        self.assertEqual(run.state, "completed")
        capture.capture_caller_signature_comparison(run)
        capture.complete()
        boundary = capture.snapshot()
        restored = reconstruct_caller_signature_projection(boundary, expected_target=initial.target)
        self.assertEqual(restored.comparison, run)
        for record in boundary.records:
            if record.family.startswith("caller_signature_"):
                self.assertEqual(record.producer_version, "1")
                self.assertNotIn("producer_version_unavailable", record.retention_gaps)
            elif record.outcome == "recorded":
                self.assertIsNone(record.producer_version)
                self.assertIn("producer_version_unavailable", record.retention_gaps)

    def test_failed_analysis_is_recorded_with_retained_sources(self):
        source = controlled_sources(limits=AnalysisLimits(max_nodes=1))
        capture = started_capture(source)
        capture.capture_caller_signature_sources(source)
        run = run_source_analysis(source.analysis_input())
        self.assertEqual(run.reason, "analysis_limit")
        capture.capture_caller_signature_comparison(run)
        boundary = capture.partial_snapshot()
        restored = reconstruct_caller_signature_projection(boundary, expected_target=boundary.target)
        self.assertEqual(restored.comparison.state, "failed")
        self.assertIsNone(restored.comparison.result)
        self.assertEqual(restored.sources.catalog.files, source.catalog.files)
        self.assertEqual(next(r for r in boundary.records if r.family == "caller_signature_comparison").outcome, "recorded")

    def test_protocol_family_preserves_witness_and_refuses_protocol_residue(self):
        def implementation(signature):
            return (f"class Handler:\n def __call__({signature}):\n  pass\n"
                    "class Proxy:\n def __getattr__(self, name):\n  return Handler()\nINSTANCE = Proxy()\n")
        source = controlled_sources(source_texts=("from vendor import INSTANCE\nINSTANCE.label(option=1)\n",
                                    implementation("self, **options"), implementation("self, value")))
        capture = started_capture(source)
        capture.capture_caller_signature_sources(source)
        run = run_source_analysis(source.analysis_input())
        self.assertEqual(run.state, "completed")
        capture.capture_caller_signature_comparison(run)
        boundary = capture.partial_snapshot()
        self.assertEqual(reconstruct_caller_signature_projection(boundary, expected_target=boundary.target).comparison, run)
        record = next(r for r in boundary.records if r.family == "caller_signature_comparison")
        packet = parse_json(record.payload)
        candidate = packet["result"]["candidates"][0]
        candidate["steps"] = [s for s in candidate["steps"] if s["operation"] not in {"allocation", "factory_return"}]
        corrupted = json_bytes(packet)
        with self.assertRaisesRegex(NativeReconstructionError, "factory"):
            reconstruct_caller_signature_projection(altered(boundary, record.family, payload=corrupted, payload_digest=sha256(corrupted).hexdigest()), expected_target=boundary.target)

    def test_failed_acquisition_without_text_is_distinct_from_unperformed(self):
        source = controlled_sources()
        receipt = replace(source.acquisition, state="failed", target=None, module_requests=(), source_work=None,
                          problems=(se.SourceProblem("target", "source_unavailable", "Controlled target read failed"),))
        capture = started_capture(source)
        capture.capture_caller_signature_sources(replace(source, catalog=None, modules=(), acquisition=receipt))
        boundary = capture.partial_snapshot()
        projection = reconstruct_caller_signature_projection(boundary, expected_target=boundary.target)
        self.assertEqual(projection.sources.acquisition.state, "failed")
        self.assertIsNone(projection.sources.catalog)
        self.assertIsNone(projection.comparison)

    def test_failed_file_read_keeps_prior_association_metadata_and_tag_progress(self):
        source = controlled_sources(full=True)
        first = source.acquisition.module_requests[0]
        failed = replace(first, state="unavailable", problem=se.SourceProblem("file", "acquisition_failed", "Controlled file read failed"),
                         sha256=None, utf8_bytes=None)
        partial = replace(source, catalog=None, modules=(), acquisition=replace(source.acquisition, state="partial", module_requests=(failed,)))
        restored = decode_sources(encode_sources(partial))
        self.assertEqual(restored.acquisition.module_requests[0], failed)
        self.assertIsNone(restored.analysis_input())
        # Those retained premises cannot authorize the original file as analyzed.
        with self.assertRaisesRegex(ValueError, "acquisition receipt"):
            encode_sources(replace(source, acquisition=replace(source.acquisition, module_requests=(failed, *source.acquisition.module_requests[1:]))))

    def test_unknown_versions_methods_missing_families_and_wrong_basis_refuse(self):
        source = controlled_sources()
        capture = started_capture(source)
        capture.capture_caller_signature_sources(source)
        boundary = capture.partial_snapshot()
        for family in ("caller_signature_sources", "caller_signature_comparison"):
            for changes in ({"codec_version": 9}, {"producer_version": "9"}, {"producer_method": "other.method"}):
                with self.subTest(family=family, changes=changes), self.assertRaises(NativeReconstructionError):
                    reconstruct_caller_signature_projection(altered(boundary, family, **changes), expected_target=boundary.target)
        # A real older family absence remains inspectable for existing projections.
        old = CapturedNativeBoundary(boundary.target, tuple(r for r in boundary.records if not r.family.startswith("caller_signature_")))
        self.assertIsNotNone(reconstruct_ci_projection(old, expected_target=old.target))
        with self.assertRaisesRegex(NativeReconstructionError, "missing_native_material"):
            reconstruct_caller_signature_projection(old, expected_target=old.target)
        comparison = next(r for r in boundary.records if r.family == "caller_signature_comparison")
        with self.assertRaisesRegex(NativeReconstructionError, "missing_native_material"):
            reconstruct_caller_signature_projection(altered(boundary, comparison.family, input_record_ids=comparison.input_record_ids[::-1]), expected_target=boundary.target)

    def test_published_source_and_failed_run_survive_fresh_process_without_producers(self):
        source = controlled_sources(limits=AnalysisLimits(max_nodes=1))
        capture = started_capture(source)
        with tempfile.TemporaryDirectory() as tmp:
            store = CheckpointStore.create(Path(tmp) / "store", schema_version=2)
            host = InvestigationWorkspaceHost(store=store, lineage_id="control")
            host.initialize(capture.partial_snapshot())
            capture.capture_caller_signature_sources(source)
            host.publish_native_progress(capture.partial_snapshot())
            source_revision = host.current.revision_id
            capture.capture_caller_signature_comparison(run_source_analysis(source.analysis_input()))
            host.publish_native_progress(capture.partial_snapshot())
            failed_revision = host.current.revision_id
            program = '''import json,sys
from pathlib import Path
from unittest.mock import patch
from contextlib import ExitStack
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_projection import reconstruct_caller_signature_projection
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
with ExitStack() as stack:
 for hook in ("ast.parse","socket.socket.connect","requests.sessions.Session.request","upgradepilot.caller_signature.worker.run_source_analysis","upgradepilot.caller_signature.worker.produce_source_analysis","upgradepilot.caller_signature.correspondence.discover_source_candidates","upgradepilot.caller_signature.analysis.compare_arguments"):
  stack.enter_context(patch(hook,side_effect=AssertionError("Forbidden recovery producer: "+hook)))
 store=CheckpointStore.open(Path(sys.argv[1]),read_only=True)
 target=ExactInvestigationTarget("owner/target",7,"b"*40,"a"*40,"vendor","1.0","2.0")
 rows=[]
 for rev in sys.argv[2:]:
  selected=store.read_revision("control",rev,expected_target=target)
  restored=reconstruct_caller_signature_projection(selected.revision.boundary,expected_target=target)
  rows.append(dict(files=len(restored.sources.catalog.files),state=restored.comparison.state if restored.comparison else None,reason=restored.comparison.reason if restored.comparison else None))
 print(json.dumps(rows))
'''
            child = subprocess.run([sys.executable, "-c", program, str(store.directory), source_revision, failed_revision],
                env=dict(os.environ), capture_output=True, text=True, timeout=20)
            self.assertEqual(child.returncode, 0, child.stderr)
            self.assertEqual(json.loads(child.stdout), [{"files": 3, "state": None, "reason": None}, {"files": 3, "state": "failed", "reason": "analysis_limit"}])
