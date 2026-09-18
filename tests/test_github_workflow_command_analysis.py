from __future__ import annotations

import unittest

from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.workflow_command_analysis import analyze_run_step_commands
from upgradepilot.github.workflow_command_shell import resolve_effective_shell_context
from upgradepilot.github.workflow_definition import (
    RunStepDefinition,
    StepsJobDefinition,
    WorkflowDefinition,
    parse_workflow_definition,
)


def _workflow(
    *,
    run: str,
    shell: str | None = None,
    runs_on: str = "ubuntu-latest",
    workflow_shell: str | None = None,
    job_shell: str | None = None,
    container: str | None = None,
) -> tuple[WorkflowDefinition, StepsJobDefinition, RunStepDefinition]:
    lines = []
    if workflow_shell is not None:
        lines.extend(["defaults:", "  run:", f"    shell: {workflow_shell}"])
    lines.extend(["jobs:", "  test:", f"    runs-on: {runs_on}"])
    if container is not None:
        lines.append(f"    container: {container}")
    if job_shell is not None:
        lines.extend(["    defaults:", "      run:", f"        shell: {job_shell}"])
    lines.append("    steps:")
    if shell is not None:
        lines.append(f"      - shell: {shell}")
        lines.append("        run: |")
    else:
        lines.append("      - run: |")
    lines.extend(f"          {line}" for line in run.splitlines())
    lines.append("")

    source = RepositoryTextFile(
        repository="example/project",
        path=".github/workflows/ci.yml",
        revision="a" * 40,
        content="\n".join(lines),
    )
    definition = parse_workflow_definition(source)
    assert isinstance(definition, WorkflowDefinition)
    job = definition.jobs[0]
    assert isinstance(job, StepsJobDefinition)
    step = job.steps[0]
    assert isinstance(step, RunStepDefinition)
    return definition, job, step


def _literal_values(analysis) -> tuple[str | None, ...]:
    occurrence = analysis.command_occurrences[0]
    return (
        occurrence.executable.literal_value,
        *(atom.literal_value for atom in occurrence.arguments),
    )


class EffectiveShellContextTests(unittest.TestCase):
    def test_precedence_is_step_then_job_then_workflow(self) -> None:
        workflow, job, step = _workflow(
            run="echo ok",
            shell="cmd",
            job_shell="pwsh",
            workflow_shell="bash",
            runs_on="windows-latest",
        )

        result = resolve_effective_shell_context(workflow, job, step)

        self.assertEqual(result.state, "resolved")
        self.assertEqual(result.source, "step")
        self.assertEqual(result.syntax_family, "cmd")
        self.assertEqual(result.execution_profile, "github_builtin_cmd")

    def test_dynamic_step_shell_shadows_lower_defaults(self) -> None:
        workflow, job, step = _workflow(
            run="echo ok",
            shell='"${{ matrix.shell }}"',
            job_shell="bash",
            workflow_shell="pwsh",
        )

        result = resolve_effective_shell_context(workflow, job, step)

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.source, "step")
        self.assertEqual(result.reason, "dynamic_shell_declaration")

    def test_hosted_platform_defaults_are_bounded(self) -> None:
        linux = _workflow(run="echo ok", runs_on="ubuntu-latest")
        windows = _workflow(run="Write-Output ok", runs_on="windows-latest")

        linux_result = resolve_effective_shell_context(*linux)
        windows_result = resolve_effective_shell_context(*windows)

        self.assertEqual(
            (linux_result.syntax_family, linux_result.execution_profile),
            ("bash", "github_default_non_windows"),
        )
        self.assertEqual(
            (windows_result.syntax_family, windows_result.execution_profile),
            ("powershell", "github_default_windows"),
        )

    def test_job_container_uses_distinct_sh_default(self) -> None:
        workflow, job, step = _workflow(
            run="echo ok",
            runs_on="ubuntu-latest",
            container="python:3.12",
        )

        result = resolve_effective_shell_context(workflow, job, step)

        self.assertEqual(result.source, "container_default")
        self.assertEqual(result.syntax_family, "bash")
        self.assertEqual(result.execution_profile, "github_default_container_sh")

    def test_dynamic_or_self_hosted_runner_does_not_invent_platform_default(self) -> None:
        dynamic = _workflow(run="echo ok", runs_on='"${{ matrix.os }}"')
        self_hosted = _workflow(run="echo ok", runs_on="self-hosted")

        dynamic_result = resolve_effective_shell_context(*dynamic)
        self_hosted_result = resolve_effective_shell_context(*self_hosted)

        self.assertEqual(dynamic_result.state, "unresolved")
        self.assertEqual(self_hosted_result.state, "unresolved")

    def test_custom_known_shell_keeps_syntax_but_custom_execution_profile(self) -> None:
        workflow, job, step = _workflow(
            run="echo ok",
            shell='"bash --noprofile {0}"',
        )

        result = resolve_effective_shell_context(workflow, job, step)

        self.assertEqual(result.state, "resolved")
        self.assertEqual(result.syntax_family, "bash")
        self.assertEqual(result.execution_profile, "custom_shell_template")

    def test_python_shell_is_not_misread_as_shell_script(self) -> None:
        workflow, job, step = _workflow(run="print('ok')", shell="python")

        result = resolve_effective_shell_context(workflow, job, step)

        self.assertEqual(result.state, "unsupported")
        self.assertEqual(result.reason, "python_shell_is_separate_language")


