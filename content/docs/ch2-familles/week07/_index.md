---
title: 'Semaine 7 : Autoencodeurs variationnels (VAE)'
weight: 70
bookCollapseSection: true
---

# Semaine 7 : Autoencodeurs variationnels (VAE)

*ELBO · KL · Reparametrization · β-VAE · CVAE*

## Vidéo d'introduction

{{< video src="videos/semaine-07.mp4" poster="videos/semaine-07.jpg" >}}

> [!IMPORTANT]
> **Question centrale de la semaine**
>
> Comment structurer l'espace latent pour pouvoir générer de nouvelles données de manière cohérente ?

## Mise en contexte

Un autoencodeur classique reconstruit bien, mais rien ne garantit que son espace latent soit assez régulier pour y échantillonner de nouveaux points. Cette semaine, nous ajoutons une **structure probabiliste** au latent afin de rendre la génération possible.

## Objectifs

À la fin de la semaine, vous saurez :

1. Expliquer pourquoi l'autoencodeur classique ne suffit pas pour générer.
2. Définir le modèle latent probabiliste d'un VAE : $p(z)$, $p_\theta(x \mid z)$ et $p_\theta(x)$.
3. Suivre la dérivation de la **ELBO** et interpréter ses deux termes.
4. Comprendre le rôle de la **divergence KL** et du **reparameterization trick**.
5. Distinguer VAE standard, **β-VAE** et **CVAE**.
6. Comprendre la génération, l'interpolation et la génération contrôlée avec un VAE.

## Support de la semaine

Téléchargez le support complet de la semaine (notes de cours, figures, encadrés et synthèse) :

{{< telecharger href="pdf/semaine-07.pdf" label="Télécharger le support de la semaine 7 (PDF)" >}}

### Plan du support

- Fil conducteur : de S6 à S7
- Pourquoi l’autoencodeur classique ne suffit pas
- Le modèle génératif d’un VAE
- Le problème d’inférence
- Approximer le posterior : inférence variationnelle
- Dérivation pas à pas de la ELBO
- Cas gaussien : formule pratique de la KL
- Le reparameterization trick
- Architecture complète d’un VAE
- Fonction de perte et entraînement
- Génération et interpolation avec un VAE
- Variante 1 : le $\beta$-VAE
- Variante 2 : le CVAE
- Comparaison synthétique des modèles
- Synthèse de la semaine 7 et transition vers S8

## Activités de la semaine

| Étape | Activité |
|:--|:--|
| 1 | Regarder la vidéo d'introduction |
| 2 | Lire le [support PDF]({{< relurl "pdf/semaine-07.pdf" >}}) |
| 3 | Faire le [laboratoire]({{< ref "laboratoire" >}}) |
| 4 | Répondre au [quiz]({{< ref "quiz" >}}) |

