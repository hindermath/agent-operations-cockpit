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
| `AEPS-FIND-AOC-006` Cross-Cutting Applicability | `CAND-AEPS-10`, `CAND-AEPS-11` | Security, A11Y, Cross-Platform, Architecture | Partial | Requirements-Evidence ist noch keine Produkt- oder Cross-Project-Evidence / requirements evidence is not product or cross-project evidence |
| `AEPS-FIND-AOC-007` Evidence Invalidation | `CAND-AEPS-05`, `CAND-AEPS-08` | Intake Update, Repair, Review, Sequencing | Gap | Kein presetübergreifender Evidence-Abhängigkeitsgraph / no cross-preset evidence dependency graph |
| `AEPS-FIND-AOC-008` Ownership Graph | `CAND-AEPS-05` | Intake Sequencing; lokaler Portfoliovertrag / local portfolio contract | Covered for AOC | Cross-Project-Kompatibilität und komplexe Parallelserie fehlen / cross-project compatibility and complex parallel series missing |
| `AEPS-FIND-AOC-009` Reproducible Evidence | `CAND-AEPS-02`, `CAND-AEPS-08` | Intake Authoring, Intake Review | Partial | Keine projektneutrale Pfad-/Command-Abstraktion / no project-neutral path and command abstraction |
| `AEPS-FIND-AOC-010` Semantic Language Review | `CAND-AEPS-11` | A11Y Governance, Intake Review | Partial | Kein wiederholter unabhängiger Cross-Project-Review / no repeated independent cross-project review |
| `AEPS-FIND-AOC-011` Ready Non-Authority | `CAND-AEPS-01`, `CAND-AEPS-06`, `CAND-AEPS-07` | Intake Review, Autonomous Run | Partial | Technische Stop-Evidence vom Review bis Runtime fehlt / technical stop evidence from review to runtime missing |
| `AEPS-FIND-AOC-012` Product Decisions | kein Preset-Kandidat / no preset candidate | Intake Repair nur für Prozessgrenze / process boundary only | AOC-specific | Technologieinhalt bleibt bei RAW-01/02 / technology content remains product-owned |
| `AEPS-FIND-AOC-013` Parallel Eligibility | `CAND-AEPS-05`, `CAND-AEPS-07` | Intake Sequencing, Parallel Autonomous Run, Intake Review | Partial | Keine Cross-Project- oder Runtime-Preflight-Evidence / no cross-project or runtime-preflight evidence |
| `AEPS-FIND-AOC-014` Wave Re-Entry | möglicher Ausbau von `CAND-AEPS-04`, `CAND-AEPS-08` | Intake Authoring, Intake Sequencing, Intake Repair | Partial | Lokale Verify-/Partial-/Collision-Fixtures bestehen; Cross-Project- und Runtime-Recovery-Evidence fehlen |

## Abgleich mit den zwölf Upstream-Kandidaten / Coverage of the twelve upstream candidates

| Upstream-Kandidat | Neue AOC-Evidence / new AOC evidence | Bewertung / assessment |
|---|---|---|
| `CAND-AEPS-01` Development Readiness | Findings 003 und 011 | fail-closed Authority-Grenze gestärkt / strengthened |
| `CAND-AEPS-02` Findings Coverage | Finding 009 | reproduzierbare Artefakt- und Command-Bindung ergänzt / added |
| `CAND-AEPS-03` Level-2-Handoff | Phase-2-Completion-Receipt, RF-15 und RF-21 | bereits ausreichend als AOC Pilot Pattern erfasst / already captured |
| `CAND-AEPS-04` Meta-Lastenhefte | META-LH-01 bis META-LH-05 Ready; Finding 014 | fünf Meta-Verträge Ready; Wave-Re-Entry lokal als Pilot Pattern belegt / five Ready, local pilot evidence exists |
| `CAND-AEPS-05` Ownership/DAG | Findings 007, 008 und 013 | Doppelowner-, Zyklus-, Shared-Write- und Shared-Decision-Evidence gestärkt / strengthened |
| `CAND-AEPS-06` Decision Gate | Findings 002, 011 und RAW-IADs | Preservation belegt; erster Specify-Lauf weiterhin offen / preservation proven, Specify still open |
| `CAND-AEPS-07` Autonomie-Modi | Findings 001, 003, 011 und 013 | neun Eligibility-Achsen sowie Review-/Authority-Trennung reproduzierbar präzisiert / reproducibly refined |
| `CAND-AEPS-08` Receipts | Findings 002, 005, 007, 009 und 014 | Lineage-, Quellenrollen-, Reproduzierbarkeits- und Re-Entry-Lücken sichtbar / gaps exposed |
| `CAND-AEPS-09` Maintenance Sync | AOC-Issue #4, PRs #5/#6 gemäß #196 | keine neue Evidence aus den fünf Ready-Reviews / no new evidence here |
| `CAND-AEPS-10` Public Readiness | Finding 006 und Phase-2-Receipt | Requirements-Evidence ergänzt, zweites Projekt fehlt / second project missing |
| `CAND-AEPS-11` A11Y/CEFR/DE-EN | Findings 006 und 010 | wiederkehrende Review-Evidence vorhanden, UI-Evidence fehlt / UI evidence missing |
| `CAND-AEPS-12` Engineering Sessions | Verweis in #196 auf ES-2026-07-30-AOC-01 | keine neue Session-Retrieval-Evidence / no new evidence |

## Reifegrenze / Maturity boundary

Kein Matrixeintrag hebt einen Kandidaten auf `Stable` oder `Canonical`.
`cross-project-validated` bleibt für alle AOC-only-Ergebnisse gesperrt. /
*No matrix row promotes a candidate to Stable or Canonical. Cross-project
validated remains unavailable for AOC-only evidence.*
