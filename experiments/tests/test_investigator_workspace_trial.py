"""New experiment/product composition boundaries; no model, network or target execution.

Controlled native capture is explicitly unfinished. Product consumer tests own the lower
level catalog/host invariants; these controls exercise wire dispatch, treatment restriction,
input visibility, attribution, budgets and trial failure handling introduced here.
"""

import json
import unittest
from dataclasses import replace
from unittest.mock import patch

from experiments.investigator_workspace_adapter import InvestigatorAssignment
from experiments.investigator_workspace_trial import (
    TrialLimits,
    mechanical_manifest,
    pack_input,
    protocol_definition,
    run_scripted_trial,
)
from upgradepilot.dependency.change import (
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.workspace.lifecycle_records import ViewDelivery
from upgradepilot.workspace.native_capture import NativeInvestigationCapture
from upgradepilot.workspace.native_representation import json_bytes
from upgradepilot.workspace.source_access import (
    RetainedSourceCatalog,
    RetainedSourceFile,
    RetainedSourceScope,
)


def fixture(treatment="structured", *, large=False, budget=256 * 1024):
    pull = PullRequestIdentity(
        "example/project",
        1,
        "A" * (6000 if large else 1),
        "open",
        False,
        "author",
        "main",
        "a" * 40,
        "update",
        "b" * 40,
        1,
    )
    dependency = DependencyVersionChange(
        "pytest",
        "pytest",
        "9.0.2",
        "9.0.3",
        (
            DependencyChangeSourceEvidence(
                "requirements.txt", "exact_requirement", "changed_file_patch"
            ),
        ),
    )
    capture = NativeInvestigationCapture()
    capture.start(
        pull,
        (ChangedFile("requirements.txt", "modified", 1, 1, 2, ""),),
        dependency,
        (),
    )
    boundary = capture.partial_snapshot()
    catalog = RetainedSourceCatalog(
        (
            RetainedSourceScope(
                "target",
                pull.repository,
                pull.head_sha,
                "repository_text",
                "Controlled text",
                "No runtime claim",
            ),
        ),
        (
            RetainedSourceFile(
                "target", "requirements.txt", "pytest==9.0.3\n" + "x" * 600 + "\n"
            ),
            RetainedSourceFile("target", "empty.txt", ""),
        ),
        target=boundary.target,
    )
    return InvestigatorAssignment(boundary, catalog, treatment, max_native_bytes=budget)


def request(tool, **arguments):
    return json_bytes({"tool": tool, "arguments": arguments})


def report(evidence=()):
    return json_bytes(
        {
            "summary": "A declared version; runtime remains unknown.",
            "claims": [
                {
                    "statement": "The file declares a version.",
                    "status": "asserted",
                    "evidence": list(evidence),
                    "missing_observation": "",
                }
            ],
            "conditions": [],
            "unexamined": ["Runtime environment"],
            "recommendation": "Resolve runtime uncertainty if decision-critical.",
            "recommendation_status": "unresolved",
            "recommendation_evidence": [],
            "recommendation_missing_observation": "Runtime binding",
            "stopping_reason": "Bounded scripted check",
        }
    )


def event_body(event):
    return json.loads(event.content)


def schema_pairs(array):
    """Independent finite-set oracle for the emitted reference-schema subset."""
    if array["maxItems"] == 0:
        return set()
    return {
        (kind, identity)
        for branch in array["items"]["anyOf"]
        for kind in branch["properties"]["kind"]["enum"]
        for identity in branch["properties"]["id"]["enum"]
    }


class InvestigatorCompositionTests(unittest.TestCase):
    def test_interruption_terminates_and_preserves_primary_when_termination_fails(self):
        assignment = fixture()
        def interrupted(packed):
            raise KeyboardInterrupt("operator stop")
        with patch.object(assignment.host, "terminate", side_effect=OSError("terminal write failed")) as terminate:
            with self.assertRaisesRegex(KeyboardInterrupt, "operator stop"):
                run_scripted_trial(assignment, interrupted)
        terminate.assert_called_once()
        result = assignment.last_trial_result
        self.assertIn("KeyboardInterrupt", result.problem)
        self.assertIn("terminal write failed", result.charges["termination_problem"])
        self.assertEqual(result.charges["consumer_invocation_attempts"], 1)
        self.assertEqual(result.original_responses, (None,))
        self.assertIsNone(result.termination_id)

    def test_correction_keeps_invalid_intent_out_of_new_citation_choices(self):
        for treatment in ("raw", "structured"):
            a = fixture(treatment)
            original = []

            def consume(packed, original=original):
                body = json.loads(packed.content)
                if body["phase"] == "investigate":
                    return (
                        request(
                            "read_source", source_id="target", path="requirements.txt"
                        )
                        if not body["events"]
                        else request("finish_investigation")
                    )
                pair = next(iter(packed.reference_pairs))
                valid = {"kind": pair[0], "id": pair[1]}
                bad = {**valid, "id": valid["id"][:60]}
                options = schema_pairs(
                    body["report_schema"]["properties"]["recommendation_evidence"]
                )
                self.assertEqual(options, {pair})
                self.assertNotIn((bad["kind"], bad["id"]), options)
                wire = report([bad] if not original else [valid])
                original.append(wire)
                return wire

            result = run_scripted_trial(
                a,
                consume,
                limits=TrialLimits(consumer_turns=4),
                reference_visibility="current_request",
            )
            self.assertEqual(result.outcome, "completed", result.problem)
            self.assertEqual(result.original_responses[-2:], tuple(original))
            self.assertEqual(len(result.charges["report_refusals"]), 1)
            self.assertEqual(result.charges["terminal_corrections"], 1)
            self.assertNotEqual(original[0], original[1])

    def test_closed_schema_tracks_actual_producers_and_uncitable_outcomes_for_both_treatments(
        self,
    ):
        for treatment in ("raw", "structured"):
            a = fixture(treatment)
            events = [a.invoke(request("list_sources"))]
            for path in ("requirements.txt", "empty.txt", "missing.txt"):
                events.append(
                    a.invoke(request("read_source", source_id="target", path=path))
                )
            events.append(a.invoke(request("search_sources", query="no-such-marker")))
            events.append(
                a.invoke(request("read_trial_event", event_id=events[0].event_id))
            )
            if treatment == "structured":
                native = a.invoke(request("read_native", families=["ci_coverage"]))
                events.append(native)
                record = event_body(native)["evidence"][0]
                record_id = a.references[record["id"]].native_ids[0]
                events.append(
                    a.invoke(request("read_native_page", record_id=record_id))
                )
            expected = {
                (v["kind"], v["id"])
                for e in events
                for v in event_body(e).get("evidence", [])
            }
            p = pack_input(
                protocol_definition(a, TrialLimits()), events, "investigate", 128 * 1024
            )
            body = json.loads(p.content)
            self.assertEqual(p.reference_pairs, expected)
            for array in [
                body["tools"]["record_note"]["properties"]["evidence"],
                body["report_schema"]["properties"]["recommendation_evidence"],
                body["report_schema"]["properties"]["claims"]["items"]["properties"][
                    "evidence"
                ],
            ]:
                self.assertEqual(schema_pairs(array), expected)
            self.assertEqual(
                [e["typed_citation_available"] for e in body["events"]],
                [bool(e.reference_pairs) for e in events],
            )
            self.assertFalse(body["events"][3]["typed_citation_available"])
            self.assertTrue(body["events"][2]["typed_citation_available"])
            self.assertTrue(body["events"][4]["typed_citation_available"])
            self.assertEqual("read_native" in body["tools"], treatment == "structured")
            for e, packed_event in zip(events, body["events"]):
                self.assertEqual(e.content.decode(), packed_event["content"])

    def test_reference_failure_classes_refuse_every_citation_surface_without_partial_publication(
        self,
    ):
        for treatment in ("raw", "structured"):
            for surface in ("claim", "recommendation", "note"):
                for variant in (
                    "mangled",
                    "wrong-kind",
                    "delivery",
                    "foreign",
                    "whitespace",
                ):
                    with self.subTest(
                        treatment=treatment, surface=surface, variant=variant
                    ):
                        a = fixture(treatment)
                        e = a.invoke(
                            request(
                                "read_source",
                                source_id="target",
                                path="requirements.txt",
                            )
                        )
                        good = event_body(e)["evidence"][0]
                        problem = a.invoke(
                            request(
                                "read_source", source_id="target", path="absent.txt"
                            )
                        )
                        foreign = fixture(treatment).invoke(
                            request(
                                "read_source",
                                source_id="target",
                                path="requirements.txt",
                            )
                        )
                        bad = {**good}
                        if variant == "mangled":
                            bad["id"] = good["id"][:60]
                        elif variant == "wrong-kind":
                            bad["kind"] = "native_record"
                        elif variant == "delivery":
                            bad["id"] = event_body(problem)["delivery_id"]
                        elif variant == "foreign":
                            bad["id"] = event_body(foreign)["evidence"][0]["id"]
                        else:
                            bad["id"] += " "
                        if surface == "note":
                            before = len(a.host.current.lifecycle_history.records)
                            refused = a.invoke(
                                request(
                                    "record_note", text="proposal", evidence=[good, bad]
                                ),
                                visible=frozenset(e.reference_ids),
                            )
                            self.assertEqual(refused.outcome, "refused")
                            self.assertFalse(a.notes)
                        else:
                            a.invoke(request("finish_investigation"))
                            before = len(a.host.current.lifecycle_history.records)
                            body = json.loads(report([good]))
                            if surface == "claim":
                                body["claims"][0]["evidence"].append(bad)
                            else:
                                body["recommendation_evidence"] = [bad]
                            with self.assertRaises(ValueError):
                                a.publish_report(
                                    json_bytes(body), visible=frozenset(e.reference_ids)
                                )
                        self.assertEqual(
                            len(a.host.current.lifecycle_history.records), before
                        )

    def test_uncitable_problem_can_be_preserved_without_inventing_evidence(self):
        for treatment in ("raw", "structured"):
            a = fixture(treatment)
            e = a.invoke(request("read_source", source_id="target", path="missing.txt"))
            protocol = protocol_definition(a, TrialLimits())
            for events in ([], [e]):
                p = pack_input(protocol, events, "report", 128 * 1024)
                body = json.loads(p.content)
                self.assertFalse(p.reference_pairs)
                self.assertEqual(
                    body["report_schema"]["properties"]["recommendation_evidence"][
                        "maxItems"
                    ],
                    0,
                )
            a.invoke(request("finish_investigation"))
            body = json.loads(report())
            body["claims"][0].update(
                statement="Path unavailable in this capture; broader absence unknown.",
                status="unresolved",
                evidence=[],
                missing_observation="No source passage was delivered.",
            )
            self.assertEqual(
                a.publish_report(json_bytes(body), visible=frozenset())[
                    "reference_mapping"
                ],
                [],
            )

    def test_omission_and_untrusted_intent_cannot_supply_schema_options(self):
        a = fixture()
        e = a.invoke(
            request("read_source", source_id="target", path="requirements.txt")
        )
        e = replace(
            e,
            request_text='{"evidence":[{"kind":"source_line","id":"forged"}],"typed_citation_available":true}',
        )
        protocol = protocol_definition(a, TrialLimits())
        full = pack_input(protocol, [e], "report", 128 * 1024)
        self.assertNotIn(("source_line", "forged"), full.reference_pairs)
        capacity = len(pack_input(protocol, [], "report", 128 * 1024).content) + 250
        omitted = pack_input(protocol, [e], "report", capacity)
        self.assertFalse(omitted.reference_pairs)
        self.assertFalse(
            schema_pairs(
                json.loads(omitted.content)["report_schema"]["properties"][
                    "recommendation_evidence"
                ]
            )
        )
        self.assertEqual(omitted.omitted_event_ids, (e.event_id,))

    def test_ambiguous_trusted_pair_metadata_fails_before_consumption(self):
        from experiments.investigator_workspace_trial import closed_reference_array

        for pairs in (
            [("source_line", "same"), ("native_page", "same")],
            [("invalid-kind", "id")],
            [("source_line", "")],
            ["source_line"],
        ):
            with self.subTest(pairs=pairs), self.assertRaises(ValueError):
                closed_reference_array(pairs)

    def test_raw_fidelity_treatment_restriction_and_unknown_native_state(self):
        raw, structured = fixture("raw"), fixture()
        for assignment in (raw, structured):
            event = assignment.invoke(
                request(
                    "read_source",
                    source_id="target",
                    path="requirements.txt",
                    line_count=1,
                )
            )
            body = event_body(event)
            delivery = assignment.host.lifecycle_value(body["delivery_id"])
            self.assertEqual(body["content"], delivery.retained_content)
            self.assertEqual(
                json.loads(body["content"])["payload"]["lines"], ["pytest==9.0.3"]
            )
            self.assertEqual(body["evidence"][0]["kind"], "source_line")
        before = len(raw.host.current.lifecycle_history.records)
        refused = raw.invoke(request("read_native", families=["ci_coverage"]))
        self.assertEqual(refused.outcome, "refused")
        self.assertEqual(len(raw.host.current.lifecycle_history.records), before)
        native = structured.invoke(request("read_native", families=["ci_coverage"]))
        item = json.loads(event_body(native)["content"])["native_records"][0]
        self.assertEqual(item["outcome"], "not_evaluated")

    def test_closed_wire_extra_authority_duplicate_keys_and_bad_integer_do_no_work(
        self,
    ):
        a = fixture()
        bad = [
            b'{"tool":"list_sources","tool":"read_native","arguments":{}}',
            b'{"tool":"list_sources","arguments":{},"authority":true}',
            request(
                "read_source",
                source_id="target",
                path="requirements.txt",
                start_line=True,
            ),
            b'{"tool":[],"arguments":{}}',
        ]
        before = len(a.host.current.lifecycle_history.records)
        for content in bad:
            self.assertEqual(a.invoke(content).outcome, "refused")
        self.assertEqual(len(a.events), len(bad))
        self.assertEqual(a.access.receipts, ())
        self.assertEqual(len(a.host.current.lifecycle_history.records), before)

    def test_callback_failure_is_not_overwritten_by_an_elapsed_deadline(self):
        def broken(_):
            raise RuntimeError("script failure after deadline")

        ticks = iter([0, 0, 2])
        result = run_scripted_trial(
            fixture(), broken, limits=TrialLimits(seconds=1), clock=lambda: next(ticks)
        )
        self.assertEqual(result.outcome, "failed")
        self.assertIn("script failure after deadline", result.problem)

    def test_zero_empty_problem_and_preview_remain_different_evidence(self):
        a = fixture()
        zero = a.invoke(request("search_sources", source_id="target", query="missing"))
        empty = a.invoke(request("read_source", source_id="target", path="empty.txt"))
        problem = a.invoke(
            request("read_source", source_id="target", path="absent.txt")
        )
        self.assertEqual(
            [zero.outcome, empty.outcome, problem.outcome],
            ["scoped_negative", "empty", "problem"],
        )
        self.assertEqual(event_body(problem)["evidence"], [])
        preview = a.invoke(request("search_sources", query="xxxxx"))
        self.assertEqual(
            event_body(preview)["evidence"][0]["kind"], "search_observation"
        )
        body = json.loads(event_body(preview)["content"])
        source_reference = body["payload"]["items"][0]["reference"]
        resolved = a.invoke(request("resolve_source", reference=source_reference))
        self.assertEqual(
            len(json.loads(event_body(resolved)["content"])["payload"]["lines"][0]), 600
        )
        self.assertEqual(event_body(resolved)["evidence"][0]["kind"], "source_line")

    def test_native_omission_page_and_foreign_page_are_not_full_record_evidence(self):
        a = fixture(large=True, budget=4096)
        view = a.invoke(request("read_native", families=["investigation_inputs"]))
        body = json.loads(event_body(view)["content"])
        self.assertEqual(body["native_records"], [])
        self.assertEqual(event_body(view)["evidence"], [])
        record = body["omitted"][0]["record_id"]
        page = a.invoke(
            request("read_native_page", record_id=record, character_count=120)
        )
        self.assertTrue(json.loads(event_body(page)["content"])["partial_payload"])
        self.assertEqual(event_body(page)["evidence"][0]["kind"], "native_page")
        ref = a.references[page.reference_ids[0]]
        self.assertTrue(ref.address.endswith(":0:120"))
        self.assertEqual(
            a.invoke(request("read_native_page", record_id="foreign")).outcome,
            "refused",
        )

    def test_reference_kind_assignment_input_visibility_and_stale_material_refuse_before_proposal(
        self,
    ):
        a, other = fixture(), fixture()
        delivered = a.invoke(
            request("read_source", source_id="target", path="requirements.txt")
        )
        evidence = event_body(delivered)["evidence"]
        a.invoke(request("finish_investigation"))
        other.invoke(request("finish_investigation"))
        before = len(a.host.current.lifecycle_history.records)
        with self.assertRaisesRegex(ValueError, "not-input-visible"):
            a.publish_report(report(evidence), visible=frozenset())
        with self.assertRaises(ValueError):
            other.publish_report(
                report(evidence), visible=frozenset(delivered.reference_ids)
            )
        forged = [{**evidence[0], "kind": "native_record"}]
        with self.assertRaises(ValueError):
            a.publish_report(report(forged), visible=frozenset(delivered.reference_ids))
        self.assertEqual(len(a.host.current.lifecycle_history.records), before)
        # New unrelated lifecycle progress keeps the genuine same-material reference valid.
        a.host.propose_stop("another", "Unrelated interaction")
        publication = a.publish_report(
            report(evidence), visible=frozenset(delivered.reference_ids)
        )
        self.assertEqual(publication["evaluation"], "unsupported")
        with patch.object(a.host, "current_validity") as validity:
            validity.return_value.status = "stale"
            with self.assertRaises(ValueError):
                a.publish_report(
                    report(evidence), visible=frozenset(delivered.reference_ids)
                )

    def test_wrong_target_method_scope_and_assignment_local_notes(self):
        a = fixture()
        with self.assertRaises(ValueError):
            InvestigatorAssignment(
                replace(
                    a.host.current.boundary,
                    target=replace(a.access.catalog.target, head_sha="c" * 40),
                ),
                a.access.catalog,
                "raw",
            )
        a.host.configure(authority=None, capabilities=())
        self.assertEqual(a.invoke(request("list_sources")).outcome, "refused")
        self.assertEqual(a.access.receipts, ())
        a, other = fixture(), fixture()
        a.invoke(request("record_note", text="My interpretation", evidence=[]))
        self.assertEqual(other.notes, {})
        self.assertNotEqual(a.host.lineage_id, other.host.lineage_id)
        note = a.invoke(request("read_trial_event", event_id="note-1"))
        self.assertEqual(event_body(note)["evidence"][0]["kind"], "trial_event")
        self.assertEqual(
            other.invoke(request("read_trial_event", event_id="note-1")).outcome,
            "refused",
        )

    def test_whole_event_packing_omits_reference_with_payload_and_refuses_tiny_context(
        self,
    ):
        a = fixture()
        event = a.invoke(
            request("read_source", source_id="target", path="requirements.txt")
        )
        protocol = protocol_definition(a, TrialLimits())
        full = pack_input(protocol, [event], "investigate", 128 * 1024)
        self.assertEqual(full.reference_ids, frozenset(event.reference_ids))
        empty_size = len(pack_input(protocol, [], "investigate", 128 * 1024).content)
        omitted = pack_input(protocol, [event], "investigate", empty_size + 250)
        self.assertEqual(omitted.omitted_event_ids, (event.event_id,))
        self.assertEqual(omitted.reference_ids, frozenset())
        self.assertEqual(
            json.loads(full.content)["budget_observation"],
            json.loads(omitted.content)["budget_observation"],
        )
        self.assertNotIn(b"pytest==9.0.3", omitted.content)
        with self.assertRaises(ValueError):
            pack_input(protocol, [], "investigate", 1)

    def test_spare_calls_do_not_make_read_plus_completion_affordable(self):
        a = fixture()
        responses = iter(
            [
                request("read_source", source_id="target", path="requirements.txt"),
                request("finish_investigation"),
            ]
        )
        refs = []
        snapshots = []

        def consumer(packed):
            body = json.loads(packed.content)
            snapshots.append(body["budget_observation"])
            for event in body["events"]:
                refs.extend(json.loads(event["content"]).get("evidence", []))
            return report(refs[:1]) if body["phase"] == "report" else next(responses)

        result = run_scripted_trial(
            a, consumer, limits=TrialLimits(consumer_turns=3, operations=9)
        )
        self.assertEqual(result.outcome, "limit_exhausted")
        self.assertIsNone(result.report_publication)
        self.assertIn("operation admission refused", result.problem)
        self.assertEqual(
            snapshots[-1]["trial_remaining"]["invocations_including_this_request"], 1
        )
        self.assertEqual(snapshots[-1]["trial_remaining"]["operation_units"], 2)

    def test_scripted_run_publishes_attribution_and_procedural_finish_without_model(
        self,
    ):
        a = fixture()
        responses = iter(
            [
                request(
                    "read_source",
                    source_id="target",
                    path="requirements.txt",
                    line_count=1,
                ),
                request("finish_investigation"),
            ]
        )
        evidence = []

        def consumer(packed):
            body = json.loads(packed.content)
            for event in body["events"]:
                observation = json.loads(event["content"])
                if observation.get("evidence"):
                    evidence[:] = observation["evidence"]
            return report(evidence) if body["phase"] == "report" else next(responses)

        result = run_scripted_trial(a, consumer)
        self.assertEqual(result.outcome, "completed", result.problem)
        self.assertEqual(result.report_publication["evaluation"], "unsupported")
        self.assertEqual(len(result.report_publication["citation_ids"]), 1)
        self.assertEqual(result.charges["model_calls"], 0)
        self.assertIsNone(result.charges["model_tokens"])
        self.assertTrue(result.termination_id)
        self.assertFalse(mechanical_manifest(a)["inference_admitted"])

    def test_budget_refusals_precede_backend_and_keep_original_response(self):
        for limits in (TrialLimits(operations=2), TrialLimits(observation_bytes=1)):
            a = fixture()
            original = request(
                "read_source", source_id="target", path="requirements.txt"
            )
            result = run_scripted_trial(
                a, lambda _, content=original: content, limits=limits
            )
            self.assertEqual(result.outcome, "limit_exhausted")
            self.assertEqual(result.original_responses, (original,))
            self.assertEqual(a.access.receipts, ())
            self.assertEqual(result.charges["observation_bytes"], 0)
            self.assertLessEqual(
                result.charges["admission_operations"], limits.operations
            )

    def test_failed_publication_retains_work_and_is_not_retried_as_empty(self):
        a = fixture()
        with patch.object(
            a.host, "deliver_view", side_effect=RuntimeError("publication unavailable")
        ):
            result = run_scripted_trial(
                a,
                lambda _: request(
                    "read_source", source_id="target", path="requirements.txt"
                ),
            )
        self.assertEqual(result.outcome, "failed")
        self.assertEqual(result.charges["consumer_invocation_attempts"], 1)
        receipt = a.access.receipts[-1]
        self.assertEqual(receipt.examined_files, 1)
        self.assertGreater(receipt.examined_lines, 0)
        self.assertIsNone(receipt.delivery_id)
        self.assertFalse(
            any(
                isinstance(a.host.lifecycle_value(r.record_id), ViewDelivery)
                for r in a.host.current.lifecycle_history.records
            )
        )

    def test_malformed_outputs_have_bounded_visible_corrections_without_salvage(self):
        a = fixture()
        responses = iter(
            [b"not json", request("finish_investigation"), b"{}", report()]
        )
        result = run_scripted_trial(a, lambda _: next(responses))
        self.assertEqual(result.outcome, "completed", result.problem)
        self.assertEqual(result.original_responses[0], b"not json")
        self.assertEqual(result.original_responses[2], b"{}")
        self.assertEqual(result.charges["corrections"], 2)
        self.assertEqual(result.charges["terminal_corrections"], 1)
        self.assertIn(b"report-error", result.packed_inputs[-1].content)
        failed = run_scripted_trial(fixture(), lambda _: b"not json")
        self.assertEqual(failed.outcome, "failed")
        self.assertEqual(failed.charges["consumer_invocation_attempts"], 3)

    def test_consumer_exception_and_deadline_never_become_success_or_zero_usage(self):
        def broken(_):
            raise RuntimeError("script failure")

        failed = run_scripted_trial(fixture(), broken)
        self.assertEqual(failed.outcome, "failed")
        self.assertEqual(failed.original_responses, (None,))
        self.assertEqual(failed.charges["consumer_invocation_attempts"], 1)
        clock_values = iter([0, 0, 2, 2, 2])
        a = fixture()
        timeout = run_scripted_trial(
            a,
            lambda _: request("list_sources"),
            limits=TrialLimits(seconds=1),
            clock=lambda: next(clock_values),
        )
        self.assertEqual(timeout.outcome, "limit_exhausted")
        self.assertEqual(a.access.receipts, ())


if __name__ == "__main__":
    unittest.main()
