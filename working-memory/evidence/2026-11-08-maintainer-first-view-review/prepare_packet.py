"""Materialize owner-local reviewer views and emit a public-safe receipt."""

import argparse
import hashlib
import json
import os
from pathlib import Path

from upgradepilot.report import render_investigation_report, render_report_source
from upgradepilot.report_file import read_report


HERE = Path(__file__).resolve().parent
EVIDENCE = HERE.parent
TASK = HERE / "REVIEWER_TASK.md"
ALLOCATION = {
    "reviewer-1": (("httpx", "full"), ("opencv", "opening"), ("soup-sieve", "full")),
    "reviewer-2": (("soup-sieve", "opening"), ("opencv", "full"), ("httpx", "opening")),
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def paired_views():
    binding = json.loads((EVIDENCE / "2026-11-07-pypi-route-repair/successor-binding.json").read_bytes())
    cases = {
        "httpx": (Path(binding["destinations"]["product_attempt"]) / "report.json",
                  "ae8bb734d6d2be78a0fc6f248747572cb68238f7ea6b840c0ac6e1e24ef691d1"),
        "opencv": (EVIDENCE / "2026-10-22-opencv-matched-report-source-capture/report.json",
                   "9f6b2d79a08421db5c113a9a0e38d34176728352d8644c52ddc86a2acea88116"),
        "soup-sieve": (EVIDENCE / "2026-10-03-report-model-recovery/rate-limited-investigation-report.json",
                       "19bbe7e31715abd22fb9773f70fe62f270e81496a0c7340be6e7359f325a595a"),
    }
    views = {}
    sources = {}
    receipt = {}
    for name, (path, digest) in cases.items():
        assert sha256(path.read_bytes()) == digest, name
        report = read_report(path)
        with_opening = render_investigation_report(report, saved=True)
        identity, opening, rest = with_opening.partition("\n\nReview at a glance\n")
        summary, details_heading, details = rest.partition("\n\nDetailed evidence and action status")
        assert opening and details_heading and summary and details.startswith("\n\n"), name
        views[name] = {"full": (identity + details + "\n").encode(),
                       "opening": (with_opening + "\n").encode()}
        sources[name] = {source.source_id: (render_report_source(report, source.source_id) + "\n").encode()
                         for source in report.sources if source.retention == "retained_text"}
        receipt[name] = {
            "report_sha256": digest, "report_id": report.report_id,
            "generator_version": report.generator_version,
            "views": {mode: sha256(text) for mode, text in views[name].items()},
            "original_text_views": {source_id: sha256(text) for source_id, text in sources[name].items()},
        }
    return views, sources, receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="new owner-only packet directory")
    args = parser.parse_args()
    views, sources, cases = paired_views()
    task = TASK.read_bytes()
    os.umask(0o077)
    args.output.mkdir(mode=0o700)
    for slot, allocation in ALLOCATION.items():
        reviewer = args.output / slot
        reviewer.mkdir()
        (reviewer / "TASK.md").write_bytes(task)
        for index, (name, mode) in enumerate(allocation, 1):
            case = reviewer / f"{index:02d}-{name}"
            case.mkdir()
            (case / "report.txt").write_bytes(views[name][mode])
            source_dir = case / "sources"
            source_dir.mkdir()
            for source_id, text in sources[name].items():
                (source_dir / f"{source_id}.txt").write_bytes(text)
    print(json.dumps({
        "status": "prepared_local_only", "renderer_version": 3,
        "assembly_sha256": sha256(Path(__file__).read_bytes()),
        "renderer_source_sha256": sha256((EVIDENCE.parents[1] / "src/upgradepilot/report.py").read_bytes()),
        "reviewer_task_sha256": sha256(task), "allocation": ALLOCATION, "cases": cases,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
