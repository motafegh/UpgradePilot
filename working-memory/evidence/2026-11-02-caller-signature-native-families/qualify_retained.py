"""Clearly labelled retained-receipt → native-family/checkpoint qualification.

PYTHONPATH=src:tests:. .venv/bin/python <this file>
No acquisition, target execution or frozen bundle mutation. Missing historical
full association/tag observations remain gaps, never reconstructed facts.
"""
from contextlib import ExitStack
from dataclasses import replace
from dataclasses import asdict
from datetime import datetime
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from unittest.mock import patch

from experiments import api_ordinary_call_signature_trial as ordinary
from upgradepilot.caller_signature import source_evidence as se
from upgradepilot.caller_signature.bindings import BindingAssessment, BindingTraceStep, ImportFact, ReferenceFact
from upgradepilot.caller_signature.correspondence import PythonSourceModule
from upgradepilot.caller_signature.evidence import AnalysisLimits, MeasuredDuration, json_structure_cost
from upgradepilot.caller_signature.source_codec import encode_sources
from upgradepilot.caller_signature.worker import run_source_analysis
from upgradepilot.dependency.change import DependencyChangeSourceEvidence, DependencyVersionChange
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost
from upgradepilot.workspace.native_boundary import encode_native_boundary
from upgradepilot.workspace.native_capture import NativeInvestigationCapture
from upgradepilot.workspace.native_projection import reconstruct_caller_signature_projection
from upgradepilot.workspace.native_representation import parse_json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EVIDENCE = ROOT / "working-memory/evidence"
ROLE = {"target": "target_repository", "native_old_version": "old_dependency", "native_proposed_version": "proposed_dependency", "constraint_sample": "constraint_sample", "explicit_version": "explicit_version"}


def read(path):
    return json.loads(path.read_bytes())


def declaration(raw):
    return se.SourceDependencyDeclaration(**dict(raw, extras=tuple(raw["extras"])))


def candidate(raw):
    return se.SourceImportCandidate(**dict(raw, declaration=declaration(raw["declaration"])))


def gap(raw):
    return se.SourceContextGap(**raw)


def metadata(raw):
    return se.SourceDependencyMetadata(**dict(raw, requirements=tuple(declaration(d) for d in raw["requirements"]), gaps=tuple(gap(g) for g in raw["gaps"])))


def origin(raw):
    if raw is None:
        return None
    if "relative_level" in raw:
        return ImportFact(**raw)
    binding = raw["binding"]
    if binding is not None:
        binding = BindingAssessment(**dict(binding, possible_imports=tuple(binding["possible_imports"]), reasons=tuple(binding["reasons"]), trace=tuple(BindingTraceStep(**s) for s in binding["trace"])))
    return ReferenceFact(**dict(raw, keyword_names=tuple(raw["keyword_names"]), binding=binding))


def module_receipt(raw, catalog):
    request = se.ModuleSourceRequest(**dict(raw["request"], version_basis=ROLE[raw["request"]["version_basis"]], origin=origin(raw["request"]["origin"])))
    if raw["state"] != "module_examined":
        return se.ModuleSourceReceipt(request, raw["state"], se.SourceProblem(raw["stage"], raw["reason"], raw["detail"]),
            None, None, None, None, None, None, None, (), None, (), None, (), ("original_provider_problem_object_not_retained",))
    return se.ModuleSourceReceipt(request, raw["state"], None, raw["repository"], raw["revision"], raw["path"], raw["sha256"], raw["bytes"],
        raw["association_basis"], raw["provenance_state"], tuple(se.SourceTagCommit(k, v) for k, v in raw["tag_commits"].items()), metadata(raw["metadata"]),
        tuple(gap(g) for g in raw["gaps"]), None, (), ("full_association_observations_not_retained", "full_tag_observations_not_retained"))


