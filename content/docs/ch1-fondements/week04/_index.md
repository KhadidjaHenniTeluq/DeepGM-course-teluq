---
title: 'Semaine 4 : Variables latentes & inférence'
weight: 40
bookCollapseSection: true
---

# Semaine 4 : Variables latentes & inférence

*Latents · Posterior · Inférence exacte / approximée · VI*

## Vidéo d'introduction

{{< video src="videos/semaine-04.mp4" poster="videos/semaine-04.jpg" >}}

> [!IMPORTANT]
> **Question centrale de la semaine**
>
> Comment inférer une variable latente $z$ non observée à partir d'une observation $x$ ?

## Mise en contexte

En S3, $p_\theta(x)$ était calculable et on maximisait $\sum \log p_\theta(x)$. Mais si les données dépendaient de facteurs qu'on n'observe pas — le style d'écriture d'un chiffre, la pose ou l'éclairage d'un visage, le sujet d'un document ? Ces facteurs expliquent la variabilité : comment les modéliser ?

## Objectifs

À la fin de la semaine, vous saurez :

1. Comprendre pourquoi on a besoin de **variables latentes** $z$ pour modéliser des données complexes.
2. Formuler le problème d'inférence : $p(z \mid x) = p(x \mid z)\,p(z) / p(x)$.
3. Distinguer inférence **exacte** (rare) et inférence **approximée** (générale).
4. Expliquer l'idée de l'**inférence variationnelle** : approximer $p(z \mid x)$ par $q_\phi(z \mid x)$.
5. Placer les modèles latents dans la taxonomie du cours (VAE, HMM, etc.).

## Support de la semaine

Téléchargez le support complet de la semaine (notes de cours, figures, encadrés et synthèse) :

{{< telecharger href="pdf/semaine-04.pdf" label="Télécharger le support de la semaine 4 (PDF)" >}}

### Plan du support

- Fil conducteur : transition S3 $\rightarrow$ S4
- Partie 1 : Pourquoi des variables latentes ?
- Partie 2 : Le problème d’inférence
- Partie 3 : Inférence approximée — Introduction à l’inférence variationnelle
- Partie 4 : Synthèse et taxonomie
- Synthèse de la semaine 4 et transition vers S5

## Activités de la semaine

| Étape | Activité |
|:--|:--|
| 1 | Regarder la vidéo d'introduction |
| 2 | Lire le [support PDF]({{< relurl "pdf/semaine-04.pdf" >}}) |
| 3 | Faire le [laboratoire]({{< ref "laboratoire" >}}) |
| 4 | Répondre au [quiz]({{< ref "quiz" >}}) |
| 5 | Réaliser l'[évaluation 2]({{< ref "/docs/ch1-fondements/evaluation-2" >}}) (mini-projet S3–S4) |

