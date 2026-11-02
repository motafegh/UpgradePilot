"""Bounded offline source analysis through the installed product entry point.

``run_source_analysis`` freezes typed input, launches this module in a child,
then admits only a complete fixed result tied to that input. The child applies
the qualified address-space limit before decoding source, and never executes
target code or acquires evidence. Existing producer work limits stay unchanged.

The parent owns the monotonic deadline and kills/reaps the child on timeout or
interruption. Parent encode/decode work is checked against the same elapsed
allowance on return; it is not an OS-enforced parent CPU/memory sandbox.
The child's result file is bounded and has no duplicated source companion.
Temporary private files are discarded; durable source-first publication belongs
to Workspace/application integration, not this worker.
"""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
from hashlib import sha256

from .correspondence import ANALYSIS_PROFILE, SourceRelationshipStep, discover_source_candidates
from .evidence import (
    AnalyzedSourceUnit, MeasuredDuration, SourceAnalysisAdmission, SourceAnalysisInput,
    SourceAnalysisResult, SourceAnalysisRun, SourceAnalysisWork,
    SourceComparisonCandidate, SourceDiscoveryGap, encode_fact_binding_traces,
)
from .native_codec import decode_source_facts, read_argument_comparison, read_source_span
from .result_codec import (
    decode_analysis_input, decode_analysis_result, encode_analysis_input,
    encode_analysis_result,
)
from ..workspace.native_representation import (
    MAX_NATIVE_JSON_BYTES, json_bytes, object_fields, parse_json,
)


def produce_source_analysis(source_input: SourceAnalysisInput) -> SourceAnalysisResult:
    """Qualified producer composition; callers normally use the bounded parent.

    This direct producer does not enforce a process deadline/address-space quota.
    It is exposed for the owned worker and focused producer qualification only.
    """
    input_data = encode_analysis_input(source_input)
    catalog, modules, limits = source_input.catalog, source_input.modules, source_input.limits
    discovery, pairs, analyzed = discover_source_candidates(catalog, modules, limits, analysis_profile=ANALYSIS_PROFILE)
    allocation = discovery.pop("analysis_admission")
    files = {catalog.descriptor(f)["file_id"]: f for f in catalog.files}
    units = []
    for item in analyzed:
        uid = item["descriptor"]["file_id"]
        facts = decode_source_facts(json_bytes(dict(codec_version=1, facts=encode_fact_binding_traces(item["facts"]))),
            unit_id=uid, text=files[uid].content, coverage=item["coverage"], limits=limits)
        units.append(AnalyzedSourceUnit(uid, item["coverage"], facts))
    seen = {u.unit_id for u in units}
    units.extend(AnalyzedSourceUnit(uid, "unexamined" if f.path.endswith(".py") else "non_python", None)
                 for uid, f in files.items() if uid not in seen)
    calls = {f.fact_id: f for u in units if u.facts for f in u.facts.calls}
    signatures = {f.fact_id: f for u in units if u.facts for f in u.facts.signatures}
    module_map = {(m.source_id, m.path): m for m in modules}
    candidates = []
    for candidate, pair in zip(discovery["candidates"], pairs):
        comparison = read_argument_comparison(parse_json(json_bytes(pair["comparison"])), calls[candidate["call_id"]],
            signatures[candidate["signature_id"]], candidate["receiver_mode"])
        role = candidate["callee_role"]
        candidates.append(SourceComparisonCandidate(candidate["id"], candidate["root_call_id"], comparison,
            tuple(SourceRelationshipStep(s["unit_id"], read_source_span(s["span"]), s["operation"], s["expression"]) for s in candidate["steps"]),
            tuple(candidate["premises"]), module_map[role["source_id"], role["path"]]))
    work = SourceAnalysisWork(len(catalog.files), sum(len(f.content.encode()) for f in catalog.files),
        sum(u.facts.ast_nodes for u in units if u.facts), len(calls) + len(signatures), len(candidates),
        allocation["scanned_ast_nodes"], allocation["fact_structure_cost"], allocation["comparison_structure_cost"],
        discovery["states_examined"], discovery["gaps_omitted"])
    return SourceAnalysisResult(sha256(input_data).hexdigest(), catalog.identity, tuple(units), tuple(candidates),
        tuple(SourceDiscoveryGap(g["reason"], g["unit_id"], read_source_span(g["span"]) if g["span"] else None, g["detail"]) for g in discovery["gaps"]),
        tuple(SourceAnalysisAdmission(**a) for a in allocation["units"]), work)


def _read_bounded(path: Path) -> bytes:
    with path.open("rb") as stream:
        payload = stream.read(MAX_NATIVE_JSON_BYTES + 1)
    if len(payload) > MAX_NATIVE_JSON_BYTES:
        raise ValueError("Worker exchange capacity exceeded.")
    return payload


