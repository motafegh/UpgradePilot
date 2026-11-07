"""First task route: literal queries over this live capture's original text only.

No report fields, native comparison offsets or expected witness IDs select reads.
The implementing reviewer is already exposed to this case; this is engineering
evidence, never independent human usefulness. Preserve every bounded response.
"""
import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import socket
import sys
from unittest.mock import patch

from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_projection import reconstruct_caller_signature_projection

HERE = Path(__file__).resolve().parent
PREPARED = HERE.parent / "2026-11-06-native-product-execution-readiness"


def write(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--capture", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    os.umask(0o077)
    args.output.mkdir(mode=0o700, exist_ok=False)
    launch = json.loads((args.capture / "launch-result.json").read_bytes())
    revision = launch["confirmed_revision"]
    write(args.output / "contract.json", dict(method_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        capture=str(args.capture), revision=revision, source_operation_limit=96, source_window_lines=100,
        tokens=["TestClient(app)", "from starlette.testclient import TestClient", "class TestClient(",
            "class Client(", "def __init__(", "super().__init__("],
        route="direct original source first; no report/comparison-driven selection", reviewer_exposed=True,
        consumer_seconds="not measured", retry=False))
    spec = importlib.util.spec_from_file_location("qualified_cold_guard", PREPARED / "cold_review.py")
    cold = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cold)
    sys.setprofile(cold.guard)
    try:
        with patch.object(socket.socket, "connect", side_effect=AssertionError("baseline network forbidden")):
            selected = CheckpointStore.open(args.capture / "store", read_only=True).read_selected_revision(revision)
            boundary = selected.revision.boundary
            # Native fixed reconstruction validates the family graph. Only its
            # original source catalog is used; comparisons are not inspected.
            sources = reconstruct_caller_signature_projection(boundary, expected_target=boundary.target).sources
            catalog = sources.catalog
            operations, windows = [], []
            def query(operation, arguments):
                if len(operations) >= 96:
                    raise RuntimeError("Frozen source-operation allowance exhausted.")
                response = catalog.query(operation, arguments)
                index = len(operations) + 1
                (args.output / f"response-{index:02d}.json").write_bytes(response.content)
                operations.append(dict(index=index, operation=operation, arguments=arguments,
                    bytes=len(response.content), outcome=response.outcome,
                    examined_files=response.examined_files, examined_lines=response.examined_lines))
                write(args.output / "operations.json", operations)
                assert response.outcome != "problem"
                return json.loads(response.content)["payload"]
            scopes = query("list_sources", {})
            target_scopes = [s for s in catalog.scopes if s.repository == boundary.target.repository and s.revision == boundary.target.head_sha]
            for scope in target_scopes:
                query("list_paths", dict(source_id=scope.source_id, offset=0))
            target = next(f for f in catalog.files if f.path == "tests/test_routes.py" and any(s.source_id == f.source_id for s in target_scopes))
            payload = query("read", dict(source_id=target.source_id, path=target.path, start_line=1, line_count=30))
            windows.append(dict(source_id=target.source_id, path=target.path, **payload))
            seen = {(target.source_id, target.path, 1)}
            tokens = json.loads((args.output / "contract.json").read_bytes())["tokens"]
            matches = []
            for token in tokens:
                offset = 0
                while True:
                    payload = query("search", dict(query=token, offset=offset))
                    matches.extend(payload["items"])
                    if payload.get("next_offset") is None:
                        break
                    offset = payload["next_offset"]
            for match in matches:
                key = (match["source_id"], match["path"], max(1, match["line"] - 5))
                if key in seen:
                    continue
                seen.add(key)
                payload = query("read", dict(source_id=key[0], path=key[1], start_line=key[2], line_count=100))
                windows.append(dict(source_id=key[0], path=key[1], **payload))
            write(args.output / "windows.json", windows)
            write(args.output / "identity-and-source-coverage.json", dict(target=vars_target(boundary.target),
                scopes=scopes, capture_state=sources.acquisition.state,
                limitations=sources.acquisition.limitations))
            summary = dict(outcome="baseline_retrieval_complete_not_yet_graded", revision=revision,
                operations=len(operations), delivered_bytes=sum(o["bytes"] for o in operations), windows=len(windows),
                read_operations=sum(o["operation"] == "read" for o in operations),
                native_pages=0, report_reads=0, real_provider_calls=0, consumer_seconds=None,
                reviewer="exposed implementing assistant", grading="Only after direct-source answers are recorded; no baseline extension after grading.")
            write(args.output / "results.json", summary)
            print(json.dumps(summary))
    finally:
        sys.setprofile(None)


def vars_target(target):
    return {name: getattr(target, name) for name in ("repository", "pull_number", "base_sha", "head_sha", "normalized_package", "old_version", "proposed_version")}


if __name__ == "__main__":
    main()
