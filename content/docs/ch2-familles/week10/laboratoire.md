---
title: Laboratoire
weight: 1
---

# Laboratoire : semaine 10

*Modèles génératifs implicites*

> [!TIP]
> Cherchez chaque exercice **avant** d'ouvrir la solution. L'objectif est de relier les équations, les architectures et les choix de modélisation vus dans le support de la semaine.

## Exercice 1 — Discriminateur optimal du GAN

Dans le GAN original, pour un générateur fixé, on a :\
$D^*(x) = p_{\text{data}}(x)/(p_{\text{data}}(x) + p_G(x))$.\
Calculez $D^*(x)$ si $p_{\text{data}}(x) = p_G(x)$, puis interprétez.

{{% details title="Voir la solution" open=false %}}
Si $p_{\text{data}}(x) = p_G(x)$, alors\
$D^*(x) = p/(p+p) = 1/2$.\
Le discriminateur optimal ne peut pas distinguer réel et généré mieux que le hasard. Cela correspond à l’équilibre théorique où les deux distributions coïncident.
{{% /details %}}

## Exercice 2 — Mode collapse

Un GAN génère 10 000 images très nettes mais presque toutes de deux classes sur un dataset comportant dix classes.
1. Quel problème observez-vous ?
2. Pourquoi une simple inspection de quelques images peut-elle le manquer ?
3. Quelle famille de métriques faut-il ajouter ?

{{% details title="Voir la solution" open=false %}}
1\. Mode collapse / mauvaise couverture des modes.
2. Des échantillons individuels peuvent être de haute qualité tout en ayant une diversité globale très faible.
3. Il faut des métriques distinguant qualité et couverture/diversité : precision/recall, density/coverage, ou une analyse de distribution de classes ; FID/KID peuvent aussi fournir une comparaison globale mais ne remplacent pas toute analyse de couverture.
{{% /details %}}

## Exercice 3 — MMD et noyaux

Deux distributions différentes $P$ et $Q$ ont $\mathrm{MMD}(P, Q) = 0$ avec un noyau polynomial de degré fini.\
Est-ce contradictoire ? Expliquez.

{{% details title="Voir la solution" open=false %}}
Non. Le MMD identifie $P$ et $Q$ seulement lorsque le noyau est caractéristique (sous les hypothèses adaptées). Un noyau polynomial de degré fini n’est pas caractéristique en général ; deux distributions peuvent partager les moments captés par ce noyau tout en restant différentes. Le choix du noyau est donc essentiel.
{{% /details %}}

---

Une fois le laboratoire terminé, testez-vous avec le [quiz de la semaine]({{< ref "quiz" >}}).
