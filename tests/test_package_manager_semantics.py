"""Test static package-manager operation identity and command-local semantic facts."""

from __future__ import annotations

import unittest

from upgradepilot.dependency.package_manager_operation import (
    PackageManagerOperationDeclaration,
    PackageManagerOperationProblem,
    parse_package_manager_operation,
)
from upgradepilot.dependency.package_manager_semantics import (
    DirectRequirementHandlingFact,
    InstallationDestinationFact,
    ManagerEnvironmentSelectionFact,
    PackageManagerSemanticProblem,
    PackageMutationModeFact,
    resolve_direct_requirement_handling,
    resolve_installation_destination,
    resolve_manager_environment_selection,
    resolve_package_mutation_mode,
)
from upgradepilot.github.process_environment import ProcessEnvironmentValueEvidence
from upgradepilot.github.workflow_command_analysis import (
    CommandSourceSpan,
    StaticCommandAtom,
    StaticCommandOccurrence,
)


def _literal(value: str) -> StaticCommandAtom:
    return StaticCommandAtom(raw_source=value, literal_value=value, state="literal")


def _dynamic(raw_source: str) -> StaticCommandAtom:
    return StaticCommandAtom(raw_source=raw_source, literal_value=None, state="dynamic")


def _occurrence(
    executable: str,
    *arguments: str | StaticCommandAtom,
) -> StaticCommandOccurrence:
    atoms = tuple(
        item if isinstance(item, StaticCommandAtom) else _literal(item)
        for item in arguments
    )
    raw_source = " ".join((executable, *(atom.raw_source for atom in atoms)))
    return StaticCommandOccurrence(
        source_order=2,
        source_span=CommandSourceSpan(
            start_byte=10,
            end_byte=10 + len(raw_source.encode("utf-8")),
            start_line=2,
            start_column=0,
            end_line=2,
            end_column=len(raw_source.encode("utf-8")),
        ),
        raw_source=raw_source,
        executable=_literal(executable),
        arguments=atoms,
        structural_context=("straightforward_top_level",),
    )


def _declaration(
    executable: str,
    *arguments: str | StaticCommandAtom,
) -> PackageManagerOperationDeclaration:
    result = parse_package_manager_operation(_occurrence(executable, *arguments))
    if not isinstance(result, PackageManagerOperationDeclaration):
        raise AssertionError(f"expected declaration, got {result!r}")
    return result


def _process_environment(
    declaration: PackageManagerOperationDeclaration,
    variable_name: str,
    *,
    state: str = "established",
    value: str | None = None,
) -> ProcessEnvironmentValueEvidence:
    return ProcessEnvironmentValueEvidence(
        state=state,  # type: ignore[arg-type]
        variable_name=variable_name,
        value=value,
        source="command_local_assignment",
        reason=(
            "process_environment_command_local_value_established"
            if state == "established"
            else "process_environment_command_local_value_unresolved"
        ),
        detail="focused package-manager semantic test evidence",
        command_location=declaration.command_location,
        workflow_path=".github/workflows/ci.yml",
        workflow_revision="a" * 40,
        job_key="test",
        step_source_index=0,
    )


