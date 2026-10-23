---
title: 'Semaine 11 : Score Matching'
weight: 110
bookCollapseSection: true
---

# Semaine 11 : Score Matching

*Score de Hyvärinen · Denoising score matching · Langevin*

## Vidéo d'introduction

{{< video src="videos/semaine-11.mp4" poster="videos/semaine-11.jpg" >}}

> [!IMPORTANT]
> **Question centrale de la semaine**
>
> Peut-on apprendre la direction vers les régions de forte probabilité sans connaître ni normaliser explicitement la densité $p(x)$ ?

## Mise en contexte

En S9, la constante de normalisation compliquait l'apprentissage des EBM ; en S10, les modèles implicites évitaient complètement la vraisemblance. En S11, nous suivons une troisième voie : apprendre directement le gradient du log de la densité, appelé **score**.

## Objectifs

À la fin de la semaine, vous saurez :

1. Définir la fonction de score $s(x) = \nabla_x \log p(x)$ et expliquer son intérêt.
2. Comprendre le score matching de **Hyvärinen** et la divergence de Fisher.
3. Comprendre le **denoising score matching** : le lien entre bruit, score et débruitage.
4. Expliquer le principe du **sliced score matching**.
5. Générer avec la **dynamique de Langevin** à partir d'un score appris.
6. Expliquer le lien conceptuel EBM ↔ score ↔ diffusion.

## Support de la semaine

Téléchargez le support complet de la semaine (notes de cours, figures, encadrés et synthèse) :

{{< telecharger href="pdf/semaine-11.pdf" label="Télécharger le support de la semaine 11 (PDF)" >}}

### Plan du support

- Pourquoi représenter une distribution par son score ?
- Score matching classique : Hyvärinen
- Denoising Score Matching (DSM)
- Sliced Score Matching
- Du score à la génération : dynamique de Langevin
- Défis sur les données réelles
- Lien EBM $\leftrightarrow$ score $\leftrightarrow$ diffusion
- Synthèse de la semaine 11 et transition vers S12

## Activités de la semaine

| Étape | Activité |
|:--|:--|
| 1 | Regarder la vidéo d'introduction |
| 2 | Lire le [support PDF]({{< relurl "pdf/semaine-11.pdf" >}}) |
| 3 | Faire le [laboratoire]({{< ref "laboratoire" >}}) |
| 4 | Répondre au [quiz]({{< ref "quiz" >}}) |

