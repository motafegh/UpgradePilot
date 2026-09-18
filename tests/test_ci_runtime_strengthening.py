from __future__ import annotations

import unittest

from upgradepilot.ci.consumption import StaticDependencyConsumptionEvidence
from upgradepilot.ci.runtime_strengthening import (
    RuntimeStrengtheningCandidate,
    candidate_from_consumption,
    candidate_from_direct_exercise,
    classify_runtime_strengthening_eligibility,
)
from upgradepilot.ci.workflow_commands import DirectPackageInvocationEvidence
from upgradepilot.github.workflow_command_analysis import CommandSourceSpan
from upgradepilot.github.workflow_command_location import StaticCommandLocation


_PATH = ".github/workflows/ci.yml"
_REVISION = "a" * 40


def _location(source_order: int) -> StaticCommandLocation:
    return StaticCommandLocation(
        source_span=CommandSourceSpan(
            start_byte=source_order * 10,
            end_byte=source_order * 10 + 5,
            start_line=source_order,
            start_column=0,
            end_line=source_order,
            end_column=5,
        ),
        source_order=source_order,
    )


def _candidate(
    *,
    structural_context: tuple[str, ...] = ("straightforward_top_level",),
    whole_step_relation: str | None = "sole_ordinary_top_level_command",
    execution_profile: str | None = "github_builtin_bash",
    source_order: int | None = 0,
) -> RuntimeStrengtheningCandidate:
    return RuntimeStrengtheningCandidate(
        proposition_kind="dependency_consumption",
        workflow_path=_PATH,
        workflow_revision=_REVISION,
        job_key="test",
        step_source_index=1,
        command_location=_location(source_order) if source_order is not None else None,
        structural_context=structural_context,  # type: ignore[arg-type]
        whole_step_relation=whole_step_relation,  # type: ignore[arg-type]
        execution_profile=execution_profile,  # type: ignore[arg-type]
    )


class RuntimeStrengtheningEligibilityTests(unittest.TestCase):
    def test_sole_command_positive_is_eligible_for_admitted_profiles(self) -> None:
        for profile in (
            "github_builtin_bash",
            "github_builtin_pwsh",
            "github_builtin_cmd",
            "github_default_non_windows",
            "github_default_windows",
            "github_default_container_sh",
        ):
            with self.subTest(profile=profile):
                result = classify_runtime_strengthening_eligibility(
                    _candidate(execution_profile=profile)
                )
                self.assertEqual(result.state, "eligible")

    def test_first_sequential_positive_requires_bash_or_sh_profile(self) -> None:
        relation = "first_ordinary_top_level_command_in_sequential_script"

        bash = classify_runtime_strengthening_eligibility(
            _candidate(
                structural_context=("linear_chain",),
                whole_step_relation=relation,
                execution_profile="github_default_non_windows",
            )
        )
        powershell = classify_runtime_strengthening_eligibility(
            _candidate(
                structural_context=("linear_chain",),
                whole_step_relation=relation,
                execution_profile="github_builtin_pwsh",
            )
        )

        self.assertEqual(bash.state, "eligible")
        self.assertEqual(powershell.state, "unresolved")

    def test_known_disqualifying_structures_are_ineligible(self) -> None:
        for structure in (
            "conditional",
            "loop",
            "function_or_block",
            "status_inverted",
            "asynchronous",
            "process_substitution",
        ):
            with self.subTest(structure=structure):
                result = classify_runtime_strengthening_eligibility(
                    _candidate(
                        structural_context=(structure,),
                        whole_step_relation=None,
                    )
                )
                self.assertEqual(result.state, "ineligible")

    def test_coarse_or_unadmitted_structures_remain_unresolved(self) -> None:
        for structure in (
            "short_circuit",
            "pipeline",
            "nested_or_subshell",
            "linear_chain",
            "straightforward_top_level",
        ):
            with self.subTest(structure=structure):
                result = classify_runtime_strengthening_eligibility(
                    _candidate(
                        structural_context=(structure,),
                        whole_step_relation=None,
                    )
                )
                self.assertEqual(result.state, "unresolved")

    def test_custom_execution_profile_remains_unresolved(self) -> None:
        result = classify_runtime_strengthening_eligibility(
            _candidate(execution_profile="custom_shell_template")
        )
        self.assertEqual(result.state, "unresolved")
        self.assertEqual(
            result.reason,
            "runtime_strengthening_custom_execution_profile_unresolved",
        )

    def test_missing_exact_occurrence_identity_remains_unresolved(self) -> None:
        result = classify_runtime_strengthening_eligibility(
            _candidate(source_order=None)
        )
        self.assertEqual(result.state, "unresolved")
        self.assertEqual(
            result.reason,
            "runtime_strengthening_occurrence_identity_unresolved",
        )

    def test_same_step_consumption_occurrences_remain_distinct_candidates(self) -> None:
        first = StaticDependencyConsumptionEvidence(
            state="supported",
            mechanism="direct_requirements",
            normalized_package="pytest",
            workflow_path=_PATH,
            workflow_revision=_REVISION,
            job_key="test",
            step_source_index=1,
            command="synthetic",
            reason="supported",
            detail="synthetic",
            command_location=_location(0),
            structural_context=("linear_chain",),
            whole_step_relation=(
                "first_ordinary_top_level_command_in_sequential_script"
            ),
            execution_profile="github_builtin_bash",
        )
        second = StaticDependencyConsumptionEvidence(
            state="supported",
            mechanism="direct_requirements",
            normalized_package="pytest",
            workflow_path=_PATH,
            workflow_revision=_REVISION,
            job_key="test",
            step_source_index=1,
            command="synthetic",
            reason="supported",
            detail="synthetic",
            command_location=_location(1),
            structural_context=("linear_chain",),
            whole_step_relation=None,
            execution_profile="github_builtin_bash",
        )

        first_candidate = candidate_from_consumption(first)
        second_candidate = candidate_from_consumption(second)

        self.assertNotEqual(
            first_candidate.command_location,
            second_candidate.command_location,
        )
        self.assertEqual(
            classify_runtime_strengthening_eligibility(first_candidate).state,
            "eligible",
        )
        self.assertEqual(
            classify_runtime_strengthening_eligibility(second_candidate).state,
            "unresolved",
        )

    def test_direct_exercise_factory_preserves_exact_identity_and_kind(self) -> None:
        evidence = DirectPackageInvocationEvidence(
            state="observed",
            job_key="test",
            step_source_index=2,
            command="pytest tests",
            command_location=_location(3),
            structural_context=("straightforward_top_level",),
            whole_step_relation="sole_ordinary_top_level_command",
            execution_profile="github_builtin_bash",
            workflow_path=_PATH,
            workflow_revision=_REVISION,
        )

        candidate = candidate_from_direct_exercise(evidence)

        self.assertEqual(candidate.proposition_kind, "direct_package_exercise")
        self.assertEqual(candidate.command_location, _location(3))
        self.assertEqual(
            classify_runtime_strengthening_eligibility(candidate).state,
            "eligible",
        )


if __name__ == "__main__":
    unittest.main()
