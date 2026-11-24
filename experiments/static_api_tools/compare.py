"""Run the exposed static comparison and retain raw and verified evidence."""

import argparse
from dataclasses import asdict
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from time import perf_counter

from upgradepilot.caller_signature.analysis import compare_arguments, extract_python_source

HERE = Path(__file__).resolve().parent
LEXICAL = {
    "av-tracer": r"\b(TestClient|__init__)\s*\(",
    "glyphslib": r"\b(raises|parametrize)\s*\(",
}
AV_PAIRS = (
    ("av-entry", "source-28", 6, "TestClient", "source-29", "TestClient.__init__"),
    ("av-httpx-old", "source-29", 399, "super().__init__", "source-36", "Client.__init__"),
    ("av-httpx-new", "source-29", 399, "super().__init__", "source-31", "Client.__init__"),
)


def read_json(path):
    return json.loads(path.read_bytes())


def write_json(path, data):
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def verify_files(packet, entries):
    for entry in entries:
        digest = hashlib.sha256((packet / entry["file"]).read_bytes()).hexdigest()
        if digest != entry["sha256"]:
            raise ValueError(f"Digest mismatch: {entry['file']}")


def unique(items):
    item, = items
    return item


def summarize_binding(pair_id, caller_path, callee_path, call, signature, receiver_mode):
    result = compare_arguments(call, signature, receiver_mode)
    return {
        "id": pair_id, "caller_file": caller_path, "caller_span": asdict(call.span),
        "callee_file": callee_path, "callee_header": asdict(signature.header_span),
        "caller_origins": list(call.binding.possible_imports) if call.binding else [],
        "receiver_mode": receiver_mode, "outcome": result.outcome,
        "violations": [asdict(item) for item in result.violations],
        "keywords": [asdict(item) for item in result.keyword_reception],
        "premises": result.remaining_premises, "unresolved_checks": result.unresolved_checks,
    }


def baseline(packet, entries):
    start = perf_counter()
    python_files = [file for file in entries if file["file"].endswith(".py")]
    facts = {
        file["file"]: extract_python_source(file["file"], (packet / file["file"]).read_text(encoding="utf-8"), complete=True)
        for file in python_files
    }
    source_paths = {(f["source_id"], f["path"]): f["file"] for f in python_files}
    av = {f["source_id"]: f["file"] for f in python_files if f.get("case") == "av-tracer"}
    results = []
    for pair_id, caller_id, line, expression, callee_id, name in AV_PAIRS:
        caller, callee = av[caller_id], av[callee_id]
        call = unique(c for c in facts[caller].calls if c.span.line == line and c.expression == expression)
        signature = unique(s for s in facts[callee].signatures if s.qualified_name == name)
        results.append(summarize_binding(
            pair_id, caller, callee, call, signature, "one_receiver_assumed",
        ))
    for pair in read_json(packet / "glyph-pairs.json"):
        caller, callee = (pair[key] for key in ("caller", "callee"))
        caller_path = source_paths[caller["source_id"], caller["path"]]
        callee_path = source_paths[callee["source_id"], callee["path"]]
        call = unique(c for c in facts[caller_path].calls if asdict(c.span) == caller["span"])
        signature = unique(s for s in facts[callee_path].signatures if asdict(s.span) == callee["span"])
        results.append(summarize_binding(
            pair["id"], caller_path, callee_path, call, signature, pair["receiver_mode"],
        ))
    return facts, results, perf_counter() - start


def run_command(output, packet, name, args, success=(0,)):
    # The packet is a working directory only. It never enters Python's import path.
    command = ["unshare", "-Urn", *map(str, args)]
    env = {"PATH": os.defpath, "HOME": str(output), "LC_ALL": "C.UTF-8"}
    started = perf_counter()
    process = subprocess.run(
        command, cwd=packet, env=env, capture_output=True, timeout=120,
        text=True, encoding="utf-8", check=False,
    )
    receipt = {"command": command, "seconds": perf_counter() - started, "exit": process.returncode}
    (output / f"{name}.stdout").write_text(process.stdout)
    (output / f"{name}.stderr").write_text(process.stderr)
    write_json(output / f"{name}.invocation.json", receipt)
    if process.returncode not in success:
        raise RuntimeError(f"{name} exited {process.returncode}. See {output / (name + '.stderr')}")
    return process.stdout, receipt


def semgrep_coordinates(match):
    start, end = match["start"], match["end"]
    return {
        "file": match["path"], "line": start["line"], "column": start["col"] - 1,
        "end_line": end["line"], "end_column": end["col"] - 1,
    }


