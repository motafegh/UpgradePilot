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
from ..github.process_environment import ProcessEnvironmentValueEvidence
from ..github.workflow_command_location import StaticCommandLocation
from .package_manager_config import PackageManagerConfigSettingEvidence
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
    "manager_environment_scheme",
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
    *,
    process_environment: tuple[ProcessEnvironmentValueEvidence, ...] = (),
    persistent_configuration: PackageManagerConfigSettingEvidence | None = None,
) -> InstallationDestinationFact | PackageManagerSemanticProblem:
    """Resolve explicit/ambient pip destination selection without inventing defaults."""

    selectors: list[InstallationDestination] = []
    arguments = declaration.operation_arguments
    index = 0
    user_scope_disabled_on_cli = False

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
        if folded == "--no-user":
            user_scope_disabled_on_cli = True
            index += 1
            continue

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

        empty_inline_option = _empty_inline_destination_option(token)
        if empty_inline_option is not None:
            return _problem(
                declaration,
                "installation_destination",
                "installation_destination_missing_value",
                f"pip destination option {empty_inline_option!r} has an empty value.",
                blocking_source="command_line",
            )

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
                "outside the admitted Increment-3 first positive family."
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

    cli_step = _command_line_step(
        "non_overriding",
        (
            "No target/prefix/root/user destination selector is present, and explicit "
            "--no-user closes the user-site branch."
            if user_scope_disabled_on_cli
            else "No command-line target/user/prefix/root selector is present."
        ),
        locator="--no-user" if user_scope_disabled_on_cli else None,
    )

    if not process_environment:
        return _problem(
            declaration,
            "installation_destination",
            "installation_destination_needs_lower_source_evidence",
            (
                "No explicit pip destination selector is visible. Process environment and "
                "persistent configuration must be ruled out before the normal manager-environment "
                "scheme can be asserted."
            ),
            resolved_prefix=(cli_step,),
            blocking_source="process_environment",
        )

    if not user_scope_disabled_on_cli:
        return _problem(
            declaration,
            "installation_destination",
            "installation_destination_user_scope_not_closed",
            (
                "The first default-destination family requires explicit --no-user so user-site "
                "selection cannot be introduced by lower sources. Broader user/no-user "
                "environment composition remains intentionally unresolved."
            ),
            resolved_prefix=(cli_step,),
            blocking_source="process_environment",
        )

    required_names = ("PIP_TARGET", "PIP_PREFIX", "PIP_ROOT")
    environment_values = _matching_process_environment_values(
        declaration,
        process_environment,
        variable_names=required_names,
        dimension="installation_destination",
        resolved_prefix=(cli_step,),
    )
    if isinstance(environment_values, PackageManagerSemanticProblem):
        return environment_values

    environment_selectors: list[InstallationDestination] = []
    if environment_values["PIP_TARGET"]:
        environment_selectors.append(
            InstallationDestination(
                kind="target_directory",
                value=environment_values["PIP_TARGET"],
            )
        )
    if environment_values["PIP_PREFIX"]:
        environment_selectors.append(
            InstallationDestination(
                kind="prefix_scheme",
                value=environment_values["PIP_PREFIX"],
            )
        )
    if environment_values["PIP_ROOT"]:
        environment_selectors.append(
            InstallationDestination(
                kind="root_relocated_scheme",
                value=environment_values["PIP_ROOT"],
            )
        )

    if len(environment_selectors) > 1:
        return _problem(
            declaration,
            "installation_destination",
            "multiple_process_environment_destination_selectors",
            (
                "Multiple exact-process pip destination environment variables are non-empty; "
                "their combined destination semantics are outside the first positive family."
            ),
            resolved_prefix=(cli_step,),
            blocking_source="process_environment",
        )

    env_step = PackageManagerSemanticResolutionStep(
        source_kind="process_environment",
        disposition="decisive" if environment_selectors else "non_overriding",
        detail=(
            "Exact process environment selects a non-default pip installation destination."
            if environment_selectors
            else (
                "Exact process PIP_TARGET, PIP_PREFIX, and PIP_ROOT are empty, so they do not "
                "retarget installation."
            )
        ),
        locator="PIP_TARGET/PIP_PREFIX/PIP_ROOT",
    )
    if environment_selectors:
        return InstallationDestinationFact(
            manager=declaration.manager,
            command_location=declaration.command_location,
            destination=environment_selectors[0],
            provenance=PackageManagerSemanticResolutionProvenance(
                dimension="installation_destination",
                inspected_sources=(cli_step, env_step),
                winning_source="process_environment",
            ),
        )

    if persistent_configuration is None:
        return _problem(
            declaration,
            "installation_destination",
            "installation_destination_needs_persistent_config_evidence",
            (
                "Command line and exact process destination variables are non-overriding; "
                "persistent configuration must be resolved before the manager-environment "
                "scheme default is valid."
            ),
            resolved_prefix=(cli_step, env_step),
            blocking_source="persistent_configuration",
        )

    config_problem = _validate_persistent_config_evidence(
        declaration,
        persistent_configuration,
        setting="installation-destination",
        dimension="installation_destination",
        resolved_prefix=(cli_step, env_step),
    )
    if config_problem is not None:
        return config_problem

    config_step = PackageManagerSemanticResolutionStep(
        source_kind="persistent_configuration",
        disposition="disabled",
        detail="Applicable pip persistent configuration is disabled for destination selection.",
        locator=persistent_configuration.source_locator,
    )
    default_step = PackageManagerSemanticResolutionStep(
        source_kind="manager_default",
        disposition="decisive",
        detail=(
            "After target/user/prefix/root selectors are closed, pip installs into the "
            "selected manager environment's normal installation scheme."
        ),
        locator="pip install destination default",
    )
    return InstallationDestinationFact(
        manager=declaration.manager,
        command_location=declaration.command_location,
        destination=InstallationDestination(kind="manager_environment_scheme"),
        provenance=PackageManagerSemanticResolutionProvenance(
            dimension="installation_destination",
            inspected_sources=(cli_step, env_step, config_step, default_step),
            winning_source="manager_default",
        ),
    )


