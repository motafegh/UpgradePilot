"""Test application sequencing independently of CLI presentation."""

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
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.investigation import investigate_public_pull_request
from upgradepilot.pypi.release import PackageReleaseEvidence, PackageReleaseProblem
from upgradepilot.upstream.repository import UpstreamRepositoryEvidence


class InvestigationTests(unittest.TestCase):
    def test_supported_dependency_runs_current_pre_step7_evidence_sequence(self) -> None:
        pull_client = Mock()
        actions_client = Mock()
        repository_client = Mock()
        package_client = Mock()
        upstream_resolver = Mock()

        identity = _identity()
        changed_file = _changed_file()
        dependency = _dependency()
        package = _package()
        upstream = UpstreamRepositoryEvidence(
            package_release=package,
            repository="example/upstream",
            source_candidates=(),
            provenance=(),
            provenance_unavailable_files=(),
        )

        pull_client.get_pull_request.return_value = identity
        pull_client.get_changed_files.return_value = (changed_file,)
        repository_client.get_exact_head_text_file.return_value = RepositoryTextFile(
            path="pyproject.toml",
            revision=identity.head_sha,
            blob_sha="target-blob",
            content='[project]\nrequires-python = ">=3.10"\n',
        )
        actions_client.get_exact_head_workflow_runs.return_value = ()
        package_client.get_release.return_value = package
        upstream_resolver.resolve.return_value = upstream

        with patch(
            "upgradepilot.investigation.analyze_dependency_change",
            return_value=DependencyChangeAnalysis(
                dependency=dependency,
                direct_requirements_install_path="requirements.txt",
            ),
        ):
            result = investigate_public_pull_request(
                "example/project",
                7,
                pull_client=pull_client,
                actions_client=actions_client,
                repository_client=repository_client,
                package_client=package_client,
                upstream_repository_resolver=upstream_resolver,
            )

        self.assertIs(result.dependency_result, dependency)
        self.assertEqual(result.target_python_result.requires_python, ">=3.10")  # type: ignore[union-attr]
        self.assertEqual(result.workflow_evidence, ())
        self.assertEqual(result.ci_exercise_result.state, "no_successful_ci")  # type: ignore[union-attr]
        self.assertIs(result.package_result, package)
        self.assertIs(result.upstream_repository_result, upstream)
        upstream_resolver.resolve.assert_called_once_with(package)

    def test_dependency_problem_stops_all_dependent_acquisition(self) -> None:
        pull_client = Mock()
        actions_client = Mock()
        repository_client = Mock()
        package_client = Mock()
        upstream_resolver = Mock()
        identity = _identity()

        pull_client.get_pull_request.return_value = identity
        pull_client.get_changed_files.return_value = ()
        problem = DependencyChangeProblem(
            reason="no_supported_dependency_file",
            detail="No dependency source.",
        )

        with patch(
            "upgradepilot.investigation.analyze_dependency_change",
            return_value=problem,
        ):
            result = investigate_public_pull_request(
                "example/project",
                7,
                pull_client=pull_client,
                actions_client=actions_client,
                repository_client=repository_client,
                package_client=package_client,
                upstream_repository_resolver=upstream_resolver,
            )

        self.assertIs(result.dependency_result, problem)
        self.assertIsNone(result.target_python_result)
        self.assertIsNone(result.ci_exercise_result)
        self.assertIsNone(result.package_result)
        self.assertIsNone(result.upstream_repository_result)
        repository_client.get_exact_head_text_file.assert_not_called()
        actions_client.get_exact_head_workflow_runs.assert_not_called()
        package_client.get_release.assert_not_called()
        upstream_resolver.resolve.assert_not_called()

    def test_package_problem_stops_upstream_repository_resolution(self) -> None:
        pull_client = Mock()
        actions_client = Mock()
        repository_client = Mock()
        package_client = Mock()
        upstream_resolver = Mock()
        identity = _identity()
        dependency = _dependency()

        pull_client.get_pull_request.return_value = identity
        pull_client.get_changed_files.return_value = (_changed_file(),)
        repository_client.get_exact_head_text_file.return_value = RepositoryTextFile(
            path="pyproject.toml",
            revision=identity.head_sha,
            blob_sha="target-blob",
            content='[project]\nrequires-python = ">=3.10"\n',
        )
        actions_client.get_exact_head_workflow_runs.return_value = ()
        package_problem = PackageReleaseProblem(
            state="version_not_found",
            requested_package="demo",
            normalized_package="demo",
            requested_version="1.1",
            source_url="https://pypi.org/pypi/demo/1.1/json",
            detail="Not found.",
            status_code=404,
        )
        package_client.get_release.return_value = package_problem

        with patch(
            "upgradepilot.investigation.analyze_dependency_change",
            return_value=DependencyChangeAnalysis(
                dependency=dependency,
                direct_requirements_install_path="requirements.txt",
            ),
        ):
            result = investigate_public_pull_request(
                "example/project",
                7,
                pull_client=pull_client,
                actions_client=actions_client,
                repository_client=repository_client,
                package_client=package_client,
                upstream_repository_resolver=upstream_resolver,
            )

        self.assertIs(result.package_result, package_problem)
        self.assertIsNone(result.upstream_repository_result)
        upstream_resolver.resolve.assert_not_called()


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
        retrieved_at=datetime(2026, 8, 4, tzinfo=timezone.utc),
        last_serial=1,
        distribution_files=(),
        project_urls=(),
    )


if __name__ == "__main__":
    unittest.main()
