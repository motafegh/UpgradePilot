"""Orchestrate the public-PR evidence pipeline from the command line.

Step 8 routes complete changed-file evidence through one multi-format dependency
coordinator. The command receives one canonical dependency identity plus a separate
optional requirements path for the current CI rule; no parser-specific branch remains
in CLI orchestration.
"""

from __future__ import annotations

import argparse
import os
from collections.abc import Sequence

from .ci_dependency_exercise import (
    DependencyCIExerciseResult,
    WorkflowDependencyExerciseInput,
    evaluate_dependency_ci_exercise,
)
from .dependency_analysis import (
    DependencyChangeAnalysis,
    analyze_dependency_change,
)
from .dependency_change import (
    DependencyChangeEvidenceProblem,
    DependencyVersionChange,
)
from .github_actions import GitHubActionsClient, WorkflowJob, WorkflowRun
from .github_api import GitHubAcquisitionError, GitHubResponseError
from .github_client import GitHubReadClient, UpgradePilotInputError
from .github_release import GitHubReleaseClient
from .github_repository import GitHubRepositoryClient
from .pypi_client import (
    PackageReleaseEvidence,
    PackageReleaseProblem,
    PackageReleaseResult,
    PyPIReleaseClient,
)
from .target_python import (
    TargetPythonDeclaration,
    TargetPythonDeclarationProblem,
    TargetPythonEvidence,
    interpret_target_python_declaration,
)
from .upstream_source import (
    UpstreamReleaseEvidence,
    UpstreamSourceProblem,
    UpstreamSourceResolver,
    UpstreamSourceResult,
)


