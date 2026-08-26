"""Test CLI presentation and exit policy independently of application orchestration."""

from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout
from datetime import datetime, timezone
from unittest.mock import patch

from upgradepilot.ci.dependency_exercise import DependencyCICoverageResult
from upgradepilot.cli import main
from upgradepilot.dependency.change import (
    DependencyChangeProblem,
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.github.api import GitHubAcquisitionError, GitHubResponseError
from upgradepilot.github.identity import UpgradePilotInputError
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.investigation import PublicPullRequestInvestigation
from upgradepilot.pypi.release import PackageReleaseEvidence
from upgradepilot.target.python import TargetPythonDeclaration
from upgradepilot.upstream.repository import UpstreamRepositoryEvidence


class CLITests(unittest.TestCase):
    def test_supported_investigation_is_rendered_without_obsolete_claim_state(self) -> None:
        investigation = _supported_investigation()
        with patch(
            "upgradepilot.cli.investigate_public_pull_request",
            return_value=investigation,
        ) as investigate:
            exit_code, output = _run(["example/project", "7"])

        self.assertEqual(exit_code, 0)
        investigate.assert_called_once()
        self.assertIn("Dependency change: supported", output)
        self.assertIn("Package: demo", output)
        self.assertIn("Target Python declaration: available", output)
        self.assertIn("Target Python source: pyproject.toml @ ", output)
        self.assertIn("Target requires-python: >=3.10", output)
        self.assertNotIn("Target Python blob SHA:", output)
        self.assertIn("CI dependency coverage: no_successful_ci", output)
        self.assertIn("Package evidence: available", output)
        self.assertIn("Upstream repository: available", output)
        self.assertIn("Upstream repository identity: example/upstream", output)
        self.assertNotIn("Claim state:", output)
        self.assertNotIn("Accepted tag:", output)

    def test_dependency_problem_renders_downstream_stops(self) -> None:
        investigation = _problem_investigation()
        with patch(
            "upgradepilot.cli.investigate_public_pull_request",
            return_value=investigation,
        ):
            exit_code, output = _run(["example/project", "7"])

        self.assertEqual(exit_code, 0)
        self.assertIn("Dependency change: unsupported", output)
        self.assertIn("Target Python declaration: not activated", output)
        self.assertIn("CI dependency coverage: not evaluated", output)
        self.assertIn("Package evidence: not evaluated", output)
        self.assertIn("Upstream repository: not evaluated", output)
        self.assertIn("Target Python relevance: not evaluated", output)

    def test_input_error_maps_to_exit_2(self) -> None:
        with patch(
            "upgradepilot.cli.investigate_public_pull_request",
            side_effect=UpgradePilotInputError("bad input"),
        ):
            exit_code, output = _run(["bad", "7"])
        self.assertEqual(exit_code, 2)
        self.assertIn("Input rejected: bad input", output)

    def test_github_acquisition_error_maps_to_exit_3(self) -> None:
        with patch(
            "upgradepilot.cli.investigate_public_pull_request",
            side_effect=GitHubAcquisitionError(
                "missing",
                reason="not_found_or_inaccessible",
                status_code=404,
            ),
        ):
            exit_code, output = _run(["example/project", "7"])
        self.assertEqual(exit_code, 3)
        self.assertIn("Reason: not_found_or_inaccessible", output)
        self.assertIn("HTTP status: 404", output)

    def test_github_response_error_maps_to_exit_4(self) -> None:
        with patch(
            "upgradepilot.cli.investigate_public_pull_request",
            side_effect=GitHubResponseError("bad JSON"),
        ):
            exit_code, output = _run(["example/project", "7"])
        self.assertEqual(exit_code, 4)
        self.assertIn("bad JSON", output)


def _run(argv: list[str]) -> tuple[int, str]:
    stream = io.StringIO()
    with redirect_stdout(stream):
        exit_code = main(argv)
    return exit_code, stream.getvalue()


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


def _supported_investigation() -> PublicPullRequestInvestigation:
    dependency = DependencyVersionChange(
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
    package = PackageReleaseEvidence(
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
    upstream = UpstreamRepositoryEvidence(
        package_release=package,
        repository="example/upstream",
        source_candidates=(),
        provenance=(),
        provenance_unavailable_files=(),
    )
    return PublicPullRequestInvestigation(
        pull_request=_identity(),
        changed_files=(
            ChangedFile(
                filename="requirements.txt",
                status="modified",
                additions=1,
                deletions=1,
                changes=2,
                patch="-demo==1.0\n+demo==1.1",
            ),
        ),
        dependency_result=dependency,
        target_python_result=TargetPythonDeclaration(
            path="pyproject.toml",
            revision="b" * 40,
            requires_python=">=3.10",
        ),
        workflow_evidence=(),
        ci_coverage_result=DependencyCICoverageResult(
            state="no_successful_ci",
            reason="no_exact_head_workflows",
            detail="No workflows.",
            workflows=(),
        ),
        package_result=package,
        upstream_repository_result=upstream,
    )


def _problem_investigation() -> PublicPullRequestInvestigation:
    return PublicPullRequestInvestigation(
        pull_request=_identity(),
        changed_files=(),
        dependency_result=DependencyChangeProblem(
            reason="no_supported_dependency_file",
            detail="No supported dependency file.",
        ),
        target_python_result=None,
        workflow_evidence=(),
        ci_coverage_result=None,
        package_result=None,
        upstream_repository_result=None,
    )


if __name__ == "__main__":
    unittest.main()
