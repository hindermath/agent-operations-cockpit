#!/usr/bin/env python3
"""Exercise the sync-home CLI no-op path with the platform Bash version."""

from __future__ import annotations

import os
from pathlib import Path
import subprocess
import tempfile
import unittest


REPOSITORY = Path(__file__).resolve().parents[2]
SCRIPT = REPOSITORY / "scripts" / "sync-home.sh"


@unittest.skipIf(os.name == "nt", "The Bash CLI test runs on macOS and Linux.")
class SyncHomeCliTests(unittest.TestCase):
    def test_second_real_sync_is_a_successful_no_op(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            environment = os.environ.copy()
            environment["HOME"] = str(home)
            for key, value in (
                ("user.name", "Home Sync Test"),
                ("user.email", "home-sync@example.invalid"),
            ):
                subprocess.run(
                    ["git", "config", "--global", key, value],
                    env=environment,
                    check=True,
                )

            first = subprocess.run(
                ["bash", str(SCRIPT), "--no-pull"],
                cwd=REPOSITORY,
                env=environment,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
            )
            self.assertEqual(first.returncode, 0, first.stdout)

            second = subprocess.run(
                ["bash", str(SCRIPT), "--no-pull"],
                cwd=REPOSITORY,
                env=environment,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
            )
            self.assertEqual(second.returncode, 0, second.stdout)
            self.assertIn("kein Commit nötig", second.stdout)
            status = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=home,
                text=True,
                stdout=subprocess.PIPE,
                check=True,
            )
            self.assertEqual(status.stdout, "")


if __name__ == "__main__":
    unittest.main()
