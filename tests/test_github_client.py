"""Tests for the first read-only GitHub acquisition behavior."""

from __future__ import annotations

import unittest
from unittest.mock import Mock

from upgradepilot.github_client import (
    GitHubAcquisitionError,
    GitHubReadClient,
)


class GitHubReadClientTests(unittest.TestCase):
    def test_get_pull_request_builds_exact_identity(self) -> None:
        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "number": 1145,
            "title": "Bump pytest from 9.0.2 to 9.0.3",
            "state": "closed",
            "merged": True,
            "user": {"login": "dependabot[bot]"},
            "base": {
                "ref": "main",
                "sha": "044f19e4b1437bfc4343592486f4e3c6040306d9",
            },
            "head": {
                "ref": "dependabot/pip/pytest-9.0.3",
                "sha": "f3cda8a94600e58d27f1bc17c99b7693718b6350",
            },
            "changed_files": 1,
        }
        session = Mock()
        session.get.return_value = response

        client = GitHubReadClient(session=session)
        identity = client.get_pull_request("googlefonts/glyphsLib", 1145)

        self.assertEqual(identity.number, 1145)
        self.assertEqual(
            identity.head_sha,
            "f3cda8a94600e58d27f1bc17c99b7693718b6350",
        )
        session.get.assert_called_once()
        _, kwargs = session.get.call_args
        self.assertEqual(kwargs["timeout"], (3.05, 15.0))
        self.assertNotIn("Authorization", kwargs["headers"])

    def test_404_preserves_nonexistence_or_access_ambiguity(self) -> None:
        response = Mock()
        response.status_code = 404
        session = Mock()
        session.get.return_value = response

        client = GitHubReadClient(session=session)

        with self.assertRaises(GitHubAcquisitionError) as caught:
            client.get_pull_request("googlefonts/glyphsLib", 999999)

        self.assertEqual(caught.exception.reason, "not_found_or_inaccessible")
        self.assertEqual(caught.exception.status_code, 404)


if __name__ == "__main__":
    unittest.main()
