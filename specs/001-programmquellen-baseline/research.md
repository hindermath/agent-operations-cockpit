# Recherche: Programmquellen-Baseline / Research: Program Sources Baseline

## Zweck / Purpose

Diese Phase klaert ausschliesslich, wie die vorhandene META-LH-01-Baseline mit minimalen Dokumentaenderungen gegen die formal geklaerte Spezifikation konvergiert. Es gibt keine Technologie- oder Produktforschung. / This phase resolves only how the existing META-LH-01 baseline converges on the formally clarified specification with minimal documentation changes. It performs no technology or product research.

## Entscheidung 1: Delta-Audit vor Bearbeitung / Decision 1: Delta audit before editing

**Entscheidung / Decision**: Jede der sechs Domain-Dateien wird zuerst gegen `FR-001` bis `FR-013`, `NFR-001` bis `NFR-005` und `SC-001` bis `SC-008` geprueft. Nur belegte Luecken werden geaendert; korrekte Inhalte bleiben wort- oder sinngleich erhalten. / Each of the six domain files is first checked against the stated functional, non-functional, and success criteria. Only evidenced gaps are changed; correct content is preserved verbatim or semantically.

**Begruendung / Rationale**: Die Dateien enthalten bereits belastbare Authority-, Supersession-, Owner- und Gate-Aussagen. Eine Neuschreibung wuerde unnoetige Drift und Review-Risiko erzeugen. / The files already contain sound authority, supersession, ownership, and gate statements. Rewriting them would create unnecessary drift and review risk.

**Gepruefte Alternativen / Alternatives considered**:

- Vollstaendige Neufassung: verworfen wegen hoher semantischer Drift. / Full rewrite: rejected due to high semantic drift.
- Nur Formatkorrektur: verworfen, weil exakte Source-/RF-/Owner-Luecken materiell sind. / Formatting-only edit: rejected because exact source, finding, and owner gaps are material.

## Entscheidung 2: Exakte Einzelzeilen statt Bereichszaehlung / Decision 2: Exact individual rows instead of range counting

**Entscheidung / Decision**: `source-pack.md` und `coverage-matrix.md` stellen jede der 23 zugelassenen Source-IDs einzeln dar. `review-findings-ledger.md` und `coverage-matrix.md` halten `RF-01` bis `RF-21` einzeln pruefbar. Bereichsnotation darf nur in erklaerendem Text stehen und nie die exakte Inventur ersetzen. / The source pack and coverage matrix represent all 23 permitted source IDs individually. The findings ledger and coverage matrix keep every finding individually verifiable. Range notation may appear in explanatory prose but never replace the exact inventory.

**Begruendung / Rationale**: Die vorhandene Sammelzeile `SRC-163–167` und gruppierte Coverage-Zeilen verhindern eine robuste Exaktmengenpruefung; `SRC-ES-01` fehlt aktuell in der Coverage Matrix. / The existing aggregate source row and grouped coverage rows prevent robust exact-set validation, and `SRC-ES-01` is currently absent from the coverage matrix.

**Gepruefte Alternativen / Alternatives considered**:

- Bereichsparser: verworfen, weil er die einfache, lesbare Source-of-Truth unnoetig kompliziert. / Range parser: rejected because it complicates the readable source of truth.
- Separate maschinenlesbare Produktdatei: verworfen, weil kein Produktmanifest oder neues Datensystem autorisiert ist. / Separate machine-readable product file: rejected because no product manifest or new data system is authorised.

## Entscheidung 3: Stabiler ausfuehrbarer Validierungsvertrag / Decision 3: Stable executable validation contract

**Entscheidung / Decision**: `contracts/baseline-validation-contract.md` beschreibt die Proof-Grenze; `contracts/validate_meta_lh01.py` ist der einzige stabile, kopierbare und read-only ausfuehrbare Vertrag. Explizite Modi pruefen Input-Bindungen, das globale 14er-Ready-Gate, Domain-Struktur, Review-Evidence, Documentation Impact, AEPS und den exakten Stage-Kandidaten. `contracts/test_validate_meta_lh01.py` nutzt nur temporaere Fixtures. / The Markdown contract describes the proof boundary; the Python file is the sole stable, copy-ready, read-only executable contract. Explicit modes validate the named evidence classes, and its tests use temporary fixtures only.

**Begruendung / Rationale**: Der unabhaengige Review hat gezeigt, dass Markdown und verstreute Inline-Pruefungen keine stabile Ausfuehrung oder Negativfaelle liefern. Das feature-lokale Standardbibliothek-Tool ist Workflow-Evidence, keine Produktfunktion, Dependency, Runtime- oder Preset-Aenderung. / The independent review showed that Markdown and scattered inline checks do not provide stable execution or negative cases. The feature-local standard-library tool is workflow evidence, not product functionality, a dependency, runtime, or preset change.

**Gepruefte Alternativen / Alternatives considered**:

