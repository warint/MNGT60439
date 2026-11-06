# Séance 02 — Pratique (deuxième moitié, ~90 min)

> **Diapositives :** [`MGMT60XXX-S02-Pratique.qmd`](MGMT60XXX-S02-Pratique.qmd) ·
> version rendue : [`docs/seance-02-pratique.html`](https://warint.github.io/MNGT60439/seance-02-pratique.html)

## Le thème

> **Quelles entreprises créent le plus de valeur — selon quelle mesure, et dans quel secteur ?**

En équipe de deux, vous calculez quatre mesures de performance, vous comparez leurs classements,
vous trouvez où l'une d'elles ment, puis vous comparez les entreprises à leurs concurrents
directs. Le livrable n'est pas un tableau : c'est un **choix de mesure**, justifié par écrit.

## Point de départ

[`starter/seance02_atelier.py`](starter/seance02_atelier.py) — à copier dans votre dossier de
travail et à exécuter cellule par cellule (`# %%`, puis `Maj + Entrée`) depuis la racine du dépôt.

| Minutes | Étape | Cellule |
|---|---|---|
| 00–10 | Regarder : types, manquants, effectifs | 1 |
| 10–25 | Mesurer : marge nette, ROA, ROE, intensité R-D | 2 |
| 25–40 | Classer : quatre top 5 pour 2023 | 3 |
| 40–50 | Le piège du dénominateur : capitaux propres négatifs | 4 |
| 50–70 | À l'intérieur des secteurs | 5 |
| 70–80 | Une année ou quinze ? | 6–7 |
| 80–90 | Écrire, puis deux minutes devant la classe | — |

## Livrable

Le script complété **et** une note de 200 mots (`note_seance02.md`) :

- quelle entreprise crée le plus de valeur, selon quelle mesure, et pourquoi cette mesure ;
- ce que vous avez fait des capitaux propres négatifs ;
- ce que votre classement ne permet pas d'affirmer ;
- une réponse de l'IA que vous avez vérifiée, et comment.

À remettre selon les consignes du plan de cours.

## Ce qui coûte des points

- Un classement sans préciser la mesure et l'année
- Un ROE interprété alors que les capitaux propres sont négatifs
- Des `NaN` remplacés par 0 sans justification
- Une médiane de secteur sans son effectif
- Un script qui ne s'exécute pas de haut en bas

---

[← Retour à la séance 02](../README.md)
