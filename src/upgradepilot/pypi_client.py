"""Acquire exact package-release identity from PyPI.

PyPI can establish that a Python distribution and exact version were published. It
cannot by itself prove compatibility or interpret release notes, so this module stops
at identity, provenance, and publisher-supplied link candidates.
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
    """A publisher-supplied link whose upstream authority is not yet proven."""

    label: str
    url: str


@dataclass(frozen=True, slots=True)
class PackageReleaseEvidence:
    """Validated identity and provenance for one exact PyPI release."""

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
    project_urls: tuple[ProjectUrlCandidate, ...]


@dataclass(frozen=True, slots=True)
class PackageReleaseProblem:
    """A bounded reason why trusted release identity was not established."""

    state: PackageReleaseProblemState
    requested_package: str
    normalized_package: str
    requested_version: str
    source_url: str
    detail: str
    status_code: int | None = None


type PackageReleaseResult = PackageReleaseEvidence | PackageReleaseProblem


class _MalformedResponse(ValueError):
    """The HTTP response arrived but did not satisfy the trusted JSON contract."""


class _BodyAcquisitionFailure(RuntimeError):
    """The response body failed while it was being streamed."""


class PyPIReleaseClient:
    """Read exact PyPI release metadata through a small read-only boundary."""

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
        """Return exact release evidence or an explicit non-success state."""

        requested_package = _valid_package(package)
        requested_version = _nonempty_text(version, "version")
        normalized_package = normalize_package_name(requested_package)
        source_url = _release_url(normalized_package, requested_version)

        response = self._get(
            source_url,
            requested_package,
            normalized_package,
            requested_version,
        )
        if isinstance(response, PackageReleaseProblem):
            return response

        if response.status_code == 404:
            response.close()
            return self._classify_release_404(
                requested_package,
                normalized_package,
                requested_version,
                source_url,
            )
        if not 200 <= response.status_code < 300:
            return self._http_problem(
                response,
                requested_package,
                normalized_package,
                requested_version,
                source_url,
                resource="release",
            )

        try:
            data = self._read_json_object(response)
            return self._parse_release(
                data,
                requested_package,
                normalized_package,
                requested_version,
                source_url,
            )
        except _BodyAcquisitionFailure:
            return self._problem(
                "acquisition_failed",
                requested_package,
                normalized_package,
                requested_version,
                source_url,
                "PyPI response ended before its complete body was acquired.",
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

    def _classify_release_404(
        self,
        package: str,
        normalized_package: str,
        version: str,
        release_url: str,
    ) -> PackageReleaseProblem:
        """Distinguish a missing version from an inaccessible package record."""

        response = self._get(
            _project_url(normalized_package),
            package,
            normalized_package,
            version,
            reported_source_url=release_url,
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
            return self._http_problem(
                response,
                package,
                normalized_package,
                version,
                release_url,
                resource="package",
            )

        try:
            data = self._read_json_object(response)
            published_name = _required_string(_required_mapping(data, "info"), "name")
        except _BodyAcquisitionFailure:
            return self._problem(
                "acquisition_failed",
                package,
                normalized_package,
                version,
                release_url,
                "PyPI package lookup ended before its complete body was acquired.",
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
        """Cross the JSON trust boundary and preserve exact requested identity."""

        info = _required_mapping(data, "info")
        published_name = _required_string(info, "name")
        published_version = _required_string(info, "version")

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
        # Exact comparison prevents a successful endpoint from silently changing version.
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
            last_serial=_required_nonnegative_int(data, "last_serial"),
            distribution_file_count=len(_required_list(data, "urls")),
            project_urls=_project_urls(info),
        )

    def _get(
        self,
        url: str,
        package: str,
        normalized_package: str,
        version: str,
        *,
        reported_source_url: str | None = None,
    ) -> Response | PackageReleaseProblem:
        """Send a streamed GET so the configured body limit can be enforced."""

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
            reported_source_url or url,
            detail,
        )

    def _read_json_object(self, response: Response) -> Mapping[str, Any]:
        """Read at most the configured bytes, close the response, and decode JSON."""

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
            try:
                for chunk in response.iter_content(chunk_size=8192):
                    if not chunk:
                        continue
                    body.extend(chunk)
                    if len(body) > self._max_response_bytes:
                        raise _MalformedResponse(
                            "PyPI response exceeded the configured size limit."
                        )
            except RequestException as exc:
                raise _BodyAcquisitionFailure from exc
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
        *,
        resource: str,
    ) -> PackageReleaseProblem:
        status_code = response.status_code
        response.close()
        return self._problem(
            "acquisition_failed",
            package,
            normalized_package,
            version,
            source_url,
            f"PyPI returned HTTP {status_code} for the {resource} request.",
            status_code,
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
    """Freeze metadata links as candidates without granting upstream authority."""

    raw = info.get("project_urls")
    if raw is None:
        return ()
    if not isinstance(raw, Mapping):
        raise _MalformedResponse("PyPI field 'project_urls' must be an object or null.")

    candidates: list[ProjectUrlCandidate] = []
    for label, url in raw.items():
        if not isinstance(label, str) or not label:
            raise _MalformedResponse("Project URL labels must be non-empty strings.")
        if not isinstance(url, str) or not url:
            raise _MalformedResponse(f"Project URL {label!r} must be non-empty text.")
        candidates.append(ProjectUrlCandidate(label=label, url=url))
    return tuple(sorted(candidates, key=lambda item: item.label.casefold()))


def _valid_package(value: str) -> str:
    package = _nonempty_text(value, "package")
    if _PACKAGE_NAME.fullmatch(package) is None:
        raise ValueError("package is not a valid Python distribution name.")
    return package


def _nonempty_text(value: str, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string.")
    return value.strip()


def _required_field(data: Mapping[str, Any], key: str) -> Any:
    try:
        return data[key]
    except KeyError as exc:
        raise _MalformedResponse(f"PyPI response is missing field {key!r}.") from exc


def _required_mapping(data: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    value = _required_field(data, key)
    if not isinstance(value, Mapping):
        raise _MalformedResponse(f"PyPI field {key!r} must be an object.")
    return value


def _required_list(data: Mapping[str, Any], key: str) -> list[Any]:
    value = _required_field(data, key)
    if not isinstance(value, list):
        raise _MalformedResponse(f"PyPI field {key!r} must be an array.")
    return value


def _required_string(data: Mapping[str, Any], key: str) -> str:
    value = _required_field(data, key)
    if not isinstance(value, str) or not value:
        raise _MalformedResponse(f"PyPI field {key!r} must be non-empty text.")
    return value


def _required_nonnegative_int(data: Mapping[str, Any], key: str) -> int:
    value = _required_field(data, key)
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise _MalformedResponse(f"PyPI field {key!r} must be a non-negative integer.")
    return value


def _release_url(package: str, version: str) -> str:
    return f"{PYPI_JSON_ROOT}/{quote(package, safe='')}/{quote(version, safe='')}/json"


def _project_url(package: str) -> str:
    return f"{PYPI_JSON_ROOT}/{quote(package, safe='')}/json"
