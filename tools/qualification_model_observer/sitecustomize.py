"""Opt-in, metadata-only observer for one local model HTTP request boundary.

Installed only in one child process via PYTHONPATH=<this directory>, with the
already-installed UpgradePilot executable. Does not override UpgradePilot
imports, model payloads, request routing, response parsing or retry behavior.
This is instrumentation and must be reported as such, not an unmodified run.
"""

from __future__ import annotations

import datetime
import json
import os
from pathlib import Path
import time


_LOG = os.environ.get("UP_QUALIFICATION_MODEL_EVENT_LOG")
_ENDPOINT = os.environ.get(
    "UP_QUALIFICATION_MODEL_ENDPOINT",
    "http://127.0.0.1:18080/v1/chat/completions",
)


def _record(event: str, *, status: int | None = None, body_bytes: int | None = None,
            error_kind: str | None = None) -> None:
    """Append private metadata only; never retain prompts, response bodies or auth."""

    if not _LOG:
        return
    try:
        path = Path(_LOG)
        parent = path.parent
        if (
            not path.is_absolute() or not parent.is_dir()
            or parent.is_symlink() or parent.stat().st_uid != os.geteuid()
            or parent.stat().st_mode & 0o077
        ):
            return
        data = {
            "schema": "upgradepilot.qualification.model_request_event/1",
            "event": event,
            "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "monotonic_ns": time.monotonic_ns(),
            "pid": os.getpid(),
            "endpoint": _ENDPOINT,
            "http_status": status,
            "request_bytes": body_bytes,
            "error_kind": error_kind,
        }
        flags = os.O_WRONLY | os.O_APPEND | os.O_CREAT
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        fd = os.open(str(path), flags, 0o600)
        try:
            st = os.fstat(fd)
            if st.st_uid != os.geteuid() or (st.st_mode & 0o077):
                return
            os.write(fd, (json.dumps(data, sort_keys=True) + "\n").encode("utf-8"))
        finally:
            os.close(fd)
    except (OSError, TypeError, ValueError):
        # Observer faults must not alter the public product result; an absent
        # event receipt fails the positive model-activation evidence requirement.
        return


if _LOG:
    import requests.sessions

    _original_send = requests.sessions.Session.send

    def _observed_send(self, request, **kwargs):
        if request.method != "POST" or request.url != _ENDPOINT:
            return _original_send(self, request, **kwargs)
        body = request.body
        size = len(body) if isinstance(body, (str, bytes, bytearray)) else None
        _record("send_entered", body_bytes=size)
        try:
            response = _original_send(self, request, **kwargs)
        except Exception as error:
            _record("transport_exception", body_bytes=size, error_kind=type(error).__name__)
            raise
        _record("http_response_received", status=response.status_code, body_bytes=size)
        return response

    requests.sessions.Session.send = _observed_send
