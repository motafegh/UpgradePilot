"""Low-level GitHub REST foundation shared by every acquisition client.

GitHub-focused clients reuse this module for request configuration, HTTP failure
classification, JSON decoding, and GitHub-compatible field helpers. Runtime JSON
value rules are delegated to the package-root ``json_contract`` primitive; GitHub
error meaning and wording remain provider-owned here.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Callable, TypeVar

import requests
from requests import Response, Session
from requests.exceptions import RequestException, Timeout

from ..json_contract import (
    JsonContractViolation,
    expect_boolean,
    expect_integer,
    expect_list,
    expect_mapping,
    expect_nonempty_text,
    expect_nonnegative_integer,
    expect_optional_nonempty_text,
    expect_positive_integer,
)

GITHUB_API_ROOT = "https://api.github.com"
GITHUB_API_VERSION = "2022-11-28"
DEFAULT_TIMEOUT = (3.05, 15.0)

_T = TypeVar("_T")


class GitHubAcquisitionError(RuntimeError):
    """The request failed before a usable successful GitHub body was obtained."""

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
    """HTTP succeeded, but returned data could not be trusted as GitHub evidence."""


class GitHubApiClient:
    """Provide reusable read-only GitHub HTTP and top-level JSON operations."""

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
        """Build a complete GitHub API URL from one root-relative path."""

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
        """GET one endpoint and require a JSON object at the top level."""

        response = self._get(url, resource=resource, params=params)
        data = self._read_json(response, resource=resource)
        try:
            return expect_mapping(data)
        except JsonContractViolation as exc:
            raise GitHubResponseError(
                f"GitHub returned JSON, but the {resource} response was not an object."
            ) from exc

    def _get_json_array(
        self,
        url: str,
        *,
        resource: str,
        params: Mapping[str, str | int] | None = None,
    ) -> list[Any]:
        """GET one endpoint and require a JSON array at the top level."""

        response = self._get(url, resource=resource, params=params)
        data = self._read_json(response, resource=resource)
        try:
            return expect_list(data)
        except JsonContractViolation as exc:
            raise GitHubResponseError(
                f"GitHub returned JSON, but the {resource} response was not an array."
            ) from exc

    def _get(
        self,
        url: str,
        *,
        resource: str,
        params: Mapping[str, str | int] | None = None,
    ) -> Response:
        """Send one GET and return only a response with a successful HTTP status."""

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
        """Translate GitHub HTTP statuses into stable acquisition categories."""

        status = response.status_code
        if 200 <= status < 300:
            return
        if status == 404:
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
        """Decode a successful body while keeping malformed JSON distinct."""

        try:
            return response.json()
        except requests.exceptions.JSONDecodeError as exc:
            raise GitHubResponseError(
                f"GitHub returned a successful {resource} response that was not valid JSON."
            ) from exc


def _github_contract(
    value: Any,
    validator: Callable[[Any], _T],
    message: str,
) -> _T:
    """Run a neutral value contract and preserve GitHub's public error contract."""

    try:
        return validator(value)
    except JsonContractViolation as exc:
        raise GitHubResponseError(message) from exc


def required_mapping(data: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    return _github_contract(
        data[key],
        expect_mapping,
        f"GitHub field '{key}' must be an object.",
    )


def required_list(data: Mapping[str, Any], key: str) -> list[Any]:
    return _github_contract(
        data[key],
        expect_list,
        f"GitHub field '{key}' must be an array.",
    )


def required_str(data: Mapping[str, Any], key: str) -> str:
    return _github_contract(
        data[key],
        expect_nonempty_text,
        f"GitHub field '{key}' must be a non-empty string.",
    )


def optional_str(data: Mapping[str, Any], key: str) -> str | None:
    return _github_contract(
        data[key],
        expect_optional_nonempty_text,
        f"GitHub field '{key}' must be a non-empty string or null.",
    )


def required_int(data: Mapping[str, Any], key: str) -> int:
    return _github_contract(
        data[key],
        expect_integer,
        f"GitHub field '{key}' must be an integer.",
    )


def required_positive_int(data: Mapping[str, Any], key: str) -> int:
    value = required_int(data, key)
    return _github_contract(
        value,
        expect_positive_integer,
        f"GitHub field '{key}' must be positive.",
    )


def required_nonnegative_int(data: Mapping[str, Any], key: str) -> int:
    value = required_int(data, key)
    return _github_contract(
        value,
        expect_nonnegative_integer,
        f"GitHub field '{key}' must not be negative.",
    )


def required_bool(data: Mapping[str, Any], key: str) -> bool:
    return _github_contract(
        data[key],
        expect_boolean,
        f"GitHub field '{key}' must be a boolean.",
    )
