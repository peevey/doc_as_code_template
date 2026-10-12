# Markdown-Cheat-Sheet

Kurzanleitung für dieses Dokumentations-Template. Der Export verwendet
**Pandoc-Markdown**. Die grundlegende Syntax funktioniert auch in GitHub.
Diese Datei liegt im Repository-Hauptverzeichnis und wird nicht automatisch
in die Dokumentation oder das PDF aufgenommen.

## Überschriften

```markdown
# Kapitel
## Unterkapitel
### Abschnitt
```

In `pages/` beginnt ein Kapitel mit `#`. Inhaltsverzeichnis und Nummerierung
werden beim Export automatisch erzeugt: keine Nummern in die Überschrift schreiben.
Überschriften erhalten Einträge im Inhaltsverzeichnis bis Ebene 3.

## Absätze und Zeilenumbrüche

Eine Leerzeile beginnt einen neuen Absatz. Ein einfacher Zeilenumbruch im
Quelltext bleibt normalerweise Teil desselben Absatzes.
Für einen erzwungenen Zeilenumbruch zwei Leerzeichen an das Zeilenende setzen.

## Text hervorheben

| Quelltext | Darstellung |
| --- | --- |
| `**fett**` | **fett** |
| `*kursiv*` | *kursiv* |
| `~~durchgestrichen~~` | ~~durchgestrichen~~ |
| `` `Code im Text` `` | `Code im Text` |

## Listen

```markdown
- Erster Punkt
- Zweiter Punkt
    - Unterpunkt

1. Erster Schritt
2. Zweiter Schritt
```

Unterpunkte mit vier Leerzeichen einrücken. Vor und nach einer Liste eine
Leerzeile lassen.

## Aufgabenlisten

```markdown
- [ ] Noch offen
- [x] Erledigt
```

GitHub zeigt Checkboxen an; im HTML- und PDF-Export kann ihre Darstellung abweichen.
Auf der veröffentlichten Website werden Änderungen an Aufgaben nicht gespeichert.

## Links und Verweise

```markdown
[GitHub](https://github.com/)
[Zum Abschnitt Installation](#installation)
```

Bei einfachen Überschriften erzeugt Pandoc den Anker automatisch aus dem Text.
Für einen stabilen Anker trotz späterer Umbenennung kann er explizit gesetzt werden:

```markdown
## Installation {#installation}

[Zur Installation](#installation)
```

Die explizite Ankersyntax ist eine Pandoc-Erweiterung und wird in der
GitHub-Vorschau nicht gleich dargestellt. Abschnittslinks ersetzen keine
Querverweise mit automatisch eingefügten Abschnittsnummern.

Alle Kapitel werden zu einer HTML-Seite und einem PDF zusammengeführt.
Für Verweise zwischen Kapiteln daher Abschnittsanker verwenden; Links auf
`kap1.md` werden beim Export nicht automatisch auf HTML umgeschrieben.

## Bilder

```markdown
![Beschreibung des Bildes](assets/images/beispiel.png)
```

Die Bilddatei unter `assets/images/` ablegen. Der Build verwendet Pfade relativ
zum Repository-Hauptverzeichnis. Deshalb kann die GitHub-Vorschau der Datei
innerhalb von `pages/` das Bild bei diesem Pfad nicht anzeigen.

Pandoc unterstützt Größenangaben, beispielsweise:

```markdown
![Beschreibung des Bildes](assets/images/beispiel.png){width=70%}
```

Größenangaben sind Pandoc-Erweiterungen. Die Beschreibung dient in HTML als
Alternativtext; ein alleinstehendes Bild kann beim Export als Abbildung mit
Bildunterschrift dargestellt werden.

## Codeblöcke

Mit drei Backticks öffnen und schließen. Die Sprache dahinter ermöglicht
Syntaxhervorhebung:

````markdown
```python
print("Hallo Welt")
```
````

## Tabellen

```markdown
| Einstellung | Wert |
| --- | --- |
| Sprache | Deutsch |
| Format | PDF |
```

Mit Doppelpunkten wird die Ausrichtung festgelegt: `:---` links,
`:---:` zentriert und `---:` rechts. Breite Tabellen im PDF prüfen, da dort
nur die Seitenbreite verfügbar ist.

## Zitate und Hinweise

```markdown
> Ein Zitat oder ein wichtiger Hinweis.
>
> Ein weiterer Absatz im selben Zitat.
```

Für einen einfachen Hinweis reicht auch:

```markdown
**Hinweis:** Änderungen werden erst nach einem erfolgreichen Build veröffentlicht.
```

GitHub-spezifische Hinweisblöcke wie `[!NOTE]` werden durch diesen Pandoc-Build
nicht automatisch als gestaltete Hinweisboxen umgesetzt.

## Trennlinie und Sonderzeichen

Eine Trennlinie mit Leerzeilen davor und danach schreiben:

```markdown
---
```

Mit einem Backslash lässt sich Markdown-Syntax als normaler Text anzeigen:

```markdown
\*Dieser Text bleibt mit Sternchen stehen.\*
```

## Fußnoten (Pandoc)

```markdown
Hier steht eine zusätzliche Erläuterung.[^hinweis]

[^hinweis]: Dies ist der Fußnotentext.
```

Fußnoten werden in HTML und PDF unterstützt. Bezeichner im gesamten Dokument
eindeutig wählen, da alle Kapitel zusammengeführt werden.

## Metadaten und neue Kapitel

Titel und Sprache stehen ausschließlich am Anfang von `pages/index.md`:

```yaml
---
title: Technische Dokumentation
lang: de
---
```

Neue Kapitel als `.md` in `pages/` ablegen. Nach `index.md` liest der Build
alle Dateien alphabetisch. Mit Namen wie `01-einleitung.md` und
`02-installation.md` lässt sich die Reihenfolge steuern.
Keinen weiteren YAML-Metadatenblock in Kapiteldateien ergänzen.

## HTML und PDF prüfen

```bash
bash scripts/build.sh
```

Anschließend `_site/index.html` und `_site/dokumentation.pdf` öffnen.
Das Pico-CSS-Theme und die GitHub-Edit-Links gelten für die HTML-Seite.
Das PDF hat ein eigenes Layout. Rohes HTML ist deshalb kein verlässlicher Weg,
um Inhalte für beide Ausgabeformate zu gestalten.
