#!/usr/bin/env python3
"""Read-only post-GlobalReady snapshot contract for META-LH-02.

The validator uses only the Python standard library. It validates immutable
programme evidence after the accepted documentary delta without treating the
now-stale generic Authoring Receipt source freshness as current evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath
from typing import Any, Callable


FEATURE = "specs/002-portfolio-ownership"
STATE = f"{FEATURE}/autonomous-run-state.json"
LIFECYCLE = f"{FEATURE}/intake-lifecycle.json"
EXPECTED_RUN_ID = "aa60069e-ded5-463f-a737-9b5aa96070c7"
EXPECTED_BRANCH = "002-portfolio-ownership"
LOGICAL_TARGET = "META-LH-02"
ORIGINAL_TARGET = (
    "requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.md"
)
ARCHIVED_TARGET = (
    "requirements/intakes/active/"
    "Lastenheft_META-LH-02-Portfolio-Ownership.002-portfolio-ownership.md"
)
ALLOWED_STAGES = {
    "Plan", "Implement", "Validate", "Publish", "Review", "MergeAndSync", "Retrospective"
}
PROGRAMME_TARGETS = (
    ("META-LH-01", "requirements/intakes/active/Lastenheft_META-LH-01-Programmquellen.md"),
    ("META-LH-02", ORIGINAL_TARGET),
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
REVIEW_BASH = (
    ".specify/presets/intake-review-governance/scripts/"
    "validate-intake-review-result.sh"
)
REVIEW_POWERSHELL = (
    ".specify/presets/intake-review-governance/scripts/"
    "validate-intake-review-result.ps1"
)
PASS_MESSAGE = (
    "PASS: post-global-ready: 14 logical Ready targets with active META-LH-02 "
    "resolution, immutable programme snapshot, and Bash/PowerShell review surfaces"
)


class ContractError(RuntimeError):
    """One precise fail-closed contract violation."""


def fail(message: str) -> None:
    raise ContractError(message)


def load_json(path: Path, label: str) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        fail(f"{label} is not valid UTF-8 JSON: {exc}")
    if not isinstance(data, dict):
        fail(f"{label} root must be an object")
    return data


def raw_sha256(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError as exc:
        fail(f"cannot hash {path}: {exc}")


def normalized_sha256(path: Path) -> str:
    try:
        raw = path.read_bytes()
    except OSError as exc:
        fail(f"cannot read {path}: {exc}")
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeError as exc:
        fail(f"{path} is not UTF-8 text: {exc}")
    if "\x00" in text:
        fail(f"binary NUL in {path}")
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def repo_path(root: Path, value: str, label: str) -> Path:
    pure = PurePosixPath(value)
    if not value or pure.is_absolute() or ".." in pure.parts or "" in pure.parts:
        fail(f"{label} must be a non-empty repository-relative path")
    return root / pure


def lowercase_sha256(value: object, label: str) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value):
        fail(f"{label} must be a lowercase SHA-256")
    return value


def run_checked(command: list[str], root: Path, label: str) -> None:
    try:
        result = subprocess.run(
            command, cwd=root, text=True, capture_output=True, check=False
        )
    except OSError as exc:
        fail(f"{label} could not start: {exc}")
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip().splitlines()
        diagnostic = detail[0] if detail else "no diagnostic"
        fail(f"{label} failed with exit {result.returncode}: {diagnostic}")
    passes = [line for line in result.stdout.splitlines() if line.startswith("PASS:")]
    if len(passes) != 1:
        fail(f"{label} must emit exactly one PASS line; found {len(passes)}")


def current_receipts(root: Path) -> dict[str, tuple[str, dict[str, Any]]]:
    result: dict[str, tuple[str, dict[str, Any]]] = {}
    directory = root / "specs/intake-authoring-receipts"
    for path in sorted(directory.glob("*.json")):
        data = load_json(path, f"Authoring Receipt {path.name}")
        target = data.get("target")
        target_path = target.get("path") if isinstance(target, dict) else None
        if not isinstance(target_path, str):
            continue
        if target_path in result:
            fail(f"multiple current Authoring Receipts target {target_path}")
        result[target_path] = (path.relative_to(root).as_posix(), data)
    return result


def current_single_reviews(root: Path) -> dict[str, tuple[str, dict[str, Any]]]:
    records: list[tuple[str, dict[str, Any], str]] = []
    directory = root / "specs/intake-review-results"
    for path in sorted(directory.glob("*.json")):
        data = load_json(path, f"review result {path.name}")
        targets = data.get("targets")
        if data.get("mode") != "Single" or not isinstance(targets, list) or len(targets) != 1:
            continue
        target = targets[0].get("path") if isinstance(targets[0], dict) else None
        if isinstance(target, str):
            records.append((path.relative_to(root).as_posix(), data, target))
    superseded = {
        data.get("supersedes")
        for _, data, _ in records
        if data.get("supersedes") not in (None, "N/A")
    }
    result: dict[str, tuple[str, dict[str, Any]]] = {}
    for target in {record[2] for record in records}:
        leaves = [
            (path, data)
            for path, data, item_target in records
            if item_target == target and path not in superseded
        ]
        if len(leaves) == 1:
            result[target] = leaves[0]
        elif target.startswith("requirements/intakes/active/"):
            fail(
                f"active target {target} needs exactly one non-superseded Single "
                f"review; found {len(leaves)}"
            )
    return result


def accepted_artifacts(state: dict[str, Any]) -> dict[str, str]:
    items = state.get("acceptedArtifacts")
    if not isinstance(items, list) or len(items) != 3:
        fail("run state must contain exactly three acceptedArtifacts")
    result: dict[str, str] = {}
    for index, item in enumerate(items):
        if not isinstance(item, dict) or set(item) != {"path", "sha256"}:
            fail(f"acceptedArtifacts[{index}] fields are incomplete or ambiguous")
        path = item.get("path")
        if not isinstance(path, str) or path in result:
            fail(f"acceptedArtifacts[{index}].path is invalid or duplicated")
        result[path] = lowercase_sha256(item.get("sha256"), f"acceptedArtifacts[{index}].sha256")
    return result


def validate_state(root: Path) -> dict[str, Any]:
    state = load_json(root / STATE, "Feature-002 autonomous run state")
    if state.get("runId") != EXPECTED_RUN_ID:
        fail("autonomous run state runId differs from the accepted Feature-002 run")
    if state.get("branch") != EXPECTED_BRANCH:
        fail("autonomous run state branch differs from the accepted Feature-002 branch")
    if state.get("featurePath") != FEATURE:
        fail("autonomous run state featurePath differs from Feature 002")
    if state.get("status") != "Active":
        fail("autonomous run state must be Active")
    if state.get("stage") not in ALLOWED_STAGES:
        fail(f"autonomous run state stage is not post-GlobalReady qualified: {state.get('stage')}")
    git_dir = root / ".git"
    if git_dir.exists():
        try:
            branch = subprocess.run(
                ["git", "branch", "--show-current"], cwd=root, text=True,
                capture_output=True, check=False,
            )
        except OSError as exc:
            fail(f"current Git branch could not be read: {exc}")
        if branch.returncode != 0 or branch.stdout.strip() != EXPECTED_BRANCH:
            fail("current Git branch differs from the accepted Feature-002 branch")
    return state


def resolve_lifecycle(root: Path, state: dict[str, Any]) -> tuple[dict[str, Any], str]:
    lifecycle = load_json(root / LIFECYCLE, "Feature-002 lifecycle")
    if set(lifecycle) != {"schemaVersion", "records", "programmeEvidenceSnapshot"}:
        fail("Feature-002 lifecycle fields are incomplete or ambiguous")
    records = lifecycle.get("records")
    if lifecycle.get("schemaVersion") != "1.1" or not isinstance(records, list) or len(records) != 1:
        fail("Feature-002 lifecycle must contain exactly one schema-1.1 record")
    record = records[0]
    required = {
        "recordVersion", "logicalTargetId", "originalPath", "archivedPath",
        "originalRawSha256", "originalNormalizedSha256", "authoringReceipt",
        "readySingleReview", "runId", "branch",
    }
    if not isinstance(record, dict) or set(record) != required:
        fail("Feature-002 lifecycle record fields are incomplete or ambiguous")
    if record.get("recordVersion") != "1.0" or record.get("logicalTargetId") != LOGICAL_TARGET:
        fail("Feature-002 lifecycle record version or logical target is invalid")
    if record.get("runId") != state.get("runId") or record.get("branch") != state.get("branch"):
        fail("Feature-002 lifecycle runId or branch differs from run state")
    if record.get("originalPath") != ORIGINAL_TARGET or record.get("archivedPath") != ARCHIVED_TARGET:
        fail("Feature-002 lifecycle original/archive paths are invalid")
    raw_digest = lowercase_sha256(record.get("originalRawSha256"), "lifecycle originalRawSha256")
    normalized_digest = lowercase_sha256(
        record.get("originalNormalizedSha256"), "lifecycle originalNormalizedSha256"
    )
    original = root / ORIGINAL_TARGET
    archive = root / ARCHIVED_TARGET
    if original.is_file() == archive.is_file():
        disposition = "both" if original.is_file() else "neither"
        fail(f"META-LH-02 original and archived paths must be mutually exclusive; found {disposition}")
    physical = ORIGINAL_TARGET if original.is_file() else ARCHIVED_TARGET
    physical_path = root / physical
    if raw_sha256(physical_path) != raw_digest:
        fail("META-LH-02 physical target raw SHA-256 drift")
    if normalized_sha256(physical_path) != normalized_digest:
        fail("META-LH-02 physical target normalized SHA-256 drift")

    receipt_binding = record.get("authoringReceipt")
    review_binding = record.get("readySingleReview")
    if not isinstance(receipt_binding, dict) or set(receipt_binding) != {"path", "rawSha256"}:
        fail("Feature-002 lifecycle authoringReceipt fields are incomplete or ambiguous")
    if not isinstance(review_binding, dict) or set(review_binding) != {"path", "rawSha256"}:
        fail("Feature-002 lifecycle readySingleReview fields are incomplete or ambiguous")
    artifacts = accepted_artifacts(state)
    if artifacts.get(ORIGINAL_TARGET) != raw_digest:
        fail("Feature-002 lifecycle target hash differs from acceptedArtifacts")
    for label, binding in (("Authoring Receipt", receipt_binding), ("Ready review", review_binding)):
        path = binding.get("path")
        digest = lowercase_sha256(binding.get("rawSha256"), f"lifecycle {label} rawSha256")
        if not isinstance(path, str) or artifacts.get(path) != digest:
            fail(f"Feature-002 lifecycle {label} differs from acceptedArtifacts")
        if raw_sha256(repo_path(root, path, f"lifecycle {label} path")) != digest:
            fail(f"Feature-002 lifecycle {label} raw SHA-256 drift")
    return lifecycle, physical


def validate_review_shape(review: dict[str, Any], target_path: str, target_hash: str,
                          label: str) -> None:
    targets = review.get("targets")
    summary = review.get("summary")
    if (
        review.get("mode") != "Single"
        or review.get("status") != "Ready"
        or not isinstance(targets, list)
        or len(targets) != 1
        or not isinstance(targets[0], dict)
        or targets[0].get("path") != target_path
        or targets[0].get("role") != "Primary"
        or targets[0].get("normalizedSha256") != target_hash
        or review.get("findings") != []
        or review.get("questions") != []
        or review.get("acceptedRisks") != []
        or review.get("operatorExceptions", []) != []
        or not isinstance(summary, dict)
        or any(summary.get(level) != 0 for level in ("critical", "high", "medium", "low"))
    ):
        fail(f"{label} is not Single/Primary/Ready with empty blockers")


def resolve_physical_target(root: Path, logical_id: str, logical_path: str,
                            expected_normalized_sha256: str,
                            meta_lh02_physical: str) -> str:
    """Resolve an already archived programme target through its lifecycle record."""
    if logical_id == LOGICAL_TARGET:
        return meta_lh02_physical
    if (root / logical_path).is_file():
        return logical_path
    matches: list[dict[str, Any]] = []
    for lifecycle_path in sorted((root / "specs").glob("[0-9][0-9][0-9]-*/intake-lifecycle.json")):
        lifecycle = load_json(lifecycle_path, f"lifecycle {lifecycle_path.relative_to(root)}")
        records = lifecycle.get("records")
        if not isinstance(records, list):
            continue
        for record in records:
            if (
                isinstance(record, dict)
                and record.get("logicalTargetId") == logical_id
                and record.get("originalPath") == logical_path
            ):
                matches.append(record)
    if len(matches) != 1:
        fail(
            f"{logical_id} missing at its snapshot path and needs exactly one lifecycle "
            f"record; found {len(matches)}"
        )
    record = matches[0]
    archive = record.get("archivedPath")
    if not isinstance(archive, str):
        fail(f"{logical_id} lifecycle archivedPath is invalid")
    original_exists = (root / logical_path).is_file()
    archive_exists = repo_path(root, archive, f"{logical_id} lifecycle archivedPath").is_file()
    if original_exists == archive_exists:
        disposition = "both" if original_exists else "neither"
        fail(f"{logical_id} original and archived paths must be mutually exclusive; found {disposition}")
    raw_digest = lowercase_sha256(
        record.get("originalRawSha256"), f"{logical_id} lifecycle originalRawSha256"
    )
    archive_path = root / archive
    if raw_sha256(archive_path) != raw_digest:
        fail(f"{logical_id} archived target raw SHA-256 drift")
    if normalized_sha256(archive_path) != expected_normalized_sha256:
        fail(f"{logical_id} archived target normalized SHA-256 drift")
    return archive


def run_review_surface(root: Path, surface: str, review_path: str,
                       logical_target: str, physical_target: str,
                       runner: Callable[[list[str], Path, str], None]) -> None:
    label = f"{surface} review validator for {logical_target}"
    review_repo = "."
    temporary: tempfile.TemporaryDirectory[str] | None = None
    try:
        if logical_target != physical_target:
            temporary = tempfile.TemporaryDirectory(prefix="meta-lh-02-review-projection-")
            projection = Path(temporary.name)
            (projection / "specs").symlink_to((root / "specs").resolve(), target_is_directory=True)
            projected = projection / logical_target
            projected.parent.mkdir(parents=True, exist_ok=True)
            projected.symlink_to((root / physical_target).resolve())
            review_repo = str(projection)
        if surface == "Bash":
            command = ["bash", REVIEW_BASH, "--result", review_path, "--repo", review_repo]
        else:
            command = [
                "pwsh", "-NoProfile", "-File", REVIEW_POWERSHELL,
                "-Result", review_path, "-Repo", review_repo,
            ]
        runner(command, root, label)
    finally:
        if temporary is not None:
            temporary.cleanup()


def validate_snapshot(root: Path, lifecycle: dict[str, Any], state: dict[str, Any],
                      physical_target: str,
                      runner: Callable[[list[str], Path, str], None] = run_checked) -> None:
    snapshot = lifecycle.get("programmeEvidenceSnapshot")
    if not isinstance(snapshot, dict) or set(snapshot) != {
        "snapshotVersion", "runId", "branch", "orderedLogicalTargets"
    }:
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
    actual_ids = [entry.get("logicalTargetId") if isinstance(entry, dict) else None for entry in ordered]
    if len(actual_ids) != len(set(actual_ids)):
        fail("programme evidence snapshot contains duplicate logical targets")
    if actual_ids != expected_ids:
        fail("programme evidence snapshot must contain the exact 14 ordered logical targets")

    receipts = current_receipts(root)
    reviews = current_single_reviews(root)
    for index, ((logical_id, expected_target), entry) in enumerate(zip(PROGRAMME_TARGETS, ordered)):
        label = f"programmeEvidenceSnapshot.orderedLogicalTargets[{index}]"
        if not isinstance(entry, dict) or set(entry) != {
            "logicalTargetId", "target", "authoringReceipt", "readySingleReview"
        }:
            fail(f"{label} fields are incomplete or ambiguous")
        if entry.get("logicalTargetId") != logical_id:
            fail(f"{label}.logicalTargetId is invalid")
        target = entry.get("target")
        receipt_binding = entry.get("authoringReceipt")
        review_binding = entry.get("readySingleReview")
        if not isinstance(target, dict) or set(target) != {"path", "normalizedSha256"}:
            fail(f"{label}.target fields are incomplete or ambiguous")
        if not isinstance(receipt_binding, dict) or set(receipt_binding) != {"path", "rawSha256"}:
            fail(f"{label}.authoringReceipt fields are incomplete or ambiguous")
        if not isinstance(review_binding, dict) or set(review_binding) != {"path", "rawSha256"}:
            fail(f"{label}.readySingleReview fields are incomplete or ambiguous")
        if target.get("path") != expected_target:
            fail(f"{label}.target.path differs from the exact programme target")
        target_hash = lowercase_sha256(target.get("normalizedSha256"), f"{label}.target.normalizedSha256")
        physical = resolve_physical_target(
            root, logical_id, expected_target, target_hash, physical_target
        )
        if normalized_sha256(repo_path(root, physical, f"{label}.target.path")) != target_hash:
            fail(f"{label}.target normalized SHA-256 drift")

        receipt_path = receipt_binding.get("path")
        receipt_hash = lowercase_sha256(
            receipt_binding.get("rawSha256"), f"{label}.authoringReceipt.rawSha256"
        )
        current_receipt = receipts.get(expected_target)
        if current_receipt is None or current_receipt[0] != receipt_path:
            fail(f"{label}.authoringReceipt.path is not the unique current receipt")
        if raw_sha256(repo_path(root, str(receipt_path), f"{label}.authoringReceipt.path")) != receipt_hash:
            fail(f"{label}.authoringReceipt raw SHA-256 drift")
        receipt = current_receipt[1]
        receipt_target = receipt.get("target")
        if (
            receipt.get("status") != "ReadyForReview"
            or not isinstance(receipt_target, dict)
            or receipt_target.get("path") != expected_target
            or receipt_target.get("normalizedSha256") != target_hash
        ):
            fail(f"{label}.authoringReceipt is not ReadyForReview for the snapshot target")

        review_path = review_binding.get("path")
        review_hash = lowercase_sha256(
            review_binding.get("rawSha256"), f"{label}.readySingleReview.rawSha256"
        )
        current_review = reviews.get(expected_target)
        if current_review is None or current_review[0] != review_path:
            fail(f"{label}.readySingleReview.path is not the unique current review leaf")
        if raw_sha256(repo_path(root, str(review_path), f"{label}.readySingleReview.path")) != review_hash:
            fail(f"{label}.readySingleReview raw SHA-256 drift")
        validate_review_shape(current_review[1], expected_target, target_hash, f"{label}.readySingleReview")
        run_review_surface(root, "Bash", str(review_path), expected_target, physical, runner)
        run_review_surface(root, "PowerShell", str(review_path), expected_target, physical, runner)


def validate_post_global_ready(root: Path,
                               runner: Callable[[list[str], Path, str], None] = run_checked) -> str:
    state = validate_state(root)
    lifecycle, physical = resolve_lifecycle(root, state)
    validate_snapshot(root, lifecycle, state, physical, runner)
    return PASS_MESSAGE


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(
        description="Read-only META-LH-02 post-GlobalReady snapshot validator"
    )
    result.add_argument("--repo", default=".", help="repository root")
    result.add_argument("mode", choices=("post-global-ready",))
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    root = Path(args.repo).resolve()
    try:
        if not root.is_dir():
            fail(f"repository root is not a directory: {root}")
        message = validate_post_global_ready(root)
    except ContractError as exc:
        print(f"ERROR: post-global-ready: {exc}", file=sys.stderr)
        return 1
    except (OSError, UnicodeError, KeyError, TypeError, ValueError) as exc:
        print(f"ERROR: post-global-ready: malformed input: {exc}", file=sys.stderr)
        return 1
    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