class PackageManagerOperationTests(unittest.TestCase):
    def test_bare_pip_install_preserves_invocation_and_operation_arguments(self) -> None:
        declaration = _declaration("pip", "install", "-r", "requirements.txt")

        self.assertEqual(declaration.manager, "pip")
        self.assertEqual(declaration.operation, "install")
        self.assertEqual(declaration.invocation_form, "pip_executable")
        self.assertEqual(declaration.launcher, "pip")
        self.assertIsNone(declaration.python_interpreter)
        self.assertEqual(
            tuple(atom.literal_value for atom in declaration.operation_arguments),
            ("-r", "requirements.txt"),
        )

    def test_python_module_invocation_is_distinct_from_bare_pip(self) -> None:
        declaration = _declaration(
            "python",
            "-m",
            "pip",
            "install",
            "-r",
            "requirements.txt",
        )

        self.assertEqual(declaration.invocation_form, "python_module")
        self.assertEqual(declaration.python_interpreter, "python")

    def test_explicit_python_interpreter_path_is_preserved(self) -> None:
        declaration = _declaration(
            "/opt/venv/bin/python3.12",
            "-m",
            "pip",
            "install",
            "-r",
            "requirements.txt",
        )

        self.assertEqual(declaration.invocation_form, "python_module")
        self.assertEqual(
            declaration.python_interpreter,
            "/opt/venv/bin/python3.12",
        )

    def test_pip_global_python_before_install_is_preserved_and_resolved(self) -> None:
        declaration = _declaration(
            "pip",
            "--python",
            "/opt/target/bin/python",
            "install",
            "-r",
            "requirements.txt",
        )
        result = resolve_manager_environment_selection(declaration)

        self.assertIsInstance(result, ManagerEnvironmentSelectionFact)
        assert isinstance(result, ManagerEnvironmentSelectionFact)
        self.assertEqual(result.environment.kind, "pip_python_target")
        self.assertEqual(result.environment.value, "/opt/target/bin/python")
        self.assertEqual(result.provenance.winning_source, "command_line")

    def test_dynamic_pip_python_value_becomes_semantic_problem_not_guess(self) -> None:
        declaration = _declaration(
            "pip",
            "--python",
            _dynamic("${{ matrix.python }}"),
            "install",
            "-r",
            "requirements.txt",
        )
        result = resolve_manager_environment_selection(declaration)

        self.assertIsInstance(result, PackageManagerSemanticProblem)
        assert isinstance(result, PackageManagerSemanticProblem)
        self.assertEqual(result.reason, "pip_python_target_unresolved")
        self.assertEqual(result.blocking_source, "command_line")

    def test_unknown_global_option_before_install_is_explicitly_unsupported(self) -> None:
        result = parse_package_manager_operation(
            _occurrence("pip", "--cache-dir", "/tmp/cache", "install", "demo")
        )

        self.assertIsInstance(result, PackageManagerOperationProblem)
        assert isinstance(result, PackageManagerOperationProblem)
        self.assertEqual(result.state, "unsupported")
        self.assertEqual(
            result.reason,
            "unsupported_pip_global_option_before_install",
        )

    def test_non_install_pip_global_flag_is_not_misclassified_as_install_problem(self) -> None:
        result = parse_package_manager_operation(_occurrence("pip", "--version"))

        self.assertIsNone(result)

    def test_non_install_pip_command_is_not_declared(self) -> None:
        result = parse_package_manager_operation(_occurrence("pip", "list"))

        self.assertIsNone(result)


