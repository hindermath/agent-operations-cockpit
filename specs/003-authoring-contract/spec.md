# Feature-Spezifikation: Authoring-Vertrag / Feature Specification: Authoring Contract

**Feature-Branch / Feature Branch**: `003-authoring-contract`

**Erstellt / Created**: 2026-09-05

**Status**: Geklaert, fuer die Checklist-Phase bereit / Clarified, ready for the Checklist phase

**Eingabe / Input**: Exakt gebunden an `requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.md`; zulaessig ist ausschliesslich dessen genehmigte post-domain Erneuerung, keine Produktimplementierung, kein weiteres Intake-Update, kein Delete, kein automatischer Review-Start, keine nachgelagerte Ausfuehrung, keine Level-0-Aenderung und keine Preset-Promotion. / Exactly bound to `requirements/intakes/active/Lastenheft_META-LH-03-Authoring-Contract.md`; only its approved post-domain renewal is allowed, with no product implementation, other intake update, delete, automatic review start, downstream execution, Level-0 change, or preset promotion.

**Zielgruppe / Audience**: IHK-IT-Auszubildende ab dem ersten Ausbildungsjahr und erfahrene Fachkraefte mit Markdown- und Git-Grundlagen; Spec-Kit-Erfahrung wird nicht vorausgesetzt. / First-year IHK IT apprentices and experienced professionals with basic Markdown and Git knowledge; no Spec Kit experience is assumed.

**Aktuelle Bindung / Current binding**:

- Lastenheft / requirements intake: SHA-256 `ca159a03a91a19c3f2812a1a638604ca29dab816a20a9a67b7c5d06b3281f5eb`
- Ready-Single-Review: `specs/intake-review-results/meta-lh-03-authoring-contract-2026-09-05-r1.json`, SHA-256 `2fe319d7c88ce5790f6ff6ba9a7d693936a7b88c787ff7dbe7588b5df9a35679`, Review-ID `0b31261e-e794-461f-8c28-3e3d9a518f69`, Status `Ready`, ohne Findings, Fragen, akzeptierte Risiken oder Operator-Ausnahmen / without findings, questions, accepted risks, or operator exceptions
- Authoring Receipt: `specs/intake-authoring-receipts/META-LH-03-Authoring-Contract.json`, SHA-256 `85ffcea67b0723241606040c5d2b9eb586a51d8d13005b676ceb6eeab2caa745`
- Freshness-Aufloesung / freshness resolution: `current-evidence-binding.json` ist fuer die erneuerten aktuellen Leaf-Bindungen von META-LH-02, META-LH-03, META-LH-05 und RAW-03 massgeblich; Hashes in terminalen oder abgeschlossenen kanonischen Snapshots bleiben ausschliesslich historische Evidence. / `current-evidence-binding.json` governs the renewed current leaf bindings for META-LH-02, META-LH-03, META-LH-05, and RAW-03; hashes in terminal or completed canonical snapshots remain historical evidence only.
- Autonomer Laufzustand / autonomous run state: `specs/003-authoring-contract/autonomous-run-state.json`, Run-ID `044b77ae-85fd-46ee-97f4-61ce7a2c9c66`
- Akzeptierte Startbasis / accepted start base: `ada16a88833aae246f2db396a565bc941109617b`; META-LH-01 und META-LH-02 sind abgeschlossen und archiviert und werden nicht als fehlende aktive Ziele wiederhergestellt. / META-LH-01 and META-LH-02 are completed and archived and are not restored as missing active targets.

Die [separat genehmigte Bindungsreparatur](binding-approval.md) erneuert nur die
Voraussetzungen dieses bestehenden Laufs. Die [aktuelle Evidence-Bindung](current-evidence-binding.json)
bewahrt die abgeschlossenen historischen Series-/META-LH-02-Nachweise.
Sie erweitert weder den fachlichen Authoring-Scope noch die Befugnis erzeugter
Prompts. Die ursprüngliche Specify-Fassung bleibt unter
[Specify-Snapshot](phase-results/specify-spec.md) erhalten. /
*The separately approved binding repair renews only this run's prerequisites.
The current-evidence binding preserves completed historical Series/META-LH-02
evidence and expands neither domain scope nor generated-prompt authority.
The original Specify version remains in the linked snapshot.*

## Begriffe fuer den Einstieg / Terms for first-time readers

- **Lastenheft / requirements intake** beschreibt Bedarf, Grenzen und messbare Ergebnisse, nicht die technische Umsetzung. / Describes needs, boundaries, and measurable outcomes rather than technical implementation.
- **Receipt / Nachweis** ist eine maschinenlesbare Bindung von Identitaet, Quellen, normalisierten Hashes, Entscheidungen, Autoritaet und genau einer naechsten Aktion. / A machine-readable binding of identity, sources, normalized hashes, decisions, authority, and exactly one next action.
- **Provenienz / provenance** bezeichnet die nachvollziehbare Herkunft und Reihenfolge der verwendeten Quellen. / Means the traceable origin and order of the sources used.
- **Normalisierter SHA-256 / normalized SHA-256** ist der Hash nach Entfernung eines UTF-8-BOM und Vereinheitlichung der Zeilenenden auf LF, ohne weitere Inhaltsaenderung. / Is the hash after removing one UTF-8 BOM and normalizing line endings to LF without another content change.
- **Review-Handoff** ist die ausdrueckliche Uebergabe an ein unabhaengiges Intake-Review; die Uebergabe startet das Review nicht. / Is the explicit handoff to an independent intake review; the handoff does not start the review.
- **Prompt-Bindung / prompt binding** bedeutet, dass sichtbarer Befehl und Receipt auf dasselbe exakte Lastenheft und dieselbe Authority-Grenze verweisen. / Means that the visible command and receipt point to the same exact intake and authority boundary.
- **Materialentscheidung / material decision** ist eine menschliche Wahl, die Scope, Security, Delivery oder Akzeptanz veraendert. / Is a human choice that changes scope, security, delivery, or acceptance.
- **Fail-closed** bedeutet, bei fehlender oder widerspruechlicher Evidence sicher zu stoppen und keine Annahme als Freigabe zu behandeln. / Means stopping safely when evidence is missing or inconsistent and never treating an assumption as approval.

Weitere Begriffe stehen im [zweisprachigen Glossar](../../requirements/baseline/glossary.md). / *The [bilingual glossary](../../requirements/baseline/glossary.md) explains additional terms.*

## Klaerungen / Clarifications

### Session 2026-09-05

