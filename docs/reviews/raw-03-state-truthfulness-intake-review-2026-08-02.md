# Einzelreview RAW-03 – Zustandswahrheit / Single Review RAW-03 – State Truthfulness

## Identität und Ergebnis / Identity and outcome

- Review-ID: `1159da03-43fd-41ae-9876-f3df2633af12`
- Modus / Mode: `Single`
- Policy: `aoc-bilingual-requirements`
- Ergebnis / Outcome: `NeedsClarification`
- Review-Zeitpunkt / Review time: `2026-08-02T13:17:50Z`
- Repository-HEAD: `60706c5dc6d96996fd7b4b4780c0b736a643dbb0`
- Ziel / Target:
  `requirements/intakes/active/Lastenheft_RAW-03-State-Truthfulness.md`
- Normalisierter SHA-256 / Normalised SHA-256:
  `6886c5cc5243f033620e82895c601d78d4309108c8f364b81900598a2f563eae`
- Git-Blob: `6eb50189630abf62a5550b088e6acaac45f2008a`
- Request:
  `specs/intake-review-requests/raw-03-state-truthfulness-2026-08-02.json`
- Request-SHA-256:
  `fc0e3b840343891dd9d52245f1209a9c5bc7c68528c586a5442982f715714d96`
- Ziele / Targets: `1`; Worker: `0`
- Critical: `0`; High: `6`; Medium: `0`; Low: `0`
- Akzeptierte Risiken / Accepted risks: `0`
- Offene Fragen / Open questions: `3`
- Supersediertes Einzelreview / Superseded Single review: keines / *none*

Dieses unabhängige Einzelreview prüft das unveränderte RAW-03. Es erweitert
den Scope nicht auf die Serie und startet weder Klärung, Reparatur, Specify,
Implementierung, autonomen Lauf, Remote Write, Merge noch Bypass. / *This
independent Single review assesses unchanged RAW-03. It does not broaden scope
to the Series or start clarification, repair, Specify, implementation,
autonomous execution, remote writes, merge, or bypass.*

## Ergebnis / Outcome

RAW-03 besitzt einen klaren fachlichen Zweck: Eine gemeinsame,
nachvollziehbare Zustandswahrheit soll Wert oder Abwesenheit, Quelle,
Zeitbezug, Freshness, Authority und Reason Code über Text, JSON und spätere
Oberflächen hinweg erhalten. RAW-01 ist abgeschlossen, RAW-03 ist der einzige
deklarierte `Eligible`-Kandidat, und Authoring Receipt sowie Serienbindung
bestehen beide Validatoroberflächen. / *RAW-03 has a clear domain purpose: a
shared, traceable state truth should preserve value or absence, source, time,
freshness, authority, and reason code across text, JSON, and later surfaces.
RAW-01 is completed, RAW-03 is the sole declared Eligible candidate, and its
Authoring Receipt and Series binding pass both validator surfaces.*

`Ready` ist dennoch nicht zulässig. Die drei materiellen Fragen aus `DEC-T03`
sind offen, während das Receipt fälschlich keine offenen Entscheidungen oder
Fragen ausweist. Fünf weitere High Findings betreffen Handoff, Sprache,
reproduzierbare Evidence, Querschnittsanwendbarkeit und Delivery Authority.
Da zuerst menschliche Fachentscheidungen erforderlich sind, lautet das
Gesamtergebnis `NeedsClarification`. / *Ready is not allowed. Three material
DEC-T03 questions remain open while the Receipt incorrectly records no open
decisions or questions. Five additional High findings cover handoff,
language, reproducible evidence, cross-cutting applicability, and delivery
authority. Human domain decisions are required first, so the overall outcome
is NeedsClarification.*

## Findings / Findings

