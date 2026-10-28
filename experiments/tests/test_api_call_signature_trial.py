"""Curated composition, immutable attempts and cold offline source inspection."""

import ast
import hashlib
import json
import os
import subprocess
import sys
from contextlib import redirect_stdout
from dataclasses import asdict
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import patch

from experiments.api_call_signature import SourceSpan
from experiments.api_call_signature_trial import (
    AnalysisLimits, SELECTION_FORMAT, open_comparison, prepare_comparison,
    main, read_comparison, render_comparison, render_source, run_comparison,
)
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
from upgradepilot.workspace.native_representation import json_bytes
from upgradepilot.workspace.source_access import (
    RetainedSourceCatalog, RetainedSourceFile, RetainedSourceScope, encode_source_catalog,
)

TARGET = ExactInvestigationTarget("owner/project", 7, "b" * 40, "a" * 40, "vendor", "1", "2")


def inputs(*, callee="def send(*, deadline=None):\n pass\n", caller="from vendor import send\nsend(timeout=1)\n"):
    files = (RetainedSourceFile("project", "caller.py", caller),
             RetainedSourceFile("project", "receiver.py", callee))
    catalog = RetainedSourceCatalog((RetainedSourceScope(
        "project", TARGET.repository, TARGET.head_sha, "repository_text",
        "locally authored controls", "complete selected files; no runtime claim",
    ),), files, target=TARGET)
    call = next(n for n in ast.walk(ast.parse(caller)) if isinstance(n, ast.Call))
    signature = next(n for n in ast.walk(ast.parse(callee)) if isinstance(n, ast.FunctionDef))
    selections = {
        "format": SELECTION_FORMAT, "target": asdict(TARGET),
        "files": [{"source_id": f.source_id, "path": f.path,
                   "content_sha256": hashlib.sha256(f.content.encode()).hexdigest(),
                   "coverage": "complete_file"} for f in files],
        "pairs": [{"id": "controlled-interaction", "receiver_mode": "as_written",
                   "caller": {"source_id": "project", "path": "caller.py", "span": asdict(SourceSpan.of(call))},
                   "callee": {"source_id": "project", "path": "receiver.py", "span": asdict(SourceSpan.of(signature))}}],
    }
    return encode_source_catalog(catalog), json_bytes(selections)


