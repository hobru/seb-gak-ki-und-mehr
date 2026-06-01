# Brand: Neuigkeiten-Workflow mit Issue-Form und PR-Gate

**Datum:** 2026-06-01T12:56:42.320+02:00  
**Status:** Implementiert  
**Owner:** Brand  

## Entscheidung

Neuigkeiten werden über eine deutsche GitHub Issue Form vorgeschlagen, durch das Maintainer-Label `freigegeben` moderiert und anschließend als automatisch erzeugter Pull Request in `content/news/` geprüft. Die Website veröffentlicht erst nach Review und Merge über den bestehenden GitHub-Pages-Workflow.

## Rationale

Das erfüllt die Teamvorgaben: kein Direkt-Publishing aus Issues, keine zusätzlichen Dienste, Privacy-by-default, GitHub-native Benachrichtigungen und ein nachvollziehbarer Review-Pfad.

## Umsetzung

- `.github/ISSUE_TEMPLATE/news.yml` trennt Zielgruppe und Thema/Kategorie, fordert GAK/SEB-Relevanz und eine No-PII-Bestätigung.
- `.github/workflows/news-from-issue.yml` reagiert auf `freigegeben`, nutzt minimale Schreibrechte für Content/PR/Issue-Kommentar und öffnet einen PR.
- `.github/scripts/news_issue_to_markdown.py` validiert Pflichtfelder, erlaubte Auswahlwerte, Datum, No-PII-Bestätigung, einfache PII-Muster und erzeugt bereinigtes Hugo-Markdown.
- `layouts/news/list.html` und `news-card.html` bieten einfache clientseitige Filter für Zielgruppe und Kategorie; ohne JavaScript bleiben alle Beiträge sichtbar.

## Betreiberhinweise

Maintainer müssen das Label `freigegeben` anlegen oder beim ersten Einsatz anlegen lassen. Approver-Benachrichtigung läuft über GitHub Watching, Zuweisung, Erwähnungen oder optionale CODEOWNERS/Review-Konventionen, nicht über externe Maildienste.
