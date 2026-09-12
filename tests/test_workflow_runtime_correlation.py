from __future__ import annotations

import unittest

from upgradepilot.ci.workflow_runtime_correlation import correlate_workflow_runtime
from upgradepilot.github.actions import WorkflowJob, WorkflowRun, WorkflowStep
from upgradepilot.github.repository import RepositoryTextFile

_REPOSITORY = "example/project"
_HEAD_SHA = "a" * 40
_WORKFLOW_PATH = ".github/workflows/ci.yml"


def _source(content: str) -> RepositoryTextFile:
    return RepositoryTextFile(
        repository=_REPOSITORY,
        path=_WORKFLOW_PATH,
        revision=_HEAD_SHA,
        content=content.lstrip(),
    )


def _run() -> WorkflowRun:
    return WorkflowRun(
        run_id=1001,
        workflow_id=2001,
        name="CI",
        event="pull_request",
        head_sha=_HEAD_SHA,
        status="completed",
        conclusion="success",
        run_attempt=2,
    )


def _step(
    number: int,
    name: str,
    *,
    status: str = "completed",
    conclusion: str | None = "success",
) -> WorkflowStep:
    return WorkflowStep(
        number=number,
        name=name,
        status=status,
        conclusion=conclusion,
    )


def _job(
    job_id: int,
    name: str,
    steps: tuple[WorkflowStep, ...] | None,
) -> WorkflowJob:
    return WorkflowJob(
        job_id=job_id,
        run_id=1001,
        name=name,
        head_sha=_HEAD_SHA,
        status="completed",
        conclusion="success",
        steps=steps,
    )


