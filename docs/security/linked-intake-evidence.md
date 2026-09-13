# Sicherheit verlinkter Intake-Evidence / Linked Intake Evidence Security

## Umfang und Vertrauensgrenze / Scope and trust boundary

Der AOC-Renderer liest das repositorylokale Phase-2-Manifest, vorhandene
Intake- und Feature-Abschlussnachweise und erzeugt zwei Markdown-Ansichten. Er
ändert weder Produktcode noch Netzwerk-, Authentifizierungs-, Cloud- oder
Deploymentgrenzen. Manifestwerte bleiben Daten und werden nie als Befehle
ausgeführt.

*The AOC renderer reads the repository-local phase-2 manifest, existing intake
and feature-completion evidence, and generates two Markdown views. It changes
no product code or network, authentication, cloud, or deployment boundary.
Manifest values remain data and are never executed as commands.*

## STRIDE, CIA und Kontrollen / STRIDE, CIA, and controls

| Risiko | CIA-Bezug | Kontrolle und Evidence |
|---|---|---|
| Spoofing: ähnlich benannte gestempelte Datei wird gewählt | Integrität | Nur genau ein Kandidat ist zulässig; dessen `specs/<stamp>/autonomous-run-state.json` muss den logischen oder aufgelösten Pfad als `acceptedArtifact` belegen. |
| Tampering: Quelle ändert sich während der Veröffentlichung | Integrität | Vollständiger Eingabefingerprint, Recheck vor Replace und atomarer Multi-Output-Rollback. |
| Repudiation: einzelne Kanten oder Proofs verschwinden in einem Summenpass | Integrität/Nachvollziehbarkeit | Fünf Felder, jede direkte Kante und jeder Feature-Proof werden einzeln gerendert und durch gemeinsame Fixtures geprüft. |
| Information Disclosure: Pfade, Credentials oder Stackdaten gelangen in Fehler | Vertraulichkeit | Sichere repositoryrelative Subjects, redigierte unsichere Werte und bilinguale `LIE001`–`LIE012`-Diagnosen. |
| Denial of Service: ungültige Daten erzeugen Teiloutputs | Verfügbarkeit/Integrität | Fail-closed vor Publication; Kandidaten zuerst; vollständiger Rollback. |
| Elevation of Privilege: Eingabewert wird als Option oder Code interpretiert | Integrität | Kein `eval`, kein `Invoke-Expression`; gequotete Pfade und `--`-Grenzen. |

Die drei historischen logischen META-LH-01/02/03-Pfade werden ausschließlich
auf ihre jeweils eine lokal vorhandene featuregestempelte Datei aufgelöst.
Manifest und Lifecycle bleiben unverändert. Fehlende, mehrdeutige, außerhalb
des Repositorys liegende oder nicht durch den Feature-Abschluss belegte Ziele
stoppen vor einem Write.

*The three historical logical META-LH-01/02/03 paths resolve only to their one
locally present feature-stamped file. The manifest and lifecycle remain
unchanged. Missing, ambiguous, escaping, or unproven targets stop before a
write.*

## Governance-Disposition

| Standard/Familie | Status | Begründung / Trigger |
|---|---|---|
| MSL-Kontext; Bash; PowerShell 7 | Applicable, erfüllt | Produktkontext bleibt MSL; sichere Shellregeln, Strict Mode und gepaarte Tests. Trigger: Sprach-/Runtimewechsel. |
| NIST SSDF; CWE Top 25; STRIDE/CIA; CAPEC | Applicable, erfüllt | Eingabe-, Pfad-, Proof-, Ausgabe- und Diagnosegrenzen sind getestet. Trigger: neue Trust Boundary. |
| OWASP SAMM | Applicable, erfüllt | Requirements, Implementierung und Verification sind nachvollziehbar verbunden. Trigger: Prozess-/Reviewmodell ändert sich. |
| OWASP ASVS | N/A / Not Assessed | Keine Web-, API-, Auth- oder Sessionfläche. Trigger: eine solche Fläche tritt in Scope. |
| SBOM; VEX; AI-SBOM; SLSA; OpenSSF Scorecard | N/A / Not Assessed | Keine neue Dependency, Runtime-, Release- oder Supply-Chain-Auswahl. Trigger: entsprechender Diff. |
| Zero Trust; BSI C3A; BSI C5 | N/A / Not Assessed | Keine Netzwerk-, Cloud- oder Remote-Access-Grenze. Trigger: Service-/Cloudscope. |
| NIS2; CRA; EU AI Act; DORA | N/A / Not Assessed | Keine neue Markt-, AI-System- oder regulierte Produktentscheidung. Trigger: regulierter Lieferumfang. |
| Secure Development Assurance v0.1.3 | Applicable als unveränderter Validatorvertrag; Produkt/Image N/A / Not Assessed | `aoc-assurance-v013` und `training` bleiben unverändert. Trigger: Kontext-, Preset-, Produkt- oder Imageänderung. |

Der Diff fügt keine Paket-, Lock-, Projekt- oder Dependency-Datei hinzu. Owner
ist der AOC Repository Owner; Reviewer ist die Security-/Architecture-Rolle des
Feature-032-Slices. Restrisiko bis zur Lieferung: native Linux-/Windows-Parität
und unabhängiger PR-Review. Re-Evaluation bei Eingabe-, Prozess-, Dependency-,
Netzwerk-, Produkt- oder Trust-Boundary-Änderung.


## Ergänzende Series-Evidence / Additional series evidence

Der lesende META-LH-04-Prüfadapter besitzt einen eigenen [Security-Review](series-eligibility.md). Seine Guard-/Sanitization- und No-start-Belege stammen aus Feature 004; die obigen Rendererbelege werden nicht als Prüfer-Pass übernommen. / *The read-only META-LH-04 adapter has its own security review. Its guard, sanitization and no-start evidence comes from feature 004; renderer evidence above is not reused as an adapter pass.*
