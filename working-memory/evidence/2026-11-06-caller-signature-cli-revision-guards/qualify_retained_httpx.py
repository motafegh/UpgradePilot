"""Controlled normal CLI qualification over the frozen ordinary HTTPX source case.

The unchanged November4 fixture adapter supplies authored provider wrappers over
retained real text. This is neither live acquisition nor authentic HTTP replay.
All product owners, including the new guard forwarding and worker, run normally.
"""
import argparse
from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
import json
import os
from pathlib import Path
import sys
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
FIXTURE = ROOT / "working-memory/evidence/2026-11-04-caller-signature-connected-retained-qualification"
sys.path.insert(0, str(FIXTURE))
from controlled_http import RetainedHTTP
from retained_cases import RetainedCase, ordinary
from upgradepilot.caller_signature.acquisition import AcquisitionPolicy, AcquisitionSession
from upgradepilot.caller_signature_delivery import open_caller_signature_checkpoint
from upgradepilot.cli import main as product_cli
from upgradepilot.workspace.checkpoint_store import CheckpointStore


def write(path, value):
    path.write_text(json.dumps(value, indent=2)+"\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    os.umask(0o077)
    args.output.mkdir(mode=0o700, exist_ok=False)
    rows = json.loads((ROOT / "working-memory/evidence/2026-11-01-analysis-capacity-and-work-admission/retained-qualification-results.json").read_bytes())
    row = next(r for r in rows if r["case"] == "httpx")
    directory = Path(row["directory"])
    body, catalog = ordinary.open_ordinary_comparison(directory)
    case = RetainedCase("httpx", directory, row["output_sha256"], body, catalog)
    case.verify_originals()
    identity = case.input_observation().identity
    source_hashes = {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest()
                     for p in sorted((ROOT / "src/upgradepilot").rglob("*.py"))}
    reference = Path("/home/motafeq/.local/share/upgradepilot/connected-retained-qualification-2026-11-04/attempt-02/http-httpx/store")
    write(args.output / "contract.json", dict(proof_class="controlled_actual_client_catalog_only_http_composition",
        input_sha256=case.hashes, product_sha256=source_hashes,
        method_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        fixture_sha256={p.name: sha256(p.read_bytes()).hexdigest()
                        for p in (FIXTURE / "controlled_http.py", FIXTURE / "retained_cases.py")},
        expected_base=identity.base_sha, expected_head=identity.head_sha,
        expected_reference_revision="a3e8b46cf968450a95037765e22212bd",
        expected_costs=dict(physical=55, github=45), no_live_provider=True))
    transport = RetainedHTTP(case)
    session = AcquisitionSession(policy=AcquisitionPolicy())
    session.mount("https://", transport)
    output = StringIO()
    with patch("upgradepilot.cli.AcquisitionSession", return_value=session), redirect_stdout(output):
        code = product_cli([identity.repository, str(identity.number), "--evidence-profile", "caller-signature",
            "--expected-base", identity.base_sha, "--expected-head", identity.head_sha,
            "--workspace-store", str(args.output / "store"), "--save-report", str(args.output / "report.json")])
    (args.output / "cli.txt").write_text(output.getvalue())
    write(args.output / "outcome.json", dict(exit=code, physical=session.provider_requests,
        github=session.github_requests, response_bytes=session.body_bytes))
    assert code == 0, output.getvalue()
    selected = next(line.removeprefix("Confirmed revision: ") for line in output.getvalue().splitlines()
                    if line.startswith("Confirmed revision: "))
    actual = open_caller_signature_checkpoint(CheckpointStore.open(args.output / "store", read_only=True), selected)
    earlier = open_caller_signature_checkpoint(CheckpointStore.open(reference, read_only=True), "a3e8b46cf968450a95037765e22212bd")
    assert actual.native.comparison.result == earlier.native.comparison.result
    assert actual.native.sources.catalog == earlier.native.sources.catalog
    assert actual.native.sources.modules == earlier.native.sources.modules
    assert actual.native.sources.analysis_limits == earlier.native.sources.analysis_limits
    assert actual.report is not None and actual.report.action.state == "abstain"
    assert session.provider_requests == 55 and session.github_requests == 45
    case.verify_originals()
    assert all(sha256((ROOT/p).read_bytes()).hexdigest() == h for p,h in source_hashes.items())
    result = actual.native.comparison.result
    summary = dict(proof_class="controlled_actual_client_catalog_only_http_composition", outcome="passed",
        exit=code, github=session.github_requests, provider=session.provider_requests, response_bytes=session.body_bytes,
        retained_files=len(actual.native.sources.catalog.files), witnesses=len(result.candidates),
        roots=len({c.root_call_id for c in result.candidates}), selected_revision=selected,
        exact_native_result_equal=True, source_catalog_modules_limits_equal=True,
        report_retained=True, fresh_live=False, untouched_transfer=False)
    write(args.output / "results.json", summary)
    print(json.dumps(summary))


if __name__ == "__main__":
    with patch("socket.socket.connect", side_effect=AssertionError("offline controlled qualification")):
        main()
