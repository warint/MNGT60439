# Séance 01 — Installer la plateforme

> **Une manchette dit que Tesla est bonne pour l'environnement. Que faudrait-il mesurer pour le vérifier — et avec quel outil ?**

> **[Diapositives du cours](https://warint.github.io/MNGT60439/seance-01-cours.html)** — source :
> [`01-cours/MNGT60439-S01-Cours.qmd`](01-cours/MNGT60439-S01-Cours.qmd) ·
> **[Chapitre 1 du livre](https://warint.github.io/MNGT60439/livre/seance-01.html)**

**Date : à confirmer** · durée 3 h · Thierry Warin

MNGT 60439 — Données et stratégie : enjeux locaux et mondiaux

---

## Objectifs

À la fin de la séance, vous saurez :

- Transformer une affirmation de la presse d'affaires en **question mesurable**, et dire quelles
  données y répondraient.
- Expliquer ce que sont **Python**, un **paquet**, un **environnement virtuel** et **VS Code**,
  et à quoi sert chacun.
- Écrire des variables, des listes, des dictionnaires et une fonction.
- Lire un fichier CSV dans un **DataFrame** pandas et en afficher la structure.
- Produire un premier graphique et l'enregistrer.
- Utiliser l'IA générative pour **expliquer** du code, et déclarer ce que vous avez vérifié.

---

## Déroulement

| Temps | Quand | Quoi | Où |
|---|---|---|---|
| **Pré-séance** | Avant le cours | Lecture, installation, vérification, autovérification | [`00-pre-seance/`](00-pre-seance/README.md) |
| **Cours** (~90 min) | En classe | La plateforme, Python en vingt minutes, le premier DataFrame, l'IA | [`01-cours/`](01-cours/README.md) |
| **Pratique** (~90 min) | En classe | *Tesla est-elle plus rentable que Ford — et depuis quand ?* | [`02-pratique/`](02-pratique/README.md) |

La pré-séance **n'est pas facultative** : la pratique commence par la vérification de votre
installation.

---

## Données

| Fichier | Contenu | Source |
|---|---|---|
| `data/entreprises.csv` | 32 grandes entreprises cotées aux États-Unis × exercices 2010–2024 | SEC EDGAR (domaine public) |

Dictionnaire des variables : [`data/README.md`](../data/README.md).

---

## Livrable

`seance01_atelier.py` (s'exécute de haut en bas) et `seance01_marges.png`, déposés sur
ZoneCours. Non noté ; compte pour la participation.

---

## Avant la prochaine séance

- Pré-séance de la [séance 02](../02-le-dataframe/README.md).
- Relire `seance01_atelier.py` et le commenter, ligne par ligne, **sans** l'IA.

---

[Séance 02 : Le DataFrame →](../02-le-dataframe/README.md)
