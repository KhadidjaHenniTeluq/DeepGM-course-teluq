---
title: 'Semaine 1 : Rappels sur les réseaux de neurones et représentations'
weight: 10
bookCollapseSection: true
---

# Semaine 1 : Rappels sur les réseaux de neurones et représentations

*CNN · RNN · attention et transformeurs*

## Vidéo d'introduction

{{< video src="videos/semaine-01.mp4" poster="videos/semaine-01.jpg" >}}

> [!IMPORTANT]
> **Question centrale de la semaine**
>
> Comment représenter les données de manière utile avec un réseau de neurones ?

## Mise en contexte

Le mot-clé de ce cours, c'est **générer** : pas reconnaître, pas classifier, mais créer du nouveau. Pour générer, il faut d'abord comprendre comment les réseaux **représentent** le monde : comment une image devient un vecteur, comment une phrase devient un point dans un espace. Cette semaine, on révise les réseaux de neurones, les CNN, les RNN et l'attention avec une question précise : *où vit la représentation ?* Et on termine par la cassure : **reconstruire ≠ générer**.

## Objectifs

À la fin de la semaine, vous saurez :

1. Identifier **où se trouve la représentation** dans chaque architecture (CNN, RNN, attention et transformeurs).
2. Expliquer pourquoi un **plongement** est une **géométrie apprise**.
3. Distinguer **reconstruction** et **génération** par le rôle de l'**espace latent**.
4. Distinguer $X$, $x$, $x_i$, $p_{\text{data}}(x)$ et $p_\theta(x)$, et expliquer ce que signifie **échantillonner** une nouvelle donnée.

## Support de la semaine

Téléchargez le support complet de la semaine (notes de cours, figures, encadrés et synthèse) :

{{< telecharger href="pdf/semaine-01.pdf" label="Télécharger le support de la semaine 1 (PDF)" >}}

### Plan du support

- Rappels : données, variables et distributions
- Partie A : Les réseaux construisent des représentations internes
- Transformeurs et Attention : représentations contextuelles
- Partie C : Génération ou Reconstruction
- Complément : échantillonnage et plausibilité
- Synthèse de la semaine 1

## Activités de la semaine

| Étape | Activité |
|:--|:--|
| 1 | Regarder la vidéo d'introduction |
| 2 | Lire le [support PDF]({{< relurl "pdf/semaine-01.pdf" >}}) |
| 3 | Faire le [laboratoire]({{< ref "laboratoire" >}}) |
| 4 | Répondre au [quiz]({{< ref "quiz" >}}) |

