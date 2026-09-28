"""Resolve bounded command-local package-manager semantic facts.

Semantic resolvers consume a previously parsed PackageManagerOperationDeclaration. They never
reparse shell text or command identity. A positive fact is emitted only when command-line
evidence is decisive for that semantic dimension; otherwise an explicit problem preserves the
next unresolved source required by the accepted demand-driven precedence model.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..github.workflow_command_analysis import StaticCommandAtom
from ..github.workflow_command_location import StaticCommandLocation
from .package_manager_operation import PackageManagerName, PackageManagerOperationDeclaration


type PackageManagerSemanticDimension = Literal[
    "manager_environment",
    "installation_destination",
    "package_mutation_mode",
    "direct_requirement_handling",
]
type PackageManagerSemanticProblemState = Literal["unresolved", "unsupported"]
type PackageManagerSemanticSourceKind = Literal[
    "command_line",
    "executable_selection",
    "process_environment",
    "persistent_configuration",
    "manager_default",
]
type PackageManagerSemanticSourceDisposition = Literal[
    "non_overriding",
    "disabled",
    "decisive",
]
type PackageManagerEnvironmentKind = Literal["pip_python_target"]
type InstallationDestinationKind = Literal[
    "target_directory",
    "user_scheme",
    "prefix_scheme",
    "root_relocated_scheme",
]
type PackageMutationMode = Literal["apply_changes", "dry_run"]
type DirectRequirementHandling = Literal["handled", "excluded"]


@dataclass(frozen=True, slots=True)
class PackageManagerSemanticResolutionStep:
    """One inspected source in a bounded semantic-resolution trace."""

    source_kind: PackageManagerSemanticSourceKind
    disposition: PackageManagerSemanticSourceDisposition
    detail: str
    locator: str | None = None


@dataclass(frozen=True, slots=True)
class PackageManagerSemanticResolutionProvenance:
    """Why one semantic source was allowed to decide a dimension."""

    dimension: PackageManagerSemanticDimension
    inspected_sources: tuple[PackageManagerSemanticResolutionStep, ...]
    winning_source: PackageManagerSemanticSourceKind


@dataclass(frozen=True, slots=True)
class PackageManagerSemanticProblem:
    """Explicit unresolved/unsupported edge for one semantic dimension."""

    state: PackageManagerSemanticProblemState
    dimension: PackageManagerSemanticDimension
    reason: str
    detail: str
    command_location: StaticCommandLocation
    resolved_prefix: tuple[PackageManagerSemanticResolutionStep, ...] = ()
    blocking_source: PackageManagerSemanticSourceKind | None = None


@dataclass(frozen=True, slots=True)
class PackageManagerEnvironmentReference:
    """Concrete command-line manager-environment selection."""

    kind: PackageManagerEnvironmentKind
    value: str


@dataclass(frozen=True, slots=True)
class ManagerEnvironmentSelectionFact:
    manager: PackageManagerName
    command_location: StaticCommandLocation
    environment: PackageManagerEnvironmentReference
    provenance: PackageManagerSemanticResolutionProvenance


@dataclass(frozen=True, slots=True)
class InstallationDestination:
    """Concrete command-line installation destination selector."""

    kind: InstallationDestinationKind
    value: str | None = None


@dataclass(frozen=True, slots=True)
class InstallationDestinationFact:
    manager: PackageManagerName
    command_location: StaticCommandLocation
    destination: InstallationDestination
    provenance: PackageManagerSemanticResolutionProvenance


@dataclass(frozen=True, slots=True)
class PackageMutationModeFact:
    manager: PackageManagerName
    command_location: StaticCommandLocation
    mode: PackageMutationMode
    provenance: PackageManagerSemanticResolutionProvenance


@dataclass(frozen=True, slots=True)
class DirectRequirementHandlingFact:
    manager: PackageManagerName
    command_location: StaticCommandLocation
    handling: DirectRequirementHandling
    provenance: PackageManagerSemanticResolutionProvenance


_DESTINATION_VALUE_OPTIONS: dict[str, InstallationDestinationKind] = {
    "--target": "target_directory",
    "-t": "target_directory",
    "--prefix": "prefix_scheme",
    "--root": "root_relocated_scheme",
}
_DESTINATION_BOOLEAN_OPTIONS: dict[str, InstallationDestinationKind] = {
    "--user": "user_scheme",
}
_VALUE_TAKING_INSTALL_OPTIONS = frozenset(
    {
        "-r",
        "--requirement",
        "-e",
        "--editable",
        "-t",
        "--target",
        "--prefix",
        "--root",
    }
)


def resolve_manager_environment_selection(
    declaration: PackageManagerOperationDeclaration,
) -> ManagerEnvironmentSelectionFact | PackageManagerSemanticProblem:
    """Resolve explicit pip --python or preserve the next lower source edge."""

    values = _global_option_values(declaration, "--python")
    if len(values) > 1:
        return _problem(
            declaration,
            "manager_environment",
            "multiple_pip_python_targets",
            (
                "Multiple pip --python selectors are outside the admitted deterministic "
                "manager-environment surface."
            ),
            state="unsupported",
            blocking_source="command_line",
        )
    if values:
        value = values[0]
        if value is None:
            return _problem(
                declaration,
                "manager_environment",
                "pip_python_target_unresolved",
                "pip --python is present but its target value is dynamic or unsupported.",
                blocking_source="command_line",
            )
        step = _command_line_step(
            "decisive",
            "Explicit pip --python selects the manager target before lower-precedence sources.",
            locator="--python",
        )
        return ManagerEnvironmentSelectionFact(
            manager=declaration.manager,
            command_location=declaration.command_location,
            environment=PackageManagerEnvironmentReference(
                kind="pip_python_target",
                value=value,
            ),
            provenance=_provenance("manager_environment", step),
        )

    return _problem(
        declaration,
        "manager_environment",
        "manager_environment_needs_lower_source_evidence",
        (
            "The invocation form is preserved, but no decisive pip --python selector is "
            "visible. Process-environment/configuration/executable evidence is still required "
            "before effective manager environment can be asserted."
        ),
        resolved_prefix=(
            _command_line_step(
                "non_overriding",
                "No command-line pip --python retargeter is present.",
                locator="--python",
            ),
        ),
        blocking_source="process_environment",
    )


def resolve_installation_destination(
    declaration: PackageManagerOperationDeclaration,
) -> InstallationDestinationFact | PackageManagerSemanticProblem:
    """Resolve one explicit pip destination selector or preserve the lower-source edge."""

    selectors: list[InstallationDestination] = []
    arguments = declaration.operation_arguments
    index = 0

    while index < len(arguments):
        atom = arguments[index]
        token = _literal_value(atom)
        if token is None:
            dynamic_name = _dynamic_inline_destination(atom.raw_source)
            if dynamic_name is not None:
                return _problem(
                    declaration,
                    "installation_destination",
                    "installation_destination_value_unresolved",
                    f"{dynamic_name} is present but its value is dynamic/unsupported.",
                    blocking_source="command_line",
                )
            index += 1
            continue

        folded = token.casefold()
        boolean_kind = _DESTINATION_BOOLEAN_OPTIONS.get(folded)
        if boolean_kind is not None:
            selectors.append(InstallationDestination(kind=boolean_kind))
            index += 1
            continue

        value_kind = _DESTINATION_VALUE_OPTIONS.get(folded)
        if value_kind is not None:
            if index + 1 >= len(arguments):
                return _problem(
                    declaration,
                    "installation_destination",
                    "installation_destination_missing_value",
                    f"pip destination option {token!r} is missing its value.",
                    blocking_source="command_line",
                )
            value = _literal_value(arguments[index + 1])
            if value is None:
                return _problem(
                    declaration,
                    "installation_destination",
                    "installation_destination_value_unresolved",
                    f"pip destination option {token!r} has a dynamic/unsupported value.",
                    blocking_source="command_line",
                )
            selectors.append(InstallationDestination(kind=value_kind, value=value))
            index += 2
            continue

        inline = _literal_inline_destination(token)
        if inline is not None:
            selectors.append(inline)
        index += 1

    if _unclassified_dynamic_operation_atoms(declaration):
        return _problem(
            declaration,
            "installation_destination",
            "installation_destination_command_line_unresolved",
            (
                "A dynamic/unsupported install argument could contain another material "
                "destination selector, so the effective command-line destination is unresolved."
            ),
            blocking_source="command_line",
        )

    if len(selectors) > 1:
        return _problem(
            declaration,
            "installation_destination",
            "multiple_installation_destination_selectors",
            (
                "Multiple command-line destination selectors require composition semantics "
                "outside the admitted Increment-2 first surface."
            ),
            state="unsupported",
            blocking_source="command_line",
        )
    if selectors:
        step = _command_line_step(
            "decisive",
            "An explicit pip destination selector determines a non-default installation scope.",
        )
        return InstallationDestinationFact(
            manager=declaration.manager,
            command_location=declaration.command_location,
            destination=selectors[0],
            provenance=_provenance("installation_destination", step),
        )

    return _problem(
        declaration,
        "installation_destination",
        "installation_destination_needs_lower_source_evidence",
        (
            "No explicit pip destination selector is visible. Process environment and "
            "persistent configuration must be ruled out before the normal manager-environment "
            "scheme can be asserted."
        ),
        resolved_prefix=(
            _command_line_step(
                "non_overriding",
                "No admitted command-line target/user/prefix/root selector is present.",
            ),
        ),
        blocking_source="process_environment",
    )


def resolve_package_mutation_mode(
    declaration: PackageManagerOperationDeclaration,
) -> PackageMutationModeFact | PackageManagerSemanticProblem:
    """Resolve explicit dry-run or preserve the unresolved effective-semantics edge."""

    if _unclassified_dynamic_operation_atoms(declaration):
        return _problem(
            declaration,
            "package_mutation_mode",
            "package_mutation_mode_command_line_unresolved",
            (
                "A dynamic/unsupported install argument could contain --dry-run, so "
                "command-line non-override is not established."
            ),
            blocking_source="command_line",
        )

    if _has_literal_option(declaration.operation_arguments, "--dry-run"):
        step = _command_line_step(
            "decisive",
            "Explicit pip --dry-run makes the install operation non-mutating.",
            locator="--dry-run",
        )
        return PackageMutationModeFact(
            manager=declaration.manager,
            command_location=declaration.command_location,
            mode="dry_run",
            provenance=_provenance("package_mutation_mode", step),
        )

    return _problem(
        declaration,
        "package_mutation_mode",
        "package_mutation_mode_needs_lower_source_evidence",
        (
            "No command-line --dry-run is visible. Process environment and persistent "
            "configuration must be resolved before the apply-changes manager default is valid."
        ),
        resolved_prefix=(
            _command_line_step(
                "non_overriding",
                "No command-line --dry-run selector is present.",
                locator="--dry-run",
            ),
        ),
        blocking_source="process_environment",
    )


def resolve_direct_requirement_handling(
    declaration: PackageManagerOperationDeclaration,
) -> DirectRequirementHandlingFact | PackageManagerSemanticProblem:
    """Resolve explicit direct exclusion or preserve the remaining lower-source edge."""

    if _unclassified_dynamic_operation_atoms(declaration):
        return _problem(
            declaration,
            "direct_requirement_handling",
            "direct_requirement_handling_command_line_unresolved",
            (
                "A dynamic/unsupported install argument could contain a direct-requirement "
                "exclusion mode."
            ),
            blocking_source="command_line",
        )

    if _has_literal_option(declaration.operation_arguments, "--only-deps"):
        step = _command_line_step(
            "decisive",
            "Explicit pip --only-deps excludes the directly requested requirement itself.",
            locator="--only-deps",
        )
        return DirectRequirementHandlingFact(
            manager=declaration.manager,
            command_location=declaration.command_location,
            handling="excluded",
            provenance=_provenance("direct_requirement_handling", step),
        )

    no_deps = _has_literal_option(declaration.operation_arguments, "--no-deps")
    return _problem(
        declaration,
        "direct_requirement_handling",
        "direct_requirement_handling_needs_lower_source_evidence",
        (
            "pip --no-deps suppresses transitive dependencies but does not exclude the direct "
            "requirement; lower semantic sources still need resolution."
            if no_deps
            else (
                "No command-line direct-requirement exclusion is visible; lower semantic "
                "sources still need resolution before effective handling can be asserted."
            )
        ),
        resolved_prefix=(
            _command_line_step(
                "non_overriding",
                (
                    "--no-deps does not exclude the direct requirement."
                    if no_deps
                    else "No command-line direct-requirement exclusion is present."
                ),
                locator="--no-deps" if no_deps else None,
            ),
        ),
        blocking_source="process_environment",
    )


def _global_option_values(
    declaration: PackageManagerOperationDeclaration,
    option_name: str,
) -> list[str | None]:
    values: list[str | None] = []
    arguments = declaration.manager_global_arguments
    index = 0
    target = option_name.casefold()

    while index < len(arguments):
        atom = arguments[index]
        token = _literal_value(atom)
        if token is None:
            if atom.raw_source.strip().casefold().startswith(target + "="):
                values.append(None)
            index += 1
            continue

        folded = token.casefold()
        if folded == target:
            values.append(
                _literal_value(arguments[index + 1])
                if index + 1 < len(arguments)
                else None
            )
            index += 2
            continue
        if folded.startswith(target + "="):
            values.append(token.split("=", 1)[1] or None)
        index += 1

    return values


def _literal_inline_destination(token: str) -> InstallationDestination | None:
    folded = token.casefold()
    for option, kind in _DESTINATION_VALUE_OPTIONS.items():
        if not option.startswith("--"):
            continue
        prefix = option + "="
        if folded.startswith(prefix):
            value = token.split("=", 1)[1]
            return InstallationDestination(kind=kind, value=value) if value else None
    return None


def _dynamic_inline_destination(raw_source: str) -> str | None:
    folded = raw_source.strip().casefold()
    for option in ("--target", "--prefix", "--root"):
        if folded.startswith(option + "="):
            return option
    return None


def _has_literal_option(
    arguments: tuple[StaticCommandAtom, ...],
    option_name: str,
) -> bool:
    target = option_name.casefold()
    return any(
        (value := _literal_value(atom)) is not None and value.casefold() == target
        for atom in arguments
    )


def _unclassified_dynamic_operation_atoms(
    declaration: PackageManagerOperationDeclaration,
) -> tuple[StaticCommandAtom, ...]:
    """Exclude dynamic values whose option position is already structurally known."""

    unresolved: list[StaticCommandAtom] = []
    arguments = declaration.operation_arguments
    index = 0

    while index < len(arguments):
        atom = arguments[index]
        token = _literal_value(atom)
        if token is not None and token.casefold() in _VALUE_TAKING_INSTALL_OPTIONS:
            index += 2 if index + 1 < len(arguments) else 1
            continue

        if token is None:
            raw = atom.raw_source.strip().casefold()
            known_inline_value = any(
                raw.startswith(prefix)
                for prefix in (
                    "--requirement=",
                    "--editable=",
                    "--target=",
                    "--prefix=",
                    "--root=",
                )
            )
            if not known_inline_value:
                unresolved.append(atom)
        index += 1

    return tuple(unresolved)


def _problem(
    declaration: PackageManagerOperationDeclaration,
    dimension: PackageManagerSemanticDimension,
    reason: str,
    detail: str,
    *,
    state: PackageManagerSemanticProblemState = "unresolved",
    resolved_prefix: tuple[PackageManagerSemanticResolutionStep, ...] = (),
    blocking_source: PackageManagerSemanticSourceKind | None = None,
) -> PackageManagerSemanticProblem:
    return PackageManagerSemanticProblem(
        state=state,
        dimension=dimension,
        reason=reason,
        detail=detail,
        command_location=declaration.command_location,
        resolved_prefix=resolved_prefix,
        blocking_source=blocking_source,
    )


def _provenance(
    dimension: PackageManagerSemanticDimension,
    decisive_step: PackageManagerSemanticResolutionStep,
) -> PackageManagerSemanticResolutionProvenance:
    return PackageManagerSemanticResolutionProvenance(
        dimension=dimension,
        inspected_sources=(decisive_step,),
        winning_source=decisive_step.source_kind,
    )


def _command_line_step(
    disposition: PackageManagerSemanticSourceDisposition,
    detail: str,
    *,
    locator: str | None = None,
) -> PackageManagerSemanticResolutionStep:
    return PackageManagerSemanticResolutionStep(
        source_kind="command_line",
        disposition=disposition,
        detail=detail,
        locator=locator,
    )


def _literal_value(atom: StaticCommandAtom) -> str | None:
    if atom.state != "literal" or atom.literal_value is None:
        return None
    return atom.literal_value


__all__ = (
    "DirectRequirementHandlingFact",
    "InstallationDestination",
    "InstallationDestinationFact",
    "ManagerEnvironmentSelectionFact",
    "PackageManagerEnvironmentReference",
    "PackageManagerSemanticProblem",
    "PackageManagerSemanticResolutionProvenance",
    "PackageManagerSemanticResolutionStep",
    "PackageMutationModeFact",
    "resolve_direct_requirement_handling",
    "resolve_installation_destination",
    "resolve_manager_environment_selection",
    "resolve_package_mutation_mode",
)
