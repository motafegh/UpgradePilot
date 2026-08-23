from __future__ import annotations

import unittest

from upgradepilot.github.repository import RepositoryTextFile, UnavailableRepositoryFile
from upgradepilot.target.artifact_environment import (
    TargetArtifactEnvironmentEvidence,
    TargetArtifactEnvironmentProblem,
    interpret_target_artifact_environment,
)

_REVISION = "b" * 40


class TargetArtifactEnvironmentTests(unittest.TestCase):
    """Protect Target interpretation after migration to the shared static workflow IR."""

    def test_literal_job_preserves_partial_facts_and_install_declaration(self) -> None:
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
        self.assertEqual(result.dependency_installation_declaration, "observed")
        self.assertEqual(
            result.installation_declaration_source,
            "pip install -r requirements-dev.txt",
        )
        self.assertEqual(result.exact_wheel_compatibility_state, "unresolved")

    def test_platform_and_python_without_install_declaration_remain_nonfinal(self) -> None:
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
        self.assertEqual(result.dependency_installation_declaration, "not_observed")
        self.assertIsNone(result.installation_declaration_source)
        self.assertIn(
            "changed_dependency_installation_declaration_not_observed",
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
        self.assertEqual(result.dependency_installation_declaration, "observed")
        self.assertEqual(result.exact_wheel_compatibility_state, "unresolved")

    def test_python_version_outside_setup_python_with_mapping_is_not_a_fact(self) -> None:
        workflow = """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/setup-python@v5
        env:
          python-version: "3.11"
      - run: pip install -r requirements-dev.txt
"""

        result = interpret_target_artifact_environment(
            _workflow_file(workflow),
            dependency_source_file="requirements-dev.txt",
        )

        self.assertIsInstance(result, TargetArtifactEnvironmentEvidence)
        assert isinstance(result, TargetArtifactEnvironmentEvidence)
        self.assertIsNone(result.python_version)
        self.assertIn("setup_python_version_not_observed", result.limitations)
        self.assertEqual(result.dependency_installation_declaration, "observed")

    def test_multiple_jobs_are_target_selection_ambiguity_not_parser_failure(self) -> None:
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
        self.assertEqual(result.state, "ambiguous_target_job_selection")

    def test_matrix_structure_is_preserved_as_target_limitation_not_parser_failure(self) -> None:
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

        self.assertIsInstance(result, TargetArtifactEnvironmentEvidence)
        assert isinstance(result, TargetArtifactEnvironmentEvidence)
        self.assertEqual(result.runner.value if result.runner else None, "ubuntu-latest")
        self.assertIn("strategy_context_not_interpreted", result.limitations)
        self.assertEqual(result.dependency_installation_declaration, "not_observed")

    def test_container_structure_is_readable_but_not_interpreted_as_complete_target(self) -> None:
        workflow = """jobs:
  test:
    runs-on: ubuntu-latest
    container: python:3.12
    steps:
      - run: pip install -r requirements-dev.txt
"""

        result = interpret_target_artifact_environment(
            _workflow_file(workflow),
            dependency_source_file="requirements-dev.txt",
        )

        self.assertIsInstance(result, TargetArtifactEnvironmentEvidence)
        assert isinstance(result, TargetArtifactEnvironmentEvidence)
        self.assertIn("container_context_not_interpreted", result.limitations)
        self.assertEqual(result.dependency_installation_declaration, "observed")
        self.assertEqual(result.exact_wheel_compatibility_state, "unresolved")

    def test_workflow_working_directory_flows_into_shared_install_observer(self) -> None:
        workflow = """defaults:
  run:
    working-directory: backend
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: pip install -r ../requirements-dev.txt
"""

        result = interpret_target_artifact_environment(
            _workflow_file(workflow),
            dependency_source_file="requirements-dev.txt",
        )

        self.assertIsInstance(result, TargetArtifactEnvironmentEvidence)
        assert isinstance(result, TargetArtifactEnvironmentEvidence)
        self.assertEqual(result.dependency_installation_declaration, "observed")
        self.assertEqual(
            result.installation_declaration_source,
            "pip install -r ../requirements-dev.txt",
        )

    def test_dynamic_working_directory_makes_install_declaration_unresolved(self) -> None:
        workflow = """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: pip install -r requirements-dev.txt
        working-directory: ${{ matrix.project }}
"""

        result = interpret_target_artifact_environment(
            _workflow_file(workflow),
            dependency_source_file="requirements-dev.txt",
        )

        self.assertIsInstance(result, TargetArtifactEnvironmentEvidence)
        assert isinstance(result, TargetArtifactEnvironmentEvidence)
        self.assertEqual(result.dependency_installation_declaration, "unresolved")
        self.assertIsNone(result.installation_declaration_source)
        self.assertIn(
            "changed_dependency_installation_declaration_unresolved",
            result.limitations,
        )

    def test_reusable_workflow_job_is_target_abstention_not_shared_parser_failure(self) -> None:
        workflow = """jobs:
  delegated:
    uses: ./.github/workflows/reusable.yml
"""

        result = interpret_target_artifact_environment(
            _workflow_file(workflow),
            dependency_source_file="requirements-dev.txt",
        )

        self.assertIsInstance(result, TargetArtifactEnvironmentProblem)
        assert isinstance(result, TargetArtifactEnvironmentProblem)
        self.assertEqual(result.state, "unsupported_target_job")
        self.assertEqual(result.job, "delegated")

    def test_malformed_workflow_is_reported_through_shared_definition_problem(self) -> None:
        result = interpret_target_artifact_environment(
            _workflow_file("jobs:\n  test: [\n"),
            dependency_source_file="requirements-dev.txt",
        )

        self.assertIsInstance(result, TargetArtifactEnvironmentProblem)
        assert isinstance(result, TargetArtifactEnvironmentProblem)
        self.assertEqual(result.state, "workflow_definition_unreadable")
        self.assertIn("workflow_yaml_parse_error", result.detail)

    def test_unavailable_workflow_source_remains_explicit_target_problem(self) -> None:
        result = interpret_target_artifact_environment(
            UnavailableRepositoryFile(
                repository="example/project",
                path=".github/workflows/ci.yml",
                revision=_REVISION,
                reason="not_found_or_inaccessible",
                detail="GitHub returned 404.",
            ),
            dependency_source_file="requirements-dev.txt",
        )

        self.assertIsInstance(result, TargetArtifactEnvironmentProblem)
        assert isinstance(result, TargetArtifactEnvironmentProblem)
        self.assertEqual(result.state, "file_unavailable")
        self.assertEqual(result.repository, "example/project")
        self.assertEqual(result.revision, _REVISION)
        self.assertEqual(result.workflow_path, ".github/workflows/ci.yml")

    def test_dependency_source_path_remains_independent_semantic_input(self) -> None:
        with self.assertRaises(ValueError):
            interpret_target_artifact_environment(
                _workflow_file("jobs:\n  test:\n    runs-on: ubuntu-latest\n    steps: []\n"),
                dependency_source_file="../requirements-dev.txt",
            )


def _workflow_file(content: str) -> RepositoryTextFile:
    """Build one strong exact-revision workflow fixture after the provider boundary."""

    return RepositoryTextFile(
        repository="example/project",
        path=".github/workflows/ci.yml",
        revision=_REVISION,
        content=content,
    )


if __name__ == "__main__":
    unittest.main()
