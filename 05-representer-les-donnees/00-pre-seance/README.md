# Séance 05 — Pré-séance

> **[Diapositives de la pré-séance](https://warint.github.io/MNGT60439/seance-05-pre-seance.html)** ·
> source : [`MNGT60439-S05-Pre-Seance.qmd`](MNGT60439-S05-Pre-Seance.qmd)

> Faites **les quatre étapes** avant le cours. Comptez 90 minutes environ.

| | Avant le cours | Utilisé en pratique pour |
|---|---|---|
| **1** | Lire Anscombe (1973) et Cleveland et McGill (1984) | choisir et défendre vos encodages |
| **2** | Vérifier `seaborn` et `plotly` | toutes les figures de l'atelier |
| **3** | Produire un premier graphique de `data/pays.csv` | gagner les vingt premières minutes |
| **4** | Tenter l'autovérification | suivre le cours sans décrocher |

---

## Étape 1 — Lire

- **Anscombe, F. J. (1973).** Graphs in Statistical Analysis. *The American Statistician*, 27(1), 17–21. <https://doi.org/10.1080/00031305.1973.10478966>
- **Cleveland, W. S. et McGill, R. (1984).** Graphical Perception. *JASA*, 79(387), 531–554. <https://doi.org/10.1080/01621459.1984.10478080> — sections 1 et 2.

Annotez : l'argument d'Anscombe en une phrase ; les six encodages de Cleveland et McGill dans
l'ordre ; un graphique de presse récent qui viole cet ordre ; ce que vous changeriez.

## Étape 2 — Vérifier les paquets

Depuis la racine du dépôt, `.venv` activé :

```bash
python -c "import matplotlib, seaborn, plotly; print(matplotlib.__version__, seaborn.__version__, plotly.__version__)"
```

En cas d'erreur : `python -m pip install -r requirements.txt`.

## Étape 3 — Un premier graphique

```python
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

Path("sorties").mkdir(exist_ok=True)
pays = pd.read_csv("data/pays.csv")
usa = pays[pays["iso3"] == "USA"]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(usa["annee"], usa["pib_hab_usd"] / 1000)
ax.set_title("États-Unis : PIB par habitant")
ax.set_ylabel("milliers de $ US courants")
fig.savefig("sorties/usa_pib_hab.png", dpi=200)
plt.show()
```

**À faire :** ajoutez le Canada, avec une autre couleur et une étiquette au bout de chaque
ligne (`ax.text`). Apportez le PNG.

## Étape 4 — Autovérification

1. Pourquoi Anscombe a-t-il construit quatre jeux de données identiques en statistiques résumées ?
2. Classez du plus précis au moins précis : couleur, position, angle, longueur, aire.
3. Une barre peut-elle commencer à 50 ? Une ligne ? Pourquoi la réponse diffère-t-elle ?
4. Pour comparer le PIB par habitant de 200 pays, quelle échelle choisir, et pourquoi ?
5. Quelle est la différence entre `fig` et `ax` dans `fig, ax = plt.subplots()` ?

---

## Utiliser l'IA sur la préparation

- « Explique-moi la différence entre `plt.plot` et `ax.plot`, et pourquoi on préfère la seconde. »
- « Voici un graphique décrit en mots. Selon Cleveland et McGill, quel encodage utilise-t-il et lequel serait plus précis ? »
- « Pose-moi cinq questions pour vérifier que je sais lire une boîte à moustaches. »

> **Règle permanente du cours.** Chaque fois que l'IA intervient dans un travail remis, indiquez
> ce que vous lui avez demandé et **ce que vous avez vérifié, et comment**.

Attention : les IA proposent encore `sns.distplot`, retiré de seaborn. Son remplaçant est `sns.histplot`.

---

[Retour à la séance 05](../README.md)
