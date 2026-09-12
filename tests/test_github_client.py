"""Test the PR and changed-file acquisition boundary without live GitHub access.

Purpose of this test file
-------------------------
The production code in ``upgradepilot.github.pull_request`` combines PR-specific input
validation, shared HTTP behavior from ``upgradepilot.github.api``, response parsing,
changed-file pagination, and snapshot-coherence checks. These tests isolate that boundary
by replacing the real Requests ``Session`` with ``Mock`` objects.

What these tests prove
----------------------
* successful PR JSON becomes an exact ``PullRequestIdentity``;
* the client sends the expected timeout, headers, and pagination parameters;
* GitHub's ambiguous 404 becomes the correct acquisition category;
* every changed-file page is requested and converted into validated records;
* changed-file locators must identify the frozen repository/path/head revision;
* repository spelling remains compatible with GitHub's case-insensitive repository identity;
* base/head/count drift around acquisition is rejected, including multi-page and zero-file cases;
* count disagreement and wrong top-level JSON shape are rejected.

What they do not prove
----------------------
No real network request is made. Therefore these tests do not prove current GitHub
availability, credentials, rate limits, transactional snapshot isolation, or compatibility
with every unmocked external response. They prove how the client behaves for the controlled
responses supplied.
"""

from __future__ import annotations

import unittest
from unittest.mock import Mock

from upgradepilot.github.api import GitHubAcquisitionError, GitHubResponseError
from upgradepilot.github.pull_request import GitHubPullRequestClient, PullRequestIdentity

_BASE_SHA = "044f19e4b1437bfc4343592486f4e3c6040306d9"
_HEAD_SHA = "f3cda8a94600e58d27f1bc17c99b7693718b6350"
_OTHER_BASE_SHA = "1" * 40
_OTHER_HEAD_SHA = "2" * 40
_REPOSITORY = "googlefonts/glyphsLib"


def _identity(
    *,
    changed_files: int,
    repository: str = _REPOSITORY,
    base_sha: str = _BASE_SHA,
    head_sha: str = _HEAD_SHA,
) -> PullRequestIdentity:
    """Build one trusted PR identity while varying snapshot-defining fields."""

    return PullRequestIdentity(
        repository=repository,
        number=1145,
        title="Bump pytest from 9.0.2 to 9.0.3",
        state="closed",
        merged=True,
        author="dependabot[bot]",
        base_ref="main",
        base_sha=base_sha,
        head_ref="dependabot/pip/pytest-9.0.3",
        head_sha=head_sha,
        changed_files=changed_files,
    )


def _pull_request_payload(identity: PullRequestIdentity) -> dict[str, object]:
    """Return the GitHub-like PR JSON needed for one identity re-read."""

    return {
        "number": identity.number,
        "title": identity.title,
        "state": identity.state,
        "merged": identity.merged,
        "user": {"login": identity.author},
        "base": {"ref": identity.base_ref, "sha": identity.base_sha},
        "head": {"ref": identity.head_ref, "sha": identity.head_sha},
        "changed_files": identity.changed_files,
    }


def _response(payload: object, *, status_code: int = 200) -> Mock:
    response = Mock()
    response.status_code = status_code
    response.json.return_value = payload
    return response


def _changed_file(
    index: int,
    *,
    repository: str = _REPOSITORY,
    head_sha: str = _HEAD_SHA,
    filename: str | None = None,
) -> dict[str, object]:
    """Build one raw GitHub-like changed-file object with an exact-head locator."""

    filename = filename or f"requirements-{index}.txt"
    return {
        "filename": filename,
        "status": "modified",
        "additions": 1,
        "deletions": 1,
        "changes": 2,
        "contents_url": (
            f"https://api.github.com/repos/{repository}/contents/{filename}?ref={head_sha}"
        ),
        "patch": "-pytest==9.0.2\n+pytest==9.0.3",
    }


