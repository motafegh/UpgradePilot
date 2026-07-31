"""Define trusted upstream release-interval identity and source authority.

This module is intentionally pure. It does not acquire GitHub or PyPI data, parse
PEP 440 versions, extract semantic claims, compare target Python declarations, or
make compatibility and maintainer-action decisions.

Step 1 receives already trusted dependency identity plus exact source records. It
then proves whether the available sources establish bounded authority for the whole
old-exclusive/proposed-inclusive release interval.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal

from .dependency_change import DependencyVersionChange, normalize_package_name
from .github_client import validate_repository
from .github_release import GitHubReleaseEvidence


type UpstreamSourceKind = Literal[
    "github_release_body",
    "tagged_changelog",
    "package_metadata",
    "dependabot_release_note_copy",
    "arbitrary_documentation",
    "model_selected_text",
]
type UpstreamSourceRole = Literal[
    "release_authority",
    "interval_authority",
    "corroboration",
    "unsupported",
]
type UpstreamAuthoritySourceKind = Literal[
    "github_release_body",
    "tagged_changelog",
    "package_metadata",
]
type UpstreamAuthoritySourceProblemState = Literal[
    "source_unavailable",
    "malformed_source",
    "identity_mismatch",
    "acquisition_failed",
]
type UpstreamIntervalAuthorityBasis = Literal[
    "complete_release_series",
    "tagged_changelog",
    "complete_release_series_and_tagged_changelog",
]
type UpstreamIntervalAuthorityProblemState = Literal[
    "no_interval_authority",
    "interval_incomplete",
    "identity_mismatch",
    "ambiguous_source",
    "conflicting_source_identity",
    "malformed_source",
    "unsupported_source_authority",
]

UPSTREAM_SOURCE_AUTHORITY_ORDER: tuple[UpstreamAuthoritySourceKind, ...] = (
    "github_release_body",
    "tagged_changelog",
    "package_metadata",
)

_SOURCE_ROLES: dict[UpstreamSourceKind, UpstreamSourceRole] = {
    "github_release_body": "release_authority",
    "tagged_changelog": "interval_authority",
    "package_metadata": "corroboration",
    "dependabot_release_note_copy": "unsupported",
    "arbitrary_documentation": "unsupported",
    "model_selected_text": "unsupported",
}


@dataclass(frozen=True, slots=True)
class DependencyReleaseInterval:
    """Exact raw dependency bounds with fixed old-exclusive/new-inclusive meaning.

    The record does not establish PEP 440 validity or forward ordering. Those
    responsibilities remain explicitly deferred to the parent plan's packaging step.
    """

    package: str
    normalized_package: str
    old_version: str
    proposed_version: str
    lower_bound_inclusive: Literal[False] = field(init=False, default=False)
    upper_bound_inclusive: Literal[True] = field(init=False, default=True)


@dataclass(frozen=True, slots=True)
class CrossedReleaseIndexEvidence:
    """Trusted complete ordered releases inside one dependency interval.

    A later acquisition/version-ordering stage must earn this record. Step 1 only
    validates structural invariants that do not require a version parser.
    """

    repository: str
    interval: DependencyReleaseInterval
    ordered_versions: tuple[str, ...]
    source_url: str
    retrieved_at: datetime


@dataclass(frozen=True, slots=True)
class IntervalGitHubReleaseSource:
    """One exact GitHub Release body associated with one raw release version."""

    release_version: str
    release: GitHubReleaseEvidence


@dataclass(frozen=True, slots=True)
class TaggedChangelogEvidence:
    """One exact proposed-tag changelog file with immutable provenance."""

    repository: str
    interval: DependencyReleaseInterval
    requested_tag: str
    tag_ref: str
    tag_object_type: str
    tag_object_sha: str
    resolved_commit_sha: str
    path: str
    returned_path: str
    blob_sha: str
    reported_byte_count: int
    decoded_byte_count: int
    content: str
    retrieved_at: datetime


@dataclass(frozen=True, slots=True)
class PackageMetadataCorroboration:
    """Exact package metadata that may corroborate, but never create, authority."""

    package: str
    normalized_package: str
    release_version: str
    source_url: str
    requires_python: str | None
    retrieved_at: datetime


@dataclass(frozen=True, slots=True)
class UpstreamAuthoritySourceProblem:
    """A recognized source-level failure preserved beside any alternative authority."""

    source_kind: UpstreamAuthoritySourceKind
    state: UpstreamAuthoritySourceProblemState
    detail: str
    release_version: str | None = None
    path: str | None = None


@dataclass(frozen=True, slots=True)
class AuthoritativeUpstreamIntervalEvidence:
    """Exact upstream sources that establish bounded interval authority."""

    interval: DependencyReleaseInterval
    repository: str
    crossed_releases: CrossedReleaseIndexEvidence | None
    release_bodies: tuple[IntervalGitHubReleaseSource, ...]
    tagged_changelog: TaggedChangelogEvidence | None
    package_metadata: tuple[PackageMetadataCorroboration, ...]
    source_problems: tuple[UpstreamAuthoritySourceProblem, ...]
    authority_basis: UpstreamIntervalAuthorityBasis


@dataclass(frozen=True, slots=True)
class UpstreamIntervalAuthorityProblem:
    """Normal stopping result when the interval authority is not trustworthy."""

    state: UpstreamIntervalAuthorityProblemState
    interval: DependencyReleaseInterval
    repository: str
    detail: str
    source_problems: tuple[UpstreamAuthoritySourceProblem, ...] = ()


type UpstreamIntervalAuthorityResult = (
    AuthoritativeUpstreamIntervalEvidence | UpstreamIntervalAuthorityProblem
)


def release_interval_from_dependency_change(
    dependency: DependencyVersionChange,
) -> DependencyReleaseInterval:
    """Copy canonical identity into the fixed old-exclusive/proposed-inclusive form."""

    return DependencyReleaseInterval(
        package=dependency.package,
        normalized_package=dependency.normalized_package,
        old_version=dependency.old_version,
        proposed_version=dependency.proposed_version,
    )


def upstream_source_role(source_kind: UpstreamSourceKind) -> UpstreamSourceRole:
    """Return the fixed authority role for one named upstream source kind."""

    return _SOURCE_ROLES[source_kind]


def assemble_upstream_interval_authority(
    interval: DependencyReleaseInterval,
    repository: str,
    *,
    crossed_releases: CrossedReleaseIndexEvidence | None = None,
    release_bodies: Sequence[IntervalGitHubReleaseSource] = (),
    tagged_changelogs: Sequence[TaggedChangelogEvidence] = (),
    package_metadata: Sequence[PackageMetadataCorroboration] = (),
    source_problems: Sequence[UpstreamAuthoritySourceProblem] = (),
) -> UpstreamIntervalAuthorityResult:
    """Assemble exact sources into one interval authority result or explicit problem.

    The function never interprets prose. It proves only source identity, immutable
    provenance, bounded interval coverage, and deterministic source preservation.
    """

    interval_problem = _validate_interval(interval)
    if interval_problem is not None:
        return _problem(
            "malformed_source",
            interval,
            repository,
            interval_problem,
            source_problems,
        )

    try:
        repository = validate_repository(repository)
    except ValueError:
        return _problem(
            "malformed_source",
            interval,
            repository,
            "The upstream repository identity was malformed.",
            source_problems,
        )

    normalized_problems = _validate_source_problems(source_problems)
    if isinstance(normalized_problems, str):
        return _problem(
            "malformed_source",
            interval,
            repository,
            normalized_problems,
            (),
        )
    collected_problems = list(normalized_problems)

    if crossed_releases is not None:
        index_problem = _validate_crossed_release_index(
            crossed_releases,
            interval,
            repository,
        )
        if index_problem is not None:
            state, detail = index_problem
            return _problem(
                state,
                interval,
                repository,
                detail,
                collected_problems,
            )

    release_result = _validate_release_bodies(
        release_bodies,
        interval,
        repository,
        crossed_releases,
    )
    if isinstance(release_result, UpstreamIntervalAuthorityProblem):
        return UpstreamIntervalAuthorityProblem(
            state=release_result.state,
            interval=interval,
            repository=repository,
            detail=release_result.detail,
            source_problems=tuple(collected_problems) + release_result.source_problems,
        )
    usable_releases, generated_release_problems = release_result
    collected_problems.extend(generated_release_problems)

    changelog_result = _validate_tagged_changelogs(
        tagged_changelogs,
        interval,
        repository,
    )
    if isinstance(changelog_result, UpstreamIntervalAuthorityProblem):
        return UpstreamIntervalAuthorityProblem(
            state=changelog_result.state,
            interval=interval,
            repository=repository,
            detail=changelog_result.detail,
            source_problems=tuple(collected_problems) + changelog_result.source_problems,
        )
    tagged_changelog = changelog_result

    metadata_result = _validate_package_metadata(
        package_metadata,
        interval,
        repository,
        crossed_releases,
    )
    if isinstance(metadata_result, UpstreamIntervalAuthorityProblem):
        return UpstreamIntervalAuthorityProblem(
            state=metadata_result.state,
            interval=interval,
            repository=repository,
            detail=metadata_result.detail,
            source_problems=tuple(collected_problems) + metadata_result.source_problems,
        )
    normalized_metadata = metadata_result

    complete_release_series = False
    missing_versions: tuple[str, ...] = ()
    if crossed_releases is not None:
        available_versions = {item.release_version for item in usable_releases}
        missing_versions = tuple(
            version
            for version in crossed_releases.ordered_versions
            if version not in available_versions
        )
        complete_release_series = not missing_versions

    has_changelog = tagged_changelog is not None
    if not complete_release_series and not has_changelog:
        if crossed_releases is not None or usable_releases:
            detail = (
                "The admitted exact GitHub Release bodies did not establish the "
                "complete crossed-release interval."
            )
            if missing_versions:
                detail += " Missing usable release bodies: " + ", ".join(missing_versions) + "."
            elif crossed_releases is None:
                detail += (
                    " No trusted complete crossed-release index or exact tagged "
                    "changelog was available."
                )
            return _problem(
                "interval_incomplete",
                interval,
                repository,
                detail,
                collected_problems,
            )

        return _problem(
            "no_interval_authority",
            interval,
            repository,
            (
                "No complete exact GitHub Release series or exact proposed-tag "
                "changelog was available. Package metadata and copied text cannot "
                "establish interval authority."
            ),
            collected_problems,
        )

    if crossed_releases is not None:
        by_version = {item.release_version: item for item in usable_releases}
        ordered_releases = tuple(
            by_version[version]
            for version in crossed_releases.ordered_versions
            if version in by_version
        )
    else:
        ordered_releases = tuple(usable_releases)

    if complete_release_series and has_changelog:
        basis: UpstreamIntervalAuthorityBasis = (
            "complete_release_series_and_tagged_changelog"
        )
    elif complete_release_series:
        basis = "complete_release_series"
    else:
        basis = "tagged_changelog"

    return AuthoritativeUpstreamIntervalEvidence(
        interval=interval,
        repository=repository,
        crossed_releases=crossed_releases,
        release_bodies=ordered_releases,
        tagged_changelog=tagged_changelog,
        package_metadata=normalized_metadata,
        source_problems=tuple(collected_problems),
        authority_basis=basis,
    )


def _validate_interval(interval: DependencyReleaseInterval) -> str | None:
    if not isinstance(interval, DependencyReleaseInterval):
        return "The dependency release interval had an unsupported type."
    if (
        not _is_trimmed_text(interval.package)
        or not _is_trimmed_text(interval.normalized_package)
        or normalize_package_name(interval.package) != interval.normalized_package
    ):
        return "The dependency release interval package identity was invalid."
    if (
        not _is_trimmed_text(interval.old_version)
        or not _is_trimmed_text(interval.proposed_version)
        or interval.old_version == interval.proposed_version
    ):
        return "The dependency release interval version bounds were invalid."
    return None


def _validate_crossed_release_index(
    index: CrossedReleaseIndexEvidence,
    interval: DependencyReleaseInterval,
    repository: str,
) -> tuple[UpstreamIntervalAuthorityProblemState, str] | None:
    if not isinstance(index, CrossedReleaseIndexEvidence):
        return "malformed_source", "The crossed-release index had an unsupported type."
    if not _same_repository(index.repository, repository) or index.interval != interval:
        return (
            "identity_mismatch",
            "The crossed-release index did not match the selected repository and interval.",
        )
    if not _is_trimmed_text(index.source_url):
        return "malformed_source", "The crossed-release index lacked a source URL."
    versions = index.ordered_versions
    if (
        not versions
        or any(not _is_trimmed_text(version) for version in versions)
        or len(set(versions)) != len(versions)
        or interval.old_version in versions
        or versions[-1] != interval.proposed_version
    ):
        return (
            "malformed_source",
            (
                "The crossed-release index must contain unique non-empty versions, "
                "exclude the old version, and end with the proposed version."
            ),
        )
    return None


def _validate_release_bodies(
    release_bodies: Sequence[IntervalGitHubReleaseSource],
    interval: DependencyReleaseInterval,
    repository: str,
    crossed_releases: CrossedReleaseIndexEvidence | None,
) -> (
    tuple[
        tuple[IntervalGitHubReleaseSource, ...],
        tuple[UpstreamAuthoritySourceProblem, ...],
    ]
    | UpstreamIntervalAuthorityProblem
):
    by_version: dict[str, IntervalGitHubReleaseSource] = {}
    generated_problems: list[UpstreamAuthoritySourceProblem] = []
    allowed_versions = (
        set(crossed_releases.ordered_versions)
        if crossed_releases is not None
        else None
    )

    for candidate in release_bodies:
        if not isinstance(candidate, IntervalGitHubReleaseSource):
            return _local_problem(
                "unsupported_source_authority",
                interval,
                repository,
                "A release-body candidate had an unsupported authority type.",
            )
        if not _is_trimmed_text(candidate.release_version):
            return _local_problem(
                "malformed_source",
                interval,
                repository,
                "A GitHub Release source lacked a valid release version.",
            )
        release = candidate.release
        if not isinstance(release, GitHubReleaseEvidence):
            return _local_problem(
                "malformed_source",
                interval,
                repository,
                "A GitHub Release source lacked exact release evidence.",
            )
        if not _same_repository(release.repository, repository):
            return _local_problem(
                "identity_mismatch",
                interval,
                repository,
                "A GitHub Release source belonged to another repository.",
            )
        if allowed_versions is not None and candidate.release_version not in allowed_versions:
            return _local_problem(
                "identity_mismatch",
                interval,
                repository,
                (
                    f"Release version {candidate.release_version!r} was outside the "
                    "trusted crossed-release index."
                ),
            )
        expected_ref = f"refs/tags/{release.requested_tag}"
        if (
            not _is_trimmed_text(release.requested_tag)
            or release.tag_ref != expected_ref
            or release.tag_object_type not in {"commit", "tag"}
            or not _is_trimmed_text(release.tag_object_sha)
            or type(release.release_id) is not int
            or release.release_id < 1
        ):
            return _local_problem(
                "malformed_source",
                interval,
                repository,
                "A GitHub Release source had inconsistent release or tag identity.",
            )

        existing = by_version.get(candidate.release_version)
        if existing is not None:
            if existing != candidate:
                return _local_problem(
                    "conflicting_source_identity",
                    interval,
                    repository,
                    (
                        "More than one conflicting exact GitHub Release record was "
                        f"supplied for {candidate.release_version!r}."
                    ),
                )
            continue

        if release.body is None or not release.body.strip():
            generated_problems.append(
                UpstreamAuthoritySourceProblem(
                    source_kind="github_release_body",
                    state="source_unavailable",
                    detail=(
                        f"GitHub Release {candidate.release_version!r} had no usable "
                        "release body."
                    ),
                    release_version=candidate.release_version,
                )
            )
            continue

        by_version[candidate.release_version] = candidate

    return tuple(by_version.values()), tuple(generated_problems)


def _validate_tagged_changelogs(
    tagged_changelogs: Sequence[TaggedChangelogEvidence],
    interval: DependencyReleaseInterval,
    repository: str,
) -> TaggedChangelogEvidence | None | UpstreamIntervalAuthorityProblem:
    unique: list[TaggedChangelogEvidence] = []
    for candidate in tagged_changelogs:
        if not isinstance(candidate, TaggedChangelogEvidence):
            return _local_problem(
                "unsupported_source_authority",
                interval,
                repository,
                "A tagged-changelog candidate had an unsupported authority type.",
            )
        if candidate not in unique:
            unique.append(candidate)

    if len(unique) > 1:
        return _local_problem(
            "ambiguous_source",
            interval,
            repository,
            "More than one distinct tagged changelog identity was supplied.",
        )
    if not unique:
        return None

    candidate = unique[0]
    if not _same_repository(candidate.repository, repository) or candidate.interval != interval:
        return _local_problem(
            "identity_mismatch",
            interval,
            repository,
            "The tagged changelog did not match the selected repository and interval.",
        )

    accepted_tags = {interval.proposed_version, f"v{interval.proposed_version}"}
    if (
        candidate.requested_tag not in accepted_tags
        or candidate.tag_ref != f"refs/tags/{candidate.requested_tag}"
        or candidate.tag_object_type not in {"commit", "tag"}
        or not _is_trimmed_text(candidate.tag_object_sha)
        or not _is_trimmed_text(candidate.resolved_commit_sha)
        or not _is_repository_path(candidate.path)
        or candidate.returned_path != candidate.path
        or not _is_trimmed_text(candidate.blob_sha)
        or type(candidate.reported_byte_count) is not int
        or type(candidate.decoded_byte_count) is not int
        or candidate.reported_byte_count < 0
        or candidate.decoded_byte_count < 0
        or candidate.reported_byte_count != candidate.decoded_byte_count
        or not isinstance(candidate.content, str)
        or not candidate.content.strip()
        or len(candidate.content.encode("utf-8")) != candidate.decoded_byte_count
    ):
        return _local_problem(
            "malformed_source",
            interval,
            repository,
            "The tagged changelog had inconsistent tag, path, blob, byte, or text evidence.",
        )
    return candidate


def _validate_package_metadata(
    package_metadata: Sequence[PackageMetadataCorroboration],
    interval: DependencyReleaseInterval,
    repository: str,
    crossed_releases: CrossedReleaseIndexEvidence | None,
) -> tuple[PackageMetadataCorroboration, ...] | UpstreamIntervalAuthorityProblem:
    allowed_versions = {interval.old_version, interval.proposed_version}
    if crossed_releases is not None:
        allowed_versions.update(crossed_releases.ordered_versions)

    normalized: list[PackageMetadataCorroboration] = []
    for candidate in package_metadata:
        if not isinstance(candidate, PackageMetadataCorroboration):
            return _local_problem(
                "unsupported_source_authority",
                interval,
                repository,
                "A package-metadata candidate had an unsupported authority type.",
            )
        if (
            candidate.package != interval.package
            or candidate.normalized_package != interval.normalized_package
            or candidate.release_version not in allowed_versions
        ):
            return _local_problem(
                "identity_mismatch",
                interval,
                repository,
                "Package metadata was outside the selected package or release interval.",
            )
        if (
            not _is_trimmed_text(candidate.source_url)
            or (
                candidate.requires_python is not None
                and not _is_trimmed_text(candidate.requires_python)
            )
        ):
            return _local_problem(
                "malformed_source",
                interval,
                repository,
                "Package metadata contained invalid source or requires-python text.",
            )
        if candidate not in normalized:
            normalized.append(candidate)
    return tuple(normalized)


def _validate_source_problems(
    source_problems: Sequence[UpstreamAuthoritySourceProblem],
) -> tuple[UpstreamAuthoritySourceProblem, ...] | str:
    normalized: list[UpstreamAuthoritySourceProblem] = []
    for problem in source_problems:
        if not isinstance(problem, UpstreamAuthoritySourceProblem):
            return "A source problem had an unsupported type."
        if (
            problem.source_kind not in UPSTREAM_SOURCE_AUTHORITY_ORDER
            or problem.state
            not in {
                "source_unavailable",
                "malformed_source",
                "identity_mismatch",
                "acquisition_failed",
            }
            or not _is_trimmed_text(problem.detail)
            or (
                problem.release_version is not None
                and not _is_trimmed_text(problem.release_version)
            )
            or (problem.path is not None and not _is_repository_path(problem.path))
        ):
            return "A source problem contained invalid identity or detail fields."
        if problem not in normalized:
            normalized.append(problem)
    return tuple(normalized)


def _same_repository(left: str, right: str) -> bool:
    try:
        return validate_repository(left).casefold() == validate_repository(right).casefold()
    except ValueError:
        return False


def _is_repository_path(path: object) -> bool:
    if not isinstance(path, str) or not path or path.startswith("/") or "\\" in path:
        return False
    parts = path.split("/")
    return not any(not part or part in {".", ".."} for part in parts)


def _is_trimmed_text(value: object) -> bool:
    return isinstance(value, str) and bool(value) and value == value.strip()


def _problem(
    state: UpstreamIntervalAuthorityProblemState,
    interval: DependencyReleaseInterval,
    repository: str,
    detail: str,
    source_problems: Sequence[UpstreamAuthoritySourceProblem],
) -> UpstreamIntervalAuthorityProblem:
    return UpstreamIntervalAuthorityProblem(
        state=state,
        interval=interval,
        repository=repository,
        detail=detail,
        source_problems=tuple(source_problems),
    )


def _local_problem(
    state: UpstreamIntervalAuthorityProblemState,
    interval: DependencyReleaseInterval,
    repository: str,
    detail: str,
) -> UpstreamIntervalAuthorityProblem:
    return UpstreamIntervalAuthorityProblem(
        state=state,
        interval=interval,
        repository=repository,
        detail=detail,
    )
