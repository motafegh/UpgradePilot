"""Fixed ordinary HTTPX native-page task through installed product consumers.

Producer/AST/network/credential work is forbidden. Expected retained results are
used only after sequential delivery; they cannot provide an undelivered page.
"""
import argparse
from dataclasses import asdict
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import resource
import socket
import subprocess
import sys
from unittest.mock import patch

import upgradepilot
from upgradepilot.caller_signature_delivery import open_caller_signature_checkpoint
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.consumer_access import WorkspaceEvidenceAccess
from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost
from upgradepilot.workspace.lifecycle_records import InvestigationNeed
from cold_pages import guard
from probe import counters

HERE = Path(__file__).resolve().parent


def write(path, value):
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(value, indent=2)+"\n")
    os.replace(temporary, path)


def delta(before):
    after = counters()
    return {k: after[k]-before[k] for k in before}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    os.umask(0o077)
    contract = json.loads((args.output / "contract.json").read_bytes())
    assert Path(upgradepilot.__file__).resolve().is_relative_to(Path(contract["installed"]))
    assert importlib.util.find_spec("experiments") is None
    stages, pages, prefix = {}, [], ""
    host = store = None
    outcome = dict(outcome="incomplete", pages=pages, stages=stages)
    try:
        before = counters()
        original = CheckpointStore.open(Path(contract["capture"]), read_only=True)
        original.backup(args.output / "store", timeout_seconds=60)
        store = CheckpointStore.open(args.output / "store")
        opened = open_caller_signature_checkpoint(store, contract["revision"])
        revision = opened.selected.revision
        bases = {bid: store.read_revision(revision.lineage_id, bid,
            expected_target=revision.boundary.target).revision.boundary
            for bid in dict.fromkeys(r.basis_revision_id for r in revision.lifecycle_history.records)}
        host = InvestigationWorkspaceHost(store=store, lineage_id=revision.lineage_id)
        host.restore(opened.selected, bases=bases)
        access = WorkspaceEvidenceAccess(host, opened.native.sources.catalog,
            native_families=("caller_signature_comparison",))
        host.configure(authority=None, capabilities=(), methods=(access.method,))
        purpose = host.add_purpose(InvestigationNeed("navigation", contract["task_question"], access.scope),
            native_record_ids=tuple(r.record_id for r in revision.boundary.records))
        record = next(r for r in revision.boundary.records if r.family == "caller_signature_comparison")
        menu_id = access.native_view(purpose, (record.family,))
        menu = host.lifecycle_value(menu_id).retained_content.encode()
        (args.output / "menu.json").write_bytes(menu)
        assert json.loads(menu)["omitted"]
        stages["setup_and_menu"] = delta(before)
        loop_before, cursor = counters(), 0
        for number in range(1, 61):
            before = counters()
            delivery_id = access.native_page(purpose, record.record_id, start_character=cursor)
            page_counters = delta(before)
            content = host.lifecycle_value(delivery_id).retained_content.encode()
            page = json.loads(content)
            assert page["start_character"] == cursor
            prefix += page["text"]
            row = dict(page=number, delivery_id=delivery_id, bytes=len(content),
                sha256=sha256(content).hexdigest(), counters=page_counters,
                confirmed_revision=host.current.revision_id)
            pages.append(row)
            (args.output / "prefix.txt").write_text(prefix)
            write(args.output / "progress.json", dict(pages=number, confirmed_revision=host.current.revision_id,
                last_page_counters=page_counters, characters=len(prefix)))
            write(args.output / "page-timings.json", pages)
            print(json.dumps(dict(event="page", page=number, confirmed_revision=host.current.revision_id)), flush=True)
            if number < 60:
                assert page["next_character"] is not None
                cursor = page["next_character"]
        stages["page_loop_with_progress_io"] = delta(loop_before)
        before = counters()
        candidates, _ = json.JSONDecoder().raw_decode(prefix.split('"candidates":', 1)[1].lstrip())
        expected = opened.native.comparison.result.candidates
        assert json.dumps(candidates, sort_keys=True) == json.dumps([asdict(c) for c in expected], sort_keys=True)
        native = [c for c in candidates if c["callee_role"]["role"] in {"old_dependency", "proposed_dependency"}]
        assert len(native) == 4 and len({c["root_call_id"] for c in native}) == 1
        assert host.current.boundary == revision.boundary
        assert store.read_selected_revision(host.current.revision_id).revision == host.current
        manifest = dict(pages=pages, prefix_sha256=sha256(prefix.encode()).hexdigest(),
                        checkpoint_digest=host.current.digest())
        write(args.output / "expected-pages.json", manifest)
        stages["verification_and_readback"] = delta(before)
        before = counters()
        usage = resource.getrusage(resource.RUSAGE_CHILDREN)
        child = subprocess.run([sys.executable, str(HERE / "cold_pages.py"), str(args.output / "store"),
            host.current.revision_id, str(args.output / "expected-pages.json")],
            env=dict(os.environ, PYTHONPATH=contract["installed"]), cwd=args.output,
            capture_output=True, timeout=60)
        after_usage = resource.getrusage(resource.RUSAGE_CHILDREN)
        (args.output / "cold.txt").write_bytes(child.stdout+child.stderr)
        stages["cold_child_wait"] = delta(before)
        outcome["cold_child_cpu_seconds"] = (after_usage.ru_utime+after_usage.ru_stime)-(usage.ru_utime+usage.ru_stime)
        assert child.returncode == 0, (child.stdout+child.stderr)[-2000:]
        cold = json.loads(child.stdout)
        assert cold["outcome"] == "passed"
        outcome.update(outcome="passed", delivered_pages=60, characters=len(prefix),
            total_delivered_bytes=sum(r.delivered_bytes for r in access.receipts),
            candidate_array_complete=True, all_candidates_equal=True,
            native_version_witnesses=4, native_paired_roots=1, native_boundary_unchanged=True,
            cold=cold, prefix_sha256=manifest["prefix_sha256"])
    except BaseException as error:
        outcome.update(outcome="interrupted" if isinstance(error, KeyboardInterrupt) else "failed",
                       problem=type(error).__name__+": "+str(error))
        raise
    finally:
        if host is not None:
            outcome["confirmed_revision"] = host.current.revision_id if host.current else None
            attempted = host.unacknowledged_revision
            outcome["attempted_revision"] = attempted.revision_id if attempted else None
            if attempted is not None:
                try:
                    outcome["publication_inspection"] = store.inspect_publication(attempted)
                except Exception:
                    outcome["publication_inspection"] = "unknown"
        write(args.output / "worker-results.json", outcome)


if __name__ == "__main__":
    sys.setprofile(guard)
    with patch.object(socket.socket, "connect", side_effect=AssertionError("timed traversal is offline")):
        main()
