"""Ordinary-input source discovery, retained comparisons and offline inspection.

Host entry: ``acquire_ordinary_comparison_inputs(repository, number, ...)`` reuses
the ordinary PR acquisition owner, then closes observed in-repository imports at
the same source run. ``run_ordinary_comparison`` analyzes that frozen input in a
bounded worker. CLI ``open --result DIRECTORY`` renders fixed saved files only.

``run_fresh_ordinary_pr_attempt`` surrounds acquisition with an immutable outer
attempt, then delegates to the unchanged bounded analysis worker. Its contract
and executable freeze must be admitted before credential/provider work. Controlled
qualification is labelled separately; a fresh label never proves installation,
runtime dispatch, compatibility or normal product adoption.
No callable selectors/expected answers are inputs. Curated v1 stays separately
readable through api_call_signature_trial; both readers share fact integrity and
source display. These experimental bundles are not Workspace checkpoints.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import stat
import subprocess
import sys
import time
import uuid
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
from .api_change_source_acquisition import AcquisitionProblem, TrialAcquisitionPolicy, TrialPublicSession
from upgradepilot.github.api import GitHubAcquisitionError
from .api_source_correspondence import (
    CORRESPONDENCE_VERSION, MAX_DISCOVERY_DEPTH, MAX_DISCOVERY_GAPS, MAX_PATH_STEPS,
    PythonSourceModule, absolute_import, discover_source_candidates, module_name,
)
from .api_target_context_smoke import (
    ChangedPackageModuleAttempt, acquire_public_pr_context, module_attempt_manifest, trial_manifest,
)

FORMAT = "caller-signature-evidence/2"
INPUT_FORMAT = "ordinary-caller-signature-input/1"
FRESH_PROOF = "fresh_ordinary_pr_acquisition"
PROOF_CLASSES = {"controlled_ordinary_pr_composition", "retained_component_discovery", FRESH_PROOF}
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
    pending = []
    interest = set()
    for reference in trial.target.references:
        origins = reference.binding.possible_imports if reference.binding else (reference.lexical_import,)
        for origin in origins:
            if origin:
                interest.update(origin.split("."))
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
    def schedule(examined, role):
        called = {r.expression.split(".")[0] for r in examined.references}
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
                bound = fact.alias or fact.member or fact.module.split(".")[0]
                priority = 0 if bound in interest else 1 if bound in called else 2
                if bound in interest and fact.member:
                    interest.add(fact.member)
                pending.append((priority, len(seen), examined, role, request))

    # This is source-selection order only, never an inferred binding/dispatch edge.
    # Seed both native sides before processing a broad export module's imports.
    with session.stage("source_closure"):
        while queue or pending:
            while queue:
                schedule(*queue.pop(0))
            if not pending:
                break
            pending.sort(key=lambda item: item[:2])
            _, _, parent, role, request = pending.pop(0)
            if len(closure) >= 256:
                omitted_target_files.extend(dict(repository=parent.file.repository, revision=parent.file.revision,
                    path=e.path, role=role, reason="closure_receipt_limit") for e in parent.inventory.entries
                    if module_name(e.path) == request.module)
                continue
            outcome = source_run.examine(request)
            closure.append(module_attempt_manifest(ChangedPackageModuleAttempt(request, outcome)))
            if isinstance(outcome, ExaminedPythonModule):
                add(outcome.file, role, outcome.metadata.package, request.version,
                    (d.package for d in outcome.metadata.requirements), outcome)
    identity = trial.identity
    target = ExactInvestigationTarget(identity.repository, identity.number, identity.base_sha,
        identity.head_sha, dependency.normalized_package, dependency.old_version, dependency.proposed_version)
    catalog = RetainedSourceCatalog(tuple(scopes.values()), tuple(files.values()), target=target)
    session.finish_acquisition()
    return catalog, tuple(modules), dict(
        native_inputs=asdict(trial.inputs), ordinary_acquisition=trial_manifest(trial, session),
        internal_module_requests=closure, source_work=asdict(source_run.work),
        material_omissions=omitted_target_files,
        retention="complete admitted files; explicit omitted material; not all target or release-window text",
    )


def encode_ordinary_inputs(catalog, modules, acquisition, *, proof_class):
    """Host-bound proof label; retained data is never promoted to fresh product proof."""
    if proof_class not in PROOF_CLASSES:
        raise ValueError("Unsupported ordinary acquisition proof class.")
    def observation_value(value):
        if isinstance(value, datetime):
            return value.isoformat()
        raise TypeError("Unsupported observation value: " + type(value).__name__)
    acquisition = json.loads(json.dumps(acquisition, default=observation_value))
    return json_bytes(dict(format=INPUT_FORMAT, proof_class=proof_class,
        catalog=parse_json(encode_source_catalog(catalog)), modules=[asdict(m) for m in modules],
        acquisition=acquisition))


def acquire_ordinary_comparison_inputs(repository, number, *, session, adapters, capture=None, **providers):
    """Ordinary repo/PR entry, exercised with controlled providers in this increment.

    Callers supply provider configuration and optional revision guards, never
    target file paths, callable pairs, source versions or expected outcomes.
    Fresh use belongs to run_fresh_ordinary_pr_attempt, not an unrecorded host call.
    Optional capture preserves completed acquisition stages for that outer owner.
    """
    if session.policy and adapters.session is not session:
        raise ValueError("Staged acquisition requires one shared adapter/transport session.")
    source_run = adapters.source_run()
    if capture is not None:
        source_run = _CapturedSourceRun(source_run, capture)
    trial = acquire_public_pr_context(repository, number, session=session, adapters=adapters,
                                      source_run=source_run, capture=capture, **providers)
    if isinstance(trial, AcquisitionProblem):
        return trial
    try:
        return prepare_ordinary_inputs(trial, session, source_run)
    except GitHubAcquisitionError as exc:
        return AcquisitionProblem("ordinary_acquisition", exc.reason, str(exc), session.acquisition_receipt())


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
    if body["proof_class"] in {"controlled_ordinary_pr_composition", FRESH_PROOF}:
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
    if "transport" in ordinary:
        _validate_transport(ordinary["transport"])
    target, changed = (ordinary.get(field, {}) for field in ("target", "changed_package_sources"))
    adapters = ordinary.get("adapter_exploration", ordinary.get("adapters", {}))
    if any(type(item) is not dict for item in (target, changed, adapters)):
        raise ValueError("Invalid acquisition coverage record.")
    read_string_sequence(target.get("omitted_paths", []), maximum=20_000)
    gaps = target.get("gaps", [])
    if type(gaps) is not list or len(gaps) > 20_000:
        raise ValueError("Invalid target acquisition gaps.")
    for gap in gaps:
        item = object_fields(gap, ("path", "reason", "detail"))
        if item["path"] is not None:
            read_bounded_text(item["path"])
        read_bounded_text(item["reason"])
        read_bounded_text(item["detail"], maximum=16_384)
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

    omitted = adapters.get("omitted_candidates", [])
    if type(omitted) is not list or len(omitted) > 20_000:
        raise ValueError("Invalid omitted adapter candidates.")
    for candidate in omitted:
        if type(candidate) is not dict or type(candidate.get("declaration")) is not dict:
            raise ValueError("Invalid omitted adapter candidate.")
        read_bounded_text(candidate.get("imported_module"))
        read_bounded_text(candidate["declaration"].get("package"))


def _validate_transport(raw):
    """Check saved accounting consistency; no credential/provider/clock access."""
    value = object_fields(raw, ("format", "limits", "auth", "github_requests", "provider_requests",
                                "decoded_body_bytes", "elapsed_seconds", "deadline_kind", "stops", "requests"))
    if value["format"] != "trial-acquisition-policy/1" or value["auth"] not in {"anonymous", "token-env"}:
        raise ValueError("Unsupported transport receipt.")
    policy = TrialAcquisitionPolicy(**object_fields(value["limits"], tuple(TrialAcquisitionPolicy.__dataclass_fields__)))
    for name in ("github_requests", "provider_requests", "decoded_body_bytes"):
        if type(value[name]) is not int or value[name] < 0:
            raise ValueError("Invalid transport work count.")
    elapsed = value["elapsed_seconds"]
    if type(elapsed) not in (int, float) or not 0 <= elapsed <= 86400:
        raise ValueError("Invalid transport elapsed time.")
    if value["deadline_kind"] != "cooperative_monotonic_checks_and_bounded_socket_timeouts":
        raise ValueError("Unsupported acquisition deadline kind.")
    requests = value["requests"]
    if type(requests) is not list or len(requests) != value["provider_requests"] or len(requests) > policy.provider_requests:
        raise ValueError("Transport request count mismatch.")
    github = body = 0
    for index, raw_event in enumerate(requests, 1):
        event = object_fields(raw_event, ("stage", "host", "path", "github_requests", "provider_requests",
                                         "decoded_body_bytes", "status", "state", "reason"))
        if event["host"] not in {"api.github.com", "pypi.org"} or event["state"] not in {"started", "received", "failed"}:
            raise ValueError("Invalid transport request state.")
        github += event["host"] == "api.github.com"
        count = event["decoded_body_bytes"]
        if (type(count) is not int or count < 0 or type(event["github_requests"]) is not int
            or event["github_requests"] != github or type(event["provider_requests"]) is not int
            or event["provider_requests"] != index):
            raise ValueError("Transport event accounting mismatch.")
        body += count
        if event["status"] is not None and (type(event["status"]) is not int or not 100 <= event["status"] <= 599):
            raise ValueError("Invalid transport response status.")
        for name in ("stage", "path"):
            read_bounded_text(event[name], maximum=512)
        if event["reason"] is not None:
            read_bounded_text(event["reason"], maximum=128)
        if event["state"] == "received" and count > policy.response_bytes:
            raise ValueError("Over-limit body labelled received.")
    if github != value["github_requests"] or github > policy.github_requests or body != value["decoded_body_bytes"]:
        raise ValueError("Transport aggregate accounting mismatch.")
    if type(value["stops"]) is not list or len(value["stops"]) > 64:
        raise ValueError("Invalid transport stop records.")
    for stop in value["stops"]:
        for text in object_fields(stop, ("stage", "reason")).values():
            read_bounded_text(text, maximum=128)


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
    protocol_operations = ("allocation", "attribute_getter", "factory_return", "call_protocol")
    step_operations = {"call", "import_origin", "reexport", "declaration", "class_declaration", "initializer", "declared_base"}
    if body["correspondence_version"] == 2:
        step_operations.update(protocol_operations)
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
        # Any protocol residue requires its complete witness. Using only allocation/
        # return as triggers let corrupted paths remove both and bypass admission.
        if any(operation in operations for operation in protocol_operations):
            position = -1
            for operation in protocol_operations:
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
    if "transport" in ordinary:
        transport = ordinary["transport"]
        limits = transport["limits"]
        lines.append("ACQUISITION WORK (local policy, independent of GitHub account quota)")
        lines.append(f"Auth: {transport['auth']}; GitHub requests: {transport['github_requests']}/{limits['github_requests']}; "
                     f"all-provider requests: {transport['provider_requests']}/{limits['provider_requests']}")
        lines.append(f"Decoded response bytes: {transport['decoded_body_bytes']}/{limits['aggregate_bytes']}; "
                     f"acquisition elapsed: {transport['elapsed_seconds']:.3f}/{limits['elapsed_seconds']}s (cooperative deadline)")
        for stop in transport["stops"]:
            lines.append("Acquisition stop: " + stop["stage"] + " | " + stop["reason"])
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
    for gap in target.get("gaps", ()):
        lines.append("Target acquisition gap: " + (gap["path"] or "(inventory/aggregate)")
                     + " | " + gap["reason"] + " | " + gap["detail"])
    for name in ordinary.get("changed_package_sources", {}).get("unexamined_modules", ()):
        lines.append("Changed-package module unexamined: " + name)
    adapters = ordinary.get("adapter_exploration", ordinary.get("adapters", {}))
    for candidate in adapters.get("omitted_candidates", ()):
        lines.append("Adapter candidate unexamined: " + candidate["declaration"]["package"]
                     + " " + candidate["imported_module"])
    for problem in adapters.get("problems", ()):
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


# Outer acquisition lifecycle. The existing worker above remains an independent
# bounded analysis attempt. Nothing in this section executes downloaded code.
class _CapturedSourceRun:
    """Delegate the existing shared run; retain returned material before later work."""

    def __init__(self, run, capture):
        self.run, self.capture = run, capture

    def __getattr__(self, name):
        return getattr(self.run, name)

    def examine(self, request):
        from .api_adapter_exploration import ExaminedPythonModule
        outcome = self.run.examine(request)
        record = module_attempt_manifest(ChangedPackageModuleAttempt(request, outcome))
        if isinstance(outcome, ExaminedPythonModule):
            record["file"] = asdict(outcome.file)
        self.capture("library_source", record)
        return outcome


class _ObservedPullClient:
    """Observe the original native read, including identities rejected by its guard."""

    def __init__(self, client, capture):
        self.client, self.capture = client, capture

    def __getattr__(self, name):
        return getattr(self.client, name)

    def get_pull_request_observation(self, repository, number):
        value = self.client.get_pull_request_observation(repository, number)
        self.capture("initial_observation", asdict(value))
        return value

    def get_changed_files(self, identity):
        self.capture("changed_files_pending", None)
        value = self.client.get_changed_files(identity)
        self.capture("changed_files", [asdict(item) for item in value])
        return value


class _InitialIdentityRefusal(ValueError):
    reason = "initial_identity_guard_refusal"


def _observation_json(value):
    if isinstance(value, datetime):
        return value.isoformat()
    raise TypeError("Unsupported capture value: " + type(value).__name__)


def _capture_bytes(value):
    return json_bytes(json.loads(json.dumps(value, default=_observation_json)))


def _write_attempt_file(path, data, maximum=MAX_SELECTION_BYTES):
    if len(data) > maximum:
        raise AnalysisLimit("outer_attempt_retention_capacity")
    # The shared writer's 16MiB result bound is intentionally NOT the input bound.
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "wb") as stream:
        stream.write(data)


def fresh_execution_identity():
    """Bind the native source forest, experimental producers and Python environment.

    Acquisition uses more native providers than the comparison's twelve-source
    closure. A coarse native-forest binding avoids pretending that closure covers
    the whole acquisition method. It does not authenticate a past network event.
    """
    from importlib.metadata import version
    root = Path(__file__).resolve().parents[1]
    sources = {**ordinary_code_identity()}
    for name in ("api_release_window_manifest.py",):
        path = "experiments/" + name
        sources[path] = content_digest((root / path).read_bytes())
    sources.update({str(path.relative_to(root)): content_digest(path.read_bytes())
                    for path in sorted((root / "src/upgradepilot").rglob("*.py"))})
    return dict(code_sha256=sources, runtime=dict(python=sys.version, executable=sys.executable,
        implementation=platform.python_implementation(), platform=sys.platform,
        executable_sha256=content_digest(Path(sys.executable).read_bytes()),
        distributions={name: version(name) for name in ("requests", "packaging")}))


def _read_fresh_contract(data):
    """Admit only the qualified operational contract, not new policy knobs.

    Selection prose/historical hashes stay as dated context. Executable values
    below must match the qualified owners; a future expansion needs a successor.
    """
    from upgradepilot.github.identity import validate_repository
    if len(data) > MAX_SELECTION_BYTES:
        raise AnalysisLimit("outer_contract_capacity")
    contract = parse_json(data)
    if type(contract) is not dict or contract.get("format") != "fresh-ordinary-pr-contract/1":
        raise ValueError("Unsupported fresh contract.")
    invocation = object_fields(contract["invocation"], ("repository", "pull_number", "expected_base", "expected_head"))
    validate_repository(invocation["repository"])
    if type(invocation["pull_number"]) is not int or invocation["pull_number"] < 1:
        raise ValueError("Invalid requested pull number.")
    for field in ("expected_base", "expected_head"):
        if not isinstance(invocation[field], str) or len(invocation[field]) != 40 or any(c not in "0123456789abcdef" for c in invocation[field]):
            raise ValueError("Missing exact revision guard.")
    policy = object_fields(contract["acquisition_policy"], tuple(TrialAcquisitionPolicy.__dataclass_fields__))
    TrialAcquisitionPolicy(**policy)  # Validate numeric types before any credential work.
    expected_policy = asdict(TrialAcquisitionPolicy())
    # Preserve the original two-candidate contract; the successor's four-work
    # frontier is independently qualified. Other ceilings are not enlarged here.
    if policy["adapter_candidate_attempts"] in {2, 4}:
        expected_policy["adapter_candidate_attempts"] = policy["adapter_candidate_attempts"]
    if (policy != expected_policy
        or contract["analysis_limits"] != asdict(AnalysisLimits())
        or contract["source_limits"] != dict(max_release_identities=4, max_dependency_hops=2,
            max_module_questions=12, max_library_source_bytes=2097152, max_target_python_files=200,
            max_target_source_bytes=2097152, max_crossed_release_metadata=10)
        or contract["correspondence_limits"] != dict(max_resolver_depth=MAX_DISCOVERY_DEPTH,
            max_literal_path_steps=MAX_PATH_STEPS, max_candidates_and_comparisons=256,
            max_resolution_states=4096, max_diagnostic_records=MAX_DISCOVERY_GAPS, omitted_diagnostics_counted=True)):
        raise ValueError("Fresh contract exceeds or changes qualified configuration.")
    scope = contract["provider_scope"]
    if (scope != dict(methods=["GET"], hosts=["api.github.com", "pypi.org"], public_only=True,
                      redirects=False, installed_or_executed_target_code=False, global_environment_mutation=False)
        or contract["authentication"]["mode"] != "token-env"
        or contract["authentication"]["ambient_credentials"] != "not_inherited"
        or contract["max_official_attempts"] != 1 or contract["automatic_retry"] is not False
        or contract["automatic_cap_enlargement"] is not False):
        raise ValueError("Unsupported fresh provider/auth/retry scope.")
    representation = contract["representation"]
    required = dict(fresh_proof_class=FRESH_PROOF, input_format=INPUT_FORMAT, comparison_format=FORMAT,
        correspondence_version=CORRESPONDENCE_VERSION, outer_attempt_format="fresh-ordinary-pr-attempt/1",
        inner_analysis_format="ordinary-caller-signature-attempt/1")
    if any(representation.get(k) != v for k, v in required.items()):
        raise ValueError("Unsupported fresh representation.")
    retention = contract["private_retention"]
    if (retention["directory_mode"] != "0700" or retention["file_mode"] != "0600"
        or retention["comparison_directory"] != "comparison" or retention["raw_http_archive"] is not False
        or retention["bounds"] != dict(encoded_input_bytes=MAX_CATALOG_BYTES,
            each_result_or_source_companion_bytes=MAX_OUTPUT_BYTES, attempt_metadata_bytes=MAX_SELECTION_BYTES)):
        raise ValueError("Unsupported fresh retention.")
    if not Path(retention["root"]).is_absolute():
        raise ValueError("Private attempt destination must be absolute.")
    return contract


def prepare_fresh_execution_freeze(contract_data, *, credential_file, mode):
    """Return a snapshot for review; creating it never authorizes live execution.

    Controlled qualification retains the controlled proof class even though it
    exercises the same outer lifecycle. The credential file is explicit, never
    read here, and its location (not value) is bound to the execution selection.
    """
    _read_fresh_contract(contract_data)
    if mode not in {"controlled_qualification", "live_activation"} or not credential_file.is_absolute():
        raise ValueError("Explicit execution mode and absolute credential file required.")
    return json_bytes(dict(format="ordinary-pr-execution-freeze/1", mode=mode,
        contract_sha256=content_digest(contract_data), credential_file=str(credential_file),
        **fresh_execution_identity()))


def _admit_execution_freeze(contract_data, freeze_data, *, current):
    if len(freeze_data) > MAX_SELECTION_BYTES:
        raise AnalysisLimit("outer_execution_freeze_capacity")
    freeze = object_fields(parse_json(freeze_data), ("format", "mode", "contract_sha256", "credential_file", "code_sha256", "runtime"))
    if (len(freeze_data) > MAX_SELECTION_BYTES or freeze["format"] != "ordinary-pr-execution-freeze/1"
        or freeze["mode"] not in {"controlled_qualification", "live_activation"}
        or freeze["contract_sha256"] != content_digest(contract_data)
        or not Path(freeze["credential_file"]).is_absolute()):
        raise ValueError("Invalid execution freeze/contract binding.")
    if current and {k: freeze[k] for k in ("code_sha256", "runtime")} != fresh_execution_identity():
        raise ValueError("Executable method/environment differs from execution freeze.")
    return freeze


def _read_attempt_credential(path):
    """Explicit owner-only file; never inspect ambient GITHUB_TOKEN or echo errors."""
    descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(descriptor, "rb") as stream:
        info = os.fstat(stream.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) != 0o600:
            raise PermissionError("Credential file must be owner-only regular file.")
        token = stream.read(4097)
    if len(token) > 4096:
        raise ValueError("Credential exceeds admitted size.")
    token = token.decode("ascii").strip()
    if not token or any(c.isspace() or ord(c) < 33 or ord(c) > 126 for c in token):
        raise ValueError("Credential is empty or malformed.")
    return token


def _fresh_providers(session):
    from upgradepilot.github.pull_request import GitHubPullRequestClient
    from .api_adapter_exploration import AdapterSourceExplorer
    return AdapterSourceExplorer(session=session), dict(pull_requests=GitHubPullRequestClient(session=session))


def _structural_disposition(body):
    """Local paired binding facts are useful; coverage closure is never implied."""
    roots = {}
    for candidate, pair in zip(body["discovery"]["candidates"], body["pairs"]):
        comparison = pair["comparison"]
        # Unknown starred arguments can prevent full binding while a named
        # keyword's reception remains established locally. Preserve that fact;
        # an overall undetermined result is not necessarily all-unknown evidence.
        informative = comparison["outcome"] in {"bound", "rejected"} or any(
            item["outcome"] != "undetermined" for item in comparison["keyword_reception"])
        if informative:
            roots.setdefault(candidate["root_call_id"], set()).add(candidate["callee_role"]["role"])
    useful = any({"native_old_version", "native_proposed_version"} <= roles for roles in roots.values())
    discovery, acquisition = body["discovery"], body["acquisition"]
    ordinary = acquisition.get("ordinary_acquisition", {})
    target = ordinary.get("target", {})
    changed = ordinary.get("changed_package_sources", {})
    adapters = ordinary.get("adapter_exploration", {})
    # Deliberately conservative: even no recorded gap is not complete coverage.
    # Unknown installed namespace/dispatch remain premises on useful local facts.
    partial = bool(discovery["gaps"] or discovery["gaps_omitted"] or acquisition.get("material_omissions")
        or target.get("gaps") or target.get("omitted_paths") or changed.get("unexamined_modules")
        or adapters.get("problems") or adapters.get("omitted_candidates")
        or ordinary.get("transport", {}).get("stops")
        or any(not item["comparison"]["checks_complete"] for item in body["pairs"])
        or any(item.get("state") != "module_examined" for item in changed.get("attempts", []))
        or any(item.get("state") != "module_examined" for item in acquisition.get("internal_module_requests", [])))
    return ("useful_partial_structural_evidence" if partial else "useful_structural_evidence") if useful else "insufficient_structural_evidence"


def run_fresh_ordinary_pr_attempt(contract_data, freeze_data, *, activate_live=False):
    """One immutable acquisition→analysis attempt, never an implicit retry.

    Validate before creating the selected private destination. Start before any
    credential/provider work. Handled failures retain completed stage snapshots;
    abrupt process loss can leave unknown completion and unrecovered intermediates.
    Live mode additionally requires an explicit caller activation; that flag is
    an operational interlock, not a source of user authorization.
    """
    contract = _read_fresh_contract(contract_data)
    freeze = _admit_execution_freeze(contract_data, freeze_data, current=True)
    if freeze["mode"] == "live_activation" and not activate_live:
        raise ValueError("Live activation withheld; no credential/provider work.")
    directory = Path(contract["private_retention"]["root"])
    if directory.parent.is_symlink() or not directory.parent.is_dir():
        raise ValueError("Private attempt parent must already be a real directory.")
    if stat.S_IMODE(directory.parent.stat().st_mode) != 0o700 or directory.parent.stat().st_uid != os.getuid():
        raise PermissionError("Private attempt parent must be owner-only.")
    directory.mkdir(mode=0o700)  # Refuses even a previous incomplete destination.
    started = time.monotonic()
    invocation = contract["invocation"]
    attempt = dict(format="fresh-ordinary-pr-attempt/1", attempt_id=uuid.uuid4().hex,
        state="started", reason=None, cause=None, stage="entry", started_at=datetime.now(UTC).isoformat(),
        ended_at=None, elapsed_seconds=None, invocation=invocation, auth_mode="token-env",
        execution_mode=freeze["mode"], contract_sha256=content_digest(contract_data),
        execution_freeze_sha256=content_digest(freeze_data), code_sha256=freeze["code_sha256"],
        runtime=freeze["runtime"], configuration=dict(acquisition_policy=contract["acquisition_policy"],
            analysis_limits=contract["analysis_limits"]), observed_identity=None,
        structural_disposition="not_assessed", coverage="not_established", inner_attempt=None,
        artifacts={})
    _write_attempt_file(directory / "contract.json", contract_data)
    _write_attempt_file(directory / "execution-freeze.json", freeze_data)
    _write_attempt_file(directory / "attempt-started.json", json_bytes(attempt))
    start_digest = content_digest((directory / "attempt-started.json").read_bytes())
    partial, session, source_records, capture_omissions = {}, None, [], []
    transport_receipt = None

    def capture(stage, value):
        attempt["stage"] = stage
        value = parse_json(_capture_bytes(value))
        if stage == "initial_observation":
            _write_attempt_file(directory / "initial-observation.json", json_bytes(value), MAX_OUTPUT_BYTES)
            attempt["observed_identity"] = value["identity"]
            identity = value["identity"]
            if any(identity.get(key) != invocation[field] for key, field in (
                ("repository", "repository"), ("number", "pull_number"),
                ("base_sha", "expected_base"), ("head_sha", "expected_head"))):
                raise _InitialIdentityRefusal("Initial observation differs from requested guards.")
        elif stage == "library_source":
            if value not in source_records:
                source_records.append(value)
        else:
            partial[stage] = value
        if len(_capture_bytes(dict(partial=partial, library_sources=source_records))) > MAX_OUTPUT_BYTES:
            if stage == "library_source":
                source_records.pop()
            else:
                partial.pop(stage, None)
            capture_omissions.append(dict(stage=stage, reason="partial_acquisition_retention_capacity"))
            raise AnalysisLimit("partial_acquisition_retention_capacity")

    try:
        attempt["stage"] = "credential"
        try:
            token = _read_attempt_credential(Path(freeze["credential_file"]))
        except (OSError, ValueError, UnicodeError) as exc:
            attempt.update(state="refused", reason="credential_unavailable_or_unsafe",
                cause=dict(type=type(exc).__name__, reason="credential_unavailable_or_unsafe", status_code=None))
        else:
            session = TrialPublicSession(token=token, policy=TrialAcquisitionPolicy(**contract["acquisition_policy"]))
            del token
            adapters, providers = _fresh_providers(session)
            providers["pull_requests"] = _ObservedPullClient(providers["pull_requests"], capture)
            attempt["stage"] = "acquisition"
            acquired = acquire_ordinary_comparison_inputs(invocation["repository"], invocation["pull_number"],
                session=session, adapters=adapters, capture=capture,
                expected_base=invocation["expected_base"], expected_head=invocation["expected_head"], **providers)
            # Stop acquisition accounting at its own boundary. Sampling this
            # clock after the worker would charge analysis time to acquisition.
            transport_receipt = session.acquisition_receipt()
            if isinstance(acquired, AcquisitionProblem):
                evidence = acquired.evidence
                attempt.update(state="acquisition_incomplete", stage=acquired.stage, reason=acquired.reason,
                    cause=dict(type=type(evidence).__name__, reason=acquired.reason,
                               status_code=getattr(evidence, "status_code", None)))
                if getattr(evidence, "status_code", None) in {401, 403}:
                    attempt["state"] = "refused"
                elif acquired.reason == "trial_acquisition_deadline":
                    attempt["state"] = "timed_out"
            else:
                attempt["stage"] = "input_freeze"
                proof = FRESH_PROOF if freeze["mode"] == "live_activation" else "controlled_ordinary_pr_composition"
                data = encode_ordinary_inputs(*acquired, proof_class=proof)
                _write_attempt_file(directory / "acquisition-input.json", data, MAX_CATALOG_BYTES)
                attempt["stage"] = "analysis"
                inner = run_ordinary_comparison(data, directory / "comparison", limits=AnalysisLimits(**contract["analysis_limits"]))
                attempt["inner_attempt"] = "comparison/attempt.json"
                attempt.update(state=inner["state"], reason=inner["reason"])
                if inner["state"] == "completed":
                    attempt["stage"] = "admission"
                    body, _ = open_ordinary_comparison(directory / "comparison")
                    if (body["inputs"]["discovery_input_sha256"] != content_digest(data)
                        or body["proof_class"] != proof
                        or (directory / "comparison/input.json").read_bytes() != data):
                        raise ValueError("Outer/inner acquired input binding mismatch.")
                    attempt["structural_disposition"] = _structural_disposition(body)
                    attempt["coverage"] = "partial; complete target/runtime coverage not established"
    except KeyboardInterrupt:
        attempt.update(state="interrupted", reason="caller_interrupt")
    except subprocess.TimeoutExpired:
        attempt.update(state="timed_out", reason="bounded_attempt_deadline")
    except (OSError, ValueError, TypeError, MemoryError, RuntimeError) as exc:
        # Exception text may contain credential/provider data. Keep typed cause,
        # classified reason and stage; source material has its own private capture.
        reason = getattr(exc, "reason", type(exc).__name__)
        state = "timed_out" if reason == "trial_acquisition_deadline" else "failed"
        if isinstance(exc, _InitialIdentityRefusal):
            state = "refused"
        attempt.update(state=state, reason=reason,
            cause=dict(type=type(exc).__name__, reason=reason, status_code=getattr(exc, "status_code", None)))
    finally:
        receipt = transport_receipt
        if receipt is None and session is not None:
            receipt = session.acquisition_receipt()
        acquisition = dict(format="fresh-ordinary-pr-acquisition/1", completed_stages=partial,
            library_sources=source_records, capture_omissions=capture_omissions, transport=receipt,
            retention="completed returned stages only; lost intermediates are not reconstructed")
        try:
            _write_attempt_file(directory / "acquisition.json", _capture_bytes(acquisition), MAX_OUTPUT_BYTES)
            if fresh_execution_identity() != {k: freeze[k] for k in ("code_sha256", "runtime")}:
                attempt.update(state="failed", reason="executable_method_changed_during_attempt",
                    structural_disposition="not_assessed")
            attempt.update(ended_at=datetime.now(UTC).isoformat(), elapsed_seconds=time.monotonic() - started,
                           started_sha256=start_digest)
            for relative in _OUTER_FILES:
                path = directory / relative
                if path.is_file():
                    attempt["artifacts"][relative] = content_digest(path.read_bytes())
            _write_attempt_file(directory / "attempt.json", json_bytes(attempt))
        finally:
            if session is not None:
                session.close()
    return attempt


_OUTER_FILES = {"contract.json", "execution-freeze.json", "attempt-started.json", "initial-observation.json",
    "acquisition-input.json", "acquisition.json", "comparison/input.json", "comparison/attempt-started.json",
    "comparison/attempt.json", "comparison/result.json", "comparison/sources.json", "comparison/view.txt",
    "comparison/_worker-result.json", "comparison/_worker-sources.json"}
_OUTER_START_FIELDS = ("format", "attempt_id", "state", "reason", "cause", "stage", "started_at", "ended_at",
    "elapsed_seconds", "invocation", "auth_mode", "execution_mode", "contract_sha256", "execution_freeze_sha256",
    "code_sha256", "runtime", "configuration", "observed_identity", "structural_disposition", "coverage", "inner_attempt", "artifacts")


def open_fresh_ordinary_pr_attempt(directory):
    """Offline fixed admission of completed, incomplete or unknown-completion attempts.

    Digests bind retained branches, not authenticity. Never compare historical
    code hashes to today's checkout or rerun acquisition/discovery/checking here.
    """
    contract_data = read_bounded_bytes(directory / "contract.json", MAX_SELECTION_BYTES)
    freeze_data = read_bounded_bytes(directory / "execution-freeze.json", MAX_SELECTION_BYTES)
    contract = _read_fresh_contract(contract_data)
    freeze = _admit_execution_freeze(contract_data, freeze_data, current=False)
    start_data = read_bounded_bytes(directory / "attempt-started.json", MAX_SELECTION_BYTES)
    start = object_fields(parse_json(start_data), _OUTER_START_FIELDS)
    for key, expected in dict(format="fresh-ordinary-pr-attempt/1", state="started",
        invocation=contract["invocation"], contract_sha256=content_digest(contract_data),
        execution_freeze_sha256=content_digest(freeze_data), code_sha256=freeze["code_sha256"],
        runtime=freeze["runtime"], execution_mode=freeze["mode"], auth_mode=contract["authentication"]["mode"],
        configuration=dict(acquisition_policy=contract["acquisition_policy"], analysis_limits=contract["analysis_limits"])).items():
        if start.get(key) != expected:
            raise ValueError("Outer start/contract/freeze binding mismatch.")
    terminal = directory / "attempt.json"
    if not terminal.exists():
        record = dict(start, state="unknown_completion", reason="terminal_record_missing")
    else:
        record = object_fields(parse_json(read_bounded_bytes(terminal, MAX_SELECTION_BYTES)), (*_OUTER_START_FIELDS, "started_sha256"))
        if (record.get("state") not in {"refused", "acquisition_incomplete", "failed", "timed_out", "interrupted", "completed"}
            or record.get("started_sha256") != content_digest(start_data)
            or type(record["elapsed_seconds"]) not in {int, float}
            or not 0 <= record["elapsed_seconds"] < float("inf")
            or datetime.fromisoformat(record["ended_at"]).utcoffset() is None):
            raise ValueError("Invalid outer terminal/start binding.")
        for key in ("format", "attempt_id", "started_at", "invocation", "auth_mode", "execution_mode",
                    "contract_sha256", "execution_freeze_sha256", "code_sha256", "runtime", "configuration"):
            if record.get(key) != start.get(key):
                raise ValueError("Outer terminal identity changed: " + key)
        artifacts = record.get("artifacts")
        if type(artifacts) is not dict or not {"contract.json", "execution-freeze.json", "attempt-started.json", "acquisition.json"} <= artifacts.keys() or not artifacts.keys() <= _OUTER_FILES:
            raise ValueError("Invalid outer artifact closure.")
        actual = {name for name in _OUTER_FILES if (directory / name).is_file()}
        if actual != artifacts.keys():
            raise ValueError("Outer retained artifact membership mismatch.")
        for name, digest in artifacts.items():
            capacity = MAX_CATALOG_BYTES if name in {"acquisition-input.json", "comparison/input.json"} else MAX_OUTPUT_BYTES
            if content_digest(read_bounded_bytes(directory / name, capacity)) != digest:
                raise ValueError("Outer artifact digest mismatch: " + name)
    observation = parse_json(read_bounded_bytes(directory / "initial-observation.json", MAX_OUTPUT_BYTES)) if (directory / "initial-observation.json").exists() else None
    acquisition = object_fields(parse_json(read_bounded_bytes(directory / "acquisition.json", MAX_OUTPUT_BYTES)),
        ("format", "completed_stages", "library_sources", "capture_omissions", "transport", "retention")) if (directory / "acquisition.json").exists() else None
    if acquisition is not None and (acquisition["format"] != "fresh-ordinary-pr-acquisition/1"
        or type(acquisition["completed_stages"]) is not dict or type(acquisition["library_sources"]) is not list
        or type(acquisition["capture_omissions"]) is not list):
        raise ValueError("Invalid partial acquisition representation.")
    if acquisition is not None and acquisition.get("transport") is not None:
        _validate_transport(acquisition["transport"])
    body, catalog = None, None
    if observation is not None and record["state"] != "unknown_completion" and record["observed_identity"] != observation["identity"]:
        raise ValueError("Outer observed identity mismatch.")
    if record["state"] == "completed":
        data = read_bounded_bytes(directory / "acquisition-input.json", MAX_CATALOG_BYTES)
        body, catalog = open_ordinary_comparison(directory / "comparison")
        raw = parse_json(data)
        expected_proof = FRESH_PROOF if freeze["mode"] == "live_activation" else "controlled_ordinary_pr_composition"
        native = raw["acquisition"]["native_inputs"]
        if (observation is None or native["identity"] != observation["identity"] or native["description"] != observation["description"]
            # The established reader validates observed_at as datetime in memory;
            # compare its fixed JSON representation with the retained input.
            or _capture_bytes(body["acquisition"]) != _capture_bytes(raw["acquisition"]) or body["proof_class"] != expected_proof
            or body["inputs"]["discovery_input_sha256"] != content_digest(data)
            or read_bounded_bytes(directory / "comparison/input.json", MAX_CATALOG_BYTES) != data
            or record["inner_attempt"] != "comparison/attempt.json"
            or record["structural_disposition"] != _structural_disposition(body)
            or record["coverage"] != "partial; complete target/runtime coverage not established"
            or body["limits"] != contract["analysis_limits"]
            or body["code_sha256"] != {k: freeze["code_sha256"].get(k) for k in body["code_sha256"]}
            or any(native["identity"].get(key) != contract["invocation"][field] for key, field in (
                ("repository", "repository"), ("number", "pull_number"),
                ("base_sha", "expected_base"), ("head_sha", "expected_head")))):
            raise ValueError("Outer observation/input/analysis binding mismatch.")
    return dict(attempt=record, initial_observation=observation, acquisition=acquisition, comparison=body, catalog=catalog)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    opened = commands.add_parser("open", help="Inspect ordinary saved evidence offline.")
    opened.add_argument("--result", required=True, type=Path)
    opened.add_argument("--source")
    opened.add_argument("--start-line", type=int, default=1)
    opened.add_argument("--line-count", type=int, default=40)
    outer = commands.add_parser("open-attempt", help="Inspect fresh acquisition lifecycle offline, including incomplete attempts.")
    outer.add_argument("--result", required=True, type=Path)
    worker = commands.add_parser("_worker", help=argparse.SUPPRESS)
    worker.add_argument("input_path", type=Path)
    worker.add_argument("directory", type=Path)
    worker.add_argument("limits")
    args = parser.parse_args(argv)
    try:
        if args.command == "_worker":
            _worker(args.input_path, args.directory, AnalysisLimits(**json.loads(args.limits)))
        elif args.command == "open-attempt":
            opened_attempt = open_fresh_ordinary_pr_attempt(args.result)
            record = opened_attempt["attempt"]
            print(render_terminal_lines(["ACQUISITION ATTEMPT: " + record["state"],
                "Stage: " + record["stage"], "Reason: " + str(record["reason"]),
                "Evidence mode: " + record["execution_mode"],
                "Structural disposition: " + record["structural_disposition"]]))
            acquisition = opened_attempt["acquisition"]
            if acquisition is not None:
                print("Retained completed stages: " + ", ".join(acquisition["completed_stages"]))
                print("Retained library module records: " + str(len(acquisition["library_sources"])))
                transport = acquisition["transport"]
                if transport is not None:
                    print("Provider work: " + str(transport["github_requests"]) + " GitHub / "
                        + str(transport["provider_requests"]) + " all-provider attempts; "
                        + str(transport["decoded_body_bytes"]) + " decoded bytes")
            if opened_attempt["comparison"] is not None:
                print(render_ordinary_comparison(opened_attempt["comparison"]))
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
