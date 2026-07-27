"""Test exact-head workflow-file acquisition and decoding without live GitHub.

Purpose of this test file
-------------------------
``github_repository.py`` performs a two-request evidence chain:

1. fetch workflow-run detail to recover the path used by that execution;
2. fetch that path from the exact PR head SHA and decode its contents.

These tests replace both HTTP responses with mocks. They protect run/path identity,
the immutable ``ref`` parameter, base64-to-UTF-8 decoding, typed 404 unavailability,
and rejection of contradictory run detail.

They do not evaluate workflow commands or CI authority. Those later responsibilities
belong to ``test_workflow_commands.py`` and ``test_ci_authority.py``.
"""

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
    """Build the trusted PR identity that fixes the expected repository revision."""

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
    """Build the validated Actions run whose workflow definition will be resolved."""

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
    """Build a Requests-like response with controlled status and JSON payload.

    ``status`` is keyword-only because most fixtures are successful; exceptional
    HTTP behavior should be visible at the call site.
    """

    response = Mock()
    response.status_code = status
    response.json.return_value = payload
    return response


def _run_detail(*, run_id: int = 1001) -> dict[str, object]:
    """Build raw run-detail JSON while allowing a focused ID contradiction."""

    return {
        "id": run_id,
        "workflow_id": 2001,
        "head_sha": _HEAD_SHA,
        "event": "pull_request",
        "path": ".github/workflows/regression.yml",
    }


class GitHubRepositoryClientTests(unittest.TestCase):
    """Protect workflow-path identity, exact revision, decoding, and unavailability."""

    def test_resolves_workflow_path_and_decodes_exact_head_text(self) -> None:
        """Two valid responses should produce exact-revision UTF-8 workflow text."""

        workflow_text = "jobs:\n  test:\n    steps:\n      - run: pytest tests\n"
        session = Mock()

        # The first GET returns run detail; the second returns contents API data.
        # ``side_effect`` models this ordered two-request protocol explicitly.
        session.get.side_effect = [
            _response(_run_detail()),
            _response(
                {
                    "type": "file",
                    "path": ".github/workflows/regression.yml",
                    "sha": "blob-sha",
                    "encoding": "base64",
                    # The fixture follows GitHub's transport contract by encoding
                    # text to bytes, then base64, then JSON-safe text.
                    "content": base64.b64encode(workflow_text.encode()).decode(),
                }
            ),
        ]

        result = GitHubRepositoryClient(session=session).get_exact_head_workflow_file(
            _identity(), _run()
        )

        self.assertIsInstance(result, RepositoryTextFile)

        # The unittest assertion verifies runtime behavior; the plain assertion narrows
        # the repository-evidence union before ``content`` is accessed.
        assert isinstance(result, RepositoryTextFile)
        self.assertEqual(result.content, workflow_text)

        # The second request must use the exact immutable head SHA as ``ref``. Reading
        # the default branch would not prove which workflow definition the run used.
        self.assertEqual(
            session.get.call_args_list[1].kwargs["params"],
            {"ref": _HEAD_SHA},
        )

    def test_ambiguous_404_becomes_explicit_unavailable_file(self) -> None:
        """A contents 404 should become typed absence/access ambiguity, not empty text."""

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

        # The reason deliberately preserves GitHub's inability to distinguish true
        # absence from inaccessible content at this boundary.
        self.assertEqual(result.reason, "not_found_or_inaccessible")

    def test_rejects_workflow_run_detail_identity_mismatch(self) -> None:
        """Run detail for another execution must not supply this run's workflow path."""

        session = Mock()
        session.get.return_value = _response(_run_detail(run_id=9999))

        # Even though the response is HTTP-successful and structurally valid, its run
        # identity contradicts the supplied ``WorkflowRun`` and must be rejected.
        with self.assertRaises(GitHubResponseError):
            GitHubRepositoryClient(session=session).get_exact_head_workflow_file(
                _identity(), _run()
            )


if __name__ == "__main__":
    unittest.main()
