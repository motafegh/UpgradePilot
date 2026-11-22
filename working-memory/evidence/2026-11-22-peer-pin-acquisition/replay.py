"""Replay the frozen peer-pin protocol against owner-retained inputs, offline."""

import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path, PurePosixPath
import re
from time import perf_counter_ns
from zipfile import ZipFile

from packaging.requirements import Requirement
from packaging.utils import canonicalize_name
from packaging.version import Version


BODY_CAP = 1_000_000
RELEASE_CAP = 20
TEXT_PATH = re.compile(r"(?<![\w/.-])[\w./-]+\.txt(?![\w/.-])")
SCENARIOS = Path(__file__).resolve().parents[3] / "product-simulation/scenarios"
CASES = (
    ("S017", "applypilot", "applypilot/replayed-report.json",
     "189313e90a01814a5569c34de3f57c1ac68057c0d7955342efed3045f2a3320e"),
    ("S019", "server-nexe", "server-nexe/frozen-report.json",
     "22ef7ef1d339291d14ae8028ad407a297daeee0c595de6ee6d113ce774e4af35"),
    ("S018", "mapproxy", "genuine.json",
     "989f4293bfbba6f00c447df495e6beade2873e1db213bf2410bfd42a3ade9931"),
)


def bounded_read(path):
    with path.open("rb") as stream:
        body = stream.read(BODY_CAP + 1)
    if len(body) > BODY_CAP:
        raise ValueError(f"Oversized retained input: {path.name}")
    return body


def text_paths(header):
    return {path for line in header for path in TEXT_PATH.findall(line)}


