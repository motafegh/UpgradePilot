from __future__ import annotations

import unittest

from upgradepilot.impact.applicability import (
    PropositionAssessment,
    evaluate_applicability_path,
    evaluate_candidate_applicability,
)


def _proposition(key: str, state: str) -> PropositionAssessment:
    coverage = "sufficient" if state in {"established", "refuted", "conflicted"} else "unresolved"
    return PropositionAssessment(
        key=key,
        state=state,  # type: ignore[arg-type]
        evidence_coverage=coverage,  # type: ignore[arg-type]
        evidence_owner="controlled-test",
        detail=f"Controlled {state} proposition.",
    )


def _path(key: str, *states: str):
    return evaluate_applicability_path(
        key,
        tuple(_proposition(f"{key}-{index}", state) for index, state in enumerate(states)),
    )


class ApplicabilityCompositionTests(unittest.TestCase):
    def test_complete_established_path_establishes_candidate(self) -> None:
        result = evaluate_candidate_applicability(
            (_path("primary", "established", "established"),),
            path_model_coverage="sufficient",
        )
        self.assertEqual(result.state, "established_applicable")

    def test_refuted_paths_with_sufficient_coverage_establish_not_applicable(self) -> None:
        result = evaluate_candidate_applicability(
            (_path("one", "refuted"), _path("two", "established", "refuted")),
            path_model_coverage="sufficient",
        )
        self.assertEqual(result.state, "established_not_applicable")

    def test_refuted_paths_without_sufficient_coverage_remain_unresolved(self) -> None:
        paths = (_path("one", "refuted"), _path("two", "refuted"))
        result = evaluate_candidate_applicability(
            paths,
            path_model_coverage="unresolved",
        )
        self.assertEqual(result.state, "unresolved")
        self.assertTrue(all(path.state == "refuted" for path in result.paths))
        self.assertEqual(result.path_model_coverage, "unresolved")

    def test_necessary_unresolved_proposition_keeps_path_unresolved(self) -> None:
        path = _path("primary", "established", "unresolved")
        self.assertEqual(path.state, "unresolved")

    def test_genuine_conflict_keeps_viable_path_conflicted(self) -> None:
        path = _path("primary", "established", "conflicted")
        self.assertEqual(path.state, "conflicted")

    def test_established_path_wins_without_erasing_conflicted_alternative(self) -> None:
        established = _path("established", "established")
        conflicted = _path("alternative", "conflicted")
        result = evaluate_candidate_applicability(
            (established, conflicted),
            path_model_coverage="sufficient",
        )
        self.assertEqual(result.state, "established_applicable")
        self.assertEqual(tuple(path.state for path in result.paths), ("established", "conflicted"))

    def test_unresolved_and_conflicted_alternatives_preserve_both_states(self) -> None:
        unresolved = _path("unresolved", "unresolved")
        conflicted = _path("conflicted", "conflicted")
        result = evaluate_candidate_applicability(
            (unresolved, conflicted),
            path_model_coverage="sufficient",
        )
        self.assertEqual(result.state, "conflicted")
        self.assertEqual(tuple(path.state for path in result.paths), ("unresolved", "conflicted"))

    def test_refuted_necessary_proposition_eliminates_path_despite_conflict_elsewhere(self) -> None:
        path = _path("primary", "refuted", "conflicted")
        self.assertEqual(path.state, "refuted")

    def test_empty_composition_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            evaluate_applicability_path("empty", ())
        with self.assertRaises(ValueError):
            evaluate_candidate_applicability((), path_model_coverage="sufficient")


if __name__ == "__main__":
    unittest.main()
