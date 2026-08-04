"""Shared bounded JSON acquisition mechanics for PyPI endpoints.

This provider module owns request configuration, streamed body limits, response
closing, and JSON-object decoding shared by release and provenance clients.
Endpoint-specific HTTP meaning remains with focused clients.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any

import requests
from requests import Response, Session
from requests.exceptions import RequestException, Timeout

from ..json_contract import JsonContractViolation, expect_mapping

DEFAULT_TIMEOUT = (3.05, 15.0)
DEFAULT_MAX_RESPONSE_BYTES = 1_000_000


class PyPIRequestError(RuntimeError):
    """A PyPI request failed before a complete usable body was acquired."""

    def __init__(
        self,
        message: str,
        *,
        reason: str,
        status_code: int | None = None,
    ) -> None:
        super().__init__(message)
        self.reason = reason
        self.status_code = status_code


class PyPIResponseError(ValueError):
    """A successful PyPI response did not satisfy the bounded JSON contract."""


class PyPIJsonApiClient:
    """Provide source-neutral mechanics shared by focused PyPI JSON clients."""

    def __init__(
        self,
        *,
        session: Session | None = None,
        timeout: tuple[float, float] = DEFAULT_TIMEOUT,
        max_response_bytes: int = DEFAULT_MAX_RESPONSE_BYTES,
        accept: str = "application/json",
    ) -> None:
        if max_response_bytes < 1:
            raise ValueError("max_response_bytes must be positive.")
        self._session = session or requests.Session()
        self._timeout = timeout
        self._max_response_bytes = max_response_bytes
        self._headers = {
            "Accept": accept,
            "User-Agent": "UpgradePilot/0.0.0",
        }

    def _get_response(self, url: str, *, resource: str) -> Response:
        try:
            return self._session.get(
                url,
                headers=self._headers,
                timeout=self._timeout,
                stream=True,
            )
        except Timeout as exc:
            raise PyPIRequestError(
                f"PyPI {resource} acquisition timed out.",
                reason="timeout",
            ) from exc
        except RequestException as exc:
            raise PyPIRequestError(
                f"PyPI {resource} acquisition failed before a usable response arrived.",
                reason="transport_error",
            ) from exc

    def _read_json_object(
        self,
        response: Response,
        *,
        resource: str,
    ) -> Mapping[str, Any]:
        try:
            declared = response.headers.get("Content-Length")
            if declared is not None:
                try:
                    declared_size = int(declared)
                except ValueError as exc:
                    raise PyPIResponseError(
                        f"PyPI {resource} returned a non-numeric Content-Length header."
                    ) from exc
                if declared_size < 0 or declared_size > self._max_response_bytes:
                    raise PyPIResponseError(
                        f"PyPI {resource} response exceeded the configured size limit."
                    )

            body = bytearray()
            try:
                for chunk in response.iter_content(chunk_size=8192):
                    if not chunk:
                        continue
                    body.extend(chunk)
                    if len(body) > self._max_response_bytes:
                        raise PyPIResponseError(
                            f"PyPI {resource} response exceeded the configured size limit."
                        )
            except RequestException as exc:
                raise PyPIRequestError(
                    f"PyPI {resource} response ended before its complete body was acquired.",
                    reason="body_incomplete",
                    status_code=response.status_code,
                ) from exc
        finally:
            response.close()

        try:
            decoded = json.loads(body)
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            raise PyPIResponseError(
                f"PyPI returned HTTP success with invalid {resource} JSON."
            ) from exc

        try:
            return expect_mapping(decoded)
        except JsonContractViolation as exc:
            raise PyPIResponseError(
                f"PyPI {resource} response JSON was not an object."
            ) from exc


__all__ = (
    "DEFAULT_MAX_RESPONSE_BYTES",
    "DEFAULT_TIMEOUT",
    "PyPIJsonApiClient",
    "PyPIRequestError",
    "PyPIResponseError",
)
