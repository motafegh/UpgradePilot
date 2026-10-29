"""Shared source/signature evidence support for curated and ordinary experiments.

Both API comparison runners depend on this public boundary: analysis limits,
bounded private-file IO, fixed source/fact/comparison decoding and terminal/source
projection. Parsing/correspondence/checking, provider acquisition, curated selectors
and each runner's attempt/CLI admission remain at their own owners. A historical
reader checks saved records only, never reruns the producer or imports target code.

Method closure is explicit: current producers hash this support owner; the two
envelopes separately admit their fixed historical source-key sets. Historical hash
values remain observations, not current-method equality or authenticity guarantees.
"""

from __future__ import annotations

import hashlib
import os
import re
from dataclasses import dataclass, fields
from pathlib import Path

from upgradepilot.github.identity import validate_commit_sha, validate_repository
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
from upgradepilot.workspace.native_representation import json_bytes, object_fields
from upgradepilot.workspace.source_access import read_source_catalog
from .api_call_signature import (
    AnalysisLimit, ArgumentComparison, BindingViolation, CallArguments,
    CallableSignature, KeywordReception, ParameterFact, SourceSpan, fact_identity,
)
from .api_python_bindings import (
    BindingAssessment, BindingTraceStep, MAX_BINDING_ORIGINS, MAX_BINDING_TRACE_STEPS, binding_state,
)

MAX_CATALOG_BYTES = 64 * 1024 * 1024
MAX_SELECTION_BYTES = 256 * 1024
MAX_OUTPUT_BYTES = 16 * 1024 * 1024
RECEIVER_MODES = {"as_written", "one_receiver_assumed", "unresolved"}

CURATED_HISTORICAL_SOURCES = (
    "experiments/api_call_signature.py", "experiments/api_call_signature_trial.py",
    "experiments/api_python_bindings.py", "src/upgradepilot/workspace/source_access.py",
    "src/upgradepilot/workspace/native_representation.py",
)
SIGNATURE_SUPPORT_SOURCES = tuple(
    name for name in CURATED_HISTORICAL_SOURCES if name != "experiments/api_call_signature_trial.py"
) + ("experiments/api_signature_evidence.py",)
CURATED_CURRENT_SOURCES = (*SIGNATURE_SUPPORT_SOURCES, "experiments/api_call_signature_trial.py")


def signature_code_identity(*, curated_runner=False):
    """Current executable support closure; historical values are never refreshed on open."""
    root = Path(__file__).resolve().parents[1]
    names = CURATED_CURRENT_SOURCES if curated_runner else SIGNATURE_SUPPORT_SOURCES
    return {name: content_digest((root / name).read_bytes()) for name in names}


def admit_method_source_names(saved, *, current, historical):
    """Only the envelope owner's fixed current/historical source-key sets are supported."""
    if type(saved) is not dict or set(saved) not in [set(current), *(set(s) for s in historical)]:
        raise ValueError("Unknown method source closure.")
    return set(saved)


def read_fact_location(raw):
    """A saved source/path/span location, not permission to select a runtime callee."""
    data = object_fields(raw, ("source_id", "path", "span"))
    read_bounded_text(data["source_id"], maximum=80)
    read_bounded_text(data["path"], maximum=512)
    read_source_span(data["span"])
    return data


@dataclass(frozen=True)
class AnalysisLimits:
    max_files: int = 32
    max_source_bytes: int = 4 * 1024 * 1024
    max_nodes_per_file: int = 100_000
    max_nodes: int = 250_000
    max_facts: int = 4096
    max_pairs: int = 256
    timeout_seconds: float = 60.0
    memory_bytes: int = 512 * 1024 * 1024

    def __post_init__(self):
        ceilings = (32, 4 * 1024 * 1024, 100_000, 250_000, 4096, 256, 60.0, 512 * 1024 * 1024)
        for field, ceiling in zip(fields(self), ceilings):
            value = getattr(self, field.name)
            expected = (int, float) if field.name == "timeout_seconds" else (int,)
            if type(value) not in expected or not 0 < value <= ceiling:
                raise ValueError("Invalid analysis limit: " + field.name)


def read_bounded_bytes(path: Path, maximum: int) -> bytes:
    with path.open("rb") as stream:
        data = stream.read(maximum + 1)
    if len(data) > maximum:
        raise AnalysisLimit("encoded_input_or_output_capacity")
    return data


