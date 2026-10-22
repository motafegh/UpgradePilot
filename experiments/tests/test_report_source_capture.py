"""Diagnostic input retention/normal composition, not independent report utility."""

import gzip
import json
import os
import tempfile
import time
import unittest
from dataclasses import asdict, replace
from datetime import UTC, datetime
from hashlib import sha256
from io import BytesIO
from pathlib import Path
from unittest.mock import patch
from urllib.parse import urlsplit

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ChunkedEncodingError, Timeout
from test_github_client import _changed_file, _identity, _pull_request_payload
from test_pypi_client import _release_payload
from urllib3.response import HTTPResponse

from tools.capture_report_sources import (
    CaptureLimits,
    CaptureStopped,
    HTTPSourceCapture,
    capture_normal_report,
    main,
)
from upgradepilot.github.auth_session import GitHubPublicSession
from upgradepilot.github.pull_request import GitHubPullRequestClient
from upgradepilot.investigation import investigate_public_pull_request
from upgradepilot.pypi.release import PyPIReleaseClient
from upgradepilot.report_file import read_report
from upgradepilot.report_projection import project_investigation_report

NOW = datetime(2026, 10, 22, tzinfo=UTC)
LIMITS = CaptureLimits(30, 1_000_000, 4_000_000, 10)
IDENTITY = _identity(changed_files=1)


def response(request, payload, status=200, headers=None, raw=None):
    result = requests.Response()
    result.request, result.url, result.status_code = request, request.url, status
    body = payload if isinstance(payload, bytes) else json.dumps(payload).encode()
    result.raw = raw or BytesIO(body)
    result.headers.update(headers or {})
    return result


def session():
    result = GitHubPublicSession()
    result.trust_env = False
    return result


def normal_transport(adapter, request, **kwargs):
    """Controlled actual HTTP bodies, not hand-assembled application/report records."""
    path = urlsplit(request.url).path
    if path.endswith("/pulls/1145"):
        return response(request, _pull_request_payload(IDENTITY))
    if path.endswith("/pulls/1145/files"):
        return response(request, [_changed_file(0, filename="requirements.txt")])
    if path.endswith("/actions/runs"):
        return response(request, {"total_count": 0, "workflow_runs": []})
    if request.url.startswith("https://pypi.org/"):
        return response(request, {}, status=404)
    raise AssertionError(f"Unexpected controlled endpoint: {request.url}")


def contract():
    return {
        "expected_identity": {
            "repository": IDENTITY.repository,
            "pull_number": str(IDENTITY.number),
            "base_sha": IDENTITY.base_sha,
            "head_sha": IDENTITY.head_sha,
            "package": "pytest",
            "old_version": "9.0.2",
            "proposed_version": "9.0.3",
        },
        "limits": asdict(LIMITS),
    }


