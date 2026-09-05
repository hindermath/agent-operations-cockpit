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
import os
import re
import shutil
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
EXPECTED_REPOSITORY = "hindermath/agent-operations-cockpit"
EXPECTED_COMPLETION_MERGE = "3c9a618243fffff187932b1ee431ffbd25d3856e"
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
    "PASS: post-global-ready: 14 logical Ready targets with archive-aware META-LH-02 "
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


def git_blob(root: Path, revision: str, relative: str) -> bytes:
    """Read one exact Git blob without shell interpolation."""
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "cat-file", "blob", f"{revision}:{relative}"],
            capture_output=True, check=False,
        )
    except OSError as exc:
        fail(f"cannot read exact Git blob for {relative}: {exc}")
    if result.returncode != 0:
        diagnostic = result.stderr.decode("utf-8", errors="replace").strip()
        fail(f"cannot read exact Git blob for {relative}: {diagnostic or 'git cat-file failed'}")
    return result.stdout


def git_blob_sha256(root: Path, relative: str) -> str:
    """Hash the exact blob at checked-out HEAD without shell interpolation."""
    return hashlib.sha256(git_blob(root, "HEAD", relative)).hexdigest()


def require_clean_git_path(root: Path, relative: str) -> None:
    """Require index and worktree equality using Git's own EOL-aware rules."""
    environment = {**os.environ, "GIT_OPTIONAL_LOCKS": "0"}
    commands = (
        ["git", "--no-optional-locks", "diff", "--no-ext-diff", "--quiet", "--", relative],
        ["git", "--no-optional-locks", "diff", "--cached", "--no-ext-diff", "--quiet",
         "HEAD", "--", relative],
    )
    for command in commands:
        try:
            result = subprocess.run(
                command, cwd=root, env=environment, capture_output=True, check=False,
            )
        except OSError as exc:
            fail(f"cannot verify clean Git path {relative}: {exc}")
        if result.returncode == 1:
            fail(f"current Git path differs from checked-out HEAD: {relative}")
        if result.returncode != 0:
            diagnostic = result.stderr.decode("utf-8", errors="replace").strip()
            fail(f"cannot verify clean Git path {relative}: {diagnostic or 'git diff failed'}")


def clean_checked_out_blob(root: Path, relative: str) -> bytes:
    """Return canonical HEAD bytes after proving an EOL-aware clean checkout."""
    require_clean_git_path(root, relative)
    head = git_blob(root, "HEAD", relative)
    try:
        current = (root / relative).read_bytes()
    except OSError as exc:
        fail(f"cannot read current file for {relative}: {exc}")
    current_normalized = normalized_bytes_sha256(current, relative)
    head_normalized = normalized_bytes_sha256(head, relative)
    if current_normalized != head_normalized:
        fail(f"current normalized content differs from checked-out Git blob: {relative}")
    return head


def immutable_raw_sha256(root: Path, relative: str) -> str:
    """Hash canonical Git bytes after proving a clean current text checkout."""
    if (root / ".git").exists():
        return hashlib.sha256(clean_checked_out_blob(root, relative)).hexdigest()
    return raw_sha256(root / relative)


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


def normalized_bytes_sha256(raw: bytes, label: str) -> str:
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeError as exc:
        fail(f"{label} is not UTF-8 text: {exc}")
    if "\x00" in text:
        fail(f"binary NUL in {label}")
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def immutable_normalized_sha256(root: Path, relative: str) -> str:
    """Bind normalized worktree content to HEAD while permitting line-ending changes."""
    current = normalized_sha256(root / relative)
    if (root / ".git").exists():
        head = normalized_bytes_sha256(clean_checked_out_blob(root, relative), relative)
        if current != head:
            fail(f"current normalized content differs from checked-out Git blob: {relative}")
    return current


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


