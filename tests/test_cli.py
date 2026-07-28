"""Test the user-facing orchestration without making live network requests."""

from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout
from datetime import datetime, timezone
from types import SimpleNamespace
from unittest.mock import patch

from upgradepilot.ci_authority import CIAuthorityResult
from upgradepilot.cli import main
from upgradepilot.dependency_change import (
    PinnedDependencyChange,
    UnsupportedDependencyChange,
)
from upgradepilot.github_client import PullRequestIdentity
from upgradepilot.github_release import GitHubReleaseEvidence
from upgradepilot.pypi_client import (
    DistributionFile,
    PackageReleaseEvidence,
    PackageReleaseProblem,
    ProjectUrlCandidate,
)
from upgradepilot.pypi_provenance import (
    FileProvenanceEvidence,
    PublisherIdentity,
)
from upgradepilot.upstream_source import (
    UpstreamReleaseEvidence,
    UpstreamSourceProblem,
)


class CLITests(unittest.TestCase):
    """Protect stage ordering, typed stopping behavior, and concise output."""

    def test_complete_package_and_upstream_evidence_is_presented(self) -> None:
        package = _package_evidence()
        upstream = _upstream_evidence(package)

        exit_code, output, package_client, resolver = self._run_cli(
            dependency_result=_supported_dependency(),
            package_result=package,
            upstream_result=upstream,
        )

        self.assertEqual(exit_code, 0)
        self.assertIn("CI authority: sufficient", output)
        self.assertIn("Package evidence: available", output)
        self.assertIn("Published package: pytest==9.0.3", output)
        self.assertIn("Distribution files: 2", output)
        self.assertIn("Upstream source: available", output)
        self.assertIn("Upstream repository: pytest-dev/pytest", output)
        self.assertIn("Provenance coverage: 2 of 2 files", output)
        self.assertIn("Accepted tag: 9.0.3", output)
        self.assertIn("Tag object SHA: tag-sha", output)
        self.assertIn("Claim state: unresolved_claim", output)
        self.assertNotIn("FULL RELEASE BODY MUST STAY HIDDEN", output)
        package_client.get_release.assert_called_once_with("pytest", "9.0.3")
        resolver.resolve.assert_called_once_with(package)

    def test_package_problem_stops_upstream_resolution(self) -> None:
        problem = PackageReleaseProblem(
            state="version_not_found",
            requested_package="pytest",
            normalized_package="pytest",
            requested_version="9.0.3",
            source_url="https://pypi.org/pypi/pytest/9.0.3/json",
            detail="The exact version was not established.",
            status_code=404,
        )

        exit_code, output, package_client, resolver = self._run_cli(
            dependency_result=_supported_dependency(),
            package_result=problem,
        )

        self.assertEqual(exit_code, 0)
        self.assertIn("Package evidence: version_not_found", output)
        self.assertIn("Package detail: The exact version was not established.", output)
        self.assertIn("Upstream source: not evaluated", output)
        package_client.get_release.assert_called_once_with("pytest", "9.0.3")
        resolver.resolve.assert_not_called()

    def test_upstream_problem_preserves_successful_package_evidence(self) -> None:
        package = _package_evidence()
        problem = UpstreamSourceProblem(
            state="identity_mismatch",
            package="pytest",
            version="9.0.3",
            detail="Source candidate and publisher repository disagree.",
        )

        exit_code, output, _, resolver = self._run_cli(
            dependency_result=_supported_dependency(),
            package_result=package,
            upstream_result=problem,
        )

        self.assertEqual(exit_code, 0)
        self.assertIn("Package evidence: available", output)
        self.assertIn("Upstream source: identity_mismatch", output)
        self.assertIn(
            "Upstream detail: Source candidate and publisher repository disagree.",
            output,
        )
        resolver.resolve.assert_called_once_with(package)

    def test_unsupported_dependency_skips_all_dependent_stages(self) -> None:
        exit_code, output, package_client, resolver = self._run_cli(
            dependency_result=UnsupportedDependencyChange(
                reason="unsupported_shape",
                detail="No single exact pinned update was established.",
            )
        )

        self.assertEqual(exit_code, 0)
        self.assertIn("Dependency change: unsupported", output)
        self.assertIn("CI authority: not evaluated", output)
        self.assertIn("Package evidence: not evaluated", output)
        self.assertIn("Upstream source: not evaluated", output)
        package_client.get_release.assert_not_called()
        resolver.resolve.assert_not_called()

    def _run_cli(
        self,
        *,
        dependency_result: PinnedDependencyChange | UnsupportedDependencyChange,
        package_result: PackageReleaseEvidence | PackageReleaseProblem | None = None,
        upstream_result: UpstreamReleaseEvidence | UpstreamSourceProblem | None = None,
    ) -> tuple[int, str, object, object]:
        pull_request = PullRequestIdentity(
            repository="googlefonts/glyphsLib",
            number=1145,
            title="Bump pytest from 9.0.2 to 9.0.3",
            state="closed",
            merged=True,
            author="dependabot[bot]",
            base_ref="main",
            base_sha="base-sha",
            head_ref="dependabot/pip/pytest-9.0.3",
            head_sha="head-sha",
            changed_files=1,
        )
        changed_file = SimpleNamespace(
            filename="requirements-dev.txt",
            status="modified",
        )
        workflow_run = SimpleNamespace(
            name="Regression Tests",
            status="completed",
            conclusion="success",
        )
        workflow_job = SimpleNamespace(
            name="test",
            status="completed",
            conclusion="success",
            steps=(),
        )
        authority = SimpleNamespace(
            status="sufficient",
            reason="exact_head_dependency_exercised",
            detail="The dependency was installed and directly exercised.",
            workflows=(),
        )

        with (
            patch("upgradepilot.cli.extract_pinned_dependency_change") as extract,
            patch("upgradepilot.cli.evaluate_ci_authority") as evaluate,
            patch("upgradepilot.cli.GitHubReadClient") as pull_client_type,
            patch("upgradepilot.cli.GitHubActionsClient") as actions_client_type,
            patch("upgradepilot.cli.GitHubRepositoryClient") as repository_client_type,
            patch("upgradepilot.cli.GitHubReleaseClient"),
            patch("upgradepilot.cli.PyPIReleaseClient") as package_client_type,
            patch("upgradepilot.cli.UpstreamSourceResolver") as resolver_type,
        ):
            pull_client = pull_client_type.return_value
            pull_client.get_pull_request.return_value = pull_request
            pull_client.get_changed_files.return_value = (changed_file,)

            actions_client = actions_client_type.return_value
            actions_client.get_exact_head_workflow_runs.return_value = (workflow_run,)
            actions_client.get_workflow_jobs.return_value = (workflow_job,)
            repository_client_type.return_value.get_exact_head_workflow_file.return_value = (
                SimpleNamespace(state="available", text="name: regression")
            )

            extract.return_value = dependency_result
            evaluate.return_value = authority

            package_client = package_client_type.return_value
            package_client.get_release.return_value = package_result
            resolver = resolver_type.return_value
            resolver.resolve.return_value = upstream_result

            stream = io.StringIO()
            with redirect_stdout(stream):
                exit_code = main(["googlefonts/glyphsLib", "1145"])

        return exit_code, stream.getvalue(), package_client, resolver


