"""Acquire exact package-release and package release-index evidence from PyPI."""

from __future__ import annotations

import re
from collections.abc import Callable, Mapping
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Literal, TypeVar
from urllib.parse import quote

from requests import Response, Session

from ..json_contract import (
    JsonContractViolation,
    expect_list,
    expect_mapping,
    expect_nonempty_text,
    expect_nonnegative_integer,
)
from ..package_identity import normalize_package_name
from .api import (
    DEFAULT_MAX_RESPONSE_BYTES,
    DEFAULT_TIMEOUT,
    PyPIJsonApiClient,
    PyPIRequestError,
    PyPIResponseError,
)

PYPI_JSON_ROOT = "https://pypi.org/pypi"
_PACKAGE_NAME = re.compile(
    r"^([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9._-]*[A-Za-z0-9])\Z"
)
_SHA256 = re.compile(r"^[0-9a-fA-F]{64}\Z")
_MAX_RELEASE_ADVISORY_ENTRIES = 32
_ADVISORY_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")
_WITHDRAWAL_TIMESTAMP = re.compile(
    r"[0-9]{4}-[0-9]{2}-[0-9]{2}[Tt](?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]"
    r"(?:\.[0-9]+)?(?:[Zz]|[+-](?:[01][0-9]|2[0-3]):[0-5][0-9])"
)
_T = TypeVar("_T")

type PackageReleaseProblemState = Literal[
    "package_not_found_or_inaccessible",
    "version_not_found",
    "identity_mismatch",
    "malformed_response",
    "acquisition_failed",
]
type PackageReleaseIndexProblemState = Literal[
    "package_not_found_or_inaccessible",
    "identity_mismatch",
    "malformed_response",
    "acquisition_failed",
]


@dataclass(frozen=True, slots=True)
class ProjectUrlCandidate:
    label: str
    url: str


@dataclass(frozen=True, slots=True)
class DistributionFile:
    filename: str
    url: str
    sha256: str
    package_type: str


@dataclass(frozen=True, slots=True)
class PublishedFileRequiresPython:
    """Selected requirements and yank status for one exact published file."""

    filename: str
    sha256: str
    requires_python: str | None
    yanked: bool | None


MAX_FILE_PYTHON_DECLARATIONS = 128
MAX_REQUIRES_PYTHON_TEXT = 256


type ReleaseAdvisoryState = Literal["reported", "withdrawn"]


@dataclass(frozen=True, slots=True)
class ReleaseAdvisory:
    advisory_id: str
    state: ReleaseAdvisoryState


@dataclass(frozen=True, slots=True)
class ReleaseAdvisoryObservation:
    state: Literal["entries_recorded", "empty_list", "field_missing", "malformed", "conflicting_ids", "over_limit"]
    entries: tuple[ReleaseAdvisory, ...] = ()


@dataclass(frozen=True, slots=True)
class PackageReleaseEvidence:
    state: Literal["available"] = field(init=False, default="available")
    requested_package: str
    normalized_package: str
    requested_version: str
    published_name: str
    published_version: str
    source_url: str
    retrieved_at: datetime
    last_serial: int
    distribution_files: tuple[DistributionFile, ...]
    project_urls: tuple[ProjectUrlCandidate, ...]

    @property
    def distribution_file_count(self) -> int:
        return len(self.distribution_files)


@dataclass(frozen=True, slots=True, kw_only=True)
class PackageReleaseEvidenceWithAdvisories(PackageReleaseEvidence):
    """Ordinary report evidence beyond the fixed caller/signature source layout."""

    advisories: ReleaseAdvisoryObservation


@dataclass(frozen=True, slots=True)
class PackageReleaseProblem:
    state: PackageReleaseProblemState
    requested_package: str
    normalized_package: str
    requested_version: str
    source_url: str
    detail: str
    status_code: int | None = None


type PackageReleaseResult = PackageReleaseEvidence | PackageReleaseProblem


@dataclass(frozen=True, slots=True)
class PackageReleaseIndexEvidence:
    state: Literal["available"] = field(init=False, default="available")
    requested_package: str
    normalized_package: str
    published_name: str
    source_url: str
    retrieved_at: datetime
    last_serial: int
    release_versions: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class PackageReleaseIndexProblem:
    state: PackageReleaseIndexProblemState
    requested_package: str
    normalized_package: str
    source_url: str
    detail: str
    status_code: int | None = None


