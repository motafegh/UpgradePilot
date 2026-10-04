"""Acquire exact target source and produce bounded static facts for the API trial.

Start at TargetContextAcquirer.acquire. A validated commit/tree inventory precedes
file selection. Python AST facts and dependency declarations come from acquired
files, never expected-answer paths. These records do not establish runtime import
binding, installed versions, code execution or compatibility. Adapter exploration
consumes explicit import/declaration candidates, not inferred resolved packages.
"""

from __future__ import annotations

import ast
import hashlib
import json
import re
import tomllib
from collections import Counter
from dataclasses import dataclass
from pathlib import PurePosixPath

from packaging.requirements import InvalidRequirement, Requirement
from requests.exceptions import RequestException

from upgradepilot.github.api import (
    GitHubAcquisitionError,
    GitHubApiClient,
    GitHubResponseError,
)
from upgradepilot.github.identity import validate_commit_sha, validate_repository
from upgradepilot.github.repository import GitHubRepositoryClient, RepositoryTextFile
from upgradepilot.package_identity import normalize_package_name
from upgradepilot.repository_path import repository_relative_parts

from .api_change_source_acquisition import AcquisitionProblem, TrialPublicSession

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
class InventoryEntry:
    path: str
    kind: str
    mode: str


@dataclass(frozen=True)
class TargetInventory:
    repository: str
    revision: str
    tree_sha: str
    entries: tuple[InventoryEntry, ...]
    truncated: bool


class TrialRepositoryInventoryClient(GitHubApiClient):
    """Validate immutable commit/tree correspondence without product adoption."""

    def _get_json_object(self, url, *, resource, params=None):
        """Bound tree/commit JSON before parsing; keep provider HTTP classification."""
        response = None
        try:
            response = self._session.get(
                url,
                headers=self._headers,
                timeout=self._timeout,
                params=params,
                stream=True,
            )
            self._raise_for_status(response, resource=resource)
            body = bytearray()
            for chunk in response.iter_content(chunk_size=8192):
                body.extend(chunk)
                if len(body) > 8 * 1024 * 1024:
                    raise GitHubResponseError(
                        "Inventory JSON exceeds 8 MiB; completeness is not established."
                    )
            data = json.loads(body)
            if not isinstance(data, dict):
                raise GitHubResponseError("Inventory JSON must be an object.")
            return data
        except RequestException as exc:
            raise GitHubAcquisitionError(
                "Inventory transport failed.", reason="transport_error"
            ) from exc
        except json.JSONDecodeError as exc:
            raise GitHubResponseError("Malformed inventory JSON.") from exc
        finally:
            if response is not None:
                response.close()

    def acquire(
        self, repository: str, revision: str
    ) -> TargetInventory | AcquisitionProblem:
        repository = validate_repository(repository)
        revision = validate_commit_sha(revision)
        try:
            commit = self._get_json_object(
                self.api_url(f"/repos/{repository}/git/commits/{revision}"),
                resource="target-git-commit",
            )
            if commit.get("sha", "").casefold() != revision:
                return AcquisitionProblem(
                    "inventory",
                    "identity_mismatch",
                    "Returned commit differs from exact target revision.",
                )
            tree_sha = validate_commit_sha(commit["tree"]["sha"])
            tree = self._get_json_object(
                self.api_url(f"/repos/{repository}/git/trees/{tree_sha}"),
                resource="target-git-tree",
                params={"recursive": 1},
            )
            if tree.get("sha", "").casefold() != tree_sha:
                return AcquisitionProblem(
                    "inventory",
                    "identity_mismatch",
                    "Returned tree differs from exact commit tree.",
                )
            if type(tree.get("truncated")) is not bool or not isinstance(
                tree.get("tree"), list
            ):
                raise ValueError(
                    "Tree must contain entries and explicit truncation state."
                )
            entries = []
            seen = set()
            for raw in tree["tree"]:
                path = raw["path"]
                kind = raw["type"]
                mode = raw["mode"]
                if (
                    repository_relative_parts(path) is None
                    or path in seen
                    or kind not in {"blob", "tree", "commit"}
                    or not isinstance(mode, str)
                ):
                    raise ValueError("Malformed, duplicate or unsupported tree entry.")
                seen.add(path)
                entries.append(InventoryEntry(path, kind, mode))
            return TargetInventory(
                repository,
                revision,
                tree_sha,
                tuple(sorted(entries, key=lambda e: e.path)),
                tree["truncated"],
            )
        except GitHubAcquisitionError as exc:
            return AcquisitionProblem(
                "inventory", exc.reason, str(exc), exc.status_code
            )
        except (
            GitHubResponseError,
            KeyError,
            ValueError,
            TypeError,
            AttributeError,
        ) as exc:
            return AcquisitionProblem("inventory", "malformed_response", str(exc))


@dataclass(frozen=True)
class ImportFact:
    source_id: str
    line: int
    module: str
    member: str | None
    alias: str | None
    relative_level: int
    module_level: bool


@dataclass(frozen=True)
class ReferenceFact:
    source_id: str
    line: int
    kind: str
    expression: str
    lexical_import: str | None
    binding_limit: str | None
    keyword_names: tuple[str, ...] = ()
    positional_count: int = 0


@dataclass(frozen=True)
class DependencyDeclaration:
    source_id: str
    location: str
    raw: str
    package: str
    specifier: str
    extras: tuple[str, ...]
    marker: str | None
    group: str


@dataclass(frozen=True)
class ImportDependencyCandidate:
    imported_module: str
    declaration: DependencyDeclaration
    import_source_id: str
    import_line: int
    # Namespace/distribution equality is a candidate mechanism, not mapping proof.
    basis: str = "same_name_import_and_declared_distribution"


