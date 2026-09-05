#!/usr/bin/env python3
"""Self-contained negative contract tests; real repository state is untouched."""

from __future__ import annotations

import hashlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import validate_meta_lh01 as contract


BI = "Deutsch / English"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def domain_fixture(root: Path) -> None:
    source = ["# Quellen / Sources", "| ID | Role | Content | Authority | Currency | Supersession | Use |",
              "|---|---|---|---|---|---|---|"]
    for source_id in sorted(contract.EXPECTED_SOURCES):
        source.append(f"| {source_id} | {BI} | {BI} | {BI} | {BI} | {BI} | {BI} |")
    write(root / contract.DOMAIN_PATHS[0], "\n".join(source) + "\n")

    constraints = ["# Vorgaben / Constraints", "| ID | Statement | Evidence |", "|---|---|---|"]
    for number in range(1, 26):
        constraints.append(f"| CON-{number:02d} | {BI} | {BI} |")
    write(root / contract.DOMAIN_PATHS[1], "\n".join(constraints) + "\n")

    findings = ["# Findings / Findings",
                "| ID | Severity | Statement | Owner | Target | Acceptance | Positive | Negative | Status | Gap |",
                "|---|---|---|---|---|---|---|---|---|---|"]
    for number in range(1, 22):
        severity = "blocking" if number == 1 else "important"
        findings.append(f"| RF-{number:02d} | {severity} | {BI} | {BI} | {BI} | {BI} | {BI} | {BI} | Covered / Covered | N/A / N/A |")
    write(root / contract.DOMAIN_PATHS[2], "\n".join(findings) + "\n")

    coverage = ["# Abdeckung / Coverage", "| ID | Meta | Domain | Coverage | Direct |", "|---|---|---|---|---|"]
    for source_id in sorted(contract.EXPECTED_SOURCES):
        coverage.append(f"| {source_id} | META-01 | RAW-01 | Covered | N/A |")
    for number in range(1, 22):
        finding = f"RF-{number:02d}"
        direct = "Yes" if finding in contract.DIRECT_META else "No"
        coverage.append(f"| {finding} | META-01 | RAW-01 | Covered | {direct} |")
    write(root / contract.DOMAIN_PATHS[3], "\n".join(coverage) + "\n")

    glossary = ["# Glossar / Glossary", "| Deutsch | English | Explanation |", "|---|---|---|"]
    for term in ("Autorität", "Evidence", "Receipt", "Coverage", "Stop-Gate"):
        glossary.append(f"| {term} | term | {BI} |")
    write(root / contract.DOMAIN_PATHS[4], "\n".join(glossary) + "\n")

    gates = ["# Gates / Gates", "| Gate | Allows | Stops | Evidence | Human | Next |", "|---|---|---|---|---|---|"]
    gates.append(f"| G-01 Source | {BI} | fail-closed / fail-closed | {BI} | {BI} | Stop / Stop |")
    gates.append(f"| G-05 Global | {BI} | Drift / Drift | 14 Ready / 14 Ready | {BI} | Stop / Stop |")
    gates.append(f"| G-06 Implementation | Dokumentation / Documentation | Gate offen / Gate open | {BI} | {BI} | Produktcode ausgeschlossen / product code excluded |")
    write(root / contract.DOMAIN_PATHS[5], "\n".join(gates) + "\n")


def lifecycle_fixture(root: Path, *, archived: bool = False) -> tuple[dict, dict]:
    original_bytes = b"Accepted META-LH-01 bytes\n"
    original_hash = hashlib.sha256(original_bytes).hexdigest()
    physical = contract.ARCHIVED_META01 if archived else contract.ORIGINAL_META01
    path = root / physical
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(original_bytes)

    receipt_path = "specs/intake-authoring-receipts/META-LH-01-Programmquellen.json"
    review_path = "specs/intake-review-results/meta-lh-01-programmquellen-2026-08-01-r2.json"
    receipt = {
        "status": "ReadyForReview",
        "target": {"path": contract.ORIGINAL_META01, "normalizedSha256": original_hash},
    }
    review = {
        "mode": "Single", "status": "Ready",
        "targets": [{"path": contract.ORIGINAL_META01, "role": "Primary",
                     "normalizedSha256": original_hash}],
        "findings": [], "questions": [], "acceptedRisks": [],
    }
    write(root / receipt_path, json.dumps(receipt) + "\n")
    write(root / review_path, json.dumps(review) + "\n")
    receipt_hash = contract.raw_sha256(root / receipt_path)
    review_hash = contract.raw_sha256(root / review_path)
    state = {
        "runId": "b3694a58-208b-4d6b-a4d4-1b01f3816dcc",
        "branch": "001-programmquellen-baseline",
        "acceptedArtifacts": [
            {"path": contract.ORIGINAL_META01, "sha256": original_hash},
            {"path": review_path, "sha256": review_hash},
            {"path": receipt_path, "sha256": receipt_hash},
        ],
        "acceptedArtifactLifecycle": {
            "path": contract.LIFECYCLE, "schemaVersion": "1.1",
            "logicalTargetId": contract.LOGICAL_META01,
        },
    }
    record = {
        "recordVersion": "1.0", "logicalTargetId": contract.LOGICAL_META01,
        "originalPath": contract.ORIGINAL_META01,
        "archivedPath": contract.ARCHIVED_META01,
        "originalRawSha256": original_hash,
        "originalNormalizedSha256": original_hash,
        "authoringReceipt": {"path": receipt_path, "rawSha256": receipt_hash},
        "readySingleReview": {"path": review_path, "rawSha256": review_hash},
        "runId": state["runId"], "branch": state["branch"],
    }
    write(root / contract.STATE, json.dumps(state) + "\n")
    write(root / contract.LIFECYCLE,
          json.dumps({
              "schemaVersion": "1.1", "records": [record],
              "programmeEvidenceSnapshot": {
                  "snapshotVersion": "1.0", "runId": state["runId"],
                  "branch": state["branch"], "orderedLogicalTargets": [],
              },
          }) + "\n")
    return state, record


