---
title: Laboratoire
weight: 1
---

# Laboratoire : semaine 15

*Projet & synthèse*

> [!TIP]
> Cherchez chaque exercice **avant** d'ouvrir la solution. L'objectif est de relier les équations, les architectures et les choix de modélisation vus dans le support de la semaine.

## Exercice 1 — Choisir une famille selon le besoin

Associez un modèle à chaque contrainte principale et justifiez :\
(a) vraisemblance exacte indispensable ;\
(b) contrôle conditionnel simple dans un latent ;\
(c) parmi les familles classiques étudiées, on privilégie un échantillonnage en un seul passage avec bonne qualité visuelle ;\
(d) génération progressive robuste avec bon contrôle ;\
(e) énergie relative sans densité normalisée tractable.

{{% details title="Voir la solution" open=false %}}
\(a\) Normalizing Flow ou modèle auto-régressif selon la structure.\
(b) CVAE.\
(c) GAN : c’est un choix naturel lorsque l’on privilégie un échantillonnage en un seul passage et une bonne qualité visuelle, sans en faire une propriété universelle.\
(d) Diffusion / DDPM-LDM.\
(e) EBM.\
Il n’existe pas de famille universellement meilleure : le choix dépend de la métrique, du coût, de la tractabilité et du type de contrôle souhaité.
{{% /details %}}

## Exercice 2 — Comparer deux modèles sur un même dataset

Vous comparez VAE et GAN sur Fashion-MNIST. Proposez au moins quatre mesures/observations permettant une comparaison plus juste qu’une simple grille de 16 images.

{{% details title="Voir la solution" open=false %}}
Exemples :
1. qualité visuelle sur un ensemble large ;
2. diversité / couverture des classes ;
3. precision/recall ou density/coverage en espace de features ;
4. temps d’entraînement et temps d’échantillonnage ;
5. stabilité entre plusieurs seeds ;
6. nearest-neighbors pour vérifier la mémorisation ;
7. reconstruction ou ELBO pour le VAE, en précisant que ce n’est pas comparable à une vraisemblance GAN inexistante.
La comparaison doit utiliser des critères adaptés à chaque famille et distinguer métriques communes et spécifiques.
{{% /details %}}

## Exercice 3 — Diagnostiquer un échec

Un DDPM ne converge pas : la loss reste élevée et les échantillons ressemblent au bruit.\
Donnez une procédure de diagnostic en cinq étapes.

{{% details title="Voir la solution" open=false %}}
1\. Vérifier le forward process `q_sample` sur quelques images et plusieurs $t$.
2. Vérifier que la cible $\epsilon$ correspond exactement au bruit utilisé.
3. Sur-apprendre volontairement un très petit sous-ensemble pour valider le pipeline.
4. Inspecter le schedule, la normalisation des données, les gradients et le learning rate.
5. Réduire le modèle et $T$ pour obtenir une version minimale fonctionnelle avant de remonter en complexité.
Un échec documenté et analysé reste scientifiquement utile.
{{% /details %}}

## Exercice 4 — Construire une carte des liens entre familles

Complétez la chaîne suivante avec une phrase de liaison pour chaque flèche :\
EBM $\to$ Score $\to$ Diffusion\
AE/VAE $\to$ LDM\
Diffusion $\to$ Flow Matching.

{{% details title="Voir la solution" open=false %}}
EBM $\to$ Score : $\nabla_x \log p_\theta(x) = -\nabla_x E_\theta(x)$, donc la constante de partition disparaît.\
Score $\to$ Diffusion : les modèles de diffusion apprennent des champs de débruitage/score à plusieurs niveaux de bruit.\
AE/VAE $\to$ LDM : l’autoencodeur fournit un espace latent comprimé dans lequel la diffusion est entraînée.\
Diffusion $\to$ Flow Matching : les deux décrivent un transport entre bruit et données ; Flow Matching apprend directement un champ de vitesse d’ODE, tandis que la diffusion est souvent introduite par une dynamique stochastique/score.
{{% /details %}}

## Exercice 5 — Concevoir un protocole final reproductible

Proposez un protocole de projet final comparant deux familles sur Fashion-MNIST en limitant les ressources.

{{% details title="Voir la solution" open=false %}}
Exemple :
- même split train/test ;
- même prétraitement et résolution ;
- même budget d’époques ou budget de calcul approximatif ;
- 3 seeds si possible ;
- 10 000 échantillons générés pour les métriques ;
- une métrique commune de qualité/diversité + mesures propres à chaque modèle ;
- temps d’entraînement et d’échantillonnage ;
- grille d’exemples + cas d’échec ;
- code versionné, seed fixé, hyperparamètres documentés.
L’objectif est de comparer proprement, pas de maximiser la taille des architectures.
{{% /details %}}

---

Une fois le laboratoire terminé, testez-vous avec le [quiz de la semaine]({{< ref "quiz" >}}).
