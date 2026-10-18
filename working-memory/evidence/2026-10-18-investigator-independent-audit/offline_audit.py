"""Read-only historical evidence audit and deterministic control counterexamples.

Run from the repository root with PYTHONPATH=src:. and the project interpreter.
No SDK import, model load, inference, acquisition or original-artifact writes.
The two counterexamples use the existing deterministic test Binding in temporary dirs.
JSON output is a new audit derivative, never a replacement experiment result.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import stat
import tempfile
from collections import Counter
from pathlib import Path


def sha(content):
    return hashlib.sha256(content).hexdigest()


def read(path):
    return json.loads(path.read_bytes())


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def retained_integrity(root):
    path = root / "completed-retention-index.json"
    index = read(path)
    actual = {str(p.relative_to(root)) for p in root.rglob("*") if p.is_file() and p != path}
    expected = {item["path"] for item in index["files"]}
    errors = []
    if actual != expected:
        errors.append("file membership differs")
    for item in index["files"]:
        p = root / item["path"]
        content = p.read_bytes()
        if (len(content), sha(content), stat.S_IMODE(p.stat().st_mode)) != (
            item["bytes"], item["sha256"], int(item["mode"], 8)
        ):
            errors.append(item["path"])
    bad_dirs = [str(p.relative_to(root)) for p in [root, *root.rglob("*")]
                if p.is_dir() and stat.S_IMODE(p.stat().st_mode) != 0o700]
    return {"index_sha256": sha(path.read_bytes()), "files": len(expected),
            "bytes": sum(x["bytes"] for x in index["files"]),
            "errors": errors, "directory_mode_errors": bad_dirs}


def call_audit(root, stage):
    rows, errors = [], []
    for request_path in sorted((root / stage).glob("*/call-*.request.json")):
        prefix = request_path.name.removesuffix(".request.json")
        directory = request_path.parent
        get = lambda suffix: directory / (prefix + suffix)
        req = read(request_path)
        packed = read(get(".packed-input.json"))
        receipt = read(get(".receipt.json")) if get(".receipt.json").exists() else None
        pairs = sorted({(r["kind"], r["id"]) for e in packed["events"]
                        for r in json.loads(e["content"]).get("evidence", [])})
        if ([list(x) for x in pairs] != req["reference_pairs"]
                or sorted(x[1] for x in pairs) != req["references"]):
            errors.append(str(request_path.relative_to(root)) + ": offered reference mismatch")
        if (sha(get(".packed-input.json").read_bytes()) != req["packed_input_sha256"]
                or sha(get(".rendered.txt").read_bytes()) != req["rendered_sha256"]):
            errors.append(str(request_path.relative_to(root)) + ": retained input mismatch")
        usage = receipt.get("usage") if receipt else None
        known = usage is not None
        if known:
            meta = read(get(".metadata.json"))
            requested = {x["key"]: x["value"] for x in req["configuration"]["layers"][0]["config"]["fields"]}
            applied = {x["key"]: x["value"] for x in meta["predictionConfig"]["fields"]}
            if (receipt["outcome"] != "returned" or not receipt["complete_response_received"]
                    or usage != meta["stats"] or usage["promptTokensCount"] != req["rendered_tokens"]
                    or usage["totalTokensCount"] != usage["promptTokensCount"] + usage["predictedTokensCount"]
                    or any(applied.get(k) != v for k, v in requested.items())
                    or meta["modelInfo"]["instanceReference"] != req["identity"]["model"]["instanceReference"]
                    or get(".visible-response.txt").read_bytes() != get(".visible-fragments.txt").read_bytes()
                    or sha(get(".visible-fragments.txt").read_bytes()) != receipt["visible_fragments_sha256"]
                    or sha(canonical(req)) != receipt["request_sha256"]):
                errors.append(str(request_path.relative_to(root)) + ": actual correspondence mismatch")
        output = read(get(".visible-response.txt")) if get(".visible-response.txt").exists() else None
        rows.append({"assignment": directory.name, "call": prefix, "phase": packed["phase"],
                     "remaining_operations": packed["budget_observation"]["trial_remaining"]["operation_units"],
                     "rendered_tokens": req["rendered_tokens"], "omitted_events": len(req["omitted_events"]),
                     "typed_references": len(pairs), "known_usage": known,
                     "input_tokens": usage["promptTokensCount"] if known else None,
                     "generated_tokens": usage["predictedTokensCount"] if known else None,
                     "client_seconds": receipt["elapsed_seconds"] if receipt else None,
                     "tool": output.get("tool") if isinstance(output, dict) else None})
    return {"calls": len(rows), "known_usage": sum(r["known_usage"] for r in rows),
            "known_input": sum(r["input_tokens"] or 0 for r in rows),
            "known_generated": sum(r["generated_tokens"] or 0 for r in rows),
            "errors": errors, "rows": rows}


def control_probes():
    from experiments.investigator_model_interface import ModelLimits, StatelessInvestigatorModel
    from experiments.tests.test_investigator_model_interface import Binding, config, packed

    class Clock:
        now = 0

        def __call__(self):
            return self.now

    with tempfile.TemporaryDirectory() as td:
        binding, clock = Binding(), Clock()
        model = StatelessInvestigatorModel(binding, config(), ModelLimits(context=10000),
                                          Path(td) / "deadline", clock=clock)
        original, timeout_values = binding.predict, []

        def late(measured, timeout, *, visible_sink):
            timeout_values.append(timeout)
            clock.now += 1801
            return original(measured, timeout, visible_sink=visible_sink)

        binding.predict = late
        model(packed())
        deadline = {"passed_timeout": timeout_values, "returned_elapsed": model.receipts[-1]["elapsed_seconds"],
                    "receipt_outcome": model.receipts[-1]["outcome"]}
        binding = Binding()
        model = StatelessInvestigatorModel(binding, config(), ModelLimits(context=10000), Path(td) / "interrupt")

        def stop(measured, timeout, *, visible_sink):
            visible_sink(b"{")
            raise KeyboardInterrupt

        binding.predict = stop
        try:
            model(packed())
        except KeyboardInterrupt:
            pass
        interrupted = {"usage_complete_after_interrupt": model.usage_complete,
                       "receipt_usage": model.receipts[-1]["usage"],
                       "receipt_outcome": model.receipts[-1]["outcome"]}
        binding.predict = Binding().predict
        try:
            model(packed())
            interrupted["another_call_permitted"] = True
        except ValueError:
            interrupted["another_call_permitted"] = False
    return {"late_return": deadline, "keyboard_interrupt": interrupted,
            "limit": "Deterministic counterexamples using a test binding; no real prediction or claim of an observed runtime overrun."}


def common_evidence_shapes(root):
    from experiments.run_investigator_semantic_comparison import load_case_assignment

    qualification = read(root / "input-qualification.json")
    rows = []
    for case in qualification["cases"]:
        assignment = load_case_assignment(
            qualification, case["case_id"], "structured", 4096
        )
        records = []
        for record in assignment.host.current.boundary.records:
            if record.family in assignment.access.native_families:
                records.append({
                    "family": record.family,
                    "payload_bytes": len(record.payload),
                    "full_text_4096_character_pages": (
                        len(record.payload.decode()) + 4095
                    ) // 4096,
                })
        rows.append({
            "case_id": case["case_id"],
            "source_files": len(assignment.access.catalog.files),
            "source_characters": sum(
                len(file.content) for file in assignment.access.catalog.files
            ),
            "offered_native_records": records,
        })
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("/home/motafeq/.local/share/upgradepilot/investigator-runs/semantic-comparison-2026-10-18-reference-v2"))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {"format": "investigator-independent-audit/1", "inspected_revision": "e0a6de39",
              "integrity": retained_integrity(args.root),
              "qualification": call_audit(args.root, "interface-results"),
              "semantic": call_audit(args.root, "semantic-results"),
              "common_evidence_shapes": common_evidence_shapes(args.root),
              "control_counterexamples": control_probes()}
    result["semantic_tool_requests"] = dict(Counter(r["tool"] for r in result["semantic"]["rows"] if r["tool"]))
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk != "rows"} if isinstance(v, dict) else v
                      for k, v in result.items()}))
    if (result["integrity"]["errors"] or result["integrity"]["directory_mode_errors"]
            or result["qualification"]["errors"] or result["semantic"]["errors"]):
        raise SystemExit("Historical evidence integrity/correspondence failed; inspect audit output")


if __name__ == "__main__":
    main()
