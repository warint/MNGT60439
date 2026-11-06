# Séance 05 — Pratique

> **[Diapositives de la pratique](https://warint.github.io/MNGT60439/seance-05-pratique.html)** ·
> source : [`MGMT60XXX-S05-Pratique.qmd`](MGMT60XXX-S05-Pratique.qmd)

**Question :** « L'Amérique crée plus de valeur que tout autre pays. » Construisez le graphique
qui défend la manchette, puis ceux qui la réfutent.

| Minutes | Étape | Figure |
|---|---|---|
| 00–20 | Défendre | `fig1.png` — les 15 plus grandes économies, barres triées, part des États-Unis calculée |
| 20–45 | Réfuter | `fig2.png` — distribution du PIB/hab. (log) ; `fig3.png` — richesse × croissance 2014-2023 |
| 45–65 | Entreprises | `fig4.png` — marge nette médiane par secteur, petits multiples |
| 65–80 | Explorer | `fig5.html` — nuage plotly PIB/hab. × IDE entrants |
| 80–90 | Rédiger | `note_seance05.md` — 200 mots |

## Démarrer

```bash
cp 05-representer-les-donnees/02-pratique/starter/seance05_atelier.py sorties/
```

Ouvrez `sorties/seance05_atelier.py` dans VS Code et exécutez-le cellule par cellule
(`# %%`, puis `Maj + Entrée`). Le fichier se place lui-même à la racine du dépôt ; remplacez
chaque `TODO`.

## Remettre

Les cinq figures, la note et votre script, qui doit tout reproduire en une exécution.

## Ce qui coûte des points

Un titre qui décrit au lieu d'affirmer ; un axe sans unité ; une figure sans source ; des
barres non triées ou qui ne partent pas de zéro ; une légende de quinze couleurs ; un chiffre
dans la note qui ne sort pas du code.

[Retour à la séance 05](../README.md)
