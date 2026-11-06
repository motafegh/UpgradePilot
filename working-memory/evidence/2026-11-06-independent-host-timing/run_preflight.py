"""Freeze and execute the fixed host-clock qualification once in a new private root.

The Windows observer times the enclosing WSL child lifetime. Child counters are
different spans; command launch/message overhead is never subtracted silently.
"""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import selectors
import signal
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
POWERSHELL = Path("/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe")


def write(path, value):
    path.write_text(json.dumps(value, indent=2)+"\n")


class HostClock:
    """One owned Windows process, with bounded line replies on its private pipes."""

    def __init__(self, directory):
        self.log = (directory / "host-stderr.txt").open("wb")
        env = dict(os.environ)
        env.pop("GITHUB_TOKEN", None)
        self.process = subprocess.Popen([str(POWERSHELL), "-NoLogo", "-NoProfile", "-NonInteractive",
            "-Command", (HERE / "host_clock.ps1").read_text()], stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=self.log, env=env)
        self.buffer = b""
        self.selector = selectors.DefaultSelector()
        self.selector.register(self.process.stdout, selectors.EVENT_READ)
        try:
            self.ready = self.read_reply()
            assert self.ready["op"] == "ready"
        except BaseException:
            # A failed constructor is not assigned to the caller's cleanup slot.
            # Closing stdin lets this owned watcher leave its ReadLine loop.
            self.process.stdin.close()
            try:
                self.process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait(timeout=2)
            self.selector.close()
            self.log.close()
            raise

    def read_reply(self):
        deadline = time.clock_gettime(time.CLOCK_MONOTONIC_RAW) + 5.0
        while b"\n" not in self.buffer:
            remaining = deadline-time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
            if remaining <= 0 or not self.selector.select(remaining):
                raise TimeoutError("Host clock reply unavailable within watchdog.")
            chunk = os.read(self.process.stdout.fileno(), 4096)
            if not chunk:
                raise RuntimeError("Host clock exited before a reply.")
            self.buffer += chunk
            if len(self.buffer) > 16384:
                raise RuntimeError("Host clock reply outside protocol bounds.")
        line, self.buffer = self.buffer.split(b"\n", 1)
        return json.loads(line.decode("utf-8-sig"))

    def command(self, verb):
        self.process.stdin.write((verb+"\n").encode("ascii"))
        self.process.stdin.flush()
        result = self.read_reply()
        assert result["op"] == verb
        return result

    def close(self):
        try:
            if self.process.poll() is None:
                self.command("quit")
        finally:
            self.process.stdin.close()
            try:
                self.process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait(timeout=2)
            self.selector.close()
            self.log.close()


def stop_child(child):
    if child.poll() is None:
        os.killpg(child.pid, signal.SIGINT)
        try:
            child.wait(timeout=5)
        except subprocess.TimeoutExpired:
            os.killpg(child.pid, signal.SIGKILL)
            child.wait(timeout=5)


