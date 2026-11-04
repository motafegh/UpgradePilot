"""Fixed retained-summary adaptation for this dated qualification.

The pure receipt converters below are carried forward from November2's qualified
adapter. No original executable is imported: that script writes evidence at top
level. This adapter preserves missing-observation gaps and never acquires data.
"""
from dataclasses import dataclass, replace
from datetime import datetime
from hashlib import sha256
import json
from pathlib import Path

from experiments import api_ordinary_call_signature_trial as ordinary
from upgradepilot.caller_signature import source_evidence as se
from upgradepilot.caller_signature.bindings import BindingAssessment, BindingTraceStep, ImportFact, ReferenceFact
from upgradepilot.caller_signature.correspondence import PythonSourceModule
from upgradepilot.caller_signature.evidence import AnalysisLimits, MeasuredDuration
from upgradepilot.dependency.change import DependencyChangeSourceEvidence, DependencyVersionChange
from upgradepilot.dependency.environment import RequirementsFileDependencyContext
from upgradepilot.github.pull_request import PullRequestIdentity, ChangedFile, PullRequestDescriptionObservation
from upgradepilot.investigation_inputs import AcquiredDependencyInputs

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


@dataclass(frozen=True)
class RetainedCase:
    name: str
    directory: Path
    hashes: dict[str, str]
    body: dict
    catalog: object

    def verify_originals(self):
        assert self.hashes == {n: sha256((self.directory / n).read_bytes()).hexdigest() for n in self.hashes}, self.name

    def native_sources(self):
        raw = self.body["acquisition"]
        if "ordinary_acquisition" not in raw or "native_inputs" not in raw:
            return None
        acquisition = receipt(raw, self.catalog)
        acquisition = replace(acquisition, retention_gaps=(
            "full_original_acquisition_observations_not_retained",
            "prefix_context_reconstructed_from_retained_summary_not_original_response",
        ))
        modules = tuple(PythonSourceModule(**dict(m, role=ROLE[m["role"]], dependencies=tuple(m["dependencies"]))) for m in self.body["modules"])
        return se.CallerSignatureSources(self.catalog, modules, AnalysisLimits(**self.body["limits"]), acquisition)

    def input_observation(self):
        raw = self.body["acquisition"]["native_inputs"]
        dependency = DependencyVersionChange(**dict(raw["dependency"],
            source_evidence=tuple(DependencyChangeSourceEvidence(**s) for s in raw["dependency"]["source_evidence"]),
            limitations=tuple(raw["dependency"]["limitations"])))
        contexts = []
        for item in raw["source_contexts"]:
            source = DependencyChangeSourceEvidence(**item["source_evidence"])
            if source.file_format != "exact_requirement":
                raise ValueError("This retained fixture only admits the selected requirements contexts.")
            contexts.append(RequirementsFileDependencyContext(**dict(item, source_evidence=source)))
        description = dict(raw["description"])
        if isinstance(description["observed_at"], str):
            description["observed_at"] = datetime.fromisoformat(description["observed_at"])
        return AcquiredDependencyInputs(PullRequestIdentity(**raw["identity"]),
            tuple(ChangedFile(**f) for f in raw["changed_files"]), dependency, tuple(contexts),
            PullRequestDescriptionObservation(**description))


def selected_cases(root: Path):
    """Frozen cohort selected by the plan's contrasting pressures, not new outcome screening."""
    evidence = root / "working-memory/evidence"
    rows = read(evidence / "2026-11-01-analysis-capacity-and-work-admission/retained-qualification-results.json")
    locations = [(r["case"], Path(r["directory"]), r["output_sha256"]) for r in rows]
    digimon = evidence / "2026-11-01-untouched-partial-analysis-qualification/ordinary-digimon-scraper-pr-16"
    private = Path(read(digimon / "contract.json")["private_retention"]["root"])
    hashes = read(digimon / "verification.json")["artifact_hashes"]
    locations.append(("digimon", private / "comparison", {n.removeprefix("comparison/"): h for n, h in hashes.items() if n.startswith("comparison/")}))
    cases = []
    for name, directory, hashes in locations:
        actual = {n: sha256((directory / n).read_bytes()).hexdigest() for n in hashes}
        assert actual == hashes, name
        body, catalog = ordinary.open_ordinary_comparison(directory)
        cases.append(RetainedCase(name, directory, hashes, body, catalog))
    return tuple(cases)
