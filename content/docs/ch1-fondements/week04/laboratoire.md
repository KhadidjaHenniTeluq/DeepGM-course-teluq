---
title: Laboratoire
weight: 1
---

# Laboratoire : semaine 4

*Variables latentes & inférence*

> [!TIP]
> Cherchez chaque exercice **avant** d'ouvrir la solution. L'objectif est de relier les équations, les architectures et les choix de modélisation vus dans le support de la semaine.

## Exercice 1 — Posterior latent par Bayes

Un modèle latent définit $p(z)$, $p_\theta(x \mid z)$ et $p_\theta(x) = \int p_\theta(x \mid z) p(z) \, dz$.
1. Écrivez $p_\theta(z \mid x)$.
2. Expliquez pourquoi ce posterior peut être difficile à calculer.

{{% details title="Voir la solution" open=false %}}
Par Bayes :\
$p_\theta(z \mid x) = p_\theta(x \mid z) p(z) / p_\theta(x)$.\
La difficulté vient du dénominateur $p_\theta(x)$, qui contient souvent une intégrale sur tous les $z$ possibles. Cette intégrale peut être intractable pour un modèle profond.
{{% /details %}}

## Exercice 2 — Exact ou approximatif ?

Pour chacun des cas suivants, indiquez si l’inférence exacte est plausible ou si une approximation est généralement nécessaire :\
(a) petit modèle discret avec peu d’états latents ;\
(b) VAE profond avec latent continu de grande dimension ;\
(c) modèle gaussien linéaire simple ;\
(d) réseau profond définissant $p_\theta(x \mid z)$ non linéaire.

{{% details title="Voir la solution" open=false %}}
\(a\) L’inférence exacte peut être plausible par sommation.\
(b) Approximation généralement nécessaire.\
(c) L’inférence exacte est souvent possible dans le cadre linéaire-gaussien.\
(d) Approximation généralement nécessaire.\
Le cours insiste sur le fait que l’inférence exacte est un cas particulier ; l’inférence approximative devient la norme dès que les modèles latents sont profonds et non linéaires.
{{% /details %}}

---

Une fois le laboratoire terminé, testez-vous avec le [quiz de la semaine]({{< ref "quiz" >}}).
