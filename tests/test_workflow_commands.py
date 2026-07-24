"""Focused tests for the shallow workflow command reader."""

from __future__ import annotations

import unittest

from upgradepilot.workflow_commands import inspect_workflow_commands


class WorkflowCommandTests(unittest.TestCase):
    """Protect command extraction separately from overall authority logic."""

    def test_reads_named_step_block_commands(self) -> None:
        workflow = """jobs:
  test:
    steps:
      - name: Install
        run: pip install -r requirements-dev.txt
      - name: Test
        run: pytest tests
"""

        result = inspect_workflow_commands(
            workflow,
            source_file="requirements-dev.txt",
            package="pytest",
            normalized_package="pytest",
        )

        self.assertEqual(result.status, "supported")

    def test_reads_dash_run_block_commands(self) -> None:
        workflow = """jobs:
  test:
    steps:
      - run: |
          pip install -r requirements-dev.txt
          pytest tests
"""

        result = inspect_workflow_commands(
            workflow,
            source_file="requirements-dev.txt",
            package="pytest",
            normalized_package="pytest",
        )

        self.assertEqual(result.status, "supported")


if __name__ == "__main__":
    unittest.main()
