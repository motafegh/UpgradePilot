"""Product source/native consumer contracts; synthetic inputs, actual product owners.

Real retained-input qualification is separate developer evidence, never a network unit test.
These controls discriminate reference scope, delivery versus acquisition, missing facts,
resource admission, accounting and guarded cold reconstruction.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from dataclasses import FrozenInstanceError, asdict, replace
from pathlib import Path
from unittest.mock import patch

from test_investigation import _Harness

from upgradepilot.github.api import GitHubAcquisitionError
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.consumer_access import WorkspaceEvidenceAccess
from upgradepilot.workspace.lifecycle_host import (
    InvestigationWorkspaceHost,
    WorkspaceHostError,
)
from upgradepilot.workspace.lifecycle_records import (
    CapabilityObservation,
    DiscoveryObjective,
    ExecutionAttempt,
    ViewDelivery,
    decode_lifecycle_value,
)
from upgradepilot.workspace.native_projection import reconstruct_ci_projection
from upgradepilot.workspace.native_representation import NativeReconstructionError
from upgradepilot.workspace.preparation import prepare_dependency_ci_workspace
from upgradepilot.workspace.source_access import (
    RetainedSourceCatalog,
    RetainedSourceFile,
    RetainedSourceScope,
    encode_source_catalog,
    read_source_catalog,
    read_source_delivery,
)


def prepared(host=None):
    harness = _Harness()
    result = prepare_dependency_ci_workspace(
        harness.identity.repository,
        harness.identity.number,
        expected_base=harness.identity.base_sha,
        expected_head=harness.identity.head_sha,
        pull_client=harness.pull_client,
        repository_client=harness.repository_client,
        actions_client=harness.actions_client,
        host=host,
    )
    return harness, result


def catalog(target=None, text="pytest\nsecond line\n", extra=()):
    return RetainedSourceCatalog(
        (
            RetainedSourceScope(
                "target",
                "example/project",
                "b" * 40,
                "repository_text",
                "Controlled exact retained text.",
                "Only retained files; runtime unknown.",
            ),
        ),
        (
            RetainedSourceFile("target", "doc/changelog.rst", text),
            RetainedSourceFile("target", "empty.txt", ""),
        )
        + extra,
        target=target,
    )


def access_setup(host=None, budget=256 * 1024):
    harness, result = prepared(host)
    source = catalog(result.host.current.boundary.target)
    access = WorkspaceEvidenceAccess(result.host, source, max_native_bytes=budget)
    result.host.configure(authority=None, capabilities=(), methods=(access.method,))
    basis = next(
        r.record_id
        for r in result.host.current.boundary.records
        if r.family == "investigation_inputs"
    )
    purpose = result.host.add_purpose(
        DiscoveryObjective(
            "Inspect update evidence.",
            access.scope,
            "Bounded discovery.",
            "Only this capture.",
        ),
        native_record_ids=(basis,),
    )
    return harness, result.host, source, access, purpose


class SourceCatalogTests(unittest.TestCase):
    def test_exact_read_empty_zero_missing_and_reference_resolution_are_distinct(self):
        source = catalog()
        read = source.query(
            "read",
            {"source_id": "target", "path": "doc/changelog.rst", "line_count": 1},
        )
        payload = read_source_delivery(read.content)["payload"]
        self.assertEqual(payload["lines"], ["pytest"])
        resolved = source.query("resolve", {"reference": payload["reference"]})
        self.assertEqual(read_source_delivery(resolved.content)["payload"], payload)
        self.assertEqual(
            source.query("read", {"source_id": "target", "path": "empty.txt"}).outcome,
            "empty",
        )
        self.assertEqual(
            source.query("search", {"query": "no match"}).outcome, "scoped_negative"
        )
        self.assertEqual(
            source.query(
                "read", {"source_id": "target", "path": "missing.txt"}
            ).outcome,
            "problem",
        )
        self.assertEqual(
            source.query("search", {"source_id": "unknown", "query": "pytest"}).outcome,
            "problem",
        )

    def test_literal_search_paging_preview_and_work_are_truthful(self):
        source = catalog(text=("PYTEST " + "x" * 600 + "\n") * 25)
        first = read_source_delivery(
            source.query("search", {"query": "pytest", "prefix": "doc/"}).content
        )
        self.assertEqual(len(first["payload"]["items"]), 20)
        self.assertEqual(first["payload"]["total_matches"], 25)
        self.assertEqual(first["payload"]["next_offset"], 20)
        self.assertEqual(first["work"]["examined_lines"], 25)
        item = first["payload"]["items"][0]
        self.assertGreater(item["preview_omitted_characters"], 0)
        exact = read_source_delivery(
            source.query("resolve", {"reference": item["reference"]}).content
        )
        self.assertGreater(len(exact["payload"]["lines"][0]), 500)
        page = source.query("search", {"query": "pytest", "offset": 20})
        self.assertEqual(len(read_source_delivery(page.content)["payload"]["items"]), 5)
        self.assertEqual(
            source.query("search", {"query": "pytest", "offset": 100}).outcome, "empty"
        )
        self.assertEqual(
            source.query("search", {"query": "pytest|second"}).outcome,
            "scoped_negative",
        )

    def test_inventory_paging_and_frozen_mutation_refusal(self):
        source = catalog(
            extra=tuple(
                RetainedSourceFile("target", f"f{i}.txt", "") for i in range(30)
            )
        )
        first = read_source_delivery(
            source.query("list_paths", {"source_id": "target"}).content
        )["payload"]
        self.assertEqual(len(first["items"]), 20)
        self.assertEqual(first["next_offset"], 20)
        with self.assertRaises(FrozenInstanceError):
            source.identity = "changed"
        with self.assertRaises(FrozenInstanceError):
            source.files[0].content = "changed"

    def test_reference_cannot_rebind_changed_content_or_source_origin(self):
        reference = read_source_delivery(
            catalog()
            .query("read", {"source_id": "target", "path": "doc/changelog.rst"})
            .content
        )["payload"]["reference"]
        self.assertEqual(
            catalog(text="different\n")
            .query("resolve", {"reference": reference})
            .outcome,
            "problem",
        )
        source = catalog()
        changed = RetainedSourceCatalog(
            (replace(source.scopes[0], capture_basis="Different capture."),),
            source.files,
        )
        self.assertEqual(
            changed.query("resolve", {"reference": reference}).outcome, "problem"
        )

    def test_invalid_shapes_paths_and_line_ranges_are_problems(self):
        for operation, args in [
            ("read", {"source_id": "target", "path": "../secret"}),
            ("read", {"source_id": "target", "path": "empty.txt", "start_line": True}),
            ("read", {"source_id": "target", "path": "empty.txt", "line_count": 101}),
            (
                "read",
                {"source_id": "target", "path": "doc/changelog.rst", "line_count": 0},
            ),
            ("search", {"query": "", "extra": "execute"}),
            ("search", {"query": "pytest", "offset": False}),
            ("list_paths", {"source_id": "target", "prefix": "/etc"}),
            ("resolve", {"reference": "source:__import__:L1:1"}),
        ]:
            with self.subTest(operation=operation, args=args):
                self.assertEqual(catalog().query(operation, args).outcome, "problem")

    def test_size_limits_refuse_before_content_is_silently_truncated(self):
        with (
            patch("upgradepilot.workspace.source_access.MAX_SOURCE_FILE_BYTES", 8),
            self.assertRaises(ValueError),
        ):
            RetainedSourceFile("target", "large.txt", "x" * 9)
        with (
            patch("upgradepilot.workspace.source_access.MAX_SOURCE_CATALOG_BYTES", 2),
            self.assertRaises(ValueError),
        ):
            catalog()
        source = catalog(text="x" * (256 * 1024) + "\n")
        result = source.query(
            "read", {"source_id": "target", "path": "doc/changelog.rst"}
        )
        self.assertEqual(result.outcome, "problem")
        self.assertEqual(
            read_source_delivery(result.content)["payload"]["reason"],
            "source_view_capacity",
        )

    def test_retained_delivery_reader_rejects_extra_authority_and_bad_work_counts(self):
        body = json.loads(catalog().query("list_sources", {}).content)
        for replacement in [
            dict(body, trusted_truth=True),
            dict(body, work={"examined_files": False, "examined_lines": 0}),
            dict(body, outcome="established_applicable"),
        ]:
            with self.assertRaises(ValueError):
                read_source_delivery(json.dumps(replacement).encode())

    def test_profile_round_trip_wrong_target_integrity_and_version_refuse(self):
        _, result = prepared()
        target = result.host.current.boundary.target
        source = catalog(target)
        encoded = encode_source_catalog(source)
        restored = read_source_catalog(encoded, expected_target=target)
        self.assertEqual(source.identity, restored.identity)
        for key, value in [
            ("catalog_id", "0" * 64),
            ("format", "retained-source-catalog/2"),
        ]:
            body = json.loads(encoded)
            body[key] = value
            with self.assertRaises(ValueError):
                read_source_catalog(json.dumps(body).encode(), expected_target=target)
        with self.assertRaises(ValueError):
            read_source_catalog(
                encoded, expected_target=replace(target, head_sha="c" * 40)
            )
        with self.assertRaises(NativeReconstructionError):
            read_source_catalog(
                encoded.replace(b'"format":', b'"format": "duplicate", "format":', 1),
                expected_target=target,
            )

    def test_catalog_rejects_duplicate_undeclared_or_non_normal_paths(self):
        source = catalog()
        for files in [
            (source.files[0], source.files[0]),
            (RetainedSourceFile("other", "file.txt", ""),),
        ]:
            with self.assertRaises(ValueError):
                RetainedSourceCatalog(source.scopes, files)
        for path in ["/etc/passwd", "a/../b", "a//b", "a\\b"]:
            with self.assertRaises(ValueError):
                RetainedSourceFile("target", path, "")


class PreparationAndConsumerTests(unittest.TestCase):
    def test_shared_native_preparation_runs_without_model_or_upstream_and_keeps_unperformed_material(
        self,
    ):
        harness, result = prepared()
        self.assertEqual(result.inputs.dependency.normalized_package, "demo")
        harness.pull_client.get_changed_files.assert_called_once()
        harness.actions_client.get_exact_head_workflow_runs.assert_called_once()
        harness.package_client.get_release.assert_not_called()
        harness.support_drop_evaluator.assert_not_called()
        projection = reconstruct_ci_projection(
            result.host.current.boundary,
            expected_target=result.host.current.boundary.target,
        )
        self.assertEqual(projection.ci_coverage_result.state, "no_successful_ci")
        self.assertTrue(
            all(
                r.outcome == "not_evaluated"
                for r in result.host.current.boundary.records
                if r.family.startswith("upstream")
            )
        )

    def test_preparation_refuses_drift_and_does_not_turn_provider_failure_into_empty_ci(
        self,
    ):
        h = _Harness()
        with self.assertRaises(ValueError):
            prepare_dependency_ci_workspace(
                h.identity.repository,
                h.identity.number,
                expected_base="c" * 40,
                expected_head=h.identity.head_sha,
                pull_client=h.pull_client,
            )
        h.pull_client.get_changed_files.assert_not_called()
        h = _Harness()
        h.actions_client.get_exact_head_workflow_runs.side_effect = (
            GitHubAcquisitionError("unavailable", reason="request_timeout")
        )
        host = InvestigationWorkspaceHost()
        with self.assertRaises(GitHubAcquisitionError):
            prepare_dependency_ci_workspace(
                h.identity.repository,
                h.identity.number,
                expected_base=h.identity.base_sha,
                expected_head=h.identity.head_sha,
                pull_client=h.pull_client,
                repository_client=h.repository_client,
                actions_client=h.actions_client,
                host=host,
            )
        self.assertEqual(
            next(
                r for r in host.current.boundary.records if r.family == "ci_coverage"
            ).outcome,
            "not_evaluated",
        )

    def test_actual_source_native_delivery_retains_payload_without_acquisition_or_use_claim(
        self,
    ):
        _, host, source, access, purpose = access_setup()
        source_id = access.source_view(
            purpose, "read", {"source_id": "target", "path": "doc/changelog.rst"}
        )
        native_id = access.native_view(purpose, ("investigation_inputs", "ci_coverage"))
        delivery = host.lifecycle_value(source_id)
        self.assertIsInstance(delivery, ViewDelivery)
        self.assertEqual(
            read_source_delivery(delivery.retained_content.encode())["payload"][
                "lines"
            ],
            ["pytest", "second line"],
        )
        self.assertEqual(
            json.loads(host.lifecycle_value(native_id).retained_content)[
                "native_records"
            ][1]["family"],
            "ci_coverage",
        )
        values = [
            host.lifecycle_value(r.record_id)
            for r in host.current.lifecycle_history.records
        ]
        self.assertFalse(
            any(
                isinstance(v, (CapabilityObservation, ExecutionAttempt)) for v in values
            )
        )
        self.assertEqual(
            access.receipts[0].delivered_bytes, len(delivery.retained_content.encode())
        )
        self.assertEqual(access.receipts[0].examined_files, 1)
        self.assertEqual(
            source.identity,
            read_source_delivery(delivery.retained_content.encode())["catalog_id"],
        )

    def test_unsupported_scope_method_and_wrong_target_refuse_without_backend_work(
        self,
    ):
        _, host, source, access, purpose = access_setup()
        host.configure(authority=None, capabilities=())
        with self.assertRaisesRegex(WorkspaceHostError, "view_method_unavailable"):
            access.source_view(purpose, "search", {"query": "pytest"})
        self.assertEqual(access.receipts[-1].examined_files, 0)
        self.assertIsNone(access.receipts[-1].delivery_id)
        with self.assertRaises(ValueError):
            WorkspaceEvidenceAccess(
                host, catalog(replace(source.target, head_sha="c" * 40))
            )

    def test_unknown_missing_scope_and_model_authority_escalation_are_charged_distinctly(
        self,
    ):
        _, host, _, access, purpose = access_setup()
        malformed = access.source_view(
            purpose, "read", {"source_id": "target", "path": "missing"}
        )
        self.assertEqual(
            read_source_delivery(
                host.lifecycle_value(malformed).retained_content.encode()
            )["outcome"],
            "problem",
        )
        with self.assertRaises(WorkspaceHostError):
            access.source_view("model-made-purpose", "search", {"query": "pytest"})
        with self.assertRaises(WorkspaceHostError):
            access.native_view(purpose, ("canonical_adequacy",))
        self.assertEqual(
            [r.outcome for r in access.receipts], ["problem", "refused", "refused"]
        )
        self.assertEqual(
            len({r.delivery_id for r in access.receipts if r.delivery_id}), 1
        )

    def test_restricted_source_menu_and_withheld_native_view_do_not_leak(self):
        _, host, source, _, purpose = access_setup()
        access = WorkspaceEvidenceAccess(
            host, source, source_ids=(), native_families=()
        )
        host.configure(authority=None, capabilities=(), methods=(access.method,))
        with self.assertRaises(WorkspaceHostError):
            access.source_view(purpose, "list_sources", {})
        with self.assertRaises(WorkspaceHostError):
            access.native_view(purpose, ("ci_coverage",))

    def test_native_budget_omits_whole_material_and_reference_page_remains_available(
        self,
    ):
        _, host, _, access, purpose = access_setup(budget=4096)
        delivery = access.native_view(
            purpose,
            (
                "investigation_inputs",
                "ci_inputs",
                "ci_coverage",
                "runtime_dependency_state",
            ),
        )
        body = json.loads(host.lifecycle_value(delivery).retained_content)
        self.assertTrue(body["omitted"])
        reference = body["omitted"][0]["record_id"]
        page = access.native_page(purpose, reference, character_count=1)
        payload = json.loads(host.lifecycle_value(page).retained_content)
        self.assertEqual(payload["record_id"], reference)
        self.assertTrue(payload["partial_payload"])
        record = next(
            r for r in host.current.boundary.records if r.record_id == reference
        )
        self.assertEqual(payload["text"], record.payload.decode()[:1])

    def test_failed_publication_counts_work_without_claiming_delivery(self):
        _, host, _, access, purpose = access_setup()
        with (
            patch.object(
                host, "deliver_view", side_effect=RuntimeError("publication failed")
            ),
            self.assertRaises(RuntimeError),
        ):
            access.source_view(purpose, "search", {"query": "pytest"})
        self.assertEqual(access.receipts[-1].outcome, "refused")
        self.assertGreater(access.receipts[-1].examined_files, 0)
        self.assertEqual(access.receipts[-1].delivered_bytes, 0)

    def test_changed_native_material_invalidates_old_purpose_without_rebinding(self):
        _, host, _, access, purpose = access_setup()
        boundary = host.current.boundary
        # An original material identity change must refuse current use even if payload is equal.
        from uuid import uuid4

        identifiers = {item.record_id: uuid4().hex for item in boundary.records}
        records = tuple(
            replace(
                item,
                record_id=identifiers[item.record_id],
                input_record_ids=tuple(
                    identifiers[ref] for ref in item.input_record_ids
                ),
            )
            for item in boundary.records
        )
        host.publish_native_progress(replace(boundary, records=records))
        with self.assertRaises(WorkspaceHostError):
            access.source_view(purpose, "list_sources", {})
        self.assertEqual(host.lifecycle_value(purpose).scope, access.scope)

    def test_delivery_material_closure_and_access_scope_cannot_be_rewritten(self):
        from upgradepilot.workspace.lifecycle_boundary import (
            CapturedLifecycleHistory,
            reconstruct_lifecycle_history,
        )

        _, host, _, access, purpose = access_setup()
        with self.assertRaises(FrozenInstanceError):
            access.source_ids = ("other",)
        identity = access.source_view(purpose, "list_sources", {})
        history = host.current.lifecycle_history
        damaged = CapturedLifecycleHistory(
            tuple(
                replace(record, native_record_ids=())
                if record.record_id == identity
                else record
                for record in history.records
            )
        )
        with self.assertRaisesRegex(NativeReconstructionError, "material basis"):
            reconstruct_lifecycle_history(damaged, bases=host._bases)

    def test_source_proposals_keep_delivered_citations_separate_from_native_truth(self):
        from upgradepilot.workspace.lifecycle_records import ContentCitation

        _, host, _, access, purpose = access_setup()
        delivery = access.source_view(
            purpose,
            "read",
            {"source_id": "target", "path": "doc/changelog.rst", "line_count": 1},
        )
        body = read_source_delivery(
            host.lifecycle_value(delivery).retained_content.encode()
        )
        reference = body["payload"]["reference"]
        proposal, citation = access.propose_source(
            purpose, delivery, "candidate", "Attributed interpretation.", reference
        )
        self.assertEqual(host.lifecycle_value(proposal).cited_native_ids, ())
        self.assertIsInstance(host.lifecycle_value(citation), ContentCitation)
        self.assertEqual(host.lifecycle_value(citation).reference, reference)
        outcome = host.evaluate_proposal(proposal)
        self.assertEqual(host.lifecycle_value(outcome).outcome, "unsupported")
        with self.assertRaises(WorkspaceHostError):
            access.propose_source(
                purpose,
                delivery,
                "candidate",
                "Undelivered line.",
                reference.replace(":L1:1", ":L2:1"),
            )

    def test_search_preview_reference_does_not_masquerade_as_a_delivered_full_line(
        self,
    ):
        _, host, _, access, purpose = access_setup()
        delivery = access.source_view(purpose, "search", {"query": "pytest"})
        body = read_source_delivery(
            host.lifecycle_value(delivery).retained_content.encode()
        )
        reference = body["payload"]["items"][0]["reference"]
        before = len(host.current.lifecycle_history.records)
        with self.assertRaisesRegex(
            WorkspaceHostError, "source_reference_not_delivered"
        ):
            access.propose_source(
                purpose, delivery, "candidate", "Unexamined full line.", reference
            )
        self.assertEqual(len(host.current.lifecycle_history.records), before)

    def test_new_delivery_codec_unknown_version_and_causal_parent_are_refused(self):
        _, host, _, access, purpose = access_setup()
        identity = access.source_view(purpose, "list_sources", {})
        record = next(
            r for r in host.current.lifecycle_history.records if r.record_id == identity
        )
        with self.assertRaisesRegex(
            NativeReconstructionError, "unsupported_lifecycle_codec"
        ):
            decode_lifecycle_value(record.kind, 2, record.payload)
        with self.assertRaises(WorkspaceHostError):
            host.deliver_view(
                purpose,
                purpose,
                representation="fake",
                content="{}",
                method=access.method,
            )

    def test_cold_store_inspection_retains_delivered_source_and_native_material_without_catalog_or_execution(
        self,
    ):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp) / "store"
            store = CheckpointStore.create(directory, schema_version=2)
            _, host, _, access, purpose = access_setup(
                InvestigationWorkspaceHost(store=store)
            )
            delivery = access.source_view(
                purpose, "read", {"source_id": "target", "path": "doc/changelog.rst"}
            )
            body = read_source_delivery(
                host.lifecycle_value(delivery).retained_content.encode()
            )
            proposal, _ = access.propose_source(
                purpose,
                delivery,
                "candidate",
                "Attributed passage.",
                body["payload"]["reference"],
            )
            host.evaluate_proposal(proposal)
            access.native_view(purpose, ("ci_coverage",))
            spec = {
                "lineage": host.lineage_id,
                "revision": host.current.revision_id,
                "target": asdict(host.current.boundary.target),
            }
            selection = Path(tmp) / "selection.json"
            selection.write_text(json.dumps(spec))
            script = r"""
