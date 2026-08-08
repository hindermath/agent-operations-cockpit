# Einzelreview RAW-05 – Execution Nodes / Single Review RAW-05 – Execution Nodes

## Identität und Ergebnis / Identity and outcome

- Review-ID: `e81d7013-defc-4649-9f08-ff839f48301b`
- Modus / Mode: `Single`
- Policy: `aoc-bilingual-requirements`
- Ergebnis / Outcome: `Ready`
- Review-Zeitpunkt / Review time: `2026-08-06T19:55:25Z`
- Repository-HEAD: `a3629bd20c3596579dfa7f333e6cc8e24ca5963a`
- Ziel / Target:
  `requirements/intakes/active/Lastenheft_RAW-05-Execution-Nodes.md`
- Normalisierter SHA-256 / Normalised SHA-256:
  `69eb3cc6c4aa43c3472f2c7f976d19de935ee28562b4eb4cb15a1bc205248659`
- Git-Blob: `N/A` – das autorisierte Update ist noch nicht committet. / *The
  authorised update is not committed yet.*
- Request:
  `specs/intake-review-requests/raw-05-execution-nodes-2026-08-06-r2.json`
- Request-SHA-256:
  `bed9fb9cd5f74bc8c55caa1993609289bbab90f7a01febd732201a989efb281b`
- Ziele / Targets: `1`; Worker: `0`
- Critical: `0`; High: `0`; Medium: `0`; Low: `0`
- Akzeptierte Risiken / Accepted risks: `0`
- Offene Fragen / Open questions: `0`
- Supersediertes Einzelreview / Superseded Single review:
  `specs/intake-review-results/raw-05-execution-nodes-2026-08-06.json`

Das vollständige Re-Review bewertet ausschließlich das erneuerte RAW-05 und
seine gebundene Requirements-Evidence. Es erweitert weder Scope noch Serie und
startet keine Folgephase. / *This complete re-review assesses only the renewed
RAW-05 intake and its bound requirements evidence. It expands neither scope nor
the Series and starts no downstream phase.*

## Ergebnis / Outcome

RAW-05 ist `Ready`. Der Execution-Node-Vertrag ist transportneutral und auf
lokale read-only Adapter für Host, WSL, Container und ABS-DD begrenzt. Remote
Nodes bleiben deaktiviert. Die konkrete spätere Remote-Transportwahl bleibt
bei RAW-06 `IAD604`; RAW-05 nimmt sie nicht vorweg. / *RAW-05 is Ready. The
Execution Node contract is transport neutral and bounded to local read-only
adapters for host, WSL, container, and ABS-DD. Remote nodes remain disabled.
The later concrete remote-transport choice remains with RAW-06 IAD604 and is
not pre-empted by RAW-05.*

Mehrquellen-Attestation ergibt ausschließlich `Verified`, `Limited`,
`Untrusted` oder `Unknown`. Fehlende und widersprüchliche Evidence bleibt
fail-closed. Versionierte Profile definieren positive Probe-Timeouts und `T`;
Freshness folgt RAW-03 mit `0,5T / T / 2T`. Recovery ist ausschließlich ein
neuer read-only Probe ohne Mount-, Prozess-, Credential-, Netzwerk-, Checkout-
oder Remote-Write-Side-Effects. / *Multi-source attestation yields only
Verified, Limited, Untrusted, or Unknown. Missing and contradictory evidence
fails closed. Versioned profiles define positive probe timeouts and T;
freshness follows RAW-03 at 0.5T/T/2T. Recovery is only a new read-only probe
without mount, process, credential, network, checkout, or remote-write side
effects.*

`IAD501`, `IAD502` und `IAD503` beantworten `IRQ501` bis `IRQ503`.
`IAD502` und `IAD503` supersedieren `DEC-T06`; `IAD501` begrenzt den lokalen
RAW-05-Vertrag und lässt `IAD604` bei RAW-06 offen. Target, Authoring Receipt
und maschinenlesbarer Vertrag enthalten keine offene RAW-05-Frage. / *IAD501,
IAD502, and IAD503 answer IRQ501 through IRQ503. IAD502 and IAD503 supersede
DEC-T06; IAD501 bounds the local RAW-05 contract and leaves IAD604 open with
RAW-06. Target, Authoring Receipt, and machine-readable contract contain no
open RAW-05 question.*

