"""Fresh installed reader checks actual deliveries, never supplies missing pages."""
import ast
from hashlib import sha256
import json
import os
from pathlib import Path
import socket
import sys
from unittest.mock import patch

from upgradepilot.caller_signature_delivery import open_caller_signature_checkpoint
from upgradepilot.caller_signature.worker import run_source_analysis
from upgradepilot.caller_signature.analysis import compare_arguments
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.lifecycle_records import decode_lifecycle_value

BLOCKED = {"acquire_dependency_inputs", "collect_source_progress", "run_source_analysis",
    "produce_source_analysis", "discover_source_candidates", "compare_arguments",
    "extract_python_source", "analyze_python_bindings", "synthesize_maintainer_action",
    "project_caller_signature_report", "project_investigation_report"}


def guard(frame, event, arg):
    if event == "call":
        module, name = frame.f_globals.get("__name__", ""), frame.f_code.co_name
        if ((module.startswith("upgradepilot.") and name in BLOCKED)
                or (module == "ast" and name == "parse") or (module == "os" and name == "getenv")):
            raise AssertionError("forbidden cold operation " + module + "." + name)


if __name__ == "__main__":
    expected = json.loads(Path(sys.argv[3]).read_bytes())
    # A hook exception disarms profiling; rearm between discriminating controls.
    for forbidden in (lambda: ast.parse("pass"), lambda: os.getenv("GITHUB_TOKEN"),
                      lambda: run_source_analysis(None), lambda: compare_arguments(None, None, None)):
        sys.setprofile(guard)
        try:
            forbidden()
        except AssertionError as error:
            assert str(error).startswith("forbidden cold operation "), error
        else:
            raise AssertionError("inactive cold guard")
    sys.setprofile(guard)
    with patch.object(socket.socket, "connect", side_effect=AssertionError("cold network forbidden")):
        opened = open_caller_signature_checkpoint(CheckpointStore.open(Path(sys.argv[1]), read_only=True), sys.argv[2])
        records = {r.record_id: r for r in opened.selected.revision.lifecycle_history.records}
        chunks, views, bases = [], set(), set()
        for row in expected["pages"]:
            record = records[row["delivery_id"]]
            delivery = decode_lifecycle_value(record.kind, record.codec_version, record.payload)
            content = delivery.retained_content.encode()
            assert sha256(content).hexdigest() == row["sha256"]
            assert len(content) == row["bytes"]
            chunks.append(json.loads(content)["text"])
            views.add(delivery.view_id)
            bases.add(record.basis_revision_id)
        assert len(chunks) == len({r["delivery_id"] for r in expected["pages"]}) == 60
        assert len(views) == len(bases) == 1
        assert sha256("".join(chunks).encode()).hexdigest() == expected["prefix_sha256"]
        assert opened.selected.revision.digest() == expected["checkpoint_digest"]
        assert opened.report is not None
    sys.setprofile(None)
    print(json.dumps(dict(outcome="passed", pages=60, exact_pages_and_prefix=True,
                         unique_views=len(views), unique_bases=len(bases), guards_discriminated=True)))