- Kein `contracts/`-Artefakt: verworfen, weil dann exakte Pruefsemantik zwischen Plan und Quickstart verteilt waere. / No contract artefact: rejected because exact validation semantics would be scattered.
- Neues Bash-/PowerShell-Paar: verworfen, weil keine neue plattformspezifische Produktoberflaeche entsteht und der Standardbibliothek-Vertrag vorhandene Paare nur read-only aufruft. / A new Bash/PowerShell pair was rejected because no platform-specific product surface is created; the standard-library contract only invokes installed pairs read-only.

## Entscheidung 4: A11Y und Sprache erhalten getrennte Reviews / Decision 4: Accessibility and language use separate reviews

**Entscheidung / Decision**: Homogeneity bleibt eine reine Strukturpruefung. Eine unabhaengige Rolle erfasst je Domain-Datei strukturierte `Pass`-/`Fail`-Werte mit Begruendung fuer Sprache, CEFR B2, Begriffe, Ueberschriften, Tabellen, Links, Text-first, fachliche Wahrheit und Authority-Auslegung. Der Python-Modus prueft nur Vollstaendigkeit und Ergebnis dieser Review-Evidence. / Homogeneity remains a structural check. An independent role records structured results and rationales per domain file; Python validates only evidence completeness and result.

**Begruendung / Rationale**: Validatoren koennen Struktur und Marker pruefen, aber keine semantische Gleichwertigkeit, Lesbarkeit, fachliche Wahrheit oder WCAG-Anwendbarkeit beweisen. Deshalb bewerten getrennte unabhaengige Rollen Sprache/Fachlichkeit und Accessibility mit eigenen Evidence-Dateien und Null-Blocking-Grenzen. / Validators cannot prove language, domain truth, or WCAG applicability, so separate independent roles and evidence files are required.

**Gepruefte Alternativen / Alternatives considered**:

- Nur Homogeneity-Scanner: verworfen wegen semantischer Proof-Grenze. / Homogeneity scanner only: rejected due to its semantic proof limit.
- Grafikbasierte Review-Evidence: verworfen, weil text-first und assistive Nutzung verbindlich sind. / Diagram-based evidence: rejected because text-first and assistive use are mandatory.

## Entscheidung 5: Security- und Public-Content-Pruefung ohne neue Supply Chain / Decision 5: Security and public-content review without a new supply chain

**Entscheidung / Decision**: `gitleaks` und die vorhandenen Scanner beweisen nur Secret-Muster. Eine getrennte strukturierte unabhaengige Public-Content-Review-Evidence deckt exakt die tatsaechliche Kandidatenliste fuer private Pfade, unnoetige Personendaten und Publikationseignung ab. / Existing scanners prove only secret-pattern results. Separate structured independent public-content evidence covers the exact candidate inventory for private paths, unnecessary personal data, and publication suitability.

**Begruendung / Rationale**: Die einzige relevante Sicherheitsgrenze ist veroeffentlichbarer Text. Das Feature liefert keine Binaerdatei, Dependency, Runtime oder Release. / The only relevant security boundary is publishable text. The feature delivers no binary, dependency, runtime, or release.

**Gepruefte Alternativen / Alternatives considered**:

- Supply-Chain-Artefakte vorsorglich erzeugen: verworfen als unbelegte Scope-Erweiterung. / Proactive supply-chain artefacts: rejected as an unsupported scope expansion.

## Entscheidung 6: Evidence und Abschluss bleiben getrennte Phasen / Decision 6: Evidence and closeout remain separate phases

**Entscheidung / Decision**: Der normale Kandidat enthaelt einen vorbenannten `Pending`-Anker. Auf seinen Commit folgt nur der constitutionelle terminale Rename-Commit; dieser unveraenderliche Head wird gepusht, reviewt, exact-head validiert und gemergt. Nach Fast-forward-Sync entsteht genau `codex/001-programmquellen-baseline-closeout` von synchronisiertem `main`. Sein einziger Commit aendert exakt Tasks, schema-1.1-Run-State und Causal Evidence, wird durch `causal-closeout` validiert und beendet T066 lokal. Spaetere Push-/Review-/Check-/Merge-/Cleanup-Fakten dieses Closeout-Commits werden extern berichtet und nicht selbstreferenziell in ihn geschrieben. / The normal candidate includes a pre-named Pending anchor and is followed only by the terminal rename commit. After that immutable feature head is merged and main is synchronized, exactly one pre-named three-path closeout commit persists completion. Its later publication facts are reported externally.

**Begruendung / Rationale**: Ein Persistenzcommit auf dem Feature-Branch wuerde den reviewten Head invalidieren; uncommittete Post-Merge-Aenderungen liessen `main` schmutzig. Die getrennte Drei-Pfad-Transaktion bindet nur bereits wahre Feature-Merge-, Sync- und Validierungsfakten und kann selbst unveraendert publiziert werden. / A feature-branch persistence commit would invalidate the reviewed head, while uncommitted post-merge changes would dirty main. The separate transaction binds only already true facts and can itself be published unchanged.

