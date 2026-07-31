# Beitragen / Contributing

Danke für Dein Interesse am Agent Operations Cockpit. Das Projekt befindet sich
in einer requirements-first Phase: Lastenhefte, Entscheidungen, Evidence und
Governance werden vor Produktcode erstellt und geprüft.

## Vor einem Beitrag

1. Lies `README.md`, `constitution.md`, `AGENTS.md` und `SECURITY.md`.
2. Prüfe, ob ein bestehendes Lastenheft oder ein Decision Intake den Concern
   bereits besitzt. Ein Concern darf genau eine kanonische Owner-Reihe haben.
3. Erstelle keine Produktimplementierung aus einem Meta-Lastenheft. Dafür ist
   eine später ausdrücklich freigegebene fachliche Spezifikation erforderlich.
4. Verwende Deutsch zuerst und Englisch danach, CEFR B2 sowie WCAG 2.2 AA für
   anwendbare Inhalte. Erkläre Fachbegriffe beim ersten relevanten Auftreten.
5. Nimm keine Geheimnisse, persönlichen lokalen Pfade, private Registry-Daten
   oder nicht redistribuierbare Inhalte auf.

## Änderungen prüfen

Führe mindestens den Homogenitäts- und Secret-Scan aus. Sobald freigegebener
Produktcode vorhanden ist, sind zusätzlich Restore, Build und Tests Pflicht.
Dokumentiere für jede Änderung genau eine Documentation-Impact-Entscheidung:
`UpdateRequired`, `NoUpdateRequired`, `GeneratedUpdate` oder `FollowUp`.

Kleine, klar begrenzte Pull Requests sind bevorzugt. Beschreibe Zweck, Scope,
Akzeptanzkriterien, positive und negative Evidence, Restrisiken und bewusst
nicht geänderte Bereiche. Ein grüner Automatismus ersetzt kein fachliches oder
sicherheitsbezogenes Review.

*Thank you for your interest in Agent Operations Cockpit. The project is in a
requirements-first phase: requirements, decisions, evidence, and governance
are authored and reviewed before product code.*

*Before contributing, read the repository guidance, verify the single canonical
owner series for the concern, and do not derive product implementation directly
from a meta requirement. Use German first and English second, CEFR B2, and WCAG
2.2 AA where applicable. Do not include secrets, personal local paths, private
registry data, or non-redistributable material.*

*Run at least the homogeneity and secret scans. Once approved product code
exists, restore, build, and tests are mandatory. Record exactly one
Documentation Impact decision for every change. Pull requests should state
purpose, scope, acceptance criteria, positive and negative evidence, residual
risk, and intentionally unchanged areas. Green automation does not replace
domain or security review.*
