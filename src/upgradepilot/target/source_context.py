"""Acquire exact target source, declarations and conditional static import context.

Start at TargetSourceAcquirer.acquire with the invocation's existing session and
observed head revision. The repository owner establishes commit/tree identity;
this owner selects complete files, preserves omissions and derives declarations
and static origins. These are exploration candidates, not installed namespace or
runtime dispatch proof. Source facts delegate to caller_signature.bindings;
Workspace publication and dependency-source exploration are separate owners.
"""
from __future__ import annotations

import ast
import hashlib
import re
import tomllib
from dataclasses import dataclass
from pathlib import PurePosixPath
from packaging.requirements import InvalidRequirement, Requirement

from ..github.api import GitHubAcquisitionError, GitHubResponseError
from ..github.repository import (
    GitHubRepositoryClient, RepositoryTextFile, GitHubRepositoryInventoryClient,
    RepositoryInventory, RepositoryInventoryEntry, RepositoryInventoryProblem,
)
from ..package_identity import normalize_package_name
from ..caller_signature.bindings import ImportFact, ReferenceFact, analyze_python_bindings
from ..caller_signature.source_evidence import (
    AcquisitionProblem, SourceDependencyDeclaration as DependencyDeclaration,
    SourceImportCandidate as ImportDependencyCandidate, SourceContextGap as ContextGap,
)

_EXCLUDED_DIRECTORIES = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    "build",
    "dist",
    "generated",
}
_DECLARATION_NAMES = {
    "pyproject.toml",
    "setup.cfg",
    "setup.py",
    "Pipfile",
    "Pipfile.lock",
    "poetry.lock",
    "uv.lock",
}


@dataclass(frozen=True)
class TargetSourceContext:
    inventory: RepositoryInventory
    files: tuple[RepositoryTextFile, ...]
    imports: tuple[ImportFact, ...]
    references: tuple[ReferenceFact, ...]
    declarations: tuple[DependencyDeclaration, ...]
    candidates: tuple[ImportDependencyCandidate, ...]
    excluded_paths: tuple[str, ...]
    omitted_paths: tuple[str, ...]
    gaps: tuple[ContextGap, ...]
    examined_bytes: int
    # Even complete admitted acquisition cannot establish dynamic behavior/absence.
    limitations: tuple[str, ...] = (
        "static_syntax_not_execution",
        "module_namespace_not_installed_distribution",
        "constraints_not_resolved_versions",
        "only_admitted_file_formats_and_paths",
        "ordered_scoped_static_origins_not_runtime_identity",
        "delayed_globals_closures_and_cross_function_values_unresolved",
        "unsupported_control_flow_and_dynamic_writes_limited",
        "unknown_call_effects_heap_identity_and_annotation_timing_unmodeled",
        "binding_trace_and_origin_budgets_can_limit_association",
    )

def source_id(file: RepositoryTextFile) -> str:
    return f"{file.repository}@{file.revision}:{file.path}"

def extract_python_facts(
    file: RepositoryTextFile,
) -> tuple[tuple[ImportFact, ...], tuple[ReferenceFact, ...], tuple[ContextGap, ...]]:
    """Parse acquired text, then delegate ordered/scoped binding propagation.

    The caller_signature.bindings owner supplies states/traces and
    positive-reference admission directly.
    Acquisition keeps source identity and parsing/analysis failures separate;
    source association never establishes execution or an installed distribution.
    """
    try:
        tree = ast.parse(file.content, filename=file.path)
    except (SyntaxError, ValueError, RecursionError) as exc:
        return (), (), (ContextGap(file.path, "python_parse_failed", str(exc)),)
    try:
        imports, references = analyze_python_bindings(
            source_id(file), file.content, tree
        )
    except RecursionError as exc:
        return (
            (),
            (),
            (ContextGap(file.path, "python_binding_analysis_limit", str(exc)),),
        )
    return imports, references, ()

