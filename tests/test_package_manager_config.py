from __future__ import annotations

import unittest

from upgradepilot.dependency.package_manager_config import (
    observe_pip_persistent_config_setting,
)
from upgradepilot.dependency.package_manager_operation import (
    PackageManagerOperationDeclaration,
    parse_package_manager_operation,
)
from upgradepilot.github.process_environment import ProcessEnvironmentValueEvidence
from upgradepilot.github.workflow_command_analysis import (
    CommandSourceSpan,
    StaticCommandAtom,
    StaticCommandOccurrence,
)


def _literal(value: str) -> StaticCommandAtom:
    return StaticCommandAtom(raw_source=value, literal_value=value, state="literal")


def _declaration() -> PackageManagerOperationDeclaration:
    raw_source = "pip install -r requirements.txt"
    occurrence = StaticCommandOccurrence(
        source_order=0,
        source_span=CommandSourceSpan(
            start_byte=0,
            end_byte=len(raw_source),
            start_line=0,
            start_column=0,
            end_line=0,
            end_column=len(raw_source),
        ),
        raw_source=raw_source,
        executable=_literal("pip"),
        arguments=tuple(
            _literal(value)
            for value in ("install", "-r", "requirements.txt")
        ),
        structural_context=("straightforward_top_level",),
    )
    result = parse_package_manager_operation(occurrence)
    assert isinstance(result, PackageManagerOperationDeclaration)
    return result


def _environment(
    declaration: PackageManagerOperationDeclaration,
    *,
    variable_name: str = "PIP_CONFIG_FILE",
    state: str = "established",
    value: str | None = None,
) -> ProcessEnvironmentValueEvidence:
    return ProcessEnvironmentValueEvidence(
        state=state,  # type: ignore[arg-type]
        variable_name=variable_name,
        value=value,
        source="command_local_assignment",
        reason="focused_test",
        detail="focused package-manager config evidence",
        command_location=declaration.command_location,
        workflow_path=".github/workflows/ci.yml",
        workflow_revision="a" * 40,
        job_key="test",
        step_source_index=0,
    )


class PipPersistentConfigEvidenceTests(unittest.TestCase):
    def test_dev_null_config_file_disables_each_supported_persistent_setting(self) -> None:
        declaration = _declaration()

        for setting in ("dry-run", "installation-destination", "only-deps"):
            with self.subTest(setting=setting):
                result = observe_pip_persistent_config_setting(
                    declaration,
                    setting=setting,  # type: ignore[arg-type]
                    config_file_environment=_environment(
                        declaration,
                        value="/dev/null",
                    ),
                )

                self.assertEqual(result.state, "disabled")
                self.assertEqual(result.setting, setting)
                self.assertEqual(result.reason, "pip_configuration_files_disabled")
                self.assertEqual(result.source_locator, "PIP_CONFIG_FILE")

    def test_other_config_file_requires_content_resolution(self) -> None:
        declaration = _declaration()

        result = observe_pip_persistent_config_setting(
            declaration,
            setting="dry-run",
            config_file_environment=_environment(
                declaration,
                value="/tmp/pip.conf",
            ),
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(
            result.reason,
            "pip_config_file_requires_content_resolution",
        )

    def test_unresolved_process_value_keeps_config_unresolved(self) -> None:
        declaration = _declaration()

        result = observe_pip_persistent_config_setting(
            declaration,
            setting="dry-run",
            config_file_environment=_environment(
                declaration,
                state="unresolved",
            ),
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(
            result.reason,
            "pip_config_file_process_environment_unresolved",
        )

    def test_wrong_process_variable_does_not_disable_config(self) -> None:
        declaration = _declaration()

        result = observe_pip_persistent_config_setting(
            declaration,
            setting="dry-run",
            config_file_environment=_environment(
                declaration,
                variable_name="PIP_DRY_RUN",
                value="/dev/null",
            ),
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(
            result.reason,
            "pip_config_file_variable_identity_mismatch",
        )


if __name__ == "__main__":
    unittest.main()