def run_phase(clock, directory, mode):
    begin = clock.command("begin")
    samples = [begin]
    child = None
    problem = None
    try:
        with (directory / f"{mode}.log").open("xb") as log:
            child = subprocess.Popen([sys.executable, str(HERE / "probe.py"), mode,
                "--output", str(directory / f"{mode}.json")], stdout=log, stderr=subprocess.STDOUT,
                start_new_session=True)
            while child.poll() is None:
                try:
                    child.wait(timeout=0.25)
                except subprocess.TimeoutExpired:
                    pass
                sample = clock.command("sample")
                samples.append(sample)
                if sample["session_ticks"]/sample["frequency"] > 90:
                    raise TimeoutError("Fixed host preflight allowance exhausted.")
    except BaseException as error:
        problem = type(error).__name__ + ": " + str(error)
        if child is not None:
            stop_child(child)
    end = clock.command("end")
    samples.append(end)
    path = directory / f"{mode}.json"
    row = dict(mode=mode, host_begin=begin, host_end=end, samples=samples,
        host_elapsed_seconds=end["elapsed_ticks"]/end["frequency"],
        host_utc_span_seconds=(end["utc_ticks"]-begin["utc_ticks"])/1e7,
        max_observation_gap_seconds=max((b["qpc_timestamp"]-a["qpc_timestamp"])/begin["frequency"]
            for a,b in zip(samples,samples[1:])),
        child_exit=child.returncode if child is not None else None, problem=problem,
        child=json.loads(path.read_bytes()) if path.exists() else None)
    write(directory / f"{mode}-observation.json", row)
    return row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    os.umask(0o077)
    args.output.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    args.output.mkdir(mode=0o700, exist_ok=False)
    methods = {name: sha256((HERE/name).read_bytes()).hexdigest()
               for name in ("README.md", "host_clock.ps1", "probe.py", "run_preflight.py")}
    qualification = ROOT / "working-memory/evidence/2026-11-06-caller-signature-cli-revision-guards/verification.json"
    qualified = json.loads(qualification.read_bytes())
    assert all(sha256((ROOT/name).read_bytes()).hexdigest() == h
               for name,h in qualified["product_source_sha256"].items())
    write(args.output / "contract.json", dict(proof="independent host elapsed-clock preflight",
        product_horizon="1e5d3aec", phases=["empty", "idle", "cpu"], max_host_seconds=90,
        max_observation_gap_seconds=2, clock_relative_tolerance=0.05,
        qualified_product_sha256=qualified["product_source_sha256"],
        qualification_sha256=sha256(qualification.read_bytes()).hexdigest(),
        methods_sha256=methods, powershell=str(POWERSHELL),
        powershell_sha256=sha256(POWERSHELL.read_bytes()).hexdigest(),
        interval="host begin before WSL child launch; host end after child exit; overhead unremoved",
        replacements=0, live_provider=False, credentials=False, product_source_changes=False))
    clock = None
    rows = []
    result = dict(outcome="unavailable", phases=rows, quality_problems=[])
    try:
        clock = HostClock(args.output)
        result["host_ready"] = clock.ready
        for mode in ("empty", "idle", "cpu"):
            row = run_phase(clock, args.output, mode)
            rows.append(row)
            print(json.dumps(dict(mode=mode, host_elapsed_seconds=row["host_elapsed_seconds"],
                                  child_exit=row["child_exit"], problem=row["problem"])), flush=True)
            if row["child_exit"] != 0 or row["problem"] or row["child"] is None:
                result["outcome"] = "failed_without_replacement"
                return 1
        problems = result["quality_problems"]
        frequency = clock.ready["frequency"]
        for row in rows:
            if not row["host_end"]["high_resolution"] or row["host_end"]["frequency"] != frequency or frequency <= 0:
                problems.append(row["mode"]+": unsupported QPC reference")
            if row["max_observation_gap_seconds"] > 2:
                problems.append(row["mode"]+": observation gap")
            if row["host_elapsed_seconds"] <= 0:
                problems.append(row["mode"]+": nonpositive host interval")
            if row["mode"] != "empty" and abs(row["host_utc_span_seconds"]/row["host_elapsed_seconds"]-1) > .05:
                problems.append(row["mode"]+": QPC/UTC disagreement")
        cpu = rows[-1]["child"]["counters"]
        if abs(cpu["cpu_ns"]/cpu["rusage_cpu_ns"]-1) > .05:
            problems.append("CPU/getrusage disagreement")
        if cpu["cpu_ns"]/1e9 > rows[-1]["host_elapsed_seconds"]*1.05:
            problems.append("serial CPU exceeds enclosing host interval")
        result["outcome"] = "qualified_host_envelope" if not problems else "timing_inconclusive"
        return 0
    except BaseException as error:
        result.update(outcome="unavailable_or_failed", problem=type(error).__name__+": "+str(error))
        return 1
    finally:
        if clock is not None:
            try:
                clock.close()
            except Exception as error:
                result["cleanup_problem"] = type(error).__name__
        result["method_hashes_unchanged"] = all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in methods.items())
        write(args.output / "results.json", result)
        print(json.dumps(dict(outcome=result["outcome"], quality_problems=result["quality_problems"],
                              problem=result.get("problem"))), flush=True)


if __name__ == "__main__":
    raise SystemExit(main())