def extract_dependency_declarations(
    file: RepositoryTextFile,
) -> tuple[tuple[DependencyDeclaration, ...], tuple[ContextGap, ...]]:
    """Preserve declaration conditions without selecting extras or resolving versions.

    Support standalone requirement lines and PEP 621 project/optional arrays.
    Other declarations/directives remain scoped gaps with original file identity.
    Direct URLs are never followed; credential-bearing raw URLs are not exported.
    """
    records = []
    gaps = []
    identity = source_id(file)

    def add(raw, location, group):
        if not isinstance(raw, str):
            gaps.append(
                ContextGap(
                    file.path,
                    "unsupported_requirement",
                    "Non-string requirement at " + location,
                )
            )
            return
        try:
            requirement = Requirement(raw)
        except InvalidRequirement:
            gaps.append(
                ContextGap(
                    file.path,
                    "unsupported_requirement",
                    "Unparsed requirement at " + location,
                )
            )
            return
        if requirement.url:
            gaps.append(
                ContextGap(
                    file.path, "direct_url_not_followed", "Direct URL at " + location
                )
            )
            return
        records.append(
            DependencyDeclaration(
                identity,
                location,
                raw,
                normalize_package_name(requirement.name),
                str(requirement.specifier),
                tuple(sorted(requirement.extras)),
                str(requirement.marker) if requirement.marker else None,
                group,
            )
        )

    name = PurePosixPath(file.path).name
    if name == "pyproject.toml":
        try:
            data = tomllib.loads(file.content)
        except tomllib.TOMLDecodeError as exc:
            return (), (ContextGap(file.path, "toml_parse_failed", str(exc)),)
        project = data.get("project", {})
        if not isinstance(project, dict):
            return (), (
                ContextGap(
                    file.path,
                    "unsupported_project_declaration",
                    "project is not a table.",
                ),
            )
        dependencies = project.get("dependencies", [])
        if isinstance(dependencies, list):
            for i, raw in enumerate(dependencies):
                add(raw, f"project.dependencies[{i}]", "project")
        else:
            gaps.append(
                ContextGap(
                    file.path,
                    "unsupported_project_declaration",
                    "dependencies is not an array.",
                )
            )
        extras = project.get("optional-dependencies", {})
        if isinstance(extras, dict):
            for extra, values in extras.items():
                if isinstance(values, list):
                    for i, raw in enumerate(values):
                        add(
                            raw,
                            f"project.optional-dependencies.{extra}[{i}]",
                            "optional:" + extra,
                        )
                else:
                    gaps.append(
                        ContextGap(
                            file.path,
                            "unsupported_optional_declaration",
                            "optional dependency is not an array.",
                        )
                    )
        else:
            gaps.append(
                ContextGap(
                    file.path,
                    "unsupported_optional_declaration",
                    "optional-dependencies is not a table.",
                )
            )
        if project.get("dynamic") or data.get("dependency-groups") or data.get("tool"):
            gaps.append(
                ContextGap(
                    file.path,
                    "other_dependency_metadata_unassessed",
                    "Dynamic/group/tool metadata is retained but not resolved.",
                )
            )
    elif re.fullmatch(r"requirements[^/]*\.(txt|in)", name):
        for number, line in enumerate(file.content.splitlines(), 1):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            # Inline comments require preceding whitespace; URL fragments are not stripped.
            raw = re.split(r"\s+#", line, maxsplit=1)[0].strip()
            add(raw, f"L{number}", "requirements")
    else:
        gaps.append(
            ContextGap(
                file.path,
                "unsupported_declaration_format",
                "File retained without dependency interpretation.",
            )
        )
    return tuple(records), tuple(gaps)

def _eligible(entry: RepositoryInventoryEntry) -> bool:
    name = PurePosixPath(entry.path).name
    return (
        name.endswith(".py")
        or name in _DECLARATION_NAMES
        or bool(re.fullmatch(r"requirements[^/]*\.(txt|in)", name))
    )

