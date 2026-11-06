"""Construit les données du cours MGMT 60XXX à partir de sources publiques.

Exécuter depuis la racine du dépôt :

    python scripts/build_course_data.py

Produit, dans data/ :

    entreprises.csv   panel de 32 grandes entreprises cotées aux États-Unis × exercices 2010-2024
                      (SEC EDGAR, API XBRL « companyfacts » ; domaine public)
    pays.csv          panel pays × année 2000-2023 (Banque mondiale, API v2 ; licence CC BY 4.0)
    secteurs.csv      table de correspondance secteur → description
    strategie.db      base SQLite qui contient les trois tables ci-dessus (séance 03)
    entreprises_fr.csv  même contenu qu'entreprises.csv, au format « Excel français »
                      (séparateur ;  décimale ,  encodage Windows-1252) — pour l'exercice d'import

La SEC demande que chaque requête automatisée s'identifie par un User-Agent. Renseignez la
variable d'environnement SEC_USER_AGENT (« Prénom Nom courriel@exemple.com ») avant d'exécuter.
"""

from __future__ import annotations

import os
import re
import sqlite3
import time
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)

UA = os.environ.get("SEC_USER_AGENT", "HEC Montreal MGMT60XXX course data builder")
HEADERS = {"User-Agent": UA}

ANNEES = range(2010, 2025)

# CIK : identifiant permanent de chaque déclarant auprès de la SEC.
CIK = {
    "TSLA": 1318605, "F": 37996, "GM": 1467858, "AAPL": 320193, "MSFT": 789019,
    "GOOGL": 1652044, "META": 1326801, "NVDA": 1045810, "INTC": 50863, "IBM": 51143,
    "AMZN": 1018724, "WMT": 104169, "COST": 909832, "TGT": 27419, "PFE": 78003,
    "JNJ": 200406, "MRK": 310158, "LLY": 59478, "XOM": 34088, "CVX": 93410, "COP": 1163165,
    "KO": 21344, "PEP": 77476, "PG": 80424, "NKE": 320187, "MCD": 63908, "SBUX": 829224,
    "BA": 12927, "CAT": 18230, "MMM": 66740, "HON": 773840, "NFLX": 1065280,
}

NOMS = {
    "TSLA": "Tesla", "F": "Ford", "GM": "General Motors", "AAPL": "Apple", "MSFT": "Microsoft",
    "GOOGL": "Alphabet", "META": "Meta Platforms", "NVDA": "Nvidia", "INTC": "Intel",
    "IBM": "IBM", "AMZN": "Amazon", "WMT": "Walmart", "COST": "Costco", "TGT": "Target",
    "PFE": "Pfizer", "JNJ": "Johnson & Johnson", "MRK": "Merck & Co.", "LLY": "Eli Lilly",
    "XOM": "ExxonMobil", "CVX": "Chevron", "COP": "ConocoPhillips", "KO": "Coca-Cola",
    "PEP": "PepsiCo", "PG": "Procter & Gamble", "NKE": "Nike", "MCD": "McDonald's",
    "SBUX": "Starbucks", "BA": "Boeing", "CAT": "Caterpillar", "MMM": "3M",
    "HON": "Honeywell", "NFLX": "Netflix",
}

# ticker -> secteur
ENTREPRISES = {
    "TSLA": "Automobile", "F": "Automobile", "GM": "Automobile",
    "AAPL": "Technologie", "MSFT": "Technologie", "GOOGL": "Technologie",
    "META": "Technologie", "NVDA": "Technologie", "INTC": "Technologie", "IBM": "Technologie",
    "AMZN": "Commerce de détail", "WMT": "Commerce de détail", "COST": "Commerce de détail",
    "TGT": "Commerce de détail",
    "PFE": "Pharmaceutique", "JNJ": "Pharmaceutique", "MRK": "Pharmaceutique",
    "LLY": "Pharmaceutique",
    "XOM": "Énergie", "CVX": "Énergie", "COP": "Énergie",
    "KO": "Biens de consommation", "PEP": "Biens de consommation", "PG": "Biens de consommation",
    "NKE": "Biens de consommation",
    "MCD": "Restauration", "SBUX": "Restauration",
    "BA": "Industrie", "CAT": "Industrie", "MMM": "Industrie", "HON": "Industrie",
    "NFLX": "Médias et divertissement",
}

# Plusieurs balises XBRL désignent la même grandeur selon l'entreprise et l'année.
# On les essaie dans l'ordre ; la première qui donne une valeur pour l'année gagne.
CONCEPTS = {
    "chiffre_affaires": [
        "RevenueFromContractWithCustomerExcludingAssessedTax",
        "Revenues",
        "RevenueFromContractWithCustomerIncludingAssessedTax",
        "SalesRevenueNet",
        "SalesRevenueGoodsNet",
    ],
    "resultat_net": ["NetIncomeLoss", "ProfitLoss"],
    "actifs_totaux": ["Assets"],
    "capitaux_propres": [
        "StockholdersEquity",
        "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest",
    ],
    "rd": [
        "ResearchAndDevelopmentExpense",
        "ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost",
    ],
    "investissements": ["PaymentsToAcquirePropertyPlantAndEquipment"],
}
INSTANT = {"actifs_totaux", "capitaux_propres"}


