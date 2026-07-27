"""Orchestrate the complete public-PR evidence pipeline from the command line.

Purpose of this file
--------------------
The focused modules each own one technical responsibility, but a user needs one
ordered workflow. This module is that coordinator. It:

* parses the repository and pull-request arguments;
* creates the three read-only GitHub clients;
* runs acquisition and interpretation stages in dependency order;
* maps different failure categories to shell exit codes;
* prints the resulting evidence and bounded classifications.

How this file relates to the rest of UpgradePilot
-------------------------------------------------
The main success path is:

1. ``github_client.py`` → PR identity and complete changed-file records;
2. ``dependency_change.py`` → supported pinned change or explicit abstention;
3. ``github_actions.py`` → exact-head workflow runs and jobs;
4. ``github_repository.py`` → exact-revision workflow definitions;
5. ``ci_authority.py`` → bounded authority result;
6. this file → human-readable presentation and process exit status.

The CLI intentionally does not duplicate lower-level parsing or decision rules. It
owns *when* each stage runs and *how* its result is presented. This separation lets
tests exercise acquisition and interpretation independently from terminal output.

Exit-code contract
------------------
* ``0``: the analysis completed, including normal unsupported/unresolved outcomes;
* ``2``: user input was outside the supported grammar;
* ``3``: GitHub evidence could not be acquired through a usable successful response;
* ``4``: GitHub returned success, but required response evidence was malformed or
  contradictory.
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
    """Create and configure the CLI parser without reading process arguments.

    Keeping parser construction separate from ``main`` makes the command interface
    directly testable and avoids performing work merely by importing this module.
    """

    parser = argparse.ArgumentParser(
        prog="upgradepilot",
        description=(
            "Acquire exact dependency and exact-head CI-authority evidence "
            "for a public GitHub pull request."
        ),
    )

    # These are positional arguments because both values are required to identify the
    # target PR. ``type=int`` asks argparse to convert the second token before ``main``
    # passes it to the stricter positive-number validator in ``github_client.py``.
    parser.add_argument(
        "repository", help="Public repository in owner/repository form."
    )
    parser.add_argument("pull_number", type=int, help="GitHub pull-request number.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the current evidence pipeline and return a shell exit status.

    ``argv`` is optional so normal execution can use the process command line, while
    tests or embedding code can supply a controlled sequence of argument strings.

    This function is orchestration rather than domain logic. Each assignment represents
    a handoff from one focused module to the next.
    """

    # ``parse_args(None)`` reads the real process arguments. Passing a sequence makes
    # the same function deterministic in tests.
    args = build_parser().parse_args(argv)

    # Authentication is optional for public repositories. Reading the environment once
    # and passing the same token to every client keeps their request identity consistent.
    token = os.getenv("GITHUB_TOKEN")

    # Three focused clients share the transport foundation in ``github_api.py`` but
    # retain separate resource-specific responsibilities.
    pull_client = GitHubReadClient(token=token)
    actions_client = GitHubActionsClient(token=token)
    repository_client = GitHubRepositoryClient(token=token)

    try:
        # Stage 1: freeze the PR identity, including the exact head SHA and declared
        # changed-file count.
        pull_request = pull_client.get_pull_request(
            args.repository, args.pull_number
        )

        # Stage 2: acquire every changed-file record and prove count completeness.
        changed_files = pull_client.get_changed_files(pull_request)

        # Stage 3: interpret validated patches as one supported pinned update or an
        # explicit unsupported result. This stage performs no network I/O.
        dependency_result = extract_pinned_dependency_change(changed_files)

        # These values begin empty because CI acquisition is conditional. Their explicit
        # types document the nested evidence shape used later by presentation code.
        workflow_evidence: tuple[
            tuple[WorkflowRun, tuple[WorkflowJob, ...]], ...
        ] = ()
        authority_result: CIAuthorityResult | None = None

        # CI work requires a known dependency identity. If extraction abstains, there is
        # no reliable package/file target for the later command rule, so orchestration
        # stops honestly instead of spending requests on an undefined question.
        if isinstance(dependency_result, PinnedDependencyChange):
            workflow_runs = actions_client.get_exact_head_workflow_runs(pull_request)

            # The comprehension keeps each run beside the jobs acquired specifically
            # for it. Converting immediately to a tuple freezes that relationship.
            workflow_evidence = tuple(
                (run, actions_client.get_workflow_jobs(pull_request, run))
                for run in workflow_runs
            )

            # Join runtime evidence with the exact workflow definition used by each run.
            # ``WorkflowAuthorityInput`` prevents jobs/definitions from being passed as
            # unrelated parallel collections to the evaluator.
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

            # This call is deterministic interpretation only; all network acquisition
            # has already occurred in the three clients above.
            authority_result = evaluate_ci_authority(
                dependency_result,
                authority_inputs,
            )

    # Exception order preserves the product's distinct failure categories. These are
    # not normal unsupported analysis results; they stop the pipeline with non-zero
    # process statuses.
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

    # Presentation begins only after the acquisition/interpretation try block completes.
    # These lines report evidence; they do not create a recommendation.
    print("UpgradePilot public pull-request evidence")
    print(f"Repository: {pull_request.repository}")
    print(f"PR: {pull_request.number}")
    print(f"Title: {pull_request.title}")
    print(f"Author: {pull_request.author}")
    print(f"State: {pull_request.state}")

    # Convert the boolean to lowercase text so output is stable and conventional for a
    # command-line report rather than Python's capitalized ``True``/``False`` spelling.
    print(f"Merged: {str(pull_request.merged).lower()}")
    print(f"Base: {pull_request.base_ref} @ {pull_request.base_sha}")
    print(f"Head: {pull_request.head_ref} @ {pull_request.head_sha}")
    print(f"Changed-file records: {len(changed_files)}")
    for changed_file in changed_files:
        print(f"Changed file: {changed_file.filename} ({changed_file.status})")

    # ``isinstance`` narrows the dependency-result union and mirrors the conditional CI
    # branch above. Inside this block, package/version fields are safe to access.
    if isinstance(dependency_result, PinnedDependencyChange):
        print("Dependency change: supported")
        print(f"Source file: {dependency_result.source_file}")
        print(f"Package: {dependency_result.package}")
        print(f"Old version: {dependency_result.old_version}")
        print(f"Proposed version: {dependency_result.proposed_version}")
        print(f"Exact-head workflow runs: {len(workflow_evidence)}")
        for run, jobs in workflow_evidence:
            # ``or 'none'`` converts a nullable conclusion into explicit output without
            # changing the underlying record.
            print(
                f"Workflow: {run.name} | status={run.status} | "
                f"conclusion={run.conclusion or 'none'} | jobs={len(jobs)}"
            )
            for job in jobs:
                # ``None`` means step evidence was unavailable; an empty tuple means an
                # explicit zero. The output preserves that difference as unknown vs 0.
                step_count = "unknown" if job.steps is None else str(len(job.steps))
                print(
                    f"  Job: {job.name} | status={job.status} | "
                    f"conclusion={job.conclusion or 'none'} | steps={step_count}"
                )

        # The earlier supported-dependency branch always assigns ``authority_result``.
        # The assertion documents that control-flow invariant and narrows the optional
        # type before the following attribute access.
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
        # Unsupported dependency extraction is a completed, honest analysis result—not
        # an exception. Therefore the process still returns zero after explaining why
        # CI evidence was not acquired or evaluated.
        print("Dependency change: unsupported")
        print(f"Reason: {dependency_result.reason}")
        print(f"Detail: {dependency_result.detail}")
        print("Exact-head workflow evidence: not acquired")
        print("CI authority: not evaluated")

    return 0
