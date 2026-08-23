"""Test exact pull-request base/head repository-file acquisition.

These tests begin at the GitHub contents API boundary. They do not parse ``uv.lock``
or interpret dependency records. Their responsibility is to prove that the pull-request
base/head wrappers bind the shared bounded text-file provider to the correct immutable PR
revision while preserving the minimum durable repository/path/revision/content contract.

Generic exact-file admission details such as malformed base64 and encoded/decoded size
bounds are owned by ``test_exact_commit_repository_files.py``. This suite keeps only
provider checks that materially exercise the PR wrapper path.
"""

from __future__ import annotations

import base64
import unittest
from unittest.mock import Mock

from upgradepilot.github.api import GitHubResponseError
from upgradepilot.github.pull_request import PullRequestIdentity
from upgradepilot.github.repository import (
    GitHubRepositoryClient,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)

_BASE_SHA = "a" * 40
_HEAD_SHA = "b" * 40
_REPOSITORY = "example/project"
_PATH = "services/api/uv.lock"


def _identity() -> PullRequestIdentity:
    """Build one case-neutral PR identity with immutable base and head revisions."""

    return PullRequestIdentity(
        repository=_REPOSITORY,
        number=42,
        title="Bump example dependency",
        state="open",
        merged=False,
        author="dependency-bot",
        base_ref="main",
        base_sha=_BASE_SHA,
        head_ref="dependency-update",
        head_sha=_HEAD_SHA,
        changed_files=1,
    )


def _response(payload: object, *, status: int = 200) -> Mock:
    """Build a Requests-like response with controlled JSON and HTTP status."""

    response = Mock()
    response.status_code = status
    response.json.return_value = payload
    return response


def _file_payload(
    raw: bytes = b'lock-version = "1"\n',
    *,
    path: str = _PATH,
) -> dict[str, object]:
    """Build the minimum GitHub contents response required by the provider."""

    return {
        "type": "file",
        "path": path,
        "encoding": "base64",
        "content": base64.b64encode(raw).decode("ascii"),
    }


class PullRequestRepositoryFileTests(unittest.TestCase):
    """Protect PR revision binding and the shared exact-file provider boundary."""

    def test_base_and_head_acquisition_preserve_minimum_exact_file_contract(self) -> None:
        raw = b'lock-version = "1"\n'
        session = Mock()
        session.get.side_effect = [
            _response(_file_payload(raw)),
            _response(_file_payload(raw)),
        ]
        client = GitHubRepositoryClient(session=session)

        base = client.get_pull_request_base_file(_identity(), _PATH)
        head = client.get_pull_request_head_file(_identity(), _PATH)

        self.assertIsInstance(base, RepositoryTextFile)
        self.assertIsInstance(head, RepositoryTextFile)
        assert isinstance(base, RepositoryTextFile)
        assert isinstance(head, RepositoryTextFile)

        self.assertEqual(base.repository, _REPOSITORY)
        self.assertEqual(base.path, _PATH)
        self.assertEqual(base.revision, _BASE_SHA)
        self.assertEqual(base.content, raw.decode("utf-8"))
        self.assertEqual(head.repository, _REPOSITORY)
        self.assertEqual(head.path, _PATH)
        self.assertEqual(head.revision, _HEAD_SHA)
        self.assertEqual(head.content, raw.decode("utf-8"))

        self.assertEqual(
            session.get.call_args_list[0].kwargs["params"],
            {"ref": _BASE_SHA},
        )
        self.assertEqual(
            session.get.call_args_list[1].kwargs["params"],
            {"ref": _HEAD_SHA},
        )

    def test_ambiguous_404_preserves_repository_path_and_revision(self) -> None:
        session = Mock()
        session.get.return_value = _response({}, status=404)

        result = GitHubRepositoryClient(session=session).get_pull_request_base_file(
            _identity(), _PATH
        )

        self.assertIsInstance(result, UnavailableRepositoryFile)
        assert isinstance(result, UnavailableRepositoryFile)
        self.assertEqual(result.repository, _REPOSITORY)
        self.assertEqual(result.path, _PATH)
        self.assertEqual(result.revision, _BASE_SHA)
        self.assertEqual(result.reason, "not_found_or_inaccessible")

    def test_returned_path_must_match_requested_path(self) -> None:
        session = Mock()
        session.get.return_value = _response(
            _file_payload(path="services/other/uv.lock")
        )

        with self.assertRaisesRegex(GitHubResponseError, "path does not match"):
            GitHubRepositoryClient(session=session).get_pull_request_head_file(
                _identity(), _PATH
            )

    def test_invalid_utf8_remains_rejected_at_provider_boundary(self) -> None:
        session = Mock()
        session.get.return_value = _response(_file_payload(raw=b"\xff"))

        with self.assertRaisesRegex(GitHubResponseError, "not valid UTF-8"):
            GitHubRepositoryClient(session=session).get_pull_request_head_file(
                _identity(), _PATH
            )


if __name__ == "__main__":
    unittest.main()
