# Séance 01 — Préparation (pré-séance)

> **[Diapositives de la pré-séance](https://warint.github.io/MNGT60439/seance-01-pre-seance.html)** ·
> source : [`MGMT60XXX-S01-Pre-Seance.qmd`](MGMT60XXX-S01-Pre-Seance.qmd)

> Faites **les cinq étapes** avant le cours. Prévoyez 90 à 120 minutes.

| | Avant le cours | Durée | Sert, en classe, à |
|---|---|---|---|
| **1** | Lire Miller (2007) | 30–45 min | la discussion d'ouverture |
| **2** | Installer Python 3.12/3.13 et VS Code | 20–30 min | tout le cours |
| **3** | Créer `.venv` et installer les paquets | 15 min | tout le cours |
| **4** | Exécuter `verifier_environnement.py` | 5 min | la première minute de la pratique |
| **5** | Choisir un assistant d'IA, faire l'autovérification | 15 min | le cours |

---

## Étape 1 — Lecture

**Miller, D. (2007). *Paradigm Prison, or In Praise of Atheoretic Research*.** *Strategic
Organization*, 5(2), 177–184. <https://doi.org/10.1177/1476127007077558>

Annotez : (1) la thèse en une phrase ; (2) ce que l'auteur reproche à la recherche guidée par la
théorie ; (3) le rôle qu'il donne à l'observation des données ; (4) une objection.

## Étape 2 — Installer Python et VS Code

- **Python 3.12 ou 3.13** : <https://www.python.org/downloads/>
  - Windows : cochez **« Add python.exe to PATH »**.
  - macOS : après l'installation, double-cliquez **`Install Certificates.command`** dans
    `Applications/Python 3.x`. Sans cela, `pd.read_csv("https://…")` échoue avec
    `CERTIFICATE_VERIFY_FAILED`.
- **VS Code** : <https://code.visualstudio.com/>, puis les extensions **Python** et **Jupyter**
  (Microsoft).

## Étape 3 — Le dossier du cours et l'environnement virtuel

Téléchargez le dossier du cours depuis <https://github.com/warint/MNGT60439> (**Code → Download
ZIP**, ou `git clone https://github.com/warint/MNGT60439.git mngt60xxx`), décompressez-le sur le Bureau sous
le nom `mngt60xxx`, ouvrez-le dans VS Code (**Fichier → Ouvrir le dossier**), puis, dans le terminal
intégré :

```bash
# macOS
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

```powershell
# Windows (PowerShell)
py -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Puis `Ctrl/Cmd + Maj + P` → **Python: Select Interpreter** → l'interpréteur de `.venv`.

## Étape 4 — Vérifier

```bash
python 01-installer-la-plateforme/00-pre-seance/verifier_environnement.py
```

Toutes les lignes doivent afficher `OK`. Sinon, suivez la consigne affichée ; si elle ne suffit
pas, écrivez-moi **avec la sortie complète**.

## Étape 5 — IA générative et autovérification

Choisissez un assistant (ChatGPT, Claude, Copilot, Gemini…) et demandez-lui de vous expliquer
ce qu'est un environnement virtuel, puis de vous poser deux questions. Répondez ensuite par
écrit :

1. Différence entre **Python**, un **paquet** et un **environnement virtuel** ?
2. Que donnent `print(2023 + 1)` et `print("2023" + "1")` ? Pourquoi ?
3. Une **question précise et mesurable** tirée de « Tesla est bonne pour l'environnement ».
4. Selon Miller (2007), qu'apporte une recherche « atéorique » ?

> **Règle permanente du cours.** Chaque usage de l'IA dans un travail remis est déclaré : ce que
> vous avez demandé, ce que vous avez vérifié, et comment.

---

[← Retour à la séance 01](../README.md)
