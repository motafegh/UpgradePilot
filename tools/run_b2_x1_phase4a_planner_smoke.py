#!/usr/bin/env python3
"""Run the B2/X1 Phase-4A planner smoke with localhost-safe HTTP settings.

This tool intentionally reuses the already-tested Step-6C proxy-isolation helper rather than
creating a second localhost transport policy. It changes only the child-process environment:
ambient HTTP(S)/ALL proxy variables are removed and loopback is placed in NO_PROXY/no_proxy.

The child experiment remains development-only and performs no target-repository mutation.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from tools.run_step6c_support_drop_smoke import build_localhost_http_environment


ROOT = Path(__file__).resolve().parents[1]
SMOKE_SCRIPT = ROOT / "experiments" / "b2_x1_phase4a_planner_smoke.py"
SMOKE_MODULE = "experiments.b2_x1_phase4a_planner_smoke"


def main() -> int:
    """Execute the planner smoke through the accepted WSL -> localhost LM Studio boundary."""

    if not SMOKE_SCRIPT.is_file():
        print(f"Planner smoke script is missing: {SMOKE_SCRIPT}", file=sys.stderr)
        return 2

    environment = build_localhost_http_environment(os.environ)
    print("B2/X1 Phase-4A localhost planner smoke runner")
    print("control plane: WSL")
    print("environment proxies for child process: disabled")
    print(f"NO_PROXY: {environment['NO_PROXY']}")
    print(f"python: {sys.executable}")
    print()

    completed = subprocess.run(
        [sys.executable, "-m", SMOKE_MODULE],
        cwd=ROOT,
        env=environment,
        check=False,
    )
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
