"""Test current application sequencing independently of CLI presentation."""

from __future__ import annotations

import unittest
from datetime import datetime, timezone
from unittest.mock import Mock, patch

from upgradepilot.dependency.analysis import DependencyChangeAnalysis
from upgradepilot.dependency.change import (
    DependencyChangeProblem,
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.dependency.environment import RequirementsFileDependencyContext
from upgradepilot.github.changelog import ChangelogPathDiscoveryProblem, DiscoveredChangelogPath
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.tag import GitHubTagCommitEvidence
from upgradepilot.investigation import investigate_public_pull_request
from upgradepilot.pypi.release import (
    PackageReleaseEvidence,
    PackageReleaseIndexEvidence,
    PyPIReleaseClient,
    PyPIReleaseIndexClient,
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
        h.package_client.get_release.assert_called_once_with("demo", "1.1")
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

        self.identity = _identity()
        self.package = _package()
        self.upstream = UpstreamRepositoryEvidence(
            package_release=self.package,
            repository="example/upstream",
            source_candidates=(),
            provenance=(),
            provenance_unavailable_files=(),
        )
        self.pull_client.get_pull_request.return_value = self.identity
        self.pull_client.get_changed_files.return_value = (_changed_file(),)
        self.actions_client.get_exact_head_workflow_runs.return_value = ()
        self.package_client.get_release.return_value = self.package
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


def _package() -> PackageReleaseEvidence:
    return PackageReleaseEvidence(
        requested_package="demo",
        normalized_package="demo",
        requested_version="1.1",
        published_name="demo",
        published_version="1.1",
        source_url="https://pypi.org/pypi/demo/1.1/json",
        retrieved_at=_NOW,
        last_serial=1,
        distribution_files=(),
        project_urls=(),
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
