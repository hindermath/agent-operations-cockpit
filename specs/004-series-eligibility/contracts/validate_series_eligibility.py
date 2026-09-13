#!/usr/bin/env python3
"""Lesende Eignungsprüfung / Read-only eligibility assessment."""

from __future__ import annotations

import argparse
import os
import stat
import types
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
MODES = ("manual-assisted", "single-autonomous", "serial-autonomous",
         "parallel-autonomous", "research-only", "blocked")
PARALLEL_ELIGIBILITY = {
    "requiresCurrentAuthority": True,
    "requiresDisjointWrites": True,
    "allowsSharedOpenDecisions": False,
    "requiresConsolidationReview": True,
    "requiresAbortRule": True,
    "requiresRecoveryRule": True,
}
FAILURE_TAXONOMY = ["ProviderFailure", "ProductFailure"]
CRITERION_FLAGS = dict(zip(("authority", "writeScope", "decisions", "review", "abort", "recovery"), FLAGS))

class ReadBoundary:
    """Eine Wurzel für Datenzugriffe / One root for data access."""

    def __init__(self, repo):
        self.root = Path(repo).resolve(strict=True)
        if not self.root.is_dir():
            raise ValueError("repository")

    @staticmethod
    def relative(value):
        # Windows-Formen auch auf POSIX ablehnen. / Reject Windows forms on POSIX too.
        if (not isinstance(value, str) or not value or '\x00' in value
                or '\\' in value or ':' in value or value.startswith('/')
                or any(part in ('', '.', '..') for part in value.split('/'))):
            raise ValueError("relative path")
        return value

    def resolve(self, value, *, missing=False, directory=False):
        value = self.relative(value)
        pending, current, links = value.split('/'), self.root, 0
        while pending:
            current = current / pending.pop(0)
            # lstat liest den Link selbst; sein Ziel erst nach Containment prüfen.
            # lstat inspects the link itself; check target containment before following.
            try:
                metadata = os.lstat(current)
                mode = metadata.st_mode
            except FileNotFoundError:
                if missing:
                    return None
                raise ValueError("missing file") from None
            if stat.S_ISLNK(mode):
                links += 1
                if links > 40:
                    raise ValueError("symlink loop")
                link = os.readlink(current)
                target = Path(os.path.normpath(os.path.join(current.parent, link)))
                try:
                    relative = target.relative_to(self.root)
                except ValueError:
                    raise ValueError("symlink escape") from None
                pending = list(relative.parts) + pending
                current = self.root
            elif (getattr(metadata, 'st_file_attributes', 0)
                  & getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0)):
                # Unbekannte Windows-Umleitungen nicht verfolgen. / Reject other reparse points.
                raise ValueError("unsupported reparse point")
            elif pending:
                if not stat.S_ISDIR(mode):
                    raise ValueError("parent is not directory")
            elif not (stat.S_ISDIR(mode) if directory else stat.S_ISREG(mode)):
                raise ValueError("not a regular file" if not directory else "not a directory")
        if current == self.root and not directory:
            raise ValueError("not a regular file")
        return current

    def file(self, value):
        return GuardedPath(self, self.relative(value))

    def read_bytes(self, value):
        value = self.relative(value)
        if os.name == 'nt':
            return self._read_windows(value)
        return self._read_descriptor_relative(value)

    def _read_descriptor_relative(self, value):
        # Jeder Pfadteil wird relativ zu einem bereits geöffneten Verzeichnis gelesen.
        # Open every component relative to an already verified directory descriptor.
        no_follow = getattr(os, 'O_NOFOLLOW', None)
        directory = getattr(os, 'O_DIRECTORY', None)
        if no_follow is None or directory is None or os.open not in os.supports_dir_fd:
            raise OSError("descriptor-relative no-follow unavailable")
        opened = []
        try:
            root_fd = os.open(self.root, os.O_RDONLY | directory | no_follow)
            opened.append(root_fd)
            current_fd = root_fd
            parts = value.split('/')
            for part in parts[:-1]:
                next_fd = os.open(part, os.O_RDONLY | directory | no_follow,
                                  dir_fd=current_fd)
                if not stat.S_ISDIR(os.fstat(next_fd).st_mode):
                    os.close(next_fd)
                    raise ValueError("parent is not directory")
                opened.append(next_fd)
                current_fd = next_fd
            descriptor = os.open(parts[-1], os.O_RDONLY | no_follow, dir_fd=current_fd)
            if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                os.close(descriptor)
                raise ValueError("not a regular file")
            with os.fdopen(descriptor, 'rb') as stream:
                return stream.read()
        finally:
            for descriptor in reversed(opened):
                os.close(descriptor)

    def _read_windows(self, value):
        # Windows besitzt kein openat/O_NOFOLLOW. Der endgültige Handle-Pfad wird
        # deshalb vor dem ersten Byte gegen die feste Repository-Wurzel geprüft.
        # Windows lacks openat/O_NOFOLLOW; validate the opened handle path before reading.
        import ctypes
        import msvcrt

        path = self.root.joinpath(*value.split('/'))
        descriptor = os.open(path, os.O_RDONLY | getattr(os, 'O_BINARY', 0))
        try:
            handle = msvcrt.get_osfhandle(descriptor)
            kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
            final_path = kernel32.GetFinalPathNameByHandleW
            final_path.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p,
                                   ctypes.c_uint32, ctypes.c_uint32]
            final_path.restype = ctypes.c_uint32
            size = final_path(handle, None, 0, 0)
            if size == 0:
                raise OSError(ctypes.get_last_error(), "final path unavailable")
            buffer = ctypes.create_unicode_buffer(size + 1)
            if final_path(handle, buffer, len(buffer), 0) == 0:
                raise OSError(ctypes.get_last_error(), "final path unavailable")
            actual = buffer.value
            if actual.startswith('\\\\?\\UNC\\'):
                actual = '\\\\' + actual[8:]
            elif actual.startswith('\\\\?\\'):
                actual = actual[4:]
            root_value = os.path.normcase(os.path.abspath(self.root))
            actual_value = os.path.normcase(os.path.abspath(actual))
            if os.path.commonpath((root_value, actual_value)) != root_value:
                raise ValueError("path escape")
            if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                raise ValueError("not a regular file")
            with os.fdopen(descriptor, 'rb', closefd=False) as stream:
                return stream.read()
        finally:
            os.close(descriptor)


