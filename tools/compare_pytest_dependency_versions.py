"""Capture and compare one pytest test in two prepared Python environments.

Invoke capture with each environment's Python in an independently authorized,
isolated checkout. It runs the named test. The operator owns environment preparation
and isolation. Compare reads the two resulting receipts without running tests.
These are developer observations, not UpgradePilot product or compatibility verdicts.
"""

from __future__ import annotations

import argparse
from importlib import metadata
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys


_FORMAT = "pytest-dependency-observation/1"
_MAX_RECEIPT_BYTES = 256 * 1024


def _normalized_name(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def _git(checkout: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-c", "core.fsmonitor=false", "-C", str(checkout), *args],
        text=True,
        timeout=10,
    ).strip()


def _require_clean_revision(checkout: Path, revision: str) -> None:
    if (
        not re.fullmatch(r"[0-9a-f]{40}", revision)
        or Path(_git(checkout, "rev-parse", "--show-toplevel")) != checkout
        or _git(checkout, "rev-parse", "HEAD") != revision
        or _git(checkout, "status", "--porcelain", "--untracked-files=all")
    ):
        raise ValueError("Expected a clean checkout at the supplied exact revision.")


def _observe_loaded_module(distribution: metadata.Distribution, module_name: str):
    # Do not import the dependency to obtain evidence. The test process must already
    # have loaded it. The recorded file must belong to the selected distribution.
    loaded = sys.modules.get(module_name)
    origin = getattr(loaded, "__file__", None)
    if not isinstance(origin, str):
        return None
    module_path = Path(origin).resolve()
    if not module_path.is_file():
        return None
    for entry in distribution.files or ():
        if distribution.locate_file(entry).resolve() == module_path:
            return {"version": distribution.version, "distribution_file": str(entry)}
    return None


class _TestObservation:
    def __init__(self, pytest, nodeid: str, distribution: metadata.Distribution, module: str):
        self.pytest = pytest
        self.nodeid = nodeid
        self.distribution = distribution
        self.module = module
        self.selected = []
        self.phases = []
        self.loaded = None
        self.marked_xfail = False

    def pytest_collection_finish(self, session):
        self.selected = [item.nodeid for item in session.items]
        if self.selected != [self.nodeid]:
            self.pytest.exit("Expected exactly the selected test node.", returncode=2)
        self.marked_xfail = session.items[0].get_closest_marker("xfail") is not None

    def pytest_runtest_logreport(self, report):
        if report.nodeid != self.nodeid:
            return
        self.phases.append({
            "phase": report.when,
            "outcome": report.outcome,
            "expected_failure": self.marked_xfail or hasattr(report, "wasxfail")
            or str(report.longrepr).startswith("[XPASS(strict)]"),
        })
        if report.when == "call":
            self.loaded = _observe_loaded_module(self.distribution, self.module)


def capture(args: argparse.Namespace) -> int:
    try:
        import pytest
    except ImportError as error:
        raise ValueError("The prepared environment must provide pytest.") from error

    checkout = args.checkout.resolve()
    output = args.output.resolve()
    if output.is_relative_to(checkout) or output.exists():
        raise ValueError("Choose a new receipt path outside the checkout.")
    _require_clean_revision(checkout, args.revision)
    test_path, separator, name = args.nodeid.partition("::")
    selected_file = (checkout / test_path).resolve()
    if (
        not separator or not name or test_path.startswith("-")
        or Path(test_path).is_absolute() or selected_file.suffix != ".py"
        or not selected_file.is_relative_to(checkout) or not selected_file.is_file()
    ):
        raise ValueError("Supply one repository-relative Python pytest node ID.")
    if os.environ.get("PYTEST_ADDOPTS") or os.environ.get("PYTEST_PLUGINS"):
        raise ValueError("Unset ambient pytest options and plugins for a controlled comparison.")

    package = _normalized_name(args.distribution)
    distributions = list(metadata.distributions())
    selected = [
        dist for dist in distributions if _normalized_name(dist.metadata["Name"]) == package
    ]
    if len(selected) != 1 or selected[0].version != args.expected_version:
        raise ValueError("Expected one installed distribution with the requested exact version.")
    other_distributions = sorted(
        (_normalized_name(dist.metadata["Name"]), dist.version)
        for dist in distributions if _normalized_name(dist.metadata["Name"]) != package
    )
    observation = _TestObservation(pytest, args.nodeid, selected[0], args.module)
    os.environ["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    sys.dont_write_bytecode = True
    os.chdir(checkout)
    sys.path.insert(0, str(checkout))
    # Keep node IDs relative to the checked-out repository even when pytest
    # discovers the test settings in a nested project such as backend/.
    options = ["-p", "no:cacheprovider", "-o", "addopts=", "--rootdir", str(checkout)]
    for plugin in args.plugin:
        options.extend(("-p", plugin))
    exit_code = int(pytest.main([*options, args.nodeid], plugins=[observation]))
    clean_revision = True
    try:
        _require_clean_revision(checkout, args.revision)
    except ValueError:
        clean_revision = False

    record = {
        "format": _FORMAT,
        "revision": args.revision,
        "nodeid": args.nodeid,
        "distribution": package,
        "module": args.module,
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "pytest": pytest.__version__,
            "plugins": args.plugin,
            "other_distributions": other_distributions,
        },
        "requested_version": args.expected_version,
        "loaded": observation.loaded,
        "selected": observation.selected,
        "phases": observation.phases,
        "pytest_exit": exit_code,
        "clean_revision": clean_revision,
    }
    payload = (json.dumps(record, indent=2, sort_keys=True) + "\n").encode()
    if len(payload) > _MAX_RECEIPT_BYTES:
        raise ValueError("Observation exceeds the bounded receipt size.")
    with output.open("xb") as handle:
        handle.write(payload)
    return exit_code if clean_revision else 2


def _read(path: Path) -> dict:
    with path.open("rb") as handle:
        payload = handle.read(_MAX_RECEIPT_BYTES + 1)
    if len(payload) > _MAX_RECEIPT_BYTES:
        raise ValueError("Observation exceeds the bounded receipt size.")
    record = json.loads(payload)
    if not isinstance(record, dict) or record.get("format") != _FORMAT:
        raise ValueError("Unsupported pytest observation.")
    return record


def _outcome(record: dict) -> str:
    loaded = record["loaded"]
    phases = record["phases"]
    if (
        record["clean_revision"] is not True
        or record["selected"] != [record["nodeid"]]
        or not isinstance(loaded, dict)
        or loaded.get("version") != record["requested_version"]
        or not loaded.get("distribution_file")
        or [phase["phase"] for phase in phases] != ["setup", "call", "teardown"]
        or any(phase["expected_failure"] for phase in phases)
        or phases[0]["outcome"] != "passed"
        or phases[2]["outcome"] != "passed"
    ):
        return "inconclusive"
    call = phases[1]["outcome"]
    if (call, record["pytest_exit"]) in {("passed", 0), ("failed", 1)}:
        return call
    return "inconclusive"


def compare(old: dict, proposed: dict) -> dict:
    identities = ("revision", "nodeid", "distribution", "module", "environment")
    if any(old[key] != proposed[key] for key in identities):
        raise ValueError("The observations differ in revision, test, dependency or environment.")
    if old["requested_version"] == proposed["requested_version"]:
        raise ValueError("The comparison requires two distinct requested versions.")
    outcomes = _outcome(old), _outcome(proposed)
    result = {
        ("passed", "passed"): "both_passed",
        ("passed", "failed"): "proposed_only_test_failure",
    }.get(outcomes, "inconclusive")
    return {
        "result": result,
        "revision": old["revision"],
        "nodeid": old["nodeid"],
        "distribution": old["distribution"],
        "old_version": old["requested_version"],
        "proposed_version": proposed["requested_version"],
        "old": outcomes[0],
        "proposed": outcomes[1],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    runner = commands.add_parser("capture", help="run one selected test and record the loaded module")
    runner.add_argument("--checkout", type=Path, required=True)
    runner.add_argument("--revision", required=True)
    runner.add_argument("--nodeid", required=True)
    runner.add_argument("--distribution", required=True)
    runner.add_argument("--module", required=True)
    runner.add_argument("--expected-version", required=True)
    runner.add_argument("--output", type=Path, required=True)
    runner.add_argument("--plugin", action="append", default=[])
    reader = commands.add_parser("compare", help="compare two saved receipts offline")
    reader.add_argument("old", type=Path)
    reader.add_argument("proposed", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "capture":
            return capture(args)
        result = compare(_read(args.old), _read(args.proposed))
        print(json.dumps(result, sort_keys=True))
        return 2 if result["result"] == "inconclusive" else 0
    except (OSError, subprocess.SubprocessError, ValueError, KeyError, TypeError, AttributeError) as error:
        print(f"Cannot qualify comparison evidence: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
