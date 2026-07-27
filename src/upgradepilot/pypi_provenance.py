"""Acquire PyPI-reported publisher identities for exact distribution files."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Literal, TypeVar
from urllib.parse import quote

from requests import Session

from .json_contract import (
    JsonContractViolation,
    expect_list,
    expect_mapping,
    expect_nonempty_text,
    expect_positive_integer,
)
from .pypi_api import (
    DEFAULT_MAX_RESPONSE_BYTES,
    DEFAULT_TIMEOUT,
    PyPIJsonApiClient,
    PyPIRequestError,
    PyPIResponseError,
)
from .pypi_client import DistributionFile, PackageReleaseEvidence

PYPI_INTEGRITY_ROOT = "https://pypi.org/integrity"
_T = TypeVar("_T")

type FileProvenanceProblemState = Literal[
    "provenance_unavailable",
    "unsupported_provenance",
    "malformed_response",
    "acquisition_failed",
]


@dataclass(frozen=True, slots=True)
class PublisherIdentity:
    """One publisher identity reported by PyPI for an exact distribution file.

    GitHub publisher records require ``repository`` and ``workflow``. Other valid
    publisher kinds are retained without pretending they fit GitHub's identity shape.
    """

    kind: str
    repository: str | None
    workflow: str | None


@dataclass(frozen=True, slots=True)
class FileProvenanceEvidence:
    """PyPI-reported provenance for one exact distribution file.

    This record does not claim that UpgradePilot independently verified the included
    attestations. It records the publisher identity exposed by PyPI's Integrity API.
    """

    state: Literal["available"] = field(init=False, default="available")
    package: str
    version: str
    filename: str
    sha256: str
    source_url: str
    retrieved_at: datetime
    api_version: int
    attestation_count: int
    publishers: tuple[PublisherIdentity, ...]


@dataclass(frozen=True, slots=True)
class FileProvenanceProblem:
    """A bounded reason why usable file provenance was not established."""

    state: FileProvenanceProblemState
    package: str
    version: str
    filename: str
    source_url: str
    detail: str
    status_code: int | None = None


type FileProvenanceResult = FileProvenanceEvidence | FileProvenanceProblem


class _MalformedProvenance(ValueError):
    pass


class PyPIProvenanceClient(PyPIJsonApiClient):
    """Read exact-file provenance through PyPI's Integrity API."""

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
            accept="application/vnd.pypi.integrity.v1+json",
        )
        self._now = now or (lambda: datetime.now(timezone.utc))

    def get_file_provenance(
        self,
        release: PackageReleaseEvidence,
        distribution: DistributionFile,
    ) -> FileProvenanceResult:
        """Return PyPI-reported publishers for one file belonging to the release."""

        if distribution not in release.distribution_files:
            raise ValueError(
                "distribution file does not belong to the supplied release evidence."
            )

        source_url = _provenance_url(
            release.normalized_package,
            release.requested_version,
            distribution.filename,
        )
        try:
            response = self._get_response(source_url, resource="provenance")
        except PyPIRequestError as exc:
            return self._problem(
                release,
                distribution,
                source_url,
                "acquisition_failed",
                str(exc),
                exc.status_code,
            )

        if response.status_code == 404:
            response.close()
            return self._problem(
                release,
                distribution,
                source_url,
                "provenance_unavailable",
                "PyPI reports no provenance for this exact distribution file.",
                404,
            )
        if response.status_code == 406:
            response.close()
            return self._problem(
                release,
                distribution,
                source_url,
                "unsupported_provenance",
                "PyPI did not accept the supported Integrity API media type.",
                406,
            )
        if not 200 <= response.status_code < 300:
            status = response.status_code
            response.close()
            return self._problem(
                release,
                distribution,
                source_url,
                "acquisition_failed",
                f"PyPI returned HTTP {status} for the provenance request.",
                status,
            )

        try:
            data = self._read_json_object(response, resource="provenance")
            api_version, attestation_count, publishers = _parse_provenance(data)
        except PyPIRequestError as exc:
            return self._problem(
                release,
                distribution,
                source_url,
                "acquisition_failed",
                str(exc),
                exc.status_code,
            )
        except (PyPIResponseError, _MalformedProvenance) as exc:
            return self._problem(
                release,
                distribution,
                source_url,
                "malformed_response",
                str(exc),
                response.status_code,
            )

        if api_version != 1:
            return self._problem(
                release,
                distribution,
                source_url,
                "unsupported_provenance",
                f"PyPI provenance version {api_version} is outside the supported version 1 contract.",
                200,
            )
        if not publishers or attestation_count < 1:
            return self._problem(
                release,
                distribution,
                source_url,
                "provenance_unavailable",
                "PyPI returned no usable attestation bundle for this file.",
                200,
            )

        return FileProvenanceEvidence(
            package=release.normalized_package,
            version=release.requested_version,
            filename=distribution.filename,
            sha256=distribution.sha256,
            source_url=source_url,
            retrieved_at=self._now(),
            api_version=api_version,
            attestation_count=attestation_count,
            publishers=publishers,
        )

    @staticmethod
    def _problem(
        release: PackageReleaseEvidence,
        distribution: DistributionFile,
        source_url: str,
        state: FileProvenanceProblemState,
        detail: str,
        status_code: int | None = None,
    ) -> FileProvenanceProblem:
        return FileProvenanceProblem(
            state=state,
            package=release.normalized_package,
            version=release.requested_version,
            filename=distribution.filename,
            source_url=source_url,
            detail=detail,
            status_code=status_code,
        )


