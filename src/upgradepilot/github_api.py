"""Shared read-only GitHub REST transport and response validation.

This module owns the boundary between untrusted HTTP/JSON data and the focused
acquisition modules that interpret GitHub resources. It deliberately knows
nothing about pull requests, changed files, workflows, jobs, or repository
content; those meanings belong to the specialized clients.

Keeping the transport layer small gives every GitHub acquisition path the same
three-stage trust pipeline: obtain a usable response, accept only an allowed HTTP
status, then decode and validate the JSON shape. A failure at each stage receives
a distinct product-facing classification without duplicating request code.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import requests
from requests import Response, Session
from requests.exceptions import RequestException, Timeout

GITHUB_API_ROOT = "https://api.github.com"
GITHUB_API_VERSION = "2022-11-28"
# Requests interprets a two-item timeout as (connection setup, response read).
# Separate limits prevent either phase from blocking the command indefinitely.
DEFAULT_TIMEOUT = (3.05, 15.0)


class GitHubAcquisitionError(RuntimeError):
    """GitHub evidence could not be acquired through an acceptable HTTP response.

    This covers transport failures, timeouts, and non-success HTTP statuses.
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
    """GitHub returned HTTP success, but its body was not trustworthy evidence.

    Examples include invalid JSON, the wrong top-level JSON shape, missing fields,
    or values that contradict the identity requested by a focused client.
    """


class GitHubApiClient:
    """Issue read-only GitHub requests and validate top-level response shapes.

    Focused clients inherit this transport behavior, then add resource-specific
    identity and field validation. A Requests ``Session`` can be injected so
    deterministic tests exercise the same request contract without live network
    traffic.
    """

    def __init__(
        self,
        *,
        token: str | None = None,
        session: Session | None = None,
        timeout: tuple[float, float] = DEFAULT_TIMEOUT,
    ) -> None:
        # Dependency injection: production receives a real Session, while tests
        # can supply a Mock exposing the same ``get`` method.
        self._session = session or requests.Session()
        self._timeout = timeout
        self._headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": GITHUB_API_VERSION,
            "User-Agent": "UpgradePilot/0.0.0",
        }
        # Public requests work without credentials. When supplied, the token is
        # attached centrally so every focused client uses the same auth contract.
        if token:
            self._headers["Authorization"] = f"Bearer {token}"

    @staticmethod
    def api_url(path: str) -> str:
        """Build one GitHub REST URL from an API-root-relative absolute path.

        Requiring the leading slash makes URL composition unambiguous and prevents
        focused clients from silently producing malformed endpoint URLs.
        """

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
        """Run the transport pipeline and require an object-shaped JSON result.

        ``Mapping`` accepts dictionary-like objects while avoiding an unnecessary
        dependency on the concrete ``dict`` implementation.
        """

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
        """Run the transport pipeline and require an array-shaped JSON result.

        The element type remains ``Any`` here because resource-specific clients
        validate each item before constructing trusted domain records.
        """

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
        """Issue one GET and distinguish transport failure from HTTP refusal.

        A transport exception means no usable response was received. A returned
        response is classified separately by ``_raise_for_status``.
        """

        # ``raise ... from exc`` below keeps the Requests exception as
        # ``__cause__`` while exposing UpgradePilot's stable error vocabulary.
        try:
            # Build keyword arguments once so optional query parameters can be
            # omitted entirely. ``**kwargs`` expands this mapping into named
            # arguments of ``Session.get``.
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
        """Map HTTP status families to stable acquisition-failure categories.

        HTTP success only permits body inspection; it does not yet make the body
        valid or trustworthy evidence.
        """

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
        """Decode a successful body without assuming that HTTP success implies JSON."""

        try:
            return response.json()
        except requests.exceptions.JSONDecodeError as exc:
            raise GitHubResponseError(
                f"GitHub returned a successful {resource} response that was not valid JSON."
            ) from exc


def required_mapping(data: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    """Return a required JSON object field after runtime type validation.

    Type hints describe trusted Python expectations; they cannot validate values
    arriving from an external JSON response.
    """

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
    """Return a required field whose value may be a string or JSON ``null``.

    The key is still accessed with ``data[key]``: optional describes the value,
    not the presence of the field.
    """

    value = data[key]
    if value is not None and (not isinstance(value, str) or not value):
        raise GitHubResponseError(
            f"GitHub field '{key}' must be a non-empty string or null."
        )
    return value


def required_int(data: Mapping[str, Any], key: str) -> int:
    """Return a required JSON integer field while rejecting booleans.

    Python defines ``bool`` as a subclass of ``int``, so ``isinstance(True, int)``
    is true. The explicit boolean check prevents JSON ``true`` from becoming the
    integer ``1`` at this trust boundary.
    """

    value = data[key]
    if isinstance(value, bool) or not isinstance(value, int):
        raise GitHubResponseError(f"GitHub field '{key}' must be an integer.")
    return value


def required_positive_int(data: Mapping[str, Any], key: str) -> int:
    """Return an integer constrained to one or greater.

    Reusing ``required_int`` keeps type and boolean validation consistent before
    this helper adds the narrower numeric invariant.
    """

    value = required_int(data, key)
    if value < 1:
        raise GitHubResponseError(f"GitHub field '{key}' must be positive.")
    return value


def required_nonnegative_int(data: Mapping[str, Any], key: str) -> int:
    """Return an integer constrained to zero or greater.

    This composes the shared integer validator with the domain-specific lower
    bound instead of duplicating validation logic.
    """

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
