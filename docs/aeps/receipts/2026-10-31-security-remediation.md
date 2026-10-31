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
`da91bf6014b22275be7b2779c6649802f96b7b18`.
Der dritte Standardscan `6d06f2fb-3793-4ed8-bb01-0de02426a963` auf
`d2914d0709993a95e0f2a7a7ead40224e67621dd` meldete drei mittlere
Befunde bei teilweiser Abdeckung. Dry-run-Vorrang und Worker-Ressourcenlimits
werden in einem weiteren lokalen Patch korrigiert; die Trennung der
Worker-Rechte bleibt vor Veröffentlichung offen. / The third Standard scan
reported three medium findings with partial coverage. A further local patch
addresses dry-run precedence and worker resource limits; worker authority
separation remains open before publication.
Der anschliessende lokale Diff-Scan `88561811-ce37-4bc3-93fa-53b8f27faba2`
fand einen weiteren bedingten Laufzeitfehler in der Log-Behandlung; der
Koordinator beendet jetzt auch bei Log-Fehlern den betroffenen Worker und ein
gezielter Fixture-Lauf prueft diesen Pfad. / The subsequent local diff scan
found one conditional log-handling runtime issue. The coordinator now stops
the affected worker on log errors, with a targeted fixture covering that path.
Der Standardscan `14b56679-c0a1-4375-96d7-bc59b131f92b` auf
`eae3590e4f37f651574a256ffc8b106ce16b7313` bestaetigte die offene
Worker-Rechtetrennung und zwei weitere Ressourcenpfade. Profilbefehle und
Ausgabekanaele nach Worker-Ende erhalten nun begrenzte Wartezeiten; gezielte
Fixtures pruefen beide Pfade. / The Standard scan confirmed the open worker
authority boundary and two further resource paths. Profile commands and
post-exit output streams now have bounded waits, covered by focused fixtures.
Der Repository Owner hat die temporaere Fail-Closed-Sperre fuer alle
produktiven Parallel-Kampagnen gewaehlt. `Start`, `Resume` und `Consolidate`
werden vor dem ersten Unterprozess abgewiesen. Deterministische Tests laufen
mit einer temporaeren Skriptkopie ohne Produktionsschalter. Die eigentliche
Isolation bleibt ein spaeteres, gesondert zu validierendes Arbeitspaket. /
The repository owner selected a temporary fail-closed suspension for all
production parallel campaigns. Start, resume and consolidation are rejected
before the first subprocess. Deterministic tests use a temporary script copy
with no production switch. Actual isolation needs separate validation.
Der Diff-Scan `e2f695f8-5c81-4424-8cea-ef421a9e8cf3` bestaetigte die
Produktionssperre ohne neuen Befund. Der anschliessende Standardscan
`8f3becfa-621f-4575-bceb-2a5a14f3d69e` auf `e2c1bff383a8` fand bei
teilweiser Repository-Abdeckung eine weitere mittlere Beobachtung zur
Bindung des Forgejo/Codeberg-Remote-Ziels. Die lokale Korrektur prueft nun
`origin`, Provider-Basis und Repository-Identitaet gemeinsam und zeigt das
vollstaendige Ziel vor einer Loeschung an. / The diff scan found no new issue
in the production suspension. The following Standard scan found one medium
remote-target binding issue under partial repository coverage. The local fix
binds origin, provider base and repository identity and displays the complete
target before deletion.
Der Forgejo-Diff-Scan `867ce36d-2a6c-4b74-a265-9d58b472464e` meldete
keinen weiteren Befund. Der Standardscan
`2c6ebc9a-22c1-4963-a7ea-9fd995adfdb3` auf `16296d30fdbb` fand bei
teilweiser Repository-Abdeckung eine niedrige lokale Ressourcenluecke in
der Lernpaket-ZIP-Pruefung. Der aktuelle Patch begrenzt das ZIP-Verzeichnis
und zaehlt Eintraege vor der vollstaendigen Parser-Materialisierung; beide
Plattformen nutzen dieselbe Vorpruefung. / The Forgejo diff scan reported no
further issue. The Standard scan found one low-severity local resource issue
under partial repository coverage. The current patch bounds ZIP directory
metadata and counts entries before full parser materialization on both
platforms.
Publikationsstand:
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
Diese Korrekturen und ihre erneute Prüfung wurden fortgesetzt; der folgende
Standardscan meldete noch die lokale ZIP-Ressourcengrenze.
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
remediation and recheck continued; a following Standard scan reported the
local ZIP resource boundary. Focused tests support the
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
und Standardscan des zweiten Patches sind abgeschlossen. Die finale
Veröffentlichung steht noch aus.
Der ZIP-Patch bestand 16 fokussierte Python-Grenztests sowie beide
Paketpruefer-Selbsttests. Ein Test mit 20.001 Eintraegen bestaetigt die
Abweisung vor Dateiliste und Extraktion. Beide Plattformen lehnen ein
uebergrosses Sparse-Archiv vor dem Hashen ab; Steuerzeichen in Eintragsnamen
koennen die Bash-Pflichtdateipruefung nicht mehr verfälschen. Finaler
Standardscan und Publikation dieses letzten Patches stehen noch aus.
Der ZIP-Diff-Scan `476d44a2-c46f-4148-8073-447b6d426afd` pruefte alle
drei geaenderten ausfuehrbaren Dateien ohne neuen Befund. Finaler
Standardscan und Publikation stehen noch aus.

*The ZIP patch passed 16 focused Python boundary tests and both package-checker
self-tests. A 20,001-entry test confirms rejection before listing and
extraction. Both platforms reject an oversized sparse archive before hashing;
control characters in entry names no longer spoof Bash required-file checks.
The ZIP diff scan `476d44a2-c46f-4148-8073-447b6d426afd` covered all three
changed executable files without a new finding. The final Standard scan and
publication remain pending.*

*Focused tests and static checks passed. Three broad fleet tests could not use
`ps` in this sandbox. The parallel coordinator and model-routing suites passed.
The Windows junction check used simulated attributes; native NTFS validation
remains open. The second patch passed focused boundary, package, teardown,
coordinator, static-analysis and clean-checkout Gitleaks checks. Diff and
Standard scans of that patch completed; final scanning and publication of the
ZIP patch remain pending at receipt time.*

Documentation Impact: `UpdateRequired`. Quelle: privater Scan und lokaler
Patch; Owner: AOC Repository Owner. Aktualisiert wurden
`docs/man/maintain-workspace-storage.1.md`, die generierte
`docs/scripts/reference.md`, die Parallel-Runner-Dokumentation, die
Verteilungsmanifeste, die Paketpruefer-Hilfe in Bash und PowerShell, dieses
Receipt und das AEPS-Ledger. Die
öffentlichen Dokumente enthalten keine Ausnutzungsdetails.

*Documentation Impact is `UpdateRequired`: the storage manual, generated script
reference, parallel runner guide, distribution manifests, package-checker help,
this receipt and
the AEPS ledger describe changed behavior and verification without publishing
exploit details.*
