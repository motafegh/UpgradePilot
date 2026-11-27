"""Test exact-head workflow-file acquisition without live GitHub."""

from __future__ import annotations

import base64
import json
import unittest
from unittest.mock import Mock

from upgradepilot.github.actions import WorkflowRun
from upgradepilot.github.api import GitHubResponseError
from upgradepilot.github.pull_request import PullRequestIdentity
from upgradepilot.github.repository import (
    GitHubRepositoryClient,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)

_HEAD_SHA = "f3cda8a94600e58d27f1bc17c99b7693718b6350"


def _identity() -> PullRequestIdentity:
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
        head_sha=_HEAD_SHA,
        changed_files=1,
    )


def _run() -> WorkflowRun:
    return WorkflowRun(
        run_id=1001,
        workflow_id=2001,
        name="Regression Tests",
        event="pull_request",
        head_sha=_HEAD_SHA,
        status="completed",
        conclusion="success",
        run_attempt=1,
    )


def _response(payload: object, *, status: int = 200) -> Mock:
    response = Mock()
    response.status_code = status
    response.iter_content.return_value = [json.dumps(payload).encode()]
    return response


def _run_detail(*, run_id: int = 1001) -> dict[str, object]:
    return {
        "id": run_id,
        "workflow_id": 2001,
        "head_sha": _HEAD_SHA,
        "event": "pull_request",
        "path": ".github/workflows/regression.yml",
    }


class GitHubRepositoryClientTests(unittest.TestCase):
    def test_exact_file_reuse_is_local_to_the_client_and_immutable_locator(self) -> None:
        identity = _identity()
        path = "pyproject.toml"
        payload = {"type": "file", "path": path, "encoding": "base64", "content": "YQ=="}
        session = Mock()
        session.get.side_effect = [
            _response({}, status=404),
            _response(payload),
            _response(payload),
            _response(payload),
            _response({**payload, "path": "setup.cfg"}),
            _response(payload),
        ]
        client = GitHubRepositoryClient(session=session, reuse_exact_files=True)

        self.assertIsInstance(client.get_pull_request_head_file(identity, path), UnavailableRepositoryFile)
        head = client.get_pull_request_head_file(identity, path)
        self.assertIsInstance(head, RepositoryTextFile)
        self.assertIs(client.get_exact_commit_text_file(identity.repository, identity.head_sha, path), head)
        self.assertEqual(session.get.call_count, 2)

        client.get_pull_request_base_file(identity, path)
        client.get_exact_commit_text_file("other/project", identity.head_sha, path)
        client.get_exact_commit_text_file(identity.repository, identity.head_sha, "setup.cfg")
        GitHubRepositoryClient(session=session, reuse_exact_files=True).get_pull_request_head_file(identity, path)
        self.assertEqual(session.get.call_count, 6)

    def test_acquires_json_envelope_for_maximum_supported_repository_text(self) -> None:
        content = b"a" * 1_000_000
        path = "requirements.txt"
        session = Mock()
        session.get.return_value = _response(
            {
                "type": "file",
                "path": path,
                "encoding": "base64",
                "content": base64.encodebytes(content).decode(),
            }
        )

        result = GitHubRepositoryClient(session=session).get_exact_head_text_file(
            _identity(), path
        )

        self.assertIsInstance(result, RepositoryTextFile)
        self.assertEqual(result.content, content.decode())

    def test_resolves_workflow_path_and_returns_exact_head_text(self) -> None:
        workflow_text = "jobs:\n  test:\n    steps:\n      - run: pytest tests\n"
        workflow_bytes = workflow_text.encode()
        session = Mock()
        session.get.side_effect = [
            _response(_run_detail()),
            _response(
                {
                    "type": "file",
                    "path": ".github/workflows/regression.yml",
                    "encoding": "base64",
                    "content": base64.b64encode(workflow_bytes).decode(),
                }
            ),
        ]

        result = GitHubRepositoryClient(session=session).get_exact_head_workflow_file(
            _identity(), _run()
        )

        self.assertIsInstance(result, RepositoryTextFile)
        assert isinstance(result, RepositoryTextFile)
        self.assertEqual(result.repository, "googlefonts/glyphsLib")
        self.assertEqual(result.path, ".github/workflows/regression.yml")
        self.assertEqual(result.revision, _HEAD_SHA)
        self.assertEqual(result.content, workflow_text)
        self.assertEqual(
            session.get.call_args_list[1].kwargs["params"],
            {"ref": _HEAD_SHA},
        )

    def test_ambiguous_404_becomes_explicit_unavailable_file(self) -> None:
        session = Mock()
        session.get.side_effect = [
            _response(_run_detail()),
            _response({}, status=404),
        ]

        result = GitHubRepositoryClient(session=session).get_exact_head_workflow_file(
            _identity(), _run()
        )

        self.assertIsInstance(result, UnavailableRepositoryFile)
        assert isinstance(result, UnavailableRepositoryFile)
        self.assertEqual(result.reason, "not_found_or_inaccessible")
        self.assertEqual(result.repository, "googlefonts/glyphsLib")
        self.assertEqual(result.path, ".github/workflows/regression.yml")
        self.assertEqual(result.revision, _HEAD_SHA)

    def test_rejects_workflow_run_detail_identity_mismatch(self) -> None:
        session = Mock()
        session.get.return_value = _response(_run_detail(run_id=9999))

        with self.assertRaises(GitHubResponseError):
            GitHubRepositoryClient(session=session).get_exact_head_workflow_file(
                _identity(), _run()
            )


if __name__ == "__main__":
    unittest.main()
