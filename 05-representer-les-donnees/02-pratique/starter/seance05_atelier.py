"""Séance 5 — Pratique : le graphique qui défend, le graphique qui réfute.

« L'Amérique crée plus de valeur que tout autre pays. »

Les figures 2 à 4 s'adaptent de la galerie PyStatlas : https://warint.github.io/pystatlas/fr/
Pour chacune, ce fichier prépare les DONNÉES et la STATISTIQUE. Vous collez le bloc FIGURE
du script de la galerie (de `fig, ax = ...` jusqu'à `plt.show()`), puis vous remplacez ses
noms de variables et réécrivez ses textes en français.

Exécutez les cellules une à une (# %% puis Maj + Entrée dans VS Code), ou tout le
fichier d'un coup. Remplacez chaque TODO. Chaque figure est enregistrée dans sorties/.
Le fichier doit, à la fin, tout reproduire en une seule exécution.
"""

# %% Préparation -----------------------------------------------------------------
import os
from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import statsmodels.api as sm
from scipy import stats
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.oneway import anova_oneway

# Se placer à la racine du dépôt, d'où que le fichier soit exécuté.
RACINE = next(p for p in [Path.cwd(), *Path.cwd().parents] if (p / "data" / "pays.csv").exists())
os.chdir(RACINE)
Path("sorties").mkdir(exist_ok=True)

plt.style.use("05-representer-les-donnees/pystatlas.mplstyle")   # le style de la galerie
BLEU, ORANGE, VERT, ROUGE, GRIS = "#007AFF", "#FF9500", "#34C759", "#FF3B30", "#8E8E93"
GRIS_TEXTE = "#6E6E73"                                          # couleur des sous-titres

pays = pd.read_csv("data/pays.csv")
pays["region"] = pays["region"].str.strip()
ent = pd.read_csv("data/entreprises.csv")
p23 = pays[pays["annee"] == 2023]
SOURCE_BM = "Source : Banque mondiale, Indicateurs du développement dans le monde"

# %% Figure 1 — Défendre : les 15 plus grandes économies -------------------------
# Pas de galerie ici : des barres horizontales triées, en matplotlib simple.
top15 = p23.nlargest(15, "pib_milliards_usd").sort_values("pib_milliards_usd")
couleurs = [ROUGE if iso == "USA" else GRIS for iso in top15["iso3"]]

fig, ax = plt.subplots(figsize=(8, 5.5))
ax.barh(top15["pays"], top15["pib_milliards_usd"] / 1000, color=couleurs)
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
# TODO : une étiquette de valeur au bout de chaque barre (boucle sur enumerate + ax.text)
# TODO : un titre qui énonce le message (ax.set_title(..., pad=26)), une étiquette d'axe avec l'unité

# TODO : la part des États-Unis dans le PIB mondial 2023 (somme sur tous les pays)
part_usa = None
# TODO : en sous-titre, ax.text(0, 1.02, f"...", transform=ax.transAxes, fontsize=9.5, color=GRIS_TEXTE)
fig.text(0.01, -0.02, SOURCE_BM, fontsize=8, color=GRIS)

fig.savefig("sorties/fig1.png")
plt.show()

# %% Figure 2 — Réfuter : la distribution du PIB par habitant --------------------
# Galerie : https://warint.github.io/pystatlas/fr/distributions/histogram-density/

# DONNÉES — le log10 du PIB par habitant : 3 = 1 000 $, 4 = 10 000 $, 5 = 100 000 $
x = np.log10(p23["pib_hab_usd"].dropna().to_numpy())
usa = np.log10(p23.loc[p23["iso3"] == "USA", "pib_hab_usd"].iloc[0])
n_devant = int((x > usa).sum())

# STATISTIQUE — mêmes noms que dans le script de la galerie
mean, median, sd = x.mean(), np.median(x), x.std(ddof=1)
skew, kurt = stats.skew(x), stats.kurtosis(x)
W, p = stats.shapiro(x)

