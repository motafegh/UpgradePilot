"""Test lock-backed membership for explicitly selected uv project environments."""

from __future__ import annotations

import unittest

from upgradepilot.dependency.change import DependencyChangeSourceEvidence
from upgradepilot.dependency.environment import UvLockDependencyContext
from upgradepilot.dependency.environment_selection import (
    AllDependencyGroupsSelector,
    AllOptionalExtrasSelector,
    DependencyGroupSelector,
    OptionalExtraSelector,
    ProjectEnvironmentSelectionDeclaration,
)
from upgradepilot.dependency.uv_membership import evaluate_uv_selected_environment_membership
from upgradepilot.github.repository import RepositoryTextFile, UnavailableRepositoryFile

_REPOSITORY = "example/project"
_HEAD_SHA = "a" * 40
_OTHER_SHA = "b" * 40


def _file(
    path: str,
    content: str,
    *,
    repository: str = _REPOSITORY,
    revision: str = _HEAD_SHA,
) -> RepositoryTextFile:
    """Build strong exact text evidence after the GitHub acquisition boundary."""

    return RepositoryTextFile(
        repository=repository,
        path=path,
        revision=revision,
        content=content,
    )


def _context(
    lock: RepositoryTextFile,
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
            path=lock.path if source_path is None else source_path,
            file_format="uv_lock",
            extraction_method="exact_base_head_files",
        ),
    )


def _declaration(*selectors: object, project_root: str | None = None):
    return ProjectEnvironmentSelectionDeclaration(
        manager="uv",
        operation="sync",
        segment_index=0,
        project_root=project_root,
        selectors=selectors,  # type: ignore[arg-type]
    )


def _project(*, groups: str = 'docs = ["mkdocs-llmstxt"]', extras: str = "") -> str:
    optional = f"\n[project.optional-dependencies]\n{extras}\n" if extras else ""
    return f'''[project]
name = "demo"
{optional}
[dependency-groups]
{groups}
'''


def _s001_lock(*, soup_marker: str = "", extra_edge: bool = False) -> str:
    marker = f', marker = "{soup_marker}"' if soup_marker else ""
    imaging = ', extra = ["imaging"]' if extra_edge else ""
    mkdocs_dependency = (
        '{ name = "mkdocs-material"' + imaging + " }"
        if extra_edge
        else '{ name = "beautifulsoup4" }'
    )
    material_package = '''
[[package]]
name = "mkdocs-material"
version = "9.0"
source = { registry = "https://pypi.org/simple" }
[package.optional-dependencies]
imaging = [
  { name = "beautifulsoup4" },
]
''' if extra_edge else ""
    return f'''version = 1
revision = 3

[[package]]
name = "demo"
source = {{ editable = "." }}
[package.dev-dependencies]
docs = [
  {{ name = "mkdocs-llmstxt" }},
]

[[package]]
name = "mkdocs-llmstxt"
version = "0.2.0"
source = {{ registry = "https://pypi.org/simple" }}
dependencies = [
  {mkdocs_dependency},
]
{material_package}
[[package]]
name = "beautifulsoup4"
version = "4.14.2"
source = {{ registry = "https://pypi.org/simple" }}
dependencies = [
  {{ name = "soupsieve"{marker} }},
]

[[package]]
name = "soupsieve"
version = "2.8.4"
source = {{ registry = "https://pypi.org/simple" }}
'''


