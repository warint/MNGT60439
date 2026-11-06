# Séance 03 — Cours

> **[Ouvrir les diapositives](https://warint.github.io/MNGT60439/seance-03-cours.html)** · source : [`MGMT60XXX-S03-Cours.qmd`](MGMT60XXX-S03-Cours.qmd)

| Bloc | Contenu | Durée |
|---|---|---|
| 1 | Une question, cinq sources : le dossier « Tesla et l'environnement » | 5 min |
| 2 | CSV local : `sep`, `decimal`, `encoding`, `usecols`, `dtype`, `nrows` ; Excel | 15 min |
| 3 | URL : Our World in Data, `read_html` ; le cache ; le piège des certificats macOS | 15 min |
| 4 | Paquets : `yfinance`, `wbgapi` | 10 min |
| 5 | API : `requests`, JSON, pagination, SEC EDGAR, clés d'API | 20 min |
| 6 | Bases de données : SQLite, `SELECT`/`WHERE`/`GROUP BY`/`JOIN`, paramètres, DuckDB | 20 min |
| 7 | Sauvegarder (CSV ou parquet), cache, fiche de provenance | 5 min |

Le code des diapositives s'exécute depuis la **racine du dépôt**. Pour le rendre :

```bash
cd 03-importer-les-donnees/01-cours
quarto render MGMT60XXX-S03-Cours.qmd
```

Le rendu télécharge les sources une seule fois dans `data/cache/` ; les rendus suivants les relisent.

[Retour à la séance 03](../README.md)
