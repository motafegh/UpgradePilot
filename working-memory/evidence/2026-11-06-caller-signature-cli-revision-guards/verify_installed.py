"""Run copied delivery/CLI/auth controls against a noneditable offline wheel.

Invoke from its private root with only installed/controls on PYTHONPATH. Existing
venv dependencies are reused; this proves product origin, not dependency isolation.
"""
import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import socket
import sys
import unittest
from unittest.mock import patch

import upgradepilot


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    args = parser.parse_args()
    installed = (args.root / "installed").resolve()
    assert Path(upgradepilot.__file__).resolve().is_relative_to(installed)
    assert importlib.util.find_spec("experiments") is None
    expected = {str(p.relative_to(args.root / "build/src")): sha256(p.read_bytes()).hexdigest()
                for p in sorted((args.root / "build/src/upgradepilot").rglob("*.py"))}
    assert all(sha256((installed / name).read_bytes()).hexdigest() == h for name,h in expected.items())
    suite = unittest.defaultTestLoader.loadTestsFromNames([
        "test_caller_signature_delivery", "test_cli", "test_github_authentication",
    ])
    with patch.object(socket.socket, "connect", side_effect=AssertionError("installed proof is offline")):
        result = unittest.TextTestRunner(verbosity=2).run(suite)
    origins = {name: str(Path(module.__file__).resolve()) for name,module in sys.modules.items()
               if name.startswith("upgradepilot") and getattr(module, "__file__", None)}
    assert all(Path(origin).is_relative_to(installed) for origin in origins.values())
    wheel = next((args.root / "wheels").glob("*.whl"))
    packet = dict(tests=result.testsRun, failures=len(result.failures), errors=len(result.errors),
        skips=len(result.skipped), successful=result.wasSuccessful(), experiments_available=False,
        installed_product_sha256=expected, loaded_product_origins=origins,
        wheel_sha256=sha256(wheel.read_bytes()).hexdigest(), dependencies="existing venv reused; no isolation claim",
        control_sha256={p.name: sha256(p.read_bytes()).hexdigest() for p in sorted((args.root / "controls").glob("*.py"))},
        method_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
    (args.root / "results.json").write_text(json.dumps(packet, indent=2)+"\n")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
