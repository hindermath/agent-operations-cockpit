# Feature-Spezifikation · RAW-01 Reference Agentic Workspace / Feature specification

**Feature** `005-reference-agentic-workspace`

**Erstellt / Created** 2026-11-27

**Status** Entwurf nach Clarify / Draft after Clarify

**Quelle / Input** [Aktiver RAW-01-Intake / Active RAW-01 intake](../../requirements/intakes/active/Lastenheft_RAW-01-Reference-Agentic-Workspace.md) · [Ready-Einzelreview / Ready Single review](../../docs/reviews/raw-01-reference-agentic-workspace-2026-11-27-dotnet11.md)

## Nutzungsszenarien und Prüfung / User scenarios and testing

DE: IT-Auszubildende ab dem ersten Lehrjahr und erfahrene Fachkräfte sollen
sehen können, welche registrierten Repositories und benötigten Werkzeuge an
einem bestimmten Ort verfügbar sind. **Discovery** bedeutet hier die lesende
Erkennung in ausdrücklich benannten Workspace-Wurzeln. Eine Wurzel ist ein
freigegebenes Startverzeichnis. Ein **Snapshot** ist eine Momentaufnahme
der belegten Beobachtungen. Grundkenntnisse in Git und Terminal reichen aus.

EN: First-year IT apprentices and experienced professionals need to see which
registered repositories and required tools are available in a given workspace.
**Discovery** means inspecting explicitly named workspace roots. A root is
an authorised starting directory. A **snapshot** is a point-in-time record
of supported observations. Basic Git and terminal knowledge is sufficient.

DE: CEFR B2 bezeichnet ein Sprachniveau für verständliche Fachtexte.
WCAG 2.2 AA bezeichnet die hier geltende Stufe der Richtlinien für
Barrierefreiheit, soweit ihre Kriterien auf den Text anwendbar sind.

EN: CEFR B2 is the target language level for understandable technical
writing. WCAG 2.2 AA is the accessibility standard used here wherever
its criteria apply to the text.

### US-1 · Workspace erfassen / Inspect a workspace (P1)

DE: Als Person, die einen Workspace prüft, möchte ich registrierte
Repositories und ihren Git-Zustand innerhalb der freigegebenen Wurzeln
erkennen. Ein verlässlicher Überblick ist Voraussetzung für jede spätere
Nutzung der Momentaufnahme. Die Prüfung ist mit einem vorbereiteten Workspace
und einem Vorher-Nachher-Vergleich unabhängig durchführbar.

EN: As a workspace reviewer, I want to identify registered repositories and
their Git state within authorised roots. A reliable inventory is the basis for
later use of the snapshot. A prepared workspace and a before-and-after
comparison make this journey independently testable.

1. Ein Lauf erfasst die Arbeitskopien von drei verschiedenen gültig
   gelisteten Repositories in freigegebenen Wurzeln sowie mindestens
   zwei gelistete Werkzeuge. Der Aufrufer sortiert
   beide Eingabelisten für den zweiten Lauf um. Bei gleichen beobachteten
   Fakten erscheinen die Arbeitskopie- und Werkzeugbeobachtungen in beiden
   Darstellungen in derselben Reihenfolge. Die Prüfumgebung belegt null
   Schreibzugriffe. / *A run observes working copies of three different
   validly listed repositories in authorised roots and at least two
   listed tools. For a second run,
   the caller reorders both input lists. With the same observed facts,
   both output views present working-copy and tool observations in the
   same order. The test environment verifies zero writes.*
2. Fehlt die Freigabe für die Wurzel einer Arbeitskopie oder für die Wurzel
   ihrer Git-Metadaten, meldet Discovery eine verständliche Ablehnung.
   Das nicht freigegebene Ziel bleibt ungelesen und sein Pfad erscheint
   in keiner Ausgabe. / *If either the working copy's root or its Git
   metadata root lacks authorisation, discovery reports a clear denial.
   It leaves the unauthorised target unread and omits its path from all output.*
3. Ein viertes Git-Repository liegt in einer freigegebenen Wurzel und fehlt
   in der übergebenen Liste. Discovery liest daraus keine Git-Metadaten und
   nimmt es nicht in die Momentaufnahme auf. / *A fourth Git repository lies
   in an authorised root and is absent from the supplied list. Discovery
   reads none of its Git metadata and omits it from the snapshot.*
4. Ein Arbeitsbaum ohne Änderungen sowie ein Arbeitsbaum mit ausschließlich
   ignorierten neuen Dateien ergeben jeweils `Clean`. Eine vorgemerkte
   Änderung, eine nicht vorgemerkte Änderung oder eine neue unignorierte
   Datei ergibt in jeweils einem separaten Prüffall `Dirty`. /
   *A working tree with no changes and a working tree with only new ignored
   files each yield Clean. A staged change, an unstaged change or a new
   unignored file each yields Dirty in a separate test case.*
5. Eine gelistete Arbeitskopie und ihre zugehörigen Git-Metadaten liegen in
   zwei ausdrücklich zum Lesen freigegebenen Wurzeln. Discovery liefert
   die erwarteten Git-Fakten der Arbeitskopie. Die Beobachtung bleibt ihrer
   eigenen Wurzel zugeordnet. / *A listed working copy and its associated
   Git metadata are in two explicitly read-authorised roots. Discovery
   reports the expected Git facts for the copy. The observation remains
   associated with the working copy's own root.*
6. Ein gelistetes Werkzeug ist im ausdrücklich freigegebenen Suchbereich
   für die aktuelle Umgebung als ausführbar erkennbar. Der Snapshot meldet
   es als verfügbar. Ein zweites Werkzeug, das nur außerhalb des
   freigegebenen Suchbereichs vorhanden ist, wird nicht als verfügbar
   gemeldet. Discovery startet keines der Werkzeuge. / *A listed tool is
   identifiable as executable for the current environment within the
   explicitly authorised search scope. The snapshot reports it as available.
   A second tool that exists only outside that scope is not reported as
   available. Discovery starts neither tool.*
7. Der Aufrufer übergibt eine leere Repository-Liste, mindestens ein
   Werkzeug und ausdrücklich freigegebene Wurzeln. Der Snapshot enthält
   die Werkzeugbeobachtungen. Discovery liest keine Git-Metadaten. /
   *The caller supplies an empty repository list, at least one tool and
   explicitly authorised roots. The snapshot contains the tool observations.
   Discovery reads no Git metadata.*
8. Eine Arbeitskopie liegt sowohl in einer äußeren als auch in einer
   inneren freigegebenen Wurzel. Der Listeneintrag benennt die äußere
   Wurzel als Bezugswurzel. Der Snapshot zeigt nur deren Kennung, auch
   wenn der Aufrufer die Reihenfolge der Wurzeln umkehrt. Die Ausgaben
   enthalten weder den Wurzelpfad noch den relativen Pfad der Arbeitskopie. /
   *A working copy is within both an outer and an inner authorised root.
   The list entry names the outer root as its reference root. The snapshot
   reports only that root's identifier, even when the caller reverses the
   order of the roots. Neither output exposes the root path or the working
   copy's relative path.*
9. Eine Arbeitskopie hat einen abgelösten HEAD. Bei einer anderen ist ein
   Branch mit dem Namen `Detached` aktiv. In beiden Ausgaben bleibt der
   Zustand `Detached` vom Branch-Namen `Detached` unterscheidbar. Der
   ermittelte HEAD-Commit bleibt sichtbar. / *One working copy has a detached
   HEAD. Another is on a branch named Detached. Both outputs distinguish
   the Detached state from the branch name Detached and show the observed
   HEAD commit.*
