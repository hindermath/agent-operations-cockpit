#!/usr/bin/env python3
"""Focused tests for the additive META-LH-03 authoring-contract validator."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CONTRACT_DIR = Path(__file__).resolve().parent
REPO = CONTRACT_DIR.parents[2]
BASH_EXECUTABLE = os.environ.get("AOC_GIT_BASH_EXE", "bash")
sys.path.insert(0, str(CONTRACT_DIR))

from validate_authoring_contract import (  # noqa: E402
    _canonical_raw_sha256,
    _resolve_completed_lifecycle_target,
    ContractViolation,
    normalized_sha256,
    validate_checkpoint,
    validate_leaf_replacement,
    validate_r2_transaction,
)


class AuthoringContractBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.binding = json.loads(
            (REPO / "specs/003-authoring-contract/current-evidence-binding.json").read_text(
                encoding="utf-8"
            )
        )

    def _one_leaf_replacement(self) -> dict:
        candidate = copy.deepcopy(self.binding)
        leaf = next(
            item
            for item in candidate["orderedLogicalTargets"]
            if item["logicalTargetId"] == "META-LH-03"
        )
        leaf["target"]["normalizedSha256"] = "1" * 64
        leaf["authoringReceipt"]["rawSha256"] = "2" * 64
        leaf["readySingleReview"]["rawSha256"] = "3" * 64
        return candidate

    def test_frozen_checkpoint_manifest_matches_repair_tree(self) -> None:
        summary = validate_checkpoint(
            REPO,
            REPO / "specs/003-authoring-contract/repair-checkpoint-manifest.json",
        )
        self.assertEqual(48, summary["validatedPathCount"])
        self.assertTrue(summary["ancestryValid"])
        self.assertFalse(summary["manifestExpectedInsideCheckpoint"])

    def test_exactly_one_meta_lh03_leaf_can_change(self) -> None:
        summary = validate_leaf_replacement(
            self.binding, self._one_leaf_replacement()
        )
        self.assertEqual(["META-LH-03"], summary["changedLogicalTargets"])
        self.assertEqual(13, summary["unchangedLogicalTargetCount"])
        self.assertTrue(summary["completedPredecessorUnchanged"])

    def test_second_changed_leaf_is_rejected(self) -> None:
        candidate = self._one_leaf_replacement()
        second = next(
            item
            for item in candidate["orderedLogicalTargets"]
            if item["logicalTargetId"] == "RAW-03"
        )
        second["authoringReceipt"]["rawSha256"] = "4" * 64
        with self.assertRaisesRegex(ContractViolation, "META-LH-03"):
            validate_leaf_replacement(self.binding, candidate)

    def test_complete_r2_transaction_is_valid(self) -> None:
        summary = validate_r2_transaction(REPO, self.binding)
        self.assertEqual("Completed", summary["operationStatus"])
        self.assertEqual(13, summary["unchangedLogicalTargetCount"])
        self.assertEqual("b8d49ed7-d05f-40b0-9e18-1aa1b689f1cf", summary["reviewId"])

    def test_completed_lifecycle_rejects_coexisting_logical_target(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary)
            logical = "requirements/intakes/active/Lastenheft_META-LH-03.md"
            archived = "requirements/intakes/active/Lastenheft_META-LH-03.003.md"
            content = b"Deutsch / English\n"
            expected = normalized_sha256(content)
            for relative in (logical, archived):
                target = repo / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
            lifecycle = repo / "specs/003-authoring-contract/intake-lifecycle.json"
            lifecycle.parent.mkdir(parents=True, exist_ok=True)
            lifecycle.write_text(json.dumps({
                "schemaVersion": "1.1",
                "records": [{
                    "originalPath": logical,
                    "archivedPath": archived,
                    "originalNormalizedSha256": expected,
                }],
            }), encoding="utf-8")
            with self.assertRaisesRegex(ContractViolation, "logical target to be absent"):
                _resolve_completed_lifecycle_target(repo, logical, expected)

    def test_wrong_reserved_ids_are_rejected(self) -> None:
        candidate = copy.deepcopy(self.binding)
        leaf = next(
            item for item in candidate["orderedLogicalTargets"]
            if item["logicalTargetId"] == "META-LH-03"
        )
        leaf["readySingleReview"]["path"] = "specs/intake-review-results/wrong.json"
        with self.assertRaises(ContractViolation):
            validate_r2_transaction(REPO, candidate)

    def test_transaction_negative_cases_fail_closed(self) -> None:
        operation_path = REPO / "specs/intake-authoring-operations/986c1d6c-d485-460b-8d8d-7cf5816a2c36/operation.json"
        operation = json.loads(operation_path.read_text(encoding="utf-8"))
        mutations = (
            ("proposal-hash", lambda value: value.__setitem__("proposalNormalizedSha256", "0" * 64)),
            ("target-set", lambda value: value["publishedTargets"].pop()),
            ("incomplete", lambda value: value.__setitem__("status", "Applying")),
            ("failed-repair", lambda value: (value.__setitem__("status", "Failed"), value.__setitem__("failure", {"class": "N/A", "message": "N/A"}))),
            ("archive-drift", lambda value: value["supersedes"].__setitem__("archiveTargetRawSha256", "0" * 64)),
            ("missing-r1-review", lambda value: value.__setitem__("r1ReviewSupersession", {})),
        )
        for name, mutate in mutations:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temporary:
                candidate = copy.deepcopy(operation)
                mutate(candidate)
                candidate_path = Path(temporary) / "operation.json"
                candidate_path.write_text(json.dumps(candidate), encoding="utf-8")
                with self.assertRaises(ContractViolation):
                    validate_r2_transaction(REPO, self.binding, operation_path=candidate_path)


class AuthoringContractAdapterTests(unittest.TestCase):
    bash_adapter = CONTRACT_DIR / "validate-authoring-contract.sh"
    powershell_adapter = CONTRACT_DIR / "validate-authoring-contract.ps1"

    def _run_pair(self, repo: Path, json_output: bool = False) -> list[subprocess.CompletedProcess[str]]:
        bash_script = self.bash_adapter.relative_to(REPO).as_posix()
        bash_args = [BASH_EXECUTABLE, bash_script, "--repo", str(repo)]
        pwsh_args = [
            "pwsh",
            "-NoProfile",
            "-File",
            str(self.powershell_adapter),
            "-Repo",
            str(repo),
        ]
        if json_output:
            bash_args.append("--json")
            pwsh_args.append("-Json")
        return [
            subprocess.run(
                args,
                cwd=REPO,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            for args in (bash_args, pwsh_args)
        ]

    def test_bash_and_powershell_success_and_json_parity(self) -> None:
        results = self._run_pair(REPO, json_output=True)
        self.assertEqual([0, 0], [item.returncode for item in results])
        payloads = [json.loads(item.stdout) for item in results]
        self.assertEqual(payloads[0], payloads[1])
        self.assertEqual("Pass", payloads[0]["outcome"])

    def test_bash_and_powershell_validation_failure_parity(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results = self._run_pair(Path(temporary), json_output=True)
        self.assertEqual([2, 2], [item.returncode for item in results])
        self.assertTrue(all(json.loads(item.stdout)["outcome"] == "Fail" for item in results))

    def test_bash_and_powershell_usage_failure_parity(self) -> None:
        commands = [
            [BASH_EXECUTABLE, self.bash_adapter.relative_to(REPO).as_posix(), "--unknown"],
            ["pwsh", "-NoProfile", "-File", str(self.powershell_adapter), "-Unknown"],
        ]
        results = [
            subprocess.run(
                args,
                cwd=REPO,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            for args in commands
        ]
        self.assertEqual([64, 64], [item.returncode for item in results])

    def test_utf8_bom_and_line_endings_normalize_identically(self) -> None:
        lf = "Deutsch zuerst / English second\n"
        crlf_bom = b"\xef\xbb\xbf" + lf.replace("\n", "\r\n").encode("utf-8")
        expected = hashlib.sha256(lf.encode("utf-8")).hexdigest()
        self.assertEqual(expected, normalized_sha256(lf.encode("utf-8")))
        self.assertEqual(expected, normalized_sha256(crlf_bom))

    def test_tracked_raw_hash_accepts_checkout_only_line_endings(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary)
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            subprocess.run(
                ["git", "-C", str(repo), "config", "user.email", "fixture@example.invalid"],
                check=True,
            )
            subprocess.run(
                ["git", "-C", str(repo), "config", "user.name", "Fixture"],
                check=True,
            )
            fixture = repo / "fixture.md"
            fixture.write_bytes(b"Deutsch / English\n")
            subprocess.run(["git", "-C", str(repo), "add", "--", "fixture.md"], check=True)
            subprocess.run(
                ["git", "-C", str(repo), "commit", "-q", "-m", "fixture"],
                check=True,
            )
            fixture.write_bytes(b"Deutsch / English\r\n")
            self.assertEqual(
                hashlib.sha256(b"Deutsch / English\n").hexdigest(),
                _canonical_raw_sha256(repo, "fixture.md"),
            )


if __name__ == "__main__":
    unittest.main()
