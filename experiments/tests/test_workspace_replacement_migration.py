"""Normal producer/consumer parity, independent material-input and loss-boundary oracles."""

import json
import tempfile
import unittest
from collections import Counter
from dataclasses import replace
from pathlib import Path
from types import MappingProxyType
from unittest.mock import patch

from experiments.run_workspace_migration_trial import (
    comparable_report,
    forbid_producer_reentry,
    trial,
)
from experiments.workspace_replacement_migration import (
    NOW,
    ProjectionUnavailable,
    add_projection_pressure,
    capture_normal_pipeline,
    project_legacy_result,
)
from experiments.workspace_revision_representation import encode_checkpoint
from experiments.workspace_seam_checkpoints import MemoryCheckpoints
from upgradepilot.maintainer_action import synthesize_maintainer_action
from upgradepilot.report_projection import project_investigation_report


def altered_record(revision, key, **changes):
    records = dict(revision.records)
    records[key] = replace(records[key], **changes)
    return replace(revision, records=MappingProxyType(records))


class WorkspaceReplacementMigrationTests(unittest.TestCase):
    def setUp(self):
        self.no_network = patch(
            "requests.sessions.Session.send",
            side_effect=AssertionError("Unexpected egress"),
        )
        self.no_network.start()
        self.addCleanup(self.no_network.stop)

    def captured(self):
        return capture_normal_pipeline(MemoryCheckpoints())

    def test_one_normal_path_all_consumer_meanings_and_checkpoint_equal_across_backends(
        self,
    ):
        outputs = []
        for backend in ("memory", "sqlite"):
            with (
                self.subTest(backend=backend),
                tempfile.TemporaryDirectory() as directory,
            ):
                summary, checkpoint, report = trial(backend, Path(directory))
            self.assertEqual(summary["native_acquisition_port_returns"], 13)
            self.assertEqual(summary["native_owner_calls"], 15)
            self.assertEqual(summary["consumer_extra_native_or_acquisition_calls"], 0)
            self.assertEqual(
                summary["parity_consumer_attempts"],
                {"report_attempts": 4, "synthesis_attempts": 7},
            )
            self.assertEqual(
                summary["calls"]["orchestration:investigate_public_pull_request"], 1
            )
            self.assertEqual(
                summary["runtime_results"],
                ["RequirementSatisfiedAtCommandCompletion", "RequirementStateProblem"],
            )
            self.assertEqual(summary["action"], "abstain")
            self.assertEqual(summary["native_after"], "established_applicable")
            assessments = {item.assessment_id: item for item in report.assessments}
            self.assertEqual(
                assessments["runtime-command-1"].state,
                "satisfied_at_command_completion",
            )
            self.assertEqual(assessments["runtime-command-2"].state, "unresolved")
            self.assertEqual(
                assessments["python-impact"].strength, "grounded_interpretation"
            )
            self.assertEqual(assessments["artifact-impact"].status, "not_evaluated")
            self.assertTrue(
                any(u.assessment_id == "runtime-command-2" for u in report.unknowns)
            )
            self.assertIn("No non-abstention", report.action.reasons[0])
            outputs.append((summary, checkpoint, comparable_report(report)))
        self.assertEqual(*outputs)

    def test_call_oracle_refuses_processing_after_the_capture_context_exits(self):
        capture, original = self.captured()
        from upgradepilot import investigation as application
        from upgradepilot.impact import python_support

        counts = Counter(capture.calls)
        with forbid_producer_reentry():
            with self.assertRaisesRegex(
                AssertionError, "re-entered evaluate_python_support_drop_impact"
            ):
                application.evaluate_python_support_drop_impact(
                    original.python_support_drop_impact_result.candidate
                )
            with self.assertRaisesRegex(
                AssertionError, "re-entered evaluate_python_support_drop_impact"
            ):
                python_support.evaluate_python_support_drop_impact(
                    original.python_support_drop_impact_result.candidate
                )
            with self.assertRaisesRegex(
                AssertionError, "re-entered investigate_public_pull_request"
            ):
                application.investigate_public_pull_request("example/project", 7)
        self.assertEqual(capture.calls, counts)

    def test_capture_retains_real_owner_inputs_not_only_legacy_fields(self):
        capture, original = self.captured()
        values = capture.values["native:evaluate_dependency_ci_coverage:1:input"]
        coverage_inputs = values["args"][1]
        contexts = values["kwargs"]["source_contexts"]
        self.assertEqual(len(coverage_inputs), 1)
        self.assertIn(
            "PIP_CONFIG_FILE=/dev/null", coverage_inputs[0].definition.content
        )
        self.assertEqual(contexts[0].source_path, "requirements.txt")
        self.assertFalse(hasattr(original, "coverage_inputs"))
        self.assertFalse(hasattr(original, "source_contexts"))
        self.assertEqual(
            original.changed_files[0].patch, "@@ -1 +1 @@\n-demo==1.0\n+demo==2.0\n"
        )
        scopes = {
            r.scope
            for r in capture.revision.records.values()
            if r.kind == "source_text"
        }
        self.assertTrue(
            any(scope.endswith(":.github/workflows/ci.yml") for scope in scopes)
        )
        self.assertTrue(any(scope.endswith(":CHANGELOG.md") for scope in scopes))
        self.assertTrue(any(scope.endswith(":pyproject.toml") for scope in scopes))
        self.assertFalse(any(scope.endswith(":requirements.txt") for scope in scopes))
        self.assertEqual(capture.calls["native:analyze_dependency_change"], 1)

    def test_changed_live_value_cannot_override_the_immutable_native_fact(self):
        capture, original = self.captured()
        live = dict(capture.values)
        key = "legacy-field:runtime_dependency_state_result"
        live[key] = replace(
            original.runtime_dependency_state_result,
            evaluation_state="no_admitted_candidate",
        )
        with self.assertRaisesRegex(
            ProjectionUnavailable, "not bound to retained bytes"
        ):
            project_legacy_result(capture.revision, live)

    def test_absent_optional_manifest_field_is_not_silently_defaulted(self):
        capture, _ = self.captured()
        mapping = json.loads(
            capture.revision.records["migration:legacy-fields"].payload
        )
        del mapping["old_package_result"]
        revision = altered_record(
            capture.revision,
            "migration:legacy-fields",
            payload=json.dumps(mapping).encode(),
        )
        with self.assertRaisesRegex(ProjectionUnavailable, "Incomplete/unsupported"):
            project_legacy_result(revision, capture.values)

    def test_explicit_missing_native_material_blocks_the_projection(self):
        capture, _ = self.captured()
        revision = altered_record(
            capture.revision,
            "legacy-field:target_python_result",
            payload=None,
            gap="missing_retained_material",
        )
        with self.assertRaisesRegex(
            ProjectionUnavailable, "Missing material native field"
        ):
            project_legacy_result(revision, capture.values)

    def test_retained_checkpoint_bytes_do_not_hydrate_trusted_objects(self):
        capture, _ = self.captured()
        counts = Counter(capture.calls)
        with self.assertRaisesRegex(ProjectionUnavailable, "unsupported_native_codec"):
            project_legacy_result(capture.port.load(), {})
        self.assertEqual(capture.calls, counts)

    def test_other_exact_target_cannot_consume_the_old_native_values(self):
        capture, _ = self.captured()
        moved = replace(
            capture.revision,
            target=capture.revision.target.replace(b"a" * 40, b"f" * 40),
        )
        with self.assertRaisesRegex(ProjectionUnavailable, "another exact target"):
            project_legacy_result(moved, capture.values)

    def test_new_lifecycle_is_retained_but_cannot_create_an_action_permission(self):
        capture, _ = self.captured()
        before = capture.revision
        data = encode_checkpoint(before)
        counts = Counter(capture.calls)
        result = project_legacy_result(before, capture.values)
        report = comparable_report(project_investigation_report(result, now=NOW))
        add_projection_pressure(capture)
        self.assertEqual(encode_checkpoint(before), data)
        after = project_legacy_result(capture.revision, capture.values)
        self.assertEqual(after, result)
        self.assertEqual(
            comparable_report(project_investigation_report(after, now=NOW)), report
        )
        self.assertEqual(synthesize_maintainer_action(after).action, "abstain")
        self.assertEqual(
            json.loads(capture.revision.records["migration:proposal"].payload)[
                "evaluation"
            ],
            "unsupported_no_admitted_evaluator",
        )
        self.assertEqual(
            json.loads(capture.revision.records["migration:unfinished"].payload)[
                "completion"
            ],
            "unknown",
        )
        self.assertFalse(
            json.loads(capture.revision.records["migration:unfinished"].payload)[
                "automatic_retry_permitted"
            ]
        )
        self.assertEqual(capture.calls, counts)


if __name__ == "__main__":
    unittest.main()
