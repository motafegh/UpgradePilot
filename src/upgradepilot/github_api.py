"""Shared read-only GitHub REST transport and response validation.

This module owns the boundary between untrusted HTTP/JSON data and the focused
acquisition modules that interpret GitHub resources.  It deliberately knows
nothing about pull requests, changed files, workflows, or jobs.  Those meanings
belong in ``github_client`` and ``github_actions``.

Keeping the transport layer small gives every GitHub acquisition path the same
classification for timeouts, HTTP refusal, invalid JSON, and malformed success
responses without duplicating request code.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import requests
from requests import Response, Session
from requests.exceptions import RequestException, Timeout

GITHUB_API_ROOT = "https://api.github.com"
GITHUB_API_VERSION = "2022-11-28"
DEFAULT_TIMEOUT = (3.05, 15.0)


class GitHubAcquisitionError(RuntimeError):
    """GitHub evidence could not be acquired through a usable HTTP response.

    ``reason`` is a stable product-facing category. ``status_code`` is present
    only when GitHub returned an HTTP response that can be classified.
    """

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


class GitHubResponseError(RuntimeError):
    """GitHub returned success, but the payload lacked trustworthy evidence."""


class GitHubApiClient:
    """Issue read-only GitHub requests and validate top-level response shapes.

    A Requests ``Session`` can be injected by deterministic tests.  Focused
    clients subclass this class and convert validated JSON objects into their own
    immutable domain records.
    """

    def __init__(
        self,
        *,
        token: str | None = None,
        session: Session | None = None,
        timeout: tuple[float, float] = DEFAULT_TIMEOUT,
    ) -> None:
        self._session = session or requests.Session()
        self._timeout = timeout
        self._headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": GITHUB_API_VERSION,
            "User-Agent": "UpgradePilot/0.0.0",
        }
        if token:
            self._headers["Authorization"] = f"Bearer {token}"

    @staticmethod
    def api_url(path: str) -> str:
        """Build one GitHub REST URL from an absolute API path."""

        if not path.startswith("/"):
            raise ValueError("GitHub API path must start with '/'.")
        return f"{GITHUB_API_ROOT}{path}"

    def _get_json_object(
        self,
        url: str,
        *,
        resource: str,
        params: Mapping[str, str | int] | None = None,
    ) -> Mapping[str, Any]:
        """Acquire successful JSON and require an object-shaped top level."""

        response = self._get(url, resource=resource, params=params)
        data = self._read_json(response, resource=resource)
        if not isinstance(data, Mapping):
            raise GitHubResponseError(
                f"GitHub returned JSON, but the {resource} response was not an object."
            )
        return data

    def _get_json_array(
        self,
        url: str,
        *,
        resource: str,
        params: Mapping[str, str | int] | None = None,
    ) -> list[Any]:
        """Acquire successful JSON and require an array-shaped top level."""

        response = self._get(url, resource=resource, params=params)
        data = self._read_json(response, resource=resource)
        if not isinstance(data, list):
            raise GitHubResponseError(
                f"GitHub returned JSON, but the {resource} response was not an array."
            )
        return data

    def _get(
        self,
        url: str,
        *,
        resource: str,
        params: Mapping[str, str | int] | None = None,
    ) -> Response:
        """Issue one read-only request and classify transport and HTTP failures."""

        try:
            kwargs: dict[str, Any] = {
                "headers": self._headers,
                "timeout": self._timeout,
            }
            if params is not None:
                kwargs["params"] = params
            response = self._session.get(url, **kwargs)
        except Timeout as exc:
            raise GitHubAcquisitionError(
                f"GitHub {resource} acquisition timed out.",
                reason="timeout",
            ) from exc
        except RequestException as exc:
            raise GitHubAcquisitionError(
                f"GitHub {resource} acquisition failed before a usable response was received.",
                reason="transport_error",
            ) from exc

        self._raise_for_status(response, resource=resource)
        return response

    @staticmethod
    def _raise_for_status(response: Response, *, resource: str) -> None:
        """Map non-success HTTP statuses to bounded acquisition reasons."""

        status = response.status_code
        if 200 <= status < 300:
            return
        if status == 404:
            # GitHub uses 404 for both absence and inaccessible resources.
            raise GitHubAcquisitionError(
                f"No accessible {resource} resource was found at the supplied locator.",
                reason="not_found_or_inaccessible",
                status_code=status,
            )
        if status in {403, 429}:
            raise GitHubAcquisitionError(
                "GitHub refused the request or the API rate limit was reached.",
                reason="forbidden_or_rate_limited",
                status_code=status,
            )
        raise GitHubAcquisitionError(
            f"GitHub returned HTTP {status} while acquiring {resource} evidence.",
            reason="http_error",
            status_code=status,
        )

    @staticmethod
    def _read_json(response: Response, *, resource: str) -> Any:
        """Decode a successful response body or raise a response-evidence error."""

        try:
            return response.json()
        except requests.exceptions.JSONDecodeError as exc:
            raise GitHubResponseError(
                f"GitHub returned a successful {resource} response that was not valid JSON."
            ) from exc


def required_mapping(data: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    """Return a required JSON object field after runtime type validation."""

    value = data[key]
    if not isinstance(value, Mapping):
        raise GitHubResponseError(f"GitHub field '{key}' must be an object.")
    return value


def required_list(data: Mapping[str, Any], key: str) -> list[Any]:
    """Return a required JSON array field after runtime type validation."""

    value = data[key]
    if not isinstance(value, list):
        raise GitHubResponseError(f"GitHub field '{key}' must be an array.")
    return value


def required_str(data: Mapping[str, Any], key: str) -> str:
    """Return a required non-empty JSON string field."""

    value = data[key]
    if not isinstance(value, str) or not value:
        raise GitHubResponseError(f"GitHub field '{key}' must be a non-empty string.")
    return value


def optional_str(data: Mapping[str, Any], key: str) -> str | None:
    """Return a nullable JSON string while rejecting other value types."""

    value = data[key]
    if value is not None and (not isinstance(value, str) or not value):
        raise GitHubResponseError(
            f"GitHub field '{key}' must be a non-empty string or null."
        )
    return value


def required_int(data: Mapping[str, Any], key: str) -> int:
    """Return a required JSON integer field while rejecting booleans."""

    value = data[key]
    if isinstance(value, bool) or not isinstance(value, int):
        raise GitHubResponseError(f"GitHub field '{key}' must be an integer.")
    return value


def required_positive_int(data: Mapping[str, Any], key: str) -> int:
    """Return a required integer field constrained to one or greater."""

    value = required_int(data, key)
    if value < 1:
        raise GitHubResponseError(f"GitHub field '{key}' must be positive.")
    return value


def required_nonnegative_int(data: Mapping[str, Any], key: str) -> int:
    """Return a required integer field constrained to zero or greater."""

    value = required_int(data, key)
    if value < 0:
        raise GitHubResponseError(f"GitHub field '{key}' must not be negative.")
    return value


def required_bool(data: Mapping[str, Any], key: str) -> bool:
    """Return a required JSON boolean field."""

    value = data[key]
    if not isinstance(value, bool):
        raise GitHubResponseError(f"GitHub field '{key}' must be a boolean.")
    return value
