"""Explicit native source-fact codec with lossless per-file trace references.

Start with encode_source_facts/decode_source_facts. These operate on one admitted
file and its original text, before the later family/material projection. Native
JSON guards apply to every packet. Decoding validates retained representation;
it never parses Python, discovers paths or invokes an argument checker. Native
family registration belongs to the enclosing Workspace integration. Cross-file
analysis admission and explicit result-method support live in result_codec;
this component remains independently usable for exact per-file reconstruction.
"""
from __future__ import annotations
from .analysis import (SourceSpan, CallArguments, CallableSignature, ParameterFact,
                       SourceFacts, fact_identity, ArgumentComparison, KeywordReception, BindingViolation)
from .bindings import (BindingAssessment, BindingTraceStep, binding_state,
                       MAX_BINDING_ORIGINS, MAX_BINDING_TRACE_STEPS)
from .evidence import AnalysisLimits, MeasuredDuration, encode_fact_binding_traces, json_structure_cost
from ..workspace.native_representation import (json_bytes, parse_json, object_fields,
    NativeValueCodec, RecordLayout, RecordRef, NativeReconstructionError)

# Fixed layouts are owned here, not discovered from dataclasses or persisted names.
_FIELDS = {
    SourceSpan: ("line", "column", "end_line", "end_column"),
    BindingTraceStep: ("source_id", "scope", "line", "column", "end_line", "end_column", "operation", "name", "origin", "input_name"),
    BindingAssessment: ("state", "possible_imports", "unknown_possible", "unbound_possible", "scope", "reasons", "trace"),
    CallArguments: ("fact_id", "unit_id", "span", "expression", "positional", "keywords", "argument_spans", "complete", "binding"),
    ParameterFact: ("name", "kind", "has_default"),
    CallableSignature: ("fact_id", "unit_id", "span", "header_span", "qualified_name", "kind", "parameters", "complete", "decorators", "class_bases", "limitations"),
    SourceFacts: ("unit_id", "calls", "signatures", "problems", "ast_nodes"),
    KeywordReception: ("name", "outcome"),
    BindingViolation: ("reason", "parameter"),
    ArgumentComparison: ("call_id", "signature_id", "receiver_mode", "outcome", "checks_complete", "keyword_reception", "violations", "unresolved_checks", "remaining_premises"),
}


def _record(raw, cls):
    return object_fields(raw, _FIELDS[cls])


def _pack(value):
    if type(value) in _FIELDS:
        return {name: _pack(getattr(value, name)) for name in _FIELDS[type(value)]}
    if type(value) is tuple:
        return [_pack(item) for item in value]
    if type(value) in (str, int, bool, type(None)):
        return value
    raise ValueError("Unsupported source fact value.")


def read_bounded_text(value, *, maximum=4096):
    if type(value) is not str or len(value) > maximum:
        raise ValueError("Invalid bounded text.")
    return value

def read_source_span(raw, text=None) -> SourceSpan:
    data = object_fields(raw, ("line", "column", "end_line", "end_column"))
    span = SourceSpan(**data)
    if (any(type(v) is not int for v in data.values()) or span.line < 1 or span.column < 0
            or span.end_column < 0 or (span.end_line, span.end_column) <= (span.line, span.column)):
        raise ValueError("Invalid source span.")
    if text is not None:
        # Split only on LF, as Python AST line coordinates do; Unicode separators
        # inside a string must not turn into invented source lines.
        lines = text if type(text) is list else [line.encode("utf-8") for line in text.split("\n")]
        for line, column in ((span.line, span.column), (span.end_line, span.end_column)):
            if line > len(lines) or column > len(lines[line - 1]):
                raise ValueError("Source span outside retained bytes.")
            # The original text is already valid Unicode. A boundary cannot
            # point into a UTF-8 continuation byte; avoid repeatedly decoding
            # entire line prefixes for every saved trace step.
            encoded = lines[line - 1]
            if column < len(encoded) and encoded[column] & 0xC0 == 0x80:
                raise ValueError("Source column splits a UTF-8 character.")
    return span

def _inside(inner: SourceSpan, outer: SourceSpan):
    if not ((outer.line, outer.column) <= (inner.line, inner.column)
            and (inner.end_line, inner.end_column) <= (outer.end_line, outer.end_column)):
        raise ValueError("Foreign source span.")

def read_string_sequence(raw, *, maximum=4096):
    if type(raw) is not list or len(raw) > maximum:
        raise ValueError("Unsupported string sequence.")
    return tuple(read_bounded_text(v) for v in raw)

