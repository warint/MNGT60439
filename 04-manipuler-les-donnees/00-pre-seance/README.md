# Séance 04 — Préparation (pré-séance)

> **[Diapositives de la pré-séance](https://warint.github.io/MNGT60439/seance-04-pre-seance.html)** ·
> source : [`MNGT60439-S04-Pre-Seance.qmd`](MNGT60439-S04-Pre-Seance.qmd)

> Faites **les quatre étapes** avant le cours. Prévoyez environ 90 minutes.

| | Avant le cours | Durée | Sert, en classe, à |
|---|---|---|---|
| **1** | Lire Wickham (2014), sections 1 à 3 | 45 min | la partie « Remodeler » du cours |
| **2** | Revoir quatre notions | 15 min | tout le cours |
| **3** | Mettre les cours boursiers en cache | 10 min | la partie 5 de la pratique |
| **4** | Faire l'autovérification | 20 min | le cours |

---

## Étape 1 — Lecture

**Wickham, H. (2014). *Tidy Data*.** *Journal of Statistical Software*, 59(10), 1–23.
<https://doi.org/10.18637/jss.v059.i10> (accès libre)

Les exemples sont en R : lisez pour l'**argument**. Annotez : (1) les trois règles des données
« rangées » ; (2) les cinq problèmes les plus courants des données en désordre ; (3) un tableau
que vous avez déjà rencontré (rapport annuel, Excel, Statistique Canada) qui viole une règle ;
(4) pourquoi ranger *avant* d'analyser fait gagner du temps.

## Étape 2 — Notions à revoir

- **Clé** : les colonnes qui identifient une ligne de façon unique — (`ticker`, `annee`) dans
  `data/entreprises.csv`.
- **Jointure** : associer deux tables par leur clé. Que se passe-t-il si une clé apparaît deux
  fois d'un côté ?
- **Format long / format large** : une ligne par entreprise × année, ou une colonne par année ?
- **Rendement** : $r_t = P_t / P_{t-1} - 1$ ; pourquoi n'existe-t-il pas pour le premier jour ?

## Étape 3 — Mettre les cours boursiers en cache

Depuis la racine du dépôt, `.venv` activé :

```python
from pathlib import Path
import pandas as pd
import yfinance as yf

Path("data/cache").mkdir(parents=True, exist_ok=True)
for t in ["SPY", "MSFT", "PFE", "JNJ", "XOM", "CVX", "AMZN", "INTC", "MRK"]:
    d = yf.download(t, start="2021-06-01", end="2023-12-31", progress=False, auto_adjust=True)
    d.columns = [c[0] if isinstance(c, tuple) else c for c in d.columns]
    d.to_parquet(f"data/cache/{t}.parquet")
    print(t, d.shape)
```

Chaque ligne doit afficher environ 650 jours de Bourse. `data/cache/` n'est pas versionné.
Sur macOS, `CERTIFICATE_VERIFY_FAILED` se règle comme à la séance 1.

## Étape 4 — Autovérification

Par écrit ; non remise, mais supposée faite.

1. `pd.to_numeric(["12", "n.d.", "3,5"], errors="coerce")` : que renvoie-t-il ? Pourquoi
   `"3,5"` pose-t-il problème ?
2. Une table de 480 lignes est jointe (`how="left"`) à une table où une clé apparaît deux fois.
   Combien de lignes peut-on obtenir ? Comment `validate="m:1"` vous protège-t-il ?
3. Un tableau a une colonne par année de 2000 à 2023 et une ligne par pays (217 pays). Combien
   de lignes après `melt` ?
4. Pourquoi `df["chiffre_affaires"].pct_change()` sur tout le panel donne-t-il une croissance
   absurde pour la première année de chaque entreprise ?

## L'IA générative pour se préparer

- « Explique la différence entre `groupby().agg()` et `groupby().transform()` avec un exemple de
  six lignes. »
- « Donne-moi trois façons dont un `merge` pandas peut multiplier les lignes sans erreur, et
  comment les détecter. »
- « Pose-moi cinq questions pour vérifier que je comprends `melt` et `pivot`. »

> **Règle permanente du cours.** Chaque usage de l'IA dans un travail remis est déclaré : ce que
> vous avez demandé, ce que vous avez vérifié, et comment.

---

[← Retour à la séance 04](../README.md)
