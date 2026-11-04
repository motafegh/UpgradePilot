"""Development probe: equivalent streaming preflight with C-level span searches.

This is not an adopted parser. Compare guard outcomes before benchmarking. JSON
syntax/UTF-8 validation remains the standard parser's job in either implementation.
"""
from hashlib import sha256
import argparse
import json
from pathlib import Path
import random
import re
import time
from unittest.mock import patch

from upgradepilot.workspace import native_representation as representation
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_boundary import encode_native_boundary
from upgradepilot.workspace.lifecycle_boundary import encode_lifecycle_history

STRUCTURAL_OR_QUOTE = re.compile(rb'["{}\[\],:]')


def candidate_scan(payload, limits):
    size, max_depth, max_tokens = limits
    def refuse(detail):
        return representation.NativeReconstructionError("native_resource_limit", detail)
    if len(payload) > size:
        raise refuse(f"Native JSON exceeds {size} bytes.")
    depth = tokens = position = 0
    while (match := STRUCTURAL_OR_QUOTE.search(payload, position)) is not None:
        position = match.start()
        byte = payload[position]
        if byte == 34:
            end = payload.find(b'"', position + 1)
            while end != -1:
                slash = end - 1
                while slash > position and payload[slash] == 92:
                    slash -= 1
                if (end - slash - 1) % 2 == 0:
                    break
                end = payload.find(b'"', end + 1)
            if end == -1:
                break  # Standard JSON parsing still refuses the unfinished string.
            position = end + 1
            continue
        if byte in (123, 91):
            depth += 1
            if depth > max_depth:
                raise refuse(f"Native JSON exceeds depth {max_depth}.")
        elif byte in (125, 93):
            depth -= 1
        tokens += 1
        if tokens > max_tokens:
            raise refuse(f"Native JSON exceeds {max_tokens} structural tokens.")
        position += 1


def outcome(call):
    try:
        call()
        return "ok"
    except representation.NativeReconstructionError as error:
        return str(error)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--store", type=Path, required=True)
    p.add_argument("--revision", required=True)
    args = p.parse_args()
    args.output.mkdir(mode=0o700, exist_ok=False)
    contract = dict(proof="development-only scanner differential and counter probe",
        source_method_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        baseline="38741c3c original byte-wise preflight", seed=20261104,
        syntax="Neither preflight owns JSON syntax; the standard parser is unchanged",
        timing="Interleaved local elapsed/CPU counter readings, not active55-minute proof")
    (args.output/"contract.json").write_text(json.dumps(contract, indent=2)+"\n")
    generator = random.Random(contract["seed"])
    alphabet = b'{}[],:"\\\\abcdefghijklmnopqrstuvwxyz0123 \n\xff'
    samples = [bytes(generator.choice(alphabet) for _ in range(generator.randrange(160))) for _ in range(2000)]
    samples += [json.dumps({"source": text, "items": [0, 1]}, ensure_ascii=False).encode()
                for text in ('[{}],: "quoted" \\ escaped', '\\'*999+'"', 'plain '*2000, 'é\\"{}[],:')]
    checked = 0
    for payload in samples:
        for limits in ((len(payload), 4, 8), (len(payload)+1, 2, 3), (max(0,len(payload)-1), 64, 262144)):
            with patch.object(representation,"MAX_NATIVE_JSON_BYTES",limits[0]), patch.object(representation,"MAX_NATIVE_JSON_DEPTH",limits[1]), patch.object(representation,"MAX_NATIVE_JSON_STRUCTURAL_TOKENS",limits[2]):
                old = outcome(lambda: representation._check_json_resources(payload))
                new = outcome(lambda: candidate_scan(payload,limits))
            assert old == new, (payload.hex(), limits, old, new)
            checked += 1
    revision = CheckpointStore.open(args.store, read_only=True).read_selected_revision(args.revision).revision
    buffers = {"comparison":next(r.payload for r in revision.boundary.records if r.family=="caller_signature_comparison"),
               "native_boundary":encode_native_boundary(revision.boundary), "lifecycle":encode_lifecycle_history(revision.lifecycle_history)}
    limits=(representation.MAX_NATIVE_JSON_BYTES,representation.MAX_NATIVE_JSON_DEPTH,representation.MAX_NATIVE_JSON_STRUCTURAL_TOKENS)
    rows=[]
    for name,payload in buffers.items():
        old = outcome(lambda: representation._check_json_resources(payload))
        new = outcome(lambda: candidate_scan(payload,limits))
        assert old == new, (name,old,new)
        times={"baseline":[],"candidate":[]}
        for order in (("baseline","candidate"),("candidate","baseline"),("baseline","candidate")):
            for method in order:
                start,cpu=time.monotonic_ns(),time.process_time_ns()
                if method=="baseline":representation._check_json_resources(payload)
                else:candidate_scan(payload,limits)
                times[method].append(dict(elapsed_counter_ns=time.monotonic_ns()-start,cpu_counter_ns=time.process_time_ns()-cpu))
        rows.append(dict(name=name,bytes=len(payload),sha256=sha256(payload).hexdigest(),outcome=old,counters=times))
    result=dict(differential_cases=checked,all_outcomes_equal=True,retained_buffers=rows)
    (args.output/"results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result))


if __name__=="__main__":
    main()
