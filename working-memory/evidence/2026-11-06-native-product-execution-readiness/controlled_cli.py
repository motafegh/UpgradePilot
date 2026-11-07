"""Offline normal CLI composition; authored HTTP adapter is not in the live argv."""
import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import runpy
import socket
import sys
from types import SimpleNamespace
from unittest.mock import patch
from urllib.parse import urlsplit

from upgradepilot.caller_signature.acquisition import AcquisitionPolicy, AcquisitionSession


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", type=Path, required=True)
    parser.add_argument("--adapter", type=Path, required=True)
    parser.add_argument("--expected-head", required=True)
    parser.add_argument("--base", required=True)
    args = parser.parse_args()
    assert importlib.util.find_spec("experiments") is None
    raw = json.loads(args.fixture.read_bytes())
    spec = importlib.util.spec_from_file_location("unchanged_authored_http", args.adapter)
    adapter_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(adapter_module)
    case = SimpleNamespace(body=raw["body"], catalog=SimpleNamespace(
        scopes=[SimpleNamespace(**s) for s in raw["scopes"]], files=[SimpleNamespace(**f) for f in raw["files"]]))

    class HeaderCheckedHTTP(adapter_module.RetainedHTTP):
        def send(self, request, **kwargs):
            expected = "Bearer synthetic-offline-control" if urlsplit(request.url).hostname == "api.github.com" else None
            assert request.headers.get("Authorization") == expected, "Incorrect synthetic auth scope."
            return super().send(request, **kwargs)

    # Product CLI constructs this actual session, with the token selected by its
    # normal auth path. Only HTTP dispatch is supplied by the control adapter.
    sessions = []
    def session_factory(*, token, policy):
        assert token == "synthetic-offline-control" and policy == AcquisitionPolicy()
        session = AcquisitionSession(token=token, policy=policy)
        session.mount("https://", HeaderCheckedHTTP(case))
        sessions.append(session)
        return session

    identity = raw["body"]["acquisition"]["native_inputs"]["identity"]
    sys.argv = ["upgradepilot", identity["repository"], str(identity["number"]), "--evidence-profile", "caller-signature",
        "--github-auth", "token-env", "--expected-base", args.base, "--expected-head", args.expected_head,
        "--workspace-store", str(Path.cwd() / "store"), "--save-report", str(Path.cwd() / "report.json")]
    with patch("upgradepilot.cli.AcquisitionSession", side_effect=session_factory), patch.object(
            socket.socket, "connect", side_effect=AssertionError("control network forbidden")):
        try:
            runpy.run_module("upgradepilot", run_name="__main__")
        except SystemExit as error:
            code = error.code
    assert len(sessions) == 1
    session = sessions[0]
    Path("controlled-costs.json").write_text(json.dumps(dict(exit=code, github=session.github_requests,
        provider=session.provider_requests, response_bytes=session.body_bytes, header_scope_checked=True,
        fixture_sha256=sha256(args.fixture.read_bytes()).hexdigest())) + "\n")
    raise SystemExit(code)


if __name__ == "__main__":
    main()
