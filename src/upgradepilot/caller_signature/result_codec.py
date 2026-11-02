"""Fixed offline analysis input/result exchange, before Workspace family integration.

Prepared catalogs carry exact text; this codec checks source/module/transition
joins but does not authenticate acquisition receipts. Results bind the entire
input, retain partial whole-file admission and normalized traces, and contain
no duplicate source text. Reconstruction validates closure without AST parsing,
discovery or argument checking. The worker is the producer, never a decoder.

Flat owner-specific fields avoid per-fact native variant wrappers. These are
typed JSON records under the existing byte/depth/structure guards, not an opaque
serialized experimental envelope. Workspace source/material publication remains
a separate integration boundary.
"""
from __future__ import annotations

from hashlib import sha256

from .analysis import METHOD_VERSION
from .bindings import BINDING_ANALYSIS_VERSION
from .correspondence import (
    ANALYSIS_PROFILE, ANALYSIS_OMISSION_REASONS, COMPARISON_STRUCTURE_BUDGET,
    CORRESPONDENCE_VERSION, FACT_STRUCTURE_BUDGET, MAX_DISCOVERY_DEPTH,
    MAX_DISCOVERY_GAPS, MAX_PATH_STEPS, PythonSourceModule,
    SourceRelationshipStep, analysis_group_key, module_name,
)
from .evidence import (
    AnalysisLimits, AnalyzedSourceUnit, MeasuredDuration, SourceAnalysisAdmission,
    SourceAnalysisInput, SourceAnalysisResult, SourceAnalysisWork,
    SourceComparisonCandidate, SourceDiscoveryGap, json_structure_cost,
)
from .native_codec import (
    decode_source_facts, encode_source_facts, pack_argument_comparison,
    read_argument_comparison, read_bounded_text, read_source_span,
    read_string_sequence,
)
from ..github.identity import validate_commit_sha, validate_repository
from ..workspace.native_boundary import ExactInvestigationTarget
from ..workspace.native_representation import json_bytes, object_fields, parse_json
from ..workspace.source_access import encode_source_catalog, read_source_catalog

INPUT_FORMAT = "caller-signature-analysis-input/1"
RESULT_FORMAT = "caller-signature-analysis-result/1"
PRODUCER_VERSION = "1"
PRODUCER_METHOD = "caller_signature.worker.produce_source_analysis"
_MODULE_FIELDS = ("source_id", "path", "module", "package", "version", "role", "dependencies")
_LIMIT_FIELDS = ("max_files", "max_source_bytes", "max_nodes_per_file", "max_nodes", "max_facts", "max_pairs", "timeout_seconds_hex", "memory_bytes")
_WORK_FIELDS = ("source_files", "source_bytes", "ast_nodes", "facts", "selected_pairs", "scanned_ast_nodes", "fact_structure_cost", "comparison_structure_cost", "states_examined", "gaps_omitted")
_PROTOCOL_OPERATIONS = ("allocation", "attribute_getter", "factory_return", "call_protocol")
_STEP_OPERATIONS = {"call", "import_origin", "reexport", "declaration", "class_declaration", "initializer", "declared_base", *_PROTOCOL_OPERATIONS}
_RECEIVER_MODES = {"as_written", "one_receiver_assumed", "unresolved"}


def _sequence(raw, maximum):
    if type(raw) is not list or len(raw) > maximum:
        raise ValueError("Unsupported analysis sequence capacity.")
    return raw


def _nonnegative(value):
    if type(value) is not int or value < 0:
        raise ValueError("Invalid analysis work count.")
    return value


def span_fields(span):
    return dict(line=span.line, column=span.column, end_line=span.end_line, end_column=span.end_column)


def module_fields(module):
    return dict(source_id=module.source_id, path=module.path, module=module.module,
                package=module.package, version=module.version, role=module.role,
                dependencies=list(module.dependencies))


def encode_analysis_limits(limits):
    return dict(max_files=limits.max_files, max_source_bytes=limits.max_source_bytes,
                max_nodes_per_file=limits.max_nodes_per_file, max_nodes=limits.max_nodes,
                max_facts=limits.max_facts, max_pairs=limits.max_pairs,
                timeout_seconds_hex=float(limits.timeout_seconds).hex(), memory_bytes=limits.memory_bytes)


def decode_analysis_limits(raw):
    data = dict(object_fields(raw, _LIMIT_FIELDS))
    timeout = MeasuredDuration(data.pop("timeout_seconds_hex"), "analysis_timeout_limit").seconds
    return AnalysisLimits(**data, timeout_seconds=timeout)


