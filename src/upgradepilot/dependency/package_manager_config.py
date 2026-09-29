"""Bounded persistent package-manager configuration evidence.

This dependency-owned layer interprets manager-specific persistent-configuration controls
from already-established exact-process environment evidence. It does not discover arbitrary
runner filesystems or assume that an unobserved config file is absent.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..github.process_environment import ProcessEnvironmentValueEvidence
from ..github.workflow_command_location import StaticCommandLocation
from .package_manager_operation import PackageManagerName, PackageManagerOperationDeclaration


type PackageManagerConfigSettingName = Literal["dry-run"]
type PackageManagerConfigSettingState = Literal["disabled", "unresolved"]


@dataclass(frozen=True, slots=True)
class PackageManagerConfigSettingEvidence:
    """Persistent-config evidence for one package-manager semantic setting."""

    manager: PackageManagerName
    setting: PackageManagerConfigSettingName
    state: PackageManagerConfigSettingState
    value: str | None
    reason: str
    detail: str
    command_location: StaticCommandLocation
    source_locator: str | None = None


def observe_pip_persistent_config_setting(
    declaration: PackageManagerOperationDeclaration,
    *,
    setting: PackageManagerConfigSettingName,
    config_file_environment: ProcessEnvironmentValueEvidence | None,
) -> PackageManagerConfigSettingEvidence:
    """Resolve the first admitted pip persistent-config control for one setting.

    The first positive family is exact PIP_CONFIG_FILE=/dev/null on the admitted
    POSIX/Bash Route-A path. Pip treats its platform null device as a directive to skip
    loading all configuration files. Any other path remains unresolved until that file
    and the rest of pip's applicable config search/precedence are acquired.
    """

    if declaration.manager != "pip":
        return _problem(
            declaration,
            setting,
            "unsupported_package_manager",
            "Persistent-config evidence is currently implemented only for pip.",
        )

    if config_file_environment is None:
        return _problem(
            declaration,
            setting,
            "pip_config_file_process_environment_missing",
            (
                "Exact-process PIP_CONFIG_FILE evidence is required before persistent "
                "configuration can be declared disabled."
            ),
        )

    if config_file_environment.command_location != declaration.command_location:
        return _problem(
            declaration,
            setting,
            "pip_config_file_command_identity_mismatch",
            "PIP_CONFIG_FILE evidence belongs to a different static command occurrence.",
        )

    if config_file_environment.variable_name != "PIP_CONFIG_FILE":
        return _problem(
            declaration,
            setting,
            "pip_config_file_variable_identity_mismatch",
            (
                "Persistent pip configuration requires exact-process PIP_CONFIG_FILE "
                f"evidence, not {config_file_environment.variable_name!r}."
            ),
        )

    if (
        config_file_environment.state != "established"
        or config_file_environment.value is None
    ):
        return _problem(
            declaration,
            setting,
            "pip_config_file_process_environment_unresolved",
            (
                "Exact-process PIP_CONFIG_FILE evidence is unresolved, so persistent "
                "configuration cannot be closed."
            ),
        )

    value = config_file_environment.value
    if value == "/dev/null":
        return PackageManagerConfigSettingEvidence(
            manager="pip",
            setting=setting,
            state="disabled",
            value=None,
            reason="pip_configuration_files_disabled",
            detail=(
                "Exact-process PIP_CONFIG_FILE=/dev/null disables loading all pip "
                "configuration files on the admitted POSIX Route-A path."
            ),
            command_location=declaration.command_location,
            source_locator="PIP_CONFIG_FILE",
        )

    return _problem(
        declaration,
        setting,
        "pip_config_file_requires_content_resolution",
        (
            f"Exact-process PIP_CONFIG_FILE={value!r} selects a concrete configuration "
            "path, but its contents and applicable precedence have not been acquired."
        ),
        source_locator="PIP_CONFIG_FILE",
    )


def _problem(
    declaration: PackageManagerOperationDeclaration,
    setting: PackageManagerConfigSettingName,
    reason: str,
    detail: str,
    *,
    source_locator: str | None = None,
) -> PackageManagerConfigSettingEvidence:
    return PackageManagerConfigSettingEvidence(
        manager=declaration.manager,
        setting=setting,
        state="unresolved",
        value=None,
        reason=reason,
        detail=detail,
        command_location=declaration.command_location,
        source_locator=source_locator,
    )


__all__ = (
    "PackageManagerConfigSettingEvidence",
    "observe_pip_persistent_config_setting",
)
