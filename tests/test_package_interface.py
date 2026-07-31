"""Protect the intentionally supported package-level Step 7 contracts."""

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


if __name__ == "__main__":
    unittest.main()
