"""Dated successor launch using the qualified local proxy for public PyPI reads."""
import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import sys
from urllib.parse import urlsplit


HERE = Path(__file__).resolve().parent
PRIOR = HERE.parent / "2026-11-06-native-product-execution-readiness"
PRIVATE = Path("/home/motafeq/.local/share/upgradepilot/pypi-route-repair-2026-11-07")
PACKAGES = ("fastapi", "pytest")


def digest(path):
    return sha256(Path(path).read_bytes()).hexdigest()


def successor_paths_and_command(parent):
    root = Path(parent["destinations"]["product_attempt"]).parent
    attempt = root / "product-attempt-02"
    destinations = dict(product_attempt=str(attempt), task_review=str(root / "task-review-02"))
    argv = list(parent["argv"])
    argv[argv.index("--workspace-store") + 1] = str(attempt / "store")
    argv[argv.index("--save-report") + 1] = str(attempt / "report.json")
    return destinations, argv


def load_launch_inputs():
    binding_path = HERE / "successor-binding.json"
    binding = json.loads(binding_path.read_bytes())
    parent_path = PRIOR / "execution-manifest.json"
    assert digest(parent_path) == binding["prior_manifest_sha256"]
    assert digest(__file__) == binding["launcher_sha256"]
    parent = json.loads(parent_path.read_bytes())
    destinations, argv = successor_paths_and_command(parent)
    assert binding["destinations"] == destinations and binding["argv"] == argv
    for key in ("bound_files_sha256", "installed_files_sha256"):
        assert all(digest(path) == expected for path, expected in parent[key].items()), key
    assert parent["interpreter"]["invocation"] == sys.executable
    proxy = os.environ["https_proxy"]
    url = urlsplit(proxy)
    assert url.scheme == "http" and url.hostname in {"127.0.0.1", "localhost", "::1"} and url.port == 8080
    assert not (url.username or url.password or url.query or url.fragment) and url.path in {"", "/"}
    assert sha256(proxy.encode()).hexdigest() == binding["proxy_sha256"]
    spec = importlib.util.spec_from_file_location("qualified_launch", PRIOR / "launch_product.py")
    launcher = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(launcher)
    env = launcher.child_environment(parent["installed"])
    env.update(https_proxy=proxy, no_proxy="api.github.com", NO_PROXY="api.github.com")
    return binding, parent, launcher, env


def verify_in_child():
    """Exercise the normal Requests environment merge and then the actual PyPI client."""
    from dataclasses import asdict
    from requests import Response
    from requests.adapters import BaseAdapter
    from requests.utils import select_proxy
    from upgradepilot.caller_signature.acquisition import AcquisitionPolicy, AcquisitionSession
    from upgradepilot.pypi.release import PyPIReleaseIndexClient

    proxy = os.environ["https_proxy"]
    assert "GITHUB_TOKEN" not in os.environ
    checks = []

    class CheckRoute(BaseAdapter):
        def send(self, request, **kwargs):
            host = urlsplit(request.url).hostname
            selected = select_proxy(request.url, kwargs["proxies"])
            if host == "api.github.com":
                assert selected is None and request.headers["Authorization"] == "Bearer synthetic-route-control"
            else:
                assert host == "pypi.org" and selected == proxy and "Authorization" not in request.headers
            assert kwargs["verify"]
            checks.append(dict(host=host, proxied=bool(selected), auth_header_present="Authorization" in request.headers))
            response = Response()
            response.status_code, response.url, response.request = 200, request.url, request
            response._content, response._content_consumed = b"{}", True
            return response

        def close(self):
            pass

    with AcquisitionSession(policy=AcquisitionPolicy(), token="synthetic-route-control") as session:
        session.mount("https://", CheckRoute())
        session.get("https://api.github.com/rate_limit")
        session.get("https://pypi.org/pypi/fastapi/json")
    observations = []
    for package in PACKAGES:
        with AcquisitionSession(policy=AcquisitionPolicy(), token=None) as session:
            with session.stage("pypi_route_verification"):
                index = PyPIReleaseIndexClient(session=session).get_release_index(package)
            receipt, = session.acquisition_receipt().requests
            observations.append(dict(package=package, state=index.state, receipt=asdict(receipt)))
        Path("route-proof.json").write_text(json.dumps(dict(offline_route_checks=checks, indices=observations), indent=2) + "\n")
    return 0 if all(row["state"] == "available" and row["receipt"]["status"] == 200 for row in observations) else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--verify-route", action="store_true")
    mode.add_argument("--verify-child", action="store_true", help=argparse.SUPPRESS)
    mode.add_argument("--execute-live", action="store_true", help="Activate the separately reviewed successor capture.")
    args = parser.parse_args()
    if args.verify_child:
        return verify_in_child()
    binding, parent, launcher, env = load_launch_inputs()
    proof_root = PRIVATE / "split-route-verification-01"
    if args.verify_route:
        result = launcher.supervise([sys.executable, str(Path(__file__).resolve()), "--verify-child"],
            env, proof_root, parent["clock_directory"], host_limit=60, execution_binding=binding)
        print(json.dumps({key:result.get(key) for key in ("outcome", "child_exit", "host_elapsed_seconds", "timing_quality")}))
        return 0 if result["outcome"] == "child_exited" and result["child_exit"] == 0 else 1
    proof = json.loads((proof_root / "route-proof.json").read_bytes())
    observed_binding = json.loads((proof_root / "execution-manifest.json").read_bytes())
    assert observed_binding == binding
    assert proof["offline_route_checks"] == [dict(host="api.github.com", proxied=False, auth_header_present=True),
        dict(host="pypi.org", proxied=True, auth_header_present=False)]
    assert [row["package"] for row in proof["indices"]] == list(PACKAGES)
    assert all(row["state"] == "available" and row["receipt"]["status"] == 200 for row in proof["indices"])
    for path in binding["destinations"].values():
        if Path(path).exists() or Path(path).is_symlink():
            raise FileExistsError("Reserved successor output already exists.")
    if not args.execute_live:
        print(json.dumps(dict(outcome="successor_route_verified_review_ready", personal_credential_read=False)))
        return 0
    env["GITHUB_TOKEN"] = launcher.read_owned_token(parent["credential_source"])
    result = launcher.supervise(binding["argv"], env, binding["destinations"]["product_attempt"],
        parent["clock_directory"], execution_binding=binding)
    print(json.dumps(result))
    return result["child_exit"] if result["outcome"] == "child_exited" else 12


if __name__ == "__main__":
    raise SystemExit(main())
