# Séance 02 — Pré-séance

> **Diapositives :** [`MGMT60XXX-S02-Pre-Seance.qmd`](MGMT60XXX-S02-Pre-Seance.qmd) ·
> version rendue : [`docs/seance-02-pre-seance.html`](https://warint.github.io/MNGT60439/seance-02-pre-seance.html)

> Faites **les quatre étapes** avant le cours. Comptez environ 110 minutes.

| | Avant le cours | Durée | Sert, en pratique, à… |
|---|---|---|---|
| **1** | Lire McKinney (2010) et le chapitre 5 de *Python for Data Analysis* | 60 min | comprendre ce qu'est un DataFrame |
| **2** | Revoir quatre ratios de gestion | 15 min | les calculer en classe |
| **3** | Ouvrir `data/entreprises.csv` | 20 min | arriver en connaissant les données |
| **4** | Autovérification | 15 min | savoir ce qui vous bloque |

---

## Étape 1 — Lire

- **McKinney, W. (2010).** *Data Structures for Statistical Computing in Python.* Proceedings of
  the 9th Python in Science Conference, 56–61.
  [doi:10.25080/Majora-92bf1922-00a](https://doi.org/10.25080/Majora-92bf1922-00a)
- **McKinney, W. (2022).** *Python for Data Analysis*, 3ᵉ éd., O'Reilly — chapitre 5,
  en accès libre : <https://wesmckinney.com/book/pandas-basics>

Annotez trois choses : la différence entre une Series et un DataFrame ; le rôle de l'index ;
un exemple du chapitre que vous pourriez refaire avec des entreprises.

## Étape 2 — Quatre notions de gestion

| Ratio | Formule |
|---|---|
| Marge nette | résultat net / chiffre d'affaires |
| ROA | résultat net / actifs totaux |
| ROE | résultat net / capitaux propres |
| Intensité R-D | dépenses de R-D / chiffre d'affaires |

## Étape 3 — Ouvrir les données

À la racine du dépôt, `.venv` activé :

```python
import pandas as pd

entreprises = pd.read_csv("data/entreprises.csv")
print(entreprises.shape)          # (480, 12)
print(entreprises.head())
print(entreprises["secteur"].value_counts())
```

Notez trois observations (valeurs manquantes, unités, ce que représente une ligne).
Le dictionnaire des variables est dans [`data/README.md`](../../data/README.md).

## Étape 4 — Autovérification

1. `df["ventes"]` et `df[["ventes"]]` : quelle différence de type, et pourquoi ?
2. Pourquoi écrit-on `(a > 0) & (b < 5)` et non `a > 0 and b < 5` ?
3. Une entreprise a des capitaux propres négatifs et un profit positif. Que vaut son ROE, et que
   vaut-il comme information ?
4. Walmart n'a aucune valeur dans la colonne `rd`. Doit-on la remplacer par 0 ?

## L'IA générative pour se préparer

- « Explique la différence entre `.loc` et `.iloc` dans pandas avec un tableau de trois
  entreprises. »
- « Pose-moi cinq questions sur `groupby`, une à la fois, et corrige mes réponses. »

> **Règle permanente du cours.** Chaque fois que l'IA intervient dans un travail remis, indiquez
> ce que vous lui avez demandé et ce que vous avez vérifié, et comment.

---

[← Retour à la séance 02](../README.md)
