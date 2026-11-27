# AEPS-Receipt · RAW-01 nach .NET-11-Update / RAW-01 after .NET 11 update

**Ergebnis / Outcome** Keine neue AEPS-Evidence / No new AEPS evidence

**Publikationsstand / Publication state** `PendingPublication`

**Basis-HEAD / Base HEAD** `128a1f45a484939185bc37b3e9a4bb5073a0c265`

## Trigger und Bindung / Trigger and binding

- Review-ID `c062d94c-272b-4beb-ad67-4fe81279b73d`, Status `Ready`.
- [Aktiver RAW-01-Intake / Active RAW-01 intake](../../../requirements/intakes/active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md)
  mit Zielhash / with target hash `bff83798789bf565b4e0b679f467f6384dcf6820fda78fcaa4fff30d54a83820`.
- [Review-Ergebnis / Review result](../../../specs/intake-review-results/raw-01-reference-agentic-workspace-2026-11-27-dotnet11.json) mit normalisiertem
  SHA-256 / with normalised SHA-256 `2dfef8bc85113419421364910213becb54b5ae33e3db4d9d39cfdafed1c27780`.
- [Authoring Receipt](../../../specs/intake-authoring-receipts/RAW-01-Reference-Agentic-Workspace.json) und Einzelreview
  bestanden die Validatoren in Bash und PowerShell. Das vollständige
  [RAW-Gate](../../../scripts/validate-aoc-raw-review-gate.py) bestand für
  alle neun Intakes. / The authoring receipt and Single review passed the Bash
  and PowerShell validators. The full RAW gate passed for all nine intakes.

## Bewertung / Assessment

Die Änderung der Zielplattform ist AOC-spezifisch. Das erneute Binden von
Intake, Receipt, Manifest und Review bestätigt die bereits erfassten Regeln
`AEPS-FIND-AOC-011` und `AEPS-FIND-AOC-015`. Das abgelöste Einzelreview bleibt
historisch erhalten. Es gibt kein neues Muster und keinen neuen Kandidaten.
Die Prüfung liefert Text- und Bindungsnachweise für den Intake. Laufzeit-,
Plattform- und projektübergreifende Nachweise folgen aus eigenen Prüfungen.

The target change is specific to AOC. Rebinding the intake, receipt, manifest
and review confirms existing findings `AEPS-FIND-AOC-011` and
`AEPS-FIND-AOC-015`. The superseded review remains as historical evidence.
The review adds no new pattern or candidate. It verifies the intake text and
bindings. Runtime, platform and cross-project evidence require their own checks.