def _read_binding_step(raw, unit_id, text):
    step = _record(raw, BindingTraceStep)
    if step["source_id"] != unit_id:
        raise ValueError("Foreign binding trace source.")
    read_source_span({k: step[k] for k in ("line", "column", "end_line", "end_column")}, text)
    for k in ("scope", "operation", "name"):
        read_bounded_text(step[k])
    for k in ("origin", "input_name"):
        if step[k] is not None:
            read_bounded_text(step[k])
    return BindingTraceStep(**step)

def _read_binding(raw, unit_id, text, validated_steps=None):
    if raw is None:
        return None
    data = _record(raw, BindingAssessment)
    origins = read_string_sequence(data["possible_imports"], maximum=MAX_BINDING_ORIGINS)
    if origins != tuple(sorted(set(origins))) or any(not o for o in origins):
        raise ValueError("Invalid imported alternatives.")
    if type(data["unknown_possible"]) is not bool or type(data["unbound_possible"]) is not bool:
        raise ValueError("Invalid binding possibility flags.")
    if not (origins or data["unknown_possible"] or data["unbound_possible"]):
        raise ValueError("Empty binding possibilities.")
    if data["state"] != binding_state(origins, data["unknown_possible"], data["unbound_possible"]):
        raise ValueError("Inconsistent binding state.")
    if type(data["trace"]) is not list or not 1 <= len(data["trace"]) <= MAX_BINDING_TRACE_STEPS:
        raise ValueError("Unsupported trace capacity.")
    steps = []
    for raw_step in data["trace"]:
        # Native tables validate a shared step once at this exact file/unit.
        # The default embedded representation still validates every raw step.
        steps.append(validated_steps[id(raw_step)] if validated_steps is not None
                     else _read_binding_step(raw_step, unit_id, text))
    return BindingAssessment(data["state"], origins, data["unknown_possible"], data["unbound_possible"],
                             read_bounded_text(data["scope"]), read_string_sequence(data["reasons"]), tuple(steps))

def _read_fact(raw, kind, unit_id, text, complete, validated_binding_steps=None):
    cls = CallArguments if kind == "call" else CallableSignature
    data = _record(raw, cls)
    span = read_source_span(data["span"], text)
    if data["unit_id"] != unit_id or data["fact_id"] != fact_identity(kind, unit_id, span):
        raise ValueError("Source fact identity mismatch.")
    if type(data["complete"]) is not bool or data["complete"] != complete:
        raise ValueError("Source fact coverage mismatch.")
    if kind == "call":
        positional = read_string_sequence(data["positional"])
        if any(v not in {"ordinary", "starred"} for v in positional):
            raise ValueError("Unknown positional syntax.")
        keywords = data["keywords"]
        if type(keywords) is not list or len(keywords) > 4096 or any(
            k is not None and (type(k) is not str or not k.isidentifier()) for k in keywords
        ):
            raise ValueError("Invalid keyword syntax.")
        if type(data["argument_spans"]) is not list or len(data["argument_spans"]) != len(positional) + len(keywords):
            raise ValueError("Argument span closure mismatch.")
        spans = tuple(read_source_span(s, text) for s in data["argument_spans"])
        for argument in spans:
            _inside(argument, span)
        return CallArguments(data["fact_id"], unit_id, span, read_bounded_text(data["expression"], maximum=4 * 1024 * 1024),
                             positional, tuple(keywords), spans, complete,
                             _read_binding(data["binding"], unit_id, text, validated_binding_steps))
    header = read_source_span(data["header_span"], text)
    _inside(header, span)
    if data["kind"] not in {"function", "async_function", "initializer"}:
        raise ValueError("Unknown declared signature kind.")
    if type(data["parameters"]) is not list or len(data["parameters"]) > 4096:
        raise ValueError("Unsupported parameter sequence.")
    parameters, names, kinds = [], set(), []
    order = {"positional_only": 0, "positional_or_keyword": 1, "variadic_positional": 2,
             "keyword_only": 3, "variadic_keyword": 4}
    for raw_parameter in data["parameters"]:
        p = _record(raw_parameter, ParameterFact)
        if (type(p["name"]) is not str or not p["name"].isidentifier() or p["name"] in names
                or p["kind"] not in order or type(p["has_default"]) is not bool):
            raise ValueError("Invalid parameter syntax.")
        if p["kind"].startswith("variadic_") and p["has_default"]:
            raise ValueError("Variadic parameter cannot have a default.")
        names.add(p["name"])
        kinds.append(order[p["kind"]])
        parameters.append(ParameterFact(**p))
    if kinds != sorted(kinds) or kinds.count(2) > 1 or kinds.count(4) > 1:
        raise ValueError("Invalid parameter kind order.")
    return CallableSignature(data["fact_id"], unit_id, span, header, read_bounded_text(data["qualified_name"]),
                             data["kind"], tuple(parameters), complete, read_string_sequence(data["decorators"]),
                             read_string_sequence(data["class_bases"]), read_string_sequence(data["limitations"]))



