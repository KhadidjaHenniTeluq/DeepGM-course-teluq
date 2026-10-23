---
title: Laboratoire
weight: 1
---

# Laboratoire : semaine 8

*Flots normalisants*

> [!TIP]
> Cherchez chaque exercice **avant** d'ouvrir la solution. L'objectif est de relier les équations, les architectures et les choix de modélisation vus dans le support de la semaine.

## Exercice 1 — Changement de variables

Soit $z \sim \mathcal{N}(0, 1)$ et $x = f(z) = 2z + 3$.
1. Donnez $f^{-1}(x)$.
2. Donnez $|dz/dx|$.
3. Écrivez $p_X(x)$ en fonction de $p_Z$.

{{% details title="Voir la solution" open=false %}}
$f^{-1}(x) = (x-3)/2$.\
$dz/dx = 1/2$, donc $|dz/dx| = 1/2$.\
Ainsi :\
$p_X(x) = p_Z((x-3)/2) \cdot 1/2$.\
Le terme jacobien corrige la déformation de volume induite par la transformation.
{{% /details %}}

## Exercice 2 — VAE ou Flow ?

Pour chaque besoin, choisissez VAE ou Flow et justifiez :\
(a) on veut une vraisemblance exacte ;\
(b) on veut une inférence amortie $z \mid x$ naturelle ;\
(c) on accepte une borne ELBO ;\
(d) on veut une transformation bijective entre $x$ et $z$.

{{% details title="Voir la solution" open=false %}}
\(a\) Flow.\
(b) VAE.\
(c) VAE.\
(d) Flow.\
Le VAE privilégie une modélisation latente probabiliste avec inférence approchée ; le flow privilégie l’inversibilité et une densité exacte via changement de variables.
{{% /details %}}

---

Une fois le laboratoire terminé, testez-vous avec le [quiz de la semaine]({{< ref "quiz" >}}).
