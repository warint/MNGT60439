# Séance 03 — Importer des données : CSV, URL, paquets, API, bases de données

> **Tesla est-elle bonne pour l'environnement ? Avant de répondre, il faut monter le dossier de données.**

> **[Ouvrir les diapositives du cours](https://warint.github.io/MNGT60439/seance-03-cours.html)** — ou lire la source :
> [`01-cours/MNGT60439-S03-Cours.qmd`](01-cours/MNGT60439-S03-Cours.qmd).

**Date : à confirmer** · durée 3 h · Thierry Warin, PhD

MNGT 60439 · Données et stratégie : enjeux locaux et mondiaux

---

## Objectifs d'apprentissage

À la fin de la séance, vous saurez :

- Traduire une affirmation stratégique en **liste de données** à réunir, chacune avec sa source.
- Lire un fichier CSV quel que soit son format : `sep`, `decimal`, `encoding`, `usecols`, `dtype`, `nrows`.
- Lire un fichier **en ligne** (URL) et un tableau d'une page web (`pd.read_html`).
- Utiliser un **paquet** qui parle à une source : `yfinance`, `wbgapi`.
- Interroger une **API** avec `requests` : paramètres, en-têtes, code de statut, JSON, pagination.
- Interroger une **base de données** en SQL (`sqlite3`, `pd.read_sql`, DuckDB).
- Mettre ses téléchargements **en cache**, et tenir une **fiche de provenance**.

---

## Déroulement

| Temps | Quand | Quoi | Où |
|---|---|---|---|
| **Pré-séance** | Avant le cours | Lecture, identité SEC, certificats, test des sources | [`00-pre-seance/`](00-pre-seance/README.md) |
| **Cours** (~90 min) | En classe | Cinq façons d'importer, démontrées en direct | [`01-cours/`](01-cours/README.md) |
| **Pratique** (~90 min) | En classe | Monter le dossier « Tesla et l'environnement » | [`02-pratique/`](02-pratique/README.md) |

Diapositives : [pré-séance](https://warint.github.io/MNGT60439/seance-03-pre-seance.html) · [cours](https://warint.github.io/MNGT60439/seance-03-cours.html) · [pratique](https://warint.github.io/MNGT60439/seance-03-pratique.html)
· Chapitre du livre : [`book/seance-03.qmd`](../book/seance-03.qmd)

---

## Données de la séance

| Source | Mode d'accès | Producteur | Licence |
|---|---|---|---|
| `data/entreprises.csv`, `data/entreprises_fr.csv` | Fichier CSV local | SEC EDGAR | Domaine public |
| Émissions de CO₂ | URL d'un CSV | Our World in Data (Global Carbon Project) | CC BY 4.0 |
| Constructeurs automobiles | Tableau HTML | Wikipédia | CC BY-SA 4.0 |
| Cours boursiers TSLA, F, GM | Paquet `yfinance` | Yahoo Finance | Usage personnel, non redistribuable |
| Électricité renouvelable, CO₂ par habitant | API v2, paquet `wbgapi` | Banque mondiale | CC BY 4.0 |
| États financiers de Tesla | API `companyfacts` | SEC EDGAR | Domaine public |
| `data/strategie.db` | Base SQLite | Construite par `scripts/build_course_data.py` | — |

Tout ce qui est téléchargé est copié dans `data/cache/` (non versionné) : après le premier
passage, la pratique fonctionne **sans réseau**.

---

## Livrable

Une archive déposée sur ZoneCours avant minuit, par équipe de deux, qui contient
`sorties/dossier_tesla/` : les fichiers CSV, **`PROVENANCE.md`** (une ligne par source :
producteur, accès, date, unité, licence, dernière année) et **`NOTE.md`** (150 mots : ce que les
données permettent et ne permettent pas d'affirmer), plus le script complété.

---

## Avant la prochaine séance

- Lire Wickham (2014), *Tidy Data* — <https://doi.org/10.18637/jss.v059.i10>, sections 1 à 3.
- Garder votre `data/cache/` : la séance 4 fusionne ces sources en un seul tableau.

---

[<- Séance 02 : Le DataFrame](../02-le-dataframe/README.md) · [Séance 04 : Manipuler les données ->](../04-manipuler-les-donnees/README.md)
