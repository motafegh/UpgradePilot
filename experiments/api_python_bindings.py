"""Ordered, scoped Python source associations for the API experiment.

Start at analyze_python_bindings with the already acquired file identity and AST.
Statements propagate possible imported origins; if branches join possibilities.
Functions get their own locals, and delayed outer/global reads remain uncertain.
Only an established assessment populates ReferenceFact.lexical_import, consumed
by adapter exploration. Traces are source observations, not execution histories.
No target code is executed and no installed distribution or compatibility follows.
"""

from __future__ import annotations

import ast
from dataclasses import asdict, dataclass, fields
from typing import Literal

BINDING_ANALYSIS_VERSION = 2
MAX_BINDING_ORIGINS = 32
MAX_BINDING_TRACE_STEPS = 128


@dataclass(frozen=True)
class ImportFact:
    source_id: str
    line: int
    module: str
    member: str | None
    alias: str | None
    relative_level: int
    module_level: bool


@dataclass(frozen=True)
class BindingTraceStep:
    """Exact file-linked AST span; columns count UTF-8 bytes, lines start at one."""

    source_id: str
    scope: str
    line: int
    column: int
    end_line: int
    end_column: int
    operation: str
    name: str
    origin: str | None = None
    input_name: str | None = None


@dataclass(frozen=True)
class BindingAssessment:
    """Imported alternatives and explicit unknown/unbound source possibilities.

    The trace includes overwritten/restored history and competing branches.
    With unknown_possible, origins are not exhaustive. Only established may
    become lexical_import; no state asserts execution.
    """

    state: Literal["established", "conditional", "unknown", "unbound"]
    possible_imports: tuple[str, ...]
    unknown_possible: bool
    unbound_possible: bool
    scope: str
    reasons: tuple[str, ...]
    trace: tuple[BindingTraceStep, ...]


@dataclass(frozen=True)
class ReferenceFact:
    source_id: str
    line: int
    kind: str
    expression: str
    lexical_import: str | None
    binding_limit: str | None
    keyword_names: tuple[str, ...] = ()
    positional_count: int = 0
    # None denotes a legacy producer/fixture, never newly inferred precision.
    binding: BindingAssessment | None = None


def binding_state(origins: tuple[str, ...], unknown: bool, unbound: bool) -> str:
    """One canonical possibility-to-state rule, also used at saved-input decoding."""
    if len(origins) == 1 and not unknown and not unbound:
        return "established"
    if len(origins) > 1 or origins and (unknown or unbound) or unknown and unbound:
        return "conditional"
    return "unbound" if unbound and not unknown else "unknown"


def _assessment(scope, origins=(), unknown=False, unbound=False, reasons=(), trace=()):
    origins = tuple(sorted(set(origins)))
    reasons = tuple(dict.fromkeys(reasons))
    # A source-ordered trace records all contributing observations, not an
    # invented linear execution path through both conditional branches.
    trace = tuple(
        sorted(
            set(trace), key=lambda s: (s.line, s.column, s.scope, s.operation, s.name)
        )
    )
    if len(origins) > MAX_BINDING_ORIGINS:
        origins = origins[:MAX_BINDING_ORIGINS]
        unknown = True
        reasons += ("binding_origin_budget_exhausted",)
    if len(trace) > MAX_BINDING_TRACE_STEPS:
        trace = trace[-MAX_BINDING_TRACE_STEPS:]
        unknown = True
        reasons += ("binding_trace_budget_exhausted",)
    return BindingAssessment(
        binding_state(origins, unknown, unbound),
        origins,
        unknown,
        unbound,
        scope,
        tuple(dict.fromkeys(reasons)),
        trace,
    )


def _dotted_name(node):
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        parent = _dotted_name(node.value)
        return f"{parent}.{node.attr}" if parent else None
    return None