def resolve_package_mutation_mode(
    declaration: PackageManagerOperationDeclaration,
    *,
    process_environment: ProcessEnvironmentValueEvidence | None = None,
    persistent_configuration: PackageManagerConfigSettingEvidence | None = None,
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

    cli_step = _command_line_step(
        "non_overriding",
        "No command-line --dry-run selector is present.",
        locator="--dry-run",
    )
    if process_environment is None:
        return _problem(
            declaration,
            "package_mutation_mode",
            "package_mutation_mode_needs_lower_source_evidence",
            (
                "No command-line --dry-run is visible. Process environment and persistent "
                "configuration must be resolved before the apply-changes manager default is valid."
            ),
            resolved_prefix=(cli_step,),
            blocking_source="process_environment",
        )

    env_value = _matching_process_environment_value(
        declaration,
        process_environment,
        variable_name="PIP_DRY_RUN",
        dimension="package_mutation_mode",
        resolved_prefix=(cli_step,),
    )
    if isinstance(env_value, PackageManagerSemanticProblem):
        return env_value

    bool_value = _pip_boolean_value(env_value)
    if bool_value is None:
        return _problem(
            declaration,
            "package_mutation_mode",
            "pip_dry_run_environment_value_invalid",
            (
                f"PIP_DRY_RUN={env_value!r} is not an admitted pip boolean value, so "
                "effective mutation mode is unresolved."
            ),
            resolved_prefix=(cli_step,),
            blocking_source="process_environment",
        )

    env_step = PackageManagerSemanticResolutionStep(
        source_kind="process_environment",
        disposition="decisive" if bool_value else "non_overriding",
        detail=(
            f"Exact process environment establishes PIP_DRY_RUN={env_value!r}; "
            + (
                "pip interprets it as enabled."
                if bool_value
                else "pip interprets it as disabled."
            )
        ),
        locator="PIP_DRY_RUN",
    )
    if bool_value:
        return PackageMutationModeFact(
            manager=declaration.manager,
            command_location=declaration.command_location,
            mode="dry_run",
            provenance=PackageManagerSemanticResolutionProvenance(
                dimension="package_mutation_mode",
                inspected_sources=(cli_step, env_step),
                winning_source="process_environment",
            ),
        )

    if persistent_configuration is None:
        return _problem(
            declaration,
            "package_mutation_mode",
            "package_mutation_mode_needs_persistent_config_evidence",
            (
                "Command line and exact PIP_DRY_RUN process environment are non-overriding; "
                "persistent configuration must still be resolved before the manager default "
                "can establish apply-changes behavior."
            ),
            resolved_prefix=(cli_step, env_step),
            blocking_source="persistent_configuration",
        )

    config_problem = _validate_persistent_config_evidence(
        declaration,
        persistent_configuration,
        setting="dry-run",
        dimension="package_mutation_mode",
        resolved_prefix=(cli_step, env_step),
    )
    if config_problem is not None:
        return config_problem

    config_step = PackageManagerSemanticResolutionStep(
        source_kind="persistent_configuration",
        disposition="disabled",
        detail=(
            "Applicable pip persistent configuration is positively disabled for "
            "the dry-run setting."
        ),
        locator=persistent_configuration.source_locator,
    )
    default_step = PackageManagerSemanticResolutionStep(
        source_kind="manager_default",
        disposition="decisive",
        detail=(
            "After command line, exact process environment, and persistent configuration "
            "are proven non-overriding/disabled, pip's normal install default applies changes."
        ),
        locator="pip install default",
    )
    return PackageMutationModeFact(
        manager=declaration.manager,
        command_location=declaration.command_location,
        mode="apply_changes",
        provenance=PackageManagerSemanticResolutionProvenance(
            dimension="package_mutation_mode",
            inspected_sources=(cli_step, env_step, config_step, default_step),
            winning_source="manager_default",
        ),
    )


def resolve_direct_requirement_handling(
    declaration: PackageManagerOperationDeclaration,
    *,
    process_environment: tuple[ProcessEnvironmentValueEvidence, ...] = (),
    persistent_configuration: PackageManagerConfigSettingEvidence | None = None,
) -> DirectRequirementHandlingFact | PackageManagerSemanticProblem:
    """Resolve whether pip handles the direct requirement under bounded precedence."""

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

    if any(
        _has_literal_option(declaration.operation_arguments, option)
        for option in ("--only-deps", "--only-dependencies")
    ):
        step = _command_line_step(
            "decisive",
            "Explicit pip --only-deps/--only-dependencies excludes direct requirements.",
            locator="--only-deps",
        )
        return DirectRequirementHandlingFact(
            manager=declaration.manager,
            command_location=declaration.command_location,
            handling="excluded",
            provenance=_provenance("direct_requirement_handling", step),
        )

    no_deps = _has_literal_option(declaration.operation_arguments, "--no-deps")
    cli_step = _command_line_step(
        "non_overriding",
        (
            "--no-deps suppresses transitive dependencies but does not exclude the direct "
            "requirement."
            if no_deps
            else "No command-line direct-requirement exclusion is present."
        ),
        locator="--no-deps" if no_deps else None,
    )

    if not process_environment:
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
            resolved_prefix=(cli_step,),
            blocking_source="process_environment",
        )

    variable_names = ("PIP_ONLY_DEPS", "PIP_ONLY_DEPENDENCIES")
    environment_values = _matching_process_environment_values(
        declaration,
        process_environment,
        variable_names=variable_names,
        dimension="direct_requirement_handling",
        resolved_prefix=(cli_step,),
    )
    if isinstance(environment_values, PackageManagerSemanticProblem):
        return environment_values

    parsed_values = {
        name: _pip_boolean_value(value)
        for name, value in environment_values.items()
    }
    if any(value is None for value in parsed_values.values()):
        return _problem(
            declaration,
            "direct_requirement_handling",
            "pip_only_deps_environment_value_invalid",
            (
                "PIP_ONLY_DEPS/PIP_ONLY_DEPENDENCIES contains a value outside pip's admitted "
                "boolean vocabulary."
            ),
            resolved_prefix=(cli_step,),
            blocking_source="process_environment",
        )

    bool_values = {value for value in parsed_values.values() if value is not None}
    if len(bool_values) != 1:
        return _problem(
            declaration,
            "direct_requirement_handling",
            "pip_only_deps_environment_alias_conflict",
            (
                "PIP_ONLY_DEPS and PIP_ONLY_DEPENDENCIES disagree; environment iteration "
                "ordering is not used as a hidden precedence rule."
            ),
            resolved_prefix=(cli_step,),
            blocking_source="process_environment",
        )

    only_deps_enabled = next(iter(bool_values))
    env_step = PackageManagerSemanticResolutionStep(
        source_kind="process_environment",
        disposition="decisive" if only_deps_enabled else "non_overriding",
        detail=(
            "Exact process environment enables pip only-dependencies handling."
            if only_deps_enabled
            else (
                "Exact process PIP_ONLY_DEPS and PIP_ONLY_DEPENDENCIES are both disabled."
            )
        ),
        locator="PIP_ONLY_DEPS/PIP_ONLY_DEPENDENCIES",
    )
    if only_deps_enabled:
        return DirectRequirementHandlingFact(
            manager=declaration.manager,
            command_location=declaration.command_location,
            handling="excluded",
            provenance=PackageManagerSemanticResolutionProvenance(
                dimension="direct_requirement_handling",
                inspected_sources=(cli_step, env_step),
                winning_source="process_environment",
            ),
        )

    if persistent_configuration is None:
        return _problem(
            declaration,
            "direct_requirement_handling",
            "direct_requirement_handling_needs_persistent_config_evidence",
            (
                "Command line and exact only-deps environment aliases are non-overriding; "
                "persistent configuration must be resolved before pip's normal direct-"
                "requirement handling default can be used."
            ),
            resolved_prefix=(cli_step, env_step),
            blocking_source="persistent_configuration",
        )

    config_problem = _validate_persistent_config_evidence(
        declaration,
        persistent_configuration,
        setting="only-deps",
        dimension="direct_requirement_handling",
        resolved_prefix=(cli_step, env_step),
    )
    if config_problem is not None:
        return config_problem

    config_step = PackageManagerSemanticResolutionStep(
        source_kind="persistent_configuration",
        disposition="disabled",
        detail="Applicable pip persistent configuration is disabled for only-deps.",
        locator=persistent_configuration.source_locator,
    )
    default_step = PackageManagerSemanticResolutionStep(
        source_kind="manager_default",
        disposition="decisive",
        detail=(
            "After direct-exclusion selectors are closed, pip's default handles the direct "
            "requirements supplied by the install command."
        ),
        locator="pip only-deps default",
    )
    return DirectRequirementHandlingFact(
        manager=declaration.manager,
        command_location=declaration.command_location,
        handling="handled",
        provenance=PackageManagerSemanticResolutionProvenance(
            dimension="direct_requirement_handling",
            inspected_sources=(cli_step, env_step, config_step, default_step),
            winning_source="manager_default",
        ),
    )