def _supported_dependency() -> PinnedDependencyChange:
    return PinnedDependencyChange(
        source_file="requirements-dev.txt",
        package="pytest",
        normalized_package="pytest",
        old_version="9.0.2",
        proposed_version="9.0.3",
    )


def _package_evidence() -> PackageReleaseEvidence:
    files = (
        DistributionFile(
            filename="pytest-9.0.3-py3-none-any.whl",
            url="https://files.pythonhosted.org/pytest-9.0.3.whl",
            sha256="a" * 64,
            package_type="bdist_wheel",
        ),
        DistributionFile(
            filename="pytest-9.0.3.tar.gz",
            url="https://files.pythonhosted.org/pytest-9.0.3.tar.gz",
            sha256="b" * 64,
            package_type="sdist",
        ),
    )
    return PackageReleaseEvidence(
        requested_package="pytest",
        normalized_package="pytest",
        requested_version="9.0.3",
        published_name="pytest",
        published_version="9.0.3",
        source_url="https://pypi.org/pypi/pytest/9.0.3/json",
        retrieved_at=datetime(2026, 7, 28, tzinfo=timezone.utc),
        last_serial=123,
        distribution_files=files,
        project_urls=(
            ProjectUrlCandidate(
                label="Source",
                url="https://github.com/pytest-dev/pytest",
            ),
        ),
    )


def _upstream_evidence(package: PackageReleaseEvidence) -> UpstreamReleaseEvidence:
    publishers = (
        PublisherIdentity(
            kind="GitHub",
            repository="pytest-dev/pytest",
            workflow="deploy.yml",
        ),
    )
    provenance = tuple(
        FileProvenanceEvidence(
            package="pytest",
            version="9.0.3",
            filename=distribution.filename,
            sha256=distribution.sha256,
            source_url=(
                "https://pypi.org/integrity/pytest/9.0.3/"
                f"{distribution.filename}/provenance"
            ),
            retrieved_at=datetime(2026, 7, 28, tzinfo=timezone.utc),
            api_version=1,
            attestation_count=1,
            publishers=publishers,
        )
        for distribution in package.distribution_files
    )
    release = GitHubReleaseEvidence(
        repository="pytest-dev/pytest",
        requested_tag="9.0.3",
        release_id=42,
        release_url="https://github.com/pytest-dev/pytest/releases/tag/9.0.3",
        release_name="pytest 9.0.3",
        body="FULL RELEASE BODY MUST STAY HIDDEN",
        prerelease=False,
        published_at="2026-04-07T17:16:45Z",
        tag_ref="refs/tags/9.0.3",
        tag_object_type="tag",
        tag_object_sha="tag-sha",
        retrieved_at=datetime(2026, 7, 28, tzinfo=timezone.utc),
    )
    return UpstreamReleaseEvidence(
        package_release=package,
        repository="pytest-dev/pytest",
        source_candidates=package.project_urls,
        provenance=provenance,
        provenance_unavailable_files=(),
        github_release=release,
    )


if __name__ == "__main__":
    unittest.main()
