"""Regression tests for valid versionless uv workspace package records.

uv may omit ``version`` for editable workspace members with dynamic versions.
Those records are structural context only: unchanged records may coexist with one
clear registry-package transition, while changed or inconsistently versioned records
must stop extraction explicitly.
"""

from __future__ import annotations

import unittest

from upgradepilot.dependency.change import (
    DependencyChangeEvidenceProblem,
    ExtractedDependencyVersionChange,
)
from upgradepilot.dependency.uv_lock import extract_uv_lock_changes
from upgradepilot.github.repository import RepositoryTextFile

_REPOSITORY = "example/project"
_PATH = "uv.lock"
_BASE_REVISION = "a" * 40
_HEAD_REVISION = "b" * 40


def _exact_file(
    content: str,
    *,
    revision: str,
) -> RepositoryTextFile:
    return RepositoryTextFile(
        repository=_REPOSITORY,
        path=_PATH,
        revision=revision,
        content=content,
    )


def _base_file(content: str) -> RepositoryTextFile:
    return _exact_file(content, revision=_BASE_REVISION)


def _head_file(content: str) -> RepositoryTextFile:
    return _exact_file(content, revision=_HEAD_REVISION)


def _lock(*records: str) -> str:
    return (
        "version = 1\n"
        "revision = 3\n"
        + "".join(f"\n[[package]]\n{record.strip()}\n" for record in records)
    )


def _workspace_record(
    *,
    source_key: str = "editable",
    dependency: str = "helper",
    version: str | None = None,
) -> str:
    lines = ['name = "workspace-package"']
    if version is not None:
        lines.append(f'version = "{version}"')
    lines.extend(
        (
            f'source = {{ {source_key} = "." }}',
            f'dependencies = [{{ name = "{dependency}" }}]',
        )
    )
    return "\n".join(lines)


def _registry_record(version: str) -> str:
    return "\n".join(
        (
            'name = "target-package"',
            f'version = "{version}"',
            'source = { registry = "https://pypi.org/simple" }',
        )
    )


class UvLockVersionlessRecordTests(unittest.TestCase):
    """Protect the local-workspace exception without widening transition logic."""

    def test_unchanged_editable_record_does_not_block_clear_transition(self) -> None:
        result = extract_uv_lock_changes(
            _base_file(
                _lock(
                    _workspace_record(source_key="editable"),
                    _registry_record("1.0"),
                )
            ),
            _head_file(
                _lock(
                    _workspace_record(source_key="editable"),
                    _registry_record("2.0"),
                )
            ),
        )

        self.assertIsInstance(result, ExtractedDependencyVersionChange)
        assert isinstance(result, ExtractedDependencyVersionChange)
        self.assertEqual(result.normalized_package, "target-package")
        self.assertEqual(result.old_version, "1.0")
        self.assertEqual(result.proposed_version, "2.0")

    def test_unchanged_virtual_record_does_not_block_clear_transition(self) -> None:
        result = extract_uv_lock_changes(
            _base_file(
                _lock(
                    _workspace_record(source_key="virtual"),
                    _registry_record("1.0"),
                )
            ),
            _head_file(
                _lock(
                    _workspace_record(source_key="virtual"),
                    _registry_record("2.0"),
                )
            ),
        )

        self.assertIsInstance(result, ExtractedDependencyVersionChange)
        assert isinstance(result, ExtractedDependencyVersionChange)
        self.assertEqual(result.normalized_package, "target-package")

    def test_changed_versionless_record_is_unsupported_structure(self) -> None:
        result = extract_uv_lock_changes(
            _base_file(
                _lock(
                    _workspace_record(dependency="helper-a"),
                    _registry_record("1.0"),
                )
            ),
            _head_file(
                _lock(
                    _workspace_record(dependency="helper-b"),
                    _registry_record("2.0"),
                )
            ),
        )

        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "unsupported_uv_lock_structural_change")

    def test_missing_version_requires_admitted_workspace_source(self) -> None:
        invalid_record = "\n".join(
            (
                'name = "workspace-package"',
                'source = { registry = "https://pypi.org/simple" }',
            )
        )
        result = extract_uv_lock_changes(
            _base_file(_lock(invalid_record)),
            _head_file(_lock(_registry_record("2.0"))),
        )

        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "invalid_dependency_record")

    def test_gaining_or_losing_version_is_unsupported_structure(self) -> None:
        result = extract_uv_lock_changes(
            _base_file(
                _lock(
                    _workspace_record(version=None),
                    _registry_record("1.0"),
                )
            ),
            _head_file(
                _lock(
                    _workspace_record(version="0.1.0"),
                    _registry_record("2.0"),
                )
            ),
        )

        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "unsupported_uv_lock_structural_change")


if __name__ == "__main__":
    unittest.main()
