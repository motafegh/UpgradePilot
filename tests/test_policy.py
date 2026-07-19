from __future__ import annotations

import unittest

from upgradepilot.domain.models import (
    ActionClass,
    DecisionEffect,
    EvidenceItem,
    EvidenceState,
    SourceReference,
)
from upgradepilot.domain.policy import decide


SOURCE = SourceReference(
    locator="https://example.test/evidence",
    retrieved_at="2026-07-19T12:00:00+00:00",
    revision="abc123",
)


def evidence_item(
    evidence_id: str,
    *,
    state: EvidenceState = EvidenceState.OBSERVED,
    effect: DecisionEffect = DecisionEffect.NEUTRAL,
    material: bool = True,
    suggested_check: str | None = None,
) -> EvidenceItem:
    source = SOURCE if state in {
        EvidenceState.OBSERVED,
        EvidenceState.INFERRED,
        EvidenceState.ACCEPTED,
        EvidenceState.REJECTED,
    } else None
    return EvidenceItem(
        evidence_id=evidence_id,
        claim=f"Claim for {evidence_id}",
        state=state,
        decision_effect=effect,
        material=material,
        interpretation=f"Interpretation for {evidence_id}",
        source=source,
        suggested_check=suggested_check,
    )


class DecisionPolicyTests(unittest.TestCase):
    def test_observed_block_signal_has_highest_precedence(self) -> None:
        decision = decide(
            (
                evidence_item("conflict", state=EvidenceState.CONFLICTING),
                evidence_item("block", effect=DecisionEffect.BLOCK),
            )
        )

        self.assertEqual(decision.action, ActionClass.INVESTIGATE_OR_BLOCK)
        self.assertEqual(decision.triggering_evidence_ids, ("block",))

    def test_observed_defer_signal_selects_defer(self) -> None:
        decision = decide((evidence_item("policy", effect=DecisionEffect.DEFER),))

        self.assertEqual(decision.action, ActionClass.DEFER)

    def test_conflicting_material_evidence_selects_abstain(self) -> None:
        decision = decide(
            (
                evidence_item("conflict", state=EvidenceState.CONFLICTING),
                evidence_item(
                    "check",
                    effect=DecisionEffect.TARGETED_CHECK,
                    suggested_check="Run one check.",
                ),
            )
        )

        self.assertEqual(decision.action, ActionClass.ABSTAIN)
        self.assertEqual(decision.triggering_evidence_ids, ("conflict",))

    def test_missing_material_evidence_selects_targeted_checks(self) -> None:
        decision = decide(
            (
                evidence_item(
                    "missing",
                    state=EvidenceState.MISSING,
                    effect=DecisionEffect.TARGETED_CHECK,
                    suggested_check="Retrieve the missing source.",
                ),
            )
        )

        self.assertEqual(decision.action, ActionClass.RUN_TARGETED_CHECKS)
        self.assertEqual(decision.targeted_checks, ("Retrieve the missing source.",))

    def test_no_material_evidence_selects_abstain(self) -> None:
        decision = decide((evidence_item("context", material=False),))

        self.assertEqual(decision.action, ActionClass.ABSTAIN)

    def test_supported_neutral_evidence_selects_normal_review(self) -> None:
        decision = decide((evidence_item("diff"),))

        self.assertEqual(decision.action, ActionClass.MERGE_AFTER_NORMAL_REVIEW)

    def test_rejected_material_evidence_requires_a_check(self) -> None:
        decision = decide((evidence_item("rejected", state=EvidenceState.REJECTED),))

        self.assertEqual(decision.action, ActionClass.RUN_TARGETED_CHECKS)
        self.assertEqual(decision.targeted_checks, ("Resolve evidence: Claim for rejected",))


if __name__ == "__main__":
    unittest.main()
