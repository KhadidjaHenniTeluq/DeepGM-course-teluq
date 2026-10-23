---
title: Laboratoire
weight: 1
---

# Laboratoire : semaine 7

*Autoencodeurs variationnels (VAE)*

> [!TIP]
> Cherchez chaque exercice **avant** d'ouvrir la solution. L'objectif est de relier les équations, les architectures et les choix de modélisation vus dans le support de la semaine.

## Exercice 1 — Lire l’ELBO

On considère :\
$\mathrm{ELBO} = \mathbb{E}_{q_\phi(z \mid x)}[\log p_\theta(x \mid z)] - \mathrm{KL}(q_\phi(z \mid x) \| p(z))$.\
Expliquez le rôle de chacun des deux termes et ce qui arriverait si on supprimait complètement le terme KL.

{{% details title="Voir la solution" open=false %}}
Le premier terme favorise une bonne reconstruction / vraisemblance conditionnelle : le décodeur doit expliquer $x$ à partir de $z$.\
Le second rapproche le posterior approché $q_\phi(z \mid x)$ de la prior $p(z)$, ce qui structure l’espace latent.\
Sans KL, le VAE se rapprocherait d’un autoencodeur stochastique axé sur la reconstruction ; l’espace latent pourrait perdre la régularité qui permet d’échantillonner facilement depuis $p(z)$.
{{% /details %}}

## Exercice 2 — Reparamétrisation

L’encodeur produit $\mu(x)$ et $\sigma(x)$. Écrivez la reparamétrisation de $z$ avec $\epsilon \sim \mathcal{N}(0, I)$ et expliquez pourquoi elle est utile pour l’optimisation.

{{% details title="Voir la solution" open=false %}}
On écrit :\
$z = \mu_\phi(x) + \sigma_\phi(x) \odot \epsilon$, $\epsilon \sim \mathcal{N}(0, I)$.\
L’aléa est déplacé dans $\epsilon$, tandis que $z$ devient une fonction différentiable de $\mu$ et $\sigma$. Le gradient peut donc remonter à travers l’échantillonnage jusqu’aux paramètres de l’encodeur.
{{% /details %}}

## Exercice 3 — Effet de β dans le β-VAE

Comparez qualitativement $\beta = 0{,}5$, $\beta = 1$ et $\beta = 4$ dans la perte d’un $\beta$-VAE :\
$$\mathcal L_{\beta\text{-VAE}} = -\mathbb E_{q_\phi(z\mid x)}[\log p_\theta(x\mid z)] + \beta\,D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\,\|\,p(z)\right).$$
Dans une écriture pédagogique, le premier terme est souvent assimilé à une erreur de reconstruction. Que prévoyez-vous pour la reconstruction et l’organisation du latent ?

{{% details title="Voir la solution" open=false %}}
$\beta = 0{,}5$ : priorité relative à la reconstruction, latent moins fortement régularisé.\
$\beta = 1$ : VAE standard.\
$\beta = 4$ : régularisation plus forte, latent souvent plus proche de la prior et potentiellement plus structuré, mais avec un risque de reconstruction plus dégradée.\
Il s’agit d’un compromis, pas d’une règle absolue.
{{% /details %}}

---

Une fois le laboratoire terminé, testez-vous avec le [quiz de la semaine]({{< ref "quiz" >}}).
