# Plan de cours — MNGT 60439

## Données et stratégie : enjeux locaux et mondiaux

**HEC Montréal** · Marie-Ann, Russell et Thierry Warin, PhD · *Version de travail — pour discussion*

---

## 1. Description

Les décisions stratégiques s'appuient de plus en plus sur des données : rendement d'une
acquisition, positionnement face aux concurrents, performance environnementale, attractivité
d'un pays pour l'investissement. Ce cours apprend à transformer une question de stratégie en
question mesurable, à réunir et analyser les données qui y répondent, et à dire honnêtement
ce qu'une analyse fondée sur les données permet — et ne permet pas — de conclure.

Le cours se déroule en trois blocs :

1. **Les outils (séances 1 à 6, Thierry Warin).** Python sur des données réelles : installer la
   plateforme, manipuler un tableau de données, importer (CSV, URL, paquets, API, bases de
   données), transformer, représenter et tester.
2. **Les questions (séances 7 à 11, Marie-Ann et Russell).** Articles de recherche et études de
   cas (Harvard Business Publishing, Ivey Publishing, dépôts de recherche) : fusions-acquisitions,
   ESG, groupes stratégiques, rémunération des dirigeants ; coaching des projets.
3. **Les projets (séances 12 et 13).** Présentations individuelles de vulgarisation.

## 2. Objectifs d'apprentissage

À la fin du cours, l'étudiant·e sera capable de :

- formuler une question de recherche en stratégie et la justifier ;
- identifier, importer et documenter les données pertinentes ;
- nettoyer, joindre et transformer ces données avec Python ;
- les représenter graphiquement de manière juste et lisible ;
- appliquer et interpréter des statistiques descriptives et des tests simples ;
- s'appuyer sur un article modèle pour construire une démarche empirique ;
- communiquer ses résultats à un public professionnel, limites comprises ;
- utiliser l'IA générative de manière transparente et vérifiée.

## 3. Calendrier

| # | Séance | Enseignant·e | Méthodes / format | Lecture principale |
|---|---|---|---|---|
| 01 | Installer la plateforme | TW | Python, VS Code, environnement virtuel ; premier DataFrame | Miller (2007) |
| 02 | Le DataFrame | TW | Sélection, filtres, nouvelles variables, `groupby` | McKinney (2010) ; McKinney (2022), ch. 5 |
| 03 | Importer des données | TW | CSV, Excel, URL, paquets, API, SQLite/DuckDB | Bosma et van Witteloostuijn (2024) |
| 04 | Manipuler les données | TW | Nettoyage, jointures, remodelage, agrégation, séries temporelles | Wickham (2014) |
| 05 | Représenter les données | TW | Galerie PyStatlas : adapter un graphique statistique ; matplotlib, plotly ; choix du graphique | Cleveland et McGill (1984) ; Anscombe (1973) |
| 06 | Statistiques de base | TW | Descriptives, intervalles de confiance, tests t, corrélation, MCO simple | Wasserstein et Lazar (2016) ; Miller et Bamberger (2016) |
| 07 | Fusions-acquisitions et création de valeur | MAB | Étude d'événement ; performance de marché et comptable | MacKinlay (1997) ; Kengelbach et al. (2023) |
| 08 | ESG et écoblanchiment | MAB | Corrélation, MCO | *à compléter* |
| 09 | Groupes stratégiques | RF | Analyse de grappes | *à compléter* |
| 10 | Rémunération des dirigeants et R-D | RF | Panel : effets fixes et aléatoires ; endogénéité | *à compléter* |
| 11 | Coaching individuel — premiers pas | MAB, RF | Rencontres | — |
| 12 | Présentations individuelles (1) | Équipe | 5 min + 5 min de rétroaction | — |
| 13 | Présentations individuelles (2) | Équipe | 5 min + 5 min de rétroaction | — |

Dates, salles et ordre des séances 7 à 11 : **à confirmer**.

## 4. Évaluation

