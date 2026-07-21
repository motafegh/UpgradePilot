import unittest

from upgradepilot.case_identity import build_initial_case_record
from upgradepilot.decision import DecisionInput, evaluate_decision
from upgradepilot.evidence import EvidenceItem, EvidenceSet
from upgradepilot.extraction import (
    CandidateExtractionResult,
    CandidatePythonSupportChange,
    PythonSupportExtractionService,
)


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


class _FakeExtractor:
    extractor_id = "fake:python-support-v1"

    def __init__(self, result):
        self.result = result
        self.received_text = None

    def extract(self, text):
        self.received_text = text
        return self.result


class PythonSupportExtractionServiceTests(unittest.TestCase):
    def test_coordinates_candidate_extraction_validation_and_decision(self):
        release_evidence = EvidenceItem(
            evidence_id="release-notes-001",
            kind="upstream_release_notes",
            state="accepted",
            source="Dependabot-provided upstream release notes",
            observation="Soup Sieve 2.8 drops Python 3.8 support.",
            limitations=("Release notes are upstream claims.",),
        )
        missing_repository_support = EvidenceItem(
            evidence_id="python-support-001",
            kind="repository_python_support",
            state="missing",
            source="Repository Python support configuration",
            limitations=("Repository Python support was not collected.",),
        )
        extractor = _FakeExtractor(
            CandidateExtractionResult(
                facts=(
                    CandidatePythonSupportChange(
                        change="dropped",
                        python_version="3.8",
                        source_quote="Soup Sieve 2.8 drops Python 3.8 support.",
                    ),
                ),
            )
        )

        extraction = PythonSupportExtractionService(extractor).extract(release_evidence)
        decision = evaluate_decision(
            DecisionInput(
                evidence=EvidenceSet(
                    case=_case(),
                    items=(release_evidence, missing_repository_support),
                ),
                python_support_changes=extraction.to_decision_facts(),
                policy_version="m2-v0.1",
            )
        )

        self.assertEqual(extractor.received_text, release_evidence.observation)
        self.assertEqual(len(extraction.accepted_facts), 1)
        self.assertEqual(extraction.validation_errors, ())
        self.assertEqual(
            extraction.accepted_facts[0].extractor_id,
            "fake:python-support-v1",
        )
        self.assertEqual(decision.outcome, "run_targeted_checks")
        self.assertEqual(
            decision.reasons[0].reason_code,
            "PYTHON_SUPPORT_DROP_UNRESOLVED",
        )

    def test_does_not_create_decision_fact_from_ungrounded_candidate(self):
        evidence = EvidenceItem(
            evidence_id="release-notes-001",
            kind="upstream_release_notes",
            state="accepted",
            source="Upstream release notes",
            observation="Documentation was updated.",
            limitations=("No compatibility conclusion is established.",),
        )
        extractor = _FakeExtractor(
            CandidateExtractionResult(
                facts=(
                    CandidatePythonSupportChange(
                        change="dropped",
                        python_version="3.8",
                        source_quote="Python 3.8 support was dropped.",
                    ),
                ),
            )
        )

        extraction = PythonSupportExtractionService(extractor).extract(evidence)

        self.assertEqual(extraction.accepted_facts, ())
        self.assertEqual(
            extraction.validation_errors,
            ("candidate[0]: SOURCE_QUOTE_NOT_FOUND",),
        )
        self.assertEqual(extraction.to_decision_facts(), ())


if __name__ == "__main__":
    unittest.main()
