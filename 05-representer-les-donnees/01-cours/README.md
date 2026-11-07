# Séance 05 — Cours

> **[Diapositives du cours](https://warint.github.io/MNGT60439/seance-05-cours.html)** ·
> source : [`MNGT60439-S05-Cours.qmd`](MNGT60439-S05-Cours.qmd)

Environ 90 minutes. Tout le code des diapositives s'exécute depuis la racine du dépôt.

| Partie | Contenu |
|---|---|
| Une manchette, quatre réponses | Le rang des États-Unis selon le PIB total, par habitant, la croissance, l'IDE |
| Pourquoi un graphique | Le quartet d'Anscombe, reconstruit à partir des valeurs publiées |
| Ce que l'œil lit bien | La hiérarchie de Cleveland et McGill ; angle contre position |
| PyStatlas | La galerie : 48 graphiques, 10 familles ; quelle famille pour quelle question |
| L'anatomie d'un script | Fiche, données, statistique, figure ; `fig, ax`, titre-message, sous-titre statistique ; `statlas.mplstyle` |
| La méthode, en cinq adaptations | Histogramme avec densité (PIB/hab.), nuage de pluie (marges par secteur), nuage avec statistiques (richesse × ouverture), fonctions de répartition (croissance, pays riches contre autres), crêtes (croissance 2007-2023) |
| Hors galerie | Lignes étiquetées, barres empilées, nuage plotly interactif |
| Du mauvais au bon | Axe tronqué, double axe, camembert en 3D ; grille de relecture |

Pour reconstruire les diapositives :

```bash
cd 05-representer-les-donnees/01-cours
quarto render MNGT60439-S05-Cours.qmd
```

Le noyau Jupyter `mngt60439` doit être installé (voir la séance 1). Les figures plotly
chargent `plotly.js` depuis un CDN au moment du rendu. Les graphiques statistiques sont adaptés
de [PyStatlas](https://warint.github.io/pystatlas/fr/) et utilisent [`../statlas.mplstyle`](../statlas.mplstyle).

[Retour à la séance 05](../README.md)
