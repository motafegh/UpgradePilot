"""Establish one trusted upstream GitHub repository from PyPI evidence.

The boundary answers only whether PyPI project metadata and PyPI-reported publisher
provenance agree on one GitHub repository identity. It does not require a GitHub
Release object and it carries no semantic claim state.
"""

from __future__ import annotations

import string
from dataclasses import dataclass, field
from typing import Literal
from urllib.parse import urlsplit

from ..github.identity import validate_repository
from ..pypi.release import PackageReleaseEvidence, ProjectUrlCandidate
from ..pypi.provenance import (
    FileProvenanceEvidence,
    FileProvenanceProblem,
    PyPIProvenanceClient,
)

_SOURCE_LABELS = {"source", "repository", "sourcecode", "github"}
_LABEL_REMOVAL_MAP = str.maketrans("", "", string.punctuation + string.whitespace)

type UpstreamRepositoryProblemState = Literal[
    "source_unavailable",
    "unsupported_source",
    "identity_mismatch",
    "ambiguous_source",
    "malformed_response",
    "acquisition_failed",
]


@dataclass(frozen=True, slots=True)
class UpstreamRepositoryEvidence:
    """PyPI-backed trusted GitHub repository identity for one package release."""

    state: Literal["available"] = field(init=False, default="available")
    package_release: PackageReleaseEvidence
    repository: str
    source_candidates: tuple[ProjectUrlCandidate, ...]
    provenance: tuple[FileProvenanceEvidence, ...]
    provenance_unavailable_files: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class UpstreamRepositoryProblem:
    """Why PyPI evidence could not establish one trusted GitHub repository."""

    state: UpstreamRepositoryProblemState
    package: str
    version: str
    detail: str


type UpstreamRepositoryResult = UpstreamRepositoryEvidence | UpstreamRepositoryProblem


class UpstreamRepositoryResolver:
    """Reconcile PyPI source metadata with PyPI publisher provenance."""

    def __init__(self, *, provenance_client: PyPIProvenanceClient | None = None) -> None:
        self._provenance = provenance_client or PyPIProvenanceClient()

    def resolve(self, release: PackageReleaseEvidence) -> UpstreamRepositoryResult:
        source_result = _resolve_source_repository(release.project_urls)
        if isinstance(source_result, _SourceProblem):
            return self._problem(release, source_result.state, source_result.detail)
        repository, source_candidates = source_result

        provenance_records: list[FileProvenanceEvidence] = []
        unavailable_files: list[str] = []
        publisher_repositories: set[str] = set()
        publisher_kinds: set[str] = set()
        saw_supported_provenance = False

        for distribution in release.distribution_files:
            result = self._provenance.get_file_provenance(release, distribution)
            if isinstance(result, FileProvenanceProblem):
                if result.state == "provenance_unavailable":
                    unavailable_files.append(distribution.filename)
                    continue
                if result.state == "unsupported_provenance":
                    return self._problem(release, "unsupported_source", result.detail)
                if result.state == "malformed_response":
                    return self._problem(release, "malformed_response", result.detail)
                return self._problem(release, "acquisition_failed", result.detail)

            provenance_records.append(result)
            publisher_kinds.update(
                publisher.kind.casefold() for publisher in result.publishers
            )
            github_publishers = [
                publisher
                for publisher in result.publishers
                if publisher.kind.casefold() == "github"
            ]
            if github_publishers:
                saw_supported_provenance = True
            for publisher in github_publishers:
                if publisher.repository is None:
                    return self._problem(
                        release,
                        "malformed_response",
                        "PyPI reported a GitHub publisher without a repository identity.",
                    )
                try:
                    normalized = validate_repository(publisher.repository)
                except ValueError:
                    return self._problem(
                        release,
                        "malformed_response",
                        "PyPI reported a malformed GitHub publisher repository identity.",
                    )
                publisher_repositories.add(normalized.casefold())

        if not provenance_records:
            return self._problem(
                release,
                "source_unavailable",
                "No exact distribution file exposed usable PyPI provenance.",
            )
        if "github" in publisher_kinds and len(publisher_kinds) > 1:
            return self._problem(
                release,
                "ambiguous_source",
                "PyPI provenance reported mixed publisher kinds for the release files.",
            )
        if not saw_supported_provenance or not publisher_repositories:
            return self._problem(
                release,
                "unsupported_source",
                "Available PyPI provenance did not report a supported GitHub publisher.",
            )
        if len(publisher_repositories) != 1:
            return self._problem(
                release,
                "ambiguous_source",
                "PyPI provenance reported more than one GitHub publisher repository.",
            )

        publisher_repository = next(iter(publisher_repositories))
        if publisher_repository != repository.casefold():
            return self._problem(
                release,
                "identity_mismatch",
                (
                    f"PyPI Source candidate {repository!r} conflicts with provenance "
                    f"publisher {publisher_repository!r}."
                ),
            )

        return UpstreamRepositoryEvidence(
            package_release=release,
            repository=repository,
            source_candidates=source_candidates,
            provenance=tuple(provenance_records),
            provenance_unavailable_files=tuple(sorted(unavailable_files)),
        )

    @staticmethod
    def _problem(
        release: PackageReleaseEvidence,
        state: UpstreamRepositoryProblemState,
        detail: str,
    ) -> UpstreamRepositoryProblem:
        return UpstreamRepositoryProblem(
            state=state,
            package=release.normalized_package,
            version=release.requested_version,
            detail=detail,
        )


