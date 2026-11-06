# Séance 02 — Le DataFrame : la table de l'analyste

> **Quelles entreprises créent le plus de valeur ?**

> **Diapositives** — pré-séance : [source](00-pre-seance/MNGT60439-S02-Pre-Seance.qmd) ·
> [rendu](https://warint.github.io/MNGT60439/seance-02-pre-seance.html) ·
> cours : [source](01-cours/MNGT60439-S02-Cours.qmd) · [rendu](https://warint.github.io/MNGT60439/seance-02-cours.html) ·
> pratique : [source](02-pratique/MNGT60439-S02-Pratique.qmd) · [rendu](https://warint.github.io/MNGT60439/seance-02-pratique.html)
>
> **Chapitre du livre :** [`book/seance-02.qmd`](../book/seance-02.qmd)

**Date : à confirmer** · durée 3 h · MNGT 60439 — Données et stratégie : enjeux locaux et mondiaux

---

## Objectifs d'apprentissage

À la fin de la séance, vous saurez :

- Distinguer la **taille** d'une entreprise (résultat net) de sa **performance** (marge nette,
  ROA, ROE) et expliquer pourquoi leurs classements diffèrent.
- Décrire un DataFrame : ses Series, son index, les types de ses colonnes.
- Inspecter un tableau avec `shape`, `info`, `describe` et `value_counts`.
- Sélectionner des colonnes (`[]`, `[[ ]]`) et des lignes (`.loc`, `.iloc`, masques booléens,
  `isin`, `between`, `query`).
- Créer des colonnes, trier (`sort_values`, `nlargest`) et résumer par groupe (`groupby().agg()`).
- Repérer les valeurs manquantes et dire ce qu'elles signifient sur la source.

---

## Déroulement de la séance

| Temps | Quand | Quoi | Où |
|---|---|---|---|
| **Pré-séance** | Avant le cours (~110 min) | Lecture, quatre ratios, premier regard sur les données, autovérification | [`00-pre-seance/`](00-pre-seance/README.md) |
| **Cours** | ~90 min | Le DataFrame de A à Z, démontré en direct sur les données des entreprises | [`01-cours/`](01-cours/README.md) |
| **Pratique** | ~90 min | En équipe de deux : quatre mesures, quatre classements, un choix justifié | [`02-pratique/`](02-pratique/README.md) |

---

## Données

[`data/entreprises.csv`](../data/entreprises.csv) — 32 grandes entreprises cotées aux États-Unis,
exercices 2010 à 2024, montants en millions de dollars US.
Source : SEC EDGAR, API XBRL *companyfacts* (domaine public). Dictionnaire et provenance :
[`data/README.md`](../data/README.md).

## Lectures

- McKinney, W. (2010). *Data Structures for Statistical Computing in Python.* Proceedings of the
  9th Python in Science Conference, 56–61.
  [doi:10.25080/Majora-92bf1922-00a](https://doi.org/10.25080/Majora-92bf1922-00a)
- McKinney, W. (2022). *Python for Data Analysis*, 3ᵉ éd., chapitre 5 (accès libre) :
  <https://wesmckinney.com/book/pandas-basics>

---

## Livrable

Le script de la pratique complété et une note de 200 mots : quelle entreprise crée le plus de
valeur, selon quelle mesure et pourquoi ; ce que vous avez fait des capitaux propres négatifs ; ce
que votre classement ne permet pas d'affirmer ; une réponse de l'IA que vous avez vérifiée.

---

## Avant la prochaine séance

- Pré-séance de la séance 3 : importer des données depuis un CSV, une URL, un paquet, une API et
  une base de données.
- Gardez votre script de la séance 2 : la séance 4 le réutilise pour joindre les entreprises aux
  données des pays.

---

[← Séance 01 : Installer la plateforme](../01-installer-la-plateforme/README.md) ·
[Séance 03 : Importer les données →](../03-importer-les-donnees/README.md)
