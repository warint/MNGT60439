"""Séance 2 — Pratique : quelles entreprises créent le plus de valeur ?

Exécutez depuis la RACINE du dépôt (le dossier qui contient data/).
Chaque bloc `# %%` est une cellule : placez le curseur dedans et faites Maj + Entrée.

Remplacez chaque `...` et chaque TODO. Après chaque étape, vérifiez la FORME du
résultat (combien de lignes, combien de colonnes) avant de passer à la suivante.
"""

# %% 0 · Charger les données
import pandas as pd

entreprises = pd.read_csv("data/entreprises.csv")
print(entreprises.shape)  # attendu : (480, 12)

# %% 1 · Regarder avant de calculer — 10 min
# TODO : affichez les types des colonnes, le nombre de valeurs manquantes par colonne,
#        et le nombre d'entreprises par secteur pour une seule année.
print(...)

# %% 2 · Quatre mesures de la création de valeur — 15 min
df = entreprises.copy()
df["marge_nette"] = df["resultat_net"] / df["chiffre_affaires"]
# TODO : créez roa, roe et intensite_rd
df["roa"] = ...
df["roe"] = ...
df["intensite_rd"] = ...

# %% 3 · Quatre classements pour 2023 — 15 min
a23 = df[df["annee"] == 2023]
# TODO : le top 5 selon le résultat net, la marge nette, le ROA et le ROE.
#        Affichez seulement entreprise, secteur et la mesure.
for mesure in ["resultat_net", "marge_nette", "roa", "roe"]:
    print(f"\n--- {mesure} ---")
    print(...)

# Question : combien d'entreprises apparaissent dans les quatre classements ?
# Indice : un ensemble Python (set) et l'opérateur & .

# %% 4 · Le piège du dénominateur — 10 min
# TODO : affichez les entreprises dont les capitaux propres sont négatifs en 2023.
#        Que vaut leur ROE ? Que décidez-vous d'en faire dans votre classement ?
print(...)

# %% 5 · À l'intérieur des secteurs — 20 min
# TODO : pour 2023, par secteur : nombre d'entreprises, marge nette médiane, ROA médian,
#        intensité R-D moyenne. Triez par ROA médian.
par_secteur = (
    a23.groupby("secteur")
    .agg(
        n=("ticker", "count"),
        # ...
    )
)
print(par_secteur.round(3))

# TODO : dans VOTRE secteur choisi, classez les entreprises par ROA en 2023.
mon_secteur = "Technologie"   # changez-le
print(...)

# %% 6 · Une année ou quinze ? — 10 min
# TODO : pour chaque entreprise, la marge nette moyenne, minimale et maximale sur 2010-2024.
#        Le classement sur quinze ans est-il celui de 2023 ?
print(...)

# %% 7 · Les manquants — 5 min
# TODO : quelle part de valeurs manquantes dans `rd`, par secteur ?
#        Expliquez en une phrase, dans votre note, pourquoi vous ne les remplacez pas par 0.
print(...)