def _validate_persistent_config_evidence(
    declaration: PackageManagerOperationDeclaration,
    evidence: PackageManagerConfigSettingEvidence,
    *,
    setting: str,
    dimension: PackageManagerSemanticDimension,
    resolved_prefix: tuple[PackageManagerSemanticResolutionStep, ...],
) -> PackageManagerSemanticProblem | None:
    if evidence.command_location != declaration.command_location:
        return _problem(
            declaration,
            dimension,
            "persistent_config_command_identity_mismatch",
            "Persistent-config evidence belongs to a different static command occurrence.",
            resolved_prefix=resolved_prefix,
            blocking_source="persistent_configuration",
        )
    if evidence.manager != declaration.manager:
        return _problem(
            declaration,
            dimension,
            "persistent_config_manager_identity_mismatch",
            "Persistent-config evidence belongs to a different package manager.",
            resolved_prefix=resolved_prefix,
            blocking_source="persistent_configuration",
        )
    if evidence.setting != setting:
        return _problem(
            declaration,
            dimension,
            "persistent_config_setting_identity_mismatch",
            (
                f"Semantic resolution requires persistent setting {setting!r}, but supplied "
                f"evidence is for {evidence.setting!r}."
            ),
            resolved_prefix=resolved_prefix,
            blocking_source="persistent_configuration",
        )
    if evidence.state != "disabled":
        return _problem(
            declaration,
            dimension,
            "persistent_config_setting_unresolved",
            (
                f"Persistent configuration for {setting!r} is unresolved: "
                f"{evidence.reason}: {evidence.detail}"
            ),
            resolved_prefix=resolved_prefix,
            blocking_source="persistent_configuration",
        )
    return None


