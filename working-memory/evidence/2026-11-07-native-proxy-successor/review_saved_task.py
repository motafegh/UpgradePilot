"""Grade the successor report against its own retained evidence after the source baseline."""
import argparse
from dataclasses import asdict
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import re
import socket
import sys
from unittest.mock import patch

from upgradepilot.caller_signature_delivery import open_caller_signature_checkpoint
from upgradepilot.report_file import encode_report
from upgradepilot.workspace.checkpoint_store import CheckpointStore


def facts(items):
    return {item.name: item.value for item in items}


def write(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


def review(capture, task, output, baseline):
    opened = open_caller_signature_checkpoint(CheckpointStore.open(capture / "store", read_only=True), baseline["revision"])
    report = opened.report
    encoded = encode_report(report)
    assert encoded == (capture / "report.json").read_bytes()
    sources = {s.source_id:s for s in report.sources}
    files = {facts(s.identity)["file_id"]:s.source_id for s in report.sources if "file_id" in facts(s.identity)}
    target = next(s for s in report.sources if facts(s.identity).get("path") == "tests/test_routes.py")
    rows = [x for x in report.assessments if "witness_id" in facts(x.facts)]
    selected = [row for row in rows if facts(row.facts)["root_location"].startswith(target.source_id + " L7 ")]
    source_requests = dict.fromkeys([(target.source_id, 7)])
    for row in selected:
        for name, value in facts(row.facts).items():
            if name in {"root_location", "caller", "callee"} or name.startswith("path_"):
                match = re.match(r"^(\S+) L(\d+)(?=[: ])", value)
                assert match, name
                source_requests[(match[1], int(match[2]))] = None
    catalog = opened.native.sources.catalog
    operations = []
    assert len(source_requests) <= 96
    for index, (source_id, line) in enumerate(source_requests, 1):
        identity = facts(sources[source_id].identity)
        arguments = dict(source_id=identity["source_id"], path=identity["path"], start_line=line, line_count=100)
        response = catalog.query("read", arguments)
        assert response.outcome == "observed"
        payload = json.loads(response.content)["payload"]
        assert payload["file"]["file_id"] == identity["file_id"] and payload["start_line"] == line
        assert 0 < len(payload["lines"]) <= 100
        (output / f"source-{index:02d}.json").write_bytes(response.content)
        operations.append(dict(report_source_id=source_id, path=identity["path"], first=line,
            last=line + len(payload["lines"]) - 1, bytes=len(response.content), exact_file_match=True))
    write(output / "operations.json", operations)

    run = opened.native.comparison
    result = run.result
    candidates = {c.candidate_id:c for c in result.candidates}
    assert {facts(row.facts)["witness_id"] for row in rows} == set(candidates)
    for row in rows:
        fields = facts(row.facts)
        candidate = candidates[fields["witness_id"]]
        comparison = candidate.comparison
        assert row.state == comparison.outcome
        assert fields["role"] == candidate.callee_role.role and fields["version"] == candidate.callee_role.version
        assert row.limitations == candidate.premises + comparison.remaining_premises + comparison.unresolved_checks
        assert [fields[f"path_{i}"] for i in range(len(candidate.steps))] == [
            f"{files[s.unit_id]} L{s.span.line}:{s.span.column} {s.operation} {s.expression}" for s in candidate.steps]
        assert [fields[f"keyword_{i}"] for i in range(len(comparison.keyword_reception))] == [
            f"{k.name}: {k.outcome}" for k in comparison.keyword_reception]
    witnesses = []
    for row in selected:
        fields = facts(row.facts)
        witnesses.append(dict(witness_id=fields["witness_id"], role=fields["role"], version=fields["version"],
            outcome=row.state, receiver=fields["receiver"], path_steps=[" ".join(v.split(" ", 3)[:3]) for k,v in fields.items() if k.startswith("path_")],
            callee=fields["callee"], keyword_reception=[v for k,v in fields.items() if k.startswith("keyword_")], premises=row.limitations))
    paired_roles = {w["role"] for w in witnesses}
    acquisition = opened.native.sources.acquisition
    coverage = next(row for row in report.assessments if row.assessment_id == "caller-signature-coverage")
    assert coverage.state == acquisition.state
    assert facts(coverage.facts)["provider_requests"] == str(acquisition.transport.provider_requests)
    assert report.action.state == "abstain"
    branch_states = {row.assessment_id:row.status for row in report.assessments if row.assessment_id in {"ci", "runtime"}}
    assert branch_states == {"ci":"not_evaluated", "runtime":"not_evaluated"}
    return dict(revision=baseline["revision"], identity=facts(report.identity), acquisition_state=acquisition.state,
        analysis_state=run.state, retained_files=len(catalog.files), source_scopes=len(catalog.scopes),
        witness_count=len(rows), selected_witnesses=witnesses, selected_pair_present={"old_dependency", "proposed_dependency"} <= paired_roles,
        acquisition_problems=[asdict(problem) for problem in acquisition.problems], transport=asdict(acquisition.transport),
        work=asdict(result.work), discovery_gaps=len(result.gaps), unexamined_units=sum(u.coverage=="unexamined" for u in result.units),
        baseline=baseline, report_route=dict(report_decodes=1, report_bytes=len(encoded), source_operations=operations,
            source_bytes=sum(op["bytes"] for op in operations), native_pages=0, consumer_seconds=None),
        report_native_fidelity=True, action=report.action.state, branch_states=branch_states,
        cold_verified=json.loads((task / "cold-review/results.json").read_bytes())["outcome"] == "passed")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture", type=Path, required=True)
    parser.add_argument("--task", type=Path, required=True)
    args = parser.parse_args()
    os.umask(0o077)
    baseline_root = args.task / "source-baseline"
    baseline = json.loads((baseline_root / "results.json").read_bytes())
    baseline_answers = baseline_root / "answers.json"
    assert baseline_answers.is_file()
    output = args.task / "report-route"
    output.mkdir(mode=0o700)
    write(output / "contract.json", dict(method_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        baseline_answers_sha256=sha256(baseline_answers.read_bytes()).hexdigest(), source_operations=96, window_lines=100,
        reviewer_exposed=True, native_page_limit=64))
    path = Path(__file__).resolve().parent.parent / "2026-11-06-native-product-execution-readiness/cold_review.py"
    spec = importlib.util.spec_from_file_location("qualified_cold_guard", path)
    cold = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cold)
    sys.setprofile(cold.guard)
    try:
        with patch.object(socket.socket, "connect", side_effect=AssertionError("review network forbidden")):
            summary = review(args.capture, args.task, output, baseline)
    finally:
        sys.setprofile(None)
    write(output / "results.json", summary)
    print(json.dumps({k:summary[k] for k in ("acquisition_state","analysis_state","retained_files","witness_count","selected_pair_present","cold_verified")}))


if __name__ == "__main__":
    main()
