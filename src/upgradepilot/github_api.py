"""Low-level GitHub REST foundation shared by every acquisition client.

Purpose of this file
--------------------
UpgradePilot has several clients that read different GitHub resources:

* ``GitHubReadClient`` in ``github_client.py`` reads pull requests and changed files.
* ``GitHubActionsClient`` in ``github_actions.py`` reads workflow runs and jobs.
* ``GitHubRepositoryClient`` in ``github_repository.py`` reads repository files.

All three inherit from ``GitHubApiClient``. This file gives them one common way to
send GET requests, classify failures, decode JSON, and validate basic JSON field
types. Without this shared layer, each client would repeat the same HTTP and JSON
error-handling code and could classify the same GitHub failure differently.

A typical call travels through the file in this order:

1. A focused client builds an endpoint with ``api_url``.
2. It calls ``_get_json_object`` or ``_get_json_array``.
3. ``_get`` sends the HTTP request and handles network/HTTP failures.
4. ``_read_json`` converts the response body into Python values.
5. The focused client uses ``required_*`` helpers to validate individual fields.
6. Only then does that client build a trusted domain record such as
   ``PullRequestIdentity`` or ``WorkflowRun``.

Boundary of responsibility
--------------------------
This module knows what a valid HTTP response and basic JSON value look like. It
does not know whether a workflow run belongs to a particular pull request, whether
pagination is complete, or what a dependency change means. Those domain-specific
checks remain in the focused client that understands that resource.
"""

# Postpone evaluation of annotations. This keeps type hints as metadata instead of
# requiring every referenced type to be resolved while the module is imported.
from __future__ import annotations

# ``Mapping`` describes any dictionary-like object and is used for JSON objects.
# ``Any`` is necessary at the untrusted boundary because decoded JSON may initially
# contain values of several possible Python types.
from collections.abc import Mapping
from typing import Any

import requests
from requests import Response, Session
from requests.exceptions import RequestException, Timeout

# Focused clients append resource paths such as ``/repos/owner/name/pulls/12`` to
# this root. Keeping the root here prevents endpoint construction from drifting.
GITHUB_API_ROOT = "https://api.github.com"

# Sending an explicit API version makes GitHub's response contract more stable than
# silently following whichever default version GitHub may use later.
GITHUB_API_VERSION = "2022-11-28"

# Requests interprets this pair as ``(connect timeout, read timeout)`` in seconds:
# 3.05 seconds to establish the connection, then 15 seconds to receive response data.
DEFAULT_TIMEOUT = (3.05, 15.0)


class GitHubAcquisitionError(RuntimeError):
    """The request failed before UpgradePilot obtained a usable successful body.

    Examples are a timeout, another network failure, HTTP 404, or HTTP 429. The
    focused clients do not need to understand Requests exceptions or every HTTP
    status; they receive this one UpgradePilot-level exception instead.

    The CLI catches this error and reports exit status 3. ``reason`` is therefore a
    stable machine-readable category, while the normal exception message remains a
    human-readable explanation. ``status_code`` is ``None`` when no HTTP response
    existed, such as during a timeout.
    """

    def __init__(
        self,
        message: str,
        *,
        reason: str,
        status_code: int | None = None,
    ) -> None:
        # ``*`` in the signature makes ``reason`` and ``status_code`` keyword-only.
        # A call must say ``reason="timeout"`` instead of passing an unclear string
        # positionally after the message.
        super().__init__(message)
        # ``super().__init__`` stores the normal exception message. These extra
        # attributes preserve structured information used by ``cli.py``.
        self.reason = reason
        self.status_code = status_code


class GitHubResponseError(RuntimeError):
    """HTTP succeeded, but the returned data cannot be trusted as evidence.

    Examples include invalid JSON, an object where an array was expected, a missing
    required field, or a field with the wrong runtime type. Focused clients also use
    this error when the data is well-formed but contradicts the requested identity,
    such as a workflow run carrying the wrong head SHA.

    The CLI catches this separately from acquisition failure and returns exit status
    4. That distinction teaches an important boundary: receiving HTTP 200 does not
    prove that the body is complete, correctly shaped, or relevant.
    """