10. Ein Repository ist initialisiert, der Branch-Name ist bekannt und der
    erste Commit fehlt noch. Beide Ausgaben zeigen den Branch-Namen und
    `Unborn` als HEAD-Zustand. / *A repository has been initialised and
    has a known branch name with no first commit yet. Both outputs show
    the branch name and Unborn as the HEAD state.*
11. Zwei identische Listeneinträge benennen dieselbe Arbeitskopie.
    Discovery erfasst ihre Git-Metadaten einmal und gibt eine Beobachtung
    aus. Die Wiederholung erzeugt keinen Fehler. / *Two identical list
    entries name the same working copy. Discovery collects its Git
    metadata once and emits one observation. The repetition causes no error.*
12. Zwei verschiedene freigegebene Wurzeln tragen die Kennungen
    `Build-A` und `build-a`. Discovery erkennt sie auf allen
    Zielplattformen als verschiedene Kennungen. Beide Ausgaben behalten
    die jeweilige Schreibweise. / *Two different authorised roots have
    identifiers Build-A and build-a. Discovery treats them as distinct on
    every target platform. Both outputs preserve the supplied case.*

### US-2 · Momentaufnahme verstehen und weitergeben / Read and share a snapshot (P2)

DE: Als lesende Person oder nachgelagertes Werkzeug möchte ich dieselben
belegten Fakten aus der Konsole oder einer maschinenlesbaren Momentaufnahme
entnehmen. Damit kann ich Ergebnisse vergleichen und der richtigen Umgebung
zuordnen. Ein vorbereiteter Snapshot reicht als Eingabe für diese Prüfung.

EN: As a reader or downstream tool, I want the same supported facts from the
console and the machine-readable snapshot. I can then compare results and
attribute them to the correct environment. A prepared snapshot is sufficient
to test this journey.

1. Für denselben Snapshot liefern beide Darstellungen dieselben fachlichen
   Felder, Werte, Fehlerstatus und dieselbe Schemaversion. Die lesbare Ausgabe
   vermittelt Zustände durch Text und erklärt die Begriffe auf Deutsch und
   Englisch. / *For the same snapshot, both views expose the same domain fields,
   values, error states and schema version. The readable view conveys states
   in text and explains terms in German and English.*
2. Der Aufrufer übergibt für einen Host und seine Sandbox (isolierte
   Umgebung) verschiedene opake Kennungen. Die beiden Snapshots führen
   jeweils die Kennung ihrer Umgebung. Opak bedeutet, dass die Kennung
   keine persönlichen Merkmale offenlegt. Gibt der Aufrufer für zwei
   Arbeitskopien dieselbe datensparsame Repository-Kennung an, zeigen beide
   Beobachtungen diese Kennung und jeweils ihren eigenen Branch. /
   *The caller supplies distinct opaque identifiers for a host and its sandbox
   (isolated environment). Each snapshot carries its environment's identifier.
   An opaque identifier reveals no personal attributes.
   When the caller supplies the same data-minimised repository identifier for
   two working copies, both observations show that identifier and their own
   branch.*
3. Zwei Arbeitskopien desselben logischen Repositorys auf demselben Host
   haben unterschiedliche Arbeitskopie-Kennungen. Ändert sich der Branch
   oder HEAD einer Kopie zwischen zwei Snapshots, bleibt ihre Kennung
   gleich. / *Two working copies of the same logical repository on the same
   host have distinct working-copy identifiers. When a copy's branch or HEAD
   changes between two snapshots, its identifier stays the same.*
4. Host und Sandbox beobachten dieselbe eingebundene physische Arbeitskopie
   in getrennten Läufen. Der Aufrufer übergibt für sie dieselbe Arbeitskopie-
   Kennung. Beide Snapshots weisen diese Kennung und jeweils die Host- oder
   Node-Kennung ihrer beobachtenden Umgebung aus. /
   *The host and its sandbox observe the same mounted physical working copy
   in separate runs. The caller supplies the same working-copy identifier
   in both runs. Each snapshot reports that identifier and its own
   observing host or node identifier.*

### US-3 · Fehlende oder veraltete Fakten erkennen / Recognise missing or stale facts (P3)

DE: Als Person, die eine Momentaufnahme bewertet, möchte ich erkennen, welche
Beobachtungen fehlen oder veraltet sind. So kann ich entscheiden, welche Fakten
ich noch verwenden kann. Vorbereitete Fehlerfälle prüfen das unabhängig von
einer echten Arbeitsumgebung.

EN: As a snapshot reviewer, I want to identify missing or stale observations
so that I can decide which facts are still usable. Prepared failure cases test
this independently of a real workspace.

1. Ein Nicht-Repository, ein fehlendes Werkzeug aus der übergebenen Liste und ein verweigerter Zugriff
   liefern unterscheidbare, strukturierte Fehler oder Verfügbarkeitszustände.
   Nachweisbare Fakten aus anderen freigegebenen Quellen bleiben sichtbar. /
   *A non-repository, a missing tool from the supplied list and denied access yield distinct
   structured issues or availability states. Supported facts from other
   authorised sources remain visible.*
2. Liegt der Erfassungsbeginn außerhalb der für die Prüfung vorgegebenen
   Gültigkeit, kennzeichnet die Prüfung die Momentaufnahme als veraltet.
   Das gilt auch, wenn das Ende der Erfassung innerhalb der Gültigkeit liegt.
   Eine unbekannte Schemaversion wird erkennbar zurückgewiesen. /
   *If capture started outside the validity defined for the check, the
   check marks the snapshot as stale, even if capture ended within that
   validity. It explicitly rejects an unknown schema version.*
3. Enthalten die Testdaten ein Geheimnis, einen privaten Pfad oder unnötige
   Personendaten, bleiben diese Werte in beiden Darstellungen verborgen.
   / *If a fixture contains a secret, a private path or unnecessary personal
   data, both views suppress those values.*
4. Zwei Listeneinträge geben für verschiedene Arbeitskopien dieselbe
   Arbeitskopie-Kennung an. Discovery weist beide vor dem Lesen ihrer
   Git-Metadaten ab. Der Snapshot enthält einen strukturierten Konfliktfehler
   und die Beobachtung eines dritten gültigen Eintrags. / *Two list entries
   give different working copies the same working-copy identifier. Discovery
   rejects both before reading their Git metadata. The snapshot contains a
   structured conflict error and the observation for a third, valid entry.*
5. Ändert sich Branch oder HEAD einer Arbeitskopie während ihrer Erfassung,
   meldet der Snapshot Branch, HEAD und Arbeitsbaumklasse dieser Kopie als
   `Unknown` und enthält einen strukturierten Fehler zur Zustandsänderung.
   Die Kennungen und die nachweisbaren Beobachtungen anderer Kopien bleiben
   erhalten. / *If a working copy's branch or HEAD changes during capture,
   the snapshot reports that copy's branch, HEAD and working-tree class as
   Unknown and includes a structured error for the state change. Identifiers
   and supported observations from other copies are retained.*
6. Bei einer gültig gelisteten Arbeitskopie fehlen die Git-Metadaten oder
   sie sind nicht lesbar. Der Snapshot enthält die Repository- und
   Arbeitskopie-Kennung sowie einen strukturierten Fehler. Branch, HEAD und
   Arbeitsbaumklasse lauten jeweils `Unavailable`. / *A validly listed
   working copy has missing or unreadable Git metadata. The snapshot retains
   the repository and working-copy identifiers and includes a structured
   error. Branch, HEAD and working-tree class each report Unavailable.*
7. Dieselbe Arbeitskopie steht mit unterschiedlichen Kennungen in der
   Liste. Discovery weist alle widersprüchlichen Einträge vor dem Lesen
   ihrer Git-Metadaten ab. Der Snapshot enthält einen strukturierten
   Konfliktfehler und die Beobachtung eines weiteren gültigen Eintrags.
   / *The same working copy is listed with different identifiers. Discovery
   rejects all conflicting entries before reading their Git metadata.
   The snapshot contains a structured conflict error and the observation
   for another, valid entry.*
