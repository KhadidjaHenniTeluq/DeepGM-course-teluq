---
title: 'Semaine 5 : Modèles auto-régressifs'
weight: 50
bookCollapseSection: true
---

# Semaine 5 : Modèles auto-régressifs

*Règle de la chaîne · NADE / MADE · PixelRNN / PixelCNN*

## Vidéo d'introduction

{{< video src="videos/semaine-05.mp4" poster="videos/semaine-05.jpg" >}}

> [!IMPORTANT]
> **Question centrale de la semaine**
>
> Comment décomposer et modéliser une distribution complexe $p(x)$ composante par composante ?

## Mise en contexte

En S3, nous avons introduit la factorisation $p_\theta(x) = \prod_i p_\theta(x_i \mid x_{<i})$. Cette semaine, nous transformons cette identité en une véritable famille de modèles : prédire chaque composante à partir de celles qui la précèdent, puis répéter jusqu'à obtenir une observation complète.

## Objectifs

À la fin de la semaine, vous saurez :

1. Lire et expliquer la factorisation auto-régressive de $p_\theta(x)$.
2. Comprendre pourquoi un **ordre** des variables est nécessaire.
3. Expliquer comment **FVSBN, NADE et MADE** paramètrent les conditionnelles.
4. Comprendre le principe de **PixelRNN** et **PixelCNN**.
5. Distinguer entraînement parallélisable et génération séquentielle.
6. Expliquer pourquoi la vraisemblance est exacte, mais la génération peut être lente.

## Support de la semaine

Téléchargez le support complet de la semaine (notes de cours, figures, encadrés et synthèse) :

{{< telecharger href="pdf/semaine-05.pdf" label="Télécharger le support de la semaine 5 (PDF)" >}}

### Plan du support

- Règle de la chaîne : cœur des modèles auto-régressifs
- Paramétrer une conditionnelle
- Apprentissage par MLE / NLL
- Repères historiques : FVSBN, NADE et MADE
- PixelRNN : appliquer l’auto-régressif aux images
- PixelCNN : convolutions masquées
- Comparer les principales familles auto-régressives
- Synthèse de la semaine 5

## Activités de la semaine

| Étape | Activité |
|:--|:--|
| 1 | Regarder la vidéo d'introduction |
| 2 | Lire le [support PDF]({{< relurl "pdf/semaine-05.pdf" >}}) |
| 3 | Faire le [laboratoire]({{< ref "laboratoire" >}}) |
| 4 | Répondre au [quiz]({{< ref "quiz" >}}) |

