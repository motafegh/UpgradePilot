"""GitHub-specific repository, pull-request, and immutable object identity rules.

These validators are pure local syntax checks. They deliberately perform no network
request and establish no authority beyond the shape of the supplied identifier.
Provider clients import this module instead of depending on an unrelated PR client for
shared GitHub identity grammar.
"""

from __future__ import annotations

import re

_REPOSITORY_PATTERN = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9_.-]{0,99})/[A-Za-z0-9_.-]{1,100}$"
)
_GIT_OBJECT_ID_PATTERN = re.compile(r"^(?:[0-9a-fA-F]{40}|[0-9a-fA-F]{64})\Z")


class UpgradePilotInputError(ValueError):
    """A user-supplied GitHub locator is outside UpgradePilot's supported grammar."""


def validate_repository(repository: str) -> str:
    """Validate and preserve one supported ``owner/repository`` locator."""

    if not isinstance(repository, str):
        raise UpgradePilotInputError(
            "Repository must use the supported 'owner/repository' form."
        )
    normalized = repository.strip()
    if _REPOSITORY_PATTERN.fullmatch(normalized) is None:
        raise UpgradePilotInputError(
            "Repository must use the supported 'owner/repository' form."
        )
    return normalized


def validate_pull_number(pull_number: int) -> int:
    """Require a positive integer pull-request number while rejecting booleans."""

    if (
        isinstance(pull_number, bool)
        or not isinstance(pull_number, int)
        or pull_number < 1
    ):
        raise UpgradePilotInputError("Pull-request number must be a positive integer.")
    return pull_number


def validate_commit_sha(commit_sha: str) -> str:
    """Require a 40- or 64-hex immutable Git object ID and normalize hex case.

    The name remains ``validate_commit_sha`` because current callers use the value as a
    commit identity, while the accepted grammar intentionally follows the stronger
    invariant already proven by exact-file and changelog acquisition: an immutable
    hexadecimal Git object identifier rather than a movable ref such as ``main``.
    """

    if (
        not isinstance(commit_sha, str)
        or _GIT_OBJECT_ID_PATTERN.fullmatch(commit_sha) is None
    ):
        raise UpgradePilotInputError(
            "commit_sha must be a 40- or 64-character hexadecimal object ID."
        )
    return commit_sha.lower()


__all__ = (
    "UpgradePilotInputError",
    "validate_commit_sha",
    "validate_pull_number",
    "validate_repository",
)
