#!/usr/bin/env python3
"""Read-only acceptance contract for META-LH-01 workflow evidence.

The validator uses only the Python standard library. Every validation mode is
read-only against the repository. The two explicit render modes may create one
named output outside the repository and refuse every repository path. After
the terminal rename, installed review validators run against an automatically
removed temporary projection outside the repository that exposes the proven
archive bytes at the immutable review's original logical path.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


FEATURE = "specs/001-programmquellen-baseline"
STATE = f"{FEATURE}/autonomous-run-state.json"
TASKS = f"{FEATURE}/tasks.md"
REQUIREMENTS = f"{FEATURE}/autonomous-run-gate-requirements.json"
LIFECYCLE = f"{FEATURE}/intake-lifecycle.json"
CAUSAL_CLOSEOUT = f"{FEATURE}/causal-closeout-evidence.json"
CLOSEOUT_BRANCH = "codex/001-programmquellen-baseline-closeout"
CLOSEOUT_PATHS = (
    TASKS,
    STATE,
    CAUSAL_CLOSEOUT,
)
LOGICAL_META01 = "META-LH-01"
EXPECTED_RUN_ID = "b3694a58-208b-4d6b-a4d4-1b01f3816dcc"
EXPECTED_BRANCH = "001-programmquellen-baseline"
ACCEPTED_BASE_SHA = "b8eb0735b2a7c46a65712d2e280242c85f8c1d64"
ORIGINAL_META01 = "requirements/intakes/active/Lastenheft_META-LH-01-Programmquellen.md"
ARCHIVED_META01 = (
    "requirements/intakes/active/"
    "Lastenheft_META-LH-01-Programmquellen.001-programmquellen-baseline.md"
)
DOMAIN_PATHS = (
    "requirements/baseline/source-pack.md",
    "requirements/baseline/constraint-register.md",
    "requirements/baseline/review-findings-ledger.md",
    "requirements/baseline/coverage-matrix.md",
    "requirements/baseline/glossary.md",
    "requirements/baseline/authority-and-stop-gates.md",
)
REVIEW_PATHS = DOMAIN_PATHS + (CAUSAL_CLOSEOUT,)
EXPECTED_SOURCES = {
    "SRC-156", "SRC-157", "SRC-159", "SRC-161", "SRC-162", "SRC-163",
    "SRC-164", "SRC-165", "SRC-166", "SRC-167", "SRC-168", "SRC-169",
    "SRC-170", "SRC-171", "SRC-172", "SRC-173", "SRC-174", "SRC-175",
    "SRC-177", "SRC-180", "SRC-181", "SRC-182", "SRC-ES-01",
}
FORBIDDEN_SOURCES = {"SRC-158", "SRC-160", "SRC-176", "SRC-178", "SRC-179"}
EXPECTED_FINDINGS = {f"RF-{number:02d}" for number in range(1, 22)}
DIRECT_META = {
    "RF-01", "RF-04", "RF-11", "RF-12", "RF-13",
    "RF-14", "RF-15", "RF-16", "RF-17", "RF-21",
}
EXPECTED_INTAKES = (
    "Lastenheft_META-LH-01-Programmquellen.md",
    "Lastenheft_META-LH-02-Portfolio-Ownership.md",
    "Lastenheft_META-LH-03-Authoring-Contract.md",
    "Lastenheft_META-LH-04-Series-Eligibility.md",
    "Lastenheft_META-LH-05-Erste-Welle.md",
    "Lastenheft_RAW-01-Reference-Agentic-Workspace.md",
    "Lastenheft_RAW-02-Workspace-Orchestrator.md",
    "Lastenheft_RAW-03-State-Truthfulness.md",
    "Lastenheft_RAW-04-Presentation-Fabric.md",
    "Lastenheft_RAW-05-Execution-Nodes.md",
    "Lastenheft_RAW-06-CLI-Environment-Orchestration.md",
    "Lastenheft_RAW-07-Hardware-Capability-Layer.md",
    "Lastenheft_RAW-08-Workflow-Engine.md",
    "Lastenheft_RAW-09-Preset-Evolution.md",
)
# Bind IDs explicitly so ordering and identity drift fail closed even if a
# filename convention changes later.
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
SEMANTIC_CRITERIA = {
    "germanFirst", "englishEquivalent", "cefrB2", "firstUseTerms",
    "domainTruth", "authorityInterpretation",
}
ACCESSIBILITY_CRITERIA = {
    "headingHierarchy", "linearReadingOrder", "descriptiveLinks", "textFirst",
    "statusNotColorOnly", "wcag22AAApplicability",
}
PUBLIC_CRITERIA = {
    "secretPatterns", "privatePaths", "unnecessaryPersonalData",
    "publicationSuitability",
}
CAUSAL_COMMAND_IDS = {
    "feature-pr-merge",
    "main-fast-forward-sync",
    "post-merge-actions",
    "archive-input-bindings-bash",
    "archive-input-bindings-powershell",
    "global-ready-14",
    "contract-tests-66",
    "domain",
    "run-state-bash",
    "run-state-powershell",
    "task-hash",
    "git-diff-check",
}


class ContractError(RuntimeError):
    """One precise fail-closed contract violation."""


def fail(message: str) -> None:
    raise ContractError(message)


def is_iso_calendar_date(value: str) -> bool:
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def load_json(path: Path, label: str) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        fail(f"{label} is not valid UTF-8 JSON: {exc}")
    if not isinstance(data, dict):
        fail(f"{label} root must be an object")
    return data


def read_text(path: Path, label: str) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        fail(f"{label} is not readable UTF-8 text: {exc}")


def raw_sha256(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError as exc:
        fail(f"cannot hash {path}: {exc}")


def normalized_sha256(path: Path) -> str:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]
    text = raw.decode("utf-8", errors="strict")
    if "\x00" in text:
        fail(f"binary NUL in {path}")
    return hashlib.sha256(text.replace("\r\n", "\n").replace("\r", "\n").encode()).hexdigest()


def repo_path(root: Path, value: str, label: str) -> Path:
    pure = PurePosixPath(value)
    if pure.is_absolute() or ".." in pure.parts or not value:
        fail(f"{label} must be a non-empty repository-relative path")
    return root / pure


def run_checked(command: list[str], root: Path, label: str) -> None:
    try:
        result = subprocess.run(command, cwd=root, text=True, capture_output=True, check=False)
    except OSError as exc:
        fail(f"{label} could not start: {exc}")
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip().splitlines()
        fail(f"{label} failed with exit {result.returncode}: {detail[0] if detail else 'no diagnostic'}")
    lines = [line for line in result.stdout.splitlines() if line.startswith("PASS:")]
    if len(lines) != 1:
        fail(f"{label} must emit exactly one PASS line; found {len(lines)}")


def table_rows(text: str, identifier: re.Pattern[str]) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in text.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
        if cells and identifier.fullmatch(cells[0]):
            rows.append(cells)
    return rows


def exact_ids(rows: list[list[str]], expected: set[str], label: str) -> None:
    ids = [row[0] for row in rows]
    missing = sorted(expected - set(ids))
    unexpected = sorted(set(ids) - expected)
    duplicates = sorted({value for value in ids if ids.count(value) > 1})
    if missing:
        fail(f"{label} missing IDs: {', '.join(missing)}")
    if unexpected:
        fail(f"{label} unexpected IDs: {', '.join(unexpected)}")
    if duplicates:
        fail(f"{label} duplicate IDs: {', '.join(duplicates)}")


def accepted_artifacts_by_path(state: dict[str, Any]) -> dict[str, str]:
    artifacts = state.get("acceptedArtifacts")
    if not isinstance(artifacts, list) or len(artifacts) != 3:
        fail("run state must contain exactly three acceptedArtifacts")
    result: dict[str, str] = {}
    for index, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            fail(f"acceptedArtifacts[{index}] must be an object")
        path, digest = artifact.get("path"), artifact.get("sha256")
        if not isinstance(path, str) or not re.fullmatch(r"[0-9a-f]{64}", str(digest)):
            fail(f"acceptedArtifacts[{index}] has an invalid path or SHA-256")
        if path in result:
            fail(f"acceptedArtifacts contains a duplicate path: {path}")
        result[path] = str(digest)
    return result


def validate_lifecycle_evidence(root: Path, record: dict[str, Any],
                                artifacts: dict[str, str]) -> None:
    original = str(record["originalPath"])
    normalized = str(record["originalNormalizedSha256"])
    receipt_binding = record.get("authoringReceipt")
    review_binding = record.get("readySingleReview")
    if not isinstance(receipt_binding, dict) or not isinstance(review_binding, dict):
        fail("lifecycle record needs authoringReceipt and readySingleReview objects")
    receipt_path = receipt_binding.get("path")
    review_path = review_binding.get("path")
    receipt_hash = receipt_binding.get("rawSha256")
    review_hash = review_binding.get("rawSha256")
    for label, value in (("authoringReceipt.rawSha256", receipt_hash),
                         ("readySingleReview.rawSha256", review_hash)):
        if not re.fullmatch(r"[0-9a-f]{64}", str(value)):
            fail(f"lifecycle {label} must be lowercase SHA-256")
    if artifacts.get(str(receipt_path)) != receipt_hash:
        fail("lifecycle Authoring Receipt binding differs from acceptedArtifacts")
    if artifacts.get(str(review_path)) != review_hash:
        fail("lifecycle Ready Single Review binding differs from acceptedArtifacts")
    receipt_file = repo_path(root, str(receipt_path), "lifecycle authoringReceipt.path")
    review_file = repo_path(root, str(review_path), "lifecycle readySingleReview.path")
    if raw_sha256(receipt_file) != receipt_hash:
        fail("lifecycle Authoring Receipt raw SHA-256 drift")
    if raw_sha256(review_file) != review_hash:
        fail("lifecycle Ready Single Review raw SHA-256 drift")

    receipt = load_json(receipt_file, "lifecycle Authoring Receipt")
    receipt_target = receipt.get("target")
    if (receipt.get("status") != "ReadyForReview" or not isinstance(receipt_target, dict)
            or receipt_target.get("path") != original
            or receipt_target.get("normalizedSha256") != normalized):
        fail("lifecycle Authoring Receipt is stale for the original logical target")

    review = load_json(review_file, "lifecycle Ready Single Review")
    targets = review.get("targets")
    if (review.get("mode") != "Single" or review.get("status") != "Ready"
            or not isinstance(targets, list) or len(targets) != 1
            or not isinstance(targets[0], dict)
            or targets[0].get("path") != original
            or targets[0].get("role") != "Primary"
            or targets[0].get("normalizedSha256") != normalized
            or review.get("findings") != [] or review.get("questions") != []
            or review.get("acceptedRisks") != []):
        fail("lifecycle Ready Single Review is stale or non-Ready for the original logical target")

    # These record-level bindings preserve the immutable evidence accepted by
    # the completed autonomous run. Current programme evidence is validated
    # independently through programmeEvidenceSnapshot and global-ready.


def resolve_meta01_target(root: Path, state: dict[str, Any]) -> tuple[str, str, dict[str, Any]]:
    binding = state.get("acceptedArtifactLifecycle")
    if not isinstance(binding, dict):
        fail("run state must bind acceptedArtifactLifecycle")
    if (binding.get("path") != LIFECYCLE or binding.get("schemaVersion") != "1.1"
            or binding.get("logicalTargetId") != LOGICAL_META01):
        fail("run-state lifecycle binding must name the exact META-LH-01 schema-1.1 contract")
    lifecycle = load_json(root / LIFECYCLE, "META-LH-01 lifecycle record")
    records = lifecycle.get("records")
    if (lifecycle.get("schemaVersion") != "1.1"
            or set(lifecycle) != {"schemaVersion", "records", "programmeEvidenceSnapshot"}
            or not isinstance(records, list) or len(records) != 1):
        fail("META-LH-01 lifecycle file must contain exactly one schema-1.1 record and one programme snapshot")
    record = records[0]
    required_keys = {
        "recordVersion", "logicalTargetId", "originalPath", "archivedPath",
        "originalRawSha256", "originalNormalizedSha256", "authoringReceipt",
        "readySingleReview", "runId", "branch",
    }
    if not isinstance(record, dict) or set(record) != required_keys:
        fail("META-LH-01 lifecycle record fields are incomplete or ambiguous")
    if record.get("recordVersion") != "1.0" or record.get("logicalTargetId") != LOGICAL_META01:
        fail("META-LH-01 lifecycle record version or logical target is invalid")
    if record.get("originalPath") != ORIGINAL_META01:
        fail("META-LH-01 lifecycle originalPath is not the accepted logical target")
    if state.get("runId") != EXPECTED_RUN_ID or state.get("branch") != EXPECTED_BRANCH:
        fail("autonomous run state differs from the accepted feature runId or branch")
    if record.get("branch") != state.get("branch") or record.get("runId") != state.get("runId"):
        fail("META-LH-01 lifecycle runId or branch differs from run state")
    expected_archive = ORIGINAL_META01.removesuffix(".md") + f".{state.get('branch')}.md"
    if record.get("archivedPath") != expected_archive or expected_archive != ARCHIVED_META01:
        fail("META-LH-01 lifecycle archivedPath has the wrong branch stamp")
    raw_digest = record.get("originalRawSha256")
    normalized_digest = record.get("originalNormalizedSha256")
    if not re.fullmatch(r"[0-9a-f]{64}", str(raw_digest)) or not re.fullmatch(
            r"[0-9a-f]{64}", str(normalized_digest)):
        fail("META-LH-01 lifecycle target hashes must be lowercase SHA-256")
    artifacts = accepted_artifacts_by_path(state)
    if artifacts.get(ORIGINAL_META01) != raw_digest:
        fail("META-LH-01 lifecycle raw hash differs from acceptedArtifacts")
    validate_lifecycle_evidence(root, record, artifacts)

    original_file = root / ORIGINAL_META01
    archived_file = root / ARCHIVED_META01
    original_exists, archived_exists = original_file.is_file(), archived_file.is_file()
    if original_exists == archived_exists:
        state_name = "both" if original_exists else "neither"
        fail(f"META-LH-01 original and archived paths must be mutually exclusive; found {state_name}")
    physical_path = ORIGINAL_META01 if original_exists else ARCHIVED_META01
    physical_file = root / physical_path
    if raw_sha256(physical_file) != raw_digest:
        fail(f"META-LH-01 {physical_path} raw SHA-256 does not match accepted bytes")
    if normalized_sha256(physical_file) != normalized_digest:
        fail(f"META-LH-01 {physical_path} normalized SHA-256 does not match accepted content")
    disposition = "Active" if original_exists else "Archived"
    return physical_path, disposition, record


def current_receipts(root: Path) -> dict[str, tuple[str, dict[str, Any]]]:
    receipts: dict[str, tuple[str, dict[str, Any]]] = {}
    for path in sorted((root / "specs/intake-authoring-receipts").glob("*.json")):
        data = load_json(path, f"receipt {path.name}")
        target = data.get("target")
        target_path = target.get("path") if isinstance(target, dict) else None
        if not isinstance(target_path, str):
            continue
        if target_path in receipts:
            fail(f"multiple current Authoring Receipts target {target_path}")
        receipts[target_path] = (path.relative_to(root).as_posix(), data)
    return receipts


def validate_programme_evidence_snapshot(
        root: Path, state: dict[str, Any], meta_physical: str) -> dict[str, dict[str, Any]]:
    lifecycle = load_json(root / LIFECYCLE, "programme evidence lifecycle")
    snapshot = lifecycle.get("programmeEvidenceSnapshot")
    if not isinstance(snapshot, dict) or set(snapshot) != {
            "snapshotVersion", "runId", "branch", "orderedLogicalTargets"}:
        fail("programme evidence snapshot fields are incomplete or ambiguous")
    if snapshot.get("snapshotVersion") != "1.0":
        fail("programme evidence snapshotVersion must be 1.0")
    if snapshot.get("runId") != state.get("runId"):
        fail("programme evidence snapshot runId differs from run state")
    if snapshot.get("branch") != state.get("branch"):
        fail("programme evidence snapshot branch differs from run state")

    ordered = snapshot.get("orderedLogicalTargets")
    if not isinstance(ordered, list):
        fail("programme evidence snapshot orderedLogicalTargets must be an array")
    expected_ids = [logical_id for logical_id, _ in PROGRAMME_TARGETS]
    actual_ids = [entry.get("logicalTargetId") if isinstance(entry, dict) else None
                  for entry in ordered]
    if len(actual_ids) != len(set(actual_ids)):
        fail("programme evidence snapshot contains duplicate logical targets")
    if set(actual_ids) == set(expected_ids) and actual_ids != expected_ids:
        fail("programme evidence snapshot logical targets are reordered")
    if actual_ids != expected_ids:
        fail("programme evidence snapshot must contain the exact 14 ordered logical targets")

    reviews = current_single_reviews(root)
    receipts = current_receipts(root)
    by_target: dict[str, dict[str, Any]] = {}
    for index, ((logical_id, expected_target), entry) in enumerate(zip(PROGRAMME_TARGETS, ordered)):
        label = f"programmeEvidenceSnapshot.orderedLogicalTargets[{index}]"
        if not isinstance(entry, dict) or set(entry) != {
                "logicalTargetId", "target", "authoringReceipt", "readySingleReview"}:
            fail(f"{label} fields are incomplete or ambiguous")
        if entry.get("logicalTargetId") != logical_id:
            fail(f"{label}.logicalTargetId is invalid")
        target_binding = entry.get("target")
        receipt_binding = entry.get("authoringReceipt")
        review_binding = entry.get("readySingleReview")
        for binding_label, binding in (("target", target_binding),
                                       ("authoringReceipt", receipt_binding),
                                       ("readySingleReview", review_binding)):
            if not isinstance(binding, dict) or set(binding) != {"path", "normalizedSha256" if binding_label == "target" else "rawSha256"}:
                fail(f"{label}.{binding_label} fields are incomplete or ambiguous")
        if target_binding.get("path") != expected_target:
            fail(f"{label}.target.path differs from the exact programme target")
        target_hash = target_binding.get("normalizedSha256")
        if not re.fullmatch(r"[0-9a-f]{64}", str(target_hash)):
            fail(f"{label}.target.normalizedSha256 must be lowercase SHA-256")
        physical_target = meta_physical if expected_target == ORIGINAL_META01 else expected_target
        if normalized_sha256(repo_path(root, physical_target, f"{label}.target.path")) != target_hash:
            fail(f"{label}.target normalized SHA-256 drift")

        receipt_path = receipt_binding.get("path")
        receipt_hash = receipt_binding.get("rawSha256")
        review_path = review_binding.get("path")
        review_hash = review_binding.get("rawSha256")
        for hash_label, digest in (("authoringReceipt.rawSha256", receipt_hash),
                                   ("readySingleReview.rawSha256", review_hash)):
            if not re.fullmatch(r"[0-9a-f]{64}", str(digest)):
                fail(f"{label}.{hash_label} must be lowercase SHA-256")

        current_receipt = receipts.get(expected_target)
        if current_receipt is None or current_receipt[0] != receipt_path:
            fail(f"{label}.authoringReceipt.path is not the unique current receipt")
        receipt_file = repo_path(root, str(receipt_path), f"{label}.authoringReceipt.path")
        if raw_sha256(receipt_file) != receipt_hash:
            fail(f"{label}.authoringReceipt raw SHA-256 drift")
        receipt = current_receipt[1]
        receipt_target = receipt.get("target")
        if (receipt.get("status") != "ReadyForReview" or not isinstance(receipt_target, dict)
                or receipt_target.get("path") != expected_target
                or receipt_target.get("normalizedSha256") != target_hash):
            fail(f"{label}.authoringReceipt is not ReadyForReview for the snapshot target")

        current_review = reviews.get(expected_target)
        if current_review is None or current_review[0] != review_path:
            fail(f"{label}.readySingleReview.path is not the unique current review leaf")
        review_file = repo_path(root, str(review_path), f"{label}.readySingleReview.path")
        if raw_sha256(review_file) != review_hash:
            fail(f"{label}.readySingleReview raw SHA-256 drift")
        review = current_review[1]
        targets = review.get("targets")
        if (review.get("mode") != "Single" or review.get("status") != "Ready"
                or not isinstance(targets, list) or len(targets) != 1
                or not isinstance(targets[0], dict)
                or targets[0].get("path") != expected_target
                or targets[0].get("role") != "Primary"
                or targets[0].get("normalizedSha256") != target_hash
                or review.get("findings") != [] or review.get("questions") != []
                or review.get("acceptedRisks") != []):
            fail(f"{label}.readySingleReview is not Single/Primary/Ready with empty blockers")
        by_target[expected_target] = entry
    return by_target


def snapshot_replacement_is_qualified(root: Path, state: dict[str, Any],
                                      meta_physical: str) -> bool:
    if (state.get("stage") != "Implement" or state.get("status") != "Active"
            or state.get("lastPassingGate") != "GlobalReadyBeforeImplement"):
        return False
    branch = subprocess.run(
        ["git", "branch", "--show-current"], cwd=root, text=True,
        capture_output=True, check=False,
    ) if (root / ".git").exists() else None
    if branch is not None and (branch.returncode or branch.stdout.strip() != state.get("branch")):
        fail("programme evidence snapshot branch differs from the current Git branch")
    validate_programme_evidence_snapshot(root, state, meta_physical)
    return True


def run_review_surface(root: Path, surface: str, review: str,
                       logical_target: str, physical_target: str,
                       label: str) -> None:
    """Run one installed review validator without changing the repository.

    Archived META-LH-01 evidence still names the immutable original logical
    path. A short-lived external projection supplies exactly the validated
    archive bytes at that path and exposes the unchanged review evidence via a
    read-only directory symlink. All other targets use the real repository.
    """
    surface_name = "Bash" if surface.lower() == "bash" else "PowerShell"
    review_repo = "."
    if logical_target != ORIGINAL_META01 or physical_target == ORIGINAL_META01:
        if surface_name == "Bash":
            command = ["bash", ".specify/presets/intake-review-governance/scripts/validate-intake-review-result.sh",
                       "--result", review, "--repo", review_repo]
        else:
            command = ["pwsh", "-NoProfile", "-File",
                       ".specify/presets/intake-review-governance/scripts/validate-intake-review-result.ps1",
                       "-Result", review, "-Repo", review_repo]
        run_checked(command, root, label)
        return

    if physical_target != ARCHIVED_META01:
        fail("archived review projection received an unexpected physical target")
    with tempfile.TemporaryDirectory(prefix="meta-lh-01-review-projection-") as temporary:
        projection = Path(temporary)
        (projection / "specs").symlink_to((root / "specs").resolve(), target_is_directory=True)
        projected_target = projection / ORIGINAL_META01
        projected_target.parent.mkdir(parents=True, exist_ok=True)
        projected_target.symlink_to((root / physical_target).resolve())
        review_repo = str(projection)
        if surface_name == "Bash":
            command = ["bash", ".specify/presets/intake-review-governance/scripts/validate-intake-review-result.sh",
                       "--result", review, "--repo", review_repo]
        else:
            command = ["pwsh", "-NoProfile", "-File",
                       ".specify/presets/intake-review-governance/scripts/validate-intake-review-result.ps1",
                       "-Result", review, "-Repo", review_repo]
        run_checked(command, root, label)


def validate_input_bindings(root: Path, surface: str) -> str:
    state_path = root / STATE
    state = load_json(state_path, "autonomous run state")
    artifacts = accepted_artifacts_by_path(state)
    physical_target, disposition, record = resolve_meta01_target(root, state)
    snapshot_qualified = snapshot_replacement_is_qualified(root, state, physical_target)
    receipt = str(record["authoringReceipt"]["path"])
    review = str(record["readySingleReview"]["path"])
    if set(artifacts) != {ORIGINAL_META01, receipt, review}:
        fail("acceptedArtifacts must bind exactly the original intake, accepted review, and receipt")
    if surface == "bash":
        commands = [
            (["bash", ".specify/presets/autonomous-run-governance/scripts/validate-autonomous-run-state.sh", "--state", STATE], "Bash run-state validator"),
        ]
        if disposition == "Active" and not snapshot_qualified:
            commands.extend((
                (["bash", ".specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.sh", "--receipt", receipt, "--repo", "."], "Bash receipt validator"),
                (["bash", ".specify/presets/intake-review-governance/scripts/validate-intake-review-result.sh", "--result", review, "--repo", "."], "Bash review validator")
            ))
    else:
        commands = [
            (["pwsh", "-NoProfile", "-File", ".specify/presets/autonomous-run-governance/scripts/validate-autonomous-run-state.ps1", "-State", STATE], "PowerShell run-state validator"),
        ]
        if disposition == "Active" and not snapshot_qualified:
            commands.extend((
                (["pwsh", "-NoProfile", "-File", ".specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.ps1", "-Receipt", receipt, "-Repo", "."], "PowerShell receipt validator"),
                (["pwsh", "-NoProfile", "-File", ".specify/presets/intake-review-governance/scripts/validate-intake-review-result.ps1", "-Result", review, "-Repo", "."], "PowerShell review validator")
            ))
    for command, label in commands:
        run_checked(command, root, label)
    if snapshot_qualified:
        surface_name = "Bash" if surface == "bash" else "PowerShell"
        run_review_surface(root, surface_name, review, ORIGINAL_META01,
                           physical_target, f"{surface_name} review validator")
    proof = "programme snapshot" if snapshot_qualified else "generic receipt freshness"
    return f"three logical accepted artifacts, {disposition.lower()} target at {physical_target}, {surface} schema/review surfaces, and {proof}"


def current_single_reviews(root: Path) -> dict[str, tuple[str, dict[str, Any]]]:
    directory = root / "specs/intake-review-results"
    records: list[tuple[str, dict[str, Any], str]] = []
    for path in sorted(directory.glob("*.json")):
        data = load_json(path, f"review result {path.name}")
        targets = data.get("targets")
        if data.get("mode") != "Single" or not isinstance(targets, list) or len(targets) != 1:
            continue
        target = targets[0].get("path") if isinstance(targets[0], dict) else None
        if isinstance(target, str):
            records.append((path.relative_to(root).as_posix(), data, target))
    superseded = {data.get("supersedes") for _, data, _ in records if data.get("supersedes") != "N/A"}
    result: dict[str, tuple[str, dict[str, Any]]] = {}
    for target in {record[2] for record in records}:
        leaves = [(path, data) for path, data, item_target in records
                  if item_target == target and path not in superseded]
        if len(leaves) == 1:
            result[target] = leaves[0]
        elif target.startswith("requirements/intakes/active/"):
            fail(f"active target {target} needs exactly one non-superseded Single review; found {len(leaves)}")
    return result


def validate_global_ready(root: Path) -> str:
    active_dir = root / "requirements/intakes/active"
    targets = tuple(f"requirements/intakes/active/{name}" for name in EXPECTED_INTAKES)
    state = load_json(root / STATE, "autonomous run state")
    meta_physical, meta_disposition, _ = resolve_meta01_target(root, state)
    snapshot_qualified = snapshot_replacement_is_qualified(root, state, meta_physical)
    physical_targets = {target: target for target in targets}
    physical_targets[ORIGINAL_META01] = meta_physical
    actual = {path.relative_to(root).as_posix() for path in active_dir.glob("Lastenheft_*.md")}
    if actual != set(physical_targets.values()):
        fail(f"global Ready gate physical target set drift; expected 14 logical targets, got {len(actual)} paths")
    if not targets[0].endswith("META-LH-01-Programmquellen.md"):
        fail("META-LH-01 must remain the first global-gate target")
    reviews = current_single_reviews(root)
    receipts = current_receipts(root)
    for target in targets:
        target_file = root / physical_targets[target]
        digest = normalized_sha256(target_file)
        if target not in reviews:
            fail(f"missing current Single review: {target}")
        review_path, review = reviews[target]
        review_target = review["targets"][0]
        if review.get("status") != "Ready":
            fail(f"current review is not Ready: {review_path}")
        if review.get("mode") != "Single" or review_target.get("role") != "Primary":
            fail(f"current review must be Single with Primary target: {review_path}")
        if review_target.get("normalizedSha256") != digest:
            fail(f"current review target hash drift: {review_path}")
        for field in ("findings", "questions", "acceptedRisks"):
            if review.get(field) != []:
                fail(f"current Ready review {review_path} must have empty {field}")
        if target not in receipts:
            fail(f"missing current Authoring Receipt: {target}")
        receipt_path, receipt = receipts[target]
        if receipt.get("status") != "ReadyForReview":
            fail(f"receipt is not ReadyForReview: {receipt_path}")
        receipt_target = receipt.get("target", {})
        if receipt_target.get("path") != target or receipt_target.get("normalizedSha256") != digest:
            fail(f"receipt target path/hash drift: {receipt_path}")
        if target == ORIGINAL_META01 and meta_disposition == "Archived" and not snapshot_qualified:
            continue
        for surface, receipt_command in (
            ("Bash",
             ["bash", ".specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.sh", "--receipt", receipt_path, "--repo", "."]),
            ("PowerShell",
             ["pwsh", "-NoProfile", "-File", ".specify/presets/intake-authoring-governance/scripts/validate-intake-authoring-receipt.ps1", "-Receipt", receipt_path, "-Repo", "."]),
        ):
            if not snapshot_qualified:
                run_checked(receipt_command, root, f"{surface} receipt validator for {target}")
            run_review_surface(root, surface, review_path, target,
                               physical_targets[target],
                               f"{surface} review validator for {target}")
    proof = "qualified immutable programme snapshot" if snapshot_qualified else "generic receipt freshness"
    return f"14 logical Ready targets with {meta_disposition.lower()} META-LH-01 resolution, {proof}, and Bash/PowerShell review surfaces"


def require_bilingual(cells: Iterable[str], label: str) -> None:
    for value in cells:
        if " / " not in value:
            fail(f"{label} must contain separate German / English values")


def validate_domain(root: Path) -> str:
    texts = {path: read_text(root / path, path) for path in DOMAIN_PATHS}
    source_rows = table_rows(texts[DOMAIN_PATHS[0]], re.compile(r"SRC-(?:\d{3}|ES-01)"))
    exact_ids(source_rows, EXPECTED_SOURCES, "source inventory")
    for row in source_rows:
        if len(row) != 7 or any(not cell for cell in row):
            fail(f"source {row[0]} needs ID plus six separate non-empty fields")
        require_bilingual(row[1:], f"source {row[0]}")
    constraint_rows = table_rows(texts[DOMAIN_PATHS[1]], re.compile(r"CON-\d{2}"))
    exact_ids(constraint_rows, {f"CON-{number:02d}" for number in range(1, 26)}, "constraint register")
    for row in constraint_rows:
        if len(row) != 3 or any(not cell for cell in row):
            fail(f"constraint {row[0]} needs ID, statement, and evidence")
        require_bilingual(row[1:], f"constraint {row[0]}")

    finding_rows = table_rows(texts[DOMAIN_PATHS[2]], re.compile(r"RF-\d{2}"))
    exact_ids(finding_rows, EXPECTED_FINDINGS, "findings ledger")
    for row in finding_rows:
        if len(row) != 10 or any(not cell for cell in row):
            fail(f"finding {row[0]} needs ten separate non-empty fields")
        require_bilingual(row[2:], f"finding {row[0]}")
        if row[1].lower().startswith("blocking") and row[8] == "Uncovered":
            fail(f"blocking finding {row[0]} must not be Uncovered")

    coverage = texts[DOMAIN_PATHS[3]]
    source_coverage = table_rows(coverage, re.compile(r"SRC-(?:\d{3}|ES-01)"))
    finding_coverage = table_rows(coverage, re.compile(r"RF-\d{2}"))
    exact_ids(source_coverage, EXPECTED_SOURCES, "source coverage")
    exact_ids(finding_coverage, EXPECTED_FINDINGS, "finding coverage")
    for row in source_coverage + finding_coverage:
        if len(row) != 5 or any(not cell for cell in row):
            fail(f"coverage {row[0]} needs five separate non-empty fields")
        if row[3] != "Covered":
            fail(f"coverage {row[0]} must be Covered")
    if {row[0] for row in finding_coverage if row[4] == "Yes"} != DIRECT_META:
        fail("direct META-LH-01 ownership must equal the exact ten-finding set")
    for row in finding_coverage:
        expected = "Yes" if row[0] in DIRECT_META else "No"
        if row[4] != expected:
            fail(f"wrong direct META-LH-01 ownership for {row[0]}: expected {expected}")

    glossary_rows = table_rows(texts[DOMAIN_PATHS[4]], re.compile(r".+"))
    glossary = {row[0]: row for row in glossary_rows if len(row) == 3}
    for term in ("Autorität", "Evidence", "Receipt", "Coverage", "Stop-Gate"):
        if term not in glossary or " / " not in glossary[term][2]:
            fail(f"glossary needs a bilingual explanation for {term}")

    gate_rows = table_rows(texts[DOMAIN_PATHS[5]], re.compile(r"G-\d{2}(?: .+)?"))
    by_gate = {row[0].split()[0]: row for row in gate_rows}
    for gate_id in ("G-01", "G-05", "G-06"):
        row = by_gate.get(gate_id)
        if row is None:
            fail(f"authority gate missing: {gate_id}")
        if len(row) != 6 or any(not cell for cell in row):
            fail(f"authority gate {gate_id} needs allowed action, stop, evidence, human decision, and one next action")
        require_bilingual(row[1:], f"authority gate {gate_id}")
    if "14" not in " ".join(by_gate["G-05"]) or "Ready" not in " ".join(by_gate["G-05"]):
        fail("G-05 must bind the 14-intake Ready gate")
    if "Produktcode" not in " ".join(by_gate["G-06"]) or "product code" not in " ".join(by_gate["G-06"]).lower():
        fail("G-06 must preserve the product-code exclusion")
    return "six domain files, 23 sources, 21 findings, ten direct owners, complete fields, and gates"


def expected_paths(path: Path) -> set[str]:
    lines = {line.strip() for line in read_text(path, "expected paths").splitlines()
             if line.strip() and not line.lstrip().startswith("#")}
    if not lines:
        fail("expected paths file must contain at least one path")
    for value in lines:
        repo_path(Path("."), value, "expected path")
    return lines


def delivery_inventory(root: Path, expected_path_file: Path) -> set[str]:
    state = load_json(root / STATE, "autonomous run state")
    _, _, record = resolve_meta01_target(root, state)
    return expected_paths(expected_path_file) | {
        str(record["originalPath"]), str(record["archivedPath"]), LIFECYCLE,
    }


def validate_review_evidence(root: Path, evidence_path: Path, expected_path_file: Path, kind: str) -> str:
    data = load_json(evidence_path, "independent review evidence")
    if data.get("schemaVersion") != "1.0":
        fail("independent review evidence schemaVersion must be 1.0")
    reviewer = data.get("reviewer")
    if not isinstance(reviewer, dict) or reviewer.get("independent") is not True:
        fail("reviewer.independent must be true")
    for field in ("role", "independenceStatement"):
        if not isinstance(reviewer.get(field), str) or not reviewer[field].strip():
            fail(f"reviewer.{field} must be non-empty")
    if kind == "semantic":
        key, criteria, required_paths = "semanticReviews", SEMANTIC_CRITERIA, set(REVIEW_PATHS)
    elif kind == "accessibility":
        key, criteria, required_paths = (
            "accessibilityReviews", ACCESSIBILITY_CRITERIA, set(REVIEW_PATHS)
        )
    else:
        key, criteria, required_paths = (
            "publicContentReviews", PUBLIC_CRITERIA,
            delivery_inventory(root, expected_path_file),
        )
    rows = data.get(key)
    if not isinstance(rows, list):
        fail(f"{key} must be an array")
    actual_paths: list[str] = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(f"{key}[{index}] must be an object")
        path = row.get("path")
        actual_paths.append(str(path))
        values = row.get("criteria")
        if not isinstance(values, dict) or set(values) != criteria:
            fail(f"{key}[{index}].criteria must contain exactly {', '.join(sorted(criteria))}")
        if any(value != "Pass" for value in values.values()):
            fail(f"{key}[{index}] contains a non-Pass criterion")
        if not isinstance(row.get("rationale"), str) or not row["rationale"].strip():
            fail(f"{key}[{index}].rationale must be non-empty")
    if len(actual_paths) != len(set(actual_paths)) or set(actual_paths) != required_paths:
        fail(f"{key} path coverage must exactly match {len(required_paths)} required paths")
    if data.get("blockingFindings") != []:
        fail("independent review evidence must have zero blockingFindings")
    return f"structured independent {kind} review for {len(required_paths)} paths"


def validate_documentation_impact(root: Path, evidence_path: Path, expected_path_file: Path) -> str:
    data = load_json(evidence_path, "Documentation Impact evidence")
    if data.get("schemaVersion") != "1.1":
        fail("Documentation Impact schemaVersion must be 1.1")
    entries = data.get("entries")
    if not isinstance(entries, list) or len(entries) != 1:
        fail(f"Documentation Impact needs exactly one entry; found {len(entries) if isinstance(entries, list) else 0}")
    entry = entries[0]
    if not isinstance(entry, dict) or entry.get("decision") != "UpdateRequired":
        fail("the single Documentation Impact decision must be UpdateRequired")
    actual = entry.get("documents")
    required = delivery_inventory(root, expected_path_file)
    if not isinstance(actual, list) or len(actual) != len(set(actual)) or set(actual) != required:
        fail("Documentation Impact documents must exactly match the planned candidate inventory")
    canonical = entry.get("canonicalSource")
    expected_canonical = "requirements/intakes/active/Lastenheft_META-LH-01-Programmquellen.md"
    if canonical != expected_canonical:
        fail(f"Documentation Impact canonicalSource must be {expected_canonical}")
    required_fields = (
        "changeId", "scope", "rationale", "owner", "audiences", "readerPaths",
        "navigationImpact", "documentClass", "languageStrategy", "languagePartners",
        "platformAndExampleProof", "distributionClass", "homeSyncRequired", "evidence",
        "risk", "criticality", "reevaluationTrigger",
    )
    for field in required_fields:
        if field not in entry or entry[field] in (None, ""):
            fail(f"Documentation Impact entry missing complete field: {field}")
    for surface, command in (
        ("Bash", ["bash", "scripts/validate-documentation-impact.sh", "--evidence", str(evidence_path)]),
        ("PowerShell", ["pwsh", "-NoProfile", "-File", "scripts/validate-documentation-impact.ps1", "-Evidence", str(evidence_path)]),
    ):
        run_checked(command, root, f"{surface} Documentation Impact validator")
    return f"schema 1.1, one entry, canonical intake, and {len(required)} planned paths"


def extract_json_block(text: str, label: str) -> dict[str, Any]:
    blocks = re.findall(r"```aeps-outcome-json\s*\n(.*?)\n```", text, flags=re.DOTALL)
    if len(blocks) != 1:
        fail(f"{label} must contain exactly one aeps-outcome-json block")
    try:
        data = json.loads(blocks[0])
    except json.JSONDecodeError as exc:
        fail(f"{label} AEPS block is invalid JSON: {exc}")
    if not isinstance(data, dict):
        fail(f"{label} AEPS block must be an object")
    return data


def validate_aeps_ledger_section(ledger: str, finding_id: str, source_path: str,
                                 receipt_path: str, maturity: str) -> None:
    headings = list(re.finditer(r"(?m)^##\s+AEPS-FIND-AOC-\d{3}\b.*$", ledger))
    matches = [item for item in headings if finding_id in item.group(0)]
    if len(matches) != 1 or len(re.findall(rf"\b{re.escape(finding_id)}\b", ledger)) != 1:
        fail("AEPS findingId must occur exactly once as its canonical ledger heading")
    start = matches[0].start()
    later = [item.start() for item in headings if item.start() > start]
    section = ledger[start:min(later) if later else len(ledger)]
    field_rows = [
        (match.group("label").strip(), match.group("value").strip())
        for match in re.finditer(
            r"(?ms)^-\s+\*\*(?P<label>[^*\n]+?):\*\*\s*(?P<value>.*?)(?=^-\s+\*\*|^##\s|\Z)",
            section,
        )
    ]
    required_patterns = {
        "source": r"(?:^|/)\s*(?:Quelle(?:\s+und\s+Lastenheft)?|Source(?:\s+and\s+intake)?)\b",
        "date and commit": r"(?:^|/)\s*(?:Datum\s+und\s+(?:Repository-)?Commit|Date\s+and\s+commit)\b",
        "problem or observation": r"(?:^|/)\s*(?:Problem(?:\s+oder\s+Beobachtung)?|Problem\s+or\s+observation)\b",
        "context": r"(?:^|/)\s*(?:Kontext(?:\s+und\s+Randbedingungen)?|Context(?:\s+and\s+constraints)?)\b",
        "positive evidence": r"(?:^|/)\s*Positive Evidence\b",
        "negative evidence": r"(?:^|/)\s*Negative Evidence\b",
        "limits": r"(?:^|/)\s*(?:Grenzen|Limits)\b",
        "AOC-specific versus generic": r"(?:^|/)\s*(?:AOC-spezifisch(?:\s+versus\s+generisch)?|AOC-specific(?:\s+versus\s+generic)?)\b",
        "domain": r"(?:^|/)\s*(?:AEPS-Dom.ne|AEPS Domain)\b",
        "maturity": r"(?:^|/)\s*(?:Reifegrad|Maturity)\b",
        "related presets": r"(?:^|/)\s*(?:Preset-Bezug|Related presets)\b",
        "next validation": r"(?:^|/)\s*(?:N.chste Validierung|Next validation)\b",
        "promotion blockers": r"(?:^|/)\s*(?:Promotion-Blocker|Promotion blockers?)\b",
        "capture status": r"(?:^|/)\s*(?:Erfassungsstatus|Capture status)\b",
        "upstream status": r"(?:^|/)\s*(?:Upstream-Status|Upstream status)\b",
    }

    def required_field(label: str, pattern: str) -> str:
        values = [value for field_label, value in field_rows
                  if re.search(pattern, field_label, flags=re.IGNORECASE)]
        if not values:
            fail(f"AEPS ledger section missing required field: {label}")
        if len(values) != 1:
            fail(f"AEPS ledger section duplicates required field: {label}")
        value = values[0]
        semantic_value = re.sub(r"[`*_~\s.;,:/|()-]", "", value)
        if not semantic_value:
            fail(f"AEPS ledger section has empty required value: {label}")
        return value

    values = {
        label: required_field(label, pattern)
        for label, pattern in required_patterns.items()
    }
    capture_states = (
        "AlreadyRecorded", "NotRecorded", "PartiallyRecorded", "AocSpecific",
        "PotentialCandidate", "MoreEvidenceRequired",
    )
    upstream_states = (
        "NotApplicable", "PendingPublication", "PendingAuthority", "Recommended",
        "Posted", "Superseded",
    )
    capture_tokens = re.findall(r"`([^`\n]+)`", values["capture status"])
    upstream_tokens = re.findall(r"`([^`\n]+)`", values["upstream status"])
    if len(capture_tokens) != 1 or capture_tokens[0] not in capture_states:
        fail("AEPS ledger section missing a valid capture status")
    if len(upstream_tokens) != 1 or upstream_tokens[0] not in upstream_states:
        fail("AEPS ledger section missing a valid upstream status")
    maturity_tokens = re.findall(r"`([^`\n]+)`", values["maturity"])
    if maturity_tokens != [maturity]:
        fail("AEPS ledger maturity must match the receipt outcome")
    source_value = values["source"]
    source_tokens = re.findall(r"`([^`\n]+)`", source_value)
    if source_tokens != [source_path, receipt_path]:
        fail("AEPS ledger section must bind both sourcePath and receipt path")
    date_tokens = re.findall(r"`([^`\n]+)`", values["date and commit"])
    published_binding = (
        len(date_tokens) == 2
        and is_iso_calendar_date(date_tokens[0])
        and re.fullmatch(r"[0-9a-f]{40,64}", date_tokens[1])
    )
    pending_binding = (
        len(date_tokens) == 4
        and is_iso_calendar_date(date_tokens[0])
        and date_tokens[1] == "PendingPublication"
        and re.fullmatch(r"[0-9a-f]{40}", date_tokens[2])
        and re.fullmatch(r"[0-9a-f]{64}", date_tokens[3])
        and re.search(r"\bBase-HEAD\b", values["date and commit"], flags=re.IGNORECASE)
        and re.search(r"\bSHA-256\b", values["date and commit"], flags=re.IGNORECASE)
    )
    if not (published_binding or pending_binding):
        fail("AEPS ledger date and commit must bind a published commit or PendingPublication evidence")
    preset_value = values["related presets"]
    preset_tokens = re.findall(r"`([^`\n]+)`", preset_value)
    if re.search(r"(?<![A-Za-z0-9_/])N/A(?![A-Za-z0-9_/])", preset_value,
                 flags=re.IGNORECASE):
        rationale_match = re.search(
            r"\b(?:weil|because|begruendet|begr.ndet|rationale)\b"
            r"\s*(?::|durch|by)?\s*(?P<reason>.+)",
            preset_value,
            flags=re.IGNORECASE,
        )
        rationale = rationale_match.group("reason") if rationale_match else ""
        semantic_rationale = re.sub(r"[`*_~\s.;,:/|()-]", "", rationale)
        if (preset_tokens and preset_tokens != ["N/A"]) or len(semantic_rationale) < 3:
            fail("AEPS ledger N/A preset relation needs an explicit rationale")


def validate_aeps(root: Path, receipt_path: Path) -> str:
    outcome = extract_json_block(read_text(receipt_path, "AEPS receipt"), "AEPS receipt")
    required = ("schemaVersion", "outcome", "trigger", "capturedAt", "sourcePath",
                "sourceSha256", "deduplicationKey", "rationale", "maturity",
                "presetPromotion", "level0Handoff")
    for field in required:
        if field not in outcome or outcome[field] in (None, ""):
            fail(f"AEPS outcome missing field: {field}")
    if outcome["schemaVersion"] != "1.0" or outcome["outcome"] not in ("Finding", "NoChange"):
        fail("AEPS outcome must use schema 1.0 and Finding or NoChange")
    if outcome["presetPromotion"] is not False or outcome["level0Handoff"] is not False:
        fail("AEPS outcome must not claim preset promotion or level-0 handoff")
    if outcome["maturity"] not in ("observation", "pilot-pattern", "candidate"):
        fail("AEPS maturity exceeds the single-AOC-run boundary")
    source_path = str(outcome["sourcePath"])
    source = repo_path(root, source_path, "AEPS sourcePath")
    if raw_sha256(source) != outcome["sourceSha256"]:
        fail("AEPS sourceSha256 is stale")
    captured_date = str(outcome["capturedAt"])[:10]
    if not is_iso_calendar_date(captured_date):
        fail("AEPS capturedAt must begin with an ISO date")
    if outcome["trigger"] == "ReadyReview":
        review = load_json(source, "AEPS Ready review source")
        targets = review.get("targets")
        if (not isinstance(review.get("reviewId"), str) or not isinstance(targets, list)
                or len(targets) != 1 or not isinstance(targets[0], dict)):
            fail("AEPS ReadyReview source must bind one reviewId and one target")
        target_path = targets[0].get("path")
        target_hash = targets[0].get("normalizedSha256")
        if not isinstance(target_path, str) or not re.fullmatch(r"[0-9a-f]{64}", str(target_hash)):
            fail("AEPS ReadyReview target path/hash is incomplete")
        expected_key = f"{review['reviewId']} + {target_path} + {target_hash}"
    else:
        expected_key = f"{source_path} + {normalized_sha256(source)} + {captured_date}"
    if outcome["deduplicationKey"] != expected_key:
        fail(f"AEPS deduplicationKey must equal the canonical {outcome['trigger']} key")
    duplicate_receipts = []
    receipt_resolved = receipt_path.resolve()
    for other in sorted((root / "docs/aeps/receipts").glob("*.md")):
        if other.resolve() != receipt_resolved and expected_key in read_text(other, f"AEPS receipt {other.name}"):
            duplicate_receipts.append(other.relative_to(root).as_posix())
    if duplicate_receipts:
        fail(f"AEPS deduplicationKey already exists in: {', '.join(duplicate_receipts)}")
    finding_id = outcome.get("findingId")
    if outcome["outcome"] == "Finding":
        if not isinstance(finding_id, str) or not re.fullmatch(r"AEPS-FIND-AOC-\d{3}", finding_id):
            fail("AEPS Finding outcome needs one valid findingId")
        ledger = read_text(root / "docs/aeps/findings-ledger.md", "AEPS ledger")
        receipt_relative = receipt_path.resolve().relative_to(root.resolve()).as_posix()
        validate_aeps_ledger_section(
            ledger, finding_id, source_path, receipt_relative, str(outcome["maturity"])
        )
    elif finding_id not in (None, "N/A"):
        fail("AEPS NoChange outcome must not contain a findingId")
    return f"one bounded AEPS {outcome['outcome']} outcome"


def parse_porcelain_z(value: bytes) -> list[tuple[str, str]]:
    parts = value.split(b"\0")
    rows: list[tuple[str, str]] = []
    index = 0
    while index < len(parts) and parts[index]:
        entry = parts[index].decode("utf-8", errors="strict")
        status, path = entry[:2], entry[3:]
        rows.append((status, path))
        if status[0] in "RC" or status[1] in "RC":
            index += 1
        index += 1
    return rows


def validate_candidate_inventory(staged: set[str], status_rows: list[tuple[str, str]],
                                 expected: set[str], allowed: set[str]) -> None:
    if not expected <= allowed:
        fail(f"expected candidate has paths outside allowlist: {', '.join(sorted(expected - allowed))}")
    if staged != expected:
        fail(f"staged paths differ from expected candidate; missing={sorted(expected-staged)}, unexpected={sorted(staged-expected)}")
    for status, path in status_rows:
        staged_state, worktree_state = status[0], status[1]
        if staged_state not in (" ", "?") and path not in expected:
            fail(f"unexpected staged path: {path}")
        if path in expected and worktree_state not in (" ", "?"):
            fail(f"candidate path still has unstaged changes: {path}")
        if path in allowed and path not in expected:
            fail(f"allowlisted feature path escaped the declared candidate: {path}")


def validate_candidate_fixpoint_inventory(status_rows: list[tuple[str, str]],
                                           expected: set[str], allowed: set[str]) -> None:
    if not expected <= allowed:
        fail(f"expected candidate has paths outside allowlist: {', '.join(sorted(expected - allowed))}")
    changed = {path for _, path in status_rows}
    actual = changed & allowed
    if actual != expected:
        fail(f"candidate fixed point differs; missing={sorted(expected-actual)}, unexpected={sorted(actual-expected)}")
    bounded = (
        "requirements/baseline/", "requirements/intakes/active/", FEATURE + "/", "docs/aeps/",
        "docs/project-statistics.md", "docs/scripts/embedded-scripts.md",
    )
    unexpected = sorted(path for path in changed if path.startswith(bounded) and path not in allowed)
    if unexpected:
        fail(f"changed META-LH-01 path outside allowlist: {', '.join(unexpected)}")


def validate_candidate_fixpoint(root: Path, allowlist_path: Path,
                                expected_path_file: Path) -> str:
    allowlist = load_json(allowlist_path, "candidate allowlist")
    if allowlist.get("schemaVersion") != "1.0" or not isinstance(allowlist.get("allowedPaths"), list):
        fail("candidate allowlist needs schemaVersion 1.0 and allowedPaths")
    expected = expected_paths(expected_path_file)
    required_evidence = {
        LIFECYCLE,
        CAUSAL_CLOSEOUT,
        f"{FEATURE}/semantic-review-evidence.json",
        f"{FEATURE}/accessibility-review-evidence.json",
        f"{FEATURE}/public-content-review-evidence.json",
        f"{FEATURE}/documentation-impact-evidence.json",
    }
    if not required_evidence <= expected:
        fail("candidate fixed point must include causal-closeout, semantic, accessibility, public, and Documentation Impact evidence paths")
    result = subprocess.run(
        ["git", "status", "--porcelain=v1", "-z", "--untracked-files=all"],
        cwd=root, capture_output=True, check=False,
    )
    if result.returncode:
        fail("git candidate fixed-point inventory command failed")
    validate_candidate_fixpoint_inventory(
        parse_porcelain_z(result.stdout), expected, set(allowlist["allowedPaths"]),
    )
    return f"stable candidate fixed point for {len(expected)} paths"


def render_candidate_paths(root: Path, allowlist_path: Path, output_path: Path) -> str:
    resolved_root = root.resolve()
    resolved_output = output_path.resolve()
    if resolved_output == resolved_root or resolved_root in resolved_output.parents:
        fail("candidate-list output must be outside the repository")
    allowlist = load_json(allowlist_path, "candidate allowlist")
    if allowlist.get("schemaVersion") != "1.0" or not isinstance(allowlist.get("allowedPaths"), list):
        fail("candidate allowlist needs schemaVersion 1.0 and allowedPaths")
    allowed = set(allowlist["allowedPaths"])
    result = subprocess.run(
        ["git", "status", "--porcelain=v1", "-z", "--untracked-files=all"],
        cwd=root, capture_output=True, check=False,
    )
    if result.returncode:
        fail("git candidate-list inventory command failed")
    rows = parse_porcelain_z(result.stdout)
    changed = {path for _, path in rows}
    bounded = (
        "requirements/baseline/", "requirements/intakes/active/", FEATURE + "/", "docs/aeps/",
        "docs/project-statistics.md", "docs/scripts/embedded-scripts.md",
    )
    unexpected = sorted(path for path in changed if path.startswith(bounded) and path not in allowed)
    if unexpected:
        fail(f"changed META-LH-01 path outside allowlist: {', '.join(unexpected)}")
    selected = sorted(changed & allowed)
    if not selected:
        fail("candidate-list selected no changed allowlisted paths")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(selected) + "\n", encoding="utf-8")
    return f"temporary candidate list for {len(selected)} paths"


def validate_check_inventory(all_checks_path: Path, required_checks_path: Path) -> str:
    def load_checks(path: Path, label: str) -> list[dict[str, Any]]:
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            fail(f"{label} is not valid UTF-8 JSON: {exc}")
        if not isinstance(value, list) or not value:
            fail(f"{label} must be a non-empty array")
        for index, item in enumerate(value):
            if not isinstance(item, dict) or not isinstance(item.get("name"), str):
                fail(f"{label}[{index}] must contain a check name")
            if item.get("bucket") not in ("pass", "skipping"):
                fail(f"{label} contains a non-successful check: {item.get('name')}={item.get('bucket')}")
        return value

    all_checks = load_checks(all_checks_path, "all PR checks")
    required_checks = load_checks(required_checks_path, "required PR checks")
    all_keys = {(item.get("name"), item.get("link")) for item in all_checks}
    required_keys = {(item.get("name"), item.get("link")) for item in required_checks}
    if not required_keys <= all_keys:
        fail("required PR checks must be a subset of all PR checks")
    return f"all {len(all_checks)} PR checks terminal-successful; {len(required_checks)} required"


def require_independent_review(review: Any, label: str,
                               expected_paths_set: set[str]) -> None:
    if not isinstance(review, dict) or review.get("result") != "Pass":
        fail(f"{label} must be a completed Pass review")
    reviewer = review.get("reviewer")
    if not isinstance(reviewer, dict) or reviewer.get("independent") is not True:
        fail(f"{label} reviewer must be independent")
    for field in ("role", "independenceStatement"):
        if not isinstance(reviewer.get(field), str) or not reviewer[field].strip():
            fail(f"{label} reviewer missing field: {field}")
    reviewed_paths = review.get("reviewedPaths", [])
    if (not isinstance(reviewed_paths, list)
            or len(reviewed_paths) != len(expected_paths_set)
            or set(reviewed_paths) != expected_paths_set):
        fail(f"{label} must cover the exact three-path closeout delta")
    if not isinstance(review.get("rationale"), str) or not review["rationale"].strip():
        fail(f"{label} needs a non-empty rationale")
    if review.get("blockingFindings") != []:
        fail(f"{label} must have zero blocking findings")


def validate_causal_closeout(root: Path, *, require_staged: bool = False) -> str:
    tasks_path = root / TASKS
    state_path = root / STATE
    evidence_path = root / CAUSAL_CLOSEOUT
    tasks_text = read_text(tasks_path, "completed tasks")
    task_rows = re.findall(r"^- \[([ xX])\] (T\d{3})\b", tasks_text, flags=re.MULTILINE)
    expected_task_ids = [f"T{number:03d}" for number in range(1, 67)]
    if [task_id for _, task_id in task_rows] != expected_task_ids:
        fail("completed tasks must contain exactly T001 through T066 once and in order")
    if any(mark.lower() != "x" for mark, _ in task_rows):
        fail("causal closeout requires exactly 66 checked tasks")

    state = load_json(state_path, "autonomous run state")
    state_tasks = state.get("tasks")
    if not isinstance(state_tasks, dict):
        fail("autonomous run state needs tasks")
    if state_tasks.get("path") != TASKS:
        fail("autonomous run state must bind the canonical tasks path")
    if state_tasks.get("completed") != 66 or state_tasks.get("total") != 66:
        fail("causal closeout requires state tasks completed/total equality at 66")
    actual_tasks_hash = raw_sha256(tasks_path)
    if state_tasks.get("sha256") != actual_tasks_hash:
        fail("autonomous run state tasks SHA-256 differs from the fully checked tasks file")
    if state.get("schemaVersion") != "1.1" or state.get("stage") != "MergeAndSync":
        fail("causal closeout requires schema-1.1 stage MergeAndSync")
    if state.get("status") != "Completed" or state.get("nextExactAction") != "N/A":
        fail("causal closeout requires Completed status and nextExactAction N/A")
    closeout = state.get("closeout")
    if not isinstance(closeout, dict):
        fail("causal closeout requires terminal run-state closeout fields")
    for field in ("mergeOrPublication", "defaultBranchSync", "finalValidation"):
        if closeout.get(field) != "Completed":
            fail(f"causal closeout requires closeout.{field} Completed")
    if closeout.get("postMergeActions") not in ("N/A", "Completed"):
        fail("causal closeout requires terminal postMergeActions")
    state_binding = state.get("causalCloseout")
    if (not isinstance(state_binding, dict)
            or state_binding.get("evidencePath") != CAUSAL_CLOSEOUT
            or state_binding.get("branch") != CLOSEOUT_BRANCH
            or state_binding.get("allowedPaths") != list(CLOSEOUT_PATHS)
            or state_binding.get("status") != "Completed"
            or state_binding.get("publicationEvidence") != "ExternalOnly"):
        fail("autonomous run state must contain the terminal exact causal-closeout binding")

    evidence = load_json(evidence_path, "causal closeout evidence")
    exact_paths = set(CLOSEOUT_PATHS)
    if evidence.get("schemaVersion") != "1.0" or evidence.get("status") != "Completed":
        fail("causal closeout evidence must be schema 1.0 and Completed")
    if evidence.get("runId") != state.get("runId"):
        fail("causal closeout evidence runId differs from autonomous run state")
    if evidence.get("closeoutBranch") != CLOSEOUT_BRANCH:
        fail(f"causal closeout branch must be {CLOSEOUT_BRANCH}")
    if evidence.get("closeoutPaths") != list(CLOSEOUT_PATHS):
        fail("causal closeout evidence must declare the exact three-path allowlist")
    for field in ("terminalFeatureHead", "featureMergeSha", "synchronizedMainSha"):
        value = evidence.get(field)
        if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", value):
            fail(f"causal closeout evidence {field} must be a full lowercase Git object ID")
    feature_pr = evidence.get("featurePullRequest")
    if (not isinstance(feature_pr, dict)
            or not isinstance(feature_pr.get("number"), int)
            or isinstance(feature_pr.get("number"), bool)
            or feature_pr["number"] <= 0
            or not isinstance(feature_pr.get("url"), str)
            or not feature_pr["url"].startswith("https://")):
        fail("causal closeout evidence needs the actual feature pull request number and HTTPS URL")

    commands = evidence.get("commands")
    if not isinstance(commands, list):
        fail("causal closeout evidence commands must be an array")
    by_id = {entry.get("checkId"): entry for entry in commands if isinstance(entry, dict)}
    if len(by_id) != len(commands) or set(by_id) != CAUSAL_COMMAND_IDS:
        fail("causal closeout evidence must contain the exact command/result inventory")
    for check_id, entry in by_id.items():
        allowed_results = ("Pass", "N/A") if check_id == "post-merge-actions" else ("Pass",)
        if entry.get("result") not in allowed_results:
            fail(f"causal closeout command {check_id} must be Pass"
                 + (" or justified N/A" if check_id == "post-merge-actions" else ""))
        for field in ("command", "evidenceReference"):
            if not isinstance(entry.get(field), str) or not entry[field].strip():
                fail(f"causal closeout command {check_id} missing field: {field}")
        if entry.get("result") == "N/A" and (
                not isinstance(entry.get("rationale"), str) or not entry["rationale"].strip()):
            fail(f"causal closeout command {check_id} N/A needs a rationale")
    expected_post_merge_result = "N/A" if closeout.get("postMergeActions") == "N/A" else "Pass"
    if by_id["post-merge-actions"].get("result") != expected_post_merge_result:
        fail("post-merge command result must match state.closeout.postMergeActions")

    require_independent_review(evidence.get("documentationReview"),
                               "documentation review", exact_paths)
    public_review = evidence.get("publicContentReview")
    require_independent_review(public_review, "public-content review", exact_paths)
    public_rows = public_review.get("reviews") if isinstance(public_review, dict) else None
    if (not isinstance(public_rows, list)
            or len(public_rows) != len(exact_paths)
            or {row.get("path") for row in public_rows
                if isinstance(row, dict)} != exact_paths):
        fail("public-content review needs exactly one row for each closeout path")
    for row in public_rows:
        if not isinstance(row, dict) or set(row.get("criteria", {})) != PUBLIC_CRITERIA:
            fail("public-content closeout criteria must be exact")
        if any(value != "Pass" for value in row["criteria"].values()):
            fail("public-content closeout criteria must all Pass")
        if not isinstance(row.get("rationale"), str) or not row["rationale"].strip():
            fail("public-content closeout row needs a rationale")

    boundary = evidence.get("nonSelfReferentialBoundary")
    if not isinstance(boundary, dict):
        fail("causal closeout evidence needs a non-self-referential boundary")
    for field in ("containingCommitSha", "closeoutPullRequest", "closeoutMergeSha"):
        if boundary.get(field) != "N/A":
            fail(f"causal closeout evidence must not claim its own {field}")
    if not isinstance(boundary.get("statement"), str) or not boundary["statement"].strip():
        fail("causal closeout non-self-referential boundary needs a statement")

    if require_staged:
        staged_result = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "-z"], cwd=root,
            capture_output=True, check=False,
        )
        status_result = subprocess.run(
            ["git", "status", "--porcelain=v1", "-z", "--untracked-files=all"], cwd=root,
            capture_output=True, check=False,
        )
        if staged_result.returncode or status_result.returncode:
            fail("causal closeout git inventory commands failed")
        staged = {part.decode() for part in staged_result.stdout.split(b"\0") if part}
        changed = {path for _, path in parse_porcelain_z(status_result.stdout)}
        if staged != exact_paths or changed != exact_paths:
            fail("causal closeout transaction must change and stage exactly the three allowed paths")
        result = subprocess.run(
            ["git", "diff", "--cached", "--check"], cwd=root,
            text=True, capture_output=True, check=False,
        )
        if result.returncode:
            fail(f"causal closeout git diff --cached --check failed: {(result.stderr or result.stdout).strip()}")
    return "66/66 tasks, terminal schema-1.1 state, exact three-path evidence transaction"


def validate_candidate(root: Path, allowlist_path: Path, expected_path_file: Path) -> str:
    allowlist = load_json(allowlist_path, "candidate allowlist")
    if allowlist.get("schemaVersion") != "1.0" or not isinstance(allowlist.get("allowedPaths"), list):
        fail("candidate allowlist needs schemaVersion 1.0 and allowedPaths")
    allowed = set(allowlist["allowedPaths"])
    expected = expected_paths(expected_path_file)
    staged_result = subprocess.run(["git", "diff", "--cached", "--name-only", "-z"], cwd=root, capture_output=True, check=False)
    status_result = subprocess.run(["git", "status", "--porcelain=v1", "-z", "--untracked-files=all"], cwd=root, capture_output=True, check=False)
    if staged_result.returncode or status_result.returncode:
        fail("git candidate inventory commands failed")
    staged = {part.decode() for part in staged_result.stdout.split(b"\0") if part}
    validate_candidate_inventory(staged, parse_porcelain_z(status_result.stdout), expected, allowed)
    result = subprocess.run(["git", "diff", "--cached", "--check"], cwd=root, text=True, capture_output=True, check=False)
    if result.returncode:
        fail(f"git diff --cached --check failed: {(result.stderr or result.stdout).strip()}")
    return f"exact staged allowlist reconciliation for {len(expected)} paths"


def validate_terminal_rename_entries(entries: list[tuple[str, str, str]],
                                     record: dict[str, Any]) -> None:
    expected = [("R100", str(record["originalPath"]), str(record["archivedPath"]))]
    if entries != expected:
        fail(f"terminal rename commit must contain exactly {expected[0]}; got {entries}")


def terminal_rename_entries(value: bytes) -> list[tuple[str, str, str]]:
    parts = [part.decode("utf-8", errors="strict") for part in value.split(b"\0") if part]
    entries: list[tuple[str, str, str]] = []
    index = 0
    while index < len(parts):
        status = parts[index]
        if not status.startswith("R") or index + 2 >= len(parts):
            fail("terminal commit contains a non-rename or malformed entry")
        entries.append((status, parts[index + 1], parts[index + 2]))
        index += 3
    return entries


def validate_terminal_rename(root: Path) -> str:
    state = load_json(root / STATE, "autonomous run state")
    physical_path, disposition, record = resolve_meta01_target(root, state)
    if disposition != "Archived" or physical_path != ARCHIVED_META01:
        fail("terminal-rename validation requires the proven archived lifecycle state")
    branch = subprocess.run(
        ["git", "branch", "--show-current"], cwd=root, text=True,
        capture_output=True, check=False,
    )
    if branch.returncode or branch.stdout.strip() != record["branch"]:
        fail("terminal rename commit must remain on the lifecycle branch")
    lineage = subprocess.run(
        ["git", "rev-list", f"{ACCEPTED_BASE_SHA}..HEAD", "--",
         str(record["originalPath"]), str(record["archivedPath"])],
        cwd=root, text=True, capture_output=True, check=False,
    )
    rename_commits = [line for line in lineage.stdout.splitlines() if line]
    if lineage.returncode or len(rename_commits) != 1:
        fail("feature lineage must contain exactly one intake lifecycle commit")
    rename_commit = rename_commits[0]
    diff = subprocess.run(
        ["git", "diff-tree", "--no-commit-id", "--name-status", "-r", "-M100%", "-z", rename_commit],
        cwd=root, capture_output=True, check=False,
    )
    if diff.returncode:
        fail("cannot inspect terminal rename lifecycle commit")
    validate_terminal_rename_entries(terminal_rename_entries(diff.stdout), record)
    staged = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "-z"], cwd=root,
        capture_output=True, check=False,
    )
    if staged.returncode or any(staged.stdout.split(b"\0")):
        fail("terminal rename commit must leave no staged paths")
    message = subprocess.run(
        ["git", "show", "-s", "--format=%B", rename_commit], cwd=root, text=True,
        capture_output=True, check=False,
    )
    trailer = "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
    if message.returncode or trailer not in message.stdout.splitlines():
        fail("terminal rename lifecycle commit lacks the exact constitutional Co-authored-by trailer")
    return "one byte-identical R100 terminal rename lifecycle commit and immutable archived reviewed head"


def render_gate_evidence(root: Path, requirements_path: Path, execution_path: Path,
                         head: str, output_path: Path) -> str:
    if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", head):
        fail("reviewed head must be a full lowercase Git object ID")
    resolved_root = root.resolve()
    resolved_output = output_path.resolve()
    if resolved_output == resolved_root or resolved_root in resolved_output.parents:
        fail("render-gate-evidence output must be outside the repository")
    requirements = load_json(requirements_path, "gate requirements")
    execution = load_json(execution_path, "exact-head execution record")
    if execution.get("schemaVersion") != "1.0" or execution.get("reviewedHead") != head:
        fail("execution record must use schema 1.0 and the exact reviewed head")
    gates = requirements.get("gates")
    records = execution.get("entries")
    if not isinstance(gates, list) or not isinstance(records, list):
        fail("requirements and execution record must contain entry arrays")
    by_id = {entry.get("gateId"): entry for entry in records if isinstance(entry, dict)}
    if len(by_id) != len(records):
        fail("execution record gate IDs must be unique")
    evidence_entries: list[dict[str, Any]] = []
    for gate in gates:
        gate_id = gate.get("gateId")
        record = by_id.get(gate_id)
        if not isinstance(record, dict):
            fail(f"execution record missing gate: {gate_id}")
        if gate.get("applicability") == "Applicable":
            for field in ("provider", "runId", "workflow", "job", "runnerOrPlatform",
                          "executedCommand", "evidenceReference"):
                if not isinstance(record.get(field), str) or not record[field].strip():
                    fail(f"execution record {gate_id} missing field: {field}")
            if record.get("result") != "Pass":
                fail(f"execution record {gate_id} must be Pass")
            entry = {**record, "applicability": "Applicable", "requiredScope": gate["requiredScope"],
                     "headSha": head, "evidenceRole": "Primary"}
        else:
            entry = {"gateId": gate_id, "evidenceRole": "Primary", "applicability": "N/A",
                     "requiredScope": gate["requiredScope"], "headSha": head, "result": "N/A",
                     "rationale": gate["rationale"], "reevaluationTrigger": gate["reevaluationTrigger"],
                     "evidenceReference": record.get("evidenceReference", REQUIREMENTS)}
        evidence_entries.append(entry)
    if set(by_id) != {gate.get("gateId") for gate in gates}:
        fail("execution record contains undeclared gates")
    output = {"schemaVersion": "1.0", "requirementsSha256": raw_sha256(requirements_path),
              "reviewedHead": head, "entries": evidence_entries}
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return f"temporary exact-head evidence for {len(evidence_entries)} gates at {head}"


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Read-only META-LH-01 acceptance contract")
    result.add_argument("--repo", default=".", help="repository root")
    sub = result.add_subparsers(dest="mode", required=True)
    for name in ("input-bindings", "global-ready", "domain", "terminal-rename",
                 "causal-closeout"):
        item = sub.add_parser(name)
        if name == "input-bindings":
            item.add_argument("--surface", required=True, choices=("bash", "powershell"))
    review = sub.add_parser("review-evidence")
    review.add_argument("--kind", required=True, choices=("semantic", "accessibility", "public"))
    review.add_argument("--evidence", required=True)
    review.add_argument("--expected-paths", required=True)
    documentation = sub.add_parser("documentation-impact")
    documentation.add_argument("--evidence", required=True)
    documentation.add_argument("--expected-paths", required=True)
    aeps = sub.add_parser("aeps")
    aeps.add_argument("--receipt", required=True)
    candidate = sub.add_parser("candidate")
    candidate.add_argument("--allowlist", required=True)
    candidate.add_argument("--expected-paths", required=True)
    fixpoint = sub.add_parser("candidate-fixpoint")
    fixpoint.add_argument("--allowlist", required=True)
    fixpoint.add_argument("--expected-paths", required=True)
    candidate_list = sub.add_parser("candidate-list")
    candidate_list.add_argument("--allowlist", required=True)
    candidate_list.add_argument("--output", required=True)
    checks = sub.add_parser("check-inventory")
    checks.add_argument("--all-checks", required=True)
    checks.add_argument("--required-checks", required=True)
    render = sub.add_parser("render-gate-evidence")
    render.add_argument("--requirements", required=True)
    render.add_argument("--execution-record", required=True)
    render.add_argument("--head", required=True)
    render.add_argument("--output", required=True)
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    root = Path(args.repo).resolve()
    try:
        if args.mode == "input-bindings":
            summary = validate_input_bindings(root, args.surface)
        elif args.mode == "global-ready":
            summary = validate_global_ready(root)
        elif args.mode == "domain":
            summary = validate_domain(root)
        elif args.mode == "terminal-rename":
            summary = validate_terminal_rename(root)
        elif args.mode == "causal-closeout":
            summary = validate_causal_closeout(root, require_staged=True)
        elif args.mode == "review-evidence":
            summary = validate_review_evidence(root, Path(args.evidence), Path(args.expected_paths), args.kind)
        elif args.mode == "documentation-impact":
            summary = validate_documentation_impact(root, Path(args.evidence), Path(args.expected_paths))
        elif args.mode == "aeps":
            summary = validate_aeps(root, Path(args.receipt))
        elif args.mode == "candidate":
            summary = validate_candidate(root, Path(args.allowlist), Path(args.expected_paths))
        elif args.mode == "candidate-fixpoint":
            summary = validate_candidate_fixpoint(root, Path(args.allowlist), Path(args.expected_paths))
        elif args.mode == "candidate-list":
            summary = render_candidate_paths(root, Path(args.allowlist), Path(args.output))
        elif args.mode == "check-inventory":
            summary = validate_check_inventory(Path(args.all_checks), Path(args.required_checks))
        else:
            summary = render_gate_evidence(root, Path(args.requirements), Path(args.execution_record),
                                           args.head, Path(args.output))
    except ContractError as exc:
        print(f"ERROR: {args.mode}: {exc}", file=sys.stderr)
        return 1
    except (OSError, UnicodeError, KeyError, TypeError, ValueError) as exc:
        print(f"ERROR: {args.mode}: malformed input: {exc}", file=sys.stderr)
        return 1
    print(f"PASS: {args.mode}: {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
