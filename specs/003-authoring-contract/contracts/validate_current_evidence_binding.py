#!/usr/bin/env python3
"""Read-only current-evidence bridge for the bounded META-LH-03 renewal."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath
from typing import Any, Callable


FEATURE = "specs/003-authoring-contract"
MANIFEST = f"{FEATURE}/current-evidence-binding.json"
AUTHORITY = f"{FEATURE}/binding-approval.md"
META02_STATE = "specs/002-portfolio-ownership/autonomous-run-state.json"
META02_LIFECYCLE = "specs/002-portfolio-ownership/intake-lifecycle.json"
FEATURE_LIFECYCLE = f"{FEATURE}/intake-lifecycle.json"
CANONICAL_SERIES_FILES = (
    "specs/intake-series/aoc-phase-2/manifest.json",
    "specs/intake-series/aoc-phase-2/operation.json",
    "specs/intake-series-receipts/aoc-phase-2.json",
    "requirements/intakes/series/order.md",
    "specs/intake-review-requests/aoc-phase-2-series-2026-08-30-r6.json",
    "specs/intake-review-results/aoc-phase-2-series-2026-08-30-r6.json",
    "docs/reviews/aoc-phase-2-intake-review-2026-08-30-r6.md",
    "requirements/baseline/coverage-matrix.md",
    "requirements/baseline/autonomy-and-evidence-model.md",
    "docs/governance/phase-2-public-readiness.md",
)
EXPECTED_ACCEPTED_RAW_SHA256 = {
    META02_STATE: "18069cb2627ac55f089117d255b1b19407d87e17b9c439fb4caccb6ae6f94893",
    META02_LIFECYCLE: "40e66d527b6e9b8d952eda1d960302bc9e5250c0eae2284b8cad87b48867a554",
    "specs/intake-series/aoc-phase-2/manifest.json":
        "6e928925d0a8133be83ddbfe75b379ed70fe82c7aeb7e34cc5c3ef10138eefec",
    "specs/intake-series/aoc-phase-2/operation.json":
        "938deb0bb6d3526f116c78c172ae239b98dbbe212550547d47f30df72a708a0b",
    "specs/intake-series-receipts/aoc-phase-2.json":
        "4566566a9263a8d86879478a078a26b25cfb3c4f3a1774805f8c12f3058cdf5a",
}
COMPLETION_MERGE = "3c9a618243fffff187932b1ee431ffbd25d3856e"
RUN_ID = "044b77ae-85fd-46ee-97f4-61ce7a2c9c66"
UUID_PATTERN = re.compile(
    r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
)
EXPECTED_RENEWALS = ("META-LH-02", "META-LH-03", "META-LH-05", "RAW-03")
EXPECTED_TARGET_CHANGES = ("META-LH-03",)
EXPECTED_META03_TARGET_SHA256 = (
    "3a5c34b54bdb0b00f78415089cc0b926b33ddeabe44ee7a130ad603acd4a98ba"
)
META03_RENEWAL_AUTHORITY = (
    "Current explicit phase instruction authorizes exactly this META-LH-03 renewal.",
    "Current explicit phase instruction to resume the existing META-LH-03 run with "
    "normal MergeAndSync and no Admin bypass.",
    "Current explicit phase instruction to resume META-LH-03 after Analyze R5 and "
    "execute T002 through T079.",
)
PROGRAMME_TARGETS = (
    ("META-LH-01", "requirements/intakes/active/Lastenheft_META-LH-01-Programmquellen.md"),
    ("META-LH-02", "requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.md"),
    ("META-LH-03", "requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.md"),
    ("META-LH-04", "requirements/intakes/active/Lastenheft_META-LH-04-Series-Eligibility.md"),
    ("META-LH-05", "requirements/intakes/active/Lastenheft_META-LH-05-Erste-Welle.md"),
    ("RAW-01", "requirements/intakes/active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md"),
    ("RAW-02", "requirements/intakes/active/Lastenheft_RAW-02-Workspace-Orchestrator.md"),
    ("RAW-03", "requirements/intakes/active/Lastenheft_RAW-03-State-Truthfulness.md"),
    ("RAW-04", "requirements/intakes/active/Lastenheft_RAW-04-Presentation-Fabric.md"),
    ("RAW-05", "requirements/intakes/active/Lastenheft_RAW-05-Execution-Nodes.md"),
    ("RAW-06", "requirements/intakes/active/Lastenheft_RAW-06-CLI-Environment-Orchestration.md"),
    ("RAW-07", "requirements/intakes/active/Lastenheft_RAW-07-Hardware-Capability-Layer.md"),
    ("RAW-08", "requirements/intakes/active/Lastenheft_RAW-08-Workflow-Engine.md"),
    ("RAW-09", "requirements/intakes/active/Lastenheft_RAW-09-Preset-Evolution.md"),
)
PHYSICAL_ARCHIVES = {
    "META-LH-01": PROGRAMME_TARGETS[0][1].removesuffix(".md") + ".001-programmquellen-baseline.md",
    "META-LH-02": PROGRAMME_TARGETS[1][1].removesuffix(".md") + ".002-portfolio-ownership.md",
}
RECEIPT_BASH = ".specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.sh"
RECEIPT_PS = ".specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.ps1"
REVIEW_BASH = ".specify/presets/intake-review-governance/scripts/validate-intake-review-result.sh"
REVIEW_PS = ".specify/presets/intake-review-governance/scripts/validate-intake-review-result.ps1"
PASS_MESSAGE = "PASS: current-evidence: immutable META-LH-02 history and 14 current Ready receipt/review bindings"


class ContractError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise ContractError(message)


def load_json(path: Path, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        fail(f"{label} is not valid UTF-8 JSON: {exc}")
    if not isinstance(value, dict):
        fail(f"{label} root must be an object")
    return value


def raw_sha(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError as exc:
        fail(f"cannot hash {path}: {exc}")


def normalized_bytes(raw: bytes, label: str) -> bytes:
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeError as exc:
        fail(f"{label} is not UTF-8: {exc}")
    if "\x00" in text:
        fail(f"binary NUL in {label}")
    return text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def normalized_sha(path: Path) -> str:
    try:
        return hashlib.sha256(normalized_bytes(path.read_bytes(), str(path))).hexdigest()
    except OSError as exc:
        fail(f"cannot hash {path}: {exc}")


def sha(value: object, label: str) -> str:
    if not isinstance(value, str) or re.fullmatch(r"[0-9a-f]{64}", value) is None:
        fail(f"{label} must be a lowercase SHA-256")
    return value


def repo_path(root: Path, value: object, label: str) -> Path:
    if not isinstance(value, str):
        fail(f"{label} must be a repository-relative path")
    pure = PurePosixPath(value)
    if not value or pure.is_absolute() or ".." in pure.parts:
        fail(f"{label} must be a repository-relative path")
    candidate = root / pure
    current = root
    for part in pure.parts:
        current = current / part
        if current.is_symlink():
            fail(f"{label} must not contain symlink components")
    try:
        if root.resolve() not in candidate.resolve().parents:
            fail(f"{label} escapes the repository root")
    except OSError as exc:
        fail(f"{label} cannot be resolved: {exc}")
    if not candidate.is_file():
        fail(f"{label} must identify an existing regular file")
    return candidate


def current_physical_target(
    root: Path, logical_id: str, logical_path: str, expected_hash: str,
) -> str:
    """Resolve a current target through the feature lifecycle after its rename."""
    if logical_id in PHYSICAL_ARCHIVES:
        return PHYSICAL_ARCHIVES[logical_id]
    lifecycle_path = root / FEATURE_LIFECYCLE
    if not lifecycle_path.is_file():
        return logical_path
    lifecycle = load_json(lifecycle_path, FEATURE_LIFECYCLE)
    records = lifecycle.get("records")
    if lifecycle.get("schemaVersion") != "1.1" or not isinstance(records, list):
        fail("feature lifecycle contract is invalid")
    matches = [
        record for record in records
        if isinstance(record, dict) and record.get("originalPath") == logical_path
    ]
    if not matches:
        return logical_path
    if len(matches) != 1:
        fail(f"feature lifecycle resolution is ambiguous for {logical_path}")
    record = matches[0]
    if record.get("originalNormalizedSha256") != expected_hash:
        fail(f"feature lifecycle target hash drift for {logical_path}")
    archived = record.get("archivedPath")
    if not isinstance(archived, str):
        fail(f"feature lifecycle archived path is invalid for {logical_path}")
    original_file = root / logical_path
    archived_file = repo_path(root, archived, f"lifecycle archived target for {logical_path}")
    if original_file.is_file() or normalized_sha(archived_file) != expected_hash:
        fail(f"feature lifecycle physical target is inconsistent for {logical_path}")
    return archived


def git_blob(root: Path, revision: str, relative: str) -> bytes:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "cat-file", "blob", f"{revision}:{relative}"],
            capture_output=True, check=False,
        )
    except OSError as exc:
        fail(f"cannot read Git blob {revision}:{relative}: {exc}")
    if result.returncode:
        fail(f"cannot read Git blob {revision}:{relative}")
    return result.stdout


def require_ancestor(root: Path) -> None:
    try:
        result = subprocess.run(
            ["git", "merge-base", "--is-ancestor", COMPLETION_MERGE, "HEAD"],
            cwd=root, env={**os.environ, "GIT_OPTIONAL_LOCKS": "0"},
            capture_output=True, check=False,
        )
    except OSError as exc:
        fail(f"completion ancestry could not be checked: {exc}")
    if result.returncode == 1:
        fail("HEAD is not a descendant of the accepted META-LH-02 completion merge")
    if result.returncode:
        fail("completion ancestry could not be checked")


def require_clean_accepted_file(root: Path, relative: str) -> bytes:
    head = git_blob(root, "HEAD", relative)
    accepted = git_blob(root, COMPLETION_MERGE, relative)
    expected_digest = EXPECTED_ACCEPTED_RAW_SHA256.get(relative)
    if expected_digest is not None and hashlib.sha256(accepted).hexdigest() != expected_digest:
        fail(f"accepted historical raw SHA-256 drift: {relative}")
    if head != accepted:
        fail(f"accepted historical blob drift: {relative}")
    for cached in (False, True):
        command = ["git", "--no-optional-locks", "diff", "--no-ext-diff", "--quiet"]
        if cached:
            command.append("--cached")
        command.extend(["--", relative])
        try:
            result = subprocess.run(
                command, cwd=root, env={**os.environ, "GIT_OPTIONAL_LOCKS": "0"}, check=False,
            )
        except OSError as exc:
            fail(f"accepted historical cleanliness could not be checked for {relative}: {exc}")
        if result.returncode == 1:
            fail(f"accepted historical checkout drift: {relative}")
        if result.returncode:
            fail(f"accepted historical cleanliness could not be checked for {relative}")
    try:
        current = repo_path(root, relative, relative).read_bytes()
    except OSError as exc:
        fail(f"cannot read accepted historical checkout {relative}: {exc}")
    if normalized_bytes(current, relative) != normalized_bytes(head, relative):
        fail(f"accepted historical checkout drift: {relative}")
    return accepted


def require_immutable_predecessor(root: Path) -> dict[str, Any]:
    require_ancestor(root)
    for relative in (META02_STATE, META02_LIFECYCLE):
        require_clean_accepted_file(root, relative)
    for relative in CANONICAL_SERIES_FILES:
        require_clean_accepted_file(root, relative)
    state = json.loads(git_blob(root, COMPLETION_MERGE, META02_STATE))
    if (
        state.get("schemaVersion") != "1.1"
        or state.get("runId") != "aa60069e-ded5-463f-a737-9b5aa96070c7"
        or state.get("branch") != "002-portfolio-ownership"
        or state.get("featurePath") != "specs/002-portfolio-ownership"
    ):
        fail("accepted META-LH-02 state identity is invalid")
    if (state.get("status"), state.get("stage"), state.get("nextExactAction")) != ("Completed", "MergeAndSync", "N/A"):
        fail("accepted META-LH-02 state is not terminal Completed/MergeAndSync")
    if state.get("tasks", {}).get("completed") != 93 or state.get("tasks", {}).get("total") != 93:
        fail("accepted META-LH-02 state is not 93/93")
    if state.get("closeout") != {
        "mergeOrPublication": "Completed", "defaultBranchSync": "Completed",
        "postMergeActions": "Completed", "finalValidation": "Completed",
    }:
        fail("accepted META-LH-02 closeout is incomplete")
    lifecycle = json.loads(git_blob(root, COMPLETION_MERGE, META02_LIFECYCLE))
    if (
        set(lifecycle) != {"schemaVersion", "records", "programmeEvidenceSnapshot"}
        or lifecycle.get("schemaVersion") != "1.1"
    ):
        fail("accepted META-LH-02 lifecycle header is invalid")
    snapshot = lifecycle.get("programmeEvidenceSnapshot")
    if not isinstance(snapshot, dict):
        fail("accepted META-LH-02 programme snapshot is missing")
    ordered = snapshot.get("orderedLogicalTargets")
    ids = [item.get("logicalTargetId") if isinstance(item, dict) else None for item in ordered or []]
    if ids != [item[0] for item in PROGRAMME_TARGETS]:
        fail("accepted META-LH-02 programme snapshot order drift")
    records = lifecycle.get("records")
    if (
        not isinstance(records, list)
        or len(records) != 1
        or records[0].get("logicalTargetId") != "META-LH-02"
        or records[0].get("runId") != state["runId"]
        or records[0].get("branch") != state["branch"]
    ):
        fail("accepted META-LH-02 lifecycle record is invalid")
    return {item["logicalTargetId"]: item for item in ordered}


def current_receipts(root: Path) -> dict[str, tuple[str, dict[str, Any]]]:
    result: dict[str, tuple[str, dict[str, Any]]] = {}
    for path in sorted((root / "specs/intake-authoring-receipts").glob("*.json")):
        relative = path.relative_to(root).as_posix()
        data = load_json(repo_path(root, relative, f"receipt {path.name}"), f"receipt {path.name}")
        target = data.get("target")
        target_path = target.get("path") if isinstance(target, dict) else None
        if isinstance(target_path, str):
            if target_path in result:
                fail(f"duplicate current receipt for {target_path}")
            result[target_path] = (relative, data)
    return result


def current_reviews(root: Path) -> dict[str, tuple[str, dict[str, Any]]]:
    records: list[tuple[str, dict[str, Any], str]] = []
    for path in sorted((root / "specs/intake-review-results").glob("*.json")):
        relative = path.relative_to(root).as_posix()
        data = load_json(repo_path(root, relative, f"review {path.name}"), f"review {path.name}")
        targets = data.get("targets")
        mode = data.get("mode")
        if mode in ("Series", "Campaign"):
            continue
        if mode != "Single":
            fail(f"review result has missing or unsupported mode: {path.name}")
        if not isinstance(targets, list) or len(targets) != 1 or not isinstance(targets[0], dict):
            fail(f"malformed Single review target: {path.name}")
        target = targets[0].get("path")
        supersedes = data.get("supersedes")
        if not isinstance(target, str) or not isinstance(supersedes, str) or not supersedes:
            fail(f"malformed Single review lineage: {path.name}")
        records.append((relative, data, target))
    by_path = {path: (data, target) for path, data, target in records}
    edges: dict[str, str] = {}
    for path, data, target in records:
        predecessor = data["supersedes"]
        if predecessor == "N/A":
            continue
        if predecessor not in by_path:
            fail(f"dangling Single review supersedes reference: {path}")
        if by_path[predecessor][1] != target:
            fail(f"cross-target Single review supersedes reference: {path}")
        edges[path] = predecessor
    for start in edges:
        seen: set[str] = set()
        node = start
        while node in edges:
            if node in seen:
                fail(f"cyclic Single review supersession chain: {start}")
            seen.add(node)
            node = edges[node]
    superseded = set(edges.values())
    result: dict[str, tuple[str, dict[str, Any]]] = {}
    for target in {item[2] for item in records}:
        leaves = [
            (path, data) for path, data, item_target in records
            if item_target == target and path not in superseded
        ]
        if len(leaves) != 1 and target in {item[1] for item in PROGRAMME_TARGETS}:
            fail(f"target {target} needs exactly one current Single review leaf; found {len(leaves)}")
        if len(leaves) == 1:
            result[target] = leaves[0]
    return result


def run_checked(command: list[str], root: Path, label: str, expected_stdout: str) -> None:
    try:
        result = subprocess.run(command, cwd=root, text=True, capture_output=True, check=False)
    except OSError as exc:
        fail(f"{label} could not start: {exc}")
    if result.returncode:
        detail = (result.stderr or result.stdout).strip().splitlines()
        fail(f"{label} failed: {detail[0] if detail else 'no diagnostic'}")
    if result.stdout != f"{expected_stdout}\n" or result.stderr:
        fail(f"{label} returned an invalid success result")


def review_surface(root: Path, surface: str, review: str, logical: str, physical: str,
                   expected_stdout: str,
                   runner: Callable[[list[str], Path, str, str], None]) -> None:
    review_root = "."
    temporary: tempfile.TemporaryDirectory[str] | None = None
    try:
        if logical != physical:
            temporary = tempfile.TemporaryDirectory(prefix="meta-lh03-current-review-")
            projection = Path(temporary.name)
            (projection / "specs").symlink_to((root / "specs").resolve(), target_is_directory=True)
            target = projection / logical
            target.parent.mkdir(parents=True, exist_ok=True)
            target.symlink_to((root / physical).resolve())
            review_root = str(projection)
        command = ([shutil.which("bash") or "bash", REVIEW_BASH, "--result", review, "--repo", review_root]
                   if surface == "Bash" else ["pwsh", "-NoProfile", "-File", REVIEW_PS, "-Result", review, "-Repo", review_root])
        runner(command, root, f"{surface} review validator for {logical}", expected_stdout)
    finally:
        if temporary:
            temporary.cleanup()


def exact_binding(value: object, kind: str, label: str) -> dict[str, str]:
    keys = {"path", "normalizedSha256" if kind == "target" else "rawSha256"}
    if not isinstance(value, dict) or set(value) != keys:
        fail(f"{label} fields are incomplete or ambiguous")
    path = value.get("path")
    digest_name = "normalizedSha256" if kind == "target" else "rawSha256"
    if not isinstance(path, str):
        fail(f"{label}.path is invalid")
    sha(value.get(digest_name), f"{label}.{digest_name}")
    return value


def validate_manifest(
    root: Path,
    runner: Callable[[list[str], Path, str, str], None] = run_checked,
) -> str:
    historical = require_immutable_predecessor(root)
    manifest = load_json(repo_path(root, MANIFEST, "current evidence binding"), "current evidence binding")
    required = {"schemaVersion", "documentType", "runId", "authorityBinding", "completedPredecessor", "renewedLogicalTargets", "orderedLogicalTargets"}
    if set(manifest) != required or manifest.get("schemaVersion") != "1.0" or manifest.get("documentType") != "CurrentEvidenceBinding" or manifest.get("runId") != RUN_ID:
        fail("current evidence binding header fields are invalid")
    authority = manifest.get("authorityBinding")
    expected_authority_keys = {"path", "rawSha256", "allowedReceiptReviewRenewals", "allowedTargetChanges", "presetVersionChange", "grants"}
    if not isinstance(authority, dict) or set(authority) != expected_authority_keys:
        fail("authorityBinding fields are incomplete or ambiguous")
    if authority.get("path") != AUTHORITY or authority.get("grants") != [] or tuple(authority.get("allowedReceiptReviewRenewals", [])) != EXPECTED_RENEWALS or tuple(authority.get("allowedTargetChanges", [])) != EXPECTED_TARGET_CHANGES:
        fail("authorityBinding exceeds the exact bounded repair scope")
    if raw_sha(repo_path(root, AUTHORITY, "authorityBinding.path")) != sha(
            authority.get("rawSha256"), "authorityBinding.rawSha256"):
        fail("bounded authority raw SHA-256 drift")
    preset = authority.get("presetVersionChange")
    if preset != {"path": ".specify/presets/intake-authoring-governance/preset.yml", "from": "0.3.0", "to": "0.3.1"}:
        fail("presetVersionChange must bind only installed 0.3.0 to 0.3.1")
    preset_file = repo_path(root, preset["path"], "presetVersionChange.path")
    if 'version: "0.3.1"' not in preset_file.read_text(encoding="utf-8"):
        fail("installed Intake Authoring preset is not 0.3.1")
    predecessor = manifest.get("completedPredecessor")
    expected_predecessor = {
        "completionMergeSha": COMPLETION_MERGE,
        "state": {"path": META02_STATE, "rawSha256": hashlib.sha256(git_blob(root, COMPLETION_MERGE, META02_STATE)).hexdigest()},
        "lifecycle": {"path": META02_LIFECYCLE, "rawSha256": hashlib.sha256(git_blob(root, COMPLETION_MERGE, META02_LIFECYCLE)).hexdigest()},
    }
    if predecessor != expected_predecessor:
        fail("completedPredecessor differs from immutable META-LH-02 history")

    ordered = manifest.get("orderedLogicalTargets")
    if not isinstance(ordered, list) or [item.get("logicalTargetId") if isinstance(item, dict) else None for item in ordered] != [item[0] for item in PROGRAMME_TARGETS]:
        fail("orderedLogicalTargets must contain the exact fixed 14-target order")
    receipts, reviews = current_receipts(root), current_reviews(root)
    current: dict[str, dict[str, Any]] = {}
    physical_set: set[str] = set()
    current_report_paths: set[str] = set()
    for index, ((logical_id, logical_path), entry) in enumerate(zip(PROGRAMME_TARGETS, ordered)):
        label = f"orderedLogicalTargets[{index}]"
        entry_keys = {"logicalTargetId", "target", "authoringReceipt", "readySingleReview"}
        if logical_id in EXPECTED_RENEWALS:
            entry_keys.add("readySingleReviewReport")
        if not isinstance(entry, dict) or set(entry) != entry_keys or entry.get("logicalTargetId") != logical_id:
            fail(f"{label} fields or logicalTargetId are invalid")
        target = exact_binding(entry.get("target"), "target", f"{label}.target")
        receipt = exact_binding(entry.get("authoringReceipt"), "raw", f"{label}.authoringReceipt")
        review = exact_binding(entry.get("readySingleReview"), "raw", f"{label}.readySingleReview")
        if logical_id in EXPECTED_RENEWALS:
            report = exact_binding(
                entry.get("readySingleReviewReport"), "raw",
                f"{label}.readySingleReviewReport",
            )
            report_path = repo_path(root, report["path"], f"{label}.readySingleReviewReport.path")
            if not report["path"].startswith("docs/reviews/") or report["path"] in current_report_paths:
                fail(f"{label}.readySingleReviewReport path is invalid or duplicated")
            if raw_sha(report_path) != report["rawSha256"]:
                fail(f"{label}.readySingleReviewReport raw SHA-256 drift")
            current_report_paths.add(report["path"])
        if target["path"] != logical_path:
            fail(f"{label}.target.path differs from the canonical target")
        physical = current_physical_target(
            root, logical_id, logical_path, target["normalizedSha256"],
        )
        physical_set.add(physical)
        target_file = repo_path(root, physical, f"{label}.physicalTarget")
        if normalized_sha(target_file) != target["normalizedSha256"]:
            fail(f"{label}.target normalized SHA-256 drift")
        current_receipt = receipts.get(logical_path)
        current_review = reviews.get(logical_path)
        receipt_file = repo_path(root, receipt["path"], f"{label}.authoringReceipt.path")
        review_file = repo_path(root, review["path"], f"{label}.readySingleReview.path")
        if current_receipt is None or current_receipt[0] != receipt["path"] or raw_sha(receipt_file) != receipt["rawSha256"]:
            fail(f"{label}.authoringReceipt is not the unique current bound receipt")
        if current_review is None or current_review[0] != review["path"] or raw_sha(review_file) != review["rawSha256"]:
            fail(f"{label}.readySingleReview is not the unique current bound leaf")
        review_data = current_review[1]
        target_row = review_data.get("targets", [{}])[0]
        if (
            review_data.get("schemaVersion") != "1.1"
            or review_data.get("mode") != "Single"
            or review_data.get("policy") != "aoc-bilingual-requirements"
            or review_data.get("status") != "Ready"
            or target_row.get("role") != "Primary"
            or target_row.get("path") != logical_path
            or target_row.get("normalizedSha256") != target["normalizedSha256"]
            or any(review_data.get(field) != [] for field in (
                "findings", "questions", "acceptedRisks", "operatorExceptions"
            ))
            or review_data.get("coverage", {}).get("individual") != [logical_path]
        ):
            fail(f"{label}.readySingleReview is not current Single/Primary/Ready")
        request = review_data.get("requestEvidence")
        if not isinstance(request, dict) or set(request) != {"path", "normalizedSha256"}:
            fail(f"{label}.readySingleReview requestEvidence is invalid")
        request_path = repo_path(root, request.get("path"), f"{label}.requestEvidence.path")
        if normalized_sha(request_path) != request.get("normalizedSha256"):
            fail(f"{label}.readySingleReview requestEvidence hash drift")
        receipt_data = current_receipt[1]
        receipt_target = receipt_data.get("target", {})
        if receipt_data.get("status") != "ReadyForReview" or receipt_target.get("normalizedSha256") != target["normalizedSha256"]:
            fail(f"{label}.authoringReceipt is not ReadyForReview for the current target")
        for surface, command in (
            ("Bash", [shutil.which("bash") or "bash", RECEIPT_BASH, "--receipt", receipt["path"], "--repo", "."]),
            ("PowerShell", ["pwsh", "-NoProfile", "-File", RECEIPT_PS, "-Receipt", receipt["path"], "-Repo", "."]),
        ):
            expected_receipt = (
                f"PASS: intake authoring {receipt_data.get('receiptId')} is current "
                f"(ReadyForReview, {len(receipt_data.get('sources', []))} sources, {logical_path})"
            )
            runner(command, root, f"{surface} receipt validator for {logical_path}", expected_receipt)
            expected_review = (
                f"PASS: intake review {review_data.get('reviewId')} is current "
                "(Single, Ready, 1 targets)"
            )
            review_surface(
                root, surface, review["path"], logical_path, physical,
                expected_review, runner,
            )
        current[logical_id] = entry
    actual = {path.relative_to(root).as_posix() for path in (root / "requirements/intakes/active").glob("Lastenheft_*.md")}
    if actual != physical_set:
        fail("current physical target inventory differs from exact 14-target resolution")

    renewals = manifest.get("renewedLogicalTargets")
    if not isinstance(renewals, list) or [item.get("logicalTargetId") if isinstance(item, dict) else None for item in renewals] != list(EXPECTED_RENEWALS):
        fail("renewedLogicalTargets must contain exactly META-LH-02, META-LH-03, META-LH-05, RAW-03")
    current_receipt_ids: set[str] = set()
    current_operation_ids: set[str] = set()
    current_review_ids: set[str] = set()
    for item in renewals:
        logical_id = item["logicalTargetId"]
        current_keys = (
            "target", "authoringReceipt", "readySingleReview", "readySingleReviewReport"
        )
        if set(item) != {"logicalTargetId", "historical", "current"} or item.get("current") != {key: current[logical_id][key] for key in current_keys}:
            fail(f"{logical_id} renewal does not bind its current ordered entry")
        old = historical[logical_id]
        history = item.get("historical")
        if not isinstance(history, dict) or set(history) != {"target", "authoringReceipt", "readySingleReview"}:
            fail(f"{logical_id}.historical fields are invalid")
        old_target, old_receipt, old_review = old["target"], old["authoringReceipt"], old["readySingleReview"]
        ht, hr, hv = history["target"], history["authoringReceipt"], history["readySingleReview"]
        if not isinstance(ht, dict) or set(ht) != {"path", "normalizedSha256", "rawSha256", "archivePath"} or ht["path"] != old_target["path"] or ht["normalizedSha256"] != old_target["normalizedSha256"]:
            fail(f"{logical_id} historical target differs from accepted snapshot")
        accepted_target_path = PHYSICAL_ARCHIVES.get(logical_id, old_target["path"])
        target_blob = git_blob(root, COMPLETION_MERGE, accepted_target_path)
        if ht["rawSha256"] != hashlib.sha256(target_blob).hexdigest():
            fail(f"{logical_id} historical target raw hash differs from exact Git")
        if hashlib.sha256(normalized_bytes(target_blob, accepted_target_path)).hexdigest() != old_target["normalizedSha256"]:
            fail(f"{logical_id} accepted target normalized hash differs from the completed snapshot")
        archive_target = repo_path(root, ht.get("archivePath"), f"{logical_id}.historical.target.archivePath")
        if archive_target.read_bytes() != target_blob:
            fail(f"{logical_id} historical target archive is not byte-identical")
        receipt_blob = git_blob(root, COMPLETION_MERGE, old_receipt["path"])
        if hashlib.sha256(receipt_blob).hexdigest() != old_receipt["rawSha256"]:
            fail(f"{logical_id} accepted receipt differs from the completed snapshot")
        if not isinstance(hr, dict) or set(hr) != {"path", "rawSha256", "archivePath"} or hr["path"] != old_receipt["path"] or hr["rawSha256"] != old_receipt["rawSha256"]:
            fail(f"{logical_id} historical receipt binding differs from the completed snapshot")
        archive_receipt = repo_path(root, hr.get("archivePath"), f"{logical_id}.historical.authoringReceipt.archivePath")
        if archive_receipt.read_bytes() != receipt_blob:
            fail(f"{logical_id} historical receipt archive differs from exact Git")
        old_receipt_data = json.loads(receipt_blob)
        review_blob = git_blob(root, COMPLETION_MERGE, old_review["path"])
        if hashlib.sha256(review_blob).hexdigest() != old_review["rawSha256"] or hv != old_review:
            fail(f"{logical_id} historical review binding differs from the completed snapshot")
        if repo_path(root, hv["path"], f"{logical_id}.historical.readySingleReview.path").read_bytes() != review_blob:
            fail(f"{logical_id} historical review bytes drift")
        new_receipt = receipts[PROGRAMME_TARGETS[[x[0] for x in PROGRAMME_TARGETS].index(logical_id)][1]][1]
        supersedes = new_receipt.get("supersedes", {})
        operation = new_receipt.get("operation")
        authority_texts = (
            new_receipt.get("updateAuthorityEvidence"),
            new_receipt.get("authorityEvidence"),
            operation.get("authorityEvidence") if isinstance(operation, dict) else None,
        )
        authority_valid = (
            authority_texts == META03_RENEWAL_AUTHORITY
            if logical_id == "META-LH-03"
            else all(
                isinstance(value, str) and AUTHORITY in value and RUN_ID in value
                for value in authority_texts
            )
        )
        if not authority_valid:
            fail(f"{logical_id} receipt is not bound to the exact current authority and run")
        expected_receipt_path = hr["archivePath"]
        expected_receipt_archive = hr["archivePath"]
        expected_target_archive = ht["archivePath"]
        expected_target_hash = old_target["normalizedSha256"]
        expected_source_boundary = "RepositoryArchiveAtApprovedBindingRenewal"
        expected_archive_identity = (new_receipt.get("intakeId"), operation.get("operationId"))
        if logical_id == "META-LH-03":
            expected_receipt_path = old_receipt["path"]
            expected_receipt_archive = supersedes.get("archiveReceiptPath")
            expected_target_archive = supersedes.get("archiveTargetPath")
            expected_target_hash = supersedes.get("targetNormalizedSha256")
            expected_source_boundary = "RepositoryArchiveAtApprovedRenewal"
            intermediate_receipt_path = repo_path(
                root, expected_receipt_archive, "META-LH-03 intermediate receipt archive",
            )
            intermediate_target_path = repo_path(
                root, expected_target_archive, "META-LH-03 intermediate target archive",
            )
            intermediate_receipt = load_json(
                intermediate_receipt_path, "META-LH-03 intermediate receipt archive",
            )
            intermediate_supersedes = intermediate_receipt.get("supersedes", {})
            if (
                raw_sha(intermediate_receipt_path) != supersedes.get("archiveReceiptRawSha256")
                or supersedes.get("receiptRawSha256") != supersedes.get("archiveReceiptRawSha256")
                or normalized_sha(intermediate_target_path) != expected_target_hash
                or supersedes.get("targetRawSha256") != raw_sha(intermediate_target_path)
                or supersedes.get("archiveTargetRawSha256") != raw_sha(intermediate_target_path)
                or intermediate_receipt.get("target", {}).get("normalizedSha256")
                != expected_target_hash
                or intermediate_supersedes.get("archiveReceiptPath") != hr["archivePath"]
                or intermediate_supersedes.get("archiveTargetPath") != ht["archivePath"]
                or intermediate_supersedes.get("targetNormalizedSha256")
                != old_target["normalizedSha256"]
            ):
                fail("META-LH-03 intermediate binding-repair predecessor is invalid")
            expected_archive_identity = (
                new_receipt.get("intakeId"), intermediate_receipt.get("receiptId"),
            )
        if new_receipt.get("provenanceMode") != "Supersession" or new_receipt.get("updateAuthorized") is not True or supersedes.get("receiptPath") != expected_receipt_path or supersedes.get("archiveReceiptPath") != expected_receipt_archive or supersedes.get("targetNormalizedSha256") != expected_target_hash:
            fail(f"{logical_id} receipt supersession or bounded update authority is invalid")
        if supersedes.get("archiveTargetPath") != expected_target_archive:
            fail(f"{logical_id} target supersession archive path drift")
        sources = new_receipt.get("sources")
        source_zero = sources[0] if isinstance(sources, list) and sources else None
        operation_id = operation.get("operationId") if isinstance(operation, dict) else None
        receipt_id = new_receipt.get("receiptId")
        if (
            new_receipt.get("schemaVersion") != "2.0"
            or new_receipt.get("documentType") != "IntakeReceipt"
            or new_receipt.get("intakeId") != old_receipt_data.get("intakeId")
            or receipt_id == old_receipt_data.get("receiptId")
            or not isinstance(receipt_id, str)
            or UUID_PATTERN.fullmatch(receipt_id) is None
            or receipt_id in current_receipt_ids
            or not isinstance(operation_id, str)
            or UUID_PATTERN.fullmatch(operation_id) is None
            or operation_id == old_receipt_data.get("operation", {}).get("operationId")
            or operation_id == receipt_id
            or operation_id in current_operation_ids
            or operation.get("type") != "Update"
            or new_receipt.get("generator") != {
                "preset": "intake-authoring-governance", "version": "0.3.1"
            }
            or current[logical_id]["authoringReceipt"]["path"] != old_receipt["path"]
            or PurePosixPath(expected_receipt_archive).parts[-3:-1]
            != expected_archive_identity
            or not isinstance(source_zero, dict)
            or source_zero.get("sourceId") != "SRC001"
            or source_zero.get("order") != 1
            or source_zero.get("kind") != "File"
            or source_zero.get("path") != expected_target_archive
            or source_zero.get("normalizedSha256") != expected_target_hash
            or source_zero.get("proofBoundary") != expected_source_boundary
        ):
            fail(f"{logical_id} renewed receipt identity or predecessor source is invalid")
        current_receipt_ids.add(receipt_id)
        current_operation_ids.add(operation_id)
        current_review = reviews[old_target["path"]][1]
        old_review_data = json.loads(review_blob)
        review_id = current_review.get("reviewId")
        expected_review_predecessor = old_review["path"]
        if logical_id == "META-LH-03":
            intermediate_review_path = current_review.get("supersedes")
            intermediate_review = load_json(
                repo_path(root, intermediate_review_path, "META-LH-03 intermediate review"),
                "META-LH-03 intermediate review",
            )
            if (
                intermediate_review.get("supersedes") != old_review["path"]
                or intermediate_review.get("status") != "Ready"
                or intermediate_review.get("targets", [{}])[0].get("normalizedSha256")
                != expected_target_hash
            ):
                fail("META-LH-03 intermediate binding-repair review is invalid")
            expected_review_predecessor = intermediate_review_path
        if (
            current_review.get("supersedes") != expected_review_predecessor
            or not isinstance(review_id, str)
            or UUID_PATTERN.fullmatch(review_id) is None
            or review_id == old_review_data.get("reviewId")
            or review_id in current_review_ids
            or current_review.get("requestEvidence", {}).get("path")
            != current[logical_id]["readySingleReview"]["path"].replace(
                "specs/intake-review-results/", "specs/intake-review-requests/"
            )
        ):
            fail(f"{logical_id} current review identity or direct supersession is invalid")
        current_review_ids.add(review_id)
        request_data = load_json(
            repo_path(root, current_review["requestEvidence"]["path"], f"{logical_id} review request"),
            f"{logical_id} review request",
        )
        if (
            request_data.get("schemaVersion") != "1.1"
            or request_data.get("reviewId") != review_id
            or request_data.get("mode") != "Single"
            or request_data.get("policy") != "aoc-bilingual-requirements"
            or request_data.get("targets") != [{"path": old_target["path"], "role": "Primary"}]
        ):
            fail(f"{logical_id} review request/result identity is invalid")
        report_binding = current[logical_id]["readySingleReviewReport"]
        report_text = repo_path(
            root, report_binding["path"], f"{logical_id} ready Single review report"
        ).read_text(encoding="utf-8")
        receipt_digest = current[logical_id]["authoringReceipt"]["rawSha256"]
        if any(value not in report_text for value in (
            review_id, receipt_id, old_receipt["path"], receipt_digest,
        )):
            fail(f"{logical_id} review report does not bind current review and receipt identity")
        changed_target = current[logical_id]["target"]["normalizedSha256"] != old_target["normalizedSha256"]
        if changed_target != (logical_id == "META-LH-03"):
            fail("only META-LH-03 target content may change")
        if logical_id == "META-LH-03":
            current_target = repo_path(
                root,
                current_physical_target(
                    root, logical_id, current[logical_id]["target"]["path"],
                    current[logical_id]["target"]["normalizedSha256"],
                ),
                "META-LH-03 current target",
            )
            if (
                current[logical_id]["target"]["normalizedSha256"]
                != EXPECTED_META03_TARGET_SHA256
                or normalized_sha(current_target) != EXPECTED_META03_TARGET_SHA256
            ):
                fail("META-LH-03 target change exceeds the exact 0.3.0 to 0.3.1 replacement")
        if current[logical_id]["authoringReceipt"]["rawSha256"] == old_receipt["rawSha256"] or current[logical_id]["readySingleReview"] == old_review:
            fail(f"{logical_id} receipt and review must both be renewed")
    for logical_id, _ in PROGRAMME_TARGETS:
        if logical_id not in EXPECTED_RENEWALS and current[logical_id] != historical[logical_id]:
            fail(f"unapproved current evidence change for {logical_id}")
    return PASS_MESSAGE


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the META-LH-03 current-evidence bridge read-only")
    parser.add_argument("--repo", default=".")
    parser.add_argument("mode", choices=("current-evidence",))
    args = parser.parse_args(argv)
    try:
        result = validate_manifest(Path(args.repo).resolve())
    except ContractError as exc:
        print(f"ERROR: current-evidence: {exc}", file=sys.stderr)
        return 1
    except (OSError, UnicodeError, KeyError, TypeError, ValueError) as exc:
        print(f"ERROR: current-evidence: malformed input: {exc}", file=sys.stderr)
        return 1
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
