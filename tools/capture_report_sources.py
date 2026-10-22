"""Capture normal investigation HTTP inputs alongside its report, for utility preparation.

Run ``python -m tools.capture_report_sources --contract FILE --output PRIVATE_NEW_DIR``.
The contract names one exact case and acquisition limits; it is not a study protocol.
``capture_normal_report`` calls the unchanged application and report projection. A scoped
HTTPAdapter observer tees decoded response chunks at their normal consumption point.
This preserves PyPI body-stage failures instead of eagerly buffering them at request time.
The source packet contains HTTP observations only; report findings never enter it.

Only anonymous public HTTPS GETs to GitHub/PyPI are admitted. Model calls, limit overruns
and identity drift stop the diagnostic, retaining partial sources without a normal report.
Bodies are private, not wire captures; no replay, semantic or utility acceptance is implied.
The CLI deadline uses POSIX signals (the project's WSL control plane), not a portable runner.
"""

from __future__ import annotations

import argparse
import json
import os
import signal
import time
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from hashlib import sha256
from pathlib import Path
from unittest.mock import patch
from urllib.parse import urlsplit

from requests import PreparedRequest, Response
from requests.adapters import HTTPAdapter

from upgradepilot.investigation import investigate_public_pull_request
from upgradepilot.report import render_investigation_report
from upgradepilot.report_file import save_report
from upgradepilot.report_projection import project_investigation_report

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
ALLOWED_HOSTS = {"api.github.com", "pypi.org"}


class CaptureStopped(BaseException):
    """Diagnostic control flow, intentionally outside product provider Exception handlers.

    A denied model POST must not become a fabricated provider-unavailable normal result.
    This is caught by this tool's top-level capture boundary, like a cancellation.
    """

    def __init__(self, reason: str):
        self.reason = reason
        super().__init__(reason)


@dataclass(frozen=True)
class CaptureLimits:
    max_requests: int
    max_body_bytes: int
    max_total_body_bytes: int
    max_elapsed_seconds: int

    def __post_init__(self) -> None:
        if any(type(v) is not int or v <= 0 for v in asdict(self).values()):
            raise ValueError("Capture limits must be positive integers")


def _write_private(path: Path, data: bytes) -> None:
    with os.fdopen(
        os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), "wb"
    ) as stream:
        stream.write(data)


def _write_owned_json(path: Path, value: object) -> None:
    """Replace only this new capture's own index/receipt, keeping interruptions inspectable."""
    temporary = path.with_name(path.name + ".tmp")
    try:
        _write_private(temporary, (json.dumps(value, indent=2) + "\n").encode())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


