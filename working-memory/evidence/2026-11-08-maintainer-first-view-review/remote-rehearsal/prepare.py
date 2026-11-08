"""Reconstruct tracked reviewer views with an optional public HTTPX derivative."""

import argparse
import hashlib
import json
import os
from pathlib import Path

from upgradepilot.report import render_investigation_report
from upgradepilot.report_file import read_report


PACKET = Path(__file__).resolve().parent.parent
EVIDENCE = PACKET.parent
REPORTS = {
    "opencv": "2026-10-22-opencv-matched-report-source-capture/report.json",
    "soup-sieve": "2026-10-03-report-model-recovery/rate-limited-investigation-report.json",
}
TOPICS = {
    "opencv": b"Review topic: published artifacts and target applicability\n",
    "soup-sieve": b"Review topic: upstream Python support evidence\n",
}


def require_digest(content: bytes, expected: str, label: str) -> None:
    if hashlib.sha256(content).hexdigest() != expected:
        raise ValueError(f"Frozen receipt hash mismatch for {label}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="new owner-only output directory")
    parser.add_argument(
        "--include-httpx-summary", action="store_true",
        help="include the published HTTPX derivative alongside the two exact cases",
    )
    args = parser.parse_args()

    original = (PACKET / "receipt.json").read_bytes()
    receipt = json.loads(original)
    revision = PACKET / "revision-2"
    updated = json.loads((revision / "receipt.json").read_bytes())
    require_digest(original, updated["original_receipt_sha256"], "original receipt")
    task = (revision / "REVIEWER_TASK.md").read_bytes()
    require_digest(task, updated["reviewer_task_sha256"], "reviewer task")
    views = {}
    topics = TOPICS.copy()
    for case, relative in REPORTS.items():
        saved = EVIDENCE / relative
        binding = receipt["cases"][case]
        require_digest(saved.read_bytes(), binding["report_sha256"], case)
        if binding["original_text_views"]:
            raise ValueError(f"Unexpected retained-text requirements for {case}")
        require_digest(TOPICS[case], updated["focus_sha256"][case], f"{case} topic")
        with_opening = render_investigation_report(read_report(saved), saved=True)
        identity, marker, remainder = with_opening.partition("\n\nReview at a glance\n")
        opening, heading, details = remainder.partition("\n\nDetailed evidence and action status")
        if not (marker and opening and heading and details.startswith("\n\n")):
            raise ValueError(f"Could not locate the frozen opening boundaries for {case}")
        views[case] = {
            "opening": (with_opening + "\n").encode(),
            "full": (identity + details + "\n").encode(),
        }
        for condition, content in views[case].items():
            require_digest(content, binding["views"][condition], f"{case} {condition}")

    if args.include_httpx_summary:
        revision_3 = PACKET / "revision-3"
        revision_3_receipt = json.loads((revision_3 / "receipt.json").read_bytes())
        require_digest(
            (revision / "receipt.json").read_bytes(),
            revision_3_receipt["revision_2_receipt_sha256"], "revision 2 receipt",
        )
        topics["httpx"] = (revision_3 / "HTTPX_FOCUS.txt").read_bytes()
        require_digest(topics["httpx"], revision_3_receipt["httpx_focus_sha256"], "HTTPX topic")
        published = Path(__file__).resolve().parent
        full = (published / "HTTPX_REPORT.md").read_bytes()
        opening = (published / "HTTPX_OPENING.md").read_bytes()
        views["httpx"] = {"full": full, "opening": opening + b"\n" + full}

    os.umask(0o077)
    args.output.mkdir(mode=0o700)
    for slot, assignments in receipt["allocation"].items():
        reviewer = args.output / slot
        reviewer.mkdir()
        (reviewer / "TASK.md").write_bytes(task)
        for index, (case, condition) in enumerate(assignments, 1):
            if case in views:
                folder = reviewer / f"{index:02d}-{case}"
                (folder / "sources").mkdir(parents=True)
                (folder / "report.txt").write_bytes(views[case][condition])
                (folder / "FOCUS.txt").write_bytes(topics[case])


if __name__ == "__main__":
    main()
