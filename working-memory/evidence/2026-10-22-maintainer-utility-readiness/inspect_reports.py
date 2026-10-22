"""One-off offline readiness receipt; no study grading or baseline construction.

Run from the repository root with PYTHONPATH=src and the project Python.
Inputs and expected historical hashes are bound by selection.json before execution.
Existing product decoding and CLI reopening run behind denied network calls.
"""

from collections import Counter
from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import socket
import sys
import time
from unittest.mock import patch

import requests

from upgradepilot.cli import main
from upgradepilot.report import render_investigation_report
from upgradepilot.report_file import decode_report, encode_report, read_report


def digest(data):
    return sha256(data).hexdigest()


def inspect(selection, root):
    attempts = []

    def deny(*args, **kwargs):
        attempts.append("network_attempt_denied")
        raise RuntimeError("This readiness inspection must remain offline")

    rows = []
    started = time.monotonic()
    for item in selection["reports"]:
        path = root / item["path"]
        original = path.read_bytes()
        if digest(original) != item["historical_sha256"]:
            raise ValueError(f"Historical report identity mismatch: {item['label']}")
        with (
            patch.object(requests.sessions.Session, "request", deny),
            patch.object(socket.socket, "connect", deny),
            patch.object(socket.socket, "connect_ex", deny),
            patch.object(socket, "create_connection", deny),
        ):
            report = read_report(path)
            if decode_report(encode_report(report)) != report:
                raise ValueError("Saved report record changed across strict round trip")
            output = StringIO()
            with redirect_stdout(output):
                code = main(["--open-report", str(path)])
            expected_text = render_investigation_report(report, saved=True) + "\n"
            if code != 0 or output.getvalue() != expected_text:
                raise ValueError("Offline CLI reopening differs from the recorded report")
        if path.read_bytes() != original:
            raise ValueError("Original report bytes changed during reopening")
        rows.append({
            **item,
            "report_id": report.report_id,
            "generated_at": report.generated_at,
            "generator_version": report.generator_version,
            "product_version": report.product_version,
            "identity": {f.name: f.value for f in report.identity},
            "dependency": [
                {f.name: f.value for f in a.facts}
                for a in report.assessments if a.assessment_id == "dependency"
            ],
            "assessments": [
                {"id": a.assessment_id, "state": a.state, "reason": a.reason,
                 "strength": a.strength, "sources": a.source_ids}
                for a in report.assessments
            ],
            "source_retention_counts": dict(Counter(s.retention for s in report.sources)),
            "sources": [
                {"id": s.source_id, "kind": s.kind, "retention": s.retention,
                 "locator": s.locator, "method": s.method,
                 "retrieved_at": s.retrieved_at,
                 "identity": {f.name: f.value for f in s.identity},
                 "content_bytes": len(s.content.encode()) if s.content is not None else None,
                 "content_sha256": digest(s.content.encode()) if s.content is not None else None,
                 "limitation": s.limitation}
                for s in report.sources
            ],
            "action": report.action.state,
            "unknown_count": len(report.unknowns),
            "production_limits": report.production_limits,
            "preservation_limits": report.preservation_limits,
            "strict_decode_round_trip": True,
            "offline_cli_exit_code": code,
            "offline_cli_text_sha256": digest(output.getvalue().encode()),
            "offline_cli_matches_saved_record": True,
            "original_bytes_unchanged": True,
        })
    if attempts:
        raise ValueError("A forbidden network operation was attempted")
    return {"purpose": "retained-report readiness, not study results",
            "selection_sha256": digest((root / selection["selection_path"]).read_bytes()),
            "elapsed_seconds": time.monotonic() - started,
            "network_attempts": len(attempts), "reports": rows}


if __name__ == "__main__":
    root = Path.cwd()
    selection_path = Path(sys.argv[1])
    selection = json.loads(selection_path.read_text())
    for item in selection["inspection_sources"]:
        if digest((root / item["path"]).read_bytes()) != item["sha256"]:
            raise ValueError(f"Inspection source drift: {item['path']}")
    result = inspect(selection, root)
    with Path(sys.argv[2]).open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({"reports_reopened": len(result["reports"]),
                      "network_attempts": result["network_attempts"],
                      "elapsed_seconds": result["elapsed_seconds"]}))