Es waren keine neuen Fragen erforderlich. Die bereits genehmigte
Versions- und Freshness-Grenze ist eindeutig: META-LH-03 verweist auf das
bereits installierte Authoring-Preset `0.3.1`; aktuelle Leaf-Hashes werden nur
ueber `current-evidence-binding.json` aufgeloest. Terminale META-LH-02- und
abgeschlossene Series-Nachweise bleiben unveraenderte historische Records.
Der Archivdateiname eines abgeschlossenen Vorgaengers ist kein fehlender
aktiver Intake. Diese Klaerung aendert weder Fachscope, FR/NFR/AC, Ownership,
Lifecycle noch Delivery-Grenzen. / *No new question was required. The approved
version and freshness boundary is unambiguous: META-LH-03 references the
already installed Authoring preset 0.3.1, and only the current-evidence binding
resolves current leaf hashes. Terminal META-LH-02 and completed Series evidence
remain immutable historical records. An archived predecessor filename is not
a missing active intake. This clarification changes no domain scope,
requirements, acceptance criteria, ownership, lifecycle, or delivery boundary.*

## Nutzungsszenarien und Pruefung / User Scenarios and Testing *(verbindlich / mandatory)*

### User Story 1 - Einen vollstaendigen Authoring-Vertrag nutzen / Use a complete authoring contract (Prioritaet / Priority: P1)

Als lernende oder erfahrene Fachkraft moechte ich fuer genau einen neuen Intake oder eine ausdruecklich genehmigte atomare Serie einen einheitlichen Vertrag nutzen, damit Identitaet, Quellen, Entscheidungen, Grenzen und Review-Handoff vollstaendig und nachvollziehbar sind. / As an apprentice or experienced professional, I want to use one uniform contract for exactly one new intake or one explicitly approved atomic series so identity, sources, decisions, boundaries, and review handoff are complete and traceable.

**Warum diese Prioritaet / Why this priority**: Ohne vollstaendigen Kern und gebundenes Receipt sind alle weiteren Pruefungen mehrdeutig. / Without a complete core and bound receipt, every later check is ambiguous.

**Unabhaengige Pruefung / Independent Test**: Ein einzelner gueltiger Intake wird gegen die fuenf kanonischen Vertragsartefakte geprueft; alle Pflichtfelder und genau eine naechste Aktion sind menschen- und maschinenlesbar gebunden. / One valid intake is checked against the five canonical contract artifacts; every mandatory field and exactly one next action are bound in human- and machine-readable form.

**Akzeptanzszenarien / Acceptance Scenarios**:

1. **Gegeben / Given** ein bestaetigter Portfolioeintrag, geordnete Quellen und das aufgeloeste Profil, **wenn / when** genau ein Intake erzeugt wird, **dann / then** enthaelt er alle Pflichtfelder aus FR-001 und sein schema-2.0-Receipt alle Bindungen aus FR-002.
2. **Gegeben / Given** eine ausdruecklich genehmigte atomare Serie, **wenn / when** sie vorbereitet wird, **dann / then** bleiben Reihenfolge, Mitgliedschaft und gemeinsame Publikationsgrenze nachvollziehbar und es entsteht keine Teilpublikation.
3. **Gegeben / Given** ein bereits aktives Ziel, **wenn / when** Create versucht wird, **dann / then** wird es nicht ueberschrieben; Update und logisches Delete bleiben getrennten autorisierten Operationen vorbehalten.

---

### User Story 2 - Offene Entscheidungen sicher stoppen / Stop safely on open decisions (Prioritaet / Priority: P2)

Als Maintainer moechte ich bei einer offenen Materialentscheidung einen eindeutigen, nicht ausfuehrbaren Stop-Zustand erhalten, damit fehlende Scope-, Security-, Delivery- oder Akzeptanzentscheidungen keine nachgelagerte Aktion ausloesen. / As a maintainer, I want an unambiguous non-executable stop state for an open material decision so missing scope, security, delivery, or acceptance decisions cannot trigger downstream action.

**Warum diese Prioritaet / Why this priority**: Ein ausfuehrbarer Prompt trotz offener Entscheidung koennte fehlende Autoritaet umgehen. / An executable prompt despite an open decision could bypass missing authority.

**Unabhaengige Pruefung / Independent Test**: Ein gebundener Negativfall erzeugt `NeedsClarification`, stabile Decision-IDs und in beiden Prompt-Bloecken `BLOCKED - DO NOT RUN`, aber keine ausfuehrbare Invocation. / A bound negative case produces `NeedsClarification`, stable decision IDs, and `BLOCKED - DO NOT RUN` in both prompt blocks, but no executable invocation.

**Akzeptanzszenarien / Acceptance Scenarios**:

1. **Gegeben / Given** mindestens eine offene Materialentscheidung, **wenn / when** das Authoring-Ergebnis geprueft wird, **dann / then** sind Status, Decision-ID und Stop-Marker vorhanden und beide Prompt-Bloecke nicht ausfuehrbar.
2. **Gegeben / Given** historische Delivery- oder Bypass-Evidence, **wenn / when** aktuelle Authority fehlt, **dann / then** wird daraus keine aktuelle Berechtigung abgeleitet.
3. **Gegeben / Given** eine neue aktuelle Entscheidung, **wenn / when** ihre Evidence gebunden wird, **dann / then** wird nur der ausdruecklich genehmigte Scope neu bewertet.

---

### User Story 3 - Ready-Prompts exakt und isoliert uebergeben / Hand off exact and isolated Ready prompts (Prioritaet / Priority: P3)

Als Reviewer*in moechte ich bei `ReadyForReview` zwei auf dasselbe Lastenheft gebundene Prompt-Bloecke sehen, damit Specify und Autonomous spaeter bewusst und getrennt gestartet werden koennen. / As a reviewer, I want two prompt blocks bound to the same intake at `ReadyForReview` so Specify and Autonomous can later be started deliberately and separately.

**Warum diese Prioritaet / Why this priority**: Prompt-Paritaet verhindert Ziel- und Authority-Drift zwischen sichtbarer Anleitung und Receipt. / Prompt parity prevents target and authority drift between visible guidance and receipt.

**Unabhaengige Pruefung / Independent Test**: Intake und Receipt werden verglichen; beide Prompt-Bloecke benennen dasselbe repository-relative Ziel, und der Authoring-Schritt startet keinen der Befehle. / Intake and receipt are compared; both prompt blocks name the same repository-relative target, and the authoring step starts neither command.

**Akzeptanzszenarien / Acceptance Scenarios**:

1. **Gegeben / Given** ein `ReadyForReview`-Ziel, **wenn / when** Prompt und Receipt verglichen werden, **dann / then** stimmen Zielpfad und Authority-Grenze exakt ueberein.
2. **Gegeben / Given** ein vollstaendiges Authoring-Ergebnis, **wenn / when** es publiziert wird, **dann / then** startet Authoring weder Review noch Specify, Autonomous, Implementierung oder Delivery.

---

### User Story 4 - Plattformgleiche und sichere Evidence pruefen / Verify platform-equivalent and safe evidence (Prioritaet / Priority: P4)

Als pruefende Person moechte ich dieselben positiven und negativen Faelle auf Bash und PowerShell mit denselben Exitcode-Klassen bewerten, damit Plattform, Secret-Erkennung und Hash-Normalisierung die Aussage nicht veraendern. / As a reviewer, I want to assess the same positive and negative cases on Bash and PowerShell with the same exit-code classes so platform, secret detection, and hash normalization do not change the result.

