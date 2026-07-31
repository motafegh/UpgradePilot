"""Test the first bounded CI-authority rule with fully constructed evidence.

``ci_authority.py`` receives a canonical dependency identity, exact-head workflow
runs/jobs, exact-revision workflow text, and—only when independently established—an
explicit direct-requirements installation path. Generic dependency evidence paths must
never be promoted into CI-consumption proof by convenience.
"""

from __future__ import annotations

import unittest

from upgradepilot.ci_authority import (
    WorkflowAuthorityInput,
    evaluate_ci_authority,
)
from upgradepilot.dependency_change import (
    DependencyFileEvidence,
    DependencyVersionChange,
)
from upgradepilot.github_actions import WorkflowJob, WorkflowRun
from upgradepilot.github_repository import (
    RepositoryTextFile,
    UnavailableRepositoryFile,
)

_HEAD_SHA = "f3cda8a94600e58d27f1bc17c99b7693718b6350"
_PATH = ".github/workflows/regression.yml"
_DIRECT_REQUIREMENTS_PATH = "requirements-dev.txt"


def _dependency(
    *,
    evidence_path: str = _DIRECT_REQUIREMENTS_PATH,
    file_format: str = "exact_requirement",
) -> DependencyVersionChange:
    """Build the canonical dependency identity evaluated by every test."""

    return DependencyVersionChange(
        package="pytest",
        normalized_package="pytest",
        old_version="9.0.2",
        proposed_version="9.0.3",
        source_evidence=(
            DependencyFileEvidence(
                path=evidence_path,
                file_format=file_format,  # type: ignore[arg-type]
                extraction_method=(
                    "exact_base_head_files"
                    if file_format == "uv_lock"
                    else "changed_file_patch"
                ),
            ),
        ),
    )


def _run(*, conclusion: str | None = "success") -> WorkflowRun:
    """Build a completed exact-head run while varying only its conclusion."""

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


def _evaluate(
    workflow: str,
    *,
    dependency: DependencyVersionChange | None = None,
    direct_requirements_install_path: str | None = _DIRECT_REQUIREMENTS_PATH,
    run_conclusion: str | None = "success",
    job_conclusion: str | None = "success",
):
    """Apply the evaluator with one controlled workflow evidence bundle."""

    return evaluate_ci_authority(
        dependency or _dependency(),
        [
            WorkflowAuthorityInput(
                _run(conclusion=run_conclusion),
                (_job(conclusion=job_conclusion),),
                _definition(workflow),
            )
        ],
        direct_requirements_install_path=direct_requirements_install_path,
    )


class CIAuthorityTests(unittest.TestCase):
    """Protect sufficient, insufficient, and unresolved authority classifications."""

    def test_sufficient_when_explicit_path_is_installed_and_package_invoked(self) -> None:
        workflow = """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: |
          pip install -r requirements.txt -r requirements-dev.txt
          pytest tests
"""

        result = _evaluate(workflow)

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

        result = _evaluate(workflow)

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

        result = _evaluate(workflow)

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

        result = _evaluate(
            workflow,
            run_conclusion="failure",
            job_conclusion="failure",
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
            direct_requirements_install_path=_DIRECT_REQUIREMENTS_PATH,
        )

        self.assertEqual(result.status, "unresolved")
        self.assertEqual(
            result.workflows[0].reason,
            "workflow_definition_unavailable",
        )

    def test_generic_evidence_path_never_becomes_installation_proof(self) -> None:
        """A tempting uv/constraints path cannot substitute for explicit CI input."""

        cases = (
            ("uv.lock", "uv_lock", "pip install -r uv.lock"),
            (
                "constraints/base.txt",
                "exact_requirement",
                "pip install -r constraints/base.txt",
            ),
        )

        for evidence_path, file_format, install_command in cases:
            with self.subTest(evidence_path=evidence_path):
                workflow = f"""jobs:
  test:
    steps:
      - run: |
          {install_command}
          pytest tests
"""
                result = _evaluate(
                    workflow,
                    dependency=_dependency(
                        evidence_path=evidence_path,
                        file_format=file_format,
                    ),
                    direct_requirements_install_path=None,
                )

                self.assertEqual(result.status, "unresolved")
                self.assertEqual(
                    result.workflows[0].reason,
                    "direct_requirements_install_path_unavailable",
                )
                self.assertIsNone(result.workflows[0].install_command)
                self.assertEqual(result.workflows[0].execution_command, None)


if __name__ == "__main__":
    unittest.main()