def programme_snapshot_fixture(root: Path, *, archived: bool = False) -> tuple[dict, dict]:
    common_source = root / "requirements/baseline/source-pack.md"
    write(common_source, "Accepted shared source snapshot\n")
    accepted_source_hash = contract.normalized_sha256(common_source)
    ordered: list[dict] = []
    receipt_by_target: dict[str, tuple[str, str]] = {}
    review_by_target: dict[str, tuple[str, str]] = {}
    target_hashes: dict[str, str] = {}
    for logical_id, target_path in contract.PROGRAMME_TARGETS:
        write(root / target_path, f"Accepted {logical_id} bytes\n")
        target_hash = contract.normalized_sha256(root / target_path)
        target_hashes[target_path] = target_hash
        receipt_path = f"specs/intake-authoring-receipts/{logical_id}.json"
        review_path = f"specs/intake-review-results/{logical_id.lower()}.json"
        receipt = {
            "status": "ReadyForReview",
            "target": {"path": target_path, "normalizedSha256": target_hash},
            "sources": [{
                "path": "requirements/baseline/source-pack.md",
                "normalizedSha256": accepted_source_hash,
            }],
        }
        review = {
            "mode": "Single", "status": "Ready", "supersedes": "N/A",
            "targets": [{"path": target_path, "role": "Primary",
                         "normalizedSha256": target_hash}],
            "findings": [], "questions": [], "acceptedRisks": [],
        }
        write(root / receipt_path, json.dumps(receipt) + "\n")
        write(root / review_path, json.dumps(review) + "\n")
        receipt_hash = contract.raw_sha256(root / receipt_path)
        review_hash = contract.raw_sha256(root / review_path)
        receipt_by_target[target_path] = (receipt_path, receipt_hash)
        review_by_target[target_path] = (review_path, review_hash)
        ordered.append({
            "logicalTargetId": logical_id,
            "target": {"path": target_path, "normalizedSha256": target_hash},
            "authoringReceipt": {"path": receipt_path, "rawSha256": receipt_hash},
            "readySingleReview": {"path": review_path, "rawSha256": review_hash},
        })

    meta_receipt_path, meta_receipt_hash = receipt_by_target[contract.ORIGINAL_META01]
    meta_review_path, meta_review_hash = review_by_target[contract.ORIGINAL_META01]
    state = {
        "runId": "b3694a58-208b-4d6b-a4d4-1b01f3816dcc",
        "branch": "001-programmquellen-baseline",
        "stage": "Implement", "status": "Active",
        "lastPassingGate": "GlobalReadyBeforeImplement",
        "acceptedArtifacts": [
            {"path": contract.ORIGINAL_META01,
             "sha256": contract.raw_sha256(root / contract.ORIGINAL_META01)},
            {"path": meta_review_path, "sha256": meta_review_hash},
            {"path": meta_receipt_path, "sha256": meta_receipt_hash},
        ],
        "acceptedArtifactLifecycle": {
            "path": contract.LIFECYCLE, "schemaVersion": "1.1",
            "logicalTargetId": contract.LOGICAL_META01,
        },
    }
    record = {
        "recordVersion": "1.0", "logicalTargetId": contract.LOGICAL_META01,
        "originalPath": contract.ORIGINAL_META01,
        "archivedPath": contract.ARCHIVED_META01,
        "originalRawSha256": contract.raw_sha256(root / contract.ORIGINAL_META01),
        "originalNormalizedSha256": target_hashes[contract.ORIGINAL_META01],
        "authoringReceipt": {"path": meta_receipt_path, "rawSha256": meta_receipt_hash},
        "readySingleReview": {"path": meta_review_path, "rawSha256": meta_review_hash},
        "runId": state["runId"], "branch": state["branch"],
    }
    lifecycle = {
        "schemaVersion": "1.1", "records": [record],
        "programmeEvidenceSnapshot": {
            "snapshotVersion": "1.0", "runId": state["runId"],
            "branch": state["branch"], "orderedLogicalTargets": ordered,
        },
    }
    write(root / contract.STATE, json.dumps(state) + "\n")
    write(root / contract.LIFECYCLE, json.dumps(lifecycle) + "\n")
    if archived:
        archive = root / contract.ARCHIVED_META01
        archive.parent.mkdir(parents=True, exist_ok=True)
        (root / contract.ORIGINAL_META01).rename(archive)
    write(common_source, "Authorised post-Implement shared source evolution\n")
    return state, lifecycle


def causal_closeout_fixture(root: Path) -> tuple[dict, dict]:
    tasks = "# Tasks\n\n" + "".join(
        f"- [x] T{number:03d} Completed task.\n" for number in range(1, 67)
    )
    write(root / contract.TASKS, tasks)
    state = {
        "schemaVersion": "1.1",
        "runId": "b3694a58-208b-4d6b-a4d4-1b01f3816dcc",
        "stage": "MergeAndSync",
        "status": "Completed",
        "nextExactAction": "N/A",
        "tasks": {
            "path": contract.TASKS,
            "sha256": contract.raw_sha256(root / contract.TASKS),
            "completed": 66,
            "total": 66,
        },
        "closeout": {
            "mergeOrPublication": "Completed",
            "defaultBranchSync": "Completed",
            "postMergeActions": "Completed",
            "finalValidation": "Completed",
        },
        "causalCloseout": {
            "evidencePath": contract.CAUSAL_CLOSEOUT,
            "branch": contract.CLOSEOUT_BRANCH,
            "allowedPaths": list(contract.CLOSEOUT_PATHS),
            "status": "Completed",
            "publicationEvidence": "ExternalOnly",
        },
    }
    write(root / contract.STATE, json.dumps(state) + "\n")
    reviewer = {
        "independent": True,
        "role": "Independent closeout reviewer",
        "independenceStatement": "The reviewer did not author the closeout delta.",
    }
    exact_paths = list(contract.CLOSEOUT_PATHS)
    public_rows = [
        {
            "path": path,
            "criteria": {key: "Pass" for key in contract.PUBLIC_CRITERIA},
            "rationale": "The path is suitable for public repository content.",
        }
        for path in exact_paths
    ]
    evidence = {
        "schemaVersion": "1.0",
        "status": "Completed",
        "runId": state["runId"],
        "closeoutBranch": contract.CLOSEOUT_BRANCH,
        "closeoutPaths": list(exact_paths),
        "terminalFeatureHead": "1" * 40,
        "featurePullRequest": {
            "number": 123,
            "url": "https://example.invalid/pull/123",
        },
        "featureMergeSha": "2" * 40,
        "synchronizedMainSha": "3" * 40,
        "commands": [
            {
                "checkId": check_id,
                "command": f"verify {check_id}",
                "result": "Pass",
                "evidenceReference": f"local://{check_id}",
            }
            for check_id in sorted(contract.CAUSAL_COMMAND_IDS)
        ],
        "documentationReview": {
            "result": "Pass",
            "reviewer": reviewer,
            "reviewedPaths": list(exact_paths),
            "rationale": "The exact closeout delta preserves the single UpdateRequired decision.",
            "blockingFindings": [],
        },
        "publicContentReview": {
            "result": "Pass",
            "reviewer": reviewer,
            "reviewedPaths": list(exact_paths),
            "rationale": "The exact closeout delta is safe to publish.",
            "blockingFindings": [],
            "reviews": public_rows,
        },
        "nonSelfReferentialBoundary": {
            "containingCommitSha": "N/A",
            "closeoutPullRequest": "N/A",
            "closeoutMergeSha": "N/A",
            "statement": "This evidence does not claim its own containing commit, PR, or merge SHA.",
        },
    }
    write(root / contract.CAUSAL_CLOSEOUT, json.dumps(evidence) + "\n")
    return state, evidence


