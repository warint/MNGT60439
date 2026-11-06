"""Séance 1 — vérifier que votre poste de travail est prêt.

Exécutez ce fichier depuis la racine du dépôt (le dossier qui contient data/) :

    python 01-installer-la-plateforme/00-pre-seance/verifier_environnement.py

Chaque ligne affiche OK ou ÉCHEC, avec la marche à suivre en cas d'échec.
Apportez la sortie complète en classe si une ligne reste en ÉCHEC.
"""

from __future__ import annotations

import importlib
import platform
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
ok = True


def ligne(etat: bool, quoi: str, conseil: str = "") -> None:
    global ok
    ok &= etat
    print(f"[{'OK    ' if etat else 'ÉCHEC '}] {quoi}")
    if not etat and conseil:
        print(f"         → {conseil}")


print(f"Python {platform.python_version()} · {platform.system()} {platform.machine()}")
print(f"Interpréteur : {sys.executable}\n")

ligne(sys.version_info >= (3, 11), "Python 3.11 ou plus récent",
      "Installez Python 3.12 ou 3.13 depuis https://www.python.org/downloads/")
ligne(sys.prefix != sys.base_prefix, "Environnement virtuel actif (.venv)",
      "Activez-le : source .venv/bin/activate (macOS) ou .venv\\Scripts\\activate (Windows)")

for paquet in ["pandas", "numpy", "matplotlib", "seaborn", "plotly", "scipy",
               "statsmodels", "requests", "yfinance", "wbgapi", "openpyxl", "duckdb"]:
    try:
        m = importlib.import_module(paquet)
        ligne(True, f"{paquet:12s} {getattr(m, '__version__', '')}")
    except ImportError:
        ligne(False, f"{paquet:12s} manquant", "python -m pip install -r requirements.txt")

try:
    import pandas as pd

    df = pd.read_csv(RACINE / "data" / "entreprises.csv")
    ligne(df.shape == (480, 12), f"data/entreprises.csv lu : {df.shape[0]} lignes × {df.shape[1]} colonnes")
except Exception as e:  # noqa: BLE001
    ligne(False, f"lecture de data/entreprises.csv ({e})",
          "Exécutez ce script depuis la racine du dépôt.")

try:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    sortie = RACINE / "sorties"
    sortie.mkdir(exist_ok=True)
    tesla = df[df["ticker"] == "TSLA"]
    plt.plot(tesla["annee"], tesla["chiffre_affaires"] / 1000, marker="o")
    plt.title("Tesla — chiffre d'affaires (milliards $ US)")
    plt.savefig(sortie / "test_graphique.png", dpi=100)
    ligne(True, "Graphique enregistré dans sorties/test_graphique.png")
except Exception as e:  # noqa: BLE001
    ligne(False, f"graphique ({e})")

try:
    import requests

    r = requests.get("https://api.worldbank.org/v2/country/CAN?format=json", timeout=15)
    ligne(r.ok, "Accès Internet sécurisé (API de la Banque mondiale)")
except requests.exceptions.SSLError:
    ligne(False, "Certificats SSL introuvables",
          "macOS : double-cliquez « Install Certificates.command » dans Applications/Python 3.x")
except Exception as e:  # noqa: BLE001
    ligne(False, f"Accès Internet ({type(e).__name__})", "Vérifiez votre connexion ou le proxy.")

try:
    import pandas as pd

    pd.read_csv("https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv", nrows=5)
    ligne(True, "pandas lit un fichier CSV en ligne (certificats en ordre)")
except Exception as e:  # noqa: BLE001
    ligne(False, f"pandas.read_csv sur une URL ({type(e).__name__})",
          "macOS : « Install Certificates.command » dans Applications/Python 3.x, puis relancez.")

print("\nTout est prêt. À mercredi !" if ok else "\nAu moins une ligne en ÉCHEC : apportez cette sortie en classe.")