class UvSelectedEnvironmentMembershipTests(unittest.TestCase):
    def test_s001_shape_establishes_transitive_docs_membership(self) -> None:
        project = _file("pyproject.toml", _project())
        lock = _file("uv.lock", _s001_lock())

        result = evaluate_uv_selected_environment_membership(
            _context(lock),
            _declaration(DependencyGroupSelector("docs")),
            project_file=project,
            lock_file=lock,
        )

        self.assertEqual(result.state, "member")
        self.assertEqual(result.membership_kind, "transitive")
        self.assertEqual(result.witness_root, "mkdocs-llmstxt")
        self.assertEqual(
            result.witness_path,
            ("mkdocs-llmstxt", "beautifulsoup4", "soupsieve"),
        )

    def test_changed_package_can_be_direct_selected_group_root(self) -> None:
        project = _file(
            "pyproject.toml",
            _project(groups='docs = ["soupsieve"]'),
        )
        lock_text = _s001_lock().replace(
            'docs = [\n  { name = "mkdocs-llmstxt" },\n]',
            'docs = [\n  { name = "soupsieve" },\n]',
        )
        lock = _file("uv.lock", lock_text)

        result = evaluate_uv_selected_environment_membership(
            _context(lock),
            _declaration(DependencyGroupSelector("docs")),
            project_file=project,
            lock_file=lock,
        )

        self.assertEqual(result.state, "member")
        self.assertEqual(result.membership_kind, "direct")
        self.assertEqual(result.witness_path, ("soupsieve",))

    def test_complete_explicit_roots_without_target_are_not_established_not_absent(self) -> None:
        project = _file("pyproject.toml", _project())
        lock = _file("uv.lock", _s001_lock())

        result = evaluate_uv_selected_environment_membership(
            _context(lock, package="other-package"),
            _declaration(DependencyGroupSelector("docs")),
            project_file=project,
            lock_file=lock,
        )

        self.assertEqual(result.state, "not_established")
        self.assertIn("not a runtime", result.detail)

    def test_marker_dependent_only_path_is_unresolved(self) -> None:
        project = _file("pyproject.toml", _project())
        lock = _file(
            "uv.lock",
            _s001_lock(soup_marker="python_version >= '3.12'"),
        )

        result = evaluate_uv_selected_environment_membership(
            _context(lock),
            _declaration(DependencyGroupSelector("docs")),
            project_file=project,
            lock_file=lock,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(
            result.reason,
            "uv_membership_conditional_or_forked_path_unresolved",
        )

    def test_activated_dependency_extra_is_traversed(self) -> None:
        project = _file("pyproject.toml", _project())
        lock = _file("uv.lock", _s001_lock(extra_edge=True))

        result = evaluate_uv_selected_environment_membership(
            _context(lock),
            _declaration(DependencyGroupSelector("docs")),
            project_file=project,
            lock_file=lock,
        )

        self.assertEqual(result.state, "member")
        self.assertEqual(
            result.witness_path,
            ("mkdocs-llmstxt", "mkdocs-material", "beautifulsoup4", "soupsieve"),
        )

    def test_optional_extra_root_selection_is_supported(self) -> None:
        project = _file(
            "pyproject.toml",
            _project(groups='dev = ["pytest"]', extras='docs = ["soupsieve"]'),
        )
        lock_text = '''version = 1
revision = 1
[[package]]
name = "demo"
source = { editable = "." }
[package.optional-dependencies]
docs = [{ name = "soupsieve" }]
[package.dev-dependencies]
dev = [{ name = "pytest" }]
[[package]]
name = "soupsieve"
version = "2.8.4"
source = { registry = "https://pypi.org/simple" }
[[package]]
name = "pytest"
version = "9.0"
source = { registry = "https://pypi.org/simple" }
'''
        lock = _file("uv.lock", lock_text)

        result = evaluate_uv_selected_environment_membership(
            _context(lock),
            _declaration(OptionalExtraSelector("docs")),
            project_file=project,
            lock_file=lock,
        )

        self.assertEqual(result.state, "member")
        self.assertEqual(result.membership_kind, "direct")

    def test_all_groups_and_all_extras_union_only_explicit_categories(self) -> None:
        project = _file(
            "pyproject.toml",
            _project(
                groups='dev = ["pytest"]\ndocs = ["mkdocs-llmstxt"]',
                extras='email = ["soupsieve"]',
            ),
        )
        lock_text = '''version = 1
revision = 1
[[package]]
name = "demo"
source = { editable = "." }
[package.optional-dependencies]
email = [{ name = "soupsieve" }]
[package.dev-dependencies]
dev = [{ name = "pytest" }]
docs = [{ name = "mkdocs-llmstxt" }]
[[package]]
name = "soupsieve"
version = "2.8.4"
source = { registry = "https://pypi.org/simple" }
[[package]]
name = "pytest"
version = "9.0"
source = { registry = "https://pypi.org/simple" }
[[package]]
name = "mkdocs-llmstxt"
version = "0.2.0"
source = { registry = "https://pypi.org/simple" }
'''
        lock = _file("uv.lock", lock_text)

        result = evaluate_uv_selected_environment_membership(
            _context(lock),
            _declaration(AllDependencyGroupsSelector(), AllOptionalExtrasSelector()),
            project_file=project,
            lock_file=lock,
        )

        self.assertEqual(result.state, "member")
        self.assertEqual(result.membership_kind, "direct")

    def test_selected_group_must_exist_in_exact_project_and_bound_lock_package(self) -> None:
        project = _file("pyproject.toml", _project())
        lock = _file("uv.lock", _s001_lock())

        result = evaluate_uv_selected_environment_membership(
            _context(lock),
            _declaration(DependencyGroupSelector("missing")),
            project_file=project,
            lock_file=lock,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "uv_membership_selected_roots_unresolved")

    def test_repeated_intermediate_package_without_edge_discriminator_is_unresolved(self) -> None:
        project = _file("pyproject.toml", _project())
        lock_text = _s001_lock().replace(
            '[[package]]\nname = "beautifulsoup4"\nversion = "4.14.2"',
            '''[[package]]
name = "beautifulsoup4"
version = "4.13.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [{ name = "soupsieve" }]

[[package]]
name = "beautifulsoup4"
version = "4.14.2"''',
        )
        lock = _file("uv.lock", lock_text)

        result = evaluate_uv_selected_environment_membership(
            _context(lock),
            _declaration(DependencyGroupSelector("docs")),
            project_file=project,
            lock_file=lock,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(
            result.reason,
            "uv_membership_conditional_or_forked_path_unresolved",
        )

    def test_version_discriminator_can_select_one_repeated_record(self) -> None:
        project = _file("pyproject.toml", _project())
        lock_text = _s001_lock().replace(
            '{ name = "beautifulsoup4" }',
            '{ name = "beautifulsoup4", version = "4.14.2" }',
            1,
        ).replace(
            '[[package]]\nname = "beautifulsoup4"\nversion = "4.14.2"',
            '''[[package]]
name = "beautifulsoup4"
version = "4.13.0"
source = { registry = "https://pypi.org/simple" }
dependencies = []

[[package]]
name = "beautifulsoup4"
version = "4.14.2"''',
        )
        lock = _file("uv.lock", lock_text)

        result = evaluate_uv_selected_environment_membership(
            _context(lock),
            _declaration(DependencyGroupSelector("docs")),
            project_file=project,
            lock_file=lock,
        )

        self.assertEqual(result.state, "member")
        self.assertEqual(result.witness_path[-1], "soupsieve")

    def test_cycle_is_safe_and_does_not_create_false_membership(self) -> None:
        project = _file("pyproject.toml", _project())
        lock_text = '''version = 1
revision = 1
[[package]]
name = "demo"
source = { editable = "." }
[package.dev-dependencies]
docs = [{ name = "a" }]
[[package]]
name = "a"
version = "1"
source = { registry = "https://pypi.org/simple" }
dependencies = [{ name = "b" }]
[[package]]
name = "b"
version = "1"
source = { registry = "https://pypi.org/simple" }
dependencies = [{ name = "a" }]
'''
        lock = _file("uv.lock", lock_text)

        result = evaluate_uv_selected_environment_membership(
            _context(lock),
            _declaration(DependencyGroupSelector("docs")),
            project_file=project,
            lock_file=lock,
        )

        self.assertEqual(result.state, "not_established")

    def test_project_root_binding_supports_nested_workspace_member(self) -> None:
        project = _file(
            "services/api/pyproject.toml",
            _project(groups='docs = ["soupsieve"]'),
        )
        lock_text = '''version = 1
revision = 1
[[package]]
name = "demo"
source = { editable = "services/api" }
[package.dev-dependencies]
docs = [{ name = "soupsieve" }]
[[package]]
name = "soupsieve"
version = "2.8.4"
source = { registry = "https://pypi.org/simple" }
'''
        lock = _file("uv.lock", lock_text)

        result = evaluate_uv_selected_environment_membership(
            _context(lock),
            _declaration(DependencyGroupSelector("docs"), project_root="services/api"),
            project_file=project,
            lock_file=lock,
        )

        self.assertEqual(result.state, "member")

    def test_exact_sources_must_match_dependency_context_repository_revision_and_path(self) -> None:
        project = _file("pyproject.toml", _project())
        lock = _file("uv.lock", _s001_lock())
        declaration = _declaration(DependencyGroupSelector("docs"))

        cases = (
            (
                _context(lock, repository="other/project"),
                project,
                lock,
            ),
            (
                _context(lock),
                _file("pyproject.toml", _project(), revision=_OTHER_SHA),
                lock,
            ),
            (
                _context(lock, source_path="other/uv.lock"),
                project,
                lock,
            ),
        )

        for context, project_file, lock_file in cases:
            with self.subTest(context=context, project_file=project_file, lock_file=lock_file):
                result = evaluate_uv_selected_environment_membership(
                    context,
                    declaration,
                    project_file=project_file,
                    lock_file=lock_file,
                )
                self.assertEqual(result.state, "unresolved")
                self.assertEqual(result.reason, "uv_membership_source_identity_unresolved")

    def test_static_declaration_project_root_must_match_exact_project_location(self) -> None:
        project = _file(
            "services/api/pyproject.toml",
            _project(groups='docs = ["soupsieve"]'),
        )
        lock = _file(
            "uv.lock",
            '''version = 1
revision = 1
[[package]]
name = "demo"
source = { editable = "services/api" }
[package.dev-dependencies]
docs = [{ name = "soupsieve" }]
[[package]]
name = "soupsieve"
version = "2.8.4"
source = { registry = "https://pypi.org/simple" }
''',
        )

        result = evaluate_uv_selected_environment_membership(
            _context(lock),
            _declaration(DependencyGroupSelector("docs"), project_root="services/web"),
            project_file=project,
            lock_file=lock,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "uv_membership_source_identity_unresolved")

    def test_unavailable_exact_source_blocks_membership_composition(self) -> None:
        project = _file("pyproject.toml", _project())
        lock = _file("uv.lock", _s001_lock())
        unavailable_lock = UnavailableRepositoryFile(
            repository=_REPOSITORY,
            path="uv.lock",
            revision=_HEAD_SHA,
            reason="not_found_or_inaccessible",
            detail="GitHub returned 404.",
        )

        result = evaluate_uv_selected_environment_membership(
            _context(lock),
            _declaration(DependencyGroupSelector("docs")),
            project_file=project,
            lock_file=unavailable_lock,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "uv_membership_source_identity_unresolved")


if __name__ == "__main__":
    unittest.main()