class HTTPSourceCapture:
    """One synchronous normal run's request/consumed-byte ledger; no domain interpretation."""

    def __init__(self, directory: Path, limits: CaptureLimits):
        self.directory = directory
        directory.mkdir(mode=0o700)
        self.limits = limits
        self.started = time.monotonic()
        self.rows: list[dict] = []
        self.responses: list[Response] = []
        self.total_bytes = 0
        self._write_index()

    def _write_index(self) -> None:
        _write_owned_json(
            self.directory / "index.json",
            {
                "format": "upgradepilot.diagnostic-http-sources/1",
                "meaning": "Normal producer HTTP observations, not findings or expected answers",
                "body_representation": "Requests decoded entity bytes, not wire compression",
                "body_hash_scope": "Retained response prefix; full body only for body_complete",
                "requests": self.rows,
            },
        )

    def check_deadline(self) -> None:
        if time.monotonic() - self.started >= self.limits.max_elapsed_seconds:
            raise CaptureStopped("elapsed_limit")

    def _admit_request(self, request: PreparedRequest) -> None:
        self.check_deadline()
        if request.method != "GET":
            raise CaptureStopped("non_get_or_model_call_not_admitted")
        url = urlsplit(request.url)
        if (
            url.scheme != "https"
            or url.hostname not in ALLOWED_HOSTS
            or url.port not in (None, 443)
            or url.username
            or url.password
        ):
            raise CaptureStopped("destination_not_admitted")
        if any(
            key.lower() in {"authorization", "cookie", "proxy-authorization"}
            for key in request.headers
        ):
            raise CaptureStopped("credential_header_not_admitted")
        if len(self.rows) >= self.limits.max_requests:
            raise CaptureStopped("request_limit")

    def send(self, original_send, adapter, request, **kwargs):
        self._admit_request(request)
        row = {
            "number": len(self.rows) + 1,
            "method": request.method,
            "url": request.url,
            "started_at": datetime.now(UTC).isoformat(),
            "state": "request_started",
        }
        self.rows.append(row)
        self._write_index()
        try:
            response = original_send(adapter, request, **kwargs)
        except BaseException as error:
            row.update(
                state="request_failed",
                error_type=type(error).__name__,
                finished_at=datetime.now(UTC).isoformat(),
            )
            self._write_index()
            raise
        row.update(
            status=response.status_code,
            response_url=response.url,
            headers={
                key: response.headers[key]
                for key in ("Content-Length", "Content-Type", "Content-Encoding")
                if key in response.headers
            },
        )
        self._observe_body(response, row)
        self.responses.append(response)
        return response

    def _observe_body(self, response: Response, row: dict) -> None:
        filename = f"{row['number']:04d}.body"
        stream = os.fdopen(
            os.open(
                self.directory / filename, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600
            ),
            "wb",
        )
        row.update(body=filename, state="response_headers_received")
        original_iterator, original_close = response.iter_content, response.close
        body_hash, length, finished = sha256(), 0, False

        def finish(state: str, error: BaseException | None = None) -> None:
            nonlocal finished
            if finished:
                return
            finished = True
            stream.close()
            row.update(
                state=state,
                body_bytes=length,
                body_sha256=body_hash.hexdigest(),
                finished_at=datetime.now(UTC).isoformat(),
            )
            if error is not None:
                row["error_type"] = type(error).__name__
            self._write_index()

        def retain(chunk: bytes) -> None:
            nonlocal length
            self.check_deadline()
            remaining = min(
                self.limits.max_body_bytes - length,
                self.limits.max_total_body_bytes - self.total_bytes,
            )
            retained = chunk[:remaining]
            stream.write(retained)
            body_hash.update(retained)
            length += len(retained)
            self.total_bytes += len(retained)
            if len(retained) != len(chunk):
                raise CaptureStopped("body_byte_limit")

        def observed_iterator(*args, **kwargs):
            if finished:
                yield from original_iterator(*args, **kwargs)
                return
            try:
                for chunk in original_iterator(*args, **kwargs):
                    if not isinstance(chunk, bytes):
                        raise CaptureStopped("non_byte_body_consumption")
                    retain(chunk)
                    yield chunk
            except GeneratorExit:
                # Consumer closure is not a body transport error. Its close below records
                # the retained prefix; normal provider code still owns why it stopped.
                finish("partial_body" if length else "body_not_consumed")
                raise
            except BaseException as error:
                finish(
                    "capture_stopped"
                    if isinstance(error, CaptureStopped)
                    else "body_failed",
                    error,
                )
                raise
            else:
                finish("body_complete")

        def observed_close():
            finish("partial_body" if length else "body_not_consumed")
            return original_close()

        response.iter_content, response.close = observed_iterator, observed_close
        # HTTPAdapter returns an unread response. Observe its normal consumer rather than
        # materializing the body here; client error categories depend on that ordering.
        self._write_index()

    @contextmanager
    def observe(self) -> Iterator[None]:
        original_send = HTTPAdapter.send

        def send(adapter, request, **kwargs):
            return self.send(original_send, adapter, request, **kwargs)

        try:
            with patch.object(HTTPAdapter, "send", send):
                yield
        finally:
            for response in self.responses:
                response.close()
            self._write_index()


def _report_identity(report) -> dict[str, str]:
    identity = {fact.name: fact.value for fact in report.identity}
    dependency = next(a for a in report.assessments if a.assessment_id == "dependency")
    identity.update(
        {
            f.name: f.value
            for f in dependency.facts
            if f.name in {"package", "old_version", "proposed_version"}
        }
    )
    return identity


