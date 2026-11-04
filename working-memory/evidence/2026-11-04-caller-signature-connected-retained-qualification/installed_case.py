"""Standalone installed-product composition over a prepared retained-byte fixture.

The preparation step serializes only provider inputs/catalog, without analysis
outputs or expected witnesses. This driver imports product and HTTP control only;
no experiment checkout is available in its working directory or import path.
"""
from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
import json
import os
from pathlib import Path
import subprocess
import sys
from types import SimpleNamespace
from unittest.mock import patch

from controlled_http import RetainedHTTP
from upgradepilot.caller_signature.acquisition import AcquisitionPolicy, AcquisitionSession
from upgradepilot.caller_signature_delivery import open_caller_signature_checkpoint
from upgradepilot.cli import main
from upgradepilot.report_file import read_report
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
from upgradepilot.workspace.source_access import read_source_catalog


def run():
    root = Path.cwd()
    fixture = json.loads((root / "fixture.json").read_bytes())
    target = ExactInvestigationTarget(**fixture["catalog"]["target"])
    case = SimpleNamespace(body=fixture["body"], catalog=read_source_catalog(
        json.dumps(fixture["catalog"]).encode(), expected_target=target))
    transport = RetainedHTTP(case)
    session = AcquisitionSession(policy=AcquisitionPolicy())
    session.mount("https://", transport)
    identity = case.body["acquisition"]["native_inputs"]["identity"]
    output = StringIO()
    with patch("upgradepilot.cli.AcquisitionSession", return_value=session), patch("socket.socket.connect", side_effect=AssertionError("live forbidden")), redirect_stdout(output):
        code = main([identity["repository"], str(identity["number"]), "--evidence-profile", "caller-signature",
                     "--workspace-store", str(root / "store"), "--save-report", str(root / "report.json")])
    (root / "cli.txt").write_text(output.getvalue())
    assert code == 0, output.getvalue()
    selected = next(line.removeprefix("Confirmed revision: ") for line in output.getvalue().splitlines() if line.startswith("Confirmed revision: "))
    opened = open_caller_signature_checkpoint(CheckpointStore.open(root / "store", read_only=True), selected)
    report = read_report(root / "report.json")
    assert report == opened.report
    native = [c for c in opened.native.comparison.result.candidates if c.callee_role.role in {"old_dependency", "proposed_dependency"}]
    roots = {}
    for candidate in native:
        roots.setdefault(candidate.root_call_id, set()).add(candidate.callee_role.role)
    assert sum(r == {"old_dependency", "proposed_dependency"} for r in roots.values()) == 1
    assert len(native) == 4 and len(opened.native.sources.catalog.files) == 24
    origin = Path(opened.native.comparison.worker_module_origin)
    assert origin.is_relative_to(root.parent / "installed"), origin
    child = subprocess.run([sys.executable, str(root / "cold_reader.py"), "--open-workspace", str(root / "store"), "--revision", selected],
        cwd=root, env=os.environ.copy(), capture_output=True, timeout=60)
    (root / "cold.txt").write_bytes(child.stdout + child.stderr)
    assert child.returncode == 0
    result = dict(proof="installed_controlled_retained_byte_composition_not_fresh_or_untouched",
        exit=code, cold_exit=child.returncode, selected_revision=selected,
        files=24, native_witnesses=len(native), paired_roots=1, report_bytes=(root / "report.json").stat().st_size,
        report_sha256=sha256((root / "report.json").read_bytes()).hexdigest(), requests=len(transport.dispatched),
        adapter_candidates=AcquisitionPolicy().adapter_candidate_attempts, worker_origin=str(origin),
        fixture_sha256=sha256((root / "fixture.json").read_bytes()).hexdigest())
    (root / "results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result))


if __name__ == "__main__":
    run()
