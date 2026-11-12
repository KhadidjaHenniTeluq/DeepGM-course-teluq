---
title: 'Semaine 14 : Hybridation et modèles modernes'
weight: 140
bookCollapseSection: true
---

# Semaine 14 : Hybridation et modèles modernes

*VAE et diffusion · flots et diffusion · lois d'échelle · modèles de fondation*

## Vidéo d'introduction

{{< video src="videos/semaine-14.mp4" poster="videos/semaine-14.jpg" >}}

> [!IMPORTANT]
> **Question centrale de la semaine**
>
> Comment combiner les forces de plusieurs modèles génératifs et les faire évoluer vers des systèmes modernes à grande échelle ?

## Mise en contexte

Les systèmes modernes ne reposent plus sur une seule famille de modèles. Ils combinent représentation latente, diffusion, transport continu et pré-entraînement massif pour obtenir un meilleur compromis entre qualité, coût, stabilité et contrôle.

## Objectifs

À la fin de la semaine, vous saurez :

1. Expliquer pourquoi on cherche à **hybrider** plusieurs familles de modèles génératifs.
2. Décrire un **modèle de diffusion latente** : autoencodeur, diffusion latente, conditionnement et guidage.
3. Définir l'**appariement de flot** : chemin de probabilités, champ de vecteurs, perte de régression, génération par EDO.
4. Interpréter une **loi d'échelle**.
5. Définir un **modèle génératif de fondation** et discuter ses compromis et enjeux éthiques.

## Support de la semaine

Téléchargez le support complet de la semaine (notes de cours, figures, encadrés et synthèse) :

{{< telecharger href="pdf/semaine-14.pdf" label="Télécharger le support de la semaine 14 (PDF)" >}}

### Plan du support

- Pourquoi hybrider les modèles génératifs ?
- VAE + diffusion : modèles de diffusion latente
- Flot + diffusion : appariement de flot
- Lois d’échelle
- Modèles génératifs de fondation
- Enjeux responsables des modèles de fondation
- Synthèse de la semaine 14 et transition vers S15

## Activités de la semaine

| Étape | Activité |
|:--|:--|
| 1 | Regarder la vidéo d'introduction |
| 2 | Lire le [support PDF]({{< relurl "pdf/semaine-14.pdf" >}}) |
| 3 | Faire le [laboratoire]({{< ref "laboratoire" >}}) |
| 4 | Répondre au [quiz]({{< ref "quiz" >}}) |
| 5 | Réaliser l'[évaluation 7]({{< ref "/docs/ch3-modernes/evaluation-7" >}}) (mini-projet S13–S14) |

