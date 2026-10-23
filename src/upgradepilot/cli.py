"""Command-line interface for the current read-only UpgradePilot investigation.

The CLI owns arguments, environment input, report integration, and shell exit policy. Application
sequencing lives in ``investigation.py`` so future interfaces can reuse the same typed
investigation without duplicating provider/domain orchestration.
"""

from __future__ import annotations

import argparse
import os
from collections.abc import Sequence

from .github.api import GitHubAcquisitionError, GitHubResponseError
from .github.identity import UpgradePilotInputError
from .investigation import investigate_public_pull_request
from .report import ReportSourceUnavailable, render_investigation_report, render_report_source
from .report_file import (
    ReportSaveError,
    ReportValidationError,
    read_report,
    save_report,
)
from .report_projection import project_investigation_report
from .workspace.native_representation import NativeReconstructionError


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="upgradepilot",
        description=(
            "Acquire exact dependency, CI, package/upstream, artifact-serviceability, "
            "bounded semantic, and conditionally activated target evidence for a public "
            "GitHub pull request."
        ),
    )
    parser.add_argument(
        "repository", nargs="?", help="Public repository in owner/repository form."
    )
    parser.add_argument(
        "pull_number", nargs="?", type=int, help="GitHub pull-request number."
    )
    parser.add_argument(
        "--github-auth",
        choices=("anonymous", "token-env"),
        default=None,
        help=(
            "GitHub authentication mode (default: anonymous). "
            "Use token-env to explicitly read GITHUB_TOKEN from the environment."
        ),
    )
    parser.add_argument(
        "--save-report",
        metavar="PATH",
        help="Also save the complete report without replacing an existing file.",
    )
    parser.add_argument(
        "--open-report",
        metavar="PATH",
        help="Open a saved report offline without gathering new evidence.",
    )
    parser.add_argument(
        "--show-source", metavar="SOURCE_ID",
        help="Inspect one retained original text source; requires --open-report.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.show_source is not None and args.open_report is None:
        parser.error("--show-source requires --open-report")
    if args.open_report is not None:
        if (
            args.repository is not None
            or args.pull_number is not None
            or args.save_report is not None
            or args.github_auth is not None
        ):
            parser.error(
                "--open-report cannot be combined with investigation, save or authentication arguments"
            )
        try:
            report = read_report(args.open_report)
        except ReportValidationError as exc:
            print(f"Saved report rejected: {exc}")
            return 6
        if args.show_source is not None:
            try:
                display = render_report_source(report, args.show_source)
            except ReportSourceUnavailable as exc:
                print(f"Source unavailable: {exc}")
                return 7
        else:
            display = render_investigation_report(report, saved=True)
        print(display)
        return 0
    if args.repository is None or args.pull_number is None:
        parser.error("repository and pull_number are required for an investigation")
    auth_mode = args.github_auth or "anonymous"
    # Public investigations must not silently adopt an unrelated shell credential.
    token = None
    if auth_mode == "token-env":
        token = os.getenv("GITHUB_TOKEN")
        if not token:
            print(
                "Input rejected: --github-auth token-env requires GITHUB_TOKEN to be set."
            )
            return 2
    try:
        investigation = investigate_public_pull_request(
            args.repository,
            args.pull_number,
            token=token,
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

    try:
        report = project_investigation_report(investigation, auth_mode=auth_mode)
    except NativeReconstructionError as exc:
        print(f"Report projection rejected: {exc}")
        return 8
    print(render_investigation_report(report))
    if args.save_report is not None:
        try:
            save_report(report, args.save_report)
        except ReportSaveError as exc:
            print(f"Report save failed: {exc}")
            return 5
        print(f"Saved report: {args.save_report}")
    return 0


__all__ = ("build_parser", "main")
