"""Écrit docs/index.html : la page d'accueil du site du cours (GitHub Pages).

Liste chaque séance, avec un lien vers chaque jeu de diapositives présent dans docs/ et vers
le chapitre du livre correspondant.
"""

from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

SEANCES = [
    ("01", "Installer la plateforme", "Tesla est-elle plus rentable que Ford — et depuis quand ?", "TW"),
    ("02", "Le DataFrame", "Quelles entreprises créent le plus de valeur ?", "TW"),
    ("03", "Importer des données", "Tesla est-elle bonne pour l'environnement ? Monter le dossier", "TW"),
    ("04", "Manipuler les données", "Les fusions-acquisitions créent-elles de la valeur ? Un premier regard", "TW"),
    ("05", "Représenter les données", "L'Amérique crée-t-elle plus de valeur que tout autre pays ?", "TW"),
    ("06", "Statistiques de base", "La R-D rend-elle les entreprises plus rentables ?", "TW"),
    ("07", "Fusions-acquisitions", "Les F&A créent-elles réellement de la valeur ?", "Marie-Ann"),
    ("08", "ESG et écoblanchiment", "Les mieux notés en ESG aident-ils vraiment la planète ?", "Marie-Ann"),
    ("09", "Groupes stratégiques", "Qui sont mes véritables concurrents ?", "Russell"),
    ("10", "Rémunération des dirigeants", "Les incitatifs de long terme poussent-ils à la R-D ?", "Russell"),
    ("11", "Coaching — premiers pas", "Votre question tient-elle debout ?", "Marie-Ann, Russell"),
    ("12", "Présentations (1)", "Vulgariser son sujet en cinq minutes", "Équipe"),
    ("13", "Présentations (2)", "Vulgariser son sujet en cinq minutes", "Équipe"),
]
KINDS = [("pre-seance", "Pré-séance"), ("cours", "Cours"), ("pratique", "Pratique")]


def row(n: str, titre: str, question: str, qui: str) -> str:
    links = [f'<a href="seance-{n}-{k}.html">{label}</a>'
             for k, label in KINDS if (DOCS / f"seance-{n}-{k}.html").exists()]
    if (DOCS / "livre" / f"seance-{n}.html").exists():
        links.append(f'<a href="livre/seance-{n}.html">Chapitre</a>')
    cell = " · ".join(links) if links else '<span class="muted">cas et articles</span>'
    return (f"<tr><td class='n'>{n}</td><td><strong>{html.escape(titre)}</strong>"
            f"<div class='q'>{html.escape(question)}</div></td>"
            f"<td class='who'>{html.escape(qui)}</td><td class='links'>{cell}</td></tr>")


PAGE = """<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MNGT 60439 · Données et stratégie</title>
<style>
:root {{ --paper:#F7F4ED; --ink:#222; --muted:#6B6B67; --red:#E3120B; --blue:#356B8C; --grid:#D8D3C8; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--paper); color:var(--ink);
       font:17px/1.5 'Helvetica Neue', Inter, system-ui, sans-serif; }}
main {{ max-width:1040px; margin:0 auto; padding:48px 16px 64px; }}
h1 {{ font-size:2rem; margin:0 0 .2em; letter-spacing:-.02em; }}
h1::before {{ content:""; display:block; width:3.2rem; height:.32rem; background:var(--red); margin-bottom:.6rem; }}
.sub {{ color:var(--muted); margin:0 0 1.6em; }}
.book {{ display:inline-block; margin:0 0 2em; padding:.6em 1em; border:1px solid var(--grid);
        background:#fff; text-decoration:none; color:var(--ink); }}
.book strong {{ color:var(--blue); }}
table {{ width:100%; border-collapse:collapse; }}
th {{ text-align:left; font-size:.8rem; text-transform:uppercase; letter-spacing:.06em; color:var(--muted);
      border-bottom:2px solid var(--ink); padding:.4em .5em; }}
td {{ border-bottom:1px solid var(--grid); padding:.7em .5em; vertical-align:top; }}
td.n {{ font-weight:700; color:var(--red); width:2.5em; }}
.q {{ color:var(--muted); font-size:.92rem; }}
td.who {{ white-space:nowrap; font-size:.9rem; }}
td.links a {{ color:var(--blue); white-space:nowrap; }}
.muted {{ color:var(--muted); font-size:.9rem; }}
@media (max-width:640px) {{ td.who {{ display:none; }} th.who {{ display:none; }} }}
</style></head>
<body><main>
<h1>Données et stratégie : enjeux locaux et mondiaux</h1>
<p class="sub">MNGT 60439 · HEC Montréal · Marie-Ann, Russell et Thierry Warin, PhD</p>
<a class="book" href="livre/index.html">📖 <strong>Le livre du cours</strong> — <em>Données et stratégie avec Python</em></a>
<table>
<thead><tr><th>#</th><th>Séance</th><th class="who">Qui</th><th>Supports</th></tr></thead>
<tbody>
{rows}
</tbody></table>
</main></body></html>
"""

if __name__ == "__main__":
    DOCS.mkdir(exist_ok=True)
    (DOCS / ".nojekyll").touch()
    (DOCS / "index.html").write_text(PAGE.format(rows="\n".join(row(*s) for s in SEANCES)),
                                     encoding="utf-8")