def _parse_provenance(
    data: Mapping[str, Any],
) -> tuple[int, int, tuple[PublisherIdentity, ...]]:
    api_version = _required_positive_int(data, "version")
    bundles = _required_list(data, "attestation_bundles")
    publishers: set[PublisherIdentity] = set()
    attestation_count = 0

    for index, raw_bundle in enumerate(bundles, start=1):
        bundle = _contract(
            raw_bundle,
            expect_mapping,
            f"PyPI provenance bundle {index} must be an object.",
        )
        attestations = _required_list(bundle, "attestations")
        if not attestations:
            raise _MalformedProvenance(
                f"PyPI provenance bundle {index} contains no attestations."
            )
        attestation_count += len(attestations)
        publisher = _required_mapping(bundle, "publisher")
        kind = _required_string(publisher, "kind")
        if kind.casefold() == "github":
            repository = _required_string(publisher, "repository")
            workflow = _required_string(publisher, "workflow")
        else:
            repository = _optional_string(publisher, "repository")
            workflow = _optional_string(publisher, "workflow")
        publishers.add(
            PublisherIdentity(
                kind=kind,
                repository=repository,
                workflow=workflow,
            )
        )

    return (
        api_version,
        attestation_count,
        tuple(
            sorted(
                publishers,
                key=lambda item: (
                    item.kind.casefold(),
                    (item.repository or "").casefold(),
                    (item.workflow or "").casefold(),
                ),
            )
        ),
    )


def _contract(value: Any, validator: Callable[[Any], _T], message: str) -> _T:
    try:
        return validator(value)
    except JsonContractViolation as exc:
        raise _MalformedProvenance(message) from exc


def _required_field(data: Mapping[str, Any], key: str) -> Any:
    try:
        return data[key]
    except KeyError as exc:
        raise _MalformedProvenance(
            f"PyPI provenance response is missing field {key!r}."
        ) from exc


def _required_mapping(data: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    return _contract(
        _required_field(data, key),
        expect_mapping,
        f"PyPI provenance field {key!r} must be an object.",
    )


def _required_list(data: Mapping[str, Any], key: str) -> list[Any]:
    return _contract(
        _required_field(data, key),
        expect_list,
        f"PyPI provenance field {key!r} must be an array.",
    )


def _required_string(data: Mapping[str, Any], key: str) -> str:
    return _contract(
        _required_field(data, key),
        expect_nonempty_text,
        f"PyPI provenance field {key!r} must be non-empty text.",
    )


def _optional_string(data: Mapping[str, Any], key: str) -> str | None:
    value = data.get(key)
    if value is None:
        return None
    return _contract(
        value,
        expect_nonempty_text,
        f"PyPI provenance field {key!r} must be non-empty text or absent.",
    )


def _required_positive_int(data: Mapping[str, Any], key: str) -> int:
    return _contract(
        _required_field(data, key),
        expect_positive_integer,
        f"PyPI provenance field {key!r} must be a positive integer.",
    )


def _provenance_url(package: str, version: str, filename: str) -> str:
    return (
        f"{PYPI_INTEGRITY_ROOT}/{quote(package, safe='')}/"
        f"{quote(version, safe='')}/{quote(filename, safe='')}/provenance"
    )
