"""Count actual original-basis decoding for one retained controlled native page.

The delegating spy observes production calls; it does not replace their results.
Counters are per transaction/basis, not inferred active traversal durations.
"""
from collections import Counter
from hashlib import sha256
import argparse
import json
from pathlib import Path
import time
from unittest.mock import patch

from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.caller_signature_delivery import open_caller_signature_checkpoint
from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost
from upgradepilot.workspace.consumer_access import WorkspaceEvidenceAccess
from upgradepilot.workspace.lifecycle_records import InvestigationNeed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--capture", type=Path, required=True)
    parser.add_argument("--revision", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(mode=0o700, exist_ok=False)
    root = Path(__file__).resolve().parent.parents[2]
    methods = {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest()
               for p in sorted((root / "src/upgradepilot").rglob("*.py"))}
    (args.output / "contract.json").write_text(json.dumps(dict(
        proof="delegating read-count control over one actual native page, no acquisition",
        capture=str(args.capture), revision=args.revision, product_source_sha256=methods,
        method_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        timing="elapsed/process-CPU counter readings only; no active55-minute inference"), indent=2)+"\n")
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
    purpose = host.add_purpose(InvestigationNeed("read-count", "Inspect one actual page.", access.scope),
        native_record_ids=tuple(x.record_id for x in revision.boundary.records))
    record = next(x for x in revision.boundary.records if x.family == "caller_signature_comparison")
    started, cpu = time.monotonic_ns(), time.process_time_ns()
    with patch.object(store, "_read", wraps=store._read) as spy:
        access.native_page(purpose, record.record_id)
        # Retained spy arguments keep connection objects distinct across the two
        # publication transactions, avoiding recycled object-ID ambiguity.
        counts = Counter((id(call.args[0]), call.args[2]) for call in spy.call_args_list
                         if call.kwargs.get("validate_lifecycle") is False)
        result = dict(total_original_basis_decodes=sum(counts.values()),
            unique_transaction_basis_pairs=len(counts), worst_repeats=max(counts.values()),
            publication_transactions=len({key[0] for key in counts}),
            elapsed_counter_ns=time.monotonic_ns()-started, process_cpu_counter_ns=time.process_time_ns()-cpu,
            delivered_bytes=access.receipts[-1].delivered_bytes, selected_revision=host.current.revision_id)
    (args.output / "results.json").write_text(json.dumps(result, indent=2)+"\n")
    assert all(sha256((root/name).read_bytes()).hexdigest() == digest for name,digest in methods.items())
    print(json.dumps(result))


if __name__ == "__main__":
    with patch("socket.socket.connect", side_effect=AssertionError("read-count control is offline")):
        main()
