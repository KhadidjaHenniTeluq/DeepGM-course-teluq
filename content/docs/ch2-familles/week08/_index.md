---
title: 'Semaine 8 : Flots normalisants'
weight: 80
bookCollapseSection: true
---

# Semaine 8 : Flots normalisants

*Changement de variables · Jacobien · RealNVP · Glow*

## Vidéo d'introduction

{{< video src="videos/semaine-08.mp4" poster="videos/semaine-08.jpg" >}}

> [!IMPORTANT]
> **Question centrale de la semaine**
>
> Comment transformer une distribution simple en une distribution complexe tout en conservant une vraisemblance exacte ?

## Mise en contexte

Le VAE optimise une borne (la ELBO). Cette semaine, nous cherchons une autre voie : une transformation **inversible** entre latent et données, qui permet de calculer **exactement** la densité. Le fil logique : changement de variables → Jacobien → transformations inversibles → RealNVP → Glow.

## Objectifs

À la fin de la semaine, vous saurez :

1. Expliquer ce qu'est un flot normalisant et pourquoi il donne une vraisemblance exacte.
2. Appliquer la formule du **changement de variables** pour calculer $p_X(x)$.
3. Comprendre le rôle du **Jacobien** et de son déterminant.
4. Décrire les architectures **RealNVP** et **Glow**.
5. Lire et relier à la théorie un fragment PyTorch de couche de couplage.
6. Expliquer l'entraînement par maximum de vraisemblance et la génération d'échantillons.

## Support de la semaine

Téléchargez le support complet de la semaine (notes de cours, figures, encadrés et synthèse) :

{{< telecharger href="pdf/semaine-08.pdf" label="Télécharger le support de la semaine 8 (PDF)" >}}

### Plan du support

- Fil conducteur : de S7 à S8
- Pourquoi les flots normalisants ?
- La formule du changement de variables
- Composition de transformations : le flot
- Le défi pratique : calcul efficace du Jacobien
- RealNVP : couches de couplage
- Architecture complète de RealNVP
- Glow : améliorations de RealNVP
- Du concept au code : couche de couplage RealNVP
- Avantages et limites des flots normalisants
- Synthèse de la semaine 8 et transition vers S9

## Activités de la semaine

| Étape | Activité |
|:--|:--|
| 1 | Regarder la vidéo d'introduction |
| 2 | Lire le [support PDF]({{< relurl "pdf/semaine-08.pdf" >}}) |
| 3 | Faire le [laboratoire]({{< ref "laboratoire" >}}) |
| 4 | Répondre au [quiz]({{< ref "quiz" >}}) |
| 5 | Réaliser l'[évaluation 4]({{< ref "/docs/ch2-familles/evaluation-4" >}}) (mini-projet S7–S8) |