def _write_private(path: Path, payload: bytes) -> None:
    with os.fdopen(os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), "wb") as stream:
        stream.write(payload)


def run_source_analysis(source_input: SourceAnalysisInput) -> SourceAnalysisRun:
    """Execute once, without retries/cap enlargement or durable-publication claims."""
    start = time.monotonic()
    # Malformed/oversized prepared inputs are caller admission errors before launch.
    # They are not a completed producer run or a result showing no exposure.
    input_data = encode_analysis_input(source_input)
    digest = sha256(input_data).hexdigest()
    limit = source_input.limits.timeout_seconds
    state, reason, result, returncode, origin, detail = "failed", None, None, None, None, None
    try:
        with tempfile.TemporaryDirectory(prefix="upgradepilot-source-analysis-") as directory:
            root = Path(directory)
            _write_private(root / "input.json", input_data)
            remaining = limit - (time.monotonic() - start)
            if remaining <= 0:
                raise subprocess.TimeoutExpired("source analysis preparation", limit)
            process = subprocess.run([sys.executable, "-m", "upgradepilot.caller_signature.worker",
                str(root / "input.json"), str(root / "output.json"), str(source_input.limits.memory_bytes)],
                stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                timeout=remaining, check=False)
            returncode = process.returncode
            if returncode != 0:
                reason = "bounded_worker_exit"
            else:
                packet = object_fields(parse_json(_read_bounded(root / "output.json")), ("state", "reason", "problem_detail", "worker_module_origin", "result"))
                if type(packet["worker_module_origin"]) is not str or not packet["worker_module_origin"]:
                    raise ValueError("Missing worker import origin.")
                origin = packet["worker_module_origin"]
                detail = packet["problem_detail"]
                if detail is not None and (type(detail) is not str or len(detail) > 2000):
                    raise ValueError("Invalid worker problem detail.")
                if packet["state"] == "failed" and packet["reason"] in {"analysis_limit", "memory_limit", "invalid_analysis", "worker_io_failure"} and packet["result"] is None:
                    reason = packet["reason"]
                elif packet["state"] == "completed" and packet["reason"] is None and detail is None:
                    result = decode_analysis_result(json_bytes(packet["result"]), source_input)
                    state = "completed"
                else:
                    raise ValueError("Unsupported worker outcome.")
            if time.monotonic() - start >= limit:
                raise subprocess.TimeoutExpired("source analysis admission", limit)
    except subprocess.TimeoutExpired:
        state, reason, result = "timed_out", "bounded_worker_deadline", None
    except KeyboardInterrupt:
        state, reason, result = "interrupted", "caller_interrupt", None
    except (OSError, ValueError, TypeError, MemoryError) as error:
        state, reason, result = "failed", "invalid_worker_exchange", None
        detail = type(error).__name__ + ": " + str(error)[:1900]
    return SourceAnalysisRun(state, reason, digest,
        MeasuredDuration.from_seconds(time.monotonic() - start, "analysis_parent_including_input_encoding_and_result_admission"),
        returncode, origin, result, detail)


def main(argv=None) -> int:
    """Private subprocess entry, not an acquisition or public report CLI."""
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 3:
        return 2
    input_path, output_path, memory = argv
    from .evidence import AnalysisLimits
    from .analysis import AnalysisLimit
    import resource
    memory = int(memory)
    AnalysisLimits(memory_bytes=memory)
    resource.setrlimit(resource.RLIMIT_AS, (memory, memory))
    resource.setrlimit(resource.RLIMIT_FSIZE, (MAX_NATIVE_JSON_BYTES, MAX_NATIVE_JSON_BYTES))
    packet = dict(state="failed", reason=None, problem_detail=None, worker_module_origin=str(Path(__file__).resolve()), result=None)
    try:
        source_input = decode_analysis_input(_read_bounded(Path(input_path)))
        if source_input.limits.memory_bytes != memory:
            raise ValueError("Worker memory policy/input mismatch.")
        result = produce_source_analysis(source_input)
        packet.update(state="completed", result=parse_json(encode_analysis_result(result, source_input)))
    except AnalysisLimit as error:
        packet.update(reason="analysis_limit", problem_detail=str(error)[:2000])
    except MemoryError:
        packet["reason"] = "memory_limit"
    except (ValueError, TypeError) as error:
        packet.update(reason="invalid_analysis", problem_detail=type(error).__name__ + ": " + str(error)[:1900])
    except OSError as error:
        packet.update(reason="worker_io_failure", problem_detail=type(error).__name__ + ": " + str(error)[:1900])
    # If even the bounded failure exchange cannot be written, parent sees nonzero
    # exit/missing exchange. No partial result is admitted from leftover files.
    _write_private(Path(output_path), json_bytes(packet))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
