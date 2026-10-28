"""Source-only Python call/signature evidence for the API experiment.

Start with ``extract_python_source``, then ``compare_arguments``. Shared scoped
bindings still belong to api_python_bindings; this module adds argument shape and
declared parameter kinds. A selected source pair and receiver mode are conditions,
never proof of effective dispatch, installed versions, execution or compatibility.
No retained expression, default, annotation, decorator or module is executed.
The trial runner owns bounded processes, source admission and saved-file validation.
"""

from __future__ import annotations

import ast
import hashlib
import json
from dataclasses import dataclass
from typing import Literal

from .api_python_bindings import BindingAssessment, analyze_python_bindings

METHOD_VERSION = 1
ReceiverMode = Literal["as_written", "one_receiver_assumed", "unresolved"]
ParameterKind = Literal[
    "positional_only", "positional_or_keyword", "variadic_positional",
    "keyword_only", "variadic_keyword",
]


@dataclass(frozen=True)
class SourceSpan:
    """AST coordinates: lines start at one; columns count UTF-8 bytes from zero."""

    line: int
    column: int
    end_line: int
    end_column: int

    @classmethod
    def of(cls, node):
        return cls(node.lineno, node.col_offset, node.end_lineno, node.end_col_offset)


def fact_identity(kind: str, unit_id: str, span: SourceSpan) -> str:
    from dataclasses import astuple

    encoded = json.dumps([kind, unit_id, astuple(span)], separators=(",", ":"))
    return hashlib.sha256(encoded.encode()).hexdigest()


@dataclass(frozen=True)
class CallArguments:
    fact_id: str
    unit_id: str
    span: SourceSpan
    expression: str
    positional: tuple[Literal["ordinary", "starred"], ...]
    keywords: tuple[str | None, ...]
    argument_spans: tuple[SourceSpan, ...]
    complete: bool
    binding: BindingAssessment | None


@dataclass(frozen=True)
class ParameterFact:
    name: str
    kind: ParameterKind
    has_default: bool


@dataclass(frozen=True)
class CallableSignature:
    fact_id: str
    unit_id: str
    span: SourceSpan
    header_span: SourceSpan
    qualified_name: str
    kind: Literal["function", "async_function", "initializer"]
    parameters: tuple[ParameterFact, ...]
    complete: bool
    decorators: tuple[str, ...]
    class_bases: tuple[str, ...]
    limitations: tuple[str, ...]


@dataclass(frozen=True)
class SourceFacts:
    unit_id: str
    calls: tuple[CallArguments, ...]
    signatures: tuple[CallableSignature, ...]
    problems: tuple[str, ...]
    ast_nodes: int


class AnalysisLimit(ValueError):
    """A work limit blocks affected completeness; it is never an empty finding."""


def _parameters(node) -> tuple[ParameterFact, ...]:
    args = node.args
    positional = [*args.posonlyargs, *args.args]
    first_default = len(positional) - len(args.defaults)
    parameters = [
        ParameterFact(
            arg.arg,
            "positional_only" if index < len(args.posonlyargs) else "positional_or_keyword",
            index >= first_default,
        )
        for index, arg in enumerate(positional)
    ]
    if args.vararg:
        parameters.append(ParameterFact(args.vararg.arg, "variadic_positional", False))
    parameters.extend(
        ParameterFact(arg.arg, "keyword_only", default is not None)
        for arg, default in zip(args.kwonlyargs, args.kw_defaults)
    )
    if args.kwarg:
        parameters.append(ParameterFact(args.kwarg.arg, "variadic_keyword", False))
    return tuple(parameters)


