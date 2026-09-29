"""Provider-owned executable-selection evidence for exact static commands.

This module records only what the command syntax itself positively establishes about
executable selection. It does not interpret package-manager semantics, prove filesystem
existence, resolve PATH, or infer virtual-environment identity.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .workflow_command_analysis import StaticCommandOccurrence
from .workflow_command_location import StaticCommandLocation


type StaticExecutableSelectionState = Literal["established", "unresolved"]
type StaticExecutableSelectionKind = Literal[
    "explicit_path",
    "path_lookup_required",
    "executable_dynamic",
]


@dataclass(frozen=True, slots=True)
class StaticExecutableSelectionObservation:
    """Selection evidence for the executable of one exact command occurrence."""

    state: StaticExecutableSelectionState
    kind: StaticExecutableSelectionKind
    executable: str | None
    reason: str
    detail: str
    command_location: StaticCommandLocation


def observe_command_executable_selection(
    occurrence: StaticCommandOccurrence,
) -> StaticExecutableSelectionObservation:
    """Preserve explicit executable paths and fail closed on PATH-dependent names."""

    location = StaticCommandLocation.from_occurrence(occurrence)
    atom = occurrence.executable
    if atom.state != "literal" or atom.literal_value is None:
        return StaticExecutableSelectionObservation(
            state="unresolved",
            kind="executable_dynamic",
            executable=None,
            reason="command_executable_not_literal",
            detail=(
                "The exact command executable is dynamic or unsupported, so executable "
                "selection cannot be established from command syntax."
            ),
            command_location=location,
        )

    executable = atom.literal_value
    normalized = executable.replace("\\", "/")
    if "/" in normalized:
        return StaticExecutableSelectionObservation(
            state="established",
            kind="explicit_path",
            executable=executable,
            reason="explicit_executable_path",
            detail=(
                "The exact command names an executable path directly; no PATH lookup is "
                "required to identify the selected command path relation."
            ),
            command_location=location,
        )

    return StaticExecutableSelectionObservation(
        state="unresolved",
        kind="path_lookup_required",
        executable=executable,
        reason="bare_executable_requires_path_resolution",
        detail=(
            f"The exact command uses bare executable {executable!r}; effective PATH or "
            "another provider/runtime selector is required before executable identity "
            "can be established."
        ),
        command_location=location,
    )


__all__ = (
    "StaticExecutableSelectionObservation",
    "observe_command_executable_selection",
)