import json,sys,socket
from pathlib import Path
from unittest.mock import patch
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
from upgradepilot.workspace.lifecycle_boundary import reconstruct_lifecycle_history
from upgradepilot.workspace.lifecycle_records import ViewDelivery,ContentCitation,EvaluationOutcome
from upgradepilot.workspace.source_access import read_source_delivery
from upgradepilot.workspace.native_projection import reconstruct_ci_projection
from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost
blocked=['upgradepilot.investigation_inputs.acquire_dependency_inputs','upgradepilot.investigation_inputs.prepare_ci_evidence','upgradepilot.github.pull_request.GitHubPullRequestClient.get_pull_request','upgradepilot.upstream.support_drop.evaluate_support_drop_runtime','upgradepilot.maintainer_action.synthesize_maintainer_action','socket.socket.connect','upgradepilot.workspace.source_access.RetainedSourceCatalog.query','upgradepilot.ci.dependency_exercise.evaluate_dependency_ci_coverage','upgradepilot.ci.dependency_state.evaluate_runtime_dependency_state']
handles=[patch(name,side_effect=AssertionError('forbidden reentry')) for name in blocked]
for handle in handles:
 value=handle.start()
 try:value()
 except AssertionError:pass
 else:raise AssertionError('inactive guard')
spec=json.loads(Path(sys.argv[2]).read_text()); target=ExactInvestigationTarget(**spec['target'])
store=CheckpointStore.open(Path(sys.argv[1]),read_only=True)
stored=store.read_revision(spec['lineage'],spec['revision'],expected_target=target)
bases={}; current=stored.revision
while True:
 bases[current.revision_id]=current.boundary
 if current.predecessor_id is None:break
 current=store.read_revision(spec['lineage'],current.predecessor_id,expected_target=target).revision
