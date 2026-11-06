"""Fresh installed historical review: decode, open and inspect; never reproduce."""
import argparse
import ast
from contextlib import redirect_stdout
from hashlib import sha256
import importlib.util
from io import StringIO
import json
import os
from pathlib import Path
import socket
import sys
from unittest.mock import patch

from upgradepilot.cli import main as product_cli
from upgradepilot.caller_signature_delivery import open_caller_signature_checkpoint
from upgradepilot.caller_signature.worker import run_source_analysis
from upgradepilot.caller_signature.analysis import compare_arguments
from upgradepilot.caller_signature.correspondence import discover_source_candidates
from upgradepilot.maintainer_action import synthesize_maintainer_action
from upgradepilot.report_file import encode_report
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.checkpoint_revision import CheckpointStorageError

BLOCKED = {"acquire_dependency_inputs", "collect_source_progress", "run_source_analysis",
    "produce_source_analysis", "discover_source_candidates", "compare_arguments",
    "extract_python_source", "analyze_python_bindings", "synthesize_maintainer_action",
    "project_caller_signature_report", "project_investigation_report"}


def guard(frame, event, arg):
    if event == "call":
        module, name = frame.f_globals.get("__name__") or "", frame.f_code.co_name
        if ((module.startswith("upgradepilot.") and name in BLOCKED)
                or (module == "ast" and name == "parse") or (module == "os" and name == "getenv")):
            raise AssertionError("forbidden cold operation " + module + "." + name)


def invoke(argv, output, name):
    text = StringIO()
    with redirect_stdout(text):
        code = product_cli(argv)
    raw = text.getvalue().encode()
    (output / (name + ".txt")).write_bytes(raw)
    return code, raw


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--store", type=Path, required=True)
    parser.add_argument("--revision", required=True)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--installed", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--reference-store", type=Path, help="Offline qualification comparator only; never a live evidence substitute.")
    parser.add_argument("--reference-revision")
    args = parser.parse_args()
    os.umask(0o077)
    args.output.mkdir(mode=0o700, exist_ok=False)
    assert importlib.util.find_spec("experiments") is None
    for forbidden in (lambda: ast.parse("pass"), lambda: os.getenv("GITHUB_TOKEN"),
                      lambda: run_source_analysis(None), lambda: discover_source_candidates(None, None, None),
                      lambda: compare_arguments(None, None, None), lambda: synthesize_maintainer_action(None)):
        sys.setprofile(guard)
        try:
            forbidden()
        except AssertionError as error:
            assert str(error).startswith("forbidden cold operation ")
        else:
            raise AssertionError("inactive cold guard")
    sys.setprofile(guard)
    with patch.object(socket.socket, "connect", side_effect=AssertionError("cold network forbidden")):
        opened = open_caller_signature_checkpoint(CheckpointStore.open(args.store, read_only=True), args.revision)
        assert opened.selected.revision.revision_id == args.revision
        prefix = ["--open-workspace", str(args.store), "--revision", args.revision]
        code, workspace_text = invoke(prefix, args.output, "workspace")
        assert code == 0
        source_sha = source_id = report_sha = None
        if opened.report is not None:
            assert args.report is not None, "Retained report needs exact external-file comparison."
            report_bytes = encode_report(opened.report)
            assert report_bytes == args.report.read_bytes()
            report_sha = sha256(report_bytes).hexdigest()
            assert opened.report.report_id.encode() in workspace_text
            code, _ = invoke(["--open-report", str(args.report)], args.output, "report")
            assert code == 0
            source = next(s for s in opened.report.sources if s.retention == "retained_text" and s.content is not None
                and any(f.name == "path" and f.value == "tests/test_routes.py" for f in s.identity))
            source_id = source.source_id
            for name, argv in (("workspace-source", prefix), ("report-source", ["--open-report", str(args.report)])):
                code, text = invoke([*argv, "--show-source", source_id], args.output, name)
                assert code == 0 and source.content.encode() in text
            source_sha = sha256(source.content.encode()).hexdigest()
        else:
            # Source-only recovery is valid, but cannot pass the positive report task.
            assert args.report is None
            assert b"retained report/action absent" in workspace_text
        if args.reference_store:
            reference = open_caller_signature_checkpoint(CheckpointStore.open(args.reference_store, read_only=True), args.reference_revision)
            assert opened.native.comparison.result == reference.native.comparison.result
            assert opened.native.sources.catalog == reference.native.sources.catalog
            assert opened.native.sources.modules == reference.native.sources.modules
            assert opened.native.sources.analysis_limits == reference.native.sources.analysis_limits
        origins = {n: str(Path(m.__file__).resolve()) for n, m in sys.modules.items()
                   if n.startswith("upgradepilot") and getattr(m, "__file__", None)}
        assert all(Path(p).is_relative_to(args.installed.resolve()) for p in origins.values())
        transport = opened.native.sources.acquisition.transport
        result = opened.native.comparison.result if opened.native.comparison else None
        summary = dict(outcome="passed", selected_revision=args.revision,
            report_present=opened.report is not None, exact_report_sha256=report_sha,
            target_source_id=source_id, target_source_sha256=source_sha,
            reference_native_equal=bool(args.reference_store), guards_discriminated=6,
            product_origins=origins, github=transport.github_requests, provider=transport.provider_requests,
            response_bytes=transport.decoded_body_bytes, acquisition_state=opened.native.sources.acquisition.state,
            witnesses=len(result.candidates) if result else None,
            roots=len({c.root_call_id for c in result.candidates}) if result else None,
            provider_calls=0, credential_value_read=False)
    sys.setprofile(None)
    (args.output / "results.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({k: v for k, v in summary.items() if k != "product_origins"}))


if __name__ == "__main__":
    try:
        main()
    except CheckpointStorageError as error:
        print(json.dumps(dict(outcome="rejected", reason=error.reason)))
        raise SystemExit(9)
    finally:
        # A refused open must disarm the hook too; interpreter shutdown clears
        # module dictionaries and is outside the historical-reading interval.
        sys.setprofile(None)
