# Séance 04 — Manipuler les données

> **Qui sont les vrais concurrents d'une entreprise — et les fusions-acquisitions créent-elles de la valeur ? Avant de répondre, il faut fabriquer des données qui le permettent.**

> **[Diapositives du cours](https://warint.github.io/MNGT60439/seance-04-cours.html)** — source :
> [`01-cours/MNGT60439-S04-Cours.qmd`](01-cours/MNGT60439-S04-Cours.qmd) ·
> **[Chapitre 4 du livre](https://warint.github.io/MNGT60439/livre/seance-04.html)**

**Date : à confirmer** · durée 3 h · Thierry Warin

MNGT 60439 — Données et stratégie : enjeux locaux et mondiaux

---

## Objectifs

À la fin de la séance, vous saurez :

- **Nettoyer** une table : noms de colonnes, texte (`.str`), types (`astype`,
  `pd.to_numeric(errors="coerce")`), doublons.
- Choisir entre **retirer, remplir et signaler** une valeur manquante — et justifier ce choix.
- **Joindre** deux tables avec `merge`, en contrôlant la relation (`validate=`) et ce qui ne
  correspond pas (`indicator=`) ; **empiler** avec `concat`.
- **Remodeler** entre format long et format large (`pivot`, `pivot_table`, `melt`).
- **Agréger** (`groupby().agg()`) et **comparer chaque observation à son groupe**
  (`groupby().transform()`).
- Calculer des variations **par entité** dans un panel (`shift`, `pct_change`, `rolling`).
- Calculer un rendement anormal naïf autour d'une annonce d'acquisition, et dire pourquoi ce
  n'est pas une étude d'événement.

---

## Déroulement

| Temps | Quand | Quoi | Où |
|---|---|---|---|
| **Pré-séance** | Avant le cours | Wickham (2014), notions, cours boursiers en cache, autovérification | [`00-pre-seance/`](00-pre-seance/README.md) |
| **Cours** (~90 min) | En classe | Nettoyer, joindre, remodeler, agréger, le temps ; Microsoft–Activision | [`01-cours/`](01-cours/README.md) |
| **Pratique** (~90 min) | En classe | *Qui sont les vrais concurrents de mon entreprise — et que dit la Bourse de ses acquisitions ?* | [`02-pratique/`](02-pratique/README.md) |

---

## Données

| Fichier | Contenu | Source |
|---|---|---|
| `data/entreprises.csv` | 32 grandes entreprises cotées aux États-Unis × exercices 2010–2024 | SEC EDGAR (domaine public) |
| `data/secteurs.csv` | Description des neuf secteurs | Cours |
| `data/pays.csv` | 217 pays × 2000–2023 : PIB, IDE, commerce, R-D… | Banque mondiale (CC BY 4.0) |
| `data/cache/*.parquet` | Cours quotidiens ajustés (SPY, MSFT, PFE…), 2021-2023 | Yahoo Finance via `yfinance` — téléchargés localement, jamais versionnés |
| `02-pratique/donnees/annonces_fa.csv` | Neuf annonces de F&A, volontairement mal saisies | Communiqués des acquéreurs |

Dictionnaire des variables : [`data/README.md`](../data/README.md).

---

## Livrable

`seance04_atelier.py` (s'exécute de haut en bas) et `sorties/seance04_car.png`, déposés sur
ZoneCours. Non noté ; compte pour la participation.

---

## Avant la prochaine séance

- Pré-séance de la [séance 05](../05-representer-les-donnees/README.md).
- Reprenez votre tableau d'écart au secteur : quel graphique le montrerait le mieux ? Esquissez-le
  à la main.

---

[← Séance 03 : Importer les données](../03-importer-les-donnees/README.md) ·
[Séance 05 : Représenter les données →](../05-representer-les-donnees/README.md)
