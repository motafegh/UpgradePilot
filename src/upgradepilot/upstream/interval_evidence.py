"""Select and compose already acquired records into upstream interval evidence.

This module is pure: it does not make network requests, resolve Git tags, discover a
changelog path, extract semantic claims, or decide target relevance.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from packaging.version import InvalidVersion, Version

from ..dependency.versioning import (
    PackagingVersionProblem,
    order_crossed_release_versions,
    parse_dependency_release_interval,
)
from ..github.identity import validate_repository
from ..github.repository import ExactRepositoryTextFile, UnavailableRepositoryFile
from ..github.tag import GitHubTagCommitEvidence
from ..pypi.release import PackageReleaseIndexEvidence
from .interval import (
    CrossedReleaseIndexEvidence,
    DependencyReleaseInterval,
    TaggedChangelogEvidence,
    UpstreamAuthoritySourceProblem,
)

type CrossedReleaseIndexSelectionProblemState = Literal[
    "identity_mismatch",
    "dependency_interval_unresolved",
    "release_index_unusable",
]


@dataclass(frozen=True, slots=True)
class SelectedCrossedReleaseIndex:
    source_index: PackageReleaseIndexEvidence
    evidence: CrossedReleaseIndexEvidence
    ignored_non_pep440_versions: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class CrossedReleaseIndexSelectionProblem:
    state: CrossedReleaseIndexSelectionProblemState
    interval: DependencyReleaseInterval
    repository: str
    detail: str
    method_problem: PackagingVersionProblem | None = None


type CrossedReleaseIndexSelectionResult = (
    SelectedCrossedReleaseIndex | CrossedReleaseIndexSelectionProblem
)
type TaggedChangelogCompositionResult = (
    TaggedChangelogEvidence | UpstreamAuthoritySourceProblem
)


def select_crossed_release_index(
    interval: DependencyReleaseInterval,
    repository: str,
    release_index: PackageReleaseIndexEvidence,
) -> CrossedReleaseIndexSelectionResult:
    if not isinstance(interval, DependencyReleaseInterval):
        raise TypeError("interval must be DependencyReleaseInterval.")
    if not isinstance(release_index, PackageReleaseIndexEvidence):
        raise TypeError("release_index must be PackageReleaseIndexEvidence.")

    repository = validate_repository(repository)
    if release_index.normalized_package != interval.normalized_package:
        return CrossedReleaseIndexSelectionProblem(
            state="identity_mismatch",
            interval=interval,
            repository=repository,
            detail=(
                "The PyPI release index does not describe the dependency package in "
                "the selected release interval."
            ),
        )

    parsed_interval = parse_dependency_release_interval(interval)
    if isinstance(parsed_interval, PackagingVersionProblem):
        return CrossedReleaseIndexSelectionProblem(
            state="dependency_interval_unresolved",
            interval=interval,
            repository=repository,
            detail=(
                "The dependency interval could not be interpreted under the accepted "
                f"PEP 440 method: {parsed_interval.detail}"
            ),
            method_problem=parsed_interval,
        )

    selected_raw_versions: list[str] = []
    ignored_non_pep440_versions: list[str] = []
    for raw_version in release_index.release_versions:
        try:
            parsed_release = Version(raw_version)
        except InvalidVersion:
            ignored_non_pep440_versions.append(raw_version)
            continue
        if parsed_interval.old_version < parsed_release <= parsed_interval.proposed_version:
            selected_raw_versions.append(raw_version)

    ordered = order_crossed_release_versions(parsed_interval, selected_raw_versions)
    if isinstance(ordered, PackagingVersionProblem):
        return CrossedReleaseIndexSelectionProblem(
            state="release_index_unusable",
            interval=interval,
            repository=repository,
            detail=(
                "The acquired PyPI release keys could not establish one complete, "
                f"unambiguous crossed-release sequence: {ordered.detail}"
            ),
            method_problem=ordered,
        )

    evidence = CrossedReleaseIndexEvidence(
        repository=repository,
        interval=interval,
        ordered_versions=ordered.ordered_raw_versions,
        source_url=release_index.source_url,
        retrieved_at=release_index.retrieved_at,
    )
    return SelectedCrossedReleaseIndex(
        source_index=release_index,
        evidence=evidence,
        ignored_non_pep440_versions=tuple(sorted(ignored_non_pep440_versions)),
    )


def build_tagged_changelog_evidence(
    interval: DependencyReleaseInterval,
    tag_commit: GitHubTagCommitEvidence,
    file_evidence: ExactRepositoryTextFile | UnavailableRepositoryFile,
) -> TaggedChangelogCompositionResult:
    if not isinstance(interval, DependencyReleaseInterval):
        raise TypeError("interval must be DependencyReleaseInterval.")
    if not isinstance(tag_commit, GitHubTagCommitEvidence):
        raise TypeError("tag_commit must be GitHubTagCommitEvidence.")
    if not isinstance(file_evidence, (ExactRepositoryTextFile, UnavailableRepositoryFile)):
        raise TypeError("file_evidence must be exact repository-file evidence.")

    repository = validate_repository(tag_commit.repository)
    accepted_tags = {interval.proposed_version, f"v{interval.proposed_version}"}
    if tag_commit.requested_tag not in accepted_tags:
        return _changelog_problem(
            "identity_mismatch",
            (
                f"Resolved tag {tag_commit.requested_tag!r} does not identify the "
                f"proposed dependency version {interval.proposed_version!r}."
            ),
        )

    lightweight_mismatch = (
        tag_commit.tag_object_type == "commit"
        and tag_commit.tag_object_sha != tag_commit.resolved_commit_sha
    )
    if (
        tag_commit.tag_ref != f"refs/tags/{tag_commit.requested_tag}"
        or tag_commit.tag_object_type not in {"commit", "tag"}
        or not _trimmed(tag_commit.tag_object_sha)
        or not _trimmed(tag_commit.resolved_commit_sha)
        or lightweight_mismatch
    ):
        return _changelog_problem(
            "malformed_source",
            "The resolved Git tag contained inconsistent reference or object identity.",
        )

    if not _same_repository(file_evidence.repository, repository):
        return _changelog_problem(
            "identity_mismatch",
            "The acquired changelog file belonged to a different repository.",
            path=file_evidence.path,
        )
    if file_evidence.revision != tag_commit.resolved_commit_sha:
        return _changelog_problem(
            "identity_mismatch",
            "The acquired changelog file did not come from the resolved tag commit.",
            path=file_evidence.path,
        )

    if isinstance(file_evidence, UnavailableRepositoryFile):
        return _changelog_problem(
            "source_unavailable",
            file_evidence.detail,
            path=file_evidence.path,
        )

    if (
        file_evidence.returned_path != file_evidence.path
        or not _trimmed(file_evidence.blob_sha)
        or type(file_evidence.reported_byte_count) is not int
        or type(file_evidence.decoded_byte_count) is not int
        or file_evidence.reported_byte_count < 0
        or file_evidence.decoded_byte_count < 0
        or file_evidence.reported_byte_count != file_evidence.decoded_byte_count
        or not isinstance(file_evidence.content, str)
        or file_evidence.retrieved_at is None
    ):
        return _changelog_problem(
            "malformed_source",
            "The acquired changelog file contained inconsistent path, blob, byte, or time evidence.",
            path=file_evidence.path,
        )

    if not file_evidence.content.strip():
        return _changelog_problem(
            "source_unavailable",
            "The exact changelog file contained no usable text.",
            path=file_evidence.path,
        )

    return TaggedChangelogEvidence(
        repository=repository,
        interval=interval,
        requested_tag=tag_commit.requested_tag,
        tag_ref=tag_commit.tag_ref,
        tag_object_type=tag_commit.tag_object_type,
        tag_object_sha=tag_commit.tag_object_sha,
        resolved_commit_sha=tag_commit.resolved_commit_sha,
        path=file_evidence.path,
        returned_path=file_evidence.returned_path,
        blob_sha=file_evidence.blob_sha,
        reported_byte_count=file_evidence.reported_byte_count,
        decoded_byte_count=file_evidence.decoded_byte_count,
        content=file_evidence.content,
        retrieved_at=file_evidence.retrieved_at,
    )


def _same_repository(left: str | None, right: str) -> bool:
    if left is None:
        return False
    try:
        return validate_repository(left).casefold() == validate_repository(right).casefold()
    except (TypeError, ValueError):
        return False


def _trimmed(value: object) -> bool:
    return isinstance(value, str) and bool(value) and value == value.strip()


def _changelog_problem(
    state: Literal[
        "source_unavailable",
        "malformed_source",
        "identity_mismatch",
        "acquisition_failed",
    ],
    detail: str,
    *,
    path: str | None = None,
) -> UpstreamAuthoritySourceProblem:
    return UpstreamAuthoritySourceProblem(
        source_kind="tagged_changelog",
        state=state,
        detail=detail,
        path=path,
    )


__all__ = (
    "CrossedReleaseIndexSelectionProblem",
    "CrossedReleaseIndexSelectionProblemState",
    "CrossedReleaseIndexSelectionResult",
    "SelectedCrossedReleaseIndex",
    "TaggedChangelogCompositionResult",
    "build_tagged_changelog_evidence",
    "select_crossed_release_index",
)
