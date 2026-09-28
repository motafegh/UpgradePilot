"""Parse one bounded static package-manager operation from parser-neutral command atoms.

This dependency-owned boundary recognizes the supported pip-install invocation forms once and
preserves command identity for downstream semantic consumers. It does not establish execution,
effective environment/configuration, package mutation, or resulting package state.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Literal

from ..github.workflow_command_analysis import StaticCommandAtom, StaticCommandOccurrence
from ..github.workflow_command_location import StaticCommandLocation


type PackageManagerName = Literal["pip"]
type PackageManagerOperationName = Literal["install"]
type PackageManagerInvocationForm = Literal["pip_executable", "python_module"]
type PackageManagerOperationProblemState = Literal["unresolved", "unsupported"]


@dataclass(frozen=True, slots=True)
class PackageManagerOperationDeclaration:
    """Static identity and arguments for one supported package-manager operation."""

    manager: PackageManagerName
    operation: PackageManagerOperationName
    invocation_form: PackageManagerInvocationForm
    launcher: str
    python_interpreter: str | None
    manager_global_arguments: tuple[StaticCommandAtom, ...]
    operation_arguments: tuple[StaticCommandAtom, ...]
    command_location: StaticCommandLocation


@dataclass(frozen=True, slots=True)
class PackageManagerOperationProblem:
    """Why a recognizable package-manager invocation could not be declared safely."""

    state: PackageManagerOperationProblemState
    reason: str
    detail: str
    command_location: StaticCommandLocation


_PYTHON_INTERPRETER = re.compile(r"^python(?:\d+(?:\.\d+)*)?(?:\.exe)?$", re.IGNORECASE)
_PIP_GLOBAL_BOOLEAN_OPTIONS = frozenset({"--isolated"})
_PIP_GLOBAL_VALUE_OPTIONS = frozenset({"--python"})


def parse_package_manager_operation(
    occurrence: StaticCommandOccurrence,
) -> PackageManagerOperationDeclaration | PackageManagerOperationProblem | None:
    """Return one supported pip-install declaration, an explicit problem, or no match."""

    executable = _literal_value(occurrence.executable)
    if executable is None:
        return None

    invocation_form: PackageManagerInvocationForm
    python_interpreter: str | None = None

    if executable.casefold() in {"pip", "pip3"}:
        invocation_form = "pip_executable"
        remaining = occurrence.arguments
    elif _is_supported_python_interpreter(executable):
        remaining_or_problem = _python_module_pip_arguments(occurrence)
        if isinstance(remaining_or_problem, PackageManagerOperationProblem):
            return remaining_or_problem
        if remaining_or_problem is None:
            return None
        invocation_form = "python_module"
        python_interpreter = executable
        remaining = remaining_or_problem
    else:
        return None

    global_arguments: list[StaticCommandAtom] = []
    index = 0
    while index < len(remaining):
        atom = remaining[index]
        token = _literal_value(atom)

        if token is None:
            if atom.raw_source.strip().casefold().startswith("--python="):
                global_arguments.append(atom)
                index += 1
                continue
            return _problem(
                occurrence,
                "pip_global_option_unresolved",
                (
                    "A recognizable pip invocation had a dynamic/unsupported token before "
                    "the install operation."
                ),
            )

        folded = token.casefold()
        if folded == "install":
            return PackageManagerOperationDeclaration(
                manager="pip",
                operation="install",
                invocation_form=invocation_form,
                launcher=executable,
                python_interpreter=python_interpreter,
                manager_global_arguments=tuple(global_arguments),
                operation_arguments=remaining[index + 1 :],
                command_location=StaticCommandLocation.from_occurrence(occurrence),
            )

        if folded in _PIP_GLOBAL_BOOLEAN_OPTIONS:
            global_arguments.append(atom)
            index += 1
            continue

        if folded in _PIP_GLOBAL_VALUE_OPTIONS:
            global_arguments.append(atom)
            if index + 1 >= len(remaining):
                return _problem(
                    occurrence,
                    "pip_global_option_missing_value",
                    f"pip global option {token!r} is missing its required value.",
                )
            global_arguments.append(remaining[index + 1])
            index += 2
            continue

        if folded.startswith("--python="):
            global_arguments.append(atom)
            index += 1
            continue

        if token.startswith("-"):
            if not _literal_install_visible(remaining[index + 1 :]):
                return None
            return _problem(
                occurrence,
                "unsupported_pip_global_option_before_install",
                (
                    f"pip global option {token!r} before install is outside the admitted "
                    "Increment-2 operation-declaration surface."
                ),
                state="unsupported",
            )

        return None

    return None


def _literal_install_visible(arguments: tuple[StaticCommandAtom, ...]) -> bool:
    return any(
        (value := _literal_value(atom)) is not None and value.casefold() == "install"
        for atom in arguments
    )


def _python_module_pip_arguments(
    occurrence: StaticCommandOccurrence,
) -> tuple[StaticCommandAtom, ...] | PackageManagerOperationProblem | None:
    arguments = occurrence.arguments
    if not arguments:
        return None

    module_switch = _literal_value(arguments[0])
    if module_switch is None:
        return _problem(
            occurrence,
            "pip_module_switch_unresolved",
            "A supported Python launcher had a dynamic/unsupported module switch.",
        )
    if module_switch.casefold() != "-m" or len(arguments) < 2:
        return None

    module_name = _literal_value(arguments[1])
    if module_name is None:
        return _problem(
            occurrence,
            "pip_module_name_unresolved",
            "A supported Python -m invocation had a dynamic/unsupported module name.",
        )
    if module_name.casefold() != "pip":
        return None

    return arguments[2:]


def _problem(
    occurrence: StaticCommandOccurrence,
    reason: str,
    detail: str,
    *,
    state: PackageManagerOperationProblemState = "unresolved",
) -> PackageManagerOperationProblem:
    return PackageManagerOperationProblem(
        state=state,
        reason=reason,
        detail=detail,
        command_location=StaticCommandLocation.from_occurrence(occurrence),
    )


def _is_supported_python_interpreter(token: str) -> bool:
    basename = token.replace("\\", "/").rsplit("/", 1)[-1]
    return _PYTHON_INTERPRETER.fullmatch(basename) is not None


def _literal_value(atom: StaticCommandAtom) -> str | None:
    if atom.state != "literal" or atom.literal_value is None:
        return None
    return atom.literal_value


__all__ = (
    "PackageManagerOperationDeclaration",
    "PackageManagerOperationProblem",
    "parse_package_manager_operation",
)