def _decode_fact_binding_traces(raw, unit_id, text, limits):
    data = object_fields(raw, ("unit_id", "calls", "signatures", "problems", "ast_nodes", "binding_trace_steps"))
    table = data["binding_trace_steps"]
    if (type(table) is not list or len(table) > limits.max_facts * MAX_BINDING_TRACE_STEPS
        or type(data["calls"]) is not list or len(data["calls"]) > limits.max_facts):
        raise ValueError("Invalid binding trace table capacity.")
    validated, keys = {}, set()
    for step in table:
        decoded = _read_binding_step(step, unit_id, text)
        if decoded in keys:
            raise ValueError("Duplicate binding trace table step.")
        keys.add(decoded)
        validated[id(step)] = decoded
    used, calls = set(), []
    for call in data["calls"]:
        if type(call) is not dict:
            raise ValueError("Invalid indexed call record.")
        binding = call.get("binding")
        if binding is not None:
            if type(binding) is not dict or type(binding.get("trace")) is not list or not 1 <= len(binding["trace"]) <= MAX_BINDING_TRACE_STEPS:
                raise ValueError("Invalid indexed binding trace.")
            trace = binding["trace"]
            if any(type(i) is not int or not 0 <= i < len(table) for i in trace):
                raise ValueError("Foreign binding trace index.")
            used.update(trace)
            call = dict(call, binding=dict(binding, trace=[table[i] for i in trace]))
        calls.append(call)
    if used != set(range(len(table))):
        raise ValueError("Unused binding trace table step.")
    return {k: calls if k == "calls" else v for k, v in data.items() if k != "binding_trace_steps"}, validated

DURATION_LAYOUT = RecordLayout("measured_duration", MeasuredDuration,
    (("seconds_hex", str), ("scope", str)))
_DURATION_CODEC = NativeValueCodec((DURATION_LAYOUT,))


def encode_duration(value: MeasuredDuration) -> bytes:
    return _DURATION_CODEC.encode(value, RecordRef("measured_duration"))


def decode_duration(payload: bytes) -> MeasuredDuration:
    return _DURATION_CODEC.decode(payload, RecordRef("measured_duration"))


def _decode_source_facts(raw, unit_id, text, coverage, limits):
    if coverage not in ("complete_file", "limited"):
        raise ValueError("Source facts require analyzed coverage.")
    if type(text) is not str or len(text.encode("utf-8")) > limits.max_source_bytes:
        raise ValueError("Unsupported retained text capacity.")
    # Trace references share the same exact text. Encode its physical lines once,
    # avoiding repeated full-file work while checking every span/reference.
    physical_lines = [line.encode("utf-8") for line in text.split("\n")]
    raw, steps = _decode_fact_binding_traces(raw, unit_id, physical_lines, limits)
    data = _record(raw, SourceFacts)
    if (data["unit_id"] != unit_id or type(data["ast_nodes"]) is not int
            or not 0 <= data["ast_nodes"] <= limits.max_nodes_per_file):
        raise ValueError("Invalid source work or identity.")
    for key in ("calls", "signatures"):
        if type(data[key]) is not list:
            raise ValueError("Invalid source fact sequence.")
    if len(data["calls"]) + len(data["signatures"]) > limits.max_facts:
        raise ValueError("Source fact limit exceeded.")
    calls = tuple(_read_fact(c, "call", unit_id, physical_lines,
                  coverage == "complete_file", steps) for c in data["calls"])
    signatures = tuple(_read_fact(c, "signature", unit_id, physical_lines,
                       coverage == "complete_file", steps) for c in data["signatures"])
    ids = [f.fact_id for f in (*calls, *signatures)]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate source fact identity.")
    return SourceFacts(unit_id, calls, signatures, read_string_sequence(data["problems"]), data["ast_nodes"])


