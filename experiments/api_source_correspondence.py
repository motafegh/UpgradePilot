"""Bounded, target-rooted Python source candidates for the API experiment.

``discover_source_candidates`` consumes a qualified retained catalog and module
roles from ordinary acquisition. It adds declaration/import/initializer paths to
the existing scoped binding facts, then calls the unchanged argument checker.
It does not solve effective module exports, namespace installation, decorators,
MRO, execution or runtime dispatch. Every declaration path retains those premises.

Acquisition and intra-repository source closure belong to the ordinary driver;
this operation is offline and runs inside that driver's bounded worker. The limited
module-allocation -> attribute-getter -> returned-class -> call-protocol pattern
adds conditional source candidates only; arbitrary object/value flow stays outside.

An unresolved Try-import superclass may also supply a guarded syntax hypothesis
through the same member resolver. Its import/exception/base-binding premises stay
explicit, and known writes or dynamic namespace uncertainty block that route.
"""

from __future__ import annotations

import ast
from dataclasses import asdict, dataclass

from .api_call_signature import (
    AnalysisLimit, SourceSpan, compare_arguments, extract_python_source, fact_identity,
)

CORRESPONDENCE_VERSION = 2
MAX_PATH_STEPS = 32
MAX_DISCOVERY_DEPTH = 8
MAX_DISCOVERY_GAPS = 256


@dataclass(frozen=True)
class PythonSourceModule:
    """Acquired module role, not a claim about the installed import namespace."""

    source_id: str
    path: str
    module: str
    package: str
    version: str
    role: str
    dependencies: tuple[str, ...]


@dataclass(frozen=True)
class SourceRelationshipStep:
    unit_id: str
    span: SourceSpan
    operation: str
    expression: str


def module_name(path: str) -> str | None:
    """Same flat/src module grammar as source acquisition, without choosing a path."""
    parts = path.split("/")
    if parts[0] == "src":
        parts = parts[1:]
    if not parts or not parts[-1].endswith(".py"):
        return None
    parts[-1] = parts[-1][:-3]
    if parts[-1] == "__init__":
        parts.pop()
    return ".".join(parts) if parts and all(p.isidentifier() for p in parts) else None


def absolute_import(module: str, path: str, imported: str, level: int) -> str | None:
    """Resolve a relative spelling inside this captured repository namespace only."""
    if not level:
        return imported
    package = module.split(".") if path.endswith("/__init__.py") else module.split(".")[:-1]
    if level > len(package):
        return None
    prefix = package[:len(package) - level + 1]
    return ".".join([*prefix, *([imported] if imported else [])]) or None


def _declarations(statements):
    """Observe module/class declarations through control suites, never nested scopes.

    This is syntax enumeration, not another assignment/branch interpreter. Order,
    branch truth, dynamic writes and effective exports remain explicit premises.
    """
    for node in statements:
        yield node
        if isinstance(node, (ast.If, ast.Try, ast.TryStar, ast.With, ast.AsyncWith,
                             ast.For, ast.AsyncFor, ast.While, ast.Match)):
            for field in ("body", "orelse", "finalbody"):
                yield from _declarations(getattr(node, field, ()))
            for handler in getattr(node, "handlers", ()):
                yield from _declarations(handler.body)
            for case in getattr(node, "cases", ()):
                yield from _declarations(case.body)


def _lexical_body_nodes(body):
    """Traverse one body, keeping nested definitions/callbacks outside its scope."""
    def visit(node):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef,
                             ast.Lambda, ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            return
        yield node
        for child in ast.iter_child_nodes(node):
            yield from visit(child)
    for statement in body:
        yield from visit(statement)


def _body_calls(body):
    """Calls in the selected lexical body, not its nested callbacks."""
    return (node for node in _lexical_body_nodes(body) if isinstance(node, ast.Call))


def _factory_returns(body):
    """Observe every lexical return alternative, never nested callbacks or values."""
    return (node for node in _lexical_body_nodes(body) if isinstance(node, ast.Return))


def _class_spelling(node):
    """A source name/attribute spelling; calls/subscripts are not type evidence."""
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        parent = _class_spelling(node.value)
        return parent + "." + node.attr if parent else None
    return None


