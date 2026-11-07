# Séance 05 — Pré-séance

> **[Diapositives de la pré-séance](https://warint.github.io/MNGT60439/seance-05-pre-seance.html)** ·
> source : [`MNGT60439-S05-Pre-Seance.qmd`](MNGT60439-S05-Pre-Seance.qmd)

> Faites **les cinq étapes** avant le cours. Comptez 1 h 45 environ.

| | Avant le cours | Utilisé en pratique pour |
|---|---|---|
| **1** | Lire Anscombe (1973) et Cleveland et McGill (1984) | choisir et défendre vos encodages |
| **2** | Parcourir la galerie [PyStatlas](https://warint.github.io/pystatlas/fr/) | trouver le bon graphique pour chaque question |
| **3** | Vérifier les paquets ; exécuter un script de la galerie tel quel | adapter les scripts en atelier |
| **4** | Produire un premier graphique de `data/pays.csv` | gagner les vingt premières minutes |
| **5** | Tenter l'autovérification | suivre le cours sans décrocher |

---

## Étape 1 — Lire

- **Anscombe, F. J. (1973).** Graphs in Statistical Analysis. *The American Statistician*, 27(1), 17–21. <https://doi.org/10.1080/00031305.1973.10478966>
- **Cleveland, W. S. et McGill, R. (1984).** Graphical Perception. *JASA*, 79(387), 531–554. <https://doi.org/10.1080/01621459.1984.10478080> — sections 1 et 2.

Annotez : l'argument d'Anscombe en une phrase ; les six encodages de Cleveland et McGill dans
l'ordre ; un graphique de presse récent qui viole cet ordre ; ce que vous changeriez.

## Étape 2 — Parcourir la galerie

<https://warint.github.io/pystatlas/fr/> : ouvrez trois pages de la famille **Distributions** et
une de **Corrélation et association**. Pour chacune, notez la question à laquelle le graphique
répond, la ligne qui charge les données, la statistique en sous-titre, et si le titre affirme
un message ou décrit un sujet.

## Étape 3 — Vérifier les paquets, exécuter un script

Depuis la racine du dépôt, `.venv` activé :

```bash
python -c "import matplotlib, seaborn, plotly, scipy, statsmodels; print('ok')"
```

En cas d'erreur : `python -m pip install -r requirements.txt`.

Copiez le code du [graphique en crêtes](https://warint.github.io/pystatlas/fr/distributions/ridgeline/)
dans `sorties/cretes.py` et exécutez-le sans rien changer : il montre la fécondité des pays de
1960 à 2010. (Quelques scripts chargent leurs données avec lifelines, non installé : en séance,
c'est précisément la ligne des données que l'on remplace.)

## Étape 4 — Un premier graphique

```python
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

plt.style.use("05-representer-les-donnees/pystatlas.mplstyle")
Path("sorties").mkdir(exist_ok=True)
pays = pd.read_csv("data/pays.csv")
usa = pays[pays["iso3"] == "USA"]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(usa["annee"], usa["pib_hab_usd"] / 1000)
ax.set_title("États-Unis : PIB par habitant")
ax.set_ylabel("milliers de $ US courants")
fig.savefig("sorties/usa_pib_hab.png")
plt.show()
```

**À faire :** ajoutez le Canada, avec une autre couleur et une étiquette au bout de chaque
ligne (`ax.text`), et un titre qui **affirme** quelque chose. Apportez le PNG.

## Étape 5 — Autovérification

1. Pourquoi Anscombe a-t-il construit quatre jeux de données identiques en statistiques résumées ?
2. Classez du plus précis au moins précis : couleur, position, angle, longueur, aire.
3. Une barre peut-elle commencer à 50 ? Une ligne ? Pourquoi la réponse diffère-t-elle ?
4. Dans un script PyStatlas, quels sont les quatre blocs, et lequel changez-vous pour vos données ?
5. Quelle est la différence entre `fig` et `ax` dans `fig, ax = plt.subplots()` ?

---

## Utiliser l'IA sur la préparation

- « Voici le script PyStatlas du nuage de pluie. Explique-moi chaque bloc, ligne par ligne. »
- « Voici un graphique décrit en mots. Selon Cleveland et McGill, quel encodage utilise-t-il et lequel serait plus précis ? »
- « Pose-moi cinq questions pour vérifier que je sais lire une boîte à moustaches. »

> **Règle permanente du cours.** Chaque fois que l'IA intervient dans un travail remis, indiquez
> ce que vous lui avez demandé et **ce que vous avez vérifié, et comment**.

Attention : les IA proposent encore `sns.distplot`, retiré de seaborn. Son remplaçant est `sns.histplot`.

---

[Retour à la séance 05](../README.md)
