# Einzelreview RAW-07 – Hardware Capability Layer / Single Review RAW-07 – Hardware Capability Layer

## Identität und Ergebnis / Identity and outcome

- Review-ID: `b4e3bed0-6002-4110-b378-01de9f3d040e`
- Modus / Mode: `Single`
- Policy: `aoc-bilingual-requirements`
- Ergebnis / Outcome: `Ready`
- Review-Zeitpunkt / Review time: `2026-08-07T20:43:31Z`
- Repository-HEAD: `a3629bd20c3596579dfa7f333e6cc8e24ca5963a`
- Ziel / Target:
  `requirements/intakes/active/Lastenheft_RAW-07-Hardware-Capability-Layer.md`
- Normalisierter SHA-256 / Normalised SHA-256:
  `319a704fcb875f3996ce5aba182c0878718a21d011b38c5af09e81998ca6a7ed`
- Git-Blob: `N/A` – das autorisierte Update ist noch nicht committet. / *The
  authorised update is not committed yet.*
- Request:
  `specs/intake-review-requests/raw-07-hardware-capability-layer-2026-08-07.json`
- Request-SHA-256:
  `2c93d886c7bd49d4b3fade6126e8a5f78fb15d7f8875ada6b8cbfb3b9e575a40`
- Ziele / Targets: `1`; Worker: `0`
- Critical: `0`; High: `0`; Medium: `0`; Low: `0`
- Akzeptierte Risiken / Accepted risks: `0`
- Offene Fragen / Open questions: `0`
- Supersediertes Einzelreview / Superseded Single review: `N/A`

Das vollständige Single Review bewertet ausschließlich das erneuerte RAW-07
und seine offline prüfbare Requirements-Evidence. Es führt kein Hardware-I/O
aus, erweitert weder Scope noch Serie und startet keine Folgephase. / *This
complete Single review assesses only the renewed RAW-07 intake and its offline
requirements evidence. It performs no hardware I/O, expands neither scope nor
the Series, and starts no downstream phase.*

## Ergebnis / Outcome

RAW-07 ist `Ready`. `IAD701` bis `IAD704` sind im Lastenheft, Decision
Register, maschinenlesbaren Hardware Capability Contract und Authoring Receipt
konsistent als beantwortet gebunden. / *RAW-07 is Ready. IAD701 through IAD704
are consistently bound as answered in the intake, Decision Register,
machine-readable contract, and Authoring Receipt.*

Die MIDI-Grenze verlangt eine plattformübergreifende Bibliothek hinter einem
dünnen herstellerneutralen Adapter. Raw MIDI bleibt aus dem Domain Contract.
Die offizielle Elgato-SDK-Bridge bleibt isoliert; TypeScript ist nur bei
SDK-Zwang zulässig und nur normalisierte Capability Events verlassen die
Bridge. / *The MIDI boundary requires a cross-platform library behind a thin,
vendor-neutral adapter. Raw MIDI stays outside the domain contract. The
official Elgato SDK bridge remains isolated; TypeScript is allowed only when
required and only normalised capability events leave the bridge.*

Die erste Referenzwelle enthält genau ein MIDI-Gerät und ein Stream Deck;
Xbox bleibt separater späterer Kandidat. Vor jedem Feldtest sind versioniertes
Lab-Inventar, gerätespezifische Risiko-/Safety-Prüfung, verifizierter Kill
Switch, beaufsichtigter Testplan und dokumentierte Freigabe erforderlich.
Diese Requirements-Evidence erteilt keine Hardware-I/O- oder Produktcommand-
Authority. / *The first reference wave contains one MIDI device and one Stream
Deck; Xbox remains separate. Every field test requires the complete lab and
safety gate. This requirements evidence grants no hardware-I/O or
product-command authority.*

## Auflösung des früheren Serien-Findings / Resolution of the earlier Series finding

