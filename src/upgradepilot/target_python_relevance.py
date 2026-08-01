"""Map a grounded Python support drop to the target's declared Python range.

Data flow
---------
This module is the pure Step 4 boundary between already-trusted evidence and the
bounded PEP 440 method from :mod:`upgradepilot.packaging_method`::

    UpstreamSupportDropClaimResult
    ├── unresolved problem
    │   └── upstream_claim_unresolved
    │
    └── GroundedPythonSupportDropClaim
        + TargetPythonEvidence
          ├── target problem
          │   └── target_declaration_unresolved
          │
          └── TargetPythonDeclaration
              └── evaluate_python_line_specifier(...)
                  ├── stable X.Y.Z exists  -> declared_python_overlap
                  ├── no stable X.Y.Z      -> outside_declared_python_range
                  └── method problem       -> bounded unresolved/unsupported state

The word ``relevance`` is deliberately narrow here: it asks only whether the Python
major/minor line dropped upstream intersects the target project's exact-head
``[project].requires-python`` declaration. It does not mean compatibility, safety,
merge readiness, or a maintainer recommendation.

Responsibility boundary
-----------------------
Step 2 already owns source grounding for ``GroundedPythonSupportDropClaim`` and
``target_python.py`` already owns exact-head ``pyproject.toml`` interpretation. This
module preserves those records rather than re-grounding quotes or re-parsing TOML.
That keeps one validation owner for each fact and makes failures easier to diagnose.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .packaging_method import (
    PythonLineSpecifierEvaluation,
    PythonLineSpecifierMethodResult,
    PythonLineSpecifierProblem,
    evaluate_python_line_specifier,
)
from .target_python import (
    TargetPythonDeclaration,
    TargetPythonDeclarationProblem,
    TargetPythonEvidence,
)
from .upstream_claim import (
    GroundedPythonSupportDropClaim,
    UpstreamSupportDropClaimProblem,
    UpstreamSupportDropClaimResult,
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
    """One bounded answer with the exact evidence and method result that produced it.

    Keeping the original nested records avoids copying package/version identities,
    target file provenance, or the PEP 440 witness into another representation that
    could later drift from its owning contract.
    """

    state: TargetPythonRelevanceState
    upstream_result: UpstreamSupportDropClaimResult
    target_evidence: TargetPythonEvidence | None
    specifier_result: PythonLineSpecifierMethodResult | None
    detail: str


def evaluate_target_python_relevance(
    upstream_result: UpstreamSupportDropClaimResult,
    target_evidence: TargetPythonEvidence | None,
) -> TargetPythonRelevanceResult:
    """Evaluate whether one dropped Python line overlaps the target declaration.

    ``target_evidence`` is intentionally optional only because an unresolved upstream
    claim must stop the data flow *before* target-Python evidence is admitted. Once a
    grounded claim exists, one target evidence result is required.

    Caller sequencing mistakes raise ``ValueError``. Ordinary evidence/method failures
    return one of the explicit product states instead of raising.
    """

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
        # This early stop is an authority rule, not merely an optimization: target
        # Python relevance is not activated until Step 2 produced one grounded claim.
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
    """Translate a Step 3 method problem according to which boundary owns it.

    The mapping is deliberately explicit:

    - invalid Python line -> upstream claim could not be trusted for comparison;
    - invalid/contradictory target specifier -> target declaration is unresolved;
    - valid-but-out-of-scope specifier form -> comparison method is unsupported.
    """

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
