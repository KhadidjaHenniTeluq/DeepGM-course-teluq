---
title: 'Semaine 9 : Modèles fondés sur l''énergie (EBM)'
weight: 90
bookCollapseSection: true
---

# Semaine 9 : Modèles fondés sur l'énergie (EBM)

*Énergie · Fonction de partition · Échantillonnage · Divergence contrastive · RBM*

## Vidéo d'introduction

{{< video src="videos/semaine-09.mp4" poster="videos/semaine-09.jpg" >}}

> [!IMPORTANT]
> **Question centrale de la semaine**
>
> Comment apprendre une distribution complexe à partir d'une fonction d'énergie lorsque sa normalisation est difficile à calculer ?

## Mise en contexte

Les flots conservaient une vraisemblance exacte grâce à l'inversibilité. Les EBM adoptent une stratégie différente : apprendre une **fonction d'énergie** qui indique quelles configurations sont plausibles. Fil logique : énergie → normalisation → $Z(\theta)$ → gradient → échantillonnage → CD → RBM.

## Objectifs

À la fin de la semaine, vous saurez :

1. Interpréter une fonction d'énergie $E_\theta(x)$.
2. Définir la **fonction de partition** $Z(\theta)$ et comprendre pourquoi elle rend la normalisation difficile.
3. Lire le gradient de la log-vraisemblance et distinguer **phase positive** et **phase négative**.
4. Comprendre le rôle du MCMC (Langevin, Gibbs) dans l'apprentissage.
5. Expliquer la **divergence contrastive** et le rôle historique des **RBM**.
6. Comprendre le lien conceptuel entre EBM et GAN.

## Support de la semaine

Téléchargez le support complet de la semaine (notes de cours, figures, encadrés et synthèse) :

{{< telecharger href="pdf/semaine-09.pdf" label="Télécharger le support de la semaine 9 (PDF)" >}}

### Plan du support

- Fil conducteur : de S8 à S9
- L’idée centrale d’un modèle fondé sur l’énergie
- De l’énergie à une distribution de probabilité
- Apprentissage par maximum de vraisemblance
- Échantillonnage par dynamique de Langevin
- Divergence contrastive
- Machine de Boltzmann restreinte (RBM)
- Produit d’experts : complément optionnel
- Lien avec les GAN : seulement l’idée nécessaire
- Avantages et limites
- Synthèse de la semaine 9 et transition vers S10

## Activités de la semaine

| Étape | Activité |
|:--|:--|
| 1 | Regarder la vidéo d'introduction |
| 2 | Lire le [support PDF]({{< relurl "pdf/semaine-09.pdf" >}}) |
| 3 | Faire le [laboratoire]({{< ref "laboratoire" >}}) |
| 4 | Répondre au [quiz]({{< ref "quiz" >}}) |

