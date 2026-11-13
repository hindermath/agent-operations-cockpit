#!/usr/bin/env python3
"""Focused regression tests for cross-shell security boundaries."""

from __future__ import annotations

import importlib.util
import codecs
import hashlib
import os
from pathlib import Path
import shlex
import shutil
import stat
import struct
import tarfile
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest import mock
import zipfile


LIBRARY = Path(__file__).resolve().parents[1] / "lib"


def path_without_gitleaks(root: Path) -> str:
    """Expose only the local tools needed by package scripts, without gitleaks."""
    tool_directory = root / "tools-without-gitleaks"
    tool_directory.mkdir()
    for name in ("git", "rsync", "zip", "shasum", "python3", "python", "tr", "date",
                 "mktemp", "mkdir", "cp", "rm", "sed", "awk", "find", "wc", "sort",
                 "grep", "basename", "dirname", "pwd", "cat", "head"):
        executable = shutil.which(name)
        if executable:
            (tool_directory / name).symlink_to(executable)
    return str(tool_directory)


def load_helper(name: str):
    specification = importlib.util.spec_from_file_location(name, LIBRARY / f"{name}.py")
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


archive = load_helper("check_learning_package_archive")
memory_patch = load_helper("apply_memory_patch")
baseline = load_helper("check_baseline_sync_path")
bootstrap_target = load_helper("check_bootstrap_target_symlinks")
origin = load_helper("validate_bootstrap_origin")
package_source = load_helper("check_learning_package_source")
teardown_remote = load_helper("parse_teardown_remote")


def teardown_fixture(root: Path) -> tuple[Path, Path, dict[str, str]]:
    home = root / "home"
    home.mkdir()
    source = home / "ConfiguredSource"
    scripts = source / "scripts"
    scripts.mkdir(parents=True)
    (scripts / "sync-home.sh").write_text("#!/usr/bin/env bash\n", encoding="utf-8")
    (scripts / "sync-home.ps1").write_text("#Requires -Version 7\n", encoding="utf-8")
    subprocess.run(["git", "-C", str(source), "init", "-q"], check=True)
    subprocess.run(["git", "-C", str(source), "remote", "add", "origin",
                    "https://example.invalid/home-baseline.git"], check=True)
    workspace = home / "Demo"
    workspace.mkdir()
    environment = dict(os.environ, HOME=str(home), HOME_BASELINE_SOURCE=str(source))
    return home, workspace, environment