type PackageReleaseIndexResult = PackageReleaseIndexEvidence | PackageReleaseIndexProblem


@dataclass(frozen=True, slots=True)
class _ReleaseRequest:
    package: str
    normalized_package: str
    version: str
    source_url: str


@dataclass(frozen=True, slots=True)
class _ProjectRequest:
    package: str
    normalized_package: str
    source_url: str


class _MalformedResponse(ValueError):
    pass


def _is_withdrawal_timestamp(value: object) -> bool:
    if not isinstance(value, str) or not _WITHDRAWAL_TIMESTAMP.fullmatch(value):
        return False
    try:
        datetime.fromisoformat(value.upper())
    except ValueError:
        return False
    return True


def _release_advisories(data: Mapping[str, Any]) -> ReleaseAdvisoryObservation:
    """Admit the optional release field without changing package availability."""
    if "vulnerabilities" not in data:
        return ReleaseAdvisoryObservation("field_missing")
    rows = data["vulnerabilities"]
    if not isinstance(rows, list):
        return ReleaseAdvisoryObservation("malformed")
    if len(rows) > _MAX_RELEASE_ADVISORY_ENTRIES:
        return ReleaseAdvisoryObservation("over_limit")
    if not rows:
        return ReleaseAdvisoryObservation("empty_list")

    entries: dict[str, ReleaseAdvisory] = {}
    for row in rows:
        if not isinstance(row, dict) or "withdrawn" not in row:
            return ReleaseAdvisoryObservation("malformed")
        advisory_id = row.get("id")
        if not isinstance(advisory_id, str) or not _ADVISORY_ID.fullmatch(advisory_id):
            return ReleaseAdvisoryObservation("malformed")
        withdrawn = row["withdrawn"]
        if withdrawn is not None and not _is_withdrawal_timestamp(withdrawn):
            return ReleaseAdvisoryObservation("malformed")
        entry = ReleaseAdvisory(advisory_id, "reported" if withdrawn is None else "withdrawn")
        if advisory_id in entries and entries[advisory_id] != entry:
            return ReleaseAdvisoryObservation("conflicting_ids")
        entries[advisory_id] = entry
    return ReleaseAdvisoryObservation("entries_recorded", tuple(entries.values()))


