# AEPS-Receipt: Security-Remediation / Security remediation

Datum / Date: 2026-10-31. Owner: AOC Repository Owner und Security Owner.
Trigger: wesentliche Korrektur nach Standard Security Scan / material remediation after a standard security scan.
Quelle / Source: privater Codex Security Standard Scan
`e1869297-2c56-4b64-a0ac-623106348ad7` und abgeschlossener
Security-Diff-Scan `3f211200-83c9-48d7-a347-1bf934ca96a4`
(Bericht-SHA-256 `ba19740afdffd9f9a2257d72cfea01f49d5b8aea4d5a555b80b7d8ec434fb1e6`)
und erneutem Diff-Scan `c2447028-ce12-47b8-9dab-67bb5247f198`
(Bericht-SHA-256 `d76f5dec427ba4910366dde3a77b41f71ed8e28840be865d044ae975e8e8c38e`)
auf Base-HEAD `8e3c737e3fcba1ba8b0f338bebb135bf7339acaf` sowie Standardscan
`b93338e2-8497-45fa-9349-e515ac021e29` auf Commit
`58da765fd1fbe1ac8089ca441c1b6ac18000bea0`, Diff-Scan
`f94c7e70-9790-46b1-a165-aea0eccc3c27` auf dem zweiten Patch und erneutem
Standardscan `c04be6bb-61a9-4fae-95a1-06ae03cf86d4` auf Commit
`da91bf6014b22275be7b2779c6649802f96b7b18`. Publikationsstand:
`PendingPublication`; AEPS-Upstream:
`NotApplicable`. Deduplizierung: Scan-ID + Datum + Remediation-Receipt.

**Keine neue AEPS-Evidence / No new AEPS evidence.** Die lokalen Korrekturen
betreffen projektspezifische Eingabe-, Pfad-, Archiv- und Ausführungsgrenzen.
Der erste Diff-Scan meldete drei verbleibende Beobachtungen; sie wurden lokal
korrigiert und erneut unabhängig geprüft. Der zweite Diff-Scan prüfte alle 18
geänderten ausführbaren Dateien ohne Befund. Der nachfolgende Standardscan
meldete sieben weitere Befunde bei teilweiser Repository-Abdeckung. Diese wurden
in einem zweiten lokalen Patch bearbeitet; eine unabhängige Gegenprüfung fand
vier Umgehungen, die vor dem nächsten Scan korrigiert wurden. Der zweite
Diff-Scan meldete keinen Befund in 13 geänderten Dateien; der anschließende
Standardscan meldete zwei weitere Beobachtungen bei teilweiser Abdeckung.
Deren Korrektur und erneute Prüfung sind zum Zeitpunkt dieses Receipts offen.
Gezielte Tests belegen die lokale Korrektur, aber keine veröffentlichte
Cross-Project-Validierung
für ein wiederverwendbares Preset-Pattern. Bestehende Finding-IDs,
Reifegrade, Matrix, Gap-Analyse und Handoff bleiben unverändert. Es erfolgen
keine Promotion und keine Upstream-Aktion.

*The local changes address project-specific input, path, archive and execution
boundaries. The first diff scan reported three further observations, corrected
and independently reviewed locally. The second diff scan covered all 18
changed executable files without a finding. The subsequent Standard scan found
seven more issues with partial repository coverage. An independent review found
four bypasses in the second local patch, which were corrected before rechecking.
The second diff scan found no issue in 13 changed files; the next Standard scan
reported two further observations with partial repository coverage. Their
remediation and recheck remain open at receipt time. Focused tests support the
local remediation, but do not establish cross-project evidence
for a reusable preset pattern. Preserve existing findings, maturity, matrix,
gap analysis and handoff. No promotion or upstream action follows.*

Verifikation / Verification: 33 gezielte Python-Tests, beide Paketprüfer-
Selbsttests, der vollständige Parallel-Koordinator- und Model-Routing-Test, PowerShell-Parser,
PSScriptAnalyzer 1.25.0 für 123 Dateien, Bash-Syntax und Skriptreferenz-Check
bestanden. Die breite Flotten-Suite hat drei umgebungsbedingte Fehler, weil
die Sandbox `ps` sperrt. Der Windows-Junction-Test nutzt simulierte
Dateiattribute; ein nativer NTFS-Lauf steht aus. Die zweite Korrekturrunde
bestand bisher zwölf Python-Grenztests, beide Paket-Selbsttests, den Teardown-
Pfadtest, Koordinator- und Konsolidierungsfixtures, PSScriptAnalyzer für die
geänderten PowerShell-Skripte und Gitleaks auf einem sauberen Checkout. Diff-
und Standardscan des zweiten Patches sind abgeschlossen. Ein weiterer
Korrekturpatch sowie Veröffentlichung stehen zum Zeitpunkt dieses Receipts aus.

*Focused tests and static checks passed. Three broad fleet tests could not use
`ps` in this sandbox. The parallel coordinator and model-routing suites passed.
The Windows junction check used simulated attributes; native NTFS validation
remains open. The second patch passed focused boundary, package, teardown,
coordinator, static-analysis and clean-checkout Gitleaks checks. Diff and
Standard scans of that patch completed; another remediation patch and
publication remain pending at receipt time.*

Documentation Impact: `UpdateRequired`. Quelle: privater Scan und lokaler
Patch; Owner: AOC Repository Owner. Aktualisiert wurden
`docs/man/maintain-workspace-storage.1.md`, die generierte
`docs/scripts/reference.md`, dieses Receipt und das AEPS-Ledger. Die
öffentlichen Dokumente enthalten keine Ausnutzungsdetails.

*Documentation Impact is `UpdateRequired`: the storage manual, generated script
reference, this receipt and the AEPS ledger describe the changed behavior and
verification without publishing exploit details.*
