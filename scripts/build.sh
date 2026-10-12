#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

mkdir -p _site/assets/images
cp -a assets/images/. _site/assets/images/

asciidoctor --failure-level WARN \
  -a imagesdir=assets/images \
  -a pdf-download=dokumentation.pdf \
  -o _site/index.html \
  pages/index.adoc

asciidoctor-pdf --failure-level WARN \
  -o _site/dokumentation.pdf \
  pages/index.adoc

touch _site/.nojekyll