def capture_normal_report(contract: dict, output: Path) -> dict:
    """Retain one exact normal result and source packet, or explicit incomplete evidence."""
    output = output.resolve()
    if output.is_relative_to(REPOSITORY_ROOT):
        raise ValueError("Capture bodies must be outside the repository")
    limits = CaptureLimits(**contract["limits"])
    expected = contract["expected_identity"]
    if set(expected) != {
        "repository",
        "pull_number",
        "base_sha",
        "head_sha",
        "package",
        "old_version",
        "proposed_version",
    }:
        raise ValueError(
            "Contract must bind exact PR, revisions and dependency transition"
        )
    output.mkdir(mode=0o700)
    _write_owned_json(output / "contract.json", contract)
    capture = HTTPSourceCapture(output / "sources", limits)
    receipt = {
        "outcome": "in_progress",
        "started_at": datetime.now(UTC).isoformat(),
        "contract_sha256": sha256((output / "contract.json").read_bytes()).hexdigest(),
        "tool_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "product_source_sha256": {
            str(p.relative_to(REPOSITORY_ROOT)): sha256(p.read_bytes()).hexdigest()
            for p in sorted((REPOSITORY_ROOT / "src/upgradepilot").rglob("*.py"))
        },
        "model_calls_admitted": 0,
    }
    _write_owned_json(output / "capture.json", receipt)
    try:
        with capture.observe():
            result = investigate_public_pull_request(
                expected["repository"], int(expected["pull_number"])
            )
            report = project_investigation_report(result, auth_mode="anonymous")
            observed = _report_identity(report)
            receipt["observed_identity"] = observed
            if any(observed.get(key) != str(value) for key, value in expected.items()):
                raise CaptureStopped("identity_mismatch")
        capture.check_deadline()
        save_report(report, output / "report.json")
        _write_private(
            output / "report.txt", (render_investigation_report(report) + "\n").encode()
        )
        _write_owned_json(
            output / "report-sources.json",
            {
                "meaning": "Report references for source-aware packet review; not coverage proof",
                "sources": [
                    {
                        "id": s.source_id,
                        "kind": s.kind,
                        "locator": s.locator,
                        "retention": s.retention,
                    }
                    for s in report.sources
                ],
            },
        )
        receipt.update(
            outcome="normal_report_captured",
            report_sha256=sha256((output / "report.json").read_bytes()).hexdigest(),
        )
    except CaptureStopped as error:
        receipt.update(
            outcome="not_comparable"
            if error.reason == "identity_mismatch"
            else "capture_stopped",
            reason=error.reason,
        )
    except Exception as error:  # noqa: BLE001 -- terminal diagnostic receipt, never a product result
        receipt.update(
            outcome="investigation_or_capture_failed", error_type=type(error).__name__
        )
    finally:
        receipt.update(
            finished_at=datetime.now(UTC).isoformat(),
            elapsed_seconds=time.monotonic() - capture.started,
            requests=len(capture.rows),
            decoded_body_bytes=capture.total_bytes,
            source_index_sha256=sha256(
                (output / "sources/index.json").read_bytes()
            ).hexdigest(),
        )
        _write_owned_json(output / "capture.json", receipt)
    return receipt


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args(argv)
    if args.contract.stat().st_size > 65_536:
        parser.error("Capture contract exceeds 64KiB")
    contract = json.loads(args.contract.read_text())
    limits = CaptureLimits(**contract["limits"])

    def deadline(signum, frame):
        raise CaptureStopped("elapsed_limit")

    # These changes affect only this standalone diagnostic process. In particular, PyPI's
    # ordinary Session cannot silently adopt .netrc credentials during a public capture.
    os.environ["NETRC"] = os.devnull
    for key in (
        "HTTP_PROXY",
        "HTTPS_PROXY",
        "ALL_PROXY",
        "http_proxy",
        "https_proxy",
        "all_proxy",
        "GITHUB_TOKEN",
        "GH_TOKEN",
    ):
        os.environ.pop(key, None)
    previous = signal.signal(signal.SIGALRM, deadline)
    signal.setitimer(signal.ITIMER_REAL, limits.max_elapsed_seconds)
    try:
        receipt = capture_normal_report(contract, args.output)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)
    print(
        json.dumps(
            {
                key: receipt[key]
                for key in (
                    "outcome",
                    "requests",
                    "decoded_body_bytes",
                    "elapsed_seconds",
                )
            }
        )
    )
    return 0 if receipt["outcome"] == "normal_report_captured" else 2


if __name__ == "__main__":
    raise SystemExit(main())
