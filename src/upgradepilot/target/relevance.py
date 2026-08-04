"""Map a grounded Python support drop to the target's declared Python range.

This pure boundary consumes already-trusted upstream and target evidence. ``relevance``
means only whether the dropped Python major/minor line intersects the target project's
exact-head ``[project].requires-python`` declaration; it does not mean compatibility,
safety, merge readiness, or a maintainer recommendation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..upstream.claim import (
    GroundedPythonSupportDropClaim,
    UpstreamSupportDropClaimProblem,
    UpstreamSupportDropClaimResult,
)
from .python import (
    TargetPythonDeclaration,
    TargetPythonDeclarationProblem,
    TargetPythonEvidence,
)
from .python_specifier import (
    PythonLineSpecifierEvaluation,
    PythonLineSpecifierMethodResult,
    PythonLineSpecifierProblem,
    evaluate_python_line_specifier,
)

type TargetPythonRelevanceState = Literal[
    "declared_python_overlap",
    "outside_declared_python_range",
    "target_declaration_unresolved",
    "upstream_claim_unresolved",
    "comparison_unsupported",
]


@dataclass(frozen=True, slots=True)
class TargetPythonRelevanceResult:
    """One bounded answer with the exact evidence and method result that produced it."""

    state: TargetPythonRelevanceState
    upstream_result: UpstreamSupportDropClaimResult
    target_evidence: TargetPythonEvidence | None
    specifier_result: PythonLineSpecifierMethodResult | None
    detail: str


def evaluate_target_python_relevance(
    upstream_result: UpstreamSupportDropClaimResult,
    target_evidence: TargetPythonEvidence | None,
) -> TargetPythonRelevanceResult:
    """Evaluate whether one dropped Python line overlaps the target declaration."""

    if not isinstance(
        upstream_result,
        (GroundedPythonSupportDropClaim, UpstreamSupportDropClaimProblem),
    ):
        raise TypeError(
            "upstream_result must be a grounded support-drop claim or its problem result."
        )

    if target_evidence is not None and not isinstance(
        target_evidence,
        (TargetPythonDeclaration, TargetPythonDeclarationProblem),
    ):
        raise TypeError(
            "target_evidence must be target Python evidence or None before activation."
        )

    if isinstance(upstream_result, UpstreamSupportDropClaimProblem):
        if target_evidence is not None:
            raise ValueError(
                "target_evidence must be None when the upstream support-drop claim "
                "is unresolved."
            )
        return TargetPythonRelevanceResult(
            state="upstream_claim_unresolved",
            upstream_result=upstream_result,
            target_evidence=None,
            specifier_result=None,
            detail=(
                "No grounded upstream Python support-drop claim was available, so "
                "target Python comparison was not activated."
            ),
        )

    if target_evidence is None:
        raise ValueError(
            "target_evidence is required after a grounded upstream support-drop claim."
        )

    if isinstance(target_evidence, TargetPythonDeclarationProblem):
        return TargetPythonRelevanceResult(
            state="target_declaration_unresolved",
            upstream_result=upstream_result,
            target_evidence=target_evidence,
            specifier_result=None,
            detail=(
                "The grounded support drop activated target-Python comparison, but "
                f"the target declaration remained unresolved: {target_evidence.detail}"
            ),
        )

    specifier_result = evaluate_python_line_specifier(
        upstream_result.python_line,
        target_evidence.requires_python,
    )

    if isinstance(specifier_result, PythonLineSpecifierProblem):
        return _result_from_specifier_problem(
            upstream_result,
            target_evidence,
            specifier_result,
        )

    assert isinstance(specifier_result, PythonLineSpecifierEvaluation)
    if specifier_result.contains_stable_release:
        assert specifier_result.witness_version is not None
        return TargetPythonRelevanceResult(
            state="declared_python_overlap",
            upstream_result=upstream_result,
            target_evidence=target_evidence,
            specifier_result=specifier_result,
            detail=(
                f"The target declaration admits stable Python "
                f"{specifier_result.witness_version}, which belongs to the dropped "
                f"Python {upstream_result.python_line} line."
            ),
        )

    return TargetPythonRelevanceResult(
        state="outside_declared_python_range",
        upstream_result=upstream_result,
        target_evidence=target_evidence,
        specifier_result=specifier_result,
        detail=(
            f"The target declaration admits no stable Python "
            f"{upstream_result.python_line}.Z version under the accepted method."
        ),
    )


def _result_from_specifier_problem(
    upstream_claim: GroundedPythonSupportDropClaim,
    target_declaration: TargetPythonDeclaration,
    problem: PythonLineSpecifierProblem,
) -> TargetPythonRelevanceResult:
    if problem.state == "invalid_python_line":
        state: TargetPythonRelevanceState = "upstream_claim_unresolved"
    elif problem.state in {
        "invalid_requires_python_specifier",
        "unsatisfiable_requires_python_specifier",
    }:
        state = "target_declaration_unresolved"
    else:
        assert problem.state == "unsupported_requires_python_specifier"
        state = "comparison_unsupported"

    return TargetPythonRelevanceResult(
        state=state,
        upstream_result=upstream_claim,
        target_evidence=target_declaration,
        specifier_result=problem,
        detail=problem.detail,
    )


__all__ = (
    "TargetPythonRelevanceResult",
    "TargetPythonRelevanceState",
    "evaluate_target_python_relevance",
)