class WorkflowRuntimeCorrelationTests(unittest.TestCase):
    def test_correlates_named_jobs_and_user_steps_as_runtime_subsequences(self) -> None:
        source = _source(
            """
jobs:
  build:
    name: Build project
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4
      - name: Install dependencies
        run: pip install -r requirements.txt
  test:
    name: Run tests
    runs-on: ubuntu-latest
    steps:
      - name: Execute tests
        run: python -m unittest
"""
        )
        jobs = (
            _job(
                502,
                "Run tests",
                (
                    _step(1, "Set up job"),
                    _step(3, "Execute tests"),
                    _step(8, "Complete job"),
                ),
            ),
            _job(
                501,
                "Build project",
                (
                    _step(1, "Set up job"),
                    _step(2, "Check out repository"),
                    _step(4, "Install dependencies"),
                    _step(9, "Post Check out repository"),
                    _step(10, "Complete job"),
                ),
            ),
        )

        result = correlate_workflow_runtime(source, _run(), jobs)

        self.assertEqual(result.state, "correlated")
        self.assertEqual(
            [correlation.static_job.key for correlation in result.jobs],
            ["build", "test"],
        )
        self.assertEqual(
            [correlation.runtime_job.job_id for correlation in result.jobs],
            [501, 502],
        )
        self.assertEqual(
            [step.runtime_step.number for step in result.jobs[0].steps],
            [2, 4],
        )
        self.assertEqual(
            [step.static_step.source_index for step in result.jobs[0].steps],
            [0, 1],
        )

    def test_matrix_or_other_strategy_is_unresolved(self) -> None:
        source = _source(
            """
jobs:
  test:
    name: Python ${{ matrix.python-version }}
    strategy:
      matrix:
        python-version: ["3.12", "3.13"]
    runs-on: ubuntu-latest
    steps:
      - name: Run tests
        run: python -m unittest
"""
        )

        result = correlate_workflow_runtime(
            source,
            _run(),
            (
                _job(501, "Python 3.12", (_step(1, "Run tests"),)),
                _job(502, "Python 3.13", (_step(1, "Run tests"),)),
            ),
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "static_job_strategy_unsupported")

    def test_reusable_workflow_job_is_unresolved(self) -> None:
        source = _source(
            """
jobs:
  delegated:
    name: Delegated tests
    uses: org/repo/.github/workflows/tests.yml@main
"""
        )

        result = correlate_workflow_runtime(
            source,
            _run(),
            (_job(501, "Delegated tests", ()),),
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "reusable_workflow_job_unsupported")

    def test_job_requires_explicit_literal_name(self) -> None:
        missing = correlate_workflow_runtime(
            _source(
                """
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Run tests
        run: python -m unittest
"""
            ),
            _run(),
            (_job(501, "test", (_step(1, "Run tests"),)),),
        )
        dynamic = correlate_workflow_runtime(
            _source(
                """
jobs:
  test:
    name: Test ${{ github.sha }}
    runs-on: ubuntu-latest
    steps:
      - name: Run tests
        run: python -m unittest
"""
            ),
            _run(),
            (_job(501, "Test abc", (_step(1, "Run tests"),)),),
        )

        self.assertEqual(missing.reason, "static_job_name_missing")
        self.assertEqual(dynamic.reason, "static_job_name_dynamic")

    def test_duplicate_static_or_runtime_job_names_are_unresolved(self) -> None:
        duplicate_static = correlate_workflow_runtime(
            _source(
                """
jobs:
  one:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: First
        run: echo first
  two:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Second
        run: echo second
"""
            ),
            _run(),
            (_job(501, "Tests", (_step(1, "First"),)),),
        )
        duplicate_runtime = correlate_workflow_runtime(
            _source(
                """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Run tests
        run: python -m unittest
"""
            ),
            _run(),
            (
                _job(501, "Tests", (_step(1, "Run tests"),)),
                _job(502, "Tests", (_step(1, "Run tests"),)),
            ),
        )

        self.assertEqual(duplicate_static.reason, "duplicate_static_job_name")
        self.assertEqual(duplicate_runtime.reason, "duplicate_runtime_job_name")

    def test_static_and_runtime_job_name_sets_must_match_exactly(self) -> None:
        result = correlate_workflow_runtime(
            _source(
                """
jobs:
  build:
    name: Build
    runs-on: ubuntu-latest
    steps:
      - name: Build package
        run: python -m build
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Run tests
        run: python -m unittest
"""
            ),
            _run(),
            (_job(501, "Build", (_step(1, "Build package"),)),),
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "static_runtime_job_name_set_mismatch")

    def test_steps_require_explicit_literal_unique_names(self) -> None:
        missing = correlate_workflow_runtime(
            _source(
                """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - run: python -m unittest
"""
            ),
            _run(),
            (_job(501, "Tests", (_step(1, "python -m unittest"),)),),
        )
        dynamic = correlate_workflow_runtime(
            _source(
                """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Run ${{ github.sha }}
        run: python -m unittest
"""
            ),
            _run(),
            (_job(501, "Tests", (_step(1, "Run abc"),)),),
        )
        duplicate = correlate_workflow_runtime(
            _source(
                """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Check
        run: echo one
      - name: Check
        run: echo two
"""
            ),
            _run(),
            (_job(501, "Tests", (_step(1, "Check"),)),),
        )

        self.assertEqual(missing.reason, "static_step_name_missing")
        self.assertEqual(dynamic.reason, "static_step_name_dynamic")
        self.assertEqual(duplicate.reason, "duplicate_static_step_name")

    def test_runtime_step_numbers_must_be_unique_and_ordered(self) -> None:
        source = _source(
            """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Install
        run: pip install .
      - name: Run tests
        run: python -m unittest
"""
        )
        duplicate = correlate_workflow_runtime(
            source,
            _run(),
            (_job(501, "Tests", (_step(2, "Install"), _step(2, "Run tests"))),),
        )
        unordered = correlate_workflow_runtime(
            source,
            _run(),
            (_job(501, "Tests", (_step(3, "Install"), _step(2, "Run tests"))),),
        )

        self.assertEqual(duplicate.reason, "duplicate_runtime_step_number")
        self.assertEqual(unordered.reason, "runtime_step_numbers_not_ordered")

    def test_each_static_step_must_have_one_runtime_name_match(self) -> None:
        source = _source(
            """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Install
        run: pip install .
"""
        )
        missing = correlate_workflow_runtime(
            source,
            _run(),
            (_job(501, "Tests", (_step(1, "Set up job"),)),),
        )
        ambiguous = correlate_workflow_runtime(
            source,
            _run(),
            (
                _job(
                    501,
                    "Tests",
                    (_step(1, "Install"), _step(2, "Install")),
                ),
            ),
        )

        self.assertEqual(missing.reason, "runtime_step_match_missing")
        self.assertEqual(ambiguous.reason, "runtime_step_match_ambiguous")

    def test_user_step_name_order_must_be_preserved(self) -> None:
        source = _source(
            """
jobs:
  test:
    name: Tests
    runs-on: ubuntu-latest
    steps:
      - name: Install
        run: pip install .
      - name: Run tests
        run: python -m unittest
"""
        )

        result = correlate_workflow_runtime(
            source,
            _run(),
            (
                _job(
                    501,
                    "Tests",
                    (_step(1, "Run tests"), _step(2, "Install")),
                ),
            ),
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "static_runtime_step_order_mismatch")


if __name__ == "__main__":
    unittest.main()
