---
title: Laboratoire
weight: 1
---

# Laboratoire : semaine 11

*Score Matching*

> [!TIP]
> Cherchez chaque exercice **avant** d'ouvrir la solution. L'objectif est de relier les équations, les architectures et les choix de modélisation vus dans le support de la semaine.

## Exercice 1 — Score d’une gaussienne

Soit $p(x) = \mathcal{N}(0, \sigma^2)$ en dimension 1.\
Calculez $s(x) = d/dx \log p(x)$ et interprétez son signe.

{{% details title="Voir la solution" open=false %}}
$\log p(x) = \text{const} - x^2/(2\sigma^2)$.\
Donc $s(x) = -x/\sigma^2$.\
Si $x > 0$, le score est négatif et pousse vers 0 ; si $x < 0$, il est positif et pousse vers 0. Le score pointe localement vers la région de densité plus élevée.
{{% /details %}}

## Exercice 2 — Score et EBM

Pour $p_\theta(x) = \exp(-E_\theta(x))/Z(\theta)$, montrez que le score ne dépend pas de $Z(\theta)$.

{{% details title="Voir la solution" open=false %}}
$\log p_\theta(x) = -E_\theta(x) - \log Z(\theta)$.\
En dérivant par rapport à $x$ :\
$\nabla_x \log p_\theta(x) = -\nabla_x E_\theta(x)$,\
car $Z(\theta)$ ne dépend pas de $x$. C’est le lien fondamental EBM $\leftrightarrow$ score.
{{% /details %}}

## Exercice 3 — Cible DSM

On ajoute un bruit gaussien : $\tilde{x} = x + \sigma \epsilon$ avec $\epsilon \sim \mathcal{N}(0, I)$.\
Montrez que la cible DSM s’écrit $-\epsilon/\sigma$.

{{% details title="Voir la solution" open=false %}}
Le score conditionnel du noyau gaussien est\
$\nabla_{\tilde{x}} \log q_\sigma(\tilde{x} \mid x) = -(\tilde{x} - x)/\sigma^2$.\
Or $\tilde{x} - x = \sigma \epsilon$.\
Donc la cible vaut $-\sigma \epsilon/\sigma^2 = -\epsilon/\sigma$.
{{% /details %}}

---

Une fois le laboratoire terminé, testez-vous avec le [quiz de la semaine]({{< ref "quiz" >}}).
