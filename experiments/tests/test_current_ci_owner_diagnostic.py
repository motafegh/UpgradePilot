"""Machinery proof on synthetic inputs; no exploratory frozen-case owner outputs."""

from __future__ import annotations

import base64
from copy import deepcopy
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

import requests

from experiments import current_ci_owner_diagnostic as diagnostic
from upgradepilot.github.api import GitHubResponseError

HEAD = "a" * 40
BASE = "b" * 40
WORKFLOW = """jobs:
  check:
    name: Check
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Test
        run: pytest
"""


def response(data, status=200):
    result = requests.Response()
    result.status_code = status
    result._content = diagnostic.json.dumps(data).encode()
    return result


def fixture(directory, *, steps="normal", workflow=WORKFLOW):
    directory.mkdir(parents=True, exist_ok=True)
    source = directory / "workflow.yml"
    source.write_text(workflow)
    manifest = {"case_id": "SYNTHETIC", "identity": {"repository": "demo/project", "pr_number": 7,
                "head_sha": HEAD, "base_sha": BASE},
                "selected_workflow": {"run_id": 10, "run_attempt": 1, "workflow_path": ".github/workflows/ci.yml"},
                "authoritative_workflow_source_artifact": "workflow.yml"}
    run = {"id": 10, "workflow_id": 20, "name": "CI", "event": "pull_request", "head_sha": HEAD,
           "status": "completed", "conclusion": "success", "run_attempt": 1}
    job = {"id": 30, "run_id": 10, "name": "Check", "status": "completed", "conclusion": "success"}
    job["steps"] = [{"number": 1, "name": "Checkout", "status": "completed", "conclusion": "skipped"},
                    {"number": 2, "name": "Test", "status": "completed", "conclusion": "skipped"}]
    if steps == "null":
        job["steps"] = None
    if steps == "empty":
        job["steps"] = []
    provider = {"selected_run": {key: value for key, value in run.items() if key != "workflow_id"},
                "exact_head_runs": [run], "jobs": [job]}
    provider_path = directory / "provider.json"
    diagnostic.write(provider_path, provider)
    return directory, manifest, provider_path, provider, provider_path, provider["jobs"]


def pr_data(head=HEAD):
    return {"number": 7, "title": "Synthetic", "state": "open", "merged": False,
            "user": {"login": "tester"}, "base": {"sha": BASE, "ref": "main"},
            "head": {"sha": head, "ref": "update"}, "changed_files": 1}


def fresh_session(inputs, *, bad_job_head=False):
    run = inputs[3]["exact_head_runs"][0]
    job = {**inputs[5][0], "head_sha": "c" * 40 if bad_job_head else HEAD}
    detail = {**run, "path": ".github/workflows/ci.yml"}
    contents = {"type": "file", "path": detail["path"], "encoding": "base64",
                "content": base64.b64encode((inputs[0] / "workflow.yml").read_bytes()).decode()}
    session = Mock()
    session.get.side_effect = [response(pr_data()), response({"total_count": 1, "workflow_runs": [run]}),
                               response({"total_count": 1, "jobs": [job]}), response(detail),
                               response(contents), response(pr_data())]
    return session


