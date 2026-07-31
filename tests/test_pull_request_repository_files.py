"""Test exact pull-request base/head repository-file acquisition.

These tests begin at the GitHub contents API boundary. They do not parse ``uv.lock``
or interpret dependency records. Their responsibility is to prove that complete text
is bound to one immutable pull-request revision with trustworthy path, blob, and size
evidence before a later source-specific parser receives it.
"""

from __future__ import annotations

import base64
import unittest
from unittest.mock import Mock

from upgradepilot.github_api import GitHubResponseError
from upgradepilot.github_client import PullRequestIdentity
from upgradepilot.github_repository import (
    ExactRepositoryTextFile,
    GitHubRepositoryClient,
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
    size: object | None = None,
    content: str | None = None,
) -> dict[str, object]:
    """Build one contents response while exposing size/encoding failure controls."""

    return {
        "type": "file",
        "path": path,
        "sha": "c" * 40,
        "size": len(raw) if size is None else size,
        "encoding": "base64",
        "content": (
            base64.b64encode(raw).decode("ascii") if content is None else content
        ),
    }


class PullRequestRepositoryFileTests(unittest.TestCase):
    """Protect exact revision, file identity, byte agreement, and text decoding."""

    def test_base_and_head_acquisition_preserve_exact_file_evidence(self) -> None:
        """Explicit methods must select only the PR's immutable base or head SHA."""

        raw = b'lock-version = "1"\n'
        session = Mock()
        session.get.side_effect = [
            _response(_file_payload(raw)),
            _response(_file_payload(raw)),
        ]
        client = GitHubRepositoryClient(session=session)

        base = client.get_pull_request_base_file(_identity(), _PATH)
        head = client.get_pull_request_head_file(_identity(), _PATH)

        self.assertIsInstance(base, ExactRepositoryTextFile)
        self.assertIsInstance(head, ExactRepositoryTextFile)
        assert isinstance(base, ExactRepositoryTextFile)
        assert isinstance(head, ExactRepositoryTextFile)

        self.assertEqual(base.repository, _REPOSITORY)
        self.assertEqual(base.path, _PATH)
        self.assertEqual(base.returned_path, _PATH)
        self.assertEqual(base.revision, _BASE_SHA)
        self.assertEqual(base.blob_sha, "c" * 40)
        self.assertEqual(base.reported_byte_count, len(raw))
        self.assertEqual(base.decoded_byte_count, len(raw))
        self.assertEqual(base.content, raw.decode("utf-8"))
        self.assertEqual(head.revision, _HEAD_SHA)

        self.assertEqual(
            session.get.call_args_list[0].kwargs["params"],
            {"ref": _BASE_SHA},
        )
        self.assertEqual(
            session.get.call_args_list[1].kwargs["params"],
            {"ref": _HEAD_SHA},
        )

    def test_ambiguous_404_preserves_repository_path_and_revision(self) -> None:
        """Missing or inaccessible exact content must not become empty text."""

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
        """HTTP success for another file must not be accepted as requested evidence."""

        session = Mock()
        session.get.return_value = _response(
            _file_payload(path="services/other/uv.lock")
        )

        with self.assertRaisesRegex(GitHubResponseError, "path does not match"):
            GitHubRepositoryClient(session=session).get_pull_request_head_file(
                _identity(), _PATH
            )

    def test_reported_size_must_be_a_nonnegative_integer(self) -> None:
        """JSON booleans and negative numbers are not valid byte-count evidence."""

        for invalid_size in (True, -1):
            with self.subTest(size=invalid_size):
                session = Mock()
                session.get.return_value = _response(
                    _file_payload(size=invalid_size)
                )

                with self.assertRaises(GitHubResponseError):
                    GitHubRepositoryClient(session=session).get_pull_request_head_file(
                        _identity(), _PATH
                    )

    def test_reported_oversize_is_rejected_before_base64_decoding(self) -> None:
        """A known oversized file should stop before malformed content is decoded."""

        session = Mock()
        session.get.return_value = _response(
            _file_payload(size=1_000_001, content="not valid base64")
        )

        with self.assertRaisesRegex(GitHubResponseError, "reported size exceeds"):
            GitHubRepositoryClient(session=session).get_pull_request_head_file(
                _identity(), _PATH
            )

    def test_malformed_base64_remains_distinct(self) -> None:
        """Transport content outside the admitted Base64 grammar must be rejected."""

        session = Mock()
        session.get.return_value = _response(
            _file_payload(size=3, content="not valid base64")
        )

        with self.assertRaisesRegex(GitHubResponseError, "not valid base64"):
            GitHubRepositoryClient(session=session).get_pull_request_head_file(
                _identity(), _PATH
            )

    def test_reported_and_decoded_sizes_must_agree(self) -> None:
        """Decoded bytes cannot silently contradict GitHub's reported file size."""

        session = Mock()
        session.get.return_value = _response(
            _file_payload(raw=b"abc", size=4)
        )

        with self.assertRaisesRegex(GitHubResponseError, "does not match"):
            GitHubRepositoryClient(session=session).get_pull_request_head_file(
                _identity(), _PATH
            )

    def test_invalid_utf8_remains_distinct(self) -> None:
        """Correct Base64 and size do not make non-UTF-8 bytes usable text."""

        session = Mock()
        session.get.return_value = _response(_file_payload(raw=b"\xff"))

        with self.assertRaisesRegex(GitHubResponseError, "not valid UTF-8"):
            GitHubRepositoryClient(session=session).get_pull_request_head_file(
                _identity(), _PATH
            )

    def test_missing_reported_size_is_malformed_response(self) -> None:
        """A successful contents response without size cannot establish exact evidence."""

        payload = _file_payload()
        del payload["size"]
        session = Mock()
        session.get.return_value = _response(payload)

        with self.assertRaisesRegex(GitHubResponseError, "missing required field: size"):
            GitHubRepositoryClient(session=session).get_pull_request_head_file(
                _identity(), _PATH
            )


if __name__ == "__main__":
    unittest.main()
