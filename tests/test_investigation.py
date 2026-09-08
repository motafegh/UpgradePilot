"""Test current application sequencing independently of CLI presentation."""

from __future__ import annotations

import unittest
from datetime import datetime, timezone
from unittest.mock import Mock, call, patch

from upgradepilot.dependency.analysis import DependencyChangeAnalysis
from upgradepilot.dependency.change import (
    DependencyChangeProblem,
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.dependency.environment import RequirementsFileDependencyContext
from upgradepilot.github.actions import WorkflowJob, WorkflowRun
from upgradepilot.github.changelog import ChangelogPathDiscoveryProblem, DiscoveredChangelogPath
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.tag import GitHubTagCommitEvidence
from upgradepilot.impact.artifact_serviceability import (
    ArtifactServiceabilityEvidenceProblem,
    ArtifactServiceabilityImpactCandidate,
)
from upgradepilot.investigation import investigate_public_pull_request
from upgradepilot.pypi.release import (
    DistributionFile,
    PackageReleaseEvidence,
    PackageReleaseIndexEvidence,
    PackageReleaseProblem,
    PyPIReleaseClient,
    PyPIReleaseIndexClient,
)
from upgradepilot.target.artifact_environment import (
    TargetArtifactEnvironmentEvidence,
    TargetArtifactEnvironmentProblem,
)
from upgradepilot.upstream.claim import (
    GroundedPythonSupportDropClaim,
    UpstreamSupportDropClaimProblem,
)
from upgradepilot.upstream.interval import release_interval_from_dependency_change
from upgradepilot.upstream.repository import UpstreamRepositoryEvidence

_NOW = datetime(2026, 8, 5, tzinfo=timezone.utc)


class InvestigationTests(unittest.TestCase):
    def test_grounded_claim_activates_selected_target_investigation_and_reevaluates_impact(self) -> None:
        h = _Harness()
        dependency = _dependency()
        claim = GroundedPythonSupportDropClaim(
            python_line="3.9",
            introduced_in_version="1.1",
            interval=release_interval_from_dependency_change(dependency),
            source_evidence=(),
        )

        def evaluator(authority):
            self.assertIsNotNone(authority)
            h.repository_client.get_exact_head_text_file.assert_not_called()
            return claim

        h.support_drop_evaluator.side_effect = evaluator
        result = _run(h, dependency)

        self.assertEqual(result.ci_coverage_result.state, "no_successful_ci")
        self.assertIs(result.upstream_support_drop_result, claim)

        self.assertIsNotNone(result.python_support_drop_pre_investigation_result)
        assert result.python_support_drop_pre_investigation_result is not None
        self.assertEqual(
            result.python_support_drop_pre_investigation_result.applicability.state,
            "unresolved",
        )
        self.assertIsNone(
            result.python_support_drop_pre_investigation_result.target_relevance
        )

        self.assertIsNotNone(result.python_support_drop_investigation_selection)
        assert result.python_support_drop_investigation_selection is not None
        self.assertEqual(
            result.python_support_drop_investigation_selection.kind,
            "acquire_exact_target_python_declaration",
        )
        self.assertEqual(
            result.python_support_drop_investigation_selection.repository,
            h.identity.repository,
        )
        self.assertEqual(
            result.python_support_drop_investigation_selection.revision,
            h.identity.head_sha,
        )
        self.assertEqual(
            result.python_support_drop_investigation_selection.path,
            "pyproject.toml",
        )

        self.assertEqual(result.target_python_result.requires_python, ">=3.10")
        self.assertEqual(
            result.target_python_relevance_result.state,
            "outside_declared_python_range",
        )
        self.assertIsNotNone(result.python_support_drop_impact_result)
        assert result.python_support_drop_impact_result is not None
        self.assertEqual(
            result.python_support_drop_impact_result.applicability.state,
            "established_not_applicable",
        )
        self.assertEqual(
            result.python_support_drop_impact_result.candidate.target_revision,
            h.identity.head_sha,
        )
        h.repository_client.get_exact_head_text_file.assert_called_once_with(
            h.identity,
            "pyproject.toml",
        )
        self.assertEqual(
            h.package_client.get_release.call_args_list,
            [call("demo", "1.1"), call("demo", "1.0")],
        )
        h.release_index_client.get_release_index.assert_called_once_with("demo")

    def test_target_overlap_surfaces_established_applicable_impact_candidate(self) -> None:
        h = _Harness()
        dependency = _dependency()
        h.support_drop_evaluator.return_value = GroundedPythonSupportDropClaim(
            python_line="3.9",
            introduced_in_version="1.1",
            interval=release_interval_from_dependency_change(dependency),
            source_evidence=(),
        )
        h.repository_client.get_exact_head_text_file.return_value = RepositoryTextFile(
            repository=h.identity.repository,
            path="pyproject.toml",
            revision=h.identity.head_sha,
            content='[project]\nrequires-python = ">=3.9"\n',
        )

        result = _run(h, dependency)

        self.assertIsNotNone(result.python_support_drop_pre_investigation_result)
        self.assertIsNotNone(result.python_support_drop_investigation_selection)
        self.assertEqual(result.target_python_relevance_result.state, "declared_python_overlap")
        self.assertIsNotNone(result.python_support_drop_impact_result)
        assert result.python_support_drop_impact_result is not None
        self.assertEqual(
            result.python_support_drop_impact_result.applicability.state,
            "established_applicable",
        )

    def test_target_evidence_problem_preserves_unresolved_after_selected_investigation(self) -> None:
        h = _Harness()
        dependency = _dependency()
        h.support_drop_evaluator.return_value = GroundedPythonSupportDropClaim(
            python_line="3.9",
            introduced_in_version="1.1",
            interval=release_interval_from_dependency_change(dependency),
            source_evidence=(),
        )
        h.repository_client.get_exact_head_text_file.return_value = RepositoryTextFile(
            repository=h.identity.repository,
            path="pyproject.toml",
            revision=h.identity.head_sha,
            content='[project]\nname = "demo"\n',
        )

        result = _run(h, dependency)

        self.assertIsNotNone(result.python_support_drop_pre_investigation_result)
        assert result.python_support_drop_pre_investigation_result is not None
        self.assertEqual(
            result.python_support_drop_pre_investigation_result.applicability.state,
            "unresolved",
        )
        self.assertIsNotNone(result.python_support_drop_investigation_selection)
        self.assertEqual(result.target_python_relevance_result.state, "target_declaration_unresolved")
        self.assertIsNotNone(result.python_support_drop_impact_result)
        assert result.python_support_drop_impact_result is not None
        self.assertEqual(result.python_support_drop_impact_result.applicability.state, "unresolved")
        propositions = result.python_support_drop_impact_result.applicability.paths[0].propositions
        self.assertEqual(propositions[1].evidence_coverage, "insufficient")

    def test_no_grounded_claim_keeps_target_investigation_and_impact_inactive_and_preserves_ci(self) -> None:
        h = _Harness()
        dependency = _dependency()
        problem = UpstreamSupportDropClaimProblem(
            state="no_support_drop_claim",
            interval=release_interval_from_dependency_change(dependency),
            detail="No admitted Python support change was established.",
        )
        h.support_drop_evaluator.return_value = problem

        result = _run(h, dependency)

        self.assertEqual(result.ci_coverage_result.state, "no_successful_ci")
        self.assertIs(result.package_result, h.package)
        self.assertIs(result.upstream_repository_result, h.upstream)
        self.assertIsNone(result.target_python_result)
        self.assertEqual(
            result.target_python_relevance_result.state,
            "upstream_claim_unresolved",
        )
        self.assertIsNone(result.python_support_drop_pre_investigation_result)
        self.assertIsNone(result.python_support_drop_investigation_selection)
        self.assertIsNone(result.python_support_drop_impact_result)
        h.repository_client.get_exact_head_text_file.assert_not_called()
        h.release_index_client.get_release_index.assert_called_once_with("demo")

    def test_upstream_source_problem_stops_semantics_target_and_impact_but_not_ci(self) -> None:
        h = _Harness()
        dependency = _dependency()
        h.changelog_client.discover.return_value = ChangelogPathDiscoveryProblem(
            state="no_candidate_path",
            repository=h.upstream.repository,
            commit_sha="c" * 40,
            detail="No admitted changelog path.",
        )

        result = _run(h, dependency)

        self.assertEqual(result.ci_coverage_result.state, "no_successful_ci")
        self.assertIs(result.package_result, h.package)
        self.assertIs(result.upstream_repository_result, h.upstream)
        self.assertIsInstance(result.changelog_path_result, ChangelogPathDiscoveryProblem)
        self.assertIsNone(result.upstream_support_drop_result)
        self.assertIsNone(result.target_python_result)
        self.assertIsNone(result.python_support_drop_pre_investigation_result)
        self.assertIsNone(result.python_support_drop_investigation_selection)
        self.assertIsNone(result.python_support_drop_impact_result)
        h.support_drop_evaluator.assert_not_called()
        h.repository_client.get_exact_head_text_file.assert_not_called()
        h.release_index_client.get_release_index.assert_called_once_with("demo")

    def test_artifact_candidate_uses_exact_old_and_proposed_release_evidence(self) -> None:
        h = _Harness()
        h.set_releases(
            old=_package(
                "1.0",
                wheel_filename="demo-1.0-cp39-cp39-manylinux_2_17_x86_64.whl",
            ),
            proposed=_package(
                "1.1",
                wheel_filename="demo-1.1-cp310-cp310-manylinux_2_17_x86_64.whl",
            ),
        )

        result = _run(h, _dependency())

        self.assertIs(result.old_package_result, h.old_package)
        self.assertIsInstance(
            result.artifact_serviceability_candidate_result,
            ArtifactServiceabilityImpactCandidate,
        )
        candidate = result.artifact_serviceability_candidate_result
        assert isinstance(candidate, ArtifactServiceabilityImpactCandidate)
        self.assertIs(candidate.old_release, h.old_package)
        self.assertIs(candidate.proposed_release, h.package)
        self.assertEqual(candidate.target_repository, h.identity.repository)
        self.assertEqual(candidate.target_revision, h.identity.head_sha)
        self.assertIsNotNone(result.artifact_serviceability_impact_result)
        assert result.artifact_serviceability_impact_result is not None
        self.assertIs(result.artifact_serviceability_impact_result.candidate, candidate)
        self.assertEqual(
            result.artifact_serviceability_impact_result.applicability.state,
            "unresolved",
        )
        self.assertIsNone(result.artifact_serviceability_impact_result.target_evidence)

    def test_artifact_no_candidate_is_distinct_from_inactive_provider_state(self) -> None:
        h = _Harness()
        h.set_releases(
            old=_package("1.0", wheel_filename="demo-1.0-py3-none-any.whl"),
            proposed=_package("1.1", wheel_filename="demo-1.1-py3-none-any.whl"),
        )

        result = _run(h, _dependency())

        self.assertIs(result.package_result, h.package)
        self.assertIs(result.old_package_result, h.old_package)
        self.assertIsNone(result.artifact_serviceability_candidate_result)
        self.assertIsNone(result.artifact_serviceability_impact_result)

    def test_artifact_evidence_problem_is_preserved_without_assessment(self) -> None:
        h = _Harness()
        h.set_releases(
            old=_package("1.0", wheel_filename="broken.whl"),
            proposed=_package("1.1", wheel_filename="demo-1.1-py3-none-any.whl"),
        )

        result = _run(h, _dependency())

        self.assertIsInstance(
            result.artifact_serviceability_candidate_result,
            ArtifactServiceabilityEvidenceProblem,
        )
        problem = result.artifact_serviceability_candidate_result
        assert isinstance(problem, ArtifactServiceabilityEvidenceProblem)
        self.assertEqual(problem.state, "wheel_filename_uninterpretable")
        self.assertEqual(problem.release_version, "1.0")
        self.assertIsNone(result.artifact_serviceability_impact_result)
        self.assertIs(result.upstream_repository_result, h.upstream)

    def test_old_release_provider_problem_blocks_only_artifact_candidate_branch(self) -> None:
        h = _Harness()
        problem = PackageReleaseProblem(
            state="acquisition_failed",
            requested_package="demo",
            normalized_package="demo",
            requested_version="1.0",
            source_url="https://pypi.org/pypi/demo/1.0/json",
            detail="Old release lookup failed.",
        )
        h.old_package = problem

        result = _run(h, _dependency())

        self.assertIs(result.old_package_result, problem)
        self.assertIsNone(result.artifact_serviceability_candidate_result)
        self.assertIsNone(result.artifact_serviceability_impact_result)
        self.assertIs(result.upstream_repository_result, h.upstream)
        h.release_index_client.get_release_index.assert_called_once_with("demo")

    def test_artifact_candidate_survives_unrelated_upstream_source_problem(self) -> None:
        h = _Harness()
        h.set_releases(
            old=_package(
                "1.0",
                wheel_filename="demo-1.0-cp39-cp39-manylinux_2_17_x86_64.whl",
            ),
            proposed=_package(
                "1.1",
                wheel_filename="demo-1.1-cp310-cp310-manylinux_2_17_x86_64.whl",
            ),
        )
        h.changelog_client.discover.return_value = ChangelogPathDiscoveryProblem(
            state="no_candidate_path",
            repository=h.upstream.repository,
            commit_sha="c" * 40,
            detail="No admitted changelog path.",
        )

        result = _run(h, _dependency())

        self.assertIsInstance(
            result.artifact_serviceability_candidate_result,
            ArtifactServiceabilityImpactCandidate,
        )
        self.assertIsNotNone(result.artifact_serviceability_impact_result)
        assert result.artifact_serviceability_impact_result is not None
        self.assertEqual(
            result.artifact_serviceability_impact_result.applicability.state,
            "unresolved",
        )
        self.assertIsInstance(result.changelog_path_result, ChangelogPathDiscoveryProblem)
        self.assertIsNone(result.upstream_support_drop_result)

    def test_target_artifact_environment_uses_supported_direct_requirements_relationship(self) -> None:
        h = _Harness()
        h.set_releases(
            old=_package(
                "1.0",
                wheel_filename="demo-1.0-cp39-cp39-manylinux_2_17_x86_64.whl",
            ),
            proposed=_package(
                "1.1",
                wheel_filename="demo-1.1-cp310-cp310-manylinux_2_17_x86_64.whl",
            ),
        )
        h.set_workflow(
            """name: ci
jobs:
  test:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.9"
      - run: pip install -r requirements.txt
      - run: pytest
"""
        )
        h.stop_upstream_at_changelog()

        result = _run(h, _dependency())

        self.assertEqual(result.ci_coverage_result.state, "supported_not_correlated")
        self.assertEqual(len(result.target_artifact_environment_results), 1)
        association = result.target_artifact_environment_results[0]
        self.assertEqual(association.dependency_source.source_path, "requirements.txt")
        self.assertEqual(association.dependency_source.revision, h.identity.head_sha)
        self.assertIsInstance(
            association.target_environment,
            TargetArtifactEnvironmentEvidence,
        )
        target = association.target_environment
        assert isinstance(target, TargetArtifactEnvironmentEvidence)
        self.assertEqual(target.repository, h.identity.repository)
        self.assertEqual(target.revision, h.identity.head_sha)
        self.assertEqual(target.workflow_path, ".github/workflows/ci.yml")
        self.assertEqual(target.job, "test")
        self.assertEqual(target.runner.value if target.runner else None, "ubuntu-22.04")
        self.assertEqual(
            target.python_version.value if target.python_version else None,
            "3.9",
        )
        self.assertEqual(target.dependency_installation_declaration, "observed")
        self.assertEqual(target.exact_wheel_compatibility_state, "unresolved")
        self.assertIsNotNone(result.artifact_serviceability_impact_result)
        assert result.artifact_serviceability_impact_result is not None
        self.assertEqual(
            result.artifact_serviceability_impact_result.applicability.state,
            "unresolved",
        )
        self.assertIsNone(result.artifact_serviceability_impact_result.target_evidence)
        h.repository_client.get_exact_head_workflow_file.assert_called_once_with(
            h.identity,
            h.workflow_run,
        )

    def test_target_artifact_environment_stays_inactive_without_real_candidate(self) -> None:
        h = _Harness()
        h.set_releases(
            old=_package("1.0", wheel_filename="demo-1.0-py3-none-any.whl"),
            proposed=_package("1.1", wheel_filename="demo-1.1-py3-none-any.whl"),
        )
        h.set_workflow(
            """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements.txt
"""
        )
        h.stop_upstream_at_changelog()

        result = _run(h, _dependency())

        self.assertEqual(result.ci_coverage_result.workflows[0].consumption_state, "supported")
        self.assertIsNone(result.artifact_serviceability_candidate_result)
        self.assertEqual(result.target_artifact_environment_results, ())

    def test_unresolved_direct_requirements_relationship_does_not_enter_target_composition(self) -> None:
        h = _Harness()
        h.set_releases(
            old=_package(
                "1.0",
                wheel_filename="demo-1.0-cp39-cp39-manylinux_2_17_x86_64.whl",
            ),
            proposed=_package(
                "1.1",
                wheel_filename="demo-1.1-cp310-cp310-manylinux_2_17_x86_64.whl",
            ),
        )
        h.set_workflow(
            """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: pip install -r requirements.txt
"""
        )
        h.stop_upstream_at_changelog()

        result = _run(h, _dependency())

        workflow_result = result.ci_coverage_result.workflows[0]
        self.assertEqual(workflow_result.consumption_state, "unresolved")
        self.assertTrue(
            any(consumption.state == "unresolved" for consumption in workflow_result.consumptions)
        )
        self.assertEqual(result.target_artifact_environment_results, ())
        self.assertIsNotNone(result.artifact_serviceability_impact_result)
        assert result.artifact_serviceability_impact_result is not None
        self.assertEqual(
            result.artifact_serviceability_impact_result.applicability.state,
            "unresolved",
        )

    def test_multi_job_target_ambiguity_is_preserved_despite_ci_job_relevance(self) -> None:
        h = _Harness()
        h.set_releases(
            old=_package(
                "1.0",
                wheel_filename="demo-1.0-cp39-cp39-manylinux_2_17_x86_64.whl",
            ),
            proposed=_package(
                "1.1",
                wheel_filename="demo-1.1-cp310-cp310-manylinux_2_17_x86_64.whl",
            ),
        )
        h.set_workflow(
            """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements.txt
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python -m compileall src
""",
            job_names=("test", "lint"),
        )
        h.stop_upstream_at_changelog()

        result = _run(h, _dependency())

        self.assertEqual(result.ci_coverage_result.workflows[0].consumption_state, "supported")
        self.assertEqual(len(result.target_artifact_environment_results), 1)
        target = result.target_artifact_environment_results[0].target_environment
        self.assertIsInstance(target, TargetArtifactEnvironmentProblem)
        assert isinstance(target, TargetArtifactEnvironmentProblem)
        self.assertEqual(target.state, "ambiguous_target_job_selection")
        self.assertIsNotNone(result.artifact_serviceability_impact_result)
        assert result.artifact_serviceability_impact_result is not None
        self.assertEqual(
            result.artifact_serviceability_impact_result.applicability.state,
            "unresolved",
        )

    def test_dependency_problem_stops_both_dependency_specific_branches(self) -> None:
        h = _Harness()
        problem = DependencyChangeProblem(
            reason="no_supported_dependency_file",
            detail="No dependency source.",
        )
        with patch("upgradepilot.investigation.analyze_dependency_change", return_value=problem):
            result = investigate_public_pull_request("example/project", 7, **h.kwargs())

        self.assertIs(result.dependency_result, problem)
        self.assertIsNone(result.ci_coverage_result)
        self.assertIsNone(result.package_result)
        self.assertIsNone(result.old_package_result)
        self.assertIsNone(result.artifact_serviceability_candidate_result)
        self.assertEqual(result.target_artifact_environment_results, ())
        self.assertIsNone(result.artifact_serviceability_impact_result)
        self.assertIsNone(result.target_python_result)
        self.assertIsNone(result.python_support_drop_pre_investigation_result)
        self.assertIsNone(result.python_support_drop_investigation_selection)
        self.assertIsNone(result.python_support_drop_impact_result)
        h.actions_client.get_exact_head_workflow_runs.assert_not_called()
        h.package_client.get_release.assert_not_called()
        h.release_index_client.get_release_index.assert_not_called()
        h.repository_client.get_exact_head_text_file.assert_not_called()


class _Harness:
    def __init__(self) -> None:
        self.pull_client = Mock()
        self.actions_client = Mock()
        self.repository_client = Mock()
        self.package_client = Mock(spec=PyPIReleaseClient)
        self.release_index_client = Mock(spec=PyPIReleaseIndexClient)
        self.upstream_resolver = Mock()
        self.tag_client = Mock()
        self.changelog_client = Mock()
        self.support_drop_evaluator = Mock()
        self.support_drop_evaluator.return_value = UpstreamSupportDropClaimProblem(
            state="no_support_drop_claim",
            interval=release_interval_from_dependency_change(_dependency()),
            detail="No admitted Python support change was established.",
        )

        self.identity = _identity()
        self.old_package = _package("1.0")
        self.package = _package("1.1")
        self.upstream = _upstream(self.package)
        self.workflow_run: WorkflowRun | None = None
        self.pull_client.get_pull_request.return_value = self.identity
        self.pull_client.get_changed_files.return_value = (_changed_file(),)
        self.actions_client.get_exact_head_workflow_runs.return_value = ()
        self.package_client.get_release.side_effect = self._get_release
        self.release_index_client.get_release_index.return_value = _release_index()
        self.upstream_resolver.resolve.return_value = self.upstream
        self.tag_client.resolve_tag_to_commit.return_value = _tag()
        self.changelog_client.discover.return_value = _changelog_path()
        self.repository_client.get_exact_commit_text_file.return_value = _changelog_file()
        self.repository_client.get_exact_head_text_file.return_value = RepositoryTextFile(
            repository=self.identity.repository,
            path="pyproject.toml",
            revision=self.identity.head_sha,
            content='[project]\nrequires-python = ">=3.10"\n',
        )

    def _get_release(self, package: str, version: str):
        if package != "demo":
            raise AssertionError(f"Unexpected package request: {package!r}")
        if version == "1.1":
            return self.package
        if version == "1.0":
            return self.old_package
        raise AssertionError(f"Unexpected release version request: {version!r}")

    def set_releases(
        self,
        *,
        old: PackageReleaseEvidence,
        proposed: PackageReleaseEvidence,
    ) -> None:
        self.old_package = old
        self.package = proposed
        self.upstream = _upstream(proposed)
        self.upstream_resolver.resolve.return_value = self.upstream

    def set_workflow(
        self,
        content: str,
        *,
        job_names: tuple[str, ...] = ("test",),
    ) -> None:
        run = WorkflowRun(
            run_id=101,
            workflow_id=201,
            name="CI",
            event="pull_request",
            head_sha=self.identity.head_sha,
            status="completed",
            conclusion="success",
            run_attempt=1,
        )
        jobs = tuple(
            WorkflowJob(
                job_id=300 + index,
                run_id=run.run_id,
                name=name,
                head_sha=self.identity.head_sha,
                status="completed",
                conclusion="success",
                steps=None,
            )
            for index, name in enumerate(job_names)
        )
        definition = RepositoryTextFile(
            repository=self.identity.repository,
            path=".github/workflows/ci.yml",
            revision=self.identity.head_sha,
            content=content,
        )
        self.workflow_run = run
        self.actions_client.get_exact_head_workflow_runs.return_value = (run,)
        self.actions_client.get_workflow_jobs.return_value = jobs
        self.repository_client.get_exact_head_workflow_file.return_value = definition

    def stop_upstream_at_changelog(self) -> None:
        self.changelog_client.discover.return_value = ChangelogPathDiscoveryProblem(
            state="no_candidate_path",
            repository=self.upstream.repository,
            commit_sha="c" * 40,
            detail="No admitted changelog path.",
        )

    def kwargs(self) -> dict[str, object]:
        return {
            "pull_client": self.pull_client,
            "actions_client": self.actions_client,
            "repository_client": self.repository_client,
            "package_client": self.package_client,
            "release_index_client": self.release_index_client,
            "upstream_repository_resolver": self.upstream_resolver,
            "tag_client": self.tag_client,
            "changelog_client": self.changelog_client,
            "support_drop_evaluator": self.support_drop_evaluator,
        }


def _run(h: _Harness, dependency: DependencyVersionChange):
    source_context = RequirementsFileDependencyContext(
        repository=h.identity.repository,
        revision=h.identity.head_sha,
        normalized_package=dependency.normalized_package,
        source_evidence=dependency.source_evidence[0],
    )
    with patch(
        "upgradepilot.investigation.analyze_dependency_change",
        return_value=DependencyChangeAnalysis(
            dependency=dependency,
            source_contexts=(source_context,),
        ),
    ):
        return investigate_public_pull_request("example/project", 7, **h.kwargs())


def _identity() -> PullRequestIdentity:
    return PullRequestIdentity(
        repository="example/project",
        number=7,
        title="Bump demo",
        state="open",
        merged=False,
        author="dependabot[bot]",
        base_ref="main",
        base_sha="a" * 40,
        head_ref="dependabot/demo",
        head_sha="b" * 40,
        changed_files=1,
    )


def _changed_file() -> ChangedFile:
    return ChangedFile(
        filename="requirements.txt",
        status="modified",
        additions=1,
        deletions=1,
        changes=2,
        patch="-demo==1.0\n+demo==1.1",
    )


def _dependency() -> DependencyVersionChange:
    return DependencyVersionChange(
        package="demo",
        normalized_package="demo",
        old_version="1.0",
        proposed_version="1.1",
        source_evidence=(
            DependencyChangeSourceEvidence(
                path="requirements.txt",
                file_format="exact_requirement",
                extraction_method="changed_file_patch",
            ),
        ),
    )


def _package(
    version: str,
    *,
    wheel_filename: str | None = None,
) -> PackageReleaseEvidence:
    distribution_files = (
        (
            DistributionFile(
                filename=wheel_filename,
                url=f"https://files.pythonhosted.org/{wheel_filename}",
                sha256="0" * 64,
                package_type="bdist_wheel",
            ),
        )
        if wheel_filename is not None
        else ()
    )
    return PackageReleaseEvidence(
        requested_package="demo",
        normalized_package="demo",
        requested_version=version,
        published_name="demo",
        published_version=version,
        source_url=f"https://pypi.org/pypi/demo/{version}/json",
        retrieved_at=_NOW,
        last_serial=1,
        distribution_files=distribution_files,
        project_urls=(),
    )


def _upstream(package: PackageReleaseEvidence) -> UpstreamRepositoryEvidence:
    return UpstreamRepositoryEvidence(
        package_release=package,
        repository="example/upstream",
        source_candidates=(),
        provenance=(),
        provenance_unavailable_files=(),
    )


def _release_index() -> PackageReleaseIndexEvidence:
    return PackageReleaseIndexEvidence(
        requested_package="demo",
        normalized_package="demo",
        published_name="demo",
        source_url="https://pypi.org/pypi/demo/json",
        retrieved_at=_NOW,
        last_serial=2,
        release_versions=("1.0", "1.1"),
    )


def _tag() -> GitHubTagCommitEvidence:
    return GitHubTagCommitEvidence(
        repository="example/upstream",
        requested_tag="1.1",
        tag_ref="refs/tags/1.1",
        tag_object_type="commit",
        tag_object_sha="c" * 40,
        resolved_commit_sha="c" * 40,
        peeled_tag_object_shas=(),
        retrieved_at=_NOW,
    )


def _changelog_path() -> DiscoveredChangelogPath:
    return DiscoveredChangelogPath(
        repository="example/upstream",
        commit_sha="c" * 40,
        tree_sha="d" * 40,
        path="CHANGELOG.md",
        candidate_paths=("CHANGELOG.md",),
    )


def _changelog_file() -> RepositoryTextFile:
    return RepositoryTextFile(
        repository="example/upstream",
        path="CHANGELOG.md",
        revision="c" * 40,
        content="## 1.1\n- Removed Python 3.9 support.\n",
    )


if __name__ == "__main__":
    unittest.main()