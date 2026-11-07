"""Finite public PyPI controls; passive stage observation, no product repair/retry.

Run only through the dated supervisor/contract. Raw exceptions and public network
addresses stay in the private output; public reporting selects safe categories.
"""
import argparse
from dataclasses import asdict
import http.client
import json
import os
from pathlib import Path
import socket
import ssl
import subprocess
import time
from unittest.mock import patch

from upgradepilot.caller_signature.acquisition import AcquisitionPolicy, AcquisitionSession
from upgradepilot.pypi.release import PyPIReleaseIndexClient

URLS = {name: "https://pypi.org/pypi/" + name + "/json" for name in ("fastapi", "pytest")}
WINDOWS_CURL = Path("/mnt/c/Windows/System32/curl.exe")


def write(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


def product_probe(package, output):
    events = []
    def event(stage, state, **data):
        if len(events) >= 128:
            raise RuntimeError("Diagnostic stage-event allowance exhausted.")
        item = dict(stage=stage, state=state, raw_counter=time.clock_gettime(time.CLOCK_MONOTONIC_RAW), **data)
        events.append(item)
        with (output / (package + "-events.jsonl")).open("a") as stream:
            stream.write(json.dumps(item) + "\n")
    resolve, connect = socket.getaddrinfo, socket.socket.connect
    handshake, response_begin = ssl.SSLSocket.do_handshake, http.client.HTTPResponse.begin
    def observed_resolve(host, port, *args, **kwargs):
        assert host in ("pypi.org", b"pypi.org") and port == 443
        event("dns", "started")
        try:
            addresses = resolve(host, port, *args, **kwargs)
        except Exception as error:
            event("dns", "failed", error_type=type(error).__name__)
            raise
        event("dns", "resolved", addresses=[dict(family=int(a[0]), address=a[4][0]) for a in addresses])
        return addresses
    def observed_connect(sock, address):
        event("tcp", "started", family=int(sock.family), address=address[0])
        try:
            value = connect(sock, address)
        except Exception as error:
            event("tcp", "failed", error_type=type(error).__name__)
            raise
        event("tcp", "connected", family=int(sock.family))
        return value
    def observed_handshake(sock, *args, **kwargs):
        event("tls", "started", certificate_verification=int(sock.context.verify_mode))
        try:
            value = handshake(sock, *args, **kwargs)
        except Exception as error:
            event("tls", "failed", error_type=type(error).__name__)
            raise
        event("tls", "established", version=sock.version())
        return value
    def observed_headers(response, *args, **kwargs):
        event("http_headers", "started")
        try:
            value = response_begin(response, *args, **kwargs)
        except Exception as error:
            event("http_headers", "failed", error_type=type(error).__name__)
            raise
        event("http_headers", "received", status=response.status)
        return value
    class ObservedSession(AcquisitionSession):
        def send(self, request, **kwargs):
            assert request.url == URLS[package]
            assert "Authorization" not in request.headers
            event("http_dispatch", "started", anonymous=True)
            return super().send(request, **kwargs)
        def _request_once(self, method, url, **kwargs):
            try:
                return super()._request_once(method, url, **kwargs)
            except Exception as error:
                chain, current, seen = [], error, set()
                while current is not None and id(current) not in seen and len(chain) < 12:
                    seen.add(id(current))
                    chain.append(dict(type=type(current).__module__ + "." + type(current).__name__, message=str(current)[:800]))
                    current = current.__cause__ or current.__context__
                event("request", "failed", exception_chain=chain)
                raise
    with ObservedSession(token=None, policy=AcquisitionPolicy()) as session:
        with patch.object(socket, "getaddrinfo", observed_resolve), patch.object(socket.socket, "connect", observed_connect), patch.object(
                ssl.SSLSocket, "do_handshake", observed_handshake), patch.object(http.client.HTTPResponse, "begin", observed_headers):
            with session.stage("pypi_transport_diagnostic"):
                index = PyPIReleaseIndexClient(session=session).get_release_index(package)
        result = dict(control="installed_product_index", package=package, index_state=index.state,
            index_detail=getattr(index, "detail", None), release_versions=len(getattr(index, "release_versions", ())),
            transport=asdict(session.acquisition_receipt()), events=events)
    write(output / (package + ".json"), result)
    print(json.dumps(dict(control="installed_product_index", package=package, index_state=index.state,
        provider_requests=session.provider_requests, body_bytes=session.body_bytes)), flush=True)
    return result


def curl_probe(output, *, family=None, windows=False):
    label = "windows-curl" if windows else "linux-curl" + ("-" + str(family) if family else "")
    command = [str(WINDOWS_CURL) if windows else "/usr/bin/curl", "-q", "--noproxy", "*", "--http1.1",
        "--proto", "=https", "--proto-redir", "=https", "--max-redirs", "0", "--retry", "0",
        "--connect-timeout", "3.05", "--max-time", "20", "--max-filesize", "8388608",
        "--user-agent", "UpgradePilot/0.0.0", "--header", "Accept: application/json",
        "--silent", "--show-error", "--output", "NUL" if windows else "/dev/null", "--write-out", "%{json}"]
    if family:
        command.append("-" + str(family))
    command.append(URLS["fastapi"])
    result = subprocess.run(command, capture_output=True, env=dict(os.environ),
        cwd="/mnt/c/Windows" if windows else output, timeout=30)
    (output / (label + "-stderr.txt")).write_bytes(result.stderr)
    (output / (label + "-writeout.json")).write_bytes(result.stdout)
    metrics = json.loads(result.stdout.decode("utf-8-sig"))
    observation = dict(control=label, exit=result.returncode, metrics=metrics, command=command)
    write(output / (label + ".json"), observation)
    print(json.dumps(dict(control=label, exit=result.returncode, http_code=metrics.get("http_code"),
                         error=metrics.get("errormsg"))), flush=True)
    return observation


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=("baseline", "families", "host"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--families", type=Path)
    args = parser.parse_args()
    os.umask(0o077)
    assert "GITHUB_TOKEN" not in os.environ
    assert all(name not in os.environ for name in ("HTTP_PROXY","HTTPS_PROXY","ALL_PROXY","http_proxy","https_proxy","all_proxy"))
    if args.phase == "baseline":
        controls = [product_probe(package, args.output) for package in ("fastapi", "pytest")]
        controls.append(curl_probe(args.output))
    else:
        baseline = json.loads((args.baseline / "worker-results.json").read_bytes())
        assert baseline["phase"] == "baseline"
        assert all(not row["transport"]["requests"][0]["status"] for row in baseline["controls"][:2])
        assert not baseline["controls"][2]["metrics"]["http_code"]
        families = {a["family"] for row in baseline["controls"][:2] for e in row["events"] if e["stage"] == "dns" and e["state"] == "resolved" for a in e["addresses"]}
        assert families, "Resolution failure does not activate family controls."
        if args.phase == "families":
            controls = [curl_probe(args.output, family=version) for version, af in ((4, socket.AF_INET),(6, socket.AF_INET6)) if af in families]
        else:
            earlier = json.loads((args.families / "worker-results.json").read_bytes())
            assert earlier["phase"] == "families" and all(not c["metrics"]["http_code"] for c in earlier["controls"])
            assert WINDOWS_CURL.is_file()
            controls = [curl_probe(args.output, windows=True)]
    write(args.output / "worker-results.json", dict(phase=args.phase, controls=controls,
        dispatched_http_requests=len(controls), new_product_attempt=False, personal_credential_read=False))


if __name__ == "__main__":
    main()