# FIGURE — TODO : collez le bloc figure de la galerie, puis :
#   - grid = np.linspace(x.min() - 0.3, x.max() + 0.3, 400)   (le script part de 0 : inadapté au log)
#   - ax.set_xticks([3, 4, 5], ["1 000 $", "10 000 $", "100 000 $"])
#   - les étiquettes Moyenne / Médiane en dollars : f"{name}\n{10 ** value:,.0f} $"
#   - ax.axvline(usa, color=ROUGE) et une annotation « États-Unis »
#   - un titre qui contient n_devant ; le sous-titre et les légendes en français
fig.savefig("sorties/fig2.png")
plt.show()

# %% Figure 3 — Réfuter : richesse et croissance ----------------------------------
# Galerie : https://warint.github.io/pystatlas/fr/correlation/scatter-with-stats/

# DONNÉES
croissance = (pays[pays["annee"].between(2014, 2023)]
              .groupby("iso3")["croissance_pib"].mean()
              .rename("croissance_moy"))
d3 = p23.merge(croissance, on="iso3").dropna(subset=["pib_hab_usd", "croissance_moy"])
x = np.log10(d3["pib_hab_usd"].to_numpy())
y = d3["croissance_moy"].to_numpy()
n = len(x)
est_usa = d3["iso3"].to_numpy() == "USA"          # x[est_usa][0], y[est_usa][0] : les États-Unis

# STATISTIQUE — mêmes noms que dans le script de la galerie
res = stats.pearsonr(x, y)
ci = res.confidence_interval(0.95)
fit = sm.OLS(y, sm.add_constant(x)).fit()
grid = np.linspace(x.min(), x.max(), 200)
band = fit.get_prediction(sm.add_constant(grid)).conf_int(alpha=0.05)

# FIGURE — TODO : collez le bloc figure de la galerie (fig = plt.figure(...) avec gridspec), puis :
#   - annotez les États-Unis ; axe x en dollars comme à la figure 2
#   - titre-message, axes avec unités, sous-titre en français, source
fig.savefig("sorties/fig3.png")
plt.show()

# %% Figure 4 — Entreprises : la marge nette de trois secteurs ----------------------
# Galerie : https://warint.github.io/pystatlas/fr/group-comparisons/between-groups-violin/

# DONNÉES
ent["marge"] = ent["resultat_net"] / ent["chiffre_affaires"] * 100
groups = ["Technologie", "Pharmaceutique", "Biens de consommation"]
data = [ent.loc[ent["secteur"] == g, "marge"].dropna().to_numpy() for g in groups]
palette = [BLEU, VERT, ORANGE]

# STATISTIQUE — mêmes noms que dans le script de la galerie
res = anova_oneway(data, use_var="unequal")                    # ANOVA de Welch
k, n = len(data), sum(len(d) for d in data)
omega2 = (res.statistic - 1) * (k - 1) / ((res.statistic - 1) * (k - 1) + n)
pairs = list(combinations(range(k), 2))
raw_p = [stats.ttest_ind(data[i], data[j], equal_var=False).pvalue for i, j in pairs]
adj_p = multipletests(raw_p, method="holm")[1]

# FIGURE — TODO : collez le bloc figure de la galerie, puis :
#   - le script de la galerie porte sur des écoles (pourcentages de 0 à 100) ; les crochets
#     conviennent tels quels à nos marges, mais supprimez les lignes propres aux écoles :
#     `lowinc = df.groupby(...)` et `ax.set_yticks(range(0, 101, 20))`
#   - étiquettes des groupes : ax.set_xticks(range(k), [f"{g}\n(n = {len(d)})" for g, d in zip(groups, data)])
#   - l'étiquette de moyenne affiche « % » : f"μ = {d.mean():.1f} %"
#   - ax.set_ylabel("Marge nette (%)"), titre-message, sous-titre en français, source SEC EDGAR
fig.savefig("sorties/fig4.png")
plt.show()

# %% Figure 5 — Explorer : IDE et richesse, en interactif --------------------------
# TODO : px.scatter(p23, x="pib_hab_usd", y="ide_entrants_pct_pib", size="population",
#                   color="region", hover_name="pays", log_x=True)
# Astuce : retirez les valeurs extrêmes d'IDE avec .between(-10, 40) après avoir regardé.
fig5 = None
# fig5.write_html("sorties/fig5.html")

# %% Note -------------------------------------------------------------------------
# Rédigez sorties/note_seance05.md (200 mots) — voir la diapositive « Rédiger ».
