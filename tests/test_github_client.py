"""Deterministic tests for public-PR and changed-file acquisition boundaries.

Mocks replace live HTTP collaborators so each test can isolate one contract,
failure category, or completeness invariant without depending on the network.
"""

from __future__ import annotations

import unittest
from unittest.mock import Mock

from upgradepilot.github_client import (
    GitHubAcquisitionError,
    GitHubReadClient,
    GitHubResponseError,
    PullRequestIdentity,
)


def _identity(*, changed_files: int) -> PullRequestIdentity:
    """Build a trusted PR identity while varying only the expected file count."""

    return PullRequestIdentity(
        repository="googlefonts/glyphsLib",
        number=1145,
        title="Bump pytest from 9.0.2 to 9.0.3",
        state="closed",
        merged=True,
        author="dependabot[bot]",
        base_ref="main",
        base_sha="044f19e4b1437bfc4343592486f4e3c6040306d9",
        head_ref="dependabot/pip/pytest-9.0.3",
        head_sha="f3cda8a94600e58d27f1bc17c99b7693718b6350",
        changed_files=changed_files,
    )


def _changed_file(index: int) -> dict[str, object]:
    """Build one raw GitHub-like file object for pagination tests."""

    return {
        "filename": f"requirements-{index}.txt",
        "status": "modified",
        "additions": 1,
        "deletions": 1,
        "changes": 2,
        "patch": "-pytest==9.0.2\n+pytest==9.0.3",
    }


class GitHubReadClientTests(unittest.TestCase):
    """Protect acquisition, validation, and completeness behavior."""

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
        # Injecting the session keeps this test deterministic and lets it inspect
        # the exact request contract without issuing network traffic.
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

    def test_get_changed_files_builds_validated_records(self) -> None:
        response = Mock()
        response.status_code = 200
        response.json.return_value = [_changed_file(1)]
        session = Mock()
        session.get.return_value = response

        records = GitHubReadClient(session=session).get_changed_files(
            _identity(changed_files=1)
        )

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].filename, "requirements-1.txt")
        _, kwargs = session.get.call_args
        self.assertEqual(kwargs["params"], {"per_page": 100, "page": 1})

    def test_get_changed_files_acquires_all_pages(self) -> None:
        first = Mock()
        first.status_code = 200
        first.json.return_value = [_changed_file(index) for index in range(100)]
        second = Mock()
        second.status_code = 200
        second.json.return_value = [_changed_file(100)]
        session = Mock()
        # ``side_effect`` returns one controlled response per successive GET.
        session.get.side_effect = [first, second]

        records = GitHubReadClient(session=session).get_changed_files(
            _identity(changed_files=101)
        )

        self.assertEqual(len(records), 101)
        pages = [call.kwargs["params"]["page"] for call in session.get.call_args_list]
        self.assertEqual(pages, [1, 2])

    def test_get_changed_files_rejects_count_disagreement(self) -> None:
        response = Mock()
        response.status_code = 200
        response.json.return_value = [_changed_file(1)]
        session = Mock()
        session.get.return_value = response

        # The metadata count is the expected completeness boundary; one valid
        # record cannot satisfy an identity that declared two changed files.
        with self.assertRaises(GitHubResponseError) as caught:
            GitHubReadClient(session=session).get_changed_files(
                _identity(changed_files=2)
            )

        self.assertIn("expected 2 records but acquired 1", str(caught.exception))

    def test_get_changed_files_rejects_non_array_success(self) -> None:
        response = Mock()
        response.status_code = 200
        response.json.return_value = {"filename": "requirements-dev.txt"}
        session = Mock()
        session.get.return_value = response

        with self.assertRaises(GitHubResponseError):
            GitHubReadClient(session=session).get_changed_files(
                _identity(changed_files=1)
            )


if __name__ == "__main__":
    unittest.main()