def receipt(raw, catalog):
    value = raw["ordinary_acquisition"]
    target = value["target"]
    target = se.TargetSourceReceipt(target["repository"], target["revision"], target["tree_sha"], target["inventory_entries"], target["inventory_truncated"],
        tuple(se.SourceFileReceipt(f["source_id"], f["sha256"], f["bytes"]) for f in target["files"]),
        tuple(declaration(d) for d in target["declarations"]), tuple(candidate(c) for c in target["candidates"]),
        tuple(target["excluded_paths"]), tuple(target["omitted_paths"]), tuple(gap(g) for g in target["gaps"]), target["examined_bytes"], tuple(target["limitations"]))
    changed = value["changed_package_sources"]
    adapters = value["adapter_exploration"]
    modules = [module_receipt(r, catalog) for r in (*changed["attempts"], *raw["internal_module_requests"])]
    selections = []
    scopes = {s.source_id: s for s in catalog.scopes}
    for sample in adapters["samples"]:
        selections.append(se.SourceSampleSelection(candidate(sample["candidate"]), sample["depth"], sample["version"], sample["selection"],
            sample["repository"], sample["revision"], sample["path"], sample["sha256"]))
        file = next(f for f in catalog.files if (scopes[f.source_id].repository, scopes[f.source_id].revision, f.path) == (sample["repository"], sample["revision"], sample["path"]))
        modules.append(se.ModuleSourceReceipt(se.ModuleSourceRequest(sample["metadata"]["package"], sample["version"], sample["candidate"]["imported_module"], "constraint_sample", None),
            "module_examined", None, sample["repository"], sample["revision"], sample["path"], sample["sha256"], len(file.content.encode()),
            sample["association_basis"], sample["provenance_state"], (), metadata(sample["metadata"]), tuple(gap(g) for g in sample["gaps"]), None, (),
            ("full_association_observations_not_retained", "full_tag_observations_not_retained", "tag_commit_summary_not_retained")))
    transport = value.get("transport")
    if transport is not None:
        limits = dict(transport["limits"])
        limits["elapsed_seconds"] = MeasuredDuration.from_seconds(float(limits["elapsed_seconds"]), "acquisition_limit_seconds")
        retry = transport.get("retry_policy")
        if retry is not None:
            assert retry == dict(host="pypi.org", method="GET", max_retries_per_request=1, max_retries_per_acquisition=2, eligible_failure="timeout_before_response", shared_limits_unchanged=True)
        transport = se.SourceTransportReceipt(se.SourceAcquisitionLimits(**limits), transport["auth"], transport["github_requests"], transport["provider_requests"], transport["decoded_body_bytes"],
            MeasuredDuration.from_seconds(float(transport["elapsed_seconds"]), "historical_acquisition_elapsed_seconds"), transport["deadline_kind"],
            tuple(se.SourceAcquisitionStop(**s) for s in transport["stops"]), tuple(se.SourceRequestEvent(**e) for e in transport["requests"]),
            "pypi-get-timeout-once/1" if retry is not None else "none", tuple(se.SourceRetryDecision(**r) for r in transport.get("retry_decisions", ())))
    work = raw.get("source_work")
    if work is not None:
        work = se.SourceAcquisitionWork(tuple(tuple(r) for r in work["release_identities"]), work["module_attempts"], work["source_bytes"])
    omissions = tuple(se.SourceMaterialOmission(**dict(m, role=ROLE[m["role"]])) for m in raw["material_omissions"])
    return se.SourceAcquisitionReceipt("retained_experiment", "complete", datetime.fromisoformat(value["timestamp"]), target, tuple(modules), tuple(selections),
        tuple(se.SourceProblem(**p) for p in adapters["problems"]), tuple(candidate(c) for c in adapters["omitted_candidates"]),
        tuple(candidate(c) for c in adapters["deferred_to_native_versions"]), tuple(changed["unexamined_modules"]), omissions, tuple(adapters["limitations"]), work, transport,
        tuple(se.SourceMethodFile(k, v) for k, v in value["code_sha256"].items()),
        ("full_original_acquisition_observations_not_retained", "native_prefix_context_types_not_reconstructed_in_this_retained_fixture"))