def _matching_process_environment_values(
    declaration: PackageManagerOperationDeclaration,
    evidence: tuple[ProcessEnvironmentValueEvidence, ...],
    *,
    variable_names: tuple[str, ...],
    dimension: PackageManagerSemanticDimension,
    resolved_prefix: tuple[PackageManagerSemanticResolutionStep, ...],
) -> dict[str, str] | PackageManagerSemanticProblem:
    by_name: dict[str, ProcessEnvironmentValueEvidence] = {}
    for item in evidence:
        if item.variable_name in by_name:
            return _problem(
                declaration,
                dimension,
                "duplicate_process_environment_variable_evidence",
                f"Multiple exact-process evidence records exist for {item.variable_name}.",
                resolved_prefix=resolved_prefix,
                blocking_source="process_environment",
            )
        by_name[item.variable_name] = item

    values: dict[str, str] = {}
    for variable_name in variable_names:
        item = by_name.get(variable_name)
        if item is None:
            return _problem(
                declaration,
                dimension,
                "process_environment_value_missing",
                (
                    f"Exact-process evidence for required variable {variable_name} was not "
                    "supplied, so the lower semantic source cannot be closed."
                ),
                resolved_prefix=resolved_prefix,
                blocking_source="process_environment",
            )
        value = _matching_process_environment_value(
            declaration,
            item,
            variable_name=variable_name,
            dimension=dimension,
            resolved_prefix=resolved_prefix,
        )
        if isinstance(value, PackageManagerSemanticProblem):
            return value
        values[variable_name] = value

    return values