class RetainedProofTests(unittest.TestCase):
    def test_strict_refusal_precedes_labelled_projection_and_preserves_raw(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            inputs = fixture(root / "case")
            original = inputs[2].read_bytes()
            raw_copy = deepcopy(inputs[3])
            with patch.object(diagnostic, "ROOT", root), patch.object(diagnostic, "case_inputs", return_value=inputs):
                result = diagnostic.retained_case("synthetic")
            self.assertEqual(result["strict_admission"], "input_unavailable")
            self.assertIn("head_sha", result["jobs"][0]["strict"]["detail"])
            self.assertFalse(result["jobs"][0]["conditional_head_scope"]["provider_observation"])
            self.assertEqual(result["conditional_owner"]["state"], "correlated")
            self.assertEqual([row["basis"] for row in result["conditional_owner"]["step_execution"]], ["runtime_non_success"] * 2)
            self.assertEqual(inputs[3], raw_copy)
            self.assertEqual(inputs[2].read_bytes(), original)

    def test_null_and_empty_remain_distinct_and_missing_name_precedes_later_matrix(self):
        workflow = "jobs:\n  first:\n    steps:\n      - run: pytest\n  later:\n    strategy:\n      matrix:\n        py: [3.12]\n    steps:\n      - run: pytest\n"
        for shape, expected in (("null", "null"), ("empty", "empty_array")):
            with self.subTest(shape=shape), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                inputs = fixture(root / "case", steps=shape, workflow=workflow)
                with patch.object(diagnostic, "ROOT", root), patch.object(diagnostic, "case_inputs", return_value=inputs):
                    result = diagnostic.retained_case("synthetic")
                self.assertEqual(result["jobs"][0]["steps_shape"], expected)
                self.assertEqual(result["conditional_owner"]["reason"], "static_job_name_missing")

    def test_ambiguous_and_conflicting_join_refused(self):
        with tempfile.TemporaryDirectory() as temporary:
            provider = fixture(Path(temporary))[3]
            duplicate = deepcopy(provider)
            duplicate["exact_head_runs"] *= 2
            conflict = deepcopy(provider)
            conflict["selected_run"]["workflow_id"] = 99
            for candidate in (duplicate, conflict):
                with self.assertRaises(ValueError):
                    diagnostic.joined_run(candidate)

    def test_other_missing_fields_cannot_be_projected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            inputs = fixture(root / "case")
            del inputs[5][0]["name"]
            with patch.object(diagnostic, "ROOT", root), patch.object(diagnostic, "case_inputs", return_value=inputs):
                with self.assertRaisesRegex(ValueError, "more than"):
                    diagnostic.retained_case("synthetic")


class FreshProofTests(unittest.TestCase):
    def test_normal_clients_bind_attempt_head_source_and_recheck(self):
        with tempfile.TemporaryDirectory() as temporary:
            inputs = fixture(Path(temporary))
            session = fresh_session(inputs)
            with patch.object(diagnostic, "case_inputs", return_value=inputs):
                row = diagnostic.fresh_case("synthetic", session)
            self.assertEqual(row["state"], "completed")
            self.assertEqual(row["jobs"][0]["head_sha"], HEAD)
            self.assertEqual(row["owner"]["state"], "correlated")
            calls = session.get.call_args_list
            self.assertIn("/runs/10/attempts/1/jobs", calls[2].args[0])
            self.assertEqual(calls[1].kwargs["params"]["head_sha"], HEAD)
            self.assertEqual(calls[4].kwargs["params"]["ref"], HEAD)
            self.assertEqual(calls[0].args, calls[-1].args)

    def test_head_attempt_and_post_acquisition_drift_preserved(self):
        with tempfile.TemporaryDirectory() as temporary:
            inputs = fixture(Path(temporary))
            session = Mock()
            session.get.return_value = response(pr_data("c" * 40))
            with patch.object(diagnostic, "case_inputs", return_value=inputs):
                self.assertEqual(diagnostic.fresh_case("synthetic", session)["state"], "target_drift")
            self.assertEqual(session.get.call_count, 1)
            inputs[3]["exact_head_runs"][0]["run_attempt"] = 2
            session = fresh_session(inputs)
            with patch.object(diagnostic, "case_inputs", return_value=inputs):
                self.assertEqual(diagnostic.fresh_case("synthetic", session)["state"], "attempt_drift")
            self.assertEqual(session.get.call_count, 2)
            inputs[3]["exact_head_runs"][0]["run_attempt"] = 1
            session = fresh_session(inputs)
            replies = list(session.get.side_effect)
            replies[-1] = response(pr_data("c" * 40))
            session.get.side_effect = replies
            with patch.object(diagnostic, "case_inputs", return_value=inputs):
                self.assertEqual(diagnostic.fresh_case("synthetic", session)["state"], "target_drift_after_acquisition")

    def test_normal_product_job_head_validation_not_bypassed(self):
        with tempfile.TemporaryDirectory() as temporary:
            inputs = fixture(Path(temporary))
            session = fresh_session(inputs, bad_job_head=True)
            with patch.object(diagnostic, "case_inputs", return_value=inputs):
                with self.assertRaises(GitHubResponseError):
                    diagnostic.fresh_case("synthetic", session)
            self.assertEqual(session.get.call_count, 3)


class RecordingAndWatchdogTests(unittest.TestCase):
    def test_redirects_and_transport_failures_count_actual_sends(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            adapter = diagnostic.RecordingAdapter(directory / "private", directory / "public", "demo/project")
            session = diagnostic.GitHubPublicSession()
            session.mount("https://", adapter)
            redirect = requests.Response()
            redirect.status_code = 302
            redirect.raw = io.BytesIO(b"redirect")
            redirect.headers["Location"] = "https://api.github.com/repos/demo/project/pulls/8"
            final = requests.Response()
            final.status_code = 200
            final.raw = io.BytesIO(b"{}")
            replies = iter([redirect, final])
            def transport(request, **kwargs):
                reply = next(replies)
                reply.request = request  # A real Requests adapter binds this field.
                return reply
            with patch.object(diagnostic.HTTPAdapter, "send", side_effect=transport):
                self.assertEqual(session.get("https://api.github.com/repos/demo/project/pulls/7").content, b"{}")
            self.assertEqual(adapter.count, 2)
            request = requests.Request("GET", "https://api.github.com/repos/demo/project/pulls/7").prepare()
            with patch.object(diagnostic.HTTPAdapter, "send", side_effect=requests.Timeout("synthetic")):
                with self.assertRaises(requests.Timeout):
                    adapter.send(request)
            self.assertEqual(adapter.count, 3)
            self.assertEqual(adapter.receipts[-1]["state"], "transport_failure")
            self.assertEqual(len(list((directory / "private").glob("*.body"))), 2)

    def test_raw_entity_identity_safe_headers_scope_and_send_cap(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            adapter = diagnostic.RecordingAdapter(directory / "private", directory / "public", "demo/project", request_left=1)
            request = requests.Request("GET", "https://api.github.com/repos/demo/project/pulls/7").prepare()
            reply = requests.Response()
            reply.status_code = 200
            reply.raw = io.BytesIO(b'{ "head_sha": "a" }\n')
            reply.headers = {"X-RateLimit-Remaining": "50", "Set-Cookie": "private"}
            with patch.object(diagnostic.HTTPAdapter, "send", return_value=reply):
                returned = adapter.send(request)
            body = returned.content
            self.assertEqual(body, (directory / "private/response-01.body").read_bytes())
            self.assertEqual(adapter.receipts[0]["sha256"], diagnostic.digest(body))
            self.assertNotIn("set-cookie", adapter.receipts[0]["headers"])
            self.assertEqual((directory / "private/response-01.body").stat().st_mode & 0o777, 0o600)
            with self.assertRaises(diagnostic.DiagnosticLimit):
                adapter.send(request)
            request.headers["Authorization"] = "test"
            with self.assertRaises(diagnostic.DiagnosticLimit):
                adapter.send(request)
            self.assertEqual(adapter.count, 1)

    def test_body_limit_retains_failure_before_product_parsing(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            adapter = diagnostic.RecordingAdapter(directory / "private", directory / "public", "demo/project", body_left=3)
            request = requests.Request("GET", "https://api.github.com/repos/demo/project/pulls/7").prepare()
            reply = requests.Response()
            reply.status_code = 200
            reply.raw = io.BytesIO(b"too big")
            with patch.object(diagnostic.HTTPAdapter, "send", return_value=reply):
                with self.assertRaises(diagnostic.DiagnosticLimit):
                    adapter.send(request)
            self.assertEqual(diagnostic.load(directory / "public/receipts.json")[0]["state"], "body_limit")
            self.assertFalse((directory / "private").exists())

    def test_parent_watchdog_kills_and_preserves_partial_result(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "result.json"
            diagnostic.write(path, {"case_id": "synthetic", "partial": "preserved"})
            diagnostic.dispatch([sys.executable, "-c", "import time; time.sleep(5)"], path, 0.05)
            row = diagnostic.load(path)
            self.assertEqual(row["state"], "watchdog_cancelled")
            self.assertEqual(row["partial"], "preserved")

    def test_changed_freeze_and_offline_access_refused(self):
        with tempfile.TemporaryDirectory() as temporary:
            freeze = Path(temporary) / "freeze.json"
            diagnostic.write(freeze, {"files": {"fake": "old"}})
            with patch.object(diagnostic, "fingerprints", return_value={"fake": "new"}):
                with self.assertRaises(ValueError):
                    diagnostic.check_freeze(freeze)
            for event in ("socket.connect", "subprocess.Popen", "os.system"):
                with self.assertRaises(diagnostic.DiagnosticLimit):
                    diagnostic.block_offline(event, ())


if __name__ == "__main__":
    unittest.main()
