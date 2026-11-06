# Séance 04 — Pratique

> **[Ouvrir les diapositives](https://warint.github.io/MNGT60439/seance-04-pratique.html)** · source :
> [`MNGT60439-S04-Pratique.qmd`](MNGT60439-S04-Pratique.qmd)

**Question :** *Qui sont les vrais concurrents de mon entreprise — et que dit la Bourse de ses
acquisitions ?*

Fichier de départ : [`starter/seance04_atelier.py`](starter/seance04_atelier.py), à exécuter
depuis la racine du dépôt. Données d'exercice :
[`donnees/annonces_fa.csv`](donnees/annonces_fa.csv) — neuf annonces d'acquisition réelles
(2022-2023), volontairement mal saisies (espaces, casse, virgules décimales, dates en texte,
`n.d.`, un doublon). Les dates et montants proviennent des communiqués des acquéreurs ;
vérifiez-en un vous-même.

| Minutes | Étape |
|---|---|
| 00–20 | Comparer votre entreprise à son secteur, la même année (`transform`) |
| 20–30 | Un tableau de synthèse par secteur (`groupby().agg()`) |
| 30–40 | Remodeler : `pivot`, puis `melt` |
| 40–60 | Nettoyer `annonces_fa.csv`, puis le joindre à `entreprises.csv` |
| 60–80 | Rendement anormal naïf autour de chaque annonce ; empiler avec `concat` ; un graphique |
| 80–90 | Ce que le calcul ne permet pas de conclure ; deux minutes devant la classe |

**Remise (ZoneCours) :** `seance04_atelier.py` et `sorties/seance04_car.png`. Compte pour la
participation.

[← Retour à la séance 04](../README.md)