class _SignatureVisitor(ast.NodeVisitor):
    def __init__(self, unit_id, text, complete):
        self.unit_id, self.text, self.complete = unit_id, text, complete
        self.owners = []
        self.owner_kinds = []
        self.classes = []
        self.signatures = []

    def visit_ClassDef(self, node):
        self.owners.append(node.name)
        self.owner_kinds.append("class")
        self.classes.append(node)
        self.generic_visit(node)
        self.classes.pop()
        self.owner_kinds.pop()
        self.owners.pop()

    def visit_FunctionDef(self, node):
        span = SourceSpan.of(node)
        body = node.body[0]
        parameters = _parameters(node)
        limitations = []
        if self.classes and any(
            p.name.startswith("__") and not p.name.endswith("__") for p in parameters
        ):
            limitations.append("class_private_parameter_mangling_unsupported")
        kind = "async_function" if isinstance(node, ast.AsyncFunctionDef) else "function"
        if self.owner_kinds and self.owner_kinds[-1] == "class" and node.name == "__init__":
            kind = "initializer"
        self.signatures.append(CallableSignature(
            fact_identity("signature", self.unit_id, span), self.unit_id, span,
            SourceSpan(span.line, span.column, body.lineno, body.col_offset),
            ".".join([*self.owners, node.name]), kind, parameters, self.complete,
            tuple(ast.get_source_segment(self.text, d) or "" for d in node.decorator_list),
            tuple(ast.get_source_segment(self.text, b) or "" for b in self.classes[-1].bases)
            if self.classes else (),
            tuple(limitations),
        ))
        self.owners.append(node.name)
        self.owner_kinds.append("function")
        self.generic_visit(node)
        self.owner_kinds.pop()
        self.owners.pop()

    visit_AsyncFunctionDef = visit_FunctionDef


def extract_python_source(
    unit_id: str, text: str, *, complete: bool,
    max_nodes: int = 100_000, max_facts: int = 4096,
) -> SourceFacts:
    """Inspect a qualified full-file capture; completeness is host metadata, not a hash.

    The runner enforces memory/time around parsing itself. Node/fact limits here
    bound the following analysis. Unknown/legacy trace joins retain syntax facts
    without fabricating a positive imported origin.
    """
    try:
        tree = ast.parse(text)
    except (SyntaxError, ValueError, RecursionError):
        return SourceFacts(unit_id, (), (), ("unsupported_or_invalid_python_syntax",), 0)
    count = 0
    for _ in ast.walk(tree):
        count += 1
        if count > max_nodes:
            raise AnalysisLimit("ast_node_limit")
    problems = []
    try:
        _, references = analyze_python_bindings(unit_id, text, tree)
    except RecursionError:
        references = ()
        problems.append("binding_recursion_limit")
    by_span = {}
    for ref in references:
        if ref.kind != "call" or ref.binding is None:
            continue
        steps = [s for s in ref.binding.trace if s.operation == "reference"]
        if steps:
            last = steps[-1]
            key = SourceSpan(last.line, last.column, last.end_line, last.end_column)
            by_span.setdefault(key, []).append(ref)
    calls = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        span = SourceSpan.of(node)
        matches = by_span.get(span, [])
        ref = matches[0] if len(matches) == 1 else None
        # Keyword extraction already belongs to ReferenceFact. A trace-less AST
        # observation is still useful, but gains no imported-origin precision.
        keywords = tuple(None if k == "**" else k for k in ref.keyword_names) if ref else tuple(
            k.arg for k in node.keywords
        )
        calls.append(CallArguments(
            fact_identity("call", unit_id, span), unit_id, span,
            ast.get_source_segment(text, node.func) or "",
            tuple("starred" if isinstance(a, ast.Starred) else "ordinary" for a in node.args),
            keywords, tuple(SourceSpan.of(a) for a in (*node.args, *node.keywords)),
            complete, ref.binding if ref else None,
        ))
        if len(calls) > max_facts:
            raise AnalysisLimit("source_fact_limit")
    visitor = _SignatureVisitor(unit_id, text, complete)
    try:
        visitor.visit(tree)
    except RecursionError:
        return SourceFacts(unit_id, tuple(calls), (), ("signature_recursion_limit",), count)
    if len(calls) + len(visitor.signatures) > max_facts:
        raise AnalysisLimit("source_fact_limit")
    key = lambda fact: (fact.span.line, fact.span.column, fact.span.end_line, fact.span.end_column)
    return SourceFacts(unit_id, tuple(sorted(calls, key=key)),
                       tuple(sorted(visitor.signatures, key=key)), tuple(problems), count)


