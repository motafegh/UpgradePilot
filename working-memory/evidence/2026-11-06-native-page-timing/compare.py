"""Freeze, supervise and retain six matched historical-product page measurements.

Only repository-owned product code is copied/executed. Private source copies and
stores never replace main or the frozen input. Any failed trial stops the sequence.
"""
import argparse
from hashlib import sha256
import io
import json
import os
from pathlib import Path
import platform
import statistics
import subprocess
import sys
import tarfile
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CAPTURE = Path("/home/motafeq/.local/share/upgradepilot/connected-retained-qualification-2026-11-04/attempt-02/http-httpx")
REVISION = "a3e8b46cf968450a95037765e22212bd"
VERSIONS = {"baseline": "6e98d0a0", "refined": "38741c3c"}
ORDER = ["baseline", "refined", "refined", "baseline", "baseline", "refined"]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def source_hashes(root):
    return {str(p.relative_to(root)): digest(p) for p in sorted((root / "src/upgradepilot").rglob("*.py"))}


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2)+"\n")


def input_hashes():
    # SQLite's transient shared-memory lock index is not evidence content. A
    # nonempty WAL would need a separately defined snapshot, not silent omission.
    wal = CAPTURE / "store/workspace.sqlite3-wal"
    assert not wal.exists() or wal.stat().st_size == 0
    return {"workspace.sqlite3": digest(CAPTURE / "store/workspace.sqlite3")}


def prepare(output):
    output.mkdir(mode=0o700, exist_ok=False)
    products = {}
    for label, revision in VERSIONS.items():
        source = output / label
        archive = subprocess.check_output(["git", "archive", revision, "src/upgradepilot"], cwd=ROOT)
        with tarfile.open(fileobj=io.BytesIO(archive)) as archive_file:
            for member in archive_file.getmembers():
                if member.isfile() and member.name.startswith("src/upgradepilot/") and member.name.endswith(".py"):
                    path = source / member.name
                    assert path.resolve().is_relative_to(source.resolve())
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(archive_file.extractfile(member).read())
        products[label] = dict(revision=subprocess.check_output(["git", "rev-parse", revision], cwd=ROOT, text=True).strip(),
            source_sha256=source_hashes(source))
    differing = [name for name in products["baseline"]["source_sha256"]
                 if products["baseline"]["source_sha256"][name] != products["refined"]["source_sha256"].get(name)]
    assert products["baseline"]["source_sha256"].keys() == products["refined"]["source_sha256"].keys()
    assert differing == ["src/upgradepilot/workspace/checkpoint_store.py"]
    assert source_hashes(ROOT) == products["refined"]["source_sha256"]
    write_json(output / "contract.json", dict(proof_class="offline retained matched-page timing control",
        input_revision=REVISION, capture=str(CAPTURE), input_sha256=input_hashes(),
        products=products, order=ORDER, timeout_seconds=1200,
        method_sha256={name: digest(HERE / name) for name in ("README.md", "compare.py", "measure_page.py")},
        interpreter=sys.executable, interpreter_sha256=digest(Path(sys.executable).resolve()),
        environment=dict(python=sys.version, platform=platform.platform(), cpu_count=os.cpu_count(),
            affinity=sorted(os.sched_getaffinity(0)), load_average=os.getloadavg()),
        criteria=dict(max_supervisor_gap_seconds=2, max_monotonic_raw_fraction=0.05,
            max_cpu_elapsed_ratio=1.05, max_cpu_rusage_fraction=0.05,
            material_median_ratio=0.90, require_every_pair_faster=True)))
    print("Prepared private contract and two pinned product copies; no timing trial executed.")


def verify(output, contract):
    assert contract["input_revision"] == REVISION and contract["order"] == ORDER
    assert contract["input_sha256"] == input_hashes()
    assert all(digest(HERE / name) == value for name, value in contract["method_sha256"].items())
    assert contract["interpreter_sha256"] == digest(Path(sys.executable).resolve())
    assert all(source_hashes(output / label) == data["source_sha256"] for label, data in contract["products"].items())