@dataclass(frozen=True, slots=True)
class _SourceProblem:
    state: Literal["unsupported_source", "ambiguous_source"]
    detail: str


def normalize_project_url_label(label: str) -> str:
    """Apply the PEP 753 consumer-side label normalization procedure."""

    return label.translate(_LABEL_REMOVAL_MAP).lower()


def _resolve_source_repository(
    candidates: tuple[ProjectUrlCandidate, ...],
) -> tuple[str, tuple[ProjectUrlCandidate, ...]] | _SourceProblem:
    source_candidates = tuple(
        candidate
        for candidate in candidates
        if normalize_project_url_label(candidate.label) in _SOURCE_LABELS
    )
    if not source_candidates:
        return _SourceProblem(
            "unsupported_source",
            "PyPI metadata contains no well-known Source candidate.",
        )

    parsed: list[tuple[ProjectUrlCandidate, str]] = []
    unsupported: list[ProjectUrlCandidate] = []
    for candidate in source_candidates:
        repository = _github_repository_from_url(candidate.url)
        if repository is None:
            unsupported.append(candidate)
        else:
            parsed.append((candidate, repository))

    if unsupported:
        if parsed or len(unsupported) > 1:
            return _SourceProblem(
                "ambiguous_source",
                "PyPI metadata contains conflicting or unsupported Source candidates.",
            )
        return _SourceProblem(
            "unsupported_source",
            "The PyPI Source candidate is outside the supported canonical GitHub format.",
        )

    repositories = {repository.casefold(): repository for _, repository in parsed}
    if len(repositories) != 1:
        return _SourceProblem(
            "ambiguous_source",
            "PyPI metadata identifies more than one GitHub source repository.",
        )
    return next(iter(repositories.values())), tuple(candidate for candidate, _ in parsed)


def _github_repository_from_url(url: str) -> str | None:
    try:
        parsed = urlsplit(url)
        port = parsed.port
    except ValueError:
        return None
    if (
        parsed.scheme.casefold() != "https"
        or parsed.hostname is None
        or parsed.hostname.casefold() != "github.com"
        or port is not None
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
    ):
        return None

    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) != 2:
        return None
    owner, repository = parts
    if repository.endswith(".git"):
        repository = repository[:-4]
    try:
        return validate_repository(f"{owner}/{repository}")
    except ValueError:
        return None


__all__ = (
    "UpstreamRepositoryEvidence",
    "UpstreamRepositoryProblem",
    "UpstreamRepositoryProblemState",
    "UpstreamRepositoryResolver",
    "UpstreamRepositoryResult",
    "normalize_project_url_label",
)
