"""Build bounded structural source windows from exact tagged Markdown changelogs.

This module performs deterministic Markdown structure selection only. It does not
interpret release prose, identify Python support changes, call a model, or decide
target relevance.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Literal

from ..github.identity import validate_repository
from .interval import (
    CrossedReleaseIndexEvidence,
    DependencyReleaseInterval,
    TaggedChangelogEvidence,
)

type CrossedReleaseSourceWindowProblemState = Literal[
    "identity_mismatch",
    "malformed_source",
    "missing_release_section",
    "duplicate_release_section",
    "source_order_conflict",
    "window_too_large",
]


@dataclass(frozen=True, slots=True)
class ChangelogSourceLine:
    """One original changelog line with stable global line and character identity."""

    line_id: str
    line_number: int
    text: str
    start_offset: int
    end_offset: int


@dataclass(frozen=True, slots=True)
class CrossedReleaseMarkdownSection:
    """One complete Markdown section for one trusted crossed release."""

    release_version: str
    heading_level: int
    heading_line_id: str
    heading_line_number: int
    section_text: str
    source_lines: tuple[ChangelogSourceLine, ...]
    start_offset: int
    end_offset: int

    @property
    def source_line_ids(self) -> tuple[str, ...]:
        return tuple(line.line_id for line in self.source_lines)


@dataclass(frozen=True, slots=True)
class CrossedReleaseSourceWindow:
    """Complete bounded source text for all trusted crossed releases."""

    state: Literal["available"] = field(init=False, default="available")
    repository: str
    interval: DependencyReleaseInterval
    path: str
    blob_sha: str
    resolved_commit_sha: str
    trusted_ordered_versions: tuple[str, ...]
    sections: tuple[CrossedReleaseMarkdownSection, ...]
    source_ordered_versions: tuple[str, ...]
    text: str
    character_count: int
    max_characters: int


@dataclass(frozen=True, slots=True)
class CrossedReleaseSourceWindowProblem:
    """Why a complete deterministic crossed-release source window was unavailable."""

    state: CrossedReleaseSourceWindowProblemState
    repository: str
    interval: DependencyReleaseInterval
    path: str
    detail: str
    release_version: str | None = None


type CrossedReleaseSourceWindowResult = (
    CrossedReleaseSourceWindow | CrossedReleaseSourceWindowProblem
)


@dataclass(frozen=True, slots=True)
class _IndexedSourceLine:
    line: ChangelogSourceLine


@dataclass(frozen=True, slots=True)
class _AtxHeading:
    level: int
    title: str
    line_index: int
    start_offset: int


_ATX_HEADING = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+(.*)|[ \t]*)$")
_FENCE_OPEN = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def build_crossed_release_source_window(
    crossed_releases: CrossedReleaseIndexEvidence,
    changelog: TaggedChangelogEvidence,
    *,
    max_characters: int,
) -> CrossedReleaseSourceWindowResult:
    """Select complete trusted release sections without assigning semantic meaning."""

    if not isinstance(crossed_releases, CrossedReleaseIndexEvidence):
        raise TypeError("crossed_releases must be CrossedReleaseIndexEvidence.")
    if not isinstance(changelog, TaggedChangelogEvidence):
        raise TypeError("changelog must be TaggedChangelogEvidence.")
    if type(max_characters) is not int or max_characters <= 0:
        raise ValueError("max_characters must be a positive integer.")

    repository = _validated_repository(crossed_releases.repository)
    changelog_repository = _validated_repository(changelog.repository)
    if repository is None or changelog_repository is None:
        return _problem(
            "malformed_source",
            crossed_releases,
            changelog,
            "The source repository identity was malformed.",
        )
    if (
        repository.casefold() != changelog_repository.casefold()
        or crossed_releases.interval != changelog.interval
    ):
        return _problem(
            "identity_mismatch",
            crossed_releases,
            changelog,
            (
                "The crossed-release index and tagged changelog describe different "
                "source identity."
            ),
        )

    versions = crossed_releases.ordered_versions
    if (
        not isinstance(versions, tuple)
        or not versions
        or any(not _trimmed_text(version) for version in versions)
        or len(set(versions)) != len(versions)
    ):
        return _problem(
            "malformed_source",
            crossed_releases,
            changelog,
            (
                "The crossed-release index did not contain one non-empty unique "
                "version sequence."
            ),
        )
    if (
        not _trimmed_text(changelog.path)
        or not _trimmed_text(changelog.blob_sha)
        or not _trimmed_text(changelog.resolved_commit_sha)
        or not isinstance(changelog.content, str)
        or not changelog.content.strip()
    ):
        return _problem(
            "malformed_source",
            crossed_releases,
            changelog,
            (
                "The tagged changelog did not preserve usable exact source identity "
                "and text."
            ),
        )

    title_map = _release_heading_titles(versions)
    if title_map is None:
        return _problem(
            "malformed_source",
            crossed_releases,
            changelog,
            (
                "The trusted raw versions produced ambiguous admitted Markdown "
                "heading forms."
            ),
        )

    indexed_lines = _index_source_lines(changelog.content)
    headings = _scan_atx_headings(indexed_lines)
    matched: dict[str, list[_AtxHeading]] = {version: [] for version in versions}
    for heading in headings:
        version = title_map.get(heading.title)
        if version is not None:
            matched[version].append(heading)

    for version in versions:
        if not matched[version]:
            return _problem(
                "missing_release_section",
                crossed_releases,
                changelog,
                (
                    "No admitted Markdown release section matched crossed release "
                    f"{version!r}."
                ),
                release_version=version,
            )
        if len(matched[version]) > 1:
            return _problem(
                "duplicate_release_section",
                crossed_releases,
                changelog,
                (
                    "More than one admitted Markdown release section matched crossed "
                    f"release {version!r}."
                ),
                release_version=version,
            )

    source_headings = sorted(
        (matched[version][0] for version in versions),
        key=lambda item: item.start_offset,
    )
    source_ordered_versions = tuple(
        title_map[heading.title] for heading in source_headings
    )
    if source_ordered_versions not in (versions, tuple(reversed(versions))):
        return _problem(
            "source_order_conflict",
            crossed_releases,
            changelog,
            (
                "The changelog release-section order contradicted the trusted "
                "crossed-release ordering."
            ),
        )

    sections: list[CrossedReleaseMarkdownSection] = []
    for heading in source_headings:
        end_line_index = _section_end_line_index(
            heading,
            headings,
            len(indexed_lines),
        )
        start_offset = heading.start_offset
        end_offset = (
            indexed_lines[end_line_index].line.start_offset
            if end_line_index < len(indexed_lines)
            else len(changelog.content)
        )
        source_lines = tuple(
            indexed_lines[index].line
            for index in range(heading.line_index, end_line_index)
        )
        sections.append(
            CrossedReleaseMarkdownSection(
                release_version=title_map[heading.title],
                heading_level=heading.level,
                heading_line_id=indexed_lines[heading.line_index].line.line_id,
                heading_line_number=indexed_lines[heading.line_index].line.line_number,
                section_text=changelog.content[start_offset:end_offset],
                source_lines=source_lines,
                start_offset=start_offset,
                end_offset=end_offset,
            )
        )

    for previous, current in zip(sections, sections[1:]):
        if previous.end_offset > current.start_offset:
            return _problem(
                "source_order_conflict",
                crossed_releases,
                changelog,
                (
                    "Crossed-release Markdown sections overlapped because their "
                    "heading levels did not form distinct release sections."
                ),
            )

    window_text = "".join(section.section_text for section in sections)
    character_count = len(window_text)
    if character_count > max_characters:
        return _problem(
            "window_too_large",
            crossed_releases,
            changelog,
            (
                "The complete crossed-release Markdown window exceeded the admitted "
                f"character bound ({character_count} > {max_characters}); no section "
                "was truncated."
            ),
        )

    return CrossedReleaseSourceWindow(
        repository=repository,
        interval=crossed_releases.interval,
        path=changelog.path,
        blob_sha=changelog.blob_sha,
        resolved_commit_sha=changelog.resolved_commit_sha,
        trusted_ordered_versions=versions,
        sections=tuple(sections),
        source_ordered_versions=source_ordered_versions,
        text=window_text,
        character_count=character_count,
        max_characters=max_characters,
    )


def _release_heading_titles(versions: tuple[str, ...]) -> dict[str, str] | None:
    titles: dict[str, str] = {}
    for version in versions:
        for title in (version, f"v{version}"):
            existing = titles.get(title)
            if existing is not None and existing != version:
                return None
            titles[title] = version
    return titles


def _index_source_lines(content: str) -> tuple[_IndexedSourceLine, ...]:
    records: list[_IndexedSourceLine] = []
    offset = 0
    for number, raw_line in enumerate(content.splitlines(keepends=True), start=1):
        text = raw_line.rstrip("\r\n")
        start = offset
        end = start + len(text)
        records.append(
            _IndexedSourceLine(
                ChangelogSourceLine(
                    line_id=f"L{number}",
                    line_number=number,
                    text=text,
                    start_offset=start,
                    end_offset=end,
                )
            )
        )
        offset += len(raw_line)
    return tuple(records)


def _scan_atx_headings(
    lines: tuple[_IndexedSourceLine, ...],
) -> tuple[_AtxHeading, ...]:
    headings: list[_AtxHeading] = []
    fence_character: str | None = None
    fence_length = 0

    for index, indexed in enumerate(lines):
        text = indexed.line.text
        if fence_character is not None:
            if _is_closing_fence(text, fence_character, fence_length):
                fence_character = None
                fence_length = 0
            continue

        fence = _opening_fence(text)
        if fence is not None:
            fence_character, fence_length = fence
            continue

        parsed = _parse_atx_heading(text)
        if parsed is not None:
            headings.append(
                _AtxHeading(
                    level=parsed[0],
                    title=parsed[1],
                    line_index=index,
                    start_offset=indexed.line.start_offset,
                )
            )
    return tuple(headings)


def _opening_fence(text: str) -> tuple[str, int] | None:
    match = _FENCE_OPEN.fullmatch(text)
    if match is None:
        return None
    marker = match.group(1)
    return marker[0], len(marker)


def _is_closing_fence(text: str, character: str, minimum_length: int) -> bool:
    stripped = text.lstrip(" ")
    if len(text) - len(stripped) > 3:
        return False
    marker_length = len(stripped) - len(stripped.lstrip(character))
    return (
        marker_length >= minimum_length
        and not stripped[marker_length:].strip(" \t")
    )


def _parse_atx_heading(text: str) -> tuple[int, str] | None:
    match = _ATX_HEADING.fullmatch(text)
    if match is None:
        return None
    title = (match.group(2) or "").strip(" \t")
    title = re.sub(r"[ \t]+#+[ \t]*$", "", title).strip(" \t")
    return len(match.group(1)), title


def _section_end_line_index(
    heading: _AtxHeading,
    headings: tuple[_AtxHeading, ...],
    line_count: int,
) -> int:
    for candidate in headings:
        if (
            candidate.line_index > heading.line_index
            and candidate.level <= heading.level
        ):
            return candidate.line_index
    return line_count


def _validated_repository(value: str) -> str | None:
    try:
        return validate_repository(value)
    except (TypeError, ValueError):
        return None


def _trimmed_text(value: object) -> bool:
    return isinstance(value, str) and bool(value) and value == value.strip()


def _problem(
    state: CrossedReleaseSourceWindowProblemState,
    crossed_releases: CrossedReleaseIndexEvidence,
    changelog: TaggedChangelogEvidence,
    detail: str,
    *,
    release_version: str | None = None,
) -> CrossedReleaseSourceWindowProblem:
    return CrossedReleaseSourceWindowProblem(
        state=state,
        repository=crossed_releases.repository,
        interval=crossed_releases.interval,
        path=changelog.path,
        detail=detail,
        release_version=release_version,
    )


__all__ = (
    "ChangelogSourceLine",
    "CrossedReleaseMarkdownSection",
    "CrossedReleaseSourceWindow",
    "CrossedReleaseSourceWindowProblem",
    "CrossedReleaseSourceWindowProblemState",
    "CrossedReleaseSourceWindowResult",
    "build_crossed_release_source_window",
)
