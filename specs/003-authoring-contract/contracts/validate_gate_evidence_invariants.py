#!/usr/bin/env python3
"""Validate feature-local Gate Evidence reference and binding invariants."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


class EvidenceViolation(ValueError):
    """Raised when a feature-local Gate Evidence invariant fails."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise EvidenceViolation(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(file_path: Path) -> dict[str, Any]:
    try:
        raw = file_path.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            raw = raw[3:]
        text = raw.decode("utf-8", errors="strict")
        if "\x00" in text:
            raise EvidenceViolation(f"binary NUL in JSON: {file_path}")
        value = json.loads(text, object_pairs_hook=_unique_object)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise EvidenceViolation(f"cannot read strict JSON {file_path}: {exc}") from exc
    if not isinstance(value, dict):
        raise EvidenceViolation(f"JSON root must be an object: {file_path}")
    return value


def normalized_hash(file_path: Path) -> str:
    raw = file_path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]
    text = raw.decode("utf-8", errors="strict")
    if "\x00" in text:
        raise EvidenceViolation(f"binary NUL in text file: {file_path}")
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def validate_supplemental_references(evidence: dict[str, Any]) -> None:
    entries = evidence.get("entries")
    if not isinstance(entries, list) or not entries:
        raise EvidenceViolation("evidence entries must be a non-empty array")
    by_gate: dict[str, list[dict[str, Any]]] = {}
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("gateId"), str):
            raise EvidenceViolation("every evidence entry requires gateId")
        by_gate.setdefault(entry["gateId"], []).append(entry)
    for gate_id, gate_entries in by_gate.items():
        primary = [entry for entry in gate_entries if entry.get("evidenceRole") == "Primary"]
        if len(primary) != 1:
            raise EvidenceViolation(f"{gate_id} must contain exactly one Primary entry")
        reference = primary[0].get("evidenceReference")
        if not isinstance(reference, str) or not reference:
            raise EvidenceViolation(f"{gate_id} Primary entry requires evidenceReference")
        for entry in gate_entries:
            role = entry.get("evidenceRole")
            if role == "Primary":
                if entry.get("supplementalFor", "") not in ("", None):
                    raise EvidenceViolation(f"{gate_id} Primary entry cannot be supplemental")
            elif role == "Supplemental":
                if entry.get("supplementalFor") != reference:
                    raise EvidenceViolation(
                        f"{gate_id} Supplemental entry must reference its unique Primary"
                    )
            else:
                raise EvidenceViolation(f"{gate_id} has invalid evidenceRole")


def validate_premerge_binding(
    evidence: dict[str, Any], expected_path: str, expected_hash: str
) -> None:
    if evidence.get("snapshotType") != "PostMerge":
        raise EvidenceViolation("accepted PreMerge binding is only valid in PostMerge")
    if evidence.get("acceptedPreMergePath") != expected_path:
        raise EvidenceViolation("acceptedPreMergePath does not match configured path")
    if str(evidence.get("acceptedPreMergeSha256", "")).lower() != expected_hash.lower():
        raise EvidenceViolation("acceptedPreMergeSha256 does not match configured evidence")


def validate(repo: Path, requirements_path: Path, evidence_path: Path) -> dict[str, Any]:
    requirements = load_json(requirements_path)
    evidence = load_json(evidence_path)
    if requirements.get("schemaVersion") != "1.0":
        raise EvidenceViolation("requirements schemaVersion must be 1.0")
    if evidence.get("schemaVersion") != "2.0":
        raise EvidenceViolation("evidence schemaVersion must be 2.0")
    if evidence.get("snapshotType") != requirements.get("snapshotType"):
        raise EvidenceViolation("snapshot type does not match requirements")
    validate_supplemental_references(evidence)

    if requirements.get("snapshotType") == "PreMerge":
        for field in ("acceptedPreMergePath", "acceptedPreMergeSha256", "mergeCommit"):
            if evidence.get(field) not in ("", None):
                raise EvidenceViolation(f"PreMerge {field} must be empty")
    elif requirements.get("snapshotType") == "PostMerge":
        contract = requirements.get("evidenceContract")
        if not isinstance(contract, dict):
            raise EvidenceViolation("PostMerge evidenceContract is missing")
        configured = contract.get("preMergeEvidencePath")
        if not isinstance(configured, str) or not configured:
            raise EvidenceViolation("configured PreMerge evidence path is missing")
        configured_path = (repo / configured).resolve()
        try:
            configured_path.relative_to(repo.resolve())
        except ValueError as exc:
            raise EvidenceViolation("configured PreMerge path escapes repository") from exc
        if not configured_path.is_file():
            raise EvidenceViolation("configured PreMerge evidence file is missing")
        validate_premerge_binding(evidence, configured, normalized_hash(configured_path))
    else:
        raise EvidenceViolation("unsupported snapshot type")
    return {
        "schemaVersion": "1.0",
        "result": "Pass",
        "snapshotType": evidence["snapshotType"],
        "entryCount": len(evidence["entries"]),
    }


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate feature-local Gate Evidence invariants.")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--requirements", required=True)
    parser.add_argument("--evidence", required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    repo = Path(args.repo).resolve()
    try:
        print(
            json.dumps(
                validate(repo, (repo / args.requirements).resolve(), (repo / args.evidence).resolve()),
                ensure_ascii=True,
                indent=2,
                sort_keys=True,
            )
        )
        return 0
    except EvidenceViolation as exc:
        print(f"AGE001: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
