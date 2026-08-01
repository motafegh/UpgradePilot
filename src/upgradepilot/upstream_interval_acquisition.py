"""Turn acquired package release keys into the trusted crossed-release index.

Data flow
---------

```text
PackageReleaseIndexEvidence          DependencyReleaseInterval
          │                                    │
          └──────── exact package identity ────┘
                           │
                           v
              parse dependency bounds
                   with PEP 440
                           │
                           v
          keep admitted releases satisfying
                 old < release <= proposed
                           │
                           v
            order_crossed_release_versions
                           │
                           v
              CrossedReleaseIndexEvidence
```

This module does not make network requests, acquire changelog text, resolve Git tags,
extract semantic claims, or decide target relevance. It owns only the deterministic
bridge between exact PyPI release-index evidence and the Step 1 crossed-release
contract.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from packaging.version import InvalidVersion, Version

from .github_client import validate_repository
from .packaging_method import (
    PackagingVersionProblem,
    order_crossed_release_versions,
    parse_dependency_release_interval,
)
from .pypi_client import PackageReleaseIndexEvidence
from .upstream_interval import CrossedReleaseIndexEvidence, DependencyReleaseInterval


type CrossedReleaseIndexSelectionProblemState = Literal[
    "identity_mismatch",
    "dependency_interval_unresolved",
    "release_index_unusable",
]


@dataclass(frozen=True, slots=True)
class SelectedCrossedReleaseIndex:
    """Trusted crossed releases plus source evidence and explicitly ignored legacy keys."""

    source_index: PackageReleaseIndexEvidence
    evidence: CrossedReleaseIndexEvidence
    ignored_non_pep440_versions: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class CrossedReleaseIndexSelectionProblem:
    """Why PyPI release keys could not earn one trusted crossed-release index."""

    state: CrossedReleaseIndexSelectionProblemState
    interval: DependencyReleaseInterval
    repository: str
    detail: str
    method_problem: PackagingVersionProblem | None = None


type CrossedReleaseIndexSelectionResult = (
    SelectedCrossedReleaseIndex | CrossedReleaseIndexSelectionProblem
)


def select_crossed_release_index(
    interval: DependencyReleaseInterval,
    repository: str,
    release_index: PackageReleaseIndexEvidence,
) -> CrossedReleaseIndexSelectionResult:
    """Select all admitted PyPI releases inside one dependency-update interval.

    PyPI supplies exact raw release keys. ``packaging.version.Version`` supplies PEP 440
    meaning. UpgradePilot supplies the product boundary: only PEP 440-comparable release
    identities are admitted into this index, and the interval is old-exclusive and
    proposed-inclusive.

    Non-PEP-440 project keys are retained in ``ignored_non_pep440_versions`` instead of
    disappearing silently. They are outside the admitted ordering domain and therefore
    do not become ``CrossedReleaseIndexEvidence``.
    """

    if not isinstance(interval, DependencyReleaseInterval):
        raise TypeError("interval must be DependencyReleaseInterval.")
    if not isinstance(release_index, PackageReleaseIndexEvidence):
        raise TypeError("release_index must be PackageReleaseIndexEvidence.")

    # Repository syntax is caller-owned identity, not an evidence problem from PyPI.
    # Reject malformed locators before they can be copied into trusted interval evidence.
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
            # PyPI can preserve legacy project keys that have no admitted PEP 440
            # ordering. They are evidence about the source response, but not members of
            # the standards-based release interval used by UpgradePilot.
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
