# Séance 06 — Préparation (pré-séance)

> **[Diapositives de la pré-séance](https://warint.github.io/MNGT60439/seance-06-pre-seance.html)** ·
> source : [`MGMT60XXX-S06-Pre-Seance.qmd`](MGMT60XXX-S06-Pre-Seance.qmd)

> Faites **les quatre étapes** avant le cours. Prévoyez environ 90 minutes.

| | Avant le cours | Durée | Sert, en classe, à |
|---|---|---|---|
| **1** | Lire la déclaration de l'ASA sur les valeurs p | 30 min | lire un test sans contresens |
| **2** | Revoir cinq notions | 30 min | suivre le cours sans redémonstration |
| **3** | Préparer les données | 15 min | la pratique |
| **4** | Autovérification | 15 min | le cours |

---

## Étape 1 — Lecture

**Wasserstein, R. L. et Lazar, N. A. (2016). *The ASA Statement on p-Values: Context, Process,
and Purpose*.** *The American Statistician*, 70(2), 129–133.
<https://doi.org/10.1080/00031305.2016.1154108> (libre accès)

Annotez : (1) les six principes, chacun en une phrase à vous ; (2) celui que la presse d'affaires
viole le plus souvent ; (3) ce que les auteurs recommandent de rapporter à la place, ou en plus,
d'une valeur p ; (4) une manchette qui viole l'un des principes.

*Facultatif :* Miller, C. C. et Bamberger, P. (2016). *Exploring Emergent and Poorly Understood
Phenomena in the Strangest of Places*. *Academy of Management Discoveries*, 2(4), 313–319.
<https://doi.org/10.5465/amd.2016.0115> — sur la valeur des résultats nuls et des réplications.

## Étape 2 — Cinq notions à revoir

- **Moyenne et médiane** : point d'équilibre et milieu du classement.
- **Écart type** : $s = \sqrt{\frac{1}{n-1}\sum_i (x_i - \bar x)^2}$, avec $n-1$.
- **Quantiles** : Q1 laisse 25 % des observations en dessous.
- **Corrélation** : entre −1 et +1, une relation linéaire.
- **Une droite** : $y = \beta_0 + \beta_1 x$, ordonnée à l'origine et pente.

## Étape 3 — Préparer les données

Depuis la racine du dépôt, `.venv` activé :

```python
import pandas as pd

entreprises = pd.read_csv("data/entreprises.csv")
entreprises["roa"] = entreprises["resultat_net"] / entreprises["actifs_totaux"]
entreprises["marge"] = entreprises["resultat_net"] / entreprises["chiffre_affaires"]
entreprises["intensite_rd"] = entreprises["rd"] / entreprises["chiffre_affaires"]

e23 = entreprises[entreprises["annee"] == 2023]
print(e23[["roa", "marge", "intensite_rd"]].describe().round(3))
```

Notez combien d'entreprises n'ont pas de R-D publiée en 2023, et lesquelles.

## Étape 4 — Autovérification

Répondez **par écrit** (rien n'est remis) :

1. Pourquoi la moyenne des chiffres d'affaires est-elle bien plus grande que leur médiane ?
2. Une valeur p de 0,11 : que pouvez-vous en conclure, et que ne pouvez-vous pas en conclure ?
3. Si l'on quadruple la taille d'un échantillon, que devient l'erreur type de la moyenne ?
4. « Les entreprises qui font beaucoup de R-D sont plus rentables. » Proposez deux explications qui
   ne passent pas par « la R-D cause la rentabilité ».

---

## L'IA générative pour préparer la séance

- « Pose-moi cinq questions sur l'intervalle de confiance ; ne donne pas les réponses avant les miennes. »
- « Explique la différence entre le test t de Student et celui de Welch, avec un exemple chiffré. »
- « Donne-moi une phrase fausse mais plausible sur une valeur p, et laisse-moi trouver l'erreur. »

> **Règle permanente du cours.** Chaque fois que l'IA intervient dans un travail remis, vous
> indiquez ce que vous lui avez demandé et ce que vous avez vérifié, et comment.

[← Retour à la séance 06](../README.md)
