"""Fixed comparison-family run state at one exact source-family basis.

Completed runs reuse result_codec's earned cross-file checks and normalized
traces. Failed/interrupted/timed-out runs retain costs/reasons but no invented
result. Source text is not duplicated. This decoder never invokes the worker.
"""
from __future__ import annotations

from hashlib import sha256

from .evidence import SourceAnalysisRun
from .native_codec import decode_duration, encode_duration
from .result_codec import decode_analysis_result, encode_analysis_input, encode_analysis_result
from .source_evidence import CallerSignatureSources
from ..workspace.native_representation import json_bytes, object_fields, parse_json

FORMAT = "caller-signature-comparison/1"


def encode_comparison(value: SourceAnalysisRun | None, sources: CallerSignatureSources | None) -> bytes:
    if value is None:
        return json_bytes(None)
    prepared = sources.analysis_input() if sources is not None else None
    if prepared is None:
        raise ValueError("Recorded comparison lacks its source analysis basis.")
    payload = json_bytes(dict(format=FORMAT, state=value.state, reason=value.reason,
        input_sha256=value.input_sha256, elapsed=parse_json(encode_duration(value.elapsed)),
        worker_returncode=value.worker_returncode, worker_module_origin=value.worker_module_origin,
        problem_detail=value.problem_detail,
        result=parse_json(encode_analysis_result(value.result, prepared)) if value.result is not None else None))
    if decode_comparison(payload, sources) != value:
        raise ValueError("Comparison family encoding changed retained meaning.")
    return payload


def decode_comparison(payload: bytes, sources: CallerSignatureSources | None) -> SourceAnalysisRun | None:
    parsed = parse_json(payload)
    if parsed is None:
        return None
    row = object_fields(parsed, ("format", "state", "reason", "input_sha256", "elapsed", "worker_returncode", "worker_module_origin", "problem_detail", "result"))
    if row["format"] != FORMAT or row["state"] not in {"completed", "failed", "timed_out", "interrupted"}:
        raise ValueError("Unsupported comparison run state.")
    prepared = sources.analysis_input() if sources is not None else None
    if prepared is None or row["input_sha256"] != sha256(encode_analysis_input(prepared)).hexdigest():
        raise ValueError("Comparison/source analysis input mismatch.")
    elapsed = decode_duration(json_bytes(row["elapsed"]))
    code, origin, detail = row["worker_returncode"], row["worker_module_origin"], row["problem_detail"]
    if code is not None and type(code) is not int:
        raise ValueError("Invalid worker return code.")
    if origin is not None and (type(origin) is not str or not origin or len(origin) > 4096):
        raise ValueError("Invalid worker module origin.")
    if detail is not None and (type(detail) is not str or len(detail) > 2000):
        raise ValueError("Invalid worker problem detail.")
    result = None
    if row["state"] == "completed":
        if row["reason"] is not None or code != 0 or origin is None or detail is not None or row["result"] is None:
            raise ValueError("Incomplete completed worker observation.")
        result = decode_analysis_result(json_bytes(row["result"]), prepared)
    else:
        allowed = {"failed": {"bounded_worker_exit", "analysis_limit", "memory_limit", "invalid_analysis", "worker_io_failure", "invalid_worker_exchange"},
                   "timed_out": {"bounded_worker_deadline"}, "interrupted": {"caller_interrupt"}}[row["state"]]
        if row["reason"] not in allowed or row["result"] is not None:
            raise ValueError("Failed worker contains unsupported reason or result.")
    return SourceAnalysisRun(row["state"], row["reason"], row["input_sha256"], elapsed, code, origin, result, detail)
