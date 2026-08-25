"""Test R4 lock-backed reachability from explicit uv selected roots."""

from __future__ import annotations

import unittest

from upgradepilot.dependency.change import DependencyChangeSourceEvidence
from upgradepilot.dependency.environment import UvLockDependencyContext
from upgradepilot.dependency.environment_selection import (
    AllDependencyGroupsSelector,
    DependencyGroupSelector,
    ProjectEnvironmentSelectionDeclaration,
)
from upgradepilot.dependency.uv_reachability import evaluate_uv_selected_root_reachability
from upgradepilot.github.repository import RepositoryTextFile, UnavailableRepositoryFile

_REPOSITORY = "example/project"
_HEAD_SHA = "a" * 40
_OTHER_SHA = "b" * 40


def _lock(content: str, *, path: str = "uv.lock", revision: str = _HEAD_SHA) -> RepositoryTextFile:
    return RepositoryTextFile(
        repository=_REPOSITORY,
        path=path,
        revision=revision,
        content=content,
    )


def _context(
    lock_file: RepositoryTextFile,
    *,
    package: str = "soupsieve",
    repository: str = _REPOSITORY,
    revision: str = _HEAD_SHA,
    source_path: str | None = None,
) -> UvLockDependencyContext:
    return UvLockDependencyContext(
        repository=repository,
        revision=revision,
        normalized_package=package,
        source_evidence=DependencyChangeSourceEvidence(
            path=lock_file.path if source_path is None else source_path,
            file_format="uv_lock",
            extraction_method="exact_base_head_files",
        ),
    )


def _declaration(
    *selectors: object,
    project_root: str | None = None,
    package_scope: str = "bound_project",
) -> ProjectEnvironmentSelectionDeclaration:
    return ProjectEnvironmentSelectionDeclaration(
        manager="uv",
        operation="sync",
        segment_index=0,
        project_root=project_root,
        selectors=selectors,  # type: ignore[arg-type]
        package_scope=package_scope,  # type: ignore[arg-type]
    )


def _s001_lock(*, marker: str = "") -> str:
    marker_text = f', marker = "{marker}"' if marker else ""
    return f'''version = 1
revision = 3

[[package]]
name = "demo"
source = {{ editable = "." }}
[package.dev-dependencies]
docs = [{{ name = "mkdocs-llmstxt" }}]

[[package]]
name = "mkdocs-llmstxt"
version = "0.2.0"
source = {{ registry = "https://pypi.org/simple" }}
dependencies = [{{ name = "beautifulsoup4" }}]

[[package]]
name = "beautifulsoup4"
version = "4.14.2"
source = {{ registry = "https://pypi.org/simple" }}
dependencies = [{{ name = "soupsieve"{marker_text} }}]

[[package]]
name = "soupsieve"
version = "2.8.4"
source = {{ registry = "https://pypi.org/simple" }}
'''