class GitHubApiClient:
    """Provide reusable read-only HTTP and top-level JSON operations.

    This is a base class rather than a complete GitHub client. Its subclasses decide
    which endpoint to call and how to interpret its fields:

    * ``GitHubReadClient`` calls these methods for PR and changed-file data.
    * ``GitHubActionsClient`` calls them for run and job pages.
    * ``GitHubRepositoryClient`` calls them for run details and file contents.

    Keeping the methods here means all those clients share authentication headers,
    timeout behavior, HTTP classification, JSON decoding, and test injection.
    """

    def __init__(
        self,
        *,
        token: str | None = None,
        session: Session | None = None,
        timeout: tuple[float, float] = DEFAULT_TIMEOUT,
    ) -> None:
        """Configure the reusable HTTP collaborator and request defaults.

        ``token``, ``session``, and ``timeout`` are keyword-only so call sites state
        what each value means. Production normally leaves ``session`` as ``None``;
        tests pass a ``Mock`` session so they can control responses without accessing
        the network and can inspect the exact request arguments.
        """

        # A Requests ``Session`` provides the ``get`` method used below and can reuse
        # connections across calls. Dependency injection lets tests replace it with
        # an object that has the same small interface.
        self._session = session or requests.Session()
        self._timeout = timeout

        # These headers apply to every specialized client because they describe the
        # shared REST protocol, not a particular GitHub resource.
        self._headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": GITHUB_API_VERSION,
            "User-Agent": "UpgradePilot/0.0.0",
        }

        # Public repositories can be read anonymously. When a token exists, adding
        # it here automatically authenticates PR, Actions, and repository-file calls.
        if token:
            self._headers["Authorization"] = f"Bearer {token}"

    @staticmethod
    def api_url(path: str) -> str:
        """Build a complete GitHub API URL from one root-relative API path.

        Example: ``api_url("/repos/acme/tool/pulls/7")`` becomes
        ``https://api.github.com/repos/acme/tool/pulls/7``.

        The method is ``@staticmethod`` because URL construction needs no client
        state such as the token, session, or timeout. Requiring the leading slash
        catches malformed paths locally before any request is attempted.
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
        """GET one endpoint and require a JSON object at the top level.

        Use this for endpoints whose JSON begins with ``{...}``. For example,
        ``GitHubReadClient.get_pull_request`` expects one PR object, and
        ``GitHubActionsClient.get_exact_head_workflow_runs`` expects an object that
        contains ``total_count`` and ``workflow_runs``.

        This function validates only the top-level container. The calling client must
        still validate fields inside it with helpers such as ``required_str``.
        """

        # First obtain a response whose transport and HTTP status are acceptable.
        response = self._get(url, resource=resource, params=params)
        # Then decode the body. Keeping these stages separate produces more accurate
        # errors: HTTP failure is not confused with malformed JSON.
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
        """GET one endpoint and require a JSON array at the top level.

        ``GitHubReadClient.get_changed_files`` uses this because GitHub returns the
        changed-file page directly as ``[...]`` rather than wrapping it in an object.

        The return type is ``list[Any]`` because this layer has proved only that the
        outer value is a list. The focused client must inspect every item and convert
        valid objects into records such as ``ChangedFile``.
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
        """Send one GET request and return only a response with a 2xx status.

        This is the central network boundary used indirectly by all focused clients.
        It has three outcomes:

        * return a ``Response`` when GitHub answered with HTTP 2xx;
        * raise ``GitHubAcquisitionError(reason="timeout")`` for a timeout;
        * raise another ``GitHubAcquisitionError`` for transport or HTTP failure.

        JSON is intentionally not decoded here. ``_get_json_object`` and
        ``_get_json_array`` perform that next stage after HTTP success is established.
        """

        try:
            # Build a dictionary because ``params`` is optional. Omitting the key
            # entirely produces a cleaner request than passing ``params=None``.
            kwargs: dict[str, Any] = {
                "headers": self._headers,
                "timeout": self._timeout,
            }
            if params is not None:
                kwargs["params"] = params

            # ``**kwargs`` expands the dictionary into named arguments, equivalent
            # to ``get(url, headers=..., timeout=..., params=...)`` when params exist.
            response = self._session.get(url, **kwargs)

        # ``Timeout`` is a subclass of ``RequestException``. It must be caught first
        # or the broader handler below would incorrectly classify it as a generic
        # transport error.
        except Timeout as exc:
            # ``raise ... from exc`` keeps the original Requests exception as the
            # cause while presenting UpgradePilot's stable public error category.
            raise GitHubAcquisitionError(
                f"GitHub {resource} acquisition timed out.",
                reason="timeout",
            ) from exc
        except RequestException as exc:
            raise GitHubAcquisitionError(
                f"GitHub {resource} acquisition failed before a usable response was received.",
                reason="transport_error",
            ) from exc

        # Requests does not raise automatically here because the code needs its own
        # bounded status categories and messages. Only a 2xx response passes through.
        self._raise_for_status(response, resource=resource)
        return response

    @staticmethod
    def _raise_for_status(response: Response, *, resource: str) -> None:
        """Translate HTTP status codes into UpgradePilot acquisition categories.

        The method is stateless, so it is ``@staticmethod``. It does not call
        ``Response.raise_for_status()`` because UpgradePilot needs stable reasons that
        the CLI and later code can inspect, rather than library-specific exceptions.
        """

        status = response.status_code

        # Any status from 200 through 299 is in the HTTP success family. This only
        # authorizes body decoding; it does not yet establish valid JSON evidence.
        if 200 <= status < 300:
            return

        if status == 404:
            # GitHub often uses 404 for both a resource that does not exist and one
            # the caller is not allowed to see. The code preserves that ambiguity
            # instead of claiming to know which case occurred.
            raise GitHubAcquisitionError(
                f"No accessible {resource} resource was found at the supplied locator.",
                reason="not_found_or_inaccessible",
                status_code=status,
            )

        # A set is used because membership in either status has the same supported
        # product meaning: access was refused or the caller should stop due to rate
        # limiting. This layer does not guess which remedy will succeed.
        if status in {403, 429}:
            raise GitHubAcquisitionError(
                "GitHub refused the request or the API rate limit was reached.",
                reason="forbidden_or_rate_limited",
                status_code=status,
            )

        # All remaining non-2xx statuses stay visible through ``status_code`` but are
        # grouped under one bounded fallback reason rather than creating a reason for
        # every possible HTTP code.
        raise GitHubAcquisitionError(
            f"GitHub returned HTTP {status} while acquiring {resource} evidence.",
            reason="http_error",
            status_code=status,
        )

    @staticmethod
    def _read_json(response: Response, *, resource: str) -> Any:
        """Decode a successful response body into Python JSON values.

        ``Response.json()`` may return a dictionary, list, string, number, boolean,
        or ``None``. Therefore this low-level function returns ``Any``; its callers
        immediately enforce the expected top-level shape.

        HTTP 2xx and valid JSON are separate facts. A server or intermediary could
        return HTML or truncated text with a success status, so decoding failure is
        reported as ``GitHubResponseError`` rather than acquisition failure.
        """

        try:
            return response.json()
        except requests.exceptions.JSONDecodeError as exc:
            raise GitHubResponseError(
                f"GitHub returned a successful {resource} response that was not valid JSON."
            ) from exc


