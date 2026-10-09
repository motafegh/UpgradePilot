"""Independent fidelity/failure oracles plus differential representation checks."""

from __future__ import annotations

import json
import unittest
from dataclasses import replace
from unittest.mock import patch

from experiments.workspace_retention_corpus import build_retention_corpus
from experiments.workspace_revision_representation import (
    ImmutableSuccessorHistory,
    MutableDraftHistory,
    TraceRecord,
    affected_dependents,
    decode_checkpoint,
    encode_checkpoint,
    material_closure,
    retention_gaps,
)

APPROACHES = (ImmutableSuccessorHistory, MutableDraftHistory)


class WorkspaceRevisionRepresentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.corpus = build_retention_corpus()

    def history(self, approach):
        history = approach(self.corpus.target)
        for additions, roots in self.corpus.steps:
            history.publish(additions, roots)
        return history

    def test_native_owners_produce_distinct_results_and_material_basis_survives(self):
        outcomes = self.corpus.native_outcomes
        self.assertEqual(
            outcomes["ci"]["runtime"][0]["type"],
            "RequirementSatisfiedAtCommandCompletion",
        )
        self.assertEqual(outcomes["ci"]["runtime"][1]["state"], "unresolved")
        self.assertEqual(
            outcomes["conditional"]["consumptions"][0]["reason"],
            "changed_requirement_marker_not_evaluated",
        )
        self.assertEqual(outcomes["support"]["before"], "unresolved")
        self.assertEqual(outcomes["support"]["after"], "established_applicable")
        for approach in APPROACHES:
            with self.subTest(approach=approach.__name__):
                restored = decode_checkpoint(
                    encode_checkpoint(self.history(approach).history[-1])
                )
                self.assertTrue(
                    {
                        "ci:workflow-text",
                        "ci:input",
                        "ci:source-context",
                        "dependency:base-text",
                        "dependency:head-text",
                        "upstream:authority",
                        "upstream:proposal",
                        "support:before",
                        "support:relevance",
                        "extra:base",
                        "target:project-text",
                        "extra:workflow",
                    }
                    <= set(material_closure(restored))
                )
                native = json.loads(restored.records["ci:runtime"].payload)
                results = native["fields"]["assessments"]["tuple"]
                self.assertTrue(
                    results[0]["fields"]["result"]["type"].endswith(
                        "RequirementSatisfiedAtCommandCompletion"
                    )
                )
                self.assertEqual(
                    results[1]["fields"]["result"]["fields"]["state"], "unresolved"
                )

    def test_both_approaches_have_byte_identical_closures_at_every_publication(self):
        first, second = (self.history(approach) for approach in APPROACHES)
        for left, right in zip(first.history, second.history, strict=True):
            self.assertEqual(encode_checkpoint(left), encode_checkpoint(right))
            restored = decode_checkpoint(encode_checkpoint(left))
            self.assertEqual(encode_checkpoint(restored), encode_checkpoint(left))
            self.assertEqual(restored.roots, left.roots)
            self.assertEqual(restored.triggering_records, left.triggering_records)

    def test_historical_views_remain_stable_when_successors_are_published(self):
        for approach in APPROACHES:
            history = approach(self.corpus.target)
            old = history.publish(*self.corpus.steps[0])
            before = encode_checkpoint(old)
            for step in self.corpus.steps[1:]:
                history.publish(*step)
            self.assertEqual(encode_checkpoint(old), before)
            self.assertNotIn("support:after", old.records)
            with self.assertRaises(TypeError):
                old.records["injected"] = next(iter(old.records.values()))

    def test_failed_batch_is_atomic_for_collision_and_broken_material_reference(self):
        for approach in APPROACHES:
            history = self.history(approach)
            old = history.history[-1]
            before = encode_checkpoint(old)
            fresh = TraceRecord("fresh", "experiment", "observation", "scope", b"fresh")
            collision = replace(old.records["ci:runtime"], scope="different-scope")
            with self.assertRaisesRegex(ValueError, "collision"):
                history.publish((fresh, collision), old.roots)
            broken = replace(fresh, dependencies=("missing",))
            with self.assertRaisesRegex(ValueError, "Broken material reference"):
                history.publish((broken,), old.roots + ("fresh",))
            self.assertEqual(len(history.history), 5)
            self.assertEqual(encode_checkpoint(history.history[-1]), before)
            accepted = history.publish((fresh,), old.roots + ("fresh",))
            self.assertEqual(accepted.records["fresh"], fresh)

    def test_identity_deduplication_does_not_conflate_scope_or_annotation_with_content(
        self,
    ):
        for approach in APPROACHES:
            history = self.history(approach)
            old = history.history[-1]
            record = old.records["ci:runtime"]
            duplicate = history.publish((record, record), old.roots)
            self.assertEqual(len(duplicate.records), len(old.records))
            self.assertEqual(duplicate.records["ci:runtime"].digest, record.digest)
            alternate = replace(
                record, record_id="ci:other-scope", scope="different-scope"
            )
            revision = history.publish((alternate,), old.roots + (alternate.record_id,))
            self.assertEqual(
                revision.records[alternate.record_id].digest, record.digest
            )
            self.assertNotEqual(
                revision.records[alternate.record_id].scope, record.scope
            )
            self.assertEqual(old.records["annotation"].dependencies, ("ci:runtime",))
            for collision in (
                replace(record, payload=b"changed"),
                replace(record, owner="model"),
            ):
                with self.assertRaisesRegex(ValueError, "collision"):
                    history.publish((collision,), old.roots)

    def test_empty_failed_unsupported_and_completion_unknown_do_not_collapse(self):
        for approach in APPROACHES:
            revision = decode_checkpoint(
                encode_checkpoint(self.history(approach).history[-1])
            )
            self.assertEqual(revision.records["read:empty"].payload, b"")
            failed = json.loads(revision.records["read:failed"].payload)
            self.assertEqual(failed["fields"]["reason"], "not_found")
            unsupported = json.loads(revision.records["evaluation:unsupported"].payload)
            self.assertEqual(
                unsupported, {"assessment": None, "outcome": "unsupported"}
            )
            unknown = json.loads(revision.records["attempt:unknown"].payload)
            self.assertEqual(unknown["outcome"], "completion_unknown")
            self.assertIsNone(unknown["retry_permission"])
            view = json.loads(revision.records["view:delivered"].payload)
            self.assertIn("support:after", view["omitted_but_addressable"])
            self.assertNotIn("support:after", view["delivered"])
            self.assertEqual(view["examined"], "unknown")

    def test_declared_gaps_are_inspectable_but_broken_or_undeclared_material_is_rejected(
        self,
    ):
        revision = self.history(ImmutableSuccessorHistory).history[-1]
        self.assertEqual(set(retention_gaps(revision)), {"method:missing"})
        self.assertNotIn("read:empty", retention_gaps(revision))
        self.assertNotIn(
            "unreferenced-debug", decode_checkpoint(encode_checkpoint(revision)).records
        )
        with self.assertRaisesRegex(ValueError, "explicit gap"):
            replace(revision.records["read:empty"], payload=None)
        body = json.loads(encode_checkpoint(revision))
        body["records"] = [
            entry for entry in body["records"] if entry["id"] != "ci:workflow-text"
        ]
        with self.assertRaisesRegex(ValueError, "Broken material reference"):
            decode_checkpoint(json.dumps(body).encode())

    def test_integrity_versions_and_trigger_links_cannot_be_silently_coerced(self):
        revision = self.history(ImmutableSuccessorHistory).history[-1]
        encoded = encode_checkpoint(revision)
        for mutate in (
            lambda body: body.update(version=True),
            lambda body: body.update(version=2),
            lambda body: body.update(predecessor=True),
            lambda body: body.update(triggering_records=["absent-trigger"]),
            lambda body: body["records"][0].update(payload="damaged"),
            lambda body: body["records"].append(body["records"][0]),
        ):
            body = json.loads(encoded)
            mutate(body)
            with self.assertRaises(ValueError):
                decode_checkpoint(json.dumps(body).encode())

    def test_basis_changes_identify_affected_successors_without_native_reinterpretation(
        self,
    ):
        revision = self.history(ImmutableSuccessorHistory).history[-1]
        original = revision.records["support:before"].payload
        affected = set(affected_dependents(revision, {"support:target-declaration"}))
        self.assertTrue(
            {"support:relevance", "support:after", "lineage", "view:delivered"}
            <= affected
        )
        self.assertTrue({"support:before", "ci:runtime"}.isdisjoint(affected))
        self.assertEqual(affected_dependents(revision, {"unreferenced-debug"}), ())
        self.assertEqual(revision.records["support:before"].payload, original)

    def test_payload_codec_fails_for_uninspected_types_instead_of_string_salvage(self):
        from experiments.workspace_revision_representation import encode_fields

        with self.assertRaisesRegex(TypeError, "Uninspected payload type"):
            encode_fields(object())

    def test_mutable_draft_has_an_explicit_unpublished_boundary(self):
        history = MutableDraftHistory(self.corpus.target)
        old = history.publish(*self.corpus.steps[0])
        old_bytes = encode_checkpoint(old)
        additions, roots = self.corpus.steps[1]
        for addition in additions:
            history.stage((addition,))
        self.assertEqual(len(history.history), 2)
        self.assertEqual(encode_checkpoint(history.history[-1]), old_bytes)
        self.assertNotIn("support:after", decode_checkpoint(old_bytes).records)
        committed = history.publish_pending(roots)
        self.assertIn("support:after", committed.records)

    def test_corpus_and_round_trip_stay_offline_and_do_not_run_a_model(self):
        with (
            patch(
                "requests.sessions.Session.request",
                side_effect=AssertionError("network call"),
            ),
            patch(
                "upgradepilot.upstream.support_drop_extractor.LocalSupportDropExtractor.extract",
                side_effect=AssertionError("model call"),
            ),
        ):
            corpus = build_retention_corpus()
            history = ImmutableSuccessorHistory(corpus.target)
            for step in corpus.steps:
                history.publish(*step)
            decode_checkpoint(encode_checkpoint(history.history[-1]))

    def test_rejected_shortcuts_have_discriminating_negative_evidence(self):
        from experiments.run_workspace_revision_comparison import negative_controls

        revision = self.history(ImmutableSuccessorHistory).history[-1]
        controls = negative_controls(self.corpus, revision)
        self.assertIn(
            "support:after",
            controls["aliased_read_only_proxy"]["historical_record_ids_added"],
        )
        self.assertTrue(controls["result_only_capture"]["structural_round_trip_passed"])
        self.assertIn(
            "ci:workflow-text",
            controls["result_only_capture"]["missing_independent_consumer_basis"],
        )
        self.assertEqual(len(set(controls["digest_only_identity"]["byte_digests"])), 1)
        self.assertTrue(all(control["rejected"] for control in controls.values()))

    def test_distinct_bindings_cannot_hide_different_bytes_for_one_exact_source(self):
        for approach in APPROACHES:
            history = self.history(approach)
            old = history.history[-1]
            source = old.records["target:project-text"]
            alias = replace(source, record_id="alias:target-project")
            history.publish((alias,), old.roots + (alias.record_id,))
            collision = replace(
                source, record_id="other:target-project", payload=b"different input"
            )
            with self.assertRaisesRegex(
                ValueError, "Exact source identity/content collision"
            ):
                history.publish((collision,), old.roots + (collision.record_id,))

    def test_reordered_delivery_preserves_native_meaning_and_target_identity(self):
        for approach in APPROACHES:
            first, second = approach(self.corpus.target), approach(self.corpus.target)
            for additions, roots in self.corpus.steps:
                first.publish(additions, roots)
                second.publish(tuple(reversed(additions)), roots)
            self.assertEqual(
                dict(first.history[-1].records), dict(second.history[-1].records)
            )
            self.assertEqual(first.history[-1].target, second.history[-1].target)
            self.assertEqual(
                set(first.history[-1].triggering_records),
                set(second.history[-1].triggering_records),
            )


if __name__ == "__main__":
    unittest.main()
