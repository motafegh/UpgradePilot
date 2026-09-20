"""Protect anonymous public GitHub acquisition at the actual request boundary.

These are deterministic tests: mocked investigations and prepared Requests objects do
not prove live GitHub reachability or the user's current proxy configuration.
"""

from __future__ import annotations

import io
import os
import unittest
from contextlib import redirect_stdout
from unittest.mock import Mock, patch

import requests
from requests import Request, Response
from requests.exceptions import Timeout

from upgradepilot.cli import build_parser, main
from upgradepilot.github.api import GitHubAcquisitionError, GitHubApiClient
from upgradepilot.github.auth_session import GitHubPublicSession


class GitHubAuthenticationCLITests(unittest.TestCase):
    def _invoke(self, argv: list[str]) -> tuple[int, str, Mock]:
        stdout = io.StringIO()
        with patch("upgradepilot.cli.investigate_public_pull_request") as investigate, patch(
            "upgradepilot.cli._print_investigation"
        ), redirect_stdout(stdout):
            status = main(argv)
        return status, stdout.getvalue(), investigate

    def test_default_is_anonymous_even_with_ambient_token(self) -> None:
        with patch.dict(os.environ, {"GITHUB_TOKEN": "unrelated-invalid-token"}):
            status, output, investigate = self._invoke(["example/project", "7"])

        self.assertEqual(status, 0)
        self.assertEqual(output, "")
        investigate.assert_called_once_with("example/project", 7, token=None)

    def test_explicit_env_token_is_passed_without_printing_secret(self) -> None:
        with patch.dict(os.environ, {"GITHUB_TOKEN": "synthetic-token"}):
            status, output, investigate = self._invoke(
                ["example/project", "7", "--github-auth", "token-env"]
            )

        self.assertEqual(status, 0)
        self.assertNotIn("synthetic-token", output)
        investigate.assert_called_once_with("example/project", 7, token="synthetic-token")

    def test_missing_or_empty_explicit_token_fails_before_investigation(self) -> None:
        for ambient in ({}, {"GITHUB_TOKEN": ""}):
            with self.subTest(ambient=ambient), patch.dict(os.environ, ambient, clear=True):
                status, output, investigate = self._invoke(
                    ["example/project", "7", "--github-auth", "token-env"]
                )
                self.assertEqual(status, 2)
                self.assertIn("requires GITHUB_TOKEN", output)
                investigate.assert_not_called()

    def test_help_describes_modes_not_secret_values(self) -> None:
        help_text = build_parser().format_help()
        self.assertIn("--github-auth", help_text)
        self.assertIn("anonymous", help_text)
        self.assertIn("token-env", help_text)
        self.assertNotIn("Bearer", help_text)


class GitHubPreparedRequestTests(unittest.TestCase):
    @staticmethod
    def _prepared(*, token: str | None = None) -> tuple[GitHubPublicSession, requests.PreparedRequest]:
        client = GitHubApiClient(token=token)
        session = client._session
        assert isinstance(session, GitHubPublicSession)
        prepared = session.prepare_request(
            Request("GET", "https://api.github.com/repos/example/project", headers=client._headers)
        )
        return session, prepared

    @staticmethod
    def _redirect(session: GitHubPublicSession, previous: requests.PreparedRequest, url: str) -> requests.PreparedRequest:
        next_request = previous.copy()
        next_request.url = url
        response = Response()
        response.status_code = 302
        response.request = previous
        session.rebuild_auth(next_request, response)
        return next_request

    def test_anonymous_prepared_request_ignores_ambient_netrc_and_preserves_proxy_config(self) -> None:
        with patch("requests.sessions.get_netrc_auth", return_value=("ambient", "secret")) as netrc:
            session, initial = self._prepared()
            redirected = self._redirect(session, initial, "https://api.github.com/next")

        self.assertTrue(session.trust_env)
        self.assertNotIn("Authorization", initial.headers)
        self.assertNotIn("Authorization", redirected.headers)
        netrc.assert_not_called()

    def test_explicit_bearer_survives_same_origin_redirect_but_not_cross_origin(self) -> None:
        with patch("requests.sessions.get_netrc_auth", return_value=("ambient", "secret")) as netrc:
            session, initial = self._prepared(token="synthetic-token")
            same_origin = self._redirect(session, initial, "https://api.github.com/next")
            cross_origin = self._redirect(session, initial, "https://other.example/next")

        self.assertEqual(initial.headers["Authorization"], "Bearer synthetic-token")
        self.assertEqual(same_origin.headers["Authorization"], "Bearer synthetic-token")
        self.assertNotIn("Authorization", cross_origin.headers)
        netrc.assert_not_called()

    def test_real_gitHub_client_uses_isolated_default_but_preserves_injected_session(self) -> None:
        self.assertIsInstance(GitHubApiClient()._session, GitHubPublicSession)
        injected = Mock()
        self.assertIs(GitHubApiClient(session=injected)._session, injected)

    def test_auth_failure_remains_distinct_from_missing_source_and_transport(self) -> None:
        client = GitHubApiClient()
        for status, reason in ((401, "http_error"), (404, "not_found_or_inaccessible")):
            with self.subTest(status=status):
                response = Response()
                response.status_code = status
                with self.assertRaises(GitHubAcquisitionError) as caught:
                    client._raise_for_status(response, resource="public PR")
                self.assertEqual(caught.exception.reason, reason)
                self.assertEqual(caught.exception.status_code, status)

        session = Mock()
        session.get.side_effect = Timeout("synthetic timeout")
        with self.assertRaises(GitHubAcquisitionError) as caught:
            GitHubApiClient(session=session)._get("https://api.github.com/test", resource="PR")
        self.assertEqual(caught.exception.reason, "timeout")
        self.assertIsNone(caught.exception.status_code)


if __name__ == "__main__":
    unittest.main()
