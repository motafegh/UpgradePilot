"""Selected CI job identity is an input, not a Target inference or runtime proof."""

from __future__ import annotations

import unittest

from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.target.artifact_environment import (
    TargetArtifactEnvironmentEvidence,
    TargetArtifactEnvironmentProblem,
    interpret_target_artifact_environment,
)

_REVISION = "b" * 40


def _workflow_file(content: str) -> RepositoryTextFile:
    return RepositoryTextFile(
        repository="example/project",
        path=".github/workflows/ci.yml",
        revision=_REVISION,
        content=content,
    )


class SelectedConsumingJobTests(unittest.TestCase):
    def test_selected_job_is_interpreted_when_an_unrelated_job_also_exists(self) -> None:
        workflow = _workflow_file(
            """jobs:
  test:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: "3.9"
      - run: pip install -r requirements.txt
  lint:
    runs-on: windows-latest
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python -m compileall src
"""
        )
        result = interpret_target_artifact_environment(
            workflow,
            dependency_source_file="requirements.txt",
            consuming_job_key="test",
        )
        self.assertIsInstance(result, TargetArtifactEnvironmentEvidence)
        assert isinstance(result, TargetArtifactEnvironmentEvidence)
        self.assertEqual(result.job, "test")
        self.assertEqual(result.python_version.value if result.python_version else None, "3.9")
        self.assertEqual(result.runner.value if result.runner else None, "ubuntu-22.04")
        self.assertEqual(result.dependency_installation_declaration, "observed")
        self.assertEqual(result.exact_wheel_compatibility_state, "unresolved")

        # Direct legacy calls without the independently established selection remain conservative.
        unselected = interpret_target_artifact_environment(
            workflow,
            dependency_source_file="requirements.txt",
        )
        self.assertIsInstance(unselected, TargetArtifactEnvironmentProblem)
        assert isinstance(unselected, TargetArtifactEnvironmentProblem)
        self.assertEqual(unselected.state, "ambiguous_target_job_selection")

    def test_missing_selected_key_must_not_fall_back_to_an_unrelated_job(self) -> None:
        workflow = _workflow_file(
            """jobs:
  lint:
    runs-on: windows-latest
    steps:
      - run: python -m compileall src
"""
        )
        result = interpret_target_artifact_environment(
            workflow,
            dependency_source_file="requirements.txt",
            consuming_job_key="test",
        )
        self.assertIsInstance(result, TargetArtifactEnvironmentProblem)
        assert isinstance(result, TargetArtifactEnvironmentProblem)
        self.assertEqual(result.state, "selected_target_job_not_found")
        self.assertEqual(result.job, "test")
        self.assertEqual(result.revision, _REVISION)

    def test_selected_reusable_job_stays_unsupported(self) -> None:
        workflow = _workflow_file(
            """jobs:
  delegated:
    uses: ./.github/workflows/reusable.yml
  lint:
    runs-on: ubuntu-latest
    steps:
      - run: python -m compileall src
"""
        )
        result = interpret_target_artifact_environment(
            workflow,
            dependency_source_file="requirements.txt",
            consuming_job_key="delegated",
        )
        self.assertIsInstance(result, TargetArtifactEnvironmentProblem)
        assert isinstance(result, TargetArtifactEnvironmentProblem)
        self.assertEqual(result.state, "unsupported_target_job")
        self.assertEqual(result.job, "delegated")

    def test_empty_selected_key_is_not_a_valid_job_identity(self) -> None:
        workflow = _workflow_file(
            """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: pip install -r requirements.txt
"""
        )
        with self.assertRaises(ValueError):
            interpret_target_artifact_environment(
                workflow,
                dependency_source_file="requirements.txt",
                consuming_job_key="",
            )


if __name__ == "__main__":
    unittest.main()
