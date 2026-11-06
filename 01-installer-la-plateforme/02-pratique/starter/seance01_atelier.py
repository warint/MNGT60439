"""Séance 1 — Atelier : Tesla est-elle plus rentable que Ford, et depuis quand ?

Exécutez depuis la racine du dépôt (le dossier qui contient data/).
Dans VS Code, chaque bloc « # %% » s'exécute avec Maj + Entrée.

Remplacez chaque TODO. Le script doit tourner de haut en bas sans erreur avant d'être remis.
"""

# %% 0. Les outils
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

Path("sorties").mkdir(exist_ok=True)   # le dossier où l'on enregistre les figures

# %% 1. Lire les données (15 min)
entreprises = pd.read_csv("data/entreprises.csv")

# TODO : affichez le nombre de lignes et de colonnes (attribut .shape)

# TODO : affichez les 5 premières lignes (méthode .head())

# TODO : quelles sont les colonnes ? Lesquelles ont des valeurs manquantes ? (méthode .info())


# %% 2. Une fonction (10 min)
def marge_nette(resultat, ventes):
    """Part de chaque dollar de ventes qui reste en profit."""
    # TODO : retournez le bon calcul
    return None


# Test : la marge de Tesla en 2023 doit être d'environ 15,5 %
test = marge_nette(14_974, 96_773)
print("Fonction à compléter" if test is None else f"Tesla 2023 : {test:.1%}")


# %% 3. Les trois constructeurs (20 min)
auto = entreprises[entreprises["secteur"] == "Automobile"].copy()

# TODO : créez une colonne "marge" avec votre fonction, appliquée aux colonnes
#        resultat_net et chiffre_affaires

# TODO : affichez entreprise, annee, chiffre_affaires, resultat_net, marge pour 2023,
#        triés de la marge la plus élevée à la plus faible


# %% 4. Depuis quand ? (20 min)
# TODO : tracez la marge de Tesla, Ford et GM de 2010 à 2024 sur un même graphique
#        (une ligne par entreprise ; un titre ; une légende)
fig, ax = plt.subplots(figsize=(8, 4))

# ...

fig.savefig("sorties/seance01_marges.png", dpi=150, bbox_inches="tight")

# TODO : à partir de quelle année la marge de Tesla dépasse-t-elle durablement celle de Ford ?
#        Répondez dans un commentaire, en citant la valeur.


# %% 5. Ce que les données ne disent pas (15 min)
# TODO : en trois lignes de commentaire, dites pourquoi ce résultat ne permet PAS de conclure
#        que « Tesla est bonne pour l'environnement ». Quelles données faudrait-il ?

# TODO : demandez à votre assistant d'IA d'expliquer le code de la section 3, ligne par ligne.
#        Copiez ici la requête, et UNE chose que vous avez vérifiée vous-même dans sa réponse.
