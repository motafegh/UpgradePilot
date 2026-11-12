"""Real source-profile control plus explicit selected CI log, native save and cold open.

The source-control transport performs genuine existing source-client code paths.
CI calls are injected, so negative cases do not depend on live Actions retention.
"""
from __future__ import annotations

import hashlib
import io
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr
from dataclasses import replace
from pathlib import Path
from unittest.mock import Mock, patch

import test_caller_signature_source_acquisition as source_controls
from test_caller_signature_delivery import _COLD_OPEN

from upgradepilot.ci.job_log_diagnostic import (
    SelectedCIJob, interpret_selected_job_log,
)
from upgradepilot.cli import main
from upgradepilot.github.actions import (
    WorkflowJob, WorkflowJobLog, WorkflowRun,
)
from upgradepilot.github.api import GitHubAcquisitionError
from upgradepilot.report_file import read_report
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_projection import reconstruct_ci_job_log_diagnostic
from upgradepilot.workspace.native_codecs import encode_native_value
from upgradepilot.workspace.native_representation import NativeReconstructionError


class CombinedCILogDeliveryTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory(prefix="upgradepilot-combined-ci-")
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.store_path = self.root / "private-store"
        self.report_path = self.root / "report.json"

    def run_combined(self, *,
                     text="2026-11-01 Successfully installed demo-2.0\n"
                          "2026-11-01 E TypeError: Client.__init__() got an unexpected "
                          "keyword argument 'option'\n"
                          "UNRETAINED_CI_PAYLOAD_SENTINEL\n",
                     unavailable=False):
        identity, session, requests = (
            source_controls.NativeSourceClientCompositionTests().controlled_transport(
                forwarded=True
            )
        )
        run = WorkflowRun(414, 43, "CI", "pull_request", identity.head_sha,
                          "completed", "failure", 2)
        job = WorkflowJob(715, 414, "backend", identity.head_sha,
                          "completed", "failure", ())
        bytes_ = text.encode()
        log = WorkflowJobLog(
            identity.repository, identity.head_sha, 414, 2, 715,
            f"https://api.github.com/repos/{identity.repository}/actions/jobs/715/logs",
            len(bytes_), hashlib.sha256(bytes_).hexdigest(), text,
        )
        actions = Mock()
        if unavailable:
            actions.get_selected_failed_workflow_job.side_effect = GitHubAcquisitionError(
                "deliberate control refusal", reason="forbidden_or_rate_limited", status_code=403,
            )
        else:
            actions.get_selected_failed_workflow_job.return_value = (run, job)
            actions.get_failed_workflow_job_log.return_value = log

        def source_session(*, token, policy):
            self.assertIsNone(token)
            session.policy = policy
            return session

        args = [
            identity.repository, str(identity.number),
            "--evidence-profile", "caller-signature-ci",
            "--ci-run-id", "414", "--ci-run-attempt", "2", "--ci-job-id", "715",
            "--expected-base", identity.base_sha,
            "--expected-head", identity.head_sha,
            "--workspace-store", str(self.store_path),
            "--save-report", str(self.report_path),
        ]
        stdout = io.StringIO()
        with (
            patch("upgradepilot.cli.AcquisitionSession", side_effect=source_session),
            patch("upgradepilot.cli.GitHubActionsClient", return_value=actions),
            patch("socket.socket.connect", side_effect=AssertionError("network forbidden")),
            redirect_stdout(stdout),
        ):
            status = main(args)
        return status, stdout.getvalue(), actions, identity, requests

    def cold(self, revision, *extra):
        env = dict(os.environ, PYTHONPATH=os.pathsep.join(
            str(Path(path).absolute()) for path in sys.path if path
        ))
        result = subprocess.run(
            [sys.executable, "-c", _COLD_OPEN,
             "--open-workspace", str(self.store_path), "--revision", revision, *extra],
            cwd=self.root, env=env, capture_output=True, text=True, timeout=45,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout

    @staticmethod
    def revision(output):
        return next(
            line.removeprefix("Confirmed revision: ")
            for line in output.splitlines() if line.startswith("Confirmed revision: ")
        )

    def test_combined_report_and_cold_workspace_preserve_separate_observations(self):
        status, output, actions, identity, requests = self.run_combined()
        self.assertEqual(status, 0, output)
        actions.get_selected_failed_workflow_job.assert_called_once()
        self.assertEqual(
            actions.get_selected_failed_workflow_job.call_args.args[1:],
            (414, 2, 715)
        )
        self.assertIn("Rejected keyword: option", output)
        self.assertIn("Observed error text: TypeError: Client.__init__", output)
        self.assertIn("Installation-summary token: demo-2.0", output)
        self.assertIn("upgrade-caused regression: not established", output)
        self.assertIn("CI dependency coverage: not evaluated", output)
        self.assertIn("Runtime dependency state: not evaluated", output)

        report = read_report(self.report_path)
        by_id = {assessment.assessment_id: assessment for assessment in report.assessments}
        self.assertEqual(by_id["ci-job-log"].state, "observed_keyword_error")
        self.assertEqual(by_id["ci"].status, "not_evaluated")
        self.assertEqual(by_id["runtime"].status, "not_evaluated")
        self.assertEqual(report.action.state, "abstain")
        self.assertTrue(any(f.name == "install_token" and f.value == "demo-2.0"
                            for f in by_id["ci-job-log"].facts))
        self.assertNotIn("UNRETAINED_CI_PAYLOAD_SENTINEL", self.report_path.read_text())
        excerpt = next(source for source in report.sources if source.kind == "ci_job_log_excerpt")
        self.assertEqual(
            excerpt.content, "TypeError: Client.__init__() got an unexpected keyword argument 'option'"
        )
        revision = self.revision(output)
        offline = self.cold(revision)
        self.assertIn("Selected historical CI job log", offline)
        self.assertIn("Observed error text: TypeError: Client.__init__", offline)
        self.assertIn("Maintainer action: abstain", offline)
        original = self.cold(revision, "--show-source", excerpt.source_id)
        self.assertIn("BEGIN LITERAL SOURCE TEXT", original)
        self.assertIn(excerpt.content, original)
        store = CheckpointStore.open(self.store_path, read_only=True)
        selected = store.read_selected_revision(revision).revision
        diagnostic = reconstruct_ci_job_log_diagnostic(
            selected.boundary, expected_target=selected.boundary.target
        )
        self.assertEqual((diagnostic.run_id, diagnostic.run_attempt, diagnostic.job_id),
                         (414, 2, 715))
        forged = replace(diagnostic, rejected_keyword="fabricated")
        payload = encode_native_value("ci_job_log_diagnostic", forged)
        altered = replace(
            selected.boundary,
            records=tuple(
                replace(record, payload=payload,
                        payload_digest=hashlib.sha256(payload).hexdigest())
                if record.family == "ci_job_log_diagnostic" else record
                for record in selected.boundary.records
            ),
        )
        with self.assertRaises(NativeReconstructionError):
            reconstruct_ci_job_log_diagnostic(
                altered, expected_target=altered.target,
            )

    def test_refusal_keeps_source_results_and_an_explicit_unavailable_ci_result(self):
        status, output, actions, _, _ = self.run_combined(unavailable=True)
        self.assertEqual(status, 3, output)
        self.assertIn("Selected exact CI job log was unavailable", output)
        report = read_report(self.report_path)
        by_id = {assessment.assessment_id: assessment for assessment in report.assessments}
        self.assertEqual(by_id["ci-job-log"].state, "unavailable")
        self.assertEqual(by_id["ci-job-log"].status, "problem")
        self.assertTrue(any(item.assessment_id.startswith("caller-signature-comparison-")
                            for item in report.assessments))
        self.assertEqual(report.action.state, "abstain")
        self.assertIn("CI log: unavailable", self.cold(self.revision(output)))
        actions.get_failed_workflow_job_log.assert_not_called()

    def test_nonmatching_and_conflicting_errors_preserve_unknown_classification(self):
        for text in (
            "2026-11-01 pytest collection failed with ValueError: something else\n",
            "TypeError: Client.__init__() got an unexpected keyword argument 'option'\n"
            "TypeError: Client.__init__() got an unexpected keyword argument 'other'\n",
        ):
            with self.subTest(text=text), tempfile.TemporaryDirectory() as subdir:
                self.store_path = Path(subdir) / "private-store"
                self.report_path = Path(subdir) / "report.json"
                status, output, _, _, _ = self.run_combined(text=text)
                self.assertEqual(status, 0, output)
                report = read_report(self.report_path)
                ci = next(a for a in report.assessments if a.assessment_id == "ci-job-log")
                self.assertEqual((ci.state, ci.status), ("unclassified_log", "problem"))
                self.assertNotIn("Observed error text:", output)
                self.assertIn("CI log: unclassified_log", self.cold(self.revision(output)))

    def test_repeated_pytest_summary_of_same_error_is_not_false_ambiguity(self):
        identity, _, _ = source_controls.NativeSourceClientCompositionTests().controlled_transport()
        selection = SelectedCIJob(414, 2, 715)
        error = "TypeError: Client.__init__() got an unexpected keyword argument 'option'"
        body = "setup complete\n" + error + "\npytest summary: " + error + "\n"
        evidence = WorkflowJobLog(
            identity.repository, identity.head_sha, 414, 2, 715,
            "https://api.github.com/repos/owner/target/actions/jobs/715/logs",
            len(body.encode()), hashlib.sha256(body.encode()).hexdigest(), body,
        )
        dependency = Mock()
        dependency.normalized_package, dependency.proposed_version = "demo", "2.0"
        result = interpret_selected_job_log(identity, dependency, selection, evidence)
        self.assertEqual(result.state, "observed_keyword_error")
        self.assertEqual(result.error_line, 2)
        self.assertEqual(result.rejected_keyword, "option")

    def test_wrong_imported_run_identity_is_not_classified(self):
        identity, _, _ = source_controls.NativeSourceClientCompositionTests().controlled_transport()
        selection = SelectedCIJob(414, 2, 715)
        text = "TypeError: Client.__init__() got an unexpected keyword argument 'option'"
        bad = WorkflowJobLog(
            identity.repository, "c" * 40, 414, 2, 715,
            "https://api.github.com/repos/owner/target/actions/jobs/715/logs",
            len(text), hashlib.sha256(text.encode()).hexdigest(), text
        )
        from upgradepilot.dependency.change import DependencyVersionChange
        with self.assertRaises(ValueError):
            interpret_selected_job_log(identity, Mock(spec=DependencyVersionChange),
                                       selection, bad)

    def test_coordinates_cannot_be_supplied_outside_combined_profile(self):
        for bad in (
            ["owner/target", "1145", "--ci-job-id", "715"],
            ["owner/target", "1145", "--evidence-profile", "caller-signature-ci"],
        ):
            with self.subTest(bad=bad):
                with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                    main(bad)


if __name__ == "__main__":
    unittest.main()
