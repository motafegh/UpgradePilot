"""Command-line orchestration for the public-PR vertical slice.

The CLI owns user input, execution order, exit-code mapping, and presentation.
It delegates GitHub evidence acquisition and dependency interpretation to their
own modules so those responsibilities can be tested independently.
"""

from __future__ import annotations

import argparse
import os
from collections.abc import Sequence

from .dependency_change import (
    PinnedDependencyChange,
    extract_pinned_dependency_change,
)
from .github_client import (
    GitHubAcquisitionError,
    GitHubReadClient,
    GitHubResponseError,
    UpgradePilotInputError,
)


def build_parser() -> argparse.ArgumentParser:
    """Build the supported command-line interface without executing it."""

    parser = argparse.ArgumentParser(
        prog="upgradepilot",
        description=(
            "Acquire exact identity and one supported pinned dependency change "
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

    ``argv`` may be supplied by tests or another Python caller. When it is
    ``None``, :mod:`argparse` reads the process command line.

    Returns:
        ``0`` for a completed supported or unsupported analysis, ``2`` for
        rejected input, ``3`` for acquisition failure, and ``4`` for a
        successful GitHub response that could not establish required evidence.
    """

    args = build_parser().parse_args(argv)
    client = GitHubReadClient(token=os.getenv("GITHUB_TOKEN"))

    # Evidence boundary: extraction must not run unless acquisition established
    # structurally valid and mutually consistent PR and changed-file records.
    try:
        pull_request = client.get_pull_request(args.repository, args.pull_number)
        changed_files = client.get_changed_files(pull_request)
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

    # Interpretation boundary: unsupported syntax is a normal bounded result,
    # not a network or response-validation exception.
    dependency_result = extract_pinned_dependency_change(changed_files)

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
    else:
        print("Dependency change: unsupported")
        print(f"Reason: {dependency_result.reason}")
        print(f"Detail: {dependency_result.detail}")

    return 0
