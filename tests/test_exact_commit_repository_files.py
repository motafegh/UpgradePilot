"""Test strict repository-file acquisition at an explicit immutable commit SHA."""

from __future__ import annotations

import base64
import unittest
from datetime import datetime, timezone
from unittest.mock import Mock

from upgradepilot.github.api import GitHubResponseError
from upgradepilot.github.repository import (
    GitHubRepositoryClient,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)

_REPOSITORY = "example/project"
_COMMIT_SHA = "a" * 40
_PATH = "docs/changelog.md"
_NOW = datetime(2026, 8, 2, 12, 0, tzinfo=timezone.utc)


def _response(payload: object, *, status: int = 200) -> Mock:
    response = Mock()
    response.status_code = status
    response.json.return_value = payload
    return response


def _file_payload(
    raw: bytes = b"## 2.8\nDrop support for Python 3.8.\n",
    *,
    path: str = _PATH,
    size: object | None = None,
    content: str | None = None,
) -> dict[str, object]:
    return {
        "type": "file",
        "path": path,
        "sha": "b" * 40,
        "size": len(raw) if size is None else size,
        "encoding": "base64",
        "content": base64.b64encode(raw).decode("ascii") if content is None else content,
    }


class ExactCommitRepositoryFileTests(unittest.TestCase):
    """Protect immutable revision input and exact file evidence for Step 5C."""

    def test_exact_commit_acquisition_preserves_file_and_retrieval_evidence(self) -> None:
        raw = b"## 2.8\nDrop support for Python 3.8.\n"
        session = Mock()
        session.get.return_value = _response(_file_payload(raw))

        result = GitHubRepositoryClient(
            session=session,
            now=lambda: _NOW,
        ).get_exact_commit_text_file(_REPOSITORY, _COMMIT_SHA, _PATH)

        self.assertIsInstance(result, RepositoryTextFile)
        assert isinstance(result, RepositoryTextFile)
        self.assertEqual(result.repository, _REPOSITORY)
        self.assertEqual(result.path, _PATH)
        self.assertEqual(result.returned_path, _PATH)
        self.assertEqual(result.revision, _COMMIT_SHA)
        self.assertEqual(result.blob_sha, "b" * 40)
        self.assertEqual(result.reported_byte_count, len(raw))
        self.assertEqual(result.decoded_byte_count, len(raw))
        self.assertEqual(result.content, raw.decode("utf-8"))
        self.assertEqual(result.retrieved_at, _NOW)
        self.assertEqual(session.get.call_args.kwargs["params"], {"ref": _COMMIT_SHA})

    def test_uppercase_sha_is_normalized_before_request(self) -> None:
        session = Mock()
        session.get.return_value = _response(_file_payload())

        result = GitHubRepositoryClient(session=session).get_exact_commit_text_file(
            _REPOSITORY,
            _COMMIT_SHA.upper(),
            _PATH,
        )

        assert isinstance(result, RepositoryTextFile)
        self.assertEqual(result.revision, _COMMIT_SHA)
        self.assertEqual(session.get.call_args.kwargs["params"], {"ref": _COMMIT_SHA})

    def test_movable_or_malformed_revision_names_are_rejected_before_network(self) -> None:
        for revision in ("main", "v2.8.4", "abc123", "g" * 40):
            with self.subTest(revision=revision):
                session = Mock()
                with self.assertRaisesRegex(ValueError, "40- or 64-character"):
                    GitHubRepositoryClient(session=session).get_exact_commit_text_file(
                        _REPOSITORY,
                        revision,
                        _PATH,
                    )
                session.get.assert_not_called()

    def test_64_character_hex_object_id_is_admitted(self) -> None:
        sha = "c" * 64
        session = Mock()
        session.get.return_value = _response(_file_payload())

        result = GitHubRepositoryClient(session=session).get_exact_commit_text_file(
            _REPOSITORY,
            sha,
            _PATH,
        )

        assert isinstance(result, RepositoryTextFile)
        self.assertEqual(result.revision, sha)

    def test_unavailable_file_preserves_repository_path_and_commit(self) -> None:
        session = Mock()
        session.get.return_value = _response({}, status=404)

        result = GitHubRepositoryClient(session=session).get_exact_commit_text_file(
            _REPOSITORY,
            _COMMIT_SHA,
            _PATH,
        )

        self.assertIsInstance(result, UnavailableRepositoryFile)
        assert isinstance(result, UnavailableRepositoryFile)
        self.assertEqual(result.repository, _REPOSITORY)
        self.assertEqual(result.path, _PATH)
        self.assertEqual(result.revision, _COMMIT_SHA)
        self.assertEqual(result.reason, "not_found_or_inaccessible")

    def test_strict_byte_agreement_is_shared_with_commit_reader(self) -> None:
        session = Mock()
        session.get.return_value = _response(_file_payload(raw=b"abc", size=4))

        with self.assertRaisesRegex(GitHubResponseError, "does not match"):
            GitHubRepositoryClient(session=session).get_exact_commit_text_file(
                _REPOSITORY,
                _COMMIT_SHA,
                _PATH,
            )


if __name__ == "__main__":
    unittest.main()