class _SourceCandidates:
    def __init__(self, catalog, modules, limits, *, max_depth, max_steps):
        self.catalog, self.limits = catalog, limits
        self.max_depth, self.max_steps = max_depth, max_steps
        self.units, self.by_module, self.pairs, self.candidates, self.gaps = {}, {}, [], [], []
        self.seen_candidates, self.work_states = set(), 0
        self.gaps_omitted = 0
        self.node_count = self.fact_count = 0
        files = {(f.source_id, f.path): f for f in catalog.files}
        for module in modules:
            file = files[(module.source_id, module.path)]
            descriptor = catalog.descriptor(file)
            unit_id = descriptor["file_id"]
            facts = extract_python_source(unit_id, file.content, complete=True,
                                          max_nodes=limits.max_nodes_per_file, max_facts=limits.max_facts)
            self.node_count += facts.ast_nodes
            self.fact_count += len(facts.calls) + len(facts.signatures)
            if self.node_count > limits.max_nodes or self.fact_count > limits.max_facts:
                raise AnalysisLimit("aggregate_analysis_limit")
            tree = ast.parse(file.content) if not facts.problems else None
            unit = dict(module=module, file=file, descriptor=descriptor, facts=facts, tree=tree)
            self.units[unit_id] = unit
            if module.module:
                self.by_module.setdefault((module.source_id, module.module), []).append(unit_id)
        self.unit_ids = {id(unit): key for key, unit in self.units.items()}
        self.base_references = {}

    def gap(self, reason, unit, span=None, detail=""):
        item = dict(reason=reason, unit_id=self.unit_ids[id(unit)],
                    span=asdict(span) if span else None, detail=detail)
        if item in self.gaps:
            return
        if len(self.gaps) < MAX_DISCOVERY_GAPS:
            self.gaps.append(item)
        else:
            self.gaps_omitted += 1

    def step(self, unit, node, operation):
        return SourceRelationshipStep(self.unit_ids[id(unit)], SourceSpan.of(node), operation,
                                      ast.get_source_segment(unit["file"].content, node) or "")

    def imported_paths(self, unit, origin, binding, path):
        """Keep alternative import witnesses separate; the full binding stays saved."""
        observed = False
        for trace in binding.trace:
            if trace.operation != "import" or not trace.origin or not (origin == trace.origin or origin.startswith(trace.origin + ".")):
                continue
            observed = True
            span = SourceSpan(trace.line, trace.column, trace.end_line, trace.end_column)
            lines = unit["file"].content.split("\n")[span.line - 1:span.end_line]
            encoded = [line.encode() for line in lines]
            encoded[-1] = encoded[-1][:span.end_column]
            encoded[0] = encoded[0][span.column:]
            yield (*path, SourceRelationshipStep(self.unit_ids[id(unit)], span, "import_origin",
                                                 b"\n".join(encoded).decode()))
        if not observed:
            # A trimmed/legacy trace does not justify inventing an import step.
            self.gap("original_import_step_unavailable", unit, detail=origin)
            yield path

    def resolve(self, unit, origin, path, premises, visited=(), *, required_module=None):
        """Follow source syntax alternatives, retaining role/version and full ancestry."""
        self.work_states += 1
        if self.work_states > 4096:
            self.gap("discovery_state_limit", unit, detail=origin)
            return
        if len(path) >= self.max_steps:
            self.gap("source_path_limit", unit, detail=origin)
            return
        module = unit["module"]
        own_namespace = any(source_id == module.source_id and
                            (origin == name or origin.startswith(name + "."))
                            for source_id, name in self.by_module)
        external_groups = {
            u["module"].source_id for u in self.units.values()
            if u["module"].package in module.dependencies
            and u["module"].package != module.package
            and u["module"].package.replace("-", "_") == origin.split(".")[0]
        }
        groups = ({module.source_id} if own_namespace else set()) | external_groups
        if own_namespace and external_groups:
            premises = (*premises, "local_and_external_namespace_candidates")
        found = False
        for source_id in sorted(groups):
            if required_module is not None and (source_id, required_module) not in self.by_module:
                # Import syntax names a module boundary. Missing captured text
                # cannot be recovered by recursively treating that module name
                # as another attribute exported by its parent package.
                self.gap("imported_source_module_unavailable_or_unsupported", unit, detail=required_module)
                continue
            matches = [(name, ids) for (sid, name), ids in self.by_module.items()
                       if sid == source_id and origin.startswith(name + ".")]
            if not matches:
                continue
            name, ids = max(matches, key=lambda item: len(item[0]))
            if len(ids) != 1:
                self.gap("ambiguous_module_layout", unit, detail=name)
                continue
            destination = self.units[ids[0]]
            role_premises = ("adapter_version_is_exploration_sample_not_target_resolution",) if destination["module"].role == "constraint_sample" else ()
            key = (ids[0], origin[len(name) + 1:])
            if key in visited:
                self.gap("source_relationship_cycle", destination, detail=origin)
                continue
            if len(visited) >= self.max_depth:
                self.gap("source_relationship_depth_limit", destination, detail=origin)
                continue
            found = True
            yield from self.member(destination, key[1].split("."), path,
                                   tuple(dict.fromkeys((*premises, *role_premises, "effective_export_binding_not_established",
                                                        "installed_namespace_and_dispatch_not_established"))),
                                   (*visited, key))
        if not found:
            self.gap("imported_source_module_unavailable_or_unsupported", unit, detail=origin)

    def member(self, unit, names, path, premises, visited):
        tree = unit["tree"]
        if tree is None:
            self.gap("source_syntax_unavailable", unit)
            return
        name, *tail = names
        found = False
        definitions = 0
        for node in _declarations(tree.body):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and node.name == name:
                found = True
                definitions += 1
                yield from self.declaration(unit, node, tail, path, premises, visited)
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                for alias in node.names:
                    bound = alias.asname or (alias.name.split(".")[0] if isinstance(node, ast.Import) else alias.name)
                    star = alias.name == "*"
                    if bound != name and not star:
                        continue
                    found = True
                    imported = node.module or "" if isinstance(node, ast.ImportFrom) else alias.name
                    level = node.level if isinstance(node, ast.ImportFrom) else 0
                    absolute = absolute_import(unit["module"].module, unit["file"].path, imported, level)
                    if not absolute:
                        self.gap("relative_import_outside_captured_namespace", unit, SourceSpan.of(node))
                        continue
                    if isinstance(node, ast.ImportFrom):
                        suffix = [name if star else alias.name, *tail]
                    else:
                        suffix = tail if alias.asname else names[len(alias.name.split(".")):]
                    origin = ".".join([absolute, *suffix])
                    next_premises = (*premises, "reexport_binding_and_branch_activation_not_established")
                    if star:
                        next_premises += ("star_export_membership_not_established",)
                    yield from self.resolve(unit, origin, (*path, self.step(unit, node, "reexport")),
                                            next_premises, visited, required_module=absolute)
            elif isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign, ast.Delete)):
                targets = getattr(node, "targets", [getattr(node, "target", None)])
                if any(isinstance(child, ast.Name) and child.id == name
                       for target in targets if target is not None for child in ast.walk(target)):
                    if (tail and isinstance(node, (ast.Assign, ast.AnnAssign))
                        and len(targets) == 1 and isinstance(targets[0], ast.Name)
                        and isinstance(node.value, ast.Call)):
                        found = True
                        yield from self.allocated_callable(unit, node, tail, path, premises, visited)
                    else:
                        self.gap("export_write_or_deletion_not_resolved", unit, SourceSpan.of(node), name)
        if definitions > 1:
            self.gap("multiple_declared_definitions_retained", unit, detail=name)
        if not found:
            self.gap("named_declaration_or_reexport_not_found", unit, detail=".".join(names))

    def class_protocol(self, unit, expression, method, path, premises, visited):
        """Reuse the same name/re-export resolver, without propagating object types."""
        spelling = _class_spelling(expression)
        if not spelling or not unit["module"].module:
            self.gap("factory_class_expression_unsupported", unit, SourceSpan.of(expression))
            return
        origin = unit["module"].module + "." + spelling + "." + method
        yield from self.resolve(unit, origin, path, premises, visited)

    def allocated_callable(self, unit, allocation, tail, path, premises, visited):
        """Inspect one syntax-backed allocation/getter/return/call chain.

        Constructor arguments, getter branch activation, attribute lookup and the
        returned instance are premises, not values computed here. Each declaration
        and return keeps its own source path; unsupported returns remain gaps even
        when another branch supplies a candidate. The outer call's arguments are
        compared with __call__, never with the allocator/getter constructors.
        """
        if len(tail) != 1 or tail[0] in {"__getattr__", "__call__", "__init__"}:
            self.gap("factory_attribute_chain_unsupported", unit, SourceSpan.of(allocation), ".".join(tail))
            return
        conditions = (*premises, "module_allocation_binding_and_constructor_success_not_established",
                      "attribute_lookup_and_getattr_activation_not_established",
                      "factory_constructor_arguments_not_checked", "getter_call_arguments_and_binding_not_checked")
        path = (*path, self.step(unit, allocation, "allocation"))
        getters = self.class_protocol(unit, allocation.value.func, "__getattr__", path, conditions, visited)
        found = False
        for getter_unit, getter, _, steps, conditions, _ in getters:
            found = True
            if isinstance(getter, ast.AsyncFunctionDef) or any(
                isinstance(n, (ast.Yield, ast.YieldFrom, ast.Await)) for n in _lexical_body_nodes(getter.body)
            ):
                self.gap("async_or_generator_getter_unsupported", getter_unit, SourceSpan.of(getter))
                continue
            returns = tuple(_factory_returns(getter.body))
            if not returns:
                self.gap("factory_getter_has_no_supported_return", getter_unit, SourceSpan.of(getter))
            for returned in returns:
                if not isinstance(returned.value, ast.Call):
                    self.gap("factory_return_expression_unsupported", getter_unit, SourceSpan.of(returned))
                    continue
                return_path = (*steps, self.step(getter_unit, returned, "factory_return"))
                return_conditions = (*conditions, "execution_reaches_factory_return_and_branch",
                                     "factory_returns_selected_declared_class_instance")
                emitted = False
                for candidate in self.class_protocol(getter_unit, returned.value.func, "__call__",
                                                      return_path, return_conditions, visited):
                    emitted = True
                    yield (*candidate[:-1], "one_receiver_assumed")
                if not emitted:
                    self.gap("factory_returned_call_protocol_unavailable", getter_unit, SourceSpan.of(returned))
        if not found:
            self.gap("allocated_class_getter_unavailable", unit, SourceSpan.of(allocation))

    def declaration(self, unit, node, tail, path, premises, visited):
        step = self.step(unit, node, "class_declaration" if isinstance(node, ast.ClassDef) else "declaration")
        path = (*path, step)
        if len(path) > self.max_steps:
            self.gap("source_path_limit", unit, SourceSpan.of(node))
            return
        if isinstance(node, ast.ClassDef):
            if tail in (["__getattr__"], ["__call__"]):
                method_name = tail[0]
                methods = [n for n in _declarations(node.body)
                           if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == method_name]
                if not methods:
                    self.gap("inherited_or_missing_protocol_method", unit, SourceSpan.of(node), method_name)
                for method in methods:
                    # Protocol operations describe an allocation-backed factory
                    # witness. An explicit Class.__call__/__getattr__ source call
                    # is an ordinary method declaration, with no factory claim.
                    operation = "declaration"
                    if any(step.operation == "allocation" for step in path):
                        operation = "attribute_getter" if method_name == "__getattr__" else "call_protocol"
                    yield unit, method, node, (*path, self.step(unit, method, operation)), (
                        *premises, "effective_protocol_method_and_receiver_binding_not_established",
                    ), "as_written"
                return
            if tail and tail != ["__init__"]:
                self.gap("class_member_or_protocol_unsupported", unit, SourceSpan.of(node), ".".join(tail))
                return
            initializers = [n for n in _declarations(node.body)
                            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == "__init__"]
            if not initializers:
                self.gap("inherited_initializer_or_allocation_unsupported", unit, SourceSpan.of(node))
            for initializer in initializers:
                yield unit, initializer, node, (*path, self.step(unit, initializer, "initializer")), (
                    *premises, "class_allocation_metaclass_and_mro_not_established",
                ), "as_written" if tail else "one_receiver_assumed"
        elif not tail:
            yield unit, node, None, path, premises, "as_written"
        else:
            self.gap("returned_value_or_callable_attribute_unsupported", unit, SourceSpan.of(node))

    def try_import_base_hypothesis(self, unit, base, reference, owner_class):
        """Admit a syntax hypothesis, never repair the binder's unknown Try state.

        The existing member resolver can retain conditional import alternatives.
        Use it only for the narrowly identified unsupported import control; known
        root writes/deletion/dynamic uncertainty must not resurrect stale imports.
        """
        spelling = _class_spelling(base)
        binding = reference.binding
        allowed = {"name_not_bound_in_examined_scope", "unsupported_write_or_control_flow", "branch_alternatives"}
        if (not spelling or not binding.unknown_possible
            or "unsupported_write_or_control_flow" not in binding.reasons
            or not set(binding.reasons) <= allowed):
            return False
        root = spelling.split(".")[0]
        unsupported_lines = {step.line for step in binding.trace if step.operation == "unsupported_write_or_control_flow"}
        found = False
        for node in _declarations(unit["tree"].body):
            if node.lineno >= owner_class.lineno:
                continue
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and node.name == root:
                return False
            for child in ast.walk(node):
                if isinstance(child, ast.Name) and child.id == root and isinstance(child.ctx, (ast.Store, ast.Del)):
                    return False
                if isinstance(child, ast.ExceptHandler) and child.name == root:
                    return False
                if isinstance(child, (ast.Assign, ast.AnnAssign, ast.AugAssign, ast.Delete)):
                    targets = getattr(child, "targets", [getattr(child, "target", None)])
                    if any(isinstance(n, ast.Name) and n.id == root for target in targets if target is not None for n in ast.walk(target)):
                        return False
            if isinstance(node, ast.Try) and node.lineno in unsupported_lines:
                for child in ast.walk(node):
                    if isinstance(child, (ast.Import, ast.ImportFrom)):
                        if any((alias.asname or (alias.name.split(".")[0] if isinstance(child, ast.Import) else alias.name)) == root
                               for alias in child.names):
                            found = True
        return found

    def follow(self, unit, call, root_id, path=(), premises=(), ancestry=(), owner_class=None):
        if len(ancestry) >= self.max_depth:
            self.gap("call_body_depth_limit", unit, call.span)
            return
        if len(path) >= self.max_steps:
            self.gap("source_path_limit", unit, call.span)
            return
        call_node = next((n for n in ast.walk(unit["tree"]) if isinstance(n, ast.Call)
                          and SourceSpan.of(n) == call.span), None) if unit["tree"] else None
        if call_node is None:
            return
        path = (*path, self.step(unit, call_node, "call"))
        binding = call.binding
        candidates = []
        if binding:
            residual = tuple(dict.fromkeys((*premises, *binding.reasons,
                                            *(() if binding.state == "established" else ("conditional_import_origin",)))))
            for origin in binding.possible_imports:
                for imported_path in self.imported_paths(unit, origin, binding, path):
                    candidates.extend(self.resolve(unit, origin, imported_path, residual))
            # The binder records declaration writes but intentionally does not
            # propagate local callable values. Such source locations can justify
            # a conditional candidate without fabricating an imported origin.
            if not binding.possible_imports and isinstance(call_node.func, ast.Name):
                for step in binding.trace:
                    if step.operation not in {"function_definition", "class_definition"}:
                        continue
                    for node in _declarations(unit["tree"].body):
                        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and node.lineno == step.line:
                            candidates.extend(self.declaration(unit, node, [], path,
                                (*residual, "effective_local_callable_binding_not_established"), ()))
        func = call_node.func
        if (owner_class is not None and isinstance(func, ast.Attribute) and func.attr == "__init__"
            and isinstance(func.value, ast.Call) and isinstance(func.value.func, ast.Name)
            and func.value.func.id == "super" and not func.value.args and not func.value.keywords):
            # This is a source-level base-initialization candidate. The builtin
            # super binding and effective MRO are premises, never inferred facts.
            for base in owner_class.bases:
                expression = ast.get_source_segment(unit["file"].content, base)
                from .api_python_bindings import analyze_python_bindings
                unit_id = self.unit_ids[id(unit)]
                if unit_id not in self.base_references:
                    self.base_references[unit_id] = analyze_python_bindings(unit_id, unit["file"].content, unit["tree"])[1]
                references = self.base_references[unit_id]
                for ref in references:
                    if ref.kind == "class_base" and ref.line == owner_class.lineno and ref.expression == expression and ref.binding:
                        for origin in ref.binding.possible_imports:
                            for resolved in self.resolve(unit, origin + ".__init__",
                                (*path, self.step(unit, base, "declared_base")),
                                (*premises, *ref.binding.reasons, "builtin_super_and_effective_mro_assumed")):
                                candidates.append((*resolved[:-1], "one_receiver_assumed"))
                        if self.try_import_base_hypothesis(unit, base, ref, owner_class):
                            conditions = (*premises, *ref.binding.reasons,
                                "builtin_super_and_effective_mro_assumed",
                                "unresolved_try_import_base_source_hypothesis",
                                "exception_matching_import_success_and_base_binding_not_established")
                            for resolved in self.class_protocol(unit, base, "__init__",
                                (*path, self.step(unit, base, "declared_base")), conditions, ()):
                                candidates.append((*resolved[:-1], "one_receiver_assumed"))
        if not candidates:
            self.gap("callable_relationship_unresolved", unit, call.span, call.expression)
        for destination, definition, class_node, steps, conditions, receiver in candidates:
            if len(steps) > self.max_steps:
                self.gap("source_path_limit", destination, SourceSpan.of(definition))
                continue
            signature = next((s for s in destination["facts"].signatures if s.span == SourceSpan.of(definition)), None)
            if signature is None:
                continue
            identity = (root_id, call.fact_id, signature.fact_id, receiver, steps, conditions)
            if identity in self.seen_candidates:
                continue
            if len(self.candidates) >= self.limits.max_pairs:
                self.gap("comparison_candidate_limit", unit, call.span)
                return
            self.seen_candidates.add(identity)
            identifier = fact_identity("candidate:" + str(len(self.candidates)), root_id, signature.span)
            comparison = compare_arguments(call, signature, receiver)
            self.candidates.append(dict(id=identifier, root_call_id=root_id, call_id=call.fact_id,
                signature_id=signature.fact_id, receiver_mode=receiver,
                steps=[asdict(s) for s in steps], premises=list(dict.fromkeys(conditions)),
                callee_role=asdict(destination["module"])))
            def selector(fact):
                source = self.units[fact.unit_id]["file"]
                return dict(source_id=source.source_id, path=source.path, span=asdict(fact.span))
            self.pairs.append(dict(selection=dict(id=identifier, caller=selector(call), callee=selector(signature),
                                                  receiver_mode=receiver), comparison=asdict(comparison), problem=None))
            edge = (call.fact_id, signature.fact_id, receiver)
            if edge in ancestry:
                self.gap("call_body_cycle", destination, signature.span)
                continue
            allowed = {SourceSpan.of(n) for n in _body_calls(definition.body)}
            for child in destination["facts"].calls:
                if child.span in allowed:
                    self.follow(destination, child, root_id, steps,
                        (*conditions, "execution_reaches_selected_body_and_branch"), (*ancestry, edge), class_node)

    def run(self):
        for unit_id, unit in self.units.items():
            if unit["module"].role == "target":
                for call in unit["facts"].calls:
                    self.follow(unit, call, call.fact_id)
        return dict(candidates=self.candidates, gaps=self.gaps,
                    gaps_omitted=self.gaps_omitted, states_examined=self.work_states,
                    max_depth=self.max_depth, max_path_steps=self.max_steps,
                    coverage="target-rooted supported source candidates only; alternatives and runtime remain unresolved"), self.pairs


