#!/usr/bin/env python3
"""Lesende Eignungsprüfung / Read-only eligibility assessment."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
SOURCE_REPO = Path(__file__).resolve().parents[3]
CONTRACT = "requirements/baseline/series-eligibility-contract.json"
LEGACY = "specs/intake-review-fixtures/meta-lh-04/validate-series-eligibility.py"


def pair(de: str, en: str) -> dict:
    return {"de": de, "en": en}


def reason(code: str, criterion: str | None, de: str, en: str) -> dict:
    return {"code": code, "criterion": criterion, **pair(de, en)}


def diagnostic(failure: str = "ProductFailure") -> dict:
    return {
        "schemaVersion": "1.0", "mode": None, "criteria": {},
        "outcome": "Blocked", "reasons": [], "failureClass": failure,
        "authorityGranted": False,
        "nextAction": pair("Eingaben und Nachweise erneut prüfen; nichts starten.",
                           "Reassess inputs and evidence; start nothing."),
    }


def load_legacy():
    spec = importlib.util.spec_from_file_location("aoc_eligibility_legacy", SOURCE_REPO / LEGACY)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def assess(repo: Path, fixture_path: str) -> tuple[dict, int]:
    contract = json.loads((repo / CONTRACT).read_text(encoding="utf-8-sig"))
    fixture = json.loads((repo / fixture_path).read_text(encoding="utf-8-sig"))
    keys = contract["criteria"]
    if len(keys) != 9 or len(set(keys)) != 9 or set(fixture["criteria"]) != set(keys):
        raise ValueError("criteria")
    mode = fixture["mode"]
    if mode not in contract["modes"]:
        raise ValueError("mode")
    result = diagnostic(None)
    result.update(mode=mode, criteria={key: fixture["criteria"][key] for key in keys})
    eligible = mode != "blocked"
    if mode == "parallel-autonomous":
        eligible = load_legacy().meets_parallel_eligibility(contract, fixture)
    elif not fixture.get("currentAuthority", False):
        eligible = False
    # Ein Flag ersetzt keinen Integrationsplan. / A flag cannot replace an integration plan.
    if fixture["criteria"]["integration"] != "planned":
        eligible = False
        result["failureClass"] = "ProductFailure"
        result["reasons"].append(reason("EL_CRITERION", "integration",
            "Ein gültiger Integrationsplan fehlt.", "A valid integration plan is missing."))
    result["outcome"] = "Eligible" if eligible else "Blocked"
    # Erst berechnen, danach die Fixture-Erwartung prüfen. / Compute before assertion.
    exit_code = 0
    if result["outcome"] != fixture.get("expectedOutcome"):
        result["failureClass"] = "ProductFailure"
        result["reasons"].append(reason("EL_EXPECTATION", None,
            "Die Fixture-Erwartung weicht vom berechneten Ergebnis ab.",
            "The fixture expectation differs from the calculated outcome."))
        exit_code = 2
    return result, exit_code


def main() -> int:
    parser = argparse.ArgumentParser(description="Eignung prüfen / Assess eligibility")
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--fixture", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        result, exit_code = assess(args.repo.resolve(), args.fixture)
    except (OSError, ValueError, KeyError, TypeError):
        result, exit_code = diagnostic(), 2
        result["reasons"] = [reason("EL_INPUT", None,
            "Eingabe ist nicht sicher prüfbar.", "Input cannot be assessed safely.")]
    if args.json:
        print(json.dumps(result, ensure_ascii=False))
    else:
        print("Ergebnis / Outcome: " + result["outcome"])
        for item in result["reasons"]:
            print(item["de"] + " / " + item["en"])
        print(result["nextAction"]["de"] + " / " + result["nextAction"]["en"])
        print("Keine Startfreigabe. / No start authority granted.")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
