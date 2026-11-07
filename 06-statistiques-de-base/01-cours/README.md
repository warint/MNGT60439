# Séance 06 — Cours

> **[Ouvrir les diapositives](https://warint.github.io/MNGT60439/seance-06-cours.html)** · source :
> [`MNGT60439-S06-Cours.qmd`](MNGT60439-S06-Cours.qmd)

| Partie | Contenu |
|---|---|
| 1 | Deux manchettes, revues avec de l'incertitude ; trois indicateurs (`roa`, `marge`, `intensite_rd`) ; la galerie PyStatlas, notion par notion |
| 2 | Décrire : moyenne ou médiane, écart type et écart interquartile, statistiques par groupe, histogramme et logarithme |
| 3 | De l'échantillon à la population : erreur type, intervalle de confiance (`stats.t.interval`) et ce que « 95 % » veut dire (cent sondages, exemple de la galerie), bootstrap et sa distribution |
| 4 | Comparer : test t sur un échantillon, test de Welch (technologie contre autres secteurs) et son graphique d'estimation, test apparié (Tesla contre Ford) ; ce qu'une valeur p n'est pas |
| 5 | Relier : nuage de points, Pearson et Spearman, matrice de corrélation |
| 6 | Une première régression : `smf.ols("roa ~ intensite_rd")`, lire la sortie |
| 7 | Corrélation n'est pas causalité : causalité inverse, secteur confondant, panel et erreurs regroupées par entreprise ; un coefficient, trois incertitudes (graphique de coefficients) |
| 8 | Les premiers pas — travail 2 |

Le code des diapositives est **exécuté** au rendu : chaque sortie affichée vient des données du
cours, et les chiffres cités dans le texte sont calculés, pas recopiés. Pour reproduire un exemple,
copiez le bloc dans un script exécuté depuis la racine du dépôt.

Rendu : `scripts/render.sh` (voir le [README principal](../../README.md)).

[← Retour à la séance 06](../README.md)
