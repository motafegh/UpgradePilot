"""Deterministic tests for exact-head repository workflow-file acquisition."""

from __future__ import annotations

import base64
import unittest
from unittest.mock import Mock

from upgradepilot.github_actions import WorkflowRun
from upgradepilot.github_api import GitHubResponseError
from upgradepilot.github_client import PullRequestIdentity
from upgradepilot.github_repository import (
    GitHubRepositoryClient,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)

_HEAD_SHA = "f3cda8a94600e58d27f1bc17c99b7693718b6350"


def _identity() -> PullRequestIdentity:
    """Build the frozen S004-shaped PR identity used by these tests."""

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
    """Build one validated exact-head workflow run."""

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
    response.json.return_value = payload
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
    """Protect run-path identity, exact revision, and content decoding."""

    def test_resolves_workflow_path_and_decodes_exact_head_text(self) -> None:
        workflow_text = "jobs:\n  test:\n    steps:\n      - run: pytest tests\n"
        session = Mock()
        session.get.side_effect = [
            _response(_run_detail()),
            _response(
                {
                    "type": "file",
                    "path": ".github/workflows/regression.yml",
                    "sha": "blob-sha",
                    "encoding": "base64",
                    "content": base64.b64encode(workflow_text.encode()).decode(),
                }
            ),
        ]

        result = GitHubRepositoryClient(session=session).get_exact_head_workflow_file(
            _identity(), _run()
        )

        self.assertIsInstance(result, RepositoryTextFile)
        assert isinstance(result, RepositoryTextFile)
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

    def test_rejects_workflow_run_detail_identity_mismatch(self) -> None:
        session = Mock()
        session.get.return_value = _response(_run_detail(run_id=9999))

        with self.assertRaises(GitHubResponseError):
            GitHubRepositoryClient(session=session).get_exact_head_workflow_file(
                _identity(), _run()
            )


if __name__ == "__main__":
    unittest.main()