def completed_meta02_dispatch_fixture(root: Path, disposition: str = "archived") -> None:
    if disposition in {"original", "both"}:
        write(root / contract.ORIGINAL_META02, "META-LH-02\n")
    if disposition in {"archived", "both"}:
        write(root / contract.ARCHIVED_META02, "META-LH-02\n")
    state = {
        "status": "Completed",
        "stage": "MergeAndSync",
        "nextExactAction": "N/A",
        "tasks": {"completed": 93, "total": 93},
        "closeout": {
            "mergeOrPublication": "Completed",
            "defaultBranchSync": "Completed",
            "postMergeActions": "Completed",
            "finalValidation": "Completed",
        },
    }
    write(root / contract.META02_STATE, json.dumps(state) + "\n")


class ContractNegativeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="meta-lh01-contract-")
        self.root = Path(self.temp.name)
        domain_fixture(self.root)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def assert_contract_error(self, action, contains: str) -> None:
        with self.assertRaises(contract.ContractError) as caught:
            action()
        self.assertIn(contains, str(caught.exception))

    @staticmethod
    def source_drift_runner(command: list[str], root: Path, label: str) -> None:
        del command, root
        if "receipt validator" in label:
            raise contract.ContractError(
                "source hash drift: requirements/baseline/source-pack.md"
            )

    def snapshot_fixture(self) -> tuple[dict, dict]:
        return programme_snapshot_fixture(self.root)

    def write_snapshot_lifecycle(self, lifecycle: dict) -> None:
        write(self.root / contract.LIFECYCLE, json.dumps(lifecycle) + "\n")

    def test_positive_domain_fixture(self) -> None:
        self.assertIn("23 sources", contract.validate_domain(self.root))

    def test_missing_source(self) -> None:
        path = self.root / contract.DOMAIN_PATHS[0]
        write(path, path.read_text().replace(f"| {sorted(contract.EXPECTED_SOURCES)[0]} | {BI}", f"| REMOVED | {BI}", 1))
        self.assert_contract_error(lambda: contract.validate_domain(self.root), "missing IDs")

    def test_duplicate_source(self) -> None:
        path = self.root / contract.DOMAIN_PATHS[0]
        row = next(line for line in path.read_text().splitlines() if line.startswith("| SRC-156 |"))
        write(path, path.read_text() + row + "\n")
        self.assert_contract_error(lambda: contract.validate_domain(self.root), "duplicate IDs")

    def test_missing_rf_field(self) -> None:
        path = self.root / contract.DOMAIN_PATHS[2]
        write(path, path.read_text().replace(f"| RF-01 | blocking | {BI} |", "| RF-01 | blocking | |", 1))
        self.assert_contract_error(lambda: contract.validate_domain(self.root), "ten separate non-empty fields")

    def test_wrong_direct_ownership(self) -> None:
        path = self.root / contract.DOMAIN_PATHS[3]
        write(path, path.read_text().replace("| RF-01 | META-01 | RAW-01 | Covered | Yes |",
                                             "| RF-01 | META-01 | RAW-01 | Covered | No |", 1))
        self.assert_contract_error(lambda: contract.validate_domain(self.root), "direct META-LH-01 ownership")

    def test_incomplete_authority_gate(self) -> None:
        path = self.root / contract.DOMAIN_PATHS[5]
        write(path, path.read_text().replace(f"| G-05 Global | {BI} |", "| G-05 Global | |", 1))
        self.assert_contract_error(lambda: contract.validate_domain(self.root), "authority gate G-05 needs")

    def test_stale_input_hash(self) -> None:
        state, _ = lifecycle_fixture(self.root)
        state["acceptedArtifacts"][0]["sha256"] = "0" * 64
        write(self.root / contract.STATE, json.dumps(state) + "\n")
        self.assert_contract_error(
            lambda: contract.validate_input_bindings(self.root, "bash"),
            "raw hash differs from acceptedArtifacts",
        )

    def test_lifecycle_pre_rename_success(self) -> None:
        lifecycle_fixture(self.root)
        physical, disposition, _ = contract.resolve_meta01_target(
            self.root, contract.load_json(self.root / contract.STATE, "state")
        )
        self.assertEqual((physical, disposition), (contract.ORIGINAL_META01, "Active"))

    def test_lifecycle_archived_success(self) -> None:
        lifecycle_fixture(self.root, archived=True)
        physical, disposition, _ = contract.resolve_meta01_target(
            self.root, contract.load_json(self.root / contract.STATE, "state")
        )
        self.assertEqual((physical, disposition), (contract.ARCHIVED_META01, "Archived"))

    def test_lifecycle_missing_both_paths(self) -> None:
        lifecycle_fixture(self.root)
        (self.root / contract.ORIGINAL_META01).unlink()
        state = contract.load_json(self.root / contract.STATE, "state")
        self.assert_contract_error(
            lambda: contract.resolve_meta01_target(self.root, state), "found neither"
        )

    def test_lifecycle_rejects_both_paths(self) -> None:
        lifecycle_fixture(self.root)
        archive = self.root / contract.ARCHIVED_META01
        archive.parent.mkdir(parents=True, exist_ok=True)
        archive.write_bytes((self.root / contract.ORIGINAL_META01).read_bytes())
        state = contract.load_json(self.root / contract.STATE, "state")
        self.assert_contract_error(
            lambda: contract.resolve_meta01_target(self.root, state), "found both"
        )

    def test_lifecycle_rejects_archived_hash_mismatch(self) -> None:
        lifecycle_fixture(self.root, archived=True)
        (self.root / contract.ARCHIVED_META01).write_bytes(b"drift\n")
        state = contract.load_json(self.root / contract.STATE, "state")
        self.assert_contract_error(
            lambda: contract.resolve_meta01_target(self.root, state), "raw SHA-256"
        )

    def test_lifecycle_rejects_wrong_branch_stamp(self) -> None:
        state, record = lifecycle_fixture(self.root, archived=True)
        record["archivedPath"] = contract.ORIGINAL_META01.removesuffix(".md") + ".wrong-branch.md"
        lifecycle = contract.load_json(self.root / contract.LIFECYCLE, "lifecycle")
        lifecycle["records"] = [record]
        write(self.root / contract.LIFECYCLE, json.dumps(lifecycle) + "\n")
        self.assert_contract_error(
            lambda: contract.resolve_meta01_target(self.root, state), "wrong branch stamp"
        )

    def test_lifecycle_rejects_duplicate_records(self) -> None:
        state, record = lifecycle_fixture(self.root)
        lifecycle = contract.load_json(self.root / contract.LIFECYCLE, "lifecycle")
        lifecycle["records"] = [record, record]
        write(self.root / contract.LIFECYCLE, json.dumps(lifecycle) + "\n")
        self.assert_contract_error(
            lambda: contract.resolve_meta01_target(self.root, state), "exactly one"
        )

    def test_lifecycle_rejects_stale_receipt_binding(self) -> None:
        state, record = lifecycle_fixture(self.root)
        receipt_path = Path(record["authoringReceipt"]["path"])
        receipt = contract.load_json(self.root / receipt_path, "receipt")
        receipt["target"]["normalizedSha256"] = "0" * 64
        write(self.root / receipt_path, json.dumps(receipt) + "\n")
        changed_hash = contract.raw_sha256(self.root / receipt_path)
        record["authoringReceipt"]["rawSha256"] = changed_hash
        state["acceptedArtifacts"][2]["sha256"] = changed_hash
        lifecycle = contract.load_json(self.root / contract.LIFECYCLE, "lifecycle")
        lifecycle["records"] = [record]
        write(self.root / contract.LIFECYCLE, json.dumps(lifecycle) + "\n")
        self.assert_contract_error(
            lambda: contract.resolve_meta01_target(self.root, state), "Receipt is stale"
        )

    def test_lifecycle_rejects_stale_review_binding(self) -> None:
        state, record = lifecycle_fixture(self.root)
        accepted_path = record["readySingleReview"]["path"]
        accepted = contract.load_json(self.root / accepted_path, "accepted review")
        accepted["status"] = "NeedsRemediation"
        write(self.root / accepted_path, json.dumps(accepted) + "\n")
        changed_hash = contract.raw_sha256(self.root / accepted_path)
        record["readySingleReview"]["rawSha256"] = changed_hash
        state["acceptedArtifacts"][1]["sha256"] = changed_hash
        lifecycle = contract.load_json(self.root / contract.LIFECYCLE, "lifecycle")
        lifecycle["records"] = [record]
        write(self.root / contract.LIFECYCLE, json.dumps(lifecycle) + "\n")
        self.assert_contract_error(
            lambda: contract.resolve_meta01_target(self.root, state), "stale or"
        )

    def test_snapshot_post_implement_input_bindings_bash(self) -> None:
        programme_snapshot_fixture(self.root, archived=True)
        calls: list[str] = []
        projected_targets: list[bool] = []

        def capture(command: list[str], root: Path, label: str) -> None:
            calls.append(label)
            if "Bash review" in label:
                review_repo = Path(command[command.index("--repo") + 1])
                projected_targets.append((review_repo / contract.ORIGINAL_META01).is_file())

        with mock.patch.object(
                contract, "run_checked",
                side_effect=capture):
            summary = contract.validate_input_bindings(self.root, "bash")
        self.assertIn("programme snapshot", summary)
        self.assertIn("archived target", summary)
        self.assertTrue(any("Bash run-state" in label for label in calls))
        self.assertTrue(any("Bash review" in label for label in calls))
        self.assertEqual([True], projected_targets)
        self.assertFalse(any("receipt validator" in label for label in calls))

    def test_snapshot_post_implement_input_bindings_powershell(self) -> None:
        self.snapshot_fixture()
        calls: list[str] = []
        with mock.patch.object(
                contract, "run_checked",
                side_effect=lambda command, root, label: calls.append(label)):
            summary = contract.validate_input_bindings(self.root, "powershell")
        self.assertIn("programme snapshot", summary)
        self.assertTrue(any("PowerShell run-state" in label for label in calls))
        self.assertTrue(any("PowerShell review" in label for label in calls))
        self.assertFalse(any("receipt validator" in label for label in calls))

    def test_snapshot_post_implement_global_ready(self) -> None:
        programme_snapshot_fixture(self.root, archived=True)
        calls: list[str] = []
        projected_targets: list[bool] = []

        def capture(command: list[str], root: Path, label: str) -> None:
            calls.append(label)
            if f"review validator for {contract.ORIGINAL_META01}" in label:
                option = "--repo" if "--repo" in command else "-Repo"
                review_repo = Path(command[command.index(option) + 1])
                projected_targets.append((review_repo / contract.ORIGINAL_META01).is_file())

        with mock.patch.object(
                contract, "run_checked",
                side_effect=capture):
            summary = contract.validate_global_ready(self.root)
        self.assertIn("qualified immutable programme snapshot", summary)
        self.assertEqual(28, sum("review validator" in label for label in calls))
        self.assertEqual([True, True], projected_targets)
        self.assertFalse(any("receipt validator" in label for label in calls))

    def test_global_ready_dispatches_to_qualified_completed_meta02(self) -> None:
        with mock.patch.object(
                contract, "qualified_completed_meta02_snapshot",
                return_value="completed snapshot proof") as dispatch:
            self.assertEqual(
                contract.validate_global_ready(self.root),
                "qualified completed META-LH-02 snapshot; completed snapshot proof",
            )
        dispatch.assert_called_once_with(self.root)

    def test_meta02_dispatch_rejects_unfinished_closeout(self) -> None:
        write(self.root / contract.ARCHIVED_META02, "archived META-LH-02\n")
        state = {
            "status": "Active",
            "stage": "MergeAndSync",
            "nextExactAction": "Complete closeout",
            "tasks": {"completed": 92, "total": 93},
            "closeout": {
                "mergeOrPublication": "Completed",
                "defaultBranchSync": "Pending",
                "postMergeActions": "Pending",
                "finalValidation": "Pending",
            },
        }
        write(self.root / contract.META02_STATE, json.dumps(state) + "\n")
        self.assert_contract_error(
            lambda: contract.qualified_completed_meta02_snapshot(self.root),
            "not a qualified terminal Completed snapshot",
        )

    def test_meta02_dispatch_rejects_ambiguous_paths(self) -> None:
        write(self.root / contract.ORIGINAL_META02, "original META-LH-02\n")
        write(self.root / contract.ARCHIVED_META02, "archived META-LH-02\n")
        self.assert_contract_error(
            lambda: contract.qualified_completed_meta02_snapshot(self.root),
            "original and archived paths are ambiguous",
        )

    def test_meta02_completed_dispatch_rejects_original_only_and_absent_target(self) -> None:
        for disposition in ("original", "absent"):
            with self.subTest(disposition=disposition):
                root = self.root / disposition
                completed_meta02_dispatch_fixture(root, disposition)
                self.assert_contract_error(
                    lambda root=root: contract.qualified_completed_meta02_snapshot(root),
                    "not a qualified terminal Completed snapshot",
                )

    def test_meta02_completed_dispatch_requires_exact_success_output(self) -> None:
        completed_meta02_dispatch_fixture(self.root)
        (self.root / ".git").mkdir()
        accepted = subprocess.CompletedProcess(
            args=[], returncode=0,
            stdout=f"{contract.META02_PASS_MESSAGE}\n", stderr="",
        )
        with mock.patch.object(contract.subprocess, "run", return_value=accepted):
            self.assertIn(
                "archive-aware META-LH-02",
                contract.qualified_completed_meta02_snapshot(self.root),
            )

        invalid_results = (
            subprocess.CompletedProcess(
                args=[], returncode=0,
                stdout=f"{contract.META02_PASS_MESSAGE} changed\n", stderr="",
            ),
            subprocess.CompletedProcess(
                args=[], returncode=0,
                stdout=f"{contract.META02_PASS_MESSAGE}\nextra\n", stderr="",
            ),
            subprocess.CompletedProcess(
                args=[], returncode=0,
                stdout=f"{contract.META02_PASS_MESSAGE}\n", stderr="warning\n",
            ),
        )
        for result in invalid_results:
            with self.subTest(stdout=result.stdout, stderr=result.stderr), mock.patch.object(
                    contract.subprocess, "run", return_value=result):
                self.assert_contract_error(
                    lambda: contract.qualified_completed_meta02_snapshot(self.root),
                    "invalid success result",
                )

    def test_snapshot_rejects_pre_implement_shared_source_drift(self) -> None:
        state, _ = self.snapshot_fixture()
        state["stage"] = "Plan"
        write(self.root / contract.STATE, json.dumps(state) + "\n")
        with mock.patch.object(contract, "run_checked", side_effect=self.source_drift_runner):
            self.assert_contract_error(
                lambda: contract.validate_global_ready(self.root), "source hash drift"
            )

    def test_snapshot_rejects_forged_stage(self) -> None:
        state, _ = self.snapshot_fixture()
        state["stage"] = "MergeAndSync"
        write(self.root / contract.STATE, json.dumps(state) + "\n")
        with mock.patch.object(contract, "run_checked", side_effect=self.source_drift_runner):
            self.assert_contract_error(
                lambda: contract.validate_global_ready(self.root), "source hash drift"
            )

    def test_snapshot_rejects_forged_status(self) -> None:
        state, _ = self.snapshot_fixture()
        state["status"] = "Completed"
        write(self.root / contract.STATE, json.dumps(state) + "\n")
        with mock.patch.object(contract, "run_checked", side_effect=self.source_drift_runner):
            self.assert_contract_error(
                lambda: contract.validate_global_ready(self.root), "source hash drift"
            )

    def test_snapshot_rejects_forged_last_passing_gate(self) -> None:
        state, _ = self.snapshot_fixture()
        state["lastPassingGate"] = "AnalyzePassed"
        write(self.root / contract.STATE, json.dumps(state) + "\n")
        with mock.patch.object(contract, "run_checked", side_effect=self.source_drift_runner):
            self.assert_contract_error(
                lambda: contract.validate_global_ready(self.root), "source hash drift"
            )

    def test_snapshot_rejects_missing_target(self) -> None:
        state, lifecycle = self.snapshot_fixture()
        lifecycle["programmeEvidenceSnapshot"]["orderedLogicalTargets"].pop()
        self.write_snapshot_lifecycle(lifecycle)
        self.assert_contract_error(
            lambda: contract.validate_programme_evidence_snapshot(
                self.root, state, contract.ORIGINAL_META01), "exact 14 ordered"
        )

    def test_snapshot_rejects_duplicate_target(self) -> None:
        state, lifecycle = self.snapshot_fixture()
        ordered = lifecycle["programmeEvidenceSnapshot"]["orderedLogicalTargets"]
        ordered[-1]["logicalTargetId"] = ordered[0]["logicalTargetId"]
        self.write_snapshot_lifecycle(lifecycle)
        self.assert_contract_error(
            lambda: contract.validate_programme_evidence_snapshot(
                self.root, state, contract.ORIGINAL_META01), "duplicate logical targets"
        )

    def test_snapshot_rejects_reordered_target(self) -> None:
        state, lifecycle = self.snapshot_fixture()
        ordered = lifecycle["programmeEvidenceSnapshot"]["orderedLogicalTargets"]
        ordered[1], ordered[2] = ordered[2], ordered[1]
        self.write_snapshot_lifecycle(lifecycle)
        self.assert_contract_error(
            lambda: contract.validate_programme_evidence_snapshot(
                self.root, state, contract.ORIGINAL_META01), "reordered"
        )

    def test_snapshot_rejects_wrong_target_path(self) -> None:
        state, lifecycle = self.snapshot_fixture()
        lifecycle["programmeEvidenceSnapshot"]["orderedLogicalTargets"][1]["target"]["path"] = "wrong.md"
        self.write_snapshot_lifecycle(lifecycle)
        self.assert_contract_error(
            lambda: contract.validate_programme_evidence_snapshot(
                self.root, state, contract.ORIGINAL_META01), "target.path differs"
        )

    def test_snapshot_rejects_wrong_target_hash(self) -> None:
        state, lifecycle = self.snapshot_fixture()
        lifecycle["programmeEvidenceSnapshot"]["orderedLogicalTargets"][1]["target"]["normalizedSha256"] = "0" * 64
        self.write_snapshot_lifecycle(lifecycle)
        self.assert_contract_error(
            lambda: contract.validate_programme_evidence_snapshot(
                self.root, state, contract.ORIGINAL_META01), "target normalized SHA-256 drift"
        )

    def test_snapshot_rejects_wrong_receipt_path(self) -> None:
        state, lifecycle = self.snapshot_fixture()
        lifecycle["programmeEvidenceSnapshot"]["orderedLogicalTargets"][1]["authoringReceipt"]["path"] = "wrong.json"
        self.write_snapshot_lifecycle(lifecycle)
        self.assert_contract_error(
            lambda: contract.validate_programme_evidence_snapshot(
                self.root, state, contract.ORIGINAL_META01), "unique current receipt"
        )

    def test_snapshot_rejects_wrong_receipt_hash(self) -> None:
        state, lifecycle = self.snapshot_fixture()
        lifecycle["programmeEvidenceSnapshot"]["orderedLogicalTargets"][1]["authoringReceipt"]["rawSha256"] = "0" * 64
        self.write_snapshot_lifecycle(lifecycle)
        self.assert_contract_error(
            lambda: contract.validate_programme_evidence_snapshot(
                self.root, state, contract.ORIGINAL_META01), "authoringReceipt raw SHA-256 drift"
        )

    def test_snapshot_rejects_wrong_review_path(self) -> None:
        state, lifecycle = self.snapshot_fixture()
        lifecycle["programmeEvidenceSnapshot"]["orderedLogicalTargets"][1]["readySingleReview"]["path"] = "wrong.json"
        self.write_snapshot_lifecycle(lifecycle)
        self.assert_contract_error(
            lambda: contract.validate_programme_evidence_snapshot(
                self.root, state, contract.ORIGINAL_META01), "unique current review leaf"
        )

    def test_snapshot_rejects_wrong_review_hash(self) -> None:
        state, lifecycle = self.snapshot_fixture()
        lifecycle["programmeEvidenceSnapshot"]["orderedLogicalTargets"][1]["readySingleReview"]["rawSha256"] = "0" * 64
        self.write_snapshot_lifecycle(lifecycle)
        self.assert_contract_error(
            lambda: contract.validate_programme_evidence_snapshot(
                self.root, state, contract.ORIGINAL_META01), "readySingleReview raw SHA-256 drift"
        )

    def test_snapshot_rejects_changed_receipt_bytes(self) -> None:
        state, lifecycle = self.snapshot_fixture()
        binding = lifecycle["programmeEvidenceSnapshot"]["orderedLogicalTargets"][1]["authoringReceipt"]
        path = self.root / binding["path"]
        write(path, path.read_text() + "\n")
        self.assert_contract_error(
            lambda: contract.validate_programme_evidence_snapshot(
                self.root, state, contract.ORIGINAL_META01), "authoringReceipt raw SHA-256 drift"
        )

    def test_snapshot_rejects_changed_review_bytes(self) -> None:
        state, lifecycle = self.snapshot_fixture()
        binding = lifecycle["programmeEvidenceSnapshot"]["orderedLogicalTargets"][1]["readySingleReview"]
        path = self.root / binding["path"]
        write(path, path.read_text() + "\n")
        self.assert_contract_error(
            lambda: contract.validate_programme_evidence_snapshot(
                self.root, state, contract.ORIGINAL_META01), "readySingleReview raw SHA-256 drift"
        )

    def test_snapshot_rejects_non_ready_review(self) -> None:
        state, lifecycle = self.snapshot_fixture()
        binding = lifecycle["programmeEvidenceSnapshot"]["orderedLogicalTargets"][1]["readySingleReview"]
        path = self.root / binding["path"]
        review = contract.load_json(path, "review")
        review["status"] = "NeedsRemediation"
        write(path, json.dumps(review) + "\n")
        binding["rawSha256"] = contract.raw_sha256(path)
        self.write_snapshot_lifecycle(lifecycle)
        self.assert_contract_error(
            lambda: contract.validate_programme_evidence_snapshot(
                self.root, state, contract.ORIGINAL_META01), "not Single/Primary/Ready"
        )

    def test_snapshot_rejects_non_unique_review_leaf(self) -> None:
        state, _ = self.snapshot_fixture()
        original = self.root / "specs/intake-review-results/meta-lh-02.json"
        duplicate = self.root / "specs/intake-review-results/meta-lh-02-duplicate.json"
        write(duplicate, original.read_text())
        self.assert_contract_error(
            lambda: contract.validate_programme_evidence_snapshot(
                self.root, state, contract.ORIGINAL_META01), "exactly one non-superseded"
        )

    def test_snapshot_rejects_wrong_branch(self) -> None:
        state, lifecycle = self.snapshot_fixture()
        state["branch"] = "wrong-branch"
        lifecycle["records"][0]["branch"] = "wrong-branch"
        lifecycle["programmeEvidenceSnapshot"]["branch"] = "wrong-branch"
        write(self.root / contract.STATE, json.dumps(state) + "\n")
        self.write_snapshot_lifecycle(lifecycle)
        self.assert_contract_error(
            lambda: contract.validate_input_bindings(self.root, "bash"),
            "accepted feature runId or branch",
        )

    def test_snapshot_rejects_wrong_run(self) -> None:
        state, lifecycle = self.snapshot_fixture()
        state["runId"] = "00000000-0000-4000-8000-000000000000"
        lifecycle["records"][0]["runId"] = state["runId"]
        lifecycle["programmeEvidenceSnapshot"]["runId"] = state["runId"]
        write(self.root / contract.STATE, json.dumps(state) + "\n")
        self.write_snapshot_lifecycle(lifecycle)
        self.assert_contract_error(
            lambda: contract.validate_input_bindings(self.root, "bash"),
            "accepted feature runId or branch",
        )

    def test_snapshot_rejects_wrong_lifecycle_binding(self) -> None:
        state, _ = self.snapshot_fixture()
        state["acceptedArtifactLifecycle"]["schemaVersion"] = "1.0"
        write(self.root / contract.STATE, json.dumps(state) + "\n")
        self.assert_contract_error(
            lambda: contract.validate_input_bindings(self.root, "bash"),
            "schema-1.1 contract",
        )

    def test_missing_review_evidence(self) -> None:
        expected = self.root / "expected.txt"
        write(expected, "one.md\n")
        rows = []
        for path in contract.REVIEW_PATHS[:-1]:
            rows.append({"path": path, "criteria": {key: "Pass" for key in contract.SEMANTIC_CRITERIA}, "rationale": "Reviewed."})
        evidence = self.root / "review.json"
        write(evidence, json.dumps({"schemaVersion": "1.0", "reviewer": {"independent": True, "role": "Reviewer", "independenceStatement": "Independent."}, "semanticReviews": rows, "blockingFindings": []}))
        self.assert_contract_error(lambda: contract.validate_review_evidence(self.root, evidence, expected, "semantic"), "path coverage")

    def test_accessibility_evidence_needs_exact_criteria(self) -> None:
        expected = self.root / "expected.txt"
        write(expected, "unused.md\n")
        rows = []
        for path in contract.REVIEW_PATHS:
            criteria = {key: "Pass" for key in contract.ACCESSIBILITY_CRITERIA}
            criteria.pop("statusNotColorOnly")
            rows.append({"path": path, "criteria": criteria, "rationale": "Reviewed."})
        evidence = self.root / "accessibility.json"
        write(evidence, json.dumps({
            "schemaVersion": "1.0",
            "reviewer": {"independent": True, "role": "A11Y Reviewer", "independenceStatement": "Independent."},
            "accessibilityReviews": rows,
            "blockingFindings": [],
        }))
        self.assert_contract_error(
            lambda: contract.validate_review_evidence(self.root, evidence, expected, "accessibility"),
            "criteria must contain exactly",
        )

    def test_multiple_documentation_impact_entries(self) -> None:
        expected = self.root / "expected.txt"
        write(expected, "one.md\n")
        evidence = self.root / "documentation.json"
        write(evidence, json.dumps({"schemaVersion": "1.1", "entries": [{}, {}]}))
        self.assert_contract_error(lambda: contract.validate_documentation_impact(self.root, evidence, expected), "exactly one entry")

    def test_invalid_aeps_dual_outcome(self) -> None:
        receipt = self.root / "aeps.md"
        invalid = {
            "schemaVersion": "1.0", "outcome": "FindingAndNoChange", "trigger": "Review",
            "capturedAt": "2026-08-09", "sourcePath": contract.DOMAIN_PATHS[0],
            "sourceSha256": "0" * 64, "deduplicationKey": "review+target+hash",
            "rationale": "A dual outcome is forbidden.", "maturity": "observation",
            "presetPromotion": False, "level0Handoff": False,
        }
        write(receipt, "```aeps-outcome-json\n" + json.dumps(invalid) + "\n```\n")
        self.assert_contract_error(lambda: contract.validate_aeps(self.root, receipt), "Finding or NoChange")

    def test_aeps_finding_needs_complete_ledger_section(self) -> None:
        source_path = contract.DOMAIN_PATHS[0]
        source = self.root / source_path
        receipt = self.root / "docs/aeps/receipts/finding.md"
        captured = "2026-08-09"
        outcome = {
            "schemaVersion": "1.0", "outcome": "Finding", "trigger": "ImplementationReceipt",
            "capturedAt": captured, "sourcePath": source_path,
            "sourceSha256": contract.raw_sha256(source),
            "deduplicationKey": f"{source_path} + {contract.normalized_sha256(source)} + {captured}",
            "rationale": "A reviewed observation.", "maturity": "observation",
            "presetPromotion": False, "level0Handoff": False,
            "findingId": "AEPS-FIND-AOC-999",
        }
        write(receipt, "```aeps-outcome-json\n" + json.dumps(outcome) + "\n```\n")
        write(self.root / "docs/aeps/findings-ledger.md", (
            "## AEPS-FIND-AOC-999 – Incomplete\n\n"
            f"- Quelle / Source: `{source_path}`; `docs/aeps/receipts/finding.md`.\n"
        ))
        self.assert_contract_error(
            lambda: contract.validate_aeps(self.root, receipt),
            "ledger section missing required field",
        )

    def test_aeps_finding_rejects_present_labels_with_empty_values(self) -> None:
        finding = "AEPS-FIND-AOC-999"
        source = contract.DOMAIN_PATHS[0]
        receipt = "docs/aeps/receipts/finding.md"
        ledger = f"""## {finding} – Empty skeleton

- **Quelle und Lastenheft / Source and intake:** `{source}`; `{receipt}`.
- **Datum und Repository-Commit / Date and commit:**
- **Problem oder Beobachtung / Problem or observation:**
- **Kontext und Randbedingungen / Context and constraints:**
- **Positive Evidence:**
- **Negative Evidence:**
- **Grenzen / Limits:**
- **AOC-spezifisch versus generisch / AOC-specific versus generic:**
- **AEPS-Domäne / AEPS Domain:**
- **Reifegrad / Maturity:**
- **Preset-Bezug / Related presets:**
- **Nächste Validierung / Next validation:**
- **Promotion-Blocker / Promotion blockers:**
- **Erfassungsstatus / Capture status:** `NotRecorded`.
- **Upstream-Status / Upstream status:** `PendingPublication`.
"""
        self.assert_contract_error(
            lambda: contract.validate_aeps_ledger_section(
                ledger, finding, source, receipt, "observation"
            ),
            "empty required value: date and commit",
        )

    def canonical_aeps_ledger(self, *, maturity: str = "observation",
                              capture: str = "NotRecorded",
                              upstream: str = "PendingPublication",
                              source_suffix: str = "",
                              receipt_suffix: str = "",
                              source_extra_token: str = "",
                              maturity_extra_token: str = "",
                              capture_extra_token: str = "",
                              date_and_commit: str | None = None,
                              related_presets: str | None = None) -> tuple[str, str, str, str]:
        finding = "AEPS-FIND-AOC-999"
        source = contract.DOMAIN_PATHS[0]
        receipt = "docs/aeps/receipts/finding.md"
        source_extra = f"; `{source_extra_token}`" if source_extra_token else ""
        maturity_extra = f"; `{maturity_extra_token}`" if maturity_extra_token else ""
        capture_extra = f"; `{capture_extra_token}`" if capture_extra_token else ""
        date_value = date_and_commit or (
            f"`2026-08-09`; `PendingPublication`; Base-HEAD "
            f"`0123456789012345678901234567890123456789`; SHA-256 `{'0' * 64}`."
        )
        preset_value = related_presets or (
            "`N/A`, because this fixture validates the receipt contract."
        )
        ledger = f"""## {finding} – Contract fixture

- **Quelle und Lastenheft / Source and intake:** `{source}{source_suffix}`; `{receipt}{receipt_suffix}`{source_extra}.
- **Datum und Repository-Commit / Date and commit:** {date_value}
- **Problem oder Beobachtung / Problem or observation:** A reproducible observation.
- **Kontext und Randbedingungen / Context and constraints:** Level-2 documentation workflow.
- **Positive Evidence:** The named contract passes.
- **Negative Evidence:** The named adversarial fixture fails closed.
- **Grenzen / Limits:** No product implementation or promotion.
- **AOC-spezifisch versus generisch / AOC-specific versus generic:** Paths are AOC-specific; the validation property is generic.
- **AEPS-Domäne / AEPS Domain:** Review and Evidence.
- **Reifegrad / Maturity:** `{maturity}`{maturity_extra}.
- **Preset-Bezug / Related presets:** {preset_value}
- **Nächste Validierung / Next validation:** Repeat in an independent project.
- **Promotion-Blocker / Promotion blockers:** Cross-project evidence remains open.
- **Erfassungsstatus / Capture status:** `{capture}`{capture_extra}.
- **Upstream-Status / Upstream status:** `{upstream}`.
"""
        return ledger, finding, source, receipt

    def test_aeps_finding_accepts_exact_canonical_fields(self) -> None:
        ledger, finding, source, receipt = self.canonical_aeps_ledger()
        contract.validate_aeps_ledger_section(
            ledger, finding, source, receipt, "observation"
        )

    def test_aeps_finding_rejects_suffixed_status_tokens(self) -> None:
        ledger, finding, source, receipt = self.canonical_aeps_ledger(
            capture="NotRecordedness", upstream="PendingPublicationLater"
        )
        self.assert_contract_error(
            lambda: contract.validate_aeps_ledger_section(
                ledger, finding, source, receipt, "observation"
            ),
            "valid capture status",
        )

    def test_aeps_finding_rejects_suffixed_maturity_token(self) -> None:
        ledger, finding, source, receipt = self.canonical_aeps_ledger(
            maturity="observation-ish"
        )
        self.assert_contract_error(
            lambda: contract.validate_aeps_ledger_section(
                ledger, finding, source, receipt, "observation"
            ),
            "maturity must match",
        )

    def test_aeps_finding_rejects_suffixed_path_tokens(self) -> None:
        ledger, finding, source, receipt = self.canonical_aeps_ledger(
            source_suffix=".bak", receipt_suffix=".bak"
        )
        self.assert_contract_error(
            lambda: contract.validate_aeps_ledger_section(
                ledger, finding, source, receipt, "observation"
            ),
            "bind both sourcePath and receipt path",
        )

    def test_aeps_finding_rejects_duplicate_or_extra_capture_tokens(self) -> None:
        for extra in ("NotRecorded", "BogusStatus"):
            ledger, finding, source, receipt = self.canonical_aeps_ledger(
                capture_extra_token=extra
            )
            self.assert_contract_error(
                lambda ledger=ledger: contract.validate_aeps_ledger_section(
                    ledger, finding, source, receipt, "observation"
                ),
                "valid capture status",
            )

    def test_aeps_finding_rejects_extra_maturity_token(self) -> None:
        ledger, finding, source, receipt = self.canonical_aeps_ledger(
            maturity_extra_token="candidate"
        )
        self.assert_contract_error(
            lambda: contract.validate_aeps_ledger_section(
                ledger, finding, source, receipt, "observation"
            ),
            "maturity must match",
        )

    def test_aeps_finding_rejects_extra_source_token(self) -> None:
        ledger, finding, source, receipt = self.canonical_aeps_ledger(
            source_extra_token="requirements/foreign.md"
        )
        self.assert_contract_error(
            lambda: contract.validate_aeps_ledger_section(
                ledger, finding, source, receipt, "observation"
            ),
            "bind both sourcePath and receipt path",
        )

    def test_aeps_finding_rejects_malformed_date_commit_binding(self) -> None:
        ledger, finding, source, receipt = self.canonical_aeps_ledger(
            date_and_commit="arbitrary."
        )
        self.assert_contract_error(
            lambda: contract.validate_aeps_ledger_section(
                ledger, finding, source, receipt, "observation"
            ),
            "published commit or PendingPublication evidence",
        )

    def test_aeps_finding_rejects_impossible_calendar_date(self) -> None:
        ledger, finding, source, receipt = self.canonical_aeps_ledger(
            date_and_commit=(
                f"`2026-99-99`; `PendingPublication`; Base-HEAD "
                f"`0123456789012345678901234567890123456789`; SHA-256 `{'0' * 64}`."
            )
        )
        self.assert_contract_error(
            lambda: contract.validate_aeps_ledger_section(
                ledger, finding, source, receipt, "observation"
            ),
            "published commit or PendingPublication evidence",
        )

    def test_aeps_finding_rejects_unjustified_na_preset_relation(self) -> None:
        ledger, finding, source, receipt = self.canonical_aeps_ledger(
            related_presets="`N/A`."
        )
        self.assert_contract_error(
            lambda: contract.validate_aeps_ledger_section(
                ledger, finding, source, receipt, "observation"
            ),
            "N/A preset relation needs an explicit rationale",
        )

    def test_aeps_finding_rejects_plain_or_empty_na_rationales(self) -> None:
        for value in ("N/A.", "N/A, because.", "`N/A`, because.", "`N/A`, weil."):
            ledger, finding, source, receipt = self.canonical_aeps_ledger(
                related_presets=value
            )
            self.assert_contract_error(
                lambda ledger=ledger: contract.validate_aeps_ledger_section(
                    ledger, finding, source, receipt, "observation"
                ),
                "N/A preset relation needs an explicit rationale",
            )

    def test_unexpected_staged_path(self) -> None:
        self.assert_contract_error(
            lambda: contract.validate_candidate_inventory({"expected.md"}, [("A ", "foreign.md")],
                                                          {"expected.md"}, {"expected.md"}),
            "unexpected staged path",
        )

    def test_candidate_fixpoint_detects_late_path(self) -> None:
        self.assert_contract_error(
            lambda: contract.validate_candidate_fixpoint_inventory(
                [("??", "one.md")], {"one.md", "late.md"}, {"one.md", "late.md"},
            ),
            "candidate fixed point differs",
        )

    def test_nonrequired_failed_check_blocks(self) -> None:
        all_checks = self.root / "all-checks.json"
        required = self.root / "required-checks.json"
        write(all_checks, json.dumps([
            {"name": "required", "link": "https://example.invalid/1", "bucket": "pass"},
            {"name": "advisory", "link": "https://example.invalid/2", "bucket": "fail"},
        ]))
        write(required, json.dumps([
            {"name": "required", "link": "https://example.invalid/1", "bucket": "pass"},
        ]))
        self.assert_contract_error(
            lambda: contract.validate_check_inventory(all_checks, required),
            "non-successful check",
        )

    def test_causal_closeout_accepts_complete_transaction(self) -> None:
        causal_closeout_fixture(self.root)
        self.assertIn("66/66 tasks", contract.validate_causal_closeout(self.root))
        requirements_path = Path(__file__).resolve().parents[1] / "autonomous-run-gate-requirements.json"
        requirements = json.loads(requirements_path.read_text(encoding="utf-8"))
        not_applicable = [
            gate for gate in requirements["gates"] if gate["applicability"] == "N/A"
        ]
        self.assertTrue(not_applicable)
        self.assertTrue(all(gate["requiredCommandTokens"] == [] for gate in not_applicable))
        self.assertTrue(all(gate["requiredRunnerOrPlatformTokens"] == [] for gate in not_applicable))

    def test_causal_closeout_rejects_unchecked_task(self) -> None:
        causal_closeout_fixture(self.root)
        tasks = self.root / contract.TASKS
        write(tasks, tasks.read_text().replace("- [x] T066", "- [ ] T066", 1))
        self.assert_contract_error(
            lambda: contract.validate_causal_closeout(self.root), "exactly 66 checked tasks"
        )

    def test_causal_closeout_rejects_task_hash_drift(self) -> None:
        state, _ = causal_closeout_fixture(self.root)
        state["tasks"]["sha256"] = "0" * 64
        write(self.root / contract.STATE, json.dumps(state) + "\n")
        self.assert_contract_error(
            lambda: contract.validate_causal_closeout(self.root), "tasks SHA-256 differs"
        )

    def test_causal_closeout_rejects_nonterminal_state(self) -> None:
        state, _ = causal_closeout_fixture(self.root)
        state["status"] = "Active"
        write(self.root / contract.STATE, json.dumps(state) + "\n")
        self.assert_contract_error(
            lambda: contract.validate_causal_closeout(self.root), "Completed status"
        )

    def test_causal_closeout_rejects_allowlist_drift(self) -> None:
        _, evidence = causal_closeout_fixture(self.root)
        evidence["closeoutPaths"].append("unexpected.md")
        write(self.root / contract.CAUSAL_CLOSEOUT, json.dumps(evidence) + "\n")
        self.assert_contract_error(
            lambda: contract.validate_causal_closeout(self.root), "exact three-path allowlist"
        )

    def test_causal_closeout_rejects_incomplete_reviews(self) -> None:
        _, evidence = causal_closeout_fixture(self.root)
        evidence["documentationReview"]["reviewedPaths"].pop()
        write(self.root / contract.CAUSAL_CLOSEOUT, json.dumps(evidence) + "\n")
        self.assert_contract_error(
            lambda: contract.validate_causal_closeout(self.root),
            "exact three-path closeout delta",
        )

    def test_causal_closeout_rejects_self_reference(self) -> None:
        _, evidence = causal_closeout_fixture(self.root)
        evidence["nonSelfReferentialBoundary"]["closeoutPullRequest"] = 456
        write(self.root / contract.CAUSAL_CLOSEOUT, json.dumps(evidence) + "\n")
        self.assert_contract_error(
            lambda: contract.validate_causal_closeout(self.root),
            "must not claim its own closeoutPullRequest",
        )


def main() -> int:
    stream = io.StringIO()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ContractNegativeTests)
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    if not result.wasSuccessful():
        sys.stderr.write(stream.getvalue())
        return 1
    print(f"PASS: contract-tests: {result.testsRun} isolated positive/negative cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
