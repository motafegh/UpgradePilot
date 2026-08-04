"""Test deterministic Step 7B crossed-release Markdown source windows."""

from __future__ import annotations

import unittest
from datetime import datetime, timezone

from upgradepilot.upstream.changelog import (
    CrossedReleaseSourceWindow,
    CrossedReleaseSourceWindowProblem,
    build_crossed_release_source_window,
)
from upgradepilot.upstream.interval import (
    CrossedReleaseIndexEvidence,
    DependencyReleaseInterval,
    TaggedChangelogEvidence,
)

_NOW = datetime(2026, 8, 4, 18, 0, tzinfo=timezone.utc)
_REPOSITORY = "example/friendly-bard"


def _interval(
    *,
    old: str = "2.6",
    proposed: str = "2.8.4",
) -> DependencyReleaseInterval:
    return DependencyReleaseInterval(
        package="friendly-bard",
        normalized_package="friendly-bard",
        old_version=old,
        proposed_version=proposed,
    )


def _index(
    versions: tuple[str, ...],
    *,
    repository: str = _REPOSITORY,
    interval: DependencyReleaseInterval | None = None,
) -> CrossedReleaseIndexEvidence:
    return CrossedReleaseIndexEvidence(
        repository=repository,
        interval=interval or _interval(),
        ordered_versions=versions,
        source_url="https://pypi.org/pypi/friendly-bard/json",
        retrieved_at=_NOW,
    )


def _changelog(
    content: str,
    *,
    repository: str = _REPOSITORY,
    interval: DependencyReleaseInterval | None = None,
) -> TaggedChangelogEvidence:
    byte_count = len(content.encode("utf-8"))
    selected_interval = interval or _interval()
    return TaggedChangelogEvidence(
        repository=repository,
        interval=selected_interval,
        requested_tag=selected_interval.proposed_version,
        tag_ref=f"refs/tags/{selected_interval.proposed_version}",
        tag_object_type="commit",
        tag_object_sha="a" * 40,
        resolved_commit_sha="a" * 40,
        path="docs/changelog.md",
        returned_path="docs/changelog.md",
        blob_sha="b" * 40,
        reported_byte_count=byte_count,
        decoded_byte_count=byte_count,
        content=content,
        retrieved_at=_NOW,
    )


