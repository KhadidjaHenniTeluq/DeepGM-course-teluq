---
title: Laboratoire
weight: 1
---

# Laboratoire : semaine 12

*Modèles de diffusion*

> [!TIP]
> Cherchez chaque exercice **avant** d'ouvrir la solution. L'objectif est de relier les équations, les architectures et les choix de modélisation vus dans le support de la semaine.

## Exercice 1 — Échantillonnage direct dans un DDPM

On donne $\bar{\alpha}_t = 0{,}64$ et un scalaire $x_0 = 2$. Pour $\epsilon = -1$, calculez $x_t$ avec :\
$x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1 - \bar{\alpha}_t} \epsilon$.

{{% details title="Voir la solution" open=false %}}
$\sqrt{0{,}64} = 0{,}8$ et $\sqrt{0{,}36} = 0{,}6$.\
Donc $x_t = 0{,}8 \cdot 2 + 0{,}6 \cdot (-1) = 1{,}6 - 0{,}6 = 1{,}0$.
{{% /details %}}

## Exercice 2 — DDPM ou DDIM ?

On dispose d’un modèle de bruit $\epsilon_\theta(x_t, t)$ déjà entraîné.\
Comparez deux stratégies :\
(a) 1000 étapes stochastiques de DDPM ;\
(b) 50 étapes déterministes DDIM.\
Quels compromis attendez-vous ?

{{% details title="Voir la solution" open=false %}}
DDPM ancestral suit une trajectoire stochastique plus longue et fidèle au sampler de référence, mais coûte de nombreux appels réseau.\
DDIM peut utiliser un sous-ensemble d’instants et, avec stochasticité nulle, une trajectoire déterministe beaucoup plus rapide. La qualité peut rester élevée mais dépend du nombre d’étapes et du modèle ; l’accélération peut introduire un compromis qualité/vitesse.
{{% /details %}}

---

Une fois le laboratoire terminé, testez-vous avec le [quiz de la semaine]({{< ref "quiz" >}}).
