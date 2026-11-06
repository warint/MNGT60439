"""Séance 3 — Pratique : monter le dossier de données « Tesla et l'environnement ».

Exécutez depuis la RACINE du dépôt (le dossier qui contient data/).
Dans VS Code, chaque bloc `# %%` s'exécute avec Maj + Entrée.

Remplacez chaque `...` et chaque TODO. Ne supprimez pas les `assert` : ils vous disent si
l'étape a réussi. Le dossier final est écrit dans sorties/dossier_tesla/.
"""

# %% 0 · Préparation ---------------------------------------------------------------
import os
import sqlite3
from pathlib import Path

import pandas as pd
import requests
import yfinance as yf

CACHE = Path("data/cache")
CACHE.mkdir(parents=True, exist_ok=True)
SORTIE = Path("sorties/dossier_tesla")
SORTIE.mkdir(parents=True, exist_ok=True)

PAYS = ["USA", "CHN", "DEU", "NOR", "CAN"]   # où Tesla vend le plus, et deux contrastes


def charger(nom, telecharger):
    """Relit data/cache/<nom>.parquet s'il existe ; sinon télécharge, enregistre, renvoie."""
    fichier = CACHE / f"{nom}.parquet"
    if fichier.exists():
        return pd.read_parquet(fichier)
    df = telecharger()
    df.to_parquet(fichier)
    return df


# %% 1 · CSV local (10 min) ---------------------------------------------------------
# Lisez data/entreprises_fr.csv (format « Excel français »). Trois options sont nécessaires.
# TODO : complétez l'appel.
ent = pd.read_csv("data/entreprises_fr.csv", ...)

auto = ent[ent["secteur"] == "Automobile"].copy()
# TODO : ajoutez une colonne "marge" = resultat_net / chiffre_affaires
...

assert auto.shape == (45, 13), f"Forme inattendue : {auto.shape} — vérifiez sep, decimal, encoding"
assert auto["chiffre_affaires"].dtype == "float64", "chiffre_affaires doit être numérique"

# %% 2 · URL : Our World in Data (10 min) -----------------------------------------
URL_CO2 = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
COLONNES = ["country", "year", "iso_code", "co2_per_capita", "share_global_co2"]

# TODO : utilisez charger("owid_co2", lambda: pd.read_csv(...)) avec usecols=COLONNES
co2 = ...

# TODO : gardez les pays de PAYS, années 2015 et suivantes
co2_sel = ...

assert set(co2_sel["iso_code"]) == set(PAYS)

# %% 3 · API Banque mondiale (15 min) -----------------------------------------------
# Indicateur EG.ELC.RNEW.ZS : part de l'électricité produite à partir de renouvelables (%).
def renouvelables():
    url = "https://api.worldbank.org/v2/country/" + ";".join(PAYS) + "/indicator/EG.ELC.RNEW.ZS"
    # TODO : requests.get avec params format=json, date=2015:2023, per_page=500, timeout=30
    r = ...
    r.raise_for_status()
    # TODO : transformez r.json()[1] en DataFrame avec les colonnes iso3, annee, renouv_pct
    return ...


elec = charger("wb_renouv_5pays", renouvelables)
print(elec.pivot(index="annee", columns="iso3", values="renouv_pct").round(1))
# QUESTION : quelle est la dernière année disponible ? Notez-la dans la fiche de provenance.

# %% 4 · Paquet yfinance (10 min) ---------------------------------------------------
# TODO : cours de clôture ajustés de TSLA, F, GM du 2020-01-01 au 2025-01-01
prix = charger("cours_auto", lambda: ...)

# Rendement annuel : dernier cours de chaque année, variation d'une année à l'autre.
rendements = prix.resample("YE").last().pct_change().dropna()
print(rendements.round(2))

# %% 5 · Base de données SQL (15 min) -----------------------------------------------
# TODO : avec sqlite3 et pd.read_sql, sur data/strategie.db, obtenez pour le secteur
# Automobile depuis 2019 : entreprise, annee, rd, chiffre_affaires et l'intensité de R-D
# en % (rd * 100.0 / chiffre_affaires), triés par entreprise puis annee.
requete = """
SELECT ...
"""
with sqlite3.connect("data/strategie.db") as con:
    rd = pd.read_sql(requete, con)
print(rd)
# QUESTION : pourquoi la R-D de General Motors est-elle manquante ? (Indice : séance 1.)

# %% 6 · (Bonus) API SEC EDGAR -----------------------------------------------------
# Votre identité vient de la variable d'environnement SEC_USER_AGENT (pré-séance).
ua = os.environ.get("SEC_USER_AGENT")
assert ua, "Définissez SEC_USER_AGENT (voir la pré-séance), puis relancez VS Code."
# TODO : téléchargez les ventes annuelles de Ford (CIK 0000037996) et comparez-les à
# entreprises.csv pour 2023. Les deux sources donnent-elles le même chiffre ?

# %% 7 · Sauvegarder le dossier (5 min) ---------------------------------------------
for nom, df in {"auto": auto, "co2": co2_sel, "elec": elec, "rd": rd}.items():
    df.to_csv(SORTIE / f"{nom}.csv", index=False)
rendements.to_csv(SORTIE / "rendements.csv")
print(sorted(f.name for f in SORTIE.iterdir()))

# %% 8 · Fiche de provenance ---------------------------------------------------------
# TODO : créez sorties/dossier_tesla/PROVENANCE.md : une ligne par source avec
# producteur, mode d'accès, date d'accès, unité, licence, dernière année disponible.