8. Ein Snapshot enthält eine belegte Git-Beobachtung und eine zweite mit
   `Unavailable`. Die gemeinsame Fehlerliste enthält einen strukturierten
   Lesefehler mit datensparsamem Verweis auf die zweite Beobachtung. Ein
   Kennungskonflikt ohne zuordenbare Beobachtung steht in derselben Liste
   ohne Beobachtungsverweis. Verbraucher erkennen Teilfehler in beiden
   Darstellungen anhand der Beobachtungszustände und der Fehlerliste. /
   *A snapshot contains a supported Git observation and another marked
   Unavailable. The shared error list contains a structured read error with
   a data-minimised reference to the second observation. An identifier
   conflict with no attributable observation appears in the same list without
   an observation reference. Consumers recognise partial failures in both
   outputs from the observation states and the error list.*
9. Ein verweigerter Zugriff und ein Kennungskonflikt haben unterschiedliche
   Fehlercodes. Jeder Code bleibt in JSON und Konsole, auf allen
   Zielplattformen und in beiden Sprachen gleich. Die Meldung erklärt
   den Fehler verständlich. / *Denied access and an identifier conflict
   have different error codes. Each code is the same in JSON and console
   output, across target platforms and in both languages. The message
   explains the error in accessible language.*
10. Ein Konsolenlauf gibt einen gültigen Snapshot mit einem Teilfehler aus.
    Der Aufruf endet mit Exit-Code `0`. Der Teilfehler bleibt in der
    gemeinsamen Fehlerliste und den Beobachtungszuständen erkennbar. /
    *A console invocation emits a valid snapshot with a partial failure and
    returns exit code 0. The partial failure remains visible in the shared
    error list and observation states.*
11. Ein Konsolenlauf ohne freigegebene Wurzel kann keinen gültigen
    Snapshot ausgeben. Die Standardausgabe (`stdout`) bleibt leer.
    Die Standardfehlerausgabe (`stderr`) enthält im JSON- und im Textmodus
    ein JSON-Fehlerobjekt mit demselben stabilen Fehlercode und einer
    verständlichen Meldung. Der Exit-Code ist ungleich `0`. /
    *A console invocation without an authorised root cannot emit a valid
    snapshot. Standard output (stdout) stays empty. In both JSON and text
    mode, standard error (stderr) carries a JSON error object with the
    same stable error code and an understandable message. The exit code
    is non-zero.*
12. Zwei verschiedene Wurzeln werden mit derselben Wurzel-Kennung
    übergeben. Discovery liest aus keiner der beiden Wurzeln und meldet
    den Kennungskonflikt strukturiert. Eine gültige Beobachtung aus einer
    dritten, konfliktfreien und freigegebenen Wurzel bleibt im Snapshot.
    / *Two different roots are supplied with the same root identifier.
    Discovery reads from neither root and reports a structured identifier
    conflict. A valid observation from a third, conflict-free and
    authorised root remains in the snapshot.*

### Grenzfälle / Edge cases

- **Keine freigegebene Wurzel / No authorised root.** Die Erkennung endet mit
  einer strukturierten Ablehnung. Das Home- oder Arbeitsverzeichnis dient
  nicht als Ersatz. / *Discovery returns a structured denial. It does not
  fall back to the home or working directory.*
- **Git-Fakt nicht ermittelbar / Git fact cannot be determined.** `Unknown`
  bezeichnet einen unbelegten Wert. `Unavailable` bezeichnet eine fehlende
  oder unzugängliche Quelle oder Fähigkeit. Bei einem abgelösten HEAD ist
  ein Commit ausgewählt, ohne dass ein Branch aktiv ist. `Detached` ist
  dafür ein belegter Zustand der Branch-Angabe. / *Unknown means a value
  could not be established. Unavailable means a source or capability is
  missing or inaccessible. A detached HEAD selects a commit with no active
  branch. Detached is the supported branch state for that case.*
- **Unerwarteter Schreibversuch / Unexpected write attempt.** Die Prüfung
  muss den Versuch erkennen, bevor eine Änderung erfolgt, und einen sicheren
  Fehler melden. / *The check must detect the attempt before a change occurs
  and report a safe error.*

## Klärungen / Clarifications

### Session 2026-11-27

- **Frage / Question** Was zählt für RAW-01 als registriertes Repository? / What counts as a registered repository for RAW-01?
  **Antwort / Answer** Der Aufrufer übergibt die Repository-Liste pro Lauf. / The caller supplies the repository list for each run.
- **Frage / Question** Wofür steht die Repository-Kennung im WorkspaceSnapshot? / What does the repository identifier represent in a WorkspaceSnapshot?
  **Antwort / Answer** Arbeitskopien desselben logischen Repositorys teilen eine Kennung. Ihre Beobachtungen bleiben getrennt. / Working copies of the same logical repository share an identifier. Their observations remain separate.
- **Frage / Question** Wie detailliert soll der Snapshot Änderungen am Arbeitsbaum zeigen? / How much detail should the snapshot provide about working-tree changes?
  **Antwort / Answer** Der Snapshot zeigt bei ermittelbarem Arbeitsbaumzustand nur `Clean` oder `Dirty`. Vorgemerkte, nicht vorgemerkte und neue unignorierte Dateien zählen als `Dirty`. / For an observable working tree, the snapshot reports only Clean or Dirty. Staged changes, unstaged changes and new unignored files count as Dirty.
- **Frage / Question** Wer legt die Kennung des logischen Repositorys fest? / Who assigns the logical repository identifier?
  **Antwort / Answer** Der Aufrufer gibt die datensparsame Kennung des logischen Repositorys für jede Arbeitskopie in der Repository-Liste an. / The caller supplies the data-minimised logical repository identifier for each working copy in the repository list.
- **Frage / Question** Sollen einzelne Arbeitskopien über mehrere Snapshots hinweg wiedererkennbar sein? / Should individual working copies be identifiable across snapshots?
  **Antwort / Answer** Der Aufrufer liefert zusätzlich eine stabile, datensparsame Kennung je Arbeitskopie, damit sie über mehrere Snapshots hinweg wiedererkennbar bleibt. / The caller also supplies a stable, data-minimised identifier for each working copy so it can be recognised across snapshots.
- **Frage / Question** Wie behandelt RAW-01 widersprüchliche Arbeitskopie-Kennungen? / How does RAW-01 handle conflicting working-copy identifiers?
  **Antwort / Answer** Discovery weist die betroffenen Einträge vor dem Lesen ihrer Git-Metadaten ab. Der Snapshot enthält eine strukturierte Fehlermeldung und die Beobachtungen der gültigen Einträge. / Discovery rejects affected entries before reading their Git metadata. The snapshot contains a structured error and observations for valid entries.
- **Frage / Question** Darf Discovery die Git-Metadaten einer Arbeitskopie in einer zweiten freigegebenen Wurzel lesen? / May discovery read a working copy's Git metadata in a second authorised root?
  **Antwort / Answer** Discovery darf die zugehörigen Git-Metadaten in der zweiten Wurzel lesen, wenn beide Wurzeln ausdrücklich zum Lesen freigegeben sind. / Discovery may read the associated Git metadata in the second root when both roots are explicitly read-authorised.
- **Frage / Question** Was zeigt der Snapshot bei einem Wechsel von Branch oder HEAD während der Erfassung? / What does the snapshot show if branch or HEAD changes during capture?
  **Antwort / Answer** Branch, HEAD und Arbeitsbaumklasse der betroffenen Arbeitskopie werden als `Unknown` gemeldet. Der Snapshot enthält einen strukturierten Fehler. / The affected working copy's branch, HEAD and working-tree class are reported as Unknown. The snapshot includes a structured error.
