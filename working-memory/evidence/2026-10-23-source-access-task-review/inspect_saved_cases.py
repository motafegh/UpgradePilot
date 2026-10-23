"""Read-only mechanical basis for an exposed maintainer-task development review.

Run from repo root with PYTHONPATH=src:. and the project interpreter. Review-specific
needles locate already exposed passages, not semantic classification or a product rule.
No investigation, acquisition, evaluator, model, source refresh or target execution runs.
"""

from contextlib import ExitStack, redirect_stdout
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
from unittest.mock import patch

from upgradepilot.cli import main
from upgradepilot.report import render_investigation_report, render_report_source
from upgradepilot.report_file import read_report


ROOT = Path("working-memory/evidence")
BUILD = ROOT / "2026-10-23-pr-description-build"
NEEDLES = {
    "httpx": {"app_mentions": "<code>app</code>", "proxies_mentions": "<code>proxies</code>",
              "cert_mentions": "<code>cert</code>", "verify_mentions": "<code>verify</code>"},
    "opencv": {"release_heading": "<h2>4.7.0.68</h2>",
               "support_statement": "Dropped Python 3.6 support.", "truncation_marker": "... (truncated)"},
}


def digest(data):
    return sha256(data).hexdigest()


def passages(text, needle):
    rows = []
    start = text.find(needle)
    while start >= 0:
        end = start + len(needle)
        rows.append({"codepoint_start": start, "codepoint_end": end,
                     "decoded_body_line": text.count("\n", 0, start) + 1,
                     "span_sha256": digest(text[start:end].encode("utf-8"))})
        start = text.find(needle, end)
    assert rows, "Previously exposed source passage unavailable"
    return rows


def inspect():
    build = json.loads((BUILD / "retained-case-receipt.json").read_text())
    result = {"mode": "exposed_implementer_development_review", "source_revision": "9f362d1f",
              "new_acquisition_inference_target_execution": False, "cases": {}}
    denied = []

    def deny(*args, **kwargs):
        denied.append(True)
        raise AssertionError("Offline review attempted forbidden work")

    with ExitStack() as stack:
        for target in ("socket.socket.connect", "requests.sessions.Session.request",
                       "upgradepilot.cli.investigate_public_pull_request", "upgradepilot.cli.os.getenv",
                       "upgradepilot.cli.save_report", "upgradepilot.report_projection.synthesize_maintainer_action",
                       "upgradepilot.upstream.support_drop.evaluate_support_drop_runtime"):
            stack.enter_context(patch(target, deny))
        for name, case in build["cases"].items():
            original_root = Path(case["source_packet"])
            private_original = Path(json.loads((original_root / "freeze.json").read_text())["private_output"])
            index_path = original_root / "source-index.json"
            rows = json.loads(index_path.read_text())["requests"]
            frozen_paths = [original_root / "report.json", private_original / "report.json", index_path]
            frozen_paths += [private_original / "sources" / row["body"] for row in rows]
            before = {str(path): digest(path.read_bytes()) for path in frozen_paths}
            for row in rows:
                assert before[str(private_original / "sources" / row["body"])] == row["body_sha256"]
            old = read_report(original_root / "report.json")
            assert old == read_report(private_original / "report.json")
            saved = Path(case["private_output"]) / "report.json"
            saved_before = saved.read_bytes()
            assert digest(saved_before) == case["new_report_sha256"]
            assert before[str(original_root / "report.json")] == case["original_report_sha256"]
            current = read_report(saved)
            source = next(s for s in current.sources if s.kind == "pull_request")
            old_source = next(s for s in old.sources if s.kind == "pull_request")
            raw = (private_original / "sources" / rows[0]["body"]).read_bytes()
            assert digest(raw) == case["original_pr_response_sha256"]
            body = json.loads(raw)["body"]
            assert source.content == body
            assert digest(body.encode("utf-8")) == case["description_sha256"]
            assert old_source.content is None and old_source.retention == "reference_only"
            parity = all(getattr(old, k) == getattr(current, k)
                         for k in ("identity", "assessments", "findings", "unknowns", "action"))
            assert parity
            summary = render_investigation_report(current, saved=True)
            view = render_report_source(current, source.source_id)
            assert digest(view.encode("utf-8")) == case["new_view_sha256"]
            assert body not in summary
            assert "--show-source SOURCE_ID" in summary
            assert source.source_id in summary
            for args, expected in ((["--open-report", str(saved)], summary),
                                   (["--open-report", str(saved), "--show-source", source.source_id], view)):
                output = StringIO()
                with redirect_stdout(output):
                    assert main(args) == 0
                assert output.getvalue() == expected + "\n"
            assert "unverified" in view and "coverage is unassessed" in view
            assert "BEGIN LITERAL SOURCE TEXT" in view
            locations = {key: passages(body, needle) for key, needle in NEEDLES[name].items()}
            for key, needle in NEEDLES[name].items():
                for located in locations[key]:
                    assert needle in view
            assert before == {str(path): digest(path.read_bytes()) for path in frozen_paths}
            assert saved.read_bytes() == saved_before
            result["cases"][name] = {
                "report_id": current.report_id, "report_sha256": digest(saved_before),
                "original_report_sha256": case["original_report_sha256"],
                "original_pr_response_sha256": digest(raw), "source_index_sha256": before[str(index_path)],
                "frozen_http_observations_verified": len(rows),
                "complete_bodies": sum(row["state"] == "body_complete" for row in rows),
                "unconsumed_status_only_bodies": sum(row["state"] == "body_not_consumed" for row in rows),
                "source_id": source.source_id, "description_utf8_bytes": len(body.encode("utf-8")),
                "description_sha256": digest(body.encode("utf-8")), "observed_at": source.retrieved_at,
                "old_retention": old_source.retention, "new_retention": source.retention,
                "recorded_generator": current.generator_version,
                "saved_summary_lines": len(summary.splitlines()), "source_view_lines": len(view.splitlines()),
                "saved_summary_words": len(summary.split()), "unknowns": len(current.unknowns),
                "source_view_sha256": digest(view.encode("utf-8")),
                "review_passage_locations": locations,
                "cli_summary_and_source_exit_codes": [0, 0], "identity_domain_action_parity": parity,
                "input_and_output_files_unchanged": True,
                "task_benefit_or_time_saving_measured": False,
            }
    assert not denied
    result["forbidden_work_attempts"] = len(denied)
    return result


if __name__ == "__main__":
    print(json.dumps(inspect(), indent=2))