def resolve_logical_branch(environment: dict[str, str], event: dict[str, Any],
                           checked_head: str, current_branch: str,
                           status: str = "Active") -> str:
    """Resolve local or CI branch identity only from a complete proof."""
    if environment.get("GITHUB_ACTIONS") != "true":
        if not current_branch:
            fail("detached local HEAD is not an accepted branch identity")
        if status == "Active" and current_branch != EXPECTED_BRANCH:
            fail("current Git branch differs from the accepted Feature-002 branch")
        return current_branch

    event_name = environment.get("GITHUB_EVENT_NAME", "")
    repository = environment.get("GITHUB_REPOSITORY", "")
    event_repository = event.get("repository")
    event_repository_name = (
        event_repository.get("full_name") if isinstance(event_repository, dict) else None
    )
    if event_name not in {"pull_request", "push"}:
        fail(f"unsupported GitHub Actions event for branch proof: {event_name or 'missing'}")
    if repository != EXPECTED_REPOSITORY or event_repository_name != EXPECTED_REPOSITORY:
        fail("GitHub Actions repository differs from the accepted Feature-002 repository")
    if not re.fullmatch(r"[0-9a-f]{40}", checked_head):
        fail("checked-out HEAD is not an exact lowercase Git SHA")

    if event_name == "pull_request":
        pull_request = event.get("pull_request")
        head = pull_request.get("head") if isinstance(pull_request, dict) else None
        event_ref = head.get("ref") if isinstance(head, dict) else None
        event_sha = head.get("sha") if isinstance(head, dict) else None
        head_repository = head.get("repo") if isinstance(head, dict) else None
        head_repository_name = (
            head_repository.get("full_name") if isinstance(head_repository, dict) else None
        )
        if (
            not isinstance(event_ref, str)
            or not event_ref
            or environment.get("GITHUB_HEAD_REF") != event_ref
            or head_repository_name != EXPECTED_REPOSITORY
            or (status == "Active" and event_ref != EXPECTED_BRANCH)
        ):
            fail("pull_request head branch differs from the accepted Feature-002 branch")
    else:
        event_ref = event.get("ref")
        event_sha = event.get("after")
        event_branch = (
            event_ref.removeprefix("refs/heads/")
            if isinstance(event_ref, str) and event_ref.startswith("refs/heads/")
            else ""
        )
        if (
            environment.get("GITHUB_HEAD_REF", "") != ""
            or environment.get("GITHUB_REF_TYPE") != "branch"
            or not event_branch
            or environment.get("GITHUB_REF_NAME") != event_branch
            or (status == "Active" and event_branch != EXPECTED_BRANCH)
        ):
            fail("push branch differs from the accepted Feature-002 branch")

    if event_sha != checked_head:
        fail("GitHub event head SHA differs from exact checked-out HEAD")
    return str(event_ref)


def remote_repository(root: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"], cwd=root,
            text=True, capture_output=True, check=False,
        )
    except OSError as exc:
        fail(f"Git origin could not be read: {exc}")
    if result.returncode != 0:
        fail("Git origin is missing")
    value = result.stdout.strip()
    patterns = (
        r"https://github\.com/([^/]+/[^/]+?)(?:\.git)?$",
        r"git@github\.com:([^/]+/[^/]+?)(?:\.git)?$",
        r"ssh://git@github\.com/([^/]+/[^/]+?)(?:\.git)?$",
    )
    for pattern in patterns:
        match = re.fullmatch(pattern, value)
        if match:
            return match.group(1).lower()
    fail("Git origin is not an accepted GitHub repository URL")


