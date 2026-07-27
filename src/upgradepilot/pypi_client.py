"""Validate exact Python package releases with the official PyPI JSON API.

This boundary proves package/version identity and preserves publisher-supplied project
links. It does not interpret release notes or claim upgrade compatibility.
"""

from __future__ import annotations

import json
import re
from collections.abc import Callable, Mapping
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Literal
from urllib.parse import quote

import requests
from requests import Response, Session
from requests.exceptions import RequestException, Timeout

from .dependency_change import normalize_package_name

PYPI_JSON_ROOT = "https://pypi.org/pypi"
DEFAULT_TIMEOUT = (3.05, 15.0)
DEFAULT_MAX_RESPONSE_BYTES = 1_000_000
_PACKAGE_NAME = re.compile(
    r"^([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9._-]*[A-Za-z0-9])\Z"
)

type PackageReleaseProblemState = Literal[
    "package_not_found_or_inaccessible",
    "version_not_found",
    "identity_mismatch",
    "malformed_response",
    "acquisition_failed",
]


@dataclass(frozen=True, slots=True)
class ProjectUrlCandidate:
    """Publisher-supplied link; authority is not yet established."""

    label: str
    url: str


@dataclass(frozen=True, slots=True)
class PackageReleaseEvidence:
    """Trusted identity for one exact release returned by PyPI."""

    state: Literal["available"] = field(init=False, default="available")
    requested_package: str
    normalized_package: str
    requested_version: str
    published_name: str
    published_version: str
    source_url: str
    retrieved_at: datetime
    last_serial: int
    distribution_file_count: int
    yanked: bool
    yanked_reason: str | None
    project_urls: tuple[ProjectUrlCandidate, ...]


@dataclass(frozen=True, slots=True)
class PackageReleaseProblem:
    """Explicit reason trusted release identity was not established."""

    state: PackageReleaseProblemState
    requested_package: str
    normalized_package: str
    requested_version: str
    source_url: str
    detail: str
    status_code: int | None = None


type PackageReleaseResult = PackageReleaseEvidence | PackageReleaseProblem


class _MalformedResponse(ValueError):
    """Internal parse error converted to a public problem state."""


