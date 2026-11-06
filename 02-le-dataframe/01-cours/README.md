# Séance 02 — Cours (première moitié, ~90 min)

> **Diapositives :** [`MNGT60439-S02-Cours.qmd`](MNGT60439-S02-Cours.qmd) ·
> version rendue : [`docs/seance-02-cours.html`](https://warint.github.io/MNGT60439/seance-02-cours.html)

## La question

> **Quelles entreprises créent le plus de valeur ?**

Le cours montre qu'il n'y a pas une réponse, mais quatre — résultat net, marge nette, ROA, ROE —
et donne les outils pandas pour calculer chacune, les comparer et voir où elles se contredisent.

## Déroulement

| Bloc | Contenu | Outils pandas |
|---|---|---|
| 1 | « Créer de la valeur » : quatre mesures | — |
| 2 | L'anatomie d'un DataFrame | `Series`, `DataFrame`, `index`, `dtypes`, `set_index` |
| 3 | Regarder avant de calculer | `shape`, `info`, `describe`, `nunique`, `value_counts` |
| 4 | Sélectionner | `[]`, `[[ ]]`, `.loc`, `.iloc` |
| 5 | Filtrer | masques booléens, `&` `\|` `~`, `isin`, `between`, `query` |
| 6 | Trier et classer | `sort_values`, `nlargest` |
| 7 | Créer des colonnes | division de colonnes, `assign`, copie à l'écriture (pandas 3) |
| 8 | Résumer par groupe | `groupby`, `.agg(nom=(colonne, fonction))` |
| 9 | Les valeurs manquantes | `isna`, `notna`, `skipna`, `fillna` |

## Trois choses à retenir

1. **Vérifiez la forme** d'un résultat après chaque opération : un filtre vide ne lève pas d'erreur.
2. **Regardez le dénominateur** avant d'interpréter un ratio : des capitaux propres négatifs
   rendent le ROE absurde.
3. **Une valeur manquante est une information** : la R-D absente des détaillants n'est pas une R-D
   nulle.

## Données

[`data/entreprises.csv`](../../data/entreprises.csv) — 32 entreprises cotées aux États-Unis,
exercices 2010-2024, en millions de dollars US (SEC EDGAR). Dictionnaire :
[`data/README.md`](../../data/README.md).

---

[← Retour à la séance 02](../README.md)
