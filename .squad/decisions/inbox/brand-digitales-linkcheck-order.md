# Brand: Digitales-Fächerreihenfolge und Linkcheck (2026-06-01)

**Context:** Holger wies darauf hin, dass das GAK ein humanistisches Gymnasium mit Latein ist und dass mehrere externe Lernlinks auf der Seite `Digitales & Informatik` fehlerhaft wirken.

**Decision:** Die Fachreihenfolge in `content/informatik/_index.md` ist nun sprach- und geisteswissenschaftlich eröffnet: Deutsch, Englisch, Französisch, Latein, Geschichte/Gesellschaft, Religion/Ethik, Musik/Kultur; danach folgen Mathematik, Physik, Chemie, Biologie, Informatik/Digitales und Elternangebote. Defekte oder beim GET-Linkcheck problematische Angebote wurden durch stabile Alternativen ersetzt.

**Rationale:** Die Reihenfolge passt besser zum GAK-Profil, ohne MINT und Informatik abzuwerten. Stabile, direkt erreichbare Links sind für Schülerinnen, Schüler und Eltern wichtiger als bekannte Marken, wenn diese 404/403 liefern oder App-Fehlertexte ausgeben.

**Verification:** Alle 43 externen URLs aus `content/informatik/_index.md` wurden per GET mit Redirects geprüft; alle finalen Links lieferten HTTP < 400 und keine gescannten Fehlertexte (`Es tut uns leid`, `beim Laden dieses Inhalts ging was schief`, `Seite nicht gefunden`, `Page not found`, `Not Found`, `Access Denied`, `Just a moment`). `hugo --minify` erfolgreich.