**Gepruefte Alternativen / Alternatives considered**:

- Evidence oder Remote-Abschluss in Plan vorziehen: verworfen, weil die behauptete Umsetzung noch nicht existiert. / Pulling evidence or remote closeout into planning: rejected because implementation does not yet exist.
- Tasks und State nach dem terminalen Rename auf dem Feature-Branch committen: verworfen, weil dadurch der unveraenderliche Feature-Head verloren ginge. / Committing tasks and state on the feature branch after the terminal rename: rejected because it would mutate the immutable feature head.
- Closeout-Publikationsfakten im eigenen Closeout-Commit speichern: verworfen als unloesbare Selbstreferenz. / Recording closeout publication facts inside their own commit was rejected as self-reference.

## Aufgeloeste Unbekannte / Resolved Unknowns

- Externe Schnittstelle: keine Produkt-API; ein Repository-Pruefvertrag ist nuetzlich und ausreichend. / External interface: no product API; a repository validation contract is useful and sufficient.
- Runtime und Dependencies: `N/A`; keine Auswahl. / Runtime and dependencies: `N/A`; no selection.
- Produktarchitektur: `N/A`; keine Struktur- oder Trust-Grenze aendert sich. / Product architecture: `N/A`; no structural or trust boundary changes.
- Teststrategie: vorhandene Dokument-/Governance-Validatoren plus semantischer Review; keine Produkttests. / Test strategy: existing documentation/governance validators plus semantic review; no product tests.
- Statistik: nach abgeschlossener Implementierung schreiben, danach read-only gegenpruefen. / Statistics: write after implementation, then verify read-only.
- AEPS: nach wesentlicher Umsetzung genau ein Finding-Pfad oder begruendetes No-change-Receipt; keine Promotion. / AEPS: after material implementation, either a finding path or a justified no-change receipt; no promotion.
- Globales Gate vor Implement: Der aktuelle nicht-supersedierte Review-Leaf jedes der 14 aktiven Ziele wird zusammen mit Zielhash, Receipt und beiden Receipt-/Review-Oberflaechen neu geprueft. / Before Implement, every current leaf, target hash, receipt, and both receipt/review surfaces are revalidated.

## Entscheidung 7: Historische Akzeptanz als unveraenderlicher Programmevidence-Snapshot / Decision 7: Historical Acceptance as an Immutable Programme Evidence Snapshot

**Entscheidung / Decision**: Schema 1.1 bewahrt den bestehenden META-LH-01-Lifecycle-Datensatz und ergaenzt genau einen geordneten 14-Ziel-Snapshot. Er bindet keine Commit-SHAs oder Zukunftsfakten, sondern nur Zielpfad/Normalhash sowie aktuelle eindeutige Receipt-/Ready-Review-Pfade und deren Rohhashes zum bereits bestandenen `GlobalReadyBeforeImplement`. Nur der exakte Run-State `Implement`/`Active`/`GlobalReadyBeforeImplement` mit passender Run-ID, Branch- und Lifecycle-Bindung darf den Snapshot statt erneuter Receipt-Quellenfrische verwenden; beide Review-Oberflaechen bleiben aktiv. / Schema 1.1 preserves the existing record and adds exactly one ordered fourteen-target snapshot. Only the exact qualified Implement state may use it instead of rechecking receipt source freshness, while both review surfaces continue.

**Begruendung / Rationale**: Alle 14 unveraenderlichen Receipts binden den damals aktuellen gemeinsamen `source-pack.md`; META-LH-05 bindet zusaetzlich `coverage-matrix.md` und `review-findings-ledger.md`. META-LH-01 durfte diese gemeinsamen Baselines danach aendern. Eine erneute Quellenfrische prueft deshalb Implementierungsevolution statt historische Akzeptanz; Receipt-Rewriting wuerde den akzeptierten Snapshot zerstoeren. / All immutable receipts bind the formerly current shared baseline, which META-LH-01 was authorised to evolve. Rechecking source freshness would test later implementation evolution rather than historical acceptance, while rewriting receipts would destroy the accepted snapshot.

**Gepruefte Alternativen / Alternatives considered**:

- Nur META-LH-01 ausnehmen: verworfen, weil alle 14 Receipts den gemeinsamen Source Pack binden und META-LH-05 zwei weitere geaenderte Baselines bindet. / Exempting only META-LH-01 was rejected because all fourteen receipts share the affected source and META-LH-05 binds two more.
- Receipts oder Reviews neu schreiben: verworfen, weil die historische akzeptierte Evidence unveraenderlich bleiben muss und keine Content-Rewrite-Autoritaet besteht. / Rewriting receipts or reviews was rejected because accepted historical evidence must remain immutable and no content-rewrite authority exists.
- Receipt-Frische allgemein deaktivieren: verworfen; vor Implement und in jedem nicht exakt qualifizierten State bleibt sie fail-closed verpflichtend. / Disabling receipt freshness generally was rejected; it remains mandatory before Implement and in every unqualified state.
