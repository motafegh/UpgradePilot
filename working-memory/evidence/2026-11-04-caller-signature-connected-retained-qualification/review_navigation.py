"""Post-measurement grading of already delivered material, never query selection.

Expected native locations are used only after the fixed source-only route has
finished. Native page text comes exclusively from acknowledged ViewDeliveries in
the backup, not from directly selecting a hidden comparison payload.
"""
from dataclasses import asdict
import argparse
import json
from pathlib import Path

from upgradepilot.caller_signature_delivery import open_caller_signature_checkpoint
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.lifecycle_boundary import reconstruct_lifecycle_history
from upgradepilot.workspace.lifecycle_records import ViewDelivery
from upgradepilot.workspace.consumer_access import NATIVE_VIEW_REPRESENTATION


def canonical(value):
    return json.dumps(value, sort_keys=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--navigation", type=Path, required=True)
    parser.add_argument("--capture", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    measured = json.loads((args.navigation / "results.json").read_bytes())
    source_store = CheckpointStore.open(args.capture / "store", read_only=True)
    original = open_caller_signature_checkpoint(source_store, measured["selected_revision"])
    result, catalog = original.native.comparison.result, original.native.sources.catalog
    witnesses = [c for c in result.candidates if c.root_call_id == measured["native_root"]
                 and c.callee_role.role in {"old_dependency", "proposed_dependency"}]
    files = {catalog.descriptor(f)["file_id"]: f for f in catalog.files}
    calls = {c.fact_id: c for u in result.units if u.facts for c in u.facts.calls}
    signatures = {s.fact_id: s for u in result.units if u.facts for s in u.facts.signatures}
    required = set()
    for candidate in witnesses:
        # Full call and signature header, plus every path start location. This is
        # location coverage, not proof of a human's interpretation of those lines.
        call, sig = calls[candidate.comparison.call_id], signatures[candidate.comparison.signature_id]
        for uid, span in [(call.unit_id, call.span), (sig.unit_id, sig.header_span)]:
            required.add((uid, span.line, span.end_line))
        required.update((s.unit_id, s.span.line, s.span.line) for s in candidate.steps)
    operations = json.loads((args.navigation / "baseline-operations.json").read_bytes())
    missing = []
    for uid, first, last in sorted(required):
        file = files[uid]
        reads = [o["arguments"] for o in operations if o["operation"] == "read"
                 and o["arguments"]["source_id"] == file.source_id and o["arguments"]["path"] == file.path]
        if not all(any(a["start_line"] <= line < a["start_line"]+a["line_count"] for a in reads)
                   for line in range(first, last+1)):
            missing.append(dict(source_id=file.source_id, path=file.path, first=first, last=last))
    grading = dict(proof="post-measurement exposed engineering review; not independent usefulness",
        source_baseline=dict(required_locations=len(required), missing_locations=missing,
            complete_location_retrieval=not missing, semantic_answer="not independently scored"))
    report = original.report
    source_ids = {next(i.value for i in s.identity if i.name == "file_id"): s.source_id
                  for s in report.sources if any(i.name == "file_id" for i in s.identity)}
    report_candidates = {next(f.value for f in a.facts if f.name == "witness_id"): a
                         for a in report.assessments if any(f.name == "witness_id" for f in a.facts)}
    for candidate in witnesses:
        assessment = report_candidates[candidate.candidate_id]
        facts = {f.name: f.value for f in assessment.facts}
        assert facts["root_call_id"] == candidate.root_call_id
        assert facts["role"] == candidate.callee_role.role and facts["version"] == candidate.callee_role.version
        assert assessment.state == candidate.comparison.outcome
        assert assessment.limitations == candidate.premises + candidate.comparison.remaining_premises + candidate.comparison.unresolved_checks
        assert [facts[f"path_{i}"] for i in range(len(candidate.steps))] == [
            f"{source_ids[s.unit_id]} L{s.span.line}:{s.span.column} {s.operation} {s.expression}" for s in candidate.steps]
    grading["report"] = dict(witnesses=len(witnesses), ordered_paths_roles_versions_outcomes_premises_equal=True,
        answer="One TestClient(app) root through fastapi/starlette to old/proposed HTTPX. Four alternative native witnesses are locally bound under retained premises.",
        next_discriminating_observation="Exact installed FastAPI/Starlette/HTTPX distributions and import/binding provenance, then evidence execution reaches the selected forwarding body/signature.",
        runtime_compatibility_or_action_proved=False)

    store = CheckpointStore.open(args.navigation / "navigation-store", read_only=True)
    historical = store.read_selected_revision(measured["selected_revision"])
    selected = store.read_selected_revision(historical.head_revision_id)
    revision = selected.revision
    bases = {r.basis_revision_id: store.read_revision(revision.lineage_id, r.basis_revision_id,
        expected_target=revision.boundary.target).revision.boundary for r in revision.lifecycle_history.records}
    decoded = reconstruct_lifecycle_history(revision.lifecycle_history, bases=bases)
    pages = []
    for record in decoded:
        value = record.value
        if isinstance(value, ViewDelivery) and value.representation == NATIVE_VIEW_REPRESENTATION:
            body = json.loads(value.retained_content)
            if "start_character" in body:
                pages.append(body)
    text = ""
    for page in pages:
        assert page["start_character"] == len(text)
        text += page["text"]
    native = dict(acknowledged_revision=revision.revision_id, acknowledged_revision_readable=True,
        delivered_pages=len(pages), delivered_characters=len(text), candidates_complete=False)
    if '"candidates":' in text:
        try:
            candidates, _ = json.JSONDecoder().raw_decode(text.split('"candidates":', 1)[1].lstrip())
        except json.JSONDecodeError:
            pass
        else:
            native["candidates_complete"] = True
            actual = [c for c in candidates if c["root_call_id"] == measured["native_root"]
                      and c["callee_role"]["role"] in {"old_dependency", "proposed_dependency"}]
            native["all_witnesses_equal"] = sorted(map(canonical, actual)) == sorted(canonical(asdict(c)) for c in witnesses)
    grading["native_delivered_material"] = native
    args.output.write_text(json.dumps(grading, indent=2)+"\n")
    print(json.dumps(grading))


if __name__ == "__main__":
    main()