## Auflösung der früheren Findings / Resolution of prior findings

| Finding | Ergebnis / Result | Nachweis / Evidence |
|---|---|---|
| IR501 | Erledigt / Resolved | IAD501–IAD503, Target, Execution-Node-Vertrag und erneuertes Receipt stimmen überein; null offene Fragen. / Decisions, target, contract, and receipt agree with zero open questions. |
| IR502 | Erledigt / Resolved | Versionierter Node Descriptor und Authority Contract, drei Validatoroberflächen, Positiv-/Negativ-Fixtures, Befehle, Sollausgaben, Exitcodes und Plattformmatrix sind gebunden. / Versioned contract, validators, fixtures, commands, expected outputs, exit codes, and platform matrix are bound. |
| IR503 | Erledigt / Resolved | Normative Abschnitte sind DE-first/EN-second; zentrale Begriffe, Lifecycle, Decision-Zustand, nächste Aktion und Authority-Trennung sind lokal erklärt. / Normative sections are bilingual; terminology, lifecycle, decisions, next action, and authority separation are explicit. |
| IR504 | Erledigt / Resolved | Security, Privacy, Public Content, WCAG 2.2 AA, macOS/Linux/Windows, WSL/Container/ABS-DD und Supply Chain besitzen messbare Grenzen und Re-Evaluation-Trigger. / Cross-cutting concerns have measurable boundaries and reassessment triggers. |
| IR505 | Erledigt / Resolved | Node Descriptor, Capability/Mount/Attestation und Health/Freshness benennen Producer, Consumer, Version, Authority, Failure Behavior sowie bindende oder bevorzugte Serienrelation. / Typed handoffs bind producer, consumer, version, authority, failure behaviour, and Series relation. |
| IR506 | Erledigt / Resolved | Prompts und Receipt erklären fail-closed, dass Eligibility, Ready und historische Delivery-Daten keine aktuelle Start-, Implementierungs-, Remote-, Merge-, Bypass- oder Provider-Autorität erteilen. / Prompts and receipt fail closed on current authority. |

## Vollständige Review-Coverage / Complete review coverage

| Prüffeld / Review area | Status | Begründung / Rationale |
|---|---|---|
| Identität, Zielgruppe, Zweck, Scope und Non-Goals / Identity, audience, purpose, scope, and non-goals | Pass | Node Evidence ist klar von Working-Copy-Ownership, CLI, Commands, Remote Transport und Produktimplementierung getrennt. / Node evidence is separated from working-copy ownership, CLI, commands, remote transport, and product implementation. |
| Vorwissen, Sprache und Begriffe / Prior knowledge, language, and terminology | Pass | DE-first/EN-second, CEFR B2 und Erstgebrauchserklärungen sind vollständig. / German-first/English-second, CEFR B2, and first-use explanations are complete. |
| Status, Abhängigkeiten, Decisions und nächste Aktion / State, dependencies, decisions, and next action | Pass | RAW-05 allein Eligible, RAW-02 nur bevorzugt, IAD501–IAD503 bestätigt, DEC-T06 supersediert und Re-Review als einzige nächste Aktion beschrieben. / Lifecycle, dependency, decision state, and review-only next action are explicit. |
| Atomare und prüfbare Anforderungen / Atomic and testable requirements | Pass | Identität, Endpoint, Attestation, Mount, Profile, Freshness, State, Health, Recovery und Ausfallcodes sind deterministisch. / Identity, endpoint, attestation, mounts, profiles, freshness, state, health, recovery, and failure codes are deterministic. |
| Messbare Akzeptanz und Evidence / Measurable acceptance and evidence | Pass | Acht Kriterien binden Vertrag, fünf Fixtures, stabile EN-Codes, Plattformmatrix und beide Shell-Oberflächen. / Eight criteria bind the contract, five fixtures, stable EN codes, platform matrix, and both shell surfaces. |
| Handoffs, Risiken und Authority / Handoffs, risks, and authority | Pass | Drei typisierte Handoffs, Revisionstrigger und Delivery-Grenzen sind vollständig und fail-closed. / Three typed handoffs, revision triggers, and delivery boundaries are complete and fail closed. |
| Security, Privacy, A11Y, Plattform und Supply Chain / Cross-cutting applicability | Pass | Anwendbarkeit, Datenminimierung, öffentliche Evidence, Plattformparität und Re-Evaluation sind prüfbar. / Applicability, data minimisation, public evidence, platform parity, and reassessment are testable. |
| Prompt-Ausrichtung / Prompt alignment | Pass | Kopierbare Prompts überschreiten keine aktuelle Authority; gespeichertes MergeAndSync bleibt historische Obergrenze. / Copy-ready prompts do not exceed current authority; stored MergeAndSync remains historical only. |
| Secrets, Personendaten, Encoding und Whitespace / Secrets, personal data, encoding, and whitespace | Pass | Logische Referenzen statt persönlicher Pfade sind normativ; JSON, strict UTF-8 und `git diff --check` bestehen. / Logical references replace personal paths; JSON, strict UTF-8, and diff checks pass. |

