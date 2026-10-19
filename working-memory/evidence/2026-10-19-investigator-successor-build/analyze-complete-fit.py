"""One-run, offline analysis of retained complete-input measurements.

Reads an existing zero-generation preflight; never constructs a model/client or
tokenizes. The candidate only decodes a known typed delivery's canonical JSON
string. Its inverse must reproduce every original event byte exactly. Candidate
byte savings are not token measurements or an executable presentation approval.
Run from the repository root with PYTHONPATH=src:.; JSON output is public-safe.
"""

import argparse
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path

from experiments.investigator_model_interface import present_request_body
from upgradepilot.workspace.native_representation import json_bytes


def digest(content):
    return sha256(content).hexdigest()


def analyze(root):
    preflight_path = root / "runtime-preflight.json"
    preflight = json.loads(preflight_path.read_bytes())
    assert preflight["prediction_attempts"] == 0
    assert not (root / "freeze.json").exists()
    assert set(preflight["fit"]) == set(preflight["roles"])
    assert 0 <= preflight["preparation_elapsed_seconds"] < 1200
    assert json.loads((root / "actual-identity.json").read_bytes()) == preflight["identity"]
    for name, expected in preflight["code_sha256"].items():
        assert digest(Path(name).read_bytes()) == expected, name
    rows = []
    for role in preflight["roles"]:
        fit = preflight["fit"][role]
        packed = (root / role / "fit-packed-input.json").read_bytes()
        rendered = (root / role / "fit-rendered.txt").read_bytes()
        assert digest(packed) == fit["packed_sha256"]
        assert digest(rendered) == fit["rendered_sha256"]
        measured = json.loads((root / role / "fit-measurement.json").read_bytes())
        assert measured == {key: value for key, value in fit.items() if key != "preparation_termination_id"}
        assert not fit["omitted_events"] and fit["preparation_termination_id"]
        body = json.loads(packed)
        user = present_request_body(body).encode()
        assert user in rendered
        candidate = deepcopy(body)
        source_text = source_descriptors = native_payload = typed = 0
        old_events = new_events = 0
        for original, proposed in zip(body["events"], candidate["events"], strict=True):
            envelope = json.loads(original["content"])
            old_events += len(original["content"].encode())
            tool = envelope.get("tool")
            if tool not in {"read_source", "read_native"}:
                new_events += len(proposed["content"].encode())
                continue
            inner = json.loads(envelope["content"])
            expected = "retained-source-view/1" if tool == "read_source" else "workspace-native-view/1"
            assert inner["format"] == expected
            assert json_bytes(inner).decode() == envelope["content"]
            envelope["content"] = inner
            proposed["content"] = json_bytes(envelope).decode()
            restored = json.loads(proposed["content"])
            restored["content"] = json_bytes(restored["content"]).decode()
            assert json_bytes(restored).decode() == original["content"]
            assert {k: v for k, v in proposed.items() if k != "content"} == {
                k: v for k, v in original.items() if k != "content"
            }
            new_events += len(proposed["content"].encode())
            typed += 1
            if tool == "read_source":
                source_text += sum(len(line.encode()) for line in inner["payload"]["lines"])
                source_descriptors += len(json_bytes(inner["payload"]["file"]))
            else:
                native_payload += sum(len(json_bytes(row["payload"])) for row in inner["native_records"])
        candidate_user = present_request_body(candidate).encode()
        savings = len(user) - len(candidate_user)
        assert savings == old_events - new_events
        cap = 4096 if role.startswith("probe-") else 16000
        tokens = fit["rendered_tokens"]
        assert fit["input_cap_met"] == (tokens <= cap)
        assert fit["context_reserve_met"] == (tokens + 8192 + 256 <= 32768)
        rows.append({
            "role": role, "rendered_tokens": tokens, "input_cap": cap,
            "input_cap_excess": max(0, tokens - cap),
            "context_input_ceiling": 24320, "context_input_headroom": 24320 - tokens,
            "input_cap_met": fit["input_cap_met"], "context_reserve_met": fit["context_reserve_met"],
            "references": len(fit["reference_pairs"]), "events": len(body["events"]),
            "omitted_events": fit["omitted_events"],
            "rendered_bytes": len(rendered), "user_presentation_bytes": len(user),
            "system_and_template_bytes": len(rendered) - len(user),
            "source_line_text_bytes_excluding_separators": source_text,
            "source_file_descriptor_bytes": source_descriptors,
            "native_payload_json_bytes": native_payload,
            "known_typed_delivery_count": typed,
            "decode_candidate": {
                "user_presentation_bytes": len(candidate_user), "bytes_saved": savings,
                "every_event_exact_byte_roundtrip": True,
                "tokens": None, "fit": "unmeasured; no runtime implementation or admission",
            },
        })
    cleanup = json.loads((root / "cleanup.json").read_bytes())
    client = json.loads((root / "client-cleanup.json").read_bytes())
    assert cleanup["confirmed"] and cleanup["remaining_identifiers"] == []
    assert client["confirmed"]
    return {
        "format": "investigator-complete-fit-analysis/1", "runtime_root": str(root.resolve()),
        "runtime_preflight_sha256": digest(preflight_path.read_bytes()),
        "analysis_source_sha256": digest(Path(__file__).read_bytes()),
        "preparation_elapsed_seconds": preflight["preparation_elapsed_seconds"],
        "prediction_attempts": 0, "executable_freeze": False,
        "source_hashes_verified": True, "loaded_identity_retained": (root / "actual-identity.json").is_file(),
        "owned_unload_confirmed": True, "client_release_confirmed": True,
        "rows": rows,
        "measured_input_sum": sum(row["rendered_tokens"] for row in rows),
        "declared_aggregate_input_ceiling": 72192,
        "limits": [
            "Counts are current zero-generation measurements, not the unknown original runtime-r1 count.",
            "Fresh host references and remaining-time facts can change exact later request counts.",
            "Byte components overlap; they do not partition tokens or establish causes of token cost.",
            "Decode candidate is an offline reversible representation check; token savings are unmeasured.",
            "No predictions, backend-cancellation qualification, semantic grading or new freeze.",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("runtime_root", type=Path)
    args = parser.parse_args()
    print(json.dumps(analyze(args.runtime_root), indent=2, sort_keys=True))
