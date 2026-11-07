"""Freeze and supervise one admitted diagnostic phase in a new private directory."""
import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import shutil
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PRIVATE = Path("/home/motafeq/.local/share/upgradepilot/pypi-transport-diagnosis-2026-11-06")
PREPARED = HERE.parent / "2026-11-06-native-product-execution-readiness"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=("baseline", "families", "host"))
    args = parser.parse_args()
    os.umask(0o077)
    PRIVATE.mkdir(mode=0o700, exist_ok=True)
    output = PRIVATE / (args.phase + "-01")
    if output.exists():
        raise FileExistsError("An executed phase cannot be reused/retried.")
    manifest = json.loads((PREPARED / "execution-manifest.json").read_bytes())
    assert all(digest(Path(p)) == h for p, h in manifest["bound_files_sha256"].items())
    assert all(digest(Path(p)) == h for p, h in manifest["installed_files_sha256"].items())
    methods = PRIVATE / (args.phase + "-01-methods")
    methods.mkdir(mode=0o700, exist_ok=False)
    for name in ("probe_transport.py", "run_diagnostic.py", "CONTRACT.md"):
        shutil.copyfile(HERE / name, methods / name)
    binding = dict(proof_class="separate_public_pypi_transport_diagnostic", phase=args.phase,
        methods_sha256={p.name:digest(p) for p in methods.iterdir()},
        installed_manifest_sha256=digest(PREPARED / "execution-manifest.json"),
        frozen_native_result_sha256=digest(HERE.parent / "2026-11-06-native-normal-product-live-qualification/task-results.json"),
        binaries_sha256={str(p):digest(p) for p in (Path('/usr/bin/curl'),Path('/mnt/c/Windows/System32/curl.exe')) if p.is_file()},
        endpoints=["https://pypi.org/pypi/fastapi/json","https://pypi.org/pypi/pytest/json"],
        max_http_requests={"baseline":3,"families":2,"host":1}[args.phase],
        retry=False, credential_mode="anonymous public PyPI; personal token never read",
        product_source_changed=False, old_capture_changed=False)
    spec = importlib.util.spec_from_file_location("qualified_launch", PREPARED / "launch_product.py")
    launcher = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(launcher)
    command = [sys.executable, str(methods / "probe_transport.py"), args.phase, "--output", str(output)]
    if args.phase != "baseline":
        command.extend(["--baseline", str(PRIVATE / "baseline-01")])
    if args.phase == "host":
        command.extend(["--families", str(PRIVATE / "families-01")])
    observation = launcher.supervise(command, launcher.child_environment(manifest["installed"]), output,
        manifest["clock_directory"], host_limit={"baseline":100,"families":60,"host":40}[args.phase], execution_binding=binding)
    print(json.dumps(observation), flush=True)
    return 0 if observation["outcome"] == "child_exited" and observation["child_exit"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
