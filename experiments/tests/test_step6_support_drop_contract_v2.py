"""Validate the deterministic Step 6 support-drop contract-v2 mechanics.

These tests make no model calls. They prove that candidate presence derives
``candidates_available`` mechanically while the unresolved/no-relevant distinction stays
semantic only on the zero-candidate branch.
"""

from __future__ import annotations

import unittest

from experiments.step6_support_drop_contract_v2 import (
    candidate_result_from_v2_selection,
    selection_from_v1_structured_output,
)
from experiments.step6_support_drop_evaluation import _load_corpus


class Step6SupportDropContractV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.context, cases = _load_corpus()
        cls.by_id = {str(case["id"]): case for case in cases}

    def test_candidate_presence_derives_available_state(self) -> None:
        case = self.by_id["s001_exact_excerpt"]
        selection = {
            "candidates": [
                {
                    "python_line": "3.8",
                    "introduced_in_version": "2.8",
                    "source_line_id": "L3",
                }
            ],
            "unresolved_if_no_candidates": True,
            "detail": "ignored on the candidate branch",
        }
        result = candidate_result_from_v2_selection(
            self.context,
            str(case["text"]),
            selection,
        )
        self.assertEqual(result.state, "candidates_available")
        self.assertIsNone(result.detail)
        self.assertEqual(len(result.candidates), 1)
        self.assertEqual(result.candidates[0].python_line, "3.8")

    def test_empty_unresolved_selection_derives_unresolved_state(self) -> None:
        case = self.by_id["raised_minimum_without_explicit_dropped_line"]
        result = candidate_result_from_v2_selection(
            self.context,
            str(case["text"]),
            {
                "candidates": [],
                "unresolved_if_no_candidates": True,
                "detail": "The dropped Python line is not explicitly stated.",
            },
        )
        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.candidates, ())
        self.assertEqual(
            result.detail,
            "The dropped Python line is not explicitly stated.",
        )

    def test_empty_clear_selection_derives_no_relevant_claim(self) -> None:
        case = self.by_id["support_added_control"]
        result = candidate_result_from_v2_selection(
            self.context,
            str(case["text"]),
            {
                "candidates": [],
                "unresolved_if_no_candidates": False,
                "detail": "",
            },
        )
        self.assertEqual(result.state, "no_relevant_claim")
        self.assertEqual(result.candidates, ())
        self.assertIsNone(result.detail)

    def test_unresolved_zero_candidate_requires_detail(self) -> None:
        case = self.by_id["ambiguous_support_wording"]
        with self.assertRaisesRegex(ValueError, "requires non-empty detail"):
            candidate_result_from_v2_selection(
                self.context,
                str(case["text"]),
                {
                    "candidates": [],
                    "unresolved_if_no_candidates": True,
                    "detail": "",
                },
            )

    def test_historical_s001_contradiction_is_replayable_without_state_failure(self) -> None:
        case = self.by_id["s001_exact_excerpt"]
        historical = {
            "state": "unresolved",
            "candidates": [
                {
                    "python_line": "3.8",
                    "introduced_in_version": "2.8",
                    "source_line_id": "L3",
                }
            ],
            "detail": "",
        }
        selection = selection_from_v1_structured_output(historical)
        self.assertFalse(selection["unresolved_if_no_candidates"])

        result = candidate_result_from_v2_selection(
            self.context,
            str(case["text"]),
            selection,
        )
        self.assertEqual(result.state, "candidates_available")
        self.assertEqual(result.candidates[0].python_line, "3.8")

    def test_historical_zero_candidate_state_is_preserved_for_replay(self) -> None:
        unresolved = selection_from_v1_structured_output(
            {"state": "unresolved", "candidates": [], "detail": "ambiguous"}
        )
        clear = selection_from_v1_structured_output(
            {"state": "no_relevant_claim", "candidates": [], "detail": ""}
        )
        self.assertTrue(unresolved["unresolved_if_no_candidates"])
        self.assertFalse(clear["unresolved_if_no_candidates"])


if __name__ == "__main__":
    unittest.main()