def _annual(facts: dict, concept: str, instant: bool) -> dict[int, float]:
    """Valeurs annuelles d'un concept, alignées sur l'année civile via le champ `frame`."""
    node = facts.get("us-gaap", {}).get(concept)
    if not node:
        return {}
    pat = re.compile(r"^CY(\d{4})Q4I$" if instant else r"^CY(\d{4})$")
    out: dict[int, float] = {}
    for unit, rows in node["units"].items():
        if unit != "USD":
            continue
        for r in rows:
            m = pat.match(r.get("frame", ""))
            if m:
                out[int(m.group(1))] = float(r["val"])
    return out


def build_entreprises() -> pd.DataFrame:
    rows = []
    for tic, secteur in ENTREPRISES.items():
        cik = CIK[tic]
        url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
        js = requests.get(url, headers=HEADERS, timeout=60).json()
        nom, facts = NOMS[tic], js["facts"]
        series = {}
        for var, concepts in CONCEPTS.items():
            merged: dict[int, float] = {}
            for c in concepts:
                for an, val in _annual(facts, c, var in INSTANT).items():
                    if var == "rd":
                        # Certaines entreprises (J&J) logent sous la balise générale une
                        # composante seulement de la R-D ; le maximum est le total publié.
                        merged[an] = max(merged.get(an, val), val)
                    else:
                        merged.setdefault(an, val)
            series[var] = merged
        for an in ANNEES:
            rows.append(
                {"ticker": tic, "entreprise": nom, "cik": cik, "secteur": secteur,
                 "pays_siege": "USA", "annee": an,
                 **{v: series[v].get(an) for v in CONCEPTS}}
            )
        print(f"  {tic:5s} {nom[:40]}")
        time.sleep(0.15)  # la SEC limite à 10 requêtes par seconde

    df = pd.DataFrame(rows)
    money = list(CONCEPTS)
    df[money] = (df[money] / 1e6).round(1)  # millions de dollars US
    return df


WB_INDICATEURS = {
    "NY.GDP.MKTP.CD": "pib_usd",
    "NY.GDP.PCAP.CD": "pib_hab_usd",
    "NY.GDP.MKTP.KD.ZG": "croissance_pib",
    "SP.POP.TOTL": "population",
    "BX.KLT.DINV.WD.GD.ZS": "ide_entrants_pct_pib",
    "NE.TRD.GNFS.ZS": "commerce_pct_pib",
    "GB.XPD.RSDV.GD.ZS": "rd_pct_pib",
    "EG.FEC.RNEW.ZS": "energie_renouv_pct",
}


def build_pays() -> pd.DataFrame:
    meta = requests.get(
        "https://api.worldbank.org/v2/country?format=json&per_page=400", timeout=60
    ).json()[1]
    meta = pd.DataFrame(
        [{"iso3": m["id"], "pays": m["name"], "region": m["region"]["value"],
          "revenu": m["incomeLevel"]["value"]} for m in meta if m["region"]["value"] != "Aggregates"]
    )
    frames = []
    for code, nom in WB_INDICATEURS.items():
        url = (f"https://api.worldbank.org/v2/country/all/indicator/{code}"
               "?format=json&date=2000:2023&per_page=20000")
        js = requests.get(url, timeout=120).json()[1]
        s = pd.DataFrame([{"iso3": r["countryiso3code"], "annee": int(r["date"]), nom: r["value"]}
                          for r in js if r["countryiso3code"]])
        frames.append(s.set_index(["iso3", "annee"]))
        print(f"  {code:22s} -> {nom}")
    wide = pd.concat(frames, axis=1).reset_index()
    df = meta.merge(wide, on="iso3", how="left").sort_values(["iso3", "annee"])
    df["pib_usd"] = (df["pib_usd"] / 1e9).round(2)  # milliards
    df = df.rename(columns={"pib_usd": "pib_milliards_usd"})
    for c in ["pib_hab_usd", "croissance_pib", "ide_entrants_pct_pib", "commerce_pct_pib",
              "rd_pct_pib", "energie_renouv_pct"]:
        df[c] = df[c].round(3)
    return df


SECTEURS = pd.DataFrame(
    [
        ("Automobile", "Constructeurs de véhicules, y compris électriques"),
        ("Technologie", "Logiciels, matériel, semi-conducteurs, plateformes"),
        ("Commerce de détail", "Distribution physique et en ligne"),
        ("Pharmaceutique", "Médicaments et produits de santé"),
        ("Énergie", "Pétrole et gaz intégrés"),
        ("Biens de consommation", "Boissons, hygiène, articles de sport"),
        ("Restauration", "Restauration rapide et cafés"),
        ("Industrie", "Aéronautique, machinerie, conglomérats industriels"),
        ("Médias et divertissement", "Diffusion en continu et contenus"),
    ],
    columns=["secteur", "description"],
)


def main() -> None:
    print("SEC EDGAR…")
    ent = build_entreprises()
    ent.to_csv(DATA / "entreprises.csv", index=False)
    ent.to_csv(DATA / "entreprises_fr.csv", index=False, sep=";", decimal=",", encoding="cp1252")
    print("Banque mondiale…")
    pays = build_pays()
    pays.to_csv(DATA / "pays.csv", index=False)
    SECTEURS.to_csv(DATA / "secteurs.csv", index=False)

    db = DATA / "strategie.db"
    db.unlink(missing_ok=True)
    with sqlite3.connect(db) as con:
        ent.to_sql("entreprises", con, index=False)
        pays.to_sql("pays", con, index=False)
        SECTEURS.to_sql("secteurs", con, index=False)
    print(f"entreprises {ent.shape}  pays {pays.shape}  -> {DATA}")


if __name__ == "__main__":
    main()
