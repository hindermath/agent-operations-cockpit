"""Regression checks for the local pre-push commit-scan boundary."""

from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


HOOK = Path(__file__).resolve().parents[1] / "hooks" / "pre-push"
ZERO_SHA = "0" * 40


class PrePushHookTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.repo = self.root / "work"
        self.repo.mkdir()
        self.private = self.root / "private.git"
        self.public = self.root / "public.git"
        self.tools = self.root / "tools"
        self.tools.mkdir()

        self.git("init", "-q", cwd=self.repo)
        self.git("checkout", "-q", "-b", "main")
        self.git("config", "user.email", "hook-test@example.invalid")
        self.git("config", "user.name", "Hook Test")
        (self.repo / "example.txt").write_text("safe content\n", encoding="utf-8")
        self.git("add", "example.txt")
        self.git("commit", "-qm", "initial")
        self.head = self.git("rev-parse", "HEAD").stdout.strip()
        self.git("init", "--bare", "-q", str(self.private), cwd=self.root)
        self.git("init", "--bare", "-q", str(self.public), cwd=self.root)
        self.git("remote", "add", "private", str(self.private))
        self.git("remote", "add", "public", str(self.public))
        self.git("push", "-q", "private", "main")

    def git(self, *args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *args], cwd=cwd or self.repo, check=True,
            text=True, capture_output=True,
        )

    def run_hook(
        self, remote_sha: str, *, scanner: bool, remote_name: str = "public"
    ) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["PATH"] = f"{self.tools}:/usr/bin:/bin"
        env["GITLEAKS_ARGUMENTS"] = str(self.root / "gitleaks-arguments.txt")
        if scanner:
            stub = self.tools / "gitleaks"
            stub.write_text(
                '#!/bin/sh\nprintf "%s\\n" "$@" > "$GITLEAKS_ARGUMENTS"\n',
                encoding="utf-8",
            )
            stub.chmod(0o755)
        else:
            git_executable = shutil.which("git")
            assert git_executable is not None
            (self.tools / "git").symlink_to(git_executable)

        ref_line = f"refs/heads/main {self.head} refs/heads/main {remote_sha}\n"
        return subprocess.run(
            ["/bin/bash", str(HOOK), remote_name, str(self.public)],
            cwd=self.repo, env=env, input=ref_line,
            text=True, capture_output=True,
        )

    def test_new_ref_on_other_remote_is_scanned(self) -> None:
        result = self.run_hook(ZERO_SHA, scanner=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        args = (self.root / "gitleaks-arguments.txt").read_text(encoding="utf-8")
        self.assertIn(f"--log-opts={self.head}", args)
        self.assertNotIn("--remotes", args)

    def test_pushurl_is_used_instead_of_fetch_url(self) -> None:
        self.git("remote", "add", "mixed", str(self.private))
        self.git("remote", "set-url", "--push", "mixed", str(self.public))
        result = self.run_hook(ZERO_SHA, scanner=True, remote_name="mixed")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        args = (self.root / "gitleaks-arguments.txt").read_text(encoding="utf-8")
        self.assertIn(f"--log-opts={self.head}", args)
        self.assertNotIn("--not", args)

    def test_missing_gitleaks_blocks_push(self) -> None:
        result = self.run_hook(ZERO_SHA, scanner=False)
        self.assertEqual(result.returncode, 2)
        self.assertIn("gitleaks fehlt", result.stderr)

    def test_unavailable_remote_sha_blocks_push(self) -> None:
        result = self.run_hook("f" * 40, scanner=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("Commit-Range", result.stderr)
        self.assertFalse((self.root / "gitleaks-arguments.txt").exists())


if __name__ == "__main__":
    unittest.main()
