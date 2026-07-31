# Sicherheitsrichtlinie / Security Policy

## Sicherheitsprobleme melden

Bitte veröffentliche vermutete Schwachstellen, Zugangsdaten, personenbezogene
Daten oder ausnutzbare Details nicht in einem öffentlichen Issue. Nutze nach
Veröffentlichung des Repositories die private GitHub-Funktion „Report a
vulnerability“ im Bereich **Security**. Falls diese Funktion nicht verfügbar
ist, eröffne nur ein neutrales Issue ohne technische Details und bitte um einen
privaten Kontaktweg.

Eine Meldung sollte die betroffene Version oder Revision, nachvollziehbare
Schritte, mögliche Auswirkungen und bereits bekannte Gegenmaßnahmen enthalten.
Entferne echte Geheimnisse und personenbezogene Daten aus allen Nachweisen.

## Unterstützter Stand

Bis zur ersten Produktversion wird ausschließlich der aktuelle Stand des
Default Branch `main` sicherheitsseitig gepflegt. Historische Commits und lokale
Forks erhalten keine gesonderte Unterstützung.

## Sicherheitsbaseline

- Geheimnisse dürfen weder in Git noch in Issues, Logs, Evidence oder Receipts
  gespeichert werden.
- Eingaben über Datei-, Prozess-, Netzwerk- und Geräte-Grenzen gelten als nicht
  vertrauenswürdig und müssen später validiert werden.
- Neue Abhängigkeiten benötigen Herkunfts-, Lizenz-, Wartungs- und
  Schwachstellenprüfung.
- Architektur- und Code-Reviews betrachten mindestens Authentifizierung,
  Autorisierung, Eingaben, Kryptografie, Fehlerausgaben sowie Datei- und
  Netzwerkzugriffe.
- Sicherheitsrelevante Entscheidungen und Restrisiken benötigen menschliche
  Freigabe.

*Do not disclose suspected vulnerabilities, credentials, personal data, or
exploitable details in a public issue. After publication, use GitHub's private
“Report a vulnerability” function in the Security area. If unavailable, open
only a neutral issue without technical details and request a private channel.*

*Until the first product release, only the current `main` branch is supported.
Secrets must never enter Git, issues, logs, evidence, or receipts. Inputs across
file, process, network, and device boundaries are untrusted. Dependencies need
provenance, licence, maintenance, and vulnerability review. Security-relevant
decisions and residual risks require human approval.*
