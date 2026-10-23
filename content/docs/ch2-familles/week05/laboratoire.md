---
title: Laboratoire
weight: 1
---

# Laboratoire : semaine 5

*Modèles auto-régressifs*

> [!TIP]
> Cherchez chaque exercice **avant** d'ouvrir la solution. L'objectif est de relier les équations, les architectures et les choix de modélisation vus dans le support de la semaine.

## Exercice 1 — Ordre auto-régressif

Une image binaire $2 \times 2$ contient les pixels $(x_1, x_2, x_3, x_4)$. Comparez deux ordres possibles : raster $x_1 \to x_2 \to x_3 \to x_4$ et un autre ordre $x_1 \to x_3 \to x_2 \to x_4$.\
La densité jointe change-t-elle mathématiquement ? Le modèle appris peut-il changer en pratique ?

{{% details title="Voir la solution" open=false %}}
La loi jointe admet une factorisation exacte pour n’importe quel ordre :\
$p(x) = \prod_i p(x_i \mid x_{<i})$.\
Mathématiquement, la même distribution peut être représentée avec différents ordres si les conditionnelles sont parfaitement modélisées.\
En pratique, l’architecture, la capacité et la difficulté des conditionnelles dépendent de l’ordre ; les performances peuvent donc changer.
{{% /details %}}

## Exercice 2 — Entraînement vs génération

Expliquez pourquoi un PixelCNN peut entraîner les prédictions de nombreux pixels en parallèle mais générer une image de manière séquentielle.

{{% details title="Voir la solution" open=false %}}
Pendant l’entraînement, l’image complète $x$ est connue ; des masques empêchent chaque prédiction de regarder le futur, ce qui permet de calculer plusieurs conditionnelles dans un même passage.\
Pendant la génération, les pixels futurs n’existent pas encore : il faut échantillonner $x_1$, puis utiliser $x_1$ pour $x_2$, etc. La génération reste donc séquentielle.
{{% /details %}}

---

Une fois le laboratoire terminé, testez-vous avec le [quiz de la semaine]({{< ref "quiz" >}}).
