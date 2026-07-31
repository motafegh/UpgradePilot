"""Test the Step 8 PR-wide multi-format dependency coordinator."""

from __future__ import annotations

import unittest
from unittest.mock import Mock

from upgradepilot.dependency_analysis import (
    DependencyChangeAnalysis,
    analyze_dependency_change,
)
from upgradepilot.dependency_change import DependencyChangeEvidenceProblem
from upgradepilot.github_client import ChangedFile, PullRequestIdentity
from upgradepilot.github_repository import (
    ExactRepositoryTextFile,
    GitHubRepositoryClient,
    UnavailableRepositoryFile,
)

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


def _changed(
    path: str,
    *,
    patch: str | None = None,
    status: str = "modified",
    additions: int = 1,
    deletions: int = 1,
) -> ChangedFile:
    return ChangedFile(
        filename=path,
        status=status,
        additions=additions,
        deletions=deletions,
        changes=additions + deletions,
        patch=patch,
    )


def _requirement(
    path: str = "requirements-dev.txt",
    *,
    package: str = "demo",
    old: str = "1.0",
    new: str = "2.0",
) -> ChangedFile:
    return _changed(path, patch=f"-{package}=={old}\n+{package}=={new}")


def _lock(package: str, version: str) -> str:
    return (
        "version = 1\n"
        "revision = 0\n\n"
        "[[package]]\n"
        f'name = "{package}"\n'
        f'version = "{version}"\n'
        'source = { registry = "https://pypi.org/simple" }\n'
    )


def _exact(
    path: str,
    content: str,
    *,
    revision: str,
    blob_sha: str,
) -> ExactRepositoryTextFile:
    size = len(content.encode("utf-8"))
    return ExactRepositoryTextFile(
        repository=_REPOSITORY,
        path=path,
        returned_path=path,
        revision=revision,
        blob_sha=blob_sha,
        reported_byte_count=size,
        decoded_byte_count=size,
        content=content,
    )


def _repository_client(
    *,
    path: str = "uv.lock",
    package: str = "demo",
    old: str = "1.0",
    new: str = "2.0",
) -> Mock:
    client = Mock(spec=GitHubRepositoryClient)
    client.get_pull_request_base_file.return_value = _exact(
        path,
        _lock(package, old),
        revision=_BASE_SHA,
        blob_sha=_BASE_BLOB,
    )
    client.get_pull_request_head_file.return_value = _exact(
        path,
        _lock(package, new),
        revision=_HEAD_SHA,
        blob_sha=_HEAD_BLOB,
    )
    return client


