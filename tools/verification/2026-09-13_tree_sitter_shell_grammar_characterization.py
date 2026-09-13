"""Characterize the Tree-sitter shell grammars selected by ADR-0009.

Responsibility
--------------
This retained developer probe verifies the exact Cycle-1 parser trial set against
UpgradePilot's real static GitHub Actions workflow IR, then prints the concrete syntax
Tree (CST) shapes, source spans, and parser-error behavior needed before permanent shell
adapters are implemented.

Why retained
------------
The accepted implementation depends on external grammar node/error behavior that should
be observed rather than guessed from package documentation. Keeping this exact probe
makes the compatibility/admission checkpoint replayable when parser versions change.

This does NOT prove
-------------------
- that a shell command executed or succeeded;
- that every valid Bash, PowerShell, or CMD program is supported;
- that the eventual UpgradePilot adapter is correct;
- that these exact package versions are the final long-term dependency constraints.

Local assumptions
-----------------
Run from the UpgradePilot repository with its virtual environment active after installing
exactly the trial versions printed by ``REQUIRED_VERSIONS`` below.
"""

from __future__ import annotations

import importlib
import importlib.metadata
from dataclasses import dataclass

from tree_sitter import Language, Node, Parser

from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.workflow_definition import (
    RunStepDefinition,
    StepsJobDefinition,
    WorkflowDefinition,
    parse_workflow_definition,
)

REQUIRED_VERSIONS = {
    "tree-sitter": "0.24.0",
    "tree-sitter-bash": "0.25.1",
    "tree-sitter-pwsh": "0.38.1",
    "tree-sitter-batch": "0.11.1",
}

GRAMMAR_MODULES = {
    "bash": "tree_sitter_bash",
    "powershell": "tree_sitter_pwsh",
    "cmd": "tree_sitter_batch",
}

_MAX_TREE_DEPTH = 4
_MAX_TEXT = 90


@dataclass(frozen=True, slots=True)
class Fixture:
    name: str
    shell: str
    command: str


FIXTURES: tuple[Fixture, ...] = (
    # Bash / sh family
    Fixture("bash_simple", "bash", "python -m pip install -r requirements.txt"),
    Fixture("bash_comment", "bash", "echo ready # pip install -r fake.txt"),
    Fixture("bash_quoted", "bash", 'echo "note; pip install -r fake.txt"'),
    Fixture("bash_multiple", "bash", "echo ready && python -m pip install -r requirements.txt"),
    Fixture("bash_short_circuit", "bash", "true || python -m pip install -r requirements.txt"),
    Fixture(
        "bash_conditional",
        "bash",
        "if false; then\n  python -m pip install -r requirements.txt\nfi\necho done",
    ),
    Fixture("bash_pipeline", "bash", "printf '%s\\n' x | grep x"),
    Fixture("bash_malformed", "bash", "if true; then\n  echo broken"),
    Fixture("bash_unicode", "bash", 'echo "café ☕"'),
    # PowerShell / pwsh family
    Fixture("powershell_simple", "pwsh", "python -m pip install -r requirements.txt"),
    Fixture("powershell_comment", "pwsh", "Write-Output ready # pip install -r fake.txt"),
    Fixture("powershell_quoted", "pwsh", 'Write-Output "note; pip install -r fake.txt"'),
    Fixture(
        "powershell_multiple",
        "pwsh",
        "Write-Output ready; python -m pip install -r requirements.txt",
    ),
    Fixture(
        "powershell_short_circuit",
        "pwsh",
        "Write-Output ready || python -m pip install -r requirements.txt",
    ),
    Fixture(
        "powershell_conditional",
        "pwsh",
        "if ($false) { python -m pip install -r requirements.txt }; Write-Output done",
    ),
    Fixture("powershell_pipeline", "pwsh", "Get-Process | Sort-Object CPU"),
    Fixture("powershell_malformed", "pwsh", "if ($true) { Write-Output broken"),
    Fixture("powershell_unicode", "pwsh", 'Write-Output "café ☕"'),
    # Windows CMD / Batch family
    Fixture("cmd_simple", "cmd", "python -m pip install -r requirements.txt"),
    Fixture("cmd_comment", "cmd", "REM pip install -r fake.txt\necho ready"),
    Fixture("cmd_quoted", "cmd", 'echo "note & pip install -r fake.txt"'),
    Fixture(
        "cmd_multiple",
        "cmd",
        "echo ready & python -m pip install -r requirements.txt",
    ),
    Fixture(
        "cmd_short_circuit",
        "cmd",
        "ver >nul || python -m pip install -r requirements.txt",
    ),
    Fixture(
        "cmd_conditional",
        "cmd",
        "if 1==2 (python -m pip install -r requirements.txt) else (echo done)",
    ),
    Fixture("cmd_pipeline", "cmd", "echo x | findstr x"),
    Fixture("cmd_malformed", "cmd", "if 1==1 (echo broken"),
    Fixture("cmd_unicode", "cmd", "echo café ☕"),
)


