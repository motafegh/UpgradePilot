"""Compose the ordinary source acquisition from the already observed PR inputs."""
from __future__ import annotations

from collections import deque
from collections.abc import Callable
from datetime import datetime, timezone
from hashlib import sha256

from ..dependency.change import DependencyVersionChange
from ..github.api import GitHubAcquisitionError, GitHubResponseError
from ..investigation_inputs import AcquiredDependencyInputs
from ..target.source_context import TargetSourceAcquirer, source_id
from ..workspace.native_boundary import exact_investigation_target
from ..workspace.source_access import RetainedSourceCatalog, RetainedSourceFile, RetainedSourceScope
from .acquisition import AcquisitionSession
from .bindings import ImportFact
from .correspondence import PythonSourceModule, absolute_import, module_name
from .evidence import AnalysisLimits
from .source_acquisition import AdapterSourceExplorer, ExaminedPythonModule, PythonModuleSourceRequest
from .source_evidence import (
    AcquisitionProblem, CallerSignatureSources, SourceAcquisitionReceipt, SourceFileReceipt,
    SourceMaterialOmission, SourceProblem, SourceSampleSelection, TargetSourceReceipt,
)


def _origin_for_module(module, origin, references):
    for reference in references:
        if reference.source_id == origin.source_id and reference.binding is not None:
            if any(name == module or name.startswith(module + ".")
                   for name in reference.binding.possible_imports):
                return reference
    return origin


def _changed_module_origins(candidates, imports, references, package):
    for candidate in candidates:
        if candidate.declaration.package == package:
            for origin in imports:
                if (origin.source_id, origin.line, origin.module) == (
                    candidate.import_source_id, candidate.import_line, candidate.imported_module
                ):
                    yield origin.module, _origin_for_module(origin.module, origin, references)


def _target_receipt(context):
    return TargetSourceReceipt(
        repository=context.inventory.repository, revision=context.inventory.revision,
        tree_sha=context.inventory.tree_sha, inventory_entries=len(context.inventory.entries),
        inventory_truncated=context.inventory.truncated,
        files=tuple(SourceFileReceipt(source_id(file), sha256(file.content.encode()).hexdigest(),
                                      len(file.content.encode())) for file in context.files),
        declarations=context.declarations, candidates=context.candidates,
        excluded_paths=context.excluded_paths, omitted_paths=context.omitted_paths,
        gaps=context.gaps, examined_bytes=context.examined_bytes, limitations=context.limitations,
    )


def _source_material(target, context, libraries, limits):
    scopes, files, modules, omissions = {}, {}, [], []
    size = 0

    def add(file, role, package, version, dependencies, module):
        nonlocal size
        scope_id = "source-" + sha256(
            "\0".join((role, file.repository, file.revision, package, version)).encode()
        ).hexdigest()
        key = scope_id, file.path
        if key in files:
            return
        byte_count = len(file.content.encode())
        if len(files) >= limits.max_files or size + byte_count > limits.max_source_bytes:
            omissions.append(SourceMaterialOmission(
                file.repository, file.revision, file.path, role, "analysis_material_limit",
            ))
            return
        size += byte_count
        if scope_id not in scopes:
            scopes[scope_id] = RetainedSourceScope(
                scope_id, file.repository, file.revision, "repository_text",
                "Exact target head" if role == "target_repository" else "Declared release repository and tag",
                "Complete admitted files within bounded source selection",
            )
        files[key] = RetainedSourceFile(scope_id, file.path, file.content)
        if module is not None:
            modules.append(PythonSourceModule(scope_id, file.path, module, package, version, role, dependencies))

    for observed, receipt in sorted(libraries, key=lambda item: item[1].request.version_basis == "constraint_sample"):
        add(observed.file, receipt.request.version_basis, receipt.request.package, receipt.request.version,
            tuple(sorted({item.package for item in observed.metadata.requirements})),
            receipt.request.module)
    if context is not None:
        dependencies = tuple(sorted({item.package for item in context.declarations}))
        for file in context.files:
            name = (module_name(file.path) or "") if file.path.endswith(".py") else None
            add(file, "target_repository", "", "", dependencies, name)
    catalog = RetainedSourceCatalog(tuple(scopes.values()), tuple(files.values()), target=target) if files else None
    return catalog, tuple(modules), tuple(omissions)


