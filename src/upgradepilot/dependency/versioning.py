"""Dependency-release interval parsing and PEP 440 ordering semantics.

This module owns dependency-version parsing and crossed-release ordering. It does not
acquire releases or decide target-Python relevance.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

from packaging.version import InvalidVersion, Version

from ..upstream.interval import DependencyReleaseInterval

type PackagingVersionProblemState = Literal[
    "invalid_python_package_version",
    "equivalent_python_package_versions",
    "dependency_version_not_forward",
    "invalid_crossed_release_version",
    "crossed_release_outside_interval",
    "equivalent_crossed_release_versions",
    "proposed_release_missing",
]


@dataclass(frozen=True, slots=True)
class ParsedDependencyReleaseInterval:
    """Raw dependency interval plus standards-parsed semantic bounds."""

    interval: DependencyReleaseInterval
    old_version: Version
    proposed_version: Version


@dataclass(frozen=True, slots=True)
class OrderedCrossedReleaseVersions:
    """Exact crossed-release identities sorted by their PEP 440 meaning."""

    interval: ParsedDependencyReleaseInterval
    ordered_raw_versions: tuple[str, ...]
    ordered_versions: tuple[Version, ...]


@dataclass(frozen=True, slots=True)
class PackagingVersionProblem:
    """Explicit reason dependency release ordering could not be established."""

    state: PackagingVersionProblemState
    interval: DependencyReleaseInterval
    detail: str
    release_version: str | None = None


type DependencyReleaseIntervalMethodResult = (
    ParsedDependencyReleaseInterval | PackagingVersionProblem
)
type CrossedReleaseOrderingResult = OrderedCrossedReleaseVersions | PackagingVersionProblem


def parse_dependency_release_interval(
    interval: DependencyReleaseInterval,
) -> DependencyReleaseIntervalMethodResult:
    """Parse and compare exact raw old/proposed dependency versions with PEP 440."""

    if not isinstance(interval, DependencyReleaseInterval):
        raise TypeError("interval must be DependencyReleaseInterval.")

    old = _parse_package_version(interval, interval.old_version, boundary="old")
    if isinstance(old, PackagingVersionProblem):
        return old
    proposed = _parse_package_version(
        interval,
        interval.proposed_version,
        boundary="proposed",
    )
    if isinstance(proposed, PackagingVersionProblem):
        return proposed

    if old == proposed:
        return PackagingVersionProblem(
            state="equivalent_python_package_versions",
            interval=interval,
            detail=(
                "The exact old and proposed version strings are PEP 440-equivalent "
                "and therefore do not establish a semantic forward update."
            ),
        )
    if proposed < old:
        return PackagingVersionProblem(
            state="dependency_version_not_forward",
            interval=interval,
            detail=(
                "The proposed dependency version precedes the old version under "
                "PEP 440 ordering."
            ),
        )

    return ParsedDependencyReleaseInterval(
        interval=interval,
        old_version=old,
        proposed_version=proposed,
    )


def order_crossed_release_versions(
    interval: ParsedDependencyReleaseInterval,
    release_versions: Sequence[str],
) -> CrossedReleaseOrderingResult:
    """Validate and order already selected crossed-release raw identities."""

    if not isinstance(interval, ParsedDependencyReleaseInterval):
        raise TypeError("interval must be ParsedDependencyReleaseInterval.")
    if isinstance(release_versions, (str, bytes)) or not isinstance(
        release_versions, Sequence
    ):
        raise TypeError("release_versions must be a sequence of exact version strings.")

    parsed_by_version: dict[Version, str] = {}
    pairs: list[tuple[Version, str]] = []

    for raw in release_versions:
        if not isinstance(raw, str) or not raw or raw != raw.strip():
            return PackagingVersionProblem(
                state="invalid_crossed_release_version",
                interval=interval.interval,
                release_version=raw if isinstance(raw, str) else None,
                detail="A crossed-release identity must be non-empty exact trimmed text.",
            )
        try:
            parsed = Version(raw)
        except InvalidVersion:
            return PackagingVersionProblem(
                state="invalid_crossed_release_version",
                interval=interval.interval,
                release_version=raw,
                detail=f"Crossed release {raw!r} is not a valid PEP 440 version.",
            )

        if not interval.old_version < parsed <= interval.proposed_version:
            return PackagingVersionProblem(
                state="crossed_release_outside_interval",
                interval=interval.interval,
                release_version=raw,
                detail=(
                    f"Crossed release {raw!r} was outside the exact old-exclusive, "
                    "proposed-inclusive dependency interval."
                ),
            )

        existing = parsed_by_version.get(parsed)
        if existing is not None:
            return PackagingVersionProblem(
                state="equivalent_crossed_release_versions",
                interval=interval.interval,
                release_version=raw,
                detail=(
                    f"Crossed releases {existing!r} and {raw!r} are PEP 440-equivalent "
                    "and cannot both identify one trusted release sequence."
                ),
            )

        parsed_by_version[parsed] = raw
        pairs.append((parsed, raw))

    if interval.interval.proposed_version not in {raw for _, raw in pairs}:
        return PackagingVersionProblem(
            state="proposed_release_missing",
            interval=interval.interval,
            release_version=interval.interval.proposed_version,
            detail=(
                "The exact raw proposed dependency version was absent from the "
                "crossed-release sequence."
            ),
        )

    ordered = tuple(sorted(pairs, key=lambda item: item[0]))
    return OrderedCrossedReleaseVersions(
        interval=interval,
        ordered_raw_versions=tuple(raw for _, raw in ordered),
        ordered_versions=tuple(parsed for parsed, _ in ordered),
    )


def _parse_package_version(
    interval: DependencyReleaseInterval,
    raw: str,
    *,
    boundary: Literal["old", "proposed"],
) -> Version | PackagingVersionProblem:
    if not isinstance(raw, str) or not raw or raw != raw.strip():
        return PackagingVersionProblem(
            state="invalid_python_package_version",
            interval=interval,
            release_version=raw if isinstance(raw, str) else None,
            detail=(
                f"The exact {boundary} dependency version must be non-empty trimmed "
                "text before PEP 440 parsing."
            ),
        )
    try:
        return Version(raw)
    except InvalidVersion:
        return PackagingVersionProblem(
            state="invalid_python_package_version",
            interval=interval,
            release_version=raw,
            detail=(
                f"The exact {boundary} dependency version {raw!r} is not a valid "
                "PEP 440 version."
            ),
        )


__all__ = (
    "CrossedReleaseOrderingResult",
    "DependencyReleaseIntervalMethodResult",
    "OrderedCrossedReleaseVersions",
    "PackagingVersionProblem",
    "PackagingVersionProblemState",
    "ParsedDependencyReleaseInterval",
    "order_crossed_release_versions",
    "parse_dependency_release_interval",
)
