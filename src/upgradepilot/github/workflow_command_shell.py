"""Resolve the effective static shell for GitHub Actions ``run`` steps.

GitHub's workflow definition owns shell/default/runner/container facts. This module applies
their precedence once and returns two deliberately separate facts:

- ``syntax_family`` selects how static script text may be parsed;
- ``execution_profile`` records which GitHub/custom wrapper semantics are established.

Resolving either fact does not prove that a command executed or succeeded.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import PurePath
from typing import Literal

from .workflow_definition import (
    RunStepDefinition,
    StaticScalarValue,
    StepsJobDefinition,
    WorkflowDefinition,
)


type ShellSyntaxFamily = Literal["bash", "powershell", "cmd"]
type ShellExecutionProfile = Literal[
    "github_builtin_bash",
    "github_builtin_sh",
    "github_builtin_pwsh",
    "github_builtin_powershell",
    "github_builtin_cmd",
    "github_default_non_windows",
    "github_default_windows",
    "github_default_container_sh",
    "custom_shell_template",
]
type EffectiveShellState = Literal["resolved", "unresolved", "unsupported"]
type EffectiveShellSource = Literal[
    "step", "job", "workflow", "container_default", "platform_default"
]


@dataclass(frozen=True, slots=True)
class EffectiveShellContext:
    """Static shell context selected for one GitHub Actions run step."""

    state: EffectiveShellState
    source: EffectiveShellSource
    syntax_family: ShellSyntaxFamily | None
    execution_profile: ShellExecutionProfile | None
    raw_declaration: str | None
    reason: str | None = None


def resolve_effective_shell_context(
    workflow: WorkflowDefinition,
    job: StepsJobDefinition,
    step: RunStepDefinition,
) -> EffectiveShellContext:
    """Apply shell precedence without inventing runner or interpreter facts.

    A dynamic higher-precedence declaration shadows lower levels. Passing this resolver
    authorizes syntax parsing only; runtime-execution authority remains a later concern.
    """

    candidates: tuple[
        tuple[EffectiveShellSource, StaticScalarValue | None], ...
    ] = (
        ("step", step.shell),
        ("job", job.run_defaults.shell if job.run_defaults is not None else None),
        (
            "workflow",
            workflow.run_defaults.shell if workflow.run_defaults is not None else None,
        ),
    )

    for source, value in candidates:
        if value is None:
            continue
        if value.contains_expression:
            return EffectiveShellContext(
                state="unresolved",
                source=source,
                syntax_family=None,
                execution_profile=None,
                raw_declaration=value.text,
                reason="dynamic_shell_declaration",
            )
        return _literal_shell_context(value.text, source)

    # GitHub runs unspecialized job-container scripts with ``sh`` regardless of the
    # host runner's ordinary default. The job-container declaration itself establishes
    # this wrapper choice; its image string need not reveal a host platform.
    if job.container is not None:
        return EffectiveShellContext(
            state="resolved",
            source="container_default",
            syntax_family="bash",
            execution_profile="github_default_container_sh",
            raw_declaration=None,
        )

    return _platform_default_shell_context(job)


def _literal_shell_context(
    raw: str, source: EffectiveShellSource
) -> EffectiveShellContext:
    stripped = raw.strip()
    first_token = _first_shell_executable(stripped)
    if first_token is None:
        return EffectiveShellContext(
            state="unresolved",
            source=source,
            syntax_family=None,
            execution_profile=None,
            raw_declaration=raw,
            reason="empty_or_unreadable_shell_declaration",
        )

    executable = first_token.lower()
    builtins: dict[str, tuple[ShellSyntaxFamily, ShellExecutionProfile]] = {
        "bash": ("bash", "github_builtin_bash"),
        "sh": ("bash", "github_builtin_sh"),
        "pwsh": ("powershell", "github_builtin_pwsh"),
        "powershell": ("powershell", "github_builtin_powershell"),
        "cmd": ("cmd", "github_builtin_cmd"),
        "cmd.exe": ("cmd", "github_builtin_cmd"),
    }
    builtin = builtins.get(executable)

    if builtin is not None:
        family, builtin_profile = builtin
        exact_builtin = stripped.lower() in {executable, executable.removesuffix(".exe")}
        return EffectiveShellContext(
            state="resolved",
            source=source,
            syntax_family=family,
            execution_profile=(
                builtin_profile if exact_builtin else "custom_shell_template"
            ),
            raw_declaration=raw,
        )

    if executable in {"python", "python3", "python.exe"}:
        return EffectiveShellContext(
            state="unsupported",
            source=source,
            syntax_family=None,
            execution_profile=None,
            raw_declaration=raw,
            reason="python_shell_is_separate_language",
        )

    return EffectiveShellContext(
        state="unsupported",
        source=source,
        syntax_family=None,
        execution_profile=None,
        raw_declaration=raw,
        reason="unsupported_shell_interpreter",
    )


def _first_shell_executable(value: str) -> str | None:
    if not value:
        return None
    token = value.split(maxsplit=1)[0].strip("'\"")
    if not token:
        return None
    return PurePath(token.replace("\\", "/")).name or None


def _platform_default_shell_context(job: StepsJobDefinition) -> EffectiveShellContext:
    runs_on = job.runs_on
    if not isinstance(runs_on, StaticScalarValue):
        return _unresolved_platform(None, "runner_platform_not_statically_established")
    if runs_on.contains_expression:
        return _unresolved_platform(runs_on.text, "dynamic_runner_platform")

    label = runs_on.text.strip().lower()
    if label.startswith(("ubuntu-", "macos-")):
        return EffectiveShellContext(
            state="resolved",
            source="platform_default",
            syntax_family="bash",
            execution_profile="github_default_non_windows",
            raw_declaration=None,
        )
    if label.startswith("windows-"):
        return EffectiveShellContext(
            state="resolved",
            source="platform_default",
            syntax_family="powershell",
            execution_profile="github_default_windows",
            raw_declaration=None,
        )
    return _unresolved_platform(
        runs_on.text, "runner_platform_not_statically_established"
    )


def _unresolved_platform(raw: str | None, reason: str) -> EffectiveShellContext:
    return EffectiveShellContext(
        state="unresolved",
        source="platform_default",
        syntax_family=None,
        execution_profile=None,
        raw_declaration=raw,
        reason=reason,
    )


__all__ = (
    "EffectiveShellContext",
    "EffectiveShellSource",
    "EffectiveShellState",
    "ShellExecutionProfile",
    "ShellSyntaxFamily",
    "resolve_effective_shell_context",
)
