"""Command-line interface for the current read-only UpgradePilot investigation.

The CLI owns arguments, environment input, rendering, and shell exit policy. Application
sequencing lives in ``investigation.py`` so future interfaces can reuse the same typed
investigation without duplicating provider/domain orchestration.
"""

from __future__ import annotations

import argparse
import os
from collections.abc import Sequence

from .ci.dependency_exercise import DependencyCIExerciseResult
from .dependency.change import DependencyChangeProblem, DependencyVersionChange
from .github.api import GitHubAcquisitionError, GitHubResponseError
from .github.identity import UpgradePilotInputError
from .investigation import PublicPullRequestInvestigation, investigate_public_pull_request
from .pypi.release import PackageReleaseEvidence, PackageReleaseProblem, PackageReleaseResult
from .target.python import (
    TargetPythonDeclaration,
    TargetPythonDeclarationProblem,
    TargetPythonEvidence,
)
from .target.relevance import TargetPythonRelevanceResult
from .upstream.claim import (
    GroundedPythonSupportDropClaim,
    UpstreamSupportDropClaimProblem,
    UpstreamSupportDropClaimResult,
)
from .upstream.interval import (
    AuthoritativeUpstreamIntervalEvidence,
    UpstreamIntervalAuthorityProblem,
    UpstreamIntervalAuthorityResult,
)
from .upstream.repository import (
    UpstreamRepositoryEvidence,
    UpstreamRepositoryProblem,
    UpstreamRepositoryResult,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="upgradepilot",
        description=(
            "Acquire exact dependency, CI, package/upstream, bounded semantic, and "
            "conditionally activated target-Python evidence for a public GitHub pull request."
        ),
    )
    parser.add_argument("repository", help="Public repository in owner/repository form.")
    parser.add_argument("pull_number", type=int, help="GitHub pull-request number.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        investigation = investigate_public_pull_request(
            args.repository,
            args.pull_number,
            token=os.getenv("GITHUB_TOKEN"),
        )
    except UpgradePilotInputError as exc:
        print(f"Input rejected: {exc}")
        return 2
    except GitHubAcquisitionError as exc:
        print("Acquisition failed.")
        print(f"Reason: {exc.reason}")
        print(f"Detail: {exc}")
        if exc.status_code is not None:
            print(f"HTTP status: {exc.status_code}")
        return 3
    except GitHubResponseError as exc:
        print("GitHub response could not establish the required evidence.")
        print(f"Detail: {exc}")
        return 4

    _print_investigation(investigation)
    return 0


def _print_investigation(result: PublicPullRequestInvestigation) -> None:
    pull_request = result.pull_request
    print("UpgradePilot public pull-request evidence")
    print(f"Repository: {pull_request.repository}")
    print(f"PR: {pull_request.number}")
    print(f"Title: {pull_request.title}")
    print(f"Author: {pull_request.author}")
    print(f"State: {pull_request.state}")
    print(f"Merged: {str(pull_request.merged).lower()}")
    print(f"Base: {pull_request.base_ref} @ {pull_request.base_sha}")
    print(f"Head: {pull_request.head_ref} @ {pull_request.head_sha}")
    print(f"Changed-file records: {len(result.changed_files)}")
    for changed_file in result.changed_files:
        print(f"Changed file: {changed_file.filename} ({changed_file.status})")

    dependency_result = result.dependency_result
    if isinstance(dependency_result, DependencyVersionChange):
        _print_dependency_change(dependency_result)

        print(f"Exact-head workflow runs: {len(result.workflow_evidence)}")
        for run, jobs in result.workflow_evidence:
            print(
                f"Workflow: {run.name} | status={run.status} | "
                f"conclusion={run.conclusion or 'none'} | jobs={len(jobs)}"
            )
            for job in jobs:
                step_count = "unknown" if job.steps is None else str(len(job.steps))
                print(
                    f"  Job: {job.name} | status={job.status} | "
                    f"conclusion={job.conclusion or 'none'} | steps={step_count}"
                )

        assert result.ci_exercise_result is not None
        _print_ci_dependency_exercise(result.ci_exercise_result)

        assert result.package_result is not None
        _print_package_and_upstream_repository(
            result.package_result,
            result.upstream_repository_result,
        )
        _print_upstream_interval(result.upstream_interval_result)
        _print_support_drop(result.upstream_support_drop_result)

        if result.target_python_result is None:
            print("Target Python declaration: not activated")
        else:
            _print_target_python(result.target_python_result)
        _print_target_relevance(result.target_python_relevance_result)
        return

    assert isinstance(dependency_result, DependencyChangeProblem)
    print("Dependency change: unsupported")
    print(f"Reason: {dependency_result.reason}")
    print(f"Detail: {dependency_result.detail}")
    print("Exact-head workflow evidence: not acquired")
    print("CI dependency exercise: not evaluated")
    print("Package evidence: not evaluated")
    print("Upstream repository: not evaluated")
    print("Upstream interval authority: not evaluated")
    print("Upstream support-drop result: not evaluated")
    print("Target Python declaration: not activated")
    print("Target Python relevance: not evaluated")


