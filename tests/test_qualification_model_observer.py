"""Offline proof for the narrowly scoped model POST telemetry observer."""

from __future__ import annotations

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import threading
import unittest


_OBSERVER_DIR = Path(__file__).resolve().parents[1] / "tools" / "qualification_model_observer"


class _Server(BaseHTTPRequestHandler):
    received: list[bytes] = []

    def do_POST(self) -> None:
        data = self.rfile.read(int(self.headers["Content-Length"]))
        self.server.received.append(data)
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"okay":true}')

    def do_GET(self) -> None:
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"read-only")

    def log_message(self, format: str, *args: object) -> None:
        return


class ModelObserverTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory(prefix="up-model-observer-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.assertEqual(self.root.stat().st_mode & 0o077, 0)

    def _child(self, code: str, url: str, logname: str = "events.jsonl") -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["PYTHONPATH"] = str(_OBSERVER_DIR)
        env["UP_QUALIFICATION_MODEL_EVENT_LOG"] = str(self.root / logname)
        env["UP_QUALIFICATION_MODEL_ENDPOINT"] = url
        return subprocess.run(
            [sys.executable, "-c", code],
            env=env, capture_output=True, text=True, timeout=8, check=False,
        )

    def test_records_response_metadata_only_without_rewriting_payload(self) -> None:
        _Server.received = []
        server = ThreadingHTTPServer(("127.0.0.1", 0), _Server)
        server.received = []
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        endpoint = f"http://127.0.0.1:{server.server_port}/v1/chat/completions"
        result = self._child(
            "import requests\n"
            "s=requests.Session();s.trust_env=False\n"
            f"r=s.post({endpoint!r},data=b'SECRET_SENTINEL',timeout=2)\n"
            "print(r.status_code, r.text)\n",
            endpoint,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(server.received, [b"SECRET_SENTINEL"])
        self.assertEqual(result.stdout.strip(), '200 {"okay":true}')
        logpath = self.root / "events.jsonl"
        rows = [json.loads(line) for line in logpath.read_text().splitlines()]
        self.assertEqual([x["event"] for x in rows], ["send_entered", "http_response_received"])
        self.assertEqual(rows[1]["http_status"], 200)
        self.assertEqual(rows[0]["request_bytes"], len(b"SECRET_SENTINEL"))
        self.assertNotIn("SECRET_SENTINEL", logpath.read_text())
        self.assertEqual(logpath.stat().st_mode & 0o077, 0)

    def test_refused_transport_has_attempt_but_not_received_response(self) -> None:
        s = socket.socket()
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
        s.close()
        endpoint = f"http://127.0.0.1:{port}/v1/chat/completions"
        result = self._child(
            "import requests\n"
            "s=requests.Session();s.trust_env=False\n"
            f"try: s.post({endpoint!r},data='x',timeout=0.5)\n"
            "except requests.RequestException: print('transport failed')\n",
            endpoint,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("transport failed", result.stdout)
        rows = [json.loads(x) for x in (self.root / "events.jsonl").read_text().splitlines()]
        self.assertEqual([x["event"] for x in rows], ["send_entered", "transport_exception"])
        self.assertEqual(rows[1]["error_kind"], "ConnectionError")

    def test_other_endpoint_or_method_not_counted(self) -> None:
        server = ThreadingHTTPServer(("127.0.0.1", 0), _Server)
        server.received = []
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        endpoint = f"http://127.0.0.1:{server.server_port}/v1/chat/completions"
        result = self._child(
            "import requests\n"
            "s=requests.Session();s.trust_env=False\n"
            f"r=s.get({endpoint!r},timeout=2)\n"
            f"p=s.post({(endpoint + '/other')!r},data='not-logged',timeout=2)\n"
            "print(r.status_code,p.status_code)\n",
            endpoint,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "200 200")
        self.assertEqual(server.received, [b"not-logged"])
        self.assertFalse((self.root / "events.jsonl").exists())

    def test_installed_project_import_remains_in_site_packages(self) -> None:
        result = self._child(
            "import upgradepilot.cli\n"
            "print(upgradepilot.cli.__file__)\n",
            "http://127.0.0.1:18080/v1/chat/completions",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("site-packages/upgradepilot/cli.py", result.stdout)
        self.assertNotIn("/src/upgradepilot/", result.stdout)


if __name__ == "__main__":
    unittest.main()