def content_digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_new_output(path: Path, data: bytes) -> None:
    if len(data) > MAX_OUTPUT_BYTES:
        raise AnalysisLimit("serialized_output_capacity")
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "wb") as stream:
        stream.write(data)


def read_bounded_text(value, *, maximum=4096):
    if type(value) is not str or len(value) > maximum:
        raise ValueError("Invalid bounded text.")
    return value


def read_content_digest(value):
    if type(value) is not str or re.fullmatch(r"[0-9a-f]{64}", value) is None:
        raise ValueError("Invalid digest.")
    return value


def read_investigation_target(raw) -> ExactInvestigationTarget:
    data = object_fields(raw, tuple(f.name for f in fields(ExactInvestigationTarget)))
    validate_repository(data["repository"])
    validate_commit_sha(data["base_sha"])
    validate_commit_sha(data["head_sha"])
    if type(data["pull_number"]) is not int or data["pull_number"] < 1:
        raise ValueError("Invalid target pull number.")
    transition = [data[n] for n in ("normalized_package", "old_version", "proposed_version")]
    if not (all(v is None for v in transition) or all(type(v) is str and 0 < len(v) <= 256 for v in transition)):
        raise ValueError("Incomplete target transition.")
    return ExactInvestigationTarget(**data)


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


def _record(raw, cls):
    return object_fields(raw, tuple(f.name for f in fields(cls)))


def read_string_sequence(raw, *, maximum=4096):
    if type(raw) is not list or len(raw) > maximum:
        raise ValueError("Unsupported string sequence.")
    return tuple(read_bounded_text(v) for v in raw)


def _read_binding(raw, unit_id, text):
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
        step = _record(raw_step, BindingTraceStep)
        if step["source_id"] != unit_id:
            raise ValueError("Foreign binding trace source.")
        read_source_span({k: step[k] for k in ("line", "column", "end_line", "end_column")}, text)
        for k in ("scope", "operation", "name"):
            read_bounded_text(step[k])
        for k in ("origin", "input_name"):
            if step[k] is not None:
                read_bounded_text(step[k])
        steps.append(BindingTraceStep(**step))
    return BindingAssessment(data["state"], origins, data["unknown_possible"], data["unbound_possible"],
                             read_bounded_text(data["scope"]), read_string_sequence(data["reasons"]), tuple(steps))


def _read_fact(raw, kind, unit_id, text, complete):
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
                             positional, tuple(keywords), spans, complete, _read_binding(data["binding"], unit_id, text))
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


def _read_comparison(raw, call, signature, receiver):
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


