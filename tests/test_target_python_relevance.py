"""Test Step 4 target-Python relevance as a pure trusted-input boundary.

These tests construct the Step 2 trusted claim type directly on purpose. Source-span
grounding is already tested by ``test_upstream_claim.py``; repeating it here would mix
responsibilities and make Step 4 tests harder to read.
"""

from __future__ import annotations

import unittest

from upgradepilot.target.python import (
    TargetPythonDeclaration,
    TargetPythonDeclarationProblem,
)
from upgradepilot.target.python_specifier import (
    PythonLineSpecifierEvaluation,
    PythonLineSpecifierProblem,
)
from upgradepilot.target.relevance import evaluate_target_python_relevance
from upgradepilot.upstream.claim import (
    GroundedPythonSupportDropClaim,
    UpstreamSupportDropClaimProblem,
)
from upgradepilot.upstream.interval import DependencyReleaseInterval

_REVISION = "b" * 40


def _interval() -> DependencyReleaseInterval:
    return DependencyReleaseInterval(
        package="soupsieve",
        normalized_package="soupsieve",
        old_version="2.6",
        proposed_version="2.8.4",
    )


def _grounded_claim(python_line: str = "3.8") -> GroundedPythonSupportDropClaim:
    return GroundedPythonSupportDropClaim(
        python_line=python_line,
        introduced_in_version="2.8",
        interval=_interval(),
        source_evidence=(),
    )


def _target(requires_python: str) -> TargetPythonDeclaration:
    return TargetPythonDeclaration(
        state="available",
        path="pyproject.toml",
        revision=_REVISION,
        requires_python=requires_python,
    )


class TargetPythonRelevanceTests(unittest.TestCase):
    def test_s001_shaped_non_overlap_is_outside_declared_python_range(self) -> None:
        result = evaluate_target_python_relevance(_grounded_claim("3.8"), _target(">=3.10"))
        self.assertEqual(result.state, "outside_declared_python_range")
        self.assertIsInstance(result.specifier_result, PythonLineSpecifierEvaluation)
        assert isinstance(result.specifier_result, PythonLineSpecifierEvaluation)
        self.assertFalse(result.specifier_result.contains_stable_release)
        self.assertIsNone(result.specifier_result.witness_version)
        self.assertEqual(result.target_evidence, _target(">=3.10"))

    def test_overlap_preserves_exact_stable_witness(self) -> None:
        result = evaluate_target_python_relevance(_grounded_claim("3.8"), _target(">=3.8"))
        self.assertEqual(result.state, "declared_python_overlap")
        self.assertIsInstance(result.specifier_result, PythonLineSpecifierEvaluation)
        assert isinstance(result.specifier_result, PythonLineSpecifierEvaluation)
        self.assertTrue(result.specifier_result.contains_stable_release)
        self.assertEqual(str(result.specifier_result.witness_version), "3.8.0")
        assert result.target_evidence is not None
        self.assertEqual(result.target_evidence.revision, _REVISION)

    def test_each_target_evidence_problem_stays_target_unresolved(self) -> None:
        for state in (
            "file_unavailable",
            "malformed_toml",
            "project_table_absent",
            "requires_python_absent",
            "invalid_requires_python",
        ):
            with self.subTest(state=state):
                target_problem = TargetPythonDeclarationProblem(
                    state=state,
                    path="pyproject.toml",
                    revision=_REVISION,
                    detail=f"Target evidence problem: {state}.",
                )
                result = evaluate_target_python_relevance(_grounded_claim(), target_problem)
                self.assertEqual(result.state, "target_declaration_unresolved")
                self.assertIs(result.target_evidence, target_problem)
                self.assertIsNone(result.specifier_result)

    def test_upstream_problem_stops_before_target_comparison(self) -> None:
        upstream_problem = UpstreamSupportDropClaimProblem(
            state="no_support_drop_claim",
            interval=_interval(),
            detail="No grounded Python support-drop claim was established.",
        )
        result = evaluate_target_python_relevance(upstream_problem, None)
        self.assertEqual(result.state, "upstream_claim_unresolved")
        self.assertIs(result.upstream_result, upstream_problem)
        self.assertIsNone(result.target_evidence)
        self.assertIsNone(result.specifier_result)

    def test_target_evidence_is_rejected_when_upstream_is_unresolved(self) -> None:
        upstream_problem = UpstreamSupportDropClaimProblem(
            state="candidate_unresolved",
            interval=_interval(),
            detail="Candidate extraction was unresolved.",
        )
        with self.assertRaises(ValueError):
            evaluate_target_python_relevance(upstream_problem, _target(">=3.10"))

    def test_grounded_claim_requires_target_evidence(self) -> None:
        with self.assertRaises(ValueError):
            evaluate_target_python_relevance(_grounded_claim(), None)

    def test_valid_but_unsupported_specifier_maps_to_comparison_unsupported(self) -> None:
        result = evaluate_target_python_relevance(_grounded_claim(), _target("===3.8.0"))
        self.assertEqual(result.state, "comparison_unsupported")
        self.assertIsInstance(result.specifier_result, PythonLineSpecifierProblem)
        assert isinstance(result.specifier_result, PythonLineSpecifierProblem)
        self.assertEqual(result.specifier_result.state, "unsupported_requires_python_specifier")

    def test_invalid_pep440_target_specifier_maps_to_target_unresolved(self) -> None:
        result = evaluate_target_python_relevance(_grounded_claim(), _target(">=not-a-version"))
        self.assertEqual(result.state, "target_declaration_unresolved")
        self.assertIsInstance(result.specifier_result, PythonLineSpecifierProblem)
        assert isinstance(result.specifier_result, PythonLineSpecifierProblem)
        self.assertEqual(result.specifier_result.state, "invalid_requires_python_specifier")

    def test_unsatisfiable_target_specifier_maps_to_target_unresolved(self) -> None:
        result = evaluate_target_python_relevance(_grounded_claim(), _target(">=3.10,<3.9"))
        self.assertEqual(result.state, "target_declaration_unresolved")
        self.assertIsInstance(result.specifier_result, PythonLineSpecifierProblem)
        assert isinstance(result.specifier_result, PythonLineSpecifierProblem)
        self.assertEqual(result.specifier_result.state, "unsatisfiable_requires_python_specifier")

    def test_invalid_line_on_purported_grounded_claim_maps_to_upstream_unresolved(self) -> None:
        result = evaluate_target_python_relevance(_grounded_claim("3.8.1"), _target(">=3.8"))
        self.assertEqual(result.state, "upstream_claim_unresolved")
        self.assertIsInstance(result.specifier_result, PythonLineSpecifierProblem)
        assert isinstance(result.specifier_result, PythonLineSpecifierProblem)
        self.assertEqual(result.specifier_result.state, "invalid_python_line")

    def test_wrong_public_argument_types_are_rejected(self) -> None:
        with self.assertRaises(TypeError):
            evaluate_target_python_relevance("not-a-claim", None)  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            evaluate_target_python_relevance(_grounded_claim(), "not-target-evidence")  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
