# Les premiers pas — travail 2

**MNGT 60439 — Données et stratégie : enjeux locaux et mondiaux**
Thierry Warin · **5 %** de la note finale · **équipes de deux** · remise : **à confirmer** (ZoneCours)

---

## Ce que l'on vous demande

Le travail 2 rassemble tout ce que les séances 1 à 6 ont enseigné : **importer, nettoyer,
décrire, représenter, tester**. Vous l'appliquez à une question de stratégie que vous choisissez,
idéalement celle de votre projet de recherche individuel ou une version préliminaire.

Ce n'est pas un article. C'est la preuve, en deux pages et un fichier de code, que vous savez
passer d'une question à des données, et des données à une réponse honnête.

---

## Le contenu attendu

| | Élément | Précisions |
|---|---|---|
| **1** | **Une question de recherche** en stratégie | Une phrase. Elle doit pouvoir être fausse. « Le secteur pharmaceutique investit-il davantage en R-D, par dollar de ventes, que le secteur technologique ? » plutôt que « La R-D en général ». |
| **2** | **Une ou deux sources de données** importées avec Python | Au moins **une** par URL, API ou paquet (`requests`, `wbgapi`, `yfinance`, l'API de la SEC, Our World in Data…). Les fichiers du dossier `data/` comptent comme seconde source. Citez chaque source, avec sa date de consultation et sa licence. |
| **3** | **Le nettoyage**, dit en clair | Lignes retirées et pourquoi, valeurs manquantes et leur traitement, fusions (`merge`) et leur clé, unités. Combien d'observations à chaque étape. |
| **4** | **Au moins trois statistiques descriptives** | Choisies et interprétées : moyenne **ou** médiane (justifiez), une mesure de dispersion, une comparaison par groupe. |
| **5** | **Deux graphiques soignés** | Titre qui dit ce qu'il faut voir, axes avec unités, source sous le graphique. Pas de graphique décoratif. |
| **6** | **Un test ou une corrélation**, interprété honnêtement | L'écart ou le coefficient **en unités**, son intervalle de confiance, puis la valeur p. Un résultat nul est un résultat : dites-le. Si vos données forment un panel, dites comment vous avez traité la dépendance entre années (une seule année, ou erreurs regroupées). |
| **7** | **Ce que vous ne pouvez pas conclure** | Au moins une limite : échantillon, mesure, causalité. |
| **8** | **La déclaration d'usage de l'IA** | Ce que vous avez demandé, à quel outil, et **ce que vous avez vérifié, et comment**. « Aucun usage » est une réponse acceptable. |

---

## Ce que vous remettez

1. **Un document de deux pages au maximum** (PDF), hors bibliographie et déclaration d'IA. Les
   deux graphiques comptent dans les deux pages.
2. **Un fichier `.py`** qui s'exécute **de bout en bout, depuis la racine du dépôt**, avec la
   commande :

   ```bash
   python travail2_equipeXX.py
   ```

   Il importe les données, les nettoie, calcule tous les chiffres du document et enregistre les
   deux graphiques dans `sorties/`. Un chiffre du document qui ne sort pas du code ne compte pas.

> Si votre source exige une clé d'API, lisez-la depuis une variable d'environnement
> (`os.environ["MA_CLE"]`) et **ne la laissez jamais dans le fichier remis**. Indiquez dans un
> commentaire comment obtenir une clé.

---

## Grille d'évaluation (sur 20 points)

| Critère | Points | Excellent | Insuffisant |
|---|---:|---|---|
| **Question** | 3 | Précise, réfutable, pertinente pour un dirigeant | Vague, ou impossible à trancher avec des données |
| **Importation** | 3 | Au moins une source par URL, API ou paquet ; sources citées avec date et licence | Uniquement des fichiers fournis ; source non citée |
| **Nettoyage** | 3 | Chaque étape justifiée, nombre d'observations suivi | Lignes disparues sans explication |
| **Description** | 3 | Statistiques choisies et interprétées, en unités | `describe()` collé sans commentaire |
| **Graphiques** | 3 | Lisibles, titrés, unités et sources ; chacun appuie un argument | Défauts de lecture, légendes absentes, graphique décoratif |
| **Test ou corrélation** | 3 | Écart en unités, intervalle, valeur p bien lue ; limites et dépendance des observations traitées | « Significatif » sans ampleur ; causalité tirée d'une corrélation |
| **Code** | 2 | S'exécute de bout en bout depuis la racine ; lisible, commenté | Ne s'exécute pas, ou chemins propres à votre ordinateur |

**Pénalités :** document de plus de deux pages (−2) ; déclaration d'IA absente (−2) ; clé d'API
dans le code (−1).

---

## Ce qui coûte des points

- Un chiffre du document qui ne sort pas du code.
- Un chemin du type `C:\Users\moi\Desktop\...` : le correcteur n'a pas votre ordinateur.
- Une période ou un sous-échantillon choisis **après** avoir vu les résultats.
- « Pas significatif, donc aucun effet. »
- Une référence ou un chiffre fourni par l'IA et non vérifié.

---

[← Retour à la séance 06](README.md)
