"""Test conservative exact-version extraction from complete admitted ``uv.lock`` files.

The tests begin after normal orchestration has admitted a modified uv.lock and acquired
exact base/head UTF-8 text. They exercise TOML schema admission, package-record validation,
normalized-name grouping, single-record comparison, duplicate-group abstention, and minimal
source provenance. They do not re-test GitHub transport or PR-wide source binding, which
belong to their upstream owners.
"""

from __future__ import annotations

import unittest

from upgradepilot.dependency.change import (
    DependencyChangeEvidenceProblem,
    ExtractedDependencyVersionChange,
)
from upgradepilot.dependency.uv_lock import (
    extract_uv_lock_changes,
    is_modified_uv_lock_file,
)
from upgradepilot.github.pull_request import ChangedFile
from upgradepilot.github.repository import (
    RepositoryTextFile,
    UnavailableRepositoryFile,
)

_REPOSITORY = "example/project"
_PATH = "services/api/uv.lock"
_BASE_REVISION = "a" * 40
_HEAD_REVISION = "b" * 40
_SOURCE = 'source = { registry = "https://pypi.org/simple" }'


def _changed_file(
    *,
    path: str = _PATH,
    status: str = "modified",
) -> ChangedFile:
    """Build one case-neutral changed-file identity for a lockfile."""

    return ChangedFile(
        filename=path,
        status=status,
        additions=1,
        deletions=1,
        changes=2,
        patch=None,
    )


def _exact_file(
    content: str,
    *,
    revision: str,
) -> RepositoryTextFile:
    """Build strong exact text evidence after the provider boundary."""

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


def _lock(*package_tables: str, version: object = 1, revision: object = 0) -> str:
    """Build a minimal controlled uv lock document from package-table bodies."""

    header = f"version = {_toml_scalar(version)}\nrevision = {_toml_scalar(revision)}\n"
    return header + "".join(f"\n[[package]]\n{table.strip()}\n" for table in package_tables)


