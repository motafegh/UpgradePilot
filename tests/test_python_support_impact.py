"""Test the first bounded A/B Python-support impact foundation."""

from __future__ import annotations

import unittest

from upgradepilot.dependency.change import (
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
)
from upgradepilot.github.pull_request import PullRequestIdentity
from upgradepilot.impact.python_support import (
    assess_python_support_applicability,
    build_python_support_drop_candidate,
)
from upgradepilot.target.python import (
    TargetPythonDeclaration,
    TargetPythonDeclarationProblem,
)
from upgradepilot.target.relevance import evaluate_target_python_relevance
from upgradepilot.upstream.claim import GroundedPythonSupportDropClaim
from upgradepilot.upstream.interval import DependencyReleaseInterval


def _pull() -> PullRequestIdentity:
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


def _dependency() -> DependencyVersionChange:
    pull = _pull()
    return DependencyVersionChange(
        package="demo",
        normalized_package="demo",
        old_version="1.0",
        proposed_version="1.1",
        source_evidence=(
            DependencyChangeSourceEvidence(
                path="requirements.txt",
                file_format="exact_requirement",
                extraction_method="exact_base_head_files",
                base_revision=pull.base_sha,
                head_revision=pull.head_sha,
            ),
        ),
    )


def _claim(python_line: str = "3.9") -> GroundedPythonSupportDropClaim:
    dependency = _dependency()
    return GroundedPythonSupportDropClaim(
        python_line=python_line,
        introduced_in_version="1.1",
        interval=DependencyReleaseInterval(
            package=dependency.package,
            normalized_package=dependency.normalized_package,
            old_version=dependency.old_version,
            proposed_version=dependency.proposed_version,
        ),
        source_evidence=(),
    )


def _target(requires_python: str) -> TargetPythonDeclaration:
    return TargetPythonDeclaration(
        state="available",
        path="pyproject.toml",
        revision=_pull().head_sha,
        blob_sha="target-blob",
        requires_python=requires_python,
    )


def _candidate():
    return build_python_support_drop_candidate(_pull(), _dependency(), _claim())


class PythonSupportImpactTests(unittest.TestCase):
    def test_candidate_preserves_identity_without_self_establishing_target_truth(self) -> None:
        candidate = _candidate()

        self.assertEqual(candidate.pull_request.repository, "example/project")
        self.assertEqual(candidate.pull_request.number, 7)
        self.assertEqual(candidate.pull_request.head_sha, "b" * 40)
        self.assertEqual(candidate.dependency.normalized_package, "demo")
        self.assertEqual(candidate.dependency.old_version, "1.0")
        self.assertEqual(candidate.dependency.proposed_version, "1.1")
        self.assertEqual(candidate.upstream_claim.python_line, "3.9")

        self.assertEqual(candidate.mechanism, "python_support_drop")
        self.assertEqual(candidate.exposure_hypothesis, "target_declared_python_range")
        self.assertEqual(
            candidate.activation_hypothesis,
            "dropped_python_line_intersects_declared_range",
        )
        self.assertEqual(
            candidate.possible_consequence,
            "dependency_may_not_support_part_of_declared_python_range",
        )

        # A names the target relation and possible consequence; B still has to evaluate them.
        self.assertFalse(hasattr(candidate, "target_declaration_state"))
        self.assertFalse(hasattr(candidate, "applicability_state"))

    def test_candidate_rejects_mismatched_dependency_interval(self) -> None:
        wrong_claim = GroundedPythonSupportDropClaim(
            python_line="3.9",
            introduced_in_version="2.0",
            interval=DependencyReleaseInterval(
                package="demo",
                normalized_package="demo",
                old_version="1.1",
                proposed_version="2.0",
            ),
            source_evidence=(),
        )

        with self.assertRaises(ValueError):
            build_python_support_drop_candidate(_pull(), _dependency(), wrong_claim)

    def test_candidate_rejects_dependency_revision_mismatch(self) -> None:
        dependency = DependencyVersionChange(
            package="demo",
            normalized_package="demo",
            old_version="1.0",
            proposed_version="1.1",
            source_evidence=(
                DependencyChangeSourceEvidence(
                    path="requirements.txt",
                    file_format="exact_requirement",
                    extraction_method="exact_base_head_files",
                    base_revision="c" * 40,
                    head_revision=_pull().head_sha,
                ),
            ),
        )

        with self.assertRaises(ValueError):
            build_python_support_drop_candidate(_pull(), dependency, _claim())

    def test_overlap_establishes_candidate_applicability(self) -> None:
        candidate = _candidate()
        relevance = evaluate_target_python_relevance(candidate.upstream_claim, _target(">=3.9"))

        result = assess_python_support_applicability(candidate, relevance)

        self.assertEqual(result.state, "established_applicable")
        self.assertEqual(
            tuple(proposition.state for proposition in result.propositions),
            ("established", "established", "established"),
        )
        self.assertEqual(result.path_model_coverage, "sufficient")
        self.assertIs(result.target_relevance, relevance)

    def test_non_overlap_refutes_only_this_bounded_candidate_path(self) -> None:
        candidate = _candidate()
        relevance = evaluate_target_python_relevance(
            candidate.upstream_claim,
            _target(">=3.10"),
        )

        result = assess_python_support_applicability(candidate, relevance)

        self.assertEqual(result.state, "established_not_applicable")
        self.assertEqual(
            tuple(proposition.state for proposition in result.propositions),
            ("established", "established", "refuted"),
        )
        self.assertIn("does not establish", result.detail)
        self.assertIn("other material impact", result.detail)

    def test_missing_target_evidence_remains_unresolved_not_refuted(self) -> None:
        candidate = _candidate()
        target_problem = TargetPythonDeclarationProblem(
            state="file_unavailable",
            path="pyproject.toml",
            revision=_pull().head_sha,
            detail="The exact-head target file could not be acquired.",
        )
        relevance = evaluate_target_python_relevance(
            candidate.upstream_claim,
            target_problem,
        )

        result = assess_python_support_applicability(candidate, relevance)

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(
            tuple(proposition.state for proposition in result.propositions),
            ("established", "unresolved", "unresolved"),
        )
        self.assertNotIn("refuted", tuple(p.state for p in result.propositions))

    def test_unsupported_comparison_preserves_established_target_but_unresolved_activation(
        self,
    ) -> None:
        candidate = _candidate()
        relevance = evaluate_target_python_relevance(
            candidate.upstream_claim,
            _target("===3.9.0"),
        )

        result = assess_python_support_applicability(candidate, relevance)

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(
            tuple(proposition.state for proposition in result.propositions),
            ("established", "established", "unresolved"),
        )

    def test_target_revision_must_match_candidate_head(self) -> None:
        candidate = _candidate()
        wrong_target = TargetPythonDeclaration(
            state="available",
            path="pyproject.toml",
            revision="c" * 40,
            blob_sha="target-blob",
            requires_python=">=3.10",
        )
        relevance = evaluate_target_python_relevance(
            candidate.upstream_claim,
            wrong_target,
        )

        with self.assertRaises(ValueError):
            assess_python_support_applicability(candidate, relevance)


if __name__ == "__main__":
    unittest.main()