class _ScopeNames(ast.NodeVisitor):
    """Names written in this lexical scope, never nested function/class bodies."""

    def __init__(self):
        self.writes = set()
        self.globals = set()
        self.nonlocals = set()
        self.star = False
        self.mutations = []
        self.calls = []

    def visit_Call(self, node):
        self.calls.append(node)
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, (ast.Store, ast.Del)):
            self.writes.add(node.id)

    def visit_Import(self, node):
        self.writes.update(a.asname or a.name.split(".")[0] for a in node.names)

    def visit_ImportFrom(self, node):
        self.star |= any(a.name == "*" for a in node.names)
        self.writes.update(a.asname or a.name for a in node.names if a.name != "*")

    def visit_FunctionDef(self, node):
        self.writes.add(node.name)
        for expression in (
            *node.decorator_list,
            *node.args.defaults,
            *[d for d in node.args.kw_defaults if d],
        ):
            self.visit(expression)

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_ClassDef(self, node):
        self.writes.add(node.name)
        for expression in (
            *node.decorator_list,
            *node.bases,
            *[k.value for k in node.keywords],
        ):
            self.visit(expression)

    def visit_Lambda(self, node):
        for expression in (
            *node.args.defaults,
            *[d for d in node.args.kw_defaults if d],
        ):
            self.visit(expression)

    def visit_Global(self, node):
        self.globals.update(node.names)

    def visit_Nonlocal(self, node):
        self.nonlocals.update(node.names)

    def visit_ExceptHandler(self, node):
        if node.name:
            self.writes.add(node.name)
        self.generic_visit(node)

    def visit_MatchAs(self, node):
        if node.name:
            self.writes.add(node.name)
        self.generic_visit(node)

    visit_MatchStar = visit_MatchAs

    def visit_MatchMapping(self, node):
        if node.rest:
            self.writes.add(node.rest)
        self.generic_visit(node)

    def visit_Attribute(self, node):
        if isinstance(node.ctx, (ast.Store, ast.Del)):
            self.mutations.append(node)
            root = _dotted_name(node.value)
            if root:
                self.writes.add(root.split(".")[0])
        self.generic_visit(node)

    visit_Subscript = visit_Attribute

    def _comprehension(self, node):
        # Comprehension iteration targets are local to its implicit scope;
        # assignment expressions can still write into the enclosing scope.
        for child in ast.walk(node):
            if isinstance(child, ast.NamedExpr):
                self.visit(child.target)

    visit_ListComp = _comprehension
    visit_SetComp = _comprehension
    visit_DictComp = _comprehension
    visit_GeneratorExp = _comprehension


class _ImportCollector(ast.NodeVisitor):
    """Syntax inventory retains true lexical scope even in unsupported control flow."""

    def __init__(self, identity):
        self.identity = identity
        self.module_level = True
        self.facts = []

    def visit_Import(self, node):
        self.facts.extend(
            ImportFact(
                self.identity,
                node.lineno,
                alias.name,
                None,
                alias.asname,
                0,
                self.module_level,
            )
            for alias in node.names
        )

    def visit_ImportFrom(self, node):
        self.facts.extend(
            ImportFact(
                self.identity,
                node.lineno,
                node.module or "",
                alias.name,
                alias.asname,
                node.level,
                self.module_level,
            )
            for alias in node.names
        )

    def visit_FunctionDef(self, node):
        previous = self.module_level
        self.module_level = False
        self.generic_visit(node)
        self.module_level = previous

    visit_AsyncFunctionDef = visit_FunctionDef
    visit_ClassDef = visit_FunctionDef


@dataclass
class _Frame:
    """One lexical namespace; branch forks copy values without merging scopes."""

    scope: str
    kind: str
    values: dict[str, BindingAssessment]
    locals: set[str]
    globals: set[str]
    nonlocals: set[str]
    outer: _Frame | None = None
    wildcard: bool = False
    limit: str | None = None

    def fork(self):
        return _Frame(
            self.scope,
            self.kind,
            dict(self.values),
            self.locals,
            self.globals,
            self.nonlocals,
            self.outer,
            self.wildcard,
            self.limit,
        )


