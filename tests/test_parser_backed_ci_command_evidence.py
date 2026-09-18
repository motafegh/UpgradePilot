from __future__ import annotations

import unittest

from upgradepilot.ci.workflow_commands import inspect_workflow_dependency_evidence
from upgradepilot.dependency.change import DependencyChangeSourceEvidence
from upgradepilot.dependency.environment import RequirementsFileDependencyContext
from upgradepilot.github.repository import RepositoryTextFile


_HEAD_SHA = "a" * 40
_PATH = ".github/workflows/ci.yml"


def _source(content: str) -> RepositoryTextFile:
    return RepositoryTextFile(
        repository="example/project",
        path=_PATH,
        revision=_HEAD_SHA,
        content=content,
    )


def _requirements_context() -> RequirementsFileDependencyContext:
    evidence = DependencyChangeSourceEvidence(
        path="requirements-dev.txt",
        file_format="exact_requirement",
        extraction_method="changed_file_patch",
    )
    return RequirementsFileDependencyContext(
        repository="example/project",
        revision=_HEAD_SHA,
        normalized_package="pytest",
        source_evidence=evidence,
    )


class ParserBackedCICommandEvidenceTests(unittest.TestCase):
    def test_one_analysis_supplies_direct_requirements_and_package_invocation_locations(
        self,
    ) -> None:
        workflow = """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: |
          pip install -r requirements-dev.txt
          pytest tests
"""

        result = inspect_workflow_dependency_evidence(
            _source(workflow),
            source_contexts=(_requirements_context(),),
            package="pytest",
            normalized_package="pytest",
        )

        self.assertEqual(result.problems, ())
        self.assertEqual(len(result.consumptions), 1)
        self.assertEqual(len(result.invocations), 1)

        consumption = result.consumptions[0]
        invocation = result.invocations[0]

        self.assertEqual(consumption.state, "supported")
        self.assertIsNotNone(consumption.command_location)
        assert consumption.command_location is not None
        self.assertEqual(consumption.command_location.source_order, 0)
        self.assertEqual(
            consumption.whole_step_relation,
            "first_ordinary_top_level_command_in_sequential_script",
        )
        self.assertEqual(
            consumption.execution_profile,
            "github_default_non_windows",
        )

        self.assertEqual(invocation.state, "observed")
        self.assertIsNotNone(invocation.command_location)
        assert invocation.command_location is not None
        self.assertEqual(invocation.command_location.source_order, 1)
        self.assertIsNone(invocation.whole_step_relation)
        self.assertEqual(
            invocation.execution_profile,
            "github_default_non_windows",
        )
        self.assertEqual(invocation.workflow_path, _PATH)
        self.assertEqual(invocation.workflow_revision, _HEAD_SHA)

    def test_quoted_package_text_does_not_manufacture_invocation(self) -> None:
        workflow = """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: |
          pip install -r requirements-dev.txt
          echo "pytest tests"
"""

        result = inspect_workflow_dependency_evidence(
            _source(workflow),
            source_contexts=(_requirements_context(),),
            package="pytest",
            normalized_package="pytest",
        )

        self.assertEqual(len(result.consumptions), 1)
        self.assertEqual(result.invocations, ())

    def test_other_repository_checkout_does_not_rebind_parsed_evidence(self) -> None:
        workflow = """jobs:
  external:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          repository: example/other
      - run: |
          pip install -r requirements-dev.txt
          pytest tests
"""

        result = inspect_workflow_dependency_evidence(
            _source(workflow),
            source_contexts=(_requirements_context(),),
            package="pytest",
            normalized_package="pytest",
        )

        self.assertEqual(result.consumptions, ())
        self.assertEqual(result.invocations, ())

    def test_missing_static_runner_context_preserves_requirements_uncertainty(self) -> None:
        workflow = """jobs:
  test:
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements-dev.txt
"""

        result = inspect_workflow_dependency_evidence(
            _source(workflow),
            source_contexts=(_requirements_context(),),
            package="pytest",
            normalized_package="pytest",
        )

        self.assertEqual(len(result.consumptions), 1)
        self.assertEqual(result.consumptions[0].state, "unresolved")
        self.assertEqual(
            result.consumptions[0].reason,
            "direct_install_command_analysis_unresolved",
        )
        self.assertIsNone(result.consumptions[0].command_location)


if __name__ == "__main__":
    unittest.main()
