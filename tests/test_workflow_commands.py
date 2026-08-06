"""Test the supported workflow-command reader independently from CI authority.

Purpose of this test file
-------------------------
``upgradepilot.ci.workflow_commands`` is intentionally a shallow text reader rather
than a full YAML or shell evaluator. These focused examples verify two supported
shapes:

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

from upgradepilot.ci.workflow_commands import inspect_workflow_commands


class WorkflowCommandTests(unittest.TestCase):
    """Protect command extraction separately from run/job success interpretation."""

    def test_reads_named_step_block_commands(self) -> None:
        """Inline run values under named steps should satisfy the direct command rule."""

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
        """A list-item block scalar should expose both visible command lines."""

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
