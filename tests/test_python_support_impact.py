from __future__ import annotations

import unittest

from upgradepilot.dependency.change import DependencyVersionChange
from upgradepilot.github.pull_request import PullRequestIdentity
from upgradepilot.impact.python_support import (
    build_python_support_drop_impact_candidate,
    evaluate_python_support_drop_impact,
)
from upgradepilot.target.python import TargetPythonDeclaration, TargetPythonDeclarationProblem
from upgradepilot.target.relevance import TargetPythonRelevanceResult
from upgradepilot.upstream.claim import GroundedPythonSupportDropClaim
from upgradepilot.upstream.interval import DependencyReleaseInterval


def _dependency() -> DependencyVersionChange:
    return DependencyVersionChange(
        package="demo",
        normalized_package="demo",
        old_version="1.0",
        proposed_version="1.1",
        source_evidence=(),
    )


def _pull_request() -> PullRequestIdentity:
    return PullRequestIdentity(
        repository="example/project",
        number=7,
        title="Bump demo",
        state="open",
        merged=False,
        author="dependabot[bot]",
        base_ref="main",
        base_sha="a" * 40,
        head_ref="dependabot/demo",
        head_sha="b" * 40,
        changed_files=1,
    )


def _claim(python_line: str = "3.9") -> GroundedPythonSupportDropClaim:
    return GroundedPythonSupportDropClaim(
        python_line=python_line,
        introduced_in_version="1.1",
        interval=DependencyReleaseInterval(
            package="demo",
            normalized_package="demo",
            old_version="1.0",
            proposed_version="1.1",
        ),
        source_evidence=(),
    )


def _target(requires_python: str = ">=3.10", *, revision: str | None = None) -> TargetPythonDeclaration:
    return TargetPythonDeclaration(
        state="available",
        path="pyproject.toml",
        revision=revision or "b" * 40,
        blob_sha="target-blob",
        requires_python=requires_python,
    )


def _relevance(candidate, state: str, target_evidence, detail: str = "Controlled result."):
    return TargetPythonRelevanceResult(
        state=state,  # type: ignore[arg-type]
        upstream_result=candidate.upstream_claim,
        target_evidence=target_evidence,
        specifier_result=None,
        detail=detail,
    )


