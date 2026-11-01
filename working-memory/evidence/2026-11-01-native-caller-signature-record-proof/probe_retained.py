"""One-run retained native component proof, not a product acquisition runner.

PYTHONPATH=src:. .venv/bin/python <this file>
Original private captures are read only. Public output contains metrics and IDs,
not retained source text. No producer replay or native-family admission is claimed.
"""
from collections import Counter, defaultdict
from contextlib import ExitStack
from hashlib import sha256
import json
from pathlib import Path
from unittest.mock import patch

from experiments import api_ordinary_call_signature_trial as donor
from experiments import api_call_signature_trial as curated
from upgradepilot.caller_signature.native_codec import (
    decode_source_facts, encode_source_facts, _pack, json_structure_cost,
    encode_duration, decode_duration,
    encode_fact_binding_traces,
)
from upgradepilot.caller_signature.evidence import MeasuredDuration
from upgradepilot.workspace.native_representation import json_bytes, parse_json
from upgradepilot.workspace.native_boundary import (
    CapturedNativeRecord, CapturedNativeBoundary, encode_native_boundary, read_native_boundary,
)
from upgradepilot.workspace.checkpoint_revision import CheckpointRevision

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EVIDENCE = ROOT / "working-memory/evidence"


def read(path):
    return json.loads(path.read_bytes())


freeze = read(EVIDENCE / "2026-11-01-analysis-capacity-and-work-admission/qualified-method.json")
for name, digest in freeze["code_sha256"].items():
    assert sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
rows = read(EVIDENCE / "2026-11-01-analysis-capacity-and-work-admission/retained-qualification-results.json")
cases = [(row["case"], Path(row["directory"]), row["output_sha256"]) for row in rows]
digimon = EVIDENCE / "2026-11-01-untouched-partial-analysis-qualification/ordinary-digimon-scraper-pr-16"
contract = read(digimon / "contract.json")
verification = read(digimon / "verification.json")
private = Path(contract["private_retention"]["root"])
digimon_hashes = {name.removeprefix("comparison/"): value for name, value in verification["artifact_hashes"].items() if name.startswith("comparison/")}
cases.append(("digimon", private / "comparison", digimon_hashes))
curated_root = Path.home() / ".local/share/upgradepilot/caller-signature-evidence/retained-httpx-2026-10-28/attempt-01"
curated_index = read(EVIDENCE / "2026-10-28-caller-signature-build/inspection.json")
curated_hashes = {name: item["sha256"] for name, item in curated_index["private_saved_files"].items()}
cases.append(("curated-httpx-rejection", curated_root, curated_hashes))
summary = []
sketch = ["# Early retained LifeLog report sketch", "",
          "Exposed experimental evidence projected for presentation review; not a native product report or usefulness test.", ""]
hooks = ("ast.parse", "requests.sessions.Session.request", "socket.socket.connect",
         "experiments.api_ordinary_call_signature_trial.discover_source_candidates",
         "experiments.api_call_signature.compare_arguments",
         "experiments.api_ordinary_call_signature_trial._read_attempt_credential")
