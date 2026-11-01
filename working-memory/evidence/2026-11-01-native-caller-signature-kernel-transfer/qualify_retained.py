"""Compare the relocated native kernel with trusted frozen project source.

PYTHONPATH=src:. .venv/bin/python <this file>
Only UpgradePilot's own reference modules are loaded. Retained target/library text
is AST-parsed, never imported or executed. Fixed cold opening is checked separately.
"""
import ast
from contextlib import ExitStack
from dataclasses import asdict
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import types
from unittest.mock import patch

from experiments import api_ordinary_call_signature_trial as ordinary
from experiments import api_call_signature_trial as curated
from upgradepilot.caller_signature import analysis, bindings, correspondence
from upgradepilot.caller_signature.evidence import AnalysisLimits

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EVIDENCE = ROOT / "working-memory/evidence"
REFERENCE = "7ed069a0"


def read(path):
    return json.loads(path.read_bytes())


def canonical(value):
    # Equality diagnostic over already bounded records, not a persisted wire or
    # a way around native representation guards. Only its digest is retained.
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def load_reference(directory):
    name = "_upgradepilot_frozen_kernel"
    package = types.ModuleType(name)
    package.__path__ = [str(directory)]
    sys.modules[name] = package
    loaded = {}
    for stem in ("api_python_bindings", "api_call_signature", "api_signature_evidence", "api_source_correspondence"):
        text = subprocess.check_output(["git", "show", f"{REFERENCE}:experiments/{stem}.py"], cwd=ROOT)
        path = directory / (stem + ".py")
        path.write_bytes(text)
        spec = importlib.util.spec_from_file_location(name + "." + stem, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        loaded[stem] = module
    return loaded


rows = read(EVIDENCE / "2026-11-01-analysis-capacity-and-work-admission/retained-qualification-results.json")
cases = [(r["case"], Path(r["directory"]), r["output_sha256"], False) for r in rows]
digimon = EVIDENCE / "2026-11-01-untouched-partial-analysis-qualification/ordinary-digimon-scraper-pr-16"
private = Path(read(digimon / "contract.json")["private_retention"]["root"])
hashes = read(digimon / "verification.json")["artifact_hashes"]
cases.append(("digimon", private / "comparison",
              {n.removeprefix("comparison/"): v for n, v in hashes.items() if n.startswith("comparison/")}, False))
index = read(EVIDENCE / "2026-10-28-caller-signature-build/inspection.json")
cases.append(("curated-httpx-rejection",
    Path.home() / ".local/share/upgradepilot/caller-signature-evidence/retained-httpx-2026-10-28/attempt-01",
    {n: v["sha256"] for n, v in index["private_saved_files"].items()}, True))

results = []
with tempfile.TemporaryDirectory(prefix="upgradepilot-reference-kernel-") as tmp:
    reference = load_reference(Path(tmp))
    old_analysis = reference["api_call_signature"]
    old_bindings = reference["api_python_bindings"]
    old_correspondence = reference["api_source_correspondence"]
    for case, directory, hashes, is_curated in cases:
        assert hashes == {n: sha256((directory / n).read_bytes()).hexdigest() for n in hashes}
        with ExitStack() as stack:
            for hook in ("ast.parse", "requests.sessions.Session.request", "socket.socket.connect",
                         "upgradepilot.caller_signature.analysis.extract_python_source",
                         "upgradepilot.caller_signature.analysis.compare_arguments",
                         "upgradepilot.caller_signature.bindings.analyze_python_bindings",
                         "upgradepilot.caller_signature.correspondence.discover_source_candidates"):
                stack.enter_context(patch(hook, side_effect=AssertionError("Forbidden on cold open: " + hook)))
            body, catalog = (curated.open_comparison(directory) if is_curated else ordinary.open_ordinary_comparison(directory))
        sources = {(f.source_id, f.path): f.content for f in catalog.files}
        old_calls, old_signatures, new_calls, new_signatures = {}, {}, {}, {}
        files_checked = facts_checked = 0
        digest = sha256()
        with patch("requests.sessions.Session.request", side_effect=AssertionError("No network")), \
             patch("socket.socket.connect", side_effect=AssertionError("No network")):
            for unit in body["files"]:
                if unit["facts"] is None:
                    continue
                descriptor = unit["descriptor"]
                text = sources[descriptor["source_id"], descriptor["path"]]
                uid = descriptor["file_id"]
                kwargs = dict(complete=unit["coverage"] == "complete_file",
                              max_nodes=body["limits"]["max_nodes_per_file"], max_facts=body["limits"]["max_facts"])
                old = old_analysis.extract_python_source(uid, text, **kwargs)
                new = analysis.extract_python_source(uid, text, **kwargs)
                encoded = canonical(asdict(new))
                assert encoded == canonical(asdict(old)) == canonical(unit["facts"]), (case, descriptor["path"])
                old_origins = old_bindings.analyze_python_bindings(uid, text, ast.parse(text))
                new_origins = bindings.analyze_python_bindings(uid, text, ast.parse(text))
                assert canonical([[asdict(x) for x in group] for group in old_origins]) == canonical(
                    [[asdict(x) for x in group] for group in new_origins])
                digest.update(encoded.encode())
                old_calls.update((x.fact_id, x) for x in old.calls)
                old_signatures.update((x.fact_id, x) for x in old.signatures)
                new_calls.update((x.fact_id, x) for x in new.calls)
                new_signatures.update((x.fact_id, x) for x in new.signatures)
                files_checked += 1
                facts_checked += len(new.calls) + len(new.signatures)
            outcomes = []
            for pair in body["pairs"]:
                saved = pair["comparison"]
                if saved is None:
                    continue
                call_id, signature_id, mode = (saved[n] for n in ("call_id", "signature_id", "receiver_mode"))
                old = old_analysis.compare_arguments(old_calls[call_id], old_signatures[signature_id], mode)
                new = analysis.compare_arguments(new_calls[call_id], new_signatures[signature_id], mode)
                assert canonical(asdict(old)) == canonical(asdict(new)) == canonical(saved)
                outcomes.append(new.outcome)
        correspondence_equal = None
        if not is_curated:
            # The declared native role mapping is the only allowed semantic-label
            # change; original scope/file/fact IDs stay unchanged in this replay.
            role_map = {"target": "target_repository", "native_old_version": "old_dependency",
                        "native_proposed_version": "proposed_dependency", "constraint_sample": "constraint_sample"}
            inverse_roles = {value: key for key, value in role_map.items()}
            old_modules = tuple(old_correspondence.PythonSourceModule(**dict(m, dependencies=tuple(m["dependencies"]))) for m in body["modules"])
            new_modules = tuple(correspondence.PythonSourceModule(**dict(m, role=role_map[m["role"]], dependencies=tuple(m["dependencies"]))) for m in body["modules"])
            options = dict(analysis_profile=body.get("analysis_admission", {}).get("profile"),
                           max_depth=body["discovery"]["max_depth"], max_path_steps=body["discovery"]["max_path_steps"])
            with patch("requests.sessions.Session.request", side_effect=AssertionError("No network")), \
                 patch("socket.socket.connect", side_effect=AssertionError("No network")):
                old_discovery, old_pairs, old_units = old_correspondence.discover_source_candidates(catalog, old_modules, AnalysisLimits(**body["limits"]), **options)
                new_discovery, new_pairs, new_units = correspondence.discover_source_candidates(catalog, new_modules, AnalysisLimits(**body["limits"]), **options)
            for candidate in new_discovery["candidates"]:
                candidate["callee_role"]["role"] = inverse_roles[candidate["callee_role"]["role"]]
            saved_discovery = dict(body["discovery"])
            if "analysis_admission" in body:
                saved_discovery["analysis_admission"] = body["analysis_admission"]
            assert canonical(old_discovery) == canonical(new_discovery) == canonical(saved_discovery)
            assert canonical(old_pairs) == canonical(new_pairs) == canonical(body["pairs"])
            assert canonical(old_units) == canonical(new_units) == canonical([u for u in body["files"] if u["facts"] is not None])
            correspondence_equal = True
        assert hashes == {n: sha256((directory / n).read_bytes()).hexdigest() for n in hashes}
        results.append(dict(case=case, admitted_files_checked=files_checked, fact_records_checked=facts_checked,
            comparisons_checked=len(outcomes), rejected_comparisons=outcomes.count("rejected"), facts_sha256=digest.hexdigest(),
            correspondence_admission_paths_premises_gaps_equal=correspondence_equal,
            native_equals_reference_and_saved=True, fixed_cold_open=True, original_artifacts_unchanged=len(hashes)))

summary = dict(reference_commit=REFERENCE, proof="native binding/extraction/checker/correspondence/admission equals frozen project implementation and retained results under explicit role mapping",
    cases=results, target_or_library_execution=False, new_acquisition=False,
    limits="Retained complete inputs/limits for four ordinary correspondence captures, plus curated fact/checker control; acquisition and native families remain unimplemented.")
(HERE / "retained-equivalence.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary, indent=2))