class _Analyzer:
    """Module/class statements first, then hypothetical function bodies.

    Deferring bodies separates definition-time values from invocation-time
    globals. Local imports propagate in body order; outer reads and heap,
    annotation and unsupported-control effects retain limitation reasons.
    """

    def __init__(self, identity, content, tree):
        self.identity, self.content, self.tree = identity, content, tree
        collector = _ImportCollector(identity)
        collector.visit(tree)
        self.imports = collector.facts
        self.references = []
        self.functions = []
        self.module = _Frame("module", "module", {}, set(), set(), set())
        self.mutable_globals = set()
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                names = self.names(node.body)
                self.mutable_globals.update(names.globals & names.writes)
        self.dynamic_global_namespace = any(
            isinstance(child, ast.Name) and child.id == "globals"
            for node in ast.walk(tree)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            for child in ast.walk(node)
        )

    @staticmethod
    def names(nodes):
        names = _ScopeNames()
        for node in nodes:
            names.visit(node)
        return names

    def step(self, node, frame, operation, name="", origin=None, input_name=None):
        return BindingTraceStep(
            self.identity,
            frame.scope,
            node.lineno,
            node.col_offset,
            node.end_lineno,
            node.end_col_offset,
            operation,
            name,
            origin,
            input_name,
        )

    def uncertain(self, value, reason, node=None, frame=None):
        trace = value.trace
        if node is not None:
            trace += (self.step(node, frame, reason),)
        return _assessment(
            value.scope,
            value.possible_imports,
            True,
            value.unbound_possible,
            (*value.reasons, reason),
            trace,
        )

    def lookup(self, name, frame, node):
        if name in frame.values:
            value = frame.values[name]
        elif frame.kind == "function" and name in frame.locals:
            value = _assessment(
                frame.scope, unbound=True, reasons=("unbound_local_name",)
            )
        elif frame.kind == "function":
            # Function definition time is not invocation time. Preserve possible
            # outer origins for inspection, never as a unique lexical relation.
            parent = (
                frame.outer
                if frame.outer
                and frame.outer.kind == "function"
                and name not in frame.globals
                else self.module
            )
            value = parent.values.get(
                name, _assessment(parent.scope, unknown=True, unbound=True)
            )
            reason = (
                "closure_or_nonlocal_read"
                if parent is not self.module or name in frame.nonlocals
                else "delayed_global_read"
            )
            value = self.uncertain(value, reason, node, frame)
        elif frame.kind == "class" and frame.outer:
            value = self.lookup(name, frame.outer, node)
        else:
            value = _assessment(
                frame.scope,
                unknown=True,
                unbound=True,
                reasons=(
                    "wildcard_namespace_unknown"
                    if frame.wildcard
                    else "name_not_bound_in_examined_scope",
                ),
            )
        if frame.kind == "module" and name in self.mutable_globals:
            value = self.uncertain(value, "cross_scope_global_mutation", node, frame)
        if frame.kind == "module" and self.dynamic_global_namespace:
            value = self.uncertain(
                value, "dynamic_global_namespace_in_nested_scope", node, frame
            )
        return _assessment(
            frame.scope,
            value.possible_imports,
            value.unknown_possible,
            value.unbound_possible,
            value.reasons,
            value.trace,
        )

    def value(self, node, frame):
        if isinstance(node, ast.Name):
            return self.lookup(node.id, frame, node)
        return _assessment(frame.scope, unknown=True, reasons=("value_origin_unknown",))

    def assign(self, name, value, node, frame, operation, input_name=None):
        previous = frame.values.get(name)
        # Restoration retains the prior uncertain write as trace history; prior
        # uncertainty does not automatically contaminate the restored value.
        trace = (*previous.trace, *value.trace) if previous else value.trace
        trace += (self.step(node, frame, operation, name, input_name=input_name),)
        if value.unbound_possible:
            value = self.uncertain(value, "assignment_from_unbound_name")
        if name in frame.globals or name in frame.nonlocals:
            value = self.uncertain(value, "cross_scope_write_unmodeled")
        frame.values[name] = _assessment(
            frame.scope,
            value.possible_imports,
            value.unknown_possible,
            value.unbound_possible,
            value.reasons,
            trace,
        )

    def invalidate(self, names, node, frame, reason):
        for name in names:
            old = self.lookup(name, frame, node)
            frame.values[name] = self.uncertain(old, reason, node, frame)

    def namespace_limit(self, node, frame, reason):
        self.invalidate(set(frame.values) | frame.locals, node, frame, reason)
        frame.wildcard = True

    def mutation(self, target, node, frame):
        dotted = (
            _dotted_name(target.value)
            if isinstance(target, (ast.Attribute, ast.Subscript))
            else None
        )
        if dotted:
            root = dotted.split(".")[0]
            value = self.lookup(root, frame, node)
            affected = {root}
            if not value.possible_imports:
                # Unknown heap identity cannot prove independence from an
                # imported object or globals dictionary. This limitation is
                # explicit; ordinary object/heap alias propagation is unmodeled.
                self.namespace_limit(node, frame, "unknown_mutation_receiver")
                return
            for name, other in frame.values.items():
                if any(
                    a == b or a.startswith(b + ".") or b.startswith(a + ".")
                    for a in other.possible_imports
                    for b in value.possible_imports
                ):
                    affected.add(name)
            self.invalidate(affected, node, frame, "attribute_or_subscript_write")
        else:
            self.namespace_limit(node, frame, "dynamic_write_receiver")

    def reference(self, node, expression, kind, frame):
        dotted = _dotted_name(expression)
        if dotted:
            root, *suffix = dotted.split(".")
            value = self.lookup(root, frame, node)
            origins = tuple(
                ".".join((origin, *suffix)) for origin in value.possible_imports
            )
            value = _assessment(
                frame.scope,
                origins,
                value.unknown_possible,
                value.unbound_possible,
                value.reasons,
                (*value.trace, self.step(node, frame, "reference", root)),
            )
        else:
            value = _assessment(
                frame.scope,
                unknown=True,
                reasons=("dynamic_reference_receiver",),
                trace=(self.step(node, frame, "reference"),),
            )
        if frame.limit:
            value = self.uncertain(value, frame.limit, node, frame)
        imported = value.possible_imports[0] if value.state == "established" else None
        self.references.append(
            ReferenceFact(
                self.identity,
                node.lineno,
                kind,
                ast.get_source_segment(self.content, expression) or "",
                imported,
                None if imported else ";".join(value.reasons) or value.state,
                tuple(k.arg or "**" for k in node.keywords)
                if isinstance(node, ast.Call)
                else (),
                len(node.args) if isinstance(node, ast.Call) else 0,
                value,
            )
        )

    def dynamic_call(self, node, frame):
        dotted = _dotted_name(node.func)
        if not dotted:
            return False
        names = {"exec", "eval", "setattr", "delattr", "globals", "locals", "vars"}
        if dotted.split(".")[-1] in names:
            return True
        value = self.lookup(dotted.split(".")[0], frame, node)
        return any(
            origin.split(".")[-1] in names for origin in value.possible_imports
        ) or any(step.input_name in names for step in value.trace)

    def expression(self, node, frame):
        if node is None:
            return
        if isinstance(node, ast.Call):
            self.expression(node.func, frame)
            # The callee is evaluated before argument expressions can rebind it.
            self.reference(node, node.func, "call", frame)
            for argument in (*node.args, *[k.value for k in node.keywords]):
                self.expression(argument, frame)
            if self.dynamic_call(node, frame):
                self.namespace_limit(node, frame, "dynamic_namespace_operation")
            return
        if isinstance(node, ast.NamedExpr):
            self.expression(node.value, frame)
            self.invalidate(
                {node.target.id}, node, frame, "assignment_expression_unmodeled"
            )
            return
        if isinstance(
            node,
            (ast.Lambda, ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp),
        ):
            # Preserve syntactic calls without importing a second, incomplete
            # implicit-scope interpreter. Writes from walrus expressions escape.
            limited = frame.fork()
            limited.scope = f"expression@{node.lineno}:{node.col_offset}"
            limited.limit = "lambda_or_comprehension_scope_unmodeled"
            for child in ast.walk(node):
                if isinstance(child, ast.Call):
                    self.reference(child, child.func, "call", limited)
                    if self.dynamic_call(child, limited):
                        self.namespace_limit(
                            node, frame, "dynamic_namespace_in_implicit_scope"
                        )
                elif isinstance(child, (ast.Attribute, ast.Subscript)) and isinstance(
                    child.ctx, (ast.Store, ast.Del)
                ):
                    self.mutation(child, node, frame)
            writes = {
                child.target.id
                for child in ast.walk(node)
                if isinstance(child, ast.NamedExpr)
            }
            self.invalidate(writes, node, frame, "assignment_expression_unmodeled")
            return
        if isinstance(node, (ast.BoolOp, ast.IfExp)):
            writes = {
                child.target.id
                for child in ast.walk(node)
                if isinstance(child, ast.NamedExpr)
            }
            self.invalidate(
                writes, node, frame, "conditional_expression_write_unmodeled"
            )
        for child in ast.iter_child_nodes(node):
            self.expression(child, frame)

    def import_statement(self, node, frame):
        for alias in node.names:
            direct = isinstance(node, ast.Import)
            module = alias.name if direct else node.module or ""
            if alias.name == "*":
                self.namespace_limit(node, frame, "star_import_namespace_unknown")
                continue
            name = alias.asname or (alias.name.split(".")[0] if direct else alias.name)
            origin = (
                alias.name
                if direct and alias.asname
                else name
                if direct
                else f"{module}.{alias.name}"
                if module
                else alias.name
            )
            relative = not direct and node.level
            value = _assessment(
                frame.scope,
                () if relative else (origin,),
                bool(relative),
                reasons=("relative_import_origin_unresolved",) if relative else (),
                trace=(self.step(node, frame, "import", name, origin),),
            )
            self.assign(name, value, node, frame, "import_binding")

    def annotation(self, node, frame):
        if node is None:
            return
        limited = frame.fork()
        limited.scope = f"{frame.scope}/annotation@{node.lineno}"
        limited.limit = "annotation_evaluation_unmodeled"
        self.expression(node, limited)
        # Annotations may be deferred; observations survive without selecting
        # evaluation timing. Explicit possible writes cannot leave stale values.
        changed = {
            name
            for name, value in limited.values.items()
            if value != frame.values.get(name)
        }
        self.invalidate(changed, node, frame, "annotation_side_effects_unmodeled")

    def block(self, nodes, frame):
        for node in nodes:
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                self.import_statement(node, frame)
            elif isinstance(node, (ast.Assign, ast.AnnAssign)):
                if isinstance(node, ast.AnnAssign):
                    self.annotation(node.annotation, frame)
                self.expression(node.value, frame)
                targets = (
                    node.targets if isinstance(node, ast.Assign) else [node.target]
                )
                if node.value is None:
                    continue
                value = self.value(node.value, frame)
                for target in targets:
                    if isinstance(target, ast.Name):
                        self.assign(
                            target.id,
                            value,
                            node,
                            frame,
                            "alias_copy"
                            if isinstance(node.value, ast.Name)
                            else "assignment_unknown",
                            node.value.id if isinstance(node.value, ast.Name) else None,
                        )
                    elif isinstance(target, (ast.Attribute, ast.Subscript)):
                        self.expression(target.value, frame)
                        self.mutation(target, node, frame)
                    else:
                        self.invalidate(
                            self.names([target]).writes,
                            node,
                            frame,
                            "complex_assignment_target_unmodeled",
                        )
            elif isinstance(node, ast.Delete):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        previous = frame.values.get(target.id)
                        frame.values[target.id] = _assessment(
                            frame.scope,
                            unbound=True,
                            reasons=("deleted_binding",),
                            trace=(
                                *(previous.trace if previous else ()),
                                self.step(node, frame, "delete", target.id),
                            ),
                        )
                    else:
                        self.mutation(target, node, frame)
            elif isinstance(node, ast.If):
                self.expression(node.test, frame)
                left, right = frame.fork(), frame.fork()
                self.block(node.body, left)
                self.block(node.orelse, right)
                for name in set(left.values) | set(right.values):
                    a, b = self.lookup(name, left, node), self.lookup(name, right, node)
                    origins = (*a.possible_imports, *b.possible_imports)
                    unknown, unbound = (
                        a.unknown_possible or b.unknown_possible,
                        a.unbound_possible or b.unbound_possible,
                    )
                    reason = (
                        ()
                        if binding_state(tuple(sorted(set(origins))), unknown, unbound)
                        == "established"
                        else ("branch_alternatives",)
                    )
                    frame.values[name] = _assessment(
                        frame.scope,
                        origins,
                        unknown,
                        unbound,
                        (*a.reasons, *b.reasons, *reason),
                        (
                            *a.trace,
                            *b.trace,
                            self.step(node, frame, "branch_join", name),
                        ),
                    )
                frame.wildcard = left.wildcard or right.wildcard
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                arguments = (
                    *node.args.posonlyargs,
                    *node.args.args,
                    *node.args.kwonlyargs,
                    *([node.args.vararg] if node.args.vararg else []),
                    *([node.args.kwarg] if node.args.kwarg else []),
                )
                for argument in arguments:
                    self.annotation(argument.annotation, frame)
                self.annotation(node.returns, frame)
                for expression in (
                    *node.decorator_list,
                    *node.args.defaults,
                    *[d for d in node.args.kw_defaults if d],
                ):
                    self.expression(expression, frame)
                self.assign(
                    node.name,
                    _assessment(
                        frame.scope,
                        unknown=True,
                        reasons=("function_value_not_propagated",),
                    ),
                    node,
                    frame,
                    "function_definition",
                )
                self.functions.append((node, frame.fork()))
            elif isinstance(node, ast.ClassDef):
                for expression in node.decorator_list:
                    self.expression(expression, frame)
                for base in node.bases:
                    self.expression(base, frame)
                    self.reference(node, base, "class_base", frame)
                for keyword in node.keywords:
                    self.expression(keyword.value, frame)
                child = _Frame(
                    f"class:{node.name}@{node.lineno}",
                    "class",
                    {},
                    set(),
                    self.names(node.body).globals,
                    self.names(node.body).nonlocals,
                    frame.fork(),
                )
                if node.keywords:
                    child.limit = "class_namespace_unmodeled"
                self.block(node.body, child)
                self.assign(
                    node.name,
                    _assessment(
                        frame.scope,
                        unknown=True,
                        reasons=("class_value_not_propagated",),
                    ),
                    node,
                    frame,
                    "class_definition",
                )
            elif isinstance(node, ast.Expr):
                self.expression(node.value, frame)
            elif isinstance(node, ast.Return):
                self.expression(node.value, frame)
                frame.limit = "syntactically_after_return"
            elif isinstance(node, (ast.Pass, ast.Global, ast.Nonlocal)):
                continue
            else:
                names = self.names([node])
                for mutation in names.mutations:
                    self.mutation(mutation, node, frame)
                if any(self.dynamic_call(call, frame) for call in names.calls):
                    self.namespace_limit(
                        node, frame, "dynamic_namespace_in_unsupported_control_flow"
                    )
                self.invalidate(
                    names.writes, node, frame, "unsupported_write_or_control_flow"
                )
                if names.star:
                    self.namespace_limit(
                        node, frame, "unsupported_star_import_control_flow"
                    )
                limited = frame.fork()
                limited.scope = f"{frame.scope}/unsupported@{node.lineno}"
                limited.limit = "unsupported_control_flow"
                for child in ast.walk(node):
                    if isinstance(child, ast.Call):
                        self.reference(child, child.func, "call", limited)
                    if isinstance(child, (ast.Import, ast.ImportFrom)):
                        self.import_statement(child, limited)
                if isinstance(node, (ast.Return, ast.Raise, ast.Break, ast.Continue)):
                    frame.limit = "following_unsupported_termination"

    def run(self):
        self.block(self.tree.body, self.module)
        index = 0
        while index < len(self.functions):
            node, parent = self.functions[index]
            index += 1
            names = self.names(node.body)
            local = names.writes - names.globals - names.nonlocals
            arguments = (
                *node.args.posonlyargs,
                *node.args.args,
                *node.args.kwonlyargs,
                *([node.args.vararg] if node.args.vararg else []),
                *([node.args.kwarg] if node.args.kwarg else []),
            )
            local.update(a.arg for a in arguments)
            frame = _Frame(
                f"{parent.scope}/function:{node.name}@{node.lineno}",
                "function",
                {},
                local,
                names.globals,
                names.nonlocals,
                parent if parent.kind == "function" else self.module,
            )
            for argument in arguments:
                frame.values[argument.arg] = _assessment(
                    frame.scope,
                    unknown=True,
                    reasons=("parameter_value_unknown",),
                    trace=(self.step(argument, frame, "parameter", argument.arg),),
                )
            self.block(node.body, frame)
        return tuple(sorted(self.imports, key=lambda f: f.line)), tuple(
            sorted(self.references, key=lambda r: r.line)
        )