def _matching_process_environment_value(
    declaration: PackageManagerOperationDeclaration,
    evidence: ProcessEnvironmentValueEvidence,
    *,
    variable_name: str,
    dimension: PackageManagerSemanticDimension,
    resolved_prefix: tuple[PackageManagerSemanticResolutionStep, ...],
) -> str | PackageManagerSemanticProblem:
    if evidence.command_location != declaration.command_location:
        return _problem(
            declaration,
            dimension,
            "process_environment_command_identity_mismatch",
            "Process-environment evidence belongs to a different static command occurrence.",
            resolved_prefix=resolved_prefix,
            blocking_source="process_environment",
        )
    if evidence.variable_name != variable_name:
        return _problem(
            declaration,
            dimension,
            "process_environment_variable_identity_mismatch",
            (
                f"Semantic resolution requires {variable_name}, but the supplied exact-process "
                f"evidence is for {evidence.variable_name}."
            ),
            resolved_prefix=resolved_prefix,
            blocking_source="process_environment",
        )
    if evidence.state != "established" or evidence.value is None:
        return _problem(
            declaration,
            dimension,
            "process_environment_value_unresolved",
            (
                f"Exact-process evidence for {variable_name} is unresolved: "
                f"{evidence.reason}: {evidence.detail}"
            ),
            resolved_prefix=resolved_prefix,
            blocking_source="process_environment",
        )
    return evidence.value


def _pip_boolean_value(value: str) -> bool | None:
    """Interpret pip's documented boolean configuration vocabulary."""

    folded = value.strip().casefold()
    if folded in {"y", "yes", "t", "true", "on", "1"}:
        return True
    if folded in {"n", "no", "f", "false", "off", "0"}:
        return False
    return None


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


def _empty_inline_destination_option(token: str) -> str | None:
    folded = token.casefold()
    for option in ("--target", "--prefix", "--root"):
        if folded == option + "=":
            return option
    return None


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
