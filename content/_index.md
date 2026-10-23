---
title: Modèles génératifs profonds
type: docs
---

# Modèles génératifs profonds

Bienvenue dans le cours **Modèles génératifs profonds**. Le mot-clé de ce cours, c'est **générer** : pas reconnaître, pas classifier, mais **créer du nouveau**. Au fil de 15 semaines, nous passerons des représentations apprises par les réseaux de neurones aux grandes familles de modèles génératifs : modèles auto-régressifs, autoencodeurs variationnels, flots normalisants, modèles fondés sur l'énergie, GAN, score matching, diffusion, jusqu'aux modèles hybrides modernes.

## Comment fonctionne chaque semaine ?

1. **Vidéo d'introduction** : une courte animation pose la question centrale de la semaine.
2. **Support PDF** : téléchargez et étudiez le support complet de la semaine.
3. **Laboratoire** : des exercices avec solutions (cachées par défaut) pour pratiquer.
4. **Quiz** : cinq questions pour vérifier votre compréhension.

Toutes les deux semaines, une **évaluation** (mini-projet pratique) met en œuvre les notions vues. Le cours se termine par un **projet final** de synthèse.

## Plan du cours

### Chapitre 01 : Fondements

| Semaine | Thème | Évaluation |
|:--|:--|:--|
| 1 | [Rappels NN & Représentations]({{< ref "/docs/ch1-fondements/week01" >}}) |  |
| 2 | [Discriminatif vs Génératif]({{< ref "/docs/ch1-fondements/week02" >}}) | [Évaluation 1]({{< ref "/docs/ch1-fondements/evaluation-1" >}}) |
| 3 | [Maximum de vraisemblance & Factorisation]({{< ref "/docs/ch1-fondements/week03" >}}) |  |
| 4 | [Variables latentes & inférence]({{< ref "/docs/ch1-fondements/week04" >}}) | [Évaluation 2]({{< ref "/docs/ch1-fondements/evaluation-2" >}}) |

### Chapitre 02 : Familles de modèles génératifs

| Semaine | Thème | Évaluation |
|:--|:--|:--|
| 5 | [Modèles auto-régressifs]({{< ref "/docs/ch2-familles/week05" >}}) |  |
| 6 | [Autoencodeurs profonds]({{< ref "/docs/ch2-familles/week06" >}}) | [Évaluation 3]({{< ref "/docs/ch2-familles/evaluation-3" >}}) |
| 7 | [Autoencodeurs variationnels (VAE)]({{< ref "/docs/ch2-familles/week07" >}}) |  |
| 8 | [Flots normalisants]({{< ref "/docs/ch2-familles/week08" >}}) | [Évaluation 4]({{< ref "/docs/ch2-familles/evaluation-4" >}}) |
| 9 | [Modèles fondés sur l'énergie (EBM)]({{< ref "/docs/ch2-familles/week09" >}}) |  |
| 10 | [Modèles génératifs implicites]({{< ref "/docs/ch2-familles/week10" >}}) | [Évaluation 5]({{< ref "/docs/ch2-familles/evaluation-5" >}}) |

### Chapitre 03 : Modèles génératifs modernes

| Semaine | Thème | Évaluation |
|:--|:--|:--|
| 11 | [Score Matching]({{< ref "/docs/ch3-modernes/week11" >}}) |  |
| 12 | [Modèles de diffusion]({{< ref "/docs/ch3-modernes/week12" >}}) | [Évaluation 6]({{< ref "/docs/ch3-modernes/evaluation-6" >}}) |
| 13 | [Modèles hiérarchiques]({{< ref "/docs/ch3-modernes/week13" >}}) |  |
| 14 | [Hybridation & modèles modernes]({{< ref "/docs/ch3-modernes/week14" >}}) | [Évaluation 7]({{< ref "/docs/ch3-modernes/evaluation-7" >}}) |
| 15 | [Projet & synthèse]({{< ref "/docs/ch3-modernes/week15" >}}) | [Projet final]({{< ref "/docs/ch3-modernes/projet-final" >}}) |

## Évaluations

| Évaluation | Semaines | Mini-projet |
|:--|:--|:--|
| [Évaluation 1]({{< ref "/docs/ch1-fondements/evaluation-1" >}}) | S1–S2 | Représentations apprises : classifier n’est pas générer |
| [Évaluation 2]({{< ref "/docs/ch1-fondements/evaluation-2" >}}) | S3–S4 | Maximum de vraisemblance et variable latente |
| [Évaluation 3]({{< ref "/docs/ch2-familles/evaluation-3" >}}) | S5–S6 | Génération auto-régressive vs reconstruction par autoencodeur |
| [Évaluation 4]({{< ref "/docs/ch2-familles/evaluation-4" >}}) | S7–S8 | Deux façons de structurer un espace latent : VAE vs Flow |
| [Évaluation 5]({{< ref "/docs/ch2-familles/evaluation-5" >}}) | S9–S10 | Énergie vs génération implicite |
| [Évaluation 6]({{< ref "/docs/ch3-modernes/evaluation-6" >}}) | S11–S12 | Du score au modèle de diffusion |
| [Évaluation 7]({{< ref "/docs/ch3-modernes/evaluation-7" >}}) | S13–S14 | Génération dans un espace latent + Flow Matching |
| [Projet final]({{< ref "/docs/ch3-modernes/projet-final" >}}) | S15 | Quel modèle génératif choisir ? |

## Conseils pour réussir

- **Commencez par la vidéo** : elle donne l'intuition avant les équations.
- **Suivez le fil conducteur** : chaque semaine répond à une limite de la précédente (reconstruire ≠ générer, borne ≠ vraisemblance exacte, densité ≠ échantillonnage…).
- **Cherchez avant de regarder la solution** dans les laboratoires.
- **Les mini-projets visent la compréhension**, pas la performance : interprétez vos résultats en termes probabilistes.
- **Datasets fil rouge** : MNIST et Fashion-MNIST, plus des jeux 2D quand la visualisation géométrique est essentielle.