- **Frage / Question** Wer legt fest, für welche Werkzeuge RAW-01 die Verfügbarkeit erfasst? / Who decides which tools RAW-01 checks for availability?
  **Antwort / Answer** Der Aufrufer übergibt die Liste der zu prüfenden Werkzeuge pro Lauf. Der Snapshot meldet deren Verfügbarkeit. / The caller supplies the list of tools to check for each run. The snapshot reports their availability.

### Session 2026-11-28

- **Frage / Question** Welcher Nachweis reicht aus, um ein Werkzeug als verfügbar zu melden? / What evidence is sufficient to report a tool as available?
  **Antwort / Answer** Discovery meldet ein Werkzeug als verfügbar, wenn es im ausdrücklich freigegebenen Suchbereich als ausführbar erkannt wird. Discovery startet es dabei nicht. / Discovery reports a tool as available when it can identify it as executable within the explicitly authorised search scope. Discovery does not start the tool.
- **Frage / Question** Welche Aufnahmezeit weist der WorkspaceSnapshot aus? / Which capture time does the WorkspaceSnapshot report?
  **Antwort / Answer** Der Snapshot enthält den Erfassungsbeginn als gemeinsamen UTC-Zeitstempel des beobachtenden Hosts oder Nodes. / The snapshot records the start of capture as one shared UTC timestamp from the observing host or node.
- **Frage / Question** Darf ein Lauf ausschließlich Werkzeuge prüfen? / May a run check tools only?
  **Antwort / Answer** Eine leere Repository-Liste ist zulässig, wenn mindestens ein Werkzeug angegeben ist. Die Wurzeln müssen ausdrücklich zum Lesen freigegeben sein. / An empty repository list is valid when at least one tool is supplied. The roots must be explicitly read-authorised.
- **Frage / Question** Welcher Wurzel ordnet der Snapshot eine Arbeitskopie in mehreren freigegebenen Wurzeln zu? / Which root does the snapshot assign to a working copy within multiple authorised roots?
  **Antwort / Answer** Wenn mehrere freigegebene Wurzeln passen, benennt der Repository-Listeneintrag die gewünschte Bezugswurzel. / When multiple authorised roots match, the repository list entry names the intended reference root.
- **Frage / Question** Woher erhält RAW-01 die opake Kennung des beobachtenden Hosts oder Nodes? / Where does RAW-01 get the observing host or node's opaque identifier?
  **Antwort / Answer** Der Aufrufer übergibt pro Lauf die opake Kennung des beobachtenden Hosts oder Nodes. / The caller supplies the observing host or node's opaque identifier for each run.
- **Frage / Question** Wie weist der Snapshot die Bezugswurzel einer Arbeitskopie aus? / How does the snapshot disclose a working copy's reference root?
  **Antwort / Answer** Der Aufrufer vergibt je Wurzel eine datensparsame Kennung. Der Snapshot weist die Bezugswurzel ausschließlich über diese Kennung aus. / The caller assigns a data-minimised identifier to each root. The snapshot identifies the reference root solely by that identifier.
- **Frage / Question** Erscheint eine gültig gelistete Arbeitskopie bei fehlenden oder unlesbaren Git-Metadaten im Snapshot? / Does a validly listed working copy appear in the snapshot if Git metadata is missing or unreadable?
  **Antwort / Answer** Der Snapshot behält die Kennungen der Arbeitskopie, meldet Branch, HEAD und Arbeitsbaumklasse als `Unavailable` und enthält einen strukturierten Fehler. / The snapshot retains the working copy's identifiers, reports branch, HEAD and working-tree class as Unavailable, and includes a structured error.
- **Frage / Question** Was passiert, wenn dieselbe Arbeitskopie mehrfach mit unterschiedlichen Kennungen in der Liste steht? / What happens when the same working copy is listed more than once with different identifiers?
  **Antwort / Answer** Discovery weist alle widersprüchlichen Einträge vor dem Lesen ihrer Git-Metadaten ab, meldet den Konflikt strukturiert und verarbeitet die übrigen gültigen Einträge. / Discovery rejects all conflicting entries before reading their Git metadata, reports a structured conflict, and processes the remaining valid entries.
- **Frage / Question** Wie stellt der Snapshot einen abgelösten HEAD dar? / How does the snapshot represent a detached HEAD?
  **Antwort / Answer** Die Branch-Angabe meldet den Zustand `Detached`, eindeutig vom gleichnamigen Branch unterscheidbar. Der HEAD-Commit bleibt sichtbar. / The branch observation reports the Detached state, distinguishable from a branch of the same name. The HEAD commit remains visible.
- **Frage / Question** Gibt es einen eigenen Gesamtstatus für Teilfehler? / Does the snapshot have a separate overall status for partial failures?
  **Antwort / Answer** Verbraucher erkennen Teilfehler anhand der strukturierten Fehler und der Zustände einzelner Beobachtungen. Der Snapshot erhält dafür kein eigenes Gesamtfeld. / Consumers identify partial failures from structured errors and individual observation states. The snapshot has no separate overall field for partial failures.
- **Frage / Question** Wo stehen die strukturierten Fehler im Snapshot? / Where are structured errors recorded in the snapshot?
  **Antwort / Answer** Alle Fehler stehen in einer gemeinsamen Liste. Ein Fehler verweist auf die betroffene Beobachtung, wenn diese eindeutig und datensparsam zugeordnet werden kann. / All errors appear in one shared list. An error references the affected observation when it can be attributed unambiguously without exposing unnecessary data.
- **Frage / Question** Braucht jeder strukturierte Fehler einen stabilen, maschinenlesbaren Fehlercode? / Does every structured error need a stable, machine-readable error code?
  **Antwort / Answer** Jeder strukturierte Fehler erhält einen stabilen, sprach- und plattformunabhängigen Fehlercode und eine verständliche Meldung. / Every structured error has a stable, language- and platform-independent error code and an understandable message.
- **Frage / Question** Wie stellt der Snapshot ein initialisiertes Repository vor dem ersten Commit dar? / How does the snapshot represent an initialised repository before its first commit?
  **Antwort / Answer** Der Snapshot zeigt den bekannten Branch-Namen und meldet HEAD als `Unborn`, solange es noch keinen Commit gibt. / The snapshot shows the known branch name and reports HEAD as Unborn until the first commit exists.
- **Frage / Question** Welchen Exit-Code liefert ein Konsolenlauf mit einem gültigen Snapshot und Teilfehlern? / Which exit code does a console invocation return when it emits a valid snapshot with partial failures?
  **Antwort / Answer** Ein ausgegebener gültiger Snapshot ergibt Exit-Code `0`, auch wenn er Teilfehler enthält. / Emitting a valid snapshot returns exit code 0 even if it contains partial failures.
- **Frage / Question** Wohin gehört die Fehlermeldung, wenn kein gültiger Snapshot ausgegeben werden kann? / Where is the error reported when a valid snapshot cannot be emitted?
  **Antwort / Answer** `stdout` bleibt leer. Der strukturierte Fehler steht auf `stderr`, und der Exit-Code ist ungleich `0`. / Stdout stays empty. The structured error is written to stderr and the exit code is non-zero.
- **Frage / Question** In welchem Format erscheint der strukturierte Fehler auf stderr? / What format does the structured error on stderr use?
  **Antwort / Answer** `stderr` enthält immer ein JSON-Fehlerobjekt mit dem stabilen Fehlercode und einer verständlichen Meldung. / Stderr always carries a JSON error object with the stable error code and an understandable message.
