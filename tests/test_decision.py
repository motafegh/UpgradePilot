import json
import unittest

from pydantic import ValidationError

from upgradepilot.case_identity import build_initial_case_record
from upgradepilot.decision import (
    DecisionInput,
    PythonSupportChange,
    evaluate_decision,
)
from upgradepilot.evidence import EvidenceItem, EvidenceSet


BASE_SHA = "652a61ce4f9d7d76eaada31535807a485ece0e21"
HEAD_SHA = "aa2dc024d33f61cdef50bf1973ab5adf0a974f5a"


def _case():
    return build_initial_case_record(
        {
            "repository": "pydantic/pydantic",
            "pr_number": 13432,
            "base_sha": BASE_SHA,
            "head_sha": HEAD_SHA,
            "dependency": "soupsieve",
            "old_version": "2.6",
            "new_version": "2.8.4",
            "changed_files": ["uv.lock"],
        }
    )


def _release_evidence() -> EvidenceItem:
    return EvidenceItem(
        evidence_id="release-notes-001",
        kind="upstream_release_notes",
        state="accepted",
        source="Dependabot-provided upstream release notes",
        observation="Soup Sieve 2.8 reports dropping Python 3.8 support.",
        limitations=(
            "Release notes are upstream claims.",
        ),
    )


def _missing_repository_support() -> EvidenceItem:
    return EvidenceItem(
        evidence_id="python-support-001",
        kind="repository_python_support",
        state="missing",
        source="Repository Python support configuration",
        limitations=(
            "Repository Python support was not collected.",
        ),
    )


class DecisionInputTests(unittest.TestCase):
    def test_accepts_traceable_python_support_fact(self) -> None:
        decision_input = DecisionInput(
            evidence=EvidenceSet(
                case=_case(),
                items=(
                    _release_evidence(),
                    _missing_repository_support(),
                ),
            ),
            python_support_changes=(
                PythonSupportChange(
                    change="dropped",
                    python_version=" 3.8 ",
                    evidence_ids=(" release-notes-001 ",),
                ),
            ),
            policy_version=" m2-v0.1 ",
        )

        change = decision_input.python_support_changes[0]
        self.assertEqual(change.python_version, "3.8")
        self.assertEqual(change.evidence_ids, ("release-notes-001",))
        self.assertEqual(decision_input.policy_version, "m2-v0.1")

    def test_rejects_unknown_fact_evidence_reference(self) -> None:
        with self.assertRaises(ValidationError) as raised:
            DecisionInput(
                evidence=EvidenceSet(
                    case=_case(),
                    items=(_release_evidence(),),
                ),
                python_support_changes=(
                    PythonSupportChange(
                        change="dropped",
                        python_version="3.8",
                        evidence_ids=("unknown-001",),
                    ),
                ),
                policy_version="m2-v0.1",
            )

        self.assertIn(
            "references unknown evidence_id: unknown-001",
            raised.exception.errors(include_url=False)[0]["msg"],
        )

    def test_rejects_positive_fact_supported_by_missing_evidence(self) -> None:
        with self.assertRaises(ValidationError) as raised:
            DecisionInput(
                evidence=EvidenceSet(
                    case=_case(),
                    items=(_missing_repository_support(),),
                ),
                python_support_changes=(
                    PythonSupportChange(
                        change="dropped",
                        python_version="3.8",
                        evidence_ids=("python-support-001",),
                    ),
                ),
                policy_version="m2-v0.1",
            )

        self.assertIn(
            "must reference accepted evidence: python-support-001",
            raised.exception.errors(include_url=False)[0]["msg"],
        )


class EvaluateDecisionTests(unittest.TestCase):
    def test_recommends_targeted_checks_for_unresolved_python_support_drop(self) -> None:
        decision_input = DecisionInput(
            evidence=EvidenceSet(
                case=_case(),
                items=(
                    _release_evidence(),
                    _missing_repository_support(),
                ),
            ),
            python_support_changes=(
                PythonSupportChange(
                    change="dropped",
                    python_version="3.8",
                    evidence_ids=("release-notes-001",),
                ),
            ),
            policy_version="m2-v0.1",
        )

        result = evaluate_decision(decision_input)

        self.assertEqual(result.outcome, "run_targeted_checks")
        self.assertEqual(
            result.reasons[0].reason_code,
            "PYTHON_SUPPORT_DROP_UNRESOLVED",
        )
        self.assertEqual(
            result.reasons[0].evidence_ids,
            ("release-notes-001", "python-support-001"),
        )
        self.assertEqual(len(result.targeted_checks), 3)
        self.assertEqual(len(result.limitations), 2)
        self.assertEqual(result.policy_version, "m2-v0.1")

    def test_abstains_when_no_bounded_rule_applies(self) -> None:
        decision_input = DecisionInput(
            evidence=EvidenceSet(
                case=_case(),
                items=(_release_evidence(),),
            ),
            python_support_changes=(),
            policy_version="m2-v0.1",
        )

        result = evaluate_decision(decision_input)

        self.assertEqual(result.outcome, "abstain")
        self.assertEqual(
            result.reasons[0].reason_code,
            "NO_SUPPORTED_DECISION_RULE",
        )
        self.assertEqual(result.targeted_checks, ())

    def test_ordinary_release_evidence_does_not_trigger_without_structured_fact(self) -> None:
        ordinary_release_evidence = EvidenceItem(
            evidence_id="release-notes-ordinary-001",
            kind="upstream_release_notes",
            state="accepted",
            source="Upstream release notes",
            observation="The release fixes documentation spelling.",
            limitations=("No compatibility conclusion is established.",),
        )
        decision_input = DecisionInput(
            evidence=EvidenceSet(
                case=_case(),
                items=(
                    ordinary_release_evidence,
                    _missing_repository_support(),
                ),
            ),
            python_support_changes=(),
            policy_version="m2-v0.1",
        )

        result = evaluate_decision(decision_input)

        self.assertEqual(result.outcome, "abstain")

    def test_serializes_machine_readable_decision_result(self) -> None:
        decision_input = DecisionInput(
            evidence=EvidenceSet(
                case=_case(),
                items=(
                    _release_evidence(),
                    _missing_repository_support(),
                ),
            ),
            python_support_changes=(
                PythonSupportChange(
                    change="dropped",
                    python_version="3.8",
                    evidence_ids=("release-notes-001",),
                ),
            ),
            policy_version="m2-v0.1",
        )

        serialized = json.loads(
            evaluate_decision(decision_input).model_dump_json()
        )

        self.assertEqual(serialized["outcome"], "run_targeted_checks")
        self.assertEqual(serialized["policy_version"], "m2-v0.1")


if __name__ == "__main__":
    unittest.main()
