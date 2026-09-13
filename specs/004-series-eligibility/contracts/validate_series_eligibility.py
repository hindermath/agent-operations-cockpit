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
FLAGS = ("currentAuthority", "disjointWrites", "sharedOpenDecisions",
         "consolidationReview", "abortRule", "recoveryRule")
VALUES = {
    "authority": ("current-and-explicit",), "sideEffects": ("bounded",),
    "reversibility": ("recoverable",), "writeScope": ("disjoint", "shared"),
    "decisions": ("no-shared-open-decisions", "shared-open-decision"),
    "integration": ("planned",), "review": ("consolidation-review-planned",),
    "abort": ("defined",), "recovery": ("defined",),
}
CRITERION_FLAGS = dict(zip(("authority", "writeScope", "decisions", "review", "abort", "recovery"), FLAGS))


def unique_object(pairs):
    # Vor dem Dictionary darf kein Schlüssel verloren gehen. / Reject before loss.
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate key")
        result[key] = value
    return result


def load_json(path: Path):
    def reject_constant(value):
        raise ValueError("non-JSON number")
    return json.loads(path.read_text(encoding="utf-8-sig"), object_pairs_hook=unique_object,
                      parse_constant=reject_constant)


def validate_schema(contract, fixture):
    keys, modes = contract["criteria"], contract["modes"]
    for values, count in [(keys, 9), (modes, 6)]:
        if (not isinstance(values, list) or len(values) != count
                or not all(isinstance(v, str) and v for v in values)
                or len(set(values)) != count):
            raise ValueError("contract set")
    required = {"fixtureId", "mode", "criteria", "expectedOutcome"}
    if (not isinstance(fixture, dict) or not required <= set(fixture)
            or set(fixture) - required - set(FLAGS)):
        raise ValueError("fixture fields")
    if (not isinstance(fixture["fixtureId"], str) or not fixture["fixtureId"].strip()
            or not isinstance(fixture["mode"], str) or fixture["mode"] not in modes
            or fixture["expectedOutcome"] not in ("Eligible", "Blocked")
            or not isinstance(fixture["criteria"], dict)
            or set(fixture["criteria"]) != set(keys)):
        raise ValueError("fixture schema")
    return keys


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


def failed_input(failure="ProductFailure"):
    result = diagnostic(failure)
    result["reasons"] = [reason("EL_PROVIDER" if failure == "ProviderFailure" else "EL_INPUT", None,
        "Die Laufzeitprüfung ist fehlgeschlagen." if failure == "ProviderFailure" else "Eingabe ist nicht sicher prüfbar.",
        "The runtime check failed." if failure == "ProviderFailure" else "Input cannot be assessed safely.")]
    return result


class SafeParser(argparse.ArgumentParser):
    def error(self, message):
        # argparse-Rohwerte nicht anzeigen. / Do not echo parser input.
        raise ValueError("arguments")


def load_legacy():
    spec = importlib.util.spec_from_file_location("aoc_eligibility_legacy", SOURCE_REPO / LEGACY)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def assess(repo: Path, fixture_path: str) -> tuple[dict, int]:
    contract = load_json(repo / CONTRACT)
    fixture = load_json(repo / fixture_path)
    keys = validate_schema(contract, fixture)
    mode = fixture["mode"]
    result = diagnostic(None)
    result["mode"] = mode
    for key in keys:
        value = fixture["criteria"][key]
        valid = isinstance(value, str) and value in VALUES[key]
        # Unbekannte Rohwerte nie ausgeben. / Never echo unknown raw values.
        result["criteria"][key] = value if valid else None
        if not valid:
            result["reasons"].append(reason("EL_CRITERION", key,
                "Ein gültiger Kriterienwert fehlt.", "A valid criterion value is missing."))
        flag = CRITERION_FLAGS.get(key)
        if flag is None:
            continue
        required = flag == "currentAuthority" or mode == "parallel-autonomous"
        if flag not in fixture:
            if required:
                result["reasons"].append(reason("EL_FLAG_REQUIRED", key,
                    "Der erforderliche Nachweis fehlt.", "The required evidence flag is missing."))
        elif type(fixture[flag]) is not bool:
            result["reasons"].append(reason("EL_FLAG_TYPE", key,
                "Der Nachweis muss true oder false sein.", "The evidence flag must be true or false."))
        elif valid:
            expected_flag = (value == "disjoint" if key == "writeScope" else
                             value == "shared-open-decision" if key == "decisions" else True)
            if fixture[flag] != expected_flag:
                result["reasons"].append(reason("EL_FLAG_CONFLICT", key,
                    "Kriterium und Nachweis widersprechen sich.", "The criterion and evidence flag conflict."))
    invalid = bool(result["reasons"])
    result["failureClass"] = "ProductFailure" if invalid else None
    eligible = not invalid and mode != "blocked"
    if eligible and mode == "parallel-autonomous":
        eligible = load_legacy().meets_parallel_eligibility(contract, fixture)
        for key, negative in [("writeScope", "shared"), ("decisions", "shared-open-decision")]:
            if fixture["criteria"][key] == negative:
                result["reasons"].append(reason("EL_PARALLEL_SHARED", key,
                    "Gemeinsame Änderungen oder offene Entscheidungen verhindern Parallelität.",
                    "Shared writes or open decisions prevent parallel execution."))
    result["outcome"] = "Eligible" if eligible else "Blocked"
    if not invalid and mode == "blocked":
        result["reasons"].append(reason("EL_MODE_BLOCKED", None,
            "Der gewählte Modus bleibt gesperrt.", "The selected mode remains blocked."))
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
    parser = SafeParser(description="Eignung prüfen / Assess eligibility")
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--fixture", required=True)
    parser.add_argument("--json", action="store_true")
    emit_json = "--json" in sys.argv[1:]
    try:
        args = parser.parse_args()
        result, exit_code = assess(args.repo.resolve(), args.fixture)
    except (OSError, ValueError, KeyError, TypeError, IndexError, AttributeError):
        result, exit_code = failed_input(), 2
    except Exception:
        # Unerwartete Laufzeitfehler bleiben getrennt. / Keep runtime faults separate.
        result, exit_code = failed_input("ProviderFailure"), 3
    if emit_json:
        print(json.dumps(result, ensure_ascii=False))
    else:
        print("Modus / Mode: " + (result["mode"] or "NotAssessed"))
        for key, value in result["criteria"].items():
            print(key + ": " + (value or "NotAssessed"))
        print("Ergebnis / Outcome: " + result["outcome"])
        for item in result["reasons"]:
            print(item["de"] + " / " + item["en"])
        print("Nächste Aktion / Next action: " + result["nextAction"]["de"] + " / " + result["nextAction"]["en"])
        print("Keine Startfreigabe. / No start authority granted.")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
