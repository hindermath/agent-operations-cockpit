# Finding-to-Preset-Candidate-Matrix / Finding-to-Preset Candidate Matrix

## Zweck / Purpose

Diese Matrix ordnet die initialen AOC-Findings bestehenden AEPS-Kandidaten und
installierten Governance-Presets zu. Eine Zuordnung ist keine Promotion und
keine Aussage, dass das Preset die Beobachtung bereits vollständig löst. /
*This matrix maps initial AOC findings to existing AEPS candidates and
installed governance presets. A mapping is neither promotion nor proof that a
preset already resolves the observation completely.*

## Zuordnung / Mapping

| AOC-Finding | Upstream-Kandidat / upstream candidate | Bestehende Presets / existing presets | Abdeckung / coverage | Restlücke / residual gap |
|---|---|---|---|---|
| `AEPS-FIND-AOC-001` Ready versus Lifecycle | `CAND-AEPS-07` | Intake Review, Intake Sequencing, Autonomous Run | Partial | Kein gemeinsamer maschinenlesbarer Ready-to-Eligibility-Vertrag / no shared machine-readable contract |
| `AEPS-FIND-AOC-002` Bounded Repair | `CAND-AEPS-06`, `CAND-AEPS-08` | Intake Repair, Intake Authoring, Intake Review | Partial | Geschützte fachliche Felder besitzen keine Cross-Project-Fixture / no cross-project protected-field fixture |
| `AEPS-FIND-AOC-003` Historic Authority | `CAND-AEPS-01`, `CAND-AEPS-07` | Autonomous Run, Parallel Autonomous Run, Intake Authoring | Partial | Keine Ende-zu-Ende-Provider-Evidence / no end-to-end provider evidence |
| `AEPS-FIND-AOC-004` Prompt-State Marker | möglicher neuer Kandidat / possible new candidate | Intake Authoring, Intake Review | Gap | Zustandsmarker und erklärende Dokumentation sind nicht formal getrennt / state marker and explanatory text are not formally separated |
| `AEPS-FIND-AOC-005` Secret Fixture Role | `CAND-AEPS-08` | Intake Authoring, Security Governance | Partial | Keine portable Rollen-Taxonomie für Provenienz und Test-Evidence / no portable role taxonomy |
| `AEPS-FIND-AOC-006` Cross-Cutting Applicability | `CAND-AEPS-10`, `CAND-AEPS-11` | Security, A11Y, Cross-Platform, Architecture | Partial | Portabler Python-Fallback ist lokal geprüft; Produkt- und Cross-Project-Evidence fehlen / portable Python fallback is locally proven; product and cross-project evidence are missing |
| `AEPS-FIND-AOC-007` Evidence Invalidation | `CAND-AEPS-05`, `CAND-AEPS-08` | Intake Update, Repair, Review, Sequencing | Gap | Kein presetübergreifender Evidence-Abhängigkeitsgraph / no cross-preset evidence dependency graph |
| `AEPS-FIND-AOC-008` Ownership Graph | `CAND-AEPS-05` | Intake Sequencing; lokaler Portfoliovertrag / local portfolio contract | Covered for AOC | Cross-Project-Kompatibilität und komplexe Parallelserie fehlen / cross-project compatibility and complex parallel series missing |
| `AEPS-FIND-AOC-009` Reproducible Evidence | `CAND-AEPS-02`, `CAND-AEPS-08` | Intake Authoring, Intake Review | Partial | Keine projektneutrale Pfad-/Command-Abstraktion / no project-neutral path and command abstraction |
| `AEPS-FIND-AOC-010` Semantic Language Review | `CAND-AEPS-11` | A11Y Governance, Intake Review | Partial | Unabhängiges Copilot-Follow-up bestätigt lokale Erkennbarkeit; Cross-Project-Review fehlt / independent Copilot follow-up confirms local detection; cross-project review is missing |
| `AEPS-FIND-AOC-011` Ready and Portfolio Non-Authority | `CAND-AEPS-01`, `CAND-AEPS-06`, `CAND-AEPS-07` | Intake Review, Intake Sequencing, Autonomous Run | Partial | AOC-weites 14er-Gate ist textuell gebunden; technische Stop- und Cross-Project-Evidence fehlen / AOC-wide fourteen-intake gate is textually bound; technical stop and cross-project evidence are missing |
| `AEPS-FIND-AOC-012` Product Decisions | kein Preset-Kandidat / no preset candidate | Intake Repair nur für Prozessgrenze / process boundary only | AOC-specific | Technologieinhalt bleibt bei RAW-01/02 / technology content remains product-owned |
| `AEPS-FIND-AOC-013` Parallel Eligibility | `CAND-AEPS-05`, `CAND-AEPS-07` | Intake Sequencing, Parallel Autonomous Run, Intake Review | Partial | Vertragsgetriebener lokaler Validator besteht; Cross-Project- und Runtime-Preflight-Evidence fehlen / contract-driven local validator passes; cross-project and runtime-preflight evidence are missing |
| `AEPS-FIND-AOC-014` Wave Re-Entry | möglicher Ausbau von `CAND-AEPS-04`, `CAND-AEPS-08` | Intake Authoring, Intake Sequencing, Intake Repair | Partial | Lokale Verify-/Partial-/Collision-Fixtures bestehen; Cross-Project- und Runtime-Recovery-Evidence fehlen |
| `AEPS-FIND-AOC-015` Receipt Decision Parity | `CAND-AEPS-06`, `CAND-AEPS-08` | Intake Authoring, Intake Review | Gap | Manuelle Reparatur und Ready-Re-Review belegen die gewünschte Parität; Hash-/Schema-Validatoren erkennen Widersprüche weiterhin nicht automatisch. / Manual repair and Ready re-review prove the desired parity; hash and schema validators still do not detect conflicts automatically. |
| `AEPS-FIND-AOC-016` Disjunkte N/A-Gate-Form | `CAND-AEPS-08` | Autonomous Run | Gap | Feature-lokaler Fix und Negativprobe liegen vor; der generische Validator akzeptiert weiterhin N/A mit Ausfuehrungstokens. / A feature-local fix and negative probe exist; the generic validator still accepts N/A with execution tokens. |
| `AEPS-FIND-AOC-017` Dauerhafte Closeout-Evidence | `CAND-AEPS-02`, `CAND-AEPS-08` | Autonomous Run | Gap | Terminaler State und Remote-Checks bestehen, aber neun lokale Pass-Ausgaben sind nur ueber verschwundene Temp-Pfade referenziert. / Terminal state and remote checks pass, but nine local passing outputs are referenced only through vanished temporary paths. |
| `AEPS-FIND-AOC-018` Konsumentenweite Lifecycle-Aufloesung | `CAND-AEPS-05`, `CAND-AEPS-08` | Intake Authoring, Intake Review, Intake Sequencing, Autonomous Run | Gap | Feature-lokale Archivauflösung besteht; beide generischen Governance-Oberflaechen blockieren den migrierten Pfad mit RIG014. / Feature-local archive resolution passes; both generic governance surfaces block the migrated path with RIG014. |

