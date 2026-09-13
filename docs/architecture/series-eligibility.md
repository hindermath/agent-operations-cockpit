# Architektur der Eignungsprüfung / Eligibility Architecture

## Kontext und Prüfstand / Context and review baseline

`manual:architecture`, T033, 2026-09-13; Reviewer: Codex, lokale Implementierungsreview-Rolle; Owner: AOC Repository Owner. [Plan](../../specs/004-series-eligibility/plan.md), [Schnittstelle](../../specs/004-series-eligibility/contracts/series-eligibility-interface.md) und [Quality-Quellbindung](../../specs/004-series-eligibility/phase-results/quality-validation.json) bestimmen den geprüften Stand. Architektur/iSAQB sind `Applicable`; die lokale Implementierung des akzeptierten Designs ist `Fulfilled`. Native Abnahme bleibt offen. / *Local implementation review against accepted design and bound source bytes; native acceptance remains open.*

Das System beantwortet eine lokale Frage: Welche Eignung oder Kandidaten sind durch vorhandene Daten belegbar? Lernende und Maintainer liefern Repository und Fixture oder Series-Manifest. Die Ausgabe ist Klartext oder JSON. Kein Produktdienst, keine Datenbank, keine Cloud und kein Workerstart entstehen. / *Users supply a repository and either an assessment fixture or series manifest. The local checker returns text or JSON, with no service, database, cloud or worker execution.*

## Datenfluss und Vertrauensgrenzen / Data flow and trust boundaries

1. Bash beziehungsweise PowerShell prüft die Aufruffläche und übergibt Argumente als einzelne Werte an die feste lokale Python-Runtime. Hilfetext und Dot-Sourcing starten keine Abfrage. / *Adapters delegate explicit arguments to local Python; help and dot-sourcing do not query.*
2. `ReadBoundary`/`GuardedPath` prüfen relative Datenpfade, reguläre Dateien und Containment. JSON wird mit Duplicate-Key- und Typprüfung gelesen. Eingabedaten sind keine ausführbaren Anweisungen. / *Guarded paths and strict JSON separate untrusted data from trusted code.*
3. Fixture: neun Kriterien/sechs Modi prüfen, `meets_parallel_eligibility` wiederverwenden, erst Ergebnis berechnen, dann `expectedOutcome` vergleichen. Series: isolierte Instanz der vorhandenen Engine; guarded `normalized_bytes`/JSON-Reader; bestehende Hash-, Graph-, Root- und Lifecycle-Regeln. / *Reuse existing assessment and graph logic after validation; expected outcome is an assertion, not classification input.*
4. Projektion ordnet Kandidaten/Blocker nach Manifest und Gründe nach Kriterien. Lifecycle, Review, Eligibility, Präferenz, Delivery, Herkunft und aktuelle Authority bleiben eigene Felder. Ergebnis geht nur an stdout; sichere Diagnose und eine DE/EN-Aktion bilden die letzte Grenze. / *Stable projection preserves separate axes and emits only a safe result and one bilingual action.*

Defense in Depth bedeutet mehrere voneinander verschiedene Schutzschritte: Pfad-/Typgrenze, fachliche Hash-/Graphprüfung und eingeschränkte Ausgabe. Ein gültiger Pfad ersetzt keinen gültigen Hash; `Eligible` ersetzt keine Startfreigabe. [Security](../security/series-eligibility.md) dokumentiert STRIDE/CIA und Restgrenzen. / *Defense in depth combines boundary validation, semantic validation and safe output. A valid path is not a valid hash; eligibility is not start authority.*

## Qualitätsszenarien / Quality scenarios