- **Frage / Question** Was passiert, wenn zwei verschiedene freigegebene Wurzeln dieselbe Wurzel-Kennung haben? / What happens when two different authorised roots share a root identifier?
  **Antwort / Answer** Discovery weist die betroffenen Wurzeln vor dem Lesen ab, meldet den Konflikt strukturiert und verarbeitet die übrigen gültigen Eingaben. / Discovery rejects the affected roots before reading them, reports a structured conflict, and processes the remaining valid inputs.
- **Frage / Question** Welche Arbeitskopie-Kennung gilt, wenn Host und Sandbox dieselbe physische Arbeitskopie beobachten? / Which working-copy identifier applies when a host and its sandbox observe the same physical working copy?
  **Antwort / Answer** Der Aufrufer vergibt dieselbe Arbeitskopie-Kennung. Die Beobachtungen behalten ihre jeweiligen Host- oder Node-Kennungen. / The caller assigns the same working-copy identifier. Observations retain their respective host or node identifiers.
- **Frage / Question** Wie behandelt Discovery zwei identische Einträge derselben Arbeitskopie? / How does discovery handle two identical entries for the same working copy?
  **Antwort / Answer** Discovery fasst identische Einträge zusammen, liest die Arbeitskopie einmal und gibt eine Beobachtung aus. Die Wiederholung wird nicht als Fehler gemeldet. / Discovery combines identical entries, reads the working copy once and emits one observation. It does not report the repetition as an error.
- **Frage / Question** Unterscheiden vom Aufrufer vergebene Kennungen Groß- und Kleinschreibung? / Are caller-assigned identifiers case-sensitive?
  **Antwort / Answer** Bei Repository-, Arbeitskopie-, Wurzel- und Host- oder Node-Kennungen wird Groß- und Kleinschreibung unterschieden. / Repository, working-copy, root and host or node identifiers are case-sensitive.
- **Frage / Question** Darf die Reihenfolge der Beobachtungen von der Reihenfolge der Eingabelisten abhängen? / May observation order depend on the input list order?
  **Antwort / Answer** Dieselben Arbeitskopie- und Werkzeugbeobachtungen erscheinen auch bei umsortierten Eingabelisten in derselben Reihenfolge. / The same working-copy and tool observations appear in the same order even if the input lists are reordered.

## Anforderungen / Requirements

### Funktionale Anforderungen / Functional requirements

- **FR-001 · Autorisierte Eingabe / Authorised input.** Der Aufrufer MUSS pro
  Lauf die Repository-Liste, die Liste der zu prüfenden Werkzeuge und die
  ausdrücklich benannten, zum Lesen freigegebenen Workspace-Wurzeln
  übergeben. Er MUSS jeder Wurzel eine datensparsame Kennung zuweisen und
  die opake Kennung des beobachtenden Hosts oder Nodes übergeben. Jeder
  Eintrag der Repository-Liste MUSS die datensparsame Kennung des logischen
  Repositorys und eine stabile, datensparsame Kennung der jeweiligen
  Arbeitskopie enthalten. Discovery
  DARF nur Daten gelisteter Arbeitskopien innerhalb der freigegebenen
  Wurzeln lesen. Zugehörige Git-Metadaten DARF sie in einer zweiten
  Wurzel lesen, wenn beide Wurzeln ausdrücklich freigegeben sind. Verweise
  und Repository-Metadaten dürfen keine zusätzliche Leseberechtigung begründen.
  / *The caller MUST
  supply the repository list, the list of tools to check and the explicitly
  named, read-authorised workspace roots for each run. The caller MUST
  assign a data-minimised identifier to each root and supply the observing
  host or node's opaque identifier. Each repository entry MUST include the
  data-minimised logical
  repository identifier and a stable, data-minimised working-copy identifier.
  Discovery may read only data for listed working copies within authorised
  roots. It may read associated Git metadata from a second root if both
  roots are explicitly authorised. References and repository metadata cannot
  grant additional read authority.*

  Discovery MUSS vom Aufrufer vergebene Repository-, Arbeitskopie-,
  Wurzel- und Host- oder Node-Kennungen auf allen Plattformen unter
  Beachtung der Groß- und Kleinschreibung vergleichen. JSON und
  Konsolenausgabe MÜSSEN ihre Schreibweise beibehalten. / *Discovery MUST
  compare caller-assigned repository, working-copy, root and host or node
  identifiers case-sensitively on all platforms. JSON and console output
  MUST preserve their case.*

  Liegt eine Arbeitskopie in mehreren freigegebenen Wurzeln, MUSS ihr
  Repository-Listeneintrag eine davon als Bezugswurzel benennen. Discovery
  MUSS die Arbeitskopie im Snapshot dieser Wurzel zuordnen. Die Zuordnung
  erteilt keine zusätzliche Leseberechtigung. / *When a working copy is within
  multiple authorised roots, its repository list entry MUST name one of
  them as the reference root. Discovery MUST associate the working copy
  with that root in the snapshot. The association grants no additional
  read authority.*

  Eine leere Repository-Liste ist zulässig, wenn mindestens ein Werkzeug
  angegeben ist. Die Wurzeln MÜSSEN auch für diesen Lauf ausdrücklich zum
  Lesen freigegeben sein. Der Snapshot MUSS die Werkzeugbeobachtungen
  enthalten. Discovery DARF in diesem Fall keine Git-Metadaten lesen. /
  *An empty repository list is valid when at least one tool is supplied.
  Roots MUST be explicitly read-authorised for this run as well. The
  snapshot MUST contain the tool observations. Discovery MUST NOT read
  Git metadata in this case.*
