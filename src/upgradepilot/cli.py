"""Orchestrate the complete public-PR evidence pipeline from the command line.

Purpose of this file
--------------------
The focused modules each own one technical responsibility, but a user needs one
ordered workflow. This module is that coordinator. It:

* parses the repository and pull-request arguments;
* creates the focused read-only GitHub and PyPI clients;
* runs acquisition and interpretation stages in dependency order;
* preserves typed unsupported, unavailable, and unresolved evidence states;
* maps exceptional GitHub failures to shell exit codes;
* prints concise evidence without producing a recommendation.

How this file relates to the rest of UpgradePilot
-------------------------------------------------
The main success path is:

1. ``github_client.py`` → PR identity and complete changed-file records;
2. ``dependency_change.py`` → supported pinned change or explicit abstention;
3. ``github_actions.py`` → exact-head workflow runs and jobs;
4. ``github_repository.py`` → exact-revision workflow definitions;
5. ``ci_authority.py`` → bounded CI-authority result;
6. ``pypi_client.py`` → exact package/version and distribution-file evidence;
7. ``upstream_source.py`` → provenance-backed exact GitHub release evidence;
8. this file → human-readable presentation and process exit status.

The CLI intentionally does not duplicate lower-level parsing, authority, or decision
rules. It owns *when* each stage runs and *how* its typed result is presented.

Exit-code contract
------------------
* ``0``: the analysis completed, including normal unsupported, unavailable, or
  unresolved evidence outcomes;
* ``2``: user input was outside the supported grammar;
* ``3``: GitHub PR/CI evidence could not be acquired through a usable response;
* ``4``: GitHub returned success, but required PR/CI evidence was malformed or
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
from .github_release import GitHubReleaseClient
from .github_repository import GitHubRepositoryClient
from .pypi_client import (
    PackageReleaseEvidence,
    PackageReleaseProblem,
    PackageReleaseResult,
    PyPIReleaseClient,
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
            "Acquire exact dependency, CI-authority, package, and upstream-release "
            "evidence for a public GitHub pull request."
        ),
    )
    parser.add_argument(
        "repository", help="Public repository in owner/repository form."
    )
    parser.add_argument("pull_number", type=int, help="GitHub pull-request number.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the current evidence pipeline and return a shell exit status.

    ``argv`` is optional so normal execution can use the process command line, while
    tests or embedding code can supply a controlled sequence of argument strings.
    This function coordinates focused components; it does not reinterpret their
    evidence contracts.
    """

    args = build_parser().parse_args(argv)

    # Authentication is optional for public repositories. Passing the same token to
    # every GitHub client keeps request identity consistent across PR, CI, repository,
    # release, and tag-ref acquisition.
    token = os.getenv("GITHUB_TOKEN")

    pull_client = GitHubReadClient(token=token)
    actions_client = GitHubActionsClient(token=token)
    repository_client = GitHubRepositoryClient(token=token)
    package_client = PyPIReleaseClient()
    upstream_resolver = UpstreamSourceResolver(
        github_release_client=GitHubReleaseClient(token=token)
    )

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

        workflow_evidence: tuple[
            tuple[WorkflowRun, tuple[WorkflowJob, ...]], ...
        ] = ()
        authority_result: CIAuthorityResult | None = None
        package_result: PackageReleaseResult | None = None
        upstream_result: UpstreamSourceResult | None = None

        # CI, package, and upstream acquisition all require one trusted dependency
        # identity. Unsupported extraction is therefore an honest stopping point.
        if isinstance(dependency_result, PinnedDependencyChange):
            workflow_runs = actions_client.get_exact_head_workflow_runs(pull_request)
            workflow_evidence = tuple(
                (run, actions_client.get_workflow_jobs(pull_request, run))
                for run in workflow_runs
            )

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

            # Package identity is acquired from the exact trusted dependency proposal.
            # A typed package problem is preserved for presentation rather than raised.
            package_result = package_client.get_release(
                dependency_result.package,
                dependency_result.proposed_version,
            )

            # Upstream resolution depends on trusted package evidence, especially the
            # immutable distribution-file records and publisher-supplied Source links.
            if isinstance(package_result, PackageReleaseEvidence):
                upstream_result = upstream_resolver.resolve(package_result)

    # Exception order preserves the existing PR/CI acquisition failure categories.
    # Package and upstream clients expose their bounded outcomes as result values.
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

    # Presentation begins only after the acquisition/interpretation block completes.
    # These lines report evidence; they do not create a recommendation.
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

        assert package_result is not None
        _print_package_and_upstream(package_result, upstream_result)
    else:
        # Unsupported dependency extraction is a completed analysis result, so the
        # command returns zero after making every skipped dependent stage explicit.
        print("Dependency change: unsupported")
        print(f"Reason: {dependency_result.reason}")
        print(f"Detail: {dependency_result.detail}")
        print("Exact-head workflow evidence: not acquired")
        print("CI authority: not evaluated")
        print("Package evidence: not evaluated")
        print("Upstream source: not evaluated")

    return 0


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

    # A successful package result always triggers the resolver in ``main``. The
    # assertion documents that orchestration invariant without inventing fallback data.
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