class PythonSupportImpactTests(unittest.TestCase):
    def test_candidate_preserves_identity_without_self_authorizing_exposure(self) -> None:
        candidate = build_python_support_drop_impact_candidate(
            _pull_request(),
            _dependency(),
            _claim(),
        )
        self.assertEqual(candidate.target_repository, "example/project")
        self.assertEqual(candidate.target_revision, "b" * 40)
        self.assertEqual(candidate.mechanism_status, "established")
        self.assertEqual(candidate.exposure_status, "to_evaluate")
        self.assertEqual(candidate.activation_status, "to_evaluate")
        self.assertEqual(candidate.consequence_status, "possible")

    def test_pre_acquisition_state_is_explicitly_unresolved(self) -> None:
        candidate = build_python_support_drop_impact_candidate(
            _pull_request(),
            _dependency(),
            _claim(),
        )
        result = evaluate_python_support_drop_impact(candidate)

        propositions = result.applicability.paths[0].propositions
        self.assertEqual(result.applicability.state, "unresolved")
        self.assertIsNone(result.target_relevance)
        self.assertEqual(propositions[1].state, "unresolved")
        self.assertEqual(propositions[1].evidence_coverage, "insufficient")
        self.assertIn("not yet been acquired", propositions[1].detail)
        self.assertEqual(propositions[2].state, "unresolved")
        self.assertEqual(propositions[2].evidence_coverage, "insufficient")

    def test_overlap_establishes_candidate_applicability(self) -> None:
        candidate = build_python_support_drop_impact_candidate(
            _pull_request(),
            _dependency(),
            _claim(),
        )
        result = evaluate_python_support_drop_impact(
            candidate,
            _relevance(candidate, "declared_python_overlap", _target(">=3.9")),
        )
        self.assertEqual(result.applicability.state, "established_applicable")
        self.assertEqual(
            tuple(
                proposition.state
                for proposition in result.applicability.paths[0].propositions
            ),
            ("established", "established", "established"),
        )

    def test_non_overlap_establishes_not_applicable_for_bounded_candidate(self) -> None:
        candidate = build_python_support_drop_impact_candidate(
            _pull_request(),
            _dependency(),
            _claim(),
        )
        result = evaluate_python_support_drop_impact(
            candidate,
            _relevance(candidate, "outside_declared_python_range", _target()),
        )
        self.assertEqual(result.applicability.state, "established_not_applicable")
        self.assertEqual(result.applicability.path_model_coverage, "sufficient")

    def test_missing_target_declaration_preserves_unresolved_evidence_coverage(self) -> None:
        candidate = build_python_support_drop_impact_candidate(
            _pull_request(),
            _dependency(),
            _claim(),
        )
        target_problem = TargetPythonDeclarationProblem(
            state="file_unavailable",
            path="pyproject.toml",
            revision="b" * 40,
            blob_sha=None,
            detail="Target declaration unavailable.",
        )
        result = evaluate_python_support_drop_impact(
            candidate,
            _relevance(candidate, "target_declaration_unresolved", target_problem),
        )
        propositions = result.applicability.paths[0].propositions
        self.assertEqual(result.applicability.state, "unresolved")
        assert result.target_relevance is not None
        self.assertIsInstance(
            result.target_relevance.target_evidence,
            TargetPythonDeclarationProblem,
        )
        self.assertEqual(propositions[1].state, "unresolved")
        self.assertEqual(propositions[1].evidence_coverage, "insufficient")
        self.assertNotIn("not yet been acquired", propositions[1].detail)
        self.assertEqual(propositions[2].state, "unresolved")

    def test_unsupported_comparison_is_not_misreported_as_missing_target_evidence(self) -> None:
        candidate = build_python_support_drop_impact_candidate(
            _pull_request(),
            _dependency(),
            _claim(),
        )
        result = evaluate_python_support_drop_impact(
            candidate,
            _relevance(candidate, "comparison_unsupported", _target("===3.9.0")),
        )
        propositions = result.applicability.paths[0].propositions
        self.assertEqual(result.applicability.state, "unresolved")
        self.assertEqual(propositions[1].state, "established")
        self.assertEqual(propositions[1].evidence_coverage, "sufficient")
        self.assertEqual(propositions[2].state, "unresolved")
        self.assertEqual(propositions[2].evidence_coverage, "sufficient")

    def test_candidate_rejects_mismatched_dependency_transition(self) -> None:
        mismatched_dependency = DependencyVersionChange(
            package="demo",
            normalized_package="demo",
            old_version="1.0",
            proposed_version="2.0",
            source_evidence=(),
        )
        with self.assertRaises(ValueError):
            build_python_support_drop_impact_candidate(
                _pull_request(),
                mismatched_dependency,
                _claim(),
            )

    def test_assessment_rejects_different_target_revision(self) -> None:
        candidate = build_python_support_drop_impact_candidate(
            _pull_request(),
            _dependency(),
            _claim(),
        )
        with self.assertRaises(ValueError):
            evaluate_python_support_drop_impact(
                candidate,
                _relevance(
                    candidate,
                    "declared_python_overlap",
                    _target(">=3.9", revision="c" * 40),
                ),
            )

    def test_unresolved_upstream_state_cannot_be_smuggled_into_grounded_candidate(self) -> None:
        candidate = build_python_support_drop_impact_candidate(
            _pull_request(),
            _dependency(),
            _claim(),
        )
        with self.assertRaises(ValueError):
            evaluate_python_support_drop_impact(
                candidate,
                _relevance(candidate, "upstream_claim_unresolved", None),
            )


if __name__ == "__main__":
    unittest.main()