def _read_target(raw):
    data = object_fields(raw, ("repository", "pull_number", "base_sha", "head_sha", "normalized_package", "old_version", "proposed_version"))
    validate_repository(data["repository"])
    validate_commit_sha(data["base_sha"])
    validate_commit_sha(data["head_sha"])
    if type(data["pull_number"]) is not int or data["pull_number"] < 1:
        raise ValueError("Invalid analysis target PR.")
    for name in ("normalized_package", "old_version", "proposed_version"):
        if not read_bounded_text(data[name], maximum=256):
            raise ValueError("Analysis needs an exact dependency transition.")
    return ExactInvestigationTarget(**data)


def _read_modules(raw, catalog, limits):
    files = {(f.source_id, f.path): f for f in catalog.files}
    scopes = {s.source_id: s for s in catalog.scopes}
    seen, modules = set(), []
    for item in _sequence(raw, limits.max_files):
        row = object_fields(item, _MODULE_FIELDS)
        for name in _MODULE_FIELDS[:-1]:
            read_bounded_text(row[name])
        key = row["source_id"], row["path"]
        if key not in files or key in seen or not key[1].endswith(".py"):
            raise ValueError("Module/source closure mismatch.")
        seen.add(key)
        expected_module = module_name(row["path"]) or ""
        if row["module"] != expected_module or not expected_module and row["role"] != "target_repository":
            raise ValueError("Module spelling differs from source path.")
        role = row["role"]
        target, scope = catalog.target, scopes[key[0]]
        if role == "target_repository":
            if (scope.repository, scope.revision) != (target.repository, target.head_sha):
                raise ValueError("Target source revision mismatch.")
        elif role in {"old_dependency", "proposed_dependency"}:
            version = target.old_version if role == "old_dependency" else target.proposed_version
            if (row["package"], row["version"]) != (target.normalized_package, version):
                raise ValueError("Dependency source role/transition mismatch.")
        elif role != "constraint_sample":
            raise ValueError("Unsupported analysis source role.")
        if role != "target_repository" and (not row["package"] or not row["version"]):
            raise ValueError("Missing dependency source identity.")
        row["dependencies"] = read_string_sequence(row["dependencies"], maximum=256)
        modules.append(PythonSourceModule(**row))
    if not modules or seen != {key for key in files if key[1].endswith(".py")}:
        raise ValueError("Unclassified Python source.")
    return tuple(modules)


def encode_analysis_input(value: SourceAnalysisInput) -> bytes:
    """Freeze exact offline work; acquisition must have admitted its source roles."""
    if type(value) is not SourceAnalysisInput:
        raise ValueError("Expected prepared source analysis input.")
    payload = json_bytes(dict(format=INPUT_FORMAT, analysis_profile=ANALYSIS_PROFILE,
        catalog=parse_json(encode_source_catalog(value.catalog)),
        modules=[module_fields(m) for m in value.modules], limits=encode_analysis_limits(value.limits)))
    decode_analysis_input(payload)
    return payload


def decode_analysis_input(payload: bytes) -> SourceAnalysisInput:
    row = object_fields(parse_json(payload), ("format", "analysis_profile", "catalog", "modules", "limits"))
    if row["format"] != INPUT_FORMAT or row["analysis_profile"] != ANALYSIS_PROFILE:
        raise ValueError("Unsupported analysis input/profile.")
    if type(row["catalog"]) is not dict:
        raise ValueError("Missing source catalog.")
    target = _read_target(row["catalog"].get("target"))
    catalog = read_source_catalog(json_bytes(row["catalog"]), expected_target=target)
    limits = decode_analysis_limits(row["limits"])
    if not 1 <= len(catalog.files) <= limits.max_files or sum(len(f.content.encode()) for f in catalog.files) > limits.max_source_bytes:
        raise ValueError("Selected source capacity exceeded.")
    return SourceAnalysisInput(catalog, _read_modules(row["modules"], catalog, limits), limits)


def candidate_records(candidate, calls, signatures, files):
    """Qualified producer cost layout, separate from the native wire overhead.

    Keep the earned work allocator's candidate+selection cost unchanged even
    though native results remove the redundant selection record. This helper
    does not discover/select relationships or recompute local argument fit.
    """
    comparison = candidate.comparison
    call, signature = calls[comparison.call_id], signatures[comparison.signature_id]
    def location(fact):
        file = files[fact.unit_id]
        return dict(source_id=file.source_id, path=file.path, span=span_fields(fact.span))
    record = dict(id=candidate.candidate_id, root_call_id=candidate.root_call_id,
        call_id=comparison.call_id, signature_id=comparison.signature_id,
        receiver_mode=comparison.receiver_mode,
        steps=[dict(unit_id=s.unit_id, span=span_fields(s.span), operation=s.operation, expression=s.expression) for s in candidate.steps],
        premises=list(candidate.premises), callee_role=module_fields(candidate.callee_role))
    pair = dict(selection=dict(id=candidate.candidate_id, caller=location(call), callee=location(signature),
                              receiver_mode=comparison.receiver_mode),
                comparison=pack_argument_comparison(comparison), problem=None)
    return record, pair