def collect_source_progress(
    inputs: AcquiredDependencyInputs,
    session: AcquisitionSession,
    publish: Callable[[CallerSignatureSources], None],
) -> CallerSignatureSources:
    """Acquire bounded source questions and publish returned material between stages."""
    dependency = inputs.dependency
    if not isinstance(dependency, DependencyVersionChange):
        raise ValueError("Source acquisition requires an established dependency transition.")
    target = exact_investigation_target(inputs.identity, dependency)
    explorer = AdapterSourceExplorer(session=session)
    run = explorer.source_run()
    limits = AnalysisLimits()
    context = target_receipt = exploration = None
    receipts, libraries, samples, problems, unexamined, closure_omissions = [], [], [], [], [], []
    selected_modules = set()
    observed_at = datetime.now(timezone.utc)

    def snapshot(state):
        catalog, modules, material_omissions = _source_material(target, context, libraries, limits)
        omissions = material_omissions + tuple(closure_omissions)
        transport = session.acquisition_receipt()
        gaps = tuple(dict.fromkeys(gap for receipt in receipts for gap in receipt.retention_gaps))
        if (problems or unexamined or omissions or transport.stops
                or any(r.state != "module_examined" for r in receipts)
                or (context and (context.gaps or context.omitted_paths))
                or (exploration and exploration.omitted_candidates)):
            if state == "complete":
                state = "partial"
        acquisition = SourceAcquisitionReceipt(
            origin="native_observation", state=state, observed_at=observed_at,
            target=target_receipt, module_requests=tuple(receipts), samples=tuple(samples),
            problems=tuple(problems),
            omitted_candidates=exploration.omitted_candidates if exploration else (),
            deferred_candidates=exploration.deferred_candidates if exploration else (),
            unexamined_modules=tuple(dict.fromkeys(unexamined)), material_omissions=omissions,
            adapter_limitations=exploration.limitations if exploration else (),
            source_work=run.work, transport=transport, method_files=(), retention_gaps=gaps,
        )
        sources = CallerSignatureSources(catalog, modules, limits, acquisition)
        publish(sources)
        return sources

    def examine(request):
        before = session.provider_requests
        outcome, receipt = run.examine_with_receipt(request)
        receipts.append(receipt)
        if isinstance(outcome, ExaminedPythonModule):
            libraries.append((outcome, receipt))
        # A budget refusal or cache hit cannot lose a new provider response.
        # Include those questions in the next stage or final publication.
        if session.provider_requests != before:
            snapshot("partial")
        return outcome

    def examine_pairs(origins):
        for module, origin in origins:
            if module in selected_modules:
                continue
            selected_modules.add(module)
            if len(selected_modules) * 2 > run.max_module_files:
                unexamined.append(module)
                continue
            for version, basis in ((dependency.old_version, "native_old_version"),
                                   (dependency.proposed_version, "native_proposed_version")):
                examine(PythonModuleSourceRequest(dependency.normalized_package, version, module, basis, origin))

    with session.stage("target_context", reserve_github=session.policy.source_request_reserve):
        try:
            acquired = TargetSourceAcquirer(session=session).acquire(
                target.repository, target.head_sha,
                changed_paths=tuple(file.filename for file in inputs.changed_files),
                max_file_attempts=session.policy.target_file_attempts,
            )
        except GitHubAcquisitionError as exc:
            acquired = AcquisitionProblem("target_context", exc.reason, str(exc))
        except GitHubResponseError as exc:
            acquired = AcquisitionProblem("target_context", "malformed_response", str(exc))
    if isinstance(acquired, AcquisitionProblem):
        problems.append(SourceProblem(acquired.stage, acquired.reason, acquired.detail))
        return snapshot("failed")
    context = acquired
    target_receipt = _target_receipt(context)
    snapshot("partial")

    with session.stage("library_sources"):
        # Exact version questions have priority over exploratory samples.
        examine_pairs(_changed_module_origins(
            context.candidates, context.imports, context.references, dependency.normalized_package,
        ))
        exploration = explorer.explore(
            context, source_run=run, stop_at_package=dependency.normalized_package,
            max_candidate_attempts=session.policy.adapter_candidate_attempts,
        )
        problems.extend(SourceProblem(p.stage, p.reason, p.detail) for p in exploration.problems)
        for sample in exploration.samples:
            question = PythonModuleSourceRequest(
                sample.metadata.package, sample.version, sample.candidate.imported_module, "constraint_sample",
            )
            # The explorer obtained this same question in the shared run.
            outcome, receipt = run.examine_with_receipt(question)
            receipts.append(receipt)
            if isinstance(outcome, ExaminedPythonModule):
                libraries.append((outcome, receipt))
                samples.append(SourceSampleSelection(
                    sample.candidate, sample.depth, sample.version, sample.selection,
                    sample.file.repository, sample.file.revision, sample.file.path, receipt.sha256,
                ))
        snapshot("partial")
        examine_pairs(
            item for candidate in exploration.deferred_candidates for sample in exploration.samples
            for item in _changed_module_origins(
                (candidate,), sample.imports, sample.references, dependency.normalized_package,
            )
        )

    with session.stage("source_closure"):
        _examine_internal_modules(context, libraries, examine, closure_omissions)
        try:
            session.finish_acquisition()
        except (GitHubAcquisitionError, GitHubResponseError) as exc:
            problems.append(SourceProblem("source_closure", getattr(exc, "reason", "malformed_response"), str(exc)))
            return snapshot("failed")
    return snapshot("complete")


