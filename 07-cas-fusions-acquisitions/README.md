# Séance 07 — Création et destruction de valeur : les fusions-acquisitions

> **Les fusions et acquisitions créent-elles réellement de la valeur économique ?**

**Date : à confirmer** · durée 3 h · Marie-Ann

MNGT 60439 — Données et stratégie : enjeux locaux et mondiaux

---

## Thèmes

- Performance de marché : rendement *buy-and-hold*, rendement total pour l'actionnaire, Q de Tobin
- Performance comptable : ROA, ROS
- Logique de l'étude d'événement (rendements anormaux autour d'une annonce)

## Déroulement

| Temps | Quand | Quoi | Où |
|---|---|---|---|
| **Pré-séance** | Avant le cours | Lire le cas et l'article ; préparer les questions | [`00-pre-seance/`](00-pre-seance/README.md) |
| **Cours** (~90 min) | En classe | Cadre conceptuel et méthode | [`01-cours/`](01-cours/README.md) |
| **Pratique** (~90 min) | En classe | Discussion du cas, en équipes puis en plénière | [`02-pratique/`](02-pratique/README.md) |

## Références clés

- MacKinlay, A. C. (1997). Event Studies in Economics and Finance. *Journal of Economic Literature*, 35(1), 13–39.
- Kengelbach, J. et al. (2023). *Bold Moves for Dealmakers in Volatile Markets* — 2023 M&A Report (BCG).

## Lien avec les séances Python

La séance 04 a calculé un premier rendement « ajusté du marché » autour de l'annonce Microsoft–Activision : c'est le point de départ de l'étude d'événement.

## Montrer les résultats : la galerie PyStatlas

> Proposition de l'équipe Python, à reprendre librement par l'enseignant·e. Les graphiques se
> construisent comme aux séances 5 et 6 : trouver le graphique, copier le script, remplacer les
> données, réécrire les textes.

| Question du cas | Graphique de la galerie | L'exemple de la galerie (à remplacer par vos opérations) |
|---|---|---|
| Comment se répartissent les rendements anormaux cumulés (RAC) autour de l'annonce ? | [Histogramme avec densité](https://warint.github.io/pystatlas/fr/distributions/histogram-density/) | fécondité des pays en 2011 |
| Les RAC des acquéreurs et des cibles diffèrent-ils ? | [Nuage de pluie](https://warint.github.io/pystatlas/fr/distributions/raincloud/) ou [graphique d'estimation](https://warint.github.io/pystatlas/fr/group-comparisons/estimation-plot/) | durée au pouvoir selon le régime ; criminalité des États pauvres et moins pauvres |
| Le RAC moyen est-il différent de zéro, et avec quelle précision ? | [Distribution bootstrap](https://warint.github.io/pystatlas/fr/inference-uncertainty/bootstrap-distribution/) | corrélation criminalité–familles monoparentales |
| Quelle part des opérations crée de la valeur (RAC > 0), par secteur ou par année ? | [Proportions avec intervalles de confiance](https://warint.github.io/pystatlas/fr/proportions-surveys/proportions-with-ci/) | enquête Redbook de 1974 |
| Le ROA ou le ROS des mêmes entreprises change-t-il entre avant et après l'opération ? | [Comparaison intra-sujets](https://warint.github.io/pystatlas/fr/group-comparisons/within-subjects/) | fécondité des mêmes pays en 1970, 1990 et 2010 |
| Qu'est-ce qui explique le RAC : taille relative, mode de paiement, secteur ? | [Graphique de coefficients](https://warint.github.io/pystatlas/fr/regression-models/coefficient-plot/) | ce qui prédit la criminalité violente des États |
| La réussite (RAC > 0) dépend-elle du mode de paiement ou du secteur ? | [Rapports de cotes](https://warint.github.io/pystatlas/fr/regression-models/odds-ratio-forest/) | enquête Redbook de 1974 |

Points de vigilance propres aux F&A, à rappeler en montrant ces graphiques : les opérations d'une
même année ne sont pas indépendantes (chocs de marché communs), la fenêtre d'événement se fixe
**avant** de regarder les résultats, et un RAC moyen proche de zéro peut cacher une forte
dispersion — d'où l'intérêt des graphiques qui montrent chaque opération.

Références des données des exemples : [Sources des données](https://warint.github.io/pystatlas/fr/about.html#data).

---

[← Séance précédente](../06-statistiques-de-base/README.md) · [Séance suivante →](../08-cas-esg-ecoblanchiment/README.md)
