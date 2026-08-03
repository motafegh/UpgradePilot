"""Validate the deterministic boundaries of the Step 6C LM Studio smoke harness.

These tests do not call LM Studio. They prove that the experiment harness maps a
schema-shaped response into the existing Step 2 contracts and, importantly, keeps the
semantic oracle separate from mechanical quote/span grounding.
"""

from __future__ import annotations

import unittest

from experiments.step6_support_drop_smoke import (
    _candidate_result_from_model,
    _load_smoke_case,
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

    def test_expected_s001_candidate_maps_and_grounds(self) -> None:
        inner = self._inner(
            python_line="3.8",
            source_quote="-   **NEW**: Drop support for Python 3.8.",
        )

        candidate_result = _candidate_result_from_model(
            self.context,
            self.source_text,
            inner,
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

    def test_semantic_oracle_catches_wrong_direction_that_quote_grounding_cannot(self) -> None:
        # The source really contains this sentence, but it says ADD, not DROP.
        # Step 2 intentionally grounds exact candidate evidence rather than interpreting
        # natural-language direction. The semantic oracle must therefore catch this
        # model error before model adoption can be justified.
        inner = self._inner(
            python_line="3.14",
            source_quote="-   **NEW**: Add support for Python 3.14.",
        )

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

    def test_mapping_rejects_quote_without_one_exact_source_occurrence(self) -> None:
        inner = self._inner(
            python_line="3.8",
            source_quote="Drop Python 3.8 in some other wording.",
        )

        with self.assertRaisesRegex(ValueError, "unique exact span"):
            _candidate_result_from_model(
                self.context,
                self.source_text,
                inner,
            )

    def _inner(self, *, python_line: str, source_quote: str) -> dict[str, object]:
        return {
            "state": "candidates_available",
            "package": str(self.context["package"]),
            "normalized_package": str(self.context["normalized_package"]),
            "old_version": str(self.context["old_version"]),
            "proposed_version": str(self.context["proposed_version"]),
            "candidates": [
                {
                    "category": "support_boundary_change",
                    "change_state": "support_dropped",
                    "python_line": python_line,
                    "introduced_in_version": "2.8",
                    "source_kind": "tagged_changelog",
                    "source_quote": source_quote,
                }
            ],
            "detail": "",
        }


if __name__ == "__main__":
    unittest.main()
