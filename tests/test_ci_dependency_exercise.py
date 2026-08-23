"""Test the dependency-CI exercise contract with controlled static/runtime evidence.

The evaluator receives canonical dependency identity, exact-head workflow runtime
records, and an exact static workflow definition. The strongest current result is
``supported_not_correlated``: successful exact-head CI exists and the static definition
contains an ordered dependency path, but those static commands are not mapped to runtime
step success.
"""

from __future__ import annotations

import unittest

from upgradepilot.ci.dependency_exercise import (
    WorkflowDependencyExerciseInput,
    evaluate_dependency_ci_exercise,
)
from upgradepilot.dependency.change import (
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.github.actions import WorkflowJob, WorkflowRun
from upgradepilot.github.repository import RepositoryTextFile, UnavailableRepositoryFile

_REPOSITORY = "example/project"
_HEAD_SHA = "f3cda8a94600e58d27f1bc17c99b7693718b6350"
_PATH = ".github/workflows/regression.yml"
_DIRECT_REQUIREMENTS_PATH = "requirements-dev.txt"


def _dependency(
    *,
    evidence_path: str = _DIRECT_REQUIREMENTS_PATH,
    file_format: str = "exact_requirement",
) -> DependencyVersionChange:
    return DependencyVersionChange(
        package="pytest",
        normalized_package="pytest",
        old_version="9.0.2",
        proposed_version="9.0.3",
        source_evidence=(
            DependencyChangeSourceEvidence(
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


def _run(
    *,
    run_id: int = 1001,
    name: str = "Regression Tests",
    status: str = "completed",
    conclusion: str | None = "success",
) -> WorkflowRun:
    return WorkflowRun(
        run_id=run_id,
        workflow_id=2000 + run_id,
        name=name,
        event="pull_request",
        head_sha=_HEAD_SHA,
        status=status,
        conclusion=conclusion,
        run_attempt=1,
    )


def _job(
    *,
    run_id: int = 1001,
    job_id: int = 3001,
    conclusion: str | None = "success",
) -> WorkflowJob:
    return WorkflowJob(
        job_id=job_id,
        run_id=run_id,
        name="test",
        head_sha=_HEAD_SHA,
        status="completed",
        conclusion=conclusion,
        steps=(),
    )


def _definition(
    content: str,
    *,
    path: str = _PATH,
    revision: str = _HEAD_SHA,
) -> RepositoryTextFile:
    return RepositoryTextFile(
        repository=_REPOSITORY,
        path=path,
        revision=revision,
        content=content,
    )


def _input(
    workflow: str,
    *,
    run: WorkflowRun | None = None,
    jobs: tuple[WorkflowJob, ...] | None = None,
    definition: RepositoryTextFile | UnavailableRepositoryFile | None = None,
) -> WorkflowDependencyExerciseInput:
    selected_run = run or _run()
    return WorkflowDependencyExerciseInput(
        run=selected_run,
        jobs=jobs if jobs is not None else (_job(run_id=selected_run.run_id),),
        definition=definition or _definition(workflow),
    )


class DependencyCIExerciseTests(unittest.TestCase):
    """Protect runtime authority, static path support, and their non-correlation."""

    def test_supported_when_static_path_exists_but_runtime_steps_are_not_correlated(self) -> None:
        workflow = """jobs:
  test:
    steps:
      - run: |
          pip install -r requirements.txt -r requirements-dev.txt
          pytest tests
"""

        result = evaluate_dependency_ci_exercise(
            _dependency(),
            [_input(workflow)],
            direct_requirements_install_path=_DIRECT_REQUIREMENTS_PATH,
        )

        self.assertEqual(result.state, "supported_not_correlated")
        self.assertEqual(
            result.reason,
            "successful_exact_head_ci_with_static_dependency_path",
        )
        self.assertEqual(result.workflows[0].state, "supported_not_correlated")
        self.assertEqual(
            result.workflows[0].reason,
            "successful_ci_with_ordered_static_dependency_path",
        )
        self.assertIn("not correlated", result.detail)
        self.assertIsNotNone(result.workflows[0].install_command)
        self.assertIsNotNone(result.workflows[0].execution_command)

    def test_no_workflow_inputs_is_no_successful_ci(self) -> None:
        result = evaluate_dependency_ci_exercise(
            _dependency(),
            [],
            direct_requirements_install_path=_DIRECT_REQUIREMENTS_PATH,
        )

        self.assertEqual(result.state, "no_successful_ci")
        self.assertEqual(result.reason, "no_exact_head_workflows")
        self.assertEqual(result.workflows, ())

    def test_no_completed_successful_job_is_no_successful_ci(self) -> None:
        workflow = """jobs:
  test:
    steps:
      - run: pytest tests
"""
        result = evaluate_dependency_ci_exercise(
            _dependency(),
            [_input(workflow, jobs=(_job(conclusion="failure"),))],
            direct_requirements_install_path=_DIRECT_REQUIREMENTS_PATH,
        )

        self.assertEqual(result.state, "no_successful_ci")
        self.assertEqual(result.reason, "no_successful_exact_head_jobs")
        self.assertEqual(result.workflows[0].state, "no_successful_ci")
        self.assertEqual(result.workflows[0].reason, "no_successful_jobs")

    def test_no_successful_job_precedes_unavailable_definition(self) -> None:
        unavailable = UnavailableRepositoryFile(
            repository=_REPOSITORY,
            path=_PATH,
            revision=_HEAD_SHA,
            reason="not_found_or_inaccessible",
            detail="No accessible repository-file resource was found.",
        )
        result = evaluate_dependency_ci_exercise(
            _dependency(),
            [_input("", jobs=(_job(conclusion="failure"),), definition=unavailable)],
            direct_requirements_install_path=_DIRECT_REQUIREMENTS_PATH,
        )

        self.assertEqual(result.state, "no_successful_ci")
        self.assertEqual(result.workflows[0].reason, "no_successful_jobs")

    def test_successful_job_with_unavailable_definition_is_unresolved(self) -> None:
        unavailable = UnavailableRepositoryFile(
            repository=_REPOSITORY,
            path=_PATH,
            revision=_HEAD_SHA,
            reason="not_found_or_inaccessible",
            detail="No accessible repository-file resource was found.",
        )
        result = evaluate_dependency_ci_exercise(
            _dependency(),
            [_input("", definition=unavailable)],
            direct_requirements_install_path=_DIRECT_REQUIREMENTS_PATH,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.workflows[0].reason, "workflow_definition_unavailable")

    def test_successful_job_with_non_successful_run_is_unresolved(self) -> None:
        workflow = """jobs:
  test:
    steps:
      - run: pytest tests
"""
        result = evaluate_dependency_ci_exercise(
            _dependency(),
            [
                _input(
                    workflow,
                    run=_run(conclusion="failure"),
                    jobs=(_job(conclusion="success"),),
                )
            ],
            direct_requirements_install_path=_DIRECT_REQUIREMENTS_PATH,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.workflows[0].reason, "workflow_not_successful")

    def test_green_tox_workflow_is_unresolved_without_config_trace(self) -> None:
        workflow = """jobs:
  test:
    steps:
      - run: pip install tox
      - run: tox -e py
"""
        result = evaluate_dependency_ci_exercise(
            _dependency(),
            [_input(workflow)],
            direct_requirements_install_path=_DIRECT_REQUIREMENTS_PATH,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.workflows[0].reason, "static_dependency_path_incomplete")

    def test_multiple_workflow_jobs_are_unresolved_without_static_runtime_job_join(self) -> None:
        workflow = """jobs:
  install:
    steps:
      - run: pip install -r requirements-dev.txt
  test:
    steps:
      - run: pytest tests
"""
        result = evaluate_dependency_ci_exercise(
            _dependency(),
            [_input(workflow)],
            direct_requirements_install_path=_DIRECT_REQUIREMENTS_PATH,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.workflows[0].reason, "multiple_or_zero_workflow_jobs")

    def test_static_invocation_before_install_is_unresolved(self) -> None:
        workflow = """jobs:
  test:
    steps:
      - run: pytest tests
      - run: pip install -r requirements-dev.txt
"""
        result = evaluate_dependency_ci_exercise(
            _dependency(),
            [_input(workflow)],
            direct_requirements_install_path=_DIRECT_REQUIREMENTS_PATH,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.workflows[0].reason, "static_install_not_before_invocation")

    def test_missing_explicit_requirements_path_is_unresolved(self) -> None:
        workflow = """jobs:
  test:
    steps:
      - run: |
          pip install -r requirements-dev.txt
          pytest tests
"""
        result = evaluate_dependency_ci_exercise(
            _dependency(),
            [_input(workflow)],
            direct_requirements_install_path=None,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(
            result.workflows[0].reason,
            "direct_requirements_install_path_unavailable",
        )
        self.assertIsNone(result.workflows[0].install_command)
        self.assertIsNone(result.workflows[0].execution_command)

    def test_generic_evidence_paths_never_become_installation_proof(self) -> None:
        cases = (
            ("uv.lock", "uv_lock", "pip install -r uv.lock"),
            (
                "constraints/base.txt",
                "exact_requirement",
                "pip install -r constraints/base.txt",
            ),
        )

        for evidence_path, file_format, command in cases:
            with self.subTest(evidence_path=evidence_path):
                workflow = f"""jobs:
  test:
    steps:
      - run: |
          {command}
          pytest tests
"""
                result = evaluate_dependency_ci_exercise(
                    _dependency(evidence_path=evidence_path, file_format=file_format),
                    [_input(workflow)],
                    direct_requirements_install_path=None,
                )

                self.assertEqual(result.state, "unresolved")
                self.assertEqual(
                    result.workflows[0].reason,
                    "direct_requirements_install_path_unavailable",
                )

    def test_supported_workflow_wins_and_all_results_are_preserved(self) -> None:
        supported_workflow = """jobs:
  test:
    steps:
      - run: |
          pip install -r requirements-dev.txt
          pytest tests
"""
        failed_workflow = """jobs:
  test:
    steps:
      - run: pytest tests
"""
        supported_run = _run(run_id=1001, name="Regression Tests")
        failed_run = _run(run_id=1002, name="Other Tests", conclusion="failure")

        result = evaluate_dependency_ci_exercise(
            _dependency(),
            [
                _input(
                    supported_workflow,
                    run=supported_run,
                    jobs=(_job(run_id=1001, job_id=3001),),
                    definition=_definition(
                        supported_workflow,
                        path=".github/workflows/regression.yml",
                    ),
                ),
                _input(
                    failed_workflow,
                    run=failed_run,
                    jobs=(_job(run_id=1002, job_id=3002, conclusion="failure"),),
                    definition=_definition(
                        failed_workflow,
                        path=".github/workflows/other.yml",
                    ),
                ),
            ],
            direct_requirements_install_path=_DIRECT_REQUIREMENTS_PATH,
        )

        self.assertEqual(result.state, "supported_not_correlated")
        self.assertEqual(len(result.workflows), 2)
        self.assertEqual(result.workflows[0].state, "supported_not_correlated")
        self.assertEqual(result.workflows[1].state, "no_successful_ci")


if __name__ == "__main__":
    unittest.main()
