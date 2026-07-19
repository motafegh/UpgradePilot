from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
from dataclasses import replace
from io import StringIO
import json
from pathlib import Path
import tempfile
import unittest

from upgradepilot.cli import main
from upgradepilot.adapters.json_input import load_analysis_input
from upgradepilot.adapters.report_files import render_markdown
from upgradepilot.application.analyze import analyze


EXAMPLE_PATH = (
    Path(__file__).resolve().parents[1] / "examples" / "pydantic-13432.bootstrap.json"
)


class CliTests(unittest.TestCase):
    def test_validate_reports_case_identity(self) -> None:
        output = StringIO()

        with redirect_stdout(output):
            result = main(["validate", str(EXAMPLE_PATH)])

        self.assertEqual(result, 0)
        self.assertIn("pydantic/pydantic#13432", output.getvalue())

    def test_analyze_writes_json_and_markdown_reports(self) -> None:
        output = StringIO()
        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory)
            with redirect_stdout(output):
                result = main(
                    ["analyze", str(EXAMPLE_PATH), "--output-dir", str(output_dir)]
                )

            self.assertEqual(result, 0)
            json_path = output_dir / "pydantic-pydantic-pr-13432.report.json"
            markdown_path = output_dir / "pydantic-pydantic-pr-13432.report.md"
            self.assertTrue(json_path.is_file())
            self.assertTrue(markdown_path.is_file())

            report = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(report["action"], "run_targeted_checks")
            self.assertEqual(report["policy_version"], "bootstrap-1")
            self.assertIn("does not prove compatibility", report["claim_boundary"])
            self.assertIn("## Claim boundary", markdown_path.read_text(encoding="utf-8"))
            self.assertIn("Action: run_targeted_checks", output.getvalue())

    def test_invalid_input_returns_two_without_traceback(self) -> None:
        error = StringIO()
        with tempfile.TemporaryDirectory() as directory:
            invalid_path = Path(directory) / "invalid.json"
            invalid_path.write_text("{not json}", encoding="utf-8")

            with redirect_stderr(error):
                result = main(["validate", str(invalid_path)])

        self.assertEqual(result, 2)
        self.assertIn("invalid JSON", error.getvalue())

    def test_markdown_renderer_flattens_untrusted_heading_injection(self) -> None:
        analysis_input = load_analysis_input(EXAMPLE_PATH)
        report = analyze(analysis_input)
        injected_evidence = replace(
            report.evidence[0],
            claim="Original claim\n# injected heading",
        )
        report = replace(report, evidence=(injected_evidence, *report.evidence[1:]))
        rendered = render_markdown(report)

        self.assertNotIn("\n# injected", rendered)
        self.assertIn("Original claim \\# injected heading", rendered)


if __name__ == "__main__":
    unittest.main()
