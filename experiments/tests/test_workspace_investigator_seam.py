"""Independent lifecycle oracles plus transport/backend equivalence, experiment only."""

import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from experiments.workspace_investigator_seam import (
    AcquisitionRequest,
    Binding,
    CheckpointUnavailable,
    InvestigatorPort,
    RevisionRef,
    TraceRecord,
    WorkspaceHost,
    decode_request,
    encode_request,
    json_bytes,
    payload,
)
from experiments.workspace_seam_checkpoints import MemoryCheckpoints, SQLiteCheckpoints
from experiments.workspace_seam_native import build_native_fixture


class InvestigatorSeamTests(unittest.TestCase):
    def setUp(self):
        self.fixture = build_native_fixture()
        self.port = MemoryCheckpoints()
        self.host = self.make_host(self.port)

    def make_host(self, port):
        host = WorkspaceHost(port, self.fixture.policy)
        host.seed(
            self.fixture.initial,
            {"candidate": "support:candidate", "need": "support:need"},
        )
        self.assertEqual(host.continue_current().status, "current_bindings_validated")
        return host

    def competing_host(self):
        port = self.port
        if isinstance(port, SQLiteCheckpoints):
            port = SQLiteCheckpoints(port.store.root)
            self.addCleanup(port.close)
        return WorkspaceHost(port, self.fixture.policy)

    def request(self, host=None, name="read"):
        host = host or self.host
        view = host.read(("support:need", "support:candidate"))
        request = self.fixture.request(view, name)
        self.assertEqual(host.request(request).status, "admitted")
        self.assertEqual(host.start(request.request_id).status, "published")
        return request

    def observation(self, host=None, name="read"):
        host = host or self.host
        request = self.request(host, name)
        self.assertEqual(
            host.observe(request.request_id, self.fixture.result()).status,
            "observation_admitted",
        )
        return request

    def test_native_need_attempt_observation_evaluation_are_distinct(self):
        self.observation()
        self.fixture.evaluate(self.host)
        kinds = {record.kind for record in self.host.revision.records.values()}
        self.assertTrue(
            {"request", "admission", "attempt", "observation", "domain_evaluation"}
            <= kinds
        )
        evaluations = [
            payload(record)
            for record in self.host.revision.records.values()
            if record.kind == "domain_evaluation"
        ]
        self.assertEqual(evaluations[-1]["status"], "established_applicable")
        self.assertEqual(
            evaluations[-1]["adequacy"], "unsupported_no_admitted_evaluator"
        )
        before = json.loads(self.host.revision.records["support:before"].payload)
        self.assertEqual(
            before["fields"]["applicability"]["fields"]["state"], "unresolved"
        )

    def test_delayed_result_survives_unrelated_revision(self):
        request = self.request()
        original = request.revision
        self.host.retain_evidence(
            TraceRecord("unrelated", "fixture", "annotation", "other", b'"unrelated"'),
            role="context",
            candidate="other-candidate",
        )
        self.assertGreater(self.host.ref.number, original.number)
        outcome = self.host.observe(request.request_id, self.fixture.result())
        self.assertEqual(outcome.status, "observation_admitted")
        completion = payload(self.host.revision.records[outcome.records[-1]])
        self.assertEqual(completion["original_revision"]["number"], original.number)
        self.assertGreater(
            completion["admitted_after_revalidation_at"]["number"], original.number
        )
        self.assertEqual(len(self.host.evaluation_inputs()), 1)

    def test_material_update_rejects_delayed_result_and_retains_old_basis(self):
        request = self.request()
        self.host.rebind(
            "candidate",
            TraceRecord(
                "candidate:refined",
                "native.fixture",
                "native",
                self.host.ref.target,
                b'"refined premise"',
            ),
        )
        self.assertEqual(
            self.host.observe(request.request_id, self.fixture.result()).status,
            "material_basis_changed",
        )
        self.assertNotIn("target:source", self.host.revision.records)
        self.assertEqual(self.host._request(request.request_id).basis, request.basis)
        self.assertTrue(
            any(
                record.kind == "problem" and "rejected_result" in payload(record)
                for record in self.host.revision.records.values()
            )
        )

    def test_current_target_change_rejects_old_result_without_rebinding_history(self):
        request = self.request()
        old_target = self.host.ref.target
        self.host.policy = replace(
            self.host.policy, target=old_target.replace("a" * 40, "d" * 40)
        )
        self.assertEqual(
            self.host.observe(request.request_id, self.fixture.result()).status,
            "target_changed",
        )
        self.assertEqual(self.host.ref.target, old_target)
        self.assertEqual(self.host.continue_current().status, "target_changed")

    def test_method_capability_and_authority_withdrawal(self):
        for changes, expected in (
            ({"method": "native-support-v2"}, "method_changed"),
            ({"capabilities": frozenset()}, "capability_unavailable"),
            ({"authorized": False}, "current_authority_unavailable"),
        ):
            with self.subTest(expected=expected):
                host = self.make_host(MemoryCheckpoints())
                request = self.request(host)
                host.policy = replace(host.policy, **changes)
                self.assertEqual(
                    host.observe(request.request_id, self.fixture.result()).status,
                    expected,
                )
                self.assertNotIn("target:source", host.revision.records)

    def test_request_needs_exact_native_basis_scope_and_discriminator(self):
        view = self.host.read(("support:need",))
        request = self.fixture.request(view)
        for name, changes, expected in (
            (
                "basis",
                {"basis": (Binding("candidate", "support:candidate"),)},
                "material_basis_changed",
            ),
            ("scope", {"scope": "other/path"}, "request_meaning_or_scope_rejected"),
            (
                "meaning",
                {"discriminator": "some-interesting-topic"},
                "request_meaning_or_scope_rejected",
            ),
            (
                "future",
                {"revision": replace(view.revision, number=10000)},
                "unknown_revision",
            ),
            (
                "lineage",
                {"revision": replace(view.revision, lineage="another-workspace")},
                "unknown_revision",
            ),
        ):
            outcome = self.host.request(
                replace(request, request_id=f"investigator:{name}", **changes)
            )
            self.assertEqual(outcome.status, expected)
            self.assertNotIn(f"attempt:investigator:{name}", self.host.revision.records)

    def test_delivery_examination_citation_evaluation_and_adequacy_not_collapsed(self):
        self.observation()
        omitted = self.host.read(("support:need",))
        self.assertIn("target:source", omitted.omitted_but_addressable)
        self.assertEqual(
            payload(self.host.revision.records[omitted.view_id])["examined_or_used"],
            "unknown",
        )
        bad = self.host.propose(
            "proposal:bad",
            omitted.revision,
            omitted.basis,
            omitted.view_id,
            ("target:source",),
            "claimed support",
        )
        self.assertEqual(bad.status, "citation_not_delivered_in_view")
        delivered = self.host.read(("target:source",))
        good = self.host.propose(
            "proposal:good",
            delivered.revision,
            delivered.basis,
            delivered.view_id,
            ("target:source",),
            "consumer interpretation",
        )
        self.assertEqual(good.status, "proposal_retained_evaluation_unsupported")
        evaluation = payload(self.host.revision.records[good.records[-1]])
        self.assertIsNone(evaluation["assessment"])
        self.assertEqual(delivered.adequacy, "unsupported_no_admitted_evaluator")

    def test_counterevidence_omitted_from_view_is_selected_and_invalidates_basis(self):
        self.observation()
        self.fixture.evaluate(self.host)
        evaluation = next(
            record
            for record in self.host.revision.records.values()
            if record.kind == "domain_evaluation"
        )
        old_native = self.host.revision.records["native:assessment"]
        self.assertEqual(
            self.host.evaluation_basis_status(evaluation.record_id),
            "unchanged_declared_basis",
        )
        counter = TraceRecord(
            "counter:gap",
            "offline.fixture",
            "counterevidence",
            self.host.ref.target,
            None,
            gap="owner_relevant_counterobservation_unavailable",
        )
        self.host.retain_evidence(
            counter, role="counterevidence", candidate="support:candidate"
        )
        view = self.host.read(("target:source",))
        self.assertIn(counter.record_id, view.omitted_but_addressable)
        self.assertEqual(
            {item.record_id for item in self.host.evaluation_inputs()},
            {"target:source", counter.record_id},
        )
        self.assertEqual(
            self.host.evaluation_basis_status(evaluation.record_id),
            "requires_owner_revalidation",
        )
        self.fixture.evaluate(self.host)
        latest = [
            payload(record)
            for record in self.host.revision.records.values()
            if record.kind == "domain_evaluation"
        ][-1]
        self.assertEqual(latest["status"], "unsupported_owner_input_set")
        self.assertEqual(self.host.revision.records["native:assessment"], old_native)

    def test_exact_duplicate_requests_and_results_do_not_advance_or_add_support(self):
        request = self.observation()
        before = self.host.ref.number
        self.assertEqual(self.host.request(request).status, "duplicate_request")
        self.assertEqual(
            self.host.observe(request.request_id, self.fixture.result()).status,
            "duplicate_delivery",
        )
        self.assertEqual(self.host.ref.number, before)
        self.assertEqual(len(self.host.evaluation_inputs()), 1)

    def test_same_result_from_second_attempt_is_one_evidence_identity(self):
        first = self.request()
        request = self.request(name="second")
        self.assertEqual(
            self.host.observe(first.request_id, self.fixture.result()).status,
            "observation_admitted",
        )
        self.assertEqual(
            self.host.observe(request.request_id, self.fixture.result()).status,
            "duplicate_delivery",
        )
        self.assertEqual(len(self.host.evaluation_inputs()), 1)
        self.assertEqual(
            sum(
                record.kind == "observation"
                for record in self.host.revision.records.values()
            ),
            2,
        )

    def test_inconsistent_id_or_exact_scope_is_problem_not_conflict_fact(self):
        request = self.request()
        second = self.request(name="alias")
        self.host.observe(request.request_id, self.fixture.result())
        original = self.fixture.result()
        self.assertEqual(
            self.host.observe(
                request.request_id, replace(original, payload=b"changed")
            ).status,
            "identity_content_collision",
        )
        self.assertEqual(
            self.host.observe(
                second.request_id,
                replace(original, record_id="alias", payload=b"changed"),
            ).status,
            "identity_content_collision",
        )
        self.assertEqual(self.host.revision.records[original.record_id], original)
        self.assertNotIn("alias", self.host.revision.records)

    def test_identical_content_in_distinct_scopes_preserves_identity(self):
        self.observation()
        original = self.fixture.result()
        other = replace(
            original, record_id="other:source", scope=original.scope + "/other"
        )
        self.host.retain_evidence(other, role="context", candidate="other-candidate")
        self.assertEqual(
            self.host.revision.records[other.record_id].digest, original.digest
        )
        self.assertNotEqual(
            self.host.revision.records[other.record_id].scope, original.scope
        )
        self.assertEqual(len(self.host.evaluation_inputs()), 1)

    def test_wrong_result_scope_or_authority_is_rejected(self):
        for change in (
            {"scope": "wrong"},
            {"owner": "Investigator"},
            {"kind": "evaluated_truth"},
        ):
            with self.subTest(change=change):
                host = self.make_host(MemoryCheckpoints())
                request = self.request(host)
                result = replace(self.fixture.result(), **change)
                self.assertEqual(
                    host.observe(request.request_id, result).status,
                    "result_identity_or_meaning_rejected",
                )
                self.assertNotIn(result.record_id, host.revision.records)

    def test_observation_without_attempt_and_rejected_admission_cannot_execute(self):
        self.assertEqual(
            self.host.observe("investigator:unknown", self.fixture.result()).status,
            "no_admitted_attempt",
        )
        view = self.host.read(("support:need",))
        request = replace(self.fixture.request(view), capability="run_target_code")
        self.assertEqual(self.host.request(request).status, "capability_unavailable")
        self.host.policy = replace(
            self.host.policy, capabilities=frozenset({"run_target_code"})
        )
        self.assertEqual(
            self.host.start(request.request_id).status, "request_not_admitted"
        )

    def test_unknown_completion_survives_recovery_and_never_auto_retries(self):
        request = self.request()
        restored = WorkspaceHost(self.port, self.fixture.policy)
        self.assertFalse(restored.active)
        self.assertEqual(
            restored.start(request.request_id).status,
            "completion_unknown_no_auto_retry",
        )
        restored.continue_current()
        self.assertEqual(
            restored.start(request.request_id).status,
            "completion_unknown_no_auto_retry",
        )
        self.assertEqual(
            sum(
                record.kind == "attempt"
                for record in restored.revision.records.values()
            ),
            1,
        )
        self.assertIsNone(
            payload(restored.revision.records[f"attempt:{request.request_id}"])[
                "retry_permission"
            ]
        )

    def test_restore_permission_is_current_and_explicit(self):
        view = self.host.read(("support:need",))
        request = self.fixture.request(view)
        self.host.request(request)
        restored = WorkspaceHost(self.port, self.fixture.policy)
        self.assertEqual(
            restored.start(request.request_id).status, "current_authority_unavailable"
        )
        restored.policy = replace(restored.policy, authorized=False)
        self.assertEqual(restored.continue_current().status, "authority_unavailable")
        restored.policy = self.fixture.policy
        self.assertEqual(
            restored.continue_current().status, "current_bindings_validated"
        )
        self.assertEqual(restored.start(request.request_id).status, "published")

    def test_missing_basis_content_blocks_continuation_not_reading_history(self):
        gap = TraceRecord(
            "candidate:missing",
            "native.fixture",
            "native",
            self.host.ref.target,
            None,
            gap="native_content_not_retained",
        )
        self.host.rebind("candidate", gap)
        restored = WorkspaceHost(self.port, self.fixture.policy)
        self.assertEqual(restored.continue_current().status, "missing_material_content")
        view = restored.read(("support:before",))
        self.assertEqual(view.continuation, "historical_only")
        self.assertEqual(view.delivered[0].record_id, "support:before")

    def test_alias_delivery_is_not_independent_support(self):
        first = self.request()
        second = self.request(name="alias-delivery")
        self.host.observe(first.request_id, self.fixture.result())
        alias = replace(self.fixture.result(), record_id="target:alias")
        self.assertEqual(
            self.host.observe(second.request_id, alias).status, "duplicate_delivery"
        )
        self.assertEqual(len(self.host.evaluation_inputs()), 1)

    def test_duplicate_acknowledgement_cannot_bypass_current_authority(self):
        first = self.request()
        second = self.request(name="second-auth")
        self.host.observe(first.request_id, self.fixture.result())
        self.host.policy = replace(self.host.policy, authorized=False)
        self.assertEqual(
            self.host.observe(second.request_id, self.fixture.result()).status,
            "current_authority_unavailable",
        )
        self.assertNotIn(f"completion:{second.request_id}", self.host.revision.records)

    def test_capability_failure_and_unknown_completion_are_not_negative_facts(self):
        for known in (False, True):
            host = self.make_host(MemoryCheckpoints())
            request = self.request(host)
            host.attempt_problem(
                request.request_id,
                "offline_provider_unavailable",
                completion_known=known,
            )
            self.assertEqual(
                host.start(request.request_id).status,
                "already_completed" if known else "completion_unknown_no_auto_retry",
            )
            self.assertEqual(host.evaluation_inputs(), ())
            self.fixture.evaluate(host)
            latest = [
                payload(record)
                for record in host.revision.records.values()
                if record.kind == "domain_evaluation"
            ][-1]
            self.assertEqual(latest["status"], "unsupported_owner_input_set")

    def test_stale_publication_needs_refresh_and_material_revalidation(self):
        request = self.request()
        competing = self.competing_host()
        competing.continue_current()
        competing.rebind(
            "candidate",
            TraceRecord(
                "candidate:updated",
                "fixture",
                "native",
                competing.ref.target,
                b'"updated"',
            ),
        )
        self.assertEqual(
            self.host.observe(request.request_id, self.fixture.result()).status,
            "publication_conflict",
        )
        self.assertNotIn("target:source", self.host.revision.records)
        self.host.refresh()
        self.host.continue_current()
        self.assertEqual(
            self.host.observe(request.request_id, self.fixture.result()).status,
            "material_basis_changed",
        )

    def test_stale_publication_after_unrelated_change_can_revalidate_and_publish(self):
        request = self.request()
        competing = self.competing_host()
        competing.continue_current()
        competing.retain_evidence(
            TraceRecord("annotation", "fixture", "annotation", "other", b'"extra"'),
            role="context",
            candidate="other",
        )
        self.assertEqual(
            self.host.observe(request.request_id, self.fixture.result()).status,
            "publication_conflict",
        )
        self.host.refresh()
        self.host.continue_current()
        self.assertEqual(
            self.host.observe(request.request_id, self.fixture.result()).status,
            "observation_admitted",
        )

    def test_wire_envelope_cannot_supply_authority_or_weak_types(self):
        view = self.host.read(("support:need",))
        request = self.fixture.request(view)
        data = encode_request(request)
        self.assertEqual(decode_request(data), request)
        for extra in (
            "admission",
            "principal",
            "evaluated_truth",
            "permission",
            "sql_table",
        ):
            with self.subTest(extra=extra), self.assertRaises(ValueError):
                decode_request(json_bytes({**json.loads(data), extra: True}))
        for bad_number in (True, -1, "0", 0.5):
            value = json.loads(data)
            value["revision"]["number"] = bad_number
            with self.subTest(number=bad_number), self.assertRaises(ValueError):
                decode_request(json_bytes(value))
        with self.assertRaises(ValueError):
            decode_request(data[:-1] + b',"method":"forged"}')
        with self.assertRaises(ValueError):
            decode_request(b" " * 65_537)
        with self.assertRaises(ValueError):
            replace(request, request_id="workspace:admission:0")

    def test_python_wire_and_sqlite_memory_consumer_traces_match(self):
        traces = []
        for backend in ("memory", "sqlite"):
            for transport in ("python", "wire"):
                with tempfile.TemporaryDirectory() as directory:
                    port = (
                        MemoryCheckpoints()
                        if backend == "memory"
                        else SQLiteCheckpoints(Path(directory) / "store", create=True)
                    )
                    try:
                        host = self.make_host(port)
                        view = host.read(("support:need", "support:candidate"))
                        request = self.fixture.request(view)
                        if transport == "wire":
                            request = decode_request(encode_request(request))
                        self.assertEqual(host.request(request).status, "admitted")
                        host.start(request.request_id)
                        host.observe(request.request_id, self.fixture.result())
                        self.fixture.evaluate(host)
                        restored = WorkspaceHost(port, self.fixture.policy)
                        traces.append(
                            tuple(
                                (key, value)
                                for key, value in sorted(
                                    restored.revision.records.items()
                                )
                            )
                        )
                        self.assertFalse(restored.active)
                    finally:
                        if backend == "sqlite":
                            port.close()
        self.assertTrue(all(trace == traces[0] for trace in traces[1:]))

    def test_request_cannot_claim_new_basis_at_an_older_revision(self):
        old = self.host.ref
        self.host.rebind(
            "candidate",
            TraceRecord("candidate:new", "fixture", "native", old.target, b'"new"'),
        )
        request = AcquisitionRequest(
            "investigator:forged-basis",
            old,
            self.host.basis,
            "read_target_declaration",
            self.fixture.policy.scope,
            self.fixture.policy.method,
            self.fixture.need.proposition_key,
        )
        self.assertEqual(
            self.host.request(request).status, "basis_not_in_original_revision"
        )

    def test_proposal_cannot_inherit_new_method_from_an_old_view(self):
        view = self.host.read(("support:candidate",))
        self.host.policy = replace(self.host.policy, method="new-method")
        self.assertEqual(
            self.host.propose(
                "proposal:implicit-method",
                view.revision,
                view.basis,
                view.view_id,
                ("support:candidate",),
                "claim",
            ).status,
            "proposal_basis_changed",
        )

    def test_contrary_source_is_selected_without_inventing_semantic_conflict(self):
        self.observation()
        self.fixture.evaluate(self.host)
        counter = self.fixture.counter_source()
        self.host.retain_evidence(
            counter, role="counterevidence", candidate="support:candidate"
        )
        view = self.host.read(("target:source",))
        self.assertIn(counter.record_id, view.omitted_but_addressable)
        self.assertNotEqual(counter.scope, self.fixture.result().scope)
        self.fixture.evaluate(self.host)
        evaluation = [
            payload(record)
            for record in self.host.revision.records.values()
            if record.kind == "domain_evaluation"
        ][-1]
        self.assertEqual(
            evaluation["selected_inputs"], [counter.record_id, "target:source"]
        )
        self.assertEqual(evaluation["status"], "unsupported_owner_input_set")
        self.assertNotIn("conflicted", [evaluation["status"]])

    def test_counterevidence_changes_delayed_request_basis_without_head_change(self):
        request = self.request()
        target = self.host.ref.target
        counter = TraceRecord(
            "counter:missing",
            "fixture",
            "counterevidence",
            target,
            None,
            gap="counterobservation_unavailable",
        )
        self.host.retain_evidence(
            counter, role="counterevidence", candidate="support:candidate"
        )
        self.assertEqual(self.host.ref.target, target)
        self.assertEqual(
            self.host.observe(request.request_id, self.fixture.result()).status,
            "material_basis_changed",
        )

    def test_native_final_assessment_retires_old_need_without_granting_adequacy(self):
        self.observation()
        self.fixture.evaluate(self.host)
        view = self.host.read(("support:need",))
        self.assertEqual(
            self.host.request(self.fixture.request(view, "again")).status,
            "no_current_material_need",
        )
        self.assertEqual(view.adequacy, "unsupported_no_admitted_evaluator")

    def test_evaluation_method_and_capability_changes_require_owner_revalidation(self):
        self.observation()
        self.fixture.evaluate(self.host)
        evaluation = next(
            record
            for record in self.host.revision.records.values()
            if record.kind == "domain_evaluation"
        )
        for change in (
            {"method": "changed"},
            {"capabilities": frozenset({"new-critical-check"})},
        ):
            self.host.policy = replace(self.fixture.policy, **change)
            self.assertEqual(
                self.host.evaluation_basis_status(evaluation.record_id),
                "requires_owner_revalidation",
            )

    def test_proposals_require_current_authority_and_exact_method_basis(self):
        view = self.host.read(("support:candidate",))
        self.host.policy = replace(self.host.policy, authorized=False)
        self.assertEqual(
            self.host.propose(
                "proposal:denied",
                view.revision,
                view.basis,
                view.view_id,
                ("support:candidate",),
                "claim",
            ).status,
            "current_authority_unavailable",
        )
        self.host.policy = self.fixture.policy
        self.assertEqual(
            self.host.propose(
                "proposal:method",
                view.revision,
                view.basis,
                view.view_id,
                ("support:candidate",),
                "claim",
                method="withdrawn",
            ).status,
            "proposal_basis_changed",
        )

    def test_checkpoint_internal_state_is_not_investigator_evidence(self):
        internal = f"workspace:state:{self.host.ref.number}"
        self.assertEqual(
            self.host.read((internal,)).status, "unknown_or_repeated_reference"
        )
        view = self.host.read(("support:need",))
        self.assertFalse(
            any(
                key.startswith("workspace:state:")
                for key in view.omitted_but_addressable
            )
        )

    def test_view_transport_preserves_content_and_gaps_without_examined_claim(self):
        from experiments.workspace_investigator_seam import encode_projection

        gap = TraceRecord(
            "unavailable",
            "fixture",
            "counterevidence",
            self.host.ref.target,
            None,
            gap="unavailable_source",
        )
        self.host.retain_evidence(gap, role="context", candidate="other")
        view = self.host.read(("support:need", "unavailable"))
        wire = json.loads(encode_projection(view))
        self.assertEqual(
            wire["delivered"][0]["content"].encode(), view.delivered[0].payload
        )
        self.assertIsNone(wire["delivered"][1]["content"])
        self.assertEqual(wire["delivered"][1]["gap"], "unavailable_source")
        self.assertEqual(
            wire["omitted_but_addressable"], list(view.omitted_but_addressable)
        )
        self.assertEqual(
            payload(self.host.revision.records[view.view_id])["examined_or_used"],
            "unknown",
        )

    def test_withdrawn_authority_views_are_historical_only(self):
        self.host.policy = replace(self.host.policy, authorized=False)
        self.assertEqual(
            self.host.read(("support:need",)).continuation, "historical_only"
        )

    def test_consumer_cannot_execute_admit_or_publish(self):
        consumer = InvestigatorPort(self.host)
        for name in (
            "start",
            "observe",
            "continue_current",
            "rebind",
            "publish_evaluation",
            "port",
            "policy",
        ):
            self.assertFalse(hasattr(consumer, name))

    def test_uncertain_checkpoint_ack_is_portable_and_not_execution_failure(self):
        class UncertainCheckpoints(MemoryCheckpoints):
            fail = False
            committed = False

            def save(self, revision, expected):
                if self.fail:
                    if self.committed:
                        super().save(revision, expected)
                    raise CheckpointUnavailable("Injected uncertain publication")
                return super().save(revision, expected)

        for committed in (False, True):
            port = UncertainCheckpoints()
            host = self.make_host(port)
            view = host.read(("support:need",))
            request = self.fixture.request(view)
            port.fail, port.committed = True, committed
            outcome = InvestigatorPort(host).request(request)
            self.assertEqual(outcome.status, "publication_unconfirmed")
            self.assertFalse(host.active)
            self.assertNotIn(request.request_id, host.revision.records)
            port.fail = False
            host.refresh()
            self.assertEqual(request.request_id in host.revision.records, committed)
            self.assertFalse(host.active)

    def test_seam_imports_no_storage_engine_and_no_public_engine_fields(self):
        import ast

        import experiments.workspace_investigator_seam as seam

        tree = ast.parse(Path(seam.__file__).read_text())
        imports = [
            node.module or ""
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom)
        ]
        self.assertFalse(
            any("checkpoint_stores" in name or "sqlite" in name for name in imports)
        )
        self.assertFalse(
            any(
                isinstance(node, ast.Import)
                and any("sqlite" in item.name for item in node.names)
                for node in ast.walk(tree)
            )
        )
        for value in (AcquisitionRequest, RevisionRef, seam.Projection, seam.Outcome):
            self.assertFalse(
                set(value.__dataclass_fields__) & {"sql", "table", "transaction", "wal"}
            )


class SQLiteInvestigatorSeamTests(InvestigatorSeamTests):
    """Repeat the independent lifecycle oracles against durable WAL/FULL checkpoints."""

    def setUp(self):
        self.fixture = build_native_fixture()
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.port = SQLiteCheckpoints(Path(self.directory.name) / "store", create=True)
        self.addCleanup(self.port.close)
        self.host = self.make_host(self.port)


if __name__ == "__main__":
    unittest.main()
