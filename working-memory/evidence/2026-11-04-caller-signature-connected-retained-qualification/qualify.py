"""Dated qualification of retained inputs and controlled normal HTTP composition.

Run with PYTHONPATH=src:tests:. and a NEW private output directory. Each case
records its actual outcome, including failed report/publication, before the next
case starts. Historical files are read/hash-checked only. No live provider,
credential, model, target-code execution or whole-attempt retry is selected.
"""
from contextlib import ExitStack, redirect_stdout
from dataclasses import asdict
from hashlib import sha256
from io import StringIO
import argparse
import ast
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from unittest.mock import patch

from controlled_http import RetainedHTTP
from retained_cases import ROLE, selected_cases
from semantic_equivalence import native_pairing, compare as compare_semantics
from upgradepilot.caller_signature.acquisition import AcquisitionPolicy, AcquisitionSession
from upgradepilot.caller_signature.result_codec import candidate_records
from upgradepilot.cli import main as product_cli
from upgradepilot.report_file import read_report
from upgradepilot.caller_signature_delivery import open_caller_signature_checkpoint
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_boundary import encode_native_boundary

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def canonical(value):
    return json.dumps(value, sort_keys=True)


def check_equivalence(case, run):
    result = run.result
    assert run.state == "completed" and result is not None, (run.state, run.reason)
    saved = {u["descriptor"]["file_id"]: u for u in case.body["files"]}
    assert len(saved) == len(result.units)
    for unit in result.units:
        old = saved[unit.unit_id]
        assert canonical(asdict(unit.facts) if unit.facts else None) == canonical(old["facts"]), unit.unit_id
        expected = "non_python" if not old["descriptor"]["path"].endswith(".py") else old["coverage"]
        assert unit.coverage == expected
    files = {case.catalog.descriptor(f)["file_id"]: f for f in case.catalog.files}
    calls = {c.fact_id: c for u in result.units if u.facts for c in u.facts.calls}
    signatures = {s.fact_id: s for u in result.units if u.facts for s in u.facts.signatures}
    projected = [candidate_records(c, calls, signatures, files) for c in result.candidates]
    expected = [(dict(c, callee_role=dict(c["callee_role"], role=ROLE[c["callee_role"]["role"]])), p)
                for c, p in zip(case.body["discovery"]["candidates"], case.body["pairs"])]
    assert canonical(projected) == canonical(expected), "witness/path/premise/outcome mismatch"
    assert canonical([asdict(g) for g in result.gaps]) == canonical(case.body["discovery"]["gaps"])
    assert canonical([asdict(a) for a in result.admission]) == canonical(case.body["analysis_admission"]["units"])
    return dict(facts=result.work.facts, witnesses=len(result.candidates),
                roots=len({c.root_call_id for c in result.candidates}),
                unexamined=sum(u.coverage == "unexamined" for u in result.units),
                facts_paths_premises_outcomes_admission_equal=True)


def cold_reader():
    """Reuse the actual CLI cold-open control, without importing test modules."""
    source = (ROOT / "tests/test_caller_signature_delivery.py").read_text()
    node = next(n for n in ast.parse(source).body if isinstance(n, ast.Assign)
                and any(isinstance(t, ast.Name) and t.id == "_COLD_OPEN" for t in n.targets))
    return ast.literal_eval(node.value)


