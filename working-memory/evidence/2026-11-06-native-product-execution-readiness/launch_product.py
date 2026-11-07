"""Dated normal-product launcher: default check only; live use requires later activation.

Bindings are checked before credential reads/output creation. The supervisor also
serves offline qualification; only its caller supplies a controlled child there.
No acquisition, analysis, HTTP replay or retry is implemented in this launcher.
"""
import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys

HERE = Path(__file__).resolve().parent
REVIEW = HERE.parent / "2026-11-06-native-normal-product-attempt-contract/contract.json"
PROXY_KEYS = ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "http_proxy", "https_proxy", "all_proxy")


def digest(path):
    return sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2) + "\n")


def child_environment(installed):
    env = dict(os.environ)
    for name in (*PROXY_KEYS, "GITHUB_TOKEN", "PYTHONPATH", "PYTHONHOME", "PYTHONSTARTUP", "PYTHONINSPECT"):
        env.pop(name, None)
    env.update(PYTHONPATH=str(installed), PYTHONNOUSERSITE="1", PYTHONDONTWRITEBYTECODE="1")
    return env


def read_owned_token(path):
    """Read only at activated launch; refuse symlinks/foreign or broad permissions."""
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) != 0o600:
            raise ValueError("Credential must be an owned0600 regular file.")
        token = os.read(fd, 8193)
        if len(token) > 8192:
            raise ValueError("Credential outside bounded input size.")
        token = token.decode("ascii").strip()
        if not token or any(c.isspace() for c in token):
            raise ValueError("Credential empty or malformed.")
        return token
    finally:
        os.close(fd)


def verify_manifest(manifest):
    if manifest["format"] != "upgradepilot-native-product-execution-manifest/1":
        raise ValueError("Unknown execution manifest.")
    review = json.loads(REVIEW.read_bytes())
    expected_command = [sys.executable, *review["normal_product"]["proposed_post_repair_argv"]]
    if manifest["argv"] != expected_command:
        raise ValueError("Invocation differs from the frozen case/profile/guards/destinations.")
    if manifest["credential_source"] != review["authentication"]["credential_source"]:
        raise ValueError("Credential source differs from the frozen contract.")
    if manifest["installed"] != str(Path(review["retention"]["runtime"]) / "installed"):
        raise ValueError("Installed runtime differs from the reserved destination.")
    if manifest["clock_directory"] != str(HERE.parent / "2026-11-06-independent-host-timing"):
        raise ValueError("Clock method location differs from the qualified method.")
    if manifest["destinations"] != {k: review["retention"][k] for k in ("product_attempt", "task_review")}:
        raise ValueError("Output destinations differ from the reserved contract.")
    for key in ("acquisition_policy", "source_limits", "analysis_limits", "correspondence_limits", "representation_limits", "retry", "maintainer_task", "transport"):
        if manifest[key] != review[key]:
            raise ValueError("Policy/task differs from the frozen contract: " + key)
    if manifest["outer_host_limit_seconds"] != 900 or not manifest["separate_live_activation_required"]:
        raise ValueError("Outer allowance or activation boundary differs.")
    for path, expected in manifest["bound_files_sha256"].items():
        if digest(path) != expected:
            raise ValueError("Execution binding differs: " + path)
    if str(Path(sys.executable).absolute()) != manifest["interpreter"]["invocation"]:
        raise ValueError("Interpreter invocation differs.")
    if sys.version != manifest["interpreter"]["version"]:
        raise ValueError("Interpreter version differs.")
    installed = Path(manifest["installed"])
    actual = {str(p): digest(p) for p in sorted(installed.rglob("*")) if p.is_file() and "__pycache__" not in p.parts}
    if actual != manifest["installed_files_sha256"]:
        raise ValueError("Installed distribution inventory differs.")
    for name in ("product_attempt", "task_review"):
        path = Path(manifest["destinations"][name])
        if path.exists() or path.is_symlink():
            raise ValueError("Reserved output already exists: " + name)
    credential = Path(manifest["credential_source"])
    info = credential.lstat()  # metadata only; check mode cannot read its value
    if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) != 0o600:
        raise ValueError("Credential metadata does not meet the contract.")
    for path in (installed, Path(manifest["destinations"]["product_attempt"]).parent):
        if not path.is_dir() or path.stat().st_uid != os.getuid() or stat.S_IMODE(path.stat().st_mode) & 0o077:
            raise ValueError("Private runtime/output parent must be owner-only.")
    return dict(outcome="bindings_match_review_ready", provider_calls=0,
                credential_value_read=False, product_attempt_started=False)


