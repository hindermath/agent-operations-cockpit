#!/usr/bin/env python3
"""Validate the additive META-LH-03 authoring-contract bridge.

The validator is repository-local and read-only.  It proves the historical
repair checkpoint directly from Git and rejects any current binding in which a
logical target other than META-LH-03 changes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


class ContractViolation(ValueError):
    """Raised when the bounded authoring contract is not satisfied."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ContractViolation(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(file_path: Path) -> dict[str, Any]:
    try:
        raw = file_path.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            raw = raw[3:]
        text = raw.decode("utf-8", errors="strict")
        if "\x00" in text:
            raise ContractViolation(f"binary NUL in JSON: {file_path}")
        value = json.loads(text, object_pairs_hook=_unique_object)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ContractViolation(f"cannot read strict JSON {file_path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ContractViolation(f"JSON root must be an object: {file_path}")
    return value


def load_json_bytes(raw: bytes, label: str) -> dict[str, Any]:
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]
    try:
        text = raw.decode("utf-8", errors="strict")
        if "\x00" in text:
            raise ContractViolation(f"binary NUL in JSON: {label}")
        value = json.loads(text, object_pairs_hook=_unique_object)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ContractViolation(f"cannot read strict JSON {label}: {exc}") from exc
    if not isinstance(value, dict):
        raise ContractViolation(f"JSON root must be an object: {label}")
    return value


def normalized_sha256(raw: bytes) -> str:
    """Return the strict UTF-8, BOM-free, LF-normalized SHA-256."""
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeError as exc:
        raise ContractViolation(f"invalid UTF-8: {exc}") from exc
    if "\x00" in text:
        raise ContractViolation("binary NUL in text input")
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def _git(repo: Path, *arguments: str, binary: bool = False) -> bytes | str:
    result = subprocess.run(
        ["git", "-C", str(repo), *arguments],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        message = result.stderr.decode("utf-8", errors="replace").strip()
        raise ContractViolation(f"git {' '.join(arguments)} failed: {message}")
    if binary:
        return result.stdout
    return result.stdout.decode("utf-8", errors="strict").strip()


def validate_checkpoint(repo: Path, manifest_path: Path) -> dict[str, Any]:
    manifest = load_json(manifest_path)
    repair_commit = str(manifest.get("repairCommit", ""))
    repair_tree = str(manifest.get("repairTree", ""))
    items = manifest.get("candidatePaths")
    if manifest.get("schemaVersion") != "1.0":
        raise ContractViolation("checkpoint manifest schemaVersion must be 1.0")
    if manifest.get("manifestCreatedAfterCheckpoint") is not True:
        raise ContractViolation("manifest must state that it was created after the checkpoint")
    if manifest.get("manifestExpectedInsideCheckpoint") is not False:
        raise ContractViolation("manifest must not claim presence inside the checkpoint")
    if not isinstance(items, list) or manifest.get("candidatePathCount") != len(items):
        raise ContractViolation("checkpoint candidate path count mismatch")
    if len(items) != 48:
        raise ContractViolation("checkpoint must bind exactly 48 paths")
    if _git(repo, "show", "-s", "--format=%T", repair_commit) != repair_tree:
        raise ContractViolation("repair checkpoint tree mismatch")

    ancestry = subprocess.run(
        ["git", "-C", str(repo), "merge-base", "--is-ancestor", repair_commit, "HEAD"],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )
    if ancestry.returncode != 0:
        raise ContractViolation("repair checkpoint is not an ancestor of HEAD")

    seen: set[str] = set()
    for item in items:
        if not isinstance(item, dict):
            raise ContractViolation("checkpoint path entry must be an object")
        relative = item.get("path")
        expected_hash = item.get("rawSha256")
        if not isinstance(relative, str) or not relative or relative in seen:
            raise ContractViolation("checkpoint paths must be non-empty and unique")
        if not isinstance(expected_hash, str) or len(expected_hash) != 64:
            raise ContractViolation(f"invalid checkpoint hash for {relative}")
        seen.add(relative)
        content = _git(repo, "show", f"{repair_commit}:{relative}", binary=True)
        assert isinstance(content, bytes)
        if hashlib.sha256(content).hexdigest() != expected_hash.lower():
            raise ContractViolation(f"checkpoint hash mismatch: {relative}")

    return {
        "repairCommit": repair_commit,
        "repairTree": repair_tree,
        "validatedPathCount": len(items),
        "ancestryValid": True,
        "manifestExpectedInsideCheckpoint": False,
    }


def _leaf_map(binding: dict[str, Any]) -> dict[str, dict[str, Any]]:
    items = binding.get("orderedLogicalTargets")
    if not isinstance(items, list) or len(items) != 14:
        raise ContractViolation("binding must contain exactly 14 logical targets")
    result: dict[str, dict[str, Any]] = {}
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get("logicalTargetId"), str):
            raise ContractViolation("binding leaf is missing logicalTargetId")
        logical_id = item["logicalTargetId"]
        if logical_id in result:
            raise ContractViolation(f"duplicate logical target: {logical_id}")
        result[logical_id] = item
    return result