- **FR-002 · Beobachtungen / Observations.** Discovery MUSS je freigegebener
  Arbeitskopie die Zuordnung zur Wurzel, den Branch (Entwicklungszweig), den
  HEAD (aktuell ausgewählten Git-Stand) und die Working-Tree-Klasse
  (Änderungszustand des Arbeitsbaums) erfassen. Die Repository-Kennung und
  die Arbeitskopie-Kennung MÜSSEN aus dem jeweiligen Listeneintrag stammen.
  Arbeitskopien desselben logischen Repositorys MÜSSEN dieselbe
  Repository-Kennung und unterschiedliche Arbeitskopie-Kennungen tragen.
  Die Arbeitskopie-Kennung MUSS dieselbe Kopie über mehrere Snapshots
  hinweg identifizierbar machen, auch wenn sich Branch oder HEAD ändern.
  Für jedes Werkzeug der übergebenen Werkzeugliste MUSS Discovery seine
  Verfügbarkeit als eigene Beobachtung erfassen. Dieselben Arbeitskopie-
  und Werkzeugbeobachtungen MÜSSEN in derselben Reihenfolge erscheinen,
  auch wenn der Aufrufer die Eingabelisten umsortiert. /
  *Discovery MUST record each authorised working copy's root association,
  branch, HEAD (selected Git revision) and working-tree class (local change
  state). Both identifiers MUST come from the corresponding list entry.
  Working copies of the same logical repository MUST share a repository
  identifier and have distinct working-copy identifiers. The working-copy
  identifier MUST identify the same copy across snapshots, even when its
  branch or HEAD changes. Discovery MUST record availability as a separate
  observation for each tool in the supplied tool list. The same working-copy
  and tool observations MUST appear in the same order even if the caller
  reorders the input lists.*

  Beobachten Host und Sandbox dieselbe physische Arbeitskopie, MUSS der
  Aufrufer in beiden Läufen dieselbe Arbeitskopie-Kennung übergeben.
  Die Beobachtungen MÜSSEN über die jeweilige Host- oder Node-Kennung
  getrennt zuordenbar bleiben. / *When a host and its sandbox observe the
  same physical working copy, the caller MUST supply the same working-copy
  identifier in both runs. Observations MUST remain separately attributable
  through their respective host or node identifiers.*

  Stimmen alle Angaben mehrerer Listeneinträge derselben Arbeitskopie
  überein, MUSS Discovery sie zusammenfassen. Sie MUSS die Git-Metadaten
  dieser Arbeitskopie einmal erfassen und eine Beobachtung ausgeben.
  Die Wiederholung erzeugt keinen Fehler. / *When all details of multiple
  list entries for the same working copy agree, discovery MUST combine
  them. It MUST collect the working copy's Git metadata once and emit
  one observation. The repetition causes no error.*

  Bei einem belegten abgelösten HEAD MUSS die Branch-Angabe den Zustand
  `Detached` melden. JSON und Konsolenausgabe MÜSSEN diesen Zustand
  eindeutig von einem Branch mit dem Namen `Detached` unterscheiden.
  Der HEAD-Commit MUSS sichtbar bleiben. / *For a verified detached HEAD,
  the branch observation MUST report the Detached state. JSON and console
  output MUST distinguish this state from a branch named Detached.
  The HEAD commit MUST remain visible.*

  Bei einem initialisierten Repository mit bekanntem Branch-Namen vor dem
  ersten Commit MUSS Discovery den Branch-Namen und den HEAD-Zustand
  `Unborn` ausgeben. `Unborn` bezeichnet die belegte Abwesenheit eines
  HEAD-Commits vor dem ersten Commit. / *For an initialised repository
  before its first commit with a known branch name, discovery MUST report
  the branch name and the Unborn HEAD state. Unborn denotes the verified
  absence of a HEAD commit before the first commit.*

  JSON und Konsolenausgabe MÜSSEN die Bezugswurzel ausschließlich durch die
  vom Aufrufer vergebene Kennung ausweisen. Die Zuordnung enthält weder den
  Wurzelpfad noch den relativen Pfad der Arbeitskopie. / *JSON and console
  output MUST refer to the reference root solely by its caller-assigned
  identifier. The association exposes neither the root path nor the working
  copy's relative path.*

  Discovery MUSS ein Werkzeug genau dann als verfügbar melden, wenn es im
  ausdrücklich zum Lesen freigegebenen Suchbereich für die aktuelle
  Umgebung als ausführbar erkannt wird. Die Suche MUSS innerhalb dieser
  Freigabe bleiben. Discovery DARF dabei kein Werkzeug starten. /
  *Discovery MUST report a tool as available if and only if it identifies it as
  executable for the current environment within the explicitly read-authorised
  search scope. The search MUST stay within that scope. Discovery MUST NOT
  start any tool as part of this check.*

  Für einen ermittelbaren Arbeitsbaumzustand MUSS Discovery `Dirty`
  ausgeben, sobald mindestens eine vorgemerkte oder nicht vorgemerkte
  Änderung oder eine neue unignorierte Datei vorliegt. Sonst MUSS sie
  `Clean` ausgeben. Die Änderungsarten werden nicht einzeln ausgegeben.
  Bei fehlenden Belegen gilt FR-005. / *For an observable working-tree state,
  discovery MUST report Dirty when there is a staged or unstaged change
  or a new unignored file. Otherwise it MUST report Clean. The output
  does not list individual change types. FR-005 governs missing evidence.*
- **FR-003 · Nur lesend / Read-only.** Discovery und Snapshot-Erzeugung
  MÜSSEN Dateien, Git-Zustand und laufende Prozesse unverändert lassen.
  Beobachtete Werkzeuge dürfen durch die Erkennung keine Arbeitsaufträge
  erhalten. / *Discovery and snapshot creation MUST leave files, Git state
  and running processes unchanged. Discovery must not dispatch work to
  discovered tools.*
- **FR-004 · Herkunft und Zeit / Source and time.** Jeder `WorkspaceSnapshot`
  MUSS Quelle und die vom Aufrufer übergebene opake Host- oder Node-Kennung
  an seine Beobachtungen binden. Für Erkennungsfehler gilt FR-006. Die
  Kennung dient der Zuordnung und erteilt keine Berechtigung. Als Aufnahmezeit MUSS der
  Snapshot den Erfassungsbeginn von der Uhr des beobachtenden Hosts oder
  Nodes als gemeinsamen
  UTC-Zeitstempel nach RFC 3339 angeben. Dieser Zeitpunkt dient als Bezug
  für die Altersprüfung. Die Angaben MÜSSEN Host und Sandbox unterscheidbar
  machen. / *Every WorkspaceSnapshot MUST associate observations with their
  source and the caller-supplied opaque host or node identifier. FR-006
  governs discovery errors. The identifier supports attribution and grants
  no authority. The snapshot MUST report the start of capture from the
  observing host's or node's clock as a
  shared RFC 3339 UTC timestamp. That timestamp is the reference for
  freshness checks. The evidence MUST distinguish host and sandbox.*
- **FR-005 · Sichere Fehler / Safe failures.** Fehlende Belege MÜSSEN je
  nach Ursache `Unknown` oder `Unavailable` ergeben. Ablehnungen,
  unbekannte Schemaversionen und veraltete Daten MÜSSEN erkennbar sein.
  Die Prüfung DARF fehlende Fakten weder erfinden noch als Erfolg ausgeben.
  / *Depending on the cause, missing evidence MUST produce Unknown or
  Unavailable. Denials, unknown schema versions and stale data MUST be
  identifiable. The check MUST neither invent missing facts nor report
  them as successful observations.*

  Fehlen die Git-Metadaten einer gültig gelisteten Arbeitskopie oder sind
  sie nicht lesbar, MUSS der Snapshot die Repository- und
  Arbeitskopie-Kennung beibehalten. Er MUSS Branch, HEAD und
  Arbeitsbaumklasse als `Unavailable` melden und einen strukturierten
  Fehler ausgeben. / *If a validly listed working copy's Git metadata
  is missing or unreadable, the snapshot MUST retain the repository and
  working-copy identifiers. It MUST report branch, HEAD and working-tree
  class as Unavailable and include a structured error.*

  Ein Kennungskonflikt liegt vor, wenn verschiedene Arbeitskopien dieselbe
  Arbeitskopie-Kennung haben oder dieselbe Arbeitskopie mit unterschiedlichen
  Repository- oder Arbeitskopie-Kennungen gelistet ist. Discovery MUSS alle
  betroffenen Einträge vor dem Lesen ihrer Git-Metadaten abweisen. Der
  Snapshot MUSS den Konflikt als strukturierten Fehler ausgeben und die
  Beobachtungen der übrigen gültigen Einträge enthalten. / *An identifier
  conflict occurs when different working copies share a working-copy
  identifier or when the same working copy is listed with different repository
  or working-copy identifiers. Discovery MUST reject all affected entries
  before reading their Git metadata. The snapshot MUST expose the conflict as
  a structured error and retain observations for the remaining valid entries.*

  Tragen verschiedene Wurzeln dieselbe Wurzel-Kennung, MUSS Discovery
  alle betroffenen Wurzeln vor dem Lesen abweisen und den Konflikt
  strukturiert melden. Sie MUSS die übrigen gültigen Eingaben verarbeiten.
  / *If different roots share a root identifier, discovery MUST reject every
  affected root before reading from it and report a structured conflict.
  It MUST process the remaining valid inputs.*

  Wenn sich Branch oder HEAD während der Erfassung einer Arbeitskopie
  nachweislich ändert, MUSS der Snapshot die drei Git-Fakten Branch, HEAD
  und Arbeitsbaumklasse dieser Kopie als `Unknown` und die Zustandsänderung
  als strukturierten Fehler ausgeben. Die Kennungen der betroffenen Kopie
  und die belegten Beobachtungen anderer Kopien bleiben erhalten. /
  *If a working copy's branch or HEAD is observed to change during capture,
  the snapshot MUST report all three Git facts for that copy as Unknown:
  branch, HEAD and working-tree class. It MUST report the state change as a
  structured error. The affected copy's identifiers and supported observations
  of other copies are retained.*