class PyPIReleaseClient(PyPIJsonApiClient):
    def __init__(
        self,
        *,
        session: Session | None = None,
        timeout: tuple[float, float] = DEFAULT_TIMEOUT,
        max_response_bytes: int = DEFAULT_MAX_RESPONSE_BYTES,
        now: Callable[[], datetime] | None = None,
        retain_advisories: bool = False,
        observe_file_python: Callable[
            [PackageReleaseEvidence, tuple[PublishedFileRequiresPython, ...]], None
        ] | None = None,
    ) -> None:
        super().__init__(
            session=session,
            timeout=timeout,
            max_response_bytes=max_response_bytes,
            accept="application/json",
        )
        self._now = now or (lambda: datetime.now(timezone.utc))
        self._retain_advisories = retain_advisories
        self._observe_file_python = observe_file_python

    def get_release(self, package: str, version: str) -> PackageReleaseResult:
        package = _valid_package(package)
        version = _nonempty_text(version, "version")
        normalized = normalize_package_name(package)
        request = _ReleaseRequest(
            package=package,
            normalized_package=normalized,
            version=version,
            source_url=_release_url(normalized, version),
        )

        response = self._get(request.source_url, request, resource="release")
        if isinstance(response, PackageReleaseProblem):
            return response
        if response.status_code == 404:
            response.close()
            return self._classify_release_404(request)
        if not 200 <= response.status_code < 300:
            return self._http_problem(response, request, resource="release")

        data = self._read_or_problem(response, request, resource="release")
        if isinstance(data, PackageReleaseProblem):
            return data
        return self._parse_release(data, request)

    def _classify_release_404(self, request: _ReleaseRequest) -> PackageReleaseProblem:
        response = self._get(
            _project_url(request.normalized_package),
            request,
            resource="package",
        )
        if isinstance(response, PackageReleaseProblem):
            return response
        if response.status_code == 404:
            response.close()
            return self._problem(
                request,
                "package_not_found_or_inaccessible",
                "No accessible PyPI package record was established.",
                404,
            )
        if not 200 <= response.status_code < 300:
            return self._http_problem(response, request, resource="package")

        data = self._read_or_problem(response, request, resource="package")
        if isinstance(data, PackageReleaseProblem):
            return data
        try:
            published_name = _required_string(_required_mapping(data, "info"), "name")
        except _MalformedResponse as exc:
            return self._problem(
                request,
                "malformed_response",
                str(exc),
                response.status_code,
            )

        if normalize_package_name(published_name) != request.normalized_package:
            return self._problem(
                request,
                "identity_mismatch",
                f"PyPI package lookup returned conflicting name {published_name!r}.",
                response.status_code,
            )
        return self._problem(
            request,
            "version_not_found",
            "The package exists, but the exact proposed version was not established.",
            404,
        )

    def _parse_release(
        self,
        data: Mapping[str, Any],
        request: _ReleaseRequest,
    ) -> PackageReleaseResult:
        try:
            info = _required_mapping(data, "info")
            published_name = _required_string(info, "name")
            published_version = _required_string(info, "version")
            last_serial = _required_nonnegative_int(data, "last_serial")
            raw_files = _required_list(data, "urls")
            files = _distribution_files(raw_files)
            project_urls = _project_urls(info)
        except _MalformedResponse as exc:
            return self._problem(request, "malformed_response", str(exc), 200)

        if normalize_package_name(published_name) != request.normalized_package:
            return self._problem(
                request,
                "identity_mismatch",
                f"PyPI returned conflicting package name {published_name!r}.",
                200,
            )
        if published_version != request.version:
            return self._problem(
                request,
                "identity_mismatch",
                f"PyPI returned conflicting version {published_version!r}.",
                200,
            )

        release_fields = dict(
            requested_package=request.package,
            normalized_package=request.normalized_package,
            requested_version=request.version,
            published_name=published_name,
            published_version=published_version,
            source_url=request.source_url,
            retrieved_at=self._now(),
            last_serial=last_serial,
            distribution_files=files,
            project_urls=project_urls,
        )
        if self._retain_advisories:
            release = PackageReleaseEvidenceWithAdvisories(
                **release_fields, advisories=_release_advisories(data),
            )
        else:
            release = PackageReleaseEvidence(**release_fields)
        if self._observe_file_python is not None:
            self._observe_file_python(release, _file_python_declarations(raw_files, files))
        return release

    def _get(
        self,
        url: str,
        request: _ReleaseRequest,
        *,
        resource: str,
    ) -> Response | PackageReleaseProblem:
        try:
            return self._get_response(url, resource=resource)
        except PyPIRequestError as exc:
            return self._problem(
                request,
                "acquisition_failed",
                str(exc),
                exc.status_code,
            )

    def _read_or_problem(
        self,
        response: Response,
        request: _ReleaseRequest,
        *,
        resource: str,
    ) -> Mapping[str, Any] | PackageReleaseProblem:
        try:
            return self._read_json_object(response, resource=resource)
        except PyPIRequestError as exc:
            return self._problem(
                request,
                "acquisition_failed",
                str(exc),
                exc.status_code,
            )
        except PyPIResponseError as exc:
            return self._problem(
                request,
                "malformed_response",
                str(exc),
                response.status_code,
            )

    def _http_problem(
        self,
        response: Response,
        request: _ReleaseRequest,
        *,
        resource: str,
    ) -> PackageReleaseProblem:
        status_code = response.status_code
        response.close()
        return self._problem(
            request,
            "acquisition_failed",
            f"PyPI returned HTTP {status_code} for the {resource} request.",
            status_code,
        )

    @staticmethod
    def _problem(
        request: _ReleaseRequest,
        state: PackageReleaseProblemState,
        detail: str,
        status_code: int | None = None,
    ) -> PackageReleaseProblem:
        return PackageReleaseProblem(
            state=state,
            requested_package=request.package,
            normalized_package=request.normalized_package,
            requested_version=request.version,
            source_url=request.source_url,
            detail=detail,
            status_code=status_code,
        )


