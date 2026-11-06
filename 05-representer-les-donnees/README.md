# Séance 05 — Représenter les données

> **L'Amérique crée-t-elle plus de valeur que tout autre pays ? Cela dépend de la mesure — et du graphique.**

> **[Diapositives du cours](https://warint.github.io/MNGT60439/seance-05-cours.html)** — ou la source :
> [`01-cours/MGMT60XXX-S05-Cours.qmd`](01-cours/MGMT60XXX-S05-Cours.qmd)

**Date : à confirmer** · 3 h · MGMT 60XXX — Données et stratégie : enjeux locaux et mondiaux

---

## Objectifs d'apprentissage

À la fin de la séance, vous serez capable de :

- Montrer qu'une même affirmation stratégique change de réponse selon la **mesure** retenue, et le dire dans un graphique.
- Expliquer, avec Anscombe (1973), pourquoi on **regarde** les données avant de les résumer.
- Classer les encodages visuels selon Cleveland et McGill (1984), et confier la comparaison principale à la **position**.
- Construire une figure matplotlib complète (`fig, ax`), avec titre-message, unités, source, étiquetage direct, et l'enregistrer avec `savefig`.
- Choisir la forme selon la question : comparaison, évolution, distribution, relation, composition.
- Produire histogrammes, boîtes, nuages, lignes et petits multiples avec **seaborn**, et un nuage interactif et une carte avec **plotly express**.
- Repérer un axe tronqué, un double axe ou un camembert en 3D, et les corriger.

---

## Déroulement

| Temps | Quand | Quoi | Où |
|---|---|---|---|
| **Pré-séance** | Avant le cours | Deux lectures, vérification des paquets, un premier graphique | [`00-pre-seance/`](00-pre-seance/README.md) |
| **Cours** (~90 min) | En classe | Anscombe, Cleveland et McGill, matplotlib, seaborn, plotly, les graphiques qui trompent | [`01-cours/`](01-cours/README.md) |
| **Pratique** (~90 min) | En classe | Le graphique qui défend la manchette, et ceux qui la réfutent | [`02-pratique/`](02-pratique/README.md) |

---

## Données

| Fichier | Contenu | Source |
|---|---|---|
| [`data/pays.csv`](../data/pays.csv) | 217 économies × 2000-2023 : PIB, PIB par habitant, croissance, population, IDE entrants, commerce, R-D, énergie renouvelable | Banque mondiale, API v2 (CC BY 4.0) |
| [`data/entreprises.csv`](../data/entreprises.csv) | 32 grandes entreprises cotées aux États-Unis × 2010-2024 : chiffre d'affaires, résultat net, actifs, R-D | SEC EDGAR (domaine public) |

Rien à télécharger : les deux fichiers sont dans le dépôt.

---

## Livrable

Dans `sorties/` : `fig1.png` à `fig4.png`, `fig5.html`, `note_seance05.md` (200 mots), et votre
copie de `seance05_atelier.py`, qui reproduit tout **en une seule exécution**. Deux minutes de
présentation orale en fin de séance. Ces figures alimentent **« Les premiers pas — travail 2 »**.

---

## Lectures

- Anscombe, F. J. (1973). Graphs in Statistical Analysis. *The American Statistician*, 27(1), 17–21. <https://doi.org/10.1080/00031305.1973.10478966>
- Cleveland, W. S. et McGill, R. (1984). Graphical Perception. *Journal of the American Statistical Association*, 79(387), 531–554. <https://doi.org/10.1080/01621459.1984.10478080>

Chapitre du livre : [`book/seance-05.qmd`](../book/seance-05.qmd).

---

## Avant la prochaine séance

- Gardez vos figures : la séance 6 teste statistiquement ce que vous avez montré.
- Revoyez moyenne, médiane, écart-type et quantiles ; la séance 6 les utilise sans les redéfinir.

---

[← Séance 04 : Manipuler les données](../04-manipuler-les-donnees/README.md) ·
[Séance 06 : Statistiques de base →](../06-statistiques-de-base/README.md)