class GuardedPath:
    """Begrenzte Path-Fläche für die Engine / Bounded engine Path surface."""

    def __init__(self, boundary, value=''):
        self.boundary, self.value = boundary, value

    def __truediv__(self, value):
        value = self.boundary.relative(value)
        return GuardedPath(self.boundary, self.value + '/' + value if self.value else value)

    def __str__(self):
        return self.value

    def __lt__(self, other):
        return self.value < other.value

    def relative_to(self, root):
        if root.boundary is not self.boundary:
            raise ValueError("different boundary")
        return self.value

    def is_file(self):
        # Ein fehlendes Original ist für historische Archivbindung zulässig.
        # A missing original is allowed only as metadata for historical resolution.
        return self.boundary.resolve(self.value, missing=True) is not None

    def read_bytes(self):
        return self.boundary.read_bytes(self.value)

    def read_text(self, encoding='utf-8'):
        return self.read_bytes().decode(encoding)

    def glob(self, pattern):
        # Die unveränderte Engine entdeckt nur specs/*/intake-lifecycle.json.
        # Only the unchanged engine's lifecycle discovery pattern is supported.
        if self.value != 'specs' or pattern != '*/intake-lifecycle.json':
            raise ValueError("unsupported discovery")
        directory = self.boundary.resolve(self.value, missing=True, directory=True)
        if directory is None:
            return
        for name in sorted(os.listdir(directory)):
            child = self / name
            mode = os.lstat(directory / name).st_mode
            if not (stat.S_ISDIR(mode) or stat.S_ISLNK(mode)):
                continue
            folder = self.boundary.resolve(child.value, directory=True)
            if folder is not None:
                candidate = child / 'intake-lifecycle.json'
                if candidate.is_file():
                    yield candidate


def unique_object(pairs):
    # Vor dem Dictionary darf kein Schlüssel verloren gehen. / Reject before loss.
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate key")
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError("non-JSON number")


def load_json(path):
    if not isinstance(path, GuardedPath):
        raise ValueError("unguarded JSON path")
    return json.loads(path.read_text(encoding="utf-8-sig"), object_pairs_hook=unique_object,
                      parse_constant=reject_constant)