def _toml_scalar(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _package(
    name: str,
    version: str,
    *,
    source: str = _SOURCE,
    extra: str = "",
) -> str:
    lines = [f'name = "{name}"', f'version = "{version}"']
    if source:
        lines.append(source)
    if extra:
        lines.append(extra.strip())
    return "\n".join(lines)


class UvLockChangeTests(unittest.TestCase):
    """Protect the first bounded ``uv.lock`` comparison contract."""

    def test_admits_only_modified_files_with_exact_uv_lock_basename(self) -> None:
        self.assertTrue(is_modified_uv_lock_file(_changed_file()))
        self.assertTrue(
            is_modified_uv_lock_file(_changed_file(path="deep/nested/uv.lock"))
        )

        for changed_file in (
            _changed_file(status="added"),
            _changed_file(status="deleted"),
            _changed_file(status="renamed"),
            _changed_file(path="uv.lock.backup"),
            _changed_file(path="UV.LOCK"),
            _changed_file(path="/uv.lock"),
            _changed_file(path="a/../uv.lock"),
            _changed_file(path="a//uv.lock"),
            _changed_file(path="a\\uv.lock"),
        ):
            with self.subTest(changed_file=changed_file):
                self.assertFalse(is_modified_uv_lock_file(changed_file))

    def test_extracts_one_transition_and_preserves_minimal_source_evidence(self) -> None:
        base = _lock(
            _package(
                "Demo_Pkg",
                "1.0",
                extra='dependencies = [{ name = "helper-old" }]',
            )
        )
        head = _lock(
            _package(
                "demo-pkg",
                "2.0",
                extra='dependencies = [{ name = "helper-new" }]',
            )
        )

        result = extract_uv_lock_changes(
            _changed_file(),
            _base_file(base),
            _head_file(head),
        )

        self.assertIsInstance(result, ExtractedDependencyVersionChange)
        assert isinstance(result, ExtractedDependencyVersionChange)
        self.assertEqual(result.package, "demo-pkg")
        self.assertEqual(result.normalized_package, "demo-pkg")
        self.assertEqual(result.old_version, "1.0")
        self.assertEqual(result.proposed_version, "2.0")

        evidence = result.source_evidence
        self.assertEqual(evidence.path, _PATH)
        self.assertEqual(evidence.file_format, "uv_lock")
        self.assertEqual(evidence.extraction_method, "exact_base_head_files")

    def test_unavailable_exact_file_blocks_extraction(self) -> None:
        unavailable = UnavailableRepositoryFile(
            repository=_REPOSITORY,
            path=_PATH,
            revision=_BASE_REVISION,
            reason="not_found_or_inaccessible",
            detail="GitHub returned 404.",
        )

        result = extract_uv_lock_changes(
            _changed_file(),
            unavailable,
            _head_file(_lock(_package("demo", "2.0"))),
        )

        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "dependency_file_unavailable")
        self.assertEqual(result.source_evidence, ())

    def test_malformed_toml_is_distinct(self) -> None:
        result = extract_uv_lock_changes(
            _changed_file(),
            _base_file("version = 1\nrevision = 0\n[[package]\n"),
            _head_file(_lock(_package("demo", "2.0"))),
        )

        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "malformed_dependency_file")

    def test_other_lock_schema_version_is_unsupported(self) -> None:
        result = extract_uv_lock_changes(
            _changed_file(),
            _base_file(_lock(_package("demo", "1.0"), version=2)),
            _head_file(_lock(_package("demo", "2.0"), version=2)),
        )

        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "unsupported_uv_lock_schema")

    def test_missing_or_invalid_schema_controls_are_malformed(self) -> None:
        invalid_documents = (
            "version = 1\n[[package]]\nname = \"demo\"\nversion = \"1.0\"\n",
            _lock(_package("demo", "1.0"), revision=-1),
            _lock(_package("demo", "1.0"), revision=True),
            "version = \"1\"\nrevision = 0\n",
        )

        for document in invalid_documents:
            with self.subTest(document=document):
                result = extract_uv_lock_changes(
                    _changed_file(),
                    _base_file(document),
                    _head_file(_lock(_package("demo", "2.0"))),
                )
                assert isinstance(result, DependencyChangeEvidenceProblem)
                self.assertEqual(result.reason, "malformed_dependency_file")

    def test_invalid_package_records_are_explicit(self) -> None:
        invalid_tables = (
            'version = "1.0"\n' + _SOURCE,
            'name = "demo"\n' + _SOURCE,
            'name = "   "\nversion = "1.0"\n' + _SOURCE,
            'name = "demo"\nversion = " 1.0"\n' + _SOURCE,
            'name = "bad name"\nversion = "1.0"\n' + _SOURCE,
        )

        for package_table in invalid_tables:
            with self.subTest(package_table=package_table):
                result = extract_uv_lock_changes(
                    _changed_file(),
                    _base_file(_lock(package_table)),
                    _head_file(_lock(_package("demo", "2.0"))),
                )
                assert isinstance(result, DependencyChangeEvidenceProblem)
                self.assertEqual(result.reason, "invalid_dependency_record")

    def test_unchanged_lockfile_has_version_unchanged_result(self) -> None:
        document = _lock(_package("demo", "1.0"))
        result = extract_uv_lock_changes(
            _changed_file(),
            _base_file(document),
            _head_file(document),
        )

        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "version_unchanged")

    def test_package_addition_or_removal_is_unsupported_structure(self) -> None:
        result = extract_uv_lock_changes(
            _changed_file(),
            _base_file(_lock(_package("existing", "1.0"))),
            _head_file(
                _lock(
                    _package("existing", "1.0"),
                    _package("new-package", "1.0"),
                )
            ),
        )

        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "unsupported_uv_lock_structural_change")

    def test_several_version_transitions_remain_explicit(self) -> None:
        result = extract_uv_lock_changes(
            _changed_file(),
            _base_file(
                _lock(
                    _package("alpha", "1.0"),
                    _package("beta", "1.0"),
                )
            ),
            _head_file(
                _lock(
                    _package("alpha", "2.0"),
                    _package("beta", "2.0"),
                )
            ),
        )

        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "multiple_dependency_version_changes")

    def test_source_change_is_not_silently_paired(self) -> None:
        result = extract_uv_lock_changes(
            _changed_file(),
            _base_file(_lock(_package("demo", "1.0"))),
            _head_file(
                _lock(
                    _package(
                        "demo",
                        "2.0",
                        source='source = { git = "https://example.invalid/demo" }',
                    )
                )
            ),
        )

        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "unsupported_uv_lock_structural_change")

    def test_resolution_marker_change_is_not_silently_paired(self) -> None:
        base = _package(
            "demo",
            "1.0",
            extra='resolution-markers = ["python_full_version < \'3.12\'"]',
        )
        head = _package(
            "demo",
            "2.0",
            extra='resolution-markers = ["python_full_version >= \'3.12\'"]',
        )

        result = extract_uv_lock_changes(
            _changed_file(),
            _base_file(_lock(base)),
            _head_file(_lock(head)),
        )

        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "unsupported_uv_lock_structural_change")

    def test_same_version_nonartifact_change_is_unsupported_structure(self) -> None:
        base = _package(
            "demo",
            "1.0",
            extra='dependencies = [{ name = "helper-a" }]',
        )
        head = _package(
            "demo",
            "1.0",
            extra='dependencies = [{ name = "helper-b" }]',
        )

        result = extract_uv_lock_changes(
            _changed_file(),
            _base_file(_lock(base)),
            _head_file(_lock(head)),
        )

        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "unsupported_uv_lock_structural_change")

    def test_artifact_only_changes_do_not_create_a_transition(self) -> None:
        base = _package(
            "demo",
            "1.0",
            extra=(
                'sdist = { url = "https://files.invalid/old.tar.gz" }\n'
                'wheels = [{ url = "https://files.invalid/old.whl" }]'
            ),
        )
        head = _package(
            "demo",
            "1.0",
            extra=(
                'sdist = { url = "https://files.invalid/new.tar.gz" }\n'
                'wheels = [{ url = "https://files.invalid/new.whl" }]'
            ),
        )

        result = extract_uv_lock_changes(
            _changed_file(),
            _base_file(_lock(base)),
            _head_file(_lock(head)),
        )

        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "version_unchanged")

    def test_unchanged_duplicate_group_does_not_block_clear_transition(self) -> None:
        duplicate_a_base = _package(
            "multi",
            "1.0",
            extra=(
                'resolution-markers = ["python_full_version < \'3.12\'"]\n'
                'wheels = [{ url = "https://files.invalid/a-old.whl" }]'
            ),
        )
        duplicate_b_base = _package(
            "multi",
            "2.0",
            extra=(
                'resolution-markers = ["python_full_version >= \'3.12\'"]\n'
                'wheels = [{ url = "https://files.invalid/b-old.whl" }]'
            ),
        )
        duplicate_a_head = _package(
            "multi",
            "1.0",
            extra=(
                'resolution-markers = ["python_full_version < \'3.12\'"]\n'
                'wheels = [{ url = "https://files.invalid/a-new.whl" }]'
            ),
        )
        duplicate_b_head = _package(
            "multi",
            "2.0",
            extra=(
                'resolution-markers = ["python_full_version >= \'3.12\'"]\n'
                'wheels = [{ url = "https://files.invalid/b-new.whl" }]'
            ),
        )

        result = extract_uv_lock_changes(
            _changed_file(),
            _base_file(
                _lock(
                    duplicate_a_base,
                    duplicate_b_base,
                    _package("target", "3.0"),
                )
            ),
            _head_file(
                _lock(
                    duplicate_b_head,
                    _package("target", "4.0"),
                    duplicate_a_head,
                )
            ),
        )

        self.assertIsInstance(result, ExtractedDependencyVersionChange)
        assert isinstance(result, ExtractedDependencyVersionChange)
        self.assertEqual(result.normalized_package, "target")
        self.assertEqual(result.old_version, "3.0")
        self.assertEqual(result.proposed_version, "4.0")

    def test_changed_duplicate_group_remains_ambiguous(self) -> None:
        base = _lock(
            _package(
                "multi",
                "1.0",
                extra='resolution-markers = ["python_full_version < \'3.12\'"]',
            ),
            _package(
                "multi",
                "2.0",
                extra='resolution-markers = ["python_full_version >= \'3.12\'"]',
            ),
        )
        head = _lock(
            _package(
                "multi",
                "1.1",
                extra='resolution-markers = ["python_full_version < \'3.12\'"]',
            ),
            _package(
                "multi",
                "2.0",
                extra='resolution-markers = ["python_full_version >= \'3.12\'"]',
            ),
        )

        result = extract_uv_lock_changes(
            _changed_file(),
            _base_file(base),
            _head_file(head),
        )

        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "ambiguous_uv_lock_package_records")


if __name__ == "__main__":
    unittest.main()
