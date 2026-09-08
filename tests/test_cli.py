"""Test CLI presentation and exit policy independently of application orchestration."""

from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout
from dataclasses import replace
from datetime import datetime, timezone
from unittest.mock import patch

from packaging.tags import Tag

from upgradepilot.ci.dependency_exercise import DependencyCICoverageResult
from upgradepilot.cli import main
from upgradepilot.dependency.change import (
    DependencyChangeProblem,
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.dependency.environment import RequirementsFileDependencyContext
from upgradepilot.github.api import GitHubAcquisitionError, GitHubResponseError
from upgradepilot.github.identity import UpgradePilotInputError
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.impact.artifact_serviceability import (
    ArtifactServiceabilityEvidenceProblem,
    ArtifactServiceabilityImpactCandidate,
    PublishedWheelArtifact,
    evaluate_artifact_serviceability_impact,
)
from upgradepilot.investigation import (
    DependencySourceArtifactEnvironmentResult,
    PublicPullRequestInvestigation,
)
from upgradepilot.pypi.release import PackageReleaseEvidence
from upgradepilot.target.artifact_environment import (
    TargetArtifactEnvironmentEvidence,
    TargetArtifactEnvironmentFact,
    TargetArtifactEnvironmentProblem,
)
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
        self.assertIn("Old package artifact evidence: not evaluated", output)
        self.assertIn("Artifact serviceability candidate: not evaluated", output)
        self.assertIn("Target artifact environments: not activated", output)
        self.assertIn("Artifact applicability: not evaluated", output)
        self.assertNotIn("Claim state:", output)
        self.assertNotIn("Accepted tag:", output)

    def test_artifact_candidate_and_target_evidence_render_proof_strength_without_tag_dump(
        self,
    ) -> None:
        investigation = _artifact_candidate_investigation()
        with patch(
            "upgradepilot.cli.investigate_public_pull_request",
            return_value=investigation,
        ):
            exit_code, output = _run(["example/project", "7"])

        self.assertEqual(exit_code, 0)
        self.assertIn("Old package artifact evidence: available", output)
        self.assertIn("Old published package: demo==1.0", output)
        self.assertIn("Artifact serviceability candidate: established", output)
        self.assertIn("Removed published wheel-tag capabilities: 1", output)
        self.assertIn("Added published wheel-tag capabilities: 1", output)
        self.assertIn("Proposed source distribution: unavailable", output)
        self.assertIn("Target artifact environments: 1", output)
        self.assertIn("Target artifact environment 1 source: requirements.txt", output)
        self.assertIn("Target artifact environment 1: available", output)
        self.assertIn("Workflow: .github/workflows/ci.yml @ ", output)
        self.assertIn("Job: test", output)
        self.assertIn("Runner: ubuntu-22.04", output)
        self.assertIn("Python: 3.9", output)
        self.assertIn("Dependency installation declaration: observed", output)
        self.assertIn("Exact wheel compatibility: unresolved", output)
        self.assertIn("Artifact applicability: unresolved", output)
        self.assertIn("Exact target wheel compatibility: not established", output)
        self.assertNotIn("cp39-cp39-manylinux_2_17_x86_64", output)
        self.assertNotIn("Maintainer recommendation", output)

    def test_artifact_target_problem_is_rendered_without_strengthening_applicability(self) -> None:
        investigation = _artifact_candidate_investigation(target_problem=True)
        with patch(
            "upgradepilot.cli.investigate_public_pull_request",
            return_value=investigation,
        ):
            exit_code, output = _run(["example/project", "7"])

        self.assertEqual(exit_code, 0)
        self.assertIn(
            "Target artifact environment 1: ambiguous_target_job_selection",
            output,
        )
        self.assertIn("Target selection remains ambiguous.", output)
        self.assertIn("Artifact applicability: unresolved", output)
        self.assertIn("Exact target wheel compatibility: not established", output)

    def test_artifact_evidence_problem_is_distinct_from_no_candidate(self) -> None:
        investigation = _artifact_problem_investigation()
        with patch(
            "upgradepilot.cli.investigate_public_pull_request",
            return_value=investigation,
        ):
            exit_code, output = _run(["example/project", "7"])

        self.assertEqual(exit_code, 0)
        self.assertIn("Artifact serviceability candidate: evidence problem", output)
        self.assertIn("Artifact candidate problem: wheel_filename_uninterpretable", output)
        self.assertIn("Artifact candidate file: broken.whl", output)
        self.assertIn("Target artifact environments: not activated", output)
        self.assertIn("Artifact applicability: not evaluated", output)
        self.assertNotIn("Artifact serviceability candidate: not observed", output)

    def test_completed_artifact_comparison_can_render_no_candidate(self) -> None:
        investigation = _no_artifact_candidate_investigation()
        with patch(
            "upgradepilot.cli.investigate_public_pull_request",
            return_value=investigation,
        ):
            exit_code, output = _run(["example/project", "7"])

        self.assertEqual(exit_code, 0)
        self.assertIn("Old package artifact evidence: available", output)
        self.assertIn("Artifact serviceability candidate: not observed", output)
        self.assertIn("comparison completed without a bounded published-wheel capability loss", output)
        self.assertIn("Target artifact environments: not activated", output)
        self.assertIn("Artifact applicability: not evaluated", output)

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
        self.assertIn("Old package artifact evidence: not evaluated", output)
        self.assertIn("Artifact serviceability candidate: not evaluated", output)
        self.assertIn("Target artifact environments: not activated", output)
        self.assertIn("Artifact applicability: not evaluated", output)
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


def _package(version: str) -> PackageReleaseEvidence:
    return PackageReleaseEvidence(
        requested_package="demo",
        normalized_package="demo",
        requested_version=version,
        published_name="demo",
        published_version=version,
        source_url=f"https://pypi.org/pypi/demo/{version}/json",
        retrieved_at=datetime(2026, 8, 4, tzinfo=timezone.utc),
        last_serial=1,
        distribution_files=(),
        project_urls=(),
    )


def _supported_investigation() -> PublicPullRequestInvestigation:
    dependency = _dependency()
    package = _package("1.1")
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


def _artifact_candidate() -> tuple[
    ArtifactServiceabilityImpactCandidate,
    PackageReleaseEvidence,
]:
    dependency = _dependency()
    identity = _identity()
    old_release = _package("1.0")
    proposed_release = _package("1.1")
    old_tag = Tag("cp39", "cp39", "manylinux_2_17_x86_64")
    proposed_tag = Tag("cp310", "cp310", "manylinux_2_17_x86_64")
    candidate = ArtifactServiceabilityImpactCandidate(
        pull_request=identity,
        dependency=dependency,
        old_release=old_release,
        proposed_release=proposed_release,
        target_repository=identity.repository,
        target_revision=identity.head_sha,
        mechanism_status="established",
        exposure_status="to_evaluate",
        consequence_status="possible",
        old_wheels=(
            PublishedWheelArtifact(
                filename="demo-1.0-cp39-cp39-manylinux_2_17_x86_64.whl",
                tags=frozenset({old_tag}),
            ),
        ),
        proposed_wheels=(
            PublishedWheelArtifact(
                filename="demo-1.1-cp310-cp310-manylinux_2_17_x86_64.whl",
                tags=frozenset({proposed_tag}),
            ),
        ),
        removed_wheel_tags=frozenset({old_tag}),
        added_wheel_tags=frozenset({proposed_tag}),
        old_source_distribution_available=False,
        proposed_source_distribution_available=False,
        exposure_proposition="Exact target wheel compatibility remains to evaluate.",
        possible_consequence="The target may lose a prebuilt wheel path.",
    )
    return candidate, old_release


def _artifact_candidate_investigation(
    *,
    target_problem: bool = False,
) -> PublicPullRequestInvestigation:
    base = _supported_investigation()
    candidate, old_release = _artifact_candidate()
    assessment = evaluate_artifact_serviceability_impact(candidate)
    dependency = candidate.dependency
    source_context = RequirementsFileDependencyContext(
        repository=candidate.target_repository,
        revision=candidate.target_revision,
        normalized_package=dependency.normalized_package,
        source_evidence=dependency.source_evidence[0],
    )

    if target_problem:
        target_result = TargetArtifactEnvironmentProblem(
            state="ambiguous_target_job_selection",
            repository=candidate.target_repository,
            revision=candidate.target_revision,
            workflow_path=".github/workflows/ci.yml",
            detail="Target selection remains ambiguous.",
        )
    else:
        target_result = TargetArtifactEnvironmentEvidence(
            repository=candidate.target_repository,
            revision=candidate.target_revision,
            workflow_path=".github/workflows/ci.yml",
            job="test",
            runner=TargetArtifactEnvironmentFact(
                value="ubuntu-22.04",
                source="runs-on declaration at line 4",
            ),
            python_version=TargetArtifactEnvironmentFact(
                value="3.9",
                source="setup-python python-version at line 8",
            ),
            dependency_installation_declaration="observed",
            installation_declaration_source="pip install -r requirements.txt",
            limitations=(),
        )

    return replace(
        base,
        package_result=candidate.proposed_release,
        old_package_result=old_release,
        artifact_serviceability_candidate_result=candidate,
        target_artifact_environment_results=(
            DependencySourceArtifactEnvironmentResult(
                dependency_source=source_context,
                target_environment=target_result,
            ),
        ),
        artifact_serviceability_impact_result=assessment,
    )


def _artifact_problem_investigation() -> PublicPullRequestInvestigation:
    base = _supported_investigation()
    old_release = _package("1.0")
    problem = ArtifactServiceabilityEvidenceProblem(
        state="wheel_filename_uninterpretable",
        release_version="1.0",
        filename="broken.whl",
        detail="Published wheel filename could not be interpreted.",
    )
    return replace(
        base,
        old_package_result=old_release,
        artifact_serviceability_candidate_result=problem,
    )


def _no_artifact_candidate_investigation() -> PublicPullRequestInvestigation:
    return replace(
        _supported_investigation(),
        old_package_result=_package("1.0"),
        artifact_serviceability_candidate_result=None,
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
