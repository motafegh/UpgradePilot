"""Offline proof for the first B2/X1 evidence-first semantic-risk probe.

The test intentionally forces a semantically wrong candidate onto the exact negated source line.
Its purpose is to establish the deterministic grounding boundary: attribution/identity checks can
accept a candidate that is perfectly grounded to source text even when the model's English
interpretation of that source would be wrong.

This does NOT prove that the live local model will make the mistake.  The matching live experiment
exists to answer that separate question.
"""

from __future__ import annotations

import unittest

from experiments.b2_x1_e1_support_drop_semantic_probe import build_probe_inputs
from upgradepilot.upstream.claim import (
    CandidateUpstreamClaim,
    CandidateUpstreamClaimResult,
    GroundedPythonSupportDropClaim,
    validate_support_drop_candidates,
)


class SupportDropSemanticProbeTests(unittest.TestCase):
    def test_deterministic_grounding_accepts_exactly_attributed_but_semantically_wrong_candidate(
        self,
    ) -> None:
        inputs = build_probe_inputs()
        negated_line = next(
            line
            for section in inputs.window.sections
            for line in section.source_lines
            if "support was not dropped" in line.text
        )

        candidate_result = CandidateUpstreamClaimResult(
            state="candidates_available",
            package=inputs.window.interval.package,
            normalized_package=inputs.window.interval.normalized_package,
            old_version=inputs.window.interval.old_version,
            proposed_version=inputs.window.interval.proposed_version,
            candidates=(
                CandidateUpstreamClaim(
                    category="support_boundary_change",
                    change_state="support_dropped",
                    python_line="3.8",
                    introduced_in_version="2.8",
                    source_kind="tagged_changelog",
                    source_release_version=None,
                    source_quote=negated_line.text,
                    quote_start=negated_line.start_offset,
                    quote_end=negated_line.end_offset,
                ),
            ),
            detail=None,
        )

        result = validate_support_drop_candidates(inputs.authority, candidate_result)

        self.assertIsInstance(result, GroundedPythonSupportDropClaim)
        assert isinstance(result, GroundedPythonSupportDropClaim)
        self.assertEqual(result.python_line, "3.8")
        self.assertEqual(result.introduced_in_version, "2.8")
        self.assertEqual(result.source_evidence[0].source_quote, negated_line.text)


if __name__ == "__main__":
    unittest.main()
