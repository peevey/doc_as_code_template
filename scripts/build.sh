#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

for dependency in pandoc xelatex python3; do
  command -v "$dependency" >/dev/null || {
    echo "Fehlendes Werkzeug: $dependency (siehe README.md)" >&2
    exit 1
  }
done

mkdir -p _site/assets/images _site/assets/styles _site/assets/scripts
cp -a assets/images/. _site/assets/images/
cp -a assets/styles/. _site/assets/styles/
cp -a assets/scripts/. _site/assets/scripts/

# index.md enthält die Metadaten; weitere Dateien folgen alphabetisch.
sources=(pages/index.md)
for chapter in pages/*.md; do
  [[ "$chapter" == "pages/index.md" ]] || sources+=("$chapter")
done

common=(--from=markdown --standalone --toc --toc-depth=3 --number-sections --resource-path=.:pages)

python3 scripts/build-html.py

pandoc "${common[@]}" "${sources[@]}" \
  --pdf-engine=xelatex \
  --variable=papersize:a4 \
  --variable=geometry:margin=25mm \
  --output=_site/dokumentation.pdf

touch _site/.nojekyll