@dataclass(frozen=True)
class ContextGap:
    path: str | None
    reason: str
    detail: str


@dataclass(frozen=True)
class TargetContext:
    inventory: TargetInventory
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
        "only_unique_unshadowed_module_level_imports_bound",
        "local_conditional_and_assignment_aliases_unresolved",
    )


def source_id(file: RepositoryTextFile) -> str:
    return f"{file.repository}@{file.revision}:{file.path}"


def _dotted_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        parent = _dotted_name(node.value)
        return f"{parent}.{node.attr}" if parent else None
    return None


def extract_python_facts(
    file: RepositoryTextFile,
) -> tuple[tuple[ImportFact, ...], tuple[ReferenceFact, ...], tuple[ContextGap, ...]]:
    """Resolve lexical calls only through unique, unshadowed top-level imports.

    Conservative file-wide rebinding checks intentionally lose some precision:
    local imports, parameters, assignment aliases and dynamic attribute receivers
    remain unresolved. Conditional imports are facts but not assumed bindings.
    This avoids attributing a shadowed name to a dependency simply because an
    import with that spelling exists elsewhere in the file.
    """
    try:
        tree = ast.parse(file.content, filename=file.path)
    except (SyntaxError, ValueError, RecursionError) as exc:
        return (), (), (ContextGap(file.path, "python_parse_failed", str(exc)),)
    identity = source_id(file)
    facts = []
    bindings = []
    top_level_ids = {id(n) for n in tree.body}
    blocked = set()
    has_star = False
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, (ast.Store, ast.Del)):
            blocked.add(node.id)
        if isinstance(node, ast.arg):
            blocked.add(node.arg)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            blocked.add(node.name)
        if isinstance(node, ast.ExceptHandler) and node.name:
            blocked.add(node.name)
        if isinstance(node, (ast.Global, ast.Nonlocal)):
            blocked.update(node.names)
        if isinstance(node, (ast.MatchAs, ast.MatchStar)) and node.name:
            blocked.add(node.name)
        if isinstance(node, ast.MatchMapping) and node.rest:
            blocked.add(node.rest)
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                is_top = id(node) in top_level_ids
                if isinstance(node, ast.Import):
                    facts.append(
                        ImportFact(
                            identity,
                            node.lineno,
                            alias.name,
                            None,
                            alias.asname,
                            0,
                            is_top,
                        )
                    )
                    name = alias.asname or alias.name.split(".")[0]
                    target = alias.name if alias.asname else name
                else:
                    facts.append(
                        ImportFact(
                            identity,
                            node.lineno,
                            node.module or "",
                            alias.name,
                            alias.asname,
                            node.level,
                            is_top,
                        )
                    )
                    name = alias.asname or alias.name
                    target = (
                        f"{node.module}.{alias.name}" if node.module else alias.name
                    )
                    if alias.name == "*":
                        has_star = True
                    if node.level or alias.name == "*":
                        blocked.add(name)
                if is_top:
                    bindings.append((name, target))
                else:
                    blocked.add(name)
    counts = Counter(name for name, _ in bindings)
    stable = {
        name: target
        for name, target in bindings
        if counts[name] == 1 and name not in blocked and not has_star
    }
    refs = []

    def add(node, kind, expression_node):
        name = _dotted_name(expression_node)
        imported = None
        if name:
            root, *suffix = name.split(".")
            if root in stable:
                imported = ".".join((stable[root], *suffix))
        refs.append(
            ReferenceFact(
                identity,
                node.lineno,
                kind,
                ast.get_source_segment(file.content, expression_node) or "",
                imported,
                None if imported else "binding_not_established",
                tuple(k.arg or "**" for k in node.keywords)
                if isinstance(node, ast.Call)
                else (),
                len(node.args) if isinstance(node, ast.Call) else 0,
            )
        )

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            add(node, "call", node.func)
        elif isinstance(node, ast.ClassDef):
            for base in node.bases:
                add(node, "class_base", base)
    return (
        tuple(sorted(facts, key=lambda f: f.line)),
        tuple(sorted(refs, key=lambda r: r.line)),
        (),
    )


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


def _eligible(entry: InventoryEntry) -> bool:
    name = PurePosixPath(entry.path).name
    return (
        name.endswith(".py")
        or name in _DECLARATION_NAMES
        or bool(re.fullmatch(r"requirements[^/]*\.(txt|in)", name))
    )


class TargetContextAcquirer:
    """Acquire complete admitted inventory before generic file selection/AST work."""

    def __init__(self, *, session=None, inventory=None, files=None):
        self.session = session or TrialPublicSession()
        self.inventory = inventory or TrialRepositoryInventoryClient(
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
    ) -> TargetContext | AcquisitionProblem:
        if (
            type(max_python_files) is not int
            or not 1 <= max_python_files <= 200
            or type(max_bytes) is not int
            or not 1 <= max_bytes <= 2 * 1024 * 1024
        ):
            raise ValueError("Budgets must be positive and within admitted limits.")
        inventory = self.inventory.acquire(repository, revision)
        if isinstance(inventory, AcquisitionProblem):
            return inventory
        included = []
        excluded = []
        omitted = []
        gaps = []
        total = 0
        python_count = 0
        if inventory.truncated:
            gaps.append(
                ContextGap(
                    None,
                    "inventory_truncated",
                    "Provider tree is incomplete; absence inference is forbidden.",
                )
            )
        for entry in inventory.entries:
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
        return TargetContext(
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