| ID | Severity | Kategorie / Category | Disposition | Nachweis / Evidence |
|---|---|---|---|---|
| IR301 | High | Offene Entscheidung und Provenienz / Open decision and provenance | NeedsClarification | RAW-03 und die Baselines führen `DEC-T03` als offen und State-blockierend; das Receipt enthält gleichzeitig `decisions=[]`, `openDecisionIds=[]` und `questionCount=0`. / RAW-03 and its baselines declare DEC-T03 open and State-blocking, while the Receipt records no decisions or questions. |
| IR302 | High | Abhängigkeit und Handoff / Dependency and handoff | NeedsRemediation | `Node Evidence` wird als Input genannt, besitzt aber im kanonischen Portfoliovertrag und aktuellen DAG keinen bindenden Producer-Handoff zu RAW-03. RAW-05 folgt später und bleibt research-only. / Node Evidence has no binding producer handoff to RAW-03 in the canonical contract or DAG. |
| IR303 | High | Sprache und Terminologie / Language and terminology | NeedsRemediation | Normative Abschnitte sind nicht vollständig DE/EN gepaart; zentrale State-, Evidence-, Lifecycle- und Spec-Kit-Begriffe bleiben für die erklärte Zielgruppe ohne Erstgebrauchserklärung. Aktueller Status, Vorgänger, Decision-ID, nächste Aktion und Nicht-Autorität fehlen als geordneter Text. / Language parity, first-use terminology, and text-first state are incomplete. |
| IR304 | High | Anforderungen und Evidence / Requirements and evidence | NeedsRemediation | Versionierter Envelope, Statusableitung, Reason-Code-Katalog, Traceability sowie benannte Fixtures, Validatoren, Sollausgaben und Exitcodes fehlen. AC-001 ist ohne definierte Reason Codes nicht auswertbar. / The versioned envelope, state derivation, reason-code catalogue, traceability, and reproducible fixture evidence are missing. |
| IR305 | High | Querschnittsanwendbarkeit / Cross-cutting applicability | NeedsRemediation | Security, Privacy, Datenminimierung, Secret-sichere Details, WCAG 2.2 AA, macOS/Linux/Windows-Parität und Supply Chain sind nicht vollständig entschieden oder nachweisbar. / Cross-cutting applicability and evidence are incomplete. |
| IR306 | High | Prompt und Delivery Authority / Prompt and delivery authority | NeedsRemediation | Der Autonomous-Prompt fordert `MergeAndSync` und nur ein aktuelles Review, obwohl `DEC-T03` offen ist und historische Receipt-Daten, Eligibility oder ein Review keine aktuelle Ausführungs-, Remote-, Merge- oder Bypass-Autorität erteilen. / The autonomous prompt exceeds the current authority boundary. |

## Offene Fragen und Entscheidungen / Open questions and decisions

`DEC-T03` benötigt drei ausdrückliche menschliche Antworten. Dieses Review
trifft sie nicht stillschweigend. / *DEC-T03 needs three explicit human
answers. This review does not decide them implicitly.*

1. **IRQ301 – Zeitquelle / Time source:** Welche autoritative Zeitquelle oder
   Kombination definiert `observed-at` und `freshness-as-of`, einschließlich
   deterministischer Tests und Wall-Clock-Sprüngen? / *Which authoritative
   time source or combination defines observed-at and freshness-as-of,
   including deterministic tests and wall-clock changes?*
2. **IRQ302 – Freshness-Schwellen / Freshness thresholds:** Welche Klassen und
   Schwellen führen zu `Known`, `Stale`, `Unavailable` oder `Degraded`, und wo
   dürfen sie konfiguriert werden? / *Which classes and thresholds produce
   Known, Stale, Unavailable, or Degraded, and where may they be configured?*
3. **IRQ303 – Confidence-Modell / Confidence model:** Benötigt das
   `StateEnvelope` ein Confidence-Feld? Falls ja: Werte und Ableitung; falls
   nein: vollständige Unsicherheitsdarstellung durch Status, Authority,
   Freshness und Reason Code. / *Does StateEnvelope need a confidence field?
   If yes, define values and derivation; if no, fully represent uncertainty
   through status, authority, freshness, and reason code.*

## Vollständige Review-Coverage / Complete review coverage

