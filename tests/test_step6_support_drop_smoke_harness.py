"""Validate deterministic boundaries of the Step 6C LM Studio smoke harness.

These tests do not call LM Studio. They prove that the model-facing semantic selection
maps into exact Step 2 evidence without asking the model to reproduce source whitespace,
and that semantic correctness remains separate from mechanical grounding.
"""

from __future__ import annotations

import unittest

from experiments.step6_support_drop_smoke import (
    _candidate_result_from_model,
    _indexed_source_lines,
    _load_smoke_case,
    _python_line_tokens,
    _semantic_oracle_errors,
    _smoke_authority,
)
from upgradepilot.upstream_claim import (
    GroundedPythonSupportDropClaim,
    validate_support_drop_candidates,
)


class Step6SupportDropSmokeHarnessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.context, self.case = _load_smoke_case()
        self.source_text = str(self.case["text"])

    def test_expected_s001_line_selection_maps_exact_quote_and_grounds(self) -> None:
        inner = self._inner(python_line="3.8", source_line_id="L3")

        candidate_result = _candidate_result_from_model(
            self.context,
            self.source_text,
            inner,
        )
        self.assertEqual(
            candidate_result.candidates[0].source_quote,
            "-   **NEW**: Drop support for Python 3.8.",
        )
        self.assertEqual(
            _semantic_oracle_errors(self.context, self.case, candidate_result),
            [],
        )

        trust_result = validate_support_drop_candidates(
            _smoke_authority(self.context, self.source_text),
            candidate_result,
        )
        self.assertIsInstance(trust_result, GroundedPythonSupportDropClaim)
        assert isinstance(trust_result, GroundedPythonSupportDropClaim)
        self.assertEqual(trust_result.python_line, "3.8")
        self.assertEqual(trust_result.introduced_in_version, "2.8")

    def test_semantic_oracle_catches_wrong_direction_that_line_grounding_cannot(self) -> None:
        # L4 is an exact source line, but it says ADD, not DROP. The adapter can recover
        # and ground the exact line mechanically; only semantic evaluation catches the
        # model choosing the wrong direction for the bounded extraction task.
        inner = self._inner(python_line="3.14", source_line_id="L4")

        candidate_result = _candidate_result_from_model(
            self.context,
            self.source_text,
            inner,
        )
        semantic_errors = _semantic_oracle_errors(
            self.context,
            self.case,
            candidate_result,
        )
        self.assertTrue(semantic_errors)

        trust_result = validate_support_drop_candidates(
            _smoke_authority(self.context, self.source_text),
            candidate_result,
        )
        self.assertIsInstance(trust_result, GroundedPythonSupportDropClaim)
        assert isinstance(trust_result, GroundedPythonSupportDropClaim)
        self.assertEqual(trust_result.python_line, "3.14")

    def test_model_facing_tokens_are_deterministically_bounded_by_source(self) -> None:
        self.assertEqual(_python_line_tokens(self.source_text), ("3.8", "3.14"))
        indexed = _indexed_source_lines(self.source_text)
        self.assertEqual(indexed[2][0], "L3")
        self.assertEqual(indexed[2][1], "-   **NEW**: Drop support for Python 3.8.")
        self.assertEqual(
            self.source_text[indexed[2][2] : indexed[2][3]],
            indexed[2][1],
        )

    def test_mapping_rejects_non_available_state_with_candidates(self) -> None:
        inner = self._inner(python_line="3.8", source_line_id="L3")
        inner["state"] = "unresolved"

        with self.assertRaisesRegex(ValueError, "cannot contain candidate claims"):
            _candidate_result_from_model(
                self.context,
                self.source_text,
                inner,
            )

    def test_mapping_rejects_unknown_source_line_id(self) -> None:
        inner = self._inner(python_line="3.8", source_line_id="L999")

        with self.assertRaisesRegex(ValueError, "source line ID"):
            _candidate_result_from_model(
                self.context,
                self.source_text,
                inner,
            )

    def _inner(self, *, python_line: str, source_line_id: str) -> dict[str, object]:
        return {
            "state": "candidates_available",
            "candidates": [
                {
                    "python_line": python_line,
                    "introduced_in_version": "2.8",
                    "source_line_id": source_line_id,
                }
            ],
            "detail": "",
        }


if __name__ == "__main__":
    unittest.main()
