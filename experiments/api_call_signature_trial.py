"""Retained-source calibration and offline inspection of caller/signature evidence.

``compare --sources CATALOG --selections FILE --output NEW_DIRECTORY`` starts one
bounded worker. ``open --result DIRECTORY`` validates and renders saved data only;
``--source UNIT_ID --start-line N --line-count N`` inspects its retained source.
Selectors are curated evidence locations, never automatic PR discovery or target
version proof. No network, model, target execution or package installation occurs.
The output directory is immutable after an attempt; retries require another path.
Shared evidence limits/decoding/rendering now belong to api_signature_evidence.
Existing public imports remain compatibility exports; new consumers use that owner.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from dataclasses import asdict
from datetime import UTC, datetime
from pathlib import Path

from upgradepilot.workspace.native_representation import json_bytes, object_fields, parse_json
from upgradepilot.workspace.source_access import (
    RetainedSourceCatalog, encode_source_catalog, read_source_catalog,
)


from .api_call_signature import METHOD_VERSION, AnalysisLimit, compare_arguments, extract_python_source
from .api_signature_evidence import (
    AnalysisLimits, MAX_CATALOG_BYTES, MAX_SELECTION_BYTES, MAX_OUTPUT_BYTES, RECEIVER_MODES,
    CURATED_CURRENT_SOURCES, CURATED_HISTORICAL_SOURCES, admit_method_source_names,
    signature_code_identity, read_comparison_records, render_comparison, render_source,
    content_digest as _digest, render_terminal_lines as _display,
    read_bounded_bytes as _read_bytes, read_source_span as _span,
    read_investigation_target as _target, read_bounded_text as _text,
    write_new_output as _write_new, read_content_digest as _hash,
    read_fact_location as _selector,
)

FORMAT = "caller-signature-evidence/1"
SELECTION_FORMAT = "caller-signature-selections/1"
PROOF_CLASS = "retained_curated_source_comparison"


def code_identity() -> dict:
    """Current curated method includes its runner and shared evidence support."""
    return signature_code_identity(curated_runner=True)


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
    return read_comparison_records(body, companion_data, method_sources=admit_method_source_names(
        body["code_sha256"], current=CURATED_CURRENT_SOURCES, historical=(CURATED_HISTORICAL_SOURCES,),
    ))


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
    deadline = started + limits.timeout_seconds

    def remaining():
        seconds = deadline - time.monotonic()
        if seconds <= 0:
            raise subprocess.TimeoutExpired("caller/signature admission", limits.timeout_seconds)
        return seconds

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
        ], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, timeout=remaining(), check=False)
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
        view = (render_comparison(body) + "\n").encode()
        remaining()
        (directory / "_worker-sources.json").rename(directory / "sources.json")
        (directory / "_worker-result.json").rename(directory / "result.json")
        _write_new(directory / "view.txt", view)
        remaining()
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
            print(_display(json.dumps(attempt, indent=2).split("\n")))
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