def build_parser() -> argparse.ArgumentParser:
    """Create and configure the CLI parser without reading process arguments."""

    parser = argparse.ArgumentParser(
        prog="upgradepilot",
        description=(
            "Acquire exact dependency, target Python, CI dependency-exercise, package, "
            "and upstream-release evidence for a public GitHub pull request."
        ),
    )
    parser.add_argument(
        "repository", help="Public repository in owner/repository form."
    )
    parser.add_argument("pull_number", type=int, help="GitHub pull-request number.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the current evidence pipeline and return a shell exit status."""

    args = build_parser().parse_args(argv)
    token = os.getenv("GITHUB_TOKEN")

    pull_client = GitHubReadClient(token=token)
    actions_client = GitHubActionsClient(token=token)
    repository_client = GitHubRepositoryClient(token=token)
    package_client = PyPIReleaseClient()
    upstream_resolver = UpstreamSourceResolver(
        github_release_client=GitHubReleaseClient(token=token)
    )

    try:
        pull_request = pull_client.get_pull_request(
            args.repository,
            args.pull_number,
        )
        changed_files = pull_client.get_changed_files(pull_request)

        analysis_result = analyze_dependency_change(
            pull_request,
            changed_files,
            repository_client,
        )
        if isinstance(analysis_result, DependencyChangeAnalysis):
            dependency_result: DependencyVersionChange | DependencyChangeEvidenceProblem = (
                analysis_result.dependency
            )
            direct_requirements_install_path = (
                analysis_result.direct_requirements_install_path
            )
        else:
            dependency_result = analysis_result
            direct_requirements_install_path = None

        target_python_result: TargetPythonEvidence | None = None
        workflow_evidence: tuple[
            tuple[WorkflowRun, tuple[WorkflowJob, ...]], ...
        ] = ()
        ci_exercise_result: DependencyCIExerciseResult | None = None
        package_result: PackageReleaseResult | None = None
        upstream_result: UpstreamSourceResult | None = None

        if isinstance(dependency_result, DependencyVersionChange):
            target_python_result = interpret_target_python_declaration(
                repository_client.get_exact_head_text_file(
                    pull_request,
                    "pyproject.toml",
                )
            )

            workflow_runs = actions_client.get_exact_head_workflow_runs(pull_request)
            workflow_evidence = tuple(
                (run, actions_client.get_workflow_jobs(pull_request, run))
                for run in workflow_runs
            )
            exercise_inputs = tuple(
                WorkflowDependencyExerciseInput(
                    run=run,
                    jobs=jobs,
                    definition=repository_client.get_exact_head_workflow_file(
                        pull_request,
                        run,
                    ),
                )
                for run, jobs in workflow_evidence
            )
            ci_exercise_result = evaluate_dependency_ci_exercise(
                dependency_result,
                exercise_inputs,
                direct_requirements_install_path=direct_requirements_install_path,
            )

            package_result = package_client.get_release(
                dependency_result.package,
                dependency_result.proposed_version,
            )
            if isinstance(package_result, PackageReleaseEvidence):
                upstream_result = upstream_resolver.resolve(package_result)

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

    print("UpgradePilot public pull-request evidence")
    print(f"Repository: {pull_request.repository}")
    print(f"PR: {pull_request.number}")
    print(f"Title: {pull_request.title}")
    print(f"Author: {pull_request.author}")
    print(f"State: {pull_request.state}")
    print(f"Merged: {str(pull_request.merged).lower()}")
    print(f"Base: {pull_request.base_ref} @ {pull_request.base_sha}")
    print(f"Head: {pull_request.head_ref} @ {pull_request.head_sha}")
    print(f"Changed-file records: {len(changed_files)}")
    for changed_file in changed_files:
        print(f"Changed file: {changed_file.filename} ({changed_file.status})")

    if isinstance(dependency_result, DependencyVersionChange):
        _print_dependency_change(dependency_result)

        assert target_python_result is not None
        _print_target_python(target_python_result)

        print(f"Exact-head workflow runs: {len(workflow_evidence)}")
        for run, jobs in workflow_evidence:
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

        assert ci_exercise_result is not None
        _print_ci_dependency_exercise(ci_exercise_result)

        assert package_result is not None
        _print_package_and_upstream(package_result, upstream_result)
    else:
        print("Dependency change: unsupported")
        print(f"Reason: {dependency_result.reason}")
        print(f"Detail: {dependency_result.detail}")
        print("Target Python declaration: not evaluated")
        print("Exact-head workflow evidence: not acquired")
        print("CI dependency exercise: not evaluated")
        print("Package evidence: not evaluated")
        print("Upstream source: not evaluated")

    return 0


def _print_dependency_change(dependency: DependencyVersionChange) -> None:
    """Present canonical identity and every source record without format branching."""

    print("Dependency change: supported")
    print(f"Package: {dependency.package}")
    print(f"Old version: {dependency.old_version}")
    print(f"Proposed version: {dependency.proposed_version}")
    print(f"Dependency evidence records: {len(dependency.source_evidence)}")

    for evidence in dependency.source_evidence:
        print(f"Dependency evidence: {evidence.path}")
        print(f"  Format: {evidence.file_format}")
        print(f"  Extraction method: {evidence.extraction_method}")
        if evidence.base_revision is not None:
            print(f"  Base revision: {evidence.base_revision}")
        if evidence.base_blob_sha is not None:
            print(f"  Base blob SHA: {evidence.base_blob_sha}")
        if evidence.base_byte_count is not None:
            print(f"  Base bytes: {evidence.base_byte_count}")
        if evidence.head_revision is not None:
            print(f"  Head revision: {evidence.head_revision}")
        if evidence.head_blob_sha is not None:
            print(f"  Head blob SHA: {evidence.head_blob_sha}")
        if evidence.head_byte_count is not None:
            print(f"  Head bytes: {evidence.head_byte_count}")

    for limitation in dependency.limitations:
        print(f"Dependency limitation: {limitation}")


def _print_ci_dependency_exercise(result: DependencyCIExerciseResult) -> None:
    """Present the shared CI exercise state without implying broader authority."""

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
    """Present target declaration evidence without evaluating its version range."""

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


def _print_package_and_upstream(
    package_result: PackageReleaseResult,
    upstream_result: UpstreamSourceResult | None,
) -> None:
    """Present typed package and upstream evidence without interpreting release prose."""

    if isinstance(package_result, PackageReleaseProblem):
        print(f"Package evidence: {package_result.state}")
        print(f"Package detail: {package_result.detail}")
        print("Upstream source: not evaluated")
        return

    print("Package evidence: available")
    print(
        f"Published package: {package_result.published_name}=="
        f"{package_result.published_version}"
    )
    print(f"Distribution files: {package_result.distribution_file_count}")

    assert upstream_result is not None
    if isinstance(upstream_result, UpstreamSourceProblem):
        print(f"Upstream source: {upstream_result.state}")
        print(f"Upstream detail: {upstream_result.detail}")
        return

    assert isinstance(upstream_result, UpstreamReleaseEvidence)
    release = upstream_result.github_release
    print("Upstream source: available")
    print(f"Upstream repository: {upstream_result.repository}")
    print(
        f"Provenance coverage: {len(upstream_result.provenance)} of "
        f"{package_result.distribution_file_count} files"
    )
    unavailable = ", ".join(upstream_result.provenance_unavailable_files) or "none"
    print(f"Provenance unavailable files: {unavailable}")
    print(f"Accepted tag: {release.requested_tag}")
    print(f"Release URL: {release.release_url}")
    print(f"Tag object SHA: {release.tag_object_sha}")
    print(f"Claim state: {upstream_result.claim_state}")
