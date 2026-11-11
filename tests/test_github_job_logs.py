"""Bounded, provenance-bound job-log acquisition without executing target code."""

from __future__ import annotations

import hashlib
import traceback
import unittest
from dataclasses import replace
from unittest.mock import Mock

from requests.exceptions import Timeout

from upgradepilot.github.actions import (
    GitHubActionsClient, WorkflowJob, WorkflowRun,
)
from upgradepilot.github.api import GitHubAcquisitionError, GitHubResponseError
from upgradepilot.github.job_log_transport import (
    MAX_JOB_LOG_BYTES, download_bounded_job_log,
)
from upgradepilot.github.pull_request import PullRequestIdentity

SHA = "a" * 40
GOOD_LOCATION = (
    "https://productionresultssa31.blob.core.windows.net/actions-results/"
    "job.txt?sig=SECRET_SIGNED_URL_NOT_TO_PRINT"
)


def identity():
    return PullRequestIdentity(
        repository="example/target", number=11, title="Bump httpx", state="open",
        merged=False, author="dependabot[bot]", base_ref="main",
        base_sha="b" * 40, head_ref="dependabot/httpx", head_sha=SHA, changed_files=1,
    )


def run():
    return WorkflowRun(100, 200, "CI", "pull_request", SHA, "completed", "failure", 2)


def job():
    return WorkflowJob(300, 100, "backend", SHA, "completed", "failure", ())


def response(status, *, headers=None, parts=()):
    r = Mock()
    r.status_code = status
    r.headers = headers or {}
    r.iter_content.return_value = iter(parts)
    return r


