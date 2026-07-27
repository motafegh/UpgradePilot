"""Test the supported workflow-command reader independently from CI authority.

Purpose of this test file
-------------------------
``workflow_commands.py`` is intentionally a shallow text reader rather than a full
YAML or shell evaluator. These focused examples verify two supported shapes:

* separate named steps with inline ``run:`` values;
* one list-item ``run: |`` block containing multiple command lines.

Both workflows contain one job, installation of the changed requirements file, and
direct invocation of the changed package. The tests therefore expect ``supported``.

These examples do not claim that every GitHub Actions YAML form is supported. Richer
indirection, multiple-job reasoning, and unresolved outcomes are exercised through
the authority tests and production abstention rules.
"""

from __future__ import annotations

import unittest

from upgradepilot.workflow_commands import inspect_workflow_commands


class WorkflowCommandTests(unittest.TestCase):
    """Protect command extraction separately from run/job success interpretation."""

    def test_reads_named_step_block_commands(self) -> None:
        """Inline run values under named steps should satisfy the direct command rule."""

        # This is ordinary Actions YAML with one job and two separately named steps.
        # The reader ignores display names and extracts the visible ``run`` values.
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
            # Keyword arguments prevent the three string identities from being
            # accidentally swapped and show the exact evidence question being asked.
            source_file="requirements-dev.txt",
            package="pytest",
            normalized_package="pytest",
        )

        # This assertion protects the combined outcome. The production evidence record
        # also retains the exact matching install and execution commands.
        self.assertEqual(result.status, "supported")

    def test_reads_dash_run_block_commands(self) -> None:
        """A list-item block scalar should expose both visible command lines."""

        # ``- run: |`` introduces an indented literal block. The shallow reader joins
        # its visible lines, then shell segmentation treats the newline as a boundary.
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