class PyPIReleaseIndexClient(PyPIJsonApiClient):
    def __init__(
        self,
        *,
        session: Session | None = None,
        timeout: tuple[float, float] = DEFAULT_TIMEOUT,
        max_response_bytes: int = DEFAULT_MAX_RESPONSE_BYTES,
        now: Callable[[], datetime] | None = None,
    ) -> None:
        super().__init__(
            session=session,
            timeout=timeout,
            max_response_bytes=max_response_bytes,
            accept="application/json",
        )
        self._now = now or (lambda: datetime.now(timezone.utc))

    def get_release_index(self, package: str) -> PackageReleaseIndexResult:
        package = _valid_package(package)
        normalized = normalize_package_name(package)
        request = _ProjectRequest(
            package=package,
            normalized_package=normalized,
            source_url=_project_url(normalized),
        )

        try:
            response = self._get_response(request.source_url, resource="release-index")
        except PyPIRequestError as exc:
            return self._index_problem(
                request,
                "acquisition_failed",
                str(exc),
                exc.status_code,
            )

        if response.status_code == 404:
            response.close()
            return self._index_problem(
                request,
                "package_not_found_or_inaccessible",
                "No accessible PyPI package record was established.",
                404,
            )
        if not 200 <= response.status_code < 300:
            status_code = response.status_code
            response.close()
            return self._index_problem(
                request,
                "acquisition_failed",
                f"PyPI returned HTTP {status_code} for the release-index request.",
                status_code,
            )

        try:
            data = self._read_json_object(response, resource="release-index")
        except PyPIRequestError as exc:
            return self._index_problem(
                request,
                "acquisition_failed",
                str(exc),
                exc.status_code,
            )
        except PyPIResponseError as exc:
            return self._index_problem(
                request,
                "malformed_response",
                str(exc),
                response.status_code,
            )

        try:
            info = _required_mapping(data, "info")
            published_name = _required_string(info, "name")
            last_serial = _required_nonnegative_int(data, "last_serial")
            release_versions = _release_version_keys(_required_mapping(data, "releases"))
        except _MalformedResponse as exc:
            return self._index_problem(
                request,
                "malformed_response",
                str(exc),
                200,
            )

        if normalize_package_name(published_name) != request.normalized_package:
            return self._index_problem(
                request,
                "identity_mismatch",
                f"PyPI returned conflicting package name {published_name!r}.",
                200,
            )

        return PackageReleaseIndexEvidence(
            requested_package=request.package,
            normalized_package=request.normalized_package,
            published_name=published_name,
            source_url=request.source_url,
            retrieved_at=self._now(),
            last_serial=last_serial,
            release_versions=release_versions,
        )

    @staticmethod
    def _index_problem(
        request: _ProjectRequest,
        state: PackageReleaseIndexProblemState,
        detail: str,
        status_code: int | None = None,
    ) -> PackageReleaseIndexProblem:
        return PackageReleaseIndexProblem(
            state=state,
            requested_package=request.package,
            normalized_package=request.normalized_package,
            source_url=request.source_url,
            detail=detail,
            status_code=status_code,
        )


def _pypi_contract(value: Any, validator: Callable[[Any], _T], message: str) -> _T:
    try:
        return validator(value)
    except JsonContractViolation as exc:
        raise _MalformedResponse(message) from exc


def _distribution_files(raw_files: list[Any]) -> tuple[DistributionFile, ...]:
    files: list[DistributionFile] = []
    seen_names: set[str] = set()
    for index, raw in enumerate(raw_files, start=1):
        item = _pypi_contract(
            raw,
            expect_mapping,
            f"PyPI distribution-file item {index} must be an object.",
        )
        filename = _required_string(item, "filename")
        if filename in seen_names:
            raise _MalformedResponse(
                f"PyPI returned duplicate distribution filename {filename!r}."
            )
        seen_names.add(filename)
        url = _required_string(item, "url")
        package_type = _required_string(item, "packagetype")
        sha256 = _required_string(_required_mapping(item, "digests"), "sha256")
        if _SHA256.fullmatch(sha256) is None:
            raise _MalformedResponse(
                f"PyPI distribution file {filename!r} has an invalid SHA-256 digest."
            )
        files.append(
            DistributionFile(
                filename=filename,
                url=url,
                sha256=sha256.lower(),
                package_type=package_type,
            )
        )
    return tuple(sorted(files, key=lambda item: item.filename))


