"""Deterministic maintainer-action synthesis at the currently admitted proof boundary.

The first evaluator deliberately admits only explained abstention.  Mechanism-specific
technical results remain owned by ``PublicPullRequestInvestigation`` and their domain
modules; this layer does not reinterpret an applicability result into maintainer policy.
Non-abstention actions are added only after their positive permission is proven through
the normal producer path required by the accepted synthesis specification.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .dependency.change import DependencyChangeProblem
from .investigation import PublicPullRequestInvestigation


type MaintainerAction = Literal["abstain"]


@dataclass(frozen=True, slots=True)
class MaintainerActionSynthesis:
    """First bounded synthesis result for one exact public pull-request investigation.

    ``source_investigation`` retains the complete typed evidence/provenance boundary
    without duplicating mechanism-specific fields into a second authority surface.
    The categorized text fields preserve why the current action is justified, what
    remains unresolved, the evaluator's admitted limitations, and explicit claim limits.
    """

    source_investigation: PublicPullRequestInvestigation
    action: MaintainerAction
    decisive_reasons: tuple[str, ...]
    residual_uncertainty: tuple[str, ...]
    limitations: tuple[str, ...]
    claim_limits: tuple[str, ...]

    def __post_init__(self) -> None:
        if self.action != "abstain":
            raise ValueError("the first admitted synthesis evaluator supports only abstain")
        if not self.decisive_reasons:
            raise ValueError("maintainer-action synthesis requires a decisive reason")
        if not self.limitations:
            raise ValueError("maintainer-action synthesis requires its admitted limitations")
        if not self.claim_limits:
            raise ValueError("maintainer-action synthesis requires explicit claim limits")
        for field_name, values in (
            ("decisive_reasons", self.decisive_reasons),
            ("residual_uncertainty", self.residual_uncertainty),
            ("limitations", self.limitations),
            ("claim_limits", self.claim_limits),
        ):
            if not isinstance(values, tuple):
                raise TypeError(f"{field_name} must be a tuple")
            if any(not isinstance(value, str) or not value.strip() for value in values):
                raise ValueError(f"{field_name} entries must be non-empty text")


def synthesize_maintainer_action(
    investigation: PublicPullRequestInvestigation,
) -> MaintainerActionSynthesis:
    """Return the strongest action admitted by the first deterministic evaluator.

    No non-abstention permission has yet passed its action-specific normal-producer proof
    gate.  This function therefore does not inspect a technical result and guess a more
    active action from it.  It preserves material non-final states for explanation while
    explicitly stating the current evaluator boundary.
    """

    if not isinstance(investigation, PublicPullRequestInvestigation):
        raise TypeError("investigation must be PublicPullRequestInvestigation")

    decisive_reasons: list[str] = []
    if isinstance(investigation.dependency_result, DependencyChangeProblem):
        decisive_reasons.append(
            "The investigation did not establish one supported dependency transition: "
            f"{investigation.dependency_result.reason}."
        )

    decisive_reasons.append(
        "No non-abstention maintainer-action permission is admitted at the current "
        "evaluator proof boundary."
    )

    return MaintainerActionSynthesis(
        source_investigation=investigation,
        action="abstain",
        decisive_reasons=tuple(decisive_reasons),
        residual_uncertainty=_material_residual_uncertainty(investigation),
        limitations=(
            "This first evaluator intentionally withholds merge, targeted-check, "
            "investigate, block, and defer until each action's positive prerequisites "
            "are proven through the normal producer path.",
        ),
        claim_limits=(
            "This abstention is not a finding that the dependency update is safe or unsafe.",
            "This result does not establish complete impact-candidate or repository-context coverage.",
            "This result does not authorize repository mutation, approval, or automatic merge.",
        ),
    )


def _material_residual_uncertainty(
    investigation: PublicPullRequestInvestigation,
) -> tuple[str, ...]:
    uncertainty: list[str] = []

    dependency = investigation.dependency_result
    if isinstance(dependency, DependencyChangeProblem):
        uncertainty.append(
            "Dependency transition remains unsupported/unresolved at the admitted "
            f"dependency-analysis boundary: {dependency.detail}"
        )

    ci = investigation.ci_coverage_result
    if ci is not None and ci.state not in {
        "supported_not_correlated",
        "supported_runtime_correlated",
    }:
        uncertainty.append(
            f"CI dependency coverage remains {ci.state}: {ci.detail}"
        )

    python_impact = investigation.python_support_drop_impact_result
    if python_impact is not None and python_impact.applicability.state in {
        "unresolved",
        "conflicted",
    }:
        uncertainty.append(
            "Python-support-drop applicability remains "
            f"{python_impact.applicability.state}: {python_impact.applicability.detail}"
        )

    artifact_impact = investigation.artifact_serviceability_impact_result
    if artifact_impact is not None and artifact_impact.applicability.state in {
        "unresolved",
        "conflicted",
    }:
        uncertainty.append(
            "Artifact-serviceability applicability remains "
            f"{artifact_impact.applicability.state}: {artifact_impact.applicability.detail}"
        )

    return tuple(uncertainty)


__all__ = (
    "MaintainerAction",
    "MaintainerActionSynthesis",
    "synthesize_maintainer_action",
)