class GitHubPullRequestClientTests(unittest.TestCase):
    """Protect PR identity, pagination, completeness, and snapshot coherence."""

    def test_get_pull_request_builds_exact_identity(self) -> None:
        """A valid response should become identity and use the shared request contract."""

        expected = _identity(changed_files=1)
        session = Mock()
        session.get.return_value = _response(_pull_request_payload(expected))

        client = GitHubPullRequestClient(session=session)
        identity = client.get_pull_request(_REPOSITORY, 1145)

        self.assertEqual(identity.number, 1145)
        self.assertEqual(identity.head_sha, _HEAD_SHA)
        session.get.assert_called_once()

        _, kwargs = session.get.call_args
        self.assertEqual(kwargs["timeout"], (3.05, 15.0))
        self.assertNotIn("Authorization", kwargs["headers"])

    def test_404_preserves_nonexistence_or_access_ambiguity(self) -> None:
        """HTTP 404 must retain GitHub's absence-versus-access ambiguity."""

        session = Mock()
        session.get.return_value = _response({}, status_code=404)
        client = GitHubPullRequestClient(session=session)

        with self.assertRaises(GitHubAcquisitionError) as caught:
            client.get_pull_request(_REPOSITORY, 999999)

        self.assertEqual(caught.exception.reason, "not_found_or_inaccessible")
        self.assertEqual(caught.exception.status_code, 404)

    def test_get_changed_files_builds_validated_records(self) -> None:
        """Matching file locator plus stable post-read should admit one changed file."""

        identity = _identity(changed_files=1)
        session = Mock()
        session.get.side_effect = [
            _response([_changed_file(1)]),
            _response(_pull_request_payload(identity)),
        ]

        records = GitHubPullRequestClient(session=session).get_changed_files(identity)

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].filename, "requirements-1.txt")
        _, kwargs = session.get.call_args_list[0]
        self.assertEqual(kwargs["params"], {"per_page": 100, "page": 1})
        self.assertNotIn("contents_url", records[0].__slots__)

    def test_get_changed_files_accepts_canonical_locator_for_repository_case_variant(self) -> None:
        """GitHub repository case normalization must not weaken exact file-path checks."""

        identity = _identity(
            changed_files=1,
            repository="GoogleFonts/glyphsLib",
        )
        session = Mock()
        session.get.side_effect = [
            _response([_changed_file(1, repository="googlefonts/glyphsLib")]),
            _response(_pull_request_payload(identity)),
        ]

        records = GitHubPullRequestClient(session=session).get_changed_files(identity)

        self.assertEqual(tuple(record.filename for record in records), ("requirements-1.txt",))

    def test_get_changed_files_acquires_all_pages_before_post_read(self) -> None:
        """A full first page must acquire page two before the final PR identity read."""

        identity = _identity(changed_files=101)
        first = _response([_changed_file(index) for index in range(100)])
        second = _response([_changed_file(100)])
        post_read = _response(_pull_request_payload(identity))
        session = Mock()
        session.get.side_effect = [first, second, post_read]

        records = GitHubPullRequestClient(session=session).get_changed_files(identity)

        self.assertEqual(len(records), 101)
        page_calls = [
            call.kwargs["params"]["page"]
            for call in session.get.call_args_list
            if "params" in call.kwargs
        ]
        self.assertEqual(page_calls, [1, 2])
        self.assertTrue(session.get.call_args_list[-1].args[0].endswith("/pulls/1145"))

    def test_get_changed_files_rejects_same_count_head_race_from_locator(self) -> None:
        """A head-B locator must be rejected even when head-A expected the same count."""

        identity = _identity(changed_files=1)
        session = Mock()
        session.get.return_value = _response(
            [_changed_file(1, head_sha=_OTHER_HEAD_SHA)]
        )

        with self.assertRaises(GitHubResponseError) as caught:
            GitHubPullRequestClient(session=session).get_changed_files(identity)

        self.assertIn("does not identify the frozen", str(caught.exception))
        session.get.assert_called_once()

    def test_get_changed_files_rejects_snapshot_drift_after_acquisition(self) -> None:
        """Observable base, head, or count drift must fail the final identity fence."""

        frozen = _identity(changed_files=1)
        changed_snapshots = (
            _identity(changed_files=1, base_sha=_OTHER_BASE_SHA),
            _identity(changed_files=1, head_sha=_OTHER_HEAD_SHA),
            _identity(changed_files=2),
        )

        for current in changed_snapshots:
            with self.subTest(
                base_sha=current.base_sha,
                head_sha=current.head_sha,
                changed_files=current.changed_files,
            ):
                session = Mock()
                session.get.side_effect = [
                    _response([_changed_file(1)]),
                    _response(_pull_request_payload(current)),
                ]

                with self.assertRaises(GitHubResponseError) as caught:
                    GitHubPullRequestClient(session=session).get_changed_files(frozen)

                self.assertIn("identity changed", str(caught.exception))

    def test_get_changed_files_rejects_snapshot_drift_after_pagination(self) -> None:
        """A multi-page collection is rejected when the post-read head has moved."""

        frozen = _identity(changed_files=101)
        current = _identity(changed_files=101, head_sha=_OTHER_HEAD_SHA)
        session = Mock()
        session.get.side_effect = [
            _response([_changed_file(index) for index in range(100)]),
            _response([_changed_file(100)]),
            _response(_pull_request_payload(current)),
        ]

        with self.assertRaises(GitHubResponseError) as caught:
            GitHubPullRequestClient(session=session).get_changed_files(frozen)

        self.assertIn("identity changed", str(caught.exception))
        page_calls = [
            call.kwargs["params"]["page"]
            for call in session.get.call_args_list
            if "params" in call.kwargs
        ]
        self.assertEqual(page_calls, [1, 2])

    def test_get_changed_files_rejects_missing_or_malformed_contents_locator(self) -> None:
        """Required exact-head locator evidence must be present and structurally usable."""

        missing = _changed_file(1)
        del missing["contents_url"]
        malformed = _changed_file(1)
        malformed["contents_url"] = (
            "https://api.github.com/repos/googlefonts/glyphsLib/contents/requirements-1.txt"
        )

        for payload in (missing, malformed):
            with self.subTest(payload=payload):
                session = Mock()
                session.get.return_value = _response([payload])

                with self.assertRaises(GitHubResponseError):
                    GitHubPullRequestClient(session=session).get_changed_files(
                        _identity(changed_files=1)
                    )

    def test_get_changed_files_rejects_locator_for_another_repository_or_path(self) -> None:
        """Head equality alone cannot admit a locator for a different file identity."""

        wrong_repository = _changed_file(1, repository="other/project")
        wrong_path = _changed_file(1)
        wrong_path["contents_url"] = (
            f"https://api.github.com/repos/{_REPOSITORY}/contents/other.txt?ref={_HEAD_SHA}"
        )

        for payload in (wrong_repository, wrong_path):
            with self.subTest(payload=payload):
                session = Mock()
                session.get.return_value = _response([payload])

                with self.assertRaises(GitHubResponseError):
                    GitHubPullRequestClient(session=session).get_changed_files(
                        _identity(changed_files=1)
                    )

    def test_get_changed_files_rejects_count_disagreement(self) -> None:
        """A valid record list is still incomplete when metadata declared more files."""

        session = Mock()
        session.get.return_value = _response([_changed_file(1)])

        with self.assertRaises(GitHubResponseError) as caught:
            GitHubPullRequestClient(session=session).get_changed_files(
                _identity(changed_files=2)
            )

        self.assertIn("expected 2 records but acquired 1", str(caught.exception))

    def test_get_changed_files_rejects_non_array_success(self) -> None:
        """HTTP success with an object body must fail the changed-file array contract."""

        session = Mock()
        session.get.return_value = _response({"filename": "requirements-dev.txt"})

        with self.assertRaises(GitHubResponseError):
            GitHubPullRequestClient(session=session).get_changed_files(
                _identity(changed_files=1)
            )

    def test_zero_changed_files_still_receives_final_identity_fence(self) -> None:
        """An empty frozen collection must not bypass post-acquisition snapshot validation."""

        frozen = _identity(changed_files=0)
        current = _identity(changed_files=1)
        session = Mock()
        session.get.return_value = _response(_pull_request_payload(current))

        with self.assertRaises(GitHubResponseError):
            GitHubPullRequestClient(session=session).get_changed_files(frozen)

        session.get.assert_called_once()
        self.assertTrue(session.get.call_args.args[0].endswith("/pulls/1145"))


if __name__ == "__main__":
    unittest.main()
