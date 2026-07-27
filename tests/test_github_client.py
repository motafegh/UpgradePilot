"""Test the PR and changed-file acquisition boundary without live GitHub access.

Purpose of this test file
-------------------------
The production code in ``github_client.py`` combines local input validation,
shared HTTP behavior from ``github_api.py``, PR-field parsing, and changed-file
pagination. These tests isolate that boundary by replacing the real Requests
``Session`` with ``Mock`` objects.

What these tests prove
----------------------
* successful PR JSON becomes an exact ``PullRequestIdentity``;
* the client sends the expected timeout, headers, and pagination parameters;
* GitHub's ambiguous 404 becomes the correct acquisition category;
* every changed-file page is requested and converted into validated records;
* count disagreement and wrong top-level JSON shape are rejected.

What they do not prove
----------------------
No real network request is made. Therefore these tests do not prove current GitHub
availability, credentials, rate limits, or compatibility with an unmocked external
response. They prove how the client behaves for the controlled responses supplied.
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
    """Build a trusted PR identity while varying only the expected file count.

    The ``*`` makes ``changed_files`` keyword-only, so each test states explicitly
    which completeness target it is creating. All unrelated identity fields remain
    fixed, allowing a test failure to be attributed to the varied count.
    """

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
    """Build one raw GitHub-like changed-file object for pagination tests.

    The return value is intentionally a dictionary rather than ``ChangedFile``.
    Production parsing must still cross the external-JSON trust boundary and create
    the domain record itself.
    """

    return {
        "filename": f"requirements-{index}.txt",
        "status": "modified",
        "additions": 1,
        "deletions": 1,
        "changes": 2,
        "patch": "-pytest==9.0.2\n+pytest==9.0.3",
    }


class GitHubReadClientTests(unittest.TestCase):
    """Protect PR identity, request construction, pagination, and completeness."""

    def test_get_pull_request_builds_exact_identity(self) -> None:
        """A valid response should become identity and use the shared request contract."""

        # Arrange: the response mock imitates the small Requests ``Response`` surface
        # used by production code: ``status_code`` and the ``json()`` method.
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

        # Injecting the session is dependency injection: production normally creates a
        # real Requests session, while this test supplies a controllable collaborator.
        session = Mock()
        session.get.return_value = response

        # Act: the public method performs input validation, request construction,
        # top-level JSON validation, and PR-specific field parsing.
        client = GitHubReadClient(session=session)
        identity = client.get_pull_request("googlefonts/glyphsLib", 1145)

        # Assert both the produced domain identity and selected request details. This
        # protects behavior across the client and inherited transport boundary.
        self.assertEqual(identity.number, 1145)
        self.assertEqual(
            identity.head_sha,
            "f3cda8a94600e58d27f1bc17c99b7693718b6350",
        )
        session.get.assert_called_once()

        # ``call_args`` stores positional arguments separately from keyword arguments.
        # The underscore intentionally ignores the positional URL because this test
        # focuses here on timeout and anonymous-header behavior.
        _, kwargs = session.get.call_args
        self.assertEqual(kwargs["timeout"], (3.05, 15.0))
        self.assertNotIn("Authorization", kwargs["headers"])

    def test_404_preserves_nonexistence_or_access_ambiguity(self) -> None:
        """HTTP 404 must retain GitHub's absence-versus-access ambiguity."""

        response = Mock()
        response.status_code = 404
        session = Mock()
        session.get.return_value = response

        client = GitHubReadClient(session=session)

        # ``assertRaises`` is a context manager. The raised exception is captured in
        # ``caught`` so the test can inspect its structured reason and status code.
        with self.assertRaises(GitHubAcquisitionError) as caught:
            client.get_pull_request("googlefonts/glyphsLib", 999999)

        self.assertEqual(caught.exception.reason, "not_found_or_inaccessible")
        self.assertEqual(caught.exception.status_code, 404)

    def test_get_changed_files_builds_validated_records(self) -> None:
        """One array item should become one domain record with page-one parameters."""

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
        """A full first page must cause acquisition of the remaining second page."""

        first = Mock()
        first.status_code = 200
        first.json.return_value = [_changed_file(index) for index in range(100)]
        second = Mock()
        second.status_code = 200
        second.json.return_value = [_changed_file(100)]
        session = Mock()

        # A sequence assigned to ``side_effect`` makes successive calls return
        # successive elements. This models page 1 and page 2 deterministically.
        session.get.side_effect = [first, second]

        records = GitHubReadClient(session=session).get_changed_files(
            _identity(changed_files=101)
        )

        self.assertEqual(len(records), 101)

        # ``call_args_list`` preserves every mock call. The comprehension extracts the
        # page query from each call so the test protects pagination order explicitly.
        pages = [call.kwargs["params"]["page"] for call in session.get.call_args_list]
        self.assertEqual(pages, [1, 2])

    def test_get_changed_files_rejects_count_disagreement(self) -> None:
        """A valid record list is still incomplete when metadata declared more files."""

        response = Mock()
        response.status_code = 200
        response.json.return_value = [_changed_file(1)]
        session = Mock()
        session.get.return_value = response

        # The metadata count is an independent completeness boundary. One structurally
        # valid record cannot satisfy an identity that declared two changed files.
        with self.assertRaises(GitHubResponseError) as caught:
            GitHubReadClient(session=session).get_changed_files(
                _identity(changed_files=2)
            )

        # ``assertIn`` protects the diagnostic's essential evidence values without
        # coupling the test to every word in the full message.
        self.assertIn("expected 2 records but acquired 1", str(caught.exception))

    def test_get_changed_files_rejects_non_array_success(self) -> None:
        """HTTP success with an object body must fail the changed-file array contract."""

        response = Mock()
        response.status_code = 200
        response.json.return_value = {"filename": "requirements-dev.txt"}
        session = Mock()
        session.get.return_value = response

        # This test separates HTTP success from response-shape trust. A 200 status does
        # not permit an object where the endpoint contract requires an array.
        with self.assertRaises(GitHubResponseError):
            GitHubReadClient(session=session).get_changed_files(
                _identity(changed_files=1)
            )


if __name__ == "__main__":
    # Direct execution remains available in addition to normal test discovery.
    unittest.main()