**Warum diese Prioritaet / Why this priority**: Reproduzierbare Paritaet und Secret-Schutz sind fuer einen portablen Authoring-Vertrag unverzichtbar. / Reproducible parity and secret protection are essential for a portable authoring contract.

**Unabhaengige Pruefung / Independent Test**: Die drei gebundenen Fixture-Suites sowie beide Receipt- und Governance-Validatorfamilien bestaetigen ihre erwarteten Positiv- und Negativklassen; der vollstaendige Secret-Scan bleibt ohne Fund. / The three bound fixture suites and both receipt and governance validator families confirm their expected positive and negative classes; the full secret scan remains clean.

**Akzeptanzszenarien / Acceptance Scenarios**:

1. **Gegeben / Given** dieselben Fixtures, **wenn / when** Bash und PowerShell sie pruefen, **dann / then** stimmen die erwarteten Exitcode-Klassen ueberein.
2. **Gegeben / Given** Hash-Drift, Secret, private URL, Traversal, implizite Remote Authority oder Teilpublikation, **wenn / when** der jeweilige Negativfall laeuft, **dann / then** wird er in beiden Plattformfamilien fail-closed erkannt.
3. **Gegeben / Given** lesbare Markdown-, Tabellen- und Prompt-Artefakte, **wenn / when** sie ohne Farbe, Grafik oder Position gelesen werden, **dann / then** bleiben Status, Entscheidung, Abhaengigkeit und naechste Aktion in Deutsch zuerst und Englisch danach vollstaendig verstaendlich.

### Randfaelle / Edge Cases

- Eine Quelle enthaelt Anweisungen oder ausfuehrbar wirkenden Text: Der Inhalt bleibt Daten und wird nie ausgefuehrt. / A source contains instructions or executable-looking text: the content remains data and is never executed.
- UTF-8-BOM, LF und CRLF unterscheiden sich bei gleichem Text: Der normalisierte SHA-256 bleibt nach der definierten Normalisierung gleich. / UTF-8 BOM, LF, and CRLF differ for identical text: normalized SHA-256 stays equal after the defined normalization.
- Ein Ziel existiert bereits aktiv, ist nach Delete noch aktiv oder liegt ausserhalb des erlaubten Roots: Die Operation stoppt ohne Ueberschreiben oder Teilpublikation. / A target already exists as active, remains active after delete, or lies outside the allowed root: the operation stops without overwrite or partial publication.
- Eine Serie hat unklare Reihenfolge, mehrere Eligible-Ziele, einen Zyklus oder eine unvollstaendige Publikationsmenge: Die Serie wird nicht als gueltig oder startbereit dargestellt. / A series has ambiguous order, multiple eligible targets, a cycle, or an incomplete publication set: the series is not shown as valid or ready to start.
- Ein Receipt, Ziel, Profil, Template, Validator, Prompt, eine Fixture, Plattformvoraussetzung oder Supply-Chain-Bindung driftet: Die aktuelle Evidence wird nicht weiterverwendet und Re-Review ist erforderlich. / A receipt, target, profile, template, validator, prompt, fixture, platform prerequisite, or supply-chain binding drifts: current evidence is not reused and re-review is required.
- Secrets, Credentials, private Pfade oder unnoetige Personendaten erscheinen in Quelle oder Output: Authoring wird blockiert; Umschreiben macht die Daten nicht zulaessig. / Secrets, credentials, private paths, or unnecessary personal data appear in a source or output: authoring is blocked; rewording does not make the data permissible.
- META-LH-01 oder META-LH-02 wird nur unter seinem akzeptierten Archivpfad gefunden: Es bleibt ein abgeschlossener Vorgaenger und wird nicht als aktiver Intake rekonstruiert. / META-LH-01 or META-LH-02 is found only at its accepted archive path: it remains a completed predecessor and is not reconstructed as an active intake.
- Der Arbeitsbaum ist nach einem abgebrochenen Vorgang nicht sauber oder das letzte Operation Receipt passt nicht: Recovery stoppt vor dem naechsten Write. / The working tree is not clean after an interrupted operation or the last operation receipt does not match: recovery stops before the next write.

## Anforderungen / Requirements *(verbindlich / mandatory)*

### Scope und ausdrueckliche Ausschluesse / Scope and explicit exclusions

**Im Scope / In scope** sind Naming, Pflichtfelder, Provenienz, normalisierte Hashes, Review-Handoff, Prompt-Bindung und Validierung fuer genau einen neuen Intake oder eine ausdruecklich genehmigte atomare Intake-Serie. Zusaetzlich ist nach dem letzten Fachartefakt genau eine genehmigte Erneuerung von META-LH-03 mit Operation `986c1d6c-d485-460b-8d8d-7cf5816a2c36`, Receipt `f41328cd-b301-4533-89dc-02aab758ab1f` und Review `b8d49ed7-d05f-40b0-9e18-1aa1b689f1cf` Teil dieses Laufs. Die fachliche Liefermenge besteht aus genau den fuenf kanonischen Vertragsartefakten und der im Lastenheft benannten positiven sowie negativen Evidence. / In scope are naming, mandatory fields, provenance, normalized hashes, review handoff, prompt binding, and validation for exactly one new intake or one explicitly approved atomic intake series. In addition, after the final domain artifact this run includes exactly one approved META-LH-03 renewal with the stated operation, receipt, and review IDs. The domain delivery set consists of exactly the five canonical contract artifacts and the positive and negative evidence named by the intake.

**Ausgeschlossen / Excluded** sind die Ausfuehrung erzeugter Prompts, jedes weitere Intake-Update, jedes Delete, Produktimplementierung, Remote Writes ausserhalb des spaeteren autorisierten Feature-Closeouts, Admin-Bypass, Provider-Administration, Level-0-Arbeit, Preset-Promotion und der Start eines weiteren Lastenhefts. / Excluded are execution of generated prompts, every other intake update, every delete, product implementation, remote writes outside the later authorized feature closeout, admin bypass, provider administration, Level-0 work, preset promotion, and starting another intake.

### Kanonische Vertragsartefakte / Canonical contract artifacts

Genau diese fuenf Pfade bilden den fachlichen Vertrag; die im akzeptierten Intake gebundene Preset-Basis ist `intake-authoring-governance 0.3.1`. Pfad-, Inhalt- oder Versionsdrift erzwingt eine erneute Bindungs- und Review-Pruefung. / Exactly these five paths form the domain contract; the preset baseline bound by the accepted intake is `intake-authoring-governance 0.3.1`. Path, content, or version drift requires renewed binding and review.

