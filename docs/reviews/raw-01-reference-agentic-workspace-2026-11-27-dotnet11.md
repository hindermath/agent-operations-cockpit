# RAW-01 · Einzelreview für .NET 11 / Single review for .NET 11

**Status** `Ready` · **Review-ID** `c062d94c-272b-4beb-ad67-4fe81279b73d` · **Datum / Date** 2026-11-27

## Ergebnis / Result

DE: Geprüft wurde ein Intake für IT-Auszubildende ab dem ersten Jahr und
erfahrene Fachkräfte. Die Prüfung hat keine offenen fachlichen Fragen,
Findings oder akzeptierten Risiken ergeben. Dieses Ergebnis löst
`5d84ad91-dd80-4c72-adc9-f54df5f089a7` für den aktiven Intake ausdrücklich ab.

EN: The review covered one intake for first-year IT apprentices and
experienced professionals. The review found no open domain questions,
findings or accepted risks. This result explicitly supersedes
`5d84ad91-dd80-4c72-adc9-f54df5f089a7` for the active intake.

## Fachliche Prüfung / Domain checks

| Prüffeld / Check | Ergebnis / Result |
|---|---|
| Ziel und Akzeptanz / Target and acceptance | `IAD101`, `AC-004`, Glossar und Receipt stimmen auf plattformneutrales `net11.0` und C# 15 überein. Domain und Core bleiben betriebssystemneutral. / The decision, acceptance criterion, glossary and receipt agree on platform-neutral `net11.0` and C# 15. Domain and core stay OS-independent. |
| Snapshot und Testvertrag / Snapshot and test contract | `IAD102`, `IAD103`, `AC-005` und `AC-006` wurden mit dem archivierten Intake verglichen. Kanonisches JSON, JSON Schema, xUnit.net v3, MTP v2 und stabile Pakete gelten weiter. / Comparison with the archived intake confirmed the canonical JSON, schema, test framework and stable package requirements. |
| Sicherheits- und Datenschutzgrenze / Security and privacy boundary | Lesender Zugriff endet an explizit freigegebenen Wurzeln. Fehlerausgaben bleiben datensparsam. Host und Sandbox bleiben über opake Kennungen unterscheidbar. / Read access ends at explicitly authorised roots. Errors minimise data. Opaque identifiers distinguish the host from a sandbox. |
| Lesbarkeit und Plattform / Readability and platform | Begriffe sind zweisprachig erklärt. Die Plattformsemantik für macOS, Linux und Windows, CEFR B2 und WCAG 2.2 AA bleiben Teil der Akzeptanz. / Terms are explained in both languages. Platform semantics on macOS, Linux and Windows, CEFR B2 and WCAG 2.2 AA remain part of acceptance. |
| Reihenfolge und Autorität / Order and authority | RAW-01 bleibt der einzige `Eligible`-Kandidat. Die Reihenfolge und Startgrenzen gelten weiter. / RAW-01 remains the sole `Eligible` candidate. The order and start boundaries still apply. |

## Gebundene Nachweise / Bound evidence

- [Aktiver Intake / Active intake](../../requirements/intakes/active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md)
- [Authoring Receipt](../../specs/intake-authoring-receipts/RAW-01-Reference-Agentic-Workspace.json)
- [Review-Anfrage / Review request](../../specs/intake-review-requests/raw-01-reference-agentic-workspace-2026-11-27-dotnet11.json)
- [Review-Ergebnis / Review result](../../specs/intake-review-results/raw-01-reference-agentic-workspace-2026-11-27-dotnet11.json)
- [Vorheriges Review / Prior review](../../specs/intake-review-results/raw-01-reference-agentic-workspace-2026-11-27-raw-series.json)
- Zielhash / Target hash `bff83798789bf565b4e0b679f467f6384dcf6820fda78fcaa4fff30d54a83820`

DE: Der nächste Schritt ist die vollständige lesende RAW-Gate-Prüfung vor
dem ausdrücklich beauftragten Specify. Die Abnahme von Build, Paketen und
Plattformverhalten folgt mit der späteren Implementierung.

EN: The next step is the full read-only RAW gate before the explicitly
requested Specify run. Build, package and platform acceptance follow during
later implementation.
