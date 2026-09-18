"""Observe bounded static Python project-environment selectors in parsed workflow commands.

GitHub owns workflow structure and parser-neutral command analysis. This dependency-owned
module interprets only the small Python project-selection semantics required by current real
pressure: local-project pip installs and explicit uv extras/groups plus the bounded uv package
scope that makes those selectors meaningful on ``uv sync`` or ``uv run``.

The result is static declaration evidence. A selector or package scope being visible does not
establish command execution, environment formation, dependency reachability, or package
exercise.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Literal

from packaging.utils import canonicalize_name

from ..github.workflow_command_analysis import (
    StaticCommandAnalysis,
    StaticCommandAtom,
    StaticCommandOccurrence,
    StaticCommandStructure,
    StaticCommandWholeStepRelation,
)
from ..github.workflow_command_location import StaticCommandLocation
from ..github.workflow_definition import RunDefaults, RunStepDefinition
from ..repository_path import repository_relative_parts
from .pip_command import parsed_pip_install_arguments
from .workflow_context import (
    EffectiveWorkingDirectory,
    resolve_effective_working_directory,
    resolve_repository_relative_path,
)


type ProjectEnvironmentSelectionState = Literal[
    "observed",
    "not_observed",
    "unresolved",
]
type ProjectEnvironmentManager = Literal["pip", "uv"]
type ProjectEnvironmentOperation = Literal["install", "sync", "run"]
type ProjectEnvironmentPackageScope = Literal[
    "bound_project",
    "all_workspace_packages",
]
type DependencyGroupSelectionMode = Literal["include", "only"]


@dataclass(frozen=True, slots=True)
class OptionalExtraSelector:
    """Visible selection of one named PEP 621 optional extra."""

    name: str

    @property
    def normalized_name(self) -> str:
        return str(canonicalize_name(self.name))


@dataclass(frozen=True, slots=True)
class DependencyGroupSelector:
    """Visible selection of one dependency group."""

    name: str
    mode: DependencyGroupSelectionMode = "include"

    @property
    def normalized_name(self) -> str:
        return str(canonicalize_name(self.name))


@dataclass(frozen=True, slots=True)
class AllOptionalExtrasSelector:
    """Visible request to include all project optional extras."""


@dataclass(frozen=True, slots=True)
class AllDependencyGroupsSelector:
    """Visible request to include all project dependency groups."""


type ProjectEnvironmentSelector = (
    OptionalExtraSelector
    | DependencyGroupSelector
    | AllOptionalExtrasSelector
    | AllDependencyGroupsSelector
)


@dataclass(frozen=True, slots=True)
class ProjectEnvironmentSelectionDeclaration:
    """One parsed static command occurrence bound to one independently known project.

    ``command_location`` is the canonical static occurrence identity and
    ``structural_context`` preserves the provider-established source structure needed by
    later CI ordering. Neither proves execution or success.
    """

    manager: ProjectEnvironmentManager
    operation: ProjectEnvironmentOperation
    project_root: str | None
    selectors: tuple[ProjectEnvironmentSelector, ...]
    package_scope: ProjectEnvironmentPackageScope = "bound_project"
    command_location: StaticCommandLocation | None = None
    structural_context: tuple[StaticCommandStructure, ...] = ()
    whole_step_relation: StaticCommandWholeStepRelation | None = None


@dataclass(frozen=True, slots=True)
class ProjectEnvironmentSelectionObservation:
    """Static project-selection evidence for one provider-owned run step."""

    state: ProjectEnvironmentSelectionState
    reason: str
    detail: str
    step_source_index: int
    command: str
    project_file_path: str
    working_directory: EffectiveWorkingDirectory
    declarations: tuple[ProjectEnvironmentSelectionDeclaration, ...] = ()


_PROJECT_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")

_UV_RUN_VALUE_OPTIONS = frozenset(
    {
        "--extra",
        "--group",
        "--only-group",
        "--project",
        "--python",
        "-p",
        "--with",
        "--with-editable",
        "--index",
        "--index-url",
        "--extra-index-url",
        "--find-links",
    }
)
_UV_MATERIAL_NEGATIVE_OR_TARGETING_OPTIONS = frozenset(
    {
        "--no-extra",
        "--no-group",
        "--directory",
        "--package",
        "--no-project",
    }
)
_UV_UNSUPPORTED_PACKAGE_SCOPE_OPTIONS = frozenset(
    {
        "--directory",
        "--package",
        "--no-project",
    }
)
_UV_VALUE_SELECTION_OPTIONS = frozenset(
    {"--extra", "--group", "--only-group", "--project"}
)


def observe_project_environment_selection(
    step: RunStepDefinition,
    *,
    project_file_path: str,
    command_analysis: StaticCommandAnalysis,
    workflow_defaults: RunDefaults | None = None,
    job_defaults: RunDefaults | None = None,
) -> ProjectEnvironmentSelectionObservation:
    """Observe explicit project extras/groups from shared parser-neutral command analysis."""

    project_parts = repository_relative_parts(project_file_path)
    if project_parts is None or project_parts[-1] != "pyproject.toml":
        raise ValueError(
            "project_file_path must be a normalized repository-relative pyproject.toml path"
        )
    normalized_project_file = "/".join(project_parts)
    project_root = "/".join(project_parts[:-1]) or None

    working_directory = resolve_effective_working_directory(
        step,
        workflow_defaults=workflow_defaults,
        job_defaults=job_defaults,
    )

    if command_analysis.state != "analyzable":
        problem_reasons = ", ".join(
            dict.fromkeys(problem.reason for problem in command_analysis.problems)
        )
        suffix = f" ({problem_reasons})" if problem_reasons else ""
        return ProjectEnvironmentSelectionObservation(
            state="unresolved",
            reason="project_environment_command_analysis_unresolved",
            detail=(
                "Static command analysis could not safely establish the run-step command "
                f"structure{suffix}; no textual fallback was used."
            ),
            step_source_index=step.source_index,
            command=step.command.text,
            project_file_path=normalized_project_file,
            working_directory=working_directory,
        )

    declarations: list[ProjectEnvironmentSelectionDeclaration] = []
    unresolved_details: list[str] = []

    for occurrence in command_analysis.command_occurrences:
        install_args, pip_prefix_unresolved = parsed_pip_install_arguments(occurrence)
        if pip_prefix_unresolved:
            unresolved_details.append(
                "A plausible pip install command had a dynamic or unsupported material prefix."
            )
        elif install_args is not None:
            parsed, unresolved = _observe_pip_occurrence(
                occurrence,
                install_args=install_args,
                project_root=project_root,
                working_directory=working_directory,
            )
            declarations.extend(parsed)
            unresolved_details.extend(unresolved)

        uv_operation, uv_args, uv_prefix_unresolved = _uv_command_arguments(occurrence)
        if uv_prefix_unresolved:
            unresolved_details.append(
                "A plausible uv project command had a dynamic or unsupported operation."
            )
        elif uv_operation is not None and uv_args is not None:
            parsed, unresolved = _observe_uv_occurrence(
                occurrence,
                operation=uv_operation,
                raw_args=uv_args,
                project_root=project_root,
                working_directory=working_directory,
            )
            declarations.extend(parsed)
            unresolved_details.extend(unresolved)

    if unresolved_details:
        return ProjectEnvironmentSelectionObservation(
            state="unresolved",
            reason="project_environment_selection_unresolved",
            detail="; ".join(dict.fromkeys(unresolved_details)),
            step_source_index=step.source_index,
            command=step.command.text,
            project_file_path=normalized_project_file,
            working_directory=working_directory,
            declarations=tuple(declarations),
        )

    if declarations:
        return ProjectEnvironmentSelectionObservation(
            state="observed",
            reason="project_environment_selection_declared",
            detail=(
                "Parsed static command occurrences visibly select the independently "
                "established project and preserve explicit optional-extra/group selectors "
                "and admitted package scope."
            ),
            step_source_index=step.source_index,
            command=step.command.text,
            project_file_path=normalized_project_file,
            working_directory=working_directory,
            declarations=tuple(declarations),
        )

    return ProjectEnvironmentSelectionObservation(
        state="not_observed",
        reason="project_environment_selection_not_observed",
        detail=(
            "The parsed static run step did not contain an admitted project-selection "
            "declaration for the independently established project."
        ),
        step_source_index=step.source_index,
        command=step.command.text,
        project_file_path=normalized_project_file,
        working_directory=working_directory,
    )


def _observe_pip_occurrence(
    occurrence: StaticCommandOccurrence,
    *,
    install_args: tuple[StaticCommandAtom, ...],
    project_root: str | None,
    working_directory: EffectiveWorkingDirectory,
) -> tuple[list[ProjectEnvironmentSelectionDeclaration], list[str]]:
    candidate_specs, material_unresolved = _pip_local_project_specs(install_args)
    if not candidate_specs and not material_unresolved:
        return [], []

    if working_directory.state == "unresolved":
        return [], [
            "A pip local-project install was visible, but effective working-directory "
            "context was dynamic or invalid."
        ]

    declarations: list[ProjectEnvironmentSelectionDeclaration] = []
    unresolved: list[str] = []
    if material_unresolved:
        unresolved.append(
            "A pip local-project requirement used a dynamic or unsupported material value."
        )

    for spec in candidate_specs:
        parsed = _parse_local_project_requirement(spec)
        if parsed is None:
            continue
        raw_path, extra_names = parsed
        resolved_root = resolve_repository_relative_path(
            raw_path,
            working_directory.path,
        )
        if resolved_root != project_root:
            continue

        declarations.append(
            ProjectEnvironmentSelectionDeclaration(
                manager="pip",
                operation="install",
                project_root=project_root,
                selectors=tuple(OptionalExtraSelector(name) for name in extra_names),
                command_location=StaticCommandLocation.from_occurrence(occurrence),
                structural_context=occurrence.structural_context,
                whole_step_relation=occurrence.whole_step_relation,
            )
        )

    return declarations, unresolved


def _pip_local_project_specs(
    args: tuple[StaticCommandAtom, ...],
) -> tuple[list[str], bool]:
    specs: list[str] = []
    unresolved = False
    index = 0

    while index < len(args):
        atom = args[index]
        literal = _literal_value(atom)
        if literal is None:
            if _dynamic_looks_like_local_project_requirement(atom):
                unresolved = True
            index += 1
            continue

        if literal in {"-e", "--editable"}:
            if index + 1 >= len(args):
                unresolved = True
                index += 1
                continue
            value = _literal_value(args[index + 1])
            if value is None:
                unresolved = True
            else:
                specs.append(value)
            index += 2
            continue

        if literal.startswith("--editable="):
            value = literal.split("=", 1)[1]
            if value:
                specs.append(value)
            else:
                unresolved = True
            index += 1
            continue

        if literal.startswith("-e") and literal != "-e":
            specs.append(literal[2:])
            index += 1
            continue

        if _looks_like_local_project_requirement(literal):
            specs.append(literal)
        index += 1

    return specs, unresolved


def _dynamic_looks_like_local_project_requirement(atom: StaticCommandAtom) -> bool:
    raw = atom.raw_source.strip().strip("'\"")
    return _looks_like_local_project_requirement(raw)


def _looks_like_local_project_requirement(token: str) -> bool:
    return (
        token == "."
        or token.startswith(".[")
        or token.startswith("./")
        or token.startswith("../")
    )


def _parse_local_project_requirement(spec: str) -> tuple[str, tuple[str, ...]] | None:
    if not _looks_like_local_project_requirement(spec):
        return None

    if "[" not in spec:
        return spec, ()
    if not spec.endswith("]"):
        return None

    raw_path, raw_extras = spec.rsplit("[", 1)
    raw_extras = raw_extras[:-1]
    if not raw_path or not raw_extras:
        return None

    names: list[str] = []
    for raw_name in raw_extras.split(","):
        name = raw_name.strip()
        if _PROJECT_NAME.fullmatch(name) is None:
            return None
        if name not in names:
            names.append(name)
    return raw_path, tuple(names)


def _uv_command_arguments(
    occurrence: StaticCommandOccurrence,
) -> tuple[
    ProjectEnvironmentOperation | None,
    tuple[StaticCommandAtom, ...] | None,
    bool,
]:
    executable = _literal_casefold(occurrence.executable)
    if executable != "uv":
        return None, None, False
    if not occurrence.arguments:
        return None, None, False

    operation = _literal_casefold(occurrence.arguments[0])
    if operation is None:
        return None, None, True
    if operation not in {"sync", "run"}:
        return None, None, False
    return operation, occurrence.arguments[1:], False  # type: ignore[return-value]


def _observe_uv_occurrence(
    occurrence: StaticCommandOccurrence,
    *,
    operation: ProjectEnvironmentOperation,
    raw_args: tuple[StaticCommandAtom, ...],
    project_root: str | None,
    working_directory: EffectiveWorkingDirectory,
) -> tuple[list[ProjectEnvironmentSelectionDeclaration], list[str]]:
    args, parsing_incomplete = (
        (raw_args, False)
        if operation == "sync"
        else _uv_run_option_prefix(raw_args)
    )

    (
        selectors,
        project_path,
        project_path_unresolved,
        package_scope,
        unresolved,
    ) = _parse_uv_selection_args(args)
    material_flags = _uv_material_flags(args)

    if parsing_incomplete:
        unresolved.append(
            "A uv run option prefix could not be safely delimited from the invoked command."
        )

    if material_flags:
        unresolved.append(
            "The uv declaration used a negative or project-targeting selector outside "
            "the first bounded positive-selection rule: "
            + ", ".join(sorted(material_flags))
            + "."
        )

    if working_directory.state == "unresolved":
        unresolved.append(
            "A uv project declaration was visible, but effective working-directory "
            "context was dynamic or invalid."
        )
        return [], unresolved

    if material_flags & _UV_UNSUPPORTED_PACKAGE_SCOPE_OPTIONS:
        return [], unresolved

    if project_path_unresolved:
        return [], unresolved

    if project_path is not None:
        resolved_project_root = resolve_repository_relative_path(
            project_path,
            working_directory.path,
        )
        if resolved_project_root is None:
            unresolved.append("The uv --project path could not be resolved safely.")
            return [], unresolved
        if resolved_project_root != project_root:
            return [], unresolved
    elif working_directory.path != project_root:
        unresolved.append(
            "uv project discovery started outside the exact expected project root; "
            "parent/nested project discovery is not established by this rule."
        )
        return [], unresolved

    declaration = ProjectEnvironmentSelectionDeclaration(
        manager="uv",
        operation=operation,
        project_root=project_root,
        selectors=tuple(selectors),
        package_scope=package_scope,
        command_location=StaticCommandLocation.from_occurrence(occurrence),
        structural_context=occurrence.structural_context,
        whole_step_relation=occurrence.whole_step_relation,
    )

    if not selectors:
        unresolved.append(
            "A uv project command was bound to the project, but no explicit extra/group "
            "selector was visible; default-group selection requires project/config evidence."
        )
        return [declaration], unresolved

    return [declaration], unresolved


def _uv_run_option_prefix(
    args: tuple[StaticCommandAtom, ...],
) -> tuple[tuple[StaticCommandAtom, ...], bool]:
    prefix: list[StaticCommandAtom] = []
    index = 0

    while index < len(args):
        atom = args[index]
        token = _literal_value(atom)
        if token is None:
            return tuple(prefix), True
        if token == "--":
            return tuple(prefix), False
        if not token.startswith("-"):
            return tuple(prefix), False

        prefix.append(atom)
        option_name = token.split("=", 1)[0]
        if "=" not in token and option_name in _UV_RUN_VALUE_OPTIONS:
            if index + 1 >= len(args):
                return tuple(prefix), True
            prefix.append(args[index + 1])
            index += 2
            continue
        index += 1

    return tuple(prefix), False


def _parse_uv_selection_args(
    args: tuple[StaticCommandAtom, ...],
) -> tuple[
    list[ProjectEnvironmentSelector],
    str | None,
    bool,
    ProjectEnvironmentPackageScope,
    list[str],
]:
    selectors: list[ProjectEnvironmentSelector] = []
    project_path: str | None = None
    project_path_unresolved = False
    package_scope: ProjectEnvironmentPackageScope = "bound_project"
    unresolved: list[str] = []
    index = 0

    while index < len(args):
        atom = args[index]
        token = _literal_value(atom)
        if token is None:
            material_option = _dynamic_material_uv_option(atom)
            if material_option is not None:
                unresolved.append(
                    f"uv option {material_option} used a dynamic or unsupported value."
                )
                if material_option == "--project":
                    project_path_unresolved = True
            index += 1
            continue

        option, inline_value = _split_option(token)

        if option in _UV_VALUE_SELECTION_OPTIONS:
            value = inline_value
            if value is None:
                if index + 1 >= len(args):
                    unresolved.append(f"uv option {option} lacked its required value.")
                    if option == "--project":
                        project_path_unresolved = True
                    index += 1
                    continue
                value_atom = args[index + 1]
                value = _literal_value(value_atom)
                if value is None:
                    unresolved.append(f"uv option {option} used a dynamic value.")
                    if option == "--project":
                        project_path_unresolved = True
                    index += 2
                    continue
                index += 1

            if option == "--project":
                if project_path is not None and project_path != value:
                    unresolved.append(
                        "The uv declaration specified conflicting --project paths."
                    )
                project_path = value
            elif _PROJECT_NAME.fullmatch(value) is None:
                unresolved.append(
                    f"uv option {option} used an invalid literal selector name."
                )
            elif option == "--extra":
                _append_unique(selectors, OptionalExtraSelector(value))
            elif option == "--group":
                _append_unique(selectors, DependencyGroupSelector(value, mode="include"))
            else:
                _append_unique(selectors, DependencyGroupSelector(value, mode="only"))

            index += 1
            continue

        if option == "--all-extras":
            _append_unique(selectors, AllOptionalExtrasSelector())
        elif option == "--all-groups":
            _append_unique(selectors, AllDependencyGroupsSelector())
        elif option == "--all-packages":
            package_scope = "all_workspace_packages"

        index += 1

    return (
        selectors,
        project_path,
        project_path_unresolved,
        package_scope,
        unresolved,
    )


def _uv_material_flags(args: tuple[StaticCommandAtom, ...]) -> set[str]:
    """Return material uv options only from uv's option prefix, never child-command args."""

    found: set[str] = set()
    for atom in args:
        token = _literal_value(atom)
        if token is not None:
            option = token.split("=", 1)[0]
            if option in _UV_MATERIAL_NEGATIVE_OR_TARGETING_OPTIONS:
                found.add(option)
            continue
        dynamic_option = _dynamic_material_uv_option(atom)
        if dynamic_option in _UV_MATERIAL_NEGATIVE_OR_TARGETING_OPTIONS:
            found.add(dynamic_option)
    return found


