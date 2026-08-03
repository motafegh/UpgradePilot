"""Discover one bounded changelog path at an exact upstream Git commit.

Data flow::

    trusted repository + resolved exact commit SHA
    → exact Git commit object
    → exact root tree SHA
    → complete recursive Git tree
    → admitted Markdown changelog basename filter
    → one path or an explicit discovery problem

This module performs GitHub source-location discovery only. It does not read the
selected changelog, interpret Markdown release sections, extract support-drop meaning,
call a model, or make target-Python/compatibility decisions.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import PurePosixPath
from typing import Any, Literal

from requests import Session

from .api import (
    DEFAULT_TIMEOUT,
    GitHubAcquisitionError,
    GitHubApiClient,
    GitHubResponseError,
    required_list,
    required_mapping,
    required_str,
)
from .identity import validate_commit_sha, validate_repository


type ChangelogPathDiscoveryProblemState = Literal[
    "source_unavailable",
    "malformed_response",
    "identity_mismatch",
    "recursive_tree_truncated",
    "no_candidate_path",
    "multiple_candidate_paths",
    "acquisition_failed",
]

ADMITTED_CHANGELOG_BASENAMES: tuple[str, ...] = (
    "changelog.md",
    "changes.md",
    "history.md",
    "release-notes.md",
)


@dataclass(frozen=True, slots=True)
class DiscoveredChangelogPath:
    """One unambiguous admitted changelog path at one exact commit tree."""

    state: Literal["available"] = field(init=False, default="available")
    repository: str
    commit_sha: str
    tree_sha: str
    path: str
    candidate_paths: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ChangelogPathDiscoveryProblem:
    """Why exact-commit tree discovery could not establish one changelog path."""

    state: ChangelogPathDiscoveryProblemState
    repository: str
    commit_sha: str
    detail: str
    tree_sha: str | None = None
    candidate_paths: tuple[str, ...] = ()
    status_code: int | None = None


type ChangelogPathDiscoveryResult = DiscoveredChangelogPath | ChangelogPathDiscoveryProblem


class GitHubChangelogPathClient(GitHubApiClient):
    """Discover one admitted Markdown changelog path from an immutable Git tree."""

    def __init__(
        self,
        *,
        token: str | None = None,
        session: Session | None = None,
        timeout: tuple[float, float] = DEFAULT_TIMEOUT,
    ) -> None:
        super().__init__(token=token, session=session, timeout=timeout)

    def discover(
        self,
        repository: str,
        commit_sha: str,
    ) -> ChangelogPathDiscoveryResult:
        repository = validate_repository(repository)
        commit_sha = validate_commit_sha(commit_sha)

        commit_url = self.api_url(f"/repos/{repository}/git/commits/{commit_sha}")
        try:
            commit = self._get_json_object(commit_url, resource="git-commit")
        except GitHubAcquisitionError as exc:
            return self._acquisition_problem(repository, commit_sha, exc)
        except GitHubResponseError as exc:
            return ChangelogPathDiscoveryProblem(
                state="malformed_response",
                repository=repository,
                commit_sha=commit_sha,
                detail=str(exc),
            )

        try:
            returned_commit = required_str(commit, "sha")
            tree = required_mapping(commit, "tree")
            tree_sha = required_str(tree, "sha")
        except (KeyError, GitHubResponseError) as exc:
            return ChangelogPathDiscoveryProblem(
                state="malformed_response",
                repository=repository,
                commit_sha=commit_sha,
                detail=_malformed_detail("git-commit", exc),
            )

        if returned_commit.casefold() != commit_sha.casefold():
            return ChangelogPathDiscoveryProblem(
                state="identity_mismatch",
                repository=repository,
                commit_sha=commit_sha,
                tree_sha=tree_sha,
                detail=(
                    f"GitHub returned commit {returned_commit!r} instead of the exact "
                    f"requested commit {commit_sha!r}."
                ),
            )

        tree_url = self.api_url(f"/repos/{repository}/git/trees/{tree_sha}")
        try:
            tree_data = self._get_json_object(
                tree_url,
                resource="git-tree",
                params={"recursive": 1},
            )
        except GitHubAcquisitionError as exc:
            return self._acquisition_problem(
                repository,
                commit_sha,
                exc,
                tree_sha=tree_sha,
            )
        except GitHubResponseError as exc:
            return ChangelogPathDiscoveryProblem(
                state="malformed_response",
                repository=repository,
                commit_sha=commit_sha,
                tree_sha=tree_sha,
                detail=str(exc),
            )

        try:
            returned_tree_sha = required_str(tree_data, "sha")
            truncated = tree_data["truncated"]
            raw_entries = required_list(tree_data, "tree")
        except (KeyError, GitHubResponseError) as exc:
            return ChangelogPathDiscoveryProblem(
                state="malformed_response",
                repository=repository,
                commit_sha=commit_sha,
                tree_sha=tree_sha,
                detail=_malformed_detail("git-tree", exc),
            )

        if returned_tree_sha.casefold() != tree_sha.casefold():
            return ChangelogPathDiscoveryProblem(
                state="identity_mismatch",
                repository=repository,
                commit_sha=commit_sha,
                tree_sha=tree_sha,
                detail=(
                    f"GitHub returned tree {returned_tree_sha!r} instead of the root "
                    f"tree {tree_sha!r} named by the exact commit."
                ),
            )
        if type(truncated) is not bool:
            return ChangelogPathDiscoveryProblem(
                state="malformed_response",
                repository=repository,
                commit_sha=commit_sha,
                tree_sha=tree_sha,
                detail="GitHub git-tree field 'truncated' must be a boolean.",
            )
        if truncated:
            return ChangelogPathDiscoveryProblem(
                state="recursive_tree_truncated",
                repository=repository,
                commit_sha=commit_sha,
                tree_sha=tree_sha,
                detail=(
                    "GitHub marked the recursive tree response as truncated, so the "
                    "candidate-path search was not complete."
                ),
            )

        parsed = _candidate_paths(raw_entries)
        if isinstance(parsed, str):
            return ChangelogPathDiscoveryProblem(
                state="malformed_response",
                repository=repository,
                commit_sha=commit_sha,
                tree_sha=tree_sha,
                detail=parsed,
            )

        if not parsed:
            return ChangelogPathDiscoveryProblem(
                state="no_candidate_path",
                repository=repository,
                commit_sha=commit_sha,
                tree_sha=tree_sha,
                detail=(
                    "The complete exact-commit tree contained no regular Markdown file "
                    "with an admitted changelog basename."
                ),
            )
        if len(parsed) > 1:
            return ChangelogPathDiscoveryProblem(
                state="multiple_candidate_paths",
                repository=repository,
                commit_sha=commit_sha,
                tree_sha=tree_sha,
                candidate_paths=parsed,
                detail=(
                    "The exact-commit tree contained several admitted changelog paths; "
                    "UpgradePilot does not rank ambiguous documentation sources."
                ),
            )

        return DiscoveredChangelogPath(
            repository=repository,
            commit_sha=commit_sha,
            tree_sha=tree_sha,
            path=parsed[0],
            candidate_paths=parsed,
        )

    @staticmethod
    def _acquisition_problem(
        repository: str,
        commit_sha: str,
        exc: GitHubAcquisitionError,
        *,
        tree_sha: str | None = None,
    ) -> ChangelogPathDiscoveryProblem:
        state: ChangelogPathDiscoveryProblemState = (
            "source_unavailable"
            if exc.reason == "not_found_or_inaccessible"
            else "acquisition_failed"
        )
        return ChangelogPathDiscoveryProblem(
            state=state,
            repository=repository,
            commit_sha=commit_sha,
            tree_sha=tree_sha,
            detail=str(exc),
            status_code=exc.status_code,
        )


def _candidate_paths(raw_entries: list[Any]) -> tuple[str, ...] | str:
    admitted = {name.casefold() for name in ADMITTED_CHANGELOG_BASENAMES}
    candidates: set[str] = set()

    for index, raw in enumerate(raw_entries, start=1):
        if not isinstance(raw, Mapping):
            return f"GitHub git-tree item {index} must be an object."
        try:
            object_type = required_str(raw, "type")
            path = required_str(raw, "path")
        except (KeyError, GitHubResponseError) as exc:
            return _malformed_detail(f"git-tree item {index}", exc)

        if not _valid_tree_path(path):
            return f"GitHub git-tree item {index} contained an invalid repository path."
        if object_type != "blob":
            continue
        if PurePosixPath(path).name.casefold() in admitted:
            candidates.add(path)

    return tuple(sorted(candidates))


def _valid_tree_path(path: str) -> bool:
    if not path or path != path.strip() or path.startswith("/") or "\\" in path:
        return False
    parts = PurePosixPath(path).parts
    return bool(parts) and all(part not in {"", ".", ".."} for part in parts)


def _malformed_detail(resource: str, exc: Exception) -> str:
    if isinstance(exc, KeyError):
        return f"GitHub {resource} response is missing required field: {exc.args[0]}."
    return str(exc)


__all__ = (
    "ADMITTED_CHANGELOG_BASENAMES",
    "ChangelogPathDiscoveryProblem",
    "ChangelogPathDiscoveryProblemState",
    "ChangelogPathDiscoveryResult",
    "DiscoveredChangelogPath",
    "GitHubChangelogPathClient",
)
