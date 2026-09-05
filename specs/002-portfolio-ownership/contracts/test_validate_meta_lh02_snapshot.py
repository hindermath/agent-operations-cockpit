#!/usr/bin/env python3
"""Isolated standard-library tests for the META-LH-02 snapshot contract."""

from __future__ import annotations

import ast
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Callable

import validate_meta_lh02_snapshot as contract


REPO = Path(__file__).resolve().parents[3]
CONTRACTS = REPO / contract.FEATURE / "contracts"
FIXTURES = CONTRACTS / "fixtures"
BASH_SURFACE = CONTRACTS / "validate-meta-lh02-snapshot.sh"
POWERSHELL_SURFACE = CONTRACTS / "validate-meta-lh02-snapshot.ps1"
MANUAL = REPO / "docs/man/validate-meta-lh02-snapshot.1"
ZERO_SHA = "0" * 64


def repository_status() -> str:
    result = subprocess.run(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"],
        cwd=REPO, text=True, capture_output=True, check=True,
    )
    return "\n".join(sorted(result.stdout.splitlines()))


def copy_path(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        shutil.copytree(source, destination)
    else:
        shutil.copy2(source, destination)

    relative = source.relative_to(REPO).as_posix()
    tracked = subprocess.run(
        ["git", "ls-files", "-z", "--", relative],
        cwd=REPO, capture_output=True, check=True,
    ).stdout.split(b"\0")
    for raw_path in tracked:
        if not raw_path:
            continue
        tracked_path = raw_path.decode("utf-8")
        blob = subprocess.run(
            ["git", "cat-file", "blob", f"HEAD:{tracked_path}"],
            cwd=REPO, capture_output=True, check=True,
        ).stdout
        target = destination if source.is_file() else destination / Path(tracked_path).relative_to(relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(blob)


def projection() -> tempfile.TemporaryDirectory[str]:
    temporary = tempfile.TemporaryDirectory(prefix="meta-lh02-contract-test-")
    root = Path(temporary.name)
    for relative in (
        "requirements/intakes/active",
        "specs/intake-authoring-receipts",
        "specs/intake-review-results",
        "specs/intake-review-requests",
        "specs/001-programmquellen-baseline/intake-lifecycle.json",
        f"{contract.FEATURE}/autonomous-run-state.json",
        f"{contract.FEATURE}/intake-lifecycle.json",
        contract.REVIEW_BASH,
        contract.REVIEW_POWERSHELL,
    ):
        copy_path(REPO / relative, root / relative)
    return temporary


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def store(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def set_target(root: Path, target: str, value: str) -> None:
    document_name, expression = target.split(".", 1)
    path = root / (contract.LIFECYCLE if document_name == "lifecycle" else contract.STATE)
    document = load(path)
    current: Any = document
    tokens = expression.replace("]", "").replace("[", ".").split(".")
    for token in tokens[:-1]:
        current = current[int(token)] if token.isdigit() else current[token]
    final = tokens[-1]
    if final.isdigit():
        current[int(final)] = value
    else:
        current[final] = value
    store(path, document)


def no_review_process(command: list[str], root: Path, label: str) -> None:
    del command, root, label


def git(root: Path, *arguments: str) -> str:
    result = subprocess.run(
        ["git", *arguments], cwd=root, text=True, capture_output=True, check=True,
    )
    return result.stdout.strip()


def identity_repository() -> tuple[tempfile.TemporaryDirectory[str], Path, str]:
    temporary = tempfile.TemporaryDirectory(prefix="meta-lh02-git-identity-")
    root = Path(temporary.name)
    git(root, "init", "-b", "main")
    git(root, "config", "user.name", "Contract Test")
    git(root, "config", "user.email", "contract-test@example.invalid")
    git(root, "remote", "add", "origin",
        "https://github.com/hindermath/agent-operations-cockpit.git")
    for relative, value in (
        (contract.STATE, {"status": "Completed"}),
        (contract.LIFECYCLE, {"schemaVersion": "1.1"}),
    ):
        (root / relative).parent.mkdir(parents=True, exist_ok=True)
        store(root / relative, value)
    git(root, "add", "--", contract.STATE, contract.LIFECYCLE)
    git(root, "commit", "-m", "fixture: completion merge")
    return temporary, root, git(root, "rev-parse", "HEAD")


class SnapshotContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.status_before = repository_status()

    @classmethod
    def tearDownClass(cls) -> None:
        if repository_status() != cls.status_before:
            raise AssertionError("snapshot tests changed repository state")

    def assert_contract_error(self, root: Path, expected: str,
                              runner: Callable[[list[str], Path, str], None] = no_review_process) -> None:
        with self.assertRaisesRegex(contract.ContractError, expected.replace("[", r"\[").replace("]", r"\]")):
            contract.validate_post_global_ready(root, runner=runner)

    def test_01_real_repository_positive_and_peer_parity(self) -> None:
        environment = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
        bash = contract.bash_executable(environment)
        commands = (
            [bash, str(BASH_SURFACE), "--repo", ".", "--", "post-global-ready"],
            ["pwsh", "-NoProfile", "-File", str(POWERSHELL_SURFACE),
             "-Repo", ".", "-Mode", "post-global-ready"],
        )
        results = [
            subprocess.run(command, cwd=REPO, env=environment, text=True,
                           capture_output=True, check=False)
            for command in commands
        ]
        self.assertEqual([item.returncode for item in results], [0, 0])
        self.assertEqual(results[0].stdout, results[1].stdout)
        self.assertEqual(results[0].stderr, results[1].stderr)
        self.assertEqual(results[0].stdout.strip(), contract.PASS_MESSAGE)

    def test_02_tracked_fixtures_fail_closed_with_peer_parity(self) -> None:
        environment = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
        bash = contract.bash_executable(environment)
        for fixture_path in sorted(FIXTURES.glob("programme-snapshot-*.json")):
            fixture = load(fixture_path)
            with self.subTest(scenario=fixture["scenario"]), projection() as temporary:
                root = Path(temporary)
                if fixture["scenario"] == "duplicate-review-leaf":
                    duplicate = load(root / fixture["source"])
                    duplicate["reviewId"] = "00000000-0000-0000-0000-000000000002"
                    duplicate["supersedes"] = "N/A"
                    store(root / fixture["destination"], duplicate)
                else:
                    set_target(root, fixture["target"], fixture["value"])
                commands = (
                    [bash, str(BASH_SURFACE), "--repo", str(root), "--", "post-global-ready"],
                    ["pwsh", "-NoProfile", "-File", str(POWERSHELL_SURFACE),
                     "-Repo", str(root), "-Mode", "post-global-ready"],
                )
                results = [
                    subprocess.run(command, cwd=REPO, env=environment, text=True,
                                   capture_output=True, check=False)
                    for command in commands
                ]
                self.assertEqual([item.returncode for item in results], [1, 1])
                self.assertEqual(results[0].stdout, results[1].stdout)
                self.assertEqual(results[0].stderr, results[1].stderr)
                self.assertIn(fixture["expectedError"], results[0].stderr)

    def test_03_temporary_lifecycle_shape_projection(self) -> None:
        with projection() as temporary:
            root = Path(temporary)
            lifecycle = load(root / contract.LIFECYCLE)
            lifecycle["unexpected"] = True
            store(root / contract.LIFECYCLE, lifecycle)
            self.assert_contract_error(root, "lifecycle fields are incomplete or ambiguous")

    def test_04_temporary_original_archive_exclusivity_projections(self) -> None:
        with projection() as temporary:
            root = Path(temporary)
            original = root / contract.ORIGINAL_TARGET
            archive = root / contract.ARCHIVED_TARGET
            physical = original if original.is_file() else archive
            counterpart = archive if physical == original else original
            counterpart.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(physical, counterpart)
            self.assert_contract_error(root, "mutually exclusive; found both")
        with projection() as temporary:
            root = Path(temporary)
            original = root / contract.ORIGINAL_TARGET
            archive = root / contract.ARCHIVED_TARGET
            physical = original if original.is_file() else archive
            physical.unlink()
            self.assert_contract_error(root, "mutually exclusive; found neither")
        with projection() as temporary:
            root = Path(temporary)
            original = root / contract.ORIGINAL_TARGET
            archive = root / contract.ARCHIVED_TARGET
            archive.rename(original)
            self.assert_contract_error(root, "must resolve exactly the archived target")

    def test_05_temporary_target_hash_drift_projection(self) -> None:
        with projection() as temporary:
            root = Path(temporary)
            set_target(
                root,
                "lifecycle.programmeEvidenceSnapshot.orderedLogicalTargets[0].target.normalizedSha256",
                ZERO_SHA,
            )
            self.assert_contract_error(root, "target normalized SHA-256 drift")

    def test_06_plan_stage_is_exactly_qualified_for_the_bound_run(self) -> None:
        expected_stages = {
            "Plan", "Implement", "Validate", "Publish", "Review",
            "MergeAndSync", "Retrospective",
        }
        self.assertEqual(contract.ALLOWED_STAGES, expected_stages)
        with projection() as temporary:
            root = Path(temporary)
            set_target(root, "state.status", "Active")
            set_target(root, "state.stage", "Plan")
            self.assertEqual(
                contract.validate_post_global_ready(
                    root, runner=no_review_process
                ),
                contract.PASS_MESSAGE,
            )

    def test_07_temporary_inactive_state_projection(self) -> None:
        with projection() as temporary:
            root = Path(temporary)
            set_target(root, "state.status", "PausedByUser")
            self.assert_contract_error(root, "autonomous run state must be Active or terminal Completed")

    def test_07b_terminal_state_requires_complete_closeout(self) -> None:
        with projection() as temporary:
            root = Path(temporary)
            set_target(root, "state.status", "Completed")
            set_target(root, "state.stage", "MergeAndSync")
            set_target(root, "state.nextExactAction", "N/A")
            set_target(root, "state.tasks.completed", 93)
            set_target(root, "state.tasks.total", 93)
            for field in (
                "mergeOrPublication", "defaultBranchSync",
                "postMergeActions", "finalValidation",
            ):
                set_target(root, f"state.closeout.{field}", "Completed")
            set_target(root, "state.closeout.finalValidation", "Pending")
            self.assert_contract_error(root, "must bind the fully completed MergeAndSync closeout")

    def test_08_each_installed_review_surface_fails_independently(self) -> None:
        for surface, relative in (("Bash", contract.REVIEW_BASH),
                                  ("PowerShell", contract.REVIEW_POWERSHELL)):
            with self.subTest(surface=surface), projection() as temporary:
                root = Path(temporary)
                script = root / relative
                if surface == "Bash":
                    script.write_text("#!/usr/bin/env bash\nexit 41\n", encoding="utf-8")
                else:
                    script.write_text("#Requires -Version 7\nexit 42\n", encoding="utf-8")
                self.assert_contract_error(
                    root,
                    f"{surface} review validator .* failed with exit",
                    runner=contract.run_checked,
                )

    def test_09_help_manual_and_cmdlet(self) -> None:
        bash = contract.bash_executable()
        commands = (
            [bash, str(BASH_SURFACE), "-h"],
            [bash, str(BASH_SURFACE), "--help"],
            ["pwsh", "-NoProfile", "-File", str(POWERSHELL_SURFACE), "-Help"],
            ["pwsh", "-NoProfile", "-Command",
             f". '{POWERSHELL_SURFACE}'; Get-Help Test-AocMetaLh02Snapshot -Full; "
             "if (-not (Get-Command Test-AocMetaLh02Snapshot -CommandType Function)) { exit 1 }"],
        )
        results = [subprocess.run(command, cwd=REPO, text=True, capture_output=True, check=False)
                   for command in commands]
        self.assertEqual([result.returncode for result in results], [0, 0, 0, 0])
        self.assertIn("docs/man/validate-meta-lh02-snapshot.1", results[0].stdout)
        self.assertIn("Test-AocMetaLh02Snapshot", results[2].stdout)
        manual = MANUAL.read_text(encoding="utf-8")
        for token in (".TH VALIDATE-META-LH02-SNAPSHOT 1", "read-only", "EXIT STATUS", "--help"):
            self.assertIn(token, manual)

    def test_10_dependency_free_and_secure_code_posture(self) -> None:
        source = (CONTRACTS / "validate_meta_lh02_snapshot.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        imports = {
            alias.name.split(".")[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.Import)
            for alias in node.names
        } | {
            (node.module or "").split(".")[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom)
        }
        allowed = {
            "__future__", "argparse", "hashlib", "json", "os", "re", "shutil",
            "subprocess", "sys", "tempfile", "pathlib", "typing",
        }
        self.assertEqual(imports - allowed, set())
        for forbidden in ("shell=True", "eval(", "exec(", "pickle", "yaml", "Invoke-Expression"):
            self.assertNotIn(forbidden, source)
        bash = BASH_SURFACE.read_text(encoding="utf-8")
        self.assertIn("set -euo pipefail", bash)
        self.assertIn("\"$repo\"", bash)
        self.assertIn(" -- ", bash)
        powershell = POWERSHELL_SURFACE.read_text(encoding="utf-8")
        for token in ("#Requires -Version 7", "Set-StrictMode -Version Latest",
                      "$ErrorActionPreference = 'Stop'", "[ValidateSet('post-global-ready')]",
                      "function Test-AocMetaLh02Snapshot"):
            self.assertIn(token, powershell)

    def test_11_exact_pull_request_head_identity(self) -> None:
        head = "1" * 40
        environment = {
            "GITHUB_ACTIONS": "true",
            "GITHUB_EVENT_NAME": "pull_request",
            "GITHUB_REPOSITORY": contract.EXPECTED_REPOSITORY,
            "GITHUB_HEAD_REF": contract.EXPECTED_BRANCH,
        }
        event = {
            "repository": {"full_name": contract.EXPECTED_REPOSITORY},
            "pull_request": {"head": {
                "ref": contract.EXPECTED_BRANCH,
                "sha": head,
                "repo": {"full_name": contract.EXPECTED_REPOSITORY},
            }},
        }
        self.assertEqual(
            contract.resolve_logical_branch(environment, event, head, ""),
            contract.EXPECTED_BRANCH,
        )

    def test_12_synthetic_or_ambiguous_identity_fails_closed(self) -> None:
        event_head = "1" * 40
        synthetic_head = "2" * 40
        environment = {
            "GITHUB_ACTIONS": "true",
            "GITHUB_EVENT_NAME": "pull_request",
            "GITHUB_REPOSITORY": contract.EXPECTED_REPOSITORY,
            "GITHUB_HEAD_REF": contract.EXPECTED_BRANCH,
        }
        event = {
            "repository": {"full_name": contract.EXPECTED_REPOSITORY},
            "pull_request": {
                "head": {
                    "ref": contract.EXPECTED_BRANCH,
                    "sha": event_head,
                    "repo": {"full_name": contract.EXPECTED_REPOSITORY},
                }
            },
        }
        with self.assertRaisesRegex(contract.ContractError, "event head SHA"):
            contract.resolve_logical_branch(environment, event, synthetic_head, "")
        with self.assertRaisesRegex(contract.ContractError, "detached local HEAD"):
            contract.resolve_logical_branch({}, {}, event_head, "")

    def test_13_lf_crlf_equivalence_and_substantive_drift(self) -> None:
        with tempfile.TemporaryDirectory(prefix="meta-lh02-line-endings-") as temporary:
            root = Path(temporary)
            lf = root / "lf.md"
            crlf = root / "crlf.md"
            changed = root / "changed.md"
            lf.write_bytes(b"alpha\nbeta\n")
            crlf.write_bytes(b"alpha\r\nbeta\r\n")
            changed.write_bytes(b"alpha\ngamma\n")
            self.assertNotEqual(contract.raw_sha256(lf), contract.raw_sha256(crlf))
            self.assertEqual(contract.normalized_sha256(lf), contract.normalized_sha256(crlf))
            self.assertNotEqual(contract.normalized_sha256(lf), contract.normalized_sha256(changed))

    def test_14_git_bash_selected_and_wsl_launcher_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="meta-lh02-bash-capability-") as temporary:
            root = Path(temporary)
            git_bash = root / "Git/bin/bash.exe"
            git_bash.parent.mkdir(parents=True)
            git_bash.write_bytes(b"fixture")
            self.assertEqual(
                contract.select_bash_executable([str(git_bash)], windows=True),
                str(git_bash),
            )
            wsl = root / "Windows/System32/bash.exe"
            wsl.parent.mkdir(parents=True)
            wsl.write_bytes(b"fixture")
            with self.assertRaisesRegex(contract.ContractError, "WSL launcher"):
                contract.select_bash_executable([str(wsl)], windows=True)

    def test_15_completed_main_and_descendant_require_completion_ancestry(self) -> None:
        temporary, root, completion = identity_repository()
        try:
            contract.validate_git_identity(
                root, status="Completed", environment={}, completion_merge=completion
            )
            git(root, "switch", "-c", "codex/later-feature")
            (root / "later.txt").write_text("later\n", encoding="utf-8")
            git(root, "add", "--", "later.txt")
            git(root, "commit", "-m", "fixture: later descendant")
            contract.validate_git_identity(
                root, status="Completed", environment={}, completion_merge=completion
            )
        finally:
            temporary.cleanup()

    def test_16_completed_identity_rejects_invalid_ancestor(self) -> None:
        temporary, root, completion = identity_repository()
        try:
            git(root, "switch", "-c", "accepted-completion")
            (root / "completion.txt").write_text("completion\n", encoding="utf-8")
            git(root, "add", "--", "completion.txt")
            git(root, "commit", "-m", "fixture: accepted completion")
            completion = git(root, "rev-parse", "HEAD")
            git(root, "switch", "main")
            (root / "unrelated.txt").write_text("unrelated\n", encoding="utf-8")
            git(root, "add", "--", "unrelated.txt")
            git(root, "commit", "-m", "fixture: unrelated head")
            with self.assertRaisesRegex(contract.ContractError, "not a descendant"):
                contract.validate_git_identity(
                    root, status="Completed", environment={},
                    completion_merge=completion,
                )
        finally:
            temporary.cleanup()

    def test_17_completed_identity_rejects_state_or_lifecycle_drift(self) -> None:
        temporary, root, completion = identity_repository()
        try:
            store(root / contract.STATE, {"status": "Completed", "drift": True})
            git(root, "add", "--", contract.STATE)
            git(root, "commit", "-m", "fixture: mutate terminal state")
            with self.assertRaisesRegex(contract.ContractError, "state/lifecycle drift"):
                contract.validate_git_identity(
                    root, status="Completed", environment={},
                    completion_merge=completion,
                )
        finally:
            temporary.cleanup()

    def test_18_completed_ci_requires_exact_event_repository_and_head(self) -> None:
        head = "1" * 40
        environment = {
            "GITHUB_ACTIONS": "true",
            "GITHUB_EVENT_NAME": "push",
            "GITHUB_REPOSITORY": contract.EXPECTED_REPOSITORY,
            "GITHUB_HEAD_REF": "",
            "GITHUB_REF_TYPE": "branch",
            "GITHUB_REF_NAME": "codex/later-feature",
        }
        event = {
            "repository": {"full_name": contract.EXPECTED_REPOSITORY},
            "ref": "refs/heads/codex/later-feature",
            "after": head,
        }
        self.assertEqual(
            contract.resolve_logical_branch(
                environment, event, head, "", status="Completed"
            ),
            "refs/heads/codex/later-feature",
        )
        event["after"] = "2" * 40
        with self.assertRaisesRegex(contract.ContractError, "event head SHA"):
            contract.resolve_logical_branch(
                environment, event, head, "", status="Completed"
            )
        event["after"] = head
        event["repository"]["full_name"] = "foreign/repository"
        with self.assertRaisesRegex(contract.ContractError, "repository differs"):
            contract.resolve_logical_branch(
                environment, event, head, "", status="Completed"
            )

    def test_19_detached_local_and_foreign_origin_fail_closed(self) -> None:
        temporary, root, completion = identity_repository()
        try:
            git(root, "switch", "--detach")
            with self.assertRaisesRegex(contract.ContractError, "detached local HEAD"):
                contract.validate_git_identity(
                    root, status="Completed", environment={},
                    completion_merge=completion,
                )
            git(root, "switch", "main")
            git(root, "remote", "set-url", "origin", "https://github.com/foreign/repo.git")
            with self.assertRaisesRegex(contract.ContractError, "Git origin differs"):
                contract.validate_git_identity(
                    root, status="Completed", environment={},
                    completion_merge=completion,
                )
        finally:
            temporary.cleanup()

    def test_20_worktree_content_is_bound_to_git_blob_with_crlf_equivalence(self) -> None:
        temporary, root, _ = identity_repository()
        try:
            git(root, "config", "core.autocrlf", "true")
            relative = "requirements/intakes/active/Lastenheft_Test.md"
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(b"alpha\nbeta\n")
            git(root, "add", "--", relative)
            git(root, "commit", "-m", "fixture: target")
            target.unlink()
            git(root, "checkout", "--", relative)
            self.assertIn(b"\r\n", target.read_bytes())
            self.assertEqual(git(root, "status", "--porcelain=v1", "--", relative), "")
            accepted = contract.normalized_bytes_sha256(
                contract.git_blob(root, "HEAD", relative), relative
            )
            self.assertEqual(contract.immutable_normalized_sha256(root, relative), accepted)

            state = root / contract.STATE
            state.unlink()
            git(root, "checkout", "--", contract.STATE)
            self.assertIn(b"\r\n", state.read_bytes())
            self.assertEqual(
                contract.immutable_raw_sha256(root, contract.STATE),
                hashlib.sha256(contract.git_blob(root, "HEAD", contract.STATE)).hexdigest(),
            )

            target.write_bytes(b"alpha\ngamma\n")
            with self.assertRaisesRegex(contract.ContractError, "current Git path"):
                contract.immutable_normalized_sha256(root, relative)
        finally:
            temporary.cleanup()

    def test_21_unexpected_physical_target_inventory_fails_closed(self) -> None:
        with projection() as temporary:
            root = Path(temporary)
            extra = root / "requirements/intakes/active/Lastenheft_Unexpected.md"
            extra.write_text("unexpected\n", encoding="utf-8")
            self.assert_contract_error(root, "physical target inventory drift")


if __name__ == "__main__":
    unittest.main(verbosity=2)