class PyPIReleaseClient:
    """Acquire exact PyPI release identity without semantic interpretation."""

    def __init__(
        self,
        *,
        session: Session | None = None,
        timeout: tuple[float, float] = DEFAULT_TIMEOUT,
        max_response_bytes: int = DEFAULT_MAX_RESPONSE_BYTES,
        now: Callable[[], datetime] | None = None,
    ) -> None:
        if max_response_bytes < 1:
            raise ValueError("max_response_bytes must be positive.")
        self._session = session or requests.Session()
        self._timeout = timeout
        self._max_response_bytes = max_response_bytes
        self._now = now or (lambda: datetime.now(timezone.utc))
        self._headers = {
            "Accept": "application/json",
            "User-Agent": "UpgradePilot/0.0.0",
        }

    def get_release(self, package: str, version: str) -> PackageReleaseResult:
        """Return exact release evidence or a bounded failure state."""

        requested_package = _valid_package(package)
        requested_version = _text(version, "version")
        normalized_package = normalize_package_name(requested_package)
        source_url = _release_url(normalized_package, requested_version)

        response = self._request_or_problem(
            source_url,
            requested_package,
            normalized_package,
            requested_version,
        )
        if isinstance(response, PackageReleaseProblem):
            return response

        if response.status_code == 404:
            response.close()
            return self._classify_404(
                requested_package,
                normalized_package,
                requested_version,
                source_url,
            )
        if not 200 <= response.status_code < 300:
            problem = self._http_problem(
                response,
                requested_package,
                normalized_package,
                requested_version,
                source_url,
                "release",
            )
            response.close()
            return problem

        try:
            data = self._json_object(response)
            return self._parse_release(
                data,
                requested_package,
                normalized_package,
                requested_version,
                source_url,
            )
        except RequestException:
            return self._problem(
                "acquisition_failed",
                requested_package,
                normalized_package,
                requested_version,
                source_url,
                "PyPI response ended before the complete body was acquired.",
                response.status_code,
            )
        except _MalformedResponse as exc:
            return self._problem(
                "malformed_response",
                requested_package,
                normalized_package,
                requested_version,
                source_url,
                str(exc),
                response.status_code,
            )

    def _classify_404(
        self,
        package: str,
        normalized_package: str,
        version: str,
        release_url: str,
    ) -> PackageReleaseProblem:
        """Check whether the package exists before declaring the version absent."""

        response = self._request_or_problem(
            _project_url(normalized_package),
            package,
            normalized_package,
            version,
            source_url=release_url,
        )
        if isinstance(response, PackageReleaseProblem):
            return response
        if response.status_code == 404:
            response.close()
            return self._problem(
                "package_not_found_or_inaccessible",
                package,
                normalized_package,
                version,
                release_url,
                "No accessible PyPI package record was established.",
                404,
            )
        if not 200 <= response.status_code < 300:
            problem = self._http_problem(
                response,
                package,
                normalized_package,
                version,
                release_url,
                "package",
            )
            response.close()
            return problem

        try:
            data = self._json_object(response)
            published_name = _string(_mapping(data, "info"), "name")
        except RequestException:
            return self._problem(
                "acquisition_failed",
                package,
                normalized_package,
                version,
                release_url,
                "PyPI package lookup ended before the complete body was acquired.",
                response.status_code,
            )
        except _MalformedResponse as exc:
            return self._problem(
                "malformed_response",
                package,
                normalized_package,
                version,
                release_url,
                str(exc),
                response.status_code,
            )

        if normalize_package_name(published_name) != normalized_package:
            return self._problem(
                "identity_mismatch",
                package,
                normalized_package,
                version,
                release_url,
                f"PyPI package lookup returned conflicting name {published_name!r}.",
                response.status_code,
            )
        return self._problem(
            "version_not_found",
            package,
            normalized_package,
            version,
            release_url,
            "The package exists, but the exact proposed version was not established.",
            404,
        )

    def _parse_release(
        self,
        data: Mapping[str, Any],
        package: str,
        normalized_package: str,
        version: str,
        source_url: str,
    ) -> PackageReleaseResult:
        info = _mapping(data, "info")
        published_name = _string(info, "name")
        published_version = _string(info, "version")

        if normalize_package_name(published_name) != normalized_package:
            return self._problem(
                "identity_mismatch",
                package,
                normalized_package,
                version,
                source_url,
                f"PyPI returned conflicting package name {published_name!r}.",
                200,
            )
        # Exact comparison prevents a successful endpoint from changing the question.
        if published_version != version:
            return self._problem(
                "identity_mismatch",
                package,
                normalized_package,
                version,
                source_url,
                f"PyPI returned conflicting version {published_version!r}.",
                200,
            )

        return PackageReleaseEvidence(
            requested_package=package,
            normalized_package=normalized_package,
            requested_version=version,
            published_name=published_name,
            published_version=published_version,
            source_url=source_url,
            retrieved_at=self._now(),
            last_serial=_integer(data, "last_serial"),
            distribution_file_count=len(_list(data, "urls")),
            yanked=_boolean(info, "yanked"),
            yanked_reason=_nullable_string(info, "yanked_reason"),
            project_urls=_project_urls(info),
        )

    def _request_or_problem(
        self,
        url: str,
        package: str,
        normalized_package: str,
        version: str,
        *,
        source_url: str | None = None,
    ) -> Response | PackageReleaseProblem:
        try:
            return self._session.get(
                url,
                headers=self._headers,
                timeout=self._timeout,
                stream=True,
            )
        except Timeout:
            detail = "PyPI acquisition timed out."
        except RequestException:
            detail = "PyPI acquisition failed before a usable response arrived."
        return self._problem(
            "acquisition_failed",
            package,
            normalized_package,
            version,
            source_url or url,
            detail,
        )

    def _json_object(self, response: Response) -> Mapping[str, Any]:
        """Read a bounded body, close the response, and require a JSON object."""

        try:
            declared = response.headers.get("Content-Length")
            if declared is not None:
                try:
                    declared_size = int(declared)
                except ValueError as exc:
                    raise _MalformedResponse(
                        "PyPI returned a non-numeric Content-Length header."
                    ) from exc
                if declared_size < 0 or declared_size > self._max_response_bytes:
                    raise _MalformedResponse(
                        "PyPI response exceeded the configured size limit."
                    )

            body = bytearray()
            for chunk in response.iter_content(chunk_size=8192):
                if not chunk:
                    continue
                body.extend(chunk)
                if len(body) > self._max_response_bytes:
                    raise _MalformedResponse(
                        "PyPI response exceeded the configured size limit."
                    )
        finally:
            response.close()

        try:
            decoded = json.loads(body)
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            raise _MalformedResponse("PyPI returned HTTP success with invalid JSON.") from exc
        if not isinstance(decoded, Mapping):
            raise _MalformedResponse("PyPI response JSON was not an object.")
        return decoded

    def _http_problem(
        self,
        response: Response,
        package: str,
        normalized_package: str,
        version: str,
        source_url: str,
        resource: str,
    ) -> PackageReleaseProblem:
        return self._problem(
            "acquisition_failed",
            package,
            normalized_package,
            version,
            source_url,
            f"PyPI returned HTTP {response.status_code} for the {resource} request.",
            response.status_code,
        )

    @staticmethod
    def _problem(
        state: PackageReleaseProblemState,
        package: str,
        normalized_package: str,
        version: str,
        source_url: str,
        detail: str,
        status_code: int | None = None,
    ) -> PackageReleaseProblem:
        return PackageReleaseProblem(
            state=state,
            requested_package=package,
            normalized_package=normalized_package,
            requested_version=version,
            source_url=source_url,
            detail=detail,
            status_code=status_code,
        )


