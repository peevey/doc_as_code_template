# Markdown-Dokumentationsvorlage

Dieses Template erzeugt aus Markdown eine HTML-Website und ein PDF. Der
GitHub-Actions-Workflow veröffentlicht die Website mit PDF-Download auf GitHub Pages
und stellt das PDF zusätzlich als Build-Artefakt bereit.

## Dokumentation bearbeiten

- `pages/index.md`: Titel und Sprache als YAML-Metadaten.
- `pages/kap1.md`: Beispielkapitel; weitere Kapitel als `.md` in `pages/` ergänzen.
- `assets/images/`: Bilder für HTML und PDF.

Der Build liest zuerst `index.md`, danach alle weiteren Markdown-Dateien in
alphabetischer Reihenfolge. Für viele Kapitel eignen sich Dateinamen wie
`01-einleitung.md`, `02-installation.md`. Kapitel beginnen mit `#`, Unterkapitel
mit `##`. Inhaltsverzeichnis und Abschnittsnummern entstehen beim Export.
Es wird Pandoc-Markdown verwendet; einfache Inhalte sind auch in GitHub lesbar.

Bilder werden relativ zum Repository referenziert:

```markdown
![Beschreibung](assets/images/beispiel.png)
```

Dieser Bildpfad wird im Build für HTML und PDF aufgelöst. Für die direkte
Bildvorschau auf GitHub innerhalb von `pages/` eignet sich stattdessen
`../assets/images/beispiel.png` derzeit nicht für die veröffentlichte HTML-Seite.

## Lokal bauen

Unter Debian/Ubuntu die Werkzeuge installieren:

```bash
sudo apt-get update
sudo apt-get install -y --no-install-recommends pandoc texlive-xetex texlive-fonts-recommended texlive-latex-extra texlive-lang-german
bash scripts/build.sh
```

Ergebnisse:

- `_site/index.html`: Website mit Inhaltsverzeichnis und PDF-Download.
- `_site/dokumentation.pdf`: PDF in A4 mit 25 mm Seitenrändern.

PDF-Layout und Exportoptionen werden zentral in `scripts/build.sh` gepflegt.
Der PDF-Download wird nur in HTML eingefügt.

## GitHub Pages

In den Repository-Einstellungen unter **Pages → Build and deployment** die
Quelle **GitHub Actions** auswählen. Pushes auf `main` und manuelle Workflow-Starts
bauen und veröffentlichen die Dokumentation.

## HTML-Theme und Bearbeiten-Links

Die Website verwendet Pico CSS 2.1.1 über jsDelivr und ein responsives
Inhaltsverzeichnis (am Desktop seitlich, auf kleinen Bildschirmen vor dem Inhalt).
Zum Laden des Pico-Themes benötigen Besucher eine Internetverbindung.
Eigene Anpassungen stehen in `assets/styles/docs.css`, das HTML-Layout in
`scripts/page.html`. Der PDF-Export verwendet weiterhin sein separates Layout.

Jedes Kapitel erhält einen **Kapitel bearbeiten**-Link zur passenden Markdown-Datei
im GitHub-Webeditor. **Titel bearbeiten** öffnet `pages/index.md`.
GitHub benötigt zum Speichern eine Anmeldung und entsprechende Berechtigungen;
je nach Berechtigung entsteht stattdessen ein Änderungsvorschlag über einen Fork.

In GitHub Actions wird das Zielrepository automatisch aus `GITHUB_REPOSITORY`
übernommen. Lokal kann es explizit gesetzt werden:

```bash
GITHUB_REPOSITORY=mein-account/meine-dokumentation DOCS_EDIT_BRANCH=main bash scripts/build.sh
```

Neue Veröffentlichungen lösen veraltete Workflow-Läufe ab. Der Build ist auf
15 Minuten begrenzt, die Werkzeuginstallation auf 10 Minuten. Die Installation
verzichtet auf empfohlene Zusatzpakete und begrenzt Netzwerk-Wartezeiten.
