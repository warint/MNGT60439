# Séance 03 — Préparation

> **[Ouvrir les diapositives de la pré-séance](https://warint.github.io/MNGT60439/seance-03-pre-seance.html)** ·
> source : [`MNGT60439-S03-Pre-Seance.qmd`](MNGT60439-S03-Pre-Seance.qmd)

> Comptez **80 minutes**. Tout ce qui suit doit être fait **avant** le cours.

| | Avant le cours | Durée | Utilisé pour |
|---|---|---|---|
| **1** | Lire l'article | 45 min | situer les sources de données en gestion internationale |
| **2** | Définir `SEC_USER_AGENT` | 5 min | l'API de la SEC |
| **3** | (Facultatif) clé d'API FRED | 5 min | l'exemple de clé d'API |
| **4** | Certificats (macOS) | 2 min | lire une URL avec pandas |
| **5** | Tester l'accès aux sources | 10 min | arriver avec un poste qui fonctionne |
| **6** | Autovérification | 15 min | le cours suppose qu'elle est tentée |

---

## 1 — Lecture

**Bosma, B. et van Witteloostuijn, A. (2024). Machine learning in international business.
*Journal of International Business Studies*, 55(6), 676–702.**
<https://doi.org/10.1057/s41267-024-00687-6>

Notez : (1) la question de recherche en une phrase ; (2) les **sources de données** citées —
lesquelles sont nouvelles ? ; (3) l'élément de preuve le plus fort ; (4) une limite.

## 2 — Votre identité pour la SEC

La SEC exige que chaque programme s'identifie par **votre** nom et **votre** courriel. Rangez-les
dans une variable d'environnement — jamais dans un script :

```bash
# macOS / Linux : ajoutez à ~/.zshrc, puis rouvrez le terminal
export SEC_USER_AGENT="Prénom Nom prenom.nom@hec.ca"
# Windows (PowerShell), puis rouvrez le terminal
setx SEC_USER_AGENT "Prénom Nom prenom.nom@hec.ca"
```

Relancez VS Code ensuite : il lit les variables d'environnement à son démarrage.

## 3 — (Facultatif) Clé d'API FRED

Compte gratuit sur <https://fred.stlouisfed.org/>, puis clé sur
<https://fred.stlouisfed.org/docs/api/api_key.html>. Rangez-la dans `FRED_API_KEY`, de la même
façon. Une clé publiée sur GitHub se révoque immédiatement.

## 4 — Certificats (macOS)

Si `pd.read_csv("https://…")` échoue avec `CERTIFICATE_VERIFY_FAILED` : Finder → Applications →
Python 3.x → double-cliquez **`Install Certificates.command`**. Dépannage d'un soir :

```bash
export SSL_CERT_FILE=$(python -c "import certifi; print(certifi.where())")
```

## 5 — Tester l'accès aux sources

Le bloc de code de la diapositive « Tester l'accès aux sources » doit afficher `True`, `200`,
`200` et `(5, 79)`. Sinon, apportez la sortie en classe.

## 6 — Autovérification

1. Dans un éditeur de texte, quel est le séparateur de colonnes de `data/entreprises_fr.csv` ? Le séparateur décimal ?
2. Que signifient les codes de statut `200`, `404`, `429` ?
3. Pourquoi une clé d'API ne doit-elle jamais être écrite dans un script versionné ?
4. Quelles colonnes relient la table `entreprises` à la table `pays` dans `data/strategie.db` ?

> **Règle permanente du cours.** Chaque fois que l'IA intervient dans un travail remis, vous
> indiquez ce que vous lui avez demandé et ce que vous avez vérifié, et comment.

---

[Retour à la séance 03](../README.md)
