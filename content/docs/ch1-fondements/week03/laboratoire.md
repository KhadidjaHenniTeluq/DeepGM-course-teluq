---
title: Laboratoire
weight: 1
---

# Laboratoire : semaine 3

*Maximum de vraisemblance & Factorisation*

> [!TIP]
> Cherchez chaque exercice **avant** d'ouvrir la solution. L'objectif est de relier les équations, les architectures et les choix de modélisation vus dans le support de la semaine.

## Exercice 1 — MLE d’une Bernoulli

On observe 10 réalisations Bernoulli : $1,1,0,1,0,1,1,1,0,1$.
1. Écrivez la vraisemblance $L(\theta)$.
2. Donnez l’estimateur MLE de $\theta$.
3. Calculez sa valeur.

{{% details title="Voir la solution" open=false %}}
Il y a 7 succès et 3 échecs.\
$L(\theta) = \theta^7 (1-\theta)^3$.\
La log-vraisemblance vaut $7 \log \theta + 3 \log(1-\theta)$.\
Pour une Bernoulli, le MLE est la moyenne empirique : $\hat{\theta} = 7/10 = 0{,}7$.
{{% /details %}}

## Exercice 2 — De la vraisemblance à la NLL

Expliquez pourquoi maximiser la log-vraisemblance d’un dataset iid revient à minimiser la Negative Log-Likelihood (NLL).

{{% details title="Voir la solution" open=false %}}
Pour des observations iid, $L(\theta) = \prod_i p_\theta(x^{(i)})$. Le logarithme transforme le produit en somme :\
$\log L(\theta) = \sum_i \log p_\theta(x^{(i)})$.\
Maximiser cette quantité est équivalent à minimiser son opposé :\
$\mathrm{NLL}(\theta) = -\sum_i \log p_\theta(x^{(i)})$.\
Les deux problèmes ont donc le même optimum.
{{% /details %}}

## Exercice 3 — Factoriser une loi jointe

Pour $x = (x_1, x_2, x_3, x_4)$, écrivez une factorisation auto-régressive complète de $p(x)$. Indiquez ce que doit apprendre le modèle à chaque étape.

{{% details title="Voir la solution" open=false %}}
$p(x) = p(x_1) p(x_2 \mid x_1) p(x_3 \mid x_1, x_2) p(x_4 \mid x_1, x_2, x_3)$.\
Le modèle apprend donc quatre distributions conditionnelles, chacune utilisant les composantes précédentes selon l’ordre choisi. Cette factorisation rend une loi jointe complexe manipulable comme une suite de prédictions conditionnelles.
{{% /details %}}

---

Une fois le laboratoire terminé, testez-vous avec le [quiz de la semaine]({{< ref "quiz" >}}).
