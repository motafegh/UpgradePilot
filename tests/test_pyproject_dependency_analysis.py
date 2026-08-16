"""Test PR-wide admission of exact pyproject optional-extra dependency evidence."""

from __future__ import annotations

import unittest
from unittest.mock import Mock

from upgradepilot.dependency.analysis import DependencyChangeAnalysis, analyze_dependency_change
from upgradepilot.dependency.change import DependencyChangeProblem
from upgradepilot.dependency.environment import (
    PyprojectOptionalExtraDependencyContext,
    RequirementsFileDependencyContext,
)
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.github.repository import GitHubRepositoryClient, RepositoryTextFile

_REPOSITORY = "dragfly/dictare"
_BASE_SHA = "9921be73b4a55ba54b7b1f46ba424ada0d38aaa7"
_HEAD_SHA = "62d65da86f902d4b54a9d87e9ced5ff2e1f61e55"
_BASE_BLOB = "c" * 40
_HEAD_BLOB = "d" * 40


def _identity(*, changed_files: int = 1) -> PullRequestIdentity:
    return PullRequestIdentity(
        repository=_REPOSITORY,
        number=34,
        title="Bump NumPy in MLX extra",
        state="open",
        merged=False,
        author="dependency-bot",
        base_ref="main",
        base_sha=_BASE_SHA,
        head_ref="dependency-update",
        head_sha=_HEAD_SHA,
        changed_files=changed_files,
    )


def _changed(*, status: str = "modified") -> ChangedFile:
    return ChangedFile(
        filename="pyproject.toml",
        status=status,
        additions=1,
        deletions=1,
        changes=2,
        patch=None,
    )


def _requirement_change() -> ChangedFile:
    return ChangedFile(
        filename="requirements.txt",
        status="modified",
        additions=1,
        deletions=1,
        changes=2,
        patch="-numpy==1.26.4\n+numpy==2.4.6",
    )


def _content(version: str, *, name: str = "dictare") -> str:
    return f'''[project]
name = "{name}"
dependencies = ["numpy>=1.24.0"]

[project.optional-dependencies]
dev = ["pytest>=8.0.0"]
mlx = [
  "mlx==0.30.4",
  "numpy=={version}",
  "soundfile>=0.12.0",
]
'''


def _exact(content: str, *, revision: str, blob_sha: str) -> RepositoryTextFile:
    size = len(content.encode("utf-8"))
    return RepositoryTextFile(
        repository=_REPOSITORY,
        path="pyproject.toml",
        returned_path="pyproject.toml",
        revision=revision,
        blob_sha=blob_sha,
        reported_byte_count=size,
        decoded_byte_count=size,
        content=content,
    )


def _client(*, optional_change: bool = True) -> Mock:
    client = Mock(spec=GitHubRepositoryClient)
    client.get_pull_request_base_file.return_value = _exact(
        _content("1.26.4"),
        revision=_BASE_SHA,
        blob_sha=_BASE_BLOB,
    )
    head_content = (
        _content("2.4.6")
        if optional_change
        else _content("1.26.4", name="dictare-renamed")
    )
    client.get_pull_request_head_file.return_value = _exact(
        head_content,
        revision=_HEAD_SHA,
        blob_sha=_HEAD_BLOB,
    )
    return client


class PyprojectDependencyAnalysisTests(unittest.TestCase):
    def test_s011_shape_produces_dependency_change_and_optional_extra_context(self) -> None:
        client = _client()
        identity = _identity()

        result = analyze_dependency_change(identity, [_changed()], client)

        self.assertIsInstance(result, DependencyChangeAnalysis)
        assert isinstance(result, DependencyChangeAnalysis)
        self.assertEqual(result.dependency.package, "numpy")
        self.assertEqual(result.dependency.old_version, "1.26.4")
        self.assertEqual(result.dependency.proposed_version, "2.4.6")
        self.assertEqual(len(result.source_contexts), 1)
        context = result.source_contexts[0]
        self.assertIsInstance(context, PyprojectOptionalExtraDependencyContext)
        assert isinstance(context, PyprojectOptionalExtraDependencyContext)
        self.assertEqual(context.extra, "mlx")
        self.assertEqual(context.repository, _REPOSITORY)
        self.assertEqual(context.revision, _HEAD_SHA)
        self.assertEqual(context.normalized_package, "numpy")
        self.assertEqual(context.source_path, "pyproject.toml")
        self.assertIsNone(result.direct_requirements_install_path)
        client.get_pull_request_base_file.assert_called_once_with(
            identity,
            "pyproject.toml",
        )
        client.get_pull_request_head_file.assert_called_once_with(
            identity,
            "pyproject.toml",
        )

    def test_unrelated_pyproject_metadata_edit_does_not_block_requirements_change(self) -> None:
        client = _client(optional_change=False)
        identity = _identity(changed_files=2)

        result = analyze_dependency_change(
            identity,
            [_changed(), _requirement_change()],
            client,
        )

        self.assertIsInstance(result, DependencyChangeAnalysis)
        assert isinstance(result, DependencyChangeAnalysis)
        self.assertEqual(result.dependency.package, "numpy")
        self.assertEqual(result.dependency.old_version, "1.26.4")
        self.assertEqual(result.dependency.proposed_version, "2.4.6")
        self.assertEqual(len(result.source_contexts), 1)
        self.assertIsInstance(
            result.source_contexts[0],
            RequirementsFileDependencyContext,
        )
        self.assertEqual(result.direct_requirements_install_path, "requirements.txt")

    def test_nonmodified_pyproject_is_explicit_and_does_not_acquire_files(self) -> None:
        client = _client()

        result = analyze_dependency_change(_identity(), [_changed(status="added")], client)

        self.assertIsInstance(result, DependencyChangeProblem)
        assert isinstance(result, DependencyChangeProblem)
        self.assertEqual(result.reason, "unsupported_dependency_file_status")
        client.get_pull_request_base_file.assert_not_called()
        client.get_pull_request_head_file.assert_not_called()


if __name__ == "__main__":
    unittest.main()
