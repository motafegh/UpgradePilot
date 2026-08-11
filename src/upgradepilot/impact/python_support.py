"""Model one bounded Python-support impact candidate and its applicability.

This module sits above the existing upstream and target evidence boundaries. It does not
acquire evidence, discover every possible impact, choose investigations, or produce a
maintainer recommendation. Its negative conclusion is scoped only to the represented
Python-support-drop candidate family.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

from ..dependency.change import DependencyVersionChange
from ..github.pull_request import PullRequestIdentity
from ..target.python import TargetPythonDeclaration, TargetPythonDeclarationProblem
from ..target.relevance import TargetPythonRelevanceResult
from ..upstream.claim import GroundedPythonSupportDropClaim
from ..upstream.interval import release_interval_from_dependency_change

type ApplicabilityPropositionState = Literal[
    "established",
    "refuted",
    "unresolved",
    "conflicted",
]
type PythonSupportApplicabilityState = Literal[
    "established_applicable",
    "established_not_applicable",
    "unresolved",
    "conflicted",
]
type PythonSupportPropositionKind = Literal[
    "upstream_support_drop",
    "target_python_declaration",
    "declared_python_intersection",
]


@dataclass(frozen=True, slots=True)
class PythonSupportDropImpactCandidate:
    """One mechanism-specific concern proposed from already-grounded upstream evidence.

    The relation, activation, and consequence fields name the bounded hypothesis being
    evaluated. They do not establish target exposure or applicability by themselves.
    """

    pull_request: PullRequestIdentity
    dependency: DependencyVersionChange
    upstream_claim: GroundedPythonSupportDropClaim
    mechanism: Literal["python_support_drop"] = field(
        init=False,
        default="python_support_drop",
    )
    exposure_hypothesis: Literal["target_declared_python_range"] = field(
        init=False,
        default="target_declared_python_range",
    )
    activation_hypothesis: Literal["dropped_python_line_intersects_declared_range"] = (
        field(
            init=False,
            default="dropped_python_line_intersects_declared_range",
        )
    )
    possible_consequence: Literal[
        "dependency_may_not_support_part_of_declared_python_range"
    ] = field(
        init=False,
        default="dependency_may_not_support_part_of_declared_python_range",
    )


@dataclass(frozen=True, slots=True)
class ApplicabilityPropositionAssessment:
    """Explicit B-level state for one proposition needed by the bounded candidate."""

    kind: PythonSupportPropositionKind
    state: ApplicabilityPropositionState
    detail: str


@dataclass(frozen=True, slots=True)
class PythonSupportApplicabilityAssessment:
    """Candidate-specific applicability with the exact lower-level evidence preserved."""

    candidate: PythonSupportDropImpactCandidate
    state: PythonSupportApplicabilityState
    propositions: tuple[ApplicabilityPropositionAssessment, ...]
    target_relevance: TargetPythonRelevanceResult
    path_model_coverage: Literal["sufficient"]
    detail: str


def build_python_support_drop_candidate(
    pull_request: PullRequestIdentity,
    dependency: DependencyVersionChange,
    upstream_claim: GroundedPythonSupportDropClaim,
) -> PythonSupportDropImpactCandidate:
    """Create A only after trusted PR, dependency, and grounded mechanism identities align."""

    if not isinstance(pull_request, PullRequestIdentity):
        raise TypeError("pull_request must be PullRequestIdentity.")
    if not isinstance(dependency, DependencyVersionChange):
        raise TypeError("dependency must be DependencyVersionChange.")
    if not isinstance(upstream_claim, GroundedPythonSupportDropClaim):
        raise TypeError("upstream_claim must be GroundedPythonSupportDropClaim.")

    expected_interval = release_interval_from_dependency_change(dependency)
    if upstream_claim.interval != expected_interval:
        raise ValueError(
            "The grounded support-drop claim does not match the trusted dependency "
            "version transition."
        )

    for source in dependency.source_evidence:
        if (
            source.base_revision is not None
            and source.base_revision != pull_request.base_sha
        ):
            raise ValueError(
                "Dependency source evidence base revision does not match the pull request."
            )
        if (
            source.head_revision is not None
            and source.head_revision != pull_request.head_sha
        ):
            raise ValueError(
                "Dependency source evidence head revision does not match the pull request."
            )

    return PythonSupportDropImpactCandidate(
        pull_request=pull_request,
        dependency=dependency,
        upstream_claim=upstream_claim,
    )


def assess_python_support_applicability(
    candidate: PythonSupportDropImpactCandidate,
    target_relevance: TargetPythonRelevanceResult,
) -> PythonSupportApplicabilityAssessment:
    """Translate existing target-Python evidence into explicit candidate propositions."""

    if not isinstance(candidate, PythonSupportDropImpactCandidate):
        raise TypeError("candidate must be PythonSupportDropImpactCandidate.")
    if not isinstance(target_relevance, TargetPythonRelevanceResult):
        raise TypeError("target_relevance must be TargetPythonRelevanceResult.")
    if target_relevance.upstream_result != candidate.upstream_claim:
        raise ValueError(
            "Target relevance was not evaluated from the candidate's grounded "
            "support-drop claim."
        )

    target_evidence = target_relevance.target_evidence
    if (
        target_evidence is not None
        and target_evidence.revision != candidate.pull_request.head_sha
    ):
        raise ValueError(
            "Target Python evidence revision does not match the candidate pull-request head."
        )

    upstream = ApplicabilityPropositionAssessment(
        kind="upstream_support_drop",
        state="established",
        detail=(
            f"Authoritative upstream evidence grounds a Python "
            f"{candidate.upstream_claim.python_line} support drop inside the trusted "
            "dependency transition."
        ),
    )

    if target_relevance.state == "declared_python_overlap":
        assert isinstance(target_evidence, TargetPythonDeclaration)
        target = _target_declaration_established(target_evidence)
        activation = ApplicabilityPropositionAssessment(
            kind="declared_python_intersection",
            state="established",
            detail=target_relevance.detail,
        )
        return _assessment(
            candidate,
            target_relevance,
            state="established_applicable",
            propositions=(upstream, target, activation),
            detail=(
                "The represented declared-Python-range path is established for this "
                "Python-support-drop candidate."
            ),
        )

    if target_relevance.state == "outside_declared_python_range":
        assert isinstance(target_evidence, TargetPythonDeclaration)
        target = _target_declaration_established(target_evidence)
        activation = ApplicabilityPropositionAssessment(
            kind="declared_python_intersection",
            state="refuted",
            detail=target_relevance.detail,
        )
        return _assessment(
            candidate,
            target_relevance,
            state="established_not_applicable",
            propositions=(upstream, target, activation),
            detail=(
                "The only represented path for this bounded candidate family is "
                "refuted by the exact target declaration. This does not establish that "
                "the dependency update has no other material impact."
            ),
        )

    if target_relevance.state == "target_declaration_unresolved":
        assert isinstance(target_evidence, TargetPythonDeclarationProblem)
        target = ApplicabilityPropositionAssessment(
            kind="target_python_declaration",
            state="unresolved",
            detail=target_evidence.detail,
        )
        activation = ApplicabilityPropositionAssessment(
            kind="declared_python_intersection",
            state="unresolved",
            detail=(
                "The intersection proposition cannot be established or refuted until "
                "the exact target Python declaration is resolved."
            ),
        )
        return _assessment(
            candidate,
            target_relevance,
            state="unresolved",
            propositions=(upstream, target, activation),
            detail=(
                "Missing or unusable target declaration evidence remains unresolved; "
                "it is not treated as evidence of non-applicability."
            ),
        )

    if target_relevance.state == "comparison_unsupported":
        assert isinstance(target_evidence, TargetPythonDeclaration)
        target = _target_declaration_established(target_evidence)
        activation = ApplicabilityPropositionAssessment(
            kind="declared_python_intersection",
            state="unresolved",
            detail=target_relevance.detail,
        )
        return _assessment(
            candidate,
            target_relevance,
            state="unresolved",
            propositions=(upstream, target, activation),
            detail=(
                "The exact target declaration is established, but the admitted "
                "deterministic comparison method cannot resolve the activation relation."
            ),
        )

    assert target_relevance.state == "upstream_claim_unresolved"
    raise ValueError(
        "A grounded impact candidate cannot be assessed from an upstream-unresolved "
        "target-relevance result."
    )


def _target_declaration_established(
    target: TargetPythonDeclaration,
) -> ApplicabilityPropositionAssessment:
    return ApplicabilityPropositionAssessment(
        kind="target_python_declaration",
        state="established",
        detail=(
            f"The exact target declaration at {target.revision} establishes "
            f"requires-python={target.requires_python!r}."
        ),
    )


def _assessment(
    candidate: PythonSupportDropImpactCandidate,
    target_relevance: TargetPythonRelevanceResult,
    *,
    state: PythonSupportApplicabilityState,
    propositions: tuple[ApplicabilityPropositionAssessment, ...],
    detail: str,
) -> PythonSupportApplicabilityAssessment:
    return PythonSupportApplicabilityAssessment(
        candidate=candidate,
        state=state,
        propositions=propositions,
        target_relevance=target_relevance,
        path_model_coverage="sufficient",
        detail=detail,
    )


__all__ = (
    "ApplicabilityPropositionAssessment",
    "ApplicabilityPropositionState",
    "PythonSupportApplicabilityAssessment",
    "PythonSupportApplicabilityState",
    "PythonSupportDropImpactCandidate",
    "PythonSupportPropositionKind",
    "assess_python_support_applicability",
    "build_python_support_drop_candidate",
)
