"""Test the temporary legacy-to-canonical dependency ingress boundary.

Step 6 keeps the validated exact-requirements command ingress temporarily, but no
runtime stage after that boundary may consume ``PinnedDependencyChange``. These tests
prove that the compatibility function converts generic legacy evidence into the shared
``DependencyVersionChange`` while carrying the direct-requirements CI path separately.
"""

from __future__ import annotations

import unittest

from upgradepilot.dependency_change import (
    DependencyFileEvidence,
    DependencyVersionChange,
    LegacyDependencyIngress,
    UnsupportedDependencyChange,
    extract_legacy_dependency_ingress,
)
from upgradepilot.github_client import ChangedFile


def _changed_file(patch: str) -> ChangedFile:
    """Build one complete fictional exact-requirements patch."""

    return ChangedFile(
        filename="requirements-ci.txt",
        status="modified",
        additions=1,
        deletions=1,
        changes=2,
        patch=patch,
    )


class LegacyDependencyIngressTests(unittest.TestCase):
    """Protect canonical conversion and containment of the legacy result."""

    def test_converts_legacy_success_to_canonical_identity_and_separate_ci_path(
        self,
    ) -> None:
        result = extract_legacy_dependency_ingress(
            [
                _changed_file(
                    "-Example_Package==1.2.3\n"
                    "+Example_Package==1.3.0"
                )
            ]
        )

        self.assertIsInstance(result, LegacyDependencyIngress)
        assert isinstance(result, LegacyDependencyIngress)

        self.assertEqual(
            result.dependency,
            DependencyVersionChange(
                package="Example_Package",
                normalized_package="example-package",
                old_version="1.2.3",
                proposed_version="1.3.0",
                source_evidence=(
                    DependencyFileEvidence(
                        path="requirements-ci.txt",
                        file_format="exact_requirement",
                        extraction_method="changed_file_patch",
                    ),
                ),
            ),
        )
        self.assertEqual(
            result.direct_requirements_install_path,
            "requirements-ci.txt",
        )
        self.assertFalse(hasattr(result.dependency, "source_file"))

    def test_preserves_legacy_abstention_without_constructing_canonical_identity(
        self,
    ) -> None:
        result = extract_legacy_dependency_ingress(
            [_changed_file("-Example_Package>=1.2.3\n+Example_Package>=1.3.0")]
        )

        self.assertIsInstance(result, UnsupportedDependencyChange)
        assert isinstance(result, UnsupportedDependencyChange)
        self.assertEqual(result.reason, "no_supported_pinned_change")


if __name__ == "__main__":
    unittest.main()