def _work_fields(work):
    return {name: getattr(work, name) for name in _WORK_FIELDS}


def _result_fields(result, source_input):
    files = {source_input.catalog.descriptor(f)["file_id"]: f for f in source_input.catalog.files}
    return dict(format=RESULT_FORMAT, producer_method=PRODUCER_METHOD, producer_version=PRODUCER_VERSION,
        binding_version=BINDING_ANALYSIS_VERSION, checker_version=METHOD_VERSION,
        correspondence_version=CORRESPONDENCE_VERSION, analysis_profile=ANALYSIS_PROFILE,
        input_sha256=result.input_sha256, catalog_id=result.catalog_id,
        units=[dict(unit_id=u.unit_id, coverage=u.coverage,
                    facts=parse_json(encode_source_facts(u.facts, text=files[u.unit_id].content,
                        coverage=u.coverage, limits=source_input.limits))["facts"] if u.facts is not None else None)
               for u in result.units],
        candidates=[dict(candidate_id=c.candidate_id, root_call_id=c.root_call_id,
            comparison=pack_argument_comparison(c.comparison),
            steps=[dict(unit_id=s.unit_id, span=span_fields(s.span), operation=s.operation, expression=s.expression) for s in c.steps],
            premises=list(c.premises), callee_role=module_fields(c.callee_role)) for c in result.candidates],
        gaps=[dict(reason=g.reason, unit_id=g.unit_id, span=span_fields(g.span) if g.span else None, detail=g.detail) for g in result.gaps],
        admission=[dict(unit_id=a.unit_id, state=a.state, reason=a.reason, scan_nodes=a.scan_nodes) for a in result.admission],
        work=_work_fields(result.work))


def encode_analysis_result(result: SourceAnalysisResult, source_input: SourceAnalysisInput) -> bytes:
    payload = json_bytes(_result_fields(result, source_input))
    if decode_analysis_result(payload, source_input) != result:
        raise ValueError("Analysis result encoding changed retained meaning.")
    return payload


def _read_units(raw, source_input):
    catalog, limits = source_input.catalog, source_input.limits
    files = {catalog.descriptor(f)["file_id"]: f for f in catalog.files}
    units, seen = [], set()
    for item in _sequence(raw, limits.max_files):
        row = object_fields(item, ("unit_id", "coverage", "facts"))
        uid = read_bounded_text(row["unit_id"], maximum=80)
        if uid not in files or uid in seen:
            raise ValueError("Foreign or duplicate analysis unit.")
        seen.add(uid)
        file, coverage, facts = files[uid], row["coverage"], row["facts"]
        if not file.path.endswith(".py"):
            if coverage != "non_python" or facts is not None:
                raise ValueError("Non-Python unit contains analysis facts.")
        elif coverage == "unexamined":
            if facts is not None:
                raise ValueError("Unexamined unit contains analysis facts.")
        elif coverage == "complete_file" and facts is not None:
            facts = decode_source_facts(json_bytes(dict(codec_version=1, facts=facts)),
                unit_id=uid, text=file.content, coverage=coverage, limits=limits)
        else:
            raise ValueError("Missing analyzed facts or unsupported coverage.")
        units.append(AnalyzedSourceUnit(uid, coverage, facts))
    if seen != set(files):
        raise ValueError("Incomplete source analysis closure.")
    return tuple(units), files


