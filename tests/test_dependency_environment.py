"""Test dependency-source context distinctions introduced for environment reasoning."""

from __future__ import annotations

import unittest
from unittest.mock import Mock

from upgradepilot.dependency.analysis import DependencyChangeAnalysis, analyze_dependency_change
from upgradepilot.dependency.change import DependencyChangeSourceEvidence
from upgradepilot.dependency.environment import (
    ConstraintsFileDependencyContext,
    PyprojectOptionalExtraDependencyContext,
    RequirementsFileDependencyContext,
    UvLockDependencyContext,
)
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.github.repository import GitHubRepositoryClient, RepositoryTextFile

_REPOSITORY = "example/project"
_BASE_SHA = "a" * 40
_HEAD_SHA = "b" * 40
_BASE_BLOB = "c" * 40
_HEAD_BLOB = "d" * 40


def _identity(*, changed_files: int = 1) -> PullRequestIdentity:
    return PullRequestIdentity(
        repository=_REPOSITORY,
        number=42,
        title="Bump dependency",
        state="open",
        merged=False,
        author="dependency-bot",
        base_ref="main",
        base_sha=_BASE_SHA,
        head_ref="dependency-update",
        head_sha=_HEAD_SHA,
        changed_files=changed_files,
    )


def _changed(path: str, patch: str | None = None) -> ChangedFile:
    return ChangedFile(
        filename=path,
        status="modified",
        additions=1,
        deletions=1,
        changes=2,
        patch=patch,
    )


def _requirement(path: str) -> ChangedFile:
    return _changed(path, "-demo==1.0\n+demo==2.0")


def _lock(version: str) -> str:
    return (
        "version = 1\n"
        "revision = 0\n\n"
        "[[package]]\n"
        'name = "demo"\n'
        f'version = "{version}"\n'
        'source = { registry = "https://pypi.org/simple" }\n'
    )


def _exact(content: str, *, revision: str, blob_sha: str) -> RepositoryTextFile:
    size = len(content.encode("utf-8"))
    return RepositoryTextFile(
        repository=_REPOSITORY,
        path="uv.lock",
        returned_path="uv.lock",
        revision=revision,
        blob_sha=blob_sha,
        reported_byte_count=size,
        decoded_byte_count=size,
        content=content,
    )


def _repository_client() -> Mock:
    client = Mock(spec=GitHubRepositoryClient)
    client.get_pull_request_base_file.return_value = _exact(
        _lock("1.0"), revision=_BASE_SHA, blob_sha=_BASE_BLOB
    )
    client.get_pull_request_head_file.return_value = _exact(
        _lock("2.0"), revision=_HEAD_SHA, blob_sha=_HEAD_BLOB
    )
    return client


class DependencyEnvironmentContextTests(unittest.TestCase):
    def test_requirements_source_is_typed_and_preserves_legacy_projection(self) -> None:
        result = analyze_dependency_change(
            _identity(),
            [_requirement("requirements-dev.txt")],
            _repository_client(),
        )

        self.assertIsInstance(result, DependencyChangeAnalysis)
        assert isinstance(result, DependencyChangeAnalysis)
        self.assertEqual(len(result.source_contexts), 1)
        context = result.source_contexts[0]
        self.assertIsInstance(context, RequirementsFileDependencyContext)
        assert isinstance(context, RequirementsFileDependencyContext)
        self.assertEqual(context.repository, _REPOSITORY)
        self.assertEqual(context.revision, _HEAD_SHA)
        self.assertEqual(context.normalized_package, "demo")
        self.assertEqual(context.source_path, "requirements-dev.txt")
        self.assertEqual(result.direct_requirements_install_path, "requirements-dev.txt")

    def test_constraints_source_remains_distinct_from_direct_requirements(self) -> None:
        result = analyze_dependency_change(
            _identity(),
            [_requirement("constraints/base.txt")],
            _repository_client(),
        )

        self.assertIsInstance(result, DependencyChangeAnalysis)
        assert isinstance(result, DependencyChangeAnalysis)
        self.assertIsInstance(result.source_contexts[0], ConstraintsFileDependencyContext)
        self.assertIsNone(result.direct_requirements_install_path)

    def test_uv_lock_source_is_typed_without_inventing_environment_membership(self) -> None:
        result = analyze_dependency_change(
            _identity(),
            [_changed("uv.lock")],
            _repository_client(),
        )

        self.assertIsInstance(result, DependencyChangeAnalysis)
        assert isinstance(result, DependencyChangeAnalysis)
        self.assertEqual(len(result.source_contexts), 1)
        context = result.source_contexts[0]
        self.assertIsInstance(context, UvLockDependencyContext)
        assert isinstance(context, UvLockDependencyContext)
        self.assertEqual(context.repository, _REPOSITORY)
        self.assertEqual(context.revision, _HEAD_SHA)
        self.assertEqual(context.source_path, "uv.lock")
        self.assertIsNone(result.direct_requirements_install_path)

    def test_optional_extra_context_preserves_spelling_and_normalizes_for_comparison(self) -> None:
        evidence = DependencyChangeSourceEvidence(
            path="pyproject.toml",
            file_format="pyproject_optional_extra",
            extraction_method="exact_base_head_files",
        )
        context = PyprojectOptionalExtraDependencyContext(
            repository=_REPOSITORY,
            revision=_HEAD_SHA,
            normalized_package="demo",
            source_evidence=evidence,
            extra="Dev_Test",
        )

        self.assertEqual(context.extra, "Dev_Test")
        self.assertEqual(context.normalized_extra, "dev-test")

    def test_multiple_requirements_contexts_preserve_both_without_guessing_one_path(self) -> None:
        result = analyze_dependency_change(
            _identity(changed_files=2),
            [
                _requirement("requirements.txt"),
                _requirement("requirements-dev.txt"),
            ],
            _repository_client(),
        )

        self.assertIsInstance(result, DependencyChangeAnalysis)
        assert isinstance(result, DependencyChangeAnalysis)
        self.assertEqual(len(result.source_contexts), 2)
        self.assertTrue(
            all(
                isinstance(context, RequirementsFileDependencyContext)
                for context in result.source_contexts
            )
        )
        self.assertIsNone(result.direct_requirements_install_path)


if __name__ == "__main__":
    unittest.main()
