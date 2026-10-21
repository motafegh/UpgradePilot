"""Real native-owner composition on controlled inputs; no frozen-case output or model call."""

from dataclasses import asdict, replace
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from test_workspace_native_reconstruction import captured_case
from experiments import investigator_ci_presentation as presentation
from upgradepilot.workspace.native_boundary import exact_investigation_target
from upgradepilot.workspace.native_projection import reconstruct_ci_projection


def native_case():
    _, original, boundary, _, _ = captured_case()
    return original, reconstruct_ci_projection(boundary, expected_target=boundary.target)


def bound_proposal(target, *, statement="INVENTED_CI_COMPATIBILITY_MARKER"):
    # Valid laboratory report shape can still contain false claims on every free-text
    # surface. The consumer must not rely on detecting those claims to exclude them.
    raw = {
        "summary": statement, "claims": [{"statement": statement, "status": "asserted", "evidence": [], "missing_observation": ""}],
        "conditions": [statement], "unexamined": [statement], "recommendation": statement,
        "recommendation_status": "asserted", "recommendation_evidence": [],
        "recommendation_missing_observation": "", "stopping_reason": statement,
    }
    packed = json.dumps({"task": {"target": asdict(target), "case_label": "controlled"}}).encode()
    published = json.dumps({"role": "controlled", "report_publication": {"proposal_id": "proposal-controlled", "evaluation": "unsupported"}}).encode()
    content = json.dumps(raw).encode()
    reference = presentation.bind_interpretation_reference(
        target=target, packed=packed, publication=published, response=content, response_path="retained/original-response.json")
    return reference, content, packed, published


class CIPresentationTests(unittest.TestCase):
    def test_valid_native_positive_is_preserved_and_every_model_surface_is_excluded(self):
        original, projection = native_case()
        target = exact_investigation_target(original.pull_request, original.dependency_result)
        reference, content, _, _ = bound_proposal(target)
        with patch("upgradepilot.report_projection.synthesize_maintainer_action", side_effect=AssertionError("CI synthesis")):
            view = presentation.compose_ci_presentation(projection, native_basis={"retention_gap": "controlled"}, interpretation=reference)
        self.assertTrue(any(a.state == "satisfied_at_command_completion" for a in view.ci.assessments))
        self.assertNotIn("INVENTED_CI_COMPATIBILITY_MARKER", view.render())
        self.assertNotIn("INVENTED_CI_COMPATIBILITY_MARKER", json.dumps(view.artifact()))
        self.assertEqual(view.artifact()["interpretation"]["response_sha256"], presentation.digest(content))
        self.assertEqual(view.artifact()["interpretation"]["evaluation"], "unsupported")
        self.assertIn("command-completion", view.render().lower())
        self.assertNotIn("Maintainer action:", view.render())

    def test_missing_proposal_does_not_drop_native_evidence_or_invent_abstention(self):
        _, projection = native_case()
        view = presentation.compose_ci_presentation(projection, native_basis={"producer_version": None})
        self.assertEqual(view.artifact()["interpretation"]["status"], "unavailable")
        self.assertTrue(view.ci.assessments)
        self.assertIn("Unavailable", view.render())
        self.assertNotIn("Maintainer action:", view.render())

    def test_cross_artifact_target_role_and_unpublished_interpretation_refused(self):
        original, projection = native_case()
        target = exact_investigation_target(original.pull_request, original.dependency_result)
        reference, content, packed, published = bound_proposal(target)
        wrong = replace(target, head_sha="e" * 40)
        with self.assertRaisesRegex(ValueError, "another exact"):
            presentation.compose_ci_presentation(projection, native_basis={}, interpretation=replace(reference, target=wrong))
        for target_value, publication_value in (
            (wrong, published),
            (target, json.dumps({"role": "foreign", "report_publication": {"proposal_id": "p", "evaluation": "unsupported"}}).encode()),
            (target, json.dumps({"role": "controlled", "report_publication": None}).encode()),
        ):
            with self.assertRaises(ValueError):
                presentation.bind_interpretation_reference(target=target_value, packed=packed, publication=publication_value,
                                                           response=content, response_path="original.json")

    def test_watchdog_and_failed_worker_preserve_original_partial_results(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "result.json"
            presentation.write(path, {"original_partial": "retained"})
            presentation.dispatch([sys.executable, "-c", "import time;time.sleep(5)"], path, .05)
            row = presentation.load(path)
            self.assertEqual(row["state"], "watchdog_cancelled")
            self.assertEqual(row["original_partial"], "retained")
            presentation.dispatch([sys.executable, "-c", "raise SystemExit(2)"], path, 1)
            row = presentation.load(path)
            self.assertEqual(row["state"], "process_failure")
            self.assertEqual(row["original_partial"], "retained")

    def test_freeze_drift_and_offline_network_process_access_refuse(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "freeze.json"
            presentation.write(path, {"source": "original"})
            with patch.object(presentation, "prepare", return_value={"source": "changed"}):
                with self.assertRaisesRegex(ValueError, "changed"):
                    presentation.verify_freeze(path)
        for event in ("socket.connect", "subprocess.Popen", "os.system"):
            with self.assertRaises(RuntimeError):
                presentation.offline_guard(event, ())

    def test_new_source_freeze_admits_only_report_changes_and_retains_membership(self):
        historical = {"src/upgradepilot/report.py": "old", "src/upgradepilot/ci/dependency_state.py": "native"}
        current = {**historical, "src/upgradepilot/report.py": "new"}
        self.assertEqual(set(presentation.report_source_delta(historical, current)), {"src/upgradepilot/report.py"})
        for invalid in ({**current, "src/upgradepilot/ci/dependency_state.py": "changed"},
                        {"src/upgradepilot/ci/dependency_state.py": "native"}):
            with self.assertRaises(ValueError):
                presentation.report_source_delta(historical, invalid)

    def test_native_refusal_is_input_unavailable_with_retained_case_row(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            frozen = {"common_root": str(root), "cases": [{"selection": {"case_id": "controlled", "directory": "source"}}]}
            with patch.object(presentation.sys, "addaudithook"), patch.object(
                presentation, "reconstruct_on_copy", side_effect=presentation.NativeReconstructionError("unsupported_native_codec", "controlled refusal")
            ):
                presentation.case_worker(frozen, 0, root / "output", root / "private")
            row = presentation.load(root / "output/result.json")
            self.assertEqual(row["state"], "input_unavailable")
            self.assertEqual(row["case_id"], "controlled")
            self.assertNotIn("abstain", json.dumps(row))


if __name__ == "__main__":
    unittest.main()
