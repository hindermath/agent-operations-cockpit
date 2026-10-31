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
Der Standardscan `37db3488-1f94-4647-af97-6f509ba160b1` auf `7115df7c1aee`
meldete bei teilweiser Repository-Abdeckung eine weitere niedrige Beobachtung
zur Groessengrenze der SHA-256-Begleitdatei. Der lokale Patch liest diese Datei
nun begrenzt und bewahrt die erzeugten ASCII- sowie bisher akzeptierten
BOM-kodierten Formate. / The Standard scan found one further low-severity
checksum-sidecar resource issue under partial repository coverage. The local
patch bounds that input and preserves generated ASCII and previously accepted
BOM-encoded formats.

*Focused tests and static checks passed. Three broad fleet tests could not use
`ps` in this sandbox. The parallel coordinator and model-routing suites passed.
The Windows junction check used simulated attributes; native NTFS validation
remains open. The second patch passed focused boundary, package, teardown,
coordinator, static-analysis and clean-checkout Gitleaks checks. Diff and
Standard scans of that patch completed; final scanning and publication of the
ZIP patch remain pending at receipt time.*
Der Sidecar-Patch bestand 19 fokussierte Python-Grenztests, beide
Paketpruefer-Selbsttests und den PowerShell-Analyselauf fuer 124 Dateien.
Die erneuten Diff- und Standardscans sowie die Publikation stehen noch aus. /
The sidecar patch passed 19 focused Python boundary tests, both package-checker
self-tests, and PowerShell analysis over 124 files. Its repeat diff and Standard
scans and publication remain pending.
Der Sidecar-Diff-Scan `d49920da-f89b-42d6-9fae-30e543313805` pruefte alle
drei geaenderten ausfuehrbaren Dateien ohne weiteren Befund. Der finale
Standardscan und die Publikation stehen noch aus. / The sidecar diff scan
covered all three changed executable files without a further finding. The
final Standard scan and publication remain pending.

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

Der Standardscan `70eece36-f626-4b26-b8c1-713d8dbc5bee` auf `8f44da7`
meldete bei teilweiser Repository-Abdeckung einen weiteren niedrigen Befund
am Lernpaket-Freigabegate. Beide Paketierer und beide Paketpruefer verlangen
nun einen erfolgreichen Secret-Scan des fertigen Stagings beziehungsweise
entpackten Pakets; nur nach Zeilenendennormalisierung hashgebundene
Lehrbeispiele bleiben zugelassen.
Vorschauen erzeugen weiterhin keine Pakete. 22 gezielte
Python-Grenztests, beide Paket-Selbsttests und der Skriptreferenz-Check
bestanden. Die erneuten Diff- und Standardscans sowie die Publikation stehen
zum Zeitpunkt dieses Eintrags noch aus. Documentation Impact bleibt
`UpdateRequired`: Skripthilfe und dieses Receipt beschreiben die geaenderte
Voraussetzung. Keine neue AEPS-Evidence oder Preset-Promotion: Die lokale
Korrektur allein belegt keine projektuebergreifende Wiederverwendung.

*The Standard scan found one further low-severity learning-package release
gate issue under partial repository coverage. Both producers and checkers now
require a successful secret scan of the staged or extracted package. Only
reviewed teaching examples bound by a line-ending-normalized hash remain
accepted; previews remain
non-writing. Twenty-two focused Python boundary tests, both package
self-tests and the script-reference check passed. Repeat diff and Standard
scans and publication remain pending at this entry. Documentation Impact stays
`UpdateRequired` for the command help and this receipt. No new AEPS evidence or
preset promotion follows from this local fix.*

Der Diff-Scan `851cf6aa-cc89-43ba-a4da-d5d4c13edea4` pruefte alle sechs
geaenderten ausfuehrbaren beziehungsweise Konfigurationsdateien und fand
einen weiteren niedrigen Umgehungspfad im Paket-Freigabegate. Der gemeinsame
Pruefer wurde korrigiert; ein negativer Test mit synthetischem Testwert
bestaetigt die Sperre. Der erneute Diff-Scan und der abschliessende
Standardscan folgen. Keine neue AEPS-Evidence oder Upstream-Aktion.

*The diff scan reviewed all six changed executable or configuration files and
found one further low-severity bypass in the package release gate. The shared
checker was corrected; a synthetic negative test confirms rejection. Repeat
diff and final Standard scans follow. No new AEPS evidence or upstream action.*