class TargetSourceAcquirer:
    """Acquire complete admitted inventory before generic file selection/AST work."""

    def __init__(self, *, session, inventory=None, files=None):
        self.session = session
        self.inventory = inventory or GitHubRepositoryInventoryClient(
            session=self.session
        )
        self.files = files or GitHubRepositoryClient(session=self.session)

    def acquire(
        self,
        repository: str,
        revision: str,
        *,
        max_python_files=200,
        max_bytes=2 * 1024 * 1024,
        changed_paths=(),
        max_file_attempts=None,
    ) -> TargetSourceContext | AcquisitionProblem:
        if (
            type(max_python_files) is not int
            or not 1 <= max_python_files <= 200
            or type(max_bytes) is not int
            or not 1 <= max_bytes <= 2 * 1024 * 1024
        ):
            raise ValueError("Budgets must be positive and within admitted limits.")
        if max_file_attempts is not None and (type(max_file_attempts) is not int or not 1 <= max_file_attempts <= 200):
            raise ValueError("Invalid target file-attempt budget.")
        inventory = self.inventory.acquire(repository, revision)
        if isinstance(inventory, RepositoryInventoryProblem):
            return AcquisitionProblem("inventory", inventory.reason, inventory.detail, inventory.status_code)
        if isinstance(inventory, AcquisitionProblem):
            return inventory
        included = []
        excluded = []
        omitted = []
        gaps = []
        total = 0
        python_count = 0
        attempts = 0
        if inventory.truncated:
            gaps.append(
                ContextGap(
                    None,
                    "inventory_truncated",
                    "Provider tree is incomplete; absence inference is forbidden.",
                )
            )
        changed_paths = set(changed_paths)
        # Ordering is acquisition policy, not evidence of dependency activation.
        # Declaration-first avoids inventory ordering starving the association basis.
        def priority(entry):
            name = PurePosixPath(entry.path).name
            declaration = name in _DECLARATION_NAMES or bool(re.fullmatch(r"requirements[^/]*\.(txt|in)", name))
            return (0 if declaration else 1 if entry.path in changed_paths else 2, entry.path)
        for entry in sorted(inventory.entries, key=priority):
            if entry.kind != "blob":
                if entry.kind == "commit":
                    gaps.append(
                        ContextGap(
                            entry.path,
                            "submodule_unexamined",
                            "Submodule contents are not target tree files.",
                        )
                    )
                continue
            if not _eligible(entry):
                continue
            if entry.mode not in {"100644", "100755"} or any(
                p in _EXCLUDED_DIRECTORIES for p in PurePosixPath(entry.path).parts[:-1]
            ):
                excluded.append(entry.path)
                continue
            if entry.path.endswith(".py"):
                if python_count >= max_python_files:
                    omitted.append(entry.path)
                    continue
                python_count += 1
            if max_file_attempts is not None and attempts >= max_file_attempts:
                omitted.append(entry.path)
                continue
            attempts += 1
            try:
                file = self.files.get_exact_commit_text_file(
                    repository, revision, entry.path
                )
            except GitHubAcquisitionError as exc:
                gaps.append(ContextGap(entry.path, exc.reason, str(exc)))
                continue
            except GitHubResponseError as exc:
                gaps.append(ContextGap(entry.path, "malformed_response", str(exc)))
                continue
            if not isinstance(file, RepositoryTextFile):
                gaps.append(ContextGap(entry.path, file.reason, file.detail))
                continue
            size = len(file.content.encode("utf-8"))
            if total + size > max_bytes:
                omitted.append(entry.path)
                continue
            total += size
            included.append(file)
        if omitted:
            gaps.append(
                ContextGap(
                    None,
                    "input_budget_exhausted",
                    "Omitted eligible files remain visible; no absence inference.",
                )
            )
        imports = []
        refs = []
        declarations = []
        for file in included:
            if file.path.endswith(".py"):
                facts, references, problems = extract_python_facts(file)
                imports.extend(facts)
                refs.extend(references)
                gaps.extend(problems)
            if PurePosixPath(file.path).name in _DECLARATION_NAMES or re.fullmatch(
                r"requirements[^/]*\.(txt|in)", PurePosixPath(file.path).name
            ):
                records, problems = extract_dependency_declarations(file)
                declarations.extend(records)
                gaps.extend(problems)
        local_roots = {
            PurePosixPath(e.path).stem
            for e in inventory.entries
            if e.path.endswith(".py")
            and (
                len(PurePosixPath(e.path).parts) == 1
                or PurePosixPath(e.path).parts[0] == "src"
                and len(PurePosixPath(e.path).parts) == 2
            )
        }
        local_roots.update(
            PurePosixPath(e.path).parts[-2]
            for e in inventory.entries
            if e.path.endswith("/__init__.py") and len(PurePosixPath(e.path).parts) <= 3
        )
        candidates = []
        for fact in imports:
            if fact.relative_level or not fact.module:
                continue
            root = fact.module.split(".")[0]
            matching = [
                d for d in declarations if normalize_package_name(root) == d.package
            ]
            if not matching:
                continue
            if root in local_roots:
                gaps.append(
                    ContextGap(
                        fact.source_id,
                        "local_namespace_collision",
                        "Declared dependency import may name a local module: " + root,
                    )
                )
                continue
            for declaration in matching:
                candidates.append(
                    ImportDependencyCandidate(
                        fact.module, declaration, fact.source_id, fact.line
                    )
                )
        return TargetSourceContext(
            inventory,
            tuple(included),
            tuple(imports),
            tuple(refs),
            tuple(declarations),
            tuple(candidates),
            tuple(excluded),
            tuple(omitted),
            tuple(gaps),
            total,
        )

def file_sha256(file: RepositoryTextFile) -> str:
    return hashlib.sha256(file.content.encode("utf-8")).hexdigest()
