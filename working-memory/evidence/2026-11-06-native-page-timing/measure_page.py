"""One actual first-page publication, isolated by the supervising comparison.

Setup/readback are deliberately outside the measured page. No production spies,
analysis, input rewriting or retained-code execution participate in this control.
"""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import resource
import socket
import time
from unittest.mock import patch

from upgradepilot.caller_signature_delivery import open_caller_signature_checkpoint
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.consumer_access import WorkspaceEvidenceAccess
from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost
from upgradepilot.workspace.lifecycle_records import InvestigationNeed


def counters():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    return dict(monotonic_ns=time.monotonic_ns(),
                raw_ns=time.clock_gettime_ns(time.CLOCK_MONOTONIC_RAW),
                cpu_ns=time.process_time_ns(),
                rusage_cpu_ns=round((usage.ru_utime + usage.ru_stime) * 1e9))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--capture", type=Path, required=True)
    parser.add_argument("--revision", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(mode=0o700, exist_ok=False)
    setup_start = counters()
    original = CheckpointStore.open(args.capture / "store", read_only=True)
    original.backup(args.output / "store", timeout_seconds=60)
    store = CheckpointStore.open(args.output / "store")
    opened = open_caller_signature_checkpoint(store, args.revision)
    revision = opened.selected.revision
    bases = {bid: store.read_revision(revision.lineage_id, bid,
        expected_target=revision.boundary.target).revision.boundary
        for bid in dict.fromkeys(x.basis_revision_id for x in revision.lifecycle_history.records)}
    host = InvestigationWorkspaceHost(store=store, lineage_id=revision.lineage_id)
    host.restore(opened.selected, bases=bases)
    access = WorkspaceEvidenceAccess(host, opened.native.sources.catalog,
        native_families=("caller_signature_comparison",))
    host.configure(authority=None, capabilities=(), methods=(access.method,))
    purpose = host.add_purpose(InvestigationNeed("page-timing", "Inspect one actual page.", access.scope),
        native_record_ids=tuple(x.record_id for x in revision.boundary.records))
    record = next(x for x in revision.boundary.records if x.family == "caller_signature_comparison")
    before = counters()
    delivery_id = access.native_page(purpose, record.record_id)
    after = counters()
    delivered = host.lifecycle_value(delivery_id).retained_content.encode()
    assert len(access.receipts) == 1 and access.receipts[0].outcome == "observed"
    assert access.receipts[0].delivered_bytes == len(delivered)
    assert host.current.boundary == revision.boundary
    acknowledged = store.read_revision(revision.lineage_id, host.current.revision_id,
        expected_target=revision.boundary.target)
    assert acknowledged.revision == host.current
    (args.output / "page.json").write_bytes(delivered)
    result = dict(outcome="passed", input_revision=args.revision,
        selected_revision=host.current.revision_id, delivery_id=delivery_id,
        delivered_bytes=len(delivered), page_sha256=sha256(delivered).hexdigest(),
        acknowledged_readback_equal=True, native_boundary_unchanged=True,
        setup_counters={k: before[k]-setup_start[k] for k in before},
        page_counters={k: after[k]-before[k] for k in after},
        loaded_product_file=str(Path(__import__("upgradepilot").__file__).resolve()))
    (args.output / "results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    with patch.object(socket.socket, "connect", side_effect=AssertionError("offline timing control")):
        main()
