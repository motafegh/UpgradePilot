#!/usr/bin/env python3
"""Run the Step 6D contract-v2 live evaluator with localhost-safe WSL HTTP settings."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from tools.run_step6c_support_drop_smoke import (
    _LOCAL_NO_PROXY,
    build_localhost_http_environment,
)


ROOT = Path(__file__).resolve().parents[1]
MODULE = "experiments.step6_support_drop_contract_v2_live_evaluation"


def main() -> int:
    environment = build_localhost_http_environment(os.environ)
    print("Step 6D contract-v2 localhost HTTP runner")
    print("control plane: WSL")
    print("environment proxies for child process: disabled")
    print(f"NO_PROXY: {_LOCAL_NO_PROXY}")
    print(f"python: {sys.executable}")
    print()

    completed = subprocess.run(
        [sys.executable, "-m", MODULE],
        cwd=ROOT,
        env=environment,
        check=False,
    )
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