| Ziel / Goal | Tatsächlicher Nachweis / Actual evidence | Disposition |
|---|---|---|
| SC-001: drei Originalfixtures / three original fixtures | [US1](../../specs/004-series-eligibility/phase-results/us1-tests.json), aktuelle US3 `final-all-bash`/`final-all-pwsh`: ein Eligible, zwei Blocked; neun Kriterien. / One eligible, two blocked. | Lokal erfüllt / Locally fulfilled |
| SC-002: strukturelle Fehler / structural failures | [US2](../../specs/004-series-eligibility/phase-results/us2-tests.json), aktuelle [US3](../../specs/004-series-eligibility/phase-results/us3-tests.json): ISG004/007/008/009, fehlende Authority/Kriterien. / Named negative cases. | Lokal erfüllt / Locally fulfilled |
| SC-003: deterministisch und lesend / deterministic and read-only | US3 `final-status-*`, Seeds 1/7/42, mehrere Vorgänger, Dateisnapshots und Core-Audit. / Seeds, predecessor order and no-write/process proofs. | Lokal erfüllt / Locally fulfilled |
| SC-004: native Plattformparität / native parity | [Plattformreview](../../specs/004-series-eligibility/checklists/cross-platform.md); lokales macOS beweist keine drei Providerplattformen. / Local macOS is not all provider platforms. | Applicable / Partly Fulfilled; T048 offen / open |
| SC-005: Bedeutung/Sprache/Autorität / meaning, language, authority | [A11Y-Review](../accessibility/series-eligibility.md), [Manpage](../man/validate-series-eligibility.1), Quickstart und Agentenreview. / Semantic and rendered review. | Lokaler Review abgeschlossen; AT-Grenzen sichtbar / Local review complete; AT limits explicit |

## Entscheidungen, Risiken und Schuld / Decisions, risks and debt

Die akzeptierte additive Adaptergrenze bleibt unverändert; keine kopierte Graphengine und kein neues Framework. Die isolierte Modulinstanz ändert nur Reader-Bindungen im Speicher. Das installierte Modul auf Platte bleibt bytegleich. / *The accepted additive boundary remains; no copied graph engine or new framework. Reader bindings change only within an isolated in-memory module instance; installed code remains unchanged.*

Gemeinsame Writes und offene gemeinsame Entscheidungen blockieren `parallel-autonomous`; Serialisierung ist eine Empfehlung und keine Erlaubnis, fremde Prozesse zu stoppen oder Teilmerges auszuführen. Die aktuelle Series-Lifecycle-Angabe `Completed` ist deklarierte Datenherkunft, kein Beweis des Abschlusses dieses autonomen Laufs. / *Shared writes/decisions block parallel eligibility. Serial advice grants no cancellation or partial-merge rights. A declared Completed series lifecycle does not prove this autonomous run completed.*

| Risiko / Risk | Behandlung, Owner und Follow-up / Treatment, owner and follow-up |
|---|---|
| Engine-Reader-API ändert sich / Reader API drift | Feste schmale GuardedPath-Fläche; Owner prüft Adapter/Transitivtests bei Preset-Änderung. / Reassess adapter on preset changes. |
| Konkurrierende Elternpfadänderung oder sehr große JSON-Datei / Concurrent parents or huge JSON | Kontrollierter lokaler Arbeitsbaum bleibt Voraussetzung; Owner bewertet Härtung vor Dienst-/Fremddatenscope. Kein uneingeschränkter Sandboxanspruch. / Controlled local worktree; no unrestricted sandbox claim. |
| Native Semantik unbewiesen / Native behavior unproven | T048 muss echte sechs Shell-/OS-Kombinationen liefern; Risiko bleibt bis dahin offen. / Actual six native combinations required. |
| Review-/Deliverywerte werden überinterpretiert / Projection overinterpreted | `NotAssessed`, `NotGrantedByQuery` und historische Herkunft sichtbar halten; Owner prüft bei UX-/Authorityänderung. / Preserve explicit unknown and authority fields. |

ADR/S-ADR: `N/A / Not Assessed`, keine neue materielle Entscheidung seit dem akzeptierten Plan. BSI C3A/C5: `N/A / Not Assessed`, keine Cloudauswahl, Providerbindung oder Shared-Responsibility-Änderung. Neue Produktbausteine, Deployment, Hardware und externe Services: `N/A / Not Assessed`, unverändert. Neue technische Schuld: keine neue Designabweichung; die oben genannten Prüf- und Betriebsgrenzen bleiben sichtbar. Owner jeweils AOC Repository Owner, Reviewer wie oben, Follow-up bei neuer Entscheidung, Trust Boundary, Dependency, Produkt- oder Cloudgrenze. / *No new material decision requires an ADR or security ADR. No cloud/provider change requires C3A/C5 evidence. Product/deployment/hardware/services are unchanged. No new design deviation is introduced; listed operational and proof limits remain explicit. Reassess on the named changes.*

Nächste sichere Aktion: Die noch offene native Abnahme am später autorisierten Lieferstand prüfen. / *Next safe action: assess missing native evidence at the later authorized delivery head.*
