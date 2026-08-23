"""Define trusted upstream release-interval identity and source authority.

This module is intentionally pure. It proves source identity, immutable provenance,
and bounded old-exclusive/proposed-inclusive interval authority. It does not acquire
sources, parse semantic prose, compare target Python, or make maintainer decisions.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal

from ..dependency.change import DependencyVersionChange
from ..github.identity import validate_commit_sha, validate_repository
from ..github.release import GitHubReleaseEvidence
from ..package_identity import normalize_package_name
from ..repository_path import repository_relative_parts

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
    package: str
    normalized_package: str
    old_version: str
    proposed_version: str
    lower_bound_inclusive: Literal[False] = field(init=False, default=False)
    upper_bound_inclusive: Literal[True] = field(init=False, default=True)


@dataclass(frozen=True, slots=True)
class CrossedReleaseIndexEvidence:
    repository: str
    interval: DependencyReleaseInterval
    ordered_versions: tuple[str, ...]
    source_url: str
    retrieved_at: datetime


@dataclass(frozen=True, slots=True)
class IntervalGitHubReleaseSource:
    release_version: str
    release: GitHubReleaseEvidence


@dataclass(frozen=True, slots=True)
class TaggedChangelogEvidence:
    """Exact proposed-tag changelog text admitted as interval-authority evidence.

    ``repository`` + ``resolved_commit_sha`` + ``path`` locate the immutable source.
    Provider transport metadata and Git tag peeling details are intentionally absent;
    their acquisition boundaries establish those facts before this durable record exists.

    This successful-evidence type owns its intrinsic locator/text invariants. Later
    authority composition therefore needs to validate only relationships to independently
    supplied repository/interval evidence, not revalidate this record field by field.
    """

    repository: str
    interval: DependencyReleaseInterval
    resolved_commit_sha: str
    path: str
    content: str

    def __post_init__(self) -> None:
        if not isinstance(self.interval, DependencyReleaseInterval):
            raise TypeError("interval must be DependencyReleaseInterval.")

        repository = validate_repository(self.repository)
        resolved_commit_sha = validate_commit_sha(self.resolved_commit_sha)
        path_parts = repository_relative_parts(self.path)
        if path_parts is None:
            raise ValueError("path must be a normalized repository-relative POSIX file path.")
        if not isinstance(self.content, str) or not self.content.strip():
            raise ValueError("content must contain usable changelog text.")

        object.__setattr__(self, "repository", repository)
        object.__setattr__(self, "resolved_commit_sha", resolved_commit_sha)
        object.__setattr__(self, "path", "/".join(path_parts))


@dataclass(frozen=True, slots=True)
class PackageMetadataCorroboration:
    package: str
    normalized_package: str
    release_version: str
    source_url: str
    requires_python: str | None
    retrieved_at: datetime


@dataclass(frozen=True, slots=True)
class UpstreamAuthoritySourceProblem:
    source_kind: UpstreamAuthoritySourceKind
    state: UpstreamAuthoritySourceProblemState
    detail: str
    release_version: str | None = None
    path: str | None = None


@dataclass(frozen=True, slots=True)
class AuthoritativeUpstreamIntervalEvidence:
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
    return DependencyReleaseInterval(
        package=dependency.package,
        normalized_package=dependency.normalized_package,
        old_version=dependency.old_version,
        proposed_version=dependency.proposed_version,
    )


def upstream_source_role(source_kind: str) -> UpstreamSourceRole:
    return _SOURCE_ROLES.get(source_kind, "unsupported")


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
    interval_error = _validate_interval(interval)
    if interval_error is not None:
        return _make_problem("malformed_source", interval, repository, interval_error)

    try:
        repository = validate_repository(repository)
    except ValueError:
        return _make_problem(
            "malformed_source",
            interval,
            repository,
            "The upstream repository identity was malformed.",
        )

    if crossed_releases is not None:
        index_error = _validate_crossed_release_index(
            crossed_releases,
            interval,
            repository,
        )
        if index_error is not None:
            state, detail = index_error
            return _make_problem(state, interval, repository, detail)

    normalized_problems = _validate_source_problems(
        source_problems,
        interval,
        repository,
        crossed_releases,
    )
    if isinstance(normalized_problems, UpstreamIntervalAuthorityProblem):
        return normalized_problems

    release_result = _validate_release_bodies(
        release_bodies,
        interval,
        repository,
        crossed_releases,
    )
    if isinstance(release_result, UpstreamIntervalAuthorityProblem):
        return _with_problems(release_result, normalized_problems)
    usable_releases, generated_release_problems = release_result
    collected_problems = normalized_problems + generated_release_problems

    changelog_result = _validate_tagged_changelogs(
        tagged_changelogs,
        interval,
        repository,
    )
    if isinstance(changelog_result, UpstreamIntervalAuthorityProblem):
        return _with_problems(changelog_result, collected_problems)

    metadata_result = _validate_package_metadata(
        package_metadata,
        interval,
        repository,
        crossed_releases,
    )
    if isinstance(metadata_result, UpstreamIntervalAuthorityProblem):
        return _with_problems(metadata_result, collected_problems)

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

    has_changelog = changelog_result is not None
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
            return _make_problem(
                "interval_incomplete",
                interval,
                repository,
                detail,
                collected_problems,
            )
        return _make_problem(
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
        ordered_releases = usable_releases

    if complete_release_series and has_changelog:
        basis: UpstreamIntervalAuthorityBasis = "complete_release_series_and_tagged_changelog"
    elif complete_release_series:
        basis = "complete_release_series"
    else:
        basis = "tagged_changelog"

    return AuthoritativeUpstreamIntervalEvidence(
        interval=interval,
        repository=repository,
        crossed_releases=crossed_releases,
        release_bodies=ordered_releases,
        tagged_changelog=changelog_result,
        package_metadata=metadata_result,
        source_problems=collected_problems,
        authority_basis=basis,
    )


def _validate_interval(interval: object) -> str | None:
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
    index: object,
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
    versions = index.ordered_versions
    if (
        not isinstance(versions, tuple)
        or not versions
        or any(not _is_trimmed_text(version) for version in versions)
        or len(set(versions)) != len(versions)
        or interval.old_version in versions
        or versions[-1] != interval.proposed_version
        or not _is_trimmed_text(index.source_url)
        or not isinstance(index.retrieved_at, datetime)
    ):
        return (
            "malformed_source",
            (
                "The crossed-release index must contain unique non-empty versions, "
                "exclude the old version, end with the proposed version, and preserve "
                "source identity."
            ),
        )
    return None


def _validate_source_problems(
    source_problems: Sequence[UpstreamAuthoritySourceProblem],
    interval: DependencyReleaseInterval,
    repository: str,
    crossed_releases: CrossedReleaseIndexEvidence | None,
) -> tuple[UpstreamAuthoritySourceProblem, ...] | UpstreamIntervalAuthorityProblem:
    allowed_versions = {interval.old_version, interval.proposed_version}
    if crossed_releases is not None:
        allowed_versions.update(crossed_releases.ordered_versions)

    normalized: list[UpstreamAuthoritySourceProblem] = []
    for problem in source_problems:
        if not isinstance(problem, UpstreamAuthoritySourceProblem):
            return _make_problem(
                "malformed_source",
                interval,
                repository,
                "A source problem had an unsupported type.",
            )
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
            return _make_problem(
                "malformed_source",
                interval,
                repository,
                "A source problem contained invalid identity or detail fields.",
                (problem,),
            )
        if (
            problem.release_version is not None
            and problem.release_version not in allowed_versions
        ):
            return _make_problem(
                "identity_mismatch",
                interval,
                repository,
                "A source problem referred to a release outside the bounded interval.",
                (problem,),
            )
        if problem not in normalized:
            normalized.append(problem)

    normalized_tuple = tuple(normalized)
    identity_problem = next(
        (item for item in normalized_tuple if item.state == "identity_mismatch"),
        None,
    )
    if identity_problem is not None:
        return _make_problem(
            "identity_mismatch",
            interval,
            repository,
            identity_problem.detail,
            normalized_tuple,
        )
    malformed_problem = next(
        (item for item in normalized_tuple if item.state == "malformed_source"),
        None,
    )
    if malformed_problem is not None:
        return _make_problem(
            "malformed_source",
            interval,
            repository,
            malformed_problem.detail,
            normalized_tuple,
        )
    return normalized_tuple


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
    seen_by_version: dict[str, IntervalGitHubReleaseSource] = {}
    usable_by_version: dict[str, IntervalGitHubReleaseSource] = {}
    generated_problems: list[UpstreamAuthoritySourceProblem] = []
    allowed_versions = set(crossed_releases.ordered_versions) if crossed_releases is not None else None

    for candidate in release_bodies:
        if not isinstance(candidate, IntervalGitHubReleaseSource):
            return _make_problem(
                "unsupported_source_authority",
                interval,
                repository,
                "A release-body candidate had an unsupported authority type.",
            )
        if not _is_trimmed_text(candidate.release_version):
            return _make_problem(
                "malformed_source",
                interval,
                repository,
                "A GitHub Release source lacked a valid release version.",
            )

        release = candidate.release
        if not isinstance(release, GitHubReleaseEvidence):
            return _make_problem(
                "malformed_source",
                interval,
                repository,
                "A GitHub Release source lacked exact release evidence.",
            )
        if not _same_repository(release.repository, repository):
            return _make_problem(
                "identity_mismatch",
                interval,
                repository,
                "A GitHub Release source belonged to another repository.",
            )
        if allowed_versions is not None and candidate.release_version not in allowed_versions:
            return _make_problem(
                "identity_mismatch",
                interval,
                repository,
                f"Release version {candidate.release_version!r} was outside the trusted crossed-release index.",
            )

        accepted_tags = {candidate.release_version, f"v{candidate.release_version}"}
        if release.requested_tag not in accepted_tags:
            return _make_problem(
                "identity_mismatch",
                interval,
                repository,
                (
                    f"GitHub Release tag {release.requested_tag!r} did not identify "
                    f"declared release version {candidate.release_version!r}."
                ),
            )
        if (
            release.tag_ref != f"refs/tags/{release.requested_tag}"
            or release.tag_object_type not in {"commit", "tag"}
            or not _is_trimmed_text(release.tag_object_sha)
            or type(release.release_id) is not int
            or release.release_id < 1
        ):
            return _make_problem(
                "malformed_source",
                interval,
                repository,
                "A GitHub Release source had inconsistent release or tag identity.",
            )

        existing = seen_by_version.get(candidate.release_version)
        if existing is not None:
            if existing != candidate:
                return _make_problem(
                    "conflicting_source_identity",
                    interval,
                    repository,
                    (
                        "More than one conflicting exact GitHub Release record was "
                        f"supplied for {candidate.release_version!r}."
                    ),
                )
            continue
        seen_by_version[candidate.release_version] = candidate

        if release.body is None or (isinstance(release.body, str) and not release.body.strip()):
            generated_problems.append(
                UpstreamAuthoritySourceProblem(
                    source_kind="github_release_body",
                    state="source_unavailable",
                    detail=f"GitHub Release {candidate.release_version!r} had no usable release body.",
                    release_version=candidate.release_version,
                )
            )
            continue
        if not isinstance(release.body, str):
            return _make_problem(
                "malformed_source",
                interval,
                repository,
                "A GitHub Release body was not text or null.",
            )
        usable_by_version[candidate.release_version] = candidate

    return tuple(usable_by_version.values()), tuple(generated_problems)


def _validate_tagged_changelogs(
    tagged_changelogs: Sequence[TaggedChangelogEvidence],
    interval: DependencyReleaseInterval,
    repository: str,
) -> TaggedChangelogEvidence | None | UpstreamIntervalAuthorityProblem:
    """Admit at most one tagged changelog and bind it to this interval/repository."""

    unique: list[TaggedChangelogEvidence] = []
    for candidate in tagged_changelogs:
        if not isinstance(candidate, TaggedChangelogEvidence):
            return _make_problem(
                "unsupported_source_authority",
                interval,
                repository,
                "A tagged-changelog candidate had an unsupported authority type.",
            )
        if candidate not in unique:
            unique.append(candidate)

    if len(unique) > 1:
        return _make_problem(
            "ambiguous_source",
            interval,
            repository,
            "More than one distinct tagged changelog identity was supplied.",
        )
    if not unique:
        return None

    candidate = unique[0]
    if not _same_repository(candidate.repository, repository) or candidate.interval != interval:
        return _make_problem(
            "identity_mismatch",
            interval,
            repository,
            "The tagged changelog did not match the selected repository and interval.",
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
            return _make_problem(
                "unsupported_source_authority",
                interval,
                repository,
                "A package-metadata candidate had an unsupported authority type.",
            )
        if (
            not _is_trimmed_text(candidate.package)
            or normalize_package_name(candidate.package) != interval.normalized_package
            or candidate.normalized_package != interval.normalized_package
            or candidate.release_version not in allowed_versions
        ):
            return _make_problem(
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
            or not isinstance(candidate.retrieved_at, datetime)
        ):
            return _make_problem(
                "malformed_source",
                interval,
                repository,
                "Package metadata contained invalid source or requires-python evidence.",
            )
        if candidate not in normalized:
            normalized.append(candidate)
    return tuple(normalized)


def _same_repository(left: object, right: object) -> bool:
    try:
        return validate_repository(left).casefold() == validate_repository(right).casefold()  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return False


def _is_repository_path(path: object) -> bool:
    if not isinstance(path, str) or not path or path.startswith("/") or "\\" in path:
        return False
    parts = path.split("/")
    return not any(not part or part in {".", ".."} for part in parts)


def _is_trimmed_text(value: object) -> bool:
    return isinstance(value, str) and bool(value) and value == value.strip()


def _make_problem(
    state: UpstreamIntervalAuthorityProblemState,
    interval: DependencyReleaseInterval,
    repository: str,
    detail: str,
    source_problems: Sequence[UpstreamAuthoritySourceProblem] = (),
) -> UpstreamIntervalAuthorityProblem:
    return UpstreamIntervalAuthorityProblem(
        state=state,
        interval=interval,
        repository=repository,
        detail=detail,
        source_problems=tuple(source_problems),
    )


def _with_problems(
    problem: UpstreamIntervalAuthorityProblem,
    source_problems: Sequence[UpstreamAuthoritySourceProblem],
) -> UpstreamIntervalAuthorityProblem:
    return UpstreamIntervalAuthorityProblem(
        state=problem.state,
        interval=problem.interval,
        repository=problem.repository,
        detail=problem.detail,
        source_problems=tuple(source_problems) + problem.source_problems,
    )


__all__ = (
    "UPSTREAM_SOURCE_AUTHORITY_ORDER",
    "AuthoritativeUpstreamIntervalEvidence",
    "CrossedReleaseIndexEvidence",
    "DependencyReleaseInterval",
    "IntervalGitHubReleaseSource",
    "PackageMetadataCorroboration",
    "TaggedChangelogEvidence",
    "UpstreamAuthoritySourceKind",
    "UpstreamAuthoritySourceProblem",
    "UpstreamAuthoritySourceProblemState",
    "UpstreamIntervalAuthorityBasis",
    "UpstreamIntervalAuthorityProblem",
    "UpstreamIntervalAuthorityProblemState",
    "UpstreamIntervalAuthorityResult",
    "UpstreamSourceKind",
    "UpstreamSourceRole",
    "assemble_upstream_interval_authority",
    "release_interval_from_dependency_change",
    "upstream_source_role",
)
