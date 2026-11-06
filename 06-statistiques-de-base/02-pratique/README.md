# Séance 06 — Pratique

> **[Ouvrir les diapositives](https://warint.github.io/MNGT60439/seance-06-pratique.html)** · source :
> [`MNGT60439-S06-Pratique.qmd`](MNGT60439-S06-Pratique.qmd)

**Question :** *Les entreprises qui investissent en R-D sont-elles plus rentables ?*

Fichier de départ : [`starter/seance06_atelier.py`](starter/seance06_atelier.py), à exécuter
depuis la racine du dépôt. Il ne s'exécute pas tant que les `...` ne sont pas remplacés : c'est
voulu ; avancez cellule par cellule (`# %%`).

| Minutes | Étape |
|---|---|
| 00–15 | **Décrire** : fixer l'année *avant* de calculer ; ROA ; qui publie sa R-D |
| 15–35 | **Comparer** : forte contre faible R-D (médiane) ; écart en points, IC bootstrap, test de Welch |
| 35–55 | **Relier** : nuage de points, Pearson, Spearman ; `roa ~ intensite_rd`, puis `+ C(secteur)` |
| 55–70 | **Casser** une hypothèse : retirer l'extrême, *ou* empiler les années avec et sans erreurs regroupées |
| 70–90 | **Écrire** 200 mots ; deux minutes devant la classe (présentateur tiré au hasard) |

**Ce qui coûte des points :** un `describe()` sans interprétation ; « significatif » sans écart ni
intervalle ; « pas significatif, donc aucun effet » ; un panel traité comme des observations
indépendantes ; une causalité tirée d'une corrélation ; une année choisie après avoir vu les
résultats.

**Remise (ZoneCours) :** `seance06_atelier.py` complété et `reponse.md`. Compte pour la
participation.

[← Retour à la séance 06](../README.md)