rows = read(EVIDENCE / "2026-11-01-analysis-capacity-and-work-admission/retained-qualification-results.json")
cases = [(r["case"], Path(r["directory"]), r["output_sha256"]) for r in rows]
digimon = EVIDENCE / "2026-11-01-untouched-partial-analysis-qualification/ordinary-digimon-scraper-pr-16"
private = Path(read(digimon / "contract.json")["private_retention"]["root"])
hashes = read(digimon / "verification.json")["artifact_hashes"]
cases.append(("digimon", private / "comparison", {n.removeprefix("comparison/"): h for n, h in hashes.items() if n.startswith("comparison/")}))
results = []
for name, directory, hashes in cases:
    assert hashes == {n: sha256((directory / n).read_bytes()).hexdigest() for n in hashes}
    body, catalog = ordinary.open_ordinary_comparison(directory)
    if "ordinary_acquisition" not in body["acquisition"] or "native_inputs" not in body["acquisition"]:
        results.append(dict(case=name, outcome="not_admitted_to_source_family",
            reason="original_selected_catalog_has_no_ordinary_acquisition_receipts_or_native_prefix",
            original_hashes=hashes, analysis_worker_qualification="separately passed in preceding result/worker cycle",
            no_fabricated_receipts=True))
        (HERE / "retained-family-results.json").write_text(json.dumps(results, indent=2) + "\n")
        print(name, "NOT ADMITTED: original selected catalog lacks ordinary acquisition receipts", flush=True)
        continue
    modules = tuple(PythonSourceModule(**dict(m, role=ROLE[m["role"]], dependencies=tuple(m["dependencies"]))) for m in body["modules"])
    source = se.CallerSignatureSources(catalog, modules, AnalysisLimits(**body["limits"]), receipt(body["acquisition"], catalog))
    source_payload = encode_sources(source)
    native = body["acquisition"]["native_inputs"]
    dependency = DependencyVersionChange(**dict(native["dependency"], source_evidence=tuple(DependencyChangeSourceEvidence(**e) for e in native["dependency"]["source_evidence"]), limitations=tuple(native["dependency"]["limitations"])))
    capture = NativeInvestigationCapture()
    capture.start(PullRequestIdentity(**native["identity"]), tuple(ChangedFile(**f) for f in native["changed_files"]), dependency, ())
    with tempfile.TemporaryDirectory(prefix="upgradepilot-native-family-retained-") as tmp:
        store = CheckpointStore.create(Path(tmp) / "store", schema_version=2)
        host = InvestigationWorkspaceHost(store=store, lineage_id="retained-qualification")
        host.initialize(capture.partial_snapshot())
        capture.capture_caller_signature_sources(source)
        host.publish_native_progress(capture.partial_snapshot())
        source_revision = host.current.revision_id
        run = run_source_analysis(source.analysis_input())
        assert run.state == "completed", (name, run.reason, run.problem_detail)
        capture.capture_caller_signature_comparison(run)
        host.publish_native_progress(capture.partial_snapshot())
        selected = store.read_revision(host.lineage_id, host.current.revision_id, expected_target=catalog.target)
        with ExitStack() as stack:
            for hook in ("ast.parse", "requests.sessions.Session.request", "socket.socket.connect", "upgradepilot.caller_signature.worker.run_source_analysis", "upgradepilot.caller_signature.worker.produce_source_analysis", "upgradepilot.caller_signature.analysis.compare_arguments"):
                stack.enter_context(patch(hook, side_effect=AssertionError("No recovery producer")))
            restored = reconstruct_caller_signature_projection(selected.revision.boundary, expected_target=catalog.target)
            assert restored.comparison == run
            assert restored.sources.acquisition == source.acquisition
            assert restored.sources.catalog.files == source.catalog.files
        comparison = next(r for r in selected.revision.boundary.records if r.family == "caller_signature_comparison")
        selection = dict(target=asdict(catalog.target), revisions=[source_revision, selected.revision.revision_id])
        cold = subprocess.run([sys.executable, str(HERE / "cold_open.py"), str(store.directory), json.dumps(selection)], capture_output=True, text=True, timeout=60)
        assert cold.returncode == 0, cold.stderr
        opened = json.loads(cold.stdout)
        assert opened[0]["state"] is None and opened[1]["state"] == "completed"
        assert opened[1]["comparison_sha256"] == comparison.payload_digest
        source_record = next(r for r in selected.revision.boundary.records if r.family == "caller_signature_sources")
        assert all(r["source_sha256"] == source_record.payload_digest for r in opened)
        boundary = encode_native_boundary(selected.revision.boundary)
        summary = dict(case=name, outcome="native_family_checkpoint_pass", original_hashes=hashes, facts=run.result.work.facts, comparisons=run.result.work.selected_pairs,
            source_payload_bytes=len(source_payload), source_structure=json_structure_cost(parse_json(source_payload)),
            comparison_payload_bytes=len(comparison.payload), comparison_structure=json_structure_cost(parse_json(comparison.payload)),
            complete_boundary_bytes=len(boundary), checkpoint_digest=selected.revision.digest(),
            source_revision=source_revision, completed_revision=selected.revision.revision_id,
            acquisition_receipt_equal=True, exact_text_equal=True, run_equal=True, producer_free_reconstruction=True,
            unexamined_units=sum(u.coverage == "unexamined" for u in run.result.units),
            historical_origin=restored.sources.acquisition.origin, acquisition_gap=restored.sources.acquisition.retention_gaps,
            elapsed_hex=run.elapsed.seconds_hex, fresh_process_cold_open=opened)
        results.append(summary)
        (HERE / "retained-family-results.json").write_text(json.dumps(results, indent=2) + "\n")
        print(name, "PASS", summary["source_structure"], summary["comparison_structure"], summary["complete_boundary_bytes"], flush=True)
    assert hashes == {n: sha256((directory / n).read_bytes()).hexdigest() for n in hashes}
