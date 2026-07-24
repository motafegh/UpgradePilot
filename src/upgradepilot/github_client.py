"""Read-only GitHub acquisition for the first UpgradePilot vertical slice."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping
import re

import requests
from requests import Response, Session
from requests.exceptions import RequestException, Timeout

_GITHUB_API = "https://api.github.com"
_API_VERSION = "2022-11-28"
_DEFAULT_TIMEOUT = (3.05, 15.0)
_REPOSITORY_PATTERN = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9_.-]{0,99})/[A-Za-z0-9_.-]{1,100}$"
)


class UpgradePilotInputError(ValueError):
    """The user-supplied repository or pull-request locator is unsupported."""


class GitHubAcquisitionError(RuntimeError):
    """GitHub evidence could not be acquired."""

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
    """GitHub returned success, but the response lacked required evidence."""


@dataclass(frozen=True, slots=True)
class PullRequestIdentity:
    """Exact public pull-request identity acquired from GitHub."""

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


class GitHubReadClient:
    """Small read-only client for public GitHub pull-request evidence."""

    def __init__(
        self,
        *,
        token: str | None = None,
        session: Session | None = None,
        timeout: tuple[float, float] = _DEFAULT_TIMEOUT,
    ) -> None:
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
        """Acquire and validate exact identity for one public pull request."""

        repository = validate_repository(repository)
        pull_number = validate_pull_number(pull_number)
        url = f"{_GITHUB_API}/repos/{repository}/pulls/{pull_number}"

        try:
            response = self._session.get(
                url,
                headers=self._headers,
                timeout=self._timeout,
            )
        except Timeout as exc:
            raise GitHubAcquisitionError(
                "GitHub pull-request acquisition timed out.",
                reason="timeout",
            ) from exc
        except RequestException as exc:
            raise GitHubAcquisitionError(
                "GitHub pull-request acquisition failed before a usable response was received.",
                reason="transport_error",
            ) from exc

        self._raise_for_status(response)
        data = self._read_json_object(response)
        return self._parse_pull_request(repository, pull_number, data)

    @staticmethod
    def _raise_for_status(response: Response) -> None:
        status = response.status_code
        if 200 <= status < 300:
            return
        if status == 404:
            raise GitHubAcquisitionError(
                "No accessible pull request was found at the supplied locator.",
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
            f"GitHub returned HTTP {status} while acquiring the pull request.",
            reason="http_error",
            status_code=status,
        )

    @staticmethod
    def _read_json_object(response: Response) -> Mapping[str, Any]:
        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError as exc:
            raise GitHubResponseError(
                "GitHub returned a successful response that was not valid JSON."
            ) from exc
        if not isinstance(data, Mapping):
            raise GitHubResponseError(
                "GitHub returned JSON, but the pull-request response was not an object."
            )
        return data

    @staticmethod
    def _parse_pull_request(
        repository: str,
        pull_number: int,
        data: Mapping[str, Any],
    ) -> PullRequestIdentity:
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
                changed_files=_required_int(data, "changed_files"),
            )
        except KeyError as exc:
            raise GitHubResponseError(
                f"GitHub response is missing required field: {exc.args[0]}."
            ) from exc


def validate_repository(repository: str) -> str:
    """Validate the initial supported ``owner/repository`` locator."""

    normalized = repository.strip()
    if not _REPOSITORY_PATTERN.fullmatch(normalized):
        raise UpgradePilotInputError(
            "Repository must use the supported 'owner/repository' form."
        )
    return normalized


def validate_pull_number(pull_number: int) -> int:
    """Validate a positive GitHub pull-request number."""

    if isinstance(pull_number, bool) or not isinstance(pull_number, int) or pull_number < 1:
        raise UpgradePilotInputError("Pull-request number must be a positive integer.")
    return pull_number


def _required_mapping(data: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    value = data[key]
    if not isinstance(value, Mapping):
        raise GitHubResponseError(f"GitHub field '{key}' must be an object.")
    return value


def _required_str(data: Mapping[str, Any], key: str) -> str:
    value = data[key]
    if not isinstance(value, str) or not value:
        raise GitHubResponseError(f"GitHub field '{key}' must be a non-empty string.")
    return value


def _required_int(data: Mapping[str, Any], key: str) -> int:
    value = data[key]
    if isinstance(value, bool) or not isinstance(value, int):
        raise GitHubResponseError(f"GitHub field '{key}' must be an integer.")
    return value


def _required_bool(data: Mapping[str, Any], key: str) -> bool:
    value = data[key]
    if not isinstance(value, bool):
        raise GitHubResponseError(f"GitHub field '{key}' must be a boolean.")
    return value
