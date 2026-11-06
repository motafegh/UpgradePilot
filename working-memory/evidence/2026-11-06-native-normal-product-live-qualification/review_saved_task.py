"""Second task route and post-route grading over the single saved live capture.

Baseline answers must already be closed. Report facts select bounded source reads;
native results are then used only to check faithful projection, never to fill a
missing dependency witness. Network/producers/AST/synthesis remain forbidden.
"""
from dataclasses import asdict
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import socket
import sys
from unittest.mock import patch

from upgradepilot.caller_signature_delivery import open_caller_signature_checkpoint
from upgradepilot.caller_signature.source_codec import decode_sources
from upgradepilot.report_file import encode_report
from upgradepilot.workspace.checkpoint_store import CheckpointStore

HERE = Path(__file__).resolve().parent
PRIVATE = Path("/home/motafeq/.local/share/upgradepilot/native-signature-kubernetes-dashboard-token-api-pr-20-httpx-2026-11-06")


def write(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


def facts(items):
    return {f.name: f.value for f in items}


def main():
    os.umask(0o077)
    task = PRIVATE / "task-review-01"
    baseline = json.loads((task / "source-baseline-finalization-01/results.json").read_bytes())
    assert baseline["outcome"] == "direct_source_baseline_closed_before_report_review"
    output = task / "report-route"
    output.mkdir(mode=0o700, exist_ok=False)
    write(output / "contract.json", dict(method_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        baseline_sha256=sha256((task / "source-baseline-finalization-01/results.json").read_bytes()).hexdigest(),
        source_operation_limit=96, source_window_lines=100, native_page_limit=64,
        prior_report_route_decodes=2, prior_failed_decode_included=True,
        cold_verification_report_decodes=5, reviewer_exposed=True, consumer_seconds=None))
    spec = importlib.util.spec_from_file_location("qualified_cold_guard", HERE.parent / "2026-11-06-native-product-execution-readiness/cold_review.py")
    cold = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cold)
    sys.setprofile(cold.guard)
    try:
        with patch.object(socket.socket, "connect", side_effect=AssertionError("saved task network forbidden")):
            opened = open_caller_signature_checkpoint(CheckpointStore.open(PRIVATE / "product-attempt-01/store", read_only=True), baseline["revision"])
            report = opened.report
            report_bytes = encode_report(report)
            assert report_bytes == (PRIVATE / "product-attempt-01/report.json").read_bytes()
            catalog = opened.native.sources.catalog
            sources = {s.source_id: s for s in report.sources}
            by_path = {facts(s.identity).get("path"): s for s in report.sources if any(f.name == "file_id" for f in s.identity)}
            operations = []
            for path in ("tests/test_routes.py", "requirements.txt"):
                source = by_path[path]
                identity = facts(source.identity)
                arguments = dict(source_id=identity["source_id"], path=path, start_line=1, line_count=100)
                response = catalog.query("read", arguments)
                assert response.outcome == "observed"
                payload = json.loads(response.content)["payload"]
                assert payload["file"]["file_id"] == identity["file_id"] and len(payload["lines"]) <= 100
                (output / (source.source_id + ".json")).write_bytes(response.content)
                operations.append(dict(source_id=source.source_id, operation="read", arguments=arguments,
                    bytes=len(response.content), lines=len(payload["lines"]), exact_source_mapping=True))
            # Producer record is already retained in the decoded report. This is
            # source inspection/fixed decoding, not native paging or acquisition.
            producer = next(s for s in report.sources if facts(s.identity).get("family") == "caller_signature_sources")
            receipt_sources = decode_sources(producer.content.encode())
            assert receipt_sources == opened.native.sources
            a = receipt_sources.acquisition
            coverage = next(x for x in report.assessments if x.assessment_id == "caller-signature-coverage")
            analysis = next(x for x in report.assessments if x.assessment_id == "caller-signature-analysis")
            comparisons = [x for x in report.assessments if any(f.name == "witness_id" for f in x.facts)]
            target_source = by_path["tests/test_routes.py"].source_id
            selected = [x for x in comparisons if facts(x.facts).get("root_location", "").startswith(target_source + " L7 ")]
            paired = [x for x in selected if facts(x.facts).get("role") in {"old_dependency", "proposed_dependency"}]
            report_answers = dict(identity=facts(report.identity), selected_call="tests/test_routes.py L7 TestClient(app), fastapi.testclient import at L2",
                source_outcomes="No selected old/proposed HTTPX witness; three report comparisons are local target get_token calls.",
                missing_evidence="No dependency module receipts/source scopes; FastAPI and pytest release-index requests timed out.",
                recovery="Exact selected call/declaration source and saved report recovered; missing library definitions cannot be recovered.",
                next_observation="A separately scoped transport diagnostic must distinguish why PyPI timed out before any new acquisition. Runtime state remains a separate later proof responsibility.")
            write(output / "route-answers.json", report_answers)
            write(output / "operations.json", operations)
            # Post-route grading: compare native facts only after both routes close.
            result = opened.native.comparison.result
            candidates = {c.candidate_id: c for c in result.candidates}
            file_sources = {facts(s.identity)["file_id"]: s.source_id for s in report.sources if "file_id" in facts(s.identity)}
            assert {facts(x.facts)["witness_id"] for x in comparisons} == set(candidates)
            for row in comparisons:
                row_facts = facts(row.facts)
                c = candidates[row_facts["witness_id"]]
                assert row.state == c.comparison.outcome
                assert row_facts["role"] == c.callee_role.role and row_facts["version"] == c.callee_role.version
                assert row.limitations == c.premises + c.comparison.remaining_premises + c.comparison.unresolved_checks
                assert [row_facts[f"path_{i}"] for i in range(len(c.steps))] == [
                    f"{file_sources[s.unit_id]} L{s.span.line}:{s.span.column} {s.operation} {s.expression}" for s in c.steps]
            assert coverage.state == a.state and facts(coverage.facts)["provider_requests"] == str(a.transport.provider_requests)
            assert report.action.state == "abstain"
            unperformed = {x.assessment_id:x.status for x in report.assessments if x.assessment_id in {"ci","runtime"}}
            assert unperformed == {"ci":"not_evaluated","runtime":"not_evaluated"}
            selected_file = facts(by_path["tests/test_routes.py"].identity)["file_id"]
            selected_gaps = [asdict(g) for g in result.gaps if g.unit_id == selected_file and g.span and g.span.line == 7]
            summary = dict(outcome="defer_positive_adoption_transport_limited", exact_revision=baseline["revision"],
                source_baseline={k:baseline[k] for k in ("operations","windows","delivered_bytes","read_operations","native_pages","report_reads")},
                report_route=dict(source_operations=len(operations), delivered_source_bytes=sum(o["bytes"] for o in operations),
                    report_decodes_this_route=3, failed_diagnostic_decode_included=True, report_bytes_per_decode=len(report_bytes),
                    cold_verification_report_decodes_separate=5, embedded_producer_records_inspected=1,
                    native_pages=0, consumer_seconds=None, faithful_answers=report_answers),
                native=dict(acquisition_state=a.state, analysis_state=opened.native.comparison.state,
                    retained_files=len(catalog.files), dependency_source_scopes=sum(s.repository!=opened.selected.revision.boundary.target.repository for s in catalog.scopes),
                    module_receipts=len(a.module_requests), comparisons=len(result.candidates), roots=len({c.root_call_id for c in result.candidates}),
                    selected_root_report_witnesses=len(selected), selected_httpx_witnesses=len(paired), gaps=len(result.gaps),
                    work=asdict(result.work), selected_call_gaps=selected_gaps),
                transport=dict(github=a.transport.github_requests, provider=a.transport.provider_requests,
                    body_bytes=a.transport.decoded_body_bytes, elapsed=asdict(a.transport.elapsed),
                    requests=[asdict(e) for e in a.transport.requests], stops=[asdict(s) for s in a.transport.stops],
                    retry_policy=a.transport.retry_policy, retry_decisions=[asdict(s) for s in a.transport.retry_decisions]),
                acquisition_problems=[asdict(p) for p in a.problems], report_projection_faithful=True,
                analysis_elapsed=asdict(opened.native.comparison.elapsed),
                unperformed_branches=unperformed, action=report.action.state,
                positive_paired_task=False, direct_baseline_extended_after_grading=False,
                report_source_recovery=True, performance_repair_selected=False,
                disposition="Defer positive native-adoption qualification: selected paired evidence unavailable after PyPI timeouts. Preserve useful partial target evidence; no checker repair/retry/cap enlargement.",
                next_responsibility="Bounded PyPI transport diagnosis against the retained failure; any network diagnostic or successor acquisition must be separately admitted.",
                independent_usefulness=False, runtime_compatibility=False, real_provider_calls_during_review=0)
            write(output / "results.json", summary)
    finally:
        sys.setprofile(None)
    print(json.dumps({k:summary[k] for k in ("outcome","exact_revision","native","report_projection_faithful","positive_paired_task","action","disposition")}))


if __name__ == "__main__":
    main()