class DependencyAnalysisTests(unittest.TestCase):
    def test_requirements_change_produces_canonical_identity_and_ci_path(self) -> None:
        client = _repository_client()

        result = analyze_dependency_change(
            _identity(),
            [_requirement()],
            client,
        )

        self.assertIsInstance(result, DependencyChangeAnalysis)
        assert isinstance(result, DependencyChangeAnalysis)
        self.assertEqual(result.dependency.package, "demo")
        self.assertEqual(result.dependency.old_version, "1.0")
        self.assertEqual(result.dependency.proposed_version, "2.0")
        self.assertEqual(
            result.direct_requirements_install_path,
            "requirements-dev.txt",
        )
        client.get_pull_request_base_file.assert_not_called()
        client.get_pull_request_head_file.assert_not_called()

    def test_constraints_change_has_no_direct_requirements_ci_path(self) -> None:
        client = _repository_client()

        result = analyze_dependency_change(
            _identity(),
            [_requirement("constraints/base.txt")],
            client,
        )

        self.assertIsInstance(result, DependencyChangeAnalysis)
        assert isinstance(result, DependencyChangeAnalysis)
        self.assertIsNone(result.direct_requirements_install_path)
        client.get_pull_request_base_file.assert_not_called()
        client.get_pull_request_head_file.assert_not_called()

    def test_modified_uv_lock_acquires_exact_files_and_preserves_provenance(self) -> None:
        client = _repository_client(path="services/api/uv.lock")
        changed_file = _changed("services/api/uv.lock")

        result = analyze_dependency_change(
            _identity(),
            [changed_file],
            client,
        )

        self.assertIsInstance(result, DependencyChangeAnalysis)
        assert isinstance(result, DependencyChangeAnalysis)
        self.assertEqual(result.dependency.package, "demo")
        self.assertIsNone(result.direct_requirements_install_path)
        evidence = result.dependency.source_evidence[0]
        self.assertEqual(evidence.path, "services/api/uv.lock")
        self.assertEqual(evidence.file_format, "uv_lock")
        self.assertEqual(evidence.base_revision, _BASE_SHA)
        self.assertEqual(evidence.base_blob_sha, _BASE_BLOB)
        self.assertEqual(evidence.head_revision, _HEAD_SHA)
        self.assertEqual(evidence.head_blob_sha, _HEAD_BLOB)
        client.get_pull_request_base_file.assert_called_once_with(
            _identity(),
            "services/api/uv.lock",
        )
        client.get_pull_request_head_file.assert_called_once_with(
            _identity(),
            "services/api/uv.lock",
        )

    def test_arbitrary_files_are_ignored(self) -> None:
        client = _repository_client()

        result = analyze_dependency_change(
            _identity(),
            [_changed("README.md", patch="-old\n+new")],
            client,
        )

        self.assertIsInstance(result, DependencyChangeEvidenceProblem)
        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "no_supported_dependency_file")
        client.get_pull_request_base_file.assert_not_called()
        client.get_pull_request_head_file.assert_not_called()

    def test_nonmodified_uv_lock_is_explicit_without_file_acquisition(self) -> None:
        client = _repository_client()

        result = analyze_dependency_change(
            _identity(),
            [_changed("uv.lock", status="added")],
            client,
        )

        self.assertIsInstance(result, DependencyChangeEvidenceProblem)
        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "unsupported_dependency_file_status")
        client.get_pull_request_base_file.assert_not_called()
        client.get_pull_request_head_file.assert_not_called()

    def test_exact_files_are_acquired_only_for_modified_uv_lock(self) -> None:
        client = _repository_client()
        identity = _identity(changed_files=3)
        uv_lock = _changed("uv.lock")

        result = analyze_dependency_change(
            identity,
            [
                _changed("README.md", patch="-old\n+new"),
                _requirement(),
                uv_lock,
            ],
            client,
        )

        self.assertIsInstance(result, DependencyChangeAnalysis)
        client.get_pull_request_base_file.assert_called_once_with(identity, "uv.lock")
        client.get_pull_request_head_file.assert_called_once_with(identity, "uv.lock")

    def test_equivalent_requirements_and_uv_lock_evidence_are_combined(self) -> None:
        client = _repository_client(package="demo", old="1.0", new="2.0")
        identity = _identity(changed_files=2)

        result = analyze_dependency_change(
            identity,
            [_requirement(), _changed("uv.lock")],
            client,
        )

        self.assertIsInstance(result, DependencyChangeAnalysis)
        assert isinstance(result, DependencyChangeAnalysis)
        self.assertEqual(len(result.dependency.source_evidence), 2)
        self.assertEqual(
            {item.file_format for item in result.dependency.source_evidence},
            {"exact_requirement", "uv_lock"},
        )
        self.assertEqual(
            result.direct_requirements_install_path,
            "requirements-dev.txt",
        )

    def test_conflicting_transitions_remain_explicit(self) -> None:
        client = _repository_client(package="demo", old="1.0", new="3.0")

        result = analyze_dependency_change(
            _identity(changed_files=2),
            [_requirement(old="1.0", new="2.0"), _changed("uv.lock")],
            client,
        )

        self.assertIsInstance(result, DependencyChangeEvidenceProblem)
        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "conflicting_dependency_version_changes")

    def test_several_packages_remain_explicit(self) -> None:
        client = _repository_client(package="other", old="1.0", new="2.0")

        result = analyze_dependency_change(
            _identity(changed_files=2),
            [_requirement(package="demo"), _changed("uv.lock")],
            client,
        )

        self.assertIsInstance(result, DependencyChangeEvidenceProblem)
        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "multiple_dependency_version_changes")

    def test_recognized_requirement_problem_blocks_valid_lockfile(self) -> None:
        client = _repository_client()

        result = analyze_dependency_change(
            _identity(changed_files=2),
            [
                _changed("requirements.txt", patch=None),
                _changed("uv.lock"),
            ],
            client,
        )

        self.assertIsInstance(result, DependencyChangeEvidenceProblem)
        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "missing_dependency_patch")

    def test_unavailable_lockfile_blocks_valid_requirements_result(self) -> None:
        client = _repository_client()
        client.get_pull_request_base_file.return_value = UnavailableRepositoryFile(
            repository=_REPOSITORY,
            path="uv.lock",
            revision=_BASE_SHA,
            reason="not_found_or_inaccessible",
            detail="GitHub returned 404.",
        )

        result = analyze_dependency_change(
            _identity(changed_files=2),
            [_requirement(), _changed("uv.lock")],
            client,
        )

        self.assertIsInstance(result, DependencyChangeEvidenceProblem)
        assert isinstance(result, DependencyChangeEvidenceProblem)
        self.assertEqual(result.reason, "dependency_file_unavailable")

    def test_multiple_requirements_paths_do_not_guess_one_ci_path(self) -> None:
        client = _repository_client()

        result = analyze_dependency_change(
            _identity(changed_files=2),
            [
                _requirement("requirements.txt"),
                _requirement("requirements-dev.txt"),
            ],
            client,
        )

        self.assertIsInstance(result, DependencyChangeAnalysis)
        assert isinstance(result, DependencyChangeAnalysis)
        self.assertEqual(len(result.dependency.source_evidence), 2)
        self.assertIsNone(result.direct_requirements_install_path)


if __name__ == "__main__":
    unittest.main()
