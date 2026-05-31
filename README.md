# GAK Digital – Gymnasium am Kaiserdom Speyer

Informatik, KI und digitale Bildung für Schülerinnen und Schüler, Lehrkräfte und Eltern.

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
hugo --minify --baseURL "https://<deine-domain>/"
# Ausgabe in: ./public/
```

## Deployment via GitHub Pages

Das Deployment erfolgt automatisch über GitHub Actions bei jedem Push auf `main`.

**Einmalige Einrichtung:**
1. Gehe zu **Settings → Pages** im GitHub-Repository
2. Wähle als Source: **GitHub Actions**
3. Der Workflow `.github/workflows/deploy.yml` baut und deployt die Seite automatisch

**Base-URL anpassen:**  
In `hugo.toml` und im Deploy-Workflow wird die `baseURL` automatisch gesetzt.
Für eine eigene Domain: Trage die Domain in den GitHub Pages Einstellungen ein.

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
├── impressum/
│   └── _index.md
└── datenschutz/
    └── _index.md
```

## Neuen Beitrag hinzufügen

Erstelle eine neue Datei in `content/news/`:

```markdown
---
title: "Titel des Beitrags"
date: 2026-06-01
draft: false
categories: ["KI"]                   # KI, Informatik, Lernen, Eltern, Coding, Tools, …
audiences: ["Schülerinnen und Schüler"]
abstract: "Kurze Zusammenfassung (max. 200 Zeichen)"
sample: false
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
