#!/usr/bin/env python3
"""Run the Step 6C LM Studio smoke with a localhost-safe HTTP environment.

UpgradePilot's local inference boundary is WSL -> LM Studio on 127.0.0.1:12345.
Some WSL environments export HTTP(S)/ALL proxy variables for ordinary outbound
traffic. Python ``requests`` honors those variables by default, which can incorrectly
route localhost traffic through Privoxy instead of LM Studio.

This runner changes only the child-process environment used for the Step 6C smoke:

- remove HTTP_PROXY / HTTPS_PROXY / ALL_PROXY and lowercase equivalents;
- set NO_PROXY / no_proxy for localhost and loopback;
- execute the experiment with the active UpgradePilot Python interpreter.

It does not modify the user's shell, system proxy settings, LM Studio configuration,
or UpgradePilot product runtime.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Mapping


ROOT = Path(__file__).resolve().parents[1]
SMOKE_SCRIPT = ROOT / "experiments" / "step6_support_drop_smoke.py"
_PROXY_KEYS = (
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "ALL_PROXY",
    "http_proxy",
    "https_proxy",
    "all_proxy",
)
_LOCAL_NO_PROXY = "127.0.0.1,localhost,::1"


def build_localhost_http_environment(
    source: Mapping[str, str],
) -> dict[str, str]:
    """Return a child environment that cannot proxy UpgradePilot localhost HTTP."""

    environment = dict(source)
    for key in _PROXY_KEYS:
        environment.pop(key, None)
    environment["NO_PROXY"] = _LOCAL_NO_PROXY
    environment["no_proxy"] = _LOCAL_NO_PROXY
    return environment


def main() -> int:
    """Execute the existing Step 6C experiment with proxy-safe localhost settings."""

    if not SMOKE_SCRIPT.is_file():
        print(f"Step 6C smoke script is missing: {SMOKE_SCRIPT}", file=sys.stderr)
        return 2

    environment = build_localhost_http_environment(os.environ)
    print("Step 6C localhost HTTP runner")
    print("control plane: WSL")
    print("environment proxies for child process: disabled")
    print(f"NO_PROXY: {_LOCAL_NO_PROXY}")
    print(f"python: {sys.executable}")
    print()

    completed = subprocess.run(
        [sys.executable, str(SMOKE_SCRIPT)],
        cwd=ROOT,
        env=environment,
        check=False,
    )
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
