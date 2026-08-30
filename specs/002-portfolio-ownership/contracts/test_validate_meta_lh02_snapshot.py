#!/usr/bin/env python3
"""Isolated standard-library tests for the META-LH-02 snapshot contract."""

from __future__ import annotations

import ast
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
            archive = root / contract.ARCHIVED_TARGET
            archive.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(root / contract.ORIGINAL_TARGET, archive)
            self.assert_contract_error(root, "mutually exclusive; found both")
        with projection() as temporary:
            root = Path(temporary)
            (root / contract.ORIGINAL_TARGET).unlink()
            self.assert_contract_error(root, "mutually exclusive; found neither")

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
            self.assertEqual(
                contract.validate_post_global_ready(
                    Path(temporary), runner=no_review_process
                ),
                contract.PASS_MESSAGE,
            )

    def test_07_temporary_inactive_state_projection(self) -> None:
        with projection() as temporary:
            root = Path(temporary)
            set_target(root, "state.status", "PausedByUser")
            self.assert_contract_error(root, "autonomous run state must be Active")

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
            "pull_request": {"head": {"ref": contract.EXPECTED_BRANCH, "sha": head}},
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
                "head": {"ref": contract.EXPECTED_BRANCH, "sha": event_head}
            },
        }
        with self.assertRaisesRegex(contract.ContractError, "event head SHA"):
            contract.resolve_logical_branch(environment, event, synthetic_head, "")
        with self.assertRaisesRegex(contract.ContractError, "current Git branch"):
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