class WorkflowJobLogTests(unittest.TestCase):
    def test_exact_failed_job_log_uses_token_only_for_api_and_preserves_identity_digest(self):
        src = b"2026-11-02 test log\nE TypeError: unexpected keyword argument 'app'\n"
        first = response(302, headers={"Location": GOOD_LOCATION})
        second = response(200, headers={"Content-Length": str(len(src))}, parts=(src,))
        session = Mock()
        session.get.side_effect = (first, second)

        observed = GitHubActionsClient(
            session=session, token="SYNTHETIC_PERSONAL_TOKEN"
        ).get_failed_workflow_job_log(identity(), run(), job(), max_bytes=1024)

        self.assertEqual((observed.run_id, observed.run_attempt, observed.job_id), (100, 2, 300))
        self.assertEqual((observed.repository, observed.head_sha), ("example/target", SHA))
        self.assertEqual((observed.utf8_bytes, observed.sha256), (len(src), hashlib.sha256(src).hexdigest()))
        self.assertEqual(observed.text, src.decode())
        self.assertEqual(observed.source_url,
            "https://api.github.com/repos/example/target/actions/jobs/300/logs")
        self.assertNotIn("TypeError", repr(observed))
        self.assertNotIn("SECRET_SIGNED_URL", repr(observed))
        self.assertEqual(session.get.call_count, 2)
        (url1,), k1 = session.get.call_args_list[0]
        (url2,), k2 = session.get.call_args_list[1]
        self.assertEqual(url1, observed.source_url)
        self.assertEqual(url2, GOOD_LOCATION)
        self.assertEqual(k1["headers"]["Authorization"], "Bearer SYNTHETIC_PERSONAL_TOKEN")
        self.assertNotIn("Authorization", k2["headers"])
        self.assertEqual(k2["headers"]["Accept"], "text/plain")
        self.assertFalse(k1["allow_redirects"])
        self.assertFalse(k2["allow_redirects"])
        self.assertTrue(k1["stream"])
        self.assertTrue(k2["stream"])
        first.close.assert_called_once()
        second.close.assert_called_once()

    def test_anonymous_stays_anonymous_in_both_hops(self):
        session = Mock()
        session.get.side_effect = (
            response(302, headers={"Location": GOOD_LOCATION}),
            response(200, parts=(b"some log",)),
        )
        result = GitHubActionsClient(session=session).get_failed_workflow_job_log(
            identity(), run(), job()
        )
        self.assertEqual(result.text, "some log")
        self.assertTrue(all("Authorization" not in call.kwargs["headers"]
                            for call in session.get.call_args_list))

    def test_refuses_wrong_identity_and_non_failed_jobs_before_network(self):
        invalid = [
            (replace(run(), head_sha="c" * 40), job()),
            (replace(run(), run_attempt=0), job()),
            (replace(run(), event="push"), job()),
            (run(), replace(job(), run_id=101)),
            (run(), replace(job(), head_sha="c" * 40)),
            (run(), replace(job(), status="queued")),
            (run(), replace(job(), conclusion="success")),
        ]
        for r, j in invalid:
            with self.subTest(run=r, job=j):
                session = Mock()
                with self.assertRaises(ValueError):
                    GitHubActionsClient(session=session).get_failed_workflow_job_log(
                        identity(), r, j
                    )
                session.get.assert_not_called()

    def test_rejects_unapproved_or_unsafe_redirects_without_second_fetch(self):
        for bad in (
            "http://productionresultssa31.blob.core.windows.net/log",
            "https://evil.example/log",
            "https://blob.core.windows.net.attacker.example/log",
            "https://user:password@productionresultssa31.blob.core.windows.net/log",
            "https://productionresultssa31.blob.core.windows.net:444/log",
            "//productionresultssa31.blob.core.windows.net/log",
            "https://productionresultssa31.blob.core.windows.net/log#fragment",
            None,
        ):
            with self.subTest(bad=bad):
                session = Mock()
                session.get.return_value = response(302, headers={"Location": bad} if bad else {})
                with self.assertRaises(GitHubResponseError) as caught:
                    GitHubActionsClient(session=session, token="SECRET").get_failed_workflow_job_log(
                        identity(), run(), job()
                    )
                self.assertNotIn("SECRET", str(caught.exception))
                self.assertEqual(session.get.call_count, 1)

    def test_refuses_oversized_body_before_or_during_streaming(self):
        cases = [
            (response(200, headers={"Content-Length": "500"}, parts=(b"x",)), 8),
            (response(200, parts=(b"abcd", b"efgh", b"i")), 8),
        ]
        for body, cap in cases:
            with self.subTest(body=body):
                session = Mock()
                session.get.return_value = body
                with self.assertRaises(GitHubAcquisitionError) as caught:
                    download_bounded_job_log(
                        session, api_url="https://api.github.com/job-log",
                        github_headers={"User-Agent": "test"}, timeout=(2, 2),
                        max_bytes=cap,
                    )
                self.assertEqual(caught.exception.reason, "response_too_large")
                body.close.assert_called_once()
        with self.assertRaises(ValueError):
            download_bounded_job_log(Mock(), api_url="https://api.github.com/",
                github_headers={"User-Agent": "test"}, timeout=(2, 2),
                max_bytes=MAX_JOB_LOG_BYTES + 1)

    def test_preserves_access_refusal_transport_timeout_and_invalid_text(self):
        for code, expected in ((403, "forbidden_or_rate_limited"), (404, "not_found_or_inaccessible")):
            with self.subTest(code=code):
                session = Mock()
                session.get.return_value = response(code)
                with self.assertRaises(GitHubAcquisitionError) as caught:
                    GitHubActionsClient(session=session).get_failed_workflow_job_log(
                        identity(), run(), job()
                    )
                self.assertEqual(caught.exception.reason, expected)
        session = Mock()
        session.get.side_effect = Timeout("SIGNED_URL_SHOULD_NOT_LEAK")
        with self.assertRaises(GitHubAcquisitionError) as caught:
            GitHubActionsClient(session=session).get_failed_workflow_job_log(
                identity(), run(), job()
            )
        self.assertEqual(caught.exception.reason, "timeout")
        self.assertNotIn("SIGNED_URL", str(caught.exception))
        self.assertNotIn(
            "SIGNED_URL",
            "".join(traceback.format_exception(caught.exception)),
        )

        session = Mock()
        session.get.return_value = response(200, parts=(b"\xff",))
        with self.assertRaises(GitHubResponseError):
            GitHubActionsClient(session=session).get_failed_workflow_job_log(
                identity(), run(), job()
            )

    def test_refuses_second_redirect_and_empty_log(self):
        for body in (response(302, headers={"Location": GOOD_LOCATION}),
                     response(200, parts=())):
            session = Mock()
            session.get.side_effect = (
                response(302, headers={"Location": GOOD_LOCATION}), body
            )
            with self.assertRaises((GitHubAcquisitionError, GitHubResponseError)):
                GitHubActionsClient(session=session).get_failed_workflow_job_log(
                    identity(), run(), job()
                )
            self.assertEqual(session.get.call_count, 2)


if __name__ == "__main__":
    unittest.main()