def read_comparison_records(body, companion_data, *, method_sources, allow_empty_pairs=False,
                            input_digest_field="selections_sha256"):
    """Shared fixed fact/source/comparison closure for curated and ordinary readers.

    Each envelope owner admits its own format and proof class before calling this
    decoder. This function checks saved records only; it never extracts facts or
    re-evaluates comparisons. Ordinary discovery may legitimately yield no pairs.
    """
    read_bounded_text(body["runtime"])
    read_bounded_text(body["coverage"])
    if type(body["code_sha256"]) is not dict or set(body["code_sha256"]) != method_sources:
        raise ValueError("Unknown method source closure.")
    for digest in body["code_sha256"].values():
        read_content_digest(digest)
    inputs = object_fields(body["inputs"], ("catalog_sha256", "catalog_id", input_digest_field))
    for digest in inputs.values():
        read_content_digest(digest)
    if read_content_digest(body["companion_sha256"]) != content_digest(companion_data):
        raise ValueError("Retained companion digest mismatch.")
    limits = AnalysisLimits(**_record(body["limits"], AnalysisLimits))
    target = read_investigation_target(body["target"])
    catalog = read_source_catalog(companion_data, expected_target=target)
    if body["companion_id"] != catalog.identity:
        raise ValueError("Retained companion identity mismatch.")
    if type(body["files"]) is not list or not 1 <= len(body["files"]) <= limits.max_files:
        raise ValueError("Invalid saved source sequence.")
    source_files = {(f.source_id, f.path): f for f in catalog.files}
    calls, signatures, by_source, seen_units = {}, {}, {}, set()
    node_count = fact_count = 0
    for raw in body["files"]:
        item = object_fields(raw, ("descriptor", "coverage", "facts"))
        descriptor = item["descriptor"]
        if type(descriptor) is not dict:
            raise ValueError("Invalid source descriptor.")
        key = (descriptor.get("source_id"), descriptor.get("path"))
        file = source_files.get(key)
        if file is None or json_bytes(descriptor) != json_bytes(catalog.descriptor(file)) or key in seen_units:
            raise ValueError("Source descriptor/companion mismatch.")
        seen_units.add(key)
        if item["coverage"] not in {"complete_file", "limited"}:
            raise ValueError("Invalid saved source coverage.")
        by_source[key] = descriptor["file_id"]
        raw_facts = item["facts"]
        if raw_facts is None:
            if file.path.endswith(".py"):
                raise ValueError("Missing Python source fact record.")
            continue
        facts = object_fields(raw_facts, ("unit_id", "calls", "signatures", "problems", "ast_nodes"))
        if facts["unit_id"] != descriptor["file_id"] or type(facts["ast_nodes"]) is not int or not 0 <= facts["ast_nodes"] <= limits.max_nodes_per_file:
            raise ValueError("Invalid source analysis work/identity.")
        read_string_sequence(facts["problems"])
        node_count += facts["ast_nodes"]
        physical_lines = [line.encode("utf-8") for line in file.content.split("\n")]
        for field, kind, destination in (("calls", "call", calls), ("signatures", "signature", signatures)):
            if type(facts[field]) is not list:
                raise ValueError("Invalid source facts.")
            for raw_fact in facts[field]:
                fact = _read_fact(raw_fact, kind, descriptor["file_id"], physical_lines, item["coverage"] == "complete_file")
                if fact.fact_id in destination:
                    raise ValueError("Duplicate source fact.")
                destination[fact.fact_id] = fact
                fact_count += 1
    byte_count = sum(len(f.content.encode()) for f in catalog.files)
    if (seen_units != set(source_files) or node_count > limits.max_nodes or fact_count > limits.max_facts
            or byte_count > limits.max_source_bytes):
        raise ValueError("Source closure or work limit mismatch.")
    if type(body["pairs"]) is not list or not (0 if allow_empty_pairs else 1) <= len(body["pairs"]) <= limits.max_pairs:
        raise ValueError("Invalid saved pair sequence.")
    seen_pairs = set()
    for raw in body["pairs"]:
        item = object_fields(raw, ("selection", "comparison", "problem"))
        pair = object_fields(item["selection"], ("id", "caller", "callee", "receiver_mode"))
        if not read_bounded_text(pair["id"], maximum=80) or pair["id"] in seen_pairs or pair["receiver_mode"] not in RECEIVER_MODES:
            raise ValueError("Invalid saved pair identity.")
        seen_pairs.add(pair["id"])
        resolved = []
        for name, kind, destination in (("caller", "call", calls), ("callee", "signature", signatures)):
            selector = read_fact_location(pair[name])
            unit_id = by_source.get((selector["source_id"], selector["path"]))
            identifier = fact_identity(kind, unit_id, read_source_span(selector["span"])) if unit_id else None
            resolved.append(destination.get(identifier))
        if item["comparison"] is None:
            if item["problem"] != "selected_call_or_signature_unavailable" or all(resolved):
                raise ValueError("Inconsistent unavailable pair.")
        elif not all(resolved) or item["problem"] is not None:
            raise ValueError("Broken selected fact reference.")
        else:
            _read_comparison(item["comparison"], *resolved, pair["receiver_mode"])
    expected_work = {"source_files": len(catalog.files), "source_bytes": byte_count,
                     "ast_nodes": node_count, "facts": fact_count, "selected_pairs": len(body["pairs"])}
    if json_bytes(body["work"]) != json_bytes(expected_work):
        raise ValueError("Saved work accounting mismatch.")
    return body, catalog


def render_terminal_lines(lines):
    """Independent terminal boundary: raw saved source stays unchanged."""
    rendered, size = [], 0
    for line in lines:
        safe = "".join(c for c in line if c == "\t" or c.isprintable())
        if len(safe) > 4000:
            safe = safe[:4000] + " [display truncated; inspect saved source/data]"
        size += len(safe.encode("utf-8")) + 1
        if size > 256 * 1024:
            rendered.append("VIEW LIMIT: remaining display omitted; saved data unchanged.")
            break
        rendered.append(safe)
    return "\n".join(rendered)


