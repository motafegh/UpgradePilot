"""Protect the shared bounded structural admission used by both uv semantic consumers.

These tests intentionally stop below transition comparison and reachability traversal except for
one regression that proves the known versionless-record disagreement can no longer reappear in
the reachability consumer. The shared parser establishes format/record truth; it does not
establish that a package changed or that any selected root reaches it.
"""

from __future__ import annotations

import unittest

from upgradepilot.dependency.change import (
    DependencyChangeEvidenceProblem,
    DependencyChangeSourceEvidence,
)
from upgradepilot.dependency.environment import UvLockDependencyContext
from upgradepilot.dependency.environment_selection import (
    DependencyGroupSelector,
    ProjectEnvironmentSelectionDeclaration,
)
from upgradepilot.dependency.uv_lock import extract_uv_lock_changes
from upgradepilot.dependency.uv_lock_structure import (
    UvLockStructure,
    UvLockStructureProblem,
    parse_uv_lock_structure,
)
from upgradepilot.dependency.uv_reachability import evaluate_uv_selected_root_reachability
from upgradepilot.github.repository import RepositoryTextFile

_REPOSITORY = "example/project"
_BASE_REVISION = "a" * 40
_HEAD_REVISION = "b" * 40


def _file(path: str, content: str, *, revision: str = _HEAD_REVISION) -> RepositoryTextFile:
    return RepositoryTextFile(
        repository=_REPOSITORY,
        path=path,
        revision=revision,
        content=content,
    )


def _lock(*records: str, version: str = "1", revision: str = "3") -> str:
    return (
        f"version = {version}\nrevision = {revision}\n"
        + "".join(f"\n[[package]]\n{record.strip()}\n" for record in records)
    )


def _registry_record(name: str, version: str) -> str:
    return "\n".join(
        (
            f'name = "{name}"',
            f'version = "{version}"',
            'source = { registry = "https://pypi.org/simple" }',
        )
    )


def _versionless_record(*, source: str) -> str:
    return "\n".join(
        (
            'name = "demo"',
            f"source = {source}",
            '[package.dev-dependencies]',
            'docs = [{ name = "target" }]',
        )
    )


class UvLockStructureTests(unittest.TestCase):
    """Protect the earliest sufficient owner of shared uv.lock structural truth."""

    def test_parses_versionless_workspace_record_and_preserves_repeated_records(self) -> None:
        result = parse_uv_lock_structure(
            _lock(
                _versionless_record(source='{ editable = "." }'),
                _registry_record("multi", "1.0"),
                _registry_record("multi", "2.0"),
            )
        )

        self.assertIsInstance(result, UvLockStructure)
        assert isinstance(result, UvLockStructure)
        self.assertEqual(result.schema_version, 1)
        self.assertEqual(result.revision, 3)
        self.assertEqual(result.packages[0].normalized_package, "demo")
        self.assertIsNone(result.packages[0].version)
        self.assertEqual(result.packages[0].source, {"editable": "."})
        self.assertEqual(len(result.by_name["multi"]), 2)
        self.assertEqual(
            tuple(record.version for record in result.by_name["multi"]),
            ("1.0", "2.0"),
        )

    def test_versionless_registry_record_is_rejected_once_for_all_consumers(self) -> None:
        invalid_lock = _lock(
            _versionless_record(
                source='{ registry = "https://pypi.org/simple" }'
            ),
            _registry_record("target", "2.0"),
        )

        structural = parse_uv_lock_structure(invalid_lock)
        self.assertIsInstance(structural, UvLockStructureProblem)
        assert isinstance(structural, UvLockStructureProblem)
        self.assertEqual(structural.code, "invalid_uv_lock_package_record")

        transition = extract_uv_lock_changes(
            _file("uv.lock", invalid_lock, revision=_BASE_REVISION),
            _file("uv.lock", _lock(_registry_record("target", "2.0"))),
        )
        self.assertIsInstance(transition, DependencyChangeEvidenceProblem)
        assert isinstance(transition, DependencyChangeEvidenceProblem)
        self.assertEqual(transition.reason, "invalid_dependency_record")

        lock_file = _file("uv.lock", invalid_lock)
        context = UvLockDependencyContext(
            repository=_REPOSITORY,
            revision=_HEAD_REVISION,
            normalized_package="target",
            source_evidence=DependencyChangeSourceEvidence(
                path="uv.lock",
                file_format="uv_lock",
                extraction_method="exact_base_head_files",
            ),
        )
        declaration = ProjectEnvironmentSelectionDeclaration(
            manager="uv",
            operation="sync",
            segment_index=0,
            project_root=None,
            selectors=(DependencyGroupSelector("docs"),),
        )

        reachability = evaluate_uv_selected_root_reachability(
            context,
            declaration,
            lock_file=lock_file,
        )
        self.assertEqual(reachability.state, "unresolved")
        self.assertEqual(
            reachability.reason,
            "uv_selected_root_lock_structure_unresolved",
        )

    def test_boolean_schema_version_is_malformed_not_schema_one(self) -> None:
        result = parse_uv_lock_structure(
            _lock(_registry_record("target", "1.0"), version="true")
        )

        self.assertIsInstance(result, UvLockStructureProblem)
        assert isinstance(result, UvLockStructureProblem)
        self.assertEqual(result.code, "malformed_uv_lock")

    def test_other_integer_schema_version_is_explicitly_unsupported(self) -> None:
        result = parse_uv_lock_structure(
            _lock(_registry_record("target", "1.0"), version="2")
        )

        self.assertIsInstance(result, UvLockStructureProblem)
        assert isinstance(result, UvLockStructureProblem)
        self.assertEqual(result.code, "unsupported_uv_lock_schema")

    def test_untrimmed_package_version_is_invalid_structural_evidence(self) -> None:
        result = parse_uv_lock_structure(
            _lock(
                '''name = "target"
version = " 1.0"
source = { registry = "https://pypi.org/simple" }'''
            )
        )

        self.assertIsInstance(result, UvLockStructureProblem)
        assert isinstance(result, UvLockStructureProblem)
        self.assertEqual(result.code, "invalid_uv_lock_package_record")


if __name__ == "__main__":
    unittest.main()
