"""Ordinary-input source discovery, retained comparisons and offline inspection.

Host entry: ``acquire_ordinary_comparison_inputs(repository, number, ...)`` reuses
the ordinary PR acquisition owner, then closes observed in-repository imports at
the same source run. ``run_ordinary_comparison`` analyzes that frozen input in a
bounded worker. CLI ``open --result DIRECTORY`` renders fixed saved files only.

This increment admits controlled-provider composition and retained component
discovery, not fresh live execution, installed versions or normal product adoption.
No callable selectors/expected answers are inputs. Curated v1 stays separately
readable through api_call_signature_trial; both readers share fact integrity and
source display. These experimental bundles are not Workspace checkpoints.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from dataclasses import asdict
from datetime import UTC, datetime
from pathlib import Path

from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
from upgradepilot.workspace.native_representation import json_bytes, object_fields, parse_json
from upgradepilot.workspace.source_access import (
    RetainedSourceCatalog, RetainedSourceFile, RetainedSourceScope,
    encode_source_catalog, read_source_catalog,
)

from .api_adapter_exploration import PythonModuleSourceRequest
from .api_call_signature import METHOD_VERSION, AnalysisLimit
from .api_signature_evidence import (
    AnalysisLimits, MAX_CATALOG_BYTES, MAX_OUTPUT_BYTES, MAX_SELECTION_BYTES,
    content_digest, render_terminal_lines, read_bounded_bytes, read_source_span,
    read_string_sequence, read_investigation_target, read_bounded_text, write_new_output,
    signature_code_identity, admit_method_source_names, CURATED_HISTORICAL_SOURCES,
    SIGNATURE_SUPPORT_SOURCES, read_comparison_records, render_comparison, render_source,
)
from .api_change_source_acquisition import AcquisitionProblem
from .api_source_correspondence import (
    CORRESPONDENCE_VERSION, MAX_DISCOVERY_DEPTH, MAX_DISCOVERY_GAPS, MAX_PATH_STEPS,
    PythonSourceModule, absolute_import, discover_source_candidates, module_name,
)
from .api_target_context_smoke import (
    ChangedPackageModuleAttempt, acquire_public_pr_context, module_attempt_manifest, trial_manifest,
)

FORMAT = "caller-signature-evidence/2"
INPUT_FORMAT = "ordinary-caller-signature-input/1"
PROOF_CLASSES = {"controlled_ordinary_pr_composition", "retained_component_discovery"}
ORDINARY_METHOD_SOURCES = (
    "experiments/api_source_correspondence.py", "experiments/api_ordinary_call_signature_trial.py",
    "experiments/api_target_context_smoke.py", "experiments/api_adapter_exploration.py",
    "experiments/api_target_context.py", "experiments/api_change_source_acquisition.py",
    "src/upgradepilot/investigation_inputs.py",
)


def ordinary_code_identity():
    root = Path(__file__).resolve().parents[1]
    return {**signature_code_identity(), **{name: content_digest((root / name).read_bytes()) for name in ORDINARY_METHOD_SOURCES}}


def _source_label(role, package, version, file):
    identity = json_bytes([role, package, version, file.repository, file.revision])
    return "source-" + content_digest(identity)[:32]


def prepare_ordinary_inputs(trial, session, source_run):
    """Freeze native observations, source-role receipts and complete admitted text.

    Internal imports only extend an already qualified repository/release. External
    package mapping is not guessed; ordinary acquisition owns its declarations.
    The existing source run controls module/release/text/provider work. Missing or
    ambiguous inventory paths remain explicit problems and never choose an answer.
    """
    from .api_adapter_exploration import ExaminedPythonModule
    from .api_python_bindings import ImportFact

    scopes, files, modules, queue, seen, closure = {}, {}, [], [], set(), []
    omitted_target_files = []
    # Match the analysis worker's existing material ceiling before admitting text.
    limits = AnalysisLimits()
    admitted_bytes = 0

    def add(file, role, package, version, dependencies, examined=None):
        nonlocal admitted_bytes
        source_id = _source_label(role, package, version, file)
        key = (source_id, file.path)
        if key in files:
            return
        size = len(file.content.encode())
        if len(files) >= limits.max_files or admitted_bytes + size > limits.max_source_bytes:
            omitted_target_files.append(dict(repository=file.repository, revision=file.revision,
                                             path=file.path, role=role, reason="analysis_material_limit"))
            return
        scopes[source_id] = RetainedSourceScope(source_id, file.repository, file.revision,
            "repository_text", role + "; declared repository/tag source, not installed artifact",
            "complete admitted files only; acquisition and discovery coverage remain partial")
        files[key] = RetainedSourceFile(source_id, file.path, file.content)
        admitted_bytes += size
        name = module_name(file.path)
        if name or role == "target" and file.path.endswith(".py"):
            modules.append(PythonSourceModule(source_id, file.path, name or "", package, version,
                                               role, tuple(sorted(set(dependencies)))))
            if examined is not None:
                queue.append((examined, role))

    dependency = trial.inputs.dependency
    target_dependencies = tuple(d.package for d in trial.target.declarations)
    # Library source roles are admitted first so a large target inventory cannot
    # discard one old/proposed side from the retained comparison material silently.
    for attempt in trial.changed_sources:
        if isinstance(attempt.outcome, ExaminedPythonModule):
            source = attempt.outcome
            add(source.file, attempt.request.version_basis, source.metadata.package,
                attempt.request.version, (d.package for d in source.metadata.requirements), source)
    for sample in trial.adapters.samples:
        request = PythonModuleSourceRequest(sample.metadata.package, sample.version,
            sample.candidate.imported_module, "constraint_sample")
        examined = source_run.examine(request)  # cache hit; preserves the source owner's qualification
        if isinstance(examined, ExaminedPythonModule):
            add(sample.file, "constraint_sample", sample.metadata.package, sample.version,
                (d.package for d in sample.metadata.requirements), examined)
    for file in trial.target.files:
        add(file, "target", "", "", target_dependencies)
    while queue:
        examined, role = queue.pop(0)
        for fact in examined.imports:
            if not isinstance(fact, ImportFact):
                continue
            current = module_name(examined.file.path)
            imported = absolute_import(current, examined.file.path, fact.module, fact.relative_level)
            if not imported:
                continue
            # Only inventory-supported spellings in this exact qualified repo.
            spellings = [imported]
            if fact.member and fact.member != "*":
                spellings.append(imported + "." + fact.member)
            inventory_names = {module_name(e.path) for e in examined.inventory.entries if e.kind == "blob"}
            for spelling in spellings:
                if spelling not in inventory_names:
                    continue
                key = (examined.request.package, examined.request.version, spelling, role)
                if key in seen:
                    continue
                seen.add(key)
                request = PythonModuleSourceRequest(examined.request.package, examined.request.version,
                                                     spelling, role, fact)
                outcome = source_run.examine(request)
                closure.append(module_attempt_manifest(ChangedPackageModuleAttempt(request, outcome)))
                if isinstance(outcome, ExaminedPythonModule):
                    add(outcome.file, role, outcome.metadata.package, request.version,
                        (d.package for d in outcome.metadata.requirements), outcome)
    identity = trial.identity
    target = ExactInvestigationTarget(identity.repository, identity.number, identity.base_sha,
        identity.head_sha, dependency.normalized_package, dependency.old_version, dependency.proposed_version)
    catalog = RetainedSourceCatalog(tuple(scopes.values()), tuple(files.values()), target=target)
    return catalog, tuple(modules), dict(
        native_inputs=asdict(trial.inputs), ordinary_acquisition=trial_manifest(trial, session),
        internal_module_requests=closure, source_work=asdict(source_run.work),
        material_omissions=omitted_target_files,
        retention="complete admitted files; explicit omitted material; not all target or release-window text",
    )


def encode_ordinary_inputs(catalog, modules, acquisition, *, proof_class):
    """Host-bound proof label; retained data is never promoted to fresh product proof."""
    if proof_class not in PROOF_CLASSES:
        raise ValueError("Fresh live/product proof is not admitted by this increment.")
    def observation_value(value):
        if isinstance(value, datetime):
            return value.isoformat()
        raise TypeError("Unsupported observation value: " + type(value).__name__)
    acquisition = json.loads(json.dumps(acquisition, default=observation_value))
    return json_bytes(dict(format=INPUT_FORMAT, proof_class=proof_class,
        catalog=parse_json(encode_source_catalog(catalog)), modules=[asdict(m) for m in modules],
        acquisition=acquisition))


def acquire_ordinary_comparison_inputs(repository, number, *, session, adapters, **providers):
    """Ordinary repo/PR entry, exercised with controlled providers in this increment.

    Callers supply provider configuration and optional revision guards, never
    target file paths, callable pairs, source versions or expected outcomes.
    Fresh live use awaits the separately selected allocation/execution contract.
    """
    source_run = adapters.source_run()
    trial = acquire_public_pr_context(repository, number, session=session, adapters=adapters,
                                      source_run=source_run, **providers)
    if isinstance(trial, AcquisitionProblem):
        return trial
    return prepare_ordinary_inputs(trial, session, source_run)


def _read_modules(raw, catalog):
    if type(raw) is not list or not 1 <= len(raw) <= 32:
        raise ValueError("Unsupported module sequence.")
    files = {(f.source_id, f.path): f for f in catalog.files}
    seen, modules = set(), []
    roles = {"target", "native_old_version", "native_proposed_version", "constraint_sample"}
    for item in raw:
        data = object_fields(item, ("source_id", "path", "module", "package", "version", "role", "dependencies"))
        key = (data["source_id"], data["path"])
        expected_module = module_name(data["path"]) or ""
        if (key not in files or key in seen or data["module"] != expected_module
            or not expected_module and not (data["role"] == "target" and data["path"].endswith(".py"))):
            raise ValueError("Module/source closure mismatch.")
        seen.add(key)
        if data["role"] not in roles:
            raise ValueError("Unsupported source role.")
        for field in ("module", "package", "version"):
            read_bounded_text(data[field])
        scope = next(s for s in catalog.scopes if s.source_id == key[0])
        if data["role"] == "target" and (scope.repository, scope.revision) != (catalog.target.repository, catalog.target.head_sha):
            raise ValueError("Target source revision mismatch.")
        if data["role"] in {"native_old_version", "native_proposed_version"}:
            expected = catalog.target.old_version if data["role"] == "native_old_version" else catalog.target.proposed_version
            if (data["package"], data["version"]) != (catalog.target.normalized_package, expected):
                raise ValueError("Native source role/transition mismatch.")
        data["dependencies"] = read_string_sequence(data["dependencies"], maximum=256)
        modules.append(PythonSourceModule(**data))
    if seen != {key for key in files if key[1].endswith(".py")}:
        raise ValueError("Unclassified Python source.")
    return tuple(modules)


def prepare_ordinary_comparison(input_data, limits):
    raw = object_fields(parse_json(input_data), ("format", "proof_class", "catalog", "modules", "acquisition"))
    if raw["format"] != INPUT_FORMAT or raw["proof_class"] not in PROOF_CLASSES:
        raise ValueError("Unsupported ordinary input/proof.")
    source_data = json_bytes(raw["catalog"])
    catalog = read_source_catalog(source_data, expected_target=read_investigation_target(raw["catalog"]["target"]))
    if catalog.target is None or catalog.target.normalized_package is None:
        raise ValueError("Ordinary discovery needs a native transition.")
    modules = _read_modules(raw["modules"], catalog)
    if len(catalog.files) > limits.max_files:
        raise AnalysisLimit("selected_file_limit")
    discovery, pairs, units = discover_source_candidates(catalog, modules, limits)
    by_key = {(u["descriptor"]["source_id"], u["descriptor"]["path"]) for u in units}
    units.extend(dict(descriptor=catalog.descriptor(f), coverage="complete_file", facts=None)
                 for f in catalog.files if (f.source_id, f.path) not in by_key)
    companion = encode_source_catalog(catalog)
    body = dict(format=FORMAT, method_version=METHOD_VERSION, proof_class=raw["proof_class"],
        target=asdict(catalog.target), runtime=sys.version.split()[0], code_sha256=ordinary_code_identity(),
        limits=asdict(limits), inputs=dict(catalog_sha256=content_digest(source_data), catalog_id=catalog.identity,
                                        discovery_input_sha256=content_digest(input_data)),
        companion_sha256=content_digest(companion), companion_id=catalog.identity,
        files=units, pairs=pairs,
        work=dict(source_files=len(catalog.files), source_bytes=sum(len(f.content.encode()) for f in catalog.files),
                  ast_nodes=sum(u["facts"]["ast_nodes"] for u in units if u["facts"]),
                  facts=sum(len(u["facts"]["calls"]) + len(u["facts"]["signatures"]) for u in units if u["facts"]),
                  selected_pairs=len(pairs)), coverage=discovery["coverage"],
        correspondence_version=CORRESPONDENCE_VERSION, modules=raw["modules"], discovery=discovery,
        acquisition=raw["acquisition"])
    result = json_bytes(body)
    if max(len(result), len(companion)) > MAX_OUTPUT_BYTES:
        raise AnalysisLimit("serialized_output_capacity")
    return result, companion


def read_ordinary_comparison(result, companion):
    if max(len(result), len(companion)) > MAX_OUTPUT_BYTES:
        raise AnalysisLimit("saved_output_capacity")
    body = object_fields(parse_json(result), (
        "format", "method_version", "proof_class", "target", "runtime", "code_sha256", "limits", "inputs",
        "companion_sha256", "companion_id", "files", "pairs", "work", "coverage",
        "correspondence_version", "modules", "discovery", "acquisition",
    ))
    if (body["format"] != FORMAT or type(body["method_version"]) is not int or body["method_version"] != METHOD_VERSION
        or type(body["correspondence_version"]) is not int or body["correspondence_version"] not in {1, CORRESPONDENCE_VERSION}
        or body["proof_class"] not in PROOF_CLASSES):
        raise ValueError("Unsupported ordinary format/method/proof.")
    source_names = admit_method_source_names(body["code_sha256"],
        current=(*SIGNATURE_SUPPORT_SOURCES, *ORDINARY_METHOD_SOURCES),
        historical=((*CURATED_HISTORICAL_SOURCES, *ORDINARY_METHOD_SOURCES),))
    body, catalog = read_comparison_records(body, companion, method_sources=source_names,
                                            allow_empty_pairs=True, input_digest_field="discovery_input_sha256")
    if (type(body["discovery"]) is not dict or body["inputs"]["catalog_id"] != catalog.identity
        or body["inputs"]["catalog_sha256"] != body["companion_sha256"]
        or body["coverage"] != body["discovery"].get("coverage")):
        raise ValueError("Ordinary material/coverage closure mismatch.")
    modules = _read_modules(body["modules"], catalog)
    _validate_discovery(body, catalog, modules)
    _validate_acquisition(body["acquisition"])
    if body["proof_class"] == "controlled_ordinary_pr_composition":
        from upgradepilot.github.pull_request import PullRequestDescriptionObservation
        native = body["acquisition"].get("native_inputs")
        if type(native) is not dict or type(native.get("identity")) is not dict or type(native.get("dependency")) is not dict:
            raise ValueError("Missing initial native observation.")
        identity, dependency = native["identity"], native["dependency"]
        for source, fields in ((identity, {"repository": "repository", "number": "pull_number", "base_sha": "base_sha", "head_sha": "head_sha"}),
                               (dependency, {"normalized_package": "normalized_package", "old_version": "old_version", "proposed_version": "proposed_version"})):
            if any(source.get(field) != body["target"][target_field] for field, target_field in fields.items()):
                raise ValueError("Initial observation/target mismatch.")
        description = object_fields(native.get("description"), ("state", "text", "source_url", "observed_at", "content_sha256", "utf8_bytes"))
        description["observed_at"] = datetime.fromisoformat(description["observed_at"])
        PullRequestDescriptionObservation(**description)
    return body, catalog


def _validate_acquisition(acquisition):
    """Admit the receipt fields consumed by the saved view; do not rerun providers."""
    if type(acquisition) is not dict:
        raise ValueError("Invalid acquisition receipt.")
    ordinary = acquisition.get("ordinary_acquisition", {})
    if type(ordinary) is not dict:
        raise ValueError("Invalid ordinary acquisition receipt.")
    target, changed, adapters = (ordinary.get(field, {}) for field in ("target", "changed_package_sources", "adapters"))
    if any(type(item) is not dict for item in (target, changed, adapters)):
        raise ValueError("Invalid acquisition coverage record.")
    read_string_sequence(target.get("omitted_paths", []), maximum=20_000)
    read_string_sequence(changed.get("unexamined_modules", []), maximum=20_000)
    for attempts in (acquisition.get("internal_module_requests", []), changed.get("attempts", [])):
        if type(attempts) is not list or len(attempts) > 256:
            raise ValueError("Invalid source attempt receipt.")
        for attempt in attempts:
            if type(attempt) is not dict or attempt.get("state") not in {"module_examined", "refused", "unavailable"}:
                raise ValueError("Invalid source attempt state.")
            if type(attempt.get("request")) is not dict:
                raise ValueError("Invalid source request receipt.")
            for field in ("package", "version", "module"):
                read_bounded_text(attempt["request"].get(field))
            if attempt["state"] != "module_examined":
                for field in ("stage", "reason", "detail"):
                    read_bounded_text(attempt.get(field), maximum=16_384)
    omissions = acquisition.get("material_omissions", [])
    if type(omissions) is not list or len(omissions) > 20_000:
        raise ValueError("Invalid material omissions.")
    for omission in omissions:
        item = object_fields(omission, ("repository", "revision", "path", "role", "reason"))
        for value in item.values():
            read_bounded_text(value)
    problems = adapters.get("problems", [])
    if type(problems) is not list or len(problems) > 256:
        raise ValueError("Invalid adapter problems.")
    for problem in problems:
        item = object_fields(problem, ("stage", "reason", "detail"))
        for value in item.values():
            read_bounded_text(value, maximum=16_384)


def _validate_discovery(body, catalog, modules):
    """Validate historical path/fact/source closure, never recompute relationships."""
    discovery = object_fields(body["discovery"], ("candidates", "gaps", "gaps_omitted", "states_examined",
                                                "max_depth", "max_path_steps", "coverage"))
    if (type(discovery["max_depth"]) is not int or not 1 <= discovery["max_depth"] <= MAX_DISCOVERY_DEPTH
        or type(discovery["max_path_steps"]) is not int or not 1 <= discovery["max_path_steps"] <= MAX_PATH_STEPS):
        raise ValueError("Invalid discovery limits.")
    for field in ("gaps_omitted", "states_examined"):
        if type(discovery[field]) is not int or discovery[field] < 0:
            raise ValueError("Invalid discovery work.")
    read_bounded_text(discovery["coverage"])
    units = {u["descriptor"]["file_id"]: u for u in body["files"]}
    texts = {catalog.descriptor(f)["file_id"]: f.content for f in catalog.files}
    facts = {f["fact_id"]: f for u in units.values() if u["facts"]
             for field in ("calls", "signatures") for f in u["facts"][field]}
    module_by_key = {(m.source_id, m.path): asdict(m) for m in modules}
    if type(discovery["candidates"]) is not list or len(discovery["candidates"]) != len(body["pairs"]):
        raise ValueError("Candidate/comparison closure mismatch.")
    step_operations = {"call", "import_origin", "reexport", "declaration", "class_declaration", "initializer", "declared_base"}
    if body["correspondence_version"] == 2:
        step_operations |= {"allocation", "attribute_getter", "factory_return", "call_protocol"}
    for candidate, pair in zip(discovery["candidates"], body["pairs"]):
        c = object_fields(candidate, ("id", "root_call_id", "call_id", "signature_id", "receiver_mode",
                                      "steps", "premises", "callee_role"))
        comparison = pair["comparison"]
        if (comparison is None or c["id"] != pair["selection"]["id"]
            or any(c[k] != comparison[k] for k in ("call_id", "signature_id", "receiver_mode"))):
            raise ValueError("Candidate/comparison identity mismatch.")
        root = facts.get(c["root_call_id"])
        if root is None or "expression" not in root:
            raise ValueError("Missing target root call.")
        root_descriptor = units[root["unit_id"]]["descriptor"]
        if module_by_key[(root_descriptor["source_id"], root_descriptor["path"])]["role"] != "target":
            raise ValueError("Foreign root call.")
        callee = facts[c["signature_id"]]
        d = units[callee["unit_id"]]["descriptor"]
        if json_bytes(c["callee_role"]) != json_bytes(module_by_key[(d["source_id"], d["path"])]):
            raise ValueError("Candidate source role mismatch.")
        read_string_sequence(c["premises"], maximum=256)
        if type(c["steps"]) is not list or not 1 <= len(c["steps"]) <= discovery["max_path_steps"]:
            raise ValueError("Invalid source path capacity.")
        for step in c["steps"]:
            s = object_fields(step, ("unit_id", "span", "operation", "expression"))
            if s["unit_id"] not in texts or s["operation"] not in step_operations:
                raise ValueError("Foreign source path step.")
            read_source_span(s["span"], texts[s["unit_id"]])
            read_bounded_text(s["expression"], maximum=4 * 1024 * 1024)
            span = s["span"]
            lines = [line.encode() for line in texts[s["unit_id"]].split("\n")]
            selected = lines[span["line"] - 1:span["end_line"]]
            selected[-1] = selected[-1][:span["end_column"]]
            selected[0] = selected[0][span["column"]:]
            if b"\n".join(selected).decode() != s["expression"]:
                raise ValueError("Source path text/span mismatch.")
        first, last = c["steps"][0], c["steps"][-1]
        if (first["operation"] != "call" or first["unit_id"] != root["unit_id"] or first["span"] != root["span"]
            or last["unit_id"] != callee["unit_id"] or last["span"] != callee["span"]):
            raise ValueError("Source path endpoint mismatch.")
        operations = [s["operation"] for s in c["steps"]]
        if "allocation" in operations or "factory_return" in operations:
            required = ("allocation", "attribute_getter", "factory_return", "call_protocol")
            position = -1
            for operation in required:
                try:
                    position = operations.index(operation, position + 1)
                except ValueError as exc:
                    raise ValueError("Incomplete or unordered factory source path.") from exc
            if not {"module_allocation_binding_and_constructor_success_not_established",
                    "attribute_lookup_and_getattr_activation_not_established",
                    "factory_returns_selected_declared_class_instance"}.issubset(c["premises"]):
                raise ValueError("Missing factory source premises.")
    if type(discovery["gaps"]) is not list or len(discovery["gaps"]) > MAX_DISCOVERY_GAPS:
        raise ValueError("Invalid discovery gaps.")
    for gap in discovery["gaps"]:
        g = object_fields(gap, ("reason", "unit_id", "span", "detail"))
        if g["unit_id"] not in texts:
            raise ValueError("Foreign gap source.")
        read_bounded_text(g["reason"])
        read_bounded_text(g["detail"])
        if g["span"] is not None:
            read_source_span(g["span"], texts[g["unit_id"]])


def render_ordinary_comparison(body):
    lines = [*render_comparison(body).split("\n"), "", "DISCOVERED SOURCE PATHS (conditional, not runtime dispatch)"]
    descriptors = {u["descriptor"]["file_id"]: u["descriptor"] for u in body["files"]}
    signatures = {s["fact_id"]: s for unit in body["files"] if unit["facts"]
                  for s in unit["facts"]["signatures"]}
    for candidate in body["discovery"]["candidates"]:
        role = candidate["callee_role"]
        lines.append("CANDIDATE " + candidate["id"] + " | " + role["role"] + " " + role["version"])
        signature = signatures[candidate["signature_id"]]
        lines.append("Declared callable: " + signature["qualified_name"])
        lines.append("Declared decorators (syntax only): " + (", ".join(signature["decorators"]) or "(none)"))
        for step in candidate["steps"]:
            source = descriptors[step["unit_id"]]
            lines.append(step["operation"] + " " + source["repository"] + "@" + source["revision"]
                         + " " + source["path"] + ":" + str(step["span"]["line"]) + " (unit " + step["unit_id"] + ")")
        lines.extend("Path premise: " + p for p in candidate["premises"])
    for gap in body["discovery"]["gaps"]:
        lines.append("Discovery gap: " + gap["reason"] + " | " + gap["unit_id"] + " | " + gap["detail"])
    lines.append("Additional gap records omitted: " + str(body["discovery"]["gaps_omitted"]))
    acquisition = body["acquisition"]
    ordinary = acquisition.get("ordinary_acquisition", {})
    for item in acquisition.get("material_omissions", ()):
        lines.append("Material omitted: " + item["role"] + " " + item["path"] + " | " + item["reason"])
    attempts = [*acquisition.get("internal_module_requests", ()),
                *ordinary.get("changed_package_sources", {}).get("attempts", ())]
    for item in attempts:
        if item["state"] != "module_examined":
            request = item["request"]
            lines.append("Source " + item["state"] + ": " + request["package"] + " " + request["version"]
                         + " " + request["module"] + " | " + item["stage"] + "/" + item["reason"])
    target = ordinary.get("target", {})
    for path in target.get("omitted_paths", ()):
        lines.append("Target source unexamined: " + path)
    for name in ordinary.get("changed_package_sources", {}).get("unexamined_modules", ()):
        lines.append("Changed-package module unexamined: " + name)
    for problem in ordinary.get("adapters", {}).get("problems", ()):
        lines.append("Adapter source unavailable: " + problem["stage"] + "/" + problem["reason"] + " | " + problem["detail"])
    lines.append("No candidates does not establish no exposure. Next evidence: resolve the displayed path/version/coverage premises.")
    return render_terminal_lines(lines)


def _worker(input_path, directory, limits):
    import resource
    resource.setrlimit(resource.RLIMIT_AS, (limits.memory_bytes, limits.memory_bytes))
    result, companion = prepare_ordinary_comparison(read_bounded_bytes(input_path, MAX_CATALOG_BYTES), limits)
    write_new_output(directory / "_worker-result.json", result)
    write_new_output(directory / "_worker-sources.json", companion)


def run_ordinary_comparison(input_data, directory, *, limits=None):
    """Analyze one immutable prepared capture; no acquisition occurs in this worker."""
    limits = limits or AnalysisLimits()
    directory.mkdir(mode=0o700)
    start = time.monotonic()
    attempt = dict(format="ordinary-caller-signature-attempt/1", state="started", reason=None,
        started_at=datetime.now(UTC).isoformat(), elapsed_seconds=None, input_sha256=content_digest(input_data),
        code_sha256=ordinary_code_identity(), limits=asdict(limits),
        result_sha256=None, companion_sha256=None, worker_returncode=None)
    write_new_output(directory / "attempt-started.json", json_bytes(attempt))
    try:
        if len(input_data) > MAX_CATALOG_BYTES:
            raise AnalysisLimit("encoded_input_or_output_capacity")
        write_new_output(directory / "input.json", input_data)
        completed = subprocess.run([sys.executable, "-m", "experiments.api_ordinary_call_signature_trial", "_worker",
            str((directory / "input.json").resolve()), str(directory.resolve()), json.dumps(asdict(limits))],
            stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, timeout=limits.timeout_seconds, check=False)
        attempt["worker_returncode"] = completed.returncode
        if completed.returncode:
            raise ValueError("bounded_worker_failed: " + completed.stderr.decode(errors="replace")[:2000])
        result = read_bounded_bytes(directory / "_worker-result.json", MAX_OUTPUT_BYTES)
        companion = read_bounded_bytes(directory / "_worker-sources.json", MAX_OUTPUT_BYTES)
        body, _ = read_ordinary_comparison(result, companion)
        if (body["inputs"]["discovery_input_sha256"] != attempt["input_sha256"]
            or body["code_sha256"] != attempt["code_sha256"] or ordinary_code_identity() != attempt["code_sha256"]):
            raise ValueError("Inputs or method changed across attempt.")
        view = (render_ordinary_comparison(body) + "\n").encode()
        if time.monotonic() - start >= limits.timeout_seconds:
            raise subprocess.TimeoutExpired("ordinary admission", limits.timeout_seconds)
        (directory / "_worker-result.json").rename(directory / "result.json")
        (directory / "_worker-sources.json").rename(directory / "sources.json")
        write_new_output(directory / "view.txt", view)
        attempt.update(state="completed", result_sha256=content_digest(result), companion_sha256=content_digest(companion))
    except subprocess.TimeoutExpired:
        attempt.update(state="timed_out", reason="bounded_worker_deadline; no completed comparison admitted")
    except KeyboardInterrupt:
        attempt.update(state="interrupted", reason="caller_interrupt; no completed comparison admitted")
    except (OSError, ValueError, TypeError, MemoryError) as exc:
        attempt.update(state="failed", reason=type(exc).__name__ + ": " + str(exc)[:2000])
    attempt["elapsed_seconds"] = time.monotonic() - start
    write_new_output(directory / "attempt.json", json_bytes(attempt))
    return attempt


def open_ordinary_comparison(directory):
    attempt = parse_json(read_bounded_bytes(directory / "attempt.json", MAX_SELECTION_BYTES))
    if (type(attempt) is not dict or attempt.get("format") != "ordinary-caller-signature-attempt/1"
        or attempt.get("state") != "completed"):
        raise ValueError("Ordinary attempt is not completed.")
    result = read_bounded_bytes(directory / "result.json", MAX_OUTPUT_BYTES)
    companion = read_bounded_bytes(directory / "sources.json", MAX_OUTPUT_BYTES)
    if attempt.get("result_sha256") != content_digest(result) or attempt.get("companion_sha256") != content_digest(companion):
        raise ValueError("Saved attempt/output digest mismatch.")
    body, catalog = read_ordinary_comparison(result, companion)
    if (body["inputs"]["discovery_input_sha256"] != attempt.get("input_sha256")
        or body["code_sha256"] != attempt.get("code_sha256") or body["limits"] != attempt.get("limits")):
        raise ValueError("Attempt/provenance binding mismatch.")
    return body, catalog


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    opened = commands.add_parser("open", help="Inspect ordinary saved evidence offline.")
    opened.add_argument("--result", required=True, type=Path)
    opened.add_argument("--source")
    opened.add_argument("--start-line", type=int, default=1)
    opened.add_argument("--line-count", type=int, default=40)
    worker = commands.add_parser("_worker", help=argparse.SUPPRESS)
    worker.add_argument("input_path", type=Path)
    worker.add_argument("directory", type=Path)
    worker.add_argument("limits")
    args = parser.parse_args(argv)
    try:
        if args.command == "_worker":
            _worker(args.input_path, args.directory, AnalysisLimits(**json.loads(args.limits)))
        else:
            body, catalog = open_ordinary_comparison(args.result)
            print(render_source(catalog, args.source, args.start_line, args.line_count)
                  if args.source else render_ordinary_comparison(body))
    except (OSError, ValueError, TypeError, MemoryError, ImportError) as exc:
        print(render_terminal_lines([type(exc).__name__ + ": " + str(exc)[:2000]]), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
