"""Test bounded repository-text acquisition at an explicit immutable commit SHA."""

from __future__ import annotations

import base64
import unittest
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


def _response(payload: object, *, status: int = 200) -> Mock:
    response = Mock()
    response.status_code = status
    response.json.return_value = payload
    return response


def _file_payload(
    raw: bytes = b"## 2.8\nDrop support for Python 3.8.\n",
    *,
    path: str = _PATH,
    content: str | None = None,
) -> dict[str, object]:
    return {
        "type": "file",
        "path": path,
        "encoding": "base64",
        "content": base64.b64encode(raw).decode("ascii") if content is None else content,
    }


class ExactCommitRepositoryFileTests(unittest.TestCase):
    """Protect immutable locator, bounded text, and typed unavailability semantics."""

    def test_exact_commit_acquisition_returns_minimum_durable_text_contract(self) -> None:
        raw = b"## 2.8\nDrop support for Python 3.8.\n"
        session = Mock()
        session.get.return_value = _response(_file_payload(raw))

        result = GitHubRepositoryClient(session=session).get_exact_commit_text_file(
            _REPOSITORY,
            _COMMIT_SHA,
            _PATH,
        )

        self.assertIsInstance(result, RepositoryTextFile)
        assert isinstance(result, RepositoryTextFile)
        self.assertEqual(result.repository, _REPOSITORY)
        self.assertEqual(result.path, _PATH)
        self.assertEqual(result.revision, _COMMIT_SHA)
        self.assertEqual(result.content, raw.decode("utf-8"))
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

    def test_repository_path_structure_uses_shared_owner_before_network(self) -> None:
        invalid_paths = (
            "",
            "/docs/changelog.md",
            "docs\\changelog.md",
            "docs//changelog.md",
            "./docs/changelog.md",
            "docs/../changelog.md",
        )

        for path in invalid_paths:
            with self.subTest(path=path):
                session = Mock()
                with self.assertRaisesRegex(
                    ValueError,
                    "repository-relative POSIX file path",
                ):
                    GitHubRepositoryClient(session=session).get_exact_commit_text_file(
                        _REPOSITORY,
                        _COMMIT_SHA,
                        path,
                    )
                session.get.assert_not_called()

    def test_unavailable_file_preserves_exact_locator(self) -> None:
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

    def test_returned_path_must_match_requested_path(self) -> None:
        session = Mock()
        session.get.return_value = _response(_file_payload(path="docs/other.md"))

        with self.assertRaisesRegex(GitHubResponseError, "does not match"):
            GitHubRepositoryClient(session=session).get_exact_commit_text_file(
                _REPOSITORY,
                _COMMIT_SHA,
                _PATH,
            )

    def test_malformed_base64_is_rejected(self) -> None:
        session = Mock()
        session.get.return_value = _response(_file_payload(content="%%%not-base64%%%"))

        with self.assertRaisesRegex(GitHubResponseError, "not valid base64"):
            GitHubRepositoryClient(session=session).get_exact_commit_text_file(
                _REPOSITORY,
                _COMMIT_SHA,
                _PATH,
            )

    def test_oversized_content_is_rejected_without_provider_size_metadata(self) -> None:
        session = Mock()
        session.get.return_value = _response(_file_payload(raw=b"x" * 1_000_001))

        with self.assertRaisesRegex(GitHubResponseError, "bounded text-file limit"):
            GitHubRepositoryClient(session=session).get_exact_commit_text_file(
                _REPOSITORY,
                _COMMIT_SHA,
                _PATH,
            )

    def test_repository_text_file_rejects_noncanonical_manual_locator(self) -> None:
        with self.assertRaises(ValueError):
            RepositoryTextFile(
                repository=" example/project ",
                path=_PATH,
                revision=_COMMIT_SHA,
                content="text",
            )
        with self.assertRaises(ValueError):
            RepositoryTextFile(
                repository=_REPOSITORY,
                path="docs/../changelog.md",
                revision=_COMMIT_SHA,
                content="text",
            )
        with self.assertRaisesRegex(ValueError, "canonical lowercase"):
            RepositoryTextFile(
                repository=_REPOSITORY,
                path=_PATH,
                revision=_COMMIT_SHA.upper(),
                content="text",
            )


if __name__ == "__main__":
    unittest.main()
