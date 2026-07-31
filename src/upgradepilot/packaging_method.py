"""Provide the bounded standards-based version method for target relevance.

This module owns PEP 440 parsing, crossed-release ordering, and stable Python-line
specifier intersection. It does not acquire sources, extract semantic claims, map
method results to target-relevance states, modify the CLI, or make compatibility,
safety, merge, and recommendation decisions.
"""

from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

from packaging.specifiers import InvalidSpecifier, Specifier, SpecifierSet
from packaging.version import InvalidVersion, Version

from .upstream_interval import DependencyReleaseInterval


type PackagingVersionProblemState = Literal[
    "invalid_python_package_version",
    "equivalent_python_package_versions",
    "dependency_version_not_forward",
    "invalid_crossed_release_version",
    "crossed_release_outside_interval",
    "equivalent_crossed_release_versions",
    "proposed_release_missing",
]
type PythonLineSpecifierProblemState = Literal[
    "invalid_python_line",
    "invalid_requires_python_specifier",
    "unsupported_requires_python_specifier",
    "unsatisfiable_requires_python_specifier",
]

_PYTHON_LINE = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\Z")
_SUPPORTED_SPECIFIER_OPERATORS = {"<", "<=", ">", ">=", "==", "!=", "~="}


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


@dataclass(frozen=True, slots=True)
class PythonLineSpecifierEvaluation:
    """Method-level answer for one stable Python line and target declaration."""

    python_line: str
    requires_python: str
    normalized_requires_python: str
    line_lower_bound: Version
    line_upper_bound: Version
    contains_stable_release: bool


@dataclass(frozen=True, slots=True)
class PythonLineSpecifierProblem:
    """Explicit reason the stable Python-line method could not evaluate."""

    state: PythonLineSpecifierProblemState
    python_line: str
    requires_python: str
    detail: str


type DependencyReleaseIntervalMethodResult = (
    ParsedDependencyReleaseInterval | PackagingVersionProblem
)
type CrossedReleaseOrderingResult = (
    OrderedCrossedReleaseVersions | PackagingVersionProblem
)
type PythonLineSpecifierMethodResult = (
    PythonLineSpecifierEvaluation | PythonLineSpecifierProblem
)


def parse_dependency_release_interval(
    interval: DependencyReleaseInterval,
) -> DependencyReleaseIntervalMethodResult:
    """Parse and compare exact raw old/proposed dependency versions with PEP 440."""

    if not isinstance(interval, DependencyReleaseInterval):
        raise TypeError("interval must be DependencyReleaseInterval.")

    old = _parse_package_version(
        interval,
        interval.old_version,
        boundary="old",
    )
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
    """Validate and order already selected crossed-release raw identities.

    The function does not discover releases. It requires every supplied candidate to
    belong to the old-exclusive/proposed-inclusive interval and preserves exact raw
    strings alongside parsed ``Version`` objects.
    """

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
                detail=(
                    "A crossed-release identity must be non-empty exact trimmed text."
                ),
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

    if interval.interval.proposed_version not in {
        raw for _, raw in pairs
    }:
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


def evaluate_python_line_specifier(
    python_line: str,
    requires_python: str,
) -> PythonLineSpecifierMethodResult:
    """Evaluate whether a target declaration admits any stable release in ``X.Y``.

    The method intersects the target specifier with the exact line interval and uses
    ``SpecifierSet.is_unsatisfiable()``. It never enumerates patch versions.
    """

    line_match = _PYTHON_LINE.fullmatch(python_line)
    if line_match is None:
        return PythonLineSpecifierProblem(
            state="invalid_python_line",
            python_line=python_line,
            requires_python=requires_python,
            detail="The Python line must be canonical non-negative major/minor text.",
        )

    if (
        not isinstance(requires_python, str)
        or not requires_python
        or requires_python != requires_python.strip()
    ):
        return PythonLineSpecifierProblem(
            state="invalid_requires_python_specifier",
            python_line=python_line,
            requires_python=requires_python,
            detail=(
                "The target requires-python declaration must be non-empty exact "
                "trimmed specifier text."
            ),
        )

    try:
        target = SpecifierSet(requires_python)
    except InvalidSpecifier as exc:
        return PythonLineSpecifierProblem(
            state="invalid_requires_python_specifier",
            python_line=python_line,
            requires_python=requires_python,
            detail=f"The target requires-python declaration was invalid: {exc}",
        )

    if len(target) == 0:
        return PythonLineSpecifierProblem(
            state="invalid_requires_python_specifier",
            python_line=python_line,
            requires_python=requires_python,
            detail="The target requires-python declaration contained no specifier.",
        )

    unsupported = _first_unsupported_specifier(target)
    if unsupported is not None:
        return PythonLineSpecifierProblem(
            state="unsupported_requires_python_specifier",
            python_line=python_line,
            requires_python=requires_python,
            detail=(
                f"Specifier {str(unsupported)!r} uses a version form outside the "
                "first stable Python-line method."
            ),
        )

    if target.is_unsatisfiable():
        return PythonLineSpecifierProblem(
            state="unsatisfiable_requires_python_specifier",
            python_line=python_line,
            requires_python=requires_python,
            detail=(
                "The target requires-python declaration is syntactically valid but "
                "cannot be satisfied by any version."
            ),
        )

    major = int(line_match.group(1))
    minor = int(line_match.group(2))
    lower = Version(f"{major}.{minor}")
    upper = Version(f"{major}.{minor + 1}")
    line_specifier = SpecifierSet(f">={lower},<{upper}")
    intersection = target & line_specifier

    return PythonLineSpecifierEvaluation(
        python_line=python_line,
        requires_python=requires_python,
        normalized_requires_python=str(target),
        line_lower_bound=lower,
        line_upper_bound=upper,
        contains_stable_release=not intersection.is_unsatisfiable(),
    )


def _parse_package_version(
    interval: DependencyReleaseInterval,
    raw: str,
    *,
    boundary: Literal["old", "proposed"],
) -> Version | PackagingVersionProblem:
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


def _first_unsupported_specifier(
    specifiers: SpecifierSet,
) -> Specifier | None:
    for specifier in specifiers:
        if specifier.operator not in _SUPPORTED_SPECIFIER_OPERATORS:
            return specifier
        if specifier.operator == "===":
            return specifier

        version_text = specifier.version
        if version_text.endswith(".*"):
            if specifier.operator not in {"==", "!="}:
                return specifier
            version_text = version_text[:-2]

        try:
            version = Version(version_text)
        except InvalidVersion:
            return specifier

        if (
            version.epoch != 0
            or version.pre is not None
            or version.post is not None
            or version.dev is not None
            or version.local is not None
        ):
            return specifier
    return None
