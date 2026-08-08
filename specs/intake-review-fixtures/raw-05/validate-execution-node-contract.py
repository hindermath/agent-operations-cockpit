#!/usr/bin/env python3
"""Validate the RAW-05 Execution Node requirements contract and fixtures."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path


class ContractError(ValueError):
    """A stable, machine-readable validation error."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(f"{code}: {message}")
        self.code = code


def load_json(file_path: Path) -> dict:
    value = json.loads(file_path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ContractError("EN001", f"{file_path}: root must be an object")
    return value


def validate_contract(contract: dict) -> None:
    if (
        contract.get("schemaVersion") != "1.0"
        or contract.get("documentType") != "AocExecutionNodeContract"
        or contract.get("owner") != "RAW-05"
    ):
        raise ContractError("EN001", "contract identity or ownership is invalid")

    decisions = contract.get("decisions", {})
    transport = decisions.get("transportBoundary", {})
    legacy = decisions.get("legacyDecision", {})
    attestation = decisions.get("attestation", {})
    timing = decisions.get("timeoutFreshnessRecovery", {})
    if (
        transport.get("id") != "IAD501"
        or transport.get("remoteNodesEnabled") is not False
        or transport.get("remoteTransportOwner") != "RAW-06/IAD604"
        or transport.get("localAdapters") != ["Host", "WSL", "Container", "ABS-DD"]
    ):
        raise ContractError("EN002", "IAD501 transport boundary is invalid")
    if (
        legacy.get("id") != "DEC-T06"
        or legacy.get("status") != "Superseded"
        or legacy.get("supersededBy") != ["IAD502", "IAD503"]
        or attestation.get("id") != "IAD502"
        or attestation.get("model") != "MultiSourceFailClosed"
        or timing.get("id") != "IAD503"
        or timing.get("profileScope") != "NodeTypeAndCapability"
    ):
        raise ContractError("EN003", "IAD502-IAD503 must supersede DEC-T06")

    expected_attestation = {
        "nodeType", "platform", "trustZone", "runtimeIdentity",
        "declaredMounts", "observedMounts", "capabilityProbe",
        "policyVersion", "observedAt",
    }
    if set(attestation.get("requiredEvidence", [])) != expected_attestation:
        raise ContractError("EN004", "multi-source attestation evidence is incomplete")
    if attestation.get("results") != ["Verified", "Limited", "Untrusted", "Unknown"]:
        raise ContractError("EN004", "attestation result classes are invalid")

    freshness = timing.get("freshnessModel", {})
    if (
        timing.get("requiredPositiveFields") != ["probeTimeoutSeconds", "freshnessTSeconds"]
        or list(freshness) != ["Fresh", "Aging", "Stale", "Expired", "Unknown"]
        or timing.get("recovery") != "A new read-only probe is the only recovery action"
    ):
        raise ContractError("EN005", "timeout, freshness, or recovery policy is invalid")

    descriptor = contract.get("descriptor", {})
    if descriptor.get("nodeTypes") != ["Host", "WSL", "Container", "ABS-DD", "Remote"]:
        raise ContractError("EN005", "node types are invalid")
    if descriptor.get("hostAndSandboxIdentityMustDiffer") is not True:
        raise ContractError("EN005", "host and sandbox identities must differ")

    mounts = contract.get("mountPolicy", {})
    if (
        mounts.get("researchMode") != "ReadOnly"
        or mounts.get("researchWriteAuthority") != "None"
        or mounts.get("absolutePersonalHostPathsAllowed") is not False
        or mounts.get("automaticMountMutationAllowed") is not False
    ):
        raise ContractError("EN005", "read-only mount boundary is invalid")

    handoffs = contract.get("handoffs", [])
    expected_handoffs = {
        ("H-RAW05-RAW02", "RAW-05", "RAW-02", "PreferredSerialOrderNonBinding"),
        ("H-RAW05-RAW06", "RAW-05", "RAW-06", "HardCompletionGateBinding"),
        ("H-RAW05-RAW08", "RAW-05", "RAW-08", "AssessmentBaselineBinding"),
    }
    actual_handoffs = {
        (item.get("id"), item.get("producer"), item.get("consumer"), item.get("seriesRelation"))
        for item in handoffs if isinstance(item, dict)
    }
    if actual_handoffs != expected_handoffs or any(
        not item.get("version") or not item.get("authority") or not item.get("failureBehavior")
        for item in handoffs if isinstance(item, dict)
    ):
        raise ContractError("EN006", "handoff type, authority, or failure behaviour is incomplete")

    cross_cutting = contract.get("crossCutting", {})
    if cross_cutting.get("platforms") != ["macOS", "Linux", "Windows"] or any(
        not cross_cutting.get(key)
        for key in ("security", "privacy", "publicContent", "accessibility", "containerAndWsl", "supplyChain")
    ):
        raise ContractError("EN006", "cross-cutting applicability is incomplete")


def parse_timestamp(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed


def classify_freshness(case: dict) -> str:
    observed = parse_timestamp(case.get("observedAt"))
    as_of = parse_timestamp(case.get("freshnessAsOf"))
    profile = case.get("profile", {})
    threshold = profile.get("freshnessTSeconds")
    if (
        observed is None or as_of is None
        or not isinstance(threshold, (int, float)) or isinstance(threshold, bool)
        or threshold <= 0 or as_of < observed
    ):
        return "Unknown"
    age = (as_of - observed).total_seconds()
    if age <= 0.5 * threshold:
        return "Fresh"
    if age <= threshold:
        return "Aging"
    if age <= 2 * threshold:
        return "Stale"
    return "Expired"


def validate_mounts(case: dict) -> tuple[bool, bool]:
    mounts = case.get("mounts")
    if not isinstance(mounts, list):
        return False, False
    drift = False
    personal_path = re.compile(r"(^/Users/|^/home/|^[A-Za-z]:[\\/]Users[\\/])")
    for mount in mounts:
        if not isinstance(mount, dict):
            return False, False
        if mount.get("mode") != "ReadOnly" or mount.get("writeAuthority") != "None":
            raise ContractError("EN008", f"{case.get('id')}: research mount exceeds read-only authority")
        if any(personal_path.search(str(mount.get(field, ""))) for field in ("sourceRef", "targetRef")):
            raise ContractError("EN008", f"{case.get('id')}: personal absolute host path is prohibited")
        if mount.get("declaredMatchesObserved") is not True:
            drift = True
    return True, drift


def derive_case(case: dict) -> dict:
    case_id = case.get("id", "unnamed-case")
    node_type = case.get("nodeType")
    profile = case.get("profile", {})
    timeout = profile.get("probeTimeoutSeconds")
    if (
        not isinstance(timeout, (int, float)) or isinstance(timeout, bool) or timeout <= 0
        or not isinstance(profile.get("freshnessTSeconds"), (int, float))
        or isinstance(profile.get("freshnessTSeconds"), bool)
        or profile.get("freshnessTSeconds") <= 0
    ):
        raise ContractError("EN005", f"{case_id}: profile thresholds must be positive")

    if node_type == "Remote":
        if case.get("remoteEnabled") is not False or case.get("endpointKind") != "Disabled":
            raise ContractError("EN007", f"{case_id}: remote nodes must remain disabled")
        return {
            "freshness": "Unknown",
            "nodeState": "Unavailable",
            "health": "Unavailable",
            "attestation": "Unknown",
            "reasonCodes": ["REMOTE_DISABLED"],
        }
    if node_type not in {"Host", "WSL", "Container", "ABS-DD"} or case.get("endpointKind") != "LocalAdapter":
        raise ContractError("EN007", f"{case_id}: local node adapter is invalid")

    identity = case.get("identity", {})
    if identity.get("stable") is not True or not identity.get("nodeId"):
        raise ContractError("EN009", f"{case_id}: stable node identity is missing")

    mounts_valid, mount_drift = validate_mounts(case)
    attestation = case.get("attestationEvidence", {})
    if not mounts_valid or attestation.get("complete") is not True:
        attestation_result = "Unknown"
    elif attestation.get("consistent") is not True or mount_drift:
        attestation_result = "Untrusted"
    elif case.get("probe", {}).get("outcome") == "NotFound":
        attestation_result = "Unknown"
    elif case.get("probe", {}).get("outcome") == "AccessRefused":
        attestation_result = "Limited"
    else:
        attestation_result = "Verified"
    if attestation.get("expectedResult") != attestation_result:
        raise ContractError("EN009", f"{case_id}: attestation must fail closed as {attestation_result}")

    side_effects = case.get("sideEffects")
    if side_effects != []:
        raise ContractError("EN010", f"{case_id}: probe or recovery side effects are prohibited")

    freshness = classify_freshness(case)
    probe = case.get("probe", {})
    elapsed = probe.get("elapsedSeconds", 0)
    outcome = probe.get("outcome")
    if outcome == "Timeout" or (isinstance(elapsed, (int, float)) and elapsed > timeout):
        state, health, reasons = "Unavailable", "Unavailable", ["PROBE_TIMEOUT"]
    elif outcome == "NotFound":
        state, health, reasons = "Unavailable", "Unavailable", ["NODE_NOT_FOUND"]
    elif outcome == "AccessRefused":
        state, health, reasons = "Degraded", "Degraded", ["ACCESS_REFUSED"]
    elif freshness == "Unknown" or attestation_result == "Unknown":
        state, health, reasons = "Unknown", "Unknown", ["NODE_EVIDENCE_MISSING"]
    elif mount_drift or attestation_result == "Untrusted":
        state, health, reasons = "Degraded", "Degraded", ["MOUNT_DRIFT"]
    elif freshness == "Expired":
        state, health, reasons = "Unavailable", "Unavailable", ["EVIDENCE_EXPIRED"]
    elif freshness == "Stale":
        state, health, reasons = "Stale", "Degraded", ["EVIDENCE_STALE"]
    else:
        state, health, reasons = "Known", "Healthy", ["NODE_VERIFIED"]
    return {
        "freshness": freshness,
        "nodeState": state,
        "health": health,
        "attestation": attestation_result,
        "reasonCodes": reasons,
    }


def validate_fixture(fixture: dict) -> None:
    if fixture.get("fixtureKind") != "ExecutionNodeCases":
        raise ContractError("EN011", "fixtureKind must be ExecutionNodeCases")
    cases = fixture.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ContractError("EN011", "at least one execution-node case is required")
    node_ids: dict[str, str] = {}
    for case in cases:
        node_type = case.get("nodeType")
        identity = case.get("identity", {})
        node_id = identity.get("nodeId")
        if node_type != "Remote" and node_id:
            previous = node_ids.get(node_id)
            if previous and previous != node_type:
                raise ContractError("EN012", f"{case.get('id')}: node identity collides with {previous}")
            node_ids[node_id] = node_type
        actual = derive_case(case)
        if case.get("expected") != actual:
            raise ContractError("EN011", f"{case.get('id')}: expected {case.get('expected')}, derived {actual}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", required=True, type=Path)
    parser.add_argument("--fixture", required=True, type=Path)
    args = parser.parse_args()
    contract = load_json(args.contract)
    fixture = load_json(args.fixture)
    expected_outcome = fixture.get("expectedOutcome")
    try:
        validate_contract(contract)
        validate_fixture(fixture)
    except ContractError as exc:
        if expected_outcome == "Rejected" and fixture.get("expectedError") == exc.code:
            print(f"{fixture.get('fixtureId')}: Abgelehnt / Rejected ({exc})")
            return 0
        raise
    if expected_outcome == "Rejected":
        raise ContractError("EN013", "fixture expected rejection but validation passed")
    if expected_outcome != "Valid":
        raise ContractError("EN013", "expectedOutcome must be Valid or Rejected")
    print(f"{fixture.get('fixtureId')}: Gültig / Valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
