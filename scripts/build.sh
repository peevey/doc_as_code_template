#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

for dependency in pandoc xelatex python3; do
  command -v "$dependency" >/dev/null || {
    echo "Fehlendes Werkzeug: $dependency (siehe README.md)" >&2
    exit 1
  }
done

mkdir -p _site/assets/images _site/assets/styles
cp -a assets/images/. _site/assets/images/
cp -a assets/styles/. _site/assets/styles/

# index.md enthält die Metadaten; weitere Dateien folgen alphabetisch.
sources=(pages/index.md)
for chapter in pages/*.md; do
  [[ "$chapter" == "pages/index.md" ]] || sources+=("$chapter")
done

common=(--from=markdown --standalone --toc --toc-depth=3 --number-sections --resource-path=.:pages)

# In Template-Kopien setzt GITHUB_REPOSITORY automatisch das Zielrepository.
repository="${GITHUB_REPOSITORY:-peevey/doc_as_code_template}"
edit_branch="${DOCS_EDIT_BRANCH:-main}"
edit_base="https://github.com/$repository/edit/$edit_branch"
html_source=$(mktemp)
trap 'rm -f "$html_source"' EXIT
python3 scripts/html-source.py "$edit_base" "${sources[@]}" > "$html_source"

pandoc "${common[@]}" "$html_source" \
  --to=html5 \
  --template=scripts/page.html \
  --variable="edit-index-url:$edit_base/pages/index.md" \
  --output=_site/index.html

pandoc "${common[@]}" "${sources[@]}" \
  --pdf-engine=xelatex \
  --variable=papersize:a4 \
  --variable=geometry:margin=25mm \
  --output=_site/dokumentation.pdf

touch _site/.nojekyll
