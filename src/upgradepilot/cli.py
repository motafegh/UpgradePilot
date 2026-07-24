"""Command-line orchestration for the public-PR vertical slice.

The CLI owns user input, execution order, exit-code mapping, and presentation.
Focused modules own pull-request acquisition, dependency interpretation, Actions
acquisition, exact-head workflow-file acquisition, and CI-authority evaluation so
that each stage remains readable and independently testable.
"""

from __future__ import annotations

import argparse
import os
from collections.abc import Sequence

from .ci_authority import (
    CIAuthorityResult,
    WorkflowAuthorityInput,
    evaluate_ci_authority,
)
from .dependency_change import (
    PinnedDependencyChange,
    extract_pinned_dependency_change,
)
from .github_actions import GitHubActionsClient, WorkflowJob, WorkflowRun
from .github_api import GitHubAcquisitionError, GitHubResponseError
from .github_client import GitHubReadClient, UpgradePilotInputError
from .github_repository import GitHubRepositoryClient


def build_parser() -> argparse.ArgumentParser:
    """Build the supported command-line interface without executing it."""

    parser = argparse.ArgumentParser(
        prog="upgradepilot",
        description=(
            "Acquire exact dependency and exact-head CI-authority evidence "
            "for a public GitHub pull request."
        ),
    )
    parser.add_argument(
        "repository", help="Public repository in owner/repository form."
    )
    parser.add_argument("pull_number", type=int, help="GitHub pull-request number.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the current public-PR evidence path and return a shell exit status.

    Returns:
        ``0`` for a completed supported or unsupported analysis, ``2`` for
        rejected input, ``3`` for acquisition failure, and ``4`` for a
        successful GitHub response that could not establish required evidence.
    """

    args = build_parser().parse_args(argv)
    token = os.getenv("GITHUB_TOKEN")
    pull_client = GitHubReadClient(token=token)
    actions_client = GitHubActionsClient(token=token)
    repository_client = GitHubRepositoryClient(token=token)

    try:
        pull_request = pull_client.get_pull_request(
            args.repository, args.pull_number
        )
        changed_files = pull_client.get_changed_files(pull_request)
        dependency_result = extract_pinned_dependency_change(changed_files)

        workflow_evidence: tuple[
            tuple[WorkflowRun, tuple[WorkflowJob, ...]], ...
        ] = ()
        authority_result: CIAuthorityResult | None = None

        # CI work is conditional on a supported dependency identity. An
        # unsupported dependency shape already supplies an honest stopping state.
        if isinstance(dependency_result, PinnedDependencyChange):
            workflow_runs = actions_client.get_exact_head_workflow_runs(pull_request)
            workflow_evidence = tuple(
                (run, actions_client.get_workflow_jobs(pull_request, run))
                for run in workflow_runs
            )

            # Resolve each run to the workflow text used at the exact PR head.
            # The evaluator receives validated records and performs no network I/O.
            authority_inputs = tuple(
                WorkflowAuthorityInput(
                    run=run,
                    jobs=jobs,
                    definition=repository_client.get_exact_head_workflow_file(
                        pull_request, run
                    ),
                )
                for run, jobs in workflow_evidence
            )
            authority_result = evaluate_ci_authority(
                dependency_result,
                authority_inputs,
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

    if isinstance(dependency_result, PinnedDependencyChange):
        print("Dependency change: supported")
        print(f"Source file: {dependency_result.source_file}")
        print(f"Package: {dependency_result.package}")
        print(f"Old version: {dependency_result.old_version}")
        print(f"Proposed version: {dependency_result.proposed_version}")
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

        assert authority_result is not None
        print(f"CI authority: {authority_result.status}")
        print(f"CI authority reason: {authority_result.reason}")
        print(f"CI authority detail: {authority_result.detail}")
        for assessment in authority_result.workflows:
            print(
                f"  Authority workflow: {assessment.workflow_name} | "
                f"status={assessment.status} | reason={assessment.reason}"
            )
            if assessment.install_command is not None:
                print(f"    Install evidence: {assessment.install_command}")
            if assessment.execution_command is not None:
                print(f"    Execution evidence: {assessment.execution_command}")
    else:
        print("Dependency change: unsupported")
        print(f"Reason: {dependency_result.reason}")
        print(f"Detail: {dependency_result.detail}")
        print("Exact-head workflow evidence: not acquired")
        print("CI authority: not evaluated")

    return 0
