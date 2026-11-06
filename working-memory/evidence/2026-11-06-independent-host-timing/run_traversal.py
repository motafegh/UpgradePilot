"""One host-supervised fixed native traversal; no automatic retry or live acquisition."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

from run_preflight import HostClock, stop_child, write

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
INSTALLED = Path("/home/motafeq/.local/share/upgradepilot/cli-revision-guards-2026-11-06-installed-01/installed")
CAPTURE = Path("/home/motafeq/.local/share/upgradepilot/connected-retained-qualification-2026-11-04/attempt-02/http-httpx/store")
PREFLIGHT = Path("/home/motafeq/.local/share/upgradepilot/native-signature-kubernetes-dashboard-token-api-pr-20-httpx-2026-11-06/timing-preflight-01")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    os.umask(0o077)
    args.output.mkdir(mode=0o700, exist_ok=False)
    preflight = json.loads((PREFLIGHT / "results.json").read_bytes())
    assert preflight["outcome"] == "qualified_host_envelope" and preflight["method_hashes_unchanged"]
    previous = json.loads((PREFLIGHT / "contract.json").read_bytes())
    assert all(sha256((HERE/n).read_bytes()).hexdigest() == h for n,h in previous["methods_sha256"].items())
    source = previous["qualified_product_sha256"]
    assert all(sha256((ROOT/n).read_bytes()).hexdigest() == h and
               sha256((INSTALLED/n.removeprefix("src/")).read_bytes()).hexdigest() == h for n,h in source.items())
    wal = CAPTURE / "workspace.sqlite3-wal"
    assert not wal.exists() or not wal.stat().st_size
    task = ROOT / "working-memory/evidence/2026-11-04-caller-signature-connected-retained-qualification/navigation-task.json"
    methods = {n: sha256((HERE/n).read_bytes()).hexdigest() for n in
        (*previous["methods_sha256"], "TRAVERSAL_CONTRACT.md", "cold_pages.py", "guarded_traversal.py", "run_traversal.py")}
    write(args.output / "contract.json", dict(proof="one independently host-timed retained native traversal",
        installed=str(INSTALLED), capture=str(CAPTURE), revision="a3e8b46cf968450a95037765e22212bd",
        pages=60, page_ceiling=64, page_characters=4096, host_seconds_limit=3600,
        task_question=json.loads(task.read_bytes())["question"], task_sha256=sha256(task.read_bytes()).hexdigest(),
        methods_sha256=methods, product_sha256=source,
        input_sqlite_sha256=sha256((CAPTURE/"workspace.sqlite3").read_bytes()).hexdigest(),
        preflight_sha256=sha256((PREFLIGHT/"results.json").read_bytes()).hexdigest(),
        reference_scope="host begin before child launch through child exit; no overhead subtraction", retries=0))
    clock, child, begin, end = None, None, None, None
    result = dict(outcome="incomplete", observations=0, max_observation_gap_seconds=0)
    previous_sample = None
    try:
        clock = HostClock(args.output)
        begin = clock.command("begin")
        previous_sample = begin
        env = dict(os.environ, PYTHONPATH=str(INSTALLED), PYTHONNOUSERSITE="1")
        env.pop("GITHUB_TOKEN", None)
        with (args.output / "worker.log").open("xb") as log, (args.output / "host-samples.jsonl").open("x") as samples:
            child = subprocess.Popen([sys.executable, str(HERE/"guarded_traversal.py"), "--output", str(args.output)],
                cwd=args.output, env=env, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            last_page, last_heartbeat = 0, 0
            while child.poll() is None:
                try:
                    child.wait(timeout=.25)
                except subprocess.TimeoutExpired:
                    pass
                observation = clock.command("sample")
                samples.write(json.dumps(observation)+"\n")
                samples.flush()
                gap = (observation["qpc_timestamp"]-previous_sample["qpc_timestamp"])/begin["frequency"]
                result["max_observation_gap_seconds"] = max(result["max_observation_gap_seconds"], gap)
                result["observations"] += 1
                previous_sample = observation
                elapsed = observation["elapsed_ticks"]/observation["frequency"]
                progress_path = args.output / "progress.json"
                progress = json.loads(progress_path.read_bytes()) if progress_path.exists() else {}
                page = progress.get("pages", 0)
                if page != last_page or elapsed-last_heartbeat >= 15:
                    print(json.dumps(dict(event="progress", pages=page, host_elapsed_seconds=elapsed)), flush=True)
                    last_page, last_heartbeat = page, elapsed
                if elapsed > 3600:
                    raise TimeoutError("Frozen host traversal allowance exhausted.")
        end = clock.command("end")
        result["max_observation_gap_seconds"] = max(result["max_observation_gap_seconds"],
            (end["qpc_timestamp"]-previous_sample["qpc_timestamp"])/begin["frequency"])
        result.update(child_exit=child.returncode, host_begin=begin, host_end=end,
            host_elapsed_seconds=end["elapsed_ticks"]/end["frequency"],
            host_utc_span_seconds=(end["utc_ticks"]-begin["utc_ticks"])/1e7)
        path = args.output / "worker-results.json"
        result["worker"] = json.loads(path.read_bytes()) if path.exists() else None
        problems = []
        if not end["high_resolution"] or end["frequency"] != begin["frequency"]:
            problems.append("QPC method/frequency inconsistency")
        if result["max_observation_gap_seconds"] > 2:
            problems.append("observation gap; uninterrupted/active interpretation withheld")
        if abs(result["host_utc_span_seconds"]/result["host_elapsed_seconds"]-1) > .05:
            problems.append("QPC/UTC disagreement")
        functional = child.returncode == 0 and result["worker"] and result["worker"]["outcome"] == "passed"
        result.update(quality_problems=problems, functional_completion=bool(functional),
            outcome="qualified_host_timed_completion" if functional and not problems else "timing_inconclusive" if functional else "incomplete_or_failed")
    except BaseException as error:
        if child is not None:
            stop_child(child)
        result.update(outcome="interrupted" if isinstance(error, KeyboardInterrupt) else "failed",
                      problem=type(error).__name__+": "+str(error))
        if clock is not None and begin is not None:
            try:
                result["host_stopped_interval"] = clock.command("end")
            except Exception:
                result["host_stopped_interval"] = "unknown"
    finally:
        if clock is not None:
            try:
                clock.close()
            except Exception as error:
                result["cleanup_problem"] = type(error).__name__
        result["method_hashes_unchanged"] = all(sha256((HERE/n).read_bytes()).hexdigest() == h for n,h in methods.items())
        result["input_unchanged"] = sha256((CAPTURE/"workspace.sqlite3").read_bytes()).hexdigest() == json.loads((args.output/"contract.json").read_bytes())["input_sqlite_sha256"]
        result["installed_hashes_unchanged"] = all(sha256((INSTALLED/n.removeprefix("src/")).read_bytes()).hexdigest() == h for n,h in source.items())
        if not all(result[k] for k in ("method_hashes_unchanged", "input_unchanged", "installed_hashes_unchanged")):
            result["outcome"] = "invalid_freeze_drift"
        write(args.output/"results.json", result)
        print(json.dumps({k:v for k,v in result.items() if k != "worker"}), flush=True)
    return 0 if result["outcome"] == "qualified_host_timed_completion" else 1


if __name__ == "__main__":
    raise SystemExit(main())
