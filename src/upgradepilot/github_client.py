"""Acquire and validate public GitHub evidence for the first vertical slice.

This module is UpgradePilot's external-data trust boundary. Values received over
HTTP are untrusted even when GitHub returns a successful status code. The code
therefore separates transport failure, HTTP refusal, invalid JSON, malformed
success payloads, and semantically inconsistent evidence before exposing small
immutable records to the rest of the package.

The client is read-only: it performs HTTP ``GET`` requests and never mutates the
target repository or pull request.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Mapping

import requests
from requests import Response, Session
from requests.exceptions import RequestException, Timeout

_GITHUB_API = "https://api.github.com"
_API_VERSION = "2022-11-28"

# Requests interprets a two-item timeout tuple as separate limits:
# ``(time to establish the connection, time waiting for response bytes)``.
_DEFAULT_TIMEOUT = (3.05, 15.0)
_CHANGED_FILES_PER_PAGE = 100

# Complete acquisition is deliberately bounded. Above this limit the current
# slice refuses the case instead of silently working with partial file evidence.
_MAX_CHANGED_FILES = 3_000

# This is an UpgradePilot input grammar, not a complete grammar for GitHub URLs
# or every repository name GitHub may technically permit.
_REPOSITORY_PATTERN = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9_.-]{0,99})/[A-Za-z0-9_.-]{1,100}$"
)


class UpgradePilotInputError(ValueError):
    """The user-supplied repository or pull-request locator is unsupported."""


class GitHubAcquisitionError(RuntimeError):
    """GitHub evidence could not be acquired through a usable HTTP response.

    ``reason`` is a stable product-facing category. ``status_code`` is present
    only when GitHub returned an HTTP response that can be classified. Transport
    failures such as timeouts have no HTTP status because no usable response was
    received.
    """

    def __init__(
        self,
        message: str,
        *,
        reason: str,
        status_code: int | None = None,
    ) -> None:
        # Initialize RuntimeError so normal exception text and traceback behavior
        # are preserved, then attach structured fields for programmatic handling.
        super().__init__(message)
        self.reason = reason
        self.status_code = status_code


class GitHubResponseError(RuntimeError):
    """GitHub returned success, but the response lacked trustworthy evidence."""


@dataclass(frozen=True, slots=True)
class PullRequestIdentity:
    """Exact proposal identity acquired from one public GitHub pull request.

    The base and head SHAs bind later evidence to the exact proposal revision
    observed during acquisition. Branch names alone are insufficient because a
    branch can move to a different commit after acquisition.

    ``frozen=True`` prevents accidental mutation after validation, while
    ``slots=True`` fixes the allowed field set and rejects undeclared attributes.
    """

    repository: str
    number: int
    title: str
    state: str
    merged: bool
    author: str
    base_ref: str
    base_sha: str
    head_ref: str
    head_sha: str
    changed_files: int


@dataclass(frozen=True, slots=True)
class ChangedFile:
    """One validated changed-file record associated with a pull request.

    ``patch`` is optional because GitHub may omit patch text even when the file
    record itself is otherwise valid. Absence remains ``None`` so later logic can
    abstain explicitly instead of confusing missing evidence with an empty patch.
    """

    filename: str
    status: str
    additions: int
    deletions: int
    changes: int
    patch: str | None


class GitHubReadClient:
    """Acquire public PR evidence without mutating the target repository.

    A Requests ``Session`` may be injected for deterministic tests. This is
    dependency injection: production uses a real session, while tests substitute
    a controlled object that implements the same ``get`` interaction.
    """

    def __init__(
        self,
        *,
        token: str | None = None,
        session: Session | None = None,
        timeout: tuple[float, float] = _DEFAULT_TIMEOUT,
    ) -> None:
        """Create a client with optional authentication and explicit timeouts.

        Args:
            token: Optional GitHub bearer token used only for request headers.
            session: Optional Requests session or test substitute.
            timeout: Connect and response-read timeout values in seconds.
        """

        # ``or`` selects the injected session when it is truthy; otherwise a real
        # Requests session is created for connection reuse across calls.
        self._session = session or requests.Session()
        self._timeout = timeout
        self._headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": _API_VERSION,
            "User-Agent": "UpgradePilot/0.0.0",
        }
        if token:
            self._headers["Authorization"] = f"Bearer {token}"

    def get_pull_request(
        self,
        repository: str,
        pull_number: int,
    ) -> PullRequestIdentity:
        """Acquire and validate exact identity for one public pull request.

        Validation proceeds in layers: local locator validation, HTTP acquisition,
        top-level JSON-shape validation, required-field validation, and finally
        semantic identity checks.

        Raises:
            UpgradePilotInputError: The local locator is outside the supported form.
            GitHubAcquisitionError: No usable successful HTTP response was obtained.
            GitHubResponseError: Successful content was malformed or contradictory.
        """

        repository = validate_repository(repository)
        pull_number = validate_pull_number(pull_number)
        url = f"{_GITHUB_API}/repos/{repository}/pulls/{pull_number}"
        response = self._get(url, resource="pull-request")
        data = self._read_json_object(response, resource="pull-request")
        return self._parse_pull_request(repository, pull_number, data)

    def get_changed_files(
        self,
        identity: PullRequestIdentity,
    ) -> tuple[ChangedFile, ...]:
        """Acquire all changed files and reconcile them with PR metadata.

        Pagination is complete only when the validated record count equals the
        ``changed_files`` count already bound into ``identity``. A valid page is
        not sufficient evidence that every page was acquired, so partial evidence
        is rejected before dependency interpretation can begin.

        Returns:
            An immutable tuple containing every validated changed-file record.
        """

        if identity.changed_files > _MAX_CHANGED_FILES:
            raise GitHubResponseError(
                "The pull request exceeds the current complete changed-file "
                f"acquisition limit of {_MAX_CHANGED_FILES} files."
            )
        if identity.changed_files == 0:
            return ()

        url = (
            f"{_GITHUB_API}/repos/{identity.repository}/pulls/"
            f"{identity.number}/files"
        )
        records: list[ChangedFile] = []
        page = 1

        # Completeness invariant: PR metadata supplies both the pagination target
        # and the final independent count against which acquisition is reconciled.
        while len(records) < identity.changed_files:
            response = self._get(
                url,
                resource="changed-file",
                params={"per_page": _CHANGED_FILES_PER_PAGE, "page": page},
            )
            items = self._read_json_array(response, resource="changed-file")
            if not items:
                break

            # Each array item remains untrusted until runtime checks convert it to
            # a ``ChangedFile``. Static type hints cannot validate external JSON.
            for item_index, item in enumerate(items):
                if not isinstance(item, Mapping):
                    raise GitHubResponseError(
                        "GitHub changed-file response item "
                        f"{len(records) + item_index + 1} was not an object."
                    )
                records.append(self._parse_changed_file(item))

            # With ``per_page=100``, a shorter page indicates that GitHub has no
            # later page. The final metadata-count check still proves completeness.
            if len(items) < _CHANGED_FILES_PER_PAGE:
                break
            page += 1

        if len(records) != identity.changed_files:
            raise GitHubResponseError(
                "GitHub pull-request metadata and changed-file acquisition disagree: "
                f"expected {identity.changed_files} records but acquired "
                f"{len(records)}."
            )

        # A tuple prevents callers from adding, removing, or reordering validated
        # records in place after the completeness check has succeeded.
        return tuple(records)

    def _get(
        self,
        url: str,
        *,
        resource: str,
        params: Mapping[str, int] | None = None,
    ) -> Response:
        """Issue one read-only request and classify transport and HTTP failures.

        Transport exceptions occur before a usable response exists. HTTP errors
        occur after a response exists but before its body is accepted as evidence.
        """

        try:
            kwargs: dict[str, Any] = {
                "headers": self._headers,
                "timeout": self._timeout,
            }
            if params is not None:
                kwargs["params"] = params
            response = self._session.get(url, **kwargs)
        except Timeout as exc:
            # ``raise ... from exc`` preserves the Requests exception as the
            # explicit cause while exposing UpgradePilot's stable error category.
            raise GitHubAcquisitionError(
                f"GitHub {resource} acquisition timed out.",
                reason="timeout",
            ) from exc
        except RequestException as exc:
            raise GitHubAcquisitionError(
                f"GitHub {resource} acquisition failed before a usable "
                "response was received.",
                reason="transport_error",
            ) from exc

        # Status must be accepted before any response body is treated as evidence.
        self._raise_for_status(response, resource=resource)
        return response

    @staticmethod
    def _raise_for_status(response: Response, *, resource: str) -> None:
        """Map non-success HTTP statuses to bounded acquisition reasons.

        The method is static because status classification depends only on its
        arguments and requires no client instance state.
        """

        status = response.status_code
        if 200 <= status < 300:
            return
        if status == 404:
            # GitHub deliberately uses 404 for both nonexistent and inaccessible
            # resources, so the product must preserve that ambiguity.
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
    def _read_json_object(
        response: Response,
        *,
        resource: str,
    ) -> Mapping[str, Any]:
        """Decode successful JSON and require an object-shaped top level."""

        data = _read_json(response, resource=resource)
        # ``Mapping`` accepts dictionary-like objects without unnecessarily
        # requiring the concrete built-in ``dict`` type.
        if not isinstance(data, Mapping):
            raise GitHubResponseError(
                f"GitHub returned JSON, but the {resource} response was not an object."
            )
        return data

    @staticmethod
    def _read_json_array(
        response: Response,
        *,
        resource: str,
    ) -> list[Any]:
        """Decode successful JSON and require an array-shaped top level."""

        data = _read_json(response, resource=resource)
        if not isinstance(data, list):
            raise GitHubResponseError(
                f"GitHub returned JSON, but the {resource} response was not an array."
            )
        return data

    @staticmethod
    def _parse_pull_request(
        repository: str,
        pull_number: int,
        data: Mapping[str, Any],
    ) -> PullRequestIdentity:
        """Convert untrusted PR JSON into an exact immutable identity.

        Required-field helpers perform runtime type checks. The additional number
        comparison is semantic validation: individually valid fields may still
        describe a different pull request than the one requested.
        """

        try:
            base = _required_mapping(data, "base")
            head = _required_mapping(data, "head")
            user = _required_mapping(data, "user")
            number = _required_int(data, "number")
            if number != pull_number:
                raise GitHubResponseError(
                    "GitHub returned a different pull-request number than requested."
                )
            return PullRequestIdentity(
                repository=repository,
                number=number,
                title=_required_str(data, "title"),
                state=_required_str(data, "state"),
                merged=_required_bool(data, "merged"),
                author=_required_str(user, "login"),
                base_ref=_required_str(base, "ref"),
                base_sha=_required_str(base, "sha"),
                head_ref=_required_str(head, "ref"),
                head_sha=_required_str(head, "sha"),
                changed_files=_required_nonnegative_int(data, "changed_files"),
            )
        except KeyError as exc:
            # Dictionary indexing intentionally raises ``KeyError`` for absence;
            # exception translation exposes a domain-specific response error.
            raise GitHubResponseError(
                f"GitHub response is missing required field: {exc.args[0]}."
            ) from exc

    @staticmethod
    def _parse_changed_file(data: Mapping[str, Any]) -> ChangedFile:
        """Convert one untrusted changed-file object into a validated record."""

        try:
            # ``dict.get`` distinguishes an absent optional field from required
            # fields below, which deliberately use indexing and raise ``KeyError``.
            patch = data.get("patch")
            if patch is not None and not isinstance(patch, str):
                raise GitHubResponseError(
                    "GitHub field 'patch' must be text or absent."
                )
            return ChangedFile(
                filename=_required_str(data, "filename"),
                status=_required_str(data, "status"),
                additions=_required_nonnegative_int(data, "additions"),
                deletions=_required_nonnegative_int(data, "deletions"),
                changes=_required_nonnegative_int(data, "changes"),
                patch=patch,
            )
        except KeyError as exc:
            raise GitHubResponseError(
                "GitHub changed-file response is missing required field: "
                f"{exc.args[0]}."
            ) from exc


def validate_repository(repository: str) -> str:
    """Return a normalized locator in the supported ``owner/repository`` form.

    Surrounding whitespace is removed before ``fullmatch`` checks the entire
    locator. Substrings and URL-shaped inputs are intentionally rejected.
    """

    normalized = repository.strip()
    if not _REPOSITORY_PATTERN.fullmatch(normalized):
        raise UpgradePilotInputError(
            "Repository must use the supported 'owner/repository' form."
        )
    return normalized


def validate_pull_number(pull_number: int) -> int:
    """Return a positive PR number while rejecting booleans as integers."""

    # ``bool`` is a subclass of ``int`` in Python: ``isinstance(True, int)`` is
    # true. The explicit first condition prevents ``True`` from becoming PR 1.
    if (
        isinstance(pull_number, bool)
        or not isinstance(pull_number, int)
        or pull_number < 1
    ):
        raise UpgradePilotInputError("Pull-request number must be a positive integer.")
    return pull_number


def _read_json(response: Response, *, resource: str) -> Any:
    """Decode a successful response body or raise a response-evidence error."""

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError as exc:
        # A 2xx response only establishes HTTP success; it does not establish that
        # the body is valid JSON or contains usable evidence.
        raise GitHubResponseError(
            f"GitHub returned a successful {resource} response that was not valid JSON."
        ) from exc


def _required_mapping(data: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    """Return a required JSON object field after runtime type validation."""

    value = data[key]
    if not isinstance(value, Mapping):
        raise GitHubResponseError(f"GitHub field '{key}' must be an object.")
    return value


def _required_str(data: Mapping[str, Any], key: str) -> str:
    """Return a required non-empty JSON string field."""

    value = data[key]
    if not isinstance(value, str) or not value:
        raise GitHubResponseError(f"GitHub field '{key}' must be a non-empty string.")
    return value


def _required_int(data: Mapping[str, Any], key: str) -> int:
    """Return a required JSON integer field while rejecting booleans."""

    value = data[key]
    # JSON booleans decode to Python ``bool`` objects, which would otherwise pass
    # an ``isinstance(value, int)`` check because of Python's class hierarchy.
    if isinstance(value, bool) or not isinstance(value, int):
        raise GitHubResponseError(f"GitHub field '{key}' must be an integer.")
    return value


def _required_nonnegative_int(data: Mapping[str, Any], key: str) -> int:
    """Return a required integer field constrained to zero or greater."""

    # Reuse the base integer validator so boolean rejection and error wording stay
    # consistent before applying the more specific nonnegative invariant.
    value = _required_int(data, key)
    if value < 0:
        raise GitHubResponseError(f"GitHub field '{key}' must not be negative.")
    return value


def _required_bool(data: Mapping[str, Any], key: str) -> bool:
    """Return a required JSON boolean field."""

    value = data[key]
    if not isinstance(value, bool):
        raise GitHubResponseError(f"GitHub field '{key}' must be a boolean.")
    return value