| Finding | Ergebnis / Result | Nachweis / Evidence |
|---|---|---|
| `IR003` aus dem Phase-2-Serienreview | Erledigt für RAW-07 / Resolved for RAW-07 | IAD701–IAD704, Target, Decision Register, Vertrag und Receipt stimmen überein; null offene Fragen. / Decisions, target, register, contract, and receipt agree with zero open questions. |

Das historische Series Review wird durch dieses Single Review nicht
überschrieben. Seine damalige Negativ-Evidence bleibt unverändert; wegen des
neuen RAW-07- und Manifest-Hashes ist es nicht aktuell und benötigt bei einem
später autorisierten Serienreview eine neue Bewertung. / *This Single review
does not overwrite the historic Series review. Its negative evidence remains
immutable; the new RAW-07 and manifest hashes make it non-current until a
separately authorised Series review reassesses it.*

## Vollständige Review-Coverage / Complete review coverage

| Prüffeld / Review area | Status | Begründung / Rationale |
|---|---|---|
| Identität, Zielgruppe, Zweck, Scope und Non-Goals / Identity, audience, purpose, scope, and non-goals | Pass | Capability-, Adapter-, Referenzwellen- und Lab-Vertrag sind von tatsächlichem I/O, UI, State, Commands, Implementierung, Presets und Level 0 getrennt. / Contracts are separated from excluded work. |
| Vorwissen, Sprache und Begriffe / Prior knowledge, language, and terminology | Pass | DE-first/EN-second, CEFR B2 und Erklärungen für Capability, Thin Adapter, Raw MIDI, SDK Bridge, Reference Wave, Lab Approval, Kill Switch und Authority sind vorhanden. / Language and terminology are complete. |
| Status, Abhängigkeiten, Decisions und nächste Aktion / State, dependencies, decisions, and next action | Pass | RAW-04 ist Completed, RAW-07 bleibt Blocked, IAD701–IAD704 sind beantwortet und nur das Review ist als aktuelle Folgeaktion autorisiert. / Lifecycle, dependency, decisions, and authority are explicit. |
| Atomare und prüfbare Anforderungen / Atomic and testable requirements | Pass | Capability Model, Adapterzustände, Profile, MIDI-/Elgato-Grenze, Gerätemenge, Lab Gate, Fehler und Authority sind deterministisch. / Requirements are deterministic and testable. |
| Messbare Akzeptanz und Evidence / Measurable acceptance and evidence | Pass | Acht Kriterien binden Vertrag, sechs Fixtures, stabile `HWC`-Codes, Sollausgaben, Exitcode und beide Shell-Oberflächen. / Eight criteria bind the contract, six fixtures, stable codes, expected output, exit code, and both shell surfaces. |
| Handoffs, Risiken und Authority / Handoffs, risks, and authority | Pass | Zwei typisierte Handoffs, Re-Evaluation-Trigger und fail-closed Hardware-/Delivery-Grenzen sind vollständig. / Handoffs, reassessment triggers, and authority boundaries are complete. |
| Security, Privacy, A11Y, Plattform und Supply Chain / Cross-cutting applicability | Pass | Safety Gate, Protokollgrenze, Seriennummernminimierung, Textalternativen, macOS/Linux/Windows-Parität und spätere Dependency-Evidence sind prüfbar. / Cross-cutting concerns have testable boundaries. |
| Prompt-Ausrichtung / Prompt alignment | Pass | Kopierbare Prompts erteilen keine aktuelle Start-, Hardware-I/O-, Device-, SDK-, Remote-, Specify-, Implementierungs-, Merge-, Bypass-, Provider-, Preset- oder Level-0-Autorität. / Copy-ready prompts grant no current downstream authority. |
| Secrets, Personendaten, Encoding und Whitespace / Secrets, personal data, encoding, and whitespace | Pass | Seriennummern und private Pfade sind ausgeschlossen; UTF-8, JSON und `git diff --check` bestehen. / Personal data, UTF-8, JSON, and whitespace boundaries pass. |

## Validation Evidence / Validation evidence

