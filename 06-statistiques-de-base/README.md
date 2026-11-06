# Séance 06 — Statistiques de base : décrire, comparer, relier

> **Les entreprises qui investissent en R-D sont-elles plus rentables ? Et Tesla l'est-elle plus que Ford — de combien, et avec quelle certitude ?**

> **[Diapositives du cours](https://warint.github.io/MNGT60439/seance-06-cours.html)** — source :
> [`01-cours/MGMT60XXX-S06-Cours.qmd`](01-cours/MGMT60XXX-S06-Cours.qmd) ·
> **[Chapitre 6 du livre](https://warint.github.io/MNGT60439/livre/seance-06.html)**

**Date : à confirmer** · durée 3 h · Thierry Warin

MGMT 60XXX — Données et stratégie : enjeux locaux et mondiaux

---

## Objectifs

À la fin de la séance, vous saurez :

- Décrire une variable par son **centre**, sa **dispersion** et sa **forme**, et choisir entre
  moyenne et médiane.
- Calculer une **erreur type** et un **intervalle de confiance à 95 %**, par formule et par
  bootstrap.
- Comparer deux groupes avec un **test t de Welch**, et deux séries appariées avec un **test t
  apparié**.
- Lire une **valeur p** sans lui faire dire ce qu'elle ne dit pas (déclaration de l'ASA).
- Mesurer une relation avec les corrélations de **Pearson** et de **Spearman**.
- Estimer et lire une **régression simple** avec `statsmodels`, avec et sans contrôle du secteur.
- Reconnaître deux pièges : la **variable confondante** et les **observations non indépendantes**
  d'un panel.

---

## Déroulement

| Temps | Quand | Quoi | Où |
|---|---|---|---|
| **Pré-séance** | Avant le cours | Lecture (ASA), cinq notions, données, autovérification | [`00-pre-seance/`](00-pre-seance/README.md) |
| **Cours** (~90 min) | En classe | Décrire, l'incertitude, comparer, relier, la régression, corrélation ≠ causalité | [`01-cours/`](01-cours/README.md) |
| **Pratique** (~90 min) | En classe | *Les entreprises qui investissent en R-D sont-elles plus rentables ?* | [`02-pratique/`](02-pratique/README.md) |

---

## Données

| Fichier | Contenu | Source |
|---|---|---|
| `data/entreprises.csv` | 32 grandes entreprises cotées aux États-Unis × exercices 2010–2024 | SEC EDGAR (domaine public) |
| `data/pays.csv` | 217 pays × 2000–2023 (pour le travail 2) | Banque mondiale (CC BY 4.0) |

Indicateurs construits pendant la séance : `roa` (résultat net / actifs), `marge` (résultat net /
ventes), `intensite_rd` (R-D / ventes). Dictionnaire : [`data/README.md`](../data/README.md).

---

## Livrables

- **Pratique** : `seance06_atelier.py` complété et `reponse.md` (200 mots), sur ZoneCours. Compte
  pour la participation.
- **Les premiers pas — travail 2** (5 %, équipes de deux) : consigne et grille dans
  [`PREMIERS-PAS-TRAVAIL-2.md`](PREMIERS-PAS-TRAVAIL-2.md). Date de remise : à confirmer.

---

## Avant la prochaine séance

- Pré-séance de la [séance 07](../07-cas-fusions-acquisitions/README.md) : les séances 7 à 11 passent
  aux articles de recherche et aux études de cas.
- Avancer le travail 2 : la question de recherche et la source de données doivent être fixées
  **avant** de calculer le moindre test.

---

[← Séance 05 : Représenter les données](../05-representer-les-donnees/README.md) ·
[Séance 07 : Fusions et acquisitions →](../07-cas-fusions-acquisitions/README.md)
