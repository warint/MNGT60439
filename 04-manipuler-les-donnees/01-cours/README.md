# Séance 04 — Cours

> **[Ouvrir les diapositives](https://warint.github.io/MNGT60439/seance-04-cours.html)** · source :
> [`MGMT60XXX-S04-Cours.qmd`](MGMT60XXX-S04-Cours.qmd)

| Partie | Contenu |
|---|---|
| 1 | Deux questions de stratégie : les vrais concurrents ; la valeur des F&A |
| 2 | Nettoyer : noms de colonnes, `.str`, `astype`, `pd.to_numeric(errors="coerce")`, doublons, valeurs manquantes (retirer, remplir, signaler) |
| 3 | Joindre : `merge` (`how`, `validate`, `indicator`), compter les lignes ; `concat` |
| 4 | Remodeler : données rangées (Wickham, 2014), `pivot`, `melt`, `pivot_table` |
| 5 | Agréger : `groupby().agg()` (agrégation nommée) et `groupby().transform()` — l'écart au secteur |
| 6 | Le temps : trier, `groupby().shift()`, `pct_change()`, moyenne mobile |
| 7 | Microsoft–Activision et Pfizer–Seagen : un rendement anormal naïf, et ses limites |

Le code des diapositives est **exécuté** au rendu : chaque sortie affichée vient des données du
cours. Les cours boursiers sont téléchargés une fois (Yahoo Finance, via `yfinance`) puis lus
dans `data/cache/`.

Rendu : `scripts/render.sh` (voir le [README principal](../../README.md)).

[← Retour à la séance 04](../README.md)