1. Intake-Kern / intake core: `.specify/presets/intake-authoring-governance/templates/intake-template.md`
2. Receipt-Schema / receipt schema: `.specify/presets/intake-authoring-governance/templates/intake-authoring-receipt-template.json`
3. Repositoryprofil / repository profile: `.specify/presets/intake-authoring-governance/templates/project-profile-template.md`
4. AOC-Sammlungsvertrag / AOC collection contract: `requirements/intake-governance.json`
5. Paket- und Feldnachweis / package and field evidence: `.specify/presets/intake-authoring-governance/templates/field-validation-summary.md`

### Funktionale Anforderungen / Functional Requirements

- **FR-001:** Jeder Intake MUSS stabile ID und DE/EN-Titel, Zweck, aktuellen
  und angestrebten Zustand, Zielgruppe und Vorwissen, Traceability,
  Scope/Non-Goals, Grenzen, atomare FR/NFR, Dependencies, Decisions, Risiken,
  erwartete Artefakte, messbare AC, positive/negative Evidence und
  Nicht-Autorität gemäß kanonischem Intake-Kern enthalten. / *Every intake MUST
  contain the listed identity, audience, state, traceability, scope,
  requirement, dependency, decision, risk, artifact, acceptance, evidence, and
  non-authority fields defined by the canonical intake core.*
- **FR-002:** Das schema-2.0-Receipt MUSS Quellenreihenfolge, normalisierte
  Quellen- und Zielhashes, stabile Intake-/Operation-ID, Profil, Decisions,
  Authority, Prompt-State, Lineage, optionale Serienbindung und genau eine
  nächste Aktion binden. / *The schema-2.0 Receipt MUST bind ordered sources,
  normalised source and target hashes, stable intake and operation identity,
  profile, decisions, authority, prompt state, lineage, optional Series
  membership, and exactly one next action.*
- **FR-003:** Eine offene Materialentscheidung MUSS `NeedsClarification`,
  stabile Decision-IDs und in beiden Prompt-Blöcken den aus `BLOCKED` und
  `DO NOT RUN` gebildeten Stop-Marker ohne ausführbare Invocation erzeugen. /
  *An open material decision MUST produce NeedsClarification, stable decision
  IDs, and the stop marker made from the two named tokens without executable
  invocations in both prompt blocks.*
- **FR-004:** `ReadyForReview`-Ziele MÜSSEN auf dasselbe exakte Lastenheft
  gebundene Specify-/Autonomous-Prompts enthalten. Kein Authoring-Schritt darf
  sie automatisch ausführen oder aus einem historischen Delivery-Modus
  aktuelle Authority ableiten. / *Ready-for-review targets MUST contain
  Specify and Autonomous prompts bound to the same exact intake. Authoring
  MUST neither execute them automatically nor infer current authority from a
  historic delivery mode.*
- **FR-005:** Bash- und PowerShell-Validatoren MÜSSEN für dieselben positiven
  und negativen Fixtures dieselben Exitcode-Klassen melden. / *Bash and
  PowerShell validators MUST report the same exit-code classes for the same
  positive and negative fixtures.*

### Nichtfunktionale Anforderungen / Non-functional Requirements

- **NFR-001:** Generierte Sprache MUSS Deutsch zuerst und Englisch danach auf
  CEFR-B2-Niveau verwenden, Fachbegriffe beim Erstgebrauch erklären,
  semantische Überschriften und stabile Lesereihenfolge bieten und
  Informationen nie nur über Farbe oder Position vermitteln. WCAG 2.2 AA gilt,
  soweit auf das Artefakt anwendbar. / *Generated language MUST be
  German-first/English-second at CEFR B2, explain first-use terms, use semantic
  headings and stable reading order, and never rely only on colour or
  position. WCAG 2.2 AA applies where relevant.*
- **NFR-002:** Secrets, Credentials, private Pfade und unnötige Personendaten
  MÜSSEN Authoring blockieren. Der eingebettete Secret-Negativfall bleibt eine
  synthetische Testeingabe; aktuell ist kein Authoring-Testpfad in Gitleaks
  ausgenommen. Eine spätere Ausnahme MUSS genau einen benannten Fixture-Pfad
  begrenzen und der vollständige Scan bleibt Pflicht. / *Secrets,
  credentials, private paths, and unnecessary personal data MUST block
  authoring. The embedded secret-negative case is synthetic; no Authoring test
  path is currently allowlisted. A future exception MUST be limited to one
  named fixture path and the full scan remains mandatory.*

### Constitution-Anforderungen / Constitution Requirements

