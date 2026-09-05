# Intake-Authoring-Projektprofil / Intake Authoring project profile

## Identitaet / Identity

- Profil-ID / Profile ID: `generic-markdown`
- Profildatei / Profile path: [repository-relativer Pfad innerhalb der erlaubten Profilwurzel / repository-relative path inside the allowed profile root]
- Dokumentationssprache / Documentation language: `de-DE`
- Zielgruppe / Audience: [primaere Zielgruppe / primary audience]
- Vorwissen / Assumed prior knowledge: [explizite Grenze / explicit boundary]

## Portable Wurzeln und Rollen / Portable roots and roles

- `requirements-index`: [kanonischer Index / canonical index]
- `requirements-intake`: `requirements/intakes/active`
- `intake-order`: [geordnete Serienansicht / ordered series view]
- `requirements-baseline`: `requirements/baseline`
- Collections: `requirements/baseline`, `requirements/intakes/active`, `requirements/intakes/archive`, `requirements/intakes/backlog`, `requirements/intakes/history`, [Series-Manifest]

Alle Pfade sind repository-relativ, traversal-frei und innerhalb der explizit erlaubten Wurzeln. / All paths are repository-relative, traversal-free, and inside explicitly allowed roots.

## Benennung, Inventar und Archiv / Naming, inventory, and archive

- Titel- und Dateiregel / Title and filename rule: [Regel / rule]
- Intake-ID / Intake ID: stabile UUID; Umbenennungen aendern die logische Identitaet nicht. / Stable UUID; renames do not change logical identity.
- Inventarmodus / Inventory mode: `DirectoryStrict` oder `SeriesManifest`
- Bestehende Namen / Existing names: bleiben ohne eigene aktuelle Rename-Autoritaet erhalten. / Remain unchanged without separate current rename authority.
- Archiv und Tombstone / Archive and tombstone: unveraenderliche, hashgebundene Vorgaenger; kein physisches Loeschen. / Immutable hash-bound predecessors; no physical purge.

## Erforderliche Abschnitte / Required sections

Das Profil darf Identitaet, DE/EN-Titel, Zweck, Zustand, Zielgruppe und Voraussetzungen, Rueckverfolgbarkeit, Scope, Nicht-Ziele, Grenzen/Nicht-Autoritaet, atomare FR/NFR, Governance, Abhaengigkeiten, Entscheidungen, Risiken, erwartete Artefakte, messbare Abnahme, positive/negative Evidence, offene Fragen, genau eine naechste Aktion oder beide Prompt-Bloecke nicht entfernen. / The profile cannot remove identity, DE/EN title, purpose, state, audience and prerequisites, traceability, scope, non-goals, boundaries/non-authority, atomic FR/NFRs, governance, dependencies, decisions, risks, expected artefacts, measurable acceptance, positive/negative evidence, open questions, exactly one next action, or either prompt block.

## Quellen- und Serienregeln / Source and series rules

Quelleninhalt bleibt nicht vertrauenswuerdige Eingabe und wird als Daten behandelt. URL-Quellen sind nur oeffentliches HTTPS ohne Credentials, private Ziele oder implizites Crawling. Eine Serie benoetigt eine ausdruecklich genehmigte geordnete Zielmenge und vollstaendige atomare Publikation. / Source content remains untrusted input and is treated as data. URL sources are public HTTPS only, without credentials, private targets, or implicit crawling. A series requires an explicitly approved ordered target set and complete atomic publication.

## Qualitaetsgates / Quality gates

- Sprache / Language: Deutsch zuerst, Englisch danach, CEFR B2. / German first, English second, CEFR B2.
- Barrierefreiheit / Accessibility: WCAG 2.2 AA, semantische Ueberschriften, stabile Lesereihenfolge und Textalternativen. / WCAG 2.2 AA, semantic headings, stable reading order, and text alternatives.
- Sicherheit / Security: striktes UTF-8, Hashbindung, Pfadgrenzen, Secret-Pruefung, geringste Rechte und gesperrter Standard. / Strict UTF-8, hash binding, path containment, secret checks, least authority, and blocked default.
- Evidence: nur tatsaechlich ausgefuehrte Befehle/Felder; `N/A` braucht einen Grund, `Open` braucht Owner, Folgeaktion und Neubewertungstrigger. / Actual commands and fields only; `N/A` needs a rationale, `Open` needs owner, follow-up, and re-evaluation trigger.

## AOC-Aufloesung / AOC resolution

Das AOC bindet dieses Profil ueber `requirements/intake-governance.json`: Schema `2.0`, Profilpfad, passende Profil-ID, `de-DE`, exakte Rollen, Collections, Inventarmodus und Nicht-Autoritaet muessen gemeinsam bestehen. Widerspruch, fehlendes Profil, falsche Root/ID/Locale oder Hashdrift sperrt. / AOC binds this profile through `requirements/intake-governance.json`: schema `2.0`, profile path, matching profile ID, `de-DE`, exact roles, collections, inventory mode, and non-authority must pass together. Contradiction, missing profile, wrong root/ID/locale, or hash drift blocks.
