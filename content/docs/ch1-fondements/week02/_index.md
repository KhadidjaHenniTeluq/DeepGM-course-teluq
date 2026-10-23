---
title: 'Semaine 2 : Discriminatif vs Génératif'
weight: 20
bookCollapseSection: true
---

# Semaine 2 : Discriminatif vs Génératif

*p(y|x) · p(x) · Explicite · Implicite*

## Vidéo d'introduction

{{< video src="videos/semaine-02.mp4" poster="videos/semaine-02.jpg" >}}

> [!IMPORTANT]
> **Question centrale de la semaine**
>
> Quelle distribution veut-on modéliser : $p(y \mid x)$, $p(x)$ ou $p(x, y)$ ?

## Mise en contexte

En S1, nous avons étudié comment un réseau construit une représentation interne des données. Cette semaine, nous changeons de point de vue : nous demandons **quelle distribution** le modèle cherche à apprendre. Décrire le monde (la distribution des données) ou simplement décider (la classe à prédire) ?

## Objectifs

À la fin de la semaine, vous saurez :

1. Lire une formule et dire : **discriminatif** ou **génératif**.
2. Comprendre ce que signifie modéliser une distribution (densité + vraisemblance + échantillonnage).
3. Distinguer génération **explicite** et **implicite**.
4. Placer AR, VAE, Flows, GAN et Diffusion dans une **taxonomie globale**.
5. Comprendre pourquoi on a besoin de S3–S4 (MLE, latents, inférence).

## Support de la semaine

Téléchargez le support complet de la semaine (notes de cours, figures, encadrés et synthèse) :

{{< telecharger href="pdf/semaine-02.pdf" label="Télécharger le support de la semaine 2 (PDF)" >}}

### Plan du support

- Du latent à la probabilité
- Partie A : Discriminatif vs Génératif
- Interlude essentiel : modéliser une distribution
- Partie B : Génération explicite vs implicite
- Partie C : Taxonomie globale des DGMs (vue d’ensemble)
- Synthèse de la semaine 2

## Activités de la semaine

| Étape | Activité |
|:--|:--|
| 1 | Regarder la vidéo d'introduction |
| 2 | Lire le [support PDF]({{< relurl "pdf/semaine-02.pdf" >}}) |
| 3 | Faire le [laboratoire]({{< ref "laboratoire" >}}) |
| 4 | Répondre au [quiz]({{< ref "quiz" >}}) |
| 5 | Réaliser l'[évaluation 1]({{< ref "/docs/ch1-fondements/evaluation-1" >}}) (mini-projet S1–S2) |