class StaticWorkflowCommandAnalysisTests(unittest.TestCase):
    def test_simple_external_command_atoms_are_shared_across_shell_families(self) -> None:
        cases = (
            ("bash", "ubuntu-latest"),
            ("pwsh", "windows-latest"),
            ("cmd", "windows-latest"),
        )

        for shell, runs_on in cases:
            with self.subTest(shell=shell):
                workflow, job, step = _workflow(
                    run="python -m pip install -r requirements.txt",
                    shell=shell,
                    runs_on=runs_on,
                )

                result = analyze_run_step_commands(workflow, job, step)

                self.assertEqual(result.state, "analyzable")
                self.assertEqual(len(result.command_occurrences), 1)
                self.assertEqual(
                    _literal_values(result),
                    ("python", "-m", "pip", "install", "-r", "requirements.txt"),
                )
                self.assertEqual(
                    result.command_occurrences[0].structural_context,
                    ("straightforward_top_level",),
                )
                self.assertEqual(
                    result.command_occurrences[0].whole_step_relation,
                    "sole_ordinary_top_level_command",
                )

    def test_comment_and_quoted_payloads_do_not_manufacture_commands(self) -> None:
        cases = (
            ("bash", 'echo "note; pip install -r fake.txt" # pip install -r fake2.txt'),
            ("pwsh", 'Write-Output "note; pip install -r fake.txt" # pip install -r fake2.txt'),
            ("cmd", 'REM pip install -r fake.txt\necho "note & pip install -r fake2.txt"'),
        )

        for shell, run in cases:
            with self.subTest(shell=shell):
                workflow, job, step = _workflow(run=run, shell=shell)
                result = analyze_run_step_commands(workflow, job, step)

                self.assertEqual(result.state, "analyzable")
                self.assertEqual(len(result.command_occurrences), 1)
                self.assertNotEqual(
                    result.command_occurrences[0].executable.literal_value, "pip"
                )

    def test_first_sequential_bash_command_gets_positive_whole_step_relation(self) -> None:
        workflow, job, step = _workflow(
            run=(
                "python -m pip install --no-cache-dir --upgrade pip -r requirements.txt\n"
                "python -m pip install ruff"
            ),
            shell="bash",
        )

        result = analyze_run_step_commands(workflow, job, step)

        self.assertEqual(result.state, "analyzable")
        self.assertEqual(len(result.command_occurrences), 2)
        first, second = result.command_occurrences
        self.assertEqual(
            first.whole_step_relation,
            "first_ordinary_top_level_command_in_sequential_script",
        )
        self.assertIsNone(second.whole_step_relation)
        self.assertIn("linear_chain", first.structural_context)
        self.assertIn("linear_chain", second.structural_context)

    def test_bash_false_straightforward_shapes_do_not_get_positive_whole_step_relation(self) -> None:
        cases = (
            (
                "! python -m pip install -r requirements.txt",
                "status_inverted",
            ),
            (
                "python -m pip install -r requirements.txt &",
                "asynchronous",
            ),
            (
                "cat <(python -m pip install -r requirements.txt)",
                "process_substitution",
            ),
            (
                "{ python -m pip install -r requirements.txt; }",
                None,
            ),
        )

        for run, expected_structure in cases:
            with self.subTest(run=run):
                workflow, job, step = _workflow(run=run, shell="bash")
                result = analyze_run_step_commands(workflow, job, step)

                self.assertEqual(result.state, "analyzable")
                target = next(
                    occurrence
                    for occurrence in result.command_occurrences
                    if occurrence.executable.literal_value == "python"
                )
                self.assertIsNone(target.whole_step_relation)
                if expected_structure is not None:
                    self.assertIn(expected_structure, target.structural_context)

    def test_non_command_control_flow_prevents_false_sole_admission(self) -> None:
        cases = (
            (
                "pwsh",
                "windows-latest",
                "exit 0\npython -m pip install -r requirements.txt",
            ),
            (
                "cmd",
                "windows-latest",
                "exit /b 0\npython -m pip install -r requirements.txt",
            ),
        )

        for shell, runs_on, run in cases:
            with self.subTest(shell=shell):
                workflow, job, step = _workflow(
                    run=run,
                    shell=shell,
                    runs_on=runs_on,
                )
                result = analyze_run_step_commands(workflow, job, step)

                self.assertEqual(result.state, "analyzable")
                target = next(
                    occurrence
                    for occurrence in result.command_occurrences
                    if occurrence.executable.literal_value == "python"
                )
                self.assertIsNone(target.whole_step_relation)

    def test_short_circuit_commands_remain_real_but_structurally_marked(self) -> None:
        cases = (
            ("bash", "true || python -m pip install -r requirements.txt"),
            ("pwsh", "Write-Output ready || python -m pip install -r requirements.txt"),
            ("cmd", "ver >nul || python -m pip install -r requirements.txt"),
        )

        for shell, run in cases:
            with self.subTest(shell=shell):
                workflow, job, step = _workflow(run=run, shell=shell)
                result = analyze_run_step_commands(workflow, job, step)

                self.assertEqual(result.state, "analyzable")
                self.assertEqual(len(result.command_occurrences), 2)
                install = result.command_occurrences[1]
                self.assertEqual(install.executable.literal_value, "python")
                self.assertIn("short_circuit", install.structural_context)

    def test_conditional_commands_are_preserved_without_top_level_claim(self) -> None:
        cases = (
            (
                "bash",
                "if false; then\n  python -m pip install -r requirements.txt\nfi\necho done",
            ),
            (
                "pwsh",
                "if ($false) { python -m pip install -r requirements.txt }; Write-Output done",
            ),
            (
                "cmd",
                "if 1==2 (python -m pip install -r requirements.txt) else (echo done)",
            ),
        )

        for shell, run in cases:
            with self.subTest(shell=shell):
                workflow, job, step = _workflow(run=run, shell=shell)
                result = analyze_run_step_commands(workflow, job, step)

                self.assertEqual(result.state, "analyzable")
                install = next(
                    occurrence
                    for occurrence in result.command_occurrences
                    if occurrence.executable.literal_value == "python"
                )
                self.assertIn("conditional", install.structural_context)
                self.assertNotIn(
                    "straightforward_top_level", install.structural_context
                )

    def test_pipelines_are_not_flattened_to_straightforward_commands(self) -> None:
        cases = (
            ("bash", "printf '%s\\n' x | grep x"),
            ("pwsh", "Get-Process | Sort-Object CPU"),
            ("cmd", "echo x | findstr x"),
        )

        for shell, run in cases:
            with self.subTest(shell=shell):
                workflow, job, step = _workflow(run=run, shell=shell)
                result = analyze_run_step_commands(workflow, job, step)

                self.assertEqual(result.state, "analyzable")
                self.assertEqual(len(result.command_occurrences), 2)
                for occurrence in result.command_occurrences:
                    self.assertIn("pipeline", occurrence.structural_context)

    def test_material_parse_error_fails_closed_without_partial_occurrences(self) -> None:
        cases = (
            ("bash", "if true; then\n  echo broken"),
            ("pwsh", "if ($true) { Write-Output broken"),
            ("cmd", "if 1==1 (echo broken"),
        )

        for shell, run in cases:
            with self.subTest(shell=shell):
                workflow, job, step = _workflow(run=run, shell=shell)
                result = analyze_run_step_commands(workflow, job, step)

                self.assertEqual(result.state, "parse_error")
                self.assertEqual(result.command_occurrences, ())
                self.assertEqual(result.problems[0].reason, "material_shell_parse_error")

    def test_unicode_occurrence_identity_uses_utf8_byte_span(self) -> None:
        workflow, job, step = _workflow(run='echo "café ☕"', shell="bash")

        result = analyze_run_step_commands(workflow, job, step)

        occurrence = result.command_occurrences[0]
        self.assertEqual(occurrence.raw_source, 'echo "café ☕"')
        self.assertEqual(
            occurrence.source_span.end_byte,
            len(occurrence.raw_source.encode("utf-8")),
        )

    def test_source_order_is_derived_from_parser_spans(self) -> None:
        workflow, job, step = _workflow(
            run="echo one\necho two\necho three",
            shell="bash",
        )

        result = analyze_run_step_commands(workflow, job, step)

        self.assertEqual(
            [item.source_order for item in result.command_occurrences],
            [0, 1, 2],
        )
        self.assertEqual(
            [item.executable.literal_value for item in result.command_occurrences],
            ["echo", "echo", "echo"],
        )
        self.assertEqual(
            sorted(item.source_span.start_byte for item in result.command_occurrences),
            [item.source_span.start_byte for item in result.command_occurrences],
        )


if __name__ == "__main__":
    unittest.main()