class ReportSourceCaptureTests(unittest.TestCase):
    def test_normal_application_report_parity_and_private_source_hashes(self):
        with (
            tempfile.TemporaryDirectory() as directory,
            patch.dict(os.environ, {"NETRC": os.devnull}),
            patch.object(HTTPAdapter, "send", normal_transport),
        ):
            ordinary = project_investigation_report(
                investigate_public_pull_request(IDENTITY.repository, IDENTITY.number)
            )
            target = Path(directory) / "capture"
            receipt = capture_normal_report(contract(), target)
            self.assertEqual(receipt["outcome"], "normal_report_captured")
            retained = read_report(target / "report.json")
            self.assertEqual(
                replace(
                    retained,
                    report_id=ordinary.report_id,
                    generated_at=ordinary.generated_at,
                ),
                ordinary,
            )
            index = json.loads((target / "sources/index.json").read_text())
            self.assertGreater(len(index["requests"]), 3)
            self.assertEqual(index["format"], "upgradepilot.diagnostic-http-sources/1")
            self.assertEqual(target.stat().st_mode & 0o777, 0o700)
            for row in index["requests"]:
                body = target / "sources" / row["body"]
                self.assertEqual(
                    sha256(body.read_bytes()).hexdigest(), row["body_sha256"]
                )
                self.assertEqual(body.stat().st_mode & 0o777, 0o600)
                self.assertIn(row["state"], {"body_complete", "body_not_consumed"})
            self.assertEqual((target / "report.json").stat().st_mode & 0o777, 0o600)
            self.assertEqual(
                receipt["report_sha256"],
                sha256((target / "report.json").read_bytes()).hexdigest(),
            )
            with self.assertRaises(FileExistsError):
                capture_normal_report(contract(), target)

    def test_public_github_and_streamed_pypi_clients_keep_native_results(self):
        def send(adapter, request, **kwargs):
            if request.url.startswith("https://api.github.com"):
                return response(request, _pull_request_payload(IDENTITY))
            body = json.dumps(_release_payload()).encode()
            raw = HTTPResponse(
                body=BytesIO(gzip.compress(body)),
                headers={"Content-Encoding": "gzip"},
                preload_content=False,
            )
            return response(request, b"", raw=raw, headers={"Content-Encoding": "gzip"})

        def read_both():
            with session() as client:
                github = GitHubPullRequestClient(session=client).get_pull_request(
                    IDENTITY.repository, IDENTITY.number
                )
                pypi = PyPIReleaseClient(session=client, now=lambda: NOW).get_release(
                    "friendly-bard", "2.4.0"
                )
            return github, pypi

        with (
            tempfile.TemporaryDirectory() as directory,
            patch.object(HTTPAdapter, "send", send),
        ):
            ordinary = read_both()
            capture = HTTPSourceCapture(Path(directory) / "sources", LIMITS)
            with capture.observe():
                recorded = read_both()
            self.assertEqual(recorded, ordinary)
            self.assertEqual([r["state"] for r in capture.rows], ["body_complete"] * 2)
            self.assertEqual(
                (capture.directory / "0002.body").read_bytes(),
                json.dumps(_release_payload()).encode(),
            )
            for row in capture.rows:
                self.assertEqual(
                    row["body_bytes"], (capture.directory / row["body"]).stat().st_size
                )

    def test_stream_failure_stays_body_stage_and_retains_prefix(self):
        class BrokenRaw:
            def stream(self, chunk_size, decode_content=True):
                yield b'{"info":'
                raise ChunkedEncodingError("controlled incomplete stream")

            def close(self):
                pass

        def send(adapter, request, **kwargs):
            return response(request, b"", raw=BrokenRaw())

        def acquire():
            with session() as client:
                return PyPIReleaseClient(session=client).get_release("demo", "1.0")

        with (
            tempfile.TemporaryDirectory() as directory,
            patch.object(HTTPAdapter, "send", send),
        ):
            ordinary = acquire()
            capture = HTTPSourceCapture(Path(directory) / "sources", LIMITS)
            with capture.observe():
                recorded = acquire()
            self.assertEqual(recorded, ordinary)
            self.assertIn("ended before its complete body", recorded.detail)
            self.assertEqual(capture.rows[0]["state"], "body_failed")
            self.assertEqual(
                (capture.directory / "0001.body").read_bytes(), b'{"info":'
            )

    def test_status_only_and_malformed_json_do_not_become_success(self):
        for status, payload in ((404, b"unread body"), (200, b"not json")):
            with (
                self.subTest(status=status),
                tempfile.TemporaryDirectory() as directory,
            ):

                def send(adapter, request, payload=payload, status=status, **kwargs):
                    return response(request, payload, status)

                with patch.object(HTTPAdapter, "send", send), session() as client:
                    ordinary = PyPIReleaseClient(session=client).get_release(
                        "demo", "1.0"
                    )
                    capture = HTTPSourceCapture(Path(directory) / "sources", LIMITS)
                    with capture.observe():
                        recorded = PyPIReleaseClient(session=client).get_release(
                            "demo", "1.0"
                        )
                self.assertEqual(recorded, ordinary)
                self.assertEqual(
                    capture.rows[0]["state"],
                    "body_not_consumed" if status == 404 else "body_complete",
                )
                self.assertNotEqual(recorded.state, "available")

    def test_denied_post_auth_destination_and_redirect_never_reach_transport(self):
        cases = [
            ("POST", "https://api.github.com/repos/example/demo", {}),
            (
                "GET",
                "https://api.github.com/repos/example/demo",
                {"Authorization": "Bearer test-only"},
            ),
            ("GET", "https://example.invalid/", {}),
        ]
        for method, url, headers in cases:
            with (
                self.subTest(method=method, url=url),
                tempfile.TemporaryDirectory() as directory,
            ):
                capture = HTTPSourceCapture(Path(directory) / "sources", LIMITS)
                with (
                    patch.object(HTTPAdapter, "send") as transport,
                    session() as client,
                ):
                    with capture.observe(), self.assertRaises(CaptureStopped):
                        client.request(method, url, headers=headers)
                    transport.assert_not_called()
                self.assertEqual(capture.rows, [])

        with tempfile.TemporaryDirectory() as directory:
            capture = HTTPSourceCapture(Path(directory) / "sources", LIMITS)
            with (
                patch.object(
                    HTTPAdapter,
                    "send",
                    side_effect=lambda adapter, request, **kwargs: response(
                        request, b"", 302, {"Location": "https://example.invalid/"}
                    ),
                ) as transport,
                session() as client,
            ):
                with capture.observe(), self.assertRaises(CaptureStopped):
                    client.get("https://api.github.com/repos/example/demo")
                self.assertEqual(transport.call_count, 1)

    def test_byte_request_and_elapsed_limits_preserve_partial_evidence(self):
        with (
            tempfile.TemporaryDirectory() as directory,
            patch.object(
                HTTPAdapter,
                "send",
                side_effect=lambda adapter, request, **kwargs: response(
                    request, b"0123456789"
                ),
            ),
        ):
            capture = HTTPSourceCapture(
                Path(directory) / "bytes", replace(LIMITS, max_body_bytes=5)
            )
            with (
                session() as client,
                capture.observe(),
                self.assertRaises(CaptureStopped),
            ):
                client.get("https://api.github.com/repos/example/demo")
            self.assertEqual((capture.directory / "0001.body").read_bytes(), b"01234")
            self.assertEqual(capture.rows[0]["state"], "capture_stopped")

            capture = HTTPSourceCapture(
                Path(directory) / "requests", replace(LIMITS, max_requests=1)
            )
            with session() as client, capture.observe():
                client.get("https://api.github.com/repos/example/demo")
                with self.assertRaises(CaptureStopped):
                    client.get("https://api.github.com/repos/example/other")
            self.assertEqual(len(capture.rows), 1)

            capture = HTTPSourceCapture(
                Path(directory) / "total",
                replace(LIMITS, max_body_bytes=20, max_total_body_bytes=15),
            )
            with session() as client, capture.observe():
                client.get("https://api.github.com/repos/example/demo")
                with self.assertRaises(CaptureStopped):
                    client.get("https://api.github.com/repos/example/other")
            self.assertEqual(capture.total_bytes, 15)
            self.assertEqual((capture.directory / "0002.body").read_bytes(), b"01234")

            capture = HTTPSourceCapture(Path(directory) / "elapsed", LIMITS)
            capture.started -= LIMITS.max_elapsed_seconds + 1
            with (
                session() as client,
                capture.observe(),
                self.assertRaises(CaptureStopped),
            ):
                client.get("https://api.github.com/repos/example/demo")
            self.assertEqual(capture.rows, [])

    def test_model_guard_withholds_report_and_cannot_become_provider_uncertainty(self):
        def model_branch(*args, **kwargs):
            try:
                with session() as client:
                    client.post("http://127.0.0.1:18080/v1/chat/completions", json={})
            except Exception:  # noqa: BLE001 -- reproduce the model owner's broad provider handler
                self.fail("Diagnostic model guard was swallowed as a provider problem")

        with (
            tempfile.TemporaryDirectory() as directory,
            patch(
                "tools.capture_report_sources.investigate_public_pull_request",
                model_branch,
            ),
            patch.object(HTTPAdapter, "send") as transport,
        ):
            target = Path(directory) / "capture"
            receipt = capture_normal_report(contract(), target)
            self.assertEqual(receipt["outcome"], "capture_stopped")
            self.assertEqual(receipt["reason"], "non_get_or_model_call_not_admitted")
            self.assertFalse((target / "report.json").exists())
            transport.assert_not_called()

    def test_identity_drift_and_transport_failure_are_not_semantic_abstention(self):
        with (
            tempfile.TemporaryDirectory() as directory,
            patch.dict(os.environ, {"NETRC": os.devnull}),
            patch.object(HTTPAdapter, "send", normal_transport),
        ):
            changed = contract()
            changed["expected_identity"]["head_sha"] = "e" * 40
            target = Path(directory) / "mismatch"
            receipt = capture_normal_report(changed, target)
            self.assertEqual(receipt["outcome"], "not_comparable")
            self.assertFalse((target / "report.json").exists())

        with (
            tempfile.TemporaryDirectory() as directory,
            patch.object(HTTPAdapter, "send", side_effect=Timeout("controlled")),
        ):
            target = Path(directory) / "failed"
            receipt = capture_normal_report(contract(), target)
            self.assertEqual(receipt["outcome"], "investigation_or_capture_failed")
            self.assertFalse((target / "report.json").exists())
            index = json.loads((target / "sources/index.json").read_text())
            self.assertEqual(index["requests"][0]["state"], "request_failed")

    def test_cli_deadline_interrupts_an_operation_that_yields_no_chunks(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {}):
            path = Path(directory) / "contract.json"
            value = contract()
            value["limits"]["max_elapsed_seconds"] = 1
            path.write_text(json.dumps(value))
            target = Path(directory) / "capture"
            with patch(
                "tools.capture_report_sources.investigate_public_pull_request",
                side_effect=lambda *args: time.sleep(5),
            ):
                started = time.monotonic()
                code = main(["--contract", str(path), "--output", str(target)])
            self.assertEqual(code, 2)
            self.assertLess(time.monotonic() - started, 3)
            self.assertEqual(
                json.loads((target / "capture.json").read_text())["reason"],
                "elapsed_limit",
            )
            self.assertFalse((target / "report.json").exists())


if __name__ == "__main__":
    unittest.main()
