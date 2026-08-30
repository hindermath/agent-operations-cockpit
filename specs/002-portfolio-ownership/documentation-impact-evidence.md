# Dokumentationsauswirkung / Documentation Impact

## Entscheidung / Decision

`UpdateRequired`

Die lesbare Portfolio-Uebersicht enthielt fuer `C-05` bis `C-09` veraltete
oder vermischte Decision-Darstellungen. Die aktuelle Aussage wird im selben
Feature korrigiert und mit dem archivbewussten Lifecycle sowie den Review- und
Liefernachweisen gemeinsam validiert. / *The readable portfolio overview held
stale or mixed decision presentations in C-05 through C-09. This feature
corrects the current statement and validates it together with lifecycle,
review, and delivery evidence.*

## Quelle, Owner und Dokumentinventar / Source, owner, and document inventory

- Kanonische fachliche Quelle / canonical domain source:
  `requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.md`,
  hashgebunden durch das aktuelle Authoring Receipt und Ready-Single-Review. /
  *The active intake is hash-bound by the current receipt and Ready review.*
- Fach-Owner / domain owner: Portfolio Owner; Dokumentations-Owner /
  documentation owner: AOC Documentation Owner; Reviewer: unabhaengige
  Documentation-, First-reader-, A11Y-/Sprach- und Public-Content-Rollen. /
  *Independent documentation, first-reader, accessibility/language, and public
  content reviewers provide separate proof classes.*
- Primaeres Aktualisierungsziel / primary update target:
  `requirements/baseline/portfolio-ownership.md`, ausschliesslich die
  Decision-Zellen `C-05` bis `C-09`.
- Validation-only, ohne nachgewiesene Drift unveraendert / unchanged absent
  proven drift: `requirements/baseline/portfolio-ownership.json`,
  `docs/decisions/open-decisions.md` und
  `specs/intake-review-fixtures/meta-lh-02/*`.
- Feature-Evidence / feature evidence: Implementierungscheckliste,
  First-reader-, Accessibility-/Sprach-, Security-/Privacy- und autonome
  Evidence unter `specs/002-portfolio-ownership/` sowie das AEPS-Receipt. /
  *The feature-local evidence set and AEPS receipt record review and delivery
  proof.*
- Lifecycle-Ableitung / lifecycle derivation:
  `specs/002-portfolio-ownership/intake-lifecycle.json` bindet Original- und
  Archivpfad. Nach normalem Merge wechselt exakt
  `requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.md`
  byteidentisch nach
  `requirements/intakes/active/Lastenheft_META-LH-02-Portfolio-Ownership.002-portfolio-ownership.md`.
  Der Pfadwechsel aendert keine fachliche Aussage. / *The later byte-identical
  path transition changes no domain statement.*
- Generierte Ableitungen / generated derivations: `docs/project-statistics.md`
  wird nach dem AEPS-Ergebnis aus `docs/project-statistics.config.json` und
  Git-Historie gerendert. Fuer T079 kommt konditional genau
  `docs/scripts/embedded-scripts.md` hinzu, weil der in-scope Feature-002-
  Skriptbestand das Embedded-Inventar aendert. Dieser Pfad wird ausschliesslich
  nach Bash-`--dry-run` und PowerShell-`-WhatIf` mit
  `render-script-reference.*` erzeugt und durch beide Check-only-Peers
  validiert; `docs/scripts/reference.md` bleibt unveraendert. Keine der beiden
  Ableitungen ist eine unabhaengige Source of Truth und keine wird
  hand-editiert. / *Statistics and the conditionally triggered embedded-script
  inventory remain renderer-owned outputs; the canonical script reference
  stays unchanged.*

## Zielgruppen und Leserpfad / Audiences and reader path

Zielgruppen sind Portfolio-Owner, nachgelagerte RAW-Teams, Maintainer,
KI-Agenten, Reviewer und Auszubildende ab dem ersten Ausbildungsjahr. Der
Leserpfad ist: / *Audiences include domain owners, downstream teams,
maintainers, AI agents, reviewers, and first-year apprentices. The reader path
is:*

1. Einstieg und Begriffe / entry and terms: `spec.md` und
   `requirements/baseline/glossary.md`.
2. Lesbare Ownership-, Decision- und Handoff-Sicht / readable ownership,
   decision, and handoff view: `requirements/baseline/portfolio-ownership.md`.
3. Vertiefung / detail: beschreibende Links zum Maschinenvertrag und zur
   Decision Map. / *Descriptive links lead to the machine contract and
   Decision Map.*
4. Pruefung / verification: sechs Bash-/PowerShell-Laeufe und die getrennten
   Review-Evidence-Dateien.
5. Naechste sichere Aktion / next safe action: bei Owner-, Handoff-, Decision-
   oder Hashdrift nachgelagerte Arbeit fail-closed stoppen und gegen die
   kanonischen Quellen neu validieren. / *Stop downstream work fail closed and
   revalidate canonical sources on drift.*

