"""Parser-backed static command analysis for GitHub Actions ``run`` steps.

RESPONSIBILITY
--------------
This module converts one already-resolved GitHub Actions shell context plus ``run`` text
into parser-neutral UpgradePilot command occurrences:

effective shell context
→ shell-family Tree-sitter parser
→ real syntactic command nodes
→ source spans + literal/dynamic atoms + structural context

It deliberately does not assign dependency meaning, prove command execution/success, or
strengthen runtime evidence. Tree-sitter ``Node`` objects never leave this module.

Parser uncertainty is fail-closed. A material parse error makes the whole run analysis
unresolved rather than falling back to the previous textual splitters.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Literal

import tree_sitter_bash
import tree_sitter_batch
import tree_sitter_pwsh
from tree_sitter import Language, Node, Parser

from .workflow_command_shell import (
    EffectiveShellContext,
    ShellSyntaxFamily,
    resolve_effective_shell_context,
)
from .workflow_definition import RunStepDefinition, StepsJobDefinition, WorkflowDefinition


type StaticCommandAnalysisState = Literal[
    "analyzable", "unresolved", "unsupported", "parse_error"
]
type StaticCommandAtomState = Literal["literal", "dynamic", "unsupported"]
type StaticCommandStructure = Literal[
    "straightforward_top_level",
    "linear_chain",
    "short_circuit",
    "conditional",
    "loop",
    "pipeline",
    "function_or_block",
    "nested_or_subshell",
]


@dataclass(frozen=True, slots=True)
class CommandSourceSpan:
    """UTF-8 byte span plus Tree-sitter row/byte-column points within ``run`` text."""

    start_byte: int
    end_byte: int
    start_line: int
    start_column: int
    end_line: int
    end_column: int


@dataclass(frozen=True, slots=True)
class StaticCommandAtom:
    """One statically recoverable executable/argument atom."""

    raw_source: str
    literal_value: str | None
    state: StaticCommandAtomState


@dataclass(frozen=True, slots=True)
class StaticCommandOccurrence:
    """One real syntactic command occurrence in deterministic source order."""

    source_order: int
    source_span: CommandSourceSpan
    raw_source: str
    executable: StaticCommandAtom
    arguments: tuple[StaticCommandAtom, ...]
    structural_context: tuple[StaticCommandStructure, ...]


@dataclass(frozen=True, slots=True)
class StaticCommandProblem:
    """Structured reason why stronger static command interpretation was not admitted."""

    reason: str
    detail: str
    source_span: CommandSourceSpan | None = None


@dataclass(frozen=True, slots=True)
class StaticCommandAnalysis:
    """Parser-neutral result for one GitHub Actions ``run`` declaration."""

    state: StaticCommandAnalysisState
    shell_context: EffectiveShellContext
    command_occurrences: tuple[StaticCommandOccurrence, ...]
    problems: tuple[StaticCommandProblem, ...]


_MAX_TREE_NODES = 50_000
_MAX_TREE_DEPTH = 200

_BASH_DYNAMIC_TYPES = frozenset(
    {
        "arithmetic_expansion",
        "command_substitution",
        "expansion",
        "process_substitution",
        "simple_expansion",
    }
)
_POWERSHELL_DYNAMIC_TYPES = frozenset(
    {
        "array_expression",
        "hashtable",
        "script_block",
        "script_block_expression",
        "sub_expression",
        "variable",
    }
)
_CMD_DYNAMIC_MARKERS = ("%", "!", "^")


def analyze_run_step_commands(
    workflow: WorkflowDefinition,
    job: StepsJobDefinition,
    step: RunStepDefinition,
) -> StaticCommandAnalysis:
    """Parse one static run step into shared command occurrences.

    The result establishes source syntax only. It does not establish that any occurrence
    executed, succeeded, or installed a dependency.
    """

    shell_context = resolve_effective_shell_context(workflow, job, step)
    if shell_context.state != "resolved" or shell_context.syntax_family is None:
        state: StaticCommandAnalysisState = (
            "unsupported" if shell_context.state == "unsupported" else "unresolved"
        )
        return StaticCommandAnalysis(
            state=state,
            shell_context=shell_context,
            command_occurrences=(),
            problems=(
                StaticCommandProblem(
                    reason=shell_context.reason or "shell_context_not_resolved",
                    detail=(
                        "Static command analysis requires an admitted, statically resolved "
                        "shell syntax family."
                    ),
                ),
            ),
        )

    source = step.command.text.encode("utf-8")
    root = Parser(_language_for_family(shell_context.syntax_family)).parse(source).root_node

    if root.has_error:
        return StaticCommandAnalysis(
            state="parse_error",
            shell_context=shell_context,
            command_occurrences=(),
            problems=(
                StaticCommandProblem(
                    reason="material_shell_parse_error",
                    detail=(
                        "Tree-sitter reported an error in the run script; command meaning "
                        "remains unresolved and no textual fallback is permitted."
                    ),
                    source_span=_source_span(root),
                ),
            ),
        )

    command_nodes, traversal_problem = _collect_command_nodes(
        root, shell_context.syntax_family
    )
    if traversal_problem is not None:
        return StaticCommandAnalysis(
            state="unresolved",
            shell_context=shell_context,
            command_occurrences=(),
            problems=(traversal_problem,),
        )

    ordered = sorted(command_nodes, key=lambda item: (item.start_byte, item.end_byte))
    occurrences = tuple(
        _occurrence_from_node(
            node,
            source=source,
            family=shell_context.syntax_family,
            source_order=index,
            root=root,
        )
        for index, node in enumerate(ordered)
    )
    return StaticCommandAnalysis(
        state="analyzable",
        shell_context=shell_context,
        command_occurrences=occurrences,
        problems=(),
    )


@lru_cache(maxsize=3)
def _language_for_family(family: ShellSyntaxFamily) -> Language:
    if family == "bash":
        return Language(tree_sitter_bash.language())
    if family == "powershell":
        return Language(tree_sitter_pwsh.language())
    if family == "cmd":
        return Language(tree_sitter_batch.language())
    raise AssertionError(f"unhandled shell syntax family: {family}")


def _collect_command_nodes(
    root: Node, family: ShellSyntaxFamily
) -> tuple[tuple[Node, ...], StaticCommandProblem | None]:
    command_type = {"bash": "command", "powershell": "command", "cmd": "cmd"}[family]
    found: list[Node] = []
    stack: list[tuple[Node, int]] = [(root, 0)]
    visited = 0

    while stack:
        node, depth = stack.pop()
        visited += 1
        if visited > _MAX_TREE_NODES:
            return (), StaticCommandProblem(
                reason="shell_tree_visit_limit",
                detail="Shell syntax tree exceeded the bounded traversal visit limit.",
            )
        if depth > _MAX_TREE_DEPTH:
            return (), StaticCommandProblem(
                reason="shell_tree_depth_limit",
                detail="Shell syntax tree exceeded the bounded traversal depth limit.",
            )

        if node.type == command_type:
            found.append(node)
        for child in reversed(node.named_children):
            stack.append((child, depth + 1))

    return tuple(found), None


def _occurrence_from_node(
    node: Node,
    *,
    source: bytes,
    family: ShellSyntaxFamily,
    source_order: int,
    root: Node,
) -> StaticCommandOccurrence:
    if family == "bash":
        executable_node, argument_nodes = _bash_command_parts(node)
    elif family == "powershell":
        executable_node, argument_nodes = _powershell_command_parts(node)
    else:
        executable_node, argument_nodes = _cmd_command_parts(node)

    return StaticCommandOccurrence(
        source_order=source_order,
        source_span=_source_span(node),
        raw_source=_node_text(node, source),
        executable=_atom_from_node(executable_node, source, family),
        arguments=tuple(
            _atom_from_node(argument_node, source, family)
            for argument_node in argument_nodes
        ),
        structural_context=_structural_context(node, root, source, family),
    )


def _bash_command_parts(node: Node) -> tuple[Node, tuple[Node, ...]]:
    children = tuple(node.named_children)
    for index, child in enumerate(children):
        if child.type == "command_name":
            return child, children[index + 1 :]
    return node, ()


def _powershell_command_parts(node: Node) -> tuple[Node, tuple[Node, ...]]:
    name = node.child_by_field_name("command_name")
    if name is None:
        name = next(
            (child for child in node.named_children if child.type == "command_name"), node
        )

    elements = node.child_by_field_name("command_elements")
    if elements is None:
        elements = next(
            (child for child in node.named_children if child.type == "command_elements"),
            None,
        )
    if elements is None:
        return name, ()

    return name, tuple(
        child
        for child in elements.named_children
        if child.type != "command_argument_sep"
    )


def _cmd_command_parts(node: Node) -> tuple[Node, tuple[Node, ...]]:
    children = tuple(node.named_children)
    name = next((child for child in children if child.type == "command_name"), node)
    argument_list = next(
        (child for child in children if child.type == "argument_list"), None
    )
    if argument_list is None:
        return name, ()
    return name, tuple(argument_list.named_children)


def _atom_from_node(
    node: Node, source: bytes, family: ShellSyntaxFamily
) -> StaticCommandAtom:
    raw = _node_text(node, source)
    if "${{" in raw:
        return StaticCommandAtom(raw_source=raw, literal_value=None, state="dynamic")

    if family == "bash" and _contains_descendant_type(node, _BASH_DYNAMIC_TYPES):
        return StaticCommandAtom(raw_source=raw, literal_value=None, state="dynamic")
    if family == "powershell" and _contains_descendant_type(
        node, _POWERSHELL_DYNAMIC_TYPES
    ):
        return StaticCommandAtom(raw_source=raw, literal_value=None, state="dynamic")
    if family == "cmd" and any(marker in raw for marker in _CMD_DYNAMIC_MARKERS):
        return StaticCommandAtom(raw_source=raw, literal_value=None, state="dynamic")

    literal = _decode_simple_literal(raw, family)
    if literal is None:
        return StaticCommandAtom(raw_source=raw, literal_value=None, state="unsupported")
    return StaticCommandAtom(raw_source=raw, literal_value=literal, state="literal")


def _contains_descendant_type(node: Node, blocked: frozenset[str]) -> bool:
    stack = [node]
    visited = 0
    while stack:
        current = stack.pop()
        visited += 1
        if visited > 1_000:
            return True
        if current.type in blocked:
            return True
        stack.extend(current.named_children)
    return False


def _decode_simple_literal(raw: str, family: ShellSyntaxFamily) -> str | None:
    value = raw.strip()
    if not value:
        return None

    if value[0:1] == value[-1:] and value[0] in {"'", '"'}:
        body = value[1:-1]
        if family == "bash":
            if value[0] == '"' and "\\" in body:
                return None
            return body
        if family == "powershell":
            if value[0] == '"' and ("`" in body or "$" in body):
                return None
            if value[0] == "'" and "''" in body:
                return None
            return body
        if family == "cmd":
            if any(marker in body for marker in _CMD_DYNAMIC_MARKERS):
                return None
            return body

    if any(character.isspace() for character in value):
        return None
    return value


def _structural_context(
    node: Node,
    root: Node,
    source: bytes,
    family: ShellSyntaxFamily,
) -> tuple[StaticCommandStructure, ...]:
    tags: list[StaticCommandStructure] = []
    ancestors = _ancestors(node, root)

    if family == "bash":
        _append_if(
            tags,
            any(item.type in {"if_statement", "case_statement"} for item in ancestors),
            "conditional",
        )
        _append_if(
            tags,
            any(
                item.type
                in {
                    "for_statement",
                    "c_style_for_statement",
                    "while_statement",
                    "until_statement",
                }
                for item in ancestors
            ),
            "loop",
        )
        _append_if(tags, any(item.type == "pipeline" for item in ancestors), "pipeline")
        _append_if(
            tags,
            any(
                item.type in {"subshell", "command_substitution"} for item in ancestors
            ),
            "nested_or_subshell",
        )
        _append_if(
            tags,
            any(item.type == "function_definition" for item in ancestors),
            "function_or_block",
        )
        list_ancestor = next((item for item in ancestors if item.type == "list"), None)
        if list_ancestor is not None:
            tags.append(
                "short_circuit"
                if _has_operator(list_ancestor, source, {"&&", "||"})
                else "linear_chain"
            )
        elif not tags and _direct_named_child_count(root, "command") > 1:
            tags.append("linear_chain")

    elif family == "powershell":
        _append_if(
            tags,
            any(item.type in {"if_statement", "switch_statement"} for item in ancestors),
            "conditional",
        )
        _append_if(
            tags,
            any(
                item.type
                in {
                    "for_statement",
                    "foreach_statement",
                    "while_statement",
                    "do_statement",
                }
                for item in ancestors
            ),
            "loop",
        )
        _append_if(
            tags,
            any(item.type == "function_statement" for item in ancestors),
            "function_or_block",
        )
        _append_if(
            tags,
            any(
                item.type in {"sub_expression", "script_block_expression"}
                for item in ancestors
            ),
            "nested_or_subshell",
        )
        pipeline = next((item for item in ancestors if item.type == "pipeline"), None)
        chain = next((item for item in ancestors if item.type == "pipeline_chain"), None)
        if pipeline is not None and _has_named_child(pipeline, "pipeline_chain_tail"):
            tags.append("short_circuit")
        elif chain is not None and _direct_named_child_count(chain, "command") > 1:
            tags.append("pipeline")
        statement_list = next(
            (item for item in ancestors if item.type == "statement_list"), None
        )
        if (
            statement_list is not None
            and not {"short_circuit", "pipeline"}.intersection(tags)
            and _powershell_statement_count(statement_list) > 1
        ):
            tags.append("linear_chain")

    else:
        _append_if(tags, any(item.type == "if_stmt" for item in ancestors), "conditional")
        _append_if(tags, any(item.type == "for_stmt" for item in ancestors), "loop")
        _append_if(tags, any(item.type == "pipe_stmt" for item in ancestors), "pipeline")
        _append_if(
            tags, any(item.type == "cond_exec" for item in ancestors), "short_circuit"
        )
        _append_if(
            tags, any(item.type == "command_sep" for item in ancestors), "linear_chain"
        )
        if not tags and _direct_named_child_count(root, "cmd") > 1:
            tags.append("linear_chain")

    if not tags:
        tags.append("straightforward_top_level")
    return tuple(dict.fromkeys(tags))


def _ancestors(node: Node, root: Node) -> tuple[Node, ...]:
    ancestors: list[Node] = []
    current = node.parent
    depth = 0
    while current is not None:
        ancestors.append(current)
        if current == root:
            break
        current = current.parent
        depth += 1
        if depth > _MAX_TREE_DEPTH:
            break
    return tuple(ancestors)


def _append_if(
    tags: list[StaticCommandStructure],
    condition: bool,
    value: StaticCommandStructure,
) -> None:
    if condition:
        tags.append(value)


def _has_operator(node: Node, source: bytes, operators: set[str]) -> bool:
    return any(
        _node_text(child, source).strip() in operators
        for child in node.children
        if not child.is_named
    )


def _has_named_child(node: Node, node_type: str) -> bool:
    return any(child.type == node_type for child in node.named_children)


def _direct_named_child_count(node: Node, node_type: str) -> int:
    return sum(1 for child in node.named_children if child.type == node_type)


def _powershell_statement_count(node: Node) -> int:
    return sum(
        1
        for child in node.named_children
        if child.type not in {"empty_statement", "comment"}
    )


def _node_text(node: Node, source: bytes) -> str:
    return source[node.start_byte : node.end_byte].decode("utf-8", errors="strict")


def _source_span(node: Node) -> CommandSourceSpan:
    start_line, start_column = tuple(node.start_point)
    end_line, end_column = tuple(node.end_point)
    return CommandSourceSpan(
        start_byte=node.start_byte,
        end_byte=node.end_byte,
        start_line=start_line,
        start_column=start_column,
        end_line=end_line,
        end_column=end_column,
    )


__all__ = (
    "CommandSourceSpan",
    "StaticCommandAnalysis",
    "StaticCommandAnalysisState",
    "StaticCommandAtom",
    "StaticCommandAtomState",
    "StaticCommandOccurrence",
    "StaticCommandProblem",
    "StaticCommandStructure",
    "analyze_run_step_commands",
)
