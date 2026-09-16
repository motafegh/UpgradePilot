"""Shared bounded recognition of parsed pip-install command prefixes.

This dependency-owned helper answers only whether one parser-neutral command occurrence has
the admitted ``pip install`` or ``python -m pip install`` prefix and, when so, returns the
remaining typed argument atoms. It does not interpret requirements files, local projects,
extras, execution, or success.
"""

from __future__ import annotations

from ..github.workflow_command_analysis import StaticCommandAtom, StaticCommandOccurrence


def parsed_pip_install_arguments(
    occurrence: StaticCommandOccurrence,
) -> tuple[tuple[StaticCommandAtom, ...] | None, bool]:
    """Return install arguments plus whether an admitted prefix is materially unresolved.

    ``(None, False)`` means the occurrence is not an admitted pip-install shape.
    ``(None, True)`` means a literal admitted executable/prefix was visible but a material
    prefix atom was dynamic or unsupported.
    """

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
    if module_switch is None:
        return None, True
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


def _literal_casefold(atom: StaticCommandAtom) -> str | None:
    if atom.state != "literal" or atom.literal_value is None:
        return None
    return atom.literal_value.casefold()


__all__ = ("parsed_pip_install_arguments",)
