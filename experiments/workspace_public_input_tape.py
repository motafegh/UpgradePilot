"""Bounded anonymous GET recording for the single known-case grounding trial.

Native acquisition clients consume these exact decoded HTTP body bytes. Retained-input
mode matches ordered URLs/status/bytes and has no network fallback. This is research
re-execution, not a product replay/authentication/native-object codec capability.
"""

from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlsplit

from requests import Response

from upgradepilot.github.auth_session import GitHubPublicSession


class PublicInputTape(GitHubPublicSession):
    def __init__(self, root: Path, *, offline=False):
        super().__init__()
        self.root = root
        self.offline = offline
        self.cursor = 0
        self.entries = []
        if offline:
            captured = json.loads((root / "manifest.json").read_text())
            self.entries = captured["requests"]
        else:
            root.mkdir(parents=True, exist_ok=False)
        self.started = (
            captured["trial_started_at"] if offline else datetime.now(UTC).isoformat()
        )

    def now(self):
        return datetime.fromisoformat(self.entries[self.cursor - 1]["received_at"])

    def snapshot(self):
        """Immutable metadata for the inputs consumed up to this publication point."""
        return {
            "trial_started_at": self.started,
            "authentication": "anonymous; no tokens/netrc/cookies",
            "input_boundary": "decoded HTTP body consumed by native clients; not compressed wire bytes",
            "requests": self.entries[: self.cursor],
        }

    def flush(self):
        if not self.offline:
            (self.root / "manifest.json").write_text(
                json.dumps(self.snapshot(), indent=2, sort_keys=True) + "\n"
            )

    def send(self, request, **kwargs):
        url = urlsplit(request.url)
        if (
            request.method != "GET"
            or url.scheme != "https"
            or url.hostname not in {"api.github.com", "pypi.org"}
        ):
            raise ValueError("Trial admits only public GitHub/PyPI HTTPS GETs")
        if "Authorization" in request.headers:
            raise ValueError("Grounding must remain anonymous")
        request.headers.pop("Cookie", None)
        if self.cursor >= 32:
            raise ValueError("Bounded trial request budget exhausted")
        if self.offline:
            if self.cursor >= len(self.entries):
                raise ValueError("Uncaptured request; no network fallback")
            entry = self.entries[self.cursor]
            if request.url != entry["url"]:
                raise ValueError("Retained request ordering/identity mismatch")
            data = (self.root / entry["body"]).read_bytes()
            if (
                len(data) != entry["bytes"]
                or hashlib.sha256(data).hexdigest() != entry["sha256"]
            ):
                raise ValueError("Retained public input digest mismatch")
            response = Response()
            response.status_code = entry["status"]
            response.url = request.url
            response.headers.update(entry["headers"])
            response.request = request
        else:
            response = super().send(request, **kwargs)
            chunks = []
            size = 0
            for chunk in response.iter_content(65_536):
                size += len(chunk)
                if size > 2_000_000:
                    response.close()
                    raise ValueError("Public response exceeds bounded recording size")
                chunks.append(chunk)
            data = b"".join(chunks)
            name = f"response-{self.cursor:03}.body"
            (self.root / name).write_bytes(data)
            self.entries.append(
                {
                    "url": request.url,
                    "status": response.status_code,
                    "body": name,
                    "sha256": hashlib.sha256(data).hexdigest(),
                    "bytes": len(data),
                    "received_at": datetime.now(UTC).isoformat(),
                    "headers": {
                        key: value
                        for key, value in response.headers.items()
                        if key.lower()
                        in {"content-type", "date", "etag", "last-modified"}
                    },
                }
            )
        response._content = data
        response._content_consumed = True
        self.cursor += 1
        self.flush()
        return response

    def assert_consumed(self):
        if self.offline and self.cursor != len(self.entries):
            raise ValueError("Retained input set not fully consumed")
