"""Retained-source calibration and offline inspection of caller/signature evidence.

``compare --sources CATALOG --selections FILE --output NEW_DIRECTORY`` starts one
bounded worker. ``open --result DIRECTORY`` validates and renders saved data only;
``--source UNIT_ID --start-line N --line-count N`` inspects its retained source.
Selectors are curated evidence locations, never automatic PR discovery or target
version proof. No network, model, target execution or package installation occurs.
The output directory is immutable after an attempt; retries require another path.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import time
from dataclasses import asdict, dataclass, fields
from datetime import UTC, datetime
from pathlib import Path

from upgradepilot.github.identity import validate_commit_sha, validate_repository
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
from upgradepilot.workspace.native_representation import json_bytes, object_fields, parse_json
from upgradepilot.workspace.source_access import (
    RetainedSourceCatalog, encode_source_catalog, read_source_catalog,
)

from .api_call_signature import (
    METHOD_VERSION, AnalysisLimit, ArgumentComparison, BindingViolation,
    CallArguments, CallableSignature, KeywordReception, ParameterFact, SourceSpan,
    compare_arguments, extract_python_source, fact_identity,
)
from .api_python_bindings import (
    BindingAssessment, BindingTraceStep, MAX_BINDING_ORIGINS, MAX_BINDING_TRACE_STEPS,
    binding_state,
)

FORMAT = "caller-signature-evidence/1"
SELECTION_FORMAT = "caller-signature-selections/1"
MAX_CATALOG_BYTES = 64 * 1024 * 1024
MAX_SELECTION_BYTES = 256 * 1024
MAX_OUTPUT_BYTES = 16 * 1024 * 1024
PROOF_CLASS = "retained_curated_source_comparison"
RECEIVER_MODES = {"as_written", "one_receiver_assumed", "unresolved"}


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
            if type(value) not in expected or not math.isfinite(value) or not 0 < value <= ceiling:
                raise ValueError("Invalid analysis limit: " + field.name)


def _read_bytes(path: Path, maximum: int) -> bytes:
    with path.open("rb") as stream:
        data = stream.read(maximum + 1)
    if len(data) > maximum:
        raise AnalysisLimit("encoded_input_or_output_capacity")
    return data


def _digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _write_new(path: Path, data: bytes) -> None:
    if len(data) > MAX_OUTPUT_BYTES:
        raise AnalysisLimit("serialized_output_capacity")
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "wb") as stream:
        stream.write(data)


def _text(value, *, maximum=4096):
    if type(value) is not str or len(value) > maximum:
        raise ValueError("Invalid bounded text.")
    return value


def _hash(value):
    if type(value) is not str or re.fullmatch(r"[0-9a-f]{64}", value) is None:
        raise ValueError("Invalid digest.")
    return value


def _target(raw) -> ExactInvestigationTarget:
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


def _span(raw, text=None) -> SourceSpan:
    data = object_fields(raw, ("line", "column", "end_line", "end_column"))
    span = SourceSpan(**data)
    if (any(type(v) is not int for v in data.values()) or span.line < 1 or span.column < 0
            or span.end_column < 0 or (span.end_line, span.end_column) <= (span.line, span.column)):
        raise ValueError("Invalid source span.")
    if text is not None:
        # Split only on LF, as Python AST line coordinates do; Unicode separators
        # inside a string must not turn into invented source lines.
        lines = text.split("\n")
        for line, column in ((span.line, span.column), (span.end_line, span.end_column)):
            if line > len(lines) or column > len(lines[line - 1].encode("utf-8")):
                raise ValueError("Source span outside retained bytes.")
            lines[line - 1].encode("utf-8")[:column].decode("utf-8")
    return span


def _inside(inner: SourceSpan, outer: SourceSpan):
    if not ((outer.line, outer.column) <= (inner.line, inner.column)
            and (inner.end_line, inner.end_column) <= (outer.end_line, outer.end_column)):
        raise ValueError("Foreign source span.")


def _selector(raw):
    data = object_fields(raw, ("source_id", "path", "span"))
    _text(data["source_id"], maximum=80)
    _text(data["path"], maximum=512)
    _span(data["span"])
    return data


def code_identity() -> dict:
    """Transformation closure, not a claim that matching hashes prove semantics."""
    root = Path(__file__).resolve().parent.parent
    names = (
        "experiments/api_call_signature.py", "experiments/api_call_signature_trial.py",
        "experiments/api_python_bindings.py", "src/upgradepilot/workspace/source_access.py",
        "src/upgradepilot/workspace/native_representation.py",
    )
    return {name: _digest((root / name).read_bytes()) for name in names}


def prepare_comparison(source_data: bytes, selection_data: bytes, limits: AnalysisLimits):
    """Decode independent inputs once at their composition boundary; no acquisition.

    A file's qualified coverage is explicit host input. Selectors locate evidence;
    they may not include interpretation/expected-result fields. Public compare
    runs this function only inside the bounded worker.
    """
    selections = object_fields(parse_json(selection_data), ("format", "target", "files", "pairs"))
    if selections["format"] != SELECTION_FORMAT:
        raise ValueError("Unsupported selections format.")
    target = _target(selections["target"])
    catalog = read_source_catalog(source_data, expected_target=target)
    requested_files, pairs = selections["files"], selections["pairs"]
    if type(requested_files) is not list or not 1 <= len(requested_files) <= limits.max_files:
        raise AnalysisLimit("selected_file_limit")
    if type(pairs) is not list or not 1 <= len(pairs) <= limits.max_pairs:
        raise AnalysisLimit("selected_pair_limit")
    available = {(f.source_id, f.path): f for f in catalog.files}
    chosen = {}
    coverage = {}
    for raw in requested_files:
        item = object_fields(raw, ("source_id", "path", "content_sha256", "coverage"))
        key = (item["source_id"], item["path"])
        if key in chosen or key not in available:
            raise ValueError("Duplicate or unavailable selected source.")
        file = available[key]
        if _hash(item["content_sha256"]) != _digest(file.content.encode()):
            raise ValueError("Selected source digest mismatch.")
        if item["coverage"] not in {"complete_file", "limited"}:
            raise ValueError("Unsupported source coverage.")
        chosen[key], coverage[key] = file, item["coverage"]
    byte_count = sum(len(f.content.encode()) for f in chosen.values())
    if byte_count > limits.max_source_bytes:
        raise AnalysisLimit("selected_source_byte_limit")
    scopes = tuple(s for s in catalog.scopes if any(k[0] == s.source_id for k in chosen))
    companion = RetainedSourceCatalog(scopes, tuple(chosen.values()), target=target)
    units, facts_by_source, count, node_count = [], {}, 0, 0
    for key, file in sorted(chosen.items()):
        descriptor = companion.descriptor(file)
        extracted = None
        if file.path.endswith(".py"):
            extracted = extract_python_source(
                descriptor["file_id"], file.content,
                complete=coverage[key] == "complete_file",
                max_nodes=limits.max_nodes_per_file, max_facts=limits.max_facts,
            )
            node_count += extracted.ast_nodes
            count += len(extracted.calls) + len(extracted.signatures)
            if node_count > limits.max_nodes or count > limits.max_facts:
                raise AnalysisLimit("aggregate_analysis_limit")
            facts_by_source[key] = extracted
        units.append({"descriptor": descriptor, "coverage": coverage[key],
                      "facts": asdict(extracted) if extracted is not None else None})
    results, pair_ids = [], set()
    for raw in pairs:
        pair = object_fields(raw, ("id", "caller", "callee", "receiver_mode"))
        pair_id = _text(pair["id"], maximum=80)
        if not pair_id or pair_id in pair_ids or pair["receiver_mode"] not in RECEIVER_MODES:
            raise ValueError("Duplicate pair or unsupported receiver mode.")
        pair_ids.add(pair_id)
        caller, callee = _selector(pair["caller"]), _selector(pair["callee"])
        selected = []
        for selector, field in ((caller, "calls"), (callee, "signatures")):
            source = facts_by_source.get((selector["source_id"], selector["path"]))
            found = [f for f in getattr(source, field, ()) if f.span == _span(selector["span"])]
            selected.append(found[0] if len(found) == 1 else None)
        compared = compare_arguments(*selected, pair["receiver_mode"]) if all(selected) else None
        results.append({"selection": pair, "comparison": asdict(compared) if compared else None,
                        "problem": None if compared else "selected_call_or_signature_unavailable"})
    companion_data = encode_source_catalog(companion)
    result = {
        "format": FORMAT, "method_version": METHOD_VERSION, "proof_class": PROOF_CLASS,
        "target": asdict(target), "runtime": sys.version.split()[0],
        "code_sha256": code_identity(), "limits": asdict(limits),
        "inputs": {"catalog_sha256": _digest(source_data), "catalog_id": catalog.identity,
                   "selections_sha256": _digest(selection_data)},
        "companion_sha256": _digest(companion_data), "companion_id": companion.identity,
        "files": units, "pairs": results,
        "work": {"source_files": len(chosen), "source_bytes": byte_count,
                 "ast_nodes": node_count, "facts": count, "selected_pairs": len(pairs)},
        "coverage": "selected_files_and_curated_pairs_only; ordinary_discovery_and_target_runtime_unproved",
    }
    result_data = json_bytes(result)
    if max(len(result_data), len(companion_data)) > MAX_OUTPUT_BYTES:
        raise AnalysisLimit("serialized_output_capacity")
    return result_data, companion_data


def _record(raw, cls):
    return object_fields(raw, tuple(f.name for f in fields(cls)))


def _strings(raw, *, maximum=4096):
    if type(raw) is not list or len(raw) > maximum:
        raise ValueError("Unsupported string sequence.")
    return tuple(_text(v) for v in raw)


def _read_binding(raw, unit_id, text):
    if raw is None:
        return None
    data = _record(raw, BindingAssessment)
    origins = _strings(data["possible_imports"], maximum=MAX_BINDING_ORIGINS)
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
        _span({k: step[k] for k in ("line", "column", "end_line", "end_column")}, text)
        for k in ("scope", "operation", "name"):
            _text(step[k])
        for k in ("origin", "input_name"):
            if step[k] is not None:
                _text(step[k])
        steps.append(BindingTraceStep(**step))
    return BindingAssessment(data["state"], origins, data["unknown_possible"], data["unbound_possible"],
                             _text(data["scope"]), _strings(data["reasons"]), tuple(steps))


def _read_fact(raw, kind, unit_id, text, complete):
    cls = CallArguments if kind == "call" else CallableSignature
    data = _record(raw, cls)
    span = _span(data["span"], text)
    if data["unit_id"] != unit_id or data["fact_id"] != fact_identity(kind, unit_id, span):
        raise ValueError("Source fact identity mismatch.")
    if type(data["complete"]) is not bool or data["complete"] != complete:
        raise ValueError("Source fact coverage mismatch.")
    if kind == "call":
        positional = _strings(data["positional"])
        if any(v not in {"ordinary", "starred"} for v in positional):
            raise ValueError("Unknown positional syntax.")
        keywords = data["keywords"]
        if type(keywords) is not list or len(keywords) > 4096 or any(
            k is not None and (type(k) is not str or not k.isidentifier()) for k in keywords
        ):
            raise ValueError("Invalid keyword syntax.")
        if type(data["argument_spans"]) is not list or len(data["argument_spans"]) != len(positional) + len(keywords):
            raise ValueError("Argument span closure mismatch.")
        spans = tuple(_span(s, text) for s in data["argument_spans"])
        for argument in spans:
            _inside(argument, span)
        return CallArguments(data["fact_id"], unit_id, span, _text(data["expression"], maximum=4 * 1024 * 1024),
                             positional, tuple(keywords), spans, complete, _read_binding(data["binding"], unit_id, text))
    header = _span(data["header_span"], text)
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
    return CallableSignature(data["fact_id"], unit_id, span, header, _text(data["qualified_name"]),
                             data["kind"], tuple(parameters), complete, _strings(data["decorators"]),
                             _strings(data["class_bases"]), _strings(data["limitations"]))


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
            _text(item["parameter"])
        violations.append(BindingViolation(**item))
    unresolved, premises = _strings(data["unresolved_checks"]), _strings(data["remaining_premises"])
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


def read_comparison(result_data: bytes, companion_data: bytes):
    """Decode bounded historical data and reference closure; never run the analyzer.

    This checks representation/integrity, not authenticity or semantic entailment.
    Saved transformation hashes remain historical; changing today's implementation
    must not silently recompute yesterday's result during open.
    """
    if max(len(result_data), len(companion_data)) > MAX_OUTPUT_BYTES:
        raise AnalysisLimit("saved_output_capacity")
    body = object_fields(parse_json(result_data), (
        "format", "method_version", "proof_class", "target", "runtime", "code_sha256", "limits",
        "inputs", "companion_sha256", "companion_id", "files", "pairs", "work", "coverage",
    ))
    if body["format"] != FORMAT or type(body["method_version"]) is not int or body["method_version"] != METHOD_VERSION:
        raise ValueError("Unsupported comparison format or method version.")
    if body["proof_class"] != PROOF_CLASS:
        raise ValueError("Unsupported proof class.")
    _text(body["runtime"])
    _text(body["coverage"])
    if type(body["code_sha256"]) is not dict or set(body["code_sha256"]) != set(code_identity()):
        raise ValueError("Unknown method source closure.")
    for digest in body["code_sha256"].values():
        _hash(digest)
    inputs = object_fields(body["inputs"], ("catalog_sha256", "catalog_id", "selections_sha256"))
    for digest in inputs.values():
        _hash(digest)
    if _hash(body["companion_sha256"]) != _digest(companion_data):
        raise ValueError("Retained companion digest mismatch.")
    limits = AnalysisLimits(**_record(body["limits"], AnalysisLimits))
    target = _target(body["target"])
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
        _strings(facts["problems"])
        node_count += facts["ast_nodes"]
        for field, kind, destination in (("calls", "call", calls), ("signatures", "signature", signatures)):
            if type(facts[field]) is not list:
                raise ValueError("Invalid source facts.")
            for raw_fact in facts[field]:
                fact = _read_fact(raw_fact, kind, descriptor["file_id"], file.content, item["coverage"] == "complete_file")
                if fact.fact_id in destination:
                    raise ValueError("Duplicate source fact.")
                destination[fact.fact_id] = fact
                fact_count += 1
    byte_count = sum(len(f.content.encode()) for f in catalog.files)
    if (seen_units != set(source_files) or node_count > limits.max_nodes or fact_count > limits.max_facts
            or byte_count > limits.max_source_bytes):
        raise ValueError("Source closure or work limit mismatch.")
    if type(body["pairs"]) is not list or not 1 <= len(body["pairs"]) <= limits.max_pairs:
        raise ValueError("Invalid saved pair sequence.")
    seen_pairs = set()
    for raw in body["pairs"]:
        item = object_fields(raw, ("selection", "comparison", "problem"))
        pair = object_fields(item["selection"], ("id", "caller", "callee", "receiver_mode"))
        if not _text(pair["id"], maximum=80) or pair["id"] in seen_pairs or pair["receiver_mode"] not in RECEIVER_MODES:
            raise ValueError("Invalid saved pair identity.")
        seen_pairs.add(pair["id"])
        resolved = []
        for name, kind, destination in (("caller", "call", calls), ("callee", "signature", signatures)):
            selector = _selector(pair[name])
            unit_id = by_source.get((selector["source_id"], selector["path"]))
            identifier = fact_identity(kind, unit_id, _span(selector["span"])) if unit_id else None
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


def _display(lines):
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
        lines.extend(["Next evidence: establish the actual target version/call relationship before claiming target effect.", ""])
    lines.append("SAVED SOURCES (explicit unit IDs for offline source inspection)")
    for unit in units.values():
        descriptor = unit["descriptor"]
        lines.append(descriptor["file_id"] + " " + descriptor["source_id"] + " " + descriptor["path"])
        if unit["facts"]:
            lines.extend("Source problem: " + problem for problem in unit["facts"]["problems"])
    return _display(lines)


def open_comparison(directory: Path):
    """Open only fixed sibling files, not paths/URLs embedded in imported JSON."""
    attempt = parse_json(_read_bytes(directory / "attempt.json", MAX_SELECTION_BYTES))
    if type(attempt) is not dict or attempt.get("format") != "caller-signature-attempt/1" or attempt.get("state") != "completed":
        raise ValueError("Comparison attempt is not completed.")
    result = _read_bytes(directory / "result.json", MAX_OUTPUT_BYTES)
    companion = _read_bytes(directory / "sources.json", MAX_OUTPUT_BYTES)
    if attempt.get("result_sha256") != _digest(result) or attempt.get("companion_sha256") != _digest(companion):
        raise ValueError("Saved attempt/output digest mismatch.")
    body, catalog = read_comparison(result, companion)
    if (body["inputs"]["catalog_sha256"] != attempt.get("input_sha256", {}).get("catalog")
            or body["inputs"]["selections_sha256"] != attempt.get("input_sha256", {}).get("selections")
            or body["code_sha256"] != attempt.get("code_sha256") or body["limits"] != attempt.get("limits")):
        raise ValueError("Attempt/provenance binding mismatch.")
    return body, catalog


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
    return _display(["LITERAL RETAINED SOURCE " + unit_id, file.source_id + " " + file.path,
                     *(f"{i}: {line}" for i, line in enumerate(selected, start_line)),
                     "END LITERAL RETAINED SOURCE"])


def _worker(source_path, selection_path, directory, limits):
    # The parent enforces wall time, including imports. Set the address-space
    # ceiling before loading/parsing any retained profile; this process is local
    # analysis code only and never imports the inspected project.
    import resource

    resource.setrlimit(resource.RLIMIT_AS, (limits.memory_bytes, limits.memory_bytes))
    result, companion = prepare_comparison(
        _read_bytes(source_path, MAX_CATALOG_BYTES),
        _read_bytes(selection_path, MAX_SELECTION_BYTES), limits,
    )
    _write_new(directory / "_worker-result.json", result)
    _write_new(directory / "_worker-sources.json", companion)


def run_comparison(source_path: Path, selection_path: Path, directory: Path, *, limits=None):
    """One immutable attempt with a bounded subprocess; failures remain inspectable.

    Partial worker files never become completed result/source files. The parent
    validates their closure and frozen input/method identity before publication.
    Existing output directories are refused, so a retry cannot overwrite history.
    """
    limits = limits or AnalysisLimits()
    directory.mkdir(mode=0o700)
    started = time.monotonic()
    attempt = {"format": "caller-signature-attempt/1", "started_at": datetime.now(UTC).isoformat(),
               "state": "started", "reason": None, "elapsed_seconds": None,
               "input_sha256": {}, "code_sha256": code_identity(), "limits": asdict(limits),
               "result_sha256": None, "companion_sha256": None, "worker_returncode": None}
    _write_new(directory / "attempt-started.json", json_bytes(attempt))
    try:
        attempt["input_sha256"] = {
            "catalog": _digest(_read_bytes(source_path, MAX_CATALOG_BYTES)),
            "selections": _digest(_read_bytes(selection_path, MAX_SELECTION_BYTES)),
        }
        completed = subprocess.run([
            sys.executable, "-m", "experiments.api_call_signature_trial", "_worker",
            str(source_path.resolve()), str(selection_path.resolve()), str(directory.resolve()),
            json.dumps(asdict(limits)),
        ], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, timeout=limits.timeout_seconds, check=False)
        attempt["worker_returncode"] = completed.returncode
        if completed.returncode:
            raise ValueError("bounded_worker_failed: " + completed.stderr.decode("utf-8", errors="replace")[:2000])
        result = _read_bytes(directory / "_worker-result.json", MAX_OUTPUT_BYTES)
        companion = _read_bytes(directory / "_worker-sources.json", MAX_OUTPUT_BYTES)
        body, _ = read_comparison(result, companion)
        if (body["inputs"]["catalog_sha256"] != attempt["input_sha256"]["catalog"]
                or body["inputs"]["selections_sha256"] != attempt["input_sha256"]["selections"]
                or body["code_sha256"] != attempt["code_sha256"] or code_identity() != attempt["code_sha256"]):
            raise ValueError("Inputs or method changed across the attempt.")
        (directory / "_worker-sources.json").rename(directory / "sources.json")
        (directory / "_worker-result.json").rename(directory / "result.json")
        _write_new(directory / "view.txt", (render_comparison(body) + "\n").encode())
        attempt.update(state="completed", result_sha256=_digest(result), companion_sha256=_digest(companion))
    except subprocess.TimeoutExpired:
        attempt.update(state="timed_out", reason="bounded_worker_deadline; no completed comparison admitted")
    except KeyboardInterrupt:
        attempt.update(state="interrupted", reason="caller_interrupt; no completed comparison admitted")
    except (OSError, ValueError, TypeError, MemoryError) as exc:
        attempt.update(state="failed", reason=type(exc).__name__ + ": " + str(exc)[:2000])
    attempt["elapsed_seconds"] = time.monotonic() - started
    _write_new(directory / "attempt.json", json_bytes(attempt))
    return attempt


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    compare = commands.add_parser("compare", help="Compare qualified retained source pairs.")
    compare.add_argument("--sources", type=Path, required=True)
    compare.add_argument("--selections", type=Path, required=True)
    compare.add_argument("--output", type=Path, required=True)
    opened = commands.add_parser("open", help="Inspect saved data offline, without reanalysis.")
    opened.add_argument("--result", type=Path, required=True)
    opened.add_argument("--source")
    opened.add_argument("--start-line", type=int, default=1)
    opened.add_argument("--line-count", type=int, default=40)
    worker = commands.add_parser("_worker", help=argparse.SUPPRESS)
    worker.add_argument("source_path", type=Path)
    worker.add_argument("selection_path", type=Path)
    worker.add_argument("directory", type=Path)
    worker.add_argument("limits")
    args = parser.parse_args(argv)
    try:
        if args.command == "_worker":
            _worker(args.source_path, args.selection_path, args.directory,
                    AnalysisLimits(**json.loads(args.limits)))
        elif args.command == "compare":
            attempt = run_comparison(args.sources, args.selections, args.output)
            print(_display([json.dumps(attempt, indent=2)]))
            return 0 if attempt["state"] == "completed" else 1
        else:
            body, catalog = open_comparison(args.result)
            print(render_source(catalog, args.source, args.start_line, args.line_count)
                  if args.source else render_comparison(body))
    except (OSError, ValueError, TypeError, MemoryError, ImportError) as exc:
        print(_display([type(exc).__name__ + ": " + str(exc)[:2000]]), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