## Abgleich mit den zwölf Upstream-Kandidaten / Coverage of the twelve upstream candidates

| Upstream-Kandidat | Neue AOC-Evidence / new AOC evidence | Bewertung / assessment |
|---|---|---|
| `CAND-AEPS-01` Development Readiness | Findings 003 und 011 | fail-closed Authority-Grenze gestärkt / strengthened |
| `CAND-AEPS-02` Findings Coverage | Findings 009 und 017 | reproduzierbare Artefakt-, Command- und Dauerhaftigkeitsbindung ergänzt / reproducible artifact, command, and durability binding added |
| `CAND-AEPS-03` Level-2-Handoff | Phase-2-Completion-Receipt, RF-15 und RF-21 | bereits ausreichend als AOC Pilot Pattern erfasst / already captured |
| `CAND-AEPS-04` Meta-Lastenhefte | META-LH-01 bis META-LH-05 Ready; Finding 014 | fünf Meta-Verträge Ready; Wave-Re-Entry lokal als Pilot Pattern belegt / five Ready, local pilot evidence exists |
| `CAND-AEPS-05` Ownership/DAG | Findings 007, 008, 013 und 018 | Doppelowner-, Zyklus-, Shared-Write-, Shared-Decision- und Lifecycle-Aufloesungsevidence gestärkt / strengthened with lifecycle-resolution evidence |
| `CAND-AEPS-06` Decision Gate | Findings 002, 011, 015 und RAW-IADs | Preservation und manuell reviewte Receipt-Parität belegt; automatische Paritätsprüfung und erster Specify-Lauf bleiben offen. / Preservation and manually reviewed Receipt parity are proven; automated parity validation and the first Specify run remain open. |
| `CAND-AEPS-07` Autonomie-Modi | Findings 001, 003, 011 und 013 | neun Eligibility-Achsen sowie Review-/Authority-Trennung reproduzierbar präzisiert / reproducibly refined |
| `CAND-AEPS-08` Receipts | Findings 002, 005, 007, 009, 014 bis 018 | Lineage-, Quellenrollen-, Reproduzierbarkeits-, N/A-, Dauerhaftigkeits- und Lifecycle-Luecken sichtbar / lineage, evidence-role, reproducibility, N/A, durability, and lifecycle gaps exposed |
| `CAND-AEPS-09` Maintenance Sync | AOC-Issue #4, PRs #5/#6 gemäß #196 | keine neue Evidence aus den fünf Ready-Reviews / no new evidence here |
| `CAND-AEPS-10` Public Readiness | Finding 006 und Phase-2-Receipt | Requirements-Evidence ergänzt, zweites Projekt fehlt / second project missing |
| `CAND-AEPS-11` A11Y/CEFR/DE-EN | Findings 006 und 010 | wiederkehrende Review-Evidence vorhanden, UI-Evidence fehlt / UI evidence missing |
| `CAND-AEPS-12` Engineering Sessions | Verweis in #196 auf ES-2026-07-30-AOC-01 | keine neue Session-Retrieval-Evidence / no new evidence |

## Reifegrenze / Maturity boundary

Kein Matrixeintrag hebt einen Kandidaten auf `Stable` oder `Canonical`.
`cross-project-validated` bleibt für alle AOC-only-Ergebnisse gesperrt. /
*No matrix row promotes a candidate to Stable or Canonical. Cross-project
validated remains unavailable for AOC-only evidence.*
