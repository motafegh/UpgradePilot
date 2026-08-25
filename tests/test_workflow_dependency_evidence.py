"""Test Cluster-5 static CI evidence before runtime authority is composed."""

from __future__ import annotations

import unittest

from upgradepilot.ci.consumption import StaticDependencyConsumptionEvidence
from upgradepilot.ci.workflow_commands import inspect_workflow_dependency_evidence
from upgradepilot.dependency.change import DependencyChangeSourceEvidence
from upgradepilot.dependency.environment import (
    ConstraintsFileDependencyContext,
    RequirementsFileDependencyContext,
)
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


def _requirements_context():
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


def _constraints_context():
    evidence = DependencyChangeSourceEvidence(
        path="constraints/base.txt",
        file_format="exact_requirement",
        extraction_method="changed_file_patch",
    )
    return ConstraintsFileDependencyContext(
        repository="example/project",
        revision=_HEAD_SHA,
        normalized_package="pytest",
        source_evidence=evidence,
    )


class WorkflowDependencyEvidenceTests(unittest.TestCase):
    def test_requirements_consumption_and_direct_invocation_are_separate_items(self) -> None:
        workflow = """jobs:
  unit:
    steps:
      - run: pip install -r requirements-dev.txt
      - run: pytest tests
"""

        result = inspect_workflow_dependency_evidence(
            _source(workflow),
            source_contexts=(_requirements_context(),),
            package="pytest",
            normalized_package="pytest",
        )

        self.assertEqual(result.job_count, 1)
        self.assertEqual(len(result.consumptions), 1)
        self.assertEqual(result.consumptions[0].state, "supported")
        self.assertEqual(result.consumptions[0].job_key, "unit")
        self.assertEqual(len(result.invocations), 1)
        self.assertEqual(result.invocations[0].job_key, "unit")
        self.assertEqual(result.problems, ())

    def test_constraints_context_is_not_promoted_to_direct_install_consumption(self) -> None:
        workflow = """jobs:
  unit:
    steps:
      - run: |
          pip install -r constraints/base.txt
          pytest tests
"""

        result = inspect_workflow_dependency_evidence(
            _source(workflow),
            source_contexts=(_constraints_context(),),
            package="pytest",
            normalized_package="pytest",
        )

        self.assertEqual(result.consumptions, ())
        self.assertEqual(len(result.invocations), 1)

    def test_multiple_jobs_are_preserved_without_one_job_restriction(self) -> None:
        workflow = """jobs:
  unit:
    steps:
      - run: pip install -r requirements-dev.txt
  lint:
    steps:
      - run: ruff check .
"""

        result = inspect_workflow_dependency_evidence(
            _source(workflow),
            source_contexts=(_requirements_context(),),
            package="pytest",
            normalized_package="pytest",
        )

        self.assertEqual(result.job_count, 2)
        self.assertEqual(len(result.consumptions), 1)
        self.assertEqual(result.consumptions[0].job_key, "unit")
        self.assertEqual(result.problems, ())

    def test_external_consumption_must_match_exact_static_step(self) -> None:
        workflow = """jobs:
  docs:
    steps:
      - run: uv sync --group docs
"""
        external = StaticDependencyConsumptionEvidence(
            state="supported",
            mechanism="project_environment",
            normalized_package="soupsieve",
            workflow_path=_PATH,
            workflow_revision=_HEAD_SHA,
            job_key="docs",
            step_source_index=0,
            segment_index=0,
            command="uv sync --group wrong",
            reason="selected_uv_roots_reach_changed_dependency",
            detail="synthetic selected-root reachability",
            source_path="uv.lock",
            reachability_kind="transitive",
            witness_path=("a", "soupsieve"),
        )

        result = inspect_workflow_dependency_evidence(
            _source(workflow),
            source_contexts=(),
            package="soupsieve",
            normalized_package="soupsieve",
            external_consumptions=(external,),
        )

        self.assertEqual(result.consumptions, ())
        self.assertEqual(len(result.problems), 1)
        self.assertEqual(
            result.problems[0].reason,
            "external_consumption_step_identity_mismatch",
        )


if __name__ == "__main__":
    unittest.main()