with ExitStack() as stack:
    for name in hooks:
        stack.enter_context(patch(name, side_effect=AssertionError("Forbidden during component proof: " + name)))
    for case, directory, hashes in cases:
        before = {name: sha256((directory / name).read_bytes()).hexdigest() for name in hashes}
        assert before == hashes
        original = read(directory / "result.json")
        body, catalog = (curated.open_comparison(directory) if case == "curated-httpx-rejection"
                         else donor.open_ordinary_comparison(directory))
        files = {(f.source_id, f.path): f for f in catalog.files}
        encoded_units, counts, normalized = [], Counter(), []
        for raw, expanded in zip(original["files"], body["files"]):
            if raw["facts"] is None:
                encoded_units.append(None)
                normalized.append(raw)
                counts[raw["coverage"]] += 1
                continue
            descriptor = raw["descriptor"]
            text = files[descriptor["source_id"], descriptor["path"]].content
            args = dict(unit_id=descriptor["file_id"], text=text, coverage=raw["coverage"])
            wire_facts = (raw["facts"] if "binding_trace_steps" in raw["facts"]
                          else encode_fact_binding_traces(raw["facts"]))
            native = decode_source_facts(json_bytes({"codec_version": 1, "facts": wire_facts}), **args)
            assert _pack(native) == expanded["facts"]
            packet = encode_source_facts(native, text=text, coverage=raw["coverage"])
            restored = decode_source_facts(packet, **args)
            assert restored == native
            assert parse_json(packet)["facts"] == wire_facts
            encoded_units.append(packet)
            normalized.append(dict(raw, facts=parse_json(packet)))
            counts["analyzed"] += 1
            counts["calls"] += len(native.calls)
            counts["signatures"] += len(native.signatures)
            counts["trace_references"] += sum(len(c.binding.trace) for c in native.calls if c.binding)
            counts["unique_steps"] += len(wire_facts["binding_trace_steps"])

        # Keep every other recorded field when testing component overhead. This is
        # an explicit unported experimental context, not a new native domain payload.
        context = dict(original, files=normalized)
        payload = json_bytes(context)
        source_payload = (directory / "sources.json").read_bytes()
        source = CapturedNativeRecord("source-probe", "retained_source_probe", "caller_signature", 1,
            catalog.target, (), source_payload, sha256(source_payload).hexdigest(), "recorded", "component-probe", "1", ())
        comparison = CapturedNativeRecord("facts-probe", "source_fact_component_probe", "caller_signature", 1,
            catalog.target, (source.record_id,), payload, sha256(payload).hexdigest(), "recorded", "component-probe", "1", ())
        boundary = CapturedNativeBoundary(catalog.target, (source, comparison))
        envelope = encode_native_boundary(boundary)
        assert read_native_boundary(envelope, expected_target=catalog.target) == boundary
        revision = CheckpointRevision("component-probe", case, None, boundary)
        digest = revision.digest()
        assert before == {name: sha256((directory / name).read_bytes()).hexdigest() for name in hashes}
        summary.append(dict(case=case, matched_input_artifacts=len(before), **counts,
            normalized_fact_packet_bytes=sum(len(x) for x in encoded_units if x is not None),
            full_context_bytes=len(payload), full_context_structure=json_structure_cost(context),
            source_catalog_bytes=len(source_payload), boundary_bytes=len(envelope), checkpoint_digest=digest,
            native_fact_equivalence=True, original_bytes_unchanged=True))
        if case == "lifelog":
            sketch += [f"Retained files: {len(original['files'])}; unexamined Python units: {counts['unexamined']}.",
                f"Comparison records: {len(original['pairs'])}; retained gaps: {len(original['discovery']['gaps'])}; omitted diagnostics: {original['discovery']['gaps_omitted']}.",
                "Binding is source-local; installation, dispatch, execution and compatibility remain unproved.", ""]
            roots = defaultdict(list)
            outcomes = {p['selection']['id']: p['comparison']['outcome'] if p['comparison'] else p['problem'] for p in original['pairs']}
            for c in original['discovery']['candidates']:
                roots[c['root_call_id']].append(c)
            root_locations = {c['fact_id']: f"{item['descriptor']['path']}:{c['span']['line']}"
                              for item in original['files'] if item['facts']
                              for c in item['facts']['calls']}
            sketch += ["| Root source location | Witnesses | Local outcomes by source role | Required premises |", "|---|---:|---|---|"]
            for root_id, candidates in roots.items():
                premises = sorted({p for c in candidates for p in c['premises']})
                def role_label(candidate):
                    role = candidate['callee_role']
                    return f"{role['role']} {role['package']} {role['version']}"
                by_role = {role: dict(Counter(outcomes[c['id']] for c in candidates if role_label(c) == role))
                           for role in sorted({role_label(c) for c in candidates})}
                sketch.append(f"| {root_locations[root_id]} ({root_id[:12]}) | {len(candidates)} | {by_role} | {', '.join(premises)} |")

duration = MeasuredDuration.from_seconds(18.991642, "retained experimental total elapsed")
assert decode_duration(encode_duration(duration)) == duration
result = dict(proof="native source-fact component equivalence and enclosing structural capacity", cases=summary,
    qualified_donor_hashes_unchanged=len(freeze["code_sha256"]), forbidden_hooks=hooks,
    limitations=["Enclosing context remains the complete retained experimental representation, not a ported native family.",
        "Probe families are structural harness identities, not registered product-family admission.",
        "Native source/comparison layouts, method/version staging and full host/store/report delivery remain to qualify.",
        "No analysis producer replay, new acquisition, runtime compatibility or independent usefulness proof."])
(HERE / "retained-results.json").write_text(json.dumps(result, indent=2) + "\n")
(HERE / "early-report-sketch.md").write_text("\n".join(sketch) + "\n")
print(json.dumps(result, indent=2))
