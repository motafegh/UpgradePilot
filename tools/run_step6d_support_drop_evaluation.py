#!/usr/bin/env python3
"""Run Step 6D with localhost-safe WSL HTTP settings.

This wrapper reuses the Step 6C child-environment isolation so LM Studio loopback traffic
cannot be intercepted by inherited HTTP(S)/ALL proxy variables. It changes only the
child process environment and does not modify the user's shell or system configuration.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.run_step6c_support_drop_smoke import (  # noqa: E402
    _LOCAL_NO_PROXY,
    build_localhost_http_environment,
)


EVALUATION_SCRIPT = ROOT / "experiments" / "step6_support_drop_evaluation.py"


def main() -> int:
    if not EVALUATION_SCRIPT.is_file():
        print(f"Step 6D evaluation script is missing: {EVALUATION_SCRIPT}", file=sys.stderr)
        return 2

    environment = build_localhost_http_environment(os.environ)
    print("Step 6D localhost HTTP runner")
    print("control plane: WSL")
    print("environment proxies for child process: disabled")
    print(f"NO_PROXY: {_LOCAL_NO_PROXY}")
    print(f"python: {sys.executable}")
    print()

    completed = subprocess.run(
        [sys.executable, str(EVALUATION_SCRIPT)],
        cwd=ROOT,
        env=environment,
        check=False,
    )
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
