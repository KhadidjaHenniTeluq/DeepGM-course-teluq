---
title: 'Semaine 3 : Maximum de vraisemblance & Factorisation'
weight: 30
bookCollapseSection: true
---

# Semaine 3 : Maximum de vraisemblance & Factorisation

*Vraisemblance · NLL · Règle de la chaîne · MLE*

## Vidéo d'introduction

{{< video src="videos/semaine-03.mp4" poster="videos/semaine-03.jpg" >}}

> [!IMPORTANT]
> **Question centrale de la semaine**
>
> Comment apprendre une distribution $p_\theta(x)$ à partir des données observées ?

## Mise en contexte

S1 : apprendre des représentations. S2 : distinguer discriminatif et génératif. S3 : apprendre **réellement** un modèle génératif. Idée clé : apprendre un modèle génératif, c'est apprendre une densité $p_\theta(x)$ qui explique les données.

## Objectifs

À la fin de la semaine, vous saurez :

1. Expliquer la différence **probabilité vs vraisemblance**.
2. Écrire une vraisemblance $L(\theta)$ et une log-vraisemblance $\ell(\theta)$.
3. Comprendre pourquoi on minimise la **NLL** en apprentissage automatique.
4. Dériver un MLE sur un cas simple (Bernoulli).
5. Expliquer la **malédiction de la dimension**.
6. Factoriser une densité jointe $p(x)$ via la **règle de la chaîne** et comprendre l'idée auto-régressive.

## Support de la semaine

Téléchargez le support complet de la semaine (notes de cours, figures, encadrés et synthèse) :

{{< telecharger href="pdf/semaine-03.pdf" label="Télécharger le support de la semaine 3 (PDF)" >}}

### Plan du support

- Fil conducteur : de S1/S2 à S3
- Probabilité vs densité (discret vs continu)
- Objectif global : apprendre une densité
- Probabilité vs vraisemblance : la confusion la plus fréquente
- MLE : définition et intuition
- Approfondissement : interprétation via KL
- Exemple pratique : MLE d’une Bernoulli
- Malédiction de la dimension : pourquoi $p(x)$ est difficile
- Factorisation de $p(x)$ : rendre l’apprentissage faisable
- Synthèse de la semaine 3 et transition vers S4

## Activités de la semaine

| Étape | Activité |
|:--|:--|
| 1 | Regarder la vidéo d'introduction |
| 2 | Lire le [support PDF]({{< relurl "pdf/semaine-03.pdf" >}}) |
| 3 | Faire le [laboratoire]({{< ref "laboratoire" >}}) |
| 4 | Répondre au [quiz]({{< ref "quiz" >}}) |