def validate_schema(contract, fixture):
    if (not isinstance(contract, dict)
            or set(contract) != {"schemaVersion", "documentType", "criteria", "modes",
                                 "parallelEligibility", "failureTaxonomy"}
            or contract.get("schemaVersion") != "1.0"
            or contract.get("documentType") != "SeriesEligibilityContract"
            or contract.get("criteria") != list(VALUES)
            or contract.get("modes") != list(MODES)
            or contract.get("parallelEligibility") != PARALLEL_ELIGIBILITY
            or contract.get("failureTaxonomy") != FAILURE_TAXONOMY
            or any(type(value) is not bool
                   for value in contract.get("parallelEligibility", {}).values())):
        raise ValueError("contract schema")
    keys, modes = contract["criteria"], contract["modes"]
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


def load_source_module(relative, name):
    # Kompilieren erzeugt keinen Importcache. / Compile without an import cache.
    path = ReadBoundary(SOURCE_REPO).file(relative)
    module = types.ModuleType(name)
    module.__file__ = str(SOURCE_REPO / relative)
    exec(compile(path.read_bytes(), module.__file__, "exec"), module.__dict__)
    return module


def load_legacy():
    return load_source_module(LEGACY, "aoc_eligibility_legacy")


def load_series_engine(repo):
    boundary = ReadBoundary(repo)
    root = GuardedPath(boundary)
    engine = load_source_module(
        ".specify/presets/intake-sequencing-governance/scripts/validate-intake-series.py",
        "aoc_series_isolated")
    normalizer = engine.normalized_bytes

    def guarded(path):
        if not isinstance(path, GuardedPath) or path.boundary is not boundary:
            raise ValueError("unbound path")
        return path

    def normalized(path):
        # Normalisierung wiederverwenden, Zugriff davor begrenzen.
        # Reuse normalization after enforcing the read boundary.
        return normalizer(guarded(path))

    def json_reader(path):
        data = json.loads(normalized(path).decode("utf-8"), object_pairs_hook=unique_object,
                          parse_constant=reject_constant)
        if not isinstance(data, dict):
            raise ValueError("JSON root")
        return data

    def relative(value):
        try:
            boundary.relative(value)
            return True
        except ValueError:
            return False

    # Nur diese Modulinstanz binden; Graph-, Hash- und Lifecycle-Regeln bleiben.
    # Bind only this module instance; retain graph, hash and lifecycle rules.
    engine.normalized_bytes = normalized
    engine.load_json = json_reader
    engine.relative_path = relative
    return engine, root


def receipt_provenance(engine, root, series_path, manifest):
    # Nur gebundene bestehende Receipts lesen; freie Authority-Texte nicht ausgeben.
    # Read only bound existing receipts; never display free-form authority text.
    references = manifest.get('evidencePaths', [])
    if not isinstance(references, list):
        raise ValueError("evidence paths")
    references = list(references)
    parts = series_path.split('/')
    if len(parts) == 4 and parts[:2] == ['specs', 'intake-series'] and parts[3] == 'manifest.json':
        conventional = 'specs/intake-series-receipts/' + parts[2] + '.json'
        if (root / conventional).is_file() and conventional not in references:
            references.append(conventional)
    records = []
    for relative in references:
        path = root / relative
        # Metadaten wie Inhalt gehen durch denselben Guard. / Guard metadata and content.
        if not path.is_file():
            raise ValueError("missing evidence")
        if not relative.endswith('.json'):
            continue
        evidence = engine.load_json(path)
        if evidence.get('documentType') != 'IntakeSeriesReceipt':
            continue
        receipt_summary = engine.validate_receipt(path, root)
        if (evidence['seriesId'] != manifest['seriesId']
                or evidence['manifest']['path'] != series_path):
            raise ValueError("receipt binding")
        records.append(dict(path=relative, receiptId=receipt_summary['receiptId'],
            operation=evidence['operation']['type'], authorityContext='HistoricalOnly'))
    return records


