---
title: 'Semaine 10 : Modèles génératifs implicites'
weight: 100
bookCollapseSection: true
---

# Semaine 10 : Modèles génératifs implicites

*GAN · MMD-GAN · absence de vraisemblance · évaluation*

## Vidéo d'introduction

{{< video src="videos/semaine-10.mp4" poster="videos/semaine-10.jpg" >}}

> [!IMPORTANT]
> **Question centrale de la semaine**
>
> Peut-on apprendre à générer des données réalistes sans jamais calculer explicitement leur vraisemblance $p_\theta(x)$ ?

## Mise en contexte

Un EBM associe une énergie aux données, mais sa normalisation et son échantillonnage sont coûteux. En S10, nous changeons de perspective : au lieu d'exiger une densité explicite, nous apprenons directement une **procédure de génération** et nous comparons les échantillons produits aux données réelles.

## Objectifs

À la fin de la semaine, vous saurez :

1. Expliquer ce qu'est un modèle génératif **implicite**.
2. Comprendre les **tests à deux échantillons** comme alternative à la comparaison de densités.
3. Décrire le jeu antagoniste **GAN** et son objectif minimax, et le relier à la divergence de Jensen–Shannon.
4. Expliquer l'instabilité et le **mode collapse**.
5. Comprendre le principe du **MMD** et du MMD-GAN.
6. Choisir des métriques adaptées : IS, FID, KID, précision/rappel, densité/couverture.

## Support de la semaine

Téléchargez le support complet de la semaine (notes de cours, figures, encadrés et synthèse) :

{{< telecharger href="pdf/semaine-10.pdf" label="Télécharger le support de la semaine 10 (PDF)" >}}

### Plan du support

- Introduction aux modèles génératifs implicites
- Tests à deux échantillons : fondement théorique
- Réseaux antagonistes génératifs (GAN)
- MMD-GAN : une alternative basée sur les noyaux
- Absence de vraisemblance dans les modèles implicites
- Évaluation des modèles génératifs implicites
- Résumé et perspectives
- Synthèse de la semaine 10 et transition vers S11

## Activités de la semaine

| Étape | Activité |
|:--|:--|
| 1 | Regarder la vidéo d'introduction |
| 2 | Lire le [support PDF]({{< relurl "pdf/semaine-10.pdf" >}}) |
| 3 | Faire le [laboratoire]({{< ref "laboratoire" >}}) |
| 4 | Répondre au [quiz]({{< ref "quiz" >}}) |
| 5 | Réaliser l'[évaluation 5]({{< ref "/docs/ch2-familles/evaluation-5" >}}) (mini-projet S9–S10) |

