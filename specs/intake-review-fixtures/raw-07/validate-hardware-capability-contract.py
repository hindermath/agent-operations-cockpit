#!/usr/bin/env python3
"""Validate the RAW-07 requirements contract without hardware I/O."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


class ContractError(ValueError):
    """A stable, machine-readable validation error."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(f"{code}: {message}")
        self.code = code


def read_json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ContractError("HWC000_INVALID_JSON", "JSON root must be an object")
    return data


def validate_contract(contract: dict) -> None:
    if (
        contract.get("documentType") != "AocHardwareCapabilityContract"
        or contract.get("schemaVersion") != "requirements-v1"
        or contract.get("owner") != "RAW-07"
    ):
        raise ContractError("HWC000_INVALID_CONTRACT", "contract identity is invalid")

    boundary = contract.get("boundary", {})
    if (
        boundary.get("presentationContractOwner") != "RAW-04"
        or boundary.get("hardwareCapabilityOwner") != "RAW-07"
        or boundary.get("workspaceStateAndProductCommandOwned") is not False
        or boundary.get("domainLogicAllowedInAdapters") is not False
        or boundary.get("hardwareIoEnabledByThisContract") is not False
    ):
        raise ContractError("HWC000_INVALID_CONTRACT", "ownership or I/O boundary is invalid")

    decisions = contract.get("decisions", {})
    midi = decisions.get("midiLibrary", {})
    if (
        midi.get("id") != "IAD701"
        or midi.get("model") != "CrossPlatformMidiLibraryBehindThinAdapter"
        or midi.get("crossPlatformRequired") is not True
        or midi.get("vendorNeutralCapabilityBoundaryRequired") is not True
        or midi.get("rawMidiAllowedInDomainContract") is not False
        or midi.get("sysExAllowedInDomainContract") is not False
    ):
        raise ContractError("HWC007_RAW_PROTOCOL_LEAK", "IAD701 is incomplete")

    elgato = decisions.get("elgatoTransport", {})
    if (
        elgato.get("id") != "IAD702"
        or elgato.get("model") != "OfficialSdkIsolatedThinBridge"
        or elgato.get("officialSdkRequired") is not True
        or elgato.get("typeScriptAllowedOnlyWhenSdkRequiresIt") is not True
        or elgato.get("normalizedCapabilityEventsRequired") is not True
        or elgato.get("vendorLogicAllowedInAocCore") is not False
    ):
        raise ContractError("HWC008_DOMAIN_COMMAND_FORBIDDEN", "IAD702 is incomplete")

    devices = decisions.get("firstApprovedDeviceSet", {})
    if (
        devices.get("id") != "IAD703"
        or devices.get("model") != "TwoClassReferenceWave"
        or devices.get("requiredDeviceClasses") != ["MidiController", "StreamDeck"]
        or devices.get("devicesPerRequiredClass") != 1
        or devices.get("xboxIncludedInFirstWave") is not False
        or devices.get("xboxRemainsSeparateCandidate") is not True
        or devices.get("serialNumbersAllowedInPublicProfiles") is not False
    ):
        raise ContractError("HWC009_DEVICE_NOT_APPROVED", "IAD703 is incomplete")

    lab = decisions.get("labAndSafetyApproval", {})
    required_evidence = {
        "VersionedLabInventory",
        "DeviceSpecificRiskAndSafetyAssessment",
        "VerifiedKillSwitch",
        "SupervisedTestPlan",
        "DocumentedApproval",
    }
    if (
        lab.get("id") != "IAD704"
        or lab.get("model") != "ExplicitPreFieldTestApprovalGate"
        or set(lab.get("requiredEvidence", [])) != required_evidence
        or lab.get("missingEvidenceState") != "Unknown"
        or lab.get("hardwareIoAllowedWhenApprovalIsNotApproved") is not False
        or lab.get("approvalGrantsProductCommandAuthority") is not False
    ):
        raise ContractError("HWC010_LAB_APPROVAL_REQUIRED", "IAD704 is incomplete")

    capability = contract.get("capabilityModel", {})
    if (
        capability.get("vendorNeutralCapabilities")
        != ["Button", "Encoder", "Fader", "Pad", "Text", "Icon", "Feedback"]
        or capability.get("profilesDeclarativeAndVersioned") is not True
        or capability.get("profilesPublishableWithoutSerialNumbers") is not True
        or capability.get("hardwareFailureMayDegradeConsoleOrJsonBaseline") is not False
        or capability.get("userFunctionsRequireKeyboardOrTextAlternative") is not True
    ):
        raise ContractError("HWC000_INVALID_CONTRACT", "capability model is incomplete")

    handoffs = contract.get("handoffs", [])
    handoff_keys = {
        (item.get("id"), item.get("producer"), item.get("consumer"))
        for item in handoffs
        if isinstance(item, dict)
    }
    if handoff_keys != {
        ("H-RAW04-RAW07", "RAW-04", "RAW-07"),
        ("H-RAW07-AOC", "RAW-07", "AOC Presentation and Orchestration"),
    }:
        raise ContractError("HWC000_INVALID_CONTRACT", "handoff set is invalid")

    cross_cutting = contract.get("crossCutting", {})
    if (
        cross_cutting.get("platforms") != ["macOS", "Linux", "Windows"]
        or cross_cutting.get("privacyDataMinimised") is not True
        or cross_cutting.get("serialNumbersExcludedFromPublicEvidence") is not True
        or cross_cutting.get("documentationGermanFirstEnglishSecond") is not True
        or cross_cutting.get("cefrB2") is not True
        or cross_cutting.get("wcag22AAWhereApplicable") is not True
    ):
        raise ContractError("HWC000_INVALID_CONTRACT", "cross-cutting contract is incomplete")


