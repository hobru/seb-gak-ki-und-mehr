# SEB GAK Digital – Schulelternbeirat des Gymnasiums am Kaiserdom Speyer

Eine Initiative des SEB: Informatik, KI und digitale Bildung für Schülerinnen und Schüler und Eltern.

---

## Voraussetzungen

- [Hugo extended](https://gohugo.io/installation/) v0.134.x oder neuer

## Lokal bauen und testen

```bash
# Im Projektverzeichnis:
hugo server

# Öffne: http://localhost:1313/
```

## Produktions-Build (statische Dateien)

```bash
hugo --minify --baseURL "https://hobru.github.io/seb-gak-ki-und-mehr/"
# Ausgabe in: ./public/
```

## Deployment via GitHub Pages

Das Deployment erfolgt automatisch über GitHub Actions bei jedem Push auf `main` oder `master`.
Für dieses Repository ist die Projektadresse:

<https://hobru.github.io/seb-gak-ki-und-mehr/>

**Einmalige Einrichtung:**
1. Gehe zu **Settings → Pages** im GitHub-Repository
2. Wähle als Source: **GitHub Actions**
3. Der Workflow `.github/workflows/deploy.yml` baut und deployt die Seite automatisch

**Base-URL anpassen:**  
In `hugo.toml` ist die GitHub-Pages-Projektadresse eingetragen. Der Deploy-Workflow überschreibt die `baseURL` beim Build zusätzlich mit der von GitHub Pages gelieferten Adresse.
Für eine eigene Domain: Trage die Domain in den GitHub Pages Einstellungen ein und passe anschließend `baseURL` entsprechend an.

## Struktur

```
content/
├── _index.md          # Startseite
├── informatik/        # Bereich Digitales & Informatik
│   └── _index.md
├── ki/                # Bereich KI in der Schule
│   └── _index.md
├── news/              # Neuigkeiten / Beiträge
│   ├── _index.md
│   └── YYYY-MM-DD-titel.md   # einzelne Beiträge
├── mitmachen/         # Beitrag vorschlagen / Redaktionsprozess
│   └── _index.md
├── impressum/
│   └── _index.md
└── datenschutz/
    └── _index.md
```

## Neuigkeiten veröffentlichen

Der bevorzugte Redaktionsweg läuft über GitHub Issues und Pull Requests:

1. Über **Issues → New issue → Neuigkeit vorschlagen** wird ein Vorschlag eingereicht.
2. Die Issue Form nutzt den GitHub-Issue-Titel als Nachrichtentitel und fragt Kurzbeschreibung, optionale Details/externen Link, Zielgruppe, Thema/Kategorie sowie optional GAK/SEB-Relevanz ab.
3. Es werden keine personenbezogenen Daten abgefragt. Die Datenschutz-Bestätigung ist Pflicht; Namen, E-Mail-Adressen, Telefonnummern, Adressen, Fotos oder private Angaben gehören nicht in Issues.
4. Redakteur:innen prüfen Inhalt, Relevanz und externe Links. Wenn der Vorschlag passt, setzen Maintainer das Label `freigegeben`.
5. Der Workflow `.github/workflows/news-from-issue.yml` validiert das Issue, erzeugt eine bereinigte Hugo-Markdown-Datei und öffnet einen Pull Request, der das Issue beim Merge schließt.
6. Erst Review und Merge des Pull Requests veröffentlichen die Neuigkeit über den bestehenden GitHub-Pages-Deploy.

Approver erhalten Benachrichtigungen über GitHub, z. B. durch Repository-Watching, Issue-Zuweisung, Erwähnungen oder CODEOWNERS/Review-Anfragen. Es wird keine externe Mail- oder Tracking-Infrastruktur verwendet.

Fallback für manuelle Beiträge: Erstelle eine neue Datei in `content/news/`. Verwende für `date` nach Möglichkeit einen ISO-8601-Zeitstempel mit Uhrzeit (UTC, `Z`), damit mehrere Beiträge am selben Tag korrekt sortiert werden:


```markdown
---
title: "Titel des Beitrags"
date: 2026-06-01T16:52:36Z
draft: false
categories: ["KI"]                   # KI, Informatik, Veranstaltung, Wettbewerb, Material, Empfehlung, Hinweis, Sonstiges
audiences: ["Schüler:innen"]         # Schüler:innen, Eltern, Lehrkräfte, SEB, Allgemein
abstract: "Kurze Zusammenfassung (max. 200 Zeichen)"
sample: false
external_link: "https://example.org" # optional
---

Inhalt des Beitrags in Markdown…
```

## Hinweise

- `site.Params.sampleSite = true` in `hugo.toml` zeigt einen Hinweis-Banner für Demo-Inhalte.
  Auf `false` setzen, wenn echte Inhalte veröffentlicht werden.
- **Impressum und Datenschutzerklärung** in `content/impressum/` und `content/datenschutz/`
  müssen vor der Veröffentlichung durch rechtlich geprüfte Texte ersetzt werden (§ 5 TMG / DSGVO).
- Keine personenbezogenen Daten in Beiträgen veröffentlichen.

## Technologie

- [Hugo](https://gohugo.io/) – statischer Website-Generator (Go, kein Ruby/Node nötig)
- GitHub Pages – kostenloses Hosting
- Kein Theme-Paket – eigene Layouts und CSS für maximale Kontrolle und einfache Wartung
