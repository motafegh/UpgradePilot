"""Protect the intentionally supported package-level integration contracts."""

from __future__ import annotations

import unittest

import upgradepilot


class PackageInterfaceTests(unittest.TestCase):
    def test_ci_dependency_exercise_contracts_are_public(self) -> None:
        expected = {
            "DependencyCIExerciseResult",
            "DependencyCIExerciseState",
            "WorkflowDependencyExerciseInput",
            "WorkflowDependencyExerciseResult",
            "evaluate_dependency_ci_exercise",
        }

        self.assertTrue(expected.issubset(set(upgradepilot.__all__)))
        for name in expected:
            self.assertTrue(hasattr(upgradepilot, name), name)

        legacy = {
            "CIAuthorityResult",
            "CIAuthorityStatus",
            "WorkflowAuthorityInput",
            "WorkflowAuthorityAssessment",
            "evaluate_ci_authority",
        }
        self.assertTrue(legacy.isdisjoint(set(upgradepilot.__all__)))

    def test_multi_format_dependency_analysis_contracts_are_public(self) -> None:
        expected = {
            "DependencyChangeAnalysis",
            "DependencyChangeAnalysisResult",
            "analyze_dependency_change",
            "is_admitted_requirements_file",
            "is_uv_lock_file",
        }

        self.assertTrue(expected.issubset(set(upgradepilot.__all__)))
        for name in expected:
            self.assertTrue(hasattr(upgradepilot, name), name)

        temporary_ingress = {
            "LegacyDependencyIngress",
            "LegacyDependencyIngressResult",
            "extract_legacy_dependency_ingress",
        }
        self.assertTrue(temporary_ingress.isdisjoint(set(upgradepilot.__all__)))

    def test_upstream_interval_authority_contracts_are_public(self) -> None:
        expected = {
            "UPSTREAM_SOURCE_AUTHORITY_ORDER",
            "AuthoritativeUpstreamIntervalEvidence",
            "CrossedReleaseIndexEvidence",
            "DependencyReleaseInterval",
            "IntervalGitHubReleaseSource",
            "PackageMetadataCorroboration",
            "TaggedChangelogEvidence",
            "UpstreamAuthoritySourceProblem",
            "UpstreamIntervalAuthorityProblem",
            "UpstreamIntervalAuthorityResult",
            "assemble_upstream_interval_authority",
            "release_interval_from_dependency_change",
            "upstream_source_role",
        }

        self.assertTrue(expected.issubset(set(upgradepilot.__all__)))
        for name in expected:
            self.assertTrue(hasattr(upgradepilot, name), name)

    def test_support_drop_claim_contracts_are_public(self) -> None:
        expected = {
            "CandidateUpstreamClaim",
            "CandidateUpstreamClaimResult",
            "GroundedPythonSupportDropClaim",
            "GroundedUpstreamClaimSource",
            "UpstreamSupportDropClaimProblem",
            "UpstreamSupportDropClaimResult",
            "validate_support_drop_candidates",
        }

        self.assertTrue(expected.issubset(set(upgradepilot.__all__)))
        for name in expected:
            self.assertTrue(hasattr(upgradepilot, name), name)

    def test_packaging_method_contracts_are_public(self) -> None:
        expected = {
            "OrderedCrossedReleaseVersions",
            "PackagingVersionProblem",
            "ParsedDependencyReleaseInterval",
            "PythonLineSpecifierEvaluation",
            "PythonLineSpecifierProblem",
            "order_crossed_release_versions",
            "parse_dependency_release_interval",
            "evaluate_python_line_specifier",
        }

        self.assertTrue(expected.issubset(set(upgradepilot.__all__)))
        for name in expected:
            self.assertTrue(hasattr(upgradepilot, name), name)

    def test_target_python_relevance_contracts_are_public(self) -> None:
        expected = {
            "TargetPythonRelevanceResult",
            "TargetPythonRelevanceState",
            "evaluate_target_python_relevance",
        }

        self.assertTrue(expected.issubset(set(upgradepilot.__all__)))
        for name in expected:
            self.assertTrue(hasattr(upgradepilot, name), name)

    def test_step_5a_release_index_contracts_are_public(self) -> None:
        expected = {
            "PackageReleaseIndexEvidence",
            "PackageReleaseIndexProblem",
            "PackageReleaseIndexResult",
            "PyPIReleaseIndexClient",
            "CrossedReleaseIndexSelectionProblem",
            "CrossedReleaseIndexSelectionResult",
            "SelectedCrossedReleaseIndex",
            "select_crossed_release_index",
        }

        self.assertTrue(expected.issubset(set(upgradepilot.__all__)))
        for name in expected:
            self.assertTrue(hasattr(upgradepilot, name), name)

    def test_step_5b_git_tag_commit_contracts_are_public(self) -> None:
        expected = {
            "GitHubTagCommitClient",
            "GitHubTagCommitEvidence",
            "GitHubTagCommitProblem",
            "GitHubTagCommitResult",
        }

        self.assertTrue(expected.issubset(set(upgradepilot.__all__)))
        for name in expected:
            self.assertTrue(hasattr(upgradepilot, name), name)

    def test_step_5c_tagged_changelog_contracts_are_public(self) -> None:
        expected = {
            "TaggedChangelogCompositionResult",
            "build_tagged_changelog_evidence",
        }

        self.assertTrue(expected.issubset(set(upgradepilot.__all__)))
        for name in expected:
            self.assertTrue(hasattr(upgradepilot, name), name)


if __name__ == "__main__":
    unittest.main()
