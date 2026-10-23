"""Finite controlled composition from two frozen HTTP packets; no live acquisition.

Run with PYTHONPATH=src:. and the project interpreter. Private original inputs are required;
there is no fetch fallback. Full new report/view output remains private; stdout is a safe
receipt. This is not a general replay mechanism or a new official capture.
"""

from contextlib import ExitStack, redirect_stdout
from datetime import UTC, datetime
from hashlib import sha256
from io import BytesIO, StringIO
import json
import os
from pathlib import Path
from unittest.mock import patch

from requests import Response
from requests.adapters import HTTPAdapter

from upgradepilot.cli import main
from upgradepilot.investigation import investigate_public_pull_request
from upgradepilot.report import render_investigation_report, render_report_source
from upgradepilot.report_file import read_report, save_report
from upgradepilot.report_projection import project_investigation_report
from upgradepilot.workspace.native_boundary import encode_native_boundary


class UnretainedBody:
    def read(self, *args, **kwargs):
        raise AssertionError("Historical status-only response has no retained server body")

    def close(self):
        pass


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def verify(name, slug, output_root):
    public = Path("working-memory/evidence") / ("2026-10-22-" + slug)
    private = Path(json.loads((public / "freeze.json").read_text())["private_output"])
    rows = json.loads((public / "source-index.json").read_text())["requests"]
    paths = [public / "report.json", private / "report.json"]
    paths += [private / "sources" / row["body"] for row in rows]
    before = {str(path): digest(path) for path in paths}
    for row in rows:
        assert digest(private / "sources" / row["body"]) == row["body_sha256"]
    original = read_report(public / "report.json")
    assert original == read_report(private / "report.json")
    initial = json.loads((private / "sources" / rows[0]["body"]).read_bytes())
    description = initial["body"]
    pending = iter(rows)
    consumed = []

    def send(adapter, request, **kwargs):
        row = next(pending)
        assert request.method == row["method"] == "GET"
        assert request.url == row["url"]
        assert "Authorization" not in request.headers
        consumed.append(row["number"])
        response = Response()
        response.request = request
        response.url = row["response_url"]
        response.status_code = row["status"]
        response.headers.update(row["headers"])
        # These files contain decoded entity bytes, not compressed wire bytes. BytesIO
        # deliberately has no urllib3 stream/decompression layer. Status-only cases must
        # remain unreadable: an empty retained prefix is not a fabricated empty server body.
        response.raw = (BytesIO((private / "sources" / row["body"]).read_bytes())
                        if row["state"] == "body_complete" else UnretainedBody())
        return response

    with ExitStack() as stack:
        stack.enter_context(patch.object(HTTPAdapter, "send", send))
        for target in ("socket.socket.connect", "upgradepilot.upstream.support_drop.evaluate_support_drop_runtime",
                       "upgradepilot.investigation.evaluate_support_drop_runtime"):
            stack.enter_context(patch(target, side_effect=AssertionError(target)))
        stack.enter_context(patch.dict(os.environ, {"NETRC": os.devnull}))
        identity = {fact.name: fact.value for fact in original.identity}
        # Identity comes from the frozen report; all actual provider/domain records below
        # are newly produced from controlled responses, never replaced with old findings.
        repository = identity["repository"]
        pull_number = initial["number"]
        result = investigate_public_pull_request(repository, pull_number)
        report = project_investigation_report(result)
    assert consumed == [row["number"] for row in rows]
    assert next(pending, None) is None
    assert report.identity == original.identity
    for field in ("assessments", "findings", "unknowns", "action"):
        assert getattr(report, field) == getattr(original, field), field
    source = next(s for s in report.sources if s.kind == "pull_request")
    assert source.content == description
    assert source.retrieved_at != rows[0]["finished_at"]  # new controlled observation time
    assert description not in render_investigation_report(report)
    case_out = output_root / name
    case_out.mkdir(mode=0o700)
    save_report(report, case_out / "report.json")
    opened = read_report(case_out / "report.json")
    assert opened == report
    view = render_report_source(opened, source.source_id)
    with patch("socket.socket.connect", side_effect=AssertionError("network")), patch(
        "upgradepilot.cli.investigate_public_pull_request", side_effect=AssertionError("acquisition")
    ):
        output = StringIO()
        with redirect_stdout(output):
            assert main(["--open-report", str(case_out / "report.json"), "--show-source", source.source_id]) == 0
        assert output.getvalue() == view + "\n"
    for filename, payload in (("source-view.txt", view.encode()),
                              ("native.json", encode_native_boundary(result.workspace_revision.boundary))):
        descriptor = os.open(case_out / filename, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(payload)
    assert before == {str(path): digest(path) for path in paths}
    return {
        "mode": "controlled_normal_composition_from_frozen_responses",
        "source_packet": str(public), "private_output": str(case_out),
        "original_report_sha256": digest(public / "report.json"),
        "original_pr_response_sha256": rows[0]["body_sha256"],
        "description_utf8_bytes": len(description.encode("utf-8")),
        "description_sha256": sha256(description.encode("utf-8")).hexdigest(),
        "new_report_id": report.report_id,
        "new_observed_at": source.retrieved_at,
        "historical_response_completed_at": rows[0]["finished_at"],
        "request_count": len(consumed), "added_requests": 0,
        "domain_findings_unknowns_action_unchanged": True,
        "source_save_open_view_exact": True, "original_inputs_reports_unchanged": True,
        "new_report_sha256": digest(case_out / "report.json"),
        "new_view_sha256": digest(case_out / "source-view.txt"),
    }


if __name__ == "__main__":
    root = Path.home() / ".local/share/upgradepilot/pr-description-build"
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    output_root = root / datetime.now(UTC).strftime("controlled-%Y%m%dT%H%M%S%fZ")
    output_root.mkdir(mode=0o700)
    cases = {}
    for name, slug in (("httpx", "matched-report-source-capture"), ("opencv", "opencv-matched-report-source-capture")):
        cases[name] = verify(name, slug, output_root)
    print(json.dumps({"cases": cases, "live_network_model_target_execution": False,
                      "not_established": ["semantic correctness", "independent usefulness", "general replay"]}, indent=2))