def _read_admission(raw, units, files, source_input):
    by_uid = {u.unit_id: u for u in units}
    expected = {uid for uid, f in files.items() if f.path.endswith(".py")}
    rows, seen = [], set()
    for item in _sequence(raw, source_input.limits.max_files):
        row = object_fields(item, ("unit_id", "state", "reason", "scan_nodes"))
        uid = read_bounded_text(row["unit_id"], maximum=80)
        if uid not in expected or uid in seen:
            raise ValueError("Foreign/duplicate analysis allocation.")
        seen.add(uid)
        unit = by_uid[uid]
        nodes = _nonnegative(row["scan_nodes"])
        if nodes > source_input.limits.max_nodes_per_file:
            raise ValueError("Analysis scan limit exceeded.")
        if row["state"] == "analyzed":
            if row["reason"] != "admitted_whole_file" or unit.facts is None or unit.coverage != "complete_file" or nodes != unit.facts.ast_nodes:
                raise ValueError("Analyzed allocation/fact mismatch.")
        elif row["state"] != "unexamined" or row["reason"] not in ANALYSIS_OMISSION_REASONS or unit.coverage != "unexamined":
            raise ValueError("Unsupported unexamined allocation.")
        rows.append(SourceAnalysisAdmission(**row))
    if seen != expected:
        raise ValueError("Incomplete analysis allocation.")
    by_key = {(f.source_id, f.path): uid for uid, f in files.items()}
    by_uid = {r.unit_id: r for r in rows}
    groups = {}
    has_dependency = any(m.role != "target_repository" for m in source_input.modules)
    for m in source_input.modules:
        row = by_uid[by_key[m.source_id, m.path]]
        if row.reason == "outside_static_import_component" and (m.role != "target_repository" or not has_dependency):
            raise ValueError("Invalid static-scope omission role.")
        if m.role in {"old_dependency", "proposed_dependency"}:
            groups.setdefault(analysis_group_key(m), set()).add((row.state, row.reason))
    if any(len(states) != 1 for states in groups.values()):
        raise ValueError("Torn paired dependency analysis group.")
    return tuple(rows)


def _read_steps(raw, root, call, signature, files, units):
    steps = []
    for item in _sequence(raw, MAX_PATH_STEPS):
        row = object_fields(item, ("unit_id", "span", "operation", "expression"))
        uid = read_bounded_text(row["unit_id"], maximum=80)
        if uid not in files or units[uid].facts is None or row["operation"] not in _STEP_OPERATIONS:
            raise ValueError("Foreign or unexamined source path step.")
        text = files[uid].content
        span = read_source_span(row["span"], text)
        expression = read_bounded_text(row["expression"], maximum=4 * 1024 * 1024)
        lines = [line.encode() for line in text.split("\n")]
        selected = lines[span.line - 1:span.end_line]
        selected[-1] = selected[-1][:span.end_column]
        selected[0] = selected[0][span.column:]
        if b"\n".join(selected).decode() != expression:
            raise ValueError("Source path text/span mismatch.")
        steps.append(SourceRelationshipStep(uid, span, row["operation"], expression))
    if (not steps or steps[0].operation != "call" or (steps[0].unit_id, steps[0].span) != (root.unit_id, root.span)
        or (steps[-1].unit_id, steps[-1].span) != (signature.unit_id, signature.span)):
        raise ValueError("Source path endpoint mismatch.")
    # A locally identical call elsewhere can have the same reception outcome.
    # Its ID cannot replace this path's actual compared invocation.
    if not any(s.operation == "call" and (s.unit_id, s.span) == (call.unit_id, call.span) for s in steps):
        raise ValueError("Source path omits its compared call.")
    return tuple(steps)


def _read_candidates(raw, units, files, source_input):
    calls = {f.fact_id: f for u in units if u.facts for f in u.facts.calls}
    signatures = {f.fact_id: f for u in units if u.facts for f in u.facts.signatures}
    by_uid = {u.unit_id: u for u in units}
    modules = {(m.source_id, m.path): m for m in source_input.modules}
    candidates, seen = [], set()
    for item in _sequence(raw, source_input.limits.max_pairs):
        row = object_fields(item, ("candidate_id", "root_call_id", "comparison", "steps", "premises", "callee_role"))
        cid = read_bounded_text(row["candidate_id"], maximum=80)
        root_id = read_bounded_text(row["root_call_id"], maximum=80)
        if not cid or cid in seen or root_id not in calls:
            raise ValueError("Foreign or duplicate source candidate.")
        seen.add(cid)
        comparison = row["comparison"]
        if type(comparison) is not dict:
            raise ValueError("Missing candidate comparison.")
        call_id = read_bounded_text(comparison.get("call_id"), maximum=80)
        signature_id = read_bounded_text(comparison.get("signature_id"), maximum=80)
        receiver = read_bounded_text(comparison.get("receiver_mode"))
        if call_id not in calls or signature_id not in signatures or receiver not in _RECEIVER_MODES:
            raise ValueError("Foreign compared fact or receiver.")
        root, call, signature = calls[root_id], calls[call_id], signatures[signature_id]
        root_file, callee_file = files[root.unit_id], files[signature.unit_id]
        if modules[root_file.source_id, root_file.path].role != "target_repository":
            raise ValueError("Foreign root call role.")
        callee_role = modules[callee_file.source_id, callee_file.path]
        if json_bytes(row["callee_role"]) != json_bytes(module_fields(callee_role)):
            raise ValueError("Candidate callee source role mismatch.")
        checked = read_argument_comparison(comparison, call, signature, receiver)
        steps = _read_steps(row["steps"], root, call, signature, files, by_uid)
        premises = read_string_sequence(row["premises"], maximum=256)
        operations = [s.operation for s in steps]
        # Every protocol-specific residue triggers the full ordered witness check.
        if any(op in operations for op in _PROTOCOL_OPERATIONS):
            position = -1
            for op in _PROTOCOL_OPERATIONS:
                try:
                    position = operations.index(op, position + 1)
                except ValueError as error:
                    raise ValueError("Incomplete or unordered factory source path.") from error
            if not {"module_allocation_binding_and_constructor_success_not_established",
                    "attribute_lookup_and_getattr_activation_not_established",
                    "factory_returns_selected_declared_class_instance"}.issubset(premises):
                raise ValueError("Missing factory source premises.")
        candidates.append(SourceComparisonCandidate(cid, root_id, checked, steps, premises, callee_role))
    return tuple(candidates), calls, signatures