## Validation Evidence / Validation evidence

- Authoring Receipt: Bash und PowerShell `PASS`, Status `ReadyForReview`, `13`
  gebundene Quellen. / *Both authoring validators pass with 13 bound sources.*
- Series Manifest und Receipt: Bash und PowerShell `PASS`, `14` Ziele, `1`
  Root und `14` Abhängigkeiten. / *Both Series validators pass.*
- RAW-05-Fixtures: Host, WSL, Container, ABS-DD und deaktivierter Remote Node;
  macOS, Linux und Windows; `0,5T`, `T`, `2T`, Expired, Timeout, fehlender Node,
  verweigerter Zugriff und Mount-Drift bestehen auf Bash und PowerShell. /
  *Positive node, platform, freshness, failure, and drift cases pass through
  Bash and PowerShell.*
- Vier negative Fixtures werden erwartungsgemäß mit `EN007`, `EN008`, `EN009`
  und `EN010` abgelehnt. Beide Oberflächen liefern Exitcode `0` für die
  erwartete Negativ-Evidence. / *All four expected rejection cases pass with
  stable codes and exit code 0 on both surfaces.*
- JSON-Syntax, Python- und Bash-Syntax, PowerShell-Parser,
  PSScriptAnalyzer `1.25.0`, Archividentität und `git diff --check` bestehen. /
  *JSON, syntax, PowerShell analysis, archive identity, and whitespace checks
  pass.*

## Serien- und Authority-Auswirkung / Series and authority impact

Das Review ändert den Series-Lifecycle nicht. RAW-05 bleibt der einzige
deklarierte `Eligible`-Kandidat und auf read-only Research begrenzt. `Ready`
bestätigt nur die Qualität des exakt hashgebundenen Lastenhefts; es setzt
RAW-05 nicht auf `Completed` und erteilt keine Start-, Specify-,
Implementierungs-, Remote-, Merge-, Bypass-, Provider-, Preset- oder Level-0-
Autorität. / *The review does not change Series lifecycle. RAW-05 remains the
sole declared Eligible candidate and is limited to read-only research. Ready
confirms only the quality of the exact hash-bound intake and grants no
downstream authority.*

Die AOC-weite Review-Sperre bleibt geschlossen, weil RAW-06 bis RAW-09 noch
keine vollständige aktuelle Ready-Coverage besitzen. `IAD604` bleibt eine
offene RAW-06-Entscheidung und ist kein offener RAW-05-Rest. / *The AOC-wide
review gate remains closed because RAW-06 through RAW-09 do not yet have full
current Ready coverage. IAD604 remains an open RAW-06 decision and is not an
open RAW-05 remainder.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle ist das ausdrücklich autorisierte
vollständige RAW-05-Re-Review; Owner ist `RAW-05 intake review`. Neu sind der
Re-Review-Request, das maschinenlesbare Ergebnis und dieser Bericht. Evidence
sind die gebundenen Target-/Request-Hashes und die oben aufgeführten
Validierungen. / *Decision: UpdateRequired. The authorised full RAW-05
re-review is the source and RAW-05 intake review is the owner. The new request,
machine-readable result, and this report are backed by the bound hashes and
listed validation evidence.*

## Exakte nächste Aktion / Exact next action

Der nächste sichere Spec-Kit-Befehl ist read-only: / *The next safe Spec Kit
command is read-only:*

```text
$speckit-intake-series-status specs/intake-series/aoc-phase-2/manifest.json
```

Er validiert den neuen Ready-Nachweis im Serienkontext und startet keine
Folgeaktion. / *It validates the new Ready evidence in Series context and
starts no downstream action.*
