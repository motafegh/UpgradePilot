"""Run native bounded workers on frozen ordinary inputs; publish only proof metadata.

PYTHONPATH=src:. .venv/bin/python <this file>
Retained source is parsed, never executed; acquisition/network are not invoked.
Original private files and indexed capture artifacts are hash-checked unchanged.
"""
from contextlib import ExitStack
from dataclasses import asdict
from hashlib import sha256
import json
from pathlib import Path
from unittest.mock import patch

from experiments import api_ordinary_call_signature_trial as ordinary
from upgradepilot.caller_signature.correspondence import PythonSourceModule
from upgradepilot.caller_signature.evidence import AnalysisLimits, SourceAnalysisInput, json_structure_cost
from upgradepilot.caller_signature.result_codec import (
    candidate_records, decode_analysis_result, encode_analysis_input, encode_analysis_result,
)
from upgradepilot.caller_signature.worker import run_source_analysis
from upgradepilot.workspace.native_representation import json_bytes, parse_json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EVIDENCE = ROOT / "working-memory/evidence"
ROLE = {"target": "target_repository", "native_old_version": "old_dependency",
        "native_proposed_version": "proposed_dependency", "constraint_sample": "constraint_sample"}
SOURCE_HASHES = {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest()
                 for p in sorted((ROOT / "src/upgradepilot/caller_signature").glob("*.py"))}


def read(path):
    return json.loads(path.read_bytes())


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


rows = read(EVIDENCE / "2026-11-01-analysis-capacity-and-work-admission/retained-qualification-results.json")
cases = [(r["case"], Path(r["directory"]), r["output_sha256"]) for r in rows]
digimon = EVIDENCE / "2026-11-01-untouched-partial-analysis-qualification/ordinary-digimon-scraper-pr-16"
private = Path(read(digimon / "contract.json")["private_retention"]["root"])
hashes = read(digimon / "verification.json")["artifact_hashes"]
cases.append(("digimon", private / "comparison",
              {n.removeprefix("comparison/"): h for n, h in hashes.items() if n.startswith("comparison/")}))
results = []
for case, directory, hashes in cases:
    assert hashes == {n: sha256((directory / n).read_bytes()).hexdigest() for n in hashes}
    body, catalog = ordinary.open_ordinary_comparison(directory)
    modules = tuple(PythonSourceModule(**dict(m, role=ROLE[m["role"]], dependencies=tuple(m["dependencies"]))) for m in body["modules"])
    source = SourceAnalysisInput(catalog, modules, AnalysisLimits(**body["limits"]))
    input_data = encode_analysis_input(source)
    run = run_source_analysis(source)
    summary = dict(case=case, state=run.state, reason=run.reason, returncode=run.worker_returncode,
                   elapsed_seconds_hex=run.elapsed.seconds_hex, worker_origin=run.worker_module_origin,
                   input_bytes=len(input_data), result_bytes=None, facts_equal=False, paths_equal=False,
                   admission_equal=False, work_equal=False, cold_open=False, original_hashes=hashes,
                   implementation_sha256=SOURCE_HASHES)
    results.append(summary)
    (HERE / "retained-results.json").write_text(json.dumps(results, indent=2) + "\n")
    assert run.state == "completed", (case, run.state, run.reason)
    result = run.result
    payload = encode_analysis_result(result, source)
    summary["result_bytes"] = len(payload)
    with ExitStack() as stack:
        for hook in ("ast.parse", "requests.sessions.Session.request", "socket.socket.connect",
                     "upgradepilot.caller_signature.worker.produce_source_analysis",
                     "upgradepilot.caller_signature.correspondence.discover_source_candidates",
                     "upgradepilot.caller_signature.analysis.compare_arguments"):
            stack.enter_context(patch(hook, side_effect=AssertionError("Forbidden cold hook: " + hook)))
        assert decode_analysis_result(payload, source) == result
    summary["cold_open"] = True
    saved = {u["descriptor"]["file_id"]: u for u in body["files"]}
    assert len(saved) == len(result.units)
    for unit in result.units:
        old = saved[unit.unit_id]
        assert canonical(asdict(unit.facts) if unit.facts else None) == canonical(old["facts"])
        expected = "non_python" if not old["descriptor"]["path"].endswith(".py") else old["coverage"]
        assert unit.coverage == expected
    summary["facts_equal"] = True
    files = {catalog.descriptor(f)["file_id"]: f for f in catalog.files}
    calls = {f.fact_id: f for u in result.units if u.facts for f in u.facts.calls}
    signatures = {f.fact_id: f for u in result.units if u.facts for f in u.facts.signatures}
    projected = [candidate_records(c, calls, signatures, files) for c in result.candidates]
    expected = [(dict(c, callee_role=dict(c["callee_role"], role=ROLE[c["callee_role"]["role"]])), p)
                for c, p in zip(body["discovery"]["candidates"], body["pairs"])]
    assert canonical(projected) == canonical(expected)
    assert canonical([asdict(g) for g in result.gaps]) == canonical(body["discovery"]["gaps"])
    summary["paths_equal"] = True
    assert canonical([asdict(a) for a in result.admission]) == canonical(body["analysis_admission"]["units"])
    summary["admission_equal"] = True
    work = asdict(result.work)
    expected_work = dict(body["work"], **{k: body["analysis_admission"][k] for k in ("scanned_ast_nodes", "fact_structure_cost", "comparison_structure_cost")},
                         **{k: body["discovery"][k] for k in ("states_examined", "gaps_omitted")})
    assert work == expected_work
    summary.update(work_equal=True, work=work, analyzed_units=sum(u.facts is not None for u in result.units),
        unexamined_units=sum(u.coverage == "unexamined" for u in result.units),
        result_sha256=sha256(payload).hexdigest(), input_sha256=run.input_sha256,
        structural_tokens=json_structure_cost(parse_json(payload)))
    assert hashes == {n: sha256((directory / n).read_bytes()).hexdigest() for n in hashes}
    assert SOURCE_HASHES == {name: sha256((ROOT / name).read_bytes()).hexdigest() for name in SOURCE_HASHES}
    (HERE / "retained-results.json").write_text(json.dumps(results, indent=2) + "\n")
    print(case, "PASS", work["facts"], work["selected_pairs"], "facts/comparisons", len(payload), "bytes", flush=True)
