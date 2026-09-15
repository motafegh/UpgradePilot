"""Observe bounded direct dependency-install declarations in static workflow run steps.

This dependency-owned responsibility interprets provider-owned static command analysis
against one independently established repository-relative dependency source path. Its proof
strength stops at visible declaration/configuration: it does not establish command execution,
success, installed versions, general dependency consumption, or package exercise.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Literal

from ..github.workflow_command_analysis import (
    StaticCommandAnalysis,
    StaticCommandAtom,
    StaticCommandOccurrence,
)
from ..github.workflow_command_location import StaticCommandLocation
from ..github.workflow_definition import RunDefaults, RunStepDefinition
from ..repository_path import repository_relative_parts
from .workflow_context import (
    EffectiveWorkingDirectory,
    WorkingDirectorySource,
    WorkingDirectoryState,
    bounded_shell_segments,
    resolve_effective_working_directory,
    resolve_repository_relative_path,
)


type DirectInstallDeclarationState = Literal["observed", "not_observed", "unresolved"]


@dataclass(frozen=True, slots=True)
class DirectInstallDeclarationObservation:
    """Static relation between one run step and one known dependency-source path.

    ``command_location`` is the provider-owned identity of the specific parsed command
    occurrence when one is established. It is static source identity only; it does not imply
    execution, success, or same-path ordering.

    ``matched_segment_index`` is retained temporarily for the still-unmigrated CI caller in
    Cycle 2 Build. New parser-backed observations leave it unset; it is not the new identity
    contract and will be removed when the CI composition seam is migrated.
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
    matched_segment_index: int | None = None


_DIRECT_PIP_INSTALL_PATTERN = re.compile(
    r"^(?:[A-Za-z_][A-Za-z0-9_]*=[^\s]+\s+)*"
    r"(?:python(?:3)?\s+-m\s+pip|pip(?:3)?)\s+install\b",
    re.IGNORECASE,
)
_REQUIREMENT_PATTERN = re.compile(
    r"(?:^|\s)(?:-r|--requirement)(?:=|\s+)(?P<path>[^\s;&|]+)",
    re.IGNORECASE,
)
_EXPRESSION_MARKER = "${{"


def observe_direct_installation_declaration(
    step: RunStepDefinition,
    *,
    dependency_source_path: str,
    command_analysis: StaticCommandAnalysis | None = None,
    workflow_defaults: RunDefaults | None = None,
    job_defaults: RunDefaults | None = None,
) -> DirectInstallDeclarationObservation:
    """Observe whether one static run step directly names the dependency source file.

    Effective ``working-directory`` follows the shared static dependency-domain context:
    ``step > job defaults.run > workflow defaults.run > repository root``.

    ``command_analysis`` is the Cycle 2 parser-backed input. When supplied, this observer
    consumes only typed command occurrences/atoms and never reconstructs shell structure from
    raw text. Analysis or material-token uncertainty remains ``unresolved`` rather than
    falling back to regex/text segmentation.

    The optional legacy route exists only while the CI orchestration caller is migrated in
    the next bounded Build slice. It preserves current product behavior for that unmigrated
    caller and is not a positive-evidence fallback for parser-backed observations.
    """

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

    if command_analysis is not None:
        return _observe_direct_installation_from_analysis(
            step,
            command_analysis=command_analysis,
            normalized_source=normalized_source,
            working_directory=working_directory,
        )

    return _observe_direct_installation_legacy(
        step,
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
        install_arguments, prefix_unresolved = _direct_pip_install_arguments(occurrence)
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


def _direct_pip_install_arguments(
    occurrence: StaticCommandOccurrence,
) -> tuple[tuple[StaticCommandAtom, ...] | None, bool]:
    """Return pip-install arguments or whether an admitted prefix is materially unresolved."""

    executable = _literal_casefold(occurrence.executable)
    if executable is None:
        return None, False

    arguments = occurrence.arguments
    if executable in {"pip", "pip3"}:
        if not arguments:
            return None, False
        operation = _literal_casefold(arguments[0])
        if operation is None:
            return None, True
        if operation != "install":
            return None, False
        return arguments[1:], False

    if executable not in {"python", "python3"} or not arguments:
        return None, False

    module_switch = _literal_casefold(arguments[0])
    if module_switch != "-m":
        return None, False
    if len(arguments) < 2:
        return None, False

    module_name = _literal_casefold(arguments[1])
    if module_name is None:
        return None, True
    if module_name != "pip":
        return None, False
    if len(arguments) < 3:
        return None, False

    operation = _literal_casefold(arguments[2])
    if operation is None:
        return None, True
    if operation != "install":
        return None, False
    return arguments[3:], False


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


def _literal_casefold(atom: StaticCommandAtom) -> str | None:
    if atom.state != "literal" or atom.literal_value is None:
        return None
    return atom.literal_value.casefold()


def _observe_direct_installation_legacy(
    step: RunStepDefinition,
    *,
    normalized_source: str,
    working_directory: EffectiveWorkingDirectory,
) -> DirectInstallDeclarationObservation:
    """Temporary Cycle 2 compatibility route for the not-yet-migrated CI caller."""

    direct_requirement_paths: list[str] = []
    unresolved_path_seen = False

    for segment_index, segment in enumerate(bounded_shell_segments(step.command.text)):
        if _DIRECT_PIP_INSTALL_PATTERN.match(segment) is None:
            continue
        for match in _REQUIREMENT_PATTERN.finditer(segment):
            raw_path = match.group("path").strip("'\"")
            direct_requirement_paths.append(raw_path)

            if _EXPRESSION_MARKER in raw_path:
                unresolved_path_seen = True
                continue
            if working_directory.state == "unresolved":
                unresolved_path_seen = True
                continue

            resolved = resolve_repository_relative_path(
                raw_path,
                working_directory.path,
            )
            if resolved is None:
                unresolved_path_seen = True
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
                    matched_segment_index=segment_index,
                )

    if unresolved_path_seen:
        return DirectInstallDeclarationObservation(
            state="unresolved",
            reason="direct_install_path_context_unresolved",
            detail=(
                "A direct pip requirements-file declaration was visible, but its path "
                "could not be safely resolved against the effective working-directory "
                "context."
            ),
            step_source_index=step.source_index,
            command=step.command.text,
            dependency_source_path=normalized_source,
            working_directory=working_directory,
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


__all__ = (
    "DirectInstallDeclarationObservation",
    "DirectInstallDeclarationState",
    "EffectiveWorkingDirectory",
    "WorkingDirectorySource",
    "WorkingDirectoryState",
    "observe_direct_installation_declaration",
)
