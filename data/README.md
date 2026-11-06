# Les données du cours

Toutes les données sont **réelles** et proviennent de sources publiques. Elles sont reconstruites
par [`scripts/build_course_data.py`](../scripts/build_course_data.py) :

```bash
export SEC_USER_AGENT="Prénom Nom courriel@exemple.com"   # exigé par la SEC
python scripts/build_course_data.py
```

| Fichier | Unité d'observation | Lignes | Source | Licence |
|---|---|---|---|---|
| `entreprises.csv` | entreprise × exercice (2010–2024) | 480 | SEC EDGAR, API XBRL *companyfacts* | Domaine public (gouvernement des États-Unis) |
| `entreprises_fr.csv` | idem, au format « Excel français » (`;`, virgule décimale, Windows-1252) | 480 | idem | idem |
| `pays.csv` | pays × année (2000–2023) | 5 208 | Banque mondiale, *World Development Indicators*, API v2 | CC BY 4.0 |
| `secteurs.csv` | secteur | 9 | Construit pour le cours | — |
| `strategie.db` | base SQLite : tables `entreprises`, `pays`, `secteurs` | — | idem | idem |

> Citation pour `pays.csv` : Banque mondiale, *World Development Indicators*, consulté via l'API
> v2 (<https://data.worldbank.org>), licence CC BY 4.0.

---

## `entreprises.csv`

32 grandes entreprises cotées aux États-Unis, choisies pour couvrir neuf secteurs. Montants en
**millions de dollars US**, alignés sur l'**année civile** (champ `frame` de la SEC : l'exercice
qui se termine dans l'année ; les stocks sont mesurés en fin d'année).

| Variable | Description |
|---|---|
| `ticker` | Symbole boursier |
| `entreprise` | Nom usuel |
| `cik` | Identifiant permanent du déclarant à la SEC |
| `secteur` | Secteur (voir `secteurs.csv`) |
| `pays_siege` | Pays du siège social (code ISO3 ; toutes `USA`) |
| `annee` | Année civile |
| `chiffre_affaires` | Revenus totaux (balises *Revenues*, *RevenueFromContractWithCustomer…*, *SalesRevenueNet*) |
| `resultat_net` | Résultat net (*NetIncomeLoss*) |
| `actifs_totaux` | Total de l'actif, fin d'année (*Assets*) |
| `capitaux_propres` | Capitaux propres, fin d'année (*StockholdersEquity*) |
| `rd` | Dépenses de recherche et développement (*ResearchAndDevelopmentExpense*) |
| `investissements` | Acquisitions d'immobilisations corporelles (*PaymentsToAcquirePropertyPlantAndEquipment*) |

### Pièges connus — à lire avant d'analyser

- **`rd` manque pour environ 28 % des lignes.** Les distributeurs (Walmart, Costco, Target), la
  restauration (McDonald's, Starbucks), Coca-Cola, Nike, General Motors et Amazon ne publient pas
  de ligne « R-D » sous cette balise. Amazon en dépense énormément, mais l'appelle
  *Technology and infrastructure*. Une valeur manquante n'est **pas** un zéro.
- **`investissements` manque pour environ 25 % des lignes**, pour des raisons semblables
  (balises différentes selon l'entreprise).
- Les **exercices décalés** (Apple, Microsoft, Nike, Costco…) sont rangés dans l'année civile où
  ils se terminent : l'exercice 2023 de Microsoft se termine le 30 juin 2023.
- Merck 2023 : la R-D (30,5 G$) inclut une acquisition de R-D en cours (Prometheus) ; c'est le
  chiffre publié, pas une erreur.
- Ce sont des **entreprises survivantes et géantes** : aucune conclusion ne s'étend aux PME, ni
  aux entreprises disparues entre 2010 et 2024.

## `pays.csv`

217 économies (agrégats régionaux exclus) × 2000–2023.

| Variable | Indicateur Banque mondiale | Unité |
|---|---|---|
| `iso3`, `pays` | — | code ISO3, nom anglais |
| `region`, `revenu` | Métadonnées pays | région ; groupe de revenu |
| `annee` | — | — |
| `pib_milliards_usd` | NY.GDP.MKTP.CD | milliards $ US courants |
| `pib_hab_usd` | NY.GDP.PCAP.CD | $ US courants par habitant |
| `croissance_pib` | NY.GDP.MKTP.KD.ZG | % annuel, prix constants |
| `population` | SP.POP.TOTL | habitants |
| `ide_entrants_pct_pib` | BX.KLT.DINV.WD.GD.ZS | IDE, entrées nettes, % du PIB |
| `commerce_pct_pib` | NE.TRD.GNFS.ZS | exportations + importations, % du PIB |
| `rd_pct_pib` | GB.XPD.RSDV.GD.ZS | dépense intérieure de R-D, % du PIB |
| `energie_renouv_pct` | EG.FEC.RNEW.ZS | part des renouvelables dans la consommation finale d'énergie |

### Pièges connus

- `rd_pct_pib` manque pour **58 %** des lignes : beaucoup de pays ne la mesurent pas, ou pas
  chaque année.
- `ide_entrants_pct_pib` peut être **négatif** (désinvestissement) et prend des valeurs extrêmes
  dans les centres financiers (îles Caïmans, Liechtenstein : plus de 1 000 % du PIB certaines années).
- `energie_renouv_pct` s'arrête en 2021 pour la plupart des pays (71 pays en 2022, aucun en 2023).
- Les dollars **courants** mélangent croissance réelle, inflation et taux de change.