| Prüffeld / Review area | Status | Begründung / Rationale |
|---|---|---|
| Identität, Zielgruppe, Zweck, Scope und Non-Goals / Identity, audience, goal, scope, and non-goals | Pass mit IR303 | State-Semantik und die Grenzen zu Discovery, UI und Orchestration sind erkennbar; sprachliche Parität und Einstiegsterminologie bleiben unvollständig. / Purpose and ownership boundaries are identifiable; language parity and terminology remain incomplete. |
| Vorwissen / Prior knowledge | Fail | „Grundlegende Zustandsmodelle“ genügt für die zahlreichen nicht erklärten State-, Evidence- und Workflow-Begriffe nicht; siehe IR303. / The stated prior knowledge does not cover the unexplained terms. |
| Sprache und Erstbegriffserklärung / Language and first-use terminology | Fail | Siehe IR303. / See IR303. |
| Text-first Status, Abhängigkeiten, Decisions und nächste Aktion / Text-first state and next action | Fail | `ReadyForReview` und RAW-01 sind genannt, aber Completed/Eligible, `DEC-T03`, Review-only Next Action und Authority-Trennung fehlen; siehe IR301 und IR303. / Current ordered state is incomplete. |
| Atomare und prüfbare Anforderungen / Atomic and testable requirements | Fail | Die offenen Zeit-/Freshness-/Confidence-Regeln und fehlenden Status-/Reason-Code-Ableitungen verhindern deterministische Prüfung; siehe IR301 und IR304. / Open decisions and missing derivation rules block deterministic tests. |
| Messbare Akzeptanz und Evidence / Measurable acceptance and evidence | Fail | Siehe IR304 und IR305. / See IR304 and IR305. |
| Abhängigkeit, Authority, Delivery, Risiken und Follow-up / Dependencies and authority | Fail | Der RAW-01-Handoff ist grundsätzlich korrekt; `Node Evidence`, Prompt-Grenze, Risiken und aktuelle Authority sind nicht sicher gebunden; siehe IR302 und IR306. / The RAW-01 handoff is valid, but node evidence and authority boundaries are not. |
| Security, Privacy, A11Y, Plattform und Supply Chain / Cross-cutting applicability | Fail | Siehe IR305. / See IR305. |
| Referenzen und Prompt-Parität / References and prompt parity | Fail | Quellen und RFs sind auffindbar, aber nicht atomar rückverfolgbar; Receipt-Decision-State und Autonomous-Prompt widersprechen dem Target; siehe IR301, IR304 und IR306. / References are discoverable but not fully traceable, and prompt/receipt state conflicts remain. |
| Secrets, unnötige Personendaten und Binärinhalt / Secrets, unnecessary personal data, and binary content | Pass mit IR305 | Ziel und neue Review-Artefakte sind strict UTF-8 ohne BOM/NUL; der Secret Scan findet nichts. Die normative Datenminimierung bleibt offen. / Files are strict UTF-8 without BOM or NUL and the secret scan is clean; normative data minimisation remains open. |

## Positive Nachweise / Positive evidence

- RAW-03-Targethash und Git-Blob stimmen mit dem unveränderten Ziel überein. /
  *The RAW-03 target hash and Git blob match the unchanged target.*
- Authoring Receipt RAW-03: Bash und PowerShell `PASS`; Ziel- und
  Source-Pack-Hashes sind aktuell. / *Both authoring validators pass.*
- Requirements Governance Schema 2.0: Bash und PowerShell `Aligned`. /
  *Both governance validators report Aligned.*
- Series Manifest und Receipt: Bash und PowerShell `PASS`; `14` Ziele, `1`
  Root und `14` Abhängigkeiten. / *Both Series validators pass.*
- RAW-01 ist `Completed`; RAW-03 ist der einzige deklarierte
  `Eligible`-Kandidat. RAW-02 und RAW-04 bleiben durch RAW-03 blockiert. /
  *RAW-01 is Completed; RAW-03 is the sole declared Eligible candidate. RAW-02
  and RAW-04 remain blocked by RAW-03.*
- `git diff --check`, UTF-8/BOM/NUL-Prüfung und Secret Scan bestehen. /
  *Whitespace, encoding, and secret checks pass.*

Die bestandenen Strukturvalidatoren widerlegen IR301 nicht: Sie bestätigen
Hash- und Schemaaktualität, prüfen aber nicht, ob die leeren Decision-Felder
des Receipts dem fachlichen Inhalt entsprechen. / *The passing structural
validators do not negate IR301: they prove hash and schema currency but do not
compare empty Receipt decision fields with the domain meaning of the target.*