def parse_file(body):
    header = []
    requirements = {}
    for line_number, raw in enumerate(body.decode("utf-8").splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            if not requirements:
                header.append(line)
            continue
        req = Requirement(re.split(r"\s+#", line, maxsplit=1)[0].strip())
        name = canonicalize_name(req.name)
        if req.url or name in requirements:
            raise ValueError("Unsupported or ambiguous declarations")
        requirements[name] = (line_number, req)
    return text_paths(header), requirements


def plain(req):
    return not (req.url or req.extras or req.marker)


def exact_pins(requirements):
    pins = {}
    for name, (line, req) in requirements.items():
        specs = list(req.specifier)
        if plain(req) and len(specs) == 1 and specs[0].operator == "==" and "*" not in specs[0].version:
            pins[name] = (str(Version(specs[0].version)), line)
    return pins


class Replay:
    def __init__(self, files, releases):
        self.started = perf_counter_ns()
        self.files = files
        self.releases = releases
        self.reads = {"files": {}, "releases": {}}

    def read(self, kind, key):
        seen = self.reads[kind]
        assert key not in seen and len(seen) < {"files": 2, "releases": RELEASE_CAP}[kind]
        source = self.files if kind == "files" else self.releases
        body = source.get(key)
        seen[key] = {"available": body is not None, "payload_bytes": len(body or b"")}
        if body is not None and len(body) <= BODY_CAP:
            return body
        return None

    def receipt(self, **result):
        return {
            **result,
            "attempted": {kind: len(reads) for kind, reads in self.reads.items()},
            "fulfilled": {
                kind: sum(read["available"] and read["payload_bytes"] <= BODY_CAP for read in reads.values())
                for kind, reads in self.reads.items()
            },
            "retained_payload_bytes": {
                kind: sum(read["payload_bytes"] for read in reads.values()) for kind, reads in self.reads.items()
            },
            "elapsed_offline_ms": round((perf_counter_ns() - self.started) / 1_000_000, 3),
        }


def compare_release(body, peer, version, changed, changed_version):
    if body is None:
        return {"state": "unresolved", "reason": "release unavailable in replay"}
    try:
        info = json.loads(body)["info"]
        if canonicalize_name(info["name"]) != peer or Version(info["version"]) != Version(version):
            raise ValueError("Release identity mismatch")
        raw = info["requires_dist"]
        if not isinstance(raw, list) or not all(isinstance(item, str) for item in raw):
            raise ValueError("Missing or unusable Requires-Dist")
        edges = [(i, Requirement(item)) for i, item in enumerate(raw)]
    except (KeyError, TypeError, ValueError):
        return {"state": "unresolved", "reason": "release identity or metadata invalid"}
    relevant = [(i, req) for i, req in edges if canonicalize_name(req.name) == changed]
    if not relevant:
        return {"state": "no_matching_declaration"}
    if len(relevant) != 1 or not plain(relevant[0][1]):
        return {"state": "unresolved", "reason": "ambiguous or conditional edge"}
    index, edge = relevant[0]
    return {
        "state": "matches" if edge.specifier.contains(changed_version) else "conflict",
        "requirement": raw[index],
        "locator": f"info.requires_dist[{index}]",
    }


def investigate(files, releases, selected, changed, version, *, operator=None):
    replay = Replay(files, releases)
    path = PurePosixPath(selected)
    if operator is None and not path.name.endswith("-lock.txt"):
        return replay.receipt(outcome="unsupported_layout")
    consumed = replay.read("files", selected)
    if consumed is None:
        return replay.receipt(outcome="consumed_file_unavailable")
    companion = path.with_name(path.name.removesuffix("-lock.txt") + ".txt") if operator is None else None
    try:
        lock_refs, lock = parse_file(consumed)
        pins = exact_pins(lock)
        if changed not in pins or Version(pins[changed][0]) != Version(version):
            return replay.receipt(outcome="changed_pin_unbound")
        if companion is None:
            candidates = [operator] if operator != changed and operator in pins else []
            excluded = []
        else:
            if lock_refs - {path.name} != {companion.name}:
                return replay.receipt(outcome="companion_ambiguous")
            body = replay.read("files", str(companion))
            if body is None:
                return replay.receipt(outcome="companion_unavailable")
            root_refs, roots = parse_file(body)
            if root_refs - {companion.name} != {path.name}:
                return replay.receipt(outcome="companion_ambiguous")
            candidates = sorted(name for name, (_, req) in roots.items()
                                if name != changed and name in pins and plain(req))
            excluded = sorted(set(roots) - set(candidates) - {changed})
    except ValueError:
        return replay.receipt(outcome="unsupported_declaration")
    inventory = {"candidate_count": len(candidates), "other_exact_pins": len(pins) - 1,
                 "excluded_roots": excluded}
    if len(candidates) > RELEASE_CAP:
        return replay.receipt(outcome="candidate_budget_exceeded", **inventory)
    results = {}
    for peer in candidates:
        peer_version, peer_line = pins[peer]
        key = f"{peer}=={peer_version}"
        result = compare_release(replay.read("releases", key), peer, peer_version, changed, version)
        results[key] = {"line": peer_line, **result}
    return replay.receipt(
        outcome="evaluated" if candidates else "no_eligible_candidates",
        changed_line=pins[changed][1], **inventory, candidates=results,
        states=dict(Counter(result["state"] for result in results.values())),
    )


def verify_inputs(case_root, report_root):
    from upgradepilot.report import render_investigation_report
    from upgradepilot.report_file import read_report

    results = {}
    for case_id, target, report_relative, report_digest in CASES:
        manifest_path, = SCENARIOS.glob(f"{case_id}-*/CASE_EVIDENCE.json")
        packet = json.loads(manifest_path.read_bytes())
        change = packet["dependency_change"]
        identity = packet["frozen_identity"]
        head = identity["head"]
        ci = packet["selected_ci_evidence"]
        assert ci["run_head"] == ci["job_head"] == head
        path, changed, version = change["file"], change["package"], change["proposed_version"]
        report_path = report_root / report_relative
        report_body = bounded_read(report_path)
        assert sha256(report_body).hexdigest() == report_digest
        baseline = read_report(report_path)
        facts = {fact.name: fact.value for fact in baseline.identity}
        assert facts["repository"] == identity["repository"]
        assert facts["base_sha"] == identity["base"] and facts["head_sha"] == head
        rendered = render_investigation_report(baseline)
        assert f"Changed file: {path} (modified)" in rendered and baseline.action.state == "abstain"
        assert f"pip install -r {PurePosixPath(path).name}" in rendered
        if case_id == "S017":
            assert "step 4" in rendered and "conclusion='failure'" in rendered
            assert b"playwright" not in report_body.lower()
        receipt = packet["retained_evidence_sha256"]
        saved = f"{target}-target-{path.replace('/', '__')}.txt"
        original_lock = bounded_read(case_root / saved)
        assert sha256(original_lock).hexdigest() == receipt[saved]
        files = {path: original_lock}
        releases = {}
        if case_id == "S017":
            companion = "services/api/requirements.txt"
            archive = case_root / "applypilot-target-archive.zip"
            assert sha256(archive.read_bytes()).hexdigest() == "ae29da42abcf227195dd240565fc19d8d398a074b0136bc6be317eb10a917dab"
            with ZipFile(archive) as target_archive:
                assert target_archive.read(f"{target}-{head}/{path}") == original_lock
                files[companion] = target_archive.read(f"{target}-{head}/{companion}")
            assert sha256(files[companion]).hexdigest() == "0afb27301d8680dae081a444906d3862dff34fb160b76bb7ad3d7b13981abbc0"
            release_path = "playwright-1.64.1.json"
            body = bounded_read(case_root / release_path)
            assert sha256(body).hexdigest() == receipt[release_path]
            releases["playwright==1.64.1"] = body
        automatic = investigate(files, releases, path, changed, version)
        results[case_id] = {"head": head, "path": path, "baseline_report_sha256": report_digest,
                            "baseline_action": baseline.action.state, "automatic": automatic}
        if case_id == "S017":
            results[case_id].update(run_controls(files, releases, path, changed, version, change["old_version"]))
            assert automatic["candidate_count"] == 17 and automatic["other_exact_pins"] == 59
            assert automatic["states"] == {"unresolved": 16, "conflict": 1}
        else:
            assert automatic["outcome"] == "unsupported_layout" and automatic["attempted"]["files"] == 0
    return results


def run_controls(files, releases, path, changed, version, old):
    companion = "services/api/requirements.txt"
    peer_key = "playwright==1.64.1"
    operator = investigate(files, releases, path, changed, version, operator="playwright")
    old_lock = files[path].replace(f"{changed}=={version}\n".encode(), f"{changed}=={old}\n".encode())
    assert old_lock != files[path]
    old_pin = investigate({**files, path: old_lock}, releases, path, changed, old)
    absent = investigate(files, {}, path, changed, version)
    missing = investigate({path: files[path]}, releases, path, changed, version)
    competing = b"# Alternate scope: requirements-other-lock.txt\n" + files[companion]
    ambiguous = investigate({**files, companion: competing}, releases, path, changed, version)
    coincidental = investigate({**files, companion: b"playwright>=1.49,<2\n"}, releases, path, changed, version)
    unsupported = investigate({**files, path: files[path] + b"\n-r other.txt\n"}, releases, path, changed, version)
    extra_pins = b"".join(f"\ncontrol-peer-{i:02}==1.0".encode() for i in range(4))
    over_cap = investigate({path: files[path] + extra_pins, companion: files[companion] + extra_pins},
                           releases, path, changed, version)
    anyio_version = exact_pins(parse_file(files[path])[1])["anyio"][0]
    transitive_key = f"anyio=={anyio_version}"
    injected = {**releases, transitive_key: json.dumps({
        "info": {"name": "anyio", "version": anyio_version, "requires_dist": ["pyee<15"]}
    }).encode()}
    transitive = investigate(files, injected, path, changed, version)
    transitive_operator = investigate(files, injected, path, changed, version, operator="anyio")
    assert operator["candidates"][peer_key]["state"] == "conflict"
    assert old_pin["candidates"][peer_key]["state"] == "matches" and "conflict" not in old_pin["states"]
    assert absent["states"] == {"unresolved": 17}
    assert missing["outcome"] == "companion_unavailable"
    assert ambiguous["outcome"] == coincidental["outcome"] == "companion_ambiguous"
    assert unsupported["outcome"] == "unsupported_declaration"
    assert over_cap["outcome"] == "candidate_budget_exceeded" and over_cap["candidate_count"] == 21
    assert all(case["attempted"]["releases"] == 0
               for case in (missing, ambiguous, coincidental, unsupported, over_cap))
    assert transitive_key not in transitive["candidates"]
    assert transitive_operator["candidates"][transitive_key]["state"] == "conflict"
    return {"operator": operator, "controls": {
        "old_pin": old_pin, "missing_release": absent, "missing_companion": missing,
        "ambiguous_companion": ambiguous, "coincidental_basename": coincidental,
        "unsupported_include": unsupported, "over_cap": over_cap,
        "synthetic_transitive": transitive, "synthetic_transitive_operator": transitive_operator,
    }}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case_root", type=Path)
    parser.add_argument("report_root", type=Path)
    args = parser.parse_args()
    print(json.dumps(verify_inputs(args.case_root, args.report_root), indent=2))
