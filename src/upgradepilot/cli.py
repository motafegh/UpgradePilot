"""Command-line interface for the current read-only UpgradePilot investigation.

The CLI owns arguments, environment input, report integration, and shell exit policy. Application
sequencing lives in ``investigation.py`` so future interfaces can reuse the same typed
investigation without duplicating provider/domain orchestration.
"""

from __future__ import annotations

import argparse
import os
import shlex
from collections.abc import Sequence
from pathlib import Path

from .caller_signature.acquisition import AcquisitionPolicy, AcquisitionSession
from .caller_signature_delivery import (
    investigate_and_deliver_caller_signature, open_caller_signature_checkpoint,
    retained_report_presence,
)
from .github.api import GitHubAcquisitionError, GitHubResponseError
from .github.identity import UpgradePilotInputError, validate_commit_sha
from .investigation import investigate_public_pull_request
from .report import (
    ReportFact, ReportSource, ReportSourceUnavailable, render_investigation_report,
    render_original_source, render_report_facts, render_report_source,
)
from .report_file import (
    ReportSaveError,
    ReportValidationError,
    read_report,
    save_report,
)
from .report_projection import project_investigation_report
from .workspace.native_representation import NativeReconstructionError
from .workspace.checkpoint_revision import CheckpointRevision, CheckpointStorageError
from .workspace.checkpoint_store import CheckpointStore
from .workspace.lifecycle_host import InvestigationWorkspaceHost


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
    inspection = parser.add_mutually_exclusive_group()
    inspection.add_argument(
        "--show-source", metavar="SOURCE_ID",
        help="Inspect one retained original text source in an offline report or Workspace.",
    )
    inspection.add_argument(
        "--show-facts", metavar="SOURCE_ID",
        help="Inspect saved artifact capability or package metadata facts with --open-report.",
    )
    parser.add_argument("--evidence-profile", choices=("caller-signature",),
                        help="Select bounded static caller/signature evidence explicitly.")
    parser.add_argument("--expected-base", type=validate_commit_sha, metavar="COMMIT_SHA",
                        help="Require this immutable PR base (live caller-signature profile only).")
    parser.add_argument("--expected-head", type=validate_commit_sha, metavar="COMMIT_SHA",
                        help="Require this immutable PR head (live caller-signature profile only).")
    parser.add_argument("--source-github-requests", type=int, metavar="COUNT",
                        help="Set the bounded GitHub request allowance for a live caller-signature run.")
    parser.add_argument("--workspace-store", metavar="PATH",
                        help="Explicit private store outside Git checkouts for caller/signature progress.")
    parser.add_argument("--open-workspace", metavar="PATH",
                        help="Open one exact retained Workspace revision offline.")
    parser.add_argument("--revision", metavar="REVISION_ID", help="Exact revision for --open-workspace.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if (args.expected_base is not None or args.expected_head is not None) and (
        args.evidence_profile != "caller-signature"
        or args.open_report is not None
        or args.open_workspace is not None
    ):
        parser.error("--expected-base/--expected-head require a live caller-signature investigation")
    if args.source_github_requests is not None and (
        args.evidence_profile != "caller-signature" or args.open_report is not None or args.open_workspace is not None
    ):
        parser.error("--source-github-requests requires a live caller-signature investigation")
    if args.show_source is not None and args.open_report is None and args.open_workspace is None:
        parser.error("--show-source requires --open-report or --open-workspace")
    if args.show_facts is not None and args.open_report is None:
        parser.error("--show-facts requires --open-report")
    if args.revision is not None and args.open_workspace is None:
        parser.error("--revision requires --open-workspace")
    if args.open_workspace is not None:
        if not args.revision or any(value is not None for value in (
            args.repository, args.pull_number, args.github_auth, args.save_report,
            args.open_report, args.evidence_profile, args.workspace_store,
        )):
            parser.error("--open-workspace requires --revision and cannot combine with live or report arguments")
        return _open_workspace(args.open_workspace, args.revision, args.show_source)
    if args.open_report is not None:
        if (
            args.repository is not None
            or args.pull_number is not None
            or args.save_report is not None
            or args.github_auth is not None
            or args.evidence_profile is not None
            or args.workspace_store is not None
        ):
            parser.error(
                "--open-report cannot be combined with investigation, save or authentication arguments"
            )
        try:
            report = read_report(args.open_report)
        except ReportValidationError as exc:
            print(f"Saved report rejected: {exc}")
            return 6
        try:
            if args.show_facts is not None:
                display = render_report_facts(report, args.show_facts)
            elif args.show_source is not None:
                display = render_report_source(report, args.show_source)
            else:
                display = render_investigation_report(report, saved=True)
        except ReportSourceUnavailable as exc:
            print(f"Source unavailable: {exc}")
            return 7
        print(display)
        return 0
    if args.repository is None or args.pull_number is None:
        parser.error("repository and pull_number are required for an investigation")
    if args.workspace_store is not None and args.evidence_profile != "caller-signature":
        parser.error("--workspace-store requires --evidence-profile caller-signature")
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
    if args.evidence_profile == "caller-signature":
        return _run_caller_signature(args, token)
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


def _safe_print(value: str) -> None:
    print("".join(c for c in value if c in "\n\t" or c.isprintable()))


