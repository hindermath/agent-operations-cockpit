#!/usr/bin/env python3
"""Focused positive and fail-closed tests for the Feature-003 evidence bridge."""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import validate_current_evidence_binding as contract


REPO = Path(__file__).resolve().parents[3]


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


class CurrentEvidenceBindingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.accepted = contract.require_immutable_predecessor(REPO)
        cls.real_git_blob = staticmethod(contract.git_blob)

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="meta-lh03-binding-tests-")
        self.root = Path(self.temporary.name)
        for relative in (
            "requirements/intakes/active",
            "specs/intake-authoring-receipts",
            "specs/intake-review-requests",
            "specs/intake-review-results",
            "specs/intake-authoring-archive",
            "docs/reviews",
        ):
            shutil.copytree(REPO / relative, self.root / relative)
        for relative in (
            contract.MANIFEST,
            contract.AUTHORITY,
            ".specify/presets/intake-authoring-governance/preset.yml",
        ):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO / relative, target)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def validate_fixture(self) -> str:
        with mock.patch.object(
                contract, "require_immutable_predecessor", return_value=self.accepted), mock.patch.object(
                contract, "git_blob",
                side_effect=lambda _root, revision, relative: self.real_git_blob(REPO, revision, relative)):
            return contract.validate_manifest(self.root, runner=lambda *_args: None)

    def manifest(self) -> dict:
        return json.loads((self.root / contract.MANIFEST).read_text(encoding="utf-8"))

    def save_manifest(self, value: dict) -> None:
        write_json(self.root / contract.MANIFEST, value)

    def replace_current_binding_hash(self, logical_id: str, kind: str, digest: str) -> None:
        manifest = self.manifest()
        field = "normalizedSha256" if kind == "target" else "rawSha256"
        for entry in manifest["orderedLogicalTargets"]:
            if entry["logicalTargetId"] == logical_id:
                entry[kind][field] = digest
        for entry in manifest["renewedLogicalTargets"]:
            if entry["logicalTargetId"] == logical_id:
                entry["current"][kind][field] = digest
        self.save_manifest(manifest)

    def assert_rejected(self, expected: str) -> None:
        with self.assertRaisesRegex(contract.ContractError, expected):
            self.validate_fixture()

    def test_bash_and_powershell_entrypoints_have_exact_parity(self) -> None:
        commands = (
            ["bash", str(REPO / contract.FEATURE / "contracts/validate-current-evidence-binding.sh"),
             "--repo", str(REPO), "--", "current-evidence"],
            ["pwsh", "-NoProfile", "-File",
             str(REPO / contract.FEATURE / "contracts/validate-current-evidence-binding.ps1"),
             "-Repo", str(REPO), "-Mode", "current-evidence"],
        )
        for command in commands:
            with self.subTest(surface=command[0]):
                result = subprocess.run(command, text=True, capture_output=True, check=False)
                self.assertEqual(0, result.returncode, result.stderr)
                self.assertEqual(f"{contract.PASS_MESSAGE}\n", result.stdout)
                self.assertEqual("", result.stderr)

    def test_isolated_current_projection_passes(self) -> None:
        self.assertEqual(self.validate_fixture(), contract.PASS_MESSAGE)

    def test_rejects_fixed_order_drift(self) -> None:
        manifest = self.manifest()
        manifest["orderedLogicalTargets"][7], manifest["orderedLogicalTargets"][8] = (
            manifest["orderedLogicalTargets"][8], manifest["orderedLogicalTargets"][7]
        )
        self.save_manifest(manifest)
        self.assert_rejected("exact fixed 14-target order")

    def test_rejects_bounded_authority_hash_drift(self) -> None:
        with (self.root / contract.AUTHORITY).open("a", encoding="utf-8") as stream:
            stream.write("drift\n")
        self.assert_rejected("bounded authority raw SHA-256 drift")

    def test_rejects_additional_grant(self) -> None:
        manifest = self.manifest()
        manifest["authorityBinding"]["grants"] = ["Bypass"]
        self.save_manifest(manifest)
        self.assert_rejected("exceeds the exact bounded repair scope")

    def test_rejects_historical_archive_byte_drift(self) -> None:
        historical = self.manifest()["renewedLogicalTargets"][0]["historical"]
        with (self.root / historical["authoringReceipt"]["archivePath"]).open("ab") as stream:
            stream.write(b"drift")
        self.assert_rejected("historical receipt archive differs from exact Git")

    def test_rejects_pending_new_review_even_when_manifest_hash_is_current(self) -> None:
        manifest = self.manifest()
        renewal = manifest["renewedLogicalTargets"][0]
        review_path = self.root / renewal["current"]["readySingleReview"]["path"]
        review = json.loads(review_path.read_text(encoding="utf-8"))
        review["status"] = "NeedsClarification"
        write_json(review_path, review)
        digest = hashlib.sha256(review_path.read_bytes()).hexdigest()
        self.replace_current_binding_hash(renewal["logicalTargetId"], "readySingleReview", digest)
        self.assert_rejected("not current Single/Primary/Ready")

    def test_rejects_duplicate_current_review_leaf(self) -> None:
        review = self.manifest()["renewedLogicalTargets"][0]["current"]["readySingleReview"]["path"]
        shutil.copy2(self.root / review, self.root / "specs/intake-review-results/duplicate-current-leaf.json")
        self.assert_rejected("exactly one current Single review leaf")

    def test_rejects_dangling_and_cross_target_review_lineage(self) -> None:
        manifest = self.manifest()
        first = manifest["renewedLogicalTargets"][0]["current"]["readySingleReview"]["path"]
        second = manifest["renewedLogicalTargets"][1]["current"]["readySingleReview"]["path"]
        for predecessor, expected in (("specs/intake-review-results/missing.json", "dangling"),
                                      (second, "cross-target")):
            with self.subTest(expected=expected):
                review = json.loads((self.root / first).read_text(encoding="utf-8"))
                review["supersedes"] = predecessor
                write_json(self.root / first, review)
                with self.assertRaisesRegex(contract.ContractError, expected):
                    contract.current_reviews(self.root)

    def test_rejects_malformed_single_review(self) -> None:
        review_path = self.root / "specs/intake-review-results/malformed-single.json"
        write_json(review_path, {"mode": "Single", "targets": []})
        with self.assertRaisesRegex(contract.ContractError, "malformed Single review target"):
            contract.current_reviews(self.root)

    def test_rejects_missing_or_unknown_review_mode(self) -> None:
        review_path = self.root / "specs/intake-review-results/unknown-mode.json"
        for mode in (None, "AdHoc"):
            with self.subTest(mode=mode):
                value = {"targets": []}
                if mode is not None:
                    value["mode"] = mode
                write_json(review_path, value)
                with self.assertRaisesRegex(contract.ContractError, "missing or unsupported mode"):
                    contract.current_reviews(self.root)

    def test_rejects_cyclic_review_lineage(self) -> None:
        review_dir = self.root / "specs/intake-review-results"
        target = "requirements/not-in-programme.md"
        first = review_dir / "cycle-a.json"
        second = review_dir / "cycle-b.json"
        write_json(first, {"mode": "Single", "targets": [{"path": target}],
                           "supersedes": second.relative_to(self.root).as_posix()})
        write_json(second, {"mode": "Single", "targets": [{"path": target}],
                            "supersedes": first.relative_to(self.root).as_posix()})
        with self.assertRaisesRegex(contract.ContractError, "cyclic Single review"):
            contract.current_reviews(self.root)

    def test_rejects_current_receipt_source_or_target_freshness_drift(self) -> None:
        renewal = self.manifest()["renewedLogicalTargets"][0]
        receipt_path = self.root / renewal["current"]["authoringReceipt"]["path"]
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        receipt["target"]["normalizedSha256"] = "0" * 64
        write_json(receipt_path, receipt)
        digest = hashlib.sha256(receipt_path.read_bytes()).hexdigest()
        self.replace_current_binding_hash(renewal["logicalTargetId"], "authoringReceipt", digest)
        self.assert_rejected("not ReadyForReview for the current target")

    def test_rejects_unapproved_meta03_target_content(self) -> None:
        target = self.root / dict(contract.PROGRAMME_TARGETS)["META-LH-03"]
        with target.open("a", encoding="utf-8") as stream:
            stream.write("unapproved\n")
        target_digest = contract.normalized_sha(target)
        self.replace_current_binding_hash("META-LH-03", "target", target_digest)
        renewal = next(
            item for item in self.manifest()["renewedLogicalTargets"]
            if item["logicalTargetId"] == "META-LH-03"
        )
        receipt_path = self.root / renewal["current"]["authoringReceipt"]["path"]
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        receipt["target"]["normalizedSha256"] = target_digest
        write_json(receipt_path, receipt)
        old_receipt_digest = renewal["current"]["authoringReceipt"]["rawSha256"]
        receipt_digest = hashlib.sha256(receipt_path.read_bytes()).hexdigest()
        self.replace_current_binding_hash("META-LH-03", "authoringReceipt", receipt_digest)
        review_path = self.root / renewal["current"]["readySingleReview"]["path"]
        review = json.loads(review_path.read_text(encoding="utf-8"))
        review["targets"][0]["normalizedSha256"] = target_digest
        write_json(review_path, review)
        self.replace_current_binding_hash(
            "META-LH-03", "readySingleReview", hashlib.sha256(review_path.read_bytes()).hexdigest()
        )
        report_path = self.root / renewal["current"]["readySingleReviewReport"]["path"]
        report_path.write_text(
            report_path.read_text(encoding="utf-8").replace(old_receipt_digest, receipt_digest),
            encoding="utf-8",
        )
        self.replace_current_binding_hash(
            "META-LH-03", "readySingleReviewReport",
            hashlib.sha256(report_path.read_bytes()).hexdigest(),
        )
        self.assert_rejected("exceeds the exact 0.3.0 to 0.3.1 replacement")

    def test_rejects_canonical_series_checkout_drift(self) -> None:
        relative = "requirements/intakes/series/order.md"
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(b"changed\n")
        accepted = b"accepted\n"
        completed = subprocess.CompletedProcess(args=[], returncode=0)
        with mock.patch.object(contract, "git_blob", return_value=accepted), mock.patch.object(
                contract.subprocess, "run", return_value=completed):
            with self.assertRaisesRegex(contract.ContractError, "accepted historical checkout drift"):
                contract.require_clean_accepted_file(self.root, relative)

    def test_rejects_symlinked_historical_archive(self) -> None:
        historical = self.manifest()["renewedLogicalTargets"][0]["historical"]
        archive = self.root / historical["authoringReceipt"]["archivePath"]
        replacement = archive.with_name("outside-copy.json")
        shutil.copy2(archive, replacement)
        archive.unlink()
        archive.symlink_to(replacement)
        self.assert_rejected("must not contain symlink components")

    def test_external_validator_success_must_be_exact(self) -> None:
        accepted = subprocess.CompletedProcess(
            args=[], returncode=0, stdout="PASS: exact\n", stderr="",
        )
        with mock.patch.object(contract.subprocess, "run", return_value=accepted):
            contract.run_checked(["validator"], self.root, "surface", "PASS: exact")
        for stdout, stderr in (("PASS: exact\nextra\n", ""), ("PASS: exact\n", "warning\n")):
            with self.subTest(stdout=stdout, stderr=stderr), mock.patch.object(
                    contract.subprocess, "run",
                    return_value=subprocess.CompletedProcess(
                        args=[], returncode=0, stdout=stdout, stderr=stderr,
                    )):
                with self.assertRaisesRegex(contract.ContractError, "invalid success result"):
                    contract.run_checked(["validator"], self.root, "surface", "PASS: exact")

    def test_bash_and_powershell_reject_missing_or_invalid_mode(self) -> None:
        scripts = (
            ["bash", str(REPO / contract.FEATURE / "contracts/validate-current-evidence-binding.sh")],
            ["pwsh", "-NoProfile", "-File",
             str(REPO / contract.FEATURE / "contracts/validate-current-evidence-binding.ps1")],
        )
        for script in scripts:
            for suffix in ([], ["invalid-mode"]):
                with self.subTest(surface=script[0], suffix=suffix):
                    result = subprocess.run(script + suffix, text=True, capture_output=True, check=False)
                    self.assertEqual(2, result.returncode)
                    self.assertIn("exactly one mode, current-evidence, is required", result.stderr)

    def test_rejects_duplicate_operation_id_or_receipt_operation_collision(self) -> None:
        manifest = self.manifest()
        renewals = manifest["renewedLogicalTargets"]
        first_path = self.root / renewals[0]["current"]["authoringReceipt"]["path"]
        second_path = self.root / renewals[1]["current"]["authoringReceipt"]["path"]
        first = json.loads(first_path.read_text(encoding="utf-8"))
        for operation_id in (first["operation"]["operationId"], None):
            with self.subTest(operation_id=operation_id):
                second = json.loads(second_path.read_text(encoding="utf-8"))
                second["operation"]["operationId"] = operation_id or second["receiptId"]
                write_json(second_path, second)
                digest = hashlib.sha256(second_path.read_bytes()).hexdigest()
                self.replace_current_binding_hash(
                    renewals[1]["logicalTargetId"], "authoringReceipt", digest
                )
                self.assert_rejected("renewed receipt identity")

    def test_rejects_review_report_hash_or_identity_drift(self) -> None:
        renewal = self.manifest()["renewedLogicalTargets"][0]
        report_path = self.root / renewal["current"]["readySingleReviewReport"]["path"]
        with report_path.open("a", encoding="utf-8") as stream:
            stream.write("drift\n")
        self.assert_rejected("readySingleReviewReport raw SHA-256 drift")

    def test_rejects_review_report_identity_drift_with_current_manifest_hash(self) -> None:
        renewal = self.manifest()["renewedLogicalTargets"][0]
        logical_id = renewal["logicalTargetId"]
        report_path = self.root / renewal["current"]["readySingleReviewReport"]["path"]
        receipt_path = self.root / renewal["current"]["authoringReceipt"]["path"]
        receipt_id = json.loads(receipt_path.read_text(encoding="utf-8"))["receiptId"]
        report_path.write_text(
            report_path.read_text(encoding="utf-8").replace(receipt_id, "0" * 36),
            encoding="utf-8",
        )
        digest = hashlib.sha256(report_path.read_bytes()).hexdigest()
        self.replace_current_binding_hash(logical_id, "readySingleReviewReport", digest)
        self.assert_rejected("does not bind current review and receipt identity")

    def test_ancestry_distinguishes_not_ancestor_and_execution_error(self) -> None:
        for returncode, expected in ((1, "not a descendant"), (2, "could not be checked")):
            with self.subTest(returncode=returncode), mock.patch.object(
                    contract.subprocess, "run",
                    return_value=subprocess.CompletedProcess(args=[], returncode=returncode)):
                with self.assertRaisesRegex(contract.ContractError, expected):
                    contract.require_ancestor(self.root)

    def test_ancestry_rejects_process_start_error(self) -> None:
        with mock.patch.object(contract.subprocess, "run", side_effect=OSError("unavailable")):
            with self.assertRaisesRegex(contract.ContractError, "could not be checked"):
                contract.require_ancestor(self.root)


if __name__ == "__main__":
    unittest.main()