class RetainedCompositionTests(TestCase):
    def test_complete_comparison_round_trip_preserves_conditional_claim(self):
        result, companion = prepare_comparison(*inputs(), AnalysisLimits())
        body, catalog = read_comparison(result, companion)
        compared = body["pairs"][0]["comparison"]
        self.assertEqual(compared["outcome"], "rejected")
        self.assertEqual(compared["violations"][0]["parameter"], "timeout")
        self.assertEqual(len(catalog.files), 2)
        view = render_comparison(body)
        self.assertIn("retained_curated_source_comparison", view)
        self.assertIn("call_reaches_selected_declared_signature", view)
        self.assertIn("Keyword timeout: not_received", view)
        self.assertIn("Next evidence: establish whether send reaches send in owner/project@", view)

    def test_selection_cannot_supply_expected_answer_or_upgrade_wrong_target(self):
        source, selections = inputs()
        raw = json.loads(selections)
        raw["pairs"][0]["expected_result"] = "rejected"
        with self.assertRaises(ValueError):
            prepare_comparison(source, json_bytes(raw), AnalysisLimits())
        raw = json.loads(selections)
        raw["target"]["head_sha"] = "c" * 40
        with self.assertRaises(ValueError):
            prepare_comparison(source, json_bytes(raw), AnalysisLimits())

    def test_missing_selector_is_a_visible_problem_not_an_empty_positive(self):
        source, selections = inputs()
        raw = json.loads(selections)
        raw["pairs"][0]["caller"]["span"]["column"] = 1
        result, companion = prepare_comparison(source, json_bytes(raw), AnalysisLimits())
        body, _ = read_comparison(result, companion)
        self.assertIsNone(body["pairs"][0]["comparison"])
        self.assertEqual(body["pairs"][0]["problem"], "selected_call_or_signature_unavailable")

    def test_limited_signature_does_not_make_an_absence_claim(self):
        source, selections = inputs()
        raw = json.loads(selections)
        raw["files"][1]["coverage"] = "limited"
        result, companion = prepare_comparison(source, json_bytes(raw), AnalysisLimits())
        body, _ = read_comparison(result, companion)
        self.assertEqual(body["pairs"][0]["comparison"]["outcome"], "undetermined")

    def test_saved_identity_version_span_and_reference_corruption_are_refused(self):
        result, companion = prepare_comparison(*inputs(), AnalysisLimits())
        mutations = [
            lambda d: d.update(method_version=999),
            lambda d: d.update(companion_sha256="0" * 64),
            lambda d: d["target"].update(head_sha="c" * 40),
            lambda d: d["files"][0]["facts"]["calls"][0]["span"].update(end_column=9999),
            lambda d: d["pairs"][0]["comparison"].update(call_id="0" * 64),
            lambda d: d["pairs"][0]["comparison"].update(remaining_premises=[]),
            lambda d: d["pairs"][0]["comparison"].update(outcome="bound", violations=[]),
            lambda d: d.update(companion_path="/etc/passwd"),
        ]
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                raw = json.loads(result)
                mutate(raw)
                with self.assertRaises(ValueError):
                    read_comparison(json_bytes(raw), companion)
        with self.assertRaises(ValueError):
            read_comparison(result, companion + b" ")

    def test_source_view_uses_physical_lines_and_sanitizes_controls_only_on_display(self):
        source, selections = inputs(caller="from vendor import send\nnote='a\u2028b' # \x1b[31m\nsend(timeout=1)\n")
        result, companion = prepare_comparison(source, selections, AnalysisLimits())
        body, catalog = read_comparison(result, companion)
        unit = next(u for u in body["files"] if u["descriptor"]["path"] == "caller.py")
        view = render_source(catalog, unit["descriptor"]["file_id"], 3, 1)
        self.assertIn("3: send(timeout=1)", view)
        self.assertNotIn("\x1b", render_source(catalog, unit["descriptor"]["file_id"], 1, 4))
        self.assertIn("\x1b", next(f.content for f in catalog.files if f.path == "caller.py"))

    def test_selected_file_byte_node_fact_and_pair_caps_are_real_limits(self):
        for limits in [AnalysisLimits(max_files=1), AnalysisLimits(max_source_bytes=1),
                       AnalysisLimits(max_nodes_per_file=1), AnalysisLimits(max_facts=1)]:
            with self.subTest(limits=limits):
                with self.assertRaises(ValueError):
                    prepare_comparison(*inputs(), limits)
        source, selections = inputs()
        raw = json.loads(selections)
        second = dict(raw["pairs"][0], id="another")
        raw["pairs"].append(second)
        with self.assertRaises(ValueError):
            prepare_comparison(source, json_bytes(raw), AnalysisLimits(max_pairs=1))
        with self.assertRaises(ValueError):
            AnalysisLimits(timeout_seconds=61)
        with self.assertRaises(ValueError):
            AnalysisLimits(max_files=10 ** 1000)

    def test_exact_work_limits_pass_and_serialized_output_limit_refuses(self):
        result, companion = prepare_comparison(*inputs(), AnalysisLimits())
        body, _ = read_comparison(result, companion)
        limits = AnalysisLimits(max_files=body["work"]["source_files"],
                                max_source_bytes=body["work"]["source_bytes"],
                                max_nodes=body["work"]["ast_nodes"],
                                max_facts=body["work"]["facts"], max_pairs=1)
        prepare_comparison(*inputs(), limits)
        with patch("experiments.api_call_signature_trial.MAX_OUTPUT_BYTES", min(len(result), len(companion)) - 1):
            with self.assertRaises(ValueError):
                prepare_comparison(*inputs(), AnalysisLimits())
            with self.assertRaises(ValueError):
                read_comparison(result, companion)


