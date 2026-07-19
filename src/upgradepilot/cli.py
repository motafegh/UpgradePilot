from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import Sequence

from upgradepilot.adapters.json_input import InputError, load_analysis_input
from upgradepilot.adapters.report_files import write_reports
from upgradepilot.application.analyze import analyze


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="upgradepilot",
        description="Produce evidence-backed dependency-update decision reports.",
    )
    subcommands = parser.add_subparsers(dest="command", required=True)

    validate_parser = subcommands.add_parser(
        "validate", help="Validate a JSON evidence package without producing a report."
    )
    validate_parser.add_argument("input", type=Path, help="Path to the JSON evidence package.")

    analyze_parser = subcommands.add_parser(
        "analyze", help="Analyze a JSON evidence package and write JSON and Markdown reports."
    )
    analyze_parser.add_argument("input", type=Path, help="Path to the JSON evidence package.")
    analyze_parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("artifacts"),
        help="Report directory (default: artifacts).",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    arguments = parser.parse_args(argv)

    try:
        analysis_input = load_analysis_input(arguments.input)
        if arguments.command == "validate":
            print(
                "Valid evidence package: "
                f"{analysis_input.case.repository_owner}/"
                f"{analysis_input.case.repository_name}#"
                f"{analysis_input.case.pull_request_number}"
            )
            return 0

        report = analyze(analysis_input)
        json_path, markdown_path = write_reports(report, arguments.output_dir)
        print(f"Action: {report.action.value}")
        print(f"JSON report: {json_path}")
        print(f"Markdown report: {markdown_path}")
        return 0
    except (InputError, OSError, ValueError) as exc:
        print(f"upgradepilot: {exc}", file=sys.stderr)
        return 2