def main() -> int:
    _verify_exact_trial_versions()
    parsers = {family: _build_parser(module_name) for family, module_name in GRAMMAR_MODULES.items()}

    print("TREE_SITTER_SHELL_CHARACTERIZATION")
    print("versions=" + ", ".join(f"{name}=={version}" for name, version in REQUIRED_VERSIONS.items()))

    for fixture in FIXTURES:
        step = _workflow_run_step(fixture)
        source = step.command.text.encode("utf-8")
        family = _syntax_family(fixture.shell)
        root = parsers[family].parse(source).root_node

        if root.start_byte != 0 or root.end_byte != len(source):
            raise AssertionError(
                f"{fixture.name}: parser root span {root.start_byte}:{root.end_byte} "
                f"does not cover {len(source)} UTF-8 bytes"
            )

        print()
        print(f"[{fixture.name}] shell={fixture.shell} family={family}")
        print(f"command={step.command.text!r}")
        print(
            "root="
            f"{root.type} bytes={root.start_byte}:{root.end_byte} "
            f"points={tuple(root.start_point)}:{tuple(root.end_point)} "
            f"has_error={root.has_error}"
        )
        _print_named_tree(root, source)

    print()
    print("RESULT=PASS")
    print(
        "PASS means the exact trial packages imported, every fixture parsed, and root UTF-8 "
        "source spans covered the exact run text. Review the printed CST/error shapes before "
        "writing permanent adapters."
    )
    return 0


def _verify_exact_trial_versions() -> None:
    mismatches: list[str] = []
    for distribution, expected in REQUIRED_VERSIONS.items():
        try:
            actual = importlib.metadata.version(distribution)
        except importlib.metadata.PackageNotFoundError:
            mismatches.append(f"{distribution}: missing (expected {expected})")
            continue
        if actual != expected:
            mismatches.append(f"{distribution}: {actual} (expected {expected})")

    if mismatches:
        raise RuntimeError(
            "Tree-sitter characterization requires the exact Cycle-1 trial set:\n- "
            + "\n- ".join(mismatches)
        )


def _build_parser(module_name: str) -> Parser:
    grammar = importlib.import_module(module_name)
    language = Language(grammar.language())
    return Parser(language)


def _syntax_family(shell: str) -> str:
    if shell in {"bash", "sh"}:
        return "bash"
    if shell in {"pwsh", "powershell"}:
        return "powershell"
    if shell == "cmd":
        return "cmd"
    raise AssertionError(f"unmapped fixture shell: {shell}")


def _workflow_run_step(fixture: Fixture) -> RunStepDefinition:
    indented = "\n".join(f"          {line}" for line in fixture.command.splitlines())
    workflow = (
        "jobs:\n"
        "  characterize:\n"
        "    runs-on: ubuntu-latest\n"
        "    steps:\n"
        "      - shell: "
        + fixture.shell
        + "\n"
        "        run: |\n"
        + indented
        + "\n"
    )
    source = RepositoryTextFile(
        repository="example/project",
        path=".github/workflows/characterize.yml",
        revision="a" * 40,
        content=workflow,
    )
    definition = parse_workflow_definition(source)
    if not isinstance(definition, WorkflowDefinition):
        raise AssertionError(f"{fixture.name}: workflow fixture did not parse: {definition!r}")
    job = definition.jobs[0]
    if not isinstance(job, StepsJobDefinition):
        raise AssertionError(f"{fixture.name}: expected a steps job, got {job!r}")
    step = job.steps[0]
    if not isinstance(step, RunStepDefinition):
        raise AssertionError(f"{fixture.name}: expected a run step, got {step!r}")
    return step


def _print_named_tree(node: Node, source: bytes, *, depth: int = 0) -> None:
    if depth > _MAX_TREE_DEPTH:
        return
    if node.is_named:
        text = source[node.start_byte : node.end_byte].decode("utf-8", errors="replace")
        compact = " ".join(text.split())
        if len(compact) > _MAX_TEXT:
            compact = compact[: _MAX_TEXT - 3] + "..."
        flags: list[str] = []
        if node.has_error:
            flags.append("has_error")
        if getattr(node, "is_error", False):
            flags.append("ERROR")
        if getattr(node, "is_missing", False):
            flags.append("MISSING")
        suffix = f" flags={','.join(flags)}" if flags else ""
        print(
            f"{'  ' * depth}- {node.type} "
            f"bytes={node.start_byte}:{node.end_byte} "
            f"points={tuple(node.start_point)}:{tuple(node.end_point)}"
            f"{suffix} text={compact!r}"
        )

    for child in node.named_children:
        _print_named_tree(child, source, depth=depth + 1)


if __name__ == "__main__":
    raise SystemExit(main())
