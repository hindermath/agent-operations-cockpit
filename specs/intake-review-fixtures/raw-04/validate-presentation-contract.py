#!/usr/bin/env python3
"""Validate the RAW-04 Presentation Contract and its review fixtures."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


class ContractError(ValueError):
    """A stable, machine-readable validation error."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(f"{code}: {message}")
        self.code = code


def load_json(file_path: Path) -> dict:
    value = json.loads(file_path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ContractError("PR001", f"{file_path}: root must be an object")
    return value


def validate_contract(contract: dict) -> None:
    if (
        contract.get("schemaVersion") != "1.0"
        or contract.get("documentType") != "AocPresentationContract"
        or contract.get("owner") != "RAW-04"
    ):
        raise ContractError("PR001", "contract identity or ownership is invalid")

    decision = contract.get("decision", {})
    if (
        decision.get("id") != "DEC-T04"
        or decision.get("status") != "Superseded"
        or decision.get("supersededBy") != ["IAD401", "IAD402", "IAD403"]
    ):
        raise ContractError("PR002", "IAD401-IAD403 must fully supersede DEC-T04")

    boundary = contract.get("boundary", {})
    if (
        boundary.get("frameworkNeutral") is not True
        or boundary.get("referenceTuiAdapter") != "Spectre.Console"
        or boundary.get("frameworkTypesAllowedInContract") is not False
        or boundary.get("canonicalProjections") != ["Console", "JSON"]
    ):
        raise ContractError("PR003", "the framework-neutral Console/JSON boundary is invalid")

    handoffs = contract.get("handoffs", [])
    expected_handoffs = {
        ("H-RAW03-RAW04", "RAW-03", "RAW-04", "State Envelope Contract"),
        ("H-RAW02-RAW04", "RAW-02", "RAW-04", "Orchestration Context Contract"),
        ("H-RAW04-RAW07", "RAW-04", "RAW-07", "Presentation Contract"),
    }
    actual_handoffs = {
        (item.get("id"), item.get("producer"), item.get("consumer"), item.get("contract"))
        for item in handoffs
        if isinstance(item, dict)
    }
    if actual_handoffs != expected_handoffs or any(
        not item.get("version") or not item.get("authority") or not item.get("failureBehavior")
        for item in handoffs
        if isinstance(item, dict)
    ):
        raise ContractError("PR004", "handoff versions, authority, or failure behaviour are incomplete")

    layout = contract.get("layoutPolicy", {})
    if layout.get("profiles") != [
        {"name": "Linear", "minimumWidthInclusive": None, "maximumWidthInclusive": 39},
        {"name": "Compact", "minimumWidthInclusive": 40, "maximumWidthInclusive": 99},
        {"name": "Enhanced", "minimumWidthInclusive": 100, "maximumWidthInclusive": None},
    ] or layout.get("referenceWidths") != [39, 79, 120]:
        raise ContractError("PR005", "layout profiles or reference widths are invalid")

    localization = contract.get("localizationPolicy", {})
    if (
        localization.get("schemaVersion") != 1
        or localization.get("catalogFormat") != "JSON"
        or localization.get("messageIdRequired") is not True
        or localization.get("requiredBcp47Languages") != ["de", "en"]
        or localization.get("displayOrder") != ["de", "en"]
        or localization.get("unsupportedLanguageFallback") != "de"
        or localization.get("missingRequiredTranslation") != "ValidationError"
    ):
        raise ContractError("PR005", "localization and fallback policy are invalid")

    record = contract.get("presentationRecord", {})
    expected_fields = {
        "schemaVersion", "presentationId", "stateStatus", "statusLabel",
        "reasonCodes", "messageId", "translations", "focusOrder",
        "capabilities", "degraded",
    }
    if set(record.get("requiredFields", [])) != expected_fields:
        raise ContractError("PR005", "presentation record fields are incomplete")
    if (
        record.get("visibleStateStatuses") != ["Known", "Unknown", "Stale", "Unavailable", "Degraded"]
        or record.get("colourOnlyMeaningAllowed") is not False
        or record.get("mouseRequired") is not False
        or record.get("canonicalStateMutationAllowed") is not False
    ):
        raise ContractError("PR005", "presentation status and accessibility invariants are invalid")

    cross_cutting = contract.get("crossCutting", {})
    if cross_cutting.get("platforms") != ["macOS", "Linux", "Windows"] or any(
        not cross_cutting.get(key)
        for key in ("security", "privacy", "publicContent", "accessibility", "supplyChain")
    ):
        raise ContractError("PR005", "cross-cutting evidence is incomplete")


def select_layout(width: object, terminal_interactive: object, tui_adapter_available: object) -> str:
    if terminal_interactive is not True or tui_adapter_available is not True:
        return "Linear"
    if not isinstance(width, int) or isinstance(width, bool) or width < 1:
        raise ContractError("PR006", "terminal width must be a positive integer")
    if width < 40:
        return "Linear"
    if width < 100:
        return "Compact"
    return "Enhanced"


def validate_fixture(fixture: dict) -> None:
    if fixture.get("fixtureKind") != "PresentationCases":
        raise ContractError("PR006", "fixtureKind must be PresentationCases")
    cases = fixture.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ContractError("PR006", "at least one presentation case is required")
    for case in cases:
        case_id = case.get("id", "unnamed-case")
        actual_layout = select_layout(
            case.get("width"),
            case.get("terminalInteractive"),
            case.get("tuiAdapterAvailable"),
        )
        if actual_layout != case.get("expectedLayout"):
            raise ContractError("PR006", f"{case_id}: expected {case.get('expectedLayout')}, selected {actual_layout}")

        status = case.get("stateStatus")
        label = case.get("statusLabel")
        expected_labels = {
            "Known": "Bekannt / Known",
            "Unknown": "Unbekannt / Unknown",
            "Stale": "Veraltet / Stale",
            "Unavailable": "Nicht verfügbar / Unavailable",
            "Degraded": "Eingeschränkt / Degraded",
        }
        if status not in expected_labels or label != expected_labels[status]:
            raise ContractError("PR007", f"{case_id}: visible status label is missing or invalid")

        message_id = case.get("messageId")
        translations = case.get("translations")
        if not isinstance(message_id, str) or not message_id.strip() or not isinstance(translations, dict):
            raise ContractError("PR008", f"{case_id}: messageId or translation catalog is missing")
        if any(not isinstance(translations.get(language), str) or not translations[language].strip() for language in ("de", "en")):
            raise ContractError("PR008", f"{case_id}: German and English translations are required")

        if case.get("consoleSemantics") != case.get("jsonSemantics"):
            raise ContractError("PR009", f"{case_id}: Console and JSON semantics differ")

        focus_order = case.get("focusOrder")
        if (
            not isinstance(focus_order, list)
            or not focus_order
            or any(not isinstance(position, int) or isinstance(position, bool) or position < 1 for position in focus_order)
            or focus_order != sorted(set(focus_order))
        ):
            raise ContractError("PR010", f"{case_id}: focus order must be positive, unique, and linear")

        if case.get("surfaceAvailable") is False:
            semantics = case.get("consoleSemantics", {})
            if status != "Degraded" or "SURFACE_UNAVAILABLE" not in semantics.get("reasonCodes", []):
                raise ContractError("PR011", f"{case_id}: unavailable surface must be visibly Degraded")


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
            print(f"{fixture.get('fixtureId')}: Rejected ({exc})")
            return 0
        raise
    if expected_outcome == "Rejected":
        raise ContractError("PR012", "fixture expected rejection but validation passed")
    if expected_outcome != "Valid":
        raise ContractError("PR012", "expectedOutcome must be Valid or Rejected")
    print(f"{fixture.get('fixtureId')}: Valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
