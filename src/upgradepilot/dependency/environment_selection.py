"""Observe bounded static Python project-environment selectors in workflow run steps.

GitHub owns ``RunStepDefinition`` and workflow structure. This dependency-owned module
interprets only a small set of visible Python project selectors needed by current real
pressure: local-project pip installs and explicit uv extras/groups on ``uv sync`` or
``uv run``.

The result is static declaration evidence. A selector being visible does not establish
that the command executed, that an environment was formed, that a lock member is
reachable from the selected roots, or that the changed dependency was exercised.
"""

from __future__ import annotations

import re
import shlex
from dataclasses import dataclass
from typing import Literal

from packaging.utils import canonicalize_name

from ..github.workflow_definition import RunDefaults, RunStepDefinition
from ..repository_path import repository_relative_parts
from .workflow_context import (
    EffectiveWorkingDirectory,
    bounded_shell_segments,
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
type DependencyGroupSelectionMode = Literal["include", "only"]


@dataclass(frozen=True, slots=True)
class OptionalExtraSelector:
    """Visible selection of one named PEP 621 optional extra.

    ``name`` preserves command spelling; ``normalized_name`` is the comparison identity
    required by Python packaging extra-name semantics.
    """

    name: str

    @property
    def normalized_name(self) -> str:
        return str(canonicalize_name(self.name))


@dataclass(frozen=True, slots=True)
class DependencyGroupSelector:
    """Visible selection of one dependency group.

    ``mode='only'`` preserves uv's explicit ``--only-group`` spelling. Group comparison
    uses normalized names while the original command spelling remains available.
    """

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
    """One static command segment bound to one independently known project.

    ``selectors`` records only explicit positive selectors. An empty tuple is meaningful
    for a local-project pip install with no optional extra. For uv, omitted selectors are
    not promoted to an observed complete environment because uv default groups require
    separate project/config evidence.
    """

    manager: ProjectEnvironmentManager
    operation: ProjectEnvironmentOperation
    segment_index: int
    project_root: str | None
    selectors: tuple[ProjectEnvironmentSelector, ...]


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


_EXPRESSION_MARKER = "${{"
_ENV_ASSIGNMENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=.*$")
_PROJECT_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
_PIP_COMMAND = re.compile(
    r"^(?:[A-Za-z_][A-Za-z0-9_]*=[^\s]+\s+)*"
    r"(?:python(?:3)?\s+-m\s+pip|pip(?:3)?)\s+install\b",
    re.IGNORECASE,
)
_UV_COMMAND = re.compile(
    r"^(?:[A-Za-z_][A-Za-z0-9_]*=[^\s]+\s+)*uv\s+(?:sync|run)\b",
    re.IGNORECASE,
)

# These uv-run options consume one following token. This is deliberately not the whole uv
# CLI grammar. If an unknown option makes command delimitation ambiguous, the observer
# abstains rather than interpreting invoked-command arguments as uv selectors.
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


def observe_project_environment_selection(
    step: RunStepDefinition,
    *,
    project_file_path: str,
    workflow_defaults: RunDefaults | None = None,
    job_defaults: RunDefaults | None = None,
) -> ProjectEnvironmentSelectionObservation:
    """Observe explicit project extras/groups selected by one static run declaration.

    ``project_file_path`` must independently identify an exact repository-relative
    ``pyproject.toml``. The observer uses it only to bind local project commands; it does
    not parse project metadata or infer dependency membership.
    """

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

    declarations: list[ProjectEnvironmentSelectionDeclaration] = []
    unresolved_details: list[str] = []

    for segment_index, segment in enumerate(bounded_shell_segments(step.command.text)):
        if _PIP_COMMAND.match(segment):
            parsed, unresolved = _observe_pip_segment(
                segment,
                segment_index=segment_index,
                project_root=project_root,
                working_directory=working_directory,
            )
            declarations.extend(parsed)
            unresolved_details.extend(unresolved)
            continue

        if _UV_COMMAND.match(segment):
            parsed, unresolved = _observe_uv_segment(
                segment,
                segment_index=segment_index,
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
                "The static run step visibly selects the independently established "
                "project and preserves its explicit optional-extra/group selectors."
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
            "The static run step did not contain an admitted project-selection "
            "declaration for the independently established project."
        ),
        step_source_index=step.source_index,
        command=step.command.text,
        project_file_path=normalized_project_file,
        working_directory=working_directory,
    )


