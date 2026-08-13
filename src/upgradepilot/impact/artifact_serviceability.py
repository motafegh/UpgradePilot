"""Mechanism-specific reasoning for published artifact-serviceability changes.

Increment 1 compares exact old/proposed PyPI release inventories and formulates a
candidate when published wheel compatibility capabilities disappear. Increment 2 adds
an exact target-side wheel-compatibility evidence contract and evaluates whether the
candidate actually applies to that target.

The boundary stays strict: package artifact facts do not manufacture target-environment
facts, and UpgradePilot's own runtime environment is never used as a proxy for the
repository being analyzed.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from packaging.tags import Tag
from packaging.utils import InvalidWheelFilename, parse_wheel_filename
from packaging.version import InvalidVersion, Version

from ..dependency.change import DependencyVersionChange
from ..github.pull_request import PullRequestIdentity
from ..pypi.release import PackageReleaseEvidence
from .applicability import (
    CandidateApplicabilityAssessment,
    PropositionAssessment,
    evaluate_applicability_path,
    evaluate_candidate_applicability,
)


type ArtifactServiceabilityComponentStatus = Literal[
    "established",
    "to_evaluate",
    "possible",
]
type ArtifactServiceabilityEvidenceProblemState = Literal[
    "wheel_filename_uninterpretable",
    "wheel_identity_mismatch",
]
type TargetWheelCompatibilityProblemState = Literal[
    "evidence_unavailable",
    "evidence_insufficient",
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
class TargetWheelCompatibilityEvidence:
    """Exact target-owned evidence of wheel tags supported by one observed environment.

    This object deliberately starts *after* evidence acquisition/interpretation. A later
    increment must earn these tags from admitted target evidence; callers must not derive
    them from UpgradePilot's own ``sys_tags()`` or guess them from broad labels such as
    merely "Python 3.6 on Linux".
    """

    repository: str
    revision: str
    source: str
    supported_tags: frozenset[Tag]

    def __post_init__(self) -> None:
        if not self.repository.strip():
            raise ValueError("target wheel-compatibility repository must be non-empty.")
        if not self.revision.strip():
            raise ValueError("target wheel-compatibility revision must be non-empty.")
        if not self.source.strip():
            raise ValueError("target wheel-compatibility source must be non-empty.")
        if not self.supported_tags:
            raise ValueError(
                "established target wheel compatibility requires at least one supported tag."
            )


@dataclass(frozen=True, slots=True)
class TargetWheelCompatibilityProblem:
    """Why exact target wheel compatibility could not be established."""

    state: TargetWheelCompatibilityProblemState
    repository: str
    revision: str
    source: str
    detail: str


type TargetWheelCompatibilityResult = (
    TargetWheelCompatibilityEvidence | TargetWheelCompatibilityProblem
)


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


@dataclass(frozen=True, slots=True)
class ArtifactServiceabilityImpactAssessment:
    """Candidate applicability before or after exact target compatibility evidence."""

    candidate: ArtifactServiceabilityImpactCandidate
    applicability: CandidateApplicabilityAssessment
    target_evidence: TargetWheelCompatibilityResult | None


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

    old_tags = _published_tags(old_inventory)
    proposed_tags = _published_tags(proposed_inventory)
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


def evaluate_artifact_serviceability_impact(
    candidate: ArtifactServiceabilityImpactCandidate,
    target_evidence: TargetWheelCompatibilityResult | None = None,
) -> ArtifactServiceabilityImpactAssessment:
    """Evaluate whether the candidate removes the target's prebuilt-wheel path.

    The target comparison uses the *complete* old and proposed wheel-tag inventories,
    not only ``candidate.removed_wheel_tags``. A particular old tag may disappear while
    a different proposed tag still serves the same target environment.
    """

    if target_evidence is not None:
        if target_evidence.repository != candidate.target_repository:
            raise ValueError(
                "target wheel-compatibility evidence must match the candidate repository."
            )
        if target_evidence.revision != candidate.target_revision:
            raise ValueError(
                "target wheel-compatibility evidence must match the candidate revision."
            )

    mechanism = PropositionAssessment(
        key="published_wheel_transition_established",
        state="established",
        evidence_coverage="sufficient",
        evidence_owner="impact.artifact_serviceability",
        detail=(
            "Exact old/proposed release inventories establish that at least one published "
            "wheel compatibility tag disappeared across the dependency transition."
        ),
    )
    target = _target_compatibility_proposition(target_evidence)
    old_path = _old_compatible_wheel_proposition(candidate, target_evidence)
    proposed_path_absent = _proposed_compatible_wheel_absence_proposition(
        candidate,
        target_evidence,
    )

    path = evaluate_applicability_path(
        "prebuilt_wheel_serviceability_loss",
        (mechanism, target, old_path, proposed_path_absent),
    )
    applicability = evaluate_candidate_applicability(
        (path,),
        path_model_coverage="sufficient",
    )

    return ArtifactServiceabilityImpactAssessment(
        candidate=candidate,
        applicability=applicability,
        target_evidence=target_evidence,
    )


def _target_compatibility_proposition(
    target_evidence: TargetWheelCompatibilityResult | None,
) -> PropositionAssessment:
    if target_evidence is None:
        return PropositionAssessment(
            key="exact_target_wheel_compatibility_established",
            state="unresolved",
            evidence_coverage="insufficient",
            evidence_owner="target.artifact_environment",
            detail="Exact target wheel-compatibility evidence is not yet available.",
        )

    if isinstance(target_evidence, TargetWheelCompatibilityProblem):
        return PropositionAssessment(
            key="exact_target_wheel_compatibility_established",
            state="unresolved",
            evidence_coverage="insufficient",
            evidence_owner="target.artifact_environment",
            detail=target_evidence.detail,
        )

    return PropositionAssessment(
        key="exact_target_wheel_compatibility_established",
        state="established",
        evidence_coverage="sufficient",
        evidence_owner="target.artifact_environment",
        detail=(
            "Target-owned evidence establishes an exact supported wheel-tag set for the "
            "candidate's target revision."
        ),
    )


def _old_compatible_wheel_proposition(
    candidate: ArtifactServiceabilityImpactCandidate,
    target_evidence: TargetWheelCompatibilityResult | None,
) -> PropositionAssessment:
    if not isinstance(target_evidence, TargetWheelCompatibilityEvidence):
        return PropositionAssessment(
            key="target_had_old_compatible_published_wheel",
            state="unresolved",
            evidence_coverage="insufficient",
            evidence_owner="target.artifact_environment+pypi.release",
            detail=(
                "Old-release wheel compatibility cannot be evaluated until exact target "
                "wheel-tag evidence is established."
            ),
        )

    # Compatibility is an intersection of capabilities: published wheel tags on one
    # side, target-supported tags on the other. We do not infer it from Python version
    # or platform strings independently.
    matches = _published_tags(candidate.old_wheels) & target_evidence.supported_tags
    if matches:
        return PropositionAssessment(
            key="target_had_old_compatible_published_wheel",
            state="established",
            evidence_coverage="sufficient",
            evidence_owner="target.artifact_environment+pypi.release",
            detail=(
                "The old release publishes at least one wheel tag supported by the exact "
                f"target environment: {_format_tags(matches)}."
            ),
        )

    return PropositionAssessment(
        key="target_had_old_compatible_published_wheel",
        state="refuted",
        evidence_coverage="sufficient",
        evidence_owner="target.artifact_environment+pypi.release",
        detail=(
            "No old-release published wheel tag intersects the exact target-supported "
            "wheel-tag set."
        ),
    )


def _proposed_compatible_wheel_absence_proposition(
    candidate: ArtifactServiceabilityImpactCandidate,
    target_evidence: TargetWheelCompatibilityResult | None,
) -> PropositionAssessment:
    if not isinstance(target_evidence, TargetWheelCompatibilityEvidence):
        return PropositionAssessment(
            key="target_lacks_proposed_compatible_published_wheel",
            state="unresolved",
            evidence_coverage="insufficient",
            evidence_owner="target.artifact_environment+pypi.release",
            detail=(
                "Proposed-release wheel compatibility cannot be evaluated until exact "
                "target wheel-tag evidence is established."
            ),
        )

    proposed_matches = (
        _published_tags(candidate.proposed_wheels) & target_evidence.supported_tags
    )
    if proposed_matches:
        return PropositionAssessment(
            key="target_lacks_proposed_compatible_published_wheel",
            state="refuted",
            evidence_coverage="sufficient",
            evidence_owner="target.artifact_environment+pypi.release",
            detail=(
                "The proposed release still publishes a wheel compatible with the exact "
                f"target environment: {_format_tags(proposed_matches)}."
            ),
        )

    return PropositionAssessment(
        key="target_lacks_proposed_compatible_published_wheel",
        state="established",
        evidence_coverage="sufficient",
        evidence_owner="target.artifact_environment+pypi.release",
        detail=(
            "The exact target environment has no compatible proposed-release published "
            "wheel under the established wheel-tag evidence."
        ),
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
            # Interpret published evidence rather than linting compressed-tag ordering.
            # ``validate_order`` is intentionally left at its default False: ordering
            # does not change the compatibility Tag set this responsibility consumes.
            parsed_name, parsed_version, _build, tags = parse_wheel_filename(
                distribution.filename,
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


def _published_tags(wheels: tuple[PublishedWheelArtifact, ...]) -> frozenset[Tag]:
    return frozenset(tag for wheel in wheels for tag in wheel.tags)


def _format_tags(tags: frozenset[Tag]) -> str:
    return ", ".join(sorted(str(tag) for tag in tags))


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
    "ArtifactServiceabilityImpactAssessment",
    "ArtifactServiceabilityImpactCandidate",
    "PublishedWheelArtifact",
    "TargetWheelCompatibilityEvidence",
    "TargetWheelCompatibilityProblem",
    "TargetWheelCompatibilityProblemState",
    "TargetWheelCompatibilityResult",
    "build_artifact_serviceability_impact_candidate",
    "evaluate_artifact_serviceability_impact",
)