def _print_workspace_handoff(
    revision: CheckpointRevision | None, *, store_path: Path | None,
    attempted: CheckpointRevision | None = None, attempt_status: str = "not_attempted",
    last_acknowledged: CheckpointRevision | None = None,
) -> None:
    if attempted is not None:
        _safe_print(f"Publication attempt: {attempted.revision_id}; exact inspection: {attempt_status}")
        _safe_print(f"Last acknowledged revision: {last_acknowledged.revision_id if last_acknowledged else 'none'}")
    if revision is None:
        print("Workspace: no confirmed revision.")
        return
    families = {r.family for r in revision.boundary.records if r.outcome == "recorded"}
    _safe_print(f"Workspace lineage: {revision.lineage_id}\nConfirmed revision: {revision.revision_id}")
    print(f"Retained sources: {'caller_signature_sources' in families}; comparison: {'caller_signature_comparison' in families}; report: {retained_report_presence(revision)}")
    if store_path is None:
        print("Workspace durability: volatile-only.")
    else:
        _safe_print(f"Workspace store: {store_path}")
        command = shlex.join(("upgradepilot", "--open-workspace", str(store_path), "--revision", revision.revision_id))
        _safe_print(f"Open confirmed revision: {command}")


def _run_caller_signature(args: argparse.Namespace, token: str | None) -> int:
    try:
        policy = (AcquisitionPolicy() if args.source_github_requests is None
                  else AcquisitionPolicy(github_requests=args.source_github_requests))
    except ValueError as error:
        print(f"Input rejected: {error}")
        return 2
    store_path = Path(args.workspace_store).absolute() if args.workspace_store else None
    try:
        store = (CheckpointStore.open(store_path) if store_path.exists()
                 else CheckpointStore.create(store_path, schema_version=2)) if store_path else None
    except CheckpointStorageError as error:
        print(f"Workspace publication unavailable: {error.reason}")
        print("Workspace: no confirmed revision.")
        return 11
    host = InvestigationWorkspaceHost(store=store)
    with AcquisitionSession(token=token, policy=policy) as session:
        outcome = investigate_and_deliver_caller_signature(
            args.repository, args.pull_number, session=session, host=host,
            expected_base=args.expected_base, expected_head=args.expected_head,
        )
    codes = {"input": 2, "acquisition": 3, "response": 4, "analysis": 10, "report": 8, "publication": 11}
    priority = {"input": 1, "acquisition": 1, "response": 1, "analysis": 1, "report": 2, "publication": 0}
    problems = sorted(outcome.problems, key=lambda p: priority[p.stage])
    exit_code = codes[problems[0].stage] if problems else 0
    for problem in problems:
        _safe_print(f"Operation problem: {problem.stage}; {problem.reason}; {problem.detail}")
    if outcome.report is not None:
        try:
            print(render_investigation_report(outcome.report))
        except Exception as error:
            print(f"Report rendering failed: {type(error).__name__}")
            exit_code = exit_code or 8
        if args.save_report is not None:
            try:
                save_report(outcome.report, args.save_report)
            except ReportSaveError:
                print("External report file save failed.")
                exit_code = exit_code or 5
            else:
                _safe_print(f"Saved report: {args.save_report}")
    _print_workspace_handoff(outcome.recoverable_revision, store_path=store_path,
                             attempted=outcome.attempted_revision, attempt_status=outcome.attempt_status,
                             last_acknowledged=outcome.last_acknowledged_revision)
    return exit_code


def _open_workspace(path: str, revision_id: str, source_id: str | None) -> int:
    try:
        store = CheckpointStore.open(Path(path), read_only=True)
        opened = open_caller_signature_checkpoint(store, revision_id)
    except (CheckpointStorageError, NativeReconstructionError, ReportValidationError) as error:
        print(f"Workspace revision rejected: {getattr(error, 'reason', type(error).__name__)}")
        return 9
    revision = opened.selected.revision
    if opened.report is not None:
        try:
            display = render_report_source(opened.report, source_id) if source_id else render_investigation_report(opened.report, saved=True)
        except ReportSourceUnavailable as error:
            print(f"Source unavailable: {error}")
            return 7
        print(display)
    else:
        native = opened.native
        catalog = native.sources.catalog if native.sources else None
        if source_id:
            file = next((f for f in catalog.files if catalog.descriptor(f)["file_id"] == source_id), None) if catalog else None
            if file is None:
                print("Source unavailable: unknown retained file identity.")
                return 7
            descriptor = catalog.descriptor(file)
            scope = next(s for s in catalog.scopes if s.source_id == file.source_id)
            source = ReportSource(source_id, "target_source" if scope.repository == revision.boundary.target.repository else "dependency_source", None,
                                  tuple(ReportFact(k, k.replace("_", " ").capitalize(), str(descriptor[k]))
                                        for k in ("repository", "revision", "path", "content_sha256")),
                                  scope.capture_basis, None, "retained_text", file.content, scope.coverage_limit)
            print(render_original_source(source, context=(f"Workspace revision: {revision.revision_id}",)))
        else:
            print("Selected source checkpoint; retained report/action absent.")
            target = revision.boundary.target
            _safe_print(f"Repository: {target.repository}\nPR: {target.pull_number}\nBase: {target.base_sha}\nHead: {target.head_sha}")
            _safe_print(f"Dependency: {target.normalized_package} {target.old_version} -> {target.proposed_version}")
            print(f"Acquisition: {native.sources.acquisition.state if native.sources else 'not evaluated'}")
            print(f"Analysis: {native.comparison.state if native.comparison else 'not evaluated'}")
            if catalog:
                for file in catalog.files:
                    _safe_print(f"Retained file: {catalog.descriptor(file)['file_id']} {file.path}")
    print(f"Later revisions excluded: {len(opened.selected.excluded_successor_ids)}")
    _print_workspace_handoff(revision, store_path=Path(path).absolute())
    return 0
