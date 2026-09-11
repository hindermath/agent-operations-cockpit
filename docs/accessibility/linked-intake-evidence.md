# Barrierearme verlinkte Intake-Evidence / Accessible Linked Intake Evidence

## Ergebnis und Prüfgrenze / Result and review boundary

Die beiden AOC-Reihenfolgeansichten, CLI-Hilfe und Referenzdiagnosen wurden am
11. September 2026 als Quelltext und linearer Text geprüft. Position, Status,
vollständiger Intake-Dateiname, direkte Kanten mit Art und Bindungsstatus sowie
Featurezustand bleiben ohne Farbe und räumliches Tabellenverständnis
erkennbar. Bash und PowerShell verwenden dieselben fünf linearen Referenzen und
dieselben zwölf bilingualen Diagnosefamilien.

*The two AOC order views, CLI help, and reference diagnostics were reviewed as
source and linear text on 11 September 2026. Position, status, complete intake
filename, direct edges with kind and binding, and feature state remain
available without colour or spatial table understanding. Bash and PowerShell
use the same five linear references and twelve bilingual diagnostic families.*

Dies ist eine macOS-Quelltext-/Linearisierungsprüfung. Ein konkreter
Screenreader oder eine Braille-Zeile wurde nicht bedient; native Linux- und
Windows-Evidence folgt im Delivery-Checkpoint. Diese Grenzen werden nicht als
erfüllt vorweggenommen.

## WCAG-2.2-AA-Disposition

| Kriterium | Anwendung | Nachweis / Grenze |
|---|---|---|
| 1.3.1 Information und Beziehungen | Stabile Überschrift und fünf Spalten; lineare Referenzen wiederholen die Feldnamen. | Paar-Fixtures; keine HTML-Behauptung. |
| 1.4.1 Farbe | Status und Gate-Bedeutung stehen als Text. | ANSI-/Farbsteuerung wird in Referenzen abgelehnt. |
| 2.1.1 Tastatur | Markdown und CLI benötigen keine Zeigeraktion. | Statische Textoberfläche; Webnavigation ist nicht im Scope. |
| 2.4.6 Überschriften und Beschriftungen | Bilinguale Überschrift und vollständige Linktexte benennen Zweck und Ziel. | Quellen- und Linkprüfung. |
| 3.1.2 Sprache von Teilen | Deutsch steht vor Englisch; technische Literale bleiben stabil. | `languageOrder: [de, en]`. |
| 3.3.1 Fehlererkennung | `LIE001`–`LIE012` benennen Fehlerfamilien textuell. | Zwölf eindeutige Fixturecodes. |
| 3.3.2 Beschriftungen/Anweisungen | Jede Referenzdiagnose enthält deutsche und englische Abhilfe. | Keine Credentials, privaten Roots oder Stackdaten. |

Eine Zeile wird in der Reihenfolge Position, Status, vollständiger Dateiname,
jede direkte Kante, Art, Bindungsstatus und Featurezustand gelesen. Der
renderer-eigene `<br>`-Separator trennt mehrere Kanten erst nach dem Escaping;
eingeschleuste Markup-Zeichen bleiben Daten.

## Agent-Parity-Disposition

Die Featurefunktion führt keine neue gemeinsame Agentenregel ein. Wegen der
bereits vorhandenen veralteten Presetreferenz wurde jedoch die operative
Versionsangabe `autonomous-run-governance` atomar in `AGENTS.md`, `CLAUDE.md`,
`GEMINI.md`, `.github/copilot-instructions.md` und
`.github/agents/copilot-instructions.md` auf die lokal installierte Version
0.4.1 berichtigt. Neue Projekttemplates, Routingregeln oder absichtliche
Abweichungen sind `N/A / Not Assessed`. Re-Evaluation bei neuer Bedien-,
Security-, A11Y-, Statistik-, Routing- oder Deliveryregel.

Owner: AOC Repository Owner. Reviewer: Feature-032 A11Y-/Agent-Parity-Rolle.
Restrisiko sind Unterschiede realer assistiver Konfigurationen. Re-Evaluation
bei Spalten-, Überschriften-, Link-, Sprach-, Diagnose-, HTML- oder
Interaktionsänderung.