def validate_leaf_replacement(
    historical: dict[str, Any], current: dict[str, Any]
) -> dict[str, Any]:
    before = _leaf_map(historical)
    after = _leaf_map(current)
    if list(before) != list(after):
        raise ContractViolation("logical target order or identity changed")
    changed = [logical_id for logical_id in before if before[logical_id] != after[logical_id]]
    if changed != ["META-LH-03"]:
        raise ContractViolation("exactly META-LH-03 must be the only changed logical target")
    predecessor_unchanged = historical.get("completedPredecessor") == current.get(
        "completedPredecessor"
    )
    if not predecessor_unchanged:
        raise ContractViolation("completed Series predecessor bridge changed")
    return {
        "changedLogicalTargets": changed,
        "unchangedLogicalTargetCount": 13,
        "completedPredecessorUnchanged": True,
    }


def _canonical_raw_sha256(repo: Path, relative: str) -> str:
    """Bind tracked text to its Git blob while accepting checkout-only EOL conversion."""
    path = repo / relative
    try:
        worktree = path.read_bytes()
    except OSError as exc:
        raise ContractViolation(f"cannot hash {path}: {exc}") from exc
    result = subprocess.run(
        ["git", "-C", str(repo), "show", f"HEAD:{relative}"],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode == 0:
        blob = result.stdout
        if normalized_sha256(worktree) == normalized_sha256(blob):
            return hashlib.sha256(blob).hexdigest()
    return hashlib.sha256(worktree).hexdigest()


def _require_file_hash(
    repo: Path, relative: str, expected: str, *, normalized: bool = False
) -> None:
    path = repo / relative
    if not path.is_file():
        raise ContractViolation(f"required transaction file is missing: {relative}")
    actual = (
        normalized_sha256(path.read_bytes())
        if normalized
        else _canonical_raw_sha256(repo, relative)
    )
    if actual != expected:
        kind = "normalized" if normalized else "raw"
        raise ContractViolation(f"{kind} hash drift: {relative}")


def validate_r2_transaction(
    repo: Path,
    current: dict[str, Any],
    *,
    operation_path: Path | None = None,
) -> dict[str, Any]:
    """Validate the single approved META-LH-03 R1-to-R2 transaction."""
    operation_id = "986c1d6c-d485-460b-8d8d-7cf5816a2c36"
    receipt_id = "f41328cd-b301-4533-89dc-02aab758ab1f"
    review_id = "b8d49ed7-d05f-40b0-9e18-1aa1b689f1cf"
    checkpoint = "ee530952acc8093c9afd8e01b97825a0a1c9ac72"
    binding_path = "specs/003-authoring-contract/current-evidence-binding.json"
    baseline_raw = _git(repo, "show", f"{checkpoint}:{binding_path}", binary=True)
    assert isinstance(baseline_raw, bytes)
    historical = load_json_bytes(baseline_raw, f"{checkpoint}:{binding_path}")
    leaf_summary = validate_leaf_replacement(historical, current)

    before_renewed = {
        item["logicalTargetId"]: item
        for item in historical.get("renewedLogicalTargets", [])
    }
    after_renewed = {
        item["logicalTargetId"]: item
        for item in current.get("renewedLogicalTargets", [])
    }
    if list(before_renewed) != list(after_renewed):
        raise ContractViolation("renewed logical target order or identity changed")
    if any(
        before_renewed[key] != after_renewed[key]
        for key in before_renewed
        if key != "META-LH-03"
    ):
        raise ContractViolation("a renewed logical target other than META-LH-03 changed")

    proposal_path = (
        "specs/intake-authoring-operations/"
        f"{operation_id}/proposal.json"
    )
    default_operation_path = repo / (
        "specs/intake-authoring-operations/"
        f"{operation_id}/operation.json"
    )
    operation = load_json(operation_path or default_operation_path)
    if operation.get("operationId") != operation_id or operation.get("type") != "Update":
        raise ContractViolation("wrong reserved operation identity or type")
    if operation.get("receiptId") != receipt_id or operation.get("reviewId") != review_id:
        raise ContractViolation("wrong reserved receipt or review identity")
    if operation.get("status") != "Completed":
        raise ContractViolation("the renewal operation must be Completed")
    if operation.get("proposalPath") != proposal_path:
        raise ContractViolation("proposal path mismatch")
    proposal_hash = operation.get("proposalNormalizedSha256")
    if not isinstance(proposal_hash, str):
        raise ContractViolation("proposalNormalizedSha256 is missing")
    _require_file_hash(repo, proposal_path, proposal_hash, normalized=True)

    expected_sources = [
        "specs/intake-authoring-archive/83b9481e-bc4c-4e3d-b67a-1c6c8d05a681/7cc121ca-9c7a-4750-85e9-9cf2ebf2aa71/Lastenheft_META-LH-03-Authoring-Contract.md",
        ".specify/presets/intake-authoring-governance/templates/intake-template.md",
        ".specify/presets/intake-authoring-governance/templates/intake-authoring-receipt-template.json",
        ".specify/presets/intake-authoring-governance/templates/project-profile-template.md",
        "requirements/intake-governance.json",
        ".specify/presets/intake-authoring-governance/templates/field-validation-summary.md",
    ]
    if operation.get("sourceOrder") != expected_sources:
        raise ContractViolation("the accepted source order changed")

    archive_target = expected_sources[0]
    archive_receipt = (
        "specs/intake-authoring-archive/83b9481e-bc4c-4e3d-b67a-1c6c8d05a681/"
        "7cc121ca-9c7a-4750-85e9-9cf2ebf2aa71/META-LH-03-Authoring-Contract.json"
    )
    active_target = "requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.md"
    active_receipt = "specs/intake-authoring-receipts/META-LH-03-Authoring-Contract.json"
    publication_set = [archive_target, archive_receipt, active_target, active_receipt]
    for field in ("intendedTargets", "validatedTargets", "publishedTargets"):
        if operation.get(field) != publication_set:
            raise ContractViolation(f"{field} does not match the exact four-path set")

    supersedes = operation.get("supersedes")
    expected_supersedes = {
        "targetPath": active_target,
        "targetRawSha256": "ca159a03a91a19c3f2812a1a638604ca29dab816a20a9a67b7c5d06b3281f5eb",
        "targetNormalizedSha256": "ca159a03a91a19c3f2812a1a638604ca29dab816a20a9a67b7c5d06b3281f5eb",
        "archiveTargetPath": archive_target,
        "archiveTargetRawSha256": "ca159a03a91a19c3f2812a1a638604ca29dab816a20a9a67b7c5d06b3281f5eb",
        "receiptPath": active_receipt,
        "receiptRawSha256": "85ffcea67b0723241606040c5d2b9eb586a51d8d13005b676ceb6eeab2caa745",
        "archiveReceiptPath": archive_receipt,
        "archiveReceiptRawSha256": "85ffcea67b0723241606040c5d2b9eb586a51d8d13005b676ceb6eeab2caa745",
    }
    if supersedes != expected_supersedes:
        raise ContractViolation("full target/receipt supersession binding mismatch")
    _require_file_hash(repo, archive_target, expected_supersedes["archiveTargetRawSha256"])
    _require_file_hash(repo, archive_receipt, expected_supersedes["archiveReceiptRawSha256"])

    r1_review = {
        "reviewId": "0b31261e-e794-461f-8c28-3e3d9a518f69",
        "requestPath": "specs/intake-review-requests/meta-lh-03-authoring-contract-2026-09-05-r1.json",
        "requestRawSha256": "8675e679f55e089c8d4081fd7d7565e351c6fa4ab3408c27b9974f872a8ed7ea",
        "resultPath": "specs/intake-review-results/meta-lh-03-authoring-contract-2026-09-05-r1.json",
        "resultRawSha256": "2fe319d7c88ce5790f6ff6ba9a7d693936a7b88c787ff7dbe7588b5df9a35679",
        "reportPath": "docs/reviews/meta-lh-03-authoring-contract-intake-review-2026-09-05-r1.md",
        "reportRawSha256": "0947e027578bb135ac7de39e3b0ff45d2f76242f6037616c40a9c866b96dd5a9",
    }
    if operation.get("r1ReviewSupersession") != r1_review:
        raise ContractViolation("R1 review request/result/report supersession mismatch")
    for kind in ("request", "result", "report"):
        _require_file_hash(repo, r1_review[f"{kind}Path"], r1_review[f"{kind}RawSha256"])

    receipt = load_json(repo / active_receipt)
    if receipt.get("receiptId") != receipt_id:
        raise ContractViolation("active receipt does not use the reserved R2 receipt ID")
    if receipt.get("operation", {}).get("operationId") != operation_id:
        raise ContractViolation("active receipt is not bound to the Completed operation")
    target_hash = "3a5c34b54bdb0b00f78415089cc0b926b33ddeabe44ee7a130ad603acd4a98ba"
    if receipt.get("target") != {"path": active_target, "normalizedSha256": target_hash}:
        raise ContractViolation("active receipt target binding mismatch")
    _require_file_hash(repo, active_target, target_hash, normalized=True)

    r2_result_path = "specs/intake-review-results/meta-lh-03-authoring-contract-2026-09-05-r2.json"
    r2_report_path = "docs/reviews/meta-lh-03-authoring-contract-intake-review-2026-09-05-r2.md"
    r2_result = load_json(repo / r2_result_path)
    if r2_result.get("reviewId") != review_id or r2_result.get("status") != "Ready":
        raise ContractViolation("R2 review is not the reserved current Ready review")
    if r2_result.get("completedOperation", {}).get("operationId") != operation_id:
        raise ContractViolation("R2 review is not bound to the Completed operation")
    if r2_result.get("supersedesReview") != r1_review:
        raise ContractViolation("R2 result does not explicitly supersede the R1 review triple")

    leaf = _leaf_map(current)["META-LH-03"]
    expected_leaf = {
        "logicalTargetId": "META-LH-03",
        "target": {"path": active_target, "normalizedSha256": target_hash},
        "authoringReceipt": {
            "path": active_receipt,
            "rawSha256": _canonical_raw_sha256(repo, active_receipt),
        },
        "readySingleReview": {
            "path": r2_result_path,
            "rawSha256": _canonical_raw_sha256(repo, r2_result_path),
        },
        "readySingleReviewReport": {
            "path": r2_report_path,
            "rawSha256": _canonical_raw_sha256(repo, r2_report_path),
        },
    }
    if leaf != expected_leaf:
        raise ContractViolation("current META-LH-03 binding leaf does not match R2 evidence")
    current_renewed = after_renewed.get("META-LH-03", {}).get("current")
    if current_renewed != {key: value for key, value in expected_leaf.items() if key != "logicalTargetId"}:
        raise ContractViolation("renewed META-LH-03 current leaf does not match R2 evidence")

    return {
        **leaf_summary,
        "operationId": operation_id,
        "operationStatus": "Completed",
        "receiptId": receipt_id,
        "reviewId": review_id,
    }


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate the read-only META-LH-03 authoring-contract bridge."
    )
    parser.add_argument("--repo", default=".", help="Repository root")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    repo = Path(args.repo).resolve()
    try:
        checkpoint = validate_checkpoint(
            repo, repo / "specs/003-authoring-contract/repair-checkpoint-manifest.json"
        )
        binding = load_json(repo / "specs/003-authoring-contract/current-evidence-binding.json")
        transaction = validate_r2_transaction(repo, binding)
        result = {
            "schemaVersion": "1.0",
            "outcome": "Pass",
            "checkpoint": checkpoint,
            "transaction": transaction,
        }
        if args.json:
            print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))
        else:
            print("PASS: META-LH-03 authoring checkpoint / Authoring-Checkpoint bestanden")
        return 0
    except ContractViolation as exc:
        if args.json:
            print(json.dumps({"schemaVersion": "1.0", "outcome": "Fail", "error": str(exc)}, ensure_ascii=True))
        else:
            print(f"FAIL: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