def validate_completed_ancestry(root: Path, checked_head: str,
                                completion_merge: str = EXPECTED_COMPLETION_MERGE) -> None:
    if not re.fullmatch(r"[0-9a-f]{40}", completion_merge):
        fail("accepted Feature-002 completion merge is not an exact lowercase Git SHA")
    try:
        ancestry = subprocess.run(
            ["git", "merge-base", "--is-ancestor", completion_merge, checked_head],
            cwd=root, capture_output=True, check=False,
        )
    except OSError as exc:
        fail(f"Feature-002 completion ancestry could not be checked: {exc}")
    if ancestry.returncode == 1:
        fail("checked-out HEAD is not a descendant of the accepted Feature-002 completion merge")
    if ancestry.returncode != 0:
        diagnostic = ancestry.stderr.decode("utf-8", errors="replace").strip()
        fail(
            "Feature-002 completion ancestry could not be checked: "
            f"{diagnostic or 'git merge-base failed'}"
        )
    for relative in (STATE, LIFECYCLE):
        head_blob = clean_checked_out_blob(root, relative)
        completion_blob = git_blob(root, completion_merge, relative)
        if head_blob != completion_blob:
            fail(f"completed Feature-002 state/lifecycle drift after accepted merge: {relative}")


def validate_git_identity(root: Path,
                          status: str = "Active",
                          environment: dict[str, str] | None = None,
                          completion_merge: str = EXPECTED_COMPLETION_MERGE) -> None:
    environment = dict(os.environ if environment is None else environment)
    try:
        head_result = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True,
            capture_output=True, check=False,
        )
        branch_result = subprocess.run(
            ["git", "branch", "--show-current"], cwd=root, text=True,
            capture_output=True, check=False,
        )
    except OSError as exc:
        fail(f"current Git identity could not be read: {exc}")
    if head_result.returncode != 0 or branch_result.returncode != 0:
        fail("current Git identity could not be read")
    if remote_repository(root) != EXPECTED_REPOSITORY:
        fail("Git origin differs from the accepted Feature-002 repository")
    event: dict[str, Any] = {}
    if environment.get("GITHUB_ACTIONS") == "true":
        event_path = environment.get("GITHUB_EVENT_PATH", "")
        if not event_path:
            fail("GitHub Actions event payload path is missing")
        event = load_json(Path(event_path), "GitHub Actions event payload")
    checked_head = head_result.stdout.strip()
    resolve_logical_branch(
        environment, event, checked_head, branch_result.stdout.strip(), status
    )
    if status == "Completed":
        validate_completed_ancestry(root, checked_head, completion_merge)


def select_bash_executable(candidates: list[str], windows: bool | None = None) -> str:
    """Select executable Git-for-Windows Bash; never accept the WSL launcher."""
    windows = sys.platform == "win32" if windows is None else windows
    if not windows:
        executable = shutil.which("bash")
        if executable:
            return executable
        fail("Bash capability is unavailable")
    for candidate in candidates:
        if not candidate:
            continue
        path = Path(candidate)
        normalized = str(path).replace("\\", "/").lower()
        if (
            path.is_absolute()
            and path.name.lower() == "bash.exe"
            and "/windows/system32/" not in normalized
            and path.is_file()
        ):
            return str(path)
    fail("Git-for-Windows bash unavailable; WSL launcher is not an accepted capability")