def clock_module(directory):
    path = Path(directory) / "run_preflight.py"
    spec = importlib.util.spec_from_file_location("qualified_host_clock", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def supervise(command, env, output, clock_directory, *, host_limit=900, execution_binding=None):
    """One child group, exact logs and host envelope; no automatic replay."""
    os.umask(0o077)
    output = Path(output)
    output.mkdir(mode=0o700, exist_ok=False)
    if execution_binding is not None:
        write_json(output / "execution-manifest.json", execution_binding)
    write_json(output / "intent.json", dict(command=command, host_limit_seconds=host_limit,
        evidence="outer launch supervision only", retries=0, credential_values_logged=False,
        execution_manifest_sha256=digest(output / "execution-manifest.json") if execution_binding is not None else None))
    module = clock_module(clock_directory)
    clock, child, begin, previous = None, None, None, None
    result = dict(outcome="not_started", child_exit=None, confirmed_revision=None,
                  publication_state="unknown_until_exact_inspection", provider_costs="unknown_until_native_receipt")
    try:
        clock = module.HostClock(output)
        begin = clock.command("begin")
        previous = begin
        result.update(observations=0, max_observation_gap_seconds=0)
        with (output / "stdout.txt").open("xb") as out, (output / "stderr.txt").open("xb") as err, (output / "host-samples.jsonl").open("x") as samples:
            child = subprocess.Popen(command, cwd=output, env=env, stdout=out, stderr=err, start_new_session=True)
            while child.poll() is None:
                try:
                    child.wait(timeout=.25)
                except subprocess.TimeoutExpired:
                    pass
                sample = clock.command("sample")
                samples.write(json.dumps(sample) + "\n")
                samples.flush()
                result["observations"] += 1
                result["max_observation_gap_seconds"] = max(result["max_observation_gap_seconds"],
                    (sample["qpc_timestamp"] - previous["qpc_timestamp"]) / begin["frequency"])
                previous = sample
                if sample["elapsed_ticks"] / sample["frequency"] > host_limit:
                    raise TimeoutError("Frozen outer host allowance exhausted.")
        end = clock.command("end")
        result["max_observation_gap_seconds"] = max(result["max_observation_gap_seconds"],
            (end["qpc_timestamp"] - previous["qpc_timestamp"]) / begin["frequency"])
        elapsed = end["elapsed_ticks"] / end["frequency"]
        utc = (end["utc_ticks"] - begin["utc_ticks"]) / 1e7
        problems = []
        if not end["high_resolution"] or end["frequency"] != begin["frequency"]:
            problems.append("host_clock_inconsistent")
        if result["max_observation_gap_seconds"] > 2:
            problems.append("observation_gap")
        if elapsed <= 0 or abs(utc / elapsed - 1) > .05:
            problems.append("host_clock_span_disagreement")
        result.update(outcome="child_exited", child_exit=child.returncode, host_begin=begin,
            host_end=end, host_elapsed_seconds=elapsed, host_utc_span_seconds=utc,
            timing_quality="inconclusive" if problems else "qualified_outer_envelope", timing_problems=problems)
    except BaseException as error:
        result["outcome"] = "interrupted" if isinstance(error, KeyboardInterrupt) else "timeout" if isinstance(error, TimeoutError) else "supervision_failed"
        result["problem_type"] = type(error).__name__  # no arbitrary secret-bearing exception text
        if child is not None:
            module.stop_child(child)
            result["child_exit"] = child.returncode
        if clock is not None and begin is not None:
            try:
                result["stopped_host_interval"] = clock.command("end")
            except Exception:
                result["stopped_host_interval"] = None
    finally:
        if clock is not None:
            try:
                clock.close()
            except Exception as error:
                result["cleanup_problem"] = type(error).__name__
        path = output / "stdout.txt"
        if path.exists():
            matches = re.findall(r"^Confirmed revision: ([0-9a-f]{32})$", path.read_text(), flags=re.MULTILINE)
            result["confirmed_revision"] = matches[-1] if matches else None
        write_json(output / "launch-result.json", result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--execute-live", action="store_true", help="Requires separate later user activation; default only verifies bindings.")
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_bytes())
    checked = verify_manifest(manifest)
    if not args.execute_live:
        print(json.dumps(checked))
        return 0
    # No credential is loaded by imports, manifest checks or offline qualification.
    env = child_environment(manifest["installed"])
    env["GITHUB_TOKEN"] = read_owned_token(manifest["credential_source"])
    result = supervise(manifest["argv"], env, manifest["destinations"]["product_attempt"], manifest["clock_directory"], execution_binding=manifest)
    print(json.dumps(result))
    return result["child_exit"] if result["outcome"] == "child_exited" else 12


if __name__ == "__main__":
    raise SystemExit(main())