class AttemptAndReopenTests(TestCase):
    def setUp(self):
        self.temporary = TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        source, selections = inputs()
        self.source, self.selections = self.root / "profile.json", self.root / "selections.json"
        self.source.write_bytes(source)
        self.selections.write_bytes(selections)

    def test_bounded_worker_completion_and_cold_open_do_not_reanalyze_or_use_network(self):
        directory = self.root / "run"
        attempt = run_comparison(self.source, self.selections, directory)
        self.assertEqual(attempt["state"], "completed", attempt)
        with patch("experiments.api_call_signature_trial.extract_python_source", side_effect=AssertionError("reanalysis")), patch("socket.socket", side_effect=AssertionError("network")):
            body, catalog = open_comparison(directory)
            self.assertEqual(body["pairs"][0]["comparison"]["outcome"], "rejected")
        cold = subprocess.run([sys.executable, "-m", "experiments.api_call_signature_trial", "open", "--result", str(directory)], capture_output=True, text=True, check=False)
        self.assertEqual(cold.returncode, 0, cold.stderr)
        self.assertIn("Keyword timeout: not_received", cold.stdout)
        unit_id = catalog.descriptor(catalog.files[0])["file_id"]
        source_view = subprocess.run([sys.executable, "-m", "experiments.api_call_signature_trial", "open", "--result", str(directory), "--source", unit_id], capture_output=True, text=True, check=False)
        self.assertEqual(source_view.returncode, 0, source_view.stderr)
        self.assertIn("LITERAL RETAINED SOURCE", source_view.stdout)
        self.assertEqual(os.stat(directory).st_mode & 0o777, 0o700)
        self.assertEqual(os.stat(directory / "sources.json").st_mode & 0o777, 0o600)

    def test_attempt_is_immutable_and_corrupt_companions_or_outputs_cannot_reopen(self):
        directory = self.root / "run"
        self.assertEqual(run_comparison(self.source, self.selections, directory)["state"], "completed")
        original = (directory / "attempt.json").read_bytes()
        with self.assertRaises(FileExistsError):
            run_comparison(self.source, self.selections, directory)
        self.assertEqual((directory / "attempt.json").read_bytes(), original)
        (directory / "sources.json").write_bytes(b"{}")
        with self.assertRaises(ValueError):
            open_comparison(directory)

    def test_deadline_failure_and_unattempted_work_are_preserved_without_completion(self):
        timeout = self.root / "timeout"
        attempt = run_comparison(self.source, self.selections, timeout,
                                 limits=AnalysisLimits(timeout_seconds=0.000001))
        self.assertEqual(attempt["state"], "timed_out")
        self.assertTrue((timeout / "attempt.json").exists())
        self.assertFalse((timeout / "result.json").exists())
        with self.assertRaises(ValueError):
            open_comparison(timeout)
        refused = self.root / "refused"
        attempt = run_comparison(self.source, self.selections, refused, limits=AnalysisLimits(max_files=1))
        self.assertEqual(attempt["state"], "failed")
        self.assertIn("selected_file_limit", attempt["reason"])
        self.assertFalse((refused / "result.json").exists())

    def test_worker_failure_and_missing_input_are_explicit_attempts(self):
        directory = self.root / "missing"
        attempt = run_comparison(self.root / "absent", self.selections, directory)
        self.assertEqual(attempt["state"], "failed")
        self.assertIsNone(attempt["worker_returncode"])
        self.assertTrue((directory / "attempt-started.json").exists())
        directory = self.root / "memory"
        attempt = run_comparison(self.source, self.selections, directory,
                                 limits=AnalysisLimits(memory_bytes=1))
        self.assertEqual(attempt["state"], "failed")
        self.assertFalse((directory / "result.json").exists())

    def test_validation_cannot_admit_a_result_after_the_total_deadline(self):
        directory = self.root / "late"
        result, companion = prepare_comparison(*inputs(), AnalysisLimits())

        def finished_worker(*args, **kwargs):
            (directory / "_worker-result.json").write_bytes(result)
            (directory / "_worker-sources.json").write_bytes(companion)
            return subprocess.CompletedProcess([], 0, b"", b"")

        with patch("experiments.api_call_signature_trial.subprocess.run", side_effect=finished_worker), patch(
            "experiments.api_call_signature_trial.time.monotonic", side_effect=[0, 0, 61, 61]
        ):
            attempt = run_comparison(self.source, self.selections, directory)
        self.assertEqual(attempt["state"], "timed_out")
        self.assertFalse((directory / "result.json").exists())

    def test_compare_cli_preserves_json_line_breaks(self):
        output = StringIO()
        with patch("experiments.api_call_signature_trial.run_comparison", return_value={"state": "completed", "reason": None}), redirect_stdout(output):
            self.assertEqual(main(["compare", "--sources", str(self.source), "--selections", str(self.selections), "--output", str(self.root / "unused")]), 0)
        self.assertIn('\n  "state"', output.getvalue())
        self.assertEqual(json.loads(output.getvalue())["state"], "completed")