- **FR-006 · Austausch und Anzeige / Exchange and display.** Ein
  `WorkspaceSnapshot` MUSS als versioniertes, kanonisches JSON vorliegen.
  Kanonisch bedeutet eine festgelegte Darstellung für Vergleiche. Das
  JSON-Dokument MUSS seine Schemaversion ausdrücklich nennen und mit dem
  zugehörigen JSON Schema prüfbar sein. Das Schema beschreibt die erlaubten
  Felder und Datentypen. Die Konsolenausgabe MUSS dieselben
  Felder, Werte, Status und dieselbe Schemaversion wiedergeben. /
  *A WorkspaceSnapshot MUST have a versioned canonical JSON form. Canonical
  means a defined representation for comparisons. The document MUST state
  its schema version and be verifiable against the corresponding JSON Schema.
  The schema describes allowed fields and data types. Console output MUST
  present the same fields, values, states and schema version.*

  Alle strukturierten Fehler MÜSSEN in einer gemeinsamen Liste stehen.
  Ein Fehler MUSS auf die betroffene Beobachtung verweisen, wenn sie sich
  eindeutig und datensparsam zuordnen lässt. Andernfalls bleibt der Fehler
  ohne Beobachtungsverweis in der Liste. / *All structured errors MUST appear
  in one shared list. An error MUST reference the affected observation when
  it can be attributed unambiguously without exposing unnecessary data.
  Otherwise, the error stays in the list without an observation reference.*

  Jeder strukturierte Fehler MUSS einen stabilen, maschinenlesbaren
  Fehlercode und eine verständliche Meldung enthalten. Für denselben
  Fehlergrund MUSS der Code unabhängig von Sprache, Plattform und
  Ausgabeform gleich sein. Die Meldung erläutert den Fehler nach FR-007
  und FR-008. / *Every structured error MUST contain a stable, machine-readable
  error code and an understandable message. The same cause MUST have the same
  code across languages, platforms and output formats. The message explains
  the error in accordance with FR-007 and FR-008.*

  Teilfehler MÜSSEN aus den strukturierten Fehlern und den Zuständen der
  einzelnen Beobachtungen erkennbar sein. Der Snapshot erhält dafür kein
  eigenes Gesamtfeld. / *Consumers MUST be able to identify partial
  failures using structured errors and individual observation states.
  The snapshot has no separate overall field for partial failures.*

  Gibt ein Konsolenlauf einen gültigen Snapshot aus, MUSS er mit Exit-Code
  `0` enden. Das gilt auch bei Teilfehlern im Snapshot. / *A console
  invocation MUST return exit code 0 when it emits a valid snapshot,
  including a snapshot with partial failures.*

  Kann ein Konsolenlauf keinen gültigen Snapshot ausgeben, MUSS `stdout`
  leer bleiben. Der Lauf MUSS auf `stderr` ein JSON-Fehlerobjekt mit
  stabilem Fehlercode und verständlicher Meldung ausgeben und mit einem
  Exit-Code ungleich `0` enden. Das JSON-Fehlerformat MUSS unabhängig vom
  gewählten Snapshot-Ausgabeformat gelten, auch wenn noch kein Format
  gewählt werden konnte. / *If a console invocation cannot emit a valid
  snapshot, stdout MUST remain empty. The invocation MUST write a JSON
  error object with a stable error code and an understandable message to
  stderr and return a non-zero exit code. This JSON error format MUST apply
  regardless of the selected snapshot output format, including failures
  before a format is selected.*
- **FR-007 · Datensparsamkeit / Data minimisation.** Die Erfassung MUSS
  austauschgeeignete Metadaten auf den Vertragszweck begrenzen. Ausgaben
  DÜRFEN keine Geheimnisse, Zugangsdaten, Benutzernamen, Home-Pfade,
  Hardware-Seriennummern, unnötige private Pfadsegmente oder Personendaten
  enthalten. Das gilt auch für die vom Aufrufer gelieferten Kennungen.
  Eine neue Datenkategorie erfordert vor ihrer Aufnahme eine
  Datenschutzprüfung. / *Discovery MUST minimise exchangeable metadata to
  what the contract needs. Outputs MUST exclude secrets, credentials, user
  names or home paths, hardware serial numbers, unnecessary private path
  segments and unnecessary personal data. This also applies to identifiers
  supplied by the caller. A new data category requires privacy review
  before adoption.*
- **FR-008 · Text und Plattform / Text and platform.** Konsolentext und
  nutzerseitige Dokumentation MÜSSEN Deutsch zuerst und Englisch danach
  liefern. Sie MÜSSEN auf CEFR-B2-Niveau verständlich sein, Zustände ohne
  Farbe vermitteln und die einschlägigen Kriterien von WCAG 2.2 AA
  berücksichtigen. Discovery, Schema, Status und Fehler MÜSSEN auf macOS,
  Linux und Windows dieselbe Bedeutung haben. / *Console text and user
  documentation MUST be German-first, English-second, understandable at
  CEFR B2, convey states without colour and meet applicable WCAG 2.2 AA
  criteria. Discovery, schema, states and errors MUST mean the same thing
  on macOS, Linux and Windows.*

### Konstitution und verbindliche Randbedingungen / Constitution and binding constraints

- **Vertragsplattform / Contract platform** · IAD101 und AC-004 binden
  plattformneutrales `net11.0` und C# 15. Domain und Core, die fachlichen
  Schichten, bleiben frei von Windows-spezifischen Abhängigkeiten. /
  *IAD101 and AC-004 bind platform-neutral net11.0 and C# 15. Domain and
  core, the business layers, stay free of Windows-specific dependencies.*
- **Testvertrag / Test contract** · IAD103 und AC-006 verlangen xUnit.net v3
  mit Microsoft Testing Platform v2, stabile Pakete und `dotnet test`
  auf macOS, Linux und Windows. AC-009 verlangt vor der ersten Paketübernahme
  stabile Versionsauflösung, erfolgreichen Restore, Schwachstellenprüfung
  und eine begründete Entscheidung zur Software-Stückliste (SBOM). /
  *IAD103 and AC-006 require xUnit.net v3 with Microsoft Testing Platform v2,
  stable packages and dotnet test on macOS, Linux and Windows. AC-009 requires
  stable version resolution, successful restore, vulnerability checking and
  a reasoned software bill of materials (SBOM) decision before first adoption.*
- **Vertrauensgrenzen / Trust boundaries** · Dateisystemdaten und beobachtete
  Werkzeugausgaben sind nicht vertrauenswürdig. Verantwortungsgrenzen
  verlaufen zwischen der expliziten Benennung einer Wurzel, dem Lesen der
  lokalen Quellen und der Ausgabe freigegebener Fakten. Eingabe, Status
  und Fehler müssen auf die erteilte Berechtigung und den Zweck beschränkt
  bleiben. / *File-system data and observed tool output are untrusted.
  Trust boundaries separate explicit root selection, local source inspection
  and the presentation of safe facts. Input, states and errors must stay
  within granted authority and purpose.*
- **Projektumgebung / Project environment** · Es gilt der AOC-Eintrag der
  [Projektkonstitution / project constitution](../../.specify/memory/constitution.md).
  C# steht auf der Liste speichersicherer Sprachen. Ausnahme oder
  Hardwarebindung sind für diesen Vertrag nicht erforderlich. /
  *The AOC registry entry applies. C# is on the approved memory-safe language
  list. This contract requires no language exception or hardware dependency.*
- **Nachweispfad / Evidence path** · Die
  [Specify-Checkliste / Specify checklist](checklists/requirements.md)
  hält Preset-Anwendbarkeit, Nachweisgrenzen und Folgeprüfungen fest.
  Plattformnachweise folgen dem macOS-zuerst-Vertrag der Konstitution
  und belegen Plattform, Revision, Befehl, Exit-Code, Hashes und null
  Schreibzugriffe. / *The checklist records preset applicability, evidence
  boundaries and later checks. Platform evidence follows the macOS-first
  constitutional rule and binds the platform, revision, command, exit code,
  hashes and zero writes.*

