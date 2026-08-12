"""Mechanism-specific candidate formulation for published artifact-serviceability changes.

This module begins the second B2 technical mechanism. It compares exact old/proposed
PyPI release inventories and formulates a candidate only when published wheel
compatibility tags present in the old release are no longer published by the proposed
release. It intentionally does not claim that any exact target loses a compatible wheel:
target interpreter/ABI/platform evidence belongs to the later applicability step.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from packaging.tags import Tag
from packaging.utils import InvalidWheelFilename, parse_wheel_filename
from packaging.version import InvalidVersion, Version

from ..dependency.change import DependencyVersionChange
from ..github.pull_request import PullRequestIdentity
from ..pypi.release import DistributionFile, PackageReleaseEvidence


type ArtifactServiceabilityComponentStatus = Literal[
    "established",
    "to_evaluate",
    "possible",
]
type ArtifactServiceabilityEvidenceProblemState = Literal[
    "wheel_filename_uninterpretable",
    "wheel_identity_mismatch",
]


@dataclass(frozen=True, slots=True)
class PublishedWheelArtifact:
    """One published wheel plus the exact compatibility tags encoded by its filename."""

    filename: str
    tags: frozenset[Tag]


@dataclass(frozen=True, slots=True)
class ArtifactServiceabilityEvidenceProblem:
    """External release evidence that cannot support deterministic wheel interpretation."""

    state: ArtifactServiceabilityEvidenceProblemState
    release_version: str
    filename: str
    detail: str


@dataclass(frozen=True, slots=True)
class ArtifactServiceabilityImpactCandidate:
    """Target-agnostic candidate for loss of published wheel compatibility tags."""

    pull_request: PullRequestIdentity
    dependency: DependencyVersionChange
    old_release: PackageReleaseEvidence
    proposed_release: PackageReleaseEvidence
    target_repository: str
    target_revision: str
    mechanism_status: ArtifactServiceabilityComponentStatus
    exposure_status: ArtifactServiceabilityComponentStatus
    consequence_status: ArtifactServiceabilityComponentStatus
    old_wheels: tuple[PublishedWheelArtifact, ...]
    proposed_wheels: tuple[PublishedWheelArtifact, ...]
    removed_wheel_tags: frozenset[Tag]
    added_wheel_tags: frozenset[Tag]
    old_source_distribution_available: bool
    proposed_source_distribution_available: bool
    exposure_proposition: str
    possible_consequence: str


type ArtifactServiceabilityCandidateResult = (
    ArtifactServiceabilityImpactCandidate
    | ArtifactServiceabilityEvidenceProblem
    | None
)


def build_artifact_serviceability_impact_candidate(
    pull_request: PullRequestIdentity,
    dependency: DependencyVersionChange,
    old_release: PackageReleaseEvidence,
    proposed_release: PackageReleaseEvidence,
) -> ArtifactServiceabilityCandidateResult:
    """Compare exact release inventories without manufacturing target applicability.

    ``None`` means the bounded mechanism did not observe loss of any exact published
    wheel compatibility tag between the two release inventories. An evidence-problem
    result means a wheel record could not be interpreted deterministically. Neither
    result is a claim about candidate-discovery completeness for the whole dependency
    transition.
    """

    _validate_release_identity(
        dependency,
        old_release,
        expected_version=dependency.old_version,
        role="old",
    )
    _validate_release_identity(
        dependency,
        proposed_release,
        expected_version=dependency.proposed_version,
        role="proposed",
    )

    old_inventory = _interpret_wheels(old_release)
    if isinstance(old_inventory, ArtifactServiceabilityEvidenceProblem):
        return old_inventory

    proposed_inventory = _interpret_wheels(proposed_release)
    if isinstance(proposed_inventory, ArtifactServiceabilityEvidenceProblem):
        return proposed_inventory

    old_tags = frozenset(tag for wheel in old_inventory for tag in wheel.tags)
    proposed_tags = frozenset(
        tag for wheel in proposed_inventory for tag in wheel.tags
    )
    removed_tags = old_tags - proposed_tags

    if not removed_tags:
        return None

    added_tags = proposed_tags - old_tags
    old_sdist = _has_source_distribution(old_release)
    proposed_sdist = _has_source_distribution(proposed_release)

    if proposed_sdist:
        possible_consequence = (
            "A target environment compatible with an old published wheel tag but with "
            "no compatible proposed wheel may move from a prebuilt wheel path to "
            "source-distribution fallback. Target compatibility and source-build success "
            "remain separate propositions to evaluate."
        )
    else:
        possible_consequence = (
            "A target environment compatible with an old published wheel tag but with "
            "no compatible proposed wheel may lose that published binary installation "
            "path; no proposed source-distribution fallback is present in this release "
            "inventory. Target compatibility remains to evaluate."
        )

    return ArtifactServiceabilityImpactCandidate(
        pull_request=pull_request,
        dependency=dependency,
        old_release=old_release,
        proposed_release=proposed_release,
        target_repository=pull_request.repository,
        target_revision=pull_request.head_sha,
        mechanism_status="established",
        exposure_status="to_evaluate",
        consequence_status="possible",
        old_wheels=old_inventory,
        proposed_wheels=proposed_inventory,
        removed_wheel_tags=removed_tags,
        added_wheel_tags=added_tags,
        old_source_distribution_available=old_sdist,
        proposed_source_distribution_available=proposed_sdist,
        exposure_proposition=(
            "The exact target environment is compatible with at least one old published "
            "wheel path that is not replaced by a compatible proposed-release wheel."
        ),
        possible_consequence=possible_consequence,
    )


def _validate_release_identity(
    dependency: DependencyVersionChange,
    release: PackageReleaseEvidence,
    *,
    expected_version: str,
    role: str,
) -> None:
    if release.normalized_package != dependency.normalized_package:
        raise ValueError(
            f"{role} package release must match the dependency's normalized package."
        )
    if (
        release.requested_version != expected_version
        or release.published_version != expected_version
    ):
        raise ValueError(
            f"{role} package release must match the exact dependency transition version."
        )


def _interpret_wheels(
    release: PackageReleaseEvidence,
) -> tuple[PublishedWheelArtifact, ...] | ArtifactServiceabilityEvidenceProblem:
    wheels: list[PublishedWheelArtifact] = []
    try:
        release_version = Version(release.published_version)
    except InvalidVersion:
        return ArtifactServiceabilityEvidenceProblem(
            state="wheel_identity_mismatch",
            release_version=release.published_version,
            filename="",
            detail="The exact release version cannot be interpreted as a packaging version.",
        )

    for distribution in release.distribution_files:
        if distribution.package_type != "bdist_wheel":
            continue

        try:
            parsed_name, parsed_version, _build, tags = parse_wheel_filename(
                distribution.filename,
                validate_order=True,
            )
        except (InvalidWheelFilename, ValueError) as exc:
            return ArtifactServiceabilityEvidenceProblem(
                state="wheel_filename_uninterpretable",
                release_version=release.published_version,
                filename=distribution.filename,
                detail=(
                    "A published wheel filename could not be interpreted by the admitted "
                    f"packaging method: {exc}"
                ),
            )

        if (
            str(parsed_name) != release.normalized_package
            or parsed_version != release_version
        ):
            return ArtifactServiceabilityEvidenceProblem(
                state="wheel_identity_mismatch",
                release_version=release.published_version,
                filename=distribution.filename,
                detail=(
                    "The published wheel filename identity does not match the exact "
                    "package release evidence."
                ),
            )

        wheels.append(
            PublishedWheelArtifact(
                filename=distribution.filename,
                tags=tags,
            )
        )

    return tuple(sorted(wheels, key=lambda item: item.filename))


def _has_source_distribution(release: PackageReleaseEvidence) -> bool:
    return any(
        distribution.package_type == "sdist"
        for distribution in release.distribution_files
    )


__all__ = (
    "ArtifactServiceabilityCandidateResult",
    "ArtifactServiceabilityComponentStatus",
    "ArtifactServiceabilityEvidenceProblem",
    "ArtifactServiceabilityEvidenceProblemState",
    "ArtifactServiceabilityImpactCandidate",
    "PublishedWheelArtifact",
    "build_artifact_serviceability_impact_candidate",
)
