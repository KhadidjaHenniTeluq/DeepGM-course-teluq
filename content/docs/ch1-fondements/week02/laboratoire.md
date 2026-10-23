---
title: Laboratoire
weight: 1
---

# Laboratoire : semaine 2

*Discriminatif vs Génératif*

> [!TIP]
> Cherchez chaque exercice **avant** d'ouvrir la solution. L'objectif est de relier les équations, les architectures et les choix de modélisation vus dans le support de la semaine.

## Exercice 1 — Discriminatif ou génératif ?

Pour chaque expression, dites si elle correspond naturellement à un objectif discriminatif ou génératif :\
(a) $p_\theta(y \mid x)$\
(b) $p_\theta(x)$\
(c) $p_\theta(x, y)$\
(d) prédire une classe à partir d’une image\
(e) produire de nouveaux échantillons ressemblant au jeu de données.

{{% details title="Voir la solution" open=false %}}
\(a\) Discriminatif.\
(b) Génératif.\
(c) Génératif, car le modèle décrit la loi jointe des observations et des étiquettes.\
(d) Discriminatif.\
(e) Génératif.\
Un modèle discriminatif cible directement la décision $y$ connaissant $x$ ; un modèle génératif décrit la distribution des données, éventuellement avec $y$.
{{% /details %}}

## Exercice 2 — Explicite ou implicite ?

Un modèle A permet de calculer $p_\theta(x)$ pour une observation donnée. Un modèle B définit seulement une procédure $z \to G_\theta(z)$ permettant d’échantillonner, sans formule exploitable de $p_\theta(x)$.\
Classez A et B comme modèles explicites ou implicites et justifiez.

{{% details title="Voir la solution" open=false %}}
A est explicite : sa densité ou sa vraisemblance est calculable.\
B est implicite : il définit surtout une procédure d’échantillonnage, sans densité explicite directement évaluée.\
Cette distinction sera importante pour comprendre pourquoi les méthodes d’apprentissage et d’évaluation diffèrent selon les familles.
{{% /details %}}

---

Une fois le laboratoire terminé, testez-vous avec le [quiz de la semaine]({{< ref "quiz" >}}).
