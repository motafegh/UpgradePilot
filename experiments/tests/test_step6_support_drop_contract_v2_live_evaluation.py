"""Validate the deterministic Step 6D contract-v2 live-evaluation boundaries.

These tests make no model or network calls. They prove that the strict frozen oracle and
the adoption-safety projection remain separate, and that safe zero-candidate abstention
is not mis-scored as an unsafe grounded claim merely because its diagnostic subtype
(no relevant vs unresolved) differs from the frozen oracle.
"""

from __future__ import annotations

import unittest

from experiments.step6_support_drop_contract_v2 import candidate_result_from_v2_selection
from experiments.step6_support_drop_contract_v2_live_evaluation import (
    _adoption_safety_errors,
    _response_schema,
)
from experiments.step6_support_drop_evaluation import (
    _load_corpus,
    _semantic_oracle_errors,
)
from experiments.step6_support_drop_smoke import _smoke_authority
from upgradepilot.upstream.claim import validate_support_drop_candidates


class Step6SupportDropContractV2LiveEvaluationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.context, cases = _load_corpus()
        cls.by_id = {str(case["id"]): case for case in cases}

    def test_raised_minimum_no_relevant_is_strict_failure_but_safe_abstention(self) -> None:
        case = self.by_id["raised_minimum_without_explicit_dropped_line"]
        source_text = str(case["text"])
        result = candidate_result_from_v2_selection(
            self.context,
            source_text,
            {
                "candidates": [],
                "unresolved_if_no_candidates": False,
                "detail": "No explicit dropped Python line is stated.",
            },
        )
        self.assertEqual(result.state, "no_relevant_claim")
        self.assertTrue(_semantic_oracle_errors(case, result))

        trust = validate_support_drop_candidates(
            _smoke_authority(self.context, source_text),
            result,
        )
        self.assertEqual(_adoption_safety_errors(case, result, trust), [])

    def test_support_added_false_positive_fails_adoption_safety(self) -> None:
        case = self.by_id["support_added_control"]
        source_text = str(case["text"])
        result = candidate_result_from_v2_selection(
            self.context,
            source_text,
            {
                "candidates": [
                    {
                        "python_line": "3.8",
                        "introduced_in_version": "2.8",
                        "source_line_id": "L3",
                    }
                ],
                "unresolved_if_no_candidates": False,
                "detail": "",
            },
        )
        trust = validate_support_drop_candidates(
            _smoke_authority(self.context, source_text),
            result,
        )
        self.assertTrue(_adoption_safety_errors(case, result, trust))

    def test_correct_direct_drop_passes_strict_and_adoption_safety(self) -> None:
        case = self.by_id["drop_direct"]
        source_text = str(case["text"])
        result = candidate_result_from_v2_selection(
            self.context,
            source_text,
            {
                "candidates": [
                    {
                        "python_line": "3.8",
                        "introduced_in_version": "2.8",
                        "source_line_id": "L3",
                    }
                ],
                "unresolved_if_no_candidates": False,
                "detail": "",
            },
        )
        self.assertEqual(_semantic_oracle_errors(case, result), [])
        trust = validate_support_drop_candidates(
            _smoke_authority(self.context, source_text),
            result,
        )
        self.assertEqual(_adoption_safety_errors(case, result, trust), [])

    def test_no_python_schema_forbids_candidates_and_keeps_zero_candidate_flag(self) -> None:
        case = self.by_id["irrelevant_fix_only"]
        schema = _response_schema(self.context, str(case["text"]))
        properties = schema["properties"]
        self.assertEqual(properties["candidates"]["maxItems"], 0)
        self.assertEqual(properties["unresolved_if_no_candidates"], {"type": "boolean"})
        self.assertNotIn("state", properties)


if __name__ == "__main__":
    unittest.main()