def _file_python_declarations(raw_files, files) -> tuple[PublishedFileRequiresPython, ...]:
    # The release parser already admitted unique filenames and content identities.
    # A refused or empty set supplies no whole-set exclusion claim.
    if len(files) > MAX_FILE_PYTHON_DECLARATIONS:
        return ()
    by_name = {item["filename"]: item for item in raw_files}
    rows = []
    for file in files:
        raw = by_name[file.filename]
        specifier, yanked = raw.get("requires_python"), raw.get("yanked")
        rows.append(PublishedFileRequiresPython(
            file.filename, file.sha256,
            specifier if type(specifier) is str and 0 < len(specifier) <= MAX_REQUIRES_PYTHON_TEXT else None,
            yanked if type(yanked) is bool else None,
        ))
    return tuple(rows)


def _project_urls(info: Mapping[str, Any]) -> tuple[ProjectUrlCandidate, ...]:
    raw = info.get("project_urls")
    if raw is None:
        return ()
    values = _pypi_contract(
        raw,
        expect_mapping,
        "PyPI field 'project_urls' must be an object or null.",
    )
    candidates: list[ProjectUrlCandidate] = []
    for label, url in values.items():
        label = _pypi_contract(
            label,
            expect_nonempty_text,
            "Project URL labels must be non-empty strings.",
        )
        url = _pypi_contract(
            url,
            expect_nonempty_text,
            f"Project URL {label!r} must be non-empty text.",
        )
        candidates.append(ProjectUrlCandidate(label=label, url=url))
    return tuple(sorted(candidates, key=lambda item: item.label.casefold()))


def _release_version_keys(releases: Mapping[str, Any]) -> tuple[str, ...]:
    versions: list[str] = []
    for raw_version, raw_files in releases.items():
        version = _pypi_contract(
            raw_version,
            expect_nonempty_text,
            "PyPI release-index keys must be non-empty version text.",
        )
        _pypi_contract(
            raw_files,
            expect_list,
            f"PyPI release-index entry {version!r} must be an array.",
        )
        versions.append(version)
    return tuple(sorted(versions))


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
    return _pypi_contract(
        _required_field(data, key),
        expect_mapping,
        f"PyPI field {key!r} must be an object.",
    )


def _required_list(data: Mapping[str, Any], key: str) -> list[Any]:
    return _pypi_contract(
        _required_field(data, key),
        expect_list,
        f"PyPI field {key!r} must be an array.",
    )


def _required_string(data: Mapping[str, Any], key: str) -> str:
    return _pypi_contract(
        _required_field(data, key),
        expect_nonempty_text,
        f"PyPI field {key!r} must be non-empty text.",
    )


def _required_nonnegative_int(data: Mapping[str, Any], key: str) -> int:
    return _pypi_contract(
        _required_field(data, key),
        expect_nonnegative_integer,
        f"PyPI field {key!r} must be a non-negative integer.",
    )


def _release_url(package: str, version: str) -> str:
    return f"{PYPI_JSON_ROOT}/{quote(package, safe='')}/{quote(version, safe='')}/json"


def _project_url(package: str) -> str:
    return f"{PYPI_JSON_ROOT}/{quote(package, safe='')}/json"


__all__ = (
    "DistributionFile",
    "PackageReleaseEvidence",
    "PackageReleaseEvidenceWithAdvisories",
    "PackageReleaseIndexEvidence",
    "PackageReleaseIndexProblem",
    "PackageReleaseIndexProblemState",
    "PackageReleaseIndexResult",
    "PackageReleaseProblem",
    "PackageReleaseProblemState",
    "PackageReleaseResult",
    "ProjectUrlCandidate",
    "PyPIReleaseClient",
    "PyPIReleaseIndexClient",
)