def execute(case, mode, destination, reference=None, *, controlled=False):
    case.verify_originals()
    row = dict(case=case.name, mode=mode, historical_hashes=case.hashes,
               proof_class="retained_input_application_delivery" if mode == "retained" else "controlled_actual_client_catalog_only_http_composition")
    if not controlled and case.native_sources() is None:
        return dict(row, outcome="not_admitted", reason="selected_catalog_missing_historical_acquisition_and_native_prefix",
                    no_receipt_backfill=True)
    destination.mkdir(mode=0o700)
    store_path, report_path = destination / "store", destination / "report.json"
    transport = RetainedHTTP(case)
    session = AcquisitionSession(policy=AcquisitionPolicy())
    session.mount("https://", transport)
    identity = case.input_observation().identity
    output = StringIO()
    started = time.monotonic()
    try:
        with ExitStack() as stack:
            stack.enter_context(patch("upgradepilot.cli.AcquisitionSession", return_value=session))
            stack.enter_context(patch("socket.socket.connect", side_effect=AssertionError("live provider forbidden")))
            if mode == "retained":
                # Deliberate controlled seam: exact historical input is returned as
                # retained_experiment, while the normal application/worker/consumers run.
                sources = case.native_sources()
                def retained_source(_inputs, _session, publish):
                    publish(sources)
                    return sources
                stack.enter_context(patch("upgradepilot.investigation.collect_source_progress", side_effect=retained_source))
                row["controlled_seam"] = "collect_source_progress; original retained receipts/gaps, no new acquisition claim"
            with redirect_stdout(output):
                code = product_cli([identity.repository, str(identity.number), "--evidence-profile", "caller-signature",
                    "--workspace-store", str(store_path), "--save-report", str(report_path)])
        row.update(exit=code, elapsed_hex=(time.monotonic()-started).hex(),
                   actual_controlled_requests=len(transport.dispatched),
                   actual_controlled_github_requests=sum(urlsplit_host(r["url"]) == "api.github.com" for r in transport.dispatched))
        (destination / "cli.txt").write_text(output.getvalue())
        (destination / "requests.json").write_text(json.dumps(transport.dispatched, indent=2)+"\n")
        selected = next((line.removeprefix("Confirmed revision: ") for line in output.getvalue().splitlines() if line.startswith("Confirmed revision: ")), None)
        row["confirmed_revision"] = selected
        if selected:
            store = CheckpointStore.open(store_path, read_only=True)
            opened = open_caller_signature_checkpoint(store, selected)
            row.update(source_files=len(opened.native.sources.catalog.files) if opened.native.sources and opened.native.sources.catalog else 0,
                       acquisition_state=opened.native.sources.acquisition.state if opened.native.sources else None,
                       analysis_state=opened.native.comparison.state if opened.native.comparison else None,
                       report_retained=opened.report is not None,
                       boundary_bytes=len(encode_native_boundary(opened.selected.revision.boundary)))
            if opened.native.comparison and opened.native.comparison.result:
                result = opened.native.comparison.result
                row.update(facts=result.work.facts, witnesses=len(result.candidates),
                    roots=len({c.root_call_id for c in result.candidates}),
                    unexamined=sum(u.coverage == "unexamined" for u in result.units),
                    outcomes=sorted({c.comparison.outcome for c in result.candidates}))
                row.update(native_pairing(opened.native.comparison))
                if mode == "retained":
                    row["equivalence"] = check_equivalence(case, opened.native.comparison)
                elif reference is not None:
                    references = json.loads((reference/"results.json").read_bytes())
                    ref = next(r for r in references if r["case"] == case.name and r["mode"] == "retained")
                    ref_store = CheckpointStore.open(reference/("retained-"+case.name)/"store", read_only=True)
                    baseline = open_caller_signature_checkpoint(ref_store, ref["confirmed_revision"])
                    row["semantic_equivalence"] = compare_semantics(baseline.native, opened.native)
            child = subprocess.run([sys.executable, "-c", cold_reader(), "--open-workspace", str(store_path), "--revision", selected],
                cwd=destination, env=dict(os.environ, PYTHONPATH=os.pathsep.join(str(Path(p).absolute()) for p in sys.path if p)),
                capture_output=True, text=True, timeout=60)
            (destination/"cold.txt").write_text(child.stdout+child.stderr)
            row["cold_exit"] = child.returncode
            assert child.returncode == 0, "cold opening failed"
            if opened.report:
                report = read_report(report_path)
                assert report == opened.report
                row.update(report_bytes=report_path.stat().st_size, report_sha256=sha256(report_path.read_bytes()).hexdigest(),
                           report_original_source_bytes=sum(len(s.content.encode()) for s in report.sources if s.retention=="retained_text"))
        row["delivery_outcome"] = "completed" if code == 0 and row.get("report_retained") else "incomplete_or_failed"
        row["positive_pair_qualification"] = row["delivery_outcome"] == "completed" and row.get("paired_roots", 0) > 0
        semantic = row.get("semantic_equivalence", {})
        row["outcome"] = ("qualified_controlled_delivery" if row["positive_pair_qualification"]
                          and all(v for k,v in semantic.items() if not k.startswith("ordered_"))
                          else "insufficient_or_discrepant")
    except Exception as error:
        row.update(outcome="failed", error=type(error).__name__, detail=str(error)[:1600], elapsed_hex=(time.monotonic()-started).hex())
        (destination/"cli.txt").write_text(output.getvalue())
    finally:
        case.verify_originals()
    return row


def urlsplit_host(url):
    from urllib.parse import urlsplit
    return urlsplit(url).hostname


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--mode", choices=("retained", "http", "both"), default="both")
    parser.add_argument("--case", action="append")
    parser.add_argument("--reference", type=Path)
    args = parser.parse_args()
    args.output.mkdir(mode=0o700, parents=True, exist_ok=False)
    cases = selected_cases(ROOT)
    cases = [c for c in cases if not args.case or c.name in args.case]
    methods = {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest()
               for p in [*sorted((ROOT/"src/upgradepilot").rglob("*.py")), *sorted(HERE.glob("*.py"))]}
    manifest = dict(proof="offline_only_not_fresh_or_untouched", cases=[dict(name=c.name,hashes=c.hashes) for c in cases],
                    method_sha256=methods, modes=args.mode, policy=asdict(AcquisitionPolicy()),
                    private_output=str(args.output), reference=str(args.reference) if args.reference else None,
                    provider_premises="Authored catalog-only inventories and provider wrappers. Original source bytes/PR snapshots retained separately.")
    (args.output/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    results=[]
    for case in cases:
        for mode in (("retained", "http") if args.mode=="both" else (args.mode,)):
            row = execute(case, mode, args.output/(mode+"-"+case.name), args.reference)
            results.append(row)
            (args.output/"results.json").write_text(json.dumps(results,indent=2)+"\n")
            print(json.dumps(row),flush=True)
    assert methods == {name:sha256((ROOT/name).read_bytes()).hexdigest() for name in methods}, "method changed during qualification"


if __name__ == "__main__":
    main()
