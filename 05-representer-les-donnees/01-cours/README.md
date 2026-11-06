# Séance 05 — Cours

> **[Diapositives du cours](https://warint.github.io/MNGT60439/seance-05-cours.html)** ·
> source : [`MNGT60439-S05-Cours.qmd`](MNGT60439-S05-Cours.qmd)

Environ 90 minutes. Tout le code des diapositives s'exécute depuis la racine du dépôt.

| Partie | Contenu |
|---|---|
| Une manchette, quatre réponses | Le rang des États-Unis selon le PIB total, par habitant, la croissance, l'IDE |
| Pourquoi un graphique | Le quartet d'Anscombe, reconstruit à partir des valeurs publiées |
| Ce que l'œil lit bien | La hiérarchie de Cleveland et McGill ; angle contre position |
| L'anatomie d'une figure | `fig, ax`, titre-message, unités, source, étiquetage direct, `savefig` |
| Choisir le graphique | Comparaison, évolution, distribution, relation, composition |
| seaborn | `boxplot`, `lineplot`, `relplot(col=...)` sur les marges des entreprises |
| plotly | Nuage interactif PIB/hab. × IDE, carte choroplèthe |
| Du mauvais au bon | Axe tronqué, double axe, camembert en 3D ; grille de relecture |

Pour reconstruire les diapositives :

```bash
cd 05-representer-les-donnees/01-cours
quarto render MNGT60439-S05-Cours.qmd
```

Le noyau Jupyter `mngt60439` doit être installé (voir la séance 1). Les figures plotly
chargent `plotly.js` depuis un CDN au moment du rendu.

[Retour à la séance 05](../README.md)
