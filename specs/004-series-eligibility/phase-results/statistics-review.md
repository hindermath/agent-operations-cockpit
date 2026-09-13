# Statistikprüfung / Statistics Review

## Aktueller Stand nach T040 / Current state after T040

Der [Checkpoint-Audit](delivery-set.json) bindet die fünf abgeschlossenen Grenzen T008/T016/T022/T031/T040, zwölf reale Commits, exakte Index-/Commit- und Ledgerhashes. Die sechs Quellencommits und sechs Statistik-only-Commits sind getrennt. Der T040-Receipt ist autoritativ und wird unverändert im Audit aufgenommen; seine Checkbox wird für den nächsten Quellencheckpoint veröffentlicht. HEAD ist `e0172f6dd4aad214cfaa40ec66cf268514a04b23`; Renderer-Quellrevision bleibt die gesondert belegte `0372f899d24e282d3ec552cb7d818f7ee4db1534`.
*The audit binds five completed checkpoints and twelve real commits with exact tree/blob/ledger hashes. Six source and six statistics-only commits remain separate. T040 is authoritative and preserved; its checkbox is prepared for the next source checkpoint. HEAD differs from the recorded renderer source revision.*

T040 belegt beide Homogeneity-Oberflächen mit 100 %. Profil 2, Methodik v2, 80/125 Zeilen/Tag, 7.8 Stunden, 21.5 Tage, ASCII/100-Spalten, chronologische Einträge und letzter Gesamtabschnitt bleiben unverändert. In T041–T045 wird kein Renderer ausgeführt. Das neue Restdelta benötigt bei T046 einen zusätzlichen vollständigen Quellen-/Statistikcheckpoint; historische Passes bestehen nicht automatisch diesen späteren Stand.
*T040 records both homogeneity checks at 100 percent with unchanged methodology and layout. No renderer runs in T041–T045. The new residual set needs a full additional T046 checkpoint; historical passes do not certify that future revision.*

## Historischer T008-Abbruch / Historical T008 Stop

Der folgende frühere Bericht bleibt historischer Negativnachweis und ist durch die oben gebundene Checkpoint-Historie abgelöst; seine damaligen Stop-Aussagen sind kein aktueller Arbeitsauftrag.
*The earlier report below remains negative history, superseded by the actual checkpoint history above; its former next action is not current.*


### T008: Blockierte Abschlussgrenze / Blocked boundary

Hilfe beider Renderer gelesen und bytegleiche Vorschauen geprüft (je Exit 0). Der einzige Schreibversuch wurde mit Exit 1 abgewiesen; es wurde kein Ledger gerendert. Beide anschließenden Check-only-Läufe melden DRIFT/1. T008 bleibt offen und sperrt T009. / *Both helps and identical previews passed. The sole write attempt was rejected with exit 1; no ledger was rendered. Both subsequent check-only commands report DRIFT/1. T008 remains incomplete and blocks T009.*

Der Renderer verlangt einen sauberen Arbeitsbaum (`scripts/render-project-statistics.ps1:1246-1250`): "Writing requires a clean working tree. Commit or stash existing changes first." Die akzeptierten Änderungen sind uncommitted; T046/T047 erlauben den Liefercommit erst nach T008 und den weiteren Tasks. Der Renderer hat keinen Dirty-Tree-Parameter. Direkte Blockübernahme, Guard-Änderung oder fremde Git-Projektion würden die aktuelle Pflicht nicht belegen. / *The renderer requires a clean worktree while accepted changes are uncommitted and delivery staging/commit follows T008. There is no dirty-tree parameter. Copying the generated block, modifying the guard or using a different Git projection would not prove the current mandatory procedure.*

[Exakte Befehle, Ausgaben und Exits](statistics-t008.json). Git-HEAD `e5083c82d80099901774518b3987f47a1a628572`; Renderer-Quellrevision `f33f161a24d5` ist der letzte relevante Nicht-Merge-Commit gemäß Methodik v2. / *The execution record binds exact commands, output and exits. Git HEAD and the renderer's last relevant non-merge source revision are distinct.*

Profil 2, Methodik v2, Konfiguration und Basis 80/125 bleiben unverändert. Ungetrackte Feature-Dateien sind noch nicht Teil der Git-Textbasis. Keine erfundenen Phasenwerte für Setup oder Planung. Nächste sichere Aktion: Der koordinierende Runner muss die kausale Reihenfolge für einen sauberen Renderer-Stand mit exakter Commitprüfung klären und neu validieren, bevor T008 wiederholt wird. / *Profile, methodology, configuration and reference values remain unchanged; untracked feature files are excluded from the Git text base. Invent no setup or planning volume. The coordinator must resolve and revalidate a causal clean-renderer/commit sequence before retrying T008.*
