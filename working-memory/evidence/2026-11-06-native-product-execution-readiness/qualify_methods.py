"""Offline qualification of this dated launcher and cold reader in new private roots.

The parent may load historical experiment input adapters to prepare data. The
supervised installed product/cold processes cannot import those adapters or
experiments. Every method version is copied before execution for failure recovery.
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

from launch_product import child_environment, digest, supervise, write_json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PRIVATE = Path("/home/motafeq/.local/share/upgradepilot/native-signature-kubernetes-dashboard-token-api-pr-20-httpx-2026-11-06")
RUNTIME = PRIVATE / "runtime"
OLD_INSTALL = Path("/home/motafeq/.local/share/upgradepilot/cli-revision-guards-2026-11-06-installed-01")
REFERENCE = Path("/home/motafeq/.local/share/upgradepilot/cli-revision-guards-httpx-2026-11-06-attempt-01")
FIXTURE = ROOT / "working-memory/evidence/2026-11-04-caller-signature-connected-retained-qualification"
CLOCK = ROOT / "working-memory/evidence/2026-11-06-independent-host-timing"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    os.umask(0o077)
    args.output.mkdir(mode=0o700, exist_ok=False)
    methods = args.output / "methods"
    methods.mkdir()
    for path in HERE.glob("*.py"):
        shutil.copyfile(path, methods / path.name)
    method_hashes = {p.name: digest(p) for p in methods.glob("*.py")}
    if not RUNTIME.exists():
        RUNTIME.mkdir(mode=0o700)
        (RUNTIME / "wheels").mkdir()
        wheel = next((OLD_INSTALL / "wheels").glob("*.whl"))
        destination = RUNTIME / "wheels" / wheel.name
        shutil.copyfile(wheel, destination)
        assert digest(destination) == "8a4e7a428ff83bf42bd2596e6c6cb84960368e56fc3ec7a1a73daa3853a0cc07"
        with (args.output / "install.log").open("xb") as log:
            subprocess.run([sys.executable, "-m", "pip", "install", "--no-index", "--no-deps", "--no-compile",
                "--target", str(RUNTIME / "installed"), str(destination)], stdout=log, stderr=subprocess.STDOUT, check=True)
    installed = RUNTIME / "installed"
    original = json.loads((ROOT / "working-memory/evidence/2026-11-06-caller-signature-cli-revision-guards/verification.json").read_bytes())
    source = original["product_source_sha256"]
    assert all(digest(ROOT / p) == h and digest(installed / p.removeprefix("src/")) == h for p, h in source.items())
    sys.path.insert(0, str(FIXTURE))
    import retained_cases
    rows = json.loads((ROOT / "working-memory/evidence/2026-11-01-analysis-capacity-and-work-admission/retained-qualification-results.json").read_bytes())
    row = next(r for r in rows if r["case"] == "httpx")
    directory = Path(row["directory"])
    assert all(digest(directory / p) == h for p, h in row["output_sha256"].items())
    body, catalog = retained_cases.ordinary.open_ordinary_comparison(directory)
    fixture = args.output / "authored-fixture.json"
    write_json(fixture, dict(body=body, scopes=[dict(source_id=s.source_id, repository=s.repository, revision=s.revision) for s in catalog.scopes],
        files=[dict(source_id=f.source_id, path=f.path, content=f.content) for f in catalog.files]))
    identity = body["acquisition"]["native_inputs"]["identity"]
    write_json(args.output / "contract.json", dict(proof_class="offline_launch_and_cold_method_qualification",
        method_sha256=method_hashes, fixture_sha256=digest(fixture), product_sha256=source,
        unchanged_adapter_sha256=digest(FIXTURE / "controlled_http.py"), personal_credential_value_read=False,
        real_provider_calls=0, control_token="synthetic; not personal", input_sha256=row["output_sha256"],
        positive_host_limit_seconds=900, failure_control_exit=7, timeout_control_host_seconds=1,
        reference_revision="e7d3a4ffbb954d7b906383e78d0bce20"))
    env = child_environment(installed)
    env["GITHUB_TOKEN"] = "synthetic-offline-control"
    command = [sys.executable, str(methods / "controlled_cli.py"), "--fixture", str(fixture),
        "--adapter", str(FIXTURE / "controlled_http.py"), "--base", identity["base_sha"], "--expected-head", identity["head_sha"]]
    print("Starting installed controlled normal composition; real network forbidden.", flush=True)
    positive = supervise(command, env, args.output / "composition", CLOCK,
        execution_binding=dict(proof_class="offline_control_not_live_execution", method_sha256=method_hashes,
                               product_sha256=source, fixture_sha256=digest(fixture)))
    write_json(args.output / "positive-observation.json", positive)
    assert positive["outcome"] == "child_exited" and positive["child_exit"] == 0, positive
    assert positive["timing_quality"] == "qualified_outer_envelope"
    costs = json.loads((args.output / "composition/controlled-costs.json").read_bytes())
    assert costs["github"] == 45 and costs["provider"] == 55 and costs["header_scope_checked"]
    print("Controlled composition passed; checking exact fresh-process cold recovery.", flush=True)
    cold_command = [sys.executable, str(methods / "cold_review.py"), "--installed", str(installed),
        "--store", str(args.output / "composition/store"), "--revision", positive["confirmed_revision"],
        "--report", str(args.output / "composition/report.json"), "--output", str(args.output / "cold"),
        "--reference-store", str(REFERENCE / "store"), "--reference-revision", "e7d3a4ffbb954d7b906383e78d0bce20"]
    cold_env = child_environment(installed)
    with (args.output / "cold.log").open("xb") as log:
        cold = subprocess.run(cold_command, cwd=args.output, env=cold_env, stdout=log, stderr=subprocess.STDOUT, timeout=120)
    assert cold.returncode == 0, "See private cold.log."
    cold_result = json.loads((args.output / "cold/results.json").read_bytes())
    assert cold_result["witnesses"] == 12 and cold_result["roots"] == 5 and cold_result["reference_native_equal"]
    # Revision refusal is tested through the same guarded installed entry.
    bad_command = list(cold_command)
    bad_command[bad_command.index("--revision") + 1] = "0" * 32
    bad_command[bad_command.index("--output") + 1] = str(args.output / "cold-missing-revision")
    with (args.output / "cold-missing-revision.log").open("xb") as log:
        bad = subprocess.run(bad_command, cwd=args.output, env=cold_env, stdout=log, stderr=subprocess.STDOUT, timeout=120)
    assert bad.returncode != 0
    assert json.loads((args.output / "cold-missing-revision.log").read_bytes()) == dict(outcome="rejected", reason="missing_checkpoint_revision")
    failure = supervise([sys.executable, "-c", "raise SystemExit(7)"], cold_env, args.output / "nonzero", CLOCK)
    assert failure["outcome"] == "child_exited" and failure["child_exit"] == 7
    timeout = supervise([sys.executable, "-c", "import time; time.sleep(30)"], cold_env, args.output / "timeout", CLOCK, host_limit=1)
    assert timeout["outcome"] == "timeout" and timeout["child_exit"] is not None
    try:
        supervise([sys.executable, "-c", "raise SystemExit(99)"], cold_env, args.output / "nonzero", CLOCK)
    except FileExistsError:
        pass
    else:
        raise AssertionError("Existing output was reused.")
    assert all(digest(methods / p) == h for p, h in method_hashes.items())
    assert all(digest(directory / p) == h for p, h in row["output_sha256"].items())
    summary = dict(outcome="passed", methods_sha256=method_hashes, real_provider_calls=0, personal_credential_value_read=False,
        composition=positive, controlled_costs=costs, cold=cold_result, unavailable_revision_refused=True,
        nonzero=failure, timeout=timeout, output_reuse_refused=True, original_inputs_unchanged=True,
        dependencies="Existing venv dependencies reused; no dependency-isolation claim.")
    write_json(args.output / "results.json", summary)
    print(json.dumps(dict(outcome="passed", installed=str(installed), provider=costs["provider"], github=costs["github"],
        cold_exact=True, nonzero_preserved=True, timeout_preserved=True, output_reuse_refused=True)), flush=True)


if __name__ == "__main__":
    main()