def _observe_pip_segment(
    segment: str,
    *,
    segment_index: int,
    project_root: str | None,
    working_directory: EffectiveWorkingDirectory,
) -> tuple[list[ProjectEnvironmentSelectionDeclaration], list[str]]:
    try:
        tokens = _strip_environment_assignments(shlex.split(segment, posix=True))
    except ValueError:
        return [], ["A plausible pip project-install declaration had malformed quoting."]

    install_args = _pip_install_args(tokens)
    if install_args is None:
        return [], []

    candidate_specs = _pip_local_project_specs(install_args)
    if not candidate_specs:
        return [], []

    if working_directory.state == "unresolved":
        return [], [
            "A pip local-project install was visible, but effective working-directory "
            "context was dynamic or invalid."
        ]

    declarations: list[ProjectEnvironmentSelectionDeclaration] = []
    unresolved: list[str] = []
    for spec in candidate_specs:
        if _EXPRESSION_MARKER in spec:
            unresolved.append(
                "A pip local-project requirement used a dynamic project path or extra."
            )
            continue

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
                segment_index=segment_index,
                project_root=project_root,
                selectors=tuple(OptionalExtraSelector(name) for name in extra_names),
            )
        )

    return declarations, unresolved


def _observe_uv_segment(
    segment: str,
    *,
    segment_index: int,
    project_root: str | None,
    working_directory: EffectiveWorkingDirectory,
) -> tuple[list[ProjectEnvironmentSelectionDeclaration], list[str]]:
    try:
        tokens = _strip_environment_assignments(shlex.split(segment, posix=True))
    except ValueError:
        return [], ["A plausible uv project-selection declaration had malformed quoting."]

    if len(tokens) < 2 or tokens[0] != "uv" or tokens[1] not in {"sync", "run"}:
        return [], []
    operation: ProjectEnvironmentOperation = tokens[1]  # type: ignore[assignment]
    raw_args = tokens[2:]
    args, parsing_incomplete = (
        (raw_args, False)
        if operation == "sync"
        else _uv_run_option_prefix(raw_args)
    )

    selectors, project_path, unresolved = _parse_uv_selection_args(args)
    material_flags = _uv_material_flags(args)

    if parsing_incomplete and _raw_uv_positive_selector_present(segment):
        unresolved.append(
            "A uv run selector was visible after option syntax the bounded parser "
            "could not safely delimit from the invoked command."
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

    if project_path is not None:
        if _EXPRESSION_MARKER in project_path:
            unresolved.append("The uv --project path was dynamic.")
            return [], unresolved
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
        # uv can discover a parent project, but proving which project wins requires exact
        # repository/project topology beyond this first selection observer.
        unresolved.append(
            "uv project discovery started outside the exact expected project root; "
            "parent/nested project discovery is not established by this rule."
        )
        return [], unresolved

    declaration = ProjectEnvironmentSelectionDeclaration(
        manager="uv",
        operation=operation,
        segment_index=segment_index,
        project_root=project_root,
        selectors=tuple(selectors),
    )

    if not selectors:
        unresolved.append(
            "A uv project command was bound to the project, but no explicit extra/group "
            "selector was visible; default-group selection requires project/config evidence."
        )
        return [declaration], unresolved

    return [declaration], unresolved


def _pip_install_args(tokens: list[str]) -> list[str] | None:
    if len(tokens) >= 2 and tokens[0] in {"pip", "pip3"} and tokens[1] == "install":
        return tokens[2:]
    if (
        len(tokens) >= 4
        and tokens[0] in {"python", "python3"}
        and tokens[1:4] == ["-m", "pip", "install"]
    ):
        return tokens[4:]
    return None


def _pip_local_project_specs(args: list[str]) -> list[str]:
    specs: list[str] = []
    i = 0
    while i < len(args):
        token = args[i]
        if token in {"-e", "--editable"}:
            if i + 1 < len(args):
                specs.append(args[i + 1])
                i += 2
                continue
            return specs
        if token.startswith("--editable="):
            specs.append(token.split("=", 1)[1])
            i += 1
            continue
        if token.startswith("-e") and token != "-e":
            specs.append(token[2:])
            i += 1
            continue
        if _looks_like_local_project_requirement(token):
            specs.append(token)
        i += 1
    return specs


def _looks_like_local_project_requirement(token: str) -> bool:
    return token == "." or token.startswith("./") or token.startswith("../")


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


def _uv_run_option_prefix(args: list[str]) -> tuple[list[str], bool]:
    prefix: list[str] = []
    i = 0
    while i < len(args):
        token = args[i]
        if token == "--":
            return prefix, False
        if not token.startswith("-"):
            return prefix, False

        prefix.append(token)
        option_name = token.split("=", 1)[0]
        if "=" not in token and option_name in _UV_RUN_VALUE_OPTIONS:
            if i + 1 >= len(args):
                return prefix, True
            prefix.append(args[i + 1])
            i += 2
            continue
        i += 1

    return prefix, False


def _parse_uv_selection_args(
    args: list[str],
) -> tuple[list[ProjectEnvironmentSelector], str | None, list[str]]:
    selectors: list[ProjectEnvironmentSelector] = []
    project_path: str | None = None
    unresolved: list[str] = []
    i = 0

    while i < len(args):
        token = args[i]
        option, inline_value = _split_option(token)

        if option in {"--extra", "--group", "--only-group", "--project"}:
            value = inline_value
            if value is None:
                if i + 1 >= len(args):
                    unresolved.append(f"uv option {option} lacked its required value.")
                    i += 1
                    continue
                value = args[i + 1]
                i += 1

            if _EXPRESSION_MARKER in value:
                unresolved.append(f"uv option {option} used a dynamic value.")
                i += 1
                continue

            if option == "--project":
                if project_path is not None and project_path != value:
                    unresolved.append("The uv declaration specified conflicting --project paths.")
                project_path = value
            elif _PROJECT_NAME.fullmatch(value) is None:
                unresolved.append(f"uv option {option} used an invalid literal selector name.")
            elif option == "--extra":
                _append_unique(selectors, OptionalExtraSelector(value))
            elif option == "--group":
                _append_unique(selectors, DependencyGroupSelector(value, mode="include"))
            else:
                _append_unique(selectors, DependencyGroupSelector(value, mode="only"))

            i += 1
            continue

        if option == "--all-extras":
            _append_unique(selectors, AllOptionalExtrasSelector())
        elif option == "--all-groups":
            _append_unique(selectors, AllDependencyGroupsSelector())

        i += 1

    return selectors, project_path, unresolved


def _raw_uv_positive_selector_present(segment: str) -> bool:
    return re.search(
        r"(?:^|\s)--(?:extra|group|only-group|all-extras|all-groups)(?:=|\s|$)",
        segment,
    ) is not None


def _uv_material_flags(args: list[str]) -> set[str]:
    """Return material uv options only from uv's option prefix, never child-command args."""

    found: set[str] = set()
    for token in args:
        option = token.split("=", 1)[0]
        if option in _UV_MATERIAL_NEGATIVE_OR_TARGETING_OPTIONS:
            found.add(option)
    return found


def _split_option(token: str) -> tuple[str, str | None]:
    if "=" not in token:
        return token, None
    option, value = token.split("=", 1)
    return option, value


def _strip_environment_assignments(tokens: list[str]) -> list[str]:
    index = 0
    while index < len(tokens) and _ENV_ASSIGNMENT.fullmatch(tokens[index]):
        index += 1
    return tokens[index:]


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
    "ProjectEnvironmentSelectionDeclaration",
    "ProjectEnvironmentSelectionObservation",
    "ProjectEnvironmentSelectionState",
    "ProjectEnvironmentSelector",
    "observe_project_environment_selection",
)