Der erneute Diff-Scan `6c045932-b070-4f03-b2fe-7e2296fc5b2c` meldete
keinen weiteren Befund. Der Standardscan
`6fae3ae3-5030-4628-8e64-93cea84f0228` auf `4b1d8e3` fand bei
teilweiser Abdeckung drei weitere Beobachtungen zu Secret-Scan, ZIP-Pruefung
und Paket-Staging. Die lokale Korrektur entfernt eine pauschale
Dokument-Ausnahme, bindet gepruefte Beispiele an Datei-Hashes, begrenzt
Archivpfade auch fuer Windows und schliesst Git-Metadaten im Staging aus.
24 gezielte Grenztests und ein Secret-Scan des sauberen getrackten
Repository-Snapshots bestanden. Native Windows-Pruefung und abschliessende
Diff- und Standardscans folgen. Documentation Impact: `UpdateRequired`;
Quelle: privater Scan und lokaler Patch; Owner: AOC Repository Owner;
aktualisiert wurden die CI- und Hook-Pruefung sowie dieses Receipt. Keine
neue AEPS-Evidence oder Upstream-Aktion ohne projektuebergreifende
Validierung.

*The repeat diff scan reported no finding. The Standard scan on `4b1d8e3`
reported three more observations with partial coverage. The local change
narrows secret-scan exceptions to reviewed, content-bound examples, checks ZIP
paths for Windows as well, and excludes Git metadata from package staging.
Twenty-four focused boundary tests and a clean tracked-snapshot secret scan
passed. Native Windows validation and final diff and Standard scans follow.
Documentation Impact is `UpdateRequired`; the repository owner updated CI,
the hook, and this receipt. No new AEPS evidence or upstream action is claimed
without cross-project validation.*

Der Diff-Scan `55029bd8-8b75-4ca5-9ea5-92292cef6f4c` fand eine weitere
Windows-Namensvariante innerhalb der ZIP-Pruefung. Der Filter und die
Negativprobe decken jetzt auch diese reservierten Namen ab. / The diff scan
found another Windows name variant in ZIP validation. The filter and negative
fixture now cover these reserved names as well.

Der korrigierte Diff-Scan `665f170b-824a-4977-9273-ed3e1c2e5f9c` meldete
keinen Befund. Der Standardscan `709905cb-9c3e-4aad-92cf-498ae0353efb`
auf `066bd24` fand bei teilweiser Repository-Abdeckung drei weitere
Beobachtungen in Teardown- und Lernpaketgrenzen. Die lokale Korrektur bindet
alle Remote-Ziele einschliesslich des Zustands ohne Remote an die Vorschau,
begrenzt den Home-Artefakt-Commit, erzwingt angeforderte Backups vor
Loeschungen und schliesst Git-Metadaten unabhaengig von Grossschreibung aus
Lernpaketen aus. Isolierte Bash- und PowerShell-Proben bestaetigen die
Sperre geaenderter Remote-Ziele, den Backup-Abbruch, den begrenzten Commit
und die Paket-Ausschluesse. Documentation Impact: `UpdateRequired`;
Quelle: privater Scan und lokaler Patch; Owner: AOC Repository Owner;
aktualisiert wurden dieses Receipt und die betroffenen Skriptoberflaechen.
Es entsteht keine neue AEPS-Evidence fuer eine projektuebergreifende
Preset-Promotion. Finaler Diff- und Standardscan sowie Publikation folgen.

*The corrected diff scan reported no finding. The Standard scan on `066bd24`
reported three further observations under partial repository coverage. The
local fix binds every remote target, including no-remote state, to its preview;
limits the Home artifact commit; requires a successful requested backup before
deletion; and excludes Git metadata from learning packages regardless of case.
Isolated Bash and PowerShell fixtures confirm the target-change gate, backup
abort, limited commit and package exclusions. Documentation Impact is
`UpdateRequired`; this receipt and affected script surfaces were updated.
No new cross-project AEPS preset evidence or promotion is claimed. Final diff
and Standard scans and publication follow.*