- **CR-001**: Der Level-2-Projektkontext `AgentOperationsCockpit` und seine C#/.NET-Primärsprache sind bindend; C# steht auf der MSL-Allowlist fuer speichersichere Sprachen. / The Level-2 project context and its C#/.NET primary language are binding; C# is on the memory-safe-language allowlist.
- **CR-002**: Alle lesbaren Artefakte folgen WCAG 2.2 AA, soweit anwendbar, und behalten Abhaengigkeiten, Status, Entscheidungen und naechste Aktionen als geordneten Text. / All readable artifacts follow WCAG 2.2 AA where applicable and retain dependencies, status, decisions, and next actions as ordered text.
- **CR-003**: Nutzer- und lernendengerichtete Inhalte sind Deutsch zuerst, Englisch danach, auf CEFR-B2-Niveau, erklaeren Fachbegriffe beim Erstgebrauch und setzen keine Spec-Kit-Erfahrung voraus. / User- and learner-facing content is German first, English second, at CEFR B2, explains terms at first use, and assumes no Spec Kit experience.
- **CR-004**: Statistik wird erst nach abgeschlossener Implementierungsphase oder Feature-Abschluss nach Methodik v2 fortgeschrieben. Der gespeicherte Retrospektivenvertrag wird atomar in Constitution, Projektvorlagen und allen gepflegten Agentenflaechen verankert; fachlicher Authoring-Scope und Delivery Authority bleiben unveraendert. / Statistics is updated only after a completed implementation phase or feature completion under methodology v2. The saved retrospective contract is anchored atomically in the constitution, project templates, and every maintained agent surface; domain authoring scope and delivery authority remain unchanged.
- **CR-005**: NIST SSDF und CWE Top 25 sind fuer dieses Level-2-Feature anwendbar; sprachspezifische sichere C#-, Bash- und PowerShell-Regeln werden bei spaeteren Codeaenderungen geprueft. / NIST SSDF and CWE Top 25 apply to this Level-2 feature; language-specific secure C#, Bash, and PowerShell rules are checked for later code changes.
- **CR-006**: Web/API/Auth, Produkt-AI, Cloud-Runtime, marktfertige Distribution und regulatorische Kundengrenzen sind nicht Teil dieses Features; die begruendeten `N/A`-Entscheidungen stehen in der Anwendbarkeitsmatrix. / Web/API/auth, product AI, cloud runtime, market distribution, and regulated customer boundaries are not part of this feature; justified `N/A` decisions are in the applicability matrix.
- **CR-007**: Die installierten Governance-Presets werden ohne zusaetzliche Autoritaetsableitung bewertet; Intake Authoring, der aktuelle autonome Lauf, Cross-Platform, A11Y, Security, Agent Parity und die begrenzte Vertragsarchitektur sind anwendbar. / Installed governance presets are assessed without deriving extra authority; intake authoring, the current autonomous run, cross-platform, accessibility, security, agent parity, and the bounded contract architecture apply.
- **CR-008**: Die einzige Dokumentationsauswirkungsentscheidung und ihre Begruendung werden im [Laufnachweis](autonomous-run-evidence.md#dokumentationsauswirkung--documentation-impact) gefuehrt; diese Spezifikation verweist darauf und erklaert keine zweite Entscheidung. / The sole documentation-impact decision and rationale are maintained in the linked run evidence; this specification references them and declares no second decision.

### Akzeptanzkriterien / Acceptance Criteria

- **AC-001:** Kanonischer Intake-Kern, Receipt-Template, Repositoryprofil,
  AOC-Sammlungsvertrag und Preset-Version sind vorhanden, hashbar und
  widerspruchsfrei; ein gültiges schema-2.0-Receipt besteht Bash und
  PowerShell. / *Canonical contract artifacts exist, are hashable and
  consistent, and one valid schema-2.0 Receipt passes Bash and PowerShell.*
- **AC-002:** Die drei gebundenen Fixture-Suites enden mit Exitcode `0` und
  bestätigen intern die erwarteten positiven sowie negativen Exitcodes für
  Hash-Drift, Secret, implizite Remote Authority, ausführbaren Blocked-Prompt,
  private URL, ungültigen Root, Teilpublikation, aktives Ziel nach Delete,
  Traversal und Mehrfach-Eligibility. / *All three bound fixture suites exit
  zero and verify the named positive and negative classes internally.*
- **AC-003:** Alle 14 aktiven Receipts bestehen beide Receipt-Validatoren;
  Pflichtfelder sind über Template und schema-2.0-Receipt maschinen- und
  menschenlesbar gebunden. / *All fourteen active Receipts pass both
  validators; required fields are bound through the template and schema-2.0
  Receipt.*
- **AC-004:** Semantisches Review bestätigt vollständige DE/EN-Paare,
  Erstbegriffserklärungen, stabile Überschriften, farbunabhängige Statusangaben
  und Prompt-Parität. Kein Authoring-Schritt startet Review, Specify,
  Autonomous, Implementierung oder Delivery. / *Semantic review confirms the
  language, terminology, structure, colour-independent status, and prompt
  contract. Authoring starts no downstream action.*
- **AC-005:** Der vollständige Gitleaks-Scan endet ohne Fund; keine
  Authoring-Testausnahme ist aktiv. Plattform- oder Supply-Chain-Drift löst
  Re-Evaluation aus. / *The full Gitleaks scan finds no leak and no Authoring
  test exception is active. Platform or supply-chain drift triggers
  re-evaluation.*

### Schluesselentitaeten / Key Entities

- **Intake / Lastenheft**: fachliches Anforderungsdokument mit stabiler Identitaet, Zielgruppe, Scope, Anforderungen, Evidence, Akzeptanz und Nicht-Autoritaet. / Domain requirements document with stable identity, audience, scope, requirements, evidence, acceptance, and non-authority.
- **Receipt / Nachweis**: schema-2.0-Bindung von Intake, Operation, geordneten Quellen, Hashes, Profil, Entscheidungen, Prompt-State, Lineage, optionaler Serienmitgliedschaft und genau einer naechsten Aktion. / Schema-2.0 binding of intake, operation, ordered sources, hashes, profile, decisions, prompt state, lineage, optional series membership, and exactly one next action.
- **Quelle / Source**: explizit geordnete, als Daten behandelte Eingabe mit Provenienz und normalisiertem Hash. / Explicitly ordered input treated as data, with provenance and normalized hash.
- **Repositoryprofil / Repository profile**: projektbezogene Regeln fuer Pfade, Sprache, Zielgruppe, Naming, Inventar, Archive und Quality Gates, ohne die portablen Kernregeln abzuschwaechen. / Project rules for paths, language, audience, naming, inventory, archives, and quality gates without weakening portable core rules.
- **Materialentscheidung / Material decision**: stabile, menschlich zu beantwortende Wahl mit Einfluss auf Scope, Security, Delivery oder Akzeptanz. / Stable human decision affecting scope, security, delivery, or acceptance.
- **Atomare Serie / Atomic series**: ausdruecklich genehmigte geordnete Gruppe vorhandener Intake-Ziele, die nur vollstaendig oder gar nicht publiziert wird. / Explicitly approved ordered group of intake targets published completely or not at all.

## Messbare Ergebnisse / Success Criteria *(verbindlich / mandatory)*

### Messbare Outcomes / Measurable Outcomes

- **SC-001**: Genau fuenf kanonische Vertragsartefakte sind vorhanden, hashbar und widerspruchsfrei; ein gueltiges schema-2.0-Receipt besteht beide Plattformvalidatoren. / Exactly five canonical contract artifacts are present, hashable, and consistent; one valid schema-2.0 receipt passes both platform validators.
- **SC-002**: Alle drei gebundenen Fixture-Suites enden jeweils mit Exitcode `0` und bestaetigen intern jede in AC-002 benannte Positiv- und Negativklasse. / All three bound fixture suites each exit with code `0` and internally confirm every positive and negative class named in AC-002.
- **SC-003**: `14/14` aktive Receipts bestehen sowohl den Bash- als auch den PowerShell-Receipt-Validator; kein Pflichtfeld ist nur maschinen- oder nur menschenlesbar vorhanden. / `14/14` active receipts pass both Bash and PowerShell receipt validators; no mandatory field is present only for machines or only for humans.
- **SC-004**: Ein semantisches Review meldet `0` fehlende DE/EN-Paare, `0` unerklaerte Erstbegriffe, `0` Ueberschriften- oder Lesereihenfolgefehler und `0` farb- oder positionsabhaengige Statusaussagen. / A semantic review reports zero missing German/English pairs, unexplained first-use terms, heading or reading-order errors, and color- or position-dependent status statements.
- **SC-005**: Der vollstaendige Gitleaks-Scan endet ohne Fund und genau `0` Authoring-Testpfade sind ausgenommen. / The full Gitleaks scan ends without a finding and exactly zero authoring test paths are exempted.
- **SC-006**: Eine Person aus der Zielgruppe kann ohne Spec-Kit-Vorwissen anhand der lesbaren Artefakte Zweck, Voraussetzungen, Status, offene Entscheidungen, Nicht-Autoritaet und genau eine naechste sichere Aktion zu `100 %` korrekt benennen. / A person from the audience can identify purpose, prerequisites, status, open decisions, non-authority, and exactly one next safe action with 100 percent accuracy without prior Spec Kit knowledge.
- **SC-007**: Der Authoring-Nachweis startet `0` Review-, Specify-, Autonomous-, Implementierungs- oder Delivery-Aktionen und erzeugt bei offenen Materialentscheidungen `0` ausfuehrbare Prompt-Invocations. / Authoring evidence starts zero review, Specify, Autonomous, implementation, or delivery actions and produces zero executable prompt invocations when material decisions are open.
- **SC-008**: Die Spezifikationsphase endet mit `0` offenen `[NEEDS CLARIFICATION]`-Markern und einer vollstaendig bestandenen Requirements-Qualitaetscheckliste. / The specification phase ends with zero open clarification markers and a fully passed requirements quality checklist.

## Annahmen und Abhaengigkeiten / Assumptions and Dependencies

- Der ausdrueckliche Startauftrag, die akzeptierte Startbasis, Global-Ready 14, das aktuelle Ready-Single-Review, das aktuelle Receipt, der nicht laufende Vorgaenger und der Routing-Status `Aligned` sind Runner-Preflight-Evidence und werden in dieser Phase nicht erneut erzeugt. / The explicit start instruction, accepted start base, Global-Ready 14, current Ready single review, current receipt, non-running predecessor, and `Aligned` routing status are runner preflight evidence and are not regenerated in this phase.
- Die erneuerten aktuellen Leaf-Bindungen fuer META-LH-02, META-LH-03, META-LH-05 und RAW-03 werden ueber `current-evidence-binding.json` aufgeloest. Alte Hashes in terminalen oder abgeschlossenen kanonischen Snapshots werden nicht als aktuelle Bindungen verwendet und nicht umgeschrieben. / Renewed current leaf bindings for the four named targets are resolved through `current-evidence-binding.json`. Old hashes in terminal or completed canonical snapshots are neither used as current bindings nor rewritten.
- META-LH-01 und META-LH-02 bleiben abgeschlossene, archivierte Vorgaenger. Ihre Archivpfade sind gueltige Lifecycle-Evidence, aber keine aktiven Ziele. / META-LH-01 and META-LH-02 remain completed archived predecessors. Their archive paths are valid lifecycle evidence, not active targets.
- Geordnete Quellen, aufgeloestes Repositoryprofil und bestaetigter Portfolioeintrag sind vor Create vorhanden; fehlen sie oder widersprechen sie sich, stoppt Authoring fail-closed. / Ordered sources, resolved repository profile, and confirmed portfolio entry exist before Create; if they are missing or inconsistent, authoring fails closed.
- Der akzeptierte Intake bindet `intake-authoring-governance 0.3.1`. Eine nachgewiesene Preset-, Template-, Validator- oder Mindestversionsdrift wird nicht still uebernommen, sondern loest die im Intake geforderte Re-Evaluation aus. / The accepted intake binds `intake-authoring-governance 0.3.1`. Proven preset, template, validator, or minimum-version drift is not silently adopted and triggers the reevaluation required by the intake.
- Diese Spezifikation trifft keine neue Produkt-, Runtime-, Hosting-, Cloud-, Release- oder Regulierungsentscheidung. / This specification makes no new product, runtime, hosting, cloud, release, or regulatory decision.

## Governance-Anwendbarkeit und Audit-Evidence / Governance Applicability and Audit Evidence

`Applicable` bedeutet, dass der Checkpoint fuer das Feature gilt. Der Umsetzungsstatus beschreibt getrennt, ob bereits Evidence vorliegt. `N/A` bedeutet nicht anwendbar und behaelt `Not Assessed`. / `Applicable` means the checkpoint applies to the feature. Implementation status separately states whether evidence already exists. `N/A` means not applicable and retains `Not Assessed`.

| Checkpoint | Anwendbarkeit / Applicability | Umsetzung / Implementation | Begruendung und Evidence / Rationale and evidence | Owner, Restrisiko, Follow-up und Trigger / Owner, residual risk, follow-up and trigger |
|---|---|---|---|---|
| Intake Authoring Governance | Applicable | Partly Fulfilled | FR-001 bis FR-005, NFR-001 bis NFR-002 und AC-001 bis AC-005 binden den Vertrag; aktuelle Phase-Evidence ist `spec.md` plus `checklists/requirements.md`. / Requirements bind the contract; current phase evidence is the spec and checklist. | AOC-Maintainer; Restrisiko: spaetere Implementierung noch ungeprueft; Follow-up in Plan/Tasks; Trigger: Vertrags- oder Hash-Drift. |
| Intake Review Governance | Applicable | Fulfilled for input | Das Ready-Single-Review ist akzeptierte Eingabe; diese Phase startet oder veraendert kein Review. / The Ready single review is accepted input; this phase starts or changes no review. | AOC-Maintainer; kein aktuelles Restrisiko; Trigger: Intake-, Receipt- oder Review-Drift. |
| Intake Sequencing Governance | Applicable | Fulfilled for input | META-LH-03 ist das autorisierte Ziel; META-LH-01/02 bleiben abgeschlossen und archiviert. Keine Lifecycle-Schreibaktion. / META-LH-03 is authorized; META-LH-01/02 remain completed and archived. No lifecycle write. | AOC-Maintainer; kein aktuelles Restrisiko; Trigger: Series- oder Vorgaengerdrift. |
| Security Governance | Applicable | Partly Fulfilled | Secret-, Privacy-, Quellen- und Hash-Grenzen stehen in NFR-002, Randfaellen und Security-Matrix. / Secret, privacy, source, and hash boundaries are specified. | Security Owner/AOC-Maintainer; spaetere Gate-Evidence fehlt; Trigger: Code-, Fixture-, Secret- oder Supply-Chain-Aenderung. |
| Architecture Governance | Applicable | Partly Fulfilled | Die bestehende Vertrauensgrenze behandelt externe oder repository-interne Quellen nur als Daten und verhindert implizite Authority; keine neue Runtime-Grenze. / The existing trust boundary treats sources only as data and prevents implicit authority; no new runtime boundary. | AOC-Maintainer; Restrisiko: semantische Drift; Follow-up im Plan; Trigger: neue Quelle, Remote-Flow oder Authority-Klasse. |
| iSAQB Architecture Governance | Applicable | Partly Fulfilled | Vertragsinterfaces, Qualitaetsattribute und Fehlerverhalten werden praezisiert; Deployment und Produktarchitektur bleiben unberuehrt. / Contract interfaces, quality attributes, and failure behavior are specified; deployment and product architecture remain unchanged. | AOC-Maintainer; spaetere Architekturpruefung; Trigger: Interface- oder Laufzeitveraenderung. |
| A11Y Governance | Applicable | Partly Fulfilled | NFR-001, SC-004 und SC-006 binden DE-first/EN-second, CEFR B2, WCAG 2.2 AA und text-first. / NFR-001, SC-004, and SC-006 bind the accessibility contract. | A11Y Reviewer/AOC-Maintainer; semantisches Review folgt; Trigger: lesbares Artefakt oder Zielgruppenwechsel. |
| Cross-Platform Governance | Applicable | Partly Fulfilled | FR-005 und AC-001 bis AC-003 verlangen Bash-/PowerShell-Paritaet auf macOS, Linux und Windows. / FR-005 and AC-001 through AC-003 require parity across the target platforms. | AOC-Maintainer; Plattform-Evidence folgt; Trigger: Validator-, Shell- oder Exitcode-Aenderung. |
| Agent Parity Governance | Applicable | Partly Fulfilled | Der Retrospektivenvertrag wird byte-identisch auf fünf Agentenflächen sowie in Constitution und Projektvorlagen verankert. / The retrospective contract is anchored byte-identically across five agent surfaces and in the constitution and project templates. | AOC-Maintainer; Restrisiko bis zur Paritätsprüfung; Follow-up in Plan/Tasks; Trigger: Drift eines Markers, Templates oder Guidance-Pfads. |
| Autonomous Run Governance | Applicable | Partly Fulfilled | Lauf `044b77ae-85fd-46ee-97f4-61ce7a2c9c66`, Modus `MergeAndSync`, aktuelle Benutzerautoritaet und Feature-lokaler Run-State sind gebunden; kein Bypass. / The run, delivery mode, current user authority, and feature-local state are bound; no bypass. | Root ist Run-State-Owner; unerwartete Unterbrechung erfordert Revalidierung, bewusster Stop `speckit-autonomous-resume`; Trigger: Authority-, Head-, Gate- oder State-Drift. |
| Parallel Autonomous Governance | N/A | Not Assessed | Keine Kampagne, keine Worker und keine parallele Lieferautoritaet gehoeren zum Feature. / No campaign, worker, or parallel delivery authority is in scope. | Root; kein Restrisiko; Re-Evaluation nur bei neuem ausdruecklichem Kampagnenauftrag. |
| Model Routing Governance | Applicable | Fulfilled for phase | Routing ist operative Runner-Evidence und keine Feature-Anforderung; keine Modellnamen werden in Anforderungen festgeschrieben. / Routing is operational runner evidence, not a feature requirement; requirements pin no model names. | Root; kein aktuelles Restrisiko; Trigger: Routingstatus nicht mehr `Aligned`. |

### Security, Privacy und Software Supply Chain / Security, Privacy, and Software Supply Chain

| Standard oder Evidence / Standard or evidence | Anwendbarkeit / Applicability | Umsetzung / Implementation | Begruendung und Re-Evaluation / Rationale and reevaluation |
|---|---|---|---|
| MSL / speichersichere Sprache | Applicable | Fulfilled for specification | Primaersprache C#/.NET ist speichersicher; spaetere Bash-/PowerShell-Aenderungen folgen ihren sicheren Sprachregeln. Trigger: Primaersprachen- oder Code-Scope-Aenderung. / Primary C#/.NET is memory-safe; later script changes follow secure language rules. |
| NIST SSDF | Applicable | Partly Fulfilled | Fuer Level-2 verbindlich; Prepare- und Protect-Grenzen sind spezifiziert, Produce-/Respond-Evidence folgt spaeter. Trigger: Plan und Implementierung. / Mandatory for Level 2; Prepare and Protect boundaries are specified, later evidence follows. |
| CWE Top 25 | Applicable | Partly Fulfilled | Fuer Level-2 verbindlich; relevant sind insbesondere Eingabevalidierung, Pfadmanipulation, Befehlsinjektion und Secret-Offenlegung. Trigger: spaetere Validatoraenderung. / Mandatory for Level 2; input validation, path manipulation, command injection, and secret exposure are relevant. |
| OWASP ASVS | N/A | Not Assessed | Kein Web-, API-, HTTP-, Authentifizierungs- oder Autorisierungsdienst. Trigger: ein solcher Dienst kommt in Scope. / No web, API, HTTP, authentication, or authorization service. |
| SBOM und VEX | N/A | Not Assessed | Diese Feature-Phase erzeugt kein Release oder distributierbares Artefakt und veraendert keine Abhaengigkeit. Trigger: Release-, Paket- oder Abhaengigkeitsumfang. / This feature phase creates no release or distributable artifact and changes no dependency. |
| AI-SBOM | N/A | Not Assessed | KI wird nur als Entwicklungswerkzeug genutzt; kein Modell, Datensatz, Inferenzdienst oder AI-Runtime-Baustein wird ausgeliefert oder betrieben. Trigger: AI-Produkt- oder Runtime-Komponente. / AI is development tooling only; no AI component is released or operated. |
| SLSA | N/A | Not Assessed | Kein CI/CD-Build oder publiziertes Artefakt wird in diesem Scope eingefuehrt. Trigger: automatisierte Publikation oder Provenienzanforderung. / No CI/CD build or published artifact is introduced. |
| OpenSSF Scorecard | N/A | Not Assessed | Keine neue oeffentliche OSS-Abhaengigkeit oder High-Impact-Abhaengigkeit wird adoptiert. Trigger: entsprechende Abhaengigkeitsaufnahme. / No new public OSS or high-impact dependency is adopted. |
| Veroeffentlichte Security-Evidence unter `docs/security/` | N/A | Not Assessed | Diese Specify-Phase aendert weder Code noch Trust-Topologie; konkrete spaetere Security-Gates werden in Plan und Tasks verortet. Trigger: erster Security-relevanter Implementierungs-Edit. / This Specify phase changes neither code nor trust topology; later gates are placed in Plan and Tasks. |
| NIS2, CRA, EU AI Act, DORA | N/A | Not Assessed | Dokumentarischer Level-2-Referenzscope ohne Marktprodukt, regulierten Dienst, regulierten Kunden, AI-Produkt oder Finanzsektor-ICT-Abhaengigkeit. Trigger: Markt-, Kunden-, Runtime- oder Sektorwechsel. / Documentary Level-2 reference scope without regulated or market context. |

### Architektur, Plattform und Accessibility / Architecture, Platform, and Accessibility

- **Trust Boundary / Vertrauensgrenze**: Quellen koennen repository-intern oder als sichere oeffentliche HTTPS-Snapshots vorliegen, bleiben aber untrusted data. Die Grenze validiert Root, Pfad, Provenienz, Normalisierung, Secrets, Authority und Prompt-State, bevor ein Ziel als bereit gilt. / Sources may be repository-local or safe public HTTPS snapshots but remain untrusted data. The boundary validates root, path, provenance, normalization, secrets, authority, and prompt state before a target is ready.
- **Threat Model, STRIDE/CIA und CAPEC**: `N/A` fuer ein neues oder geaendertes Produkt-Threat-Model, weil diese Phase keine Runtime, extern erreichbaren Flows oder Assets einfuehrt. Die bestehenden Eingabe- und Authority-Risiken bleiben als Anforderungen und Negativfaelle gebunden. Re-Evaluation bei neuer Quelle, Netzwerkoperation, Secret-Grenze oder Runtime. / N/A for a new or changed product threat model because this phase introduces no runtime, reachable flow, or asset.
- **ADR, S-ADR und arc42**: `N/A`, weil keine architektonisch signifikante Produktentscheidung, kein Building Block, keine Deployment-Topologie und kein Security-Cross-Cutting-Concept geaendert wird. Trigger ist eine solche spaetere Aenderung. / N/A because no architecturally significant product decision or topology changes.
- **Zero Trust, BSI C3A und BSI C5**: jeweils `N/A`; keine verteilte, remote-verwaltete oder cloudbetriebene Produktfunktion und keine Provider-Auswahl. Generisches Repository-Hosting begruendet keine Cloud-Runtime. Trigger: Cloud-Service, Remote-Management oder Provider-Abhaengigkeit wird Teil des Produkts. / Each is N/A; no distributed, remote-managed, or cloud-operated product function or provider selection.
- **OWASP SAMM**: `N/A` fuer eine neue Feature-Evidence, weil keine Programmreifeentscheidung getroffen wird. Trigger: periodische Reifegradbewertung oder daraus abgeleitete Massnahme. / N/A for new feature evidence because no program-maturity decision is made.
- **Plattformvertrag / Platform contract**: macOS und Linux nutzen Bash, Windows nutzt PowerShell Core 7; beide Familien pruefen dieselben Klassen. Fuer das bestehende read-only Validierungskonzept sind `--dry-run` und `-WhatIf` `N/A`, weil der normale Lauf keine fachlichen Writes ausfuehrt. Falls ein schreibendes Tool in Scope kommt, werden beide Preview-Modi Pflicht. / macOS and Linux use Bash, Windows uses PowerShell Core 7; both check the same classes. Preview modes are N/A for read-only validation and become mandatory if a writing tool enters scope.
- **Cmdlet und Man-Page / Cmdlet and man page**: Falls der bestehende Receipt-Validator fachlich geaendert wird, bleibt `Test-IntakeAuthoringReceipt` der genehmigte Verb-Noun-Vertrag und `.specify/presets/intake-authoring-governance/docs/man/validate-intake-authoring-receipt.1` der Unix-Leserpfad; PowerShell-Hilfe bleibt bilingual. Das ist eine Bindung bestehender Oberflaechen, keine neue Anforderung. / If the existing receipt validator changes, the named cmdlet and man page remain the existing interface contract; this adds no new scope.
- **Accessibility-Evidence**: `docs/accessibility/` ist `N/A` fuer diese reine Specify-Phase; die vollstaendige Requirements-Checkliste ist der aktuelle A11Y-Nachweis. Trigger: neues UI, HTML, Bild oder eigenstaendige Accessibility-Baseline. / `docs/accessibility/` is N/A for this Specify-only phase; the requirements checklist is current evidence.
- **Didaktische Code-Kommentare / Didactic code comments**: `N/A` in Specify, da kein Code geaendert wird. Bei spaeterer nichttrivialer Validatorlogik wird der Kommentarbedarf fuer Warum, Grenze oder Beweislimit geprueft. / N/A in Specify because no code changes; later non-trivial validator logic requires review.

## Autonomer Lauf, Evidence und Authority / Autonomous Run, Evidence, and Authority

- **Delivery-Modus / Delivery mode**: `MergeAndSync`, ausdruecklich fuer genau diesen META03-Lauf autorisiert. Root besitzt Run-State und spaeteren Closeout. Diese Spezifikationsphase fuehrt keinen Commit, Push, Merge oder Sync aus. / `MergeAndSync`, explicitly authorized for this META03 run only. Root owns run state and later closeout. This specification phase performs no commit, push, merge, or sync.
- **Akzeptierte Eingaben / Accepted inputs**: exakt die oben gebundenen Intake-, Ready-Review- und Receipt-Artefakte. / Exactly the intake, Ready review, and receipt artifacts bound above.
- **Nicht-Autoritaet / Non-authority**: Kein Admin-Bypass, keine Provider-Administration, keine Level-0-Aenderung, keine Preset-Promotion und kein Folge-Lastenheft. Historische Receipt- oder Delivery-Autoritaet erweitert den aktuellen Auftrag nicht. / No admin bypass, provider administration, Level-0 change, preset promotion, or next intake. Historical authority does not expand this instruction.
- **Mutable Validation Tokens / veraenderliche Pruefwerte**: Pfade, normalisierte SHA-256-Werte, Exitcode-Klassen, Status, Artefaktzaehler und Run-State sind an konkrete Evidence gebunden. Jede Drift stoppt fail-closed und verlangt Revalidierung. / Paths, normalized hashes, exit-code classes, status, artifact counts, and run state are bound to concrete evidence. Drift fails closed and requires revalidation.
- **Causal Closeout / kausaler Abschluss**: Spaeter erforderlich, weil `MergeAndSync` autorisiert ist; er muss den exakt reviewten Head, technische Gates, Review-Threads, tatsaechlichen Merge, Default-Branch-Sync und finale Validierung zeitlich korrekt binden. / Required later because `MergeAndSync` is authorized; it must causally bind the reviewed head, gates, review threads, actual merge, default-branch sync, and final validation.
- **Stop und Recovery / Stop and recovery**: Ein bewusster Stop wird als `PausedByUser` behandelt und nur per Resume fortgesetzt. Eine unerwartete Unterbrechung, ein nicht sauberer Arbeitsbaum oder Evidence-Drift erzwingt vollstaendige Revalidierung vor dem naechsten Write. / A deliberate stop is treated as `PausedByUser` and resumes only through the resume flow. An interruption, dirty worktree, or evidence drift requires revalidation before another write.

## Dokumentationsauswirkung / Documentation Impact

Die einzige Entscheidung, ihre Quelle, den Owner, den Leserpfad und die
Re-Evaluation fuehrt der
[Laufnachweis](autonomous-run-evidence.md#dokumentationsauswirkung--documentation-impact).
Diese Spezifikation verweist auf diese kanonische Entscheidung und erklaert
keine eigene oder zusaetzliche Dokumentationsauswirkung. / *The linked run
evidence owns the sole decision, its source, owner, reader path, and
reevaluation. This specification references that canonical decision and does
not declare an independent or additional documentation impact.*

## Aktuelle Phasengrenze / Current Phase Boundary

Diese Phase schreibt nur `spec.md`, bei einem tatsaechlich geaenderten Marker
`checklists/requirements.md`, `phase-results/clarify-report.md` und den exakten
strukturierten Runner-Output. Sie aendert keine Intakes, Receipts, Reviews,
kanonischen Series, Presets, Baseline, Shared Ledgers, Run-State-Datei oder
historische Evidence, startet keine naechste Phase und fuehrt keinen Git- oder
Remote-Schritt aus. / *This phase writes only the spec, the requirements
checklist when a marker actually changes, the Clarify report, and the exact
structured runner output. It changes no intake, receipt, review, canonical
Series, preset, baseline, shared ledger, run-state file, or historical evidence,
starts no next phase, and performs no Git or remote action.*