def _examine_internal_modules(context, libraries, examine, omissions):
    """Apply the qualified import priority to questions inside observed inventories."""
    interest = set()
    for reference in context.references:
        origins = reference.binding.possible_imports if reference.binding else (reference.lexical_import,)
        for origin in origins:
            if origin:
                interest.update(origin.split("."))
    queue = deque(observed for observed, _ in sorted(
        libraries, key=lambda item: item[1].request.version_basis == "constraint_sample",
    ))
    pending = {}
    seen = set()
    order = 0
    questions = 0
    while queue or pending:
        while queue:
            parent = queue.popleft()
            current = module_name(parent.file.path)
            if current is None:
                continue
            called = {ref.expression.split(".")[0] for ref in parent.references}
            available = {module_name(entry.path) for entry in parent.inventory.entries if entry.kind == "blob"}
            for fact in parent.imports:
                if not isinstance(fact, ImportFact):
                    continue
                imported = absolute_import(current, parent.file.path, fact.module, fact.relative_level)
                if not imported:
                    continue
                names = (imported, imported + "." + fact.member) if fact.member and fact.member != "*" else (imported,)
                bound = fact.alias or fact.member or fact.module.split(".")[0]
                priority = 0 if bound in interest else 1 if bound in called else 2
                if bound in interest and fact.member and any(name in available for name in names):
                    interest.add(fact.member)
                for name in names:
                    if name not in available:
                        continue
                    question = PythonModuleSourceRequest(
                        parent.request.package, parent.request.version, name, parent.request.version_basis, fact,
                    )
                    key = question.package, question.version, question.module, question.version_basis
                    if key in pending:
                        rank, old_priority, *original = pending[key]
                        pending[key] = (rank, min(priority, old_priority), *original)
                    elif key not in seen:
                        seen.add(key)
                        order += 1
                        pending[key] = (
                            int(question.version_basis == "constraint_sample"), priority, order, parent, question,
                        )
        if not pending:
            break
        ordered = sorted(pending, key=lambda key: pending[key][:3])
        first = ordered[0]
        selected = [first]
        if pending[first][0] == 0:
            other = next((key for key in ordered[1:] if pending[key][0] == 0
                          and (key[0], key[2]) == (first[0], first[2]) and key[3] != first[3]), None)
            if other is not None:
                selected.append(other)
        for key in selected:
            _, _, _, parent, question = pending.pop(key)
            if questions >= 256:
                role = {"native_old_version": "old_dependency",
                        "native_proposed_version": "proposed_dependency"}.get(
                            question.version_basis, question.version_basis,
                        )
                omissions.extend(SourceMaterialOmission(
                    parent.file.repository, parent.file.revision, entry.path, role, "closure_receipt_limit",
                ) for entry in parent.inventory.entries
                    if entry.kind == "blob" and module_name(entry.path) == question.module)
                continue
            questions += 1
            outcome = examine(question)
            if isinstance(outcome, ExaminedPythonModule):
                queue.append(outcome)
