"""Séance 4 — Atelier : qui sont les vrais concurrents de mon entreprise,
et que dit la Bourse de ses acquisitions ?

Exécutez depuis la racine du dépôt (le dossier qui contient data/).
Dans VS Code, chaque bloc « # %% » s'exécute avec Maj + Entrée.

Remplacez chaque TODO. Le script doit tourner de haut en bas sans erreur avant d'être remis.
La partie 4 télécharge des cours boursiers (Internet requis la première fois) ; ils sont
ensuite gardés dans data/cache/ et le script fonctionne hors ligne.
"""

# %% 0. Les outils
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

Path("sorties").mkdir(exist_ok=True)

# TODO : choisissez votre entreprise parmi les 32 (son ticker, ex. "PFE", "KO", "TSLA")
MON_ENTREPRISE = "TODO"

entreprises = pd.read_csv("data/entreprises.csv")


# %% 1. Comparer à son secteur, la même année (20 min)
# Le rendement des actifs (ROA) : résultat net / actifs totaux
entreprises["roa"] = entreprises["resultat_net"] / entreprises["actifs_totaux"]

# TODO : roa_secteur = moyenne du ROA par (secteur, annee), sur CHAQUE ligne
#        indice : groupby([...])["roa"].transform("mean")

# TODO : ecart_secteur = roa - roa_secteur

# TODO : affichez annee, roa, roa_secteur, ecart_secteur pour MON_ENTREPRISE (2019-2024)

# TODO : refaites le calcul avec la MÉDIANE du secteur. Le diagnostic change-t-il ?
#        Répondez en commentaire, chiffres à l'appui.

# TODO : combien d'entreprises compte votre secteur ? (nunique) Qu'est-ce que cela change ?


# %% 2. Un tableau de synthèse par secteur, 2023 (10 min)
# TODO : avec groupby("secteur").agg(...) et l'agrégation nommée, produisez :
#        n (nombre d'entreprises), roa_moyen, roa_median, rd_publiee (nombre de valeurs non
#        manquantes de rd). Triez par roa_median décroissant.


# %% 3. Remodeler (10 min)
# TODO : un tableau LARGE : une ligne par année, une colonne par entreprise de VOTRE secteur,
#        valeurs = roa (pivot). Gardez 2019 et après.

# TODO : remettez-le au format LONG avec melt. Combien de lignes ? Pourquoi ce nombre ?


# %% 4. Nettoyer un fichier d'annonces de fusions-acquisitions (20 min)
brut = pd.read_csv("04-manipuler-les-donnees/02-pratique/donnees/annonces_fa.csv", sep=";")
print(brut)
print(brut.dtypes)

# TODO : renommez les colonnes : ticker, cible, date, valeur_gusd, secteur_cible

# TODO : nettoyez ticker (espaces, majuscules) avec .str

# TODO : convertissez date en vraie date : pd.to_datetime(..., format="%d/%m/%Y")

# TODO : convertissez valeur_gusd en nombre (virgule décimale ! puis errors="coerce")
#        et créez une colonne valeur_manquante (booléen) AVANT toute autre opération

# TODO : retirez les doublons ; affichez le nombre de lignes avant et après

# TODO : ajoutez entreprise et secteur de l'acquéreur avec un merge sur ticker
#        (how="left", validate="m:1", indicator=True). Vérifiez que le nombre de lignes
#        n'a pas changé.


# %% 5. Que dit la Bourse ? Un premier regard (20 min)
def cours(ticker, debut="2021-06-01", fin="2023-12-31"):
    """Cours de clôture ajustés, mis en cache dans data/cache/ au premier appel."""
    fichier = Path("data/cache") / f"{ticker}.parquet"
    if not fichier.exists():
        fichier.parent.mkdir(parents=True, exist_ok=True)
        d = yf.download(ticker, start=debut, end=fin, progress=False, auto_adjust=True)
        d.columns = [c[0] if isinstance(c, tuple) else c for c in d.columns]
        d.to_parquet(fichier)
    return pd.read_parquet(fichier)["Close"]


def fenetre(ticker, annonce, avant=5, apres=5):
    """Rendement anormal naïf (entreprise - SPY) autour d'une annonce."""
    prix = pd.DataFrame({ticker: cours(ticker), "SPY": cours("SPY")})
    r = prix.pct_change().dropna()
    # TODO : colonne "anormal" = rendement de l'entreprise - rendement de SPY

    # Une annonce peut tomber un dimanche : searchsorted prend le jour de Bourse suivant.
    i = r.index.searchsorted(pd.Timestamp(annonce))
    w = r.iloc[i - avant : i + apres + 1].copy()
    w["jour"] = range(-avant, apres + 1)
    # TODO : colonne "cumul" = somme cumulée de "anormal"

    return w


# TODO : appliquez fenetre() à chaque annonce du fichier nettoyé (boucle sur fa.iterrows()),
#        ajoutez une colonne "cible" à chaque fenêtre, puis EMPILEZ-les avec pd.concat

# TODO : un tableau : une ligne par annonce, le cumul au jour +5, trié

# TODO : un graphique : une ligne par annonce (cumul en %, jours -5 à +5), ligne verticale
#        à 0 ; enregistrez-le dans sorties/seance04_car.png


# %% 6. Ce que ce calcul ne permet pas de conclure (10 min)
# TODO : en trois à cinq lignes de commentaire : pourquoi ces cumuls ne prouvent-ils pas que
#        les acquisitions créent ou détruisent de la valeur ? Citez au moins deux limites
#        (voir la dernière diapositive du cours).
