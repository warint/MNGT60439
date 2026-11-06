# MNGT 60439 — Données et stratégie : enjeux locaux et mondiaux

**HEC Montréal** · Marie-Ann, Russell et Thierry Warin, PhD

> *Une manchette affirme que Tesla est bonne pour l'environnement, que l'Amérique crée plus de
> valeur que tout autre pays, que les fusions créent de la valeur. Que faudrait-il mesurer pour
> le savoir — et que les données ne permettront jamais de conclure ?*

Ce cours apprend à poser une question de stratégie à des données réelles, à y répondre avec
rigueur, et à dire honnêtement où s'arrête la réponse. Les six premières séances donnent les
outils (Python) ; les cinq suivantes les mettent au service de questions de recherche, à partir
d'articles et d'études de cas ; les deux dernières sont celles des étudiant·es.

📖 **[Le livre du cours : *Données et stratégie avec Python*](https://warint.github.io/MNGT60439/livre/index.html)** ·
📋 **[Plan de cours](PLAN-DE-COURS.md)** · 🗂️ **[Les données](data/README.md)**

---

## Les séances

Chaque séance suit **trois temps** : une **pré-séance** (lecture, installation, données,
autovérification), un **cours** (~90 min) et une **pratique** (~90 min).

| # | Séance | Question | Qui | Format |
|---|---|---|---|---|
| 01 | [Installer la plateforme](01-installer-la-plateforme/README.md) | Tesla est-elle plus rentable que Ford — et depuis quand ? | TW | Python |
| 02 | [Le DataFrame](02-le-dataframe/README.md) | Quelles entreprises créent le plus de valeur ? | TW | Python |
| 03 | [Importer des données](03-importer-les-donnees/README.md) | Tesla est-elle bonne pour l'environnement ? Monter le dossier | TW | Python |
| 04 | [Manipuler les données](04-manipuler-les-donnees/README.md) | Les fusions-acquisitions créent-elles de la valeur ? Un premier regard | TW | Python |
| 05 | [Représenter les données](05-representer-les-donnees/README.md) | L'Amérique crée-t-elle plus de valeur que tout autre pays ? | TW | Python |
| 06 | [Statistiques de base](06-statistiques-de-base/README.md) | La R-D rend-elle les entreprises plus rentables ? | TW | Python |
| 07 | [Fusions-acquisitions](07-cas-fusions-acquisitions/README.md) | Les F&A créent-elles réellement de la valeur ? | Marie-Ann | Article + cas |
| 08 | [ESG et écoblanchiment](08-cas-esg-ecoblanchiment/README.md) | Les mieux notés en ESG aident-ils vraiment la planète ? | Marie-Ann | Article + cas |
| 09 | [Groupes stratégiques](09-cas-groupes-strategiques/README.md) | Qui sont mes véritables concurrents ? | Russell | Article + cas |
| 10 | [Rémunération des dirigeants](10-cas-remuneration-dirigeants/README.md) | Les incitatifs de long terme poussent-ils à la R-D ? | Russell | Article + cas |
| 11 | [Coaching — premiers pas](11-coaching-premiers-pas/README.md) | Votre question tient-elle debout ? | Marie-Ann, Russell | Rencontres |
| 12 | [Présentations (1)](12-presentations-1/README.md) | Vulgariser son sujet en cinq minutes | Équipe | Présentations |
| 13 | [Présentations (2)](13-presentations-2/README.md) | Vulgariser son sujet en cinq minutes | Équipe | Présentations |

Les dossiers 07 à 13 contiennent la même structure (pré-séance, cours, pratique), avec des
emplacements **à compléter** par les enseignant·es responsables.

---

## Démarrer (étudiant·es)

1. Installez **Python 3.12 ou 3.13** et **VS Code** — voir la
   [pré-séance 01](01-installer-la-plateforme/00-pre-seance/README.md).
2. Téléchargez ce dépôt (**Code → Download ZIP**, ou `git clone https://github.com/warint/MNGT60439.git`), puis, dans le dossier :

```bash
python3 -m venv .venv                    # Windows : py -m venv .venv
source .venv/bin/activate                # Windows : .venv\Scripts\activate
python -m pip install -r requirements.txt
python 01-installer-la-plateforme/00-pre-seance/verifier_environnement.py
```

---

## Organisation du dépôt

```text
NN-nom-de-la-seance/
├── README.md                ← la page d'accueil de la séance
├── 00-pre-seance/           ← lecture, installation, données, autovérification (+ diapositives)
├── 01-cours/                ← diapositives du cours (Quarto → reveal.js), code exécuté
└── 02-pratique/             ← diapositives de l'atelier + starter/ (script de départ)
book/                        ← le livre (Quarto book), un chapitre par séance Python
data/                        ← données réelles du cours (SEC EDGAR, Banque mondiale) + SQLite
docs/                        ← le site rendu : diapositives et livre (GitHub Pages)
scripts/                     ← construction des données et rendu
slides/                      ← thème des diapositives et style des graphiques
```

## Construire (enseignant·es)

```bash
source .venv/bin/activate
python -m ipykernel install --user --name mngt60439      # une fois : le noyau des diapositives
scripts/render.sh            # toutes les diapositives et le livre → docs/
scripts/render.sh livre      # le livre seulement
scripts/render.sh 03         # les diapositives de la séance 03 seulement
python scripts/build_course_data.py   # reconstruire data/ depuis la SEC et la Banque mondiale
```

Exige [Quarto](https://quarto.org) ≥ 1.5 et, pour le PDF du livre, une distribution LaTeX avec
`xelatex`.

---

## Licences

Textes, diapositives et code : © Thierry Warin — licence à préciser. Données : voir [`data/README.md`](data/README.md) (SEC EDGAR — domaine public ;
Banque mondiale — CC BY 4.0).
