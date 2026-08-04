"""Resolve one exact Git version tag to the immutable commit it identifies.

A lightweight tag points directly to a commit. An annotated tag points to a Git tag
object and must be peeled through a bounded object chain. This module owns exact tag
reference identity and peeling only; it does not interpret release prose or changelogs.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable, Literal
from urllib.parse import quote

from requests import Session

from .api import (
    DEFAULT_TIMEOUT,
    GitHubAcquisitionError,
    GitHubApiClient,
    GitHubResponseError,
    required_mapping,
    required_str,
)
from .identity import validate_repository

type GitHubTagObjectType = Literal["commit", "tag"]
type GitHubTagCommitProblemState = Literal[
    "source_unavailable",
    "identity_mismatch",
    "malformed_response",
    "unsupported_object_type",
    "peel_cycle",
    "peel_depth_exceeded",
    "acquisition_failed",
]


@dataclass(frozen=True, slots=True)
class GitHubTagCommitEvidence:
    state: Literal["available"] = field(init=False, default="available")
    repository: str
    requested_tag: str
    tag_ref: str
    tag_object_type: GitHubTagObjectType
    tag_object_sha: str
    resolved_commit_sha: str
    peeled_tag_object_shas: tuple[str, ...]
    retrieved_at: datetime

    @property
    def peel_depth(self) -> int:
        return len(self.peeled_tag_object_shas)


@dataclass(frozen=True, slots=True)
class GitHubTagCommitProblem:
    state: GitHubTagCommitProblemState
    repository: str
    requested_tag: str
    detail: str
    status_code: int | None = None
    object_sha: str | None = None


type GitHubTagCommitResult = GitHubTagCommitEvidence | GitHubTagCommitProblem


class GitHubTagCommitClient(GitHubApiClient):
    """Resolve an explicitly supplied GitHub tag through a bounded read-only path."""

    def __init__(
        self,
        *,
        token: str | None = None,
        session: Session | None = None,
        timeout: tuple[float, float] = DEFAULT_TIMEOUT,
        now: Callable[[], datetime] | None = None,
        max_peel_depth: int = 8,
    ) -> None:
        if isinstance(max_peel_depth, bool) or not isinstance(max_peel_depth, int):
            raise ValueError("max_peel_depth must be a positive integer.")
        if max_peel_depth < 1:
            raise ValueError("max_peel_depth must be a positive integer.")
        super().__init__(token=token, session=session, timeout=timeout)
        self._now = now or (lambda: datetime.now(timezone.utc))
        self._max_peel_depth = max_peel_depth

    def resolve_tag_to_commit(
        self,
        repository: str,
        requested_tag: str,
    ) -> GitHubTagCommitResult:
        repository = validate_repository(repository)
        requested_tag = _nonempty_trimmed_text(requested_tag, "requested_tag")

        ref_url = self.api_url(
            f"/repos/{repository}/git/ref/tags/{quote(requested_tag, safe='')}"
        )
        ref_data = self._get_or_problem(
            ref_url,
            repository,
            requested_tag,
            resource="tag-reference",
        )
        if isinstance(ref_data, GitHubTagCommitProblem):
            return ref_data

        try:
            tag_ref, top_type, top_sha = parse_exact_tag_reference(
                ref_data,
                requested_tag,
            )
        except _TagIdentityMismatch as exc:
            return self._problem(
                "identity_mismatch", repository, requested_tag, str(exc)
            )
        except _UnsupportedGitObjectType as exc:
            return self._problem(
                "unsupported_object_type",
                repository,
                requested_tag,
                str(exc),
                object_sha=exc.object_sha,
            )
        except (KeyError, GitHubResponseError) as exc:
            return self._problem(
                "malformed_response",
                repository,
                requested_tag,
                _malformed_detail("tag-reference", exc),
            )

        if top_type == "commit":
            return GitHubTagCommitEvidence(
                repository=repository,
                requested_tag=requested_tag,
                tag_ref=tag_ref,
                tag_object_type=top_type,
                tag_object_sha=top_sha,
                resolved_commit_sha=top_sha,
                peeled_tag_object_shas=(),
                retrieved_at=self._now(),
            )

        resolved = self._peel_annotated_tag(
            repository,
            requested_tag,
            top_sha,
        )
        if isinstance(resolved, GitHubTagCommitProblem):
            return resolved
        resolved_commit_sha, peeled_shas = resolved

        return GitHubTagCommitEvidence(
            repository=repository,
            requested_tag=requested_tag,
            tag_ref=tag_ref,
            tag_object_type=top_type,
            tag_object_sha=top_sha,
            resolved_commit_sha=resolved_commit_sha,
            peeled_tag_object_shas=peeled_shas,
            retrieved_at=self._now(),
        )

    def _peel_annotated_tag(
        self,
        repository: str,
        requested_tag: str,
        first_tag_object_sha: str,
    ) -> tuple[str, tuple[str, ...]] | GitHubTagCommitProblem:
        current_sha = first_tag_object_sha
        visited: set[str] = set()
        peeled_shas: list[str] = []

        while True:
            if current_sha in visited:
                return self._problem(
                    "peel_cycle",
                    repository,
                    requested_tag,
                    "Annotated Git tag peeling encountered an object cycle.",
                    object_sha=current_sha,
                )
            if len(peeled_shas) >= self._max_peel_depth:
                return self._problem(
                    "peel_depth_exceeded",
                    repository,
                    requested_tag,
                    (
                        "Annotated Git tag peeling exceeded the configured maximum "
                        f"depth of {self._max_peel_depth}."
                    ),
                    object_sha=current_sha,
                )

            visited.add(current_sha)
            object_url = self.api_url(
                f"/repos/{repository}/git/tags/{quote(current_sha, safe='')}"
            )
            tag_data = self._get_or_problem(
                object_url,
                repository,
                requested_tag,
                resource="annotated-tag-object",
                object_sha=current_sha,
            )
            if isinstance(tag_data, GitHubTagCommitProblem):
                return tag_data

            try:
                target_type, target_sha = _parse_annotated_tag_object(
                    tag_data,
                    expected_sha=current_sha,
                )
            except _TagIdentityMismatch as exc:
                return self._problem(
                    "identity_mismatch",
                    repository,
                    requested_tag,
                    str(exc),
                    object_sha=current_sha,
                )
            except _UnsupportedGitObjectType as exc:
                return self._problem(
                    "unsupported_object_type",
                    repository,
                    requested_tag,
                    str(exc),
                    object_sha=exc.object_sha,
                )
            except (KeyError, GitHubResponseError) as exc:
                return self._problem(
                    "malformed_response",
                    repository,
                    requested_tag,
                    _malformed_detail("annotated-tag-object", exc),
                    object_sha=current_sha,
                )

            peeled_shas.append(current_sha)
            if target_type == "commit":
                return target_sha, tuple(peeled_shas)
            current_sha = target_sha

    def _get_or_problem(
        self,
        url: str,
        repository: str,
        requested_tag: str,
        *,
        resource: str,
        object_sha: str | None = None,
    ) -> Mapping[str, Any] | GitHubTagCommitProblem:
        try:
            return self._get_json_object(url, resource=resource)
        except GitHubAcquisitionError as exc:
            state: GitHubTagCommitProblemState = (
                "source_unavailable"
                if exc.reason == "not_found_or_inaccessible"
                else "acquisition_failed"
            )
            return self._problem(
                state,
                repository,
                requested_tag,
                str(exc),
                status_code=exc.status_code,
                object_sha=object_sha,
            )
        except GitHubResponseError as exc:
            return self._problem(
                "malformed_response",
                repository,
                requested_tag,
                str(exc),
                object_sha=object_sha,
            )

    @staticmethod
    def _problem(
        state: GitHubTagCommitProblemState,
        repository: str,
        requested_tag: str,
        detail: str,
        *,
        status_code: int | None = None,
        object_sha: str | None = None,
    ) -> GitHubTagCommitProblem:
        return GitHubTagCommitProblem(
            state=state,
            repository=repository,
            requested_tag=requested_tag,
            detail=detail,
            status_code=status_code,
            object_sha=object_sha,
        )


class _TagIdentityMismatch(ValueError):
    pass


class _UnsupportedGitObjectType(ValueError):
    def __init__(self, object_type: str, object_sha: str) -> None:
        super().__init__(
            f"Git tag resolution encountered unsupported object type {object_type!r}."
        )
        self.object_sha = object_sha


def parse_exact_tag_reference(
    data: Mapping[str, Any],
    requested_tag: str,
) -> tuple[str, GitHubTagObjectType, str]:
    expected_ref = f"refs/tags/{requested_tag}"
    returned_ref = required_str(data, "ref")
    if returned_ref != expected_ref:
        raise _TagIdentityMismatch(
            f"GitHub returned tag reference {returned_ref!r} instead of {expected_ref!r}."
        )

    target = required_mapping(data, "object")
    object_type = required_str(target, "type")
    object_sha = required_str(target, "sha")
    if object_type not in {"commit", "tag"}:
        raise _UnsupportedGitObjectType(object_type, object_sha)
    return returned_ref, object_type, object_sha  # type: ignore[return-value]


def _parse_annotated_tag_object(
    data: Mapping[str, Any],
    *,
    expected_sha: str,
) -> tuple[GitHubTagObjectType, str]:
    returned_sha = required_str(data, "sha")
    if returned_sha != expected_sha:
        raise _TagIdentityMismatch(
            f"GitHub returned annotated tag object {returned_sha!r} instead of {expected_sha!r}."
        )

    target = required_mapping(data, "object")
    object_type = required_str(target, "type")
    object_sha = required_str(target, "sha")
    if object_type not in {"commit", "tag"}:
        raise _UnsupportedGitObjectType(object_type, object_sha)
    return object_type, object_sha  # type: ignore[return-value]


def _nonempty_trimmed_text(value: str, name: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{name} must be non-empty exact trimmed text.")
    return value


def _malformed_detail(resource: str, exc: Exception) -> str:
    if isinstance(exc, KeyError):
        return f"GitHub {resource} response is missing required field: {exc.args[0]}."
    return str(exc)


__all__ = (
    "GitHubTagCommitClient",
    "GitHubTagCommitEvidence",
    "GitHubTagCommitProblem",
    "GitHubTagCommitProblemState",
    "GitHubTagCommitResult",
    "GitHubTagObjectType",
    "parse_exact_tag_reference",
)