def analyze_python_bindings(identity: str, content: str, tree: ast.Module):
    """Return source facts for one bounded acquired file, without executing it."""
    return _Analyzer(identity, content, tree).run()


def python_facts_manifest(imports, references) -> dict:
    """Intern source trace steps once; indices preserve each assessment's trace.

    Native facts remain typed. This version-2 saved representation avoids copying
    the same import/assignment history into every reference and exceeding the
    existing replay input budget. Tables are local to one target/sample packet.
    """
    steps = []
    indices = {}
    records = []
    for reference in references:
        record = {
            field.name: getattr(reference, field.name)
            for field in fields(reference)
            if field.name != "binding"
        }
        binding = reference.binding
        record["binding"] = None
        if binding is not None:
            trace = []
            for step in binding.trace:
                if step not in indices:
                    indices[step] = len(steps)
                    steps.append(asdict(step))
                trace.append(indices[step])
            record["binding"] = {
                field.name: getattr(binding, field.name)
                for field in fields(binding)
                if field.name != "trace"
            }
            record["binding"]["trace"] = trace
        records.append(record)
    return {
        "binding_analysis_version": BINDING_ANALYSIS_VERSION,
        "binding_trace_steps": steps,
        "imports": [asdict(fact) for fact in imports],
        "references": records,
    }
