"""Test CI-specific static path interpretation independently from runtime authority.

The provider parser and dependency install observer are tested in their own suites. This
file protects the CI-only composition that remains here: one bounded static steps job,
an independently established direct requirements path, direct package invocation, and
install-before-invocation source order.
"""

from __future__ import annotations

import unittest

from upgradepilot.ci.workflow_commands import inspect_workflow_commands
from upgradepilot.github.repository import RepositoryTextFile


class WorkflowCommandTests(unittest.TestCase):
    """Protect the static CI path without implying runtime execution."""

    def test_reads_ordered_named_step_commands(self) -> None:
        workflow = """jobs:
  test:
    steps:
      - name: Install
        run: pip install -r requirements-dev.txt
      - name: Test
        run: pytest tests
"""

        result = _inspect(workflow)

        self.assertEqual(result.status, "supported")
        self.assertEqual(result.reason, "ordered_static_dependency_path_declared")
        self.assertEqual(result.job_key, "test")
        self.assertEqual(result.install_step_source_index, 0)
        self.assertEqual(result.execution_step_source_index, 1)

    def test_reads_ordered_commands_inside_one_run_block(self) -> None:
        workflow = """jobs:
  test:
    steps:
      - run: |
          pip install -r requirements-dev.txt
          pytest tests
"""

        result = _inspect(workflow)

        self.assertEqual(result.status, "supported")
        self.assertEqual(result.install_step_source_index, 0)
        self.assertEqual(result.execution_step_source_index, 0)

    def test_invocation_before_install_is_unresolved(self) -> None:
        workflow = """jobs:
  test:
    steps:
      - run: |
          pytest tests
          pip install -r requirements-dev.txt
"""

        result = _inspect(workflow)

        self.assertEqual(result.status, "unresolved")
        self.assertEqual(result.reason, "static_install_not_before_invocation")

    def test_multiple_jobs_remain_unresolved_without_job_correlation(self) -> None:
        workflow = """jobs:
  unit:
    steps:
      - run: pip install -r requirements-dev.txt
      - run: pytest tests
  lint:
    steps:
      - run: ruff check .
"""

        result = _inspect(workflow)

        self.assertEqual(result.status, "unresolved")
        self.assertEqual(result.reason, "multiple_or_zero_workflow_jobs")


def _inspect(content: str):
    return inspect_workflow_commands(
        RepositoryTextFile(
            repository="example/project",
            path=".github/workflows/ci.yml",
            revision="a" * 40,
            content=content,
        ),
        source_file="requirements-dev.txt",
        package="pytest",
        normalized_package="pytest",
    )


if __name__ == "__main__":
    unittest.main()
