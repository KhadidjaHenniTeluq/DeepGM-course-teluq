---
title: 'Semaine 13 : Modèles hiérarchiques'
weight: 130
bookCollapseSection: true
---

# Semaine 13 : Modèles hiérarchiques

*Latents multi-niveaux · génération multi-échelle · StyleGAN · diffusion hiérarchique*

## Vidéo d'introduction

{{< video src="videos/semaine-13.mp4" poster="videos/semaine-13.jpg" >}}

> [!IMPORTANT]
> **Question centrale de la semaine**
>
> Comment représenter et générer une donnée complexe en organisant ses facteurs latents à plusieurs niveaux et plusieurs échelles ?

## Mise en contexte

Un modèle de diffusion construit une donnée progressivement, du bruit à une structure cohérente. La S13 pose une question plus profonde : les données possèdent-elles **plusieurs niveaux d'organisation** ? Si oui, un bon modèle génératif doit les représenter et les produire du global vers le local.

## Objectifs

À la fin de la semaine, vous saurez :

1. Expliquer le rôle de **latents multi-niveaux** dans une représentation hiérarchique.
2. Comprendre la génération **multi-échelle**, du global vers le local.
3. Définir le **Random Hierarchy Model** (RHM).
4. Comprendre comment les expériences forward–backward révèlent une transition d'échelle.
5. Relier ces idées à **StyleGAN** et aux **Latent Diffusion Models**.

## Support de la semaine

Téléchargez le support complet de la semaine (notes de cours, figures, encadrés et synthèse) :

{{< telecharger href="pdf/semaine-13.pdf" label="Télécharger le support de la semaine 13 (PDF)" >}}

### Plan du support

- Pourquoi des modèles hiérarchiques ?
- Latents multi-niveaux : le Random Hierarchy Model
- Diffusion sur une hiérarchie et transition de phase
- Signature expérimentale : changements corrélés et susceptibilité
- Validation sur texte et images
- StyleGAN : génération explicite du grossier vers le fin
- Diffusion latente : aperçu multi-échelle
- Synthèse de la semaine 13 et transition vers S14

## Activités de la semaine

| Étape | Activité |
|:--|:--|
| 1 | Regarder la vidéo d'introduction |
| 2 | Lire le [support PDF]({{< relurl "pdf/semaine-13.pdf" >}}) |
| 3 | Faire le [laboratoire]({{< ref "laboratoire" >}}) |
| 4 | Répondre au [quiz]({{< ref "quiz" >}}) |

