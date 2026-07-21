"""Validate a manual dependency-update case and build trusted case contracts."""

from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Self

from pydantic import BaseModel, ConfigDict, ValidationInfo, field_validator, model_validator


_SHA_PATTERN = re.compile(r"[0-9a-fA-F]{40}")


def _normalize_non_empty_text(value: str, field_name: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} must not be empty")
    return normalized


def _normalize_repository(value: str) -> str:
    normalized = _normalize_non_empty_text(value, "repository")
    if normalized.count("/") != 1:
        raise ValueError("repository must use owner/name form")

    owner, name = normalized.split("/", maxsplit=1)
    if not owner or not name:
        raise ValueError("repository must use owner/name form")
    return normalized


def _normalize_sha(value: str, field_name: str) -> str:
    normalized = _normalize_non_empty_text(value, field_name)
    if _SHA_PATTERN.fullmatch(normalized) is None:
        raise ValueError(f"{field_name} must be exactly 40 hexadecimal characters")
    return normalized.lower()


def _normalize_paths(paths: list[str] | tuple[str, ...]) -> tuple[str, ...]:
    if not paths:
        raise ValueError("changed files must contain at least one path")

    normalized = tuple(
        _normalize_non_empty_text(path, "changed file path") for path in paths
    )
    seen: set[str] = set()
    for path in normalized:
        if path in seen:
            raise ValueError(
                f"duplicate changed file path after normalization: {path}"
            )
        seen.add(path)
    return normalized


class ManualCaseInput(BaseModel):
    """Validated form of the provisional flat M2 manual input."""

    model_config = ConfigDict(strict=True, extra="forbid")

    repository: str
    pr_number: int
    base_sha: str
    head_sha: str
    dependency: str
    old_version: str
    new_version: str
    changed_files: list[str]

    @field_validator("repository")
    @classmethod
    def normalize_repository(cls, value: str) -> str:
        return _normalize_repository(value)

    @field_validator("pr_number")
    @classmethod
    def validate_pr_number(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("pr_number must be a positive integer")
        return value

    @field_validator("base_sha", "head_sha")
    @classmethod
    def normalize_sha(cls, value: str, info: ValidationInfo) -> str:
        return _normalize_sha(value, info.field_name)

    @field_validator("dependency", "old_version", "new_version")
    @classmethod
    def normalize_required_text(cls, value: str, info: ValidationInfo) -> str:
        return _normalize_non_empty_text(value, info.field_name)

    @field_validator("changed_files")
    @classmethod
    def normalize_changed_files(cls, value: list[str]) -> list[str]:
        return list(_normalize_paths(value))

    @model_validator(mode="after")
    def validate_version_change(self) -> Self:
        if self.old_version == self.new_version:
            raise ValueError("old_version and new_version must differ")
        return self


class PullRequestSnapshotIdentity(BaseModel):
    """Trusted identity of one exact pull-request snapshot."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    repository: str
    pr_number: int
    base_sha: str
    head_sha: str

    @field_validator("repository")
    @classmethod
    def normalize_repository(cls, value: str) -> str:
        return _normalize_repository(value)

    @field_validator("pr_number")
    @classmethod
    def validate_pr_number(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("pr_number must be a positive integer")
        return value

    @field_validator("base_sha", "head_sha")
    @classmethod
    def normalize_sha(cls, value: str, info: ValidationInfo) -> str:
        return _normalize_sha(value, info.field_name)


class DependencyChange(BaseModel):
    """Trusted dependency and version transition for the selected snapshot."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    dependency: str
    old_version: str
    new_version: str

    @field_validator("dependency", "old_version", "new_version")
    @classmethod
    def normalize_required_text(cls, value: str, info: ValidationInfo) -> str:
        return _normalize_non_empty_text(value, info.field_name)

    @model_validator(mode="after")
    def validate_version_change(self) -> Self:
        if self.old_version == self.new_version:
            raise ValueError("old_version and new_version must differ")
        return self


class ChangedFileEvidence(BaseModel):
    """Trusted ordered changed-file paths associated with the snapshot."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    paths: tuple[str, ...]

    @field_validator("paths")
    @classmethod
    def normalize_paths(cls, value: tuple[str, ...]) -> tuple[str, ...]:
        return _normalize_paths(value)


class InitialCaseRecord(BaseModel):
    """Trusted aggregate of the M2-activated case concepts."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    snapshot_identity: PullRequestSnapshotIdentity
    dependency_change: DependencyChange
    changed_file_evidence: ChangedFileEvidence


def build_initial_case_record(raw_input: Mapping[str, object]) -> InitialCaseRecord:
    """Validate a flat manual input and explicitly assemble its trusted record."""

    manual_input = ManualCaseInput.model_validate(dict(raw_input))

    return InitialCaseRecord(
        snapshot_identity=PullRequestSnapshotIdentity(
            repository=manual_input.repository,
            pr_number=manual_input.pr_number,
            base_sha=manual_input.base_sha,
            head_sha=manual_input.head_sha,
        ),
        dependency_change=DependencyChange(
            dependency=manual_input.dependency,
            old_version=manual_input.old_version,
            new_version=manual_input.new_version,
        ),
        changed_file_evidence=ChangedFileEvidence(
            paths=tuple(manual_input.changed_files),
        ),
    )
