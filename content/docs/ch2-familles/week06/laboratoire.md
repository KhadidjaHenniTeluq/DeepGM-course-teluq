---
title: Laboratoire
weight: 1
---

# Laboratoire : semaine 6

*Autoencodeurs profonds*

> [!TIP]
> Cherchez chaque exercice **avant** d'ouvrir la solution. L'objectif est de relier les équations, les architectures et les choix de modélisation vus dans le support de la semaine.

## Exercice 1 — Construire un autoencodeur conceptuel

On veut compresser des images de 784 dimensions dans un latent $z$ de dimension 16.\
Proposez la chaîne encodeur-décodeur minimale et donnez une perte de reconstruction adaptée à des pixels continus.

{{% details title="Voir la solution" open=false %}}
Une architecture conceptuelle possible :\
$x \in \mathbb{R}^{784} \to h_1 \to z \in \mathbb{R}^{16} \to h_1' \to \hat{x} \in \mathbb{R}^{784}$.\
L’encodeur $f_\phi$ calcule $z = f_\phi(x)$, le décodeur $g_\theta$ calcule $\hat{x} = g_\theta(z)$.\
Pour des pixels continus, on peut utiliser $L_{\text{rec}} = \|x - \hat{x}\|^2$ (MSE).
{{% /details %}}

## Exercice 2 — Effet du bottleneck

Que se passe-t-il conceptuellement si on augmente la dimension du latent d’un autoencodeur de 2 à 512 sur un dataset simple ? Discutez reconstruction et qualité de représentation.

{{% details title="Voir la solution" open=false %}}
Un latent plus large facilite généralement la reconstruction car le modèle peut conserver davantage d’information. Mais un bottleneck trop large peut réduire la pression à apprendre une représentation compacte et structurée ; le modèle peut se rapprocher d’une copie de l’entrée. Un latent très petit force une compression plus forte mais peut perdre de l’information. Le bon compromis dépend du dataset et de l’objectif.
{{% /details %}}

## Exercice 3 — Pourquoi l’AE n’est pas encore un vrai générateur

Un autoencodeur reconstruit presque parfaitement le dataset. On échantillonne ensuite $z \sim \mathcal{N}(0, I)$ et on décode. Les sorties sont mauvaises. Expliquez ce résultat sans invoquer un bug de code.

{{% details title="Voir la solution" open=false %}}
L’autoencodeur classique n’a jamais été entraîné à faire correspondre la distribution de ses codes à $\mathcal{N}(0, I)$. Les codes $z = f_\phi(x)$ peuvent occuper une région irrégulière ou discontinue de l’espace latent. Des $z$ tirés au hasard peuvent tomber dans des zones jamais vues par le décodeur, qui n’a été entraîné qu’autour des codes produits par l’encodeur. D’où : bonne reconstruction $\neq$ espace latent échantillonnable. C’est précisément cette limite qui motive l’introduction du VAE en S7, où une régularisation KL rapproche $q_\phi(z \mid x)$ d’une prior simple $p(z) = \mathcal{N}(0, I)$.
{{% /details %}}

---

Une fois le laboratoire terminé, testez-vous avec le [quiz de la semaine]({{< ref "quiz" >}}).