def _project_urls(info: Mapping[str, Any]) -> tuple[ProjectUrlCandidate, ...]:
    """Validate and freeze metadata links without treating them as official yet."""

    raw = info.get("project_urls")
    if raw is None:
        return ()
    if not isinstance(raw, Mapping):
        raise _MalformedResponse("'project_urls' must be an object or null.")

    candidates: list[ProjectUrlCandidate] = []
    for label, url in raw.items():
        if not isinstance(label, str) or not label:
            raise _MalformedResponse("Project URL labels must be non-empty strings.")
        if not isinstance(url, str) or not url:
            raise _MalformedResponse(f"Project URL {label!r} must be non-empty text.")
        candidates.append(ProjectUrlCandidate(label, url))
    return tuple(sorted(candidates, key=lambda item: item.label.casefold()))


def _valid_package(value: str) -> str:
    package = _text(value, "package")
    if _PACKAGE_NAME.fullmatch(package) is None:
        raise ValueError("package is not a valid Python distribution name.")
    return package


def _text(value: str, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string.")
    return value.strip()


def _field(data: Mapping[str, Any], key: str) -> Any:
    try:
        return data[key]
    except KeyError as exc:
        raise _MalformedResponse(f"PyPI response is missing field {key!r}.") from exc


def _mapping(data: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    value = _field(data, key)
    if not isinstance(value, Mapping):
        raise _MalformedResponse(f"PyPI field {key!r} must be an object.")
    return value


def _list(data: Mapping[str, Any], key: str) -> list[Any]:
    value = _field(data, key)
    if not isinstance(value, list):
        raise _MalformedResponse(f"PyPI field {key!r} must be an array.")
    return value


def _string(data: Mapping[str, Any], key: str) -> str:
    value = _field(data, key)
    if not isinstance(value, str) or not value:
        raise _MalformedResponse(f"PyPI field {key!r} must be non-empty text.")
    return value


def _nullable_string(data: Mapping[str, Any], key: str) -> str | None:
    value = _field(data, key)
    if value is not None and (not isinstance(value, str) or not value):
        raise _MalformedResponse(f"PyPI field {key!r} must be text or null.")
    return value


def _integer(data: Mapping[str, Any], key: str) -> int:
    value = _field(data, key)
    if isinstance(value, bool) or not isinstance(value, int):
        raise _MalformedResponse(f"PyPI field {key!r} must be an integer.")
    return value


def _boolean(data: Mapping[str, Any], key: str) -> bool:
    value = _field(data, key)
    if not isinstance(value, bool):
        raise _MalformedResponse(f"PyPI field {key!r} must be a boolean.")
    return value


def _release_url(package: str, version: str) -> str:
    return f"{PYPI_JSON_ROOT}/{quote(package, safe='')}/{quote(version, safe='')}/json"


def _project_url(package: str) -> str:
    return f"{PYPI_JSON_ROOT}/{quote(package, safe='')}/json"
