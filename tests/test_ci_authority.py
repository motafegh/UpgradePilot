"""Deterministic tests for the first bounded CI-authority rule."""

from __future__ import annotations

import unittest

from upgradepilot.ci_authority import (
    WorkflowAuthorityInput,
    evaluate_ci_authority,
)
from upgradepilot.dependency_change import PinnedDependencyChange
from upgradepilot.github_actions import WorkflowJob, WorkflowRun
from upgradepilot.github_repository import (
    RepositoryTextFile,
    UnavailableRepositoryFile,
)

_HEAD_SHA = "f3cda8a94600e58d27f1bc17c99b7693718b6350"
_PATH = ".github/workflows/regression.yml"


def _dependency() -> PinnedDependencyChange:
    return PinnedDependencyChange(
        source_file="requirements-dev.txt",
        package="pytest",
        normalized_package="pytest",
        old_version="9.0.2",
        proposed_version="9.0.3",
    )


def _run(*, conclusion: str | None = "success") -> WorkflowRun:
    return WorkflowRun(
        run_id=1001,
        workflow_id=2001,
        name="Regression Tests",
        event="pull_request",
        head_sha=_HEAD_SHA,
        status="completed",
        conclusion=conclusion,
        run_attempt=1,
    )


def _job(*, conclusion: str | None = "success") -> WorkflowJob:
    return WorkflowJob(
        job_id=3001,
        run_id=1001,
        name="test",
        head_sha=_HEAD_SHA,
        status="completed",
        conclusion=conclusion,
        steps=(),
    )


def _definition(content: str) -> RepositoryTextFile:
    return RepositoryTextFile(
        path=_PATH,
        revision=_HEAD_SHA,
        blob_sha="blob-sha",
        content=content,
    )


class CIAuthorityTests(unittest.TestCase):
    """Protect sufficient, insufficient, and unresolved authority outcomes."""

    def test_sufficient_when_single_job_installs_and_invokes_dependency(self) -> None:
        workflow = """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: |
          pip install -r requirements.txt -r requirements-dev.txt
          pytest tests
"""

        result = evaluate_ci_authority(
            _dependency(),
            [WorkflowAuthorityInput(_run(), (_job(),), _definition(workflow))],
        )

        self.assertEqual(result.status, "sufficient")
        self.assertEqual(result.reason, "exact_head_dependency_exercised")
        self.assertIsNotNone(result.workflows[0].install_command)
        self.assertIsNotNone(result.workflows[0].execution_command)

    def test_green_tox_workflow_remains_unresolved_without_config_trace(self) -> None:
        workflow = """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: pip install tox
      - run: tox -e py
"""

        result = evaluate_ci_authority(
            _dependency(),
            [WorkflowAuthorityInput(_run(), (_job(),), _definition(workflow))],
        )

        self.assertEqual(result.status, "unresolved")
        self.assertEqual(
            result.workflows[0].reason,
            "direct_dependency_exercise_not_proven",
        )

    def test_multiple_jobs_remain_unresolved_to_avoid_cross_job_inference(self) -> None:
        workflow = """jobs:
  install:
    steps:
      - run: pip install -r requirements-dev.txt
  test:
    steps:
      - run: pytest tests
"""

        result = evaluate_ci_authority(
            _dependency(),
            [WorkflowAuthorityInput(_run(), (_job(),), _definition(workflow))],
        )

        self.assertEqual(result.status, "unresolved")
        self.assertEqual(
            result.workflows[0].reason,
            "multiple_or_zero_workflow_jobs",
        )

    def test_no_successful_exact_head_jobs_is_insufficient(self) -> None:
        workflow = """jobs:
  test:
    steps:
      - run: pytest tests
"""

        result = evaluate_ci_authority(
            _dependency(),
            [
                WorkflowAuthorityInput(
                    _run(conclusion="failure"),
                    (_job(conclusion="failure"),),
                    _definition(workflow),
                )
            ],
        )

        self.assertEqual(result.status, "insufficient")
        self.assertEqual(result.reason, "no_successful_exact_head_jobs")

    def test_unavailable_workflow_definition_is_unresolved(self) -> None:
        unavailable = UnavailableRepositoryFile(
            path=_PATH,
            revision=_HEAD_SHA,
            reason="not_found_or_inaccessible",
            detail="No accessible repository-file resource was found.",
        )

        result = evaluate_ci_authority(
            _dependency(),
            [WorkflowAuthorityInput(_run(), (_job(),), unavailable)],
        )

        self.assertEqual(result.status, "unresolved")
        self.assertEqual(
            result.workflows[0].reason,
            "workflow_definition_unavailable",
        )


if __name__ == "__main__":
    unittest.main()
