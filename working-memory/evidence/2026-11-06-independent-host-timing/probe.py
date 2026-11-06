"""Fixed empty/idle/serial-CPU work; no product imports, network or target code."""
import argparse
import json
from pathlib import Path
import resource
import time


def counters():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    return dict(monotonic_ns=time.monotonic_ns(),
        raw_ns=time.clock_gettime_ns(time.CLOCK_MONOTONIC_RAW),
        cpu_ns=time.process_time_ns(),
        rusage_cpu_ns=round((usage.ru_utime + usage.ru_stime) * 1e9))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("empty", "idle", "cpu"))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    before = counters()
    if args.mode == "idle":
        time.sleep(10.0)
    elif args.mode == "cpu":
        while time.process_time_ns() - before["cpu_ns"] < 10_000_000_000:
            pass
    after = counters()
    with args.output.open("x") as stream:
        json.dump(dict(mode=args.mode, counters={k: after[k]-before[k] for k in before},
                       clock_implementations={k: vars(time.get_clock_info(k))
                                              for k in ("monotonic", "process_time", "perf_counter")}), stream, indent=2)
        stream.write("\n")