def bash_executable(environment: dict[str, str] | None = None) -> str:
    environment = dict(os.environ if environment is None else environment)
    if sys.platform != "win32":
        return select_bash_executable([], windows=False)
    candidates = [environment.get("AOC_GIT_BASH_EXE", "")]
    for variable in ("ProgramW6432", "ProgramFiles", "LocalAppData"):
        base = environment.get(variable, "")
        if base:
            suffix = Path("Programs/Git/bin/bash.exe") if variable == "LocalAppData" else Path("Git/bin/bash.exe")
            candidates.append(str(Path(base) / suffix))
    candidates.append(str(Path(environment.get("SystemRoot", r"C:\Windows")) / "System32/bash.exe"))
    return select_bash_executable(candidates, windows=True)


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
    status = state.get("status")
    if status not in {"Active", "Completed"}:
        fail("autonomous run state must be Active or terminal Completed")
    if state.get("stage") not in ALLOWED_STAGES:
        fail(f"autonomous run state stage is not post-GlobalReady qualified: {state.get('stage')}")
    if status == "Completed":
        if state.get("stage") != "MergeAndSync" or state.get("nextExactAction") != "N/A":
            fail("terminal Completed state must be at MergeAndSync with nextExactAction N/A")
        tasks = state.get("tasks")
        if not isinstance(tasks, dict) or tasks.get("completed") != 93 or tasks.get("total") != 93:
            fail("terminal Completed state must bind exactly 93 of 93 completed tasks")
        closeout = state.get("closeout")
        required_closeout = {
            "mergeOrPublication": "Completed",
            "defaultBranchSync": "Completed",
            "postMergeActions": "Completed",
            "finalValidation": "Completed",
        }
        if not isinstance(closeout, dict) or closeout != required_closeout:
            fail("terminal Completed state must bind the fully completed MergeAndSync closeout")
    if (root / ".git").exists():
        validate_git_identity(root, status=status)
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
    raw_digest = lowercase_sha256(
        record.get("originalRawSha256"), "lifecycle originalRawSha256"
    )
    normalized_digest = lowercase_sha256(
        record.get("originalNormalizedSha256"), "lifecycle originalNormalizedSha256"
    )
    original = root / ORIGINAL_TARGET
    archive = root / ARCHIVED_TARGET
    if original.is_file() == archive.is_file():
        disposition = "both" if original.is_file() else "neither"
        fail(f"META-LH-02 original and archived paths must be mutually exclusive; found {disposition}")
    if state.get("status") == "Completed" and original.is_file():
        fail("terminal Completed META-LH-02 must resolve exactly the archived target")
    physical = ORIGINAL_TARGET if original.is_file() else ARCHIVED_TARGET
    physical_path = root / physical
    if immutable_normalized_sha256(root, physical) != normalized_digest:
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
        repo_path(root, path, f"lifecycle {label} path")
        if immutable_raw_sha256(root, path) != digest:
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
    if immutable_raw_sha256(root, archive) != raw_digest:
        fail(f"{logical_id} archived target raw SHA-256 drift")
    if immutable_normalized_sha256(root, archive) != expected_normalized_sha256:
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
            command = [bash_executable(), REVIEW_BASH, "--result", review_path, "--repo", review_repo]
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
    resolved_targets: set[str] = set()
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
        resolved_targets.add(physical)
        repo_path(root, physical, f"{label}.target.path")
        if immutable_normalized_sha256(root, physical) != target_hash:
            fail(f"{label}.target normalized SHA-256 drift")

        receipt_path = receipt_binding.get("path")
        receipt_hash = lowercase_sha256(
            receipt_binding.get("rawSha256"), f"{label}.authoringReceipt.rawSha256"
        )
        current_receipt = receipts.get(expected_target)
        if current_receipt is None or current_receipt[0] != receipt_path:
            fail(f"{label}.authoringReceipt.path is not the unique current receipt")
        repo_path(root, str(receipt_path), f"{label}.authoringReceipt.path")
        if immutable_raw_sha256(root, str(receipt_path)) != receipt_hash:
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
        repo_path(root, str(review_path), f"{label}.readySingleReview.path")
        if immutable_raw_sha256(root, str(review_path)) != review_hash:
            fail(f"{label}.readySingleReview raw SHA-256 drift")
        validate_review_shape(current_review[1], expected_target, target_hash, f"{label}.readySingleReview")
        run_review_surface(root, "Bash", str(review_path), expected_target, physical, runner)
        run_review_surface(root, "PowerShell", str(review_path), expected_target, physical, runner)

    active_dir = root / "requirements/intakes/active"
    actual_targets = {
        path.relative_to(root).as_posix()
        for path in active_dir.glob("Lastenheft_*.md")
    }
    if actual_targets != resolved_targets:
        fail(
            "programme physical target inventory drift; expected exactly the 14 "
            f"resolved targets, found {len(actual_targets)} paths"
        )


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