def run(output):
    contract = json.loads((output / "contract.json").read_bytes())
    verify(output, contract)
    # This intent file also prevents accidental reruns over a partial sequence.
    with (output / "run-intent.json").open("x") as stream:
        json.dump(dict(contract_sha256=digest(output / "contract.json"), started_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                       load_average=os.getloadavg()), stream)
    trials = []
    for index, label in enumerate(contract["order"]):
        name = f"trial-{index+1:02d}-{label}"
        env = dict(os.environ, PYTHONPATH=str(output / label / "src"), PYTHONNOUSERSITE="1")
        argv = [sys.executable, str(HERE / "measure_page.py"), "--capture", str(CAPTURE),
                "--revision", REVISION, "--output", str(output / name)]
        print(f"Starting {name}", flush=True)
        ticks = []
        previous = started = time.monotonic()
        with (output / f"{name}.log").open("x") as log:
            process = subprocess.Popen(argv, cwd=output, env=env, stdout=log, stderr=subprocess.STDOUT)
            timed_out = False
            while process.poll() is None:
                try:
                    process.wait(timeout=0.25)
                except subprocess.TimeoutExpired:
                    pass
                now = time.monotonic()
                ticks.append(now-previous)
                previous = now
                if now-started > contract["timeout_seconds"]:
                    timed_out = True
                    process.terminate()
                    try:
                        process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait()
                    break
        supervision = dict(exit_code=process.returncode, timed_out=timed_out,
            elapsed_seconds=time.monotonic()-started, sampling_gaps_seconds=ticks)
        write_json(output / f"{name}-supervision.json", supervision)
        result_path = output / name / "results.json"
        trial = dict(name=name, label=label, supervision=supervision,
                     result=json.loads(result_path.read_bytes()) if result_path.exists() else None)
        trials.append(trial)
        write_json(output / "partial-results.json", trials)
        print(f"Finished {name}: exit={process.returncode}, supervised elapsed={supervision['elapsed_seconds']:.3f}s", flush=True)
        if process.returncode != 0 or timed_out or trial["result"] is None:
            write_json(output / "summary.json", dict(outcome="failed_stopped_without_retry", trials=trials))
            return 1
        verify(output, contract)
    criteria = contract["criteria"]
    quality_problems = []
    for trial in trials:
        timing = trial["result"]["page_counters"]
        elapsed, raw, cpu, usage = (timing[k] for k in ("monotonic_ns", "raw_ns", "cpu_ns", "rusage_cpu_ns"))
        if min(timing.values()) <= 0 or abs(elapsed/raw-1) > criteria["max_monotonic_raw_fraction"]:
            quality_problems.append(trial["name"]+": elapsed clock inconsistency")
        if cpu/elapsed > criteria["max_cpu_elapsed_ratio"] or abs(cpu/usage-1) > criteria["max_cpu_rusage_fraction"]:
            quality_problems.append(trial["name"]+": CPU clock inconsistency")
        if max(trial["supervision"]["sampling_gaps_seconds"]) > criteria["max_supervisor_gap_seconds"]:
            quality_problems.append(trial["name"]+": supervisor sampling gap")
    signatures = {(t["result"]["page_sha256"], t["result"]["delivered_bytes"]) for t in trials}
    if len(signatures) != 1:
        quality_problems.append("delivered page differs")
    pairs = []
    for offset in range(0, len(trials), 2):
        pair = {t["label"]: t["result"]["page_counters"] for t in trials[offset:offset+2]}
        pairs.append({k: pair["refined"][k]/pair["baseline"][k] for k in ("monotonic_ns", "cpu_ns")})
    medians = {k: statistics.median(p[k] for p in pairs) for k in pairs[0]}
    faster = all(p[k] < 1 for p in pairs for k in p) and all(v <= criteria["material_median_ratio"] for v in medians.values())
    outcome = "timing_inconclusive" if quality_problems else "local_operation_materially_faster" if faster else "mixed_or_no_material_improvement"
    write_json(output / "summary.json", dict(outcome=outcome, quality_problems=quality_problems,
        contract_sha256=digest(output / "contract.json"), pairs_refined_over_baseline=pairs,
        median_paired_ratios=medians, trials=trials))
    print(json.dumps(dict(outcome=outcome, quality_problems=quality_problems, median_paired_ratios=medians)), flush=True)
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("prepare", "run"))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if args.action == "prepare":
        prepare(output)
    else:
        sys.exit(run(output))
