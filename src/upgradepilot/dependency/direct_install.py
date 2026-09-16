"""Observe bounded direct dependency-install declarations in static workflow run steps.

This dependency-owned responsibility interprets provider-owned static command analysis
against one independently established repository-relative dependency source path. Its proof
strength stops at visible declaration/configuration: it does not establish command execution,
success, installed versions, general dependency consumption, or package exercise.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..github.workflow_command_analysis import StaticCommandAnalysis, StaticCommandAtom
from ..github.workflow_command_location import StaticCommandLocation
from ..github.workflow_definition import RunDefaults, RunStepDefinition
from ..repository_path import repository_relative_parts
from .pip_command import parsed_pip_install_arguments
from .workflow_context import (
    EffectiveWorkingDirectory,
    WorkingDirectorySource,
    WorkingDirectoryState,
    resolve_effective_working_directory,
    resolve_repository_relative_path,
)


type DirectInstallDeclarationState = Literal["observed", "not_observed", "unresolved"]


@dataclass(frozen=True, slots=True)
class DirectInstallDeclarationObservation:
    """Static relation between one run step and one known dependency-source path.

    ``command_location`` identifies the specific parsed static command occurrence when one is
    established. It is source identity only; it does not imply execution, success, or
    same-path ordering.
    """

    state: DirectInstallDeclarationState
    reason: str
    detail: str
    step_source_index: int
    command: str
    dependency_source_path: str
    working_directory: EffectiveWorkingDirectory
    matched_requirement_path: str | None = None
    command_location: StaticCommandLocation | None = None


def observe_direct_installation_declaration(
    step: RunStepDefinition,
    *,
    dependency_source_path: str,
    command_analysis: StaticCommandAnalysis,
    workflow_defaults: RunDefaults | None = None,
    job_defaults: RunDefaults | None = None,
) -> DirectInstallDeclarationObservation:
    """Observe whether one parsed static run step directly names the dependency source file."""

    dependency_parts = repository_relative_parts(dependency_source_path)
    if dependency_parts is None:
        raise ValueError(
            "dependency_source_path must be a normalized repository-relative POSIX path"
        )
    normalized_source = "/".join(dependency_parts)

    working_directory = resolve_effective_working_directory(
        step,
        workflow_defaults=workflow_defaults,
        job_defaults=job_defaults,
    )

    return _observe_direct_installation_from_analysis(
        step,
        command_analysis=command_analysis,
        normalized_source=normalized_source,
        working_directory=working_directory,
    )


def _observe_direct_installation_from_analysis(
    step: RunStepDefinition,
    *,
    command_analysis: StaticCommandAnalysis,
    normalized_source: str,
    working_directory: EffectiveWorkingDirectory,
) -> DirectInstallDeclarationObservation:
    """Interpret direct-requirements meaning from shared parser-neutral command atoms."""

    if command_analysis.state != "analyzable":
        problem_reasons = ", ".join(
            dict.fromkeys(problem.reason for problem in command_analysis.problems)
        )
        suffix = f" ({problem_reasons})" if problem_reasons else ""
        return DirectInstallDeclarationObservation(
            state="unresolved",
            reason="direct_install_command_analysis_unresolved",
            detail=(
                "Static command analysis could not safely establish the run-step command "
                f"structure{suffix}; no textual fallback was used."
            ),
            step_source_index=step.source_index,
            command=step.command.text,
            dependency_source_path=normalized_source,
            working_directory=working_directory,
        )

    direct_requirement_paths: list[str] = []
    unresolved_seen = False
    unresolved_location: StaticCommandLocation | None = None

    for occurrence in command_analysis.command_occurrences:
        install_arguments, prefix_unresolved = parsed_pip_install_arguments(occurrence)
        if prefix_unresolved:
            unresolved_seen = True
            if unresolved_location is None:
                unresolved_location = StaticCommandLocation.from_occurrence(occurrence)
            continue
        if install_arguments is None:
            continue

        requirement_paths, arguments_unresolved = _requirement_paths_from_atoms(
            install_arguments
        )
        if arguments_unresolved:
            unresolved_seen = True
            if unresolved_location is None:
                unresolved_location = StaticCommandLocation.from_occurrence(occurrence)

        for raw_path in requirement_paths:
            direct_requirement_paths.append(raw_path)
            if working_directory.state == "unresolved":
                unresolved_seen = True
                if unresolved_location is None:
                    unresolved_location = StaticCommandLocation.from_occurrence(occurrence)
                continue

            resolved = resolve_repository_relative_path(
                raw_path,
                working_directory.path,
            )
            if resolved is None:
                unresolved_seen = True
                if unresolved_location is None:
                    unresolved_location = StaticCommandLocation.from_occurrence(occurrence)
                continue
            if resolved == normalized_source:
                return DirectInstallDeclarationObservation(
                    state="observed",
                    reason="direct_requirements_install_declared",
                    detail=(
                        "The static run step directly declares installation from the "
                        "independently established dependency source path."
                    ),
                    step_source_index=step.source_index,
                    command=step.command.text,
                    dependency_source_path=normalized_source,
                    working_directory=working_directory,
                    matched_requirement_path=raw_path,
                    command_location=StaticCommandLocation.from_occurrence(occurrence),
                )

    if unresolved_seen:
        return DirectInstallDeclarationObservation(
            state="unresolved",
            reason="direct_install_path_context_unresolved",
            detail=(
                "A plausible direct pip requirements-file declaration was visible, but a "
                "material command token, requirements path, or working-directory relation "
                "could not be safely resolved."
            ),
            step_source_index=step.source_index,
            command=step.command.text,
            dependency_source_path=normalized_source,
            working_directory=working_directory,
            command_location=unresolved_location,
        )

    if direct_requirement_paths:
        detail = (
            "Direct pip requirements-file declarations were visible, but none resolved "
            "to the independently established dependency source path."
        )
        reason = "dependency_source_not_directly_declared"
    else:
        detail = (
            "The static run step did not contain an admitted direct pip "
            "requirements-file declaration."
        )
        reason = "direct_requirements_install_not_observed"

    return DirectInstallDeclarationObservation(
        state="not_observed",
        reason=reason,
        detail=detail,
        step_source_index=step.source_index,
        command=step.command.text,
        dependency_source_path=normalized_source,
        working_directory=working_directory,
    )


def _requirement_paths_from_atoms(
    arguments: tuple[StaticCommandAtom, ...],
) -> tuple[tuple[str, ...], bool]:
    """Read bounded ``-r/--requirement`` values without reparsing shell source."""

    paths: list[str] = []
    unresolved = False
    index = 0

    while index < len(arguments):
        atom = arguments[index]
        if atom.state != "literal" or atom.literal_value is None:
            unresolved = True
            index += 1
            continue

        token = atom.literal_value
        folded = token.casefold()
        if folded in {"-r", "--requirement"}:
            if index + 1 >= len(arguments):
                unresolved = True
                index += 1
                continue
            value_atom = arguments[index + 1]
            if value_atom.state != "literal" or value_atom.literal_value is None:
                unresolved = True
            else:
                paths.append(value_atom.literal_value)
            index += 2
            continue

        if folded.startswith("--requirement=") or folded.startswith("-r="):
            value = token.split("=", 1)[1]
            if value:
                paths.append(value)
            else:
                unresolved = True

        index += 1

    return tuple(paths), unresolved


__all__ = (
    "DirectInstallDeclarationObservation",
    "DirectInstallDeclarationState",
    "EffectiveWorkingDirectory",
    "WorkingDirectorySource",
    "WorkingDirectoryState",
    "observe_direct_installation_declaration",
)
