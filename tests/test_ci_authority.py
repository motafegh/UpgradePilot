"""Test the first bounded CI-authority rule with fully constructed evidence.

Purpose of this test file
-------------------------
``ci_authority.py`` performs deterministic interpretation only. It receives a
supported dependency identity, validated workflow runs/jobs, and exact-revision
workflow-file evidence. These tests construct those records directly, so no HTTP,
JSON parsing, pagination, or base64 decoding is involved.

The suite protects the distinction among:

* ``sufficient`` — one successful exact-head workflow directly installs and invokes
  the changed dependency;
* ``insufficient`` — required successful execution evidence is positively absent;
* ``unresolved`` — relevant CI exists, but command indirection, multiple jobs, or
  unavailable workflow text prevents proof.

A sufficient result here remains deliberately narrow. It does not prove complete
test coverage, compatibility, upgrade safety, or a merge recommendation.
"""

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

# Fixed provenance keeps every normal fixture on the same revision and workflow path.
_HEAD_SHA = "f3cda8a94600e58d27f1bc17c99b7693718b6350"
_PATH = ".github/workflows/regression.yml"


def _dependency() -> PinnedDependencyChange:
    """Build the already-proven dependency question evaluated by every test."""

    return PinnedDependencyChange(
        source_file="requirements-dev.txt",
        package="pytest",
        normalized_package="pytest",
        old_version="9.0.2",
        proposed_version="9.0.3",
    )


def _run(*, conclusion: str | None = "success") -> WorkflowRun:
    """Build a completed exact-head run while varying only its conclusion.

    The keyword-only parameter makes failure scenarios explicit. ``status`` remains
    completed, allowing tests to isolate final conclusion rather than lifecycle state.
    """

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
    """Build a completed exact-head job while varying only its conclusion."""

    return WorkflowJob(
        job_id=3001,
        run_id=1001,
        name="test",
        head_sha=_HEAD_SHA,
        status="completed",
        conclusion=conclusion,
        # An explicit empty tuple means GitHub supplied zero step summaries. Command
        # authority in these tests comes from workflow text, not step display metadata.
        steps=(),
    )


def _definition(content: str) -> RepositoryTextFile:
    """Attach supplied workflow text to the same exact revision and path."""

    return RepositoryTextFile(
        path=_PATH,
        revision=_HEAD_SHA,
        blob_sha="blob-sha",
        content=content,
    )


class CIAuthorityTests(unittest.TestCase):
    """Protect sufficient, insufficient, and unresolved authority classifications."""

    def test_sufficient_when_single_job_installs_and_invokes_dependency(self) -> None:
        """One successful job with both direct commands should satisfy the rule."""

        workflow = """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: |
          pip install -r requirements.txt -r requirements-dev.txt
          pytest tests
"""

        # ``WorkflowAuthorityInput`` keeps one run, its jobs, and its definition in a
        # single bundle so evidence from unrelated workflows cannot be mixed.
        result = evaluate_ci_authority(
            _dependency(),
            [WorkflowAuthorityInput(_run(), (_job(),), _definition(workflow))],
        )

        self.assertEqual(result.status, "sufficient")
        self.assertEqual(result.reason, "exact_head_dependency_exercised")

        # The assessment retains the actual matched commands, making the classification
        # inspectable rather than a bare status.
        self.assertIsNotNone(result.workflows[0].install_command)
        self.assertIsNotNone(result.workflows[0].execution_command)

    def test_green_tox_workflow_remains_unresolved_without_config_trace(self) -> None:
        """Successful tox execution is indirect until its configuration is traced."""

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

        # The workflow is green, so execution evidence exists. However, visible text
        # does not prove that tox installed the changed file or invoked pytest directly.
        self.assertEqual(result.status, "unresolved")
        self.assertEqual(
            result.workflows[0].reason,
            "direct_dependency_exercise_not_proven",
        )

    def test_multiple_jobs_remain_unresolved_to_avoid_cross_job_inference(self) -> None:
        """Install and invocation in separate jobs must not be combined heuristically."""

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

        # Separate jobs may run on different machines and environments. The current
        # single-job rule therefore abstains rather than joining their commands.
        self.assertEqual(result.status, "unresolved")
        self.assertEqual(
            result.workflows[0].reason,
            "multiple_or_zero_workflow_jobs",
        )

    def test_no_successful_exact_head_jobs_is_insufficient(self) -> None:
        """Failed run and job evidence positively lacks the required successful path."""

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

        # This is insufficient rather than unresolved because the evidence positively
        # establishes that no completed-successful exact-head job is present.
        self.assertEqual(result.status, "insufficient")
        self.assertEqual(result.reason, "no_successful_exact_head_jobs")

    def test_unavailable_workflow_definition_is_unresolved(self) -> None:
        """A green run cannot prove commands when exact-revision text is unavailable."""

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

        # Unavailable text is not evidence that the commands were absent. The honest
        # state remains unresolved because the command question cannot be evaluated.
        self.assertEqual(result.status, "unresolved")
        self.assertEqual(
            result.workflows[0].reason,
            "workflow_definition_unavailable",
        )


if __name__ == "__main__":
    unittest.main()