| Niveau | Activité | Poids |
|---|---|---|
| Individuel | Présentation de vulgarisation (S12–S13, 5 min) : importance du sujet et limites d'une analyse fondée sur les données | 10 % |
| Individuel | Participation | 10 % |
| Individuel | **Projet de recherche** (fin de session) : question, brève revue de littérature, article modèle, démarche empirique, données, résultats, discussion, pertinence pratique — **rapport écrit + fichier de code Python** | 60 % |
| Équipe de 2 | **Les premiers pas — travail 1** (MAB, RF) : question de recherche, base(s) de données, article modèle, méthode, premières statistiques descriptives avec code | 5 % |
| Équipe de 2 | **Les premiers pas — travail 2** (TW) : voir [`06-statistiques-de-base/PREMIERS-PAS-TRAVAIL-2.md`](06-statistiques-de-base/PREMIERS-PAS-TRAVAIL-2.md) | 5 % |
| Équipe de 2–3 | Présentation en début de séance (10 min) | 20 % |
| | **Total** | **100 %** |

## 5. IA générative

L'usage de l'IA générative est **permis et encouragé** pour expliquer du code, diagnostiquer une
erreur ou s'exercer. **Règle permanente :** chaque usage dans un travail remis est déclaré —
ce qui a été demandé, ce qui a été vérifié, et comment. Une affirmation non vérifiée d'un modèle
de langage a la valeur d'une affirmation non vérifiée d'un inconnu.

## 6. Logiciels

Python 3.12 ou 3.13, VS Code (extensions Python et Jupyter), paquets listés dans
[`requirements.txt`](requirements.txt). Les séances 7 à 13 ne requièrent pas Python ; le projet
final, oui (fichier de code).

## 7. Références

- Anscombe, F. J. (1973). Graphs in Statistical Analysis. *The American Statistician*, 27(1), 17–21. <https://doi.org/10.1080/00031305.1973.10478966>
- Bosma, B. et van Witteloostuijn, A. (2024). Machine Learning in International Business. *Journal of International Business Studies*, 55(6), 676–702. <https://doi.org/10.1057/s41267-024-00687-6>
- Cleveland, W. S. et McGill, R. (1984). Graphical Perception. *Journal of the American Statistical Association*, 79(387), 531–554. <https://doi.org/10.1080/01621459.1984.10478080>
- Kengelbach, J. et al. (2023). *Bold Moves for Dealmakers in Volatile Markets*. 2023 M&A Report. Boston Consulting Group.
- MacKinlay, A. C. (1997). Event Studies in Economics and Finance. *Journal of Economic Literature*, 35(1), 13–39.
- McKinney, W. (2010). Data Structures for Statistical Computing in Python. *Proceedings of the 9th Python in Science Conference*, 56–61. <https://doi.org/10.25080/Majora-92bf1922-00a>
- McKinney, W. (2022). *Python for Data Analysis* (3ᵉ éd.). O'Reilly. Accès libre : <https://wesmckinney.com/book/>
- Miller, C. C. et Bamberger, P. (2016). Exploring Emergent and Poorly Understood Phenomena in the Strangest of Places. *Academy of Management Discoveries*, 2(4), 313–319. <https://doi.org/10.5465/amd.2016.0115>
- Miller, D. (2007). Paradigm Prison, or In Praise of Atheoretic Research. *Strategic Organization*, 5(2), 177–184. <https://doi.org/10.1177/1476127007077558>
- Teodorescu, M. (2017). *Machine Learning Methods for Strategy Research*. Harvard Business School Research Paper No. 18-011.
- Wasserstein, R. L. et Lazar, N. A. (2016). The ASA Statement on p-Values. *The American Statistician*, 70(2), 129–133. <https://doi.org/10.1080/00031305.2016.1154108>
- Wickham, H. (2014). Tidy Data. *Journal of Statistical Software*, 59(10), 1–23. <https://doi.org/10.18637/jss.v059.i10>
