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
from ..github.repository import RepositoryFileEvidence, RepositoryTextFile, UnavailableRepositoryFile
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
    file_evidence: RepositoryFileEvidence,
) -> TaggedChangelogCompositionResult:
    """Package one already-bound proposed-tag changelog as interval-authority evidence.

    Normal investigation orchestration resolves the proposed-version tag, discovers the
    changelog at that exact commit, and acquires the file with the same repository and
    resolved commit before this function runs. This boundary therefore does not re-prove
    provider tag internals or exact-file transport metadata. It preserves only the
    durable immutable source identity/text needed downstream.
    """

    if not isinstance(interval, DependencyReleaseInterval):
        raise TypeError("interval must be DependencyReleaseInterval.")
    if not isinstance(tag_commit, GitHubTagCommitEvidence):
        raise TypeError("tag_commit must be GitHubTagCommitEvidence.")
    if not isinstance(file_evidence, (RepositoryTextFile, UnavailableRepositoryFile)):
        raise TypeError("file_evidence must be repository-file evidence.")

    if isinstance(file_evidence, UnavailableRepositoryFile):
        return _changelog_problem(
            "source_unavailable",
            file_evidence.detail,
            path=file_evidence.path,
        )

    if not file_evidence.content.strip():
        return _changelog_problem(
            "source_unavailable",
            "The exact changelog file contained no usable text.",
            path=file_evidence.path,
        )

    return TaggedChangelogEvidence(
        repository=tag_commit.repository,
        interval=interval,
        resolved_commit_sha=tag_commit.resolved_commit_sha,
        path=file_evidence.path,
        content=file_evidence.content,
    )


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
