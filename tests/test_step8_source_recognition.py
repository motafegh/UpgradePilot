"""Protect Step 8 source recognition before coordinator implementation."""

from __future__ import annotations

import unittest

from upgradepilot.dependency.analysis import is_uv_lock_file
from upgradepilot.dependency.uv_lock import is_modified_uv_lock_file
from upgradepilot.github.pull_request import ChangedFile


def _changed(path: str, *, status: str = "modified") -> ChangedFile:
    return ChangedFile(
        filename=path,
        status=status,
        additions=1,
        deletions=1,
        changes=2,
        patch=None,
    )


class Step8SourceRecognitionTests(unittest.TestCase):
    def test_uv_lock_path_recognition_is_separate_from_status_admission(self) -> None:
        for status in ("modified", "added", "deleted", "renamed"):
            with self.subTest(status=status):
                changed_file = _changed("services/api/uv.lock", status=status)
                self.assertTrue(is_uv_lock_file(changed_file))
                self.assertEqual(
                    is_modified_uv_lock_file(changed_file),
                    status == "modified",
                )

    def test_uv_lock_recognition_rejects_other_or_non_normalized_paths(self) -> None:
        for path in (
            "uv.lock.backup",
            "UV.LOCK",
            "/uv.lock",
            "a/../uv.lock",
            "a//uv.lock",
            "a\\uv.lock",
        ):
            with self.subTest(path=path):
                changed_file = _changed(path)
                self.assertFalse(is_uv_lock_file(changed_file))
                self.assertFalse(is_modified_uv_lock_file(changed_file))


if __name__ == "__main__":
    unittest.main()