class CrossedReleaseSourceWindowTests(unittest.TestCase):
    def test_complete_reverse_chronological_sections_preserve_exact_source(self) -> None:
        content = (
            "# Changelog\n\n"
            "## 2.9\nfuture\n\n"
            "## 2.8.4\nfix\n### Notes\nnested detail\n\n"
            "## 2.8\n- Drop support for Python 3.8.\n\n"
            "## 2.7\n- Add feature.\n\n"
            "## 2.6\nold\n"
        )

        result = build_crossed_release_source_window(
            _index(("2.7", "2.8", "2.8.4")),
            _changelog(content),
        )

        self.assertIsInstance(result, CrossedReleaseSourceWindow)
        assert isinstance(result, CrossedReleaseSourceWindow)
        self.assertEqual(result.source_ordered_versions, ("2.8.4", "2.8", "2.7"))
        self.assertEqual(
            tuple(section.release_version for section in result.sections),
            result.source_ordered_versions,
        )
        self.assertNotIn("## 2.9", result.text)
        self.assertNotIn("## 2.6", result.text)
        self.assertIn("Drop support for Python 3.8.", result.text)

        first = result.sections[0]
        self.assertEqual(first.heading_line_id, "L6")
        self.assertEqual(first.heading_line_number, 6)
        self.assertEqual(first.source_line_ids, ("L6", "L7", "L8", "L9", "L10"))
        self.assertEqual(content[first.start_offset:first.end_offset], first.section_text)
        self.assertEqual(result.character_count, len(result.text))

    def test_v_prefix_and_closing_atx_hashes_are_admitted(self) -> None:
        content = (
            "## v2.8.4 ##\nfix\n"
            "## v2.8 ##\nchange\n"
            "## v2.7 ##\nchange\n"
        )

        result = build_crossed_release_source_window(
            _index(("2.7", "2.8", "2.8.4")),
            _changelog(content),
        )

        self.assertIsInstance(result, CrossedReleaseSourceWindow)
        assert isinstance(result, CrossedReleaseSourceWindow)
        self.assertEqual(result.source_ordered_versions, ("2.8.4", "2.8", "2.7"))

    def test_heading_like_text_inside_fenced_code_is_not_a_release_heading(self) -> None:
        content = (
            "## 2.8.4\nfix\n"
            "```text\n## 2.8\nnot a heading\n```\n"
            "## 2.8\nreal section\n"
            "## 2.7\nreal section\n"
        )

        result = build_crossed_release_source_window(
            _index(("2.7", "2.8", "2.8.4")),
            _changelog(content),
        )

        self.assertIsInstance(result, CrossedReleaseSourceWindow)
        assert isinstance(result, CrossedReleaseSourceWindow)
        self.assertEqual(result.sections[1].heading_line_id, "L7")

    def test_non_exact_release_heading_remains_missing(self) -> None:
        content = "## 2.8.4\nfix\n## Release 2.8\nchange\n## 2.7\nchange\n"

        result = build_crossed_release_source_window(
            _index(("2.7", "2.8", "2.8.4")),
            _changelog(content),
        )

        self.assertIsInstance(result, CrossedReleaseSourceWindowProblem)
        assert isinstance(result, CrossedReleaseSourceWindowProblem)
        self.assertEqual(result.state, "missing_release_section")
        self.assertEqual(result.release_version, "2.8")

    def test_duplicate_release_heading_stops(self) -> None:
        content = "## 2.8.4\nfix\n## 2.8\none\n## 2.8\ntwo\n## 2.7\nchange\n"

        result = build_crossed_release_source_window(
            _index(("2.7", "2.8", "2.8.4")),
            _changelog(content),
        )

        self.assertIsInstance(result, CrossedReleaseSourceWindowProblem)
        assert isinstance(result, CrossedReleaseSourceWindowProblem)
        self.assertEqual(result.state, "duplicate_release_section")
        self.assertEqual(result.release_version, "2.8")

    def test_scrambled_release_order_stops(self) -> None:
        content = "## 2.8.4\nfix\n## 2.7\nchange\n## 2.8\nchange\n"

        result = build_crossed_release_source_window(
            _index(("2.7", "2.8", "2.8.4")),
            _changelog(content),
        )

        self.assertIsInstance(result, CrossedReleaseSourceWindowProblem)
        assert isinstance(result, CrossedReleaseSourceWindowProblem)
        self.assertEqual(result.state, "source_order_conflict")

    def test_nested_release_heading_that_overlaps_another_release_stops(self) -> None:
        content = "## 2.8.4\nfix\n### 2.8\nchange\n## 2.7\nchange\n"

        result = build_crossed_release_source_window(
            _index(("2.7", "2.8", "2.8.4")),
            _changelog(content),
        )

        self.assertIsInstance(result, CrossedReleaseSourceWindowProblem)
        assert isinstance(result, CrossedReleaseSourceWindowProblem)
        self.assertEqual(result.state, "source_order_conflict")

    def test_complete_window_over_bound_stops_without_truncation(self) -> None:
        content = "## 2.8.4\nabcdefghij\n## 2.8\nabcdefghij\n## 2.7\nabcdefghij\n"

        result = build_crossed_release_source_window(
            _index(("2.7", "2.8", "2.8.4")),
            _changelog(content),
            max_characters=20,
        )

        self.assertIsInstance(result, CrossedReleaseSourceWindowProblem)
        assert isinstance(result, CrossedReleaseSourceWindowProblem)
        self.assertEqual(result.state, "window_too_large")
        self.assertIn("no section was truncated", result.detail)

    def test_crlf_line_ids_and_character_offsets_reference_original_content(self) -> None:
        interval = _interval(old="2.8", proposed="2.8.4")
        content = "## 2.8.4\r\nαβ\r\n## 2.8.3\r\nold\r\n"

        result = build_crossed_release_source_window(
            _index(("2.8.4",), interval=interval),
            _changelog(content, interval=interval),
        )

        self.assertIsInstance(result, CrossedReleaseSourceWindow)
        assert isinstance(result, CrossedReleaseSourceWindow)
        section = result.sections[0]
        self.assertEqual(section.source_line_ids, ("L1", "L2"))
        self.assertEqual(section.end_offset, content.index("## 2.8.3"))
        self.assertEqual(content[section.start_offset:section.end_offset], section.section_text)
        self.assertEqual(section.source_lines[1].start_offset, len("## 2.8.4\r\n"))
        self.assertEqual(section.source_lines[1].end_offset, len("## 2.8.4\r\nαβ"))

    def test_repository_or_interval_mismatch_stops(self) -> None:
        interval = _interval(old="2.8", proposed="2.8.4")
        other_interval = _interval(old="1.0", proposed="2.8.4")
        cases = (
            (
                _index(("2.8.4",), repository="other/project", interval=interval),
                _changelog("## 2.8.4\nchange\n", interval=interval),
            ),
            (
                _index(("2.8.4",), interval=interval),
                _changelog("## 2.8.4\nchange\n", interval=other_interval),
            ),
        )

        for crossed, changelog in cases:
            with self.subTest(crossed=crossed, changelog=changelog):
                result = build_crossed_release_source_window(crossed, changelog)
                self.assertIsInstance(result, CrossedReleaseSourceWindowProblem)
                assert isinstance(result, CrossedReleaseSourceWindowProblem)
                self.assertEqual(result.state, "identity_mismatch")

    def test_invalid_character_bound_is_rejected(self) -> None:
        interval = _interval(old="2.8", proposed="2.8.4")
        crossed = _index(("2.8.4",), interval=interval)
        changelog = _changelog("## 2.8.4\nchange\n", interval=interval)

        for value in (0, -1, True):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    build_crossed_release_source_window(
                        crossed,
                        changelog,
                        max_characters=value,
                    )


if __name__ == "__main__":
    unittest.main()
