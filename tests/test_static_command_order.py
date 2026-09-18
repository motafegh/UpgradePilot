from __future__ import annotations

import unittest

from upgradepilot.ci.consumption import StaticDependencyConsumptionEvidence
from upgradepilot.ci.static_command_order import relate_invocation_after_consumption
from upgradepilot.ci.workflow_commands import DirectPackageInvocationEvidence
from upgradepilot.github.workflow_command_analysis import CommandSourceSpan
from upgradepilot.github.workflow_command_location import StaticCommandLocation


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


def _consumption(
    *,
    step_source_index: int,
    source_order: int | None = None,
    structural_context: tuple[str, ...] = ("straightforward_top_level",),
) -> StaticDependencyConsumptionEvidence:
    return StaticDependencyConsumptionEvidence(
        state="supported",
        mechanism="direct_requirements",
        normalized_package="pytest",
        workflow_path=".github/workflows/ci.yml",
        workflow_revision="a" * 40,
        job_key="test",
        step_source_index=step_source_index,
        command="synthetic",
        reason="direct_requirements_consumption_declared",
        detail="synthetic",
        source_path="requirements-dev.txt",
        command_location=(
            _location(source_order) if source_order is not None else None
        ),
        structural_context=structural_context,  # type: ignore[arg-type]
    )


def _invocation(
    *,
    step_source_index: int,
    source_order: int | None = None,
    structural_context: tuple[str, ...] = ("straightforward_top_level",),
) -> DirectPackageInvocationEvidence:
    return DirectPackageInvocationEvidence(
        state="observed",
        job_key="test",
        step_source_index=step_source_index,
        command="synthetic",
        command_location=(
            _location(source_order) if source_order is not None else None
        ),
        structural_context=structural_context,  # type: ignore[arg-type]
    )


class StaticCommandOrderTests(unittest.TestCase):
    def test_later_run_step_is_ordered_after(self) -> None:
        relation = relate_invocation_after_consumption(
            _consumption(step_source_index=1, source_order=0),
            _invocation(step_source_index=2, source_order=0),
        )
        self.assertEqual(relation, "ordered_after")

    def test_clean_same_step_source_order_is_ordered_after(self) -> None:
        relation = relate_invocation_after_consumption(
            _consumption(step_source_index=1, source_order=0),
            _invocation(step_source_index=1, source_order=1),
        )
        self.assertEqual(relation, "ordered_after")

    def test_later_short_circuit_occurrence_is_unresolved_not_supported(self) -> None:
        relation = relate_invocation_after_consumption(
            _consumption(
                step_source_index=1,
                source_order=0,
                structural_context=("short_circuit",),
            ),
            _invocation(
                step_source_index=1,
                source_order=1,
                structural_context=("short_circuit",),
            ),
        )
        self.assertEqual(relation, "unresolved")

    def test_new_cycle3_path_dependent_structures_do_not_earn_same_step_order(self) -> None:
        for structure in (
            "status_inverted",
            "asynchronous",
            "process_substitution",
        ):
            with self.subTest(structure=structure):
                relation = relate_invocation_after_consumption(
                    _consumption(
                        step_source_index=1,
                        source_order=0,
                        structural_context=(structure,),
                    ),
                    _invocation(
                        step_source_index=1,
                        source_order=1,
                        structural_context=("straightforward_top_level",),
                    ),
                )
                self.assertEqual(relation, "unresolved")

    def test_invocation_before_consumption_is_not_after_even_if_path_dependent(self) -> None:
        relation = relate_invocation_after_consumption(
            _consumption(
                step_source_index=1,
                source_order=1,
                structural_context=("short_circuit",),
            ),
            _invocation(
                step_source_index=1,
                source_order=0,
                structural_context=("short_circuit",),
            ),
        )
        self.assertEqual(relation, "not_after")

    def test_missing_same_step_command_identity_is_unresolved(self) -> None:
        relation = relate_invocation_after_consumption(
            _consumption(step_source_index=1, source_order=None),
            _invocation(step_source_index=1, source_order=1),
        )
        self.assertEqual(relation, "unresolved")


if __name__ == "__main__":
    unittest.main()