def render_comparison(body) -> str:
    """One projection of validated saved facts; no new semantic or action verdict."""
    units = {u["descriptor"]["file_id"]: u for u in body["files"]}
    facts = {}
    for unit in units.values():
        if unit["facts"]:
            for kind in ("calls", "signatures"):
                facts.update((f["fact_id"], f) for f in unit["facts"][kind])
    lines = ["CALLER / DECLARED SIGNATURE EVIDENCE", "Proof: " + body["proof_class"],
             "Conditional source comparisons; installed versions, runtime and compatibility are not established.",
             "Source capture: " + body["coverage"], ""]
    for item in body["pairs"]:
        pair = item["selection"]
        lines.append("PAIR " + pair["id"] + " | receiver: " + pair["receiver_mode"])
        comparison = item["comparison"]
        if comparison is None:
            lines.extend(["UNAVAILABLE: " + item["problem"], ""])
            continue
        call, signature = facts[comparison["call_id"]], facts[comparison["signature_id"]]
        for label, fact in (("Caller", call), ("Declared receiver", signature)):
            descriptor = units[fact["unit_id"]]["descriptor"]
            lines.append(f"{label}: {descriptor['source_id']} {descriptor['repository']}@{descriptor['revision']} "
                         f"{descriptor['path']}:{fact['span']['line']} (unit {fact['unit_id']})")
        lines.append("Call expression: " + call["expression"])
        lines.append("Explicit keywords: " + ", ".join(k for k in call["keywords"] if k is not None))
        lines.append("Parameters: " + ", ".join(
            p["name"] + "[" + p["kind"] + (",optional" if p["has_default"] else "") + "]"
            for p in signature["parameters"]
        ))
        lines.append("Outcome under stated premises: " + comparison["outcome"])
        lines.append("Complete syntactic binding checked: " + str(comparison["checks_complete"]))
        for keyword in comparison["keyword_reception"]:
            lines.append("Keyword " + keyword["name"] + ": " + keyword["outcome"])
        for violation in comparison["violations"]:
            lines.append("Violation: " + violation["reason"] + " " + (violation["parameter"] or ""))
        lines.extend("Unresolved check: " + reason for reason in comparison["unresolved_checks"])
        lines.extend("Premise/limit: " + reason for reason in comparison["remaining_premises"])
        caller_source = units[call["unit_id"]]["descriptor"]
        receiver_source = units[signature["unit_id"]]["descriptor"]
        if (caller_source["repository"], caller_source["revision"]) != (body["target"]["repository"], body["target"]["head_sha"]):
            lines.append("Next evidence: establish which revision of " + caller_source["repository"]
                         + " the actual target uses; this captured caller is " + caller_source["revision"] + ".")
        lines.extend([
            "Next evidence: establish whether " + call["expression"] + " reaches "
            + signature["qualified_name"] + " in " + receiver_source["repository"] + "@"
            + receiver_source["revision"] + " with receiver mode " + pair["receiver_mode"] + ".",
            "",
        ])
    lines.append("SAVED SOURCES (explicit unit IDs for offline source inspection)")
    for unit in units.values():
        descriptor = unit["descriptor"]
        lines.append(descriptor["file_id"] + " " + descriptor["source_id"] + " " + descriptor["path"])
        if unit["facts"]:
            lines.extend("Source problem: " + problem for problem in unit["facts"]["problems"])
    return render_terminal_lines(lines)


def render_source(catalog, unit_id: str, start_line: int = 1, line_count: int = 40):
    """Use physical LF coordinates, as the AST does, and retain literal source bytes."""
    if type(start_line) is not int or start_line < 1 or type(line_count) is not int or not 1 <= line_count <= 100:
        raise ValueError("Invalid source line range.")
    matches = [f for f in catalog.files if catalog.descriptor(f)["file_id"] == unit_id]
    if len(matches) != 1:
        raise ValueError("Source unit unavailable in this saved companion.")
    file = matches[0]
    lines = file.content.split("\n")
    if start_line > len(lines):
        raise ValueError("Source range outside retained text.")
    selected = lines[start_line - 1:start_line - 1 + line_count]
    return render_terminal_lines(["LITERAL RETAINED SOURCE " + unit_id, file.source_id + " " + file.path,
                     *(f"{i}: {line}" for i, line in enumerate(selected, start_line)),
                     "END LITERAL RETAINED SOURCE"])

