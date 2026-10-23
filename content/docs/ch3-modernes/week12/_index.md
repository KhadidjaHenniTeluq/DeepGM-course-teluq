---
title: 'Semaine 12 : Modèles de diffusion'
weight: 120
bookCollapseSection: true
---

# Semaine 12 : Modèles de diffusion

*Processus direct/inverse · DDPM · génération progressive · multi-modalité*

## Vidéo d'introduction

{{< video src="videos/semaine-12.mp4" poster="videos/semaine-12.jpg" >}}

> [!IMPORTANT]
> **Question centrale de la semaine**
>
> Comment apprendre à transformer progressivement du bruit aléatoire en une donnée réaliste ?

## Mise en contexte

En S11, le score permettait de guider un échantillonnage de Langevin, mais il est mal estimé dans les régions de faible densité. La diffusion répond à cette difficulté en introduisant **plusieurs niveaux de bruit** : on apprend progressivement à revenir du bruit vers les données.

## Objectifs

À la fin de la semaine, vous saurez :

1. Expliquer le **processus direct** qui transforme les données en bruit et le **processus inverse** appris.
2. Comprendre les équations du **DDPM** et pourquoi l'entraînement revient à prédire le bruit.
3. Expliquer la génération progressive et pourquoi elle est plus lente qu'un GAN ou un flow.
4. Situer **DDIM** et les stratégies d'accélération ; comprendre le rôle du schedule $\beta_t$.
5. Expliquer la **classifier-free guidance** et situer la **diffusion latente**.

## Support de la semaine

Téléchargez le support complet de la semaine (notes de cours, figures, encadrés et synthèse) :

{{< telecharger href="pdf/semaine-12.pdf" label="Télécharger le support de la semaine 12 (PDF)" >}}

### Plan du support

- Introduction : pourquoi les modèles de diffusion ?
- Processus direct : transformer les données en bruit
- Processus inverse : apprendre à débruiter
- DDPM : Denoising Diffusion Probabilistic Models
- Génération progressive
- Accélération : DDIM et autres stratégies
- Généralisation multi-modalité
- Comparaison et perspectives
- Synthèse de la semaine 12 et transition vers S13

## Activités de la semaine

| Étape | Activité |
|:--|:--|
| 1 | Regarder la vidéo d'introduction |
| 2 | Lire le [support PDF]({{< relurl "pdf/semaine-12.pdf" >}}) |
| 3 | Faire le [laboratoire]({{< ref "laboratoire" >}}) |
| 4 | Répondre au [quiz]({{< ref "quiz" >}}) |
| 5 | Réaliser l'[évaluation 6]({{< ref "/docs/ch3-modernes/evaluation-6" >}}) (mini-projet S11–S12) |