def _print_dependency_change(dependency: DependencyVersionChange) -> None:
    print("Dependency change: supported")
    print(f"Package: {dependency.package}")
    print(f"Old version: {dependency.old_version}")
    print(f"Proposed version: {dependency.proposed_version}")
    print(f"Dependency evidence records: {len(dependency.source_evidence)}")

    for evidence in dependency.source_evidence:
        print(f"Dependency evidence: {evidence.path}")
        print(f"  Format: {evidence.file_format}")
        print(f"  Extraction method: {evidence.extraction_method}")

    for limitation in dependency.limitations:
        print(f"Dependency limitation: {limitation}")


def _print_ci_dependency_exercise(result: DependencyCIExerciseResult) -> None:
    print(f"CI dependency exercise: {result.state}")
    print(f"CI dependency exercise reason: {result.reason}")
    print(f"CI dependency exercise detail: {result.detail}")
    for workflow in result.workflows:
        print(
            f"  Dependency exercise workflow: {workflow.workflow_name} | "
            f"state={workflow.state} | reason={workflow.reason}"
        )
        if workflow.install_command is not None:
            print(f"    Install evidence: {workflow.install_command}")
        if workflow.execution_command is not None:
            print(f"    Execution evidence: {workflow.execution_command}")


def _print_target_python(result: TargetPythonEvidence) -> None:
    if isinstance(result, TargetPythonDeclarationProblem):
        print(f"Target Python declaration: {result.state}")
        print(f"Target Python source: {result.path} @ {result.revision}")
        if result.blob_sha is not None:
            print(f"Target Python blob SHA: {result.blob_sha}")
        print(f"Target Python detail: {result.detail}")
        return

    assert isinstance(result, TargetPythonDeclaration)
    print("Target Python declaration: available")
    print(f"Target Python source: {result.path} @ {result.revision}")
    print(f"Target Python blob SHA: {result.blob_sha}")
    print(f"Target requires-python: {result.requires_python}")


def _print_package_and_upstream_repository(
    package_result: PackageReleaseResult,
    upstream_result: UpstreamRepositoryResult | None,
) -> None:
    if isinstance(package_result, PackageReleaseProblem):
        print(f"Package evidence: {package_result.state}")
        print(f"Package detail: {package_result.detail}")
        print("Upstream repository: not evaluated")
        return

    assert isinstance(package_result, PackageReleaseEvidence)
    print("Package evidence: available")
    print(
        f"Published package: {package_result.published_name}=="
        f"{package_result.published_version}"
    )
    print(f"Distribution files: {package_result.distribution_file_count}")

    if upstream_result is None:
        print("Upstream repository: not evaluated")
        return
    if isinstance(upstream_result, UpstreamRepositoryProblem):
        print(f"Upstream repository: {upstream_result.state}")
        print(f"Upstream detail: {upstream_result.detail}")
        return

    assert isinstance(upstream_result, UpstreamRepositoryEvidence)
    print("Upstream repository: available")
    print(f"Upstream repository identity: {upstream_result.repository}")
    print(
        f"Provenance coverage: {len(upstream_result.provenance)} of "
        f"{package_result.distribution_file_count} files"
    )
    unavailable = ", ".join(upstream_result.provenance_unavailable_files) or "none"
    print(f"Provenance unavailable files: {unavailable}")


def _print_upstream_interval(result: UpstreamIntervalAuthorityResult | None) -> None:
    if result is None:
        print("Upstream interval authority: not established")
        return
    if isinstance(result, UpstreamIntervalAuthorityProblem):
        print(f"Upstream interval authority: {result.state}")
        print(f"Upstream interval detail: {result.detail}")
        return

    assert isinstance(result, AuthoritativeUpstreamIntervalEvidence)
    print("Upstream interval authority: available")
    print(f"Upstream interval authority basis: {result.authority_basis}")
    if result.crossed_releases is not None:
        print(
            "Crossed releases: "
            + ", ".join(result.crossed_releases.ordered_versions)
        )


def _print_support_drop(result: UpstreamSupportDropClaimResult | None) -> None:
    if result is None:
        print("Upstream support-drop result: not evaluated")
        return
    if isinstance(result, UpstreamSupportDropClaimProblem):
        print(f"Upstream support-drop result: {result.state}")
        print(f"Upstream support-drop detail: {result.detail}")
        return

    assert isinstance(result, GroundedPythonSupportDropClaim)
    print("Upstream support-drop result: grounded")
    print(f"Dropped Python line: {result.python_line}")
    print(f"Introduced in upstream release: {result.introduced_in_version}")
    print(f"Grounded source records: {len(result.source_evidence)}")


def _print_target_relevance(result: TargetPythonRelevanceResult | None) -> None:
    if result is None:
        print("Target Python relevance: not evaluated")
        return
    print(f"Target Python relevance: {result.state}")
    print(f"Target Python relevance detail: {result.detail}")


__all__ = ("build_parser", "main")