class UvSelectedRootReachabilityTests(unittest.TestCase):
    def test_s001_shape_establishes_transitive_selected_root_reachability_without_pyproject(self) -> None:
        lock_file = _lock(_s001_lock())

        result = evaluate_uv_selected_root_reachability(
            _context(lock_file),
            _declaration(DependencyGroupSelector("docs")),
            lock_file=lock_file,
        )

        self.assertEqual(result.state, "reachable")
        self.assertEqual(result.reachability_kind, "transitive")
        self.assertEqual(result.witness_root, "mkdocs-llmstxt")
        self.assertEqual(
            result.witness_path,
            ("mkdocs-llmstxt", "beautifulsoup4", "soupsieve"),
        )

    def test_direct_selected_root_is_reachable(self) -> None:
        lock_file = _lock(
            '''version = 1
revision = 1
[[package]]
name = "demo"
source = { editable = "." }
[package.dev-dependencies]
docs = [{ name = "soupsieve" }]
[[package]]
name = "soupsieve"
version = "2.8.4"
source = { registry = "https://pypi.org/simple" }
'''
        )

        result = evaluate_uv_selected_root_reachability(
            _context(lock_file),
            _declaration(DependencyGroupSelector("docs")),
            lock_file=lock_file,
        )

        self.assertEqual(result.state, "reachable")
        self.assertEqual(result.reachability_kind, "direct")
        self.assertEqual(result.witness_path, ("soupsieve",))

    def test_complete_bound_project_roots_without_target_are_not_established(self) -> None:
        lock_file = _lock(_s001_lock())

        result = evaluate_uv_selected_root_reachability(
            _context(lock_file, package="other-package"),
            _declaration(DependencyGroupSelector("docs")),
            lock_file=lock_file,
        )

        self.assertEqual(result.state, "not_established")
        self.assertEqual(result.reason, "uv_selected_root_reachability_not_established")
        self.assertIn("complete bounded selected-root domain", result.detail)

    def test_all_workspace_scope_without_current_package_witness_is_unresolved(self) -> None:
        lock_file = _lock(
            '''version = 1
revision = 1
[[package]]
name = "demo"
source = { editable = "." }
[package.dev-dependencies]
docs = [{ name = "pytest" }]
[[package]]
name = "workspace-member"
source = { editable = "packages/member" }
[package.dev-dependencies]
docs = [{ name = "soupsieve" }]
[[package]]
name = "pytest"
version = "9.0"
source = { registry = "https://pypi.org/simple" }
[[package]]
name = "soupsieve"
version = "2.8.4"
source = { registry = "https://pypi.org/simple" }
'''
        )

        result = evaluate_uv_selected_root_reachability(
            _context(lock_file),
            _declaration(
                DependencyGroupSelector("docs"),
                package_scope="all_workspace_packages",
            ),
            lock_file=lock_file,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "uv_selected_root_workspace_scope_not_exhausted")

    def test_project_root_binds_directly_to_matching_local_lock_package(self) -> None:
        lock_file = _lock(
            '''version = 1
revision = 1
[[package]]
name = "root-package"
source = { editable = "." }
[package.dev-dependencies]
docs = [{ name = "pytest" }]
[[package]]
name = "api-package"
source = { editable = "services/api" }
[package.dev-dependencies]
docs = [{ name = "soupsieve" }]
[[package]]
name = "pytest"
version = "9.0"
source = { registry = "https://pypi.org/simple" }
[[package]]
name = "soupsieve"
version = "2.8.4"
source = { registry = "https://pypi.org/simple" }
'''
        )

        result = evaluate_uv_selected_root_reachability(
            _context(lock_file),
            _declaration(DependencyGroupSelector("docs"), project_root="services/api"),
            lock_file=lock_file,
        )

        self.assertEqual(result.state, "reachable")
        self.assertEqual(result.project_root, "services/api")
        self.assertEqual(result.witness_path, ("soupsieve",))

    def test_selector_absent_from_bound_lock_package_is_unresolved(self) -> None:
        lock_file = _lock(_s001_lock())

        result = evaluate_uv_selected_root_reachability(
            _context(lock_file),
            _declaration(DependencyGroupSelector("missing")),
            lock_file=lock_file,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "uv_selected_root_selection_unresolved")

    def test_all_groups_are_taken_from_lock_not_project_metadata(self) -> None:
        lock_file = _lock(
            '''version = 1
revision = 1
[[package]]
name = "demo"
source = { editable = "." }
[package.dev-dependencies]
dev = [{ name = "pytest" }]
docs = [{ name = "soupsieve" }]
[[package]]
name = "pytest"
version = "9.0"
source = { registry = "https://pypi.org/simple" }
[[package]]
name = "soupsieve"
version = "2.8.4"
source = { registry = "https://pypi.org/simple" }
'''
        )

        result = evaluate_uv_selected_root_reachability(
            _context(lock_file),
            _declaration(AllDependencyGroupsSelector()),
            lock_file=lock_file,
        )

        self.assertEqual(result.state, "reachable")
        self.assertEqual(result.reachability_kind, "direct")

    def test_marker_only_path_remains_unresolved(self) -> None:
        lock_file = _lock(_s001_lock(marker="python_version >= '3.12'"))

        result = evaluate_uv_selected_root_reachability(
            _context(lock_file),
            _declaration(DependencyGroupSelector("docs")),
            lock_file=lock_file,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "uv_selected_root_conditional_or_forked_path_unresolved")

    def test_lock_identity_mismatch_or_unavailability_is_unresolved(self) -> None:
        lock_file = _lock(_s001_lock())
        declaration = _declaration(DependencyGroupSelector("docs"))
        unavailable = UnavailableRepositoryFile(
            repository=_REPOSITORY,
            path="uv.lock",
            revision=_HEAD_SHA,
            reason="not_found_or_inaccessible",
            detail="GitHub returned 404.",
        )

        cases = (
            (_context(lock_file, repository="other/project"), lock_file),
            (_context(lock_file), _lock(_s001_lock(), revision=_OTHER_SHA)),
            (_context(lock_file, source_path="other/uv.lock"), lock_file),
            (_context(lock_file), unavailable),
        )
        for context, evidence in cases:
            with self.subTest(context=context, evidence=evidence):
                result = evaluate_uv_selected_root_reachability(
                    context,
                    declaration,
                    lock_file=evidence,
                )
                self.assertEqual(result.state, "unresolved")
                self.assertEqual(result.reason, "uv_selected_root_source_identity_unresolved")


if __name__ == "__main__":
    unittest.main()
