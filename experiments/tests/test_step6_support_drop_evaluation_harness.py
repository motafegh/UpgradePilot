"""Validate deterministic mechanics of the Step 6D semantic evaluation harness.

These tests do not call LM Studio. They verify corpus scheduling, no-claim schema behavior,
order-insensitive semantic scoring, and false-positive diagnostics around the already
validated Step 6C adapter boundary.
"""

from __future__ import annotations

import unittest

from experiments.step6_support_drop_evaluation import (
    CRITICAL_REPEAT_CASE_IDS,
    TOTAL_CRITICAL_TRIALS,
    _diagnostic_flags,
    _evaluation_response_schema,
    _load_corpus,
    _planned_runs,
    _semantic_oracle_errors,
)
from experiments.step6_support_drop_smoke import _candidate_result_from_model


class Step6SupportDropEvaluationHarnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.context, cls.cases = _load_corpus()
        cls.by_id = {str(case["id"]): case for case in cls.cases}

    def test_no_python_control_schema_forbids_candidates(self) -> None:
        case = self.by_id["irrelevant_fix_only"]
        schema = _evaluation_response_schema(self.context, str(case["text"]))
        candidates = schema["properties"]["candidates"]
        self.assertEqual(candidates["maxItems"], 0)

    def test_planned_runs_cover_all_cases_and_repeat_only_critical_controls(self) -> None:
        planned = _planned_runs(self.cases)
        expected_count = len(self.cases) + len(CRITICAL_REPEAT_CASE_IDS) * (
            TOTAL_CRITICAL_TRIALS - 1
        )
        self.assertEqual(len(planned), expected_count)

        counts: dict[str, int] = {}
        for case, _ in planned:
            case_id = str(case["id"])
            counts[case_id] = counts.get(case_id, 0) + 1

        for case in self.cases:
            case_id = str(case["id"])
            expected = (
                TOTAL_CRITICAL_TRIALS
                if case_id in CRITICAL_REPEAT_CASE_IDS
                else 1
            )
            self.assertEqual(counts[case_id], expected, case_id)

    def test_multiple_claim_semantic_scoring_is_order_insensitive(self) -> None:
        case = self.by_id["multiple_distinct_dropped_lines"]
        source_text = str(case["text"])
        inner = {
            "state": "candidates_available",
            "candidates": [
                {
                    "python_line": "3.9",
                    "introduced_in_version": "2.8",
                    "source_line_id": "L4",
                },
                {
                    "python_line": "3.8",
                    "introduced_in_version": "2.8",
                    "source_line_id": "L3",
                },
            ],
            "detail": "",
        }
        candidate_result = _candidate_result_from_model(
            self.context,
            source_text,
            inner,
        )
        self.assertEqual(_semantic_oracle_errors(case, candidate_result), [])

    def test_support_added_as_drop_is_scored_as_false_positive(self) -> None:
        case = self.by_id["support_added_control"]
        source_text = str(case["text"])
        inner = {
            "state": "candidates_available",
            "candidates": [
                {
                    "python_line": "3.8",
                    "introduced_in_version": "2.8",
                    "source_line_id": "L3",
                }
            ],
            "detail": "",
        }
        candidate_result = _candidate_result_from_model(
            self.context,
            source_text,
            inner,
        )
        self.assertTrue(_semantic_oracle_errors(case, candidate_result))
        flags = _diagnostic_flags(case, candidate_result)
        self.assertTrue(flags["false_positive"])
        self.assertFalse(flags["false_negative"])


if __name__ == "__main__":
    unittest.main()