def control_missing_definition(packet, output, entries):
    control_packet = output / "missing-definition"
    for entry in entries:
        if entry["role"] not in {"httpx-old", "httpx-new"}:
            continue
        if entry["source_id"] == "source-31":
            continue
        relative = entry["file"]
        destination = control_packet / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(packet / relative, destination)
    return control_packet


def compare(packet, toolenv, output):
    output.mkdir(mode=0o700)
    manifest = read_json(packet / "manifest.json")
    files, controls = manifest["files"], manifest["controls"]
    verify_files(packet, files + controls)
    facts, findings, native_seconds = baseline(
        packet, files + [dict(control, path=control["file"], source_id="control") for control in controls],
    )
    write_json(output / "baseline.json", {
        "seconds": native_seconds, "findings": findings,
        "parse_problems": {name: data.problems for name, data in facts.items() if data.problems},
    })

    griffe = [toolenv / "bin/python", "-I", HERE / "griffe_static.py"]
    run_command(output, packet, "griffe", [
        *griffe, packet, "httpx-public", "httpx-client", "pytest-raises", "pytest-mark",
    ])
    missing = control_missing_definition(packet, output, files)
    run_command(output, packet, "griffe-missing", [*griffe, missing, "httpx-client"])

    for case, pattern in LEXICAL.items():
        roles = {"target", "fastapi", "starlette"} if case == "av-tracer" else {
            "target-base", "target-proposed",
        }
        paths = sorted(entry["file"] for entry in files if entry["case"] == case
                       and entry["role"] in roles and entry["file"].endswith(".py"))
        if case == "av-tracer":
            paths.extend(control["file"] for control in controls)
        lexical, lexical_run = run_command(
            output, packet, f"{case}-lexical", ["rg", "--json", "--", pattern, *paths], success=(0, 1),
        )
        semgrep, semgrep_run = run_command(output, packet, f"{case}-semgrep", [
            toolenv / "bin/semgrep", "scan", "--config", HERE / "calls.yaml", "--metrics", "off",
            "--disable-version-check", "--no-git-ignore", "--disable-nosem", "--strict",
            "--no-rewrite-rule-ids", "--exclude-rule",
            "glyph-candidate" if case == "av-tracer" else "av-candidate",
            "--verbose", "--json", "--jobs", "1", "--", *paths,
        ])
        lexical_rows = [json.loads(row) for row in lexical.splitlines()]
        hits = [
            {"file": row["data"]["path"]["text"], "line": row["data"]["line_number"],
             "occurrences": len(row["data"]["submatches"])}
            for row in lexical_rows if row["type"] == "match"
        ]
        data = json.loads(semgrep)
        matches = [semgrep_coordinates(match) for match in data["results"]]
        pairs = {}
        for match in matches:
            coordinates = {key: value for key, value in match.items() if key != "file"}
            calls = [c for c in facts[match["file"]].calls if asdict(c.span) == coordinates]
            match["native_parse_matches"] = len(calls)
            match["native_origins"] = [
                origin for c in calls if c.binding for origin in c.binding.possible_imports
            ]
            if len(calls) != 1:
                continue
            # Reuse the exact reviewed signature and receiver premise for an affirmed span.
            for finding in findings:
                if finding["caller_file"] != match["file"] or finding["caller_span"] != coordinates:
                    continue
                signatures = facts[finding["callee_file"]].signatures
                signature = unique(
                    s for s in signatures if asdict(s.header_span) == finding["callee_header"]
                )
                recounted = summarize_binding(
                    finding["id"], match["file"], finding["callee_file"], calls[0],
                    signature, finding["receiver_mode"],
                )
                if recounted != finding:
                    raise ValueError(f"Candidate changed the original binding: {match}")
                pairs[finding["id"]] = recounted
        write_json(output / f"{case}-comparison.json", {
            "paths": paths, "lexical_seconds": lexical_run["seconds"], "lexical_hits": hits,
            "semgrep_seconds": semgrep_run["seconds"], "semgrep_matches": matches,
            "semgrep_paths": data["paths"], "semgrep_errors": data["errors"],
            "semgrep_verified_pairs": pairs,
        })

    write_json(output / "environment.json", {
        "native_package": importlib.metadata.version("upgradepilot"),
        "native_python": sys.version, "offline": "unshare -Urn for coordinator and every subprocess",
    })


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    parser.add_argument("toolenv", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    compare(args.packet.resolve(), args.toolenv.resolve(), args.output.resolve())
