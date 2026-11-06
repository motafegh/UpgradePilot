"""Focused successor-cold and final manifest checks; never activates live launch."""
import argparse
from copy import deepcopy
import json
import os
from pathlib import Path
import shutil
import socket
import subprocess
import sys
from unittest.mock import patch

from launch_product import child_environment, digest, read_owned_token, supervise, verify_manifest, write_json

HERE = Path(__file__).resolve().parent
PRIVATE = Path("/home/motafeq/.local/share/upgradepilot/native-signature-kubernetes-dashboard-token-api-pr-20-httpx-2026-11-06")


def cold_controls(output):
    prior = PRIVATE / "method-qualification-01"
    positive = json.loads((prior / "results.json").read_bytes())
    method = output / "cold_review.py"
    shutil.copyfile(HERE / "cold_review.py", method)
    write_json(output / "contract.json", dict(method_sha256=digest(method),
        original_positive_packet_sha256=digest(prior / "results.json"),
        controls=["exact_positive", "missing_revision", "changed_report_bytes"], real_provider_calls=0))
    command = [sys.executable, str(method), "--installed", str(PRIVATE / "runtime/installed"),
        "--store", str(prior / "composition/store"), "--revision", positive["composition"]["confirmed_revision"],
        "--report", str(prior / "composition/report.json"), "--output", str(output / "positive")]
    env = child_environment(PRIVATE / "runtime/installed")
    def run(name, argv):
        with (output / (name + ".log")).open("xb") as log:
            return subprocess.run(argv, cwd=output, env=env, stdout=log, stderr=subprocess.STDOUT, timeout=120).returncode
    assert run("positive", command) == 0
    bad = list(command)
    bad[bad.index("--revision") + 1] = "0" * 32
    bad[bad.index("--output") + 1] = str(output / "missing-revision")
    assert run("missing-revision", bad) == 9
    rejected = json.loads((output / "missing-revision.log").read_bytes())
    assert rejected == dict(outcome="rejected", reason="missing_checkpoint_revision")
    changed = output / "changed-report.json"
    changed.write_bytes((prior / "composition/report.json").read_bytes() + b" ")
    bad = list(command)
    bad[bad.index("--report") + 1] = str(changed)
    bad[bad.index("--output") + 1] = str(output / "changed-report")
    assert run("changed-report", bad) != 0
    assert "AssertionError" in (output / "changed-report.log").read_text()
    assert "Exception ignored" not in (output / "changed-report.log").read_text()
    assert digest(method) == digest(HERE / "cold_review.py")
    return dict(outcome="passed", cold_method_sha256=digest(method), exact_positive=True,
        missing_revision_reason=rejected["reason"], changed_report_bytes_refused=True,
        hook_cleanup_on_failure=True, real_provider_calls=0, personal_credential_value_read=False)


def binding_controls(output, manifest_path):
    manifest = json.loads(manifest_path.read_bytes())
    credential = Path(manifest["credential_source"])
    original_read = Path.read_bytes
    def guarded_read(path):
        if path.absolute() == credential.absolute():
            raise AssertionError("Personal credential value read during check.")
        return original_read(path)
    with patch.object(Path, "read_bytes", guarded_read), patch("launch_product.read_owned_token", side_effect=AssertionError("secret loading forbidden")), patch.object(
            socket.socket, "connect", side_effect=AssertionError("provider calls forbidden")):
        checked = verify_manifest(manifest)
        assert checked["outcome"] == "bindings_match_review_ready"
        negatives = []
        for name in ("wrong_head", "wrong_product_hash", "different_destination", "raised_policy_limit", "different_clock_method"):
            bad = deepcopy(manifest)
            if name == "wrong_head":
                bad["argv"][bad["argv"].index("--expected-head") + 1] = "0" * 40
            elif name == "wrong_product_hash":
                path = next(p for p in bad["bound_files_sha256"] if "/src/upgradepilot/" in p)
                bad["bound_files_sha256"][path] = "0" * 64
            elif name == "different_destination":
                bad["destinations"]["product_attempt"] += "-different"
            elif name == "raised_policy_limit":
                bad["acquisition_policy"]["github_requests"] += 1
            else:
                bad["clock_directory"] = str(output / "unqualified-clock")
            try:
                verify_manifest(bad)
            except ValueError:
                negatives.append(name)
            else:
                raise AssertionError("Manifest corruption admitted: " + name)
        original_exists = Path.exists
        with patch.object(Path, "exists", lambda p: True if str(p) == manifest["destinations"]["product_attempt"] else original_exists(p)):
            try:
                verify_manifest(manifest)
            except ValueError as error:
                assert "already exists" in str(error)
                negatives.append("existing_output")
            else:
                raise AssertionError("Existing output admitted.")
    with patch.dict(os.environ, {"GITHUB_TOKEN": "synthetic-inherited", "HTTP_PROXY": "http://invalid", "PYTHONPATH": "/poison", "PYTHONHOME": "/poison"}):
        env = child_environment(manifest["installed"])
        assert "GITHUB_TOKEN" not in env and "HTTP_PROXY" not in env and "PYTHONHOME" not in env
        assert env["PYTHONPATH"] == manifest["installed"]
    token = output / "synthetic-credential"
    token.write_text("synthetic-offline-control\n")
    token.chmod(0o600)
    assert read_owned_token(token) == "synthetic-offline-control"
    token.chmod(0o644)
    try:
        read_owned_token(token)
    except ValueError:
        pass
    else:
        raise AssertionError("Broad credential permissions admitted.")
    token.chmod(0o600)
    link = output / "synthetic-credential-link"
    link.symlink_to(token)
    try:
        read_owned_token(link)
    except OSError:
        pass
    else:
        raise AssertionError("Symlink credential admitted.")
    # Qualify the final intent-binding branch without launching product/provider
    # work or loading the personal credential. Its command is visibly a control.
    intent = supervise([sys.executable, "-c", "raise SystemExit(7)"], child_environment(manifest["installed"]),
        output / "bound-intent-control", manifest["clock_directory"], execution_binding=manifest)
    assert intent["outcome"] == "child_exited" and intent["child_exit"] == 7
    preserved = output / "bound-intent-control/execution-manifest.json"
    assert preserved.read_bytes() == manifest_path.read_bytes()
    assert json.loads((output / "bound-intent-control/intent.json").read_bytes())["execution_manifest_sha256"] == digest(manifest_path)
    return dict(outcome="passed", manifest_sha256=digest(manifest_path), default_check=checked,
        corruption_refusals=negatives, inherited_environment_sanitized=True,
        synthetic_owned_token_accepted=True, broad_mode_and_symlink_refused=True,
        exact_manifest_retained_before_control_dispatch=True, real_provider_calls=0, personal_credential_value_read=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=("cold", "bindings"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args()
    os.umask(0o077)
    args.output.mkdir(mode=0o700, exist_ok=False)
    shutil.copyfile(Path(__file__), args.output / "qualify_readiness.py")
    summary = cold_controls(args.output) if args.phase == "cold" else binding_controls(args.output, args.manifest)
    write_json(args.output / "results.json", summary)
    print(json.dumps(summary))


if __name__ == "__main__":
    main()