@dataclass(frozen=True)
class KeywordReception:
    name: str
    outcome: Literal["named_parameter", "variadic_keyword", "not_received", "undetermined"]


@dataclass(frozen=True)
class BindingViolation:
    reason: str
    parameter: str | None


@dataclass(frozen=True)
class ArgumentComparison:
    call_id: str
    signature_id: str
    receiver_mode: ReceiverMode
    outcome: Literal["rejected", "bound", "undetermined"]
    checks_complete: bool
    keyword_reception: tuple[KeywordReception, ...]
    violations: tuple[BindingViolation, ...]
    unresolved_checks: tuple[str, ...]
    remaining_premises: tuple[str, ...]


def compare_arguments(
    call: CallArguments, signature: CallableSignature, receiver_mode: ReceiverMode,
) -> ArgumentComparison:
    """Compare declared syntax under a selected pairing, without solving dispatch.

    Positional-only names never fill keyword slots, including when the same name
    legitimately enters **kwargs. This explicitly handles the local 3.12 inspect
    helper disagreement preserved in the design. No argument values are needed.
    """
    if receiver_mode not in {"as_written", "one_receiver_assumed", "unresolved"}:
        raise ValueError("Unsupported receiver mode.")
    unresolved = []
    if not call.complete:
        unresolved.append("caller_source_coverage_limited")
    if not signature.complete:
        unresolved.append("signature_source_coverage_limited")
    unresolved.extend(signature.limitations)
    if receiver_mode == "unresolved":
        unresolved.append("receiver_binding_unresolved")
    if "starred" in call.positional:
        unresolved.append("positional_expansion_unresolved")
    if None in call.keywords:
        unresolved.append("keyword_expansion_unresolved")
    parameters = signature.parameters
    named = {p.name: p for p in parameters if p.kind in {"positional_or_keyword", "keyword_only"}}
    posonly = {p.name for p in parameters if p.kind == "positional_only"}
    positional = [p for p in parameters if p.kind in {"positional_only", "positional_or_keyword"}]
    has_varargs = any(p.kind == "variadic_positional" for p in parameters)
    has_kwargs = any(p.kind == "variadic_keyword" for p in parameters)
    signature_usable = signature.complete and not signature.limitations
    violations = []
    reception = []
    for name in call.keywords:
        if name is None:
            continue
        if not signature_usable:
            outcome = "undetermined"
        elif name in named:
            outcome = "named_parameter"
        elif has_kwargs:
            outcome = "variadic_keyword"
        else:
            outcome = "not_received"
            violations.append(BindingViolation(
                "positional_only_by_keyword" if name in posonly else "unexpected_keyword", name,
            ))
        reception.append(KeywordReception(name, outcome))
    complete = not unresolved
    if complete:
        # Only this branch knows all positional items and keyword names. A
        # starred syntax item is never counted as one expanded runtime value.
        count = len(call.positional) + (receiver_mode == "one_receiver_assumed")
        assigned = {p.name for p in positional[:count]}
        if count > len(positional) and not has_varargs:
            violations.append(BindingViolation("excess_positional", None))
        seen_keywords = set()
        for name in call.keywords:
            if name in seen_keywords:
                violations.append(BindingViolation("duplicate_keyword", name))
            seen_keywords.add(name)
            if name in named:
                if name in assigned:
                    violations.append(BindingViolation("duplicate_argument", name))
                assigned.add(name)
        for p in parameters:
            if p.kind not in {"variadic_positional", "variadic_keyword"} and not p.has_default and p.name not in assigned:
                violations.append(BindingViolation("missing_required_argument", p.name))
    else:
        unresolved.append("full_argument_binding_not_checked")
    premises = ["call_reaches_selected_declared_signature", "target_installed_versions_and_runtime_not_established"]
    if receiver_mode == "one_receiver_assumed":
        premises.append("one_bound_positional_receiver_assumed")
    if signature.decorators:
        premises.append("effective_decorator_signature_not_established")
    outcome = "rejected" if violations else "bound" if complete else "undetermined"
    return ArgumentComparison(call.fact_id, signature.fact_id, receiver_mode, outcome, complete,
                              tuple(reception), tuple(violations), tuple(unresolved), tuple(premises))
