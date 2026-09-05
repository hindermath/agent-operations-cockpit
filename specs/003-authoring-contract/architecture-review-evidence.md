# Architektur- und iSAQB-Review / Architecture and iSAQB review

## Ergebnis / Outcome

Der additive Vertrag erweitert die bestehende Governance-Schicht, ohne
Produktarchitektur oder Laufzeitkomponenten einzuführen. Die R1-Historie bleibt
unveränderlich; der Dispatcher akzeptiert entweder den eingefrorenen R1-Hash
oder die vollständige R2-Metadatenbindung und weist Mischzustände ab. / *The
additive contract extends the existing governance layer without adding product
architecture or runtime components. R1 stays immutable; the dispatcher accepts
either its frozen hash or the complete R2 metadata binding and rejects mixed
states.*

| Prüffeld / Checkpoint | Status | Evidence oder Begründung / Evidence or reason |
|---|---|---|
| Architekturziele und Qualitätsziele / Architecture and quality goals | Pass | Reproduzierbarkeit, Integrität, Plattformparität, Verständlichkeit und fail-closed Authority sind in Spec, Plan und fünf kanonischen Artefakten messbar. |
| Kontext und Trust Boundaries | Pass | Benutzer-Authority, Repositorydateien, untrusted sources, Git/GitHub und runner-externe Gate-Evidence sind getrennte Grenzen. |
| Schichten und Schnittstellen / Layers and interfaces | Pass | Template -> Receipt/Operation -> additive Validator -> Global-Ready-Dispatcher -> CI/Gates; Bash und PowerShell teilen Exitklassen. |
| Views und Datenfluss / Views and data flow | Pass | `current-evidence-binding.json` ist die Current-Projection; Reparatur-Manifest, R1-Archive und R2-Review bilden getrennte historische und aktuelle Sichten. |
| CIA | Pass | Confidentiality: Secret-/private-path rejection; Integrity: SHA-256 und exact sets; Availability: keine Produktlaufzeit betroffen. |
| STRIDE und CAPEC | Pass | Spoofing/Tampering durch UUID-, Hash-, Path- und Approval-Bindung; Injection durch data-only-Verarbeitung; Repudiation durch Receipts/Review. Nicht anwendbare Netzwerkangriffe bleiben `N/A`. |
| Qualitätsszenarien / Quality scenarios | Pass | R1-Hash wählt historischen Checker; vollständige R2-Metadaten wählen additiven Checker; unbekannt/mixed/ambiguous stoppt; Drift in Proposal, Archiv oder Zielmenge stoppt. |
| Fail-safe defaults | Pass | Nur `Completed` ist Operationserfolg; nur `Ready` ohne Findings/Risiken qualifiziert R2; jeder Auswahlfehler stoppt. |
| Risiken und technische Schuld / Risks and technical debt | Open | Owner: AOC-Maintainer. Follow-up: veröffentlichte Drei-Runner- und GitHub-Gate-Evidence nach Wiederherstellung des `.git`-Schreibzugriffs. Trigger: schreibfähige Git-Metadaten und pushbarer Kandidat. |
| ADR/S-ADR und arc42 | N/A | Keine neue Produktarchitekturentscheidung; der akzeptierte Designvertrag ist die feature-lokale Entscheidungsevidence. Re-Evaluation bei neuer Komponente oder Trust Boundary. |
| Zero Trust | Pass | Kein gespeicherter historischer Grant wird als aktuelle Authority übernommen; jede Boundary wird mit aktueller Evidence und Hash erneut geprüft. |
| BSI C3A/C5 | N/A | Kein Cloud-Service oder Betreiberkontrollsystem wird geändert; Re-Evaluation bei Cloud- oder Provider-Scope. |
| Threat Model | N/A | Kein neuer ausführbarer Datenpfad; anwendbare Threats sind in den Security-/Negativtests abgedeckt. Formales Modell bei Produkt- oder Netzwerkpfad neu bewerten. |
| Cloud-Autonomie / Cloud autonomy | N/A | Kein Provider- oder Cloud-Admin-Scope; Remote-Lieferung bleibt normales GitHub MergeAndSync ohne Bypass. |
| Separater `docs/architecture/`-Nachweis | N/A | Die akzeptierte Allowlist bindet das Feature-Review hier; kein Architektur-Baseline-Artefakt ist betroffen. Re-Evaluation bei Produktarchitekturänderung. |
