"""Focused tests for exact Forgejo/Codeberg teardown identity binding."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


PARSER = Path(__file__).resolve().parents[1] / "lib" / "validate_forgejo_teardown_remote.py"
SPEC = importlib.util.spec_from_file_location("validate_forgejo_teardown_remote", PARSER)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ForgejoTeardownRemoteTests(unittest.TestCase):
    def test_matching_https_and_ssh_origins(self) -> None:
        for origin in (
            "https://forgejo.example/owner/repo.git",
            "git@forgejo.example:owner/repo.git",
            "ssh://git@forgejo.example/owner/repo.git",
        ):
            with self.subTest(origin=origin):
                self.assertEqual(
                    MODULE.validate_remote(
                        origin, "https://forgejo.example", "forgejo", "owner", "repo"
                    ),
                    "https://forgejo.example/owner/repo",
                )

    def test_rejects_different_target_or_host(self) -> None:
        for origin, base_url, platform, owner, repository in (
            ("https://forgejo.example/owner/repo.git", "https://forgejo.example", "forgejo", "owner", "other"),
            ("https://other.example/owner/repo.git", "https://forgejo.example", "forgejo", "owner", "repo"),
            ("https://codeberg.org/owner/repo.git", "https://other.example", "codeberg", "owner", "repo"),
            ("https://forgejo.example/owner/other.git", "https://forgejo.example", "forgejo", "owner", "repo"),
            ("https://forgejo.example/owner/repo/extra.git", "https://forgejo.example", "forgejo", "owner", "repo"),
            ("git@forgejo.example:owner/repo.git", "https://forgejo.example:8443", "forgejo", "owner", "repo"),
        ):
            with self.subTest(origin=origin, repository=repository):
                self.assertIsNone(
                    MODULE.validate_remote(origin, base_url, platform, owner, repository)
                )

    def test_codeberg_and_subpath(self) -> None:
        self.assertEqual(
            MODULE.validate_remote(
                "https://codeberg.org/owner/repo.git", "https://codeberg.org",
                "codeberg", "owner", "repo",
            ),
            "https://codeberg.org/owner/repo",
        )
        self.assertEqual(
            MODULE.validate_remote(
                "https://forgejo.example/prefix/owner/repo.git",
                "https://forgejo.example/prefix", "forgejo", "owner", "repo",
            ),
            "https://forgejo.example/prefix/owner/repo",
        )


if __name__ == "__main__":
    unittest.main()
