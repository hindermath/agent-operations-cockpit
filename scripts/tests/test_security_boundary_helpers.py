#!/usr/bin/env python3
"""Focused regression tests for cross-shell security boundaries."""

from __future__ import annotations

import importlib.util
import hashlib
import os
from pathlib import Path
import shutil
import stat
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest import mock
import zipfile


LIBRARY = Path(__file__).resolve().parents[1] / "lib"


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


class SecurityBoundaryHelpersTests(unittest.TestCase):
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
                with self.assertRaisesRegex(archive.UnsafePackage, "too many entries"):
                    archive.extract_bounded(package, other)

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
