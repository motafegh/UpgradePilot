"""First mechanism-specific A→B model for upstream Python-support drops.

The candidate is grounded only after an authoritative upstream support-drop claim exists.
Its target exposure and activation remain propositions to evaluate; creating the candidate
does not establish applicability. The bounded B adapter can represent the pre-acquisition
state explicitly and reuses the existing target-Python relevance result once target evidence
has been acquired, avoiding duplicated Python-specifier semantics.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..dependency.change import DependencyVersionChange
from ..github.pull_request import PullRequestIdentity
from ..target.python import TargetPythonDeclaration, TargetPythonDeclarationProblem
from ..target.relevance import TargetPythonRelevanceResult
from ..upstream.claim import GroundedPythonSupportDropClaim
from .applicability import (
    CandidateApplicabilityAssessment,
    PropositionAssessment,
    evaluate_applicability_path,
    evaluate_candidate_applicability,
)


type CandidateComponentStatus = Literal["established", "to_evaluate", "possible"]


@dataclass(frozen=True, slots=True)
class PythonSupportDropImpactCandidate:
    """Bounded A-level candidate for one exact dependency update and target revision."""

    pull_request: PullRequestIdentity
    dependency: DependencyVersionChange
    upstream_claim: GroundedPythonSupportDropClaim
    target_repository: str
    target_revision: str
    mechanism_status: CandidateComponentStatus
    exposure_status: CandidateComponentStatus
    activation_status: CandidateComponentStatus
    consequence_status: CandidateComponentStatus
    exposure_proposition: str
    activation_proposition: str
    possible_consequence: str


@dataclass(frozen=True, slots=True)
class PythonSupportDropImpactAssessment:
    """Candidate applicability before or after exact target-relevance evidence acquisition."""

    candidate: PythonSupportDropImpactCandidate
    applicability: CandidateApplicabilityAssessment
    target_relevance: TargetPythonRelevanceResult | None


def build_python_support_drop_impact_candidate(
    pull_request: PullRequestIdentity,
    dependency: DependencyVersionChange,
    upstream_claim: GroundedPythonSupportDropClaim,
) -> PythonSupportDropImpactCandidate:
    """Create one grounded mechanism candidate without self-authorizing exposure."""

    interval = upstream_claim.interval
    if (
        interval.normalized_package != dependency.normalized_package
        or interval.old_version != dependency.old_version
        or interval.proposed_version != dependency.proposed_version
    ):
        raise ValueError(
            "upstream support-drop claim interval must match the exact dependency transition."
        )

    return PythonSupportDropImpactCandidate(
        pull_request=pull_request,
        dependency=dependency,
        upstream_claim=upstream_claim,
        target_repository=pull_request.repository,
        target_revision=pull_request.head_sha,
        mechanism_status="established",
        exposure_status="to_evaluate",
        activation_status="to_evaluate",
        consequence_status="possible",
        exposure_proposition=(
            "The exact target revision declares an installation Python range relevant "
            "to the upstream support-drop mechanism."
        ),
        activation_proposition=(
            f"The exact target declaration admits at least one stable Python "
            f"{upstream_claim.python_line}.Z version affected by the upstream support drop."
        ),
        possible_consequence=(
            "The proposed dependency may no longer support part of the target's declared "
            "Python installation range."
        ),
    )


def evaluate_python_support_drop_impact(
    candidate: PythonSupportDropImpactCandidate,
    target_relevance: TargetPythonRelevanceResult | None = None,
) -> PythonSupportDropImpactAssessment:
    """Evaluate candidate applicability before or after target evidence acquisition."""

    if target_relevance is not None:
        if target_relevance.upstream_result != candidate.upstream_claim:
            raise ValueError(
                "target relevance must be derived from the candidate's exact upstream claim."
            )

        target_evidence = target_relevance.target_evidence
        if isinstance(
            target_evidence,
            (TargetPythonDeclaration, TargetPythonDeclarationProblem),
        ):
            if target_evidence.revision != candidate.target_revision:
                raise ValueError(
                    "target relevance must refer to the candidate's exact target revision."
                )

    upstream_proposition = PropositionAssessment(
        key="upstream_python_support_drop_crossed",
        state="established",
        evidence_coverage="sufficient",
        evidence_owner="upstream.claim",
        detail=(
            f"Authoritative upstream evidence grounds a Python "
            f"{candidate.upstream_claim.python_line} support drop inside the exact "
            "dependency release interval."
        ),
    )

    target_declaration_proposition = _target_declaration_proposition(target_relevance)
    activation_proposition = _activation_proposition(target_relevance)

    path = evaluate_applicability_path(
        "declared_python_installation_range",
        (
            upstream_proposition,
            target_declaration_proposition,
            activation_proposition,
        ),
    )

    applicability = evaluate_candidate_applicability(
        (path,),
        path_model_coverage="sufficient",
    )

    return PythonSupportDropImpactAssessment(
        candidate=candidate,
        applicability=applicability,
        target_relevance=target_relevance,
    )


def _target_declaration_proposition(
    target_relevance: TargetPythonRelevanceResult | None,
) -> PropositionAssessment:
    if target_relevance is None:
        return PropositionAssessment(
            key="exact_target_python_declaration_established",
            state="unresolved",
            evidence_coverage="insufficient",
            evidence_owner="target.python",
            detail="Exact target Python declaration evidence has not yet been acquired.",
        )

    if target_relevance.state == "target_declaration_unresolved":
        return PropositionAssessment(
            key="exact_target_python_declaration_established",
            state="unresolved",
            evidence_coverage="insufficient",
            evidence_owner="target.python",
            detail=target_relevance.detail,
        )

    if target_relevance.state == "upstream_claim_unresolved":
        raise ValueError(
            "a grounded Python-support-drop candidate cannot consume unresolved upstream state."
        )

    return PropositionAssessment(
        key="exact_target_python_declaration_established",
        state="established",
        evidence_coverage="sufficient",
        evidence_owner="target.python",
        detail="The exact target revision supplied an interpretable Python declaration.",
    )


def _activation_proposition(
    target_relevance: TargetPythonRelevanceResult | None,
) -> PropositionAssessment:
    if target_relevance is None:
        return PropositionAssessment(
            key="declared_python_range_intersects_dropped_line",
            state="unresolved",
            evidence_coverage="insufficient",
            evidence_owner="target.relevance",
            detail=(
                "Activation cannot be evaluated before exact target declaration evidence "
                "has been acquired."
            ),
        )

    if target_relevance.state == "declared_python_overlap":
        return PropositionAssessment(
            key="declared_python_range_intersects_dropped_line",
            state="established",
            evidence_coverage="sufficient",
            evidence_owner="target.relevance",
            detail=target_relevance.detail,
        )

    if target_relevance.state == "outside_declared_python_range":
        return PropositionAssessment(
            key="declared_python_range_intersects_dropped_line",
            state="refuted",
            evidence_coverage="sufficient",
            evidence_owner="target.relevance",
            detail=target_relevance.detail,
        )

    if target_relevance.state == "comparison_unsupported":
        return PropositionAssessment(
            key="declared_python_range_intersects_dropped_line",
            state="unresolved",
            evidence_coverage="sufficient",
            evidence_owner="target.relevance",
            detail=(
                "The exact target declaration was acquired, but the accepted deterministic "
                f"comparison method cannot resolve the activation proposition: {target_relevance.detail}"
            ),
        )

    if target_relevance.state == "target_declaration_unresolved":
        return PropositionAssessment(
            key="declared_python_range_intersects_dropped_line",
            state="unresolved",
            evidence_coverage="insufficient",
            evidence_owner="target.relevance",
            detail=(
                "Activation cannot be resolved until authoritative target declaration "
                "evidence is established."
            ),
        )

    raise ValueError(
        "a grounded Python-support-drop candidate cannot consume unresolved upstream state."
    )


__all__ = (
    "CandidateComponentStatus",
    "PythonSupportDropImpactAssessment",
    "PythonSupportDropImpactCandidate",
    "build_python_support_drop_impact_candidate",
    "evaluate_python_support_drop_impact",
)
