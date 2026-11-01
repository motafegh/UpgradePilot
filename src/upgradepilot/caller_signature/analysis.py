"""Pure call/signature facts, before the parser/checker producer transfer.

Native representation consumes these records without loading an AST or executing
source. Conditional receiver and signature premises retain their original meaning.
"""
from __future__ import annotations
import hashlib
import json
from dataclasses import dataclass
from typing import Literal
from .bindings import BindingAssessment

ParameterKind = Literal["positional_only", "positional_or_keyword", "variadic_positional", "keyword_only", "variadic_keyword"]


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
