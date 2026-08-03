#!/usr/bin/env python3
"""Run the Step 6D contract-v2 live evaluator with localhost-safe WSL HTTP settings."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Mapping


ROOT = Path(__file__).resolve().parents[1]
MODULE = "experiments.step6_support_drop_contract_v2_live_evaluation"
_PROXY_KEYS = (
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "ALL_PROXY",
    "http_proxy",
    "https_proxy",
    "all_proxy",
)
_LOCAL_NO_PROXY = "127.0.0.1,localhost,::1"


def build_localhost_http_environment(source: Mapping[str, str]) -> dict[str, str]:
    """Return a child environment that cannot proxy UpgradePilot localhost HTTP."""

    environment = dict(source)
    for key in _PROXY_KEYS:
        environment.pop(key, None)
    environment["NO_PROXY"] = _LOCAL_NO_PROXY
    environment["no_proxy"] = _LOCAL_NO_PROXY
    return environment


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
