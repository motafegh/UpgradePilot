from __future__ import annotations

import unittest
from datetime import datetime, timezone

from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.target.artifact_environment import (
    TargetArtifactEnvironmentEvidence,
    TargetArtifactEnvironmentProblem,
    interpret_target_artifact_environment,
)

_REVISION = "b" * 40
_RETRIEVED_AT = datetime(2026, 8, 14, tzinfo=timezone.utc)


class TargetArtifactEnvironmentTests(unittest.TestCase):
    def test_literal_job_preserves_partial_environment_facts_and_formation(self) -> None:
        workflow = """name: ci
jobs:
  test:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements-dev.txt
      - run: pytest
"""

        result = interpret_target_artifact_environment(
            _workflow_file(workflow),
            dependency_source_file="requirements-dev.txt",
        )

        self.assertIsInstance(result, TargetArtifactEnvironmentEvidence)
        assert isinstance(result, TargetArtifactEnvironmentEvidence)
        self.assertEqual(result.repository, "example/project")
        self.assertEqual(result.revision, _REVISION)
        self.assertEqual(result.workflow_path, ".github/workflows/ci.yml")
        self.assertEqual(result.job, "test")
        self.assertEqual(result.runner.value if result.runner else None, "ubuntu-22.04")
        self.assertEqual(
            result.python_version.value if result.python_version else None,
            "3.11",
        )
        self.assertEqual(result.dependency_environment_formation, "established")
        self.assertEqual(
            result.formation_source,
            "pip install -r requirements-dev.txt",
        )
        self.assertEqual(result.exact_wheel_compatibility_state, "unresolved")

    def test_platform_and_python_without_changed_dependency_install_do_not_claim_formation(
        self,
    ) -> None:
        workflow = """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pytest
"""

        result = interpret_target_artifact_environment(
            _workflow_file(workflow),
            dependency_source_file="requirements-dev.txt",
        )

        self.assertIsInstance(result, TargetArtifactEnvironmentEvidence)
        assert isinstance(result, TargetArtifactEnvironmentEvidence)
        self.assertEqual(result.dependency_environment_formation, "not_observed")
        self.assertIsNone(result.formation_source)
        self.assertIn(
            "changed_dependency_environment_not_directly_observed",
            result.limitations,
        )
        self.assertEqual(result.exact_wheel_compatibility_state, "unresolved")

    def test_dynamic_python_preserves_known_facts_without_inventing_exact_compatibility(
        self,
    ) -> None:
        workflow = """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ vars.PYTHON_VERSION }}
      - run: python -m pip install -r ./requirements-dev.txt
"""

        result = interpret_target_artifact_environment(
            _workflow_file(workflow),
            dependency_source_file="requirements-dev.txt",
        )

        self.assertIsInstance(result, TargetArtifactEnvironmentEvidence)
        assert isinstance(result, TargetArtifactEnvironmentEvidence)
        self.assertEqual(result.runner.value if result.runner else None, "ubuntu-latest")
        self.assertIsNone(result.python_version)
        self.assertIn("setup_python_version_not_literal", result.limitations)
        self.assertEqual(result.dependency_environment_formation, "established")
        self.assertEqual(result.exact_wheel_compatibility_state, "unresolved")

    def test_multiple_jobs_remain_explicitly_unsupported(self) -> None:
        workflow = """jobs:
  unit:
    runs-on: ubuntu-latest
    steps:
      - run: pytest
  integration:
    runs-on: ubuntu-latest
    steps:
      - run: pytest
"""

        result = interpret_target_artifact_environment(
            _workflow_file(workflow),
            dependency_source_file="requirements-dev.txt",
        )

        self.assertIsInstance(result, TargetArtifactEnvironmentProblem)
        assert isinstance(result, TargetArtifactEnvironmentProblem)
        self.assertEqual(result.state, "multiple_or_zero_workflow_jobs")

    def test_matrix_job_remains_explicitly_unsupported(self) -> None:
        workflow = """jobs:
  test:
    strategy:
      matrix:
        python: ["3.11", "3.12"]
    runs-on: ubuntu-latest
    steps:
      - run: pytest
"""

        result = interpret_target_artifact_environment(
            _workflow_file(workflow),
            dependency_source_file="requirements-dev.txt",
        )

        self.assertIsInstance(result, TargetArtifactEnvironmentProblem)
        assert isinstance(result, TargetArtifactEnvironmentProblem)
        self.assertEqual(result.state, "unsupported_or_ambiguous_job_shape")


def _workflow_file(content: str) -> RepositoryTextFile:
    byte_count = len(content.encode("utf-8"))
    return RepositoryTextFile(
        repository="example/project",
        path=".github/workflows/ci.yml",
        returned_path=".github/workflows/ci.yml",
        revision=_REVISION,
        blob_sha="a" * 40,
        reported_byte_count=byte_count,
        decoded_byte_count=byte_count,
        retrieved_at=_RETRIEVED_AT,
        content=content,
    )


if __name__ == "__main__":
    unittest.main()