- Authoring Receipt: Bash und PowerShell `PASS`, Status `ReadyForReview`, `16`
  gebundene Quellen. / *Both authoring validators pass with 16 bound sources.*
- Single Review: Bash und PowerShell `PASS`, Status `Ready`, ein aktuelles
  Ziel. / *Both review validators pass with one current target.*
- Series Manifest und Receipt: Bash und PowerShell `PASS`, `14` Ziele, `1`
  Root und `14` Abhängigkeiten. / *Both Series validators pass.*
- Die Schema-2.0-Requirements-Governance löst Rollen und Pfade korrekt auf,
  meldet aber weiterhin den bereits bestehenden globalen Serienblocker
  `RIG017`: null statt genau eines `Eligible`-Ziels. Das ist keine RAW-07-
  Qualitätsfreigabe und wird durch dieses Single Review nicht repariert. /
  *Schema 2.0 resolves roles and paths but retains the existing global Series
  blocker RIG017: zero rather than exactly one Eligible target. This Single
  review does not repair or bypass it.*
- RAW-07-Fixtures: eine positive Zwei-Geräteklassen-Evidence sowie fünf
  erwartete Ablehnungen für Raw-Protokollleakage, Domain Command,
  nicht freigegebenes Gerät, fehlendes Lab Gate und fehlenden Kill Switch
  bestehen auf Bash und PowerShell mit identischen Codes und Exitcode `0`. /
  *The positive fixture and five expected rejection fixtures pass identically
  on both surfaces.*
- JSON-, Python-, Bash- und PowerShell-Syntax sowie PSScriptAnalyzer bestehen;
  die archivierten Vorgängerhashes sind unverändert gebunden. / *Syntax,
  PowerShell analysis, and archived predecessor hashes pass.*
- Der begrenzte Secret-/Personendaten-Musterscan und `git diff --check` melden
  keinen Treffer. / *The bounded sensitive-data and whitespace checks report
  no finding.*

## Serien- und Authority-Auswirkung / Series and authority impact

Das Review ändert den Series-Lifecycle nicht. RAW-07 bleibt `Blocked`; es gibt
weiterhin keinen `Eligible`-Kandidaten. `Ready` bestätigt nur die Qualität des
exakt hashgebundenen Lastenhefts und erteilt keine Start-, Hardware-I/O-,
Device-, SDK-, Produkt-, Remote-, Specify-, Implementierungs-, Merge-, Bypass-,
Provider-, Preset-, GitHub- oder Level-0-Autorität. / *The review does not
change Series lifecycle. RAW-07 remains Blocked and no target is Eligible.
Ready confirms only the quality of the exact hash-bound intake and grants no
downstream authority.*

Die AOC-weite Review-Sperre bleibt geschlossen: Zwölf der vierzehn aktiven
Lastenhefte besitzen nun aktuelle formal validierte Ready-Evidence; RAW-08 und
RAW-09 fehlen noch. / *The AOC-wide review gate remains closed: twelve of
fourteen active intakes now have current, formally validated Ready evidence;
RAW-08 and RAW-09 remain outstanding.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle ist das ausdrücklich autorisierte
vollständige RAW-07-Single-Review; Owner ist `RAW-07 intake review`. Neu sind
Review-Request, maschinenlesbares Ergebnis und dieser Bericht. Evidence sind
die gebundenen Target-/Request-Hashes und die aufgeführten Offline-
Validierungen. / *Decision: UpdateRequired. The authorised full RAW-07 Single
review is the source and RAW-07 intake review is the owner. The request,
machine-readable result, and this report are backed by the listed offline
validation.*

## Exakte nächste Aktion / Exact next action

Der nächste sichere Spec-Kit-Befehl ist read-only: / *The next safe Spec Kit
command is read-only:*

```text
$speckit-intake-series-status specs/intake-series/aoc-phase-2/manifest.json
```

Er validiert den neuen Ready-Nachweis im Serienkontext und startet keine
Folgeaktion. / *It validates the new Ready evidence in Series context and
starts no downstream action.*