Der Security-Diff-Scan `d22c6a52-2c73-4f2b-9bb4-9360f9768e2a` schloss
die acht geaenderten Dateien ohne neuen Befund ab. Der erneute Standardscan
`6fd94dbd-e21e-4fb6-9fbb-4d24c85f1f68` auf `3abcd65` bestaetigte zwei
weitere Teardown-Grenzen. Die nachfolgende Korrektur bricht bei nicht
pruefbaren Git-Metadaten ab und bindet angeforderte Backups an das ausgewaehlte
Verzeichnis. Die Agenten-Einstiege fuer produktive Parallel-Kampagnen nennen
jetzt einheitlich die bis zur Worker-Isolation geltende Sperre.
Documentation Impact: `UpdateRequired`; Quelle: lokaler Standardscan,
Owner: AOC Repository Owner; aktualisiert wurden Teardown-Skripte,
Regressionstests, Agenten-Einstiege, Preset-Dokumentation und dieses Receipt.
Es entsteht keine neue projektuebergreifende AEPS-Evidence.

*The diff scan closed eight changed files without a new finding. The Standard
scan on `3abcd65` confirmed two more teardown boundaries. The subsequent fix
stops when Git metadata cannot be inspected and binds requested backups to the
selected directory. Agent entry points now consistently state that production
parallel campaigns remain suspended until workers are isolated. Documentation
Impact is `UpdateRequired`; the teardown scripts, regression tests, agent
entry points, preset documentation and this receipt were updated. No new
cross-project AEPS evidence is claimed.*

Der Security-Diff-Scan `95f03408-71be-4c6d-953c-e90504e451d1` meldete
keinen neuen Befund. Der Standardscan `9647413e-e49c-43a6-bb53-119da1dc3371`
auf `a593830` identifizierte eine weitere PowerShell-Git-Pruefgrenze.
Die Korrektur erkennt Git-Worktrees mit `.git`-Datei, behandelt fehlgeschlagene
Git-Abfragen als Abbruchgrund und schliesst lokale Git-Historie ohne pruefbaren
Upstream in beiden Shells vom Standard-Teardown aus. Alle lokalen Branches
und Stash-Daten werden vor einer rekursiven Loeschung geprueft. `Force` bleibt
ein ausdruecklicher Override. Isolierte Regressionen pruefen diese Grenzen
sowie leere Git-Repositories und den vorgesehenen Override. Documentation Impact:
`UpdateRequired`; Quelle: privater lokaler Standardscan; Owner: AOC Repository
Owner; aktualisiert wurden Teardown-Skripte, Regressionstests und dieses
Receipt. Keine neue projektuebergreifende AEPS-Evidence.

*The diff scan reported no new finding. The Standard scan on `a593830`
identified another PowerShell Git-inspection boundary. The fix recognizes
Git worktree metadata files, aborts on failed Git inspection, and prevents
default teardown of local Git history without a verifiable upstream in both
shells. All local branches and stashed work are checked before recursive
deletion. Force remains an explicit override. Isolated regression checks cover
these boundaries, empty Git repositories, and the override. Documentation
Impact is `UpdateRequired`; the teardown scripts, regression tests and this
receipt were updated. No new cross-project AEPS evidence is claimed.*

Der Standardscan `26dd62d7-2453-4997-8f05-b42d0506fdd9` auf `555b9aa`
meldete bei teilweiser Repository-Abdeckung sechs weitere Teardown-Befunde.
Der lokale Patch behandelt eine fehlgeschlagene Level-2-Suche als Abbruch,
schuetzt auch ignorierte lokale Dateien, verlangt die GitLab-CLI fuer eine
angeforderte Remote-Loeschung und eine pruefbare Level-0-Quelle auch bei
`Force`. Fehler beim lokalen Loeschen und bei der Home-Artefakt-Bereinigung
beenden den Ablauf ohne falsche Erfolgsmeldung. Die Regressionen verwenden
isolierte temporaere Home-Verzeichnisse. Documentation Impact:
`UpdateRequired`; Quelle: privater Standardscan, Owner: AOC Repository Owner;
aktualisiert wurden Teardown-Skripte, Regressionstests und dieses Receipt.
Die neue Evidence ist projektspezifisch; keine AEPS-Promotion oder
Upstream-Aktion folgt daraus.

*The Standard scan on `555b9aa` reported six further teardown findings with
partial repository coverage. The local patch aborts on failed Level-2
discovery, protects ignored local files, requires the GitLab CLI for requested
remote deletion, and requires a resolvable Level-0 source even with `Force`.
Local deletion and Home artifact cleanup errors now stop without false success.
Regression tests use isolated temporary Home directories. Documentation Impact
is `UpdateRequired`; the teardown scripts, regression tests and this receipt
were updated. This evidence is project-specific and does not justify AEPS
promotion or an upstream action.*