# ---------------------------------------------------------------------------
# Reusable JSON field validators
# ---------------------------------------------------------------------------
# Focused parsers call these after a top-level object has been accepted. They use
# ``data[key]`` rather than ``data.get(key)`` because these fields are required.
# A missing key therefore raises ``KeyError``; the focused parser catches it and
# adds a resource-specific message such as "workflow-run item is missing field...".
# Type hints alone cannot validate external JSON at runtime, so each helper performs
# an explicit ``isinstance`` check before returning the value as trusted Python data.


def required_mapping(data: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    """Return a required nested JSON object.

    ``github_client.py`` uses this for fields such as ``base``, ``head``, and
    ``user`` before reading their inner values. ``Mapping`` is checked instead of
    concrete ``dict`` so the code depends on dictionary behavior, not one class.
    """

    value = data[key]
    if not isinstance(value, Mapping):
        raise GitHubResponseError(f"GitHub field '{key}' must be an object.")
    return value


def required_list(data: Mapping[str, Any], key: str) -> list[Any]:
    """Return a required nested JSON array.

    ``github_actions.py`` uses this for fields such as ``workflow_runs`` and
    ``jobs``. Items remain ``Any`` until that client validates each object.
    """

    value = data[key]
    if not isinstance(value, list):
        raise GitHubResponseError(f"GitHub field '{key}' must be an array.")
    return value


def required_str(data: Mapping[str, Any], key: str) -> str:
    """Return a required, non-empty JSON string.

    Identity fields such as repository paths, names, events, and commit SHAs should
    not silently accept ``null``, numbers, or empty text. This helper gives all
    focused clients the same rule and error wording.
    """

    value = data[key]
    if not isinstance(value, str) or not value:
        raise GitHubResponseError(f"GitHub field '{key}' must be a non-empty string.")
    return value


def optional_str(data: Mapping[str, Any], key: str) -> str | None:
    """Return a required field whose value may be text or JSON ``null``.

    The name means the string value is optional, not that the key may be missing.
    For example, GitHub includes ``conclusion`` for a workflow run, but its value can
    be ``null`` while the run is still queued or executing. Using ``data[key]`` keeps
    absence distinct from a present null value.
    """

    value = data[key]
    if value is not None and (not isinstance(value, str) or not value):
        raise GitHubResponseError(
            f"GitHub field '{key}' must be a non-empty string or null."
        )
    return value


def required_int(data: Mapping[str, Any], key: str) -> int:
    """Return a required JSON integer while rejecting booleans.

    Python defines ``bool`` as a subclass of ``int``:
    ``isinstance(True, int)`` is ``True``. JSON ``true`` must not therefore be
    accepted as numeric ID ``1``. The boolean check is intentionally performed
    before the ordinary integer check.
    """

    value = data[key]
    if isinstance(value, bool) or not isinstance(value, int):
        raise GitHubResponseError(f"GitHub field '{key}' must be an integer.")
    return value


def required_positive_int(data: Mapping[str, Any], key: str) -> int:
    """Return a required integer greater than zero.

    IDs and run-attempt numbers use this stronger rule. Calling ``required_int``
    first reuses the type/boolean checks, then this function adds the numeric range
    rule instead of duplicating the whole validator.
    """

    value = required_int(data, key)
    if value < 1:
        raise GitHubResponseError(f"GitHub field '{key}' must be positive.")
    return value


def required_nonnegative_int(data: Mapping[str, Any], key: str) -> int:
    """Return a required integer that may be zero but cannot be negative.

    Counts such as ``changed_files`` and ``total_count`` legitimately use zero, so
    they need a different lower bound from IDs. This function composes the common
    integer validator with that count-specific rule.
    """

    value = required_int(data, key)
    if value < 0:
        raise GitHubResponseError(f"GitHub field '{key}' must not be negative.")
    return value


def required_bool(data: Mapping[str, Any], key: str) -> bool:
    """Return a required JSON boolean.

    ``github_client.py`` uses this for the PR ``merged`` field. Requiring actual
    ``True``/``False`` prevents strings such as ``"false"`` from being treated as
    truthy Python values later.
    """

    value = data[key]
    if not isinstance(value, bool):
        raise GitHubResponseError(f"GitHub field '{key}' must be a boolean.")
    return value
