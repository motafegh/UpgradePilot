"""Validate material-repeat scoring for the Step 6 contract-v2 assessment."""

from __future__ import annotations

import json
import unittest

from experiments.step6_support_drop_contract_v2_assessment import (
    material_trusted_outcome_signature,
)


class Step6ContractV2AssessmentTests(unittest.TestCase):
    def _run(self, *, detail: str, trust_state: str = "candidate_unresolved") -> dict[str, object]:
        return {
            "candidate_result": {
                "state": "unresolved",
                "package": "soupsieve",
                "normalized_package": "soupsieve",
                "old_version": "2.6",
                "proposed_version": "2.8.4",
                "candidates": [],
                "detail": detail,
            },
            "trust_result": {
                "kind": "problem",
                "state": trust_state,
                "detail": detail,
            },
            "adoption_safety_pass": True,
        }

    def test_detail_wording_does_not_change_material_signature(self) -> None:
        first = self._run(detail="The exact dropped line is not explicit.")
        second = self._run(detail="No specific older Python line can be established.")
        self.assertEqual(
            material_trusted_outcome_signature(first),
            material_trusted_outcome_signature(second),
        )

    def test_trust_problem_state_changes_material_signature(self) -> None:
        unresolved = self._run(detail="x", trust_state="candidate_unresolved")
        no_claim = self._run(detail="x", trust_state="no_support_drop_claim")
        self.assertNotEqual(
            material_trusted_outcome_signature(unresolved),
            material_trusted_outcome_signature(no_claim),
        )

    def test_candidate_identity_changes_material_signature(self) -> None:
        first = {
            "candidate_result": {
                "state": "candidates_available",
                "candidates": [
                    {
                        "category": "support_boundary_change",
                        "change_state": "support_dropped",
                        "python_line": "3.8",
                        "introduced_in_version": "2.8",
                        "source_kind": "tagged_changelog",
                        "source_release_version": None,
                        "source_quote": "Drop support for Python 3.8.",
                        "quote_start": 8,
                        "quote_end": 36,
                    }
                ],
                "detail": None,
            },
            "trust_result": {
                "kind": "grounded",
                "python_line": "3.8",
                "introduced_in_version": "2.8",
                "source_count": 1,
            },
            "adoption_safety_pass": True,
        }
        second = json.loads(json.dumps(first))
        second["candidate_result"]["candidates"][0]["python_line"] = "3.9"
        self.assertNotEqual(
            material_trusted_outcome_signature(first),
            material_trusted_outcome_signature(second),
        )


if __name__ == "__main__":
    unittest.main()