def assess_series(repo, series_path, action="status"):
    engine, root = load_series_engine(repo)
    try:
        if action not in ('status', 'next'):
            raise ValueError("query action")
        data, summary = engine.validate_manifest(root / series_path, root)
        paths = [target['path'] for target in data['orderedTargets']]
        order = {path: index for index, path in enumerate(paths)}
        for key in ['eligible', 'declaredEligible']:
            summary[key] = sorted(summary[key], key=order.__getitem__)
        summary['blockers'] = {path: sorted(summary['blockers'][path], key=order.__getitem__)
                               for path in paths if path in summary['blockers']}
        provenance = receipt_provenance(engine, root, series_path, data)

    except engine.ValidationError as error:
        result = failed_input()
        result['reasons'] = [reason(error.code, None,
            "Der Seriennachweis ist ungültig; Eingaben erneut prüfen.",
            "The series evidence is invalid; reassess the inputs.")]
        return result, 2
    except (OSError, ValueError, KeyError, TypeError, IndexError, AttributeError):
        return failed_input(), 2
    result = diagnostic(None)
    result['outcome'] = 'Eligible'
    result['summary'] = summary
    result['outcome'] = 'Eligible' if summary['eligible'] else 'Blocked'
    result.update(
        declaredLifecycle=dict(series=summary['status'], targets={
            target['path']: target['status'] for target in data['orderedTargets']}),
        reviewState='NotAssessed', eligibleCandidates=summary['eligible'],
        preferredCandidate=next(iter(summary['declaredEligible']), None),
        blockers=summary['blockers'], deliveryMode='NotAssessed',
        currentStartAuthority='NotGrantedByQuery', historicalReceiptProvenance=provenance)
    for target, predecessors in result['blockers'].items():
        for predecessor in predecessors:
            item = reason('EL_PREDECESSOR', None,
                'Ein verbindlicher Vorgänger ist noch nicht abgeschlossen.',
                'A binding predecessor is not yet completed.')
            item.update(target=target, predecessor=predecessor)
            result['reasons'].append(item)
    # Eignung ist keine Autorität; auch Stop/Recovery starten keine fremden Prozesse.
    # Eligibility grants no authority, including cancellation or recovery of others.
    if summary['status'] in ('Active', 'NeedsClarification', 'Deleted'):
        result['nextAction'] = pair(
            'Manifest und Eignung erneut prüfen; nichts starten oder teilweise mergen; fremde Prozesse nur mit gesonderter Autorität stoppen oder wiederanlaufen lassen.',
            'Reassess manifest and eligibility; start nothing and do not partially merge; stop or restart other processes only with separate authority.')
    elif summary['eligible']:
        result['nextAction'] = pair(
            'Kandidaten mit einer verantwortlichen Person prüfen und auswählen; vor jedem Start aktuelle Reviews und gesonderte Startautorität prüfen.',
            'Review and select candidates with a responsible person; verify current reviews and separate start authority before any start.')
    else:
        result['nextAction'] = pair(
            'Manifest und Nachweise mit einer verantwortlichen Person erneut prüfen; nichts starten.',
            'Reassess manifest and evidence with a responsible person; start nothing.')
    return result, 0


def assess(repo: Path, fixture_path: str) -> tuple[dict, int]:
    boundary = ReadBoundary(repo)
    contract = load_json(boundary.file(CONTRACT))
    fixture = load_json(boundary.file(fixture_path))
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
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--fixture")
    source.add_argument("--series")
    parser.add_argument("--action", choices=['status', 'next'])
    parser.add_argument("--json", action="store_true")
    emit_json = "--json" in sys.argv[1:]
    try:
        args = parser.parse_args()
        if args.fixture:
            if args.action is not None:
                raise ValueError("fixture action")
            result, exit_code = assess(args.repo.resolve(), args.fixture)
        else:
            result, exit_code = assess_series(args.repo.resolve(), args.series, args.action or 'status')
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
        if 'declaredLifecycle' in result:
            for label, key in [
                ('Lifecycle / Lifecycle', 'declaredLifecycle'), ('Review / Review', 'reviewState'),
                ('Kandidaten / Candidates', 'eligibleCandidates'), ('Präferenz / Preference', 'preferredCandidate'),
                ('Blocker / Blockers', 'blockers'), ('Liefermodus / Delivery mode', 'deliveryMode'),
                ('Startautorität / Start authority', 'currentStartAuthority'),
                ('Historische Receipt-Herkunft / Historical receipt provenance', 'historicalReceiptProvenance')]:
                print(label + ': ' + json.dumps(result[key], ensure_ascii=False))
        for item in result["reasons"]:
            print(item["de"] + " / " + item["en"])
        print("Nächste Aktion / Next action: " + result["nextAction"]["de"] + " / " + result["nextAction"]["en"])
        print("Keine Startfreigabe. / No start authority granted.")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