def discover_source_candidates(catalog, modules, limits, *, max_depth=MAX_DISCOVERY_DEPTH,
                               max_path_steps=MAX_PATH_STEPS):
    """Return discovered candidates, comparisons and analyzed source units.

    The host-derived module roles are not curated callable selectors. Distinct
    captured source/version roles remain separate even when their text agrees.
    Limits produce explicit omissions or a failed analysis, never safe/no-impact.
    """
    if (type(max_depth) is not int or not 1 <= max_depth <= MAX_DISCOVERY_DEPTH
        or type(max_path_steps) is not int or not 1 <= max_path_steps <= MAX_PATH_STEPS):
        raise ValueError("Unsupported correspondence limits.")
    if not modules or len(modules) > limits.max_files or len({(m.source_id, m.path) for m in modules}) != len(modules):
        raise AnalysisLimit("source_module_limit_or_duplicate")
    if sum(len(f.content.encode()) for f in catalog.files) > limits.max_source_bytes:
        raise AnalysisLimit("selected_source_byte_limit")
    operation = _SourceCandidates(catalog, modules, limits, max_depth=max_depth, max_steps=max_path_steps)
    discovery, pairs = operation.run()
    units = [dict(descriptor=u["descriptor"], coverage="complete_file", facts=asdict(u["facts"]))
             for u in operation.units.values()]
    return discovery, pairs, units
