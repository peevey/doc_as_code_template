# Markdown-Dokumentationsvorlage

Dieses Template erzeugt aus Markdown eine HTML-Website und ein PDF. Der
GitHub-Actions-Workflow veröffentlicht die Website mit PDF-Download auf GitHub Pages
und stellt das PDF zusätzlich als Build-Artefakt bereit.

## Dokumentation bearbeiten

Syntax und Beispiele stehen im [Markdown-Cheat-Sheet](MARKDOWN-CHEAT-SHEET.md).

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
sudo apt-get install -y --no-install-recommends pandoc lmodern texlive-xetex texlive-fonts-recommended texlive-latex-extra texlive-lang-german
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

## HTML-Layout, Navigation und Bearbeiten

Die Website verwendet eigenes, lokal gespeichertes CSS und JavaScript. Es gibt
keine externen Theme-Abhängigkeiten. Layout: `scripts/page.html`, Styles:
`assets/styles/docs.css`, Hell-/Dunkel-Schalter: `assets/scripts/theme.js`.
Der Schalter speichert die Auswahl lokal; ohne Auswahl gilt die Systemeinstellung.

Jede Markdown-Datei in `pages/` ergibt eine eigene HTML-Seite im Website-Hauptverzeichnis.
`index.md` ist die Startseite; weitere Kapitel erscheinen alphabetisch links.
Der PDF-Download steht unten in dieser Navigation. Das Inhaltsverzeichnis des
aktuellen Kapitels steht rechts, auf kleineren Bildschirmen vor dem Inhalt.
Alle Kapitel bleiben im gemeinsamen PDF enthalten.

**✎ Bearbeiten** öffnet die jeweilige Quelldatei im GitHub-Webeditor, auch auf der
Startseite. Zum Speichern benötigt GitHub eine Anmeldung und passende Rechte;
sonst kann ein Änderungsvorschlag über einen Fork erstellt werden.
Links auf andere Kapiteldateien (z. B. `kap2.md#installation`) werden für HTML
auf die entsprechende `.html`-Seite umgesetzt. Für PDF weiterhin bevorzugt
Abschnittsanker verwenden.

In GitHub Actions wird das Repository aus `GITHUB_REPOSITORY` übernommen.
Lokal sind Zielrepository und Editierbranch konfigurierbar:

```bash
GITHUB_REPOSITORY=mein-account/meine-dokumentation DOCS_EDIT_BRANCH=main bash scripts/build.sh
```

Neue Veröffentlichungen lösen veraltete Workflow-Läufe ab. Der Build ist auf
15 Minuten begrenzt, die Werkzeuginstallation auf 10 Minuten. Die Installation
verzichtet auf empfohlene Zusatzpakete und begrenzt Netzwerk-Wartezeiten.
