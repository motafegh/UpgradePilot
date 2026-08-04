"""Test the boundary-complete stable Python-line specifier method."""

from __future__ import annotations

import unittest
from unittest.mock import patch

from packaging.version import Version

from upgradepilot.target.python_specifier import (
    PythonLineSpecifierEvaluation,
    PythonLineSpecifierProblem,
    evaluate_python_line_specifier,
)


class PythonLineSpecifierMethodTests(unittest.TestCase):
    def assert_overlap(self, python_line: str, requires_python: str) -> None:
        result = evaluate_python_line_specifier(python_line, requires_python)
        self.assertIsInstance(result, PythonLineSpecifierEvaluation)
        assert isinstance(result, PythonLineSpecifierEvaluation)
        self.assertTrue(result.contains_stable_release)
        self.assertIsNotNone(result.witness_version)

    def assert_outside(self, python_line: str, requires_python: str) -> None:
        result = evaluate_python_line_specifier(python_line, requires_python)
        self.assertIsInstance(result, PythonLineSpecifierEvaluation)
        assert isinstance(result, PythonLineSpecifierEvaluation)
        self.assertFalse(result.contains_stable_release)
        self.assertIsNone(result.witness_version)

    def assert_problem(
        self,
        python_line: str,
        requires_python: str,
        state: str,
    ) -> PythonLineSpecifierProblem:
        result = evaluate_python_line_specifier(python_line, requires_python)
        self.assertIsInstance(result, PythonLineSpecifierProblem)
        assert isinstance(result, PythonLineSpecifierProblem)
        self.assertEqual(result.state, state)
        return result

    def test_lower_bound_at_line_start_overlaps(self) -> None:
        self.assert_overlap("3.9", ">=3.9")

    def test_patch_lower_bound_inside_line_overlaps(self) -> None:
        result = evaluate_python_line_specifier("3.9", ">=3.9.7")
        self.assertIsInstance(result, PythonLineSpecifierEvaluation)
        assert isinstance(result, PythonLineSpecifierEvaluation)
        self.assertEqual(result.witness_version, Version("3.9.7"))

    def test_very_high_patch_boundary_is_reached_without_a_fixed_ceiling(self) -> None:
        result = evaluate_python_line_specifier("3.9", ">=3.9.500000")
        self.assertIsInstance(result, PythonLineSpecifierEvaluation)
        assert isinstance(result, PythonLineSpecifierEvaluation)
        self.assertEqual(result.witness_version, Version("3.9.500000"))
        self.assertLessEqual(len(result.candidate_versions_checked), 4)

    def test_consecutive_exact_exclusions_advance_to_next_boundary_candidate(self) -> None:
        result = evaluate_python_line_specifier(
            "3.9",
            ">=3.9.500000,!=3.9.500000,!=3.9.500001",
        )
        self.assertIsInstance(result, PythonLineSpecifierEvaluation)
        assert isinstance(result, PythonLineSpecifierEvaluation)
        self.assertEqual(result.witness_version, Version("3.9.500002"))

    def test_later_lower_bound_excludes_line(self) -> None:
        self.assert_outside("3.9", ">=3.10")

    def test_wildcard_exclusion_removes_entire_line(self) -> None:
        self.assert_outside("3.9", "!=3.9.*")

    def test_compound_range_overlaps_line(self) -> None:
        self.assert_overlap("3.9", ">=3.8,<3.10")

    def test_wildcard_equality_selects_line(self) -> None:
        self.assert_overlap("3.9", "==3.9.*")

    def test_different_wildcard_equality_excludes_line(self) -> None:
        self.assert_outside("3.9", "==3.10.*")

    def test_compatible_release_at_line_start_overlaps(self) -> None:
        self.assert_overlap("3.9", "~=3.9")

    def test_compatible_release_for_later_line_excludes(self) -> None:
        self.assert_outside("3.9", "~=3.10")

    def test_compatible_patch_release_overlaps(self) -> None:
        self.assert_overlap("3.9", "~=3.9.7")

    def test_exact_patch_inside_line_overlaps(self) -> None:
        self.assert_overlap("3.9", "==3.9.7")

    def test_exact_release_in_later_line_excludes(self) -> None:
        self.assert_outside("3.9", "==3.10.0")

    def test_one_exact_patch_exclusion_does_not_remove_whole_line(self) -> None:
        result = evaluate_python_line_specifier("3.9", "!=3.9.0")
        self.assertIsInstance(result, PythonLineSpecifierEvaluation)
        assert isinstance(result, PythonLineSpecifierEvaluation)
        self.assertEqual(result.witness_version, Version("3.9.1"))

    def test_satisfiable_target_can_exclude_only_the_selected_line(self) -> None:
        self.assert_outside("3.9", ">=3.8,<3.11,!=3.9.*")

    def test_inclusive_upper_bound_at_line_start_overlaps(self) -> None:
        self.assert_overlap("3.9", "<=3.9")

    def test_exclusive_upper_bound_at_line_start_excludes(self) -> None:
        self.assert_outside("3.9", "<3.9")

    def test_exclusive_lower_bound_at_line_start_still_overlaps_later_patches(self) -> None:
        result = evaluate_python_line_specifier("3.9", ">3.9")
        self.assertIsInstance(result, PythonLineSpecifierEvaluation)
        assert isinstance(result, PythonLineSpecifierEvaluation)
        self.assertEqual(result.witness_version, Version("3.9.1"))

    def test_invalid_specifier_syntax_is_explicit(self) -> None:
        self.assert_problem("3.9", "not-a-specifier", "invalid_requires_python_specifier")

    def test_empty_specifier_is_invalid_for_target_declaration(self) -> None:
        self.assert_problem("3.9", "", "invalid_requires_python_specifier")

    def test_surrounding_whitespace_is_not_silently_normalized(self) -> None:
        self.assert_problem("3.9", " >=3.9 ", "invalid_requires_python_specifier")

    def test_arbitrary_equality_is_unsupported(self) -> None:
        self.assert_problem("3.9", "===3.9", "unsupported_requires_python_specifier")

    def test_prerelease_boundary_is_unsupported(self) -> None:
        self.assert_problem("3.9", ">=3.9rc1", "unsupported_requires_python_specifier")

    def test_development_boundary_is_unsupported(self) -> None:
        self.assert_problem("3.9", ">=3.9.dev1", "unsupported_requires_python_specifier")

    def test_post_release_boundary_is_unsupported(self) -> None:
        self.assert_problem("3.9", ">=3.9.post1", "unsupported_requires_python_specifier")

    def test_local_version_is_unsupported(self) -> None:
        self.assert_problem("3.9", "==3.9+local", "unsupported_requires_python_specifier")

    def test_epoch_version_is_unsupported(self) -> None:
        self.assert_problem("3.9", ">=1!3.9", "unsupported_requires_python_specifier")

    def test_more_than_three_release_components_are_unsupported(self) -> None:
        self.assert_problem("3.9", ">=3.9.1.1", "unsupported_requires_python_specifier")

    def test_unsatisfiable_target_declaration_is_not_ordinary_non_overlap(self) -> None:
        self.assert_problem("3.9", ">=3.10,<3.9", "unsatisfiable_requires_python_specifier")

    def test_python_line_with_leading_zero_is_invalid(self) -> None:
        self.assert_problem("03.9", ">=3.9", "invalid_python_line")

    def test_python_line_with_patch_component_is_invalid(self) -> None:
        self.assert_problem("3.9.1", ">=3.9", "invalid_python_line")

    def test_line_bounds_and_checked_candidates_are_preserved(self) -> None:
        result = evaluate_python_line_specifier("3.9", ">=3.9")
        self.assertIsInstance(result, PythonLineSpecifierEvaluation)
        assert isinstance(result, PythonLineSpecifierEvaluation)
        self.assertEqual(result.line_lower_bound, Version("3.9.0"))
        self.assertEqual(result.line_upper_bound, Version("3.10.0"))
        self.assertEqual(result.python_line, "3.9")
        self.assertEqual(result.requires_python, ">=3.9")
        self.assertEqual(result.normalized_requires_python, ">=3.9")
        self.assertEqual(result.candidate_versions_checked, (Version("3.9.0"),))
        self.assertEqual(result.witness_version, Version("3.9.0"))

    def test_method_uses_target_satisfiability_and_exact_contains(self) -> None:
        with (
            patch(
                "upgradepilot.target.python_specifier.SpecifierSet.is_unsatisfiable",
                return_value=False,
            ) as is_unsatisfiable,
            patch(
                "upgradepilot.target.python_specifier.SpecifierSet.contains",
                return_value=True,
            ) as contains,
        ):
            result = evaluate_python_line_specifier("3.9", ">=3.9")

        self.assertIsInstance(result, PythonLineSpecifierEvaluation)
        self.assertEqual(is_unsatisfiable.call_count, 1)
        self.assertGreaterEqual(contains.call_count, 1)


if __name__ == "__main__":
    unittest.main()