def _read_gaps(raw, units, files):
    gaps = []
    for item in _sequence(raw, MAX_DISCOVERY_GAPS):
        row = object_fields(item, ("reason", "unit_id", "span", "detail"))
        uid = read_bounded_text(row["unit_id"], maximum=80)
        if uid not in files:
            raise ValueError("Foreign discovery gap source.")
        span = read_source_span(row["span"], files[uid].content) if row["span"] is not None else None
        gaps.append(SourceDiscoveryGap(read_bounded_text(row["reason"]), uid, span, read_bounded_text(row["detail"])))
    return tuple(gaps)


def decode_analysis_result(payload: bytes, source_input: SourceAnalysisInput) -> SourceAnalysisResult:
    """Read fixed saved evidence at its exact prepared input; never reevaluate it."""
    row = object_fields(parse_json(payload), ("format", "producer_method", "producer_version", "binding_version", "checker_version", "correspondence_version", "analysis_profile", "input_sha256", "catalog_id", "units", "candidates", "gaps", "admission", "work"))
    support = dict(format=RESULT_FORMAT, producer_method=PRODUCER_METHOD, producer_version=PRODUCER_VERSION,
        binding_version=BINDING_ANALYSIS_VERSION, checker_version=METHOD_VERSION,
        correspondence_version=CORRESPONDENCE_VERSION, analysis_profile=ANALYSIS_PROFILE)
    if any(type(row[k]) is not type(v) or row[k] != v for k, v in support.items()):
        raise ValueError("Unsupported analysis result method/version/profile.")
    if row["input_sha256"] != sha256(encode_analysis_input(source_input)).hexdigest() or row["catalog_id"] != source_input.catalog.identity:
        raise ValueError("Analysis result has another input/catalog.")
    units, files = _read_units(row["units"], source_input)
    admission = _read_admission(row["admission"], units, files, source_input)
    candidates, calls, signatures = _read_candidates(row["candidates"], units, files, source_input)
    gaps = _read_gaps(row["gaps"], units, files)
    work = SourceAnalysisWork(**{k: _nonnegative(v) for k, v in object_fields(row["work"], _WORK_FIELDS).items()})
    source_bytes = sum(len(f.content.encode()) for f in files.values())
    nodes = sum(u.facts.ast_nodes for u in units if u.facts)
    # Fact/candidate costs preserve the qualified allocator, not native wire size.
    fact_cost = sum(json_structure_cost(u["facts"]) for u in row["units"] if u["facts"] is not None)
    comparison_cost = sum(sum(json_structure_cost(p) for p in candidate_records(c, calls, signatures, files)) + 2 for c in candidates)
    expected = dict(source_files=len(files), source_bytes=source_bytes, ast_nodes=nodes,
        facts=len(calls) + len(signatures), selected_pairs=len(candidates),
        scanned_ast_nodes=sum(a.scan_nodes for a in admission),
        fact_structure_cost=fact_cost, comparison_structure_cost=comparison_cost,
        states_examined=work.states_examined, gaps_omitted=work.gaps_omitted)
    if _work_fields(work) != expected:
        raise ValueError("Analysis result work accounting mismatch.")
    limits = source_input.limits
    if (nodes > limits.max_nodes or work.scanned_ast_nodes > limits.max_nodes or work.facts > limits.max_facts
        or fact_cost > FACT_STRUCTURE_BUDGET or comparison_cost > COMPARISON_STRUCTURE_BUDGET):
        raise ValueError("Analysis result exceeded admitted work.")
    return SourceAnalysisResult(row["input_sha256"], row["catalog_id"], units, candidates, gaps, admission, work)