def _dynamic_material_uv_option(atom: StaticCommandAtom) -> str | None:
    raw = atom.raw_source.strip().strip("'\"").casefold()
    material = (
        _UV_VALUE_SELECTION_OPTIONS
        | _UV_MATERIAL_NEGATIVE_OR_TARGETING_OPTIONS
    )
    for option in material:
        if raw == option or raw.startswith(f"{option}="):
            return option
    return None


def _split_option(token: str) -> tuple[str, str | None]:
    if "=" not in token:
        return token, None
    option, value = token.split("=", 1)
    return option, value


def _literal_value(atom: StaticCommandAtom) -> str | None:
    if atom.state != "literal" or atom.literal_value is None:
        return None
    return atom.literal_value


def _literal_casefold(atom: StaticCommandAtom) -> str | None:
    value = _literal_value(atom)
    return value.casefold() if value is not None else None


def _append_unique(
    selectors: list[ProjectEnvironmentSelector],
    selector: ProjectEnvironmentSelector,
) -> None:
    if selector not in selectors:
        selectors.append(selector)


__all__ = (
    "AllDependencyGroupsSelector",
    "AllOptionalExtrasSelector",
    "DependencyGroupSelector",
    "DependencyGroupSelectionMode",
    "OptionalExtraSelector",
    "ProjectEnvironmentManager",
    "ProjectEnvironmentOperation",
    "ProjectEnvironmentPackageScope",
    "ProjectEnvironmentSelectionDeclaration",
    "ProjectEnvironmentSelectionObservation",
    "ProjectEnvironmentSelectionState",
    "ProjectEnvironmentSelector",
    "observe_project_environment_selection",
)
