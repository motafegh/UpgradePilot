"""Dated, exposed-implementer navigation measurement; no usefulness inference.

Report and native paths may use retained comparisons. The source-only baseline
uses only catalog descriptors, literal search and bounded source reads. No native
fact offsets or expected witness IDs are supplied to that baseline.
"""
from dataclasses import asdict
from hashlib import sha256
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
from unittest.mock import patch

from qualify import cold_reader
from upgradepilot.caller_signature_delivery import open_caller_signature_checkpoint
from upgradepilot.report_file import read_report
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.consumer_access import WorkspaceEvidenceAccess
from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost
from upgradepilot.workspace.lifecycle_records import InvestigationNeed

HERE = Path(__file__).resolve().parent


def write(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--attempt", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(mode=0o700, exist_ok=False)
    task = json.loads((HERE / "navigation-task.json").read_bytes())
    # Freeze operation ceilings before opening any comparison. A refusal is a
    # result; this driver never enlarges limits or repairs the input in place.
    contract = dict(task=task, native_pages=64, page_characters=4096,
                    source_operations=96, source_window_lines=100,
                    native_session="durable validated backup; new consumer purpose only",
                    baseline="direct bounded catalog queries, no lifecycle publication cost",
                    manual_time="unmeasured", implementer_exposed=True,
                    script_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
    write(args.output / "contract.json", contract)
    row = next(r for r in json.loads((args.attempt / "results.json").read_bytes()) if r["case"] == "httpx")
    capture = args.attempt / "http-httpx"
    store = CheckpointStore.open(capture / "store", read_only=True)
    opened = open_caller_signature_checkpoint(store, row["confirmed_revision"])
    catalog, result = opened.native.sources.catalog, opened.native.comparison.result
    target = task["target_file"]
    scopes = {s.source_id: s for s in catalog.scopes}
    files = {catalog.descriptor(f)["file_id"]: f for f in catalog.files}
    target_file = next(f for f in catalog.files if f.path == target["path"]
                       and scopes[f.source_id].repository == target["repository"]
                       and scopes[f.source_id].revision == target["revision"])
    uid = catalog.descriptor(target_file)["file_id"]
    root = next(c for u in result.units if u.facts for c in u.facts.calls
                if c.unit_id == uid and asdict(c.span) == target["span"])
    expected = [c for c in result.candidates if c.root_call_id == root.fact_id
                and c.callee_role.role in {"old_dependency", "proposed_dependency"}]
    outcomes = dict(proof_class=task["proof_class"], selected_revision=row["confirmed_revision"],
                    native_root=root.fact_id, expected_native_witnesses=len(expected))

    # Actual saved report decode plus guarded cold CLI original-source opening.
    report_path = capture / "report.json"
    report = read_report(report_path)
    witnesses = [a for a in report.assessments if {f.name: f.value for f in a.facts}.get("root_call_id") == root.fact_id
                 and {f.name: f.value for f in a.facts}.get("role") in {"old_dependency", "proposed_dependency"}]
    ids = set()
    for a in witnesses:
        facts = {f.name: f.value for f in a.facts}
        for key, value in facts.items():
            if key in {"root_location", "caller", "callee"} or key.startswith("path_"):
                ids.add(value.split()[0])
    source_results = []
    for sid in sorted(ids):
        source = next(s for s in report.sources if s.source_id == sid)
        child = subprocess.run([sys.executable, "-c", cold_reader(), "--open-report", str(report_path), "--show-source", sid],
            cwd=args.output, env=dict(os.environ, PYTHONPATH=os.pathsep.join(str(Path(p).absolute()) for p in sys.path if p)),
            capture_output=True, timeout=60)
        (args.output / (sid + ".txt")).write_bytes(child.stdout + child.stderr)
        assert child.returncode == 0 and source.content.encode() in child.stdout
        source_results.append(dict(source_id=sid, output_bytes=len(child.stdout), exact_text=True))
    by_witness = {next(f.value for f in a.facts if f.name == "witness_id"): a for a in witnesses}
    assert set(by_witness) == {c.candidate_id for c in expected}
    assert all(by_witness[c.candidate_id].state == c.comparison.outcome
               and by_witness[c.candidate_id].limitations == c.premises + c.comparison.remaining_premises + c.comparison.unresolved_checks
               for c in expected)
    outcomes["report"] = dict(witnesses=len(witnesses), all_premises_equal=True,
        calls=1+len(ids), decoded_report_bytes=report_path.stat().st_size,
        source_cli_bytes=sum(r["output_bytes"] for r in source_results), source_opens=source_results,
        semantics="structured report decode and full original-source CLI opens; no timed human task")
    write(args.output / "results.json", outcomes)

    # Mechanical source baseline. Searches decide read locations from delivered
    # text alone; no root/signature facts or comparison offsets enter this route.
    operations = []
    def query(op, arguments):
        assert len(operations) < contract["source_operations"]
        response = catalog.query(op, arguments)
        body = json.loads(response.content)
        operations.append(dict(operation=op, arguments=arguments, bytes=len(response.content),
            outcome=response.outcome, examined_files=response.examined_files, examined_lines=response.examined_lines))
        assert response.outcome != "problem", body
        return body["payload"]
    query("list_sources", {})
    query("read", dict(source_id=target_file.source_id, path=target_file.path, start_line=1, line_count=30))
    matches = []
    # Roots/signatures/forwarding are discoverable by literal tokens in this
    # already exposed task. This is a reproducible route, not an unbiased search.
    for term in ("TestClient", "class Client(", "super().__init__("):
        offset = 0
        while True:
            body = query("search", dict(query=term, offset=offset))
            matches.extend(body["items"])
            if body.get("next_offset") is None:
                break
            offset = body["next_offset"]
    seen, windows = set(), []
    for match in matches:
        key = (match["source_id"], match["path"], max(1, match["line"]-5))
        if key in seen:
            continue
        seen.add(key)
        body = query("read", dict(source_id=key[0], path=key[1], start_line=key[2], line_count=100))
        windows.append(dict(source_id=key[0], path=key[1], start=body["start_line"], lines=body["lines"]))
    write(args.output / "baseline-source-windows.json", windows)
    write(args.output / "baseline-operations.json", operations)
    outcomes["source_baseline"] = dict(calls=len(operations), bytes=sum(o["bytes"] for o in operations),
        examined_files=sum(o["examined_files"] for o in operations), examined_lines=sum(o["examined_lines"] for o in operations),
        windows=len(windows), matched_scopes=sorted({m["source_id"] for m in matches}),
        witness_premises="not encoded by source-only access; require reviewer interpretation",
        completeness="mechanical source retrieval only; no independent all-witness reasoning or time measurement")
    write(args.output / "results.json", outcomes)

    # Full native record omission must be respected. Pages are obtained from the
    # first character in order; no oracle offset or hidden candidate selection.
    native = dict(pages=0, candidates_complete=False, all_witnesses=False)
    access = None
    try:
        backup = args.output / "navigation-store"
        store.backup(backup)
        mutable = CheckpointStore.open(backup)
        selected = mutable.read_selected_revision(row["confirmed_revision"])
        revision = selected.revision
        host = InvestigationWorkspaceHost(store=mutable, lineage_id=revision.lineage_id)
        bases = {r.basis_revision_id: mutable.read_revision(revision.lineage_id, r.basis_revision_id,
            expected_target=revision.boundary.target).revision.boundary for r in revision.lifecycle_history.records}
        host.restore(selected, bases=bases)
        access = WorkspaceEvidenceAccess(host, catalog, native_families=("caller_signature_comparison",))
        host.configure(authority=None, capabilities=(), methods=(access.method,))
        purpose = host.add_purpose(InvestigationNeed("navigation", task["question"], access.scope),
            native_record_ids=tuple(r.record_id for r in revision.boundary.records))
        delivery = access.native_view(purpose, ("caller_signature_comparison",))
        menu = json.loads(host.lifecycle_value(delivery).retained_content)
        write(args.output / "native-menu.json", menu)
        native["initial_omitted"] = bool(menu["omitted"])
        record = next(r for r in revision.boundary.records if r.family == "caller_signature_comparison")
        text, cursor = "", 0
        candidates = None
        for _ in range(contract["native_pages"]):
            did = access.native_page(purpose, record.record_id, start_character=cursor)
            page = json.loads(host.lifecycle_value(did).retained_content)
            text += page["text"]
            native["pages"] += 1
            marker = '"candidates":'
            if marker in text:
                try:
                    candidates, _ = json.JSONDecoder().raw_decode(text.split(marker, 1)[1].lstrip())
                except json.JSONDecodeError:
                    pass
                else:
                    break
            if page["next_character"] is None:
                break
            cursor = page["next_character"]
        (args.output / "native-page-prefix.txt").write_text(text)
        native["candidates_complete"] = candidates is not None
        if candidates is not None:
            actual = [c for c in candidates if c["root_call_id"] == root.fact_id
                      and c["callee_role"]["role"] in {"old_dependency", "proposed_dependency"}]
            native["all_witnesses"] = sorted(c["candidate_id"] for c in actual) == sorted(c.candidate_id for c in expected)
            native["ordered_paths_comparisons_premises_equal"] = all(
                c == asdict(next(e for e in expected if e.candidate_id == c["candidate_id"])) for c in actual)
        native["confirmed_revision"] = host.current.revision_id
        mutable.read_selected_revision(host.current.revision_id)
        native["durable_reopen"] = True
    except Exception as error:
        native.update(error=type(error).__name__, reason=str(error)[:500])
    finally:
        if access:
            native["receipts"] = [asdict(r) for r in access.receipts]
            native["bytes"] = sum(r.delivered_bytes for r in access.receipts)
        outcomes["bounded_native"] = native
        write(args.output / "results.json", outcomes)
    print(json.dumps({k: v for k,v in outcomes.items() if k != "bounded_native"}))
    print(json.dumps({k:v for k,v in native.items() if k != "receipts"}))


if __name__ == "__main__":
    with patch("socket.socket.connect", side_effect=AssertionError("offline navigation")):
        main()
