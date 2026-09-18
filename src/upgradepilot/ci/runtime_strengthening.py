"""CI-owned runtime-strengthening candidate and eligibility classification.

This module does not correlate runtime steps or interpret GitHub runtime conclusions.
It converts already-produced static occurrence evidence into the bounded eligibility state
accepted by Cycle 3:

provider/static occurrence facts
+ execution profile
→ eligible | ineligible | unresolved

Tree-sitter nodes never enter this module.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..github.workflow_command_analysis import (
    StaticCommandStructure,
    StaticCommandWholeStepRelation,
)
from ..github.workflow_command_location import StaticCommandLocation
from ..github.workflow_command_shell import ShellExecutionProfile


type RuntimeStrengtheningPropositionKind = Literal[
    "dependency_consumption",
    "direct_package_exercise",
]
type RuntimeStrengtheningEligibilityState = Literal[
    "eligible",
    "ineligible",
    "unresolved",
]


@dataclass(frozen=True, slots=True)
class RuntimeStrengtheningCandidate:
    """Exact static occurrence context considered for later runtime strengthening."""

    proposition_kind: RuntimeStrengtheningPropositionKind
    workflow_path: str | None
    workflow_revision: str | None
    job_key: str
    step_source_index: int
    command_location: StaticCommandLocation | None
    structural_context: tuple[StaticCommandStructure, ...]
    whole_step_relation: StaticCommandWholeStepRelation | None
    execution_profile: ShellExecutionProfile | None


@dataclass(frozen=True, slots=True)
class RuntimeStrengtheningEligibility:
    """CI policy result for one exact runtime-strengthening candidate."""

    state: RuntimeStrengtheningEligibilityState
    reason: str
    detail: str


_KNOWN_INELIGIBLE_STRUCTURES = frozenset(
    {
        "conditional",
        "loop",
        "function_or_block",
        "status_inverted",
        "asynchronous",
        "process_substitution",
    }
)

_SOLE_COMMAND_EXECUTION_PROFILES = frozenset(
    {
        "github_builtin_bash",
        "github_builtin_sh",
        "github_builtin_pwsh",
        "github_builtin_powershell",
        "github_builtin_cmd",
        "github_default_non_windows",
        "github_default_windows",
        "github_default_container_sh",
    }
)

_FIRST_SEQUENTIAL_BASH_EXECUTION_PROFILES = frozenset(
    {
        "github_builtin_bash",
        "github_builtin_sh",
        "github_default_non_windows",
        "github_default_container_sh",
    }
)


def classify_runtime_strengthening_eligibility(
    candidate: RuntimeStrengtheningCandidate,
) -> RuntimeStrengtheningEligibility:
    """Classify whether step-level runtime evidence may strengthen this occurrence.

    This function intentionally does not inspect runtime correlation or runtime status.
    """

    known_ineligible = next(
        (
            structure
            for structure in candidate.structural_context
            if structure in _KNOWN_INELIGIBLE_STRUCTURES
        ),
        None,
    )
    if known_ineligible is not None:
        return RuntimeStrengtheningEligibility(
            state="ineligible",
            reason="runtime_strengthening_structure_ineligible",
            detail=(
                "The exact static occurrence is inside a positively identified structure "
                f"({known_ineligible}) whose containing step may succeed without providing "
                "the admitted runtime-correlated support for this occurrence."
            ),
        )

    if (
        not candidate.workflow_path
        or not candidate.workflow_revision
        or not candidate.job_key
        or candidate.command_location is None
    ):
        return RuntimeStrengtheningEligibility(
            state="unresolved",
            reason="runtime_strengthening_occurrence_identity_unresolved",
            detail=(
                "The stronger runtime proposition requires exact workflow/job/step/command "
                "occurrence identity, but the supplied static evidence does not preserve it."
            ),
        )

    if candidate.execution_profile is None:
        return RuntimeStrengtheningEligibility(
            state="unresolved",
            reason="runtime_strengthening_execution_profile_unresolved",
            detail=(
                "The exact static occurrence is known, but its effective GitHub Actions "
                "execution profile is not established for runtime-strengthening policy."
            ),
        )

    if candidate.execution_profile == "custom_shell_template":
        return RuntimeStrengtheningEligibility(
            state="unresolved",
            reason="runtime_strengthening_custom_execution_profile_unresolved",
            detail=(
                "The command syntax family may be parsed, but a custom shell template does "
                "not inherit GitHub's built-in wrapper guarantees."
            ),
        )

    if candidate.whole_step_relation == "sole_ordinary_top_level_command":
        if candidate.execution_profile in _SOLE_COMMAND_EXECUTION_PROFILES:
            return RuntimeStrengtheningEligibility(
                state="eligible",
                reason="sole_ordinary_top_level_command_runtime_strengthening_eligible",
                detail=(
                    "The provider positively established this exact occurrence as the sole "
                    "ordinary top-level command under an admitted GitHub execution profile."
                ),
            )

    if (
        candidate.whole_step_relation
        == "first_ordinary_top_level_command_in_sequential_script"
    ):
        if candidate.execution_profile in _FIRST_SEQUENTIAL_BASH_EXECUTION_PROFILES:
            return RuntimeStrengtheningEligibility(
                state="eligible",
                reason="first_sequential_bash_command_runtime_strengthening_eligible",
                detail=(
                    "The provider positively established this exact occurrence as the first "
                    "ordinary top-level command in a sequential Bash/sh script under an "
                    "admitted GitHub fail-fast execution profile."
                ),
            )
        return RuntimeStrengtheningEligibility(
            state="unresolved",
            reason="first_sequential_command_execution_profile_unresolved",
            detail=(
                "The first-sequential positive relation is admitted only for the selected "
                "GitHub Bash/sh execution profiles."
            ),
        )

    return RuntimeStrengtheningEligibility(
        state="unresolved",
        reason="runtime_strengthening_positive_structure_not_established",
        detail=(
            "No currently admitted positive whole-step relationship establishes runtime "
            "strengthening for this exact occurrence. The structure is not converted into "
            "a negative conclusion merely because stronger support was not earned."
        ),
    )


__all__ = (
    "RuntimeStrengtheningCandidate",
    "RuntimeStrengtheningEligibility",
    "RuntimeStrengtheningEligibilityState",
    "RuntimeStrengtheningPropositionKind",
    "classify_runtime_strengthening_eligibility",
)
