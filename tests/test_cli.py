"""Test user-facing orchestration without live network requests."""

from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout
from datetime import datetime, timezone
from types import SimpleNamespace
from unittest.mock import patch

from upgradepilot.cli import _print_dependency_change, main
from upgradepilot.dependency_analysis import DependencyChangeAnalysis
from upgradepilot.dependency_change import (
    DependencyChangeEvidenceProblem,
    DependencyFileEvidence,
    DependencyVersionChange,
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
from upgradepilot.target_python import TargetPythonDeclaration
from upgradepilot.upstream_source import (
    UpstreamReleaseEvidence,
    UpstreamSourceProblem,
)


class CLITests(unittest.TestCase):
    """Protect coordinator input, stopping behavior, and generic presentation."""

    def test_complete_package_and_upstream_evidence_is_presented(self) -> None:
        package = _package_evidence()
        upstream = _upstream_evidence(package)

        exit_code, output, package_client, resolver, evaluate = self._run_cli(
            dependency_analysis_result=_supported_analysis(),
            package_result=package,
            upstream_result=upstream,
        )

        self.assertEqual(exit_code, 0)
        self.assertIn("Dependency change: supported", output)
        self.assertIn("Dependency evidence records: 1", output)
        self.assertIn("Dependency evidence: requirements-dev.txt", output)
        self.assertIn("  Format: exact_requirement", output)
        self.assertIn("  Extraction method: changed_file_patch", output)
        self.assertIn("Target Python declaration: available", output)
        self.assertIn("Target Python source: pyproject.toml @ head-sha", output)
        self.assertIn("Target requires-python: >=3.10", output)
        self.assertIn("CI dependency exercise: proven", output)
        self.assertIn(
            "CI dependency exercise reason: exact_head_dependency_exercised",
            output,
        )
        self.assertNotIn("CI authority", output)
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
        self.assertNotIn("Source file:", output)
        package_client.get_release.assert_called_once_with("pytest", "9.0.3")
        resolver.resolve.assert_called_once_with(package)

        evaluated_dependency = evaluate.call_args.args[0]
        self.assertIsInstance(evaluated_dependency, DependencyVersionChange)
        self.assertEqual(
            evaluate.call_args.kwargs["direct_requirements_install_path"],
            "requirements-dev.txt",
        )

    def test_uv_lock_analysis_uses_no_requirements_path_and_renders_provenance(self) -> None:
        unresolved = _exercise_result(
            state="unresolved",
            reason="dependency_exercise_not_proven",
            detail="Successful CI exists, but dependency exercise was not proven.",
        )
        package_problem = _package_problem(
            package="soupsieve",
            version="2.8.4",
        )

        exit_code, output, package_client, resolver, evaluate = self._run_cli(
            dependency_analysis_result=_uv_analysis(),
            exercise_result=unresolved,
            package_result=package_problem,
        )

        self.assertEqual(exit_code, 0)
        self.assertIn("Package: soupsieve", output)
        self.assertIn("Old version: 2.6", output)
        self.assertIn("Proposed version: 2.8.4", output)
        self.assertIn("Dependency evidence: uv.lock", output)
        self.assertIn("  Format: uv_lock", output)
        self.assertIn("  Extraction method: exact_base_head_files", output)
        self.assertIn("  Base revision: base-sha", output)
        self.assertIn("  Base blob SHA: base-blob", output)
        self.assertIn("  Base bytes: 606307", output)
        self.assertIn("  Head revision: head-sha", output)
        self.assertIn("  Head blob SHA: head-blob", output)
        self.assertIn("  Head bytes: 606313", output)
        self.assertIn("CI dependency exercise: unresolved", output)
        self.assertIsNone(
            evaluate.call_args.kwargs["direct_requirements_install_path"]
        )
        package_client.get_release.assert_called_once_with("soupsieve", "2.8.4")
        resolver.resolve.assert_not_called()

    def test_unresolved_ci_exercise_does_not_block_package_or_upstream(self) -> None:
        package = _package_evidence()
        upstream = _upstream_evidence(package)
        unresolved = _exercise_result(
            state="unresolved",
            reason="dependency_exercise_not_proven",
            detail="Successful CI exists, but dependency exercise was not proven.",
        )

        exit_code, output, package_client, resolver, _ = self._run_cli(
            dependency_analysis_result=_supported_analysis(),
            exercise_result=unresolved,
            package_result=package,
            upstream_result=upstream,
        )

        self.assertEqual(exit_code, 0)
        self.assertIn("CI dependency exercise: unresolved", output)
        self.assertIn("Package evidence: available", output)
        self.assertIn("Upstream source: available", output)
        package_client.get_release.assert_called_once_with("pytest", "9.0.3")
        resolver.resolve.assert_called_once_with(package)

    def test_no_successful_ci_state_uses_new_label(self) -> None:
        problem = _package_problem()
        no_successful_ci = _exercise_result(
            state="no_successful_ci",
            reason="no_successful_exact_head_jobs",
            detail="No completed successful exact-head job was available.",
        )

        exit_code, output, _, _, _ = self._run_cli(
            dependency_analysis_result=_supported_analysis(),
            exercise_result=no_successful_ci,
            package_result=problem,
        )

        self.assertEqual(exit_code, 0)
        self.assertIn("CI dependency exercise: no_successful_ci", output)
        self.assertNotIn("CI authority", output)

    def test_package_problem_stops_upstream_resolution(self) -> None:
        problem = _package_problem()

        exit_code, output, package_client, resolver, _ = self._run_cli(
            dependency_analysis_result=_supported_analysis(),
            package_result=problem,
        )

        self.assertEqual(exit_code, 0)
        self.assertIn("Target Python declaration: available", output)
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

        exit_code, output, _, resolver, _ = self._run_cli(
            dependency_analysis_result=_supported_analysis(),
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

    def test_dependency_problem_skips_all_dependent_stages(self) -> None:
        exit_code, output, package_client, resolver, evaluate = self._run_cli(
            dependency_analysis_result=DependencyChangeEvidenceProblem(
                reason="no_supported_dependency_file",
                detail="No admitted dependency source was found.",
            )
        )

        self.assertEqual(exit_code, 0)
        self.assertIn("Dependency change: unsupported", output)
        self.assertIn("Reason: no_supported_dependency_file", output)
        self.assertIn("Target Python declaration: not evaluated", output)
        self.assertIn("CI dependency exercise: not evaluated", output)
        self.assertNotIn("CI authority", output)
        self.assertIn("Package evidence: not evaluated", output)
        self.assertIn("Upstream source: not evaluated", output)
        package_client.get_release.assert_not_called()
        resolver.resolve.assert_not_called()
        evaluate.assert_not_called()

    def test_uv_lock_evidence_presentation_preserves_exact_provenance(self) -> None:
        output = _render_dependency(_uv_analysis().dependency)

        self.assertIn("Dependency evidence: uv.lock", output)
        self.assertIn("  Format: uv_lock", output)
        self.assertIn("  Extraction method: exact_base_head_files", output)
        self.assertIn("  Base revision: base-sha", output)
        self.assertIn("  Base blob SHA: base-blob", output)
        self.assertIn("  Base bytes: 606307", output)
        self.assertIn("  Head revision: head-sha", output)
        self.assertIn("  Head blob SHA: head-blob", output)
        self.assertIn("  Head bytes: 606313", output)

    def test_multiple_evidence_records_and_limitations_render_generically(self) -> None:
        dependency = DependencyVersionChange(
            package="demo",
            normalized_package="demo",
            old_version="1.0",
            proposed_version="1.1",
            source_evidence=(
                DependencyFileEvidence(
                    path="requirements.txt",
                    file_format="exact_requirement",
                    extraction_method="changed_file_patch",
                ),
                DependencyFileEvidence(
                    path="uv.lock",
                    file_format="uv_lock",
                    extraction_method="exact_base_head_files",
                ),
            ),
            limitations=("Dependency role was not established.",),
        )

        output = _render_dependency(dependency)

        self.assertIn("Dependency evidence records: 2", output)
        self.assertEqual(output.count("Dependency evidence:"), 2)
        self.assertIn(
            "Dependency limitation: Dependency role was not established.",
            output,
        )

    def _run_cli(
        self,
        *,
        dependency_analysis_result: DependencyChangeAnalysis
        | DependencyChangeEvidenceProblem,
        exercise_result: object | None = None,
        package_result: PackageReleaseEvidence | PackageReleaseProblem | None = None,
        upstream_result: UpstreamReleaseEvidence | UpstreamSourceProblem | None = None,
    ) -> tuple[int, str, object, object, object]:
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
        target_python = TargetPythonDeclaration(
            state="available",
            path="pyproject.toml",
            revision="head-sha",
            blob_sha="target-blob-sha",
            requires_python=">=3.10",
        )

        with (
            patch("upgradepilot.cli.analyze_dependency_change") as analyze,
            patch("upgradepilot.cli.evaluate_dependency_ci_exercise") as evaluate,
            patch("upgradepilot.cli.interpret_target_python_declaration") as interpret_target,
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
            repository_client = repository_client_type.return_value
            repository_client.get_exact_head_workflow_file.return_value = SimpleNamespace(
                state="available",
                text="name: regression",
            )
            target_file_evidence = SimpleNamespace(
                path="pyproject.toml",
                revision="head-sha",
                blob_sha="target-blob-sha",
                content='[project]\nrequires-python = ">=3.10"\n',
            )
            repository_client.get_exact_head_text_file.return_value = target_file_evidence

            analyze.return_value = dependency_analysis_result
            evaluate.return_value = exercise_result or _exercise_result()
            interpret_target.return_value = target_python

            package_client = package_client_type.return_value
            package_client.get_release.return_value = package_result
            resolver = resolver_type.return_value
            resolver.resolve.return_value = upstream_result

            stream = io.StringIO()
            with redirect_stdout(stream):
                exit_code = main(["googlefonts/glyphsLib", "1145"])

            analyze.assert_called_once_with(
                pull_request,
                (changed_file,),
                repository_client,
            )

            if isinstance(dependency_analysis_result, DependencyChangeAnalysis):
                repository_client.get_exact_head_text_file.assert_called_once_with(
                    pull_request,
                    "pyproject.toml",
                )
                interpret_target.assert_called_once_with(target_file_evidence)
            else:
                repository_client.get_exact_head_text_file.assert_not_called()
                interpret_target.assert_not_called()

        return exit_code, stream.getvalue(), package_client, resolver, evaluate


def _exercise_result(
    *,
    state: str = "proven",
    reason: str = "exact_head_dependency_exercised",
    detail: str = "The dependency was consumed and directly exercised.",
) -> SimpleNamespace:
    return SimpleNamespace(
        state=state,
        reason=reason,
        detail=detail,
        workflows=(),
    )


def _supported_analysis() -> DependencyChangeAnalysis:
    return DependencyChangeAnalysis(
        dependency=DependencyVersionChange(
            package="pytest",
            normalized_package="pytest",
            old_version="9.0.2",
            proposed_version="9.0.3",
            source_evidence=(
                DependencyFileEvidence(
                    path="requirements-dev.txt",
                    file_format="exact_requirement",
                    extraction_method="changed_file_patch",
                ),
            ),
        ),
        direct_requirements_install_path="requirements-dev.txt",
    )


def _uv_analysis() -> DependencyChangeAnalysis:
    return DependencyChangeAnalysis(
        dependency=DependencyVersionChange(
            package="soupsieve",
            normalized_package="soupsieve",
            old_version="2.6",
            proposed_version="2.8.4",
            source_evidence=(
                DependencyFileEvidence(
                    path="uv.lock",
                    file_format="uv_lock",
                    extraction_method="exact_base_head_files",
                    base_revision="base-sha",
                    base_blob_sha="base-blob",
                    base_byte_count=606307,
                    head_revision="head-sha",
                    head_blob_sha="head-blob",
                    head_byte_count=606313,
                ),
            ),
        ),
        direct_requirements_install_path=None,
    )


def _render_dependency(dependency: DependencyVersionChange) -> str:
    stream = io.StringIO()
    with redirect_stdout(stream):
        _print_dependency_change(dependency)
    return stream.getvalue()


def _package_problem(
    *,
    package: str = "pytest",
    version: str = "9.0.3",
) -> PackageReleaseProblem:
    return PackageReleaseProblem(
        state="version_not_found",
        requested_package=package,
        normalized_package=package,
        requested_version=version,
        source_url=f"https://pypi.org/pypi/{package}/{version}/json",
        detail="The exact version was not established.",
        status_code=404,
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
