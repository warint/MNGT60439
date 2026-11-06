#!/usr/bin/env bash
# Rend les diapositives et le livre dans docs/ (servi par GitHub Pages).
#
#   scripts/render.sh          tout
#   scripts/render.sh livre    le livre seulement
#   scripts/render.sh 03       les trois jeux de diapositives de la séance 03
#
# Exige : .venv avec requirements.txt, le noyau Jupyter « mgmt60xxx », Quarto.
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT=$(pwd)

PY="$ROOT/.venv/bin/python"
export QUARTO_PYTHON="$PY"
# macOS + python.org : sans ceci, pandas ne lit pas les URL https (voir séance 01).
export SSL_CERT_FILE="$("$PY" -c 'import certifi; print(certifi.where())')"

mkdir -p docs

render_decks() {
  local n="$1"
  for dir in "$ROOT"/"$n"-*/; do
    for qmd in "$dir"00-pre-seance/*.qmd "$dir"01-cours/*.qmd "$dir"02-pratique/*.qmd; do
      [ -f "$qmd" ] || continue
      local kind
      case "$qmd" in
        *Pre-Seance*) kind="pre-seance" ;;
        *Cours*)      kind="cours" ;;
        *Pratique*)   kind="pratique" ;;
        *) continue ;;
      esac
      echo "→ séance $n · $kind"
      (cd "$(dirname "$qmd")" && quarto render "$(basename "$qmd")" --quiet)
      mv "${qmd%.qmd}.html" "docs/seance-$n-$kind.html"
    done
  done
}

render_book() {
  # Le PDF d'abord : un rendu PDF seul efface les pages HTML déjà présentes dans docs/livre.
  echo "→ livre (PDF)"
  (cd book && quarto render --to pdf --quiet) || echo "   (PDF ignoré : xelatex indisponible ou erreur LaTeX)"
  echo "→ livre (HTML)"
  (cd book && quarto render --to html --quiet)
}

case "${1:-tout}" in
  livre) render_book ;;
  tout)
    for n in 01 02 03 04 05 06; do render_decks "$n"; done
    render_book ;;
  *) render_decks "$1" ;;
esac

"$PY" scripts/build_index.py
echo "Terminé : docs/index.html"