class PackageManagerSemanticFactTests(unittest.TestCase):
    def test_explicit_dry_run_is_decisive_non_mutating_fact(self) -> None:
        declaration = _declaration(
            "pip",
            "install",
            "--dry-run",
            "-r",
            "requirements.txt",
        )
        result = resolve_package_mutation_mode(declaration)

        self.assertIsInstance(result, PackageMutationModeFact)
        assert isinstance(result, PackageMutationModeFact)
        self.assertEqual(result.mode, "dry_run")
        self.assertEqual(result.provenance.winning_source, "command_line")

    def test_absent_dry_run_does_not_fabricate_apply_changes_default(self) -> None:
        declaration = _declaration(
            "pip",
            "install",
            "-r",
            "requirements.txt",
        )
        result = resolve_package_mutation_mode(declaration)

        self.assertIsInstance(result, PackageManagerSemanticProblem)
        assert isinstance(result, PackageManagerSemanticProblem)
        self.assertEqual(
            result.reason,
            "package_mutation_mode_needs_lower_source_evidence",
        )
        self.assertEqual(result.blocking_source, "process_environment")

    def test_exact_process_dry_run_true_is_decisive_after_cli_non_override(self) -> None:
        declaration = _declaration(
            "pip",
            "install",
            "-r",
            "requirements.txt",
        )

        result = resolve_package_mutation_mode(
            declaration,
            process_environment=_process_environment(
                declaration,
                "PIP_DRY_RUN",
                value="1",
            ),
        )

        self.assertIsInstance(result, PackageMutationModeFact)
        assert isinstance(result, PackageMutationModeFact)
        self.assertEqual(result.mode, "dry_run")
        self.assertEqual(result.provenance.winning_source, "process_environment")
        self.assertEqual(
            [step.source_kind for step in result.provenance.inspected_sources],
            ["command_line", "process_environment"],
        )

    def test_exact_process_dry_run_false_moves_blocker_to_persistent_config(self) -> None:
        declaration = _declaration(
            "pip",
            "install",
            "-r",
            "requirements.txt",
        )

        result = resolve_package_mutation_mode(
            declaration,
            process_environment=_process_environment(
                declaration,
                "PIP_DRY_RUN",
                value="0",
            ),
        )

        self.assertIsInstance(result, PackageManagerSemanticProblem)
        assert isinstance(result, PackageManagerSemanticProblem)
        self.assertEqual(
            result.reason,
            "package_mutation_mode_needs_persistent_config_evidence",
        )
        self.assertEqual(result.blocking_source, "persistent_configuration")
        self.assertEqual(
            [step.source_kind for step in result.resolved_prefix],
            ["command_line", "process_environment"],
        )

    def test_unresolved_exact_process_dry_run_does_not_fall_through(self) -> None:
        declaration = _declaration(
            "pip",
            "install",
            "-r",
            "requirements.txt",
        )

        result = resolve_package_mutation_mode(
            declaration,
            process_environment=_process_environment(
                declaration,
                "PIP_DRY_RUN",
                state="unresolved",
            ),
        )

        self.assertIsInstance(result, PackageManagerSemanticProblem)
        assert isinstance(result, PackageManagerSemanticProblem)
        self.assertEqual(result.reason, "process_environment_value_unresolved")
        self.assertEqual(result.blocking_source, "process_environment")

    def test_invalid_exact_process_dry_run_value_does_not_become_false(self) -> None:
        declaration = _declaration(
            "pip",
            "install",
            "-r",
            "requirements.txt",
        )

        result = resolve_package_mutation_mode(
            declaration,
            process_environment=_process_environment(
                declaration,
                "PIP_DRY_RUN",
                value="maybe",
            ),
        )

        self.assertIsInstance(result, PackageManagerSemanticProblem)
        assert isinstance(result, PackageManagerSemanticProblem)
        self.assertEqual(result.reason, "pip_dry_run_environment_value_invalid")
        self.assertEqual(result.blocking_source, "process_environment")

    def test_manager_environment_and_target_destination_are_independent_facts(self) -> None:
        declaration = _declaration(
            "pip",
            "--python",
            "/opt/manager/bin/python",
            "install",
            "--target",
            "vendor",
            "-r",
            "requirements.txt",
        )

        manager = resolve_manager_environment_selection(declaration)
        destination = resolve_installation_destination(declaration)

        self.assertIsInstance(manager, ManagerEnvironmentSelectionFact)
        self.assertIsInstance(destination, InstallationDestinationFact)
        assert isinstance(manager, ManagerEnvironmentSelectionFact)
        assert isinstance(destination, InstallationDestinationFact)
        self.assertEqual(manager.environment.value, "/opt/manager/bin/python")
        self.assertEqual(destination.destination.kind, "target_directory")
        self.assertEqual(destination.destination.value, "vendor")

    def test_supported_alternate_destination_selectors_remain_typed(self) -> None:
        cases = (
            (("--user",), "user_scheme", None),
            (("--prefix", "/opt/prefix"), "prefix_scheme", "/opt/prefix"),
            (("--root", "/staging"), "root_relocated_scheme", "/staging"),
            (("--target=vendor",), "target_directory", "vendor"),
        )
        for arguments, expected_kind, expected_value in cases:
            with self.subTest(arguments=arguments):
                declaration = _declaration("pip", "install", *arguments, "demo")
                result = resolve_installation_destination(declaration)
                self.assertIsInstance(result, InstallationDestinationFact)
                assert isinstance(result, InstallationDestinationFact)
                self.assertEqual(result.destination.kind, expected_kind)
                self.assertEqual(result.destination.value, expected_value)

    def test_empty_inline_destination_is_command_line_problem(self) -> None:
        declaration = _declaration("pip", "install", "--target=", "demo")
        result = resolve_installation_destination(declaration)

        self.assertIsInstance(result, PackageManagerSemanticProblem)
        assert isinstance(result, PackageManagerSemanticProblem)
        self.assertEqual(result.reason, "installation_destination_missing_value")
        self.assertEqual(result.blocking_source, "command_line")

    def test_no_deps_is_not_treated_as_direct_requirement_exclusion(self) -> None:
        declaration = _declaration(
            "pip",
            "install",
            "--no-deps",
            "-r",
            "requirements.txt",
        )
        result = resolve_direct_requirement_handling(declaration)

        self.assertIsInstance(result, PackageManagerSemanticProblem)
        assert isinstance(result, PackageManagerSemanticProblem)
        self.assertEqual(
            result.reason,
            "direct_requirement_handling_needs_lower_source_evidence",
        )
        self.assertIn("does not exclude", result.detail)
        self.assertNotEqual(result.reason, "direct_requirement_excluded")

    def test_explicit_only_deps_is_decisive_direct_requirement_exclusion(self) -> None:
        declaration = _declaration(
            "pip",
            "install",
            "--only-deps",
            "-r",
            "requirements.txt",
        )
        result = resolve_direct_requirement_handling(declaration)

        self.assertIsInstance(result, DirectRequirementHandlingFact)
        assert isinstance(result, DirectRequirementHandlingFact)
        self.assertEqual(result.handling, "excluded")

    def test_dynamic_unknown_install_argument_remains_dimension_problem(self) -> None:
        declaration = _declaration(
            "pip",
            "install",
            _dynamic("${{ matrix.pip_flags }}"),
            "-r",
            "requirements.txt",
        )

        mutation = resolve_package_mutation_mode(declaration)
        destination = resolve_installation_destination(declaration)
        direct = resolve_direct_requirement_handling(declaration)

        for result in (mutation, destination, direct):
            self.assertIsInstance(result, PackageManagerSemanticProblem)
            assert isinstance(result, PackageManagerSemanticProblem)
            self.assertEqual(result.blocking_source, "command_line")

    def test_dynamic_cli_material_blocks_otherwise_visible_semantic_winners(self) -> None:
        declaration = _declaration(
            "pip",
            "install",
            "--target",
            "vendor",
            "--dry-run",
            "--only-deps",
            _dynamic("${{ matrix.extra_pip_flags }}"),
            "-r",
            "requirements.txt",
        )

        for result in (
            resolve_installation_destination(declaration),
            resolve_package_mutation_mode(declaration),
            resolve_direct_requirement_handling(declaration),
        ):
            self.assertIsInstance(result, PackageManagerSemanticProblem)
            assert isinstance(result, PackageManagerSemanticProblem)
            self.assertEqual(result.blocking_source, "command_line")

    def test_dynamic_requirement_value_is_not_misread_as_unknown_option_bundle(self) -> None:
        declaration = _declaration(
            "pip",
            "install",
            "-r",
            _dynamic("${{ matrix.requirements_file }}"),
        )
        result = resolve_package_mutation_mode(declaration)

        self.assertIsInstance(result, PackageManagerSemanticProblem)
        assert isinstance(result, PackageManagerSemanticProblem)
        self.assertEqual(
            result.reason,
            "package_mutation_mode_needs_lower_source_evidence",
        )
        self.assertEqual(result.blocking_source, "process_environment")

    def test_one_declaration_feeds_all_semantic_dimensions_without_reparsing(self) -> None:
        declaration = _declaration(
            "pip",
            "--python",
            "/opt/manager/bin/python",
            "install",
            "--target",
            "vendor",
            "--dry-run",
            "--only-deps",
            "-r",
            "requirements.txt",
        )

        facts = (
            resolve_manager_environment_selection(declaration),
            resolve_installation_destination(declaration),
            resolve_package_mutation_mode(declaration),
            resolve_direct_requirement_handling(declaration),
        )

        self.assertTrue(
            all(
                isinstance(
                    fact,
                    (
                        ManagerEnvironmentSelectionFact,
                        InstallationDestinationFact,
                        PackageMutationModeFact,
                        DirectRequirementHandlingFact,
                    ),
                )
                for fact in facts
            )
        )
        self.assertEqual(
            {fact.command_location for fact in facts},
            {declaration.command_location},
        )


if __name__ == "__main__":
    unittest.main()
