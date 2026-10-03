"""Discriminating saved-record validation and atomic non-replacing publication tests."""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from test_cli import _supported_investigation

from upgradepilot.report_file import (
    ReportSaveError,
    ReportValidationError,
    decode_report,
    encode_report,
    read_report,
    save_report,
)
from upgradepilot.report_projection import project_investigation_report


def _signed(data):
    payload = {key: data[key] for key in ("schema", "schema_version", "report")}
    data["integrity"]["digest"] = hashlib.sha256(
        json.dumps(
            payload,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode()
    ).hexdigest()
    return json.dumps(data).encode()


class ReportFileTests(unittest.TestCase):
    def setUp(self):
        self.report = project_investigation_report(_supported_investigation())
        self.data = encode_report(self.report)

    def test_corruption_fails_even_when_json_remains_valid(self):
        data = json.loads(self.data)
        data["report"]["identity"][0]["value"] = "other/project"
        with self.assertRaisesRegex(ReportValidationError, "digest mismatch"):
            decode_report(json.dumps(data).encode())

    def test_resigned_invalid_records_are_rejected_without_authenticity_claim(self):
        mutations = (
            lambda d: d.update(schema_version=2),
            lambda d: d.update(schema_version=True),
            lambda d: d["report"]["assessments"][0].update(source_ids=["missing"]),
            lambda d: d["report"]["sources"][0].update(
                source_id=d["report"]["sources"][1]["source_id"]
            ),
            lambda d: d["report"].pop("unknowns"),
            lambda d: d["report"]["action"].update(state="merge"),
            lambda d: d["report"]["assessments"][0].update(status="not_evaluated"),
            lambda d: d["report"]["assessments"][0].update(state="invented_state"),
            lambda d: d["report"]["findings"][0].update(strength="candidate"),
            lambda d: d["report"]["sources"][0].update(retention="retained_text"),
            lambda d: d["report"].update(generated_at="2026-10-03T00:00:00"),
            lambda d: d["report"].update(findings=[]),
            lambda d: d["report"]["assessments"].pop(0),
        )
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                data = json.loads(self.data)
                mutate(data)
                with self.assertRaises(ReportValidationError):
                    decode_report(_signed(data))

    def test_duplicate_keys_nonfinite_invalid_unicode_and_deep_inputs_fail(self):
        for data in (
            b'{"schema":1,"schema":2}',
            b'{"value":NaN}',
            b'{"value":Infinity}',
            b"\xff",
            b"[" * 25 + b"0" + b"]" * 25,
            b'{"unterminated":',
        ):
            with self.subTest(data=data), self.assertRaises(ReportValidationError):
                decode_report(data)
        with (
            patch("upgradepilot.report_file.MAX_REPORT_BYTES", 10),
            self.assertRaisesRegex(ReportValidationError, "exceeds"),
        ):
            decode_report(self.data)

    def test_valid_publication_has_complete_contents_and_no_temporary_leftovers(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            save_report(self.report, path)
            self.assertEqual(read_report(path), self.report)
            self.assertEqual(list(Path(directory).iterdir()), [path])

    def test_existing_file_and_symlink_are_never_replaced(self):
        with tempfile.TemporaryDirectory() as directory:
            existing = Path(directory) / "existing.json"
            existing.write_text("original")
            link = Path(directory) / "link.json"
            link.symlink_to(existing)
            for path in (existing, link):
                with self.assertRaises(ReportSaveError):
                    save_report(self.report, path)
                self.assertEqual(existing.read_text(), "original")
            self.assertTrue(link.is_symlink())
            self.assertFalse(list(Path(directory).glob(".upgradepilot-report-*")))

    def test_destination_created_during_publication_wins_without_replacement(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "race.json"
            original_link = os.link

            def concurrent_link(source, destination):
                Path(destination).write_text("concurrent writer")
                original_link(source, destination)

            with (
                patch("upgradepilot.report_file.os.link", side_effect=concurrent_link),
                self.assertRaises(ReportSaveError),
            ):
                save_report(self.report, path)
            self.assertEqual(path.read_text(), "concurrent writer")
            self.assertFalse(list(Path(directory).glob(".upgradepilot-report-*")))

    def test_interrupted_prepublication_write_leaves_no_final_or_temporary_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            with (
                patch(
                    "upgradepilot.report_file.os.fsync",
                    side_effect=OSError("interrupted"),
                ),
                self.assertRaises(ReportSaveError),
            ):
                save_report(self.report, path)
            self.assertFalse(path.exists())
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_fifo_is_rejected_without_waiting_for_a_writer(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "pipe"
            os.mkfifo(path)
            with self.assertRaisesRegex(ReportValidationError, "regular file"):
                read_report(path)

    def test_unencodable_source_text_has_a_file_error_not_an_uncaught_traceback(self):
        from dataclasses import replace

        source = replace(
            self.report.sources[0], limitation="unpaired surrogate: \ud800"
        )
        report = replace(self.report, sources=(source,) + self.report.sources[1:])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            with self.assertRaises(ReportSaveError):
                save_report(report, path)
            self.assertFalse(path.exists())

    def test_missing_or_directory_file_has_explicit_read_error(self):
        with tempfile.TemporaryDirectory() as directory:
            for path in (Path(directory), Path(directory) / "absent.json"):
                with self.assertRaisesRegex(ReportValidationError, "Could not read"):
                    read_report(path)
