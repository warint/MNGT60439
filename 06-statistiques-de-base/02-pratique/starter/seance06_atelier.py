"""Séance 6 — Pratique : les entreprises qui investissent en R-D sont-elles plus rentables ?

Exécutez depuis la racine du dépôt (le dossier qui contient data/) :

    python 06-statistiques-de-base/02-pratique/starter/seance06_atelier.py

Dans VS Code, chaque ligne « # %% » ouvre une cellule : Maj + Entrée l'exécute.
Remplacez chaque « ... » marqué TODO. Le fichier doit s'exécuter de bout en bout.
"""

# %% 0 · Importations et données
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats

plt.style.use("05-representer-les-donnees/pystatlas.mplstyle")   # le style de la galerie
Path("sorties").mkdir(exist_ok=True)

entreprises = pd.read_csv("data/entreprises.csv")

# TODO : créez les trois indicateurs
#   roa          = resultat_net / actifs_totaux
#   marge        = resultat_net / chiffre_affaires
#   intensite_rd = rd / chiffre_affaires
entreprises["roa"] = ...
entreprises["marge"] = ...
entreprises["intensite_rd"] = ...

# %% 1 · Décrire — 15 min
ANNEE = 2023  # TODO : fixez l'année AVANT de regarder les résultats, et justifiez-la en commentaire
coupe = entreprises[entreprises["annee"] == ANNEE].copy()

# TODO : moyenne, médiane, écart type et écart interquartile du ROA
print(...)

# TODO : combien d'entreprises n'ont pas de R-D publiée cette année-là ? Lesquelles ?
print(...)

# TODO : créez une variable « fait_rd » : True si intensite_rd est au-dessus de la médiane
# des entreprises qui publient leur R-D, False sinon (laissez NaN si la R-D est manquante)
coupe["fait_rd"] = ...

# %% 2 · Comparer — 20 min
# TODO : ROA moyen des deux groupes, écart, et test de Welch (equal_var=False)
groupe_fort = ...
groupe_faible = ...
test = stats.ttest_ind(groupe_fort, groupe_faible, equal_var=False)
print(f"Écart de ROA : {groupe_fort.mean() - groupe_faible.mean():+.3f}, p = {test.pvalue:.3f}")

# TODO : intervalle de confiance à 95 % de l'écart, par bootstrap (5 000 tirages)
rng = np.random.default_rng(60)
ecarts = []
for _ in range(5_000):
    ...
print(f"IC bootstrap 95 % : [{np.percentile(ecarts, 2.5):.3f} ; {np.percentile(ecarts, 97.5):.3f}]")

# TODO : montrez l'écart avec le graphique d'estimation de la galerie
#   https://warint.github.io/pystatlas/fr/group-comparisons/estimation-plot/
#   Le script de la galerie compare deux groupes appelés `low` et `high` : ce sont les vôtres.
#   Collez son bloc « bootstrap » et son bloc « figure », puis réécrivez titres et axes
#   (ROA en %, noms des groupes). Le script utilise aussi un DataFrame `df` avec une colonne
#   `group` pour le nuage de points : créez-le à partir de `coupe`. Ses étiquettes d'axe x
#   parlent de taux de pauvreté (`cut`) : remplacez-les par « Faible R-D » / « Forte R-D ».
low, high = 100 * groupe_faible, 100 * groupe_fort      # en points de ROA
# fig.savefig("sorties/s06_comparer.png")

# %% 3 · Relier — 20 min
donnees = coupe.dropna(subset=["intensite_rd", "roa"])   # une ligne par entreprise qui publie sa R-D

# TODO : le nuage, AVANT les coefficients — nuage de points avec statistiques de la galerie
#   https://warint.github.io/pystatlas/fr/correlation/scatter-with-stats/
#   Le script de la galerie attend deux tableaux `x` et `y` : les voici. Collez ses blocs
#   « statistique » et « figure » tels quels, puis réécrivez titre, axes et sous-titre.
x = 100 * donnees["intensite_rd"].to_numpy()     # intensité de R-D, en % des ventes
y = 100 * donnees["roa"].to_numpy()              # ROA, en %
n = len(x)
# fig.savefig("sorties/s06_relier.png")

# TODO : corrélations de Pearson et de Spearman entre intensite_rd et roa (sur `donnees`)
print(...)

# TODO : régression simple roa ~ intensite_rd, puis avec C(secteur) (data=donnees)
m1 = ...
m2 = ...
print(m1.summary().tables[1])
print(m2.params["intensite_rd"], m2.pvalues["intensite_rd"])

# %% 4 · Casser une hypothèse — 15 min
# TODO : choisissez UNE de ces deux expériences et notez ce qui change dans votre réponse
#   (a) retirez l'entreprise la plus extrême (laquelle ? pourquoi ?) et refaites la section 3
#   (b) utilisez TOUTES les années, d'abord naïvement, puis avec cov_type="cluster"
#       et cov_kwds={"groups": panel["ticker"]}
#       Facultatif : montrez les deux intervalles avec le graphique de coefficients
#       https://warint.github.io/pystatlas/fr/regression-models/coefficient-plot/
...

# %% 5 · Écrire — 20 min
# Rédigez 200 mots dans 06-statistiques-de-base/02-pratique/reponse.md :
#   - l'écart, EN UNITÉS (points de ROA), et son intervalle
#   - ce que l'hypothèse cassée a fait à votre réponse
#   - ce que ce résultat NE vous autorise PAS à recommander à un dirigeant
#   - la règle permanente : une sortie de l'IA que vous avez vérifiée, et comment
