"""Séance 5 — Pratique : le graphique qui défend, le graphique qui réfute.

« L'Amérique crée plus de valeur que tout autre pays. »

Exécutez les cellules une à une (# %% puis Maj + Entrée dans VS Code), ou tout le
fichier d'un coup. Remplacez chaque TODO. Chaque figure est enregistrée dans sorties/.
Le fichier doit, à la fin, tout reproduire en une seule exécution.
"""

# %% Préparation -----------------------------------------------------------------
import os
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns

# Se placer à la racine du dépôt, d'où que le fichier soit exécuté.
RACINE = next(p for p in [Path.cwd(), *Path.cwd().parents] if (p / "data" / "pays.csv").exists())
os.chdir(RACINE)
Path("sorties").mkdir(exist_ok=True)

pays = pd.read_csv("data/pays.csv")
ent = pd.read_csv("data/entreprises.csv")
p23 = pays[pays["annee"] == 2023]
SOURCE_BM = "Source : Banque mondiale, Indicateurs du développement dans le monde"

# %% Figure 1 — Défendre : les 15 plus grandes économies -------------------------
top15 = p23.nlargest(15, "pib_milliards_usd").sort_values("pib_milliards_usd")
couleurs = ["#B4553A" if iso == "USA" else "#9A9A9A" for iso in top15["iso3"]]

fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(top15["pays"], top15["pib_milliards_usd"] / 1000, color=couleurs)
# TODO : une étiquette de valeur au bout de chaque barre (boucle sur enumerate + ax.text)
# TODO : un titre qui énonce le message, une étiquette d'axe avec l'unité
fig.text(0.01, 0.01, SOURCE_BM, fontsize=7)

# TODO : calculez la part des États-Unis dans le PIB mondial 2023 (somme sur tous les pays)
part_usa = None
print(f"Part des États-Unis : {part_usa}")

fig.savefig("sorties/fig1.png", dpi=200, bbox_inches="tight")
plt.show()

# %% Figure 2 — Réfuter : la distribution du PIB par habitant --------------------
usa_pc = p23.loc[p23["iso3"] == "USA", "pib_hab_usd"].iloc[0]
fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(p23["pib_hab_usd"], bins=30, log_scale=True, ax=ax)
# TODO : une ligne verticale (ax.axvline) au niveau des États-Unis, annotée
# TODO : combien de pays ont un PIB par habitant supérieur ? Mettez-le dans le titre.
n_devant = None
fig.savefig("sorties/fig2.png", dpi=200, bbox_inches="tight")
plt.show()

# %% Figure 3 — Réfuter : richesse et croissance ----------------------------------
croissance = (pays[pays["annee"].between(2014, 2023)]
              .groupby("iso3")["croissance_pib"].mean()
              .rename("croissance_moy"))
d3 = p23.merge(croissance, on="iso3").dropna(subset=["pib_hab_usd", "croissance_moy"])

fig, ax = plt.subplots(figsize=(8, 4.5))
# TODO : sns.scatterplot, x = PIB par habitant, y = croissance_moy, size = population
# TODO : échelle log en x, annotation des États-Unis, titre-message, source
fig.savefig("sorties/fig3.png", dpi=200, bbox_inches="tight")
plt.show()

# %% Figure 4 — Entreprises : la marge nette par secteur ---------------------------
ent["marge"] = ent["resultat_net"] / ent["chiffre_affaires"] * 100
# TODO : sns.relplot(data=ent, x="annee", y="marge", col="secteur", col_wrap=3,
#                    kind="line", estimator="median", errorbar=None, ...)
# TODO : essayez facet_kws={"sharey": True} puis False ; gardez celle que vous défendez
g = None
# g.savefig("sorties/fig4.png", dpi=200)

# %% Figure 5 — Explorer : IDE et richesse, en interactif --------------------------
# TODO : px.scatter(p23, x="pib_hab_usd", y="ide_entrants_pct_pib", size="population",
#                   color="region", hover_name="pays", log_x=True)
# Astuce : retirez les valeurs extrêmes d'IDE avec .between(-10, 40) après avoir regardé.
fig5 = None
# fig5.write_html("sorties/fig5.html")

# %% Note -------------------------------------------------------------------------
# Rédigez sorties/note_seance05.md (200 mots) — voir la diapositive « Rédiger ».
