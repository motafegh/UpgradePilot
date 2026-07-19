from __future__ import annotations

from upgradepilot.domain.models import (
    ActionClass,
    DecisionEffect,
    EvidenceItem,
    EvidenceState,
    PolicyDecision,
)


POLICY_VERSION = "bootstrap-1"

_SUPPORTED_FACT_STATES = {EvidenceState.OBSERVED, EvidenceState.ACCEPTED}
_ABSTAIN_STATES = {EvidenceState.CONFLICTING, EvidenceState.INVALID}
_CHECK_STATES = {
    EvidenceState.INFERRED,
    EvidenceState.MISSING,
    EvidenceState.INACCESSIBLE,
    EvidenceState.STALE,
    EvidenceState.REJECTED,
}


def decide(evidence: tuple[EvidenceItem, ...]) -> PolicyDecision:
    material = tuple(item for item in evidence if item.material)

    blocking = tuple(
        item
        for item in material
        if item.decision_effect is DecisionEffect.BLOCK
        and item.state in _SUPPORTED_FACT_STATES
    )
    if blocking:
        return PolicyDecision(
            action=ActionClass.INVESTIGATE_OR_BLOCK,
            reason="Material observed evidence identifies a blocking risk.",
            triggering_evidence_ids=_ids(blocking),
            targeted_checks=_checks(blocking),
            uncertainties=_uncertainties(material),
        )

    deferrals = tuple(
        item
        for item in material
        if item.decision_effect is DecisionEffect.DEFER
        and item.state in _SUPPORTED_FACT_STATES
    )
    if deferrals:
        return PolicyDecision(
            action=ActionClass.DEFER,
            reason="Material observed evidence supports deferring this update.",
            triggering_evidence_ids=_ids(deferrals),
            targeted_checks=_checks(deferrals),
            uncertainties=_uncertainties(material),
        )

    unusable = tuple(item for item in material if item.state in _ABSTAIN_STATES)
    if unusable:
        return PolicyDecision(
            action=ActionClass.ABSTAIN,
            reason=(
                "Material evidence is conflicting or invalid, "
                "so no defensible action is available."
            ),
            triggering_evidence_ids=_ids(unusable),
            targeted_checks=_checks(unusable),
            uncertainties=_uncertainties(material),
        )

    checks = tuple(
        item
        for item in material
        if item.decision_effect is DecisionEffect.TARGETED_CHECK
        or item.state in _CHECK_STATES
    )
    if checks:
        return PolicyDecision(
            action=ActionClass.RUN_TARGETED_CHECKS,
            reason="Material evidence is incomplete or identifies a proportional check.",
            triggering_evidence_ids=_ids(checks),
            targeted_checks=_checks(checks),
            uncertainties=_uncertainties(material),
        )

    if not material:
        return PolicyDecision(
            action=ActionClass.ABSTAIN,
            reason="No material evidence was supplied.",
            triggering_evidence_ids=(),
            targeted_checks=(),
            uncertainties=("No material evidence was supplied.",),
        )

    return PolicyDecision(
        action=ActionClass.MERGE_AFTER_NORMAL_REVIEW,
        reason="No material blocker or additional-check signal appears in the supplied evidence.",
        triggering_evidence_ids=_ids(material),
        targeted_checks=(),
        uncertainties=_uncertainties(material),
    )


def _ids(items: tuple[EvidenceItem, ...]) -> tuple[str, ...]:
    return tuple(item.evidence_id for item in items)


def _checks(items: tuple[EvidenceItem, ...]) -> tuple[str, ...]:
    return tuple(
        dict.fromkeys(
            (
                item.suggested_check.strip()
                if item.suggested_check is not None and item.suggested_check.strip()
                else f"Resolve evidence: {item.claim}"
            )
            for item in items
        )
    )


def _uncertainties(items: tuple[EvidenceItem, ...]) -> tuple[str, ...]:
    uncertain_states = _ABSTAIN_STATES | _CHECK_STATES
    return tuple(item.claim for item in items if item.state in uncertain_states)
