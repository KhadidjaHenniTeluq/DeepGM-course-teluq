---
title: Laboratoire
weight: 1
---

# Laboratoire : semaine 13

*Modèles hiérarchiques*

> [!TIP]
> Cherchez chaque exercice **avant** d'ouvrir la solution. L'objectif est de relier les équations, les architectures et les choix de modélisation vus dans le support de la semaine.

## Exercice 1 — Taille d’un RHM

Un Random Hierarchy Model a un facteur de branchement $s = 2$ et une profondeur $L = 6$.
1. Combien de feuilles visibles contient-il ?
2. Combien de feuilles un latent situé 3 niveaux au-dessus des feuilles peut-il influencer directement dans cette hiérarchie idéale ?

{{% details title="Voir la solution" open=false %}}
1\. $d = s^L = 2^6 = 64$ feuilles.
2. Un latent situé 3 niveaux au-dessus des feuilles contrôle un bloc de taille $s^3 = 8$ feuilles.
Cette relation matérialise le passage du local au global.
{{% /details %}}

## Exercice 2 — Lire une transition d’échelle

Lors d’une expérience forward-backward, la susceptibilité $\chi(t)$ présente un pic à $t^* = 0{,}35\,T$.\
Que signifie ce pic conceptuellement ?

{{% details title="Voir la solution" open=false %}}
Le pic indique qu’autour de $t^*$, de nombreuses positions changent de manière corrélée. La taille effective des blocs de changements est maximale : on observe un changement d’échelle entre modifications locales et restructuration plus globale. Ce n’est pas nécessairement une preuve qu’un arbre latent explicite existe dans le modèle réel.
{{% /details %}}

## Exercice 3 — StyleGAN : global vs local

Expliquez le rôle distinct de l’injection de style et de l’injection de bruit dans le StyleGAN original.

{{% details title="Voir la solution" open=false %}}
Le style dérivé de $w$ module les activations à différentes résolutions et contrôle des facteurs relativement structurés, des propriétés grossières vers les détails selon les couches.\
Le bruit injecté fournit une source de variation stochastique locale, utile pour des détails aléatoires qui n’ont pas besoin d’être codés dans $w$.\
Les deux mécanismes séparent donc contrôle structuré et stochasticité locale.
{{% /details %}}

---

Une fois le laboratoire terminé, testez-vous avec le [quiz de la semaine]({{< ref "quiz" >}}).