values=reconstruct_lifecycle_history(stored.revision.lifecycle_history,bases=bases)
deliveries=[item.value for item in values if isinstance(item.value,ViewDelivery)]
source=next(v for v in deliveries if v.representation=='retained-source-view/1')
projection=reconstruct_ci_projection(stored.revision.boundary, expected_target=target)
host=InvestigationWorkspaceHost(lineage_id=spec['lineage']);host.restore(stored,bases=bases)
print(json.dumps({'lines':read_source_delivery(source.retained_content.encode())['payload']['lines'],'state':projection.ci_coverage_result.state,'deliveries':len(deliveries),'citations':sum(isinstance(v.value,ContentCitation) for v in values),'evaluations':[v.value.outcome for v in values if isinstance(v.value,EvaluationOutcome)],'guards':len(handles)}))
"""
            child = subprocess.run(
                [sys.executable, "-c", script, str(directory), str(selection)],
                cwd=tmp,
                check=False,
                env=dict(
                    os.environ,
                    PYTHONPATH=os.pathsep.join(
                        str(Path(item).resolve())
                        for item in os.environ.get("PYTHONPATH", "").split(os.pathsep)
                        if item
                    ),
                ),
                capture_output=True,
                text=True,
                timeout=30,
            )
            self.assertEqual(child.returncode, 0, child.stderr)
            value = json.loads(child.stdout)
            self.assertEqual(
                value,
                {
                    "lines": ["pytest", "second line"],
                    "state": "no_successful_ci",
                    "deliveries": 2,
                    "citations": 1,
                    "evaluations": ["unsupported"],
                    "guards": 9,
                },
            )
