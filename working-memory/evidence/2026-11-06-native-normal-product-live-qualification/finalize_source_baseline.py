"""Finish baseline bookkeeping from saved responses; never repeat/extend queries.

The original collector failed after delivering all windows because it used a
nonexistent receipt field. Preserve that execution and its method digest; the
correct metadata owner is SourceAcquisitionReceipt.adapter_limitations.
"""
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import shutil
import socket
import sys
from unittest.mock import patch

from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_projection import reconstruct_caller_signature_projection

HERE = Path(__file__).resolve().parent
PRIVATE = Path("/home/motafeq/.local/share/upgradepilot/native-signature-kubernetes-dashboard-token-api-pr-20-httpx-2026-11-06")


def main():
    os.umask(0o077)
    baseline = PRIVATE / "task-review-01/source-baseline"
    output = PRIVATE / "task-review-01/source-baseline-finalization-01"
    output.mkdir(mode=0o700, exist_ok=False)
    original = HERE / "collect_source_baseline.py"
    contract = json.loads((baseline / "contract.json").read_bytes())
    assert sha256(original.read_bytes()).hexdigest() == contract["method_sha256"]
    shutil.copyfile(original, output / "executed-collector.py")
    operations = json.loads((baseline / "operations.json").read_bytes())
    windows = json.loads((baseline / "windows.json").read_bytes())
    assert len(operations) <= 96 and all(len(w["lines"]) <= 100 for w in windows)
    spec = importlib.util.spec_from_file_location("qualified_cold_guard", HERE.parent / "2026-11-06-native-product-execution-readiness/cold_review.py")
    cold = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cold)
    sys.setprofile(cold.guard)
    try:
        with patch.object(socket.socket, "connect", side_effect=AssertionError("baseline finalization network forbidden")):
            selected = CheckpointStore.open(PRIVATE / "product-attempt-01/store", read_only=True).read_selected_revision(contract["revision"])
            target = selected.revision.boundary.target
            sources = reconstruct_caller_signature_projection(selected.revision.boundary, expected_target=target).sources
            summary = dict(outcome="direct_source_baseline_closed_before_report_review", revision=contract["revision"],
                operations=len(operations), windows=len(windows), delivered_bytes=sum(o["bytes"] for o in operations),
                read_operations=sum(o["operation"] == "read" for o in operations), native_pages=0, report_reads=0,
                real_provider_calls=0, additional_source_queries=0, consumer_seconds=None,
                identity={name:getattr(target,name) for name in ("repository","pull_number","base_sha","head_sha","normalized_package","old_version","proposed_version")},
                capture_state=sources.acquisition.state, adapter_limitations=sources.acquisition.adapter_limitations,
                answers={
                    "identity":"Exact frozen target identity is retained; see identity fields.",
                    "selected_call":"tests/test_routes.py L7 TestClient(app), imported from fastapi.testclient at L2. No downstream definitions appear in delivered source searches.",
                    "local_outcomes":"Cannot establish old/proposed signature reception from the delivered original sources; no dependency-source scopes are available.",
                    "limits":"Only retained target-source scope was listed. Scoped-negative signature/forwarder searches do not prove those definitions absent upstream or unexecuted in reality.",
                    "recovery":"Selected call text is recoverable from this capture; dependency forwarder/signature originals are unavailable to this route.",
                    "next_observation":"First inspect this capture's acquisition receipts for missing dependency material. Actual installed/imported/dispatch/exercised state would require separate matched runtime evidence."},
                correction=dict(stage="post-query summary only", error="AttributeError: SourceAcquisitionReceipt has no limitations field",
                    correct_field="adapter_limitations", original_queries_repeated=False, product_changed=False),
                original_response_sha256={p.name:sha256(p.read_bytes()).hexdigest() for p in sorted(baseline.iterdir()) if p.is_file()},
                method_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
    finally:
        sys.setprofile(None)
    (output / "results.json").write_text(json.dumps(summary,indent=2)+"\n")
    print(json.dumps({k:v for k,v in summary.items() if k not in {"original_response_sha256","answers","adapter_limitations"}}))


if __name__ == "__main__":
    main()
