from __future__ import annotations

from collections.abc import Callable
from datetime import datetime, timezone

from upgradepilot.domain.models import AnalysisInput, DecisionReport
from upgradepilot.domain.policy import POLICY_VERSION, decide


CLAIM_BOUNDARY = (
    "This report supports a bounded maintainer decision from the supplied evidence. "
    "It does not prove compatibility, security, absence of regressions, or maintainer intent."
)


def analyze(
    analysis_input: AnalysisInput,
    *,
    clock: Callable[[], datetime] | None = None,
) -> DecisionReport:
    now = (clock or _utc_now)()
    if now.tzinfo is None:
        raise ValueError("analysis clock must return a timezone-aware datetime")

    decision = decide(analysis_input.evidence)
    return DecisionReport(
        schema_version=analysis_input.schema_version,
        policy_version=POLICY_VERSION,
        generated_at=now.isoformat(),
        case=analysis_input.case,
        evidence=analysis_input.evidence,
        action=decision.action,
        reason=decision.reason,
        triggering_evidence_ids=decision.triggering_evidence_ids,
        targeted_checks=decision.targeted_checks,
        uncertainties=decision.uncertainties,
        limitations=analysis_input.limitations,
        claim_boundary=CLAIM_BOUNDARY,
    )


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)
