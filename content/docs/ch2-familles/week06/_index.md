---
title: 'Semaine 6 : Autoencodeurs profonds'
weight: 60
bookCollapseSection: true
---

# Semaine 6 : Autoencodeurs profonds

*Encodeur · Latent · Reconstruction · Manifold*

## Vidéo d'introduction

{{< video src="videos/semaine-06.mp4" poster="videos/semaine-06.jpg" >}}

> [!IMPORTANT]
> **Question centrale de la semaine**
>
> Comment apprendre une représentation compacte $z$ qui conserve l'information essentielle de $x$ ?

## Mise en contexte

En S5, nous modélisions directement $p_\theta(x)$ composante par composante : vraisemblance exacte, mais génération séquentielle. Cette semaine, nous changeons de stratégie : apprendre une **représentation compacte** $z$ de l'observation, puis reconstruire $x$ à partir de cette représentation.

## Objectifs

À la fin de la semaine, vous saurez :

1. Comprendre l'architecture **encodeur / décodeur** d'un autoencodeur.
2. Expliquer le rôle de la compression et du **goulot d'étranglement**.
3. Comprendre intuitivement la notion de **variété** (manifold) des données.
4. Expliquer la différence entre reconstruction et génération.
5. Identifier les **limites génératives** d'un autoencodeur classique et pourquoi elles motivent les VAE (S7).

## Support de la semaine

Téléchargez le support complet de la semaine (notes de cours, figures, encadrés et synthèse) :

{{< telecharger href="pdf/semaine-06.pdf" label="Télécharger le support de la semaine 6 (PDF)" >}}

### Plan du support

- Fil conducteur : de S5 à S6
- Introduction : apprentissage non supervisé
- Architecture générale d’un autoencodeur
- Compression et goulot d’étranglement
- Manifold learning : intuition géométrique
- Autoencodeurs profonds
- Limites génératives des autoencodeurs classiques
- Vers les autoencodeurs variationnels (VAE)
- Synthèse de la semaine 6 et transition vers S7

## Activités de la semaine

| Étape | Activité |
|:--|:--|
| 1 | Regarder la vidéo d'introduction |
| 2 | Lire le [support PDF]({{< relurl "pdf/semaine-06.pdf" >}}) |
| 3 | Faire le [laboratoire]({{< ref "laboratoire" >}}) |
| 4 | Répondre au [quiz]({{< ref "quiz" >}}) |
| 5 | Réaliser l'[évaluation 3]({{< ref "/docs/ch2-familles/evaluation-3" >}}) (mini-projet S5–S6) |