class SecurityBoundaryHelpersTests(unittest.TestCase):
    @unittest.skipIf(os.name == "nt", "POSIX wildcard filename fixture")
    def test_memory_patch_is_contained_and_commits_only_its_target(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            repository = root / "repository"
            repository.mkdir()
            subprocess.run(["git", "init", "-q", str(repository)], check=True)
            subprocess.run(["git", "-C", str(repository), "config", "user.name", "Test"], check=True)
            subprocess.run(["git", "-C", str(repository), "config", "user.email", "test@example.invalid"], check=True)
            (repository / "README.md").write_text("original\n", encoding="utf-8")
            (repository / "other.md").write_text("other\n", encoding="utf-8")
            (repository / "foobar.md").write_text("tracked\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(repository), "add", "README.md", "other.md", "foobar.md"], check=True)
            subprocess.run(["git", "-C", str(repository), "commit", "-qm", "initial"], check=True)
            outside = root / "outside.md"
            outside.write_text("private\n", encoding="utf-8")
            patch = root / "memory-patch.md"
            patch.write_text("### Target: README.md\n+++ unexpected\n", encoding="utf-8")
            original_head = subprocess.run(["git", "-C", str(repository), "rev-parse", "HEAD"],
                                           capture_output=True, text=True, check=True).stdout.strip()
            for command in (["bash", str(LIBRARY.parent / "check-homogeneity.sh"),
                             "--dry-run", "--apply-patch", str(patch), "--yes", str(repository)],
                            ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "check-homogeneity.ps1"),
                             "-DryRun", "-ApplyPatch", str(patch), "-Yes", "-TargetDir", str(repository)]):
                if not shutil.which(command[0]):
                    continue
                result = subprocess.run(command, capture_output=True, text=True, check=False)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertEqual((repository / "README.md").read_text(encoding="utf-8"), "original\n")
                current_head = subprocess.run(["git", "-C", str(repository), "rev-parse", "HEAD"],
                                              capture_output=True, text=True, check=True).stdout.strip()
                self.assertEqual(current_head, original_head)
            for command in (["bash", str(LIBRARY.parent / "check-homogeneity.sh"),
                             "--apply-patch", str(patch), "--yes", str(repository)],
                            ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "check-homogeneity.ps1"),
                             "-ApplyPatch", str(patch), "-Yes", "-TargetDir", str(repository)]):
                if not shutil.which(command[0]):
                    continue
                patch.write_text(f"### Target: {outside}\n+++ injected\n", encoding="utf-8")
                result = subprocess.run(command, capture_output=True, text=True, check=False)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertEqual(outside.read_text(encoding="utf-8"), "private\n")
            wildcard = repository / "foo*.md"
            wildcard.write_text("untracked\n", encoding="utf-8")
            patch.write_text("### Target: foo*.md\n+++ injected\n", encoding="utf-8")
            result = subprocess.run(["bash", str(LIBRARY.parent / "check-homogeneity.sh"),
                                     "--apply-patch", str(patch), "--yes", str(repository)],
                                    capture_output=True, text=True, check=False)
            self.assertNotEqual(result.returncode, 0, result.stdout)
            self.assertEqual(wildcard.read_text(encoding="utf-8"), "untracked\n")
            patch.write_text("### Target: README.md\n+++ [Review needed: inspect]\n", encoding="utf-8")
            result = subprocess.run(["bash", str(LIBRARY.parent / "check-homogeneity.sh"),
                                     "--apply-patch", str(patch), "--yes", str(repository)],
                                    capture_output=True, text=True, check=False)
            self.assertNotEqual(result.returncode, 0, result.stdout)
            self.assertEqual((repository / "README.md").read_text(encoding="utf-8"), "original\n")
            _, relative, identity = memory_patch.checked_target(repository, "README.md")
            replacement = repository / "replacement.tmp"
            replacement.write_text("original\n", encoding="utf-8")
            os.replace(replacement, repository / "README.md")
            with self.assertRaisesRegex(ValueError, "validated file"):
                memory_patch.open_target(repository, relative, identity)
            (repository / "other.md").write_text("unrelated staged\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(repository), "add", "other.md"], check=True)
            patch.write_text("### Target: README.md\n+++ approved\n", encoding="utf-8")
            result = subprocess.run(["bash", str(LIBRARY.parent / "check-homogeneity.sh"),
                                     "--apply-patch", str(patch), "--yes", str(repository)],
                                    capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            committed = subprocess.run(["git", "-C", str(repository), "show", "--pretty=format:",
                                        "--name-only", "HEAD"], capture_output=True, text=True,
                                       check=True).stdout.strip().splitlines()
            self.assertEqual(committed, ["README.md"])
            staged = subprocess.run(["git", "-C", str(repository), "diff", "--cached", "--name-only"],
                                    capture_output=True, text=True, check=True).stdout.strip().splitlines()
            self.assertEqual(staged, ["other.md"])

    def test_teardown_remote_requires_exact_provider_host(self) -> None:
        self.assertEqual(teardown_remote.parse_remote("https://github.com/owner/repository.git"),
                         ("github", "owner/repository"))
        self.assertEqual(teardown_remote.parse_remote("git@gitlab.com:group/sub/repository.git"),
                         ("gitlab", "group/sub/repository"))
        self.assertEqual(teardown_remote.parse_remote("ssh://git@github.com/owner/repository.git"),
                         ("github", "owner/repository"))
        for remote in ("https://evil.invalid/github.com/owner/victim.git",
                       "https://github.com.evil.invalid/owner/victim.git",
                       "https://github.com/owner/victim.git?x=1",
                       "https://github.com/owner/../victim.git",
                       "https://user:secret@github.com/owner/victim.git"):
            with self.subTest(remote=remote):
                self.assertIsNone(teardown_remote.parse_remote(remote))

    @unittest.skipIf(os.name == "nt", "POSIX fake command fixture")
    def test_teardown_rejects_remote_changed_after_preview(self) -> None:
        real_git = shutil.which("git")
        assert real_git is not None
        for shell, replacement in (("bash", "https://github.com/owner/other.git"),
                                   ("pwsh", "https://github.com/owner/other.git"),
                                   ("pwsh", "https://github.com/owner/APPROVED.git")):
            if not shutil.which(shell):
                continue
            with self.subTest(shell=shell, replacement=replacement), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                _, workspace, environment = teardown_fixture(root)
                subprocess.run(["git", "-C", str(workspace), "init", "-q"], check=True)
                subprocess.run(["git", "-C", str(workspace), "remote", "add", "origin",
                                "https://github.com/owner/approved.git"], check=True)
                fake = root / "bin"
                fake.mkdir()
                count = root / "remote-reads"
                marker = root / "provider-called"
                git_wrapper = fake / "git"
                change_after = 2 if shell == "pwsh" else 3
                git_wrapper.write_text(
                    "#!/bin/sh\n"
                    'case "$2" in */Demo) candidate=1 ;; *) candidate=0 ;; esac\n'
                    'if [ "$1" = -C ] && [ "$candidate" = 1 ] && '
                    '[ "$3" = remote ] && [ "$4" = get-url ]; then\n'
                    f'  count=$(cat {shlex.quote(str(count))} 2>/dev/null || printf 0)\n'
                    '  count=$((count + 1))\n'
                    f'  printf "%s" "$count" > {shlex.quote(str(count))}\n'
                    f'  if [ "$count" -ge {change_after} ]; then '
                    f"printf '%s\\n' {shlex.quote(replacement)}; exit 0; fi\n"
                    'fi\n'
                    f'exec {shlex.quote(real_git)} "$@"\n', encoding="utf-8")
                git_wrapper.chmod(0o755)
                provider = fake / "gh"
                provider.write_text(f"#!/bin/sh\nprintf called > {shlex.quote(str(marker))}\n",
                                    encoding="utf-8")
                provider.chmod(0o755)
                environment["PATH"] = f"{fake}{os.pathsep}{os.environ['PATH']}"
                command = (["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                            "Demo", "--force", "--yes"] if shell == "bash" else
                           ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "teardown-workspace.ps1"),
                            "-WorkspaceName", "Demo", "-Force", "-Yes"])
                result = subprocess.run(command, env=environment, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertEqual(count.read_text(encoding="utf-8"), str(change_after))
                self.assertFalse(marker.exists(), result.stdout)
                self.assertTrue(workspace.exists())

    @unittest.skipIf(os.name == "nt", "POSIX fake command fixture")
    def test_requested_backup_failure_preserves_workspace(self) -> None:
        for shell in ("bash", "pwsh"):
            if not shutil.which(shell):
                continue
            with self.subTest(shell=shell), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                _, workspace, environment = teardown_fixture(root)
                (workspace / "payload.txt").write_text("keep\n", encoding="utf-8")
                fake = root / "bin"
                fake.mkdir()
                tar = fake / "tar"
                tar.write_text("#!/bin/sh\nexit 1\n", encoding="utf-8")
                tar.chmod(0o755)
                environment["PATH"] = f"{fake}{os.pathsep}{os.environ['PATH']}"
                command = (["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                            "Demo", "--backup", "--keep-remote", "--force", "--yes"]
                           if shell == "bash" else
                           ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "teardown-workspace.ps1"),
                            "-WorkspaceName", "Demo", "-Backup", "-KeepRemote", "-Force", "-Yes"])
                result = subprocess.run(command, env=environment, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertTrue((workspace / "payload.txt").exists(), result.stdout)

    @unittest.skipIf(os.name == "nt", "POSIX fake Git fixture")
    def test_teardown_git_inspection_failure_preserves_workspace(self) -> None:
        real_git = shutil.which("git")
        assert real_git is not None
        for failed_command in ("rev-parse", "status", "rev-list", "config-get"):
            with self.subTest(failed_command=failed_command), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                _, workspace, environment = teardown_fixture(root)
                subprocess.run(["git", "-C", str(workspace), "init", "-q"], check=True)
                subprocess.run(["git", "-C", str(workspace), "config", "user.name", "Test"], check=True)
                subprocess.run(["git", "-C", str(workspace), "config", "user.email", "test@example.invalid"],
                               check=True)
                (workspace / "payload.txt").write_text("keep\n", encoding="utf-8")
                if failed_command in {"rev-list", "config-get"}:
                    subprocess.run(["git", "-C", str(workspace), "add", "payload.txt"], check=True)
                    subprocess.run(["git", "-C", str(workspace), "commit", "-qm", "initial"], check=True)
                    branch = subprocess.run(["git", "-C", str(workspace), "branch", "--show-current"],
                                            capture_output=True, text=True, check=True).stdout.strip()
                    if failed_command == "rev-list":
                        subprocess.run(["git", "-C", str(workspace), "update-ref",
                                        f"refs/remotes/origin/{branch}", "HEAD"], check=True)
                        subprocess.run(["git", "-C", str(workspace), "remote", "add", "origin",
                                        "https://example.invalid/workspace.git"], check=True)
                    subprocess.run(["git", "-C", str(workspace), "config",
                                    f"branch.{branch}.remote", "origin"], check=True)
                    subprocess.run(["git", "-C", str(workspace), "config",
                                    f"branch.{branch}.merge", f"refs/heads/{branch}"], check=True)
                fake = root / "bin"
                fake.mkdir()
                git_wrapper = fake / "git"
                failed_test = ('[ "$3" = config ] && [ "$4" = --local ] && [ "$5" = --get ]'
                               if failed_command == "config-get" else
                               f'[ "$3" = {failed_command} ]')
                git_wrapper.write_text(
                    "#!/bin/sh\n"
                    'if [ "${2##*/}" = Demo ] && '
                    f"{failed_test}; then exit 2; fi\n"
                    f'exec {shlex.quote(real_git)} "$@"\n', encoding="utf-8")
                git_wrapper.chmod(0o755)
                environment["PATH"] = f"{fake}{os.pathsep}{os.environ['PATH']}"
                result = subprocess.run(["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                                         "Demo", "--keep-remote", "--yes"],
                                        env=environment, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertTrue((workspace / "payload.txt").exists(), result.stdout)

    @unittest.skipIf(os.name == "nt", "POSIX fake command fixture")
    def test_teardown_find_failure_preserves_nested_repository(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            _, workspace, environment = teardown_fixture(root)
            child = workspace / "child"
            child.mkdir()
            subprocess.run(["git", "-C", str(child), "init", "-q"], check=True)
            (child / "local.txt").write_text("preserve\n", encoding="utf-8")
            fake = root / "bin"
            fake.mkdir()
            finder = fake / "find"
            finder.write_text("#!/bin/sh\nexit 2\n", encoding="utf-8")
            finder.chmod(0o755)
            environment["PATH"] = f"{fake}{os.pathsep}{os.environ['PATH']}"
            result = subprocess.run(["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                                     "Demo", "--keep-remote", "--yes"],
                                    env=environment, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0, result.stdout)
            self.assertIn("Level 2 projects unavailable", result.stderr)
            self.assertTrue((child / "local.txt").exists(), result.stdout)

    def test_teardown_preserves_ignored_local_file(self) -> None:
        for shell in ("bash", "pwsh"):
            if not shutil.which(shell):
                continue
            with self.subTest(shell=shell), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                _, workspace, environment = teardown_fixture(root)
                subprocess.run(["git", "-C", str(workspace), "init", "-q"], check=True)
                (workspace / ".git" / "info" / "exclude").write_text("local.txt\n", encoding="utf-8")
                (workspace / "local.txt").write_text("preserve\n", encoding="utf-8")
                command = (["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                            "Demo", "--keep-remote", "--yes"] if shell == "bash" else
                           ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "teardown-workspace.ps1"),
                            "-WorkspaceName", "Demo", "-KeepRemote", "-Yes"])
                result = subprocess.run(command, env=environment, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertTrue((workspace / "local.txt").exists(), result.stdout)

    @unittest.skipIf(os.name == "nt", "POSIX PATH fixture")
    def test_teardown_missing_gitlab_cli_preserves_workspace(self) -> None:
        for shell in ("bash", "pwsh"):
            if not shutil.which(shell):
                continue
            with self.subTest(shell=shell), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                _, workspace, environment = teardown_fixture(root)
                subprocess.run(["git", "-C", str(workspace), "init", "-q"], check=True)
                subprocess.run(["git", "-C", str(workspace), "remote", "add", "origin",
                                "https://gitlab.com/example/demo.git"], check=True)
                fake = root / "bin"
                fake.mkdir()
                for command_name in ("bash", "pwsh", "python3"):
                    executable = shutil.which(command_name)
                    if executable:
                        (fake / command_name).symlink_to(executable)
                environment["PATH"] = f"{fake}{os.pathsep}/usr/bin{os.pathsep}/bin"
                command = (["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                            "Demo", "--yes"] if shell == "bash" else
                           ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "teardown-workspace.ps1"),
                            "-WorkspaceName", "Demo", "-Yes"])
                result = subprocess.run(command, env=environment, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertIn("glab missing", result.stdout)
                self.assertTrue(workspace.exists(), result.stdout)

    def test_teardown_rejects_unresolvable_level0_source(self) -> None:
        for shell in ("bash", "pwsh"):
            if not shutil.which(shell):
                continue
            with self.subTest(shell=shell), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                home, _, environment = teardown_fixture(root)
                source = home / "ConfiguredSource"
                subprocess.run(["git", "-C", str(source), "remote", "remove", "origin"], check=True)
                command = (["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                            "ConfiguredSource", "--force", "--keep-remote", "--yes"] if shell == "bash" else
                           ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "teardown-workspace.ps1"),
                            "-WorkspaceName", "ConfiguredSource", "-Force", "-KeepRemote", "-Yes"])
                result = subprocess.run(command, env=environment, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertTrue((source / "scripts" / "sync-home.sh").exists(), result.stdout)

    @unittest.skipIf(os.name == "nt", "POSIX PATH fixture")
    def test_teardown_missing_jq_cannot_skip_configured_source(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            home, _, environment = teardown_fixture(root)
            source = home / "ConfiguredSource"
            fallback = home / "home-baseline-source"
            fallback.mkdir()
            (fallback / "scripts").mkdir()
            (fallback / "scripts" / "sync-home.sh").write_text("#!/bin/sh\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(fallback), "init", "-q"], check=True)
            subprocess.run(["git", "-C", str(fallback), "remote", "add", "origin",
                            "https://example.invalid/old-source.git"], check=True)
            state = home / ".home-baseline" / "source-repository.json"
            state.parent.mkdir()
            state.write_text('{"sourcePath":"' + str(source) + '"}\n', encoding="utf-8")
            environment.pop("HOME_BASELINE_SOURCE", None)
            fake = root / "bin"
            fake.mkdir()
            for command_name in ("bash", "python3", "dirname", "basename", "tr", "git", "sed"):
                executable = shutil.which(command_name)
                assert executable is not None
                (fake / command_name).symlink_to(executable)
            environment["PATH"] = str(fake)
            result = subprocess.run(["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                                     "ConfiguredSource", "--force", "--keep-remote", "--yes"],
                                    env=environment, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0, result.stdout)
            self.assertIn("source state unavailable", result.stderr)
            self.assertTrue((source / "scripts" / "sync-home.sh").exists(), result.stdout)

    def test_teardown_rejects_configured_source_with_fallback(self) -> None:
        for shell in ("bash", "pwsh"):
            if not shutil.which(shell):
                continue
            with self.subTest(shell=shell), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                home, _, environment = teardown_fixture(root)
                source = home / "ConfiguredSource"
                subprocess.run(["git", "-C", str(source), "remote", "remove", "origin"], check=True)
                fallback = home / "home-baseline-source"
                fallback.mkdir()
                (fallback / "scripts").mkdir()
                (fallback / "scripts" / "sync-home.sh").write_text("#!/bin/sh\n", encoding="utf-8")
                (fallback / "scripts" / "sync-home.ps1").write_text("#Requires -Version 7\n", encoding="utf-8")
                subprocess.run(["git", "-C", str(fallback), "init", "-q"], check=True)
                subprocess.run(["git", "-C", str(fallback), "remote", "add", "origin",
                                "https://example.invalid/old-source.git"], check=True)
                state = home / ".home-baseline" / "source-repository.json"
                state.parent.mkdir()
                state.write_text('{"sourcePath":"' + str(source) + '"}\n', encoding="utf-8")
                environment.pop("HOME_BASELINE_SOURCE", None)
                command = (["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                            "ConfiguredSource", "--force", "--keep-remote", "--yes"] if shell == "bash" else
                           ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "teardown-workspace.ps1"),
                            "-WorkspaceName", "ConfiguredSource", "-Force", "-KeepRemote", "-Yes"])
                result = subprocess.run(command, env=environment, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertTrue((source / "scripts" / "sync-home.sh").exists(), result.stdout)

    @unittest.skipIf(os.name == "nt", "POSIX find fixture")
    def test_teardown_detects_case_variant_git_marker(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            _, workspace, environment = teardown_fixture(root)
            child = workspace / "child"
            child.mkdir()
            (child / ".GIT").mkdir()
            result = subprocess.run(["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                                     "Demo", "--keep-remote", "--yes", "--dry-run"],
                                    env=environment, capture_output=True, text=True)
            if (child / ".git").exists():
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertIn("Level-2 repositories detected", result.stdout)
            else:
                self.assertEqual(result.returncode, 0, result.stdout)
            self.assertTrue((child / ".GIT").exists(), result.stdout)

    @unittest.skipIf(os.name == "nt", "POSIX Home and Bash fixture")
    def test_teardown_preserves_nonbranch_git_reference(self) -> None:
        for shell in ("bash", "pwsh"):
            if not shutil.which(shell):
                continue
            with self.subTest(shell=shell), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                _, workspace, environment = teardown_fixture(root)
                subprocess.run(["git", "-C", str(workspace), "init", "-q"], check=True)
                subprocess.run(["git", "-C", str(workspace), "config", "user.name", "Test"], check=True)
                subprocess.run(["git", "-C", str(workspace), "config", "user.email", "test@example.invalid"], check=True)
                (workspace / "tracked.txt").write_text("base\n", encoding="utf-8")
                subprocess.run(["git", "-C", str(workspace), "add", "tracked.txt"], check=True)
                subprocess.run(["git", "-C", str(workspace), "commit", "-qm", "initial"], check=True)
                branch = subprocess.run(["git", "-C", str(workspace), "branch", "--show-current"],
                                        capture_output=True, text=True, check=True).stdout.strip()
                subprocess.run(["git", "-C", str(workspace), "remote", "add", "origin",
                                "https://example.invalid/workspace.git"], check=True)
                subprocess.run(["git", "-C", str(workspace), "update-ref",
                                f"refs/remotes/origin/{branch}", "HEAD"], check=True)
                subprocess.run(["git", "-C", str(workspace), "config", f"branch.{branch}.remote", "origin"], check=True)
                subprocess.run(["git", "-C", str(workspace), "config", f"branch.{branch}.merge",
                                f"refs/heads/{branch}"], check=True)
                subprocess.run(["git", "-C", str(workspace), "tag", "local-only"], check=True)
                command = (["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                            "Demo", "--keep-remote", "--yes"] if shell == "bash" else
                           ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "teardown-workspace.ps1"),
                            "-WorkspaceName", "Demo", "-KeepRemote", "-Yes"])
                result = subprocess.run(command, env=environment, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertTrue(workspace.exists(), result.stdout)
                self.assertIn("local-only", subprocess.run(["git", "-C", str(workspace), "tag"],
                                                        capture_output=True, text=True, check=True).stdout)
                backed_up_command = [*command, "--backup" if shell == "bash" else "-Backup"]
                backed_up = subprocess.run(backed_up_command, env=environment, capture_output=True, text=True)
                archives = list((root / "home").glob("Demo-backup-*.tar.gz"))
                self.assertEqual(len(archives), 1, backed_up.stdout + backed_up.stderr)
                with tarfile.open(archives[0], "r:gz") as package:
                    self.assertTrue(any(name.endswith(".git/refs/tags/local-only") for name in package.getnames()))
                self.assertFalse(workspace.exists(), backed_up.stdout + backed_up.stderr)

    @unittest.skipIf(os.name == "nt", "POSIX tar wrapper fixture")
    def test_teardown_rejects_refs_changed_during_backup(self) -> None:
        for shell in ("bash", "pwsh"):
            if not shutil.which(shell):
                continue
            with self.subTest(shell=shell), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                _, workspace, environment = teardown_fixture(root)
                subprocess.run(["git", "-C", str(workspace), "init", "-q"], check=True)
                subprocess.run(["git", "-C", str(workspace), "config", "user.name", "Test"], check=True)
                subprocess.run(["git", "-C", str(workspace), "config", "user.email", "test@example.invalid"], check=True)
                (workspace / "tracked.txt").write_text("base\n", encoding="utf-8")
                subprocess.run(["git", "-C", str(workspace), "add", "tracked.txt"], check=True)
                subprocess.run(["git", "-C", str(workspace), "commit", "-qm", "initial"], check=True)
                branch = subprocess.run(["git", "-C", str(workspace), "branch", "--show-current"],
                                        capture_output=True, text=True, check=True).stdout.strip()
                subprocess.run(["git", "-C", str(workspace), "remote", "add", "origin",
                                "https://example.invalid/workspace.git"], check=True)
                subprocess.run(["git", "-C", str(workspace), "update-ref",
                                f"refs/remotes/origin/{branch}", "HEAD"], check=True)
                subprocess.run(["git", "-C", str(workspace), "config", f"branch.{branch}.remote", "origin"], check=True)
                subprocess.run(["git", "-C", str(workspace), "config", f"branch.{branch}.merge",
                                f"refs/heads/{branch}"], check=True)
                fake = root / "bin"
                fake.mkdir()
                real_tar = shutil.which("tar")
                assert real_tar is not None
                wrapper = fake / "tar"
                wrapper.write_text("#!/bin/sh\n"
                                   f'{shlex.quote(real_tar)} "$@" || exit $?\n'
                                   'git -C "$TEST_REPO" tag late-tag\n', encoding="utf-8")
                wrapper.chmod(0o755)
                environment["PATH"] = f"{fake}{os.pathsep}{os.environ['PATH']}"
                environment["TEST_REPO"] = str(workspace)
                command = (["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                            "Demo", "--backup", "--keep-remote", "--yes"] if shell == "bash" else
                           ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "teardown-workspace.ps1"),
                            "-WorkspaceName", "Demo", "-Backup", "-KeepRemote", "-Yes"])
                result = subprocess.run(command, env=environment, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertTrue(workspace.exists(), result.stdout)
                self.assertIn("late-tag", subprocess.run(["git", "-C", str(workspace), "tag"],
                                                      capture_output=True, text=True, check=True).stdout)

    @unittest.skipIf(os.name == "nt", "POSIX fake command fixture")
    def test_teardown_failed_local_delete_preserves_home_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            home, workspace, environment = teardown_fixture(root)
            readme = home / "README.md"
            readme.write_text("Keep ~/Demo/ entry\n", encoding="utf-8")
            fake = root / "bin"
            fake.mkdir()
            remover = fake / "rm"
            real_rm = shutil.which("rm")
            assert real_rm is not None
            remover.write_text("#!/bin/sh\n"
                               'if [ "${2##*/}" = Demo ]; then exit 2; fi\n'
                               f'exec {shlex.quote(real_rm)} "$@"\n', encoding="utf-8")
            remover.chmod(0o755)
            environment["PATH"] = f"{fake}{os.pathsep}{os.environ['PATH']}"
            result = subprocess.run(["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                                     "Demo", "--keep-remote", "--yes"],
                                    env=environment, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0, result.stdout)
            self.assertTrue(workspace.exists(), result.stdout)
            self.assertEqual(readme.read_text(encoding="utf-8"), "Keep ~/Demo/ entry\n")

    @unittest.skipIf(os.name == "nt", "POSIX fake command fixture")
    def test_teardown_failed_home_read_preserves_original(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            home, _, environment = teardown_fixture(root)
            readme = home / "README.md"
            readme.write_text("Keep ~/Demo/ entry\n", encoding="utf-8")
            fake = root / "bin"
            fake.mkdir()
            reader = fake / "awk"
            real_awk = shutil.which("awk")
            assert real_awk is not None
            reader.write_text("#!/bin/sh\n"
                              'for arg in "$@"; do case "$arg" in */README.md) exit 2;; esac; done\n'
                              f'exec {shlex.quote(real_awk)} "$@"\n', encoding="utf-8")
            reader.chmod(0o755)
            environment["PATH"] = f"{fake}{os.pathsep}{os.environ['PATH']}"
            result = subprocess.run(["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                                     "Demo", "--keep-remote", "--yes"],
                                    env=environment, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0, result.stdout)
            self.assertEqual(readme.read_text(encoding="utf-8"), "Keep ~/Demo/ entry\n")

    @unittest.skipIf(os.name == "nt", "POSIX temporary Home fixture")
    def test_teardown_backup_option_name_archives_selected_workspace(self) -> None:
        for shell in ("bash", "pwsh"):
            if not shutil.which(shell):
                continue
            with self.subTest(shell=shell), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                home, workspace, environment = teardown_fixture(root)
                workspace.rename(home / "-Tlist")
                (home / "-Tlist" / "payload.txt").write_text("backup me\n", encoding="utf-8")
                (root / "list").write_text("other.txt\n", encoding="utf-8")
                (root / "other.txt").write_text("not the target\n", encoding="utf-8")
                command = (["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                            "--backup", "--keep-remote", "--yes", "--", "-Tlist"] if shell == "bash" else
                           ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "teardown-workspace.ps1"),
                            "-WorkspaceName", "-Tlist", "-Backup", "-KeepRemote", "-Yes"])
                result = subprocess.run(command, cwd=root, env=environment, capture_output=True, text=True)
                archives = list(home.glob("-Tlist-backup-*.tar.gz"))
                self.assertEqual(len(archives), 1, result.stdout + result.stderr)
                with tarfile.open(archives[0], "r:gz") as package:
                    members = {name.removeprefix("./") for name in package.getnames()}
                    self.assertIn("-Tlist/payload.txt", members, result.stdout)
                    self.assertNotIn("other.txt", members, result.stdout)
                self.assertFalse((home / "-Tlist").exists(), result.stdout)

    @unittest.skipIf(os.name == "nt", "POSIX Home and Bash fixture")
    def test_teardown_preserves_local_history_without_upstream(self) -> None:
        for shell in ("bash", "pwsh"):
            if not shutil.which(shell):
                continue
            with self.subTest(shell=shell), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                _, workspace, environment = teardown_fixture(root)
                subprocess.run(["git", "-C", str(workspace), "init", "-q"], check=True)
                subprocess.run(["git", "-C", str(workspace), "config", "user.name", "Test"], check=True)
                subprocess.run(["git", "-C", str(workspace), "config", "user.email", "test@example.invalid"],
                               check=True)
                (workspace / "payload.txt").write_text("committed\n", encoding="utf-8")
                subprocess.run(["git", "-C", str(workspace), "add", "payload.txt"], check=True)
                subprocess.run(["git", "-C", str(workspace), "commit", "-qm", "initial"], check=True)
                command = (["bash", str(LIBRARY.parent / "teardown-workspace.sh"), "Demo", "--yes"]
                           if shell == "bash" else
                           ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "teardown-workspace.ps1"),
                            "-WorkspaceName", "Demo", "-Yes"])
                result = subprocess.run(command, env=environment, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertTrue((workspace / "payload.txt").exists(), result.stdout)
                override = [*command, "--force" if shell == "bash" else "-Force"]
                subprocess.run(override, env=environment, capture_output=True, text=True)
                self.assertFalse(workspace.exists(), "explicit Force should allow teardown")

    @unittest.skipIf(os.name == "nt", "POSIX Home and Bash fixture")
    def test_teardown_allows_empty_unborn_git_repository(self) -> None:
        for shell in ("bash", "pwsh"):
            if not shutil.which(shell):
                continue
            with self.subTest(shell=shell), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                _, workspace, environment = teardown_fixture(root)
                subprocess.run(["git", "-C", str(workspace), "init", "-q"], check=True)
                command = (["bash", str(LIBRARY.parent / "teardown-workspace.sh"), "Demo", "--yes"]
                           if shell == "bash" else
                           ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "teardown-workspace.ps1"),
                            "-WorkspaceName", "Demo", "-Yes"])
                result = subprocess.run(command, env=environment, capture_output=True, text=True)
                self.assertIn("Sicherheitsprüfung bestanden", result.stdout)
                self.assertFalse(workspace.exists(), result.stdout)

    @unittest.skipIf(os.name == "nt", "POSIX Home and Bash fixture")
    def test_teardown_checks_every_branch_and_rejects_local_upstream(self) -> None:
        for shell in ("bash", "pwsh"):
            if not shutil.which(shell):
                continue
            for variant in ("extra_branch", "local_upstream", "stash", "tracked_control"):
                with self.subTest(shell=shell, variant=variant), tempfile.TemporaryDirectory() as temporary:
                    root = Path(temporary)
                    _, workspace, environment = teardown_fixture(root)
                    subprocess.run(["git", "-C", str(workspace), "init", "-q"], check=True)
                    subprocess.run(["git", "-C", str(workspace), "config", "user.name", "Test"], check=True)
                    subprocess.run(["git", "-C", str(workspace), "config", "user.email", "test@example.invalid"],
                                   check=True)
                    (workspace / "tracked.txt").write_text("base\n", encoding="utf-8")
                    subprocess.run(["git", "-C", str(workspace), "add", "tracked.txt"], check=True)
                    subprocess.run(["git", "-C", str(workspace), "commit", "-qm", "initial"], check=True)
                    branch = subprocess.run(["git", "-C", str(workspace), "branch", "--show-current"],
                                            capture_output=True, text=True, check=True).stdout.strip()
                    subprocess.run(["git", "-C", str(workspace), "remote", "add", "origin",
                                    "https://example.invalid/workspace.git"], check=True)
                    subprocess.run(["git", "-C", str(workspace), "update-ref",
                                    f"refs/remotes/origin/{branch}", "HEAD"], check=True)
                    subprocess.run(["git", "-C", str(workspace), "config",
                                    f"branch.{branch}.remote", "origin"], check=True)
                    subprocess.run(["git", "-C", str(workspace), "config",
                                    f"branch.{branch}.merge", f"refs/heads/{branch}"], check=True)
                    if variant == "extra_branch":
                        subprocess.run(["git", "-C", str(workspace), "switch", "-qc", "feature"], check=True)
                        (workspace / "feature.txt").write_text("local only\n", encoding="utf-8")
                        subprocess.run(["git", "-C", str(workspace), "add", "feature.txt"], check=True)
                        subprocess.run(["git", "-C", str(workspace), "commit", "-qm", "feature"], check=True)
                        subprocess.run(["git", "-C", str(workspace), "switch", "-q", branch], check=True)
                    elif variant == "local_upstream":
                        subprocess.run(["git", "-C", str(workspace), "branch", "backup"], check=True)
                        subprocess.run(["git", "-C", str(workspace), "config", "branch.backup.remote",
                                        "origin"], check=True)
                        subprocess.run(["git", "-C", str(workspace), "config", "branch.backup.merge",
                                        f"refs/heads/{branch}"], check=True)
                        subprocess.run(["git", "-C", str(workspace), "config",
                                        f"branch.{branch}.remote", "."], check=True)
                        subprocess.run(["git", "-C", str(workspace), "config",
                                        f"branch.{branch}.merge", "refs/heads/backup"], check=True)
                    elif variant == "stash":
                        (workspace / "tracked.txt").write_text("local stash\n", encoding="utf-8")
                        subprocess.run(["git", "-C", str(workspace), "stash", "push", "-q"], check=True)
                    command = (["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                                "Demo", "--keep-remote", "--yes"] if shell == "bash" else
                               ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "teardown-workspace.ps1"),
                                "-WorkspaceName", "Demo", "-KeepRemote", "-Yes"])
                    result = subprocess.run(command, env=environment, capture_output=True, text=True)
                    if variant == "tracked_control":
                        self.assertIn("Sicherheitsprüfung bestanden", result.stdout)
                        self.assertFalse(workspace.exists(), result.stdout)
                    else:
                        self.assertNotEqual(result.returncode, 0, result.stdout)
                        self.assertTrue(workspace.exists(), result.stdout)

    def test_recursive_teardown_preflights_parent_before_child_deletion(self) -> None:
        for shell in ("bash", "pwsh"):
            if not shutil.which(shell):
                continue
            with self.subTest(shell=shell), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                _, workspace, environment = teardown_fixture(root)
                subprocess.run(["git", "-C", str(workspace), "init", "-q"], check=True)
                subprocess.run(["git", "-C", str(workspace), "config", "user.name", "Test"], check=True)
                subprocess.run(["git", "-C", str(workspace), "config", "user.email", "test@example.invalid"],
                               check=True)
                (workspace / ".gitignore").write_text("child/\n", encoding="utf-8")
                subprocess.run(["git", "-C", str(workspace), "add", ".gitignore"], check=True)
                subprocess.run(["git", "-C", str(workspace), "commit", "-qm", "parent"], check=True)
                child = workspace / "child"
                child.mkdir()
                subprocess.run(["git", "-C", str(child), "init", "-q"], check=True)
                subprocess.run(["git", "-C", str(child), "config", "user.name", "Test"], check=True)
                subprocess.run(["git", "-C", str(child), "config", "user.email", "test@example.invalid"],
                               check=True)
                (child / "child.txt").write_text("preserve\n", encoding="utf-8")
                subprocess.run(["git", "-C", str(child), "add", "child.txt"], check=True)
                subprocess.run(["git", "-C", str(child), "commit", "-qm", "child"], check=True)
                branch = subprocess.run(["git", "-C", str(child), "branch", "--show-current"],
                                        capture_output=True, text=True, check=True).stdout.strip()
                subprocess.run(["git", "-C", str(child), "remote", "add", "origin",
                                "https://example.invalid/child.git"], check=True)
                subprocess.run(["git", "-C", str(child), "update-ref",
                                f"refs/remotes/origin/{branch}", "HEAD"], check=True)
                subprocess.run(["git", "-C", str(child), "config", f"branch.{branch}.remote",
                                "origin"], check=True)
                subprocess.run(["git", "-C", str(child), "config", f"branch.{branch}.merge",
                                f"refs/heads/{branch}"], check=True)
                command = (["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                            "Demo", "--recursive", "--keep-remote", "--yes"] if shell == "bash" else
                           ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "teardown-workspace.ps1"),
                            "-WorkspaceName", "Demo", "-Recursive", "-KeepRemote", "-Yes"])
                result = subprocess.run(command, env=environment, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertTrue((child / "child.txt").exists(), result.stdout)

    def test_teardown_rejects_unreadable_git_metadata(self) -> None:
        for shell in ("bash", "pwsh"):
            if not shutil.which(shell):
                continue
            with self.subTest(shell=shell), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                _, workspace, environment = teardown_fixture(root)
                (workspace / ".git").mkdir()
                (workspace / "payload.txt").write_text("keep\n", encoding="utf-8")
                command = (["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                            "Demo", "--keep-remote", "--yes"] if shell == "bash" else
                           ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "teardown-workspace.ps1"),
                            "-WorkspaceName", "Demo", "-KeepRemote", "-Yes"])
                result = subprocess.run(command, env=environment, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertTrue((workspace / "payload.txt").exists(), result.stdout)

    @unittest.skipIf(os.name == "nt" or not shutil.which("pwsh"), "POSIX PowerShell Git shim fixture")
    def test_powershell_teardown_rejects_failed_git_commands(self) -> None:
        real_git = shutil.which("git")
        assert real_git is not None
        for failed_command in ("status", "rev-list", "origin"):
            with self.subTest(command=failed_command), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                _, workspace, environment = teardown_fixture(root)
                subprocess.run(["git", "-C", str(workspace), "init", "-q"], check=True)
                subprocess.run(["git", "-C", str(workspace), "config", "user.name", "Test"], check=True)
                subprocess.run(["git", "-C", str(workspace), "config", "user.email", "test@example.invalid"],
                               check=True)
                (workspace / "payload.txt").write_text("keep\n", encoding="utf-8")
                if failed_command == "rev-list":
                    subprocess.run(["git", "-C", str(workspace), "add", "payload.txt"], check=True)
                    subprocess.run(["git", "-C", str(workspace), "commit", "-qm", "initial"], check=True)
                    branch = subprocess.run(["git", "-C", str(workspace), "branch", "--show-current"],
                                            capture_output=True, text=True, check=True).stdout.strip()
                    subprocess.run(["git", "-C", str(workspace), "update-ref",
                                    f"refs/remotes/origin/{branch}", "HEAD"], check=True)
                    subprocess.run(["git", "-C", str(workspace), "remote", "add", "origin",
                                    "https://example.invalid/workspace.git"], check=True)
                    subprocess.run(["git", "-C", str(workspace), "config",
                                    f"branch.{branch}.remote", "origin"], check=True)
                    subprocess.run(["git", "-C", str(workspace), "config",
                                    f"branch.{branch}.merge", f"refs/heads/{branch}"], check=True)
                if failed_command == "origin":
                    subprocess.run(["git", "-C", str(workspace), "remote", "add", "origin",
                                    "https://github.com/example/workspace.git"], check=True)
                fake = root / "bin"
                fake.mkdir()
                failed_test = ('[ "$3" = remote ] && [ "$4" = get-url ]'
                               if failed_command == "origin" else f'[ "$3" = {failed_command} ]')
                wrapper = fake / "git"
                wrapper.write_text(
                    "#!/bin/sh\n"
                    f'if [ "${{2##*/}}" = Demo ] && {failed_test}; '
                    "then exit 42; fi\n"
                    f'exec {shlex.quote(real_git)} "$@"\n', encoding="utf-8")
                wrapper.chmod(0o755)
                environment["PATH"] = f"{fake}{os.pathsep}{os.environ['PATH']}"
                command = ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "teardown-workspace.ps1"),
                           "-WorkspaceName", "Demo", "-Yes"]
                if failed_command != "origin":
                    command.append("-KeepRemote")
                result = subprocess.run(command, env=environment, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertTrue((workspace / "payload.txt").exists(), result.stdout)

    @unittest.skipUnless(shutil.which("pwsh"), "PowerShell required")
    def test_powershell_teardown_protects_git_file_worktrees(self) -> None:
        for nested, recursive in ((False, False), (True, False), (True, True)):
            with self.subTest(nested=nested, recursive=recursive), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                _, workspace, environment = teardown_fixture(root)
                parent = root / "parent"
                parent.mkdir()
                subprocess.run(["git", "-C", str(parent), "init", "-q"], check=True)
                subprocess.run(["git", "-C", str(parent), "config", "user.name", "Test"], check=True)
                subprocess.run(["git", "-C", str(parent), "config", "user.email", "test@example.invalid"],
                               check=True)
                (parent / "tracked.txt").write_text("source\n", encoding="utf-8")
                subprocess.run(["git", "-C", str(parent), "add", "tracked.txt"], check=True)
                subprocess.run(["git", "-C", str(parent), "commit", "-qm", "initial"], check=True)
                if nested:
                    target = workspace / "child"
                else:
                    workspace.rmdir()
                    target = workspace
                subprocess.run(["git", "-C", str(parent), "worktree", "add", "-q", "-b", "feature",
                                str(target)], check=True)
                self.assertTrue((target / ".git").is_file())
                (target / "payload.txt").write_text("keep\n", encoding="utf-8")
                command = ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "teardown-workspace.ps1"),
                           "-WorkspaceName", "Demo", "-KeepRemote", "-Yes"]
                if recursive:
                    command.append("-Recursive")
                result = subprocess.run(command, env=environment, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertTrue((target / "payload.txt").exists(), result.stdout)

    @unittest.skipIf(os.name == "nt", "POSIX temporary Home fixture")
    def test_teardown_artifact_commit_preserves_unrelated_index(self) -> None:
        for shell in ("bash", "pwsh"):
            if not shutil.which(shell):
                continue
            with self.subTest(shell=shell), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                home, workspace, environment = teardown_fixture(root)
                subprocess.run(["git", "-C", str(home), "init", "-q"], check=True)
                subprocess.run(["git", "-C", str(home), "config", "user.name", "Test"], check=True)
                subprocess.run(["git", "-C", str(home), "config", "user.email", "test@example.invalid"],
                               check=True)
                (home / "README.md").write_text("# Home\n~/Demo/\n", encoding="utf-8")
                (home / ".gitignore").write_text("Demo/\n", encoding="utf-8")
                (home / "private.txt").write_text("old\n", encoding="utf-8")
                subprocess.run(["git", "-C", str(home), "add", "--", "README.md", ".gitignore",
                                "private.txt"], check=True)
                subprocess.run(["git", "-C", str(home), "commit", "-qm", "initial"], check=True)
                (home / "private.txt").write_text("unrelated staged content\n", encoding="utf-8")
                subprocess.run(["git", "-C", str(home), "add", "--", "private.txt"], check=True)
                command = (["bash", str(LIBRARY.parent / "teardown-workspace.sh"),
                            "Demo", "--keep-remote", "--force", "--yes"] if shell == "bash" else
                           ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "teardown-workspace.ps1"),
                            "-WorkspaceName", "Demo", "-KeepRemote", "-Force", "-Yes"])
                subprocess.run(command, env=environment, capture_output=True, text=True)
                committed = subprocess.run(["git", "-C", str(home), "show", "--pretty=format:",
                                            "--name-only", "HEAD"], capture_output=True, text=True,
                                           check=True).stdout.splitlines()
                staged = subprocess.run(["git", "-C", str(home), "diff", "--cached", "--name-only"],
                                        capture_output=True, text=True, check=True).stdout.splitlines()
                self.assertTrue(any(name in {"README.md", ".gitignore"} for name in committed))
                self.assertNotIn("private.txt", committed)
                self.assertEqual(staged, ["private.txt"])
                self.assertFalse(workspace.exists())

    def test_learning_package_rejects_external_link_and_keeps_regular_source(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "lessons"
            source.mkdir()
            guides = source / "docs/learning-units"
            guides.mkdir(parents=True)
            for name in ("START-HERE-FUER-LERNENDE.md", "GIT-START-FUER-LERNENDE.md",
                         "INSTITUTIONELLES-GIT-HOSTING.md"):
                (guides / name).write_text("guide\n", encoding="utf-8")
            (source / "README.md").write_text("public\n", encoding="utf-8")
            package_source.check_tree(source, skip_excluded=True)
            outside = root / "private.txt"
            outside.write_text("sensitive marker\n", encoding="utf-8")
            (source / "innocent.txt").symlink_to(outside)
            with self.assertRaisesRegex(ValueError, "link"):
                package_source.check_tree(source, skip_excluded=True)
            for command in (["bash", str(LIBRARY.parent / "package-learning-series.sh"),
                             "--source-dir", str(source), "--output-dir", str(root / "out")],
                            ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "package-learning-series.ps1"),
                             "-SourceDir", str(source), "-OutputDir", str(root / "out")]):
                if shutil.which(command[0]):
                    result = subprocess.run(command, capture_output=True, text=True, check=False)
                    self.assertNotEqual(result.returncode, 0, result.stdout)
                    self.assertFalse(list((root / "out").glob("*.zip")) if (root / "out").exists() else False)
            (source / "innocent.txt").unlink()
            package_source.check_tree(source, skip_excluded=True)
            (source / "bin").symlink_to(root, target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "link"):
                package_source.check_tree(source, skip_excluded=True)
            if shutil.which("pwsh"):
                result = subprocess.run(
                    ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "package-learning-series.ps1"),
                     "-SourceDir", str(source), "-OutputDir", str(root / "out")],
                    capture_output=True, text=True, check=False,
                )
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertFalse(list((root / "out").glob("*.zip")) if (root / "out").exists() else False)
            (source / "bin").unlink()

    @unittest.skipUnless(shutil.which("bash") and shutil.which("rsync") and shutil.which("gitleaks"),
                         "Bash, rsync and Gitleaks are required")
    def test_bash_package_excludes_git_pointer_files(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "lessons"
            guides = source / "docs/learning-units"
            guides.mkdir(parents=True)
            for name in ("START-HERE-FUER-LERNENDE.md", "GIT-START-FUER-LERNENDE.md",
                         "INSTITUTIONELLES-GIT-HOSTING.md"):
                (guides / name).write_text("# Guide\n", encoding="utf-8")
            (source / "README.md").write_text("# Lesson\n", encoding="utf-8")
            (source / ".git").write_text("gitdir: ../private/root\n", encoding="utf-8")
            nested = source / "lesson"
            nested.mkdir()
            (nested / ".git").write_text("gitdir: ../../private/nested\n", encoding="utf-8")
            mixed_case = source / "other/.GIT"
            mixed_case.mkdir(parents=True)
            (mixed_case / "config").write_text("[remote \"origin\"]\n", encoding="utf-8")
            command = ["bash", str(LIBRARY.parent / "package-learning-series.sh"),
                       "--source-dir", str(source), "--output-dir", str(root / "out")]
            preview = subprocess.run([*command, "--dry-run"], capture_output=True, text=True)
            self.assertEqual(preview.returncode, 0, preview.stderr)
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            with zipfile.ZipFile(next((root / "out").glob("*.zip"))) as package:
                self.assertFalse(any(Path(name).name.casefold() == ".git" for name in package.namelist()))
            with self.assertRaisesRegex(ValueError, "excluded path"):
                package_source.check_tree(source, skip_excluded=False)

    @unittest.skipIf(os.name == "nt", "Restricted POSIX PATH fixture requires Unix tools")
    def test_learning_package_secret_scan_is_required_before_release(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "lessons"
            guides = source / "docs/learning-units"
            guides.mkdir(parents=True)
            for name in ("START-HERE-FUER-LERNENDE.md", "GIT-START-FUER-LERNENDE.md",
                         "INSTITUTIONELLES-GIT-HOSTING.md"):
                (guides / name).write_text("# Guide\n", encoding="utf-8")
            (source / "README.md").write_text("# Lesson\n", encoding="utf-8")
            output = root / "out"
            commands = [
                ["bash", str(LIBRARY.parent / "package-learning-series.sh"),
                 "--source-dir", str(source), "--output-dir", str(output)],
                ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "package-learning-series.ps1"),
                 "-SourceDir", str(source), "-OutputDir", str(output)],
            ]
            restricted_environment = dict(os.environ, PATH=path_without_gitleaks(root))
            for command in commands:
                executable = shutil.which(command[0])
                if not executable:
                    continue
                preview_option = "--dry-run" if command[0] == "bash" else "-WhatIf"
                with self.subTest(platform=command[0], scanner="missing", mode="preview"):
                    preview = subprocess.run([executable, *command[1:], preview_option],
                                             env=restricted_environment, capture_output=True,
                                             text=True, check=False)
                    self.assertEqual(preview.returncode, 0, preview.stderr)
                    self.assertFalse(list(output.glob("*.zip")))
                with self.subTest(platform=command[0], scanner="missing"):
                    result = subprocess.run([executable, *command[1:]], env=restricted_environment,
                                            capture_output=True, text=True, check=False)
                    self.assertNotEqual(result.returncode, 0, result.stdout)
                    self.assertIn("gitleaks", result.stderr)
                    self.assertFalse(list(output.glob("*.zip")))

            fake_bin = root / "fake-bin"
            fake_bin.mkdir()
            fake_scanner = fake_bin / "gitleaks"
            fake_scanner.write_text("#!/bin/sh\nexit 1\n", encoding="utf-8")
            fake_scanner.chmod(0o755)
            failing_environment = dict(os.environ, PATH=f"{fake_bin}{os.pathsep}{os.environ['PATH']}")
            for command in commands:
                executable = shutil.which(command[0])
                if not executable:
                    continue
                with self.subTest(platform=command[0], scanner="failure"):
                    result = subprocess.run([executable, *command[1:]], env=failing_environment,
                                            capture_output=True, text=True, check=False)
                    self.assertNotEqual(result.returncode, 0, result.stdout)
                    self.assertFalse(list(output.glob("*.zip")))

    @unittest.skipIf(os.name == "nt", "Restricted POSIX PATH fixture requires Unix tools")
    def test_learning_package_checker_rejects_missing_secret_scanner(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / "lesson.zip"
            with zipfile.ZipFile(package, "w") as writer:
                for name in ("START-HERE-FUER-LERNENDE.md", "GIT-START-FUER-LERNENDE.md",
                             "INSTITUTIONELLES-GIT-HOSTING.md"):
                    writer.writestr(f"lesson/{name}", "# Guide\n")
                writer.writestr("lesson/PACKAGING-MANIFEST.txt",
                                "Git data included: no (package only)\n"
                                "Original remotes included: no\n"
                                "Start here after extracting: START-HERE-FUER-LERNENDE.md\n"
                                "Institutional hosting guide: INSTITUTIONELLES-GIT-HOSTING.md\n")
            (root / "lesson.zip.sha256").write_text(
                f"{hashlib.sha256(package.read_bytes()).hexdigest()}  lesson.zip\n", encoding="ascii")
            environment = dict(os.environ, PATH=path_without_gitleaks(root))
            commands = [
                ["bash", str(LIBRARY.parent / "check-learning-package.sh"), str(package)],
                ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "check-learning-package.ps1"),
                 "-PackagePath", str(package)],
            ]
            for command in commands:
                executable = shutil.which(command[0])
                if not executable:
                    continue
                with self.subTest(platform=command[0]):
                    result = subprocess.run([executable, *command[1:]], env=environment,
                                            capture_output=True, text=True, check=False)
                    self.assertNotEqual(result.returncode, 0, result.stdout)
                    self.assertIn("gitleaks", result.stderr)
                    self.assertNotIn("PASS:", result.stdout)

    def test_learning_package_checkers_reject_case_variant_git_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / "lesson.zip"
            with zipfile.ZipFile(package, "w") as writer:
                for name in ("START-HERE-FUER-LERNENDE.md", "GIT-START-FUER-LERNENDE.md",
                             "INSTITUTIONELLES-GIT-HOSTING.md"):
                    writer.writestr(f"lesson/{name}", "# Guide\n")
                writer.writestr("lesson/PACKAGING-MANIFEST.txt",
                                "Git data included: no (package only)\n"
                                "Original remotes included: no\n"
                                "Start here after extracting: START-HERE-FUER-LERNENDE.md\n"
                                "Institutional hosting guide: INSTITUTIONELLES-GIT-HOSTING.md\n")
                writer.writestr("lesson/sub/.GIT/config", "[remote \"origin\"]\n")
            (root / "lesson.zip.sha256").write_text(
                f"{hashlib.sha256(package.read_bytes()).hexdigest()}  lesson.zip\n", encoding="ascii")
            commands = (
                ["bash", str(LIBRARY.parent / "check-learning-package.sh"), str(package)],
                ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "check-learning-package.ps1"),
                 "-PackagePath", str(package)],
            )
            for command in commands:
                if not shutil.which(command[0]):
                    continue
                with self.subTest(platform=command[0]):
                    result = subprocess.run(command, capture_output=True, text=True)
                    self.assertNotEqual(result.returncode, 0, result.stdout)
                    self.assertNotIn("PASS:", result.stdout)

    @unittest.skipUnless(shutil.which("gitleaks"), "Gitleaks is required for the real scan fixture")
    def test_learning_package_scan_blocks_secret_in_teaching_path(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "lessons"
            source.mkdir()
            guides = source / "docs/learning-units"
            guides.mkdir(parents=True)
            for name in ("START-HERE-FUER-LERNENDE.md", "GIT-START-FUER-LERNENDE.md",
                         "INSTITUTIONELLES-GIT-HOSTING.md"):
                (guides / name).write_text("# Guide\n", encoding="utf-8")
            (source / "README.md").write_text("# Lesson\n", encoding="utf-8")
            project_root = LIBRARY.parent.parent
            reviewed_example = Path("docs/secure-development/checklisten/CL_09_KI-Codeerzeugung.md")
            (source / reviewed_example).parent.mkdir(parents=True)
            shutil.copy2(project_root / reviewed_example, source / reviewed_example)
            secret_file = source / "docs/secure-development/example.md"
            secret_file.write_text("GITHUB_TOKEN=" + "ghp_" +
                                   "abcdef0123456789abcdef0123456789abcd" +
                                   " # gitleaks:allow\n", encoding="utf-8")
            (source / ".gitleaks.toml").write_text(
                "title = 'untrusted package config'\n[extend]\nuseDefault = true\n"
                "[allowlist]\npaths = ['''docs/secure-development/.*''']\n", encoding="utf-8")

            for executable_name, arguments in (
                ("bash", [str(LIBRARY.parent / "package-learning-series.sh"),
                          "--source-dir", str(source), "--output-dir", str(root / "bash-out")]),
                ("pwsh", ["-NoProfile", "-File", str(LIBRARY.parent / "package-learning-series.ps1"),
                           "-SourceDir", str(source), "-OutputDir", str(root / "pwsh-out")]),
            ):
                executable = shutil.which(executable_name)
                if not executable:
                    continue
                with self.subTest(command=executable_name, mode="produce"):
                    result = subprocess.run([executable, *arguments], capture_output=True, text=True,
                                            check=False)
                    self.assertNotEqual(result.returncode, 0, result.stdout)
                    self.assertFalse(list((root / f"{executable_name}-out").glob("*.zip")))

            (source / "PACKAGING-MANIFEST.txt").write_text(
                "Git data included: no (package only)\nOriginal remotes included: no\n"
                "Start here after extracting: START-HERE-FUER-LERNENDE.md\n"
                "Institutional hosting guide: INSTITUTIONELLES-GIT-HOSTING.md\n", encoding="utf-8")
            package = root / "lesson.zip"
            with zipfile.ZipFile(package, "w") as writer:
                for file_path in source.rglob("*"):
                    if file_path.is_file():
                        writer.write(file_path, f"lesson/{file_path.relative_to(source).as_posix()}")
            (root / "lesson.zip.sha256").write_text(
                f"{hashlib.sha256(package.read_bytes()).hexdigest()}  lesson.zip\n", encoding="ascii")
            for executable_name, arguments in (
                ("bash", [str(LIBRARY.parent / "check-learning-package.sh"), str(package)]),
                ("pwsh", ["-NoProfile", "-File", str(LIBRARY.parent / "check-learning-package.ps1"),
                           "-PackagePath", str(package)]),
            ):
                executable = shutil.which(executable_name)
                if not executable:
                    continue
                with self.subTest(command=executable_name, mode="check"):
                    result = subprocess.run([executable, *arguments], capture_output=True, text=True,
                                            check=False)
                    self.assertNotEqual(result.returncode, 0, result.stdout)
                    self.assertNotIn("PASS:", result.stdout)

            secret_file.unlink()
            for executable_name, arguments in (
                ("bash", [str(LIBRARY.parent / "package-learning-series.sh"),
                          "--source-dir", str(source), "--output-dir", str(root / "bash-out")]),
                ("pwsh", ["-NoProfile", "-File", str(LIBRARY.parent / "package-learning-series.ps1"),
                           "-SourceDir", str(source), "-OutputDir", str(root / "pwsh-out")]),
            ):
                executable = shutil.which(executable_name)
                if not executable:
                    continue
                with self.subTest(command=executable_name, mode="reviewed-example"):
                    result = subprocess.run([executable, *arguments], capture_output=True, text=True,
                                            check=False)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(len(list((root / f"{executable_name}-out").glob("*.zip"))), 1)

    @unittest.skipUnless(shutil.which("gitleaks"), "Gitleaks is required")
    def test_repository_scan_reviews_exact_examples_and_rejects_new_secret(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            project_root = LIBRARY.parent.parent
            examples = (
                "docs/secure-development/mitgeltende-dokumente/Leitlinie_Sichere-Programmierung.md",
                "docs/secure-development/checklisten/CL_09_KI-Codeerzeugung.md",
                "docs/secure-development/Checklistensammelband_Sichere-Entwicklung.md",
                "specs/004-series-eligibility/phase-results/us1-tests.json",
                "specs/004-series-eligibility/phase-results/us2-tests.json",
            )
            for relative in examples:
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(project_root / relative, target)
            scanner = LIBRARY / "check_learning_package_secrets.py"
            command = [sys.executable, str(scanner), str(root)]
            accepted = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(accepted.returncode, 0, accepted.stderr)
            extra = root / "docs/secure-development/example.md"
            extra.write_text("GITHUB_TOKEN=" + "ghp_" +
                             "abcdef0123456789abcdef0123456789abcd\n",
                             encoding="utf-8")
            rejected = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(rejected.returncode, 0, rejected.stdout)
            extra.unlink()
            reviewed = root / examples[0]
            reviewed.write_text(reviewed.read_text(encoding="utf-8") + "\nChanged\n", encoding="utf-8")
            changed = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(changed.returncode, 0, changed.stdout)

    @unittest.skipIf(os.name == "nt", "Bash archive fixture requires POSIX")
    @unittest.skipUnless(shutil.which("bash") and shutil.which("shasum"), "Bash checksum check requires shasum")
    def test_bash_checker_binds_custom_sidecar_to_selected_archive(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first = root / "first.zip"
            second = root / "second.zip"
            with zipfile.ZipFile(first, "w") as writer:
                writer.writestr("lesson/one.txt", "one")
            with zipfile.ZipFile(second, "w") as writer:
                writer.writestr("lesson/two.txt", "two")
            sidecar = root / "first.sha256"
            sidecar.write_text(f"{hashlib.sha256(first.read_bytes()).hexdigest()}  first.zip\n")
            checker = LIBRARY.parent / "check-learning-package.sh"
            result = subprocess.run(
                ["bash", str(checker), "--checksum", str(sidecar), str(second)],
                capture_output=True, text=True, check=False,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("SHA-256 stimmt nicht", result.stderr)

    def test_checksum_sidecar_is_bounded_and_preserves_generated_formats(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            sidecar = root / "package.sha256"
            digest = "a" * 64
            sidecar.write_bytes((digest.upper() + "  ").encode("ascii") + b"name-\xff.zip\r\nignored line\n")
            self.assertEqual(archive.read_checksum_bounded(sidecar), digest)
            for marker, encoding in (
                (codecs.BOM_UTF16_LE, "utf-16-le"),
                (codecs.BOM_UTF16_BE, "utf-16-be"),
                (codecs.BOM_UTF32_LE, "utf-32-le"),
                (codecs.BOM_UTF32_BE, "utf-32-be"),
            ):
                sidecar.write_bytes(marker + (digest.upper() + "  package.zip\r\n").encode(encoding))
                self.assertEqual(archive.read_checksum_bounded(sidecar), digest)
            sidecar.write_bytes((digest + "\n").encode("ascii") + b"x" * (archive.MAX_CHECKSUM_BYTES - 65))
            self.assertEqual(sidecar.stat().st_size, archive.MAX_CHECKSUM_BYTES)
            self.assertEqual(archive.read_checksum_bounded(sidecar), digest)
            with sidecar.open("ab") as output:
                output.write(b"x")
            with self.assertRaisesRegex(archive.UnsafePackage, "sidecar exceeds byte limit"):
                archive.read_checksum_bounded(sidecar)
            sidecar.write_bytes(b"\n" + digest.encode("ascii"))
            with self.assertRaisesRegex(archive.UnsafePackage, "no valid digest"):
                archive.read_checksum_bounded(sidecar)

    @unittest.skipIf(os.name == "nt", "Bash archive fixture requires POSIX")
    def test_oversized_checksum_sidecar_is_rejected_by_both_checkers(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / "small.zip"
            with zipfile.ZipFile(package, "w") as writer:
                writer.writestr("lesson/one.txt", "one")
            sidecar = root / "other.sha256"
            digest = hashlib.sha256(package.read_bytes()).hexdigest()
            sidecar.write_bytes((digest + "  small.zip\n").encode("ascii") + b"x" * 4096)
            for command in (
                ["bash", str(LIBRARY.parent / "check-learning-package.sh"), "--checksum", str(sidecar), str(package)],
                ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "check-learning-package.ps1"),
                 "-ChecksumPath", str(sidecar), "-PackagePath", str(package)],
            ):
                if not shutil.which(command[0]):
                    continue
                result = subprocess.run(command, capture_output=True, text=True, check=False)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("sidecar exceeds byte limit", result.stderr)

    def test_utf16_checksum_sidecar_remains_usable_by_powershell(self) -> None:
        if not shutil.which("pwsh") or not shutil.which("gitleaks"):
            self.skipTest("PowerShell 7 and gitleaks are required")
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / "package.zip"
            with zipfile.ZipFile(package, "w") as writer:
                for required in ("START-HERE-FUER-LERNENDE.md", "GIT-START-FUER-LERNENDE.md",
                                 "INSTITUTIONELLES-GIT-HOSTING.md"):
                    writer.writestr(f"lesson/{required}", "# Guide\n")
                writer.writestr("lesson/PACKAGING-MANIFEST.txt",
                                "Git data included: no (package only)\n"
                                "Original remotes included: no\n"
                                "Start here after extracting: START-HERE-FUER-LERNENDE.md\n"
                                "Institutional hosting guide: INSTITUTIONELLES-GIT-HOSTING.md\n")
            sidecar = root / "other.sha256"
            digest = hashlib.sha256(package.read_bytes()).hexdigest()
            sidecar.write_bytes(codecs.BOM_UTF16_LE + (digest + "  package.zip\r\n").encode("utf-16-le"))
            result = subprocess.run(
                ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "check-learning-package.ps1"),
                 "-ChecksumPath", str(sidecar), "-PackagePath", str(package)],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)

    @unittest.skipIf(os.name == "nt", "WSL fixture requires a configured distribution")
    @unittest.skipUnless(shutil.which("pwsh"), "PowerShell 7 is required")
    def test_wsl_wrapper_passes_metacharacters_as_one_argument(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fake_wsl = root / "wsl"
            capture = root / "arguments.txt"
            fake_wsl.write_text('#!/bin/sh\nprintf "%s\\n" "$@" > "$WSL_CAPTURE"\n')
            fake_wsl.chmod(0o755)
            value = "series; touch /tmp/should-not-run"
            result = subprocess.run(
                ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "propagate-learning-series.ps1"),
                 "-Series", value],
                env={**os.environ, "PATH": f"{root}{os.pathsep}{os.environ.get('PATH', '')}", "WSL_CAPTURE": str(capture)},
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(capture.read_text().splitlines()[-1], value)

    def test_archive_accepts_normal_package_and_rejects_entry_budget(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / "package.zip"
            destination = root / "out"
            destination.mkdir()
            with zipfile.ZipFile(package, "w") as writer:
                writer.writestr("lesson/README.md", "valid")
                writer.writestr("lesson/start.md", "start")
            archive.extract_bounded(package, destination)
            self.assertEqual((destination / "lesson/README.md").read_text(), "valid")
            other = root / "other"
            other.mkdir()
            with mock.patch.object(archive, "MAX_ENTRIES", 1):
                with mock.patch.object(archive.zipfile, "ZipFile", side_effect=AssertionError("parsed")):
                    with self.assertRaisesRegex(archive.UnsafePackage, "too many entries"):
                        archive.extract_bounded(package, other)

    def test_archive_rejects_metadata_before_zipfile_parse(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / "package.zip"
            destination = root / "out"
            destination.mkdir()
            with zipfile.ZipFile(package, "w") as writer:
                writer.writestr("lesson/one.txt", "one")
                writer.writestr("lesson/two.txt", "two")
            with mock.patch.object(archive, "MAX_CENTRAL_DIRECTORY_BYTES", 60):
                with mock.patch.object(archive.zipfile, "ZipFile", side_effect=AssertionError("parsed")):
                    with self.assertRaisesRegex(archive.UnsafePackage, "central directory exceeds byte limit"):
                        archive.extract_bounded(package, destination)
            with mock.patch.object(archive, "MAX_ARCHIVE_BYTES", 100):
                with package.open("rb") as source:
                    with self.assertRaisesRegex(archive.UnsafePackage, "archive exceeds byte limit"):
                        archive.check_archive_size(source)

            forged = bytearray(package.read_bytes())
            end_record = forged.rfind(b"PK\x05\x06")
            struct.pack_into("<HH", forged, end_record + 8, 1, 1)
            package.write_bytes(forged)
            with mock.patch.object(archive.zipfile, "ZipFile", side_effect=AssertionError("parsed")):
                with self.assertRaisesRegex(archive.UnsafePackage, "entry count is inconsistent"):
                    archive.extract_bounded(package, destination)

            regular = bytearray(forged)
            struct.pack_into("<HH", regular, end_record + 8, 2, 2)
            regular[end_record:end_record] = b"PK\x06\x07" + bytes(16)
            package.write_bytes(regular)
            with mock.patch.object(archive.zipfile, "ZipFile", side_effect=AssertionError("parsed")):
                with self.assertRaisesRegex(archive.UnsafePackage, "ZIP64 metadata"):
                    archive.extract_bounded(package, destination)

    def test_archive_accepts_comment_and_prepended_data(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / "package.zip"
            destination = root / "out"
            destination.mkdir()
            with zipfile.ZipFile(package, "w") as writer:
                writer.writestr("lesson/one.txt", "one")
                writer.comment = b"learning package"
            package.write_bytes(b"launcher-prefix" + package.read_bytes())
            listed = subprocess.run(
                [sys.executable, str(LIBRARY / "check_learning_package_archive.py"), "--list", str(package)],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(listed.returncode, 0, listed.stderr)
            self.assertEqual(listed.stdout.splitlines(), ["lesson/one.txt"])
            archive.extract_bounded(package, destination)
            self.assertEqual((destination / "lesson/one.txt").read_text(), "one")

    @unittest.skipIf(os.name == "nt", "Bash archive fixture requires POSIX")
    def test_archive_over_entry_budget_never_reaches_listing_or_extraction(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / "too-many.zip"
            with zipfile.ZipFile(package, "w", allowZip64=False) as writer:
                for index in range(archive.MAX_ENTRIES + 1):
                    writer.writestr(f"lesson/item-{index:05d}.txt", "")
            listed = subprocess.run(
                [sys.executable, str(LIBRARY / "check_learning_package_archive.py"), "--list", str(package)],
                capture_output=True, text=True, check=False,
            )
            self.assertNotEqual(listed.returncode, 0)
            self.assertEqual(listed.stdout, "")
            self.assertIn("too many entries", listed.stderr)
            with mock.patch.object(archive.zipfile, "ZipFile", side_effect=AssertionError("parsed")):
                with self.assertRaisesRegex(archive.UnsafePackage, "too many entries"):
                    archive.extract_bounded(package, root)
            sidecar = root / "too-many.zip.sha256"
            sidecar.write_text(f"{hashlib.sha256(package.read_bytes()).hexdigest()}  too-many.zip\n")
            if shutil.which("bash") and shutil.which("shasum"):
                result = subprocess.run(
                    ["bash", str(LIBRARY.parent / "check-learning-package.sh"), str(package)],
                    capture_output=True, text=True, check=False,
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("too many entries", result.stderr)
            if shutil.which("pwsh"):
                result = subprocess.run(
                    ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "check-learning-package.ps1"),
                     "-PackagePath", str(package)],
                    capture_output=True, text=True, check=False,
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("too many entries", result.stderr)

    @unittest.skipIf(os.name == "nt", "Bash archive fixture requires POSIX")
    def test_archive_control_character_cannot_spoof_required_bash_entries(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / "spoof.zip"
            with zipfile.ZipFile(package, "w") as writer:
                writer.writestr(
                    "lesson/START-HERE-FUER-LERNENDE.md\n"
                    "lesson/GIT-START-FUER-LERNENDE.md\n"
                    "lesson/INSTITUTIONELLES-GIT-HOSTING.md", "fake guides"
                )
                writer.writestr("lesson/PACKAGING-MANIFEST.txt", "Git data included: no \n")
            listed = subprocess.run(
                [sys.executable, str(LIBRARY / "check_learning_package_archive.py"), "--list", str(package)],
                capture_output=True, text=True, check=False,
            )
            self.assertNotEqual(listed.returncode, 0)
            self.assertIn("control character", listed.stderr)
            if shutil.which("bash") and shutil.which("shasum"):
                sidecar = root / "spoof.zip.sha256"
                sidecar.write_text(f"{hashlib.sha256(package.read_bytes()).hexdigest()}  spoof.zip\n")
                result = subprocess.run(
                    ["bash", str(LIBRARY.parent / "check-learning-package.sh"), str(package)],
                    capture_output=True, text=True, check=False,
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("control character", result.stderr)

    def test_archive_rejects_byte_budget_parent_path_and_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            destination = root / "out"
            destination.mkdir()
            package = root / "package.zip"
            with zipfile.ZipFile(package, "w") as writer:
                writer.writestr("lesson/large.txt", "12345")
            with mock.patch.object(archive, "MAX_UNCOMPRESSED_BYTES", 4):
                with self.assertRaisesRegex(archive.UnsafePackage, "byte limit"):
                    archive.extract_bounded(package, destination)
            with zipfile.ZipFile(package, "w") as writer:
                writer.writestr("lesson/../../outside", "bad")
            with self.assertRaisesRegex(archive.UnsafePackage, "unsafe ZIP entry"):
                archive.extract_bounded(package, destination)
            for name in ("lesson/D:escape.txt", "lesson/file.txt:stream", "lesson/CON",
                         "lesson/.GIT/config", "lesson\\sub\\.GIT\\config",
                         "lesson/COM¹", "lesson/COM².txt", "lesson/COM³",
                         "lesson/LPT¹", "lesson/LPT².txt", "lesson/LPT³"):
                with self.subTest(name=name):
                    with zipfile.ZipFile(package, "w") as writer:
                        writer.writestr(name, "bad")
                    with self.assertRaisesRegex(archive.UnsafePackage, "unsafe ZIP entry"):
                        archive.extract_bounded(package, destination)
            link = zipfile.ZipInfo("lesson/link")
            link.create_system = 3
            link.external_attr = (stat.S_IFLNK | 0o777) << 16
            with zipfile.ZipFile(package, "w") as writer:
                writer.writestr(link, "../outside")
            with self.assertRaisesRegex(archive.UnsafePackage, "unsafe ZIP entry"):
                archive.extract_bounded(package, destination)
            self.assertFalse((root / "outside").exists())

    def test_origin_binds_host_owner_and_repository(self) -> None:
        self.assertTrue(origin.matches_origin(
            "git@github.com:Thorsten/Example.git", "https://github.com", "Thorsten", "Example"
        ))
        self.assertTrue(origin.matches_origin(
            "https://github.com/Thorsten/Example.git", "https://github.com", "Thorsten", "Example"
        ))
        self.assertTrue(origin.matches_origin(
            "ssh://git@forge.example.edu/git/Thorsten/Example.git",
            "https://forge.example.edu/git", "Thorsten", "Example",
        ))
        for remote in (
            "https://github.com/other/Example.git",
            "https://github.com/Thorsten/Other.git",
            "https://evil.invalid/Thorsten/Example.git",
            "file:///tmp/Example.git",
            "https://github.com/Thorsten/../Example.git",
        ):
            with self.subTest(remote=remote):
                self.assertFalse(origin.matches_origin(remote, "https://github.com", "Thorsten", "Example"))

    def test_origin_binds_effective_git_push_destinations(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            repository = Path(temporary)
            subprocess.run(["git", "init", "-q", str(repository)], check=True)
            trusted = "https://github.com/Thorsten/Example.git"
            foreign = "https://example.invalid/Thorsten/Example.git"
            subprocess.run(["git", "-C", str(repository), "remote", "add", "origin", trusted], check=True)
            self.assertTrue(origin.matches_effective_push_urls(repository, "https://github.com", "Thorsten", "Example"))
            subprocess.run(["git", "-C", str(repository), "config", "remote.origin.pushurl", foreign], check=True)
            self.assertFalse(origin.matches_effective_push_urls(repository, "https://github.com", "Thorsten", "Example"))
            subprocess.run(["git", "-C", str(repository), "config", "--unset", "remote.origin.pushurl"], check=True)
            subprocess.run(["git", "-C", str(repository), "config", f"url.{foreign}.pushInsteadOf", trusted], check=True)
            self.assertFalse(origin.matches_effective_push_urls(repository, "https://github.com", "Thorsten", "Example"))

    def test_baseline_rejects_linked_parent_and_linked_leaf(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            repository = root / "repository"
            repository.mkdir()
            outside = root / "outside"
            outside.mkdir()
            (repository / "docs").symlink_to(outside, target_is_directory=True)
            self.assertFalse(baseline.is_safe(repository, repository / "docs/secure-development/managed.md"))
            (repository / "docs").unlink()
            (repository / "docs").mkdir()
            (repository / "docs/secure-development").symlink_to(repository, target_is_directory=True)
            self.assertFalse(baseline.is_safe(repository, repository / "docs/secure-development/README.md"))
            (repository / "docs/secure-development").unlink()
            (repository / "docs/secure-development").mkdir()
            (repository / "docs/secure-development/managed.md").symlink_to(outside / "data.md")
            self.assertFalse(baseline.is_safe(repository, repository / "docs/secure-development/managed.md"))
            (repository / "docs/secure-development/managed.md").unlink()
            self.assertTrue(baseline.is_safe(repository, repository / "docs/secure-development/managed.md"))
            root_readme = repository / "README.md"
            root_readme.write_text("keep\n", encoding="utf-8")
            os.link(root_readme, repository / "docs/secure-development/README.md")
            self.assertFalse(baseline.is_safe(repository, repository / "docs/secure-development/README.md"))

    def test_bootstrap_rejects_existing_child_symlink_before_force(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            project = root / "Project"
            project.mkdir()
            outside = root / "outside.md"
            outside.write_text("keep\n", encoding="utf-8")
            (project / "AGENTS.md").symlink_to(outside)
            self.assertFalse(bootstrap_target.is_safe_target(project))
            shell = subprocess.run(
                ["bash", str(LIBRARY.parent / "bootstrap-project.sh"), "Project", str(root), "--force", "--preview"],
                capture_output=True, text=True, check=False,
            )
            self.assertNotEqual(shell.returncode, 0)
            self.assertEqual(outside.read_text(encoding="utf-8"), "keep\n")
            if shutil.which("pwsh"):
                powershell = subprocess.run(
                    ["pwsh", "-NoProfile", "-File", str(LIBRARY.parent / "bootstrap-project.ps1"),
                     "-ProjectName", "Project", "-TargetWorkspace", str(root), "-Force", "-Preview"],
                    capture_output=True, text=True, check=False,
                )
                self.assertNotEqual(powershell.returncode, 0)
                self.assertEqual(outside.read_text(encoding="utf-8"), "keep\n")
            (project / "AGENTS.md").unlink()
            os.link(outside, project / "AGENTS.md")
            self.assertFalse(bootstrap_target.is_safe_target(project))

    def test_reparse_point_attribute_is_rejected(self) -> None:
        metadata = SimpleNamespace(st_mode=stat.S_IFDIR, st_file_attributes=0x400, st_nlink=1)
        with mock.patch.object(Path, "lstat", return_value=metadata):
            self.assertTrue(baseline.is_indirect_path(Path("junction")))
            self.assertTrue(bootstrap_target.is_indirect_path(Path("junction")))


if __name__ == "__main__":
    unittest.main()
