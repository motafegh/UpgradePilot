"""Offline proof for the public-CLI subprocess deadline and private receipt."""

from __future__ import annotations

import json
import os
import stat
import sys
import tempfile
import time
import unittest
from pathlib import Path

from tools.run_qualification_cli import supervise


class QualificationSupervisorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="upgradepilot-supervision-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def _fake_cli(self, code: str) -> Path:
        path = self.root / "fake-upgradepilot"
        path.write_text(f"#!{sys.executable}\n" + code, encoding="utf-8")
        path.chmod(0o700)
        return path

    def _read_receipt(self, output: Path) -> dict:
        return json.loads((output / "execution-receipt.json").read_text())

    def test_actual_cli_stdout_stderr_exit_and_report_hash(self) -> None:
        cli = self._fake_cli(
            "import pathlib,sys\n"
            "print('visible stdout')\n"
            "print('visible stderr',file=sys.stderr)\n"
            "args=sys.argv[1:]\n"
            "path=pathlib.Path(args[args.index('--save-report')+1])\n"
            "path.write_bytes(b'{\\\"ok\\\":true}')\n"
            "raise SystemExit(7)\n"
        )
        out = self.root / "result"
        report = out / "report.json"
        code = supervise(
            cli=cli,
            output=out,
            deadline_seconds=2,
            arguments=["--save-report", str(report)],
        )
        self.assertEqual(code, 7)
        data = self._read_receipt(out)
        self.assertEqual(data["exit_code"], 7)
        self.assertEqual(data["status"], "completed")
        self.assertEqual(data["report"]["bytes"], len(report.read_bytes()))
        self.assertEqual(len(data["report"]["sha256"]), 64)
        self.assertFalse(data["http_requests_measured"])
        self.assertFalse(data["model_dispatch_measured"])
        self.assertIn("visible stdout", (out / "stdout.txt").read_text())
        self.assertIn("visible stderr", (out / "stderr.txt").read_text())
        self.assertEqual(stat.S_IMODE(out.stat().st_mode), 0o700)
        for name in ("stdout.txt", "stderr.txt", "execution-receipt.json"):
            self.assertEqual(stat.S_IMODE((out / name).stat().st_mode), 0o600)

    def test_parent_deadline_terminates_stalled_cli(self) -> None:
        cli = self._fake_cli("import time\ntime.sleep(20)\n")
        out = self.root / "timeout"
        start = time.time()
        code = supervise(cli=cli, output=out, deadline_seconds=0.3, arguments=[])
        elapsed = time.time() - start
        self.assertEqual(code, 124)
        self.assertEqual(self._read_receipt(out)["status"], "deadline_exceeded")
        self.assertLess(elapsed, 5)

    def test_existing_output_directory_refused_before_execution(self) -> None:
        cli = self._fake_cli("print('should not execute')\n")
        out = self.root / "existing"
        out.mkdir()
        marker = out / "keep.txt"
        marker.write_text("unchanged")
        with self.assertRaises(FileExistsError):
            supervise(cli=cli, output=out, deadline_seconds=2, arguments=[])
        self.assertEqual(marker.read_text(), "unchanged")
        self.assertFalse((out / "stdout.txt").exists())

    def test_nonexistent_cli_refused_without_new_directory(self) -> None:
        out = self.root / "nonexistent"
        with self.assertRaises(ValueError):
            supervise(
                cli=self.root / "missing-upgradepilot",
                output=out,
                deadline_seconds=2,
                arguments=[],
            )
        self.assertFalse(out.exists())

    def test_invalid_deadline_refused_without_new_directory(self) -> None:
        cli = self._fake_cli("print('should not execute')\n")
        out = self.root / "bad-deadline"
        with self.assertRaises(ValueError):
            supervise(cli=cli, output=out, deadline_seconds=0, arguments=[])
        self.assertFalse(out.exists())


    def test_nonprivate_output_parent_refused(self) -> None:
        cli = self._fake_cli("print('should not execute')\n")
        public_parent = self.root / "group-readable"
        public_parent.mkdir()
        public_parent.chmod(0o755)
        with self.assertRaises(ValueError):
            supervise(
                cli=cli,
                output=public_parent / "result",
                deadline_seconds=2,
                arguments=[],
            )
        self.assertFalse((public_parent / "result").exists())

    def test_deadline_kills_descendant_ignoring_sigterm_after_leader_exits(self) -> None:
        """The old leader-only wait returned while the stubborn child survived."""

        ready = self.root / "handler-ready"
        marker = self.root / "unexpected-stubborn-child-alive"
        child_code = (
            "import pathlib,signal,time;"
            "signal.signal(signal.SIGTERM,signal.SIG_IGN);"
            f"pathlib.Path({str(ready)!r}).write_text('ready');"
            "time.sleep(1.4);"
            f"pathlib.Path({str(marker)!r}).write_text('escaped')"
        )
        parent_code = (
            "import pathlib,subprocess,sys,time\n"
            f"subprocess.Popen([sys.executable, '-c', {child_code!r}])\n"
            f"ready=pathlib.Path({str(ready)!r})\n"
            "while not ready.exists(): time.sleep(0.01)\n"
            "time.sleep(20)\n"
        )
        cli = self._fake_cli(parent_code)
        output = self.root / "stubborn-descendant"
        self.assertEqual(
            supervise(cli=cli, output=output, deadline_seconds=0.35, arguments=[]),
            124,
        )
        self.assertTrue(ready.exists(), "The child must install its SIGTERM handler")
        self.assertEqual(self._read_receipt(output)["status"], "deadline_exceeded")
        time.sleep(1.45)
        self.assertFalse(marker.exists(), "A signal-ignoring descendant survived the timeout")

    def test_deadline_terminates_process_descendants(self) -> None:
        marker = self.root / "unexpected-child-file"
        child_code = (
            "import pathlib,time;"
            "time.sleep(0.7);"
            f"pathlib.Path({str(marker)!r}).write_text('alive')"
        )
        cli = self._fake_cli(
            "import subprocess,sys,time\n"
            f"subprocess.Popen([sys.executable, '-c', {child_code!r}])\n"
            "time.sleep(20)\n"
        )
        out = self.root / "children"
        self.assertEqual(
            supervise(cli=cli, output=out, deadline_seconds=0.25, arguments=[]),
            124,
        )
        time.sleep(0.85)
        self.assertFalse(marker.exists())


if __name__ == "__main__":
    unittest.main()
