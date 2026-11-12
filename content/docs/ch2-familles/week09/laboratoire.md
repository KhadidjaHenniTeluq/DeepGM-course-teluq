---
title: Laboratoire
weight: 1
---

# Laboratoire : semaine 9

*Modèles fondés sur l'énergie (EBM)*

> [!TIP]
> Cherchez chaque exercice **avant** d'ouvrir la solution. L'objectif est de relier les équations, les architectures et les choix de modélisation vus dans le support de la semaine.

## Exercice 1 — Énergie et probabilité

On définit $p_\theta(x) = \exp(-E_\theta(x))/Z(\theta)$.
1. Que se passe-t-il pour $p_\theta(x)$ quand $E_\theta(x)$ diminue ?
2. Quel est le rôle de $Z(\theta)$ ?
3. Pourquoi $Z(\theta)$ pose-t-il un problème en haute dimension ?

{{% details title="Voir la solution" open=false %}}
1\. Une énergie plus faible augmente la densité relative de $x$.
2. $Z(\theta)$ normalise la densité pour que l’intégrale / somme totale vaille 1.
3. $Z(\theta)$ exige en général une intégration ou sommation sur toutes les configurations possibles, ce qui devient intractable en haute dimension.
{{% /details %}}

## Exercice 2 — Phase positive et phase négative

Expliquez qualitativement les deux termes du gradient de log-vraisemblance d’un EBM : contribution des données et contribution des échantillons du modèle.

{{% details title="Voir la solution" open=false %}}
La phase positive baisse l’énergie des vraies données / augmente leur probabilité. La phase négative pousse dans l’autre sens pour les configurations produites par le modèle, afin d’éviter que toute la distribution ne s’effondre. Le gradient dépend donc à la fois des données et de l’espérance sous le modèle, ce qui explique le besoin d’échantillonnage MCMC.
{{% /details %}}

---

Une fois le laboratoire terminé, testez-vous avec le [quiz de la semaine]({{< ref "quiz" >}}).