Kein neuer globaler Einstieg ist erforderlich: `spec.md` verlinkt das
Glossar; die Portfolio-Uebersicht verlinkt Vertrag und Decision Map; das
Glossar fuehrt zu den Authority- und Stop-Gates. Die bestehende progressive
Offenlegung bleibt geschlossen und beschreibend. / *No new global entry point
is needed because the existing progressive-disclosure links already connect
terms, portfolio, contract, decisions, and stop gates.*

Der Link- und Kontexttest am Implementierungsstand hat die folgenden fünf vom
feature-lokalen Evidence-Hub ausgehenden repository-relativen Leserpfade
einzeln auf vorhandenes Ziel und beschreibenden Linktext geprüft: die
[Feature-Spezifikation](spec.md), die
[lesbare Portfolio-Übersicht](../../requirements/baseline/portfolio-ownership.md),
den [maschinenprüfbaren Portfoliovertrag](../../requirements/baseline/portfolio-ownership.json),
die [Decision Map mit offenen und bestätigten Entscheidungen](../../docs/decisions/open-decisions.md)
und das [zweisprachige Glossar](../../requirements/baseline/glossary.md).
Alle fünf Prüfungen bestanden. Es wird ausdrücklich keine bidirektionale
Verlinkung der kanonischen Zielartefakte behauptet: Der Feature-Hub liefert
den Rückkehr- und Prüfungskontext, während die Portfolio-Übersicht bereits zu
Vertrag und Decision Map führt. Ein neuer globaler Einstieg würde diesen
progressiven Pfad duplizieren und ist deshalb nicht erforderlich. / *The
implementation check verified all five outgoing repository-relative targets
and descriptive labels. It does not claim that every canonical target links
back; the feature evidence hub supplies return and verification context. A new
global entry point would duplicate this progressive path.*

## Dokumentklasse, Sprache, Plattform und Distribution / Document class, language, platform, and distribution

- Dokumentklasse / document class: Level-2 Governance- und
  Requirements-Dokumentation mit auditierbarer Delivery-Evidence; keine
  Produkt- oder Runtime-Dokumentation. / *Level-2 governance and requirements
  documentation, not product/runtime documentation.*
- Sprache / language: kurze Dokumente inline DE-first/EN-second, etwa CEFR B2;
  kein separater Sprachpartner erforderlich. Begriffe werden beim Erstgebrauch
  erklaert oder im zweisprachigen Glossar vertieft. / *Short files remain
  inline bilingual at approximately CEFR B2; no companion file is needed.*
- Plattform- und Beispielnachweis / platform and example proof: text-first
  Markdown auf macOS, Linux und Windows; vorhandene Bash- und PowerShell-Peers
  liefern dieselben positiven und negativen Ergebnisse. Kein Produktbeispiel
  ist anwendbar. / *Text-first Markdown is cross-platform and paired validators
  produce equivalent outcomes; no product example applies.*
- Distribution: repository-intern auf dem Default-Branch `main`; kein Build-,
  Installations-, Deployment- oder Release-Artefakt. / *Repository-local on
  main; no build, install, deployment, or release artefact.*
- Home Sync: `N/A`. Dieses Level-2-Feature aendert weder Level 0 noch eine
  Home-Runtime-Kopie und fuehrt keinen Sync aus. / *No Level-0 or home-runtime
  copy is changed or synchronized.*

## Validierung, Review und Neubewertung / Validation, review, and re-evaluation

Evidence sind der fokussierte Fuenf-Zellen-Diff, unveraenderte Hashes der
validation-only Quellen, sechs aktuelle Portfolio-Laeufe, First-reader `6/6`,
separate A11Y-/Sprach- und Public-Content-Reviews, Secret-Musterchecks,
Documentation- und Governance-Review, der Lifecycle-/R100-Nachweis, AEPS vor
Statistik, exakte Stage, CI/Review-Konvergenz sowie kausales PostMerge. /
*Evidence spans the focused diff, unchanged validation sources, six current
runs, separate human reviews, security scans, lifecycle proof, ordered AEPS
and statistics, exact stage, CI/review convergence, and causal post-merge
proof.*

Neu zu bewerten ist bei Concern-, Owner-, Handoff-, Decision-, Pfad-, Hash-,
A11Y-, Sprach-, Security-, Review-, Receipt-, Series-, CI-, Head- oder
Authority-Drift. Kein Ergebnis erteilt Produkt-, RAW-, Level-0-, Preset-,
Remote-, Merge-, Bypass- oder Provider-Administration-Authority. /
*Re-evaluate on any named drift. No documentation result grants product, RAW,
Level-0, preset, remote, merge, bypass, or provider-administration authority.*