## Serienauswirkung / Series impact

Dieses Single Review ändert weder RAW-03, dessen Authoring Receipt noch die
Serienartefakte. Die bereits autorisierte, noch uncommittete Series-Operation
bleibt unberührt: RAW-03 ist `Eligible`, aber wegen dieses
`NeedsClarification`-Ergebnisses nicht startfähig. Eligibility ist
Reihenfolge-Evidence, keine Qualitäts-, Start- oder Delivery-Freigabe. /
*This Single review changes neither RAW-03, its Authoring Receipt, nor the
Series artifacts. The existing authorised but uncommitted Series operation is
preserved. RAW-03 is Eligible but cannot start with this NeedsClarification
result. Eligibility is ordering evidence, not quality, start, or delivery
authority.*

## AEPS-Evidence-Folgeprüfung / AEPS evidence follow-up

Das materielle Review löst die vorgeschriebene AEPS-Prüfung aus. IR302 bis
IR306 sind durch vorhandene Findings abgedeckt. IR301 liefert jedoch neue,
reproduzierbare Negativ-Evidence: Beide Authoring-Validatoren melden `PASS`,
obwohl die leeren Decision-Felder des Receipts dem offenen `DEC-T03` im
hashgebundenen Target widersprechen. `AEPS-FIND-AOC-015` erfasst diese
semantische Receipt-Lücke; Matrix, Gap-Analyse und Handoff-Empfehlung werden
atomar ergänzt. Das Capture Receipt liegt unter
`docs/aeps/receipts/2026-08-02-raw-03-needs-clarification.md`. / *The material
review triggers the required AEPS assessment. Existing findings cover IR302
through IR306. IR301 adds reproducible negative evidence: both authoring
validators pass even though empty Receipt decision fields contradict open
DEC-T03 in the hash-bound target. AEPS-FIND-AOC-015 records this semantic
Receipt gap, with atomic updates to the matrix, gap analysis, and handoff
recommendation.*

## Dokumentationsauswirkung / Documentation impact

Entscheidung: `UpdateRequired`. Quelle ist das ausdrücklich angeforderte
unabhängige RAW-03-Single-Review; Owner ist `RAW-03 intake review`. Neu sind
Review-Request, maschinenlesbares Ergebnis und dieser Bericht. Evidence sind
die gebundenen Ziel-/Request-Hashes und die bestandenen Authoring-,
Governance-, Series-, Encoding-, Whitespace- und Secret-Prüfungen. Das
reviewte Lastenheft bleibt unverändert. / *Decision: UpdateRequired. The
requested independent RAW-03 Single review is the source and RAW-03 intake
review is the owner. The request, machine-readable result, and this report are
new; the reviewed intake remains unchanged.*

## Risiken, Ausnahmen und Nicht-Autorität / Risks, exceptions, and non-authority

Es wurden keine Risiken akzeptiert und keine Operator-Ausnahmen erteilt.
Zusammenfassung: Critical `0`, High `6`, Medium `0`, Low `0`. Das Review
genehmigt weder die fachlichen Antworten noch eine Intake-Reparatur, Specify,
Implementierung, Remote Writes, Merge, Bypass, Preset-Änderung oder
Upstream-Handoff. / *No risk or operator exception was accepted. Summary:
Critical 0, High 6, Medium 0, Low 0. The review authorises no decision,
repair, delivery, preset change, or upstream handoff.*

## Exakte nächste Aktion / Exact next action

Thorsten beantwortet ausdrücklich `IRQ301`, `IRQ302` und `IRQ303`. Erst danach
kann ein begrenzter `$speckit-intake-update` die bestätigten Antworten und die
Findings `IR301` bis `IR306` einarbeiten, Receipt-/Serien-Hashbindung erneuern
und ein vollständiges RAW-03-Re-Review vorbereiten. Ohne diese Antworten gibt
es keinen sicheren schreibenden Spec-Kit-Befehl. / *Thorsten explicitly
answers IRQ301 through IRQ303. Only then can a bounded intake update record
the confirmed answers and remediate IR301 through IR306, renew Receipt and
Series hashes, and prepare a full RAW-03 re-review. No safe writing Spec Kit
command exists before those answers.*
