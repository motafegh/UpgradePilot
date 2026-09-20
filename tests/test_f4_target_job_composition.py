"""Protect the application boundary that carries CI's exact consuming job to Target.

The end-to-end investigation test covers selection from real CI analysis. These focused
composition cases cover different cross-branch identities and two supported jobs that
must not be collapsed into one Target result.
"""

from __future__ import annotations

import unittest
from types import SimpleNamespace

from upgradepilot.ci.consumption import StaticDependencyConsumptionEvidence
from upgradepilot.dependency.change import DependencyChangeSourceEvidence
from upgradepilot.dependency.environment import RequirementsFileDependencyContext
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.investigation import _compose_target_artifact_environments
from upgradepilot.target.artifact_environment import (
    TargetArtifactEnvironmentEvidence,
    TargetArtifactEnvironmentProblem,
)

_REVISION = "b" * 40
_WORKFLOW_PATH = ".github/workflows/ci.yml"


def _workflow() -> RepositoryTextFile:
    return RepositoryTextFile(
        repository="example/project",
        path=_WORKFLOW_PATH,
        revision=_REVISION,
        content="""jobs:
  test:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: "3.9"
      - run: pip install -r requirements.txt
  smoke:
    runs-on: windows-latest
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
""",
    )


def _consumption(job_key: str, *, revision: str = _REVISION) -> StaticDependencyConsumptionEvidence:
    return StaticDependencyConsumptionEvidence(
        state="supported",
        mechanism="direct_requirements",
        normalized_package="demo",
        workflow_path=_WORKFLOW_PATH,
        workflow_revision=revision,
        job_key=job_key,
        step_source_index=2,
        command="pip install -r requirements.txt",
        reason="direct_requirements_install_observed",
        detail="Controlled exact source and job relationship.",
        source_path="requirements.txt",
    )


def _source(*, repository: str = "example/project") -> RequirementsFileDependencyContext:
    return RequirementsFileDependencyContext(
        repository=repository,
        revision=_REVISION,
        normalized_package="demo",
        source_evidence=DependencyChangeSourceEvidence(
            path="requirements.txt",
            file_format="exact_requirement",
            extraction_method="changed_file_patch",
        ),
    )


def _compose(*consumptions: StaticDependencyConsumptionEvidence, source_repository: str = "example/project"):
    definition = _workflow()
    # These narrow containers exercise the application composition seam; CI's own
    # producer and run/job identity are tested separately and in test_investigation.py.
    coverage = SimpleNamespace(
        workflows=(SimpleNamespace(workflow_path=_WORKFLOW_PATH, consumptions=consumptions),)
    )
    inputs = [SimpleNamespace(definition=definition)]
    return _compose_target_artifact_environments(
        coverage,
        inputs,
        (_source(repository=source_repository),),
    )


class ConsumingJobCompositionTests(unittest.TestCase):
    def test_two_consuming_jobs_keep_distinct_target_environments(self) -> None:
        results = _compose(_consumption("test"), _consumption("smoke"))
        self.assertEqual(len(results), 2)
        self.assertTrue(
            all(isinstance(item.target_environment, TargetArtifactEnvironmentEvidence) for item in results)
        )
        by_job = {item.target_environment.job: item.target_environment for item in results}
        self.assertEqual(set(by_job), {"test", "smoke"})
        self.assertEqual(by_job["test"].python_version.value, "3.9")
        self.assertEqual(by_job["smoke"].python_version.value, "3.12")
        self.assertEqual(by_job["test"].exact_wheel_compatibility_state, "unresolved")
        self.assertEqual(by_job["smoke"].exact_wheel_compatibility_state, "unresolved")

    def test_same_consuming_job_is_not_duplicated_by_two_supported_observations(self) -> None:
        results = _compose(_consumption("test"), _consumption("test"))
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].target_environment.job, "test")

    def test_missing_ci_selected_job_does_not_fall_back_to_another_job(self) -> None:
        results = _compose(_consumption("missing"))
        self.assertEqual(len(results), 1)
        result = results[0].target_environment
        self.assertIsInstance(result, TargetArtifactEnvironmentProblem)
        self.assertEqual(result.state, "selected_target_job_not_found")
        self.assertEqual(result.job, "missing")

    def test_ci_source_and_workflow_revision_mismatch_is_not_composed(self) -> None:
        with self.assertRaisesRegex(ValueError, "exact workflow identity"):
            _compose(_consumption("test", revision="c" * 40))

    def test_ci_source_repository_mismatch_is_not_composed(self) -> None:
        with self.assertRaisesRegex(ValueError, "one exact dependency source context"):
            _compose(_consumption("test"), source_repository="another/project")


if __name__ == "__main__":
    unittest.main()