def validate_fixture(fixture: dict) -> tuple[str, str]:
    fixture_id = fixture.get("fixtureId")
    kind = fixture.get("fixtureKind")
    expected = fixture.get("expectedOutcome")
    if not isinstance(fixture_id, str) or not fixture_id:
        raise ContractError("HWC000_INVALID_FIXTURE", "fixtureId is required")

    if kind == "ValidContract":
        cases = fixture.get("cases")
        if expected != "Valid" or not isinstance(cases, list) or len(cases) != 2:
            raise ContractError("HWC000_INVALID_FIXTURE", "two positive device cases are required")
        if {case.get("deviceClass") for case in cases} != {"MidiController", "StreamDeck"}:
            raise ContractError("HWC009_DEVICE_NOT_APPROVED", "reference wave is incomplete")
        for case in cases:
            if (
                case.get("rawProtocolInDomain") is not False
                or case.get("domainCommandEmitted") is not False
                or case.get("deviceApproved") is not True
                or case.get("labApproval") != "Approved"
                or case.get("killSwitchVerified") is not True
            ):
                raise ContractError("HWC010_LAB_APPROVAL_REQUIRED", "positive case is unsafe")
        expected_failures = {
            ("Disconnect", "Disconnected"),
            ("UnknownControl", "Unsupported"),
            ("MalformedMidi", "RejectedInAdapter"),
        }
        actual_failures = {
            (case.get("input"), case.get("expectedState"))
            for case in fixture.get("failureCases", [])
            if isinstance(case, dict)
        }
        if actual_failures != expected_failures:
            raise ContractError("HWC000_INVALID_FIXTURE", "failure coverage is incomplete")
        return fixture_id, "Gültig / Valid"

    negative_rules = {
        "RawProtocolLeak": (
            "HWC007_RAW_PROTOCOL_LEAK",
            fixture.get("rawMidiInDomainContract") is True
            or fixture.get("vendorProtocolInDomainContract") is True,
        ),
        "DomainCommand": (
            "HWC008_DOMAIN_COMMAND_FORBIDDEN",
            fixture.get("adapterEmitsProductCommand") is True
            or fixture.get("adapterOwnsState") is True,
        ),
        "UnapprovedDevice": (
            "HWC009_DEVICE_NOT_APPROVED",
            fixture.get("includedInFirstWave") is False
            and fixture.get("separateEvidencePresent") is False,
        ),
        "MissingLabApproval": (
            "HWC010_LAB_APPROVAL_REQUIRED",
            fixture.get("fieldTestRequested") is True
            and (
                fixture.get("labInventoryPresent") is False
                or fixture.get("riskAndSafetyAssessmentPresent") is False
                or fixture.get("documentedApproval") != "Approved"
            ),
        ),
        "MissingKillSwitch": (
            "HWC011_KILL_SWITCH_REQUIRED",
            fixture.get("fieldTestRequested") is True
            and fixture.get("killSwitchVerified") is False,
        ),
    }
    if kind not in negative_rules:
        raise ContractError("HWC000_INVALID_FIXTURE", f"unknown fixtureKind {kind}")
    reason_code, condition = negative_rules[kind]
    if expected != "Rejected" or fixture.get("expectedReasonCode") != reason_code or not condition:
        raise ContractError("HWC000_INVALID_FIXTURE", "negative fixture does not prove its rejection")
    return fixture_id, f"Abgelehnt / Rejected ({reason_code})"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", required=True, type=Path)
    parser.add_argument("--fixture", required=True, type=Path)
    args = parser.parse_args()

    try:
        contract = read_json(args.contract)
        fixture = read_json(args.fixture)
        validate_contract(contract)
        fixture_id, result = validate_fixture(fixture)
    except (OSError, json.JSONDecodeError, ContractError) as exc:
        print(f"ERROR: {exc}")
        return 2

    print(f"{fixture_id}: {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