def decode_source_facts(payload: bytes, *, unit_id: str, text: str,
                        coverage: str, limits: AnalysisLimits | None = None) -> SourceFacts:
    """Read codec1 at the supplied exact source file, without rederivation."""
    raw = object_fields(parse_json(payload), ("codec_version", "facts"))
    if type(raw["codec_version"]) is not int or raw["codec_version"] != 1:
        raise NativeReconstructionError("unsupported_native_codec", "Unknown source fact codec.")
    return _decode_source_facts(raw["facts"], unit_id, text, coverage, limits or AnalysisLimits())


def encode_source_facts(facts: SourceFacts, *, text: str, coverage: str,
                        limits: AnalysisLimits | None = None) -> bytes:
    """Emit validated flat records; shared trace objects are encoded only once."""
    if type(facts) is not SourceFacts:
        raise ValueError("Expected native SourceFacts.")
    packed = encode_fact_binding_traces(_pack(facts))
    # Validate this independently admitted encoder boundary before publishing bytes.
    checked = _decode_source_facts(packed, facts.unit_id, text, coverage, limits or AnalysisLimits())
    if checked != facts:
        raise ValueError("Source fact encoding changed retained meaning.")
    return json_bytes({"codec_version": 1, "facts": packed})


def read_argument_comparison(raw, call, signature, receiver):
    """Validate saved local reception and premises without rerunning the checker."""
    data = _record(raw, ArgumentComparison)
    if (data["call_id"] != call.fact_id or data["signature_id"] != signature.fact_id
            or data["receiver_mode"] != receiver or type(data["checks_complete"]) is not bool):
        raise ValueError("Comparison identity or receiver mismatch.")
    reception = []
    if type(data["keyword_reception"]) is not list:
        raise ValueError("Invalid keyword reception.")
    for raw_item in data["keyword_reception"]:
        item = _record(raw_item, KeywordReception)
        if item["outcome"] not in {"named_parameter", "variadic_keyword", "not_received", "undetermined"}:
            raise ValueError("Unknown keyword reception.")
        reception.append(KeywordReception(**item))
    if [r.name for r in reception] != [k for k in call.keywords if k is not None]:
        raise ValueError("Foreign or omitted keyword finding.")
    violations = []
    if type(data["violations"]) is not list:
        raise ValueError("Invalid violations.")
    for raw_item in data["violations"]:
        item = _record(raw_item, BindingViolation)
        if item["reason"] not in {"unexpected_keyword", "positional_only_by_keyword", "excess_positional",
                                  "duplicate_keyword", "duplicate_argument", "missing_required_argument"}:
            raise ValueError("Unknown binding violation.")
        if item["parameter"] is not None:
            read_bounded_text(item["parameter"])
        violations.append(BindingViolation(**item))
    unresolved, premises = read_string_sequence(data["unresolved_checks"]), read_string_sequence(data["remaining_premises"])
    not_received = {r.name for r in reception if r.outcome == "not_received"}
    keyword_violations = {v.parameter for v in violations if v.reason in {"unexpected_keyword", "positional_only_by_keyword"}}
    if not_received != keyword_violations:
        raise ValueError("Keyword rejection witness/violation mismatch.")
    parameter_names = {p.name for p in signature.parameters}
    if any(v.parameter is not None and v.parameter not in parameter_names | set(call.keywords) for v in violations):
        raise ValueError("Foreign violation parameter.")
    supported_complete = (call.complete and signature.complete and not signature.limitations
                          and receiver != "unresolved" and "starred" not in call.positional
                          and None not in call.keywords)
    expected = "rejected" if violations else "bound" if data["checks_complete"] else "undetermined"
    if (data["outcome"] != expected or data["checks_complete"] != supported_complete
            or data["checks_complete"] == bool(unresolved)
            or "call_reaches_selected_declared_signature" not in premises
            or "target_installed_versions_and_runtime_not_established" not in premises
            or receiver == "one_receiver_assumed" and "one_bound_positional_receiver_assumed" not in premises
            or signature.decorators and "effective_decorator_signature_not_established" not in premises):
        raise ValueError("Inconsistent comparison outcome or missing premise.")
    return ArgumentComparison(call.fact_id, signature.fact_id, receiver, expected, data["checks_complete"],
                              tuple(reception), tuple(violations), unresolved, premises)


def pack_argument_comparison(value: ArgumentComparison) -> dict:
    """Fixed flat representation, shared by result encoding and capacity accounting."""
    if type(value) is not ArgumentComparison:
        raise ValueError("Expected native argument comparison.")
    return _pack(value)
