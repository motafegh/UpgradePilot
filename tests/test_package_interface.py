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


if __name__ == "__main__":
    unittest.main()
