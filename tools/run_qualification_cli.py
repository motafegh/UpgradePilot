"""Supervise one installed UpgradePilot CLI invocation without modifying its behavior.

This is a process deadline and private execution receipt, not an HTTP observer.
Physical request counts, model dispatch and consumed bytes remain unmeasured.
The public CLI and its normal producers execute as installed in the chosen venv.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import signal
import subprocess
import sys
import time
from datetime import UTC, datetime
from pathlib import Path


def _now_utc() -> str:
    return datetime.now(UTC).isoformat()


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def _stop_group(process: subprocess.Popen[bytes]) -> None:
    """Terminate the *entire* dedicated process group, not just its leader.

    The child was started as a new session leader. Do not reap that leader
    before the final group signal: reaping it early permits the group ID to
    disappear or be recycled while a signal-ignoring descendant still lives.
    """
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        process.wait()
        return

    # Give cooperating descendants a short opportunity to close cleanly.
    # The leader can exit first; this must NOT suppress escalation to the group.
    time.sleep(0.4)
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    process.wait()


def supervise(
    *,
    cli: Path,
    output: Path,
    deadline_seconds: float,
    arguments: list[str],
) -> int:
    """Run one process; never reuse an output directory or suppress child failure."""

    if not cli.is_absolute() or not cli.is_file() or not os.access(cli, os.X_OK):
        raise ValueError("An existing, absolute, executable CLI path is required.")
    if not math.isfinite(deadline_seconds) or not 0 < deadline_seconds <= 3600:
        raise ValueError("Deadline must be finite and in (0, 3600] seconds.")
    if not output.is_absolute() or output.is_symlink():
        raise ValueError("A new absolute, non-symlink output path is required.")
    parent = output.parent
    if (
        not parent.is_dir()
        or parent.stat().st_uid != os.geteuid()
        or (parent.stat().st_mode & 0o077) != 0
    ):
        raise ValueError("Output parent must be an owner-private directory.")

    old_umask = os.umask(0o077)
    try:
        output.mkdir(mode=0o700, parents=False, exist_ok=False)
        stdout_path = output / "stdout.txt"
        stderr_path = output / "stderr.txt"
        receipt_path = output / "execution-receipt.json"

        start_time = _now_utc()
        start_clock = time.monotonic()
        status = "launch_error"
        exit_code: int | None = None
        process: subprocess.Popen[bytes] | None = None

        try:
            with stdout_path.open("xb") as stdout, stderr_path.open("xb") as stderr:
                process = subprocess.Popen(
                    [str(cli), *arguments],
                    stdout=stdout,
                    stderr=stderr,
                    start_new_session=True,
                )
                try:
                    exit_code = process.wait(timeout=deadline_seconds)
                    status = "completed"
                except subprocess.TimeoutExpired:
                    status = "deadline_exceeded"
                    _stop_group(process)
                    exit_code = 124
                except KeyboardInterrupt:
                    status = "interrupted"
                    _stop_group(process)
                    exit_code = 130
        except OSError as exc:
            status = "launch_error"
            exit_code = 125
            # Avoid persisting arbitrary environment or credentials from exception text.
            with stderr_path.open("ab") as stream:
                stream.write(f"Execution launch failed: {type(exc).__name__}\n".encode())

        report = None
        if "--save-report" in arguments:
            index = arguments.index("--save-report")
            if index + 1 < len(arguments):
                report_path = Path(arguments[index + 1])
                if report_path.is_file():
                    report = {
                        "path": str(report_path),
                        "bytes": report_path.stat().st_size,
                        "sha256": _sha256(report_path),
                    }

        receipt = {
            "schema": "upgradepilot.qualification.execution_receipt/1",
            "started_utc": start_time,
            "finished_utc": _now_utc(),
            "elapsed_monotonic_seconds": round(time.monotonic() - start_clock, 6),
            "deadline_seconds": deadline_seconds,
            "cli": str(cli),
            "cli_sha256": _sha256(cli),
            "arguments": arguments,
            "status": status,
            "exit_code": exit_code,
            "stdout_file": stdout_path.name,
            "stderr_file": stderr_path.name,
            "report": report,
            "http_requests_measured": False,
            "model_dispatch_measured": False,
        }
        with receipt_path.open("x", encoding="utf-8") as stream:
            json.dump(receipt, stream, sort_keys=True, indent=2)
            stream.write("\n")
        return exit_code if exit_code is not None else 125
    finally:
        os.umask(old_umask)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cli", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--deadline-seconds", type=float, required=True)
    parser.add_argument("cli_args", nargs=argparse.REMAINDER)
    args = parser.parse_args(argv)
    cli_args = args.cli_args[1:] if args.cli_args[:1] == ["--"] else args.cli_args
    try:
        return supervise(
            cli=args.cli,
            output=args.output,
            deadline_seconds=args.deadline_seconds,
            arguments=cli_args,
        )
    except (OSError, ValueError) as exc:
        print(f"Qualification launch refused: {type(exc).__name__}", file=sys.stderr)
        return 125


if __name__ == "__main__":
    raise SystemExit(main())