### Zentrale Begriffe im Vertrag / Key entities

| Entität / Entity | Vertragsinhalt / Contract meaning |
|---|---|
| Workspace-Wurzel / Workspace root | Explizit freigegebener Rahmen für die Erkennung mit einer datensparsamen Kennung vom Aufrufer. / Explicitly authorised discovery scope with a caller-assigned, data-minimised identifier. |
| Repository-Beobachtung / Repository observation | Eine Beobachtung je Arbeitskopie mit gemeinsamer Repository-Kennung, stabiler Arbeitskopie-Kennung sowie Zuordnung zur Wurzel, Branch, HEAD und Arbeitsbaumklasse. / One observation per working copy with a shared repository identifier, a stable working-copy identifier, root association, branch, HEAD and working-tree class. |
| Werkzeug-Beobachtung / Tool observation | Verfügbarkeit eines Werkzeugs aus der für den Lauf übergebenen Liste. / Availability of a tool from the list supplied for the run. |
| `WorkspaceSnapshot` | Versionierte Momentaufnahme mit Quelle, Erfassungsbeginn in UTC, opaker Kennung, Beobachtungen und einer gemeinsamen Liste strukturierter Fehler. / Versioned record with source, UTC capture start, opaque identity, observations and one shared list of structured errors. |

## Erfolgskriterien / Success criteria

| ID | Beobachtbares Ergebnis / Observable outcome | Intake |
|---|---|---|
| SC-001 | Zwei Läufe mit umsortierten Eingabelisten zeigen dieselben drei erwarteten Arbeitskopien und dieselben Werkzeugbeobachtungen in unveränderter Reihenfolge. Die Git-Fakten und die Werkzeugverfügbarkeit bleiben bei unveränderten Testbedingungen gleich. Eine weitere Arbeitskopie in der Wurzel bleibt ohne Listeneintrag ungelesen. / Two runs with reordered input lists show the same three expected working copies and tool observations in an unchanged order. Git facts and tool availability stay the same under unchanged test conditions. An additional working copy in a root is left unread if absent from the list. | AC-001 |
| SC-002 | Die Fehlerfälle nach US-3 liefern unterscheidbare Status und strukturierte Fehler. Fehlende oder unlesbare Git-Metadaten einer gültig gelisteten Kopie ergeben `Unavailable` für alle drei Git-Fakten, mit erhaltenen Kennungen. Ein Kennungskonflikt ergibt null Lesezugriffe auf die betroffenen Git-Metadaten. Ein Wechsel von Branch oder HEAD während der Erfassung ergibt `Unknown` für alle drei Git-Fakten der betroffenen Kopie. Belegte Beobachtungen anderer Kopien bleiben erhalten. / The US-3 failure cases yield distinct states and structured errors. Missing or unreadable metadata for a validly listed copy makes all three Git facts Unavailable while retaining both identifiers. An identifier conflict causes zero reads of affected Git metadata. A branch or HEAD change during capture makes all three Git facts of the affected copy Unknown. Supported observations of other copies are retained. | AC-002, negative evidence |
| SC-003 | Zwei Arbeitskopien desselben logischen Repositorys liefern dieselbe Repository-Kennung und zwei unterscheidbare Arbeitskopie-Kennungen, auch wenn beide auf demselben Host liegen. Die Arbeitskopie-Kennung bleibt bei geändertem Branch oder HEAD gleich. Bei derselben physischen Arbeitskopie auf Host und Sandbox bleibt die Arbeitskopie-Kennung gleich, während die Host- oder Node-Kennung die Beobachtungen unterscheidet. / Two working copies of the same logical repository yield one shared repository identifier and two distinct working-copy identifiers, even on the same host. The working-copy identifier stays the same when its branch or HEAD changes. For the same physical working copy on a host and sandbox, the working-copy identifier is shared and the host or node identifier distinguishes the observations. | AC-003 |
| SC-004 | Beide Darstellungen enthalten bei allen positiven und negativen Testaufnahmen dieselben fachlichen Informationen, dieselbe Version und dieselbe Fehlerliste. Die Fehlerliste erhält einen Beobachtungsverweis nur bei eindeutiger, datensparsamer Zuordnung. / Both views convey the same domain information, version and error list for all positive and negative test snapshots. The error list includes an observation reference only when attribution is unambiguous and data-minimised. | AC-005 |
| SC-005 | Jede Erkennungsprüfung verursacht null Schreibzugriffe. Git-Metadaten in einer zweiten Wurzel liefern die erwarteten Fakten, wenn beide Wurzeln freigegeben sind. Ohne Freigabe gibt es null Lesezugriffe am jeweiligen Ziel. Die Werkzeugprüfung meldet nur im freigegebenen Suchbereich als ausführbar erkannte Werkzeuge als verfügbar und startet null geprüfte Werkzeuge. Kein vorbereiteter sensibler Testwert erscheint in einer Ausgabe. / Every discovery case causes zero writes. Git metadata in a second root yields the expected facts when both roots are authorised. Without authorisation there are zero reads at the relevant target. Tool checks report availability only for executables identified within the authorised search scope and start zero checked tools. No planted sensitive value appears in either output. | AC-007 |
| SC-006 | Dieselben Testfälle zeigen auf den drei benannten Plattformen dieselben Status und Fehler. Ein Textreview bestätigt DE/EN, CEFR B2, anwendbare WCAG-2.2-AA-Kriterien und verständliche Zustände ohne Farbe. / The same test cases show the same states and errors on all three named platforms. A text review confirms German and English, CEFR B2, applicable WCAG 2.2 AA criteria and states understandable without colour. | AC-008 |

Die technologischen Akzeptanzvorgaben AC-004, AC-006 und AC-009 stehen bei
den verbindlichen Randbedingungen. / *The binding constraints carry the
technology acceptance conditions AC-004, AC-006 and AC-009.*

## Annahmen und Abgrenzung / Assumptions and boundaries

- DE: Die aufrufende Stelle liefert pro Lauf die Repository-Liste, die
  Werkzeugliste, Wurzeln, Berechtigung und die opake Host- oder Node-Kennung.
  Verbraucher verwenden den Erfassungsbeginn für die jeweils vorgegebene
  Gültigkeitsprüfung.
  Der Vertrag setzt kein allgemeines Ablaufintervall.
  / *EN: The caller supplies the repository list, tool list, roots, authority
  and opaque host or node identifier for each run. Consumers use the capture
  start with the validity rule defined for their check. The contract sets no universal
  expiry interval.*
- DE: Der Umfang endet bei Beobachtung und Ausgabe von Metadaten. Befehls- und
  Workflow-Ausführung, Arbeitsdateiinhalte, grafische UI, Hardwareerkennung,
  Zugangsdatenverwaltung, Fernzugriff und automatische Snapshot-Speicherung
  gehören nicht zum Vertrag. / *EN: Scope stops at metadata observation and
  output. Command and workflow execution, working-file contents, graphical
  UI, hardware discovery, credential management, remote access and automatic
  snapshot storage are outside this contract.*
- DE: RAW-03 folgt in der Serie vor RAW-02. Übergaben an RAW-02, RAW-03,
  RAW-05 und RAW-06 verwenden den Snapshot-Vertrag. Dieser Text dokumentiert
  die Schnittstelle und die Prüfanforderungen. / *EN: RAW-03 precedes RAW-02
  in the series. Handoffs to RAW-02, RAW-03, RAW-05 and RAW-06 use the snapshot
  contract. This document records the interface and its acceptance conditions.*
