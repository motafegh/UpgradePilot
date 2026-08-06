"""Test exact-head GitHub Actions acquisition with controlled responses.

Purpose of this test file
-------------------------
``upgradepilot.github.actions`` acquires workflow runs, jobs, and optional step
summaries for the frozen PR head SHA. These tests inject a mocked HTTP session so each
scenario can control GitHub's response and inspect the request parameters.

The suite protects:

* query filters and local exact-head identity checks;
* explicit empty-run evidence;
* complete multi-page run acquisition;
* job/run/head relationships;
* step-summary parsing;
* latest-attempt job filtering.

These are acquisition tests, not CI-authority tests. Successful mocked jobs do not
prove that a dependency was installed or exercised; that later interpretation is
covered by the CI dependency-exercise tests.
"""

from __future__ import annotations

import unittest
from unittest.mock import Mock

from upgradepilot.github.actions import GitHubActionsClient, WorkflowRun
from upgradepilot.github.api import GitHubResponseError
from upgradepilot.github.pull_request import PullRequestIdentity

_HEAD_SHA = "f3cda8a94600e58d27f1bc17c99b7693718b6350"


def _identity() -> PullRequestIdentity:
    """Build the frozen PR identity that establishes the expected head revision."""

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


def _run(index: int, *, head_sha: str = _HEAD_SHA) -> dict[str, object]:
    """Build one raw run object while allowing a focused head-SHA variation."""

    return {
        "id": 1000 + index,
        "workflow_id": 2000 + index,
        "name": f"Workflow {index}",
        "event": "pull_request",
        "head_sha": head_sha,
        "status": "completed",
        "conclusion": "success",
        "run_attempt": 1,
    }


def _response(payload: object) -> Mock:
    """Build the minimal successful Requests-like response used by the client."""

    response = Mock()
    response.status_code = 200
    response.json.return_value = payload
    return response


class GitHubActionsClientTests(unittest.TestCase):
    """Protect run/job pagination, exact-head binding, and step parsing."""

    def test_acquires_runs_for_exact_head_and_event(self) -> None:
        session = Mock()
        session.get.return_value = _response(
            {"total_count": 1, "workflow_runs": [_run(1)]}
        )

        runs = GitHubActionsClient(session=session).get_exact_head_workflow_runs(
            _identity()
        )

        self.assertEqual(len(runs), 1)
        self.assertEqual(runs[0].head_sha, _HEAD_SHA)
        _, kwargs = session.get.call_args
        self.assertEqual(
            kwargs["params"],
            {
                "event": "pull_request",
                "head_sha": _HEAD_SHA,
                "per_page": 100,
                "page": 1,
            },
        )

    def test_empty_exact_head_result_is_explicit_not_successful_ci(self) -> None:
        session = Mock()
        session.get.return_value = _response(
            {"total_count": 0, "workflow_runs": []}
        )

        runs = GitHubActionsClient(session=session).get_exact_head_workflow_runs(
            _identity()
        )
        self.assertEqual(runs, ())

    def test_rejects_run_for_different_head(self) -> None:
        session = Mock()
        session.get.return_value = _response(
            {
                "total_count": 1,
                "workflow_runs": [_run(1, head_sha="different")],
            }
        )

        with self.assertRaises(GitHubResponseError):
            GitHubActionsClient(session=session).get_exact_head_workflow_runs(
                _identity()
            )

    def test_acquires_all_workflow_run_pages(self) -> None:
        first = _response(
            {"total_count": 101, "workflow_runs": [_run(i) for i in range(100)]}
        )
        second = _response({"total_count": 101, "workflow_runs": [_run(100)]})
        session = Mock()
        session.get.side_effect = [first, second]

        runs = GitHubActionsClient(session=session).get_exact_head_workflow_runs(
            _identity()
        )

        self.assertEqual(len(runs), 101)
        pages = [call.kwargs["params"]["page"] for call in session.get.call_args_list]
        self.assertEqual(pages, [1, 2])

    def test_acquires_jobs_and_step_summaries_for_run(self) -> None:
        session = Mock()
        session.get.return_value = _response(
            {
                "total_count": 1,
                "jobs": [
                    {
                        "id": 3001,
                        "run_id": 1001,
                        "name": "test (3.10, ubuntu-latest)",
                        "head_sha": _HEAD_SHA,
                        "status": "completed",
                        "conclusion": "success",
                        "steps": [
                            {
                                "number": 1,
                                "name": "Set up job",
                                "status": "completed",
                                "conclusion": "success",
                            },
                            {
                                "number": 2,
                                "name": "Test with tox",
                                "status": "completed",
                                "conclusion": "success",
                            },
                        ],
                    }
                ],
            }
        )
        client = GitHubActionsClient(session=session)
        run = WorkflowRun(
            run_id=1001,
            workflow_id=2001,
            name="Workflow 1",
            event="pull_request",
            head_sha=_HEAD_SHA,
            status="completed",
            conclusion="success",
            run_attempt=1,
        )

        jobs = client.get_workflow_jobs(_identity(), run)

        self.assertEqual(len(jobs), 1)
        self.assertEqual(jobs[0].run_id, run.run_id)
        assert jobs[0].steps is not None
        self.assertEqual(jobs[0].steps[1].name, "Test with tox")
        _, kwargs = session.get.call_args
        self.assertEqual(
            kwargs["params"],
            {"filter": "latest", "per_page": 100, "page": 1},
        )

    def test_rejects_job_for_different_head(self) -> None:
        session = Mock()
        session.get.return_value = _response(
            {
                "total_count": 1,
                "jobs": [
                    {
                        "id": 3001,
                        "run_id": 1001,
                        "name": "test",
                        "head_sha": "different",
                        "status": "completed",
                        "conclusion": "success",
                        "steps": [],
                    }
                ],
            }
        )
        client = GitHubActionsClient(session=session)
        run = WorkflowRun(
            run_id=1001,
            workflow_id=2001,
            name="Workflow 1",
            event="pull_request",
            head_sha=_HEAD_SHA,
            status="completed",
            conclusion="success",
            run_attempt=1,
        )

        with self.assertRaises(GitHubResponseError):
            client.get_workflow_jobs(_identity(), run)


if __name__ == "__main__":
    unittest.main()
