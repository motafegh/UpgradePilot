"""Deterministic candidate-applicability composition for the first A→B slice.

This module models only the bounded semantics required by the approved B2 plan:
proposition state, proposition evidence coverage, conjunctive applicability paths,
path-model coverage, and candidate-level applicability. It intentionally does not
model candidate-discovery completeness, final maintainer action, numerical scoring,
or a generic Boolean/rule engine.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


type PropositionState = Literal["established", "refuted", "unresolved", "conflicted"]
type EvidenceCoverageState = Literal["sufficient", "insufficient", "unresolved"]
type ApplicabilityPathState = PropositionState
type PathModelCoverageState = Literal["sufficient", "insufficient", "unresolved"]
type CandidateApplicabilityState = Literal[
    "established_applicable",
    "established_not_applicable",
    "unresolved",
    "conflicted",
]


@dataclass(frozen=True, slots=True)
class PropositionAssessment:
    """Assessment of one candidate-specific proposition and its evidence coverage."""

    key: str
    state: PropositionState
    evidence_coverage: EvidenceCoverageState
    evidence_owner: str
    detail: str


@dataclass(frozen=True, slots=True)
class ApplicabilityPathAssessment:
    """Deterministic result for one represented conjunctive applicability path."""

    key: str
    state: ApplicabilityPathState
    propositions: tuple[PropositionAssessment, ...]
    detail: str


@dataclass(frozen=True, slots=True)
class CandidateApplicabilityAssessment:
    """Candidate-level applicability while preserving path-level reasoning state."""

    state: CandidateApplicabilityState
    paths: tuple[ApplicabilityPathAssessment, ...]
    path_model_coverage: PathModelCoverageState
    detail: str


def evaluate_applicability_path(
    key: str,
    propositions: tuple[PropositionAssessment, ...],
) -> ApplicabilityPathAssessment:
    """Compose necessary propositions for one path without a general rule engine."""

    if not key.strip():
        raise ValueError("applicability path key must be non-empty.")
    if not propositions:
        raise ValueError("an applicability path requires at least one proposition.")

    states = {proposition.state for proposition in propositions}

    # One refuted necessary proposition is enough to eliminate this conjunctive path,
    # even if another proposition on the same path remains unresolved or conflicted.
    if "refuted" in states:
        state: ApplicabilityPathState = "refuted"
        detail = "At least one necessary proposition is refuted, so this path is eliminated."
    elif states == {"established"}:
        state = "established"
        detail = "Every necessary proposition is established, so this path is established."
    elif "conflicted" in states:
        state = "conflicted"
        detail = (
            "No necessary proposition is refuted, but at least one remains genuinely "
            "conflicted, so this path is conflicted."
        )
    else:
        state = "unresolved"
        detail = (
            "No necessary proposition is refuted, but at least one remains unresolved, "
            "so this path is unresolved."
        )

    return ApplicabilityPathAssessment(
        key=key,
        state=state,
        propositions=propositions,
        detail=detail,
    )


def evaluate_candidate_applicability(
    paths: tuple[ApplicabilityPathAssessment, ...],
    *,
    path_model_coverage: PathModelCoverageState,
) -> CandidateApplicabilityAssessment:
    """Compose represented alternative paths into one bounded candidate state.

    The returned scalar state is intentionally accompanied by the complete path results.
    In particular, all represented paths being refuted is not enough for an unqualified
    ``established_not_applicable`` result unless path-model coverage is sufficient.
    """

    if not paths:
        raise ValueError("candidate applicability requires at least one represented path.")

    if any(path.state == "established" for path in paths):
        return CandidateApplicabilityAssessment(
            state="established_applicable",
            paths=paths,
            path_model_coverage=path_model_coverage,
            detail=(
                "At least one complete represented applicability path is established; "
                "other unresolved or conflicted alternatives are not required to establish "
                "candidate applicability."
            ),
        )

    if all(path.state == "refuted" for path in paths):
        if path_model_coverage == "sufficient":
            return CandidateApplicabilityAssessment(
                state="established_not_applicable",
                paths=paths,
                path_model_coverage=path_model_coverage,
                detail=(
                    "Every represented applicability path is refuted and path-model "
                    "coverage is sufficient for this bounded candidate."
                ),
            )
        return CandidateApplicabilityAssessment(
            state="unresolved",
            paths=paths,
            path_model_coverage=path_model_coverage,
            detail=(
                "Every represented path is refuted, but path-model coverage is not "
                "sufficient; preserve the refutations without claiming candidate-level "
                "non-applicability."
            ),
        )

    if any(path.state == "conflicted" for path in paths):
        return CandidateApplicabilityAssessment(
            state="conflicted",
            paths=paths,
            path_model_coverage=path_model_coverage,
            detail=(
                "No represented path is established and at least one viable alternative "
                "remains genuinely conflicted; path-level unresolved alternatives are "
                "preserved in the result."
            ),
        )

    return CandidateApplicabilityAssessment(
        state="unresolved",
        paths=paths,
        path_model_coverage=path_model_coverage,
        detail=(
            "No represented path is established or genuinely conflicted, and at least "
            "one viable alternative remains unresolved."
        ),
    )


__all__ = (
    "ApplicabilityPathAssessment",
    "ApplicabilityPathState",
    "CandidateApplicabilityAssessment",
    "CandidateApplicabilityState",
    "EvidenceCoverageState",
    "PathModelCoverageState",
    "PropositionAssessment",
    "PropositionState",
    "evaluate_applicability_path",
    "evaluate_candidate_applicability",
)
