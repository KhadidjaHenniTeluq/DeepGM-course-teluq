---
title: 'Évaluation 4 : Deux façons de structurer un espace latent : VAE vs Flow'
weight: 85
---

# Évaluation 4 : Deux façons de structurer un espace latent : VAE vs Flow

**Mini-projet 4 — Semaines 7–8.** Ce mini-projet met en pratique les concepts vus en [semaine 7]({{< ref "/docs/ch2-familles/week07" >}}) et [semaine 8]({{< ref "/docs/ch2-familles/week08" >}}). Il est réalisable en quelques heures.

{{< telecharger href="pdf/mini-projet-4.pdf" label="Télécharger l'énoncé de l'évaluation 4 (PDF)" >}}

> **Description**
>
> Comparer un VAE entraîné avec une ELBO et un normalizing flow qui impose l’inversibilité pour calculer une vraisemblance exacte.

> **Dataset**
>
> **Dataset principal : Fashion-MNIST.** Le VAE est entraîné sur les images $28\times28$.
>
> Lien : <https://github.com/zalandoresearch/fashion-mnist>
>
> Pour le Flow, on travaille volontairement dans un **espace 2D continu et visualisable**, construit à partir de Fashion-MNIST : PCA 2D ou codes latents 2D du VAE. Ainsi, RealNVP n’est pas entraîné directement sur les 784 pixels.

> **Problème à traiter**
>
> Construire un VAE sur Fashion-MNIST avec un latent 
>
> $$z\in\mathbb{R}^2.$$
>
>
> Pour le Flow, ne pas entraîner RealNVP directement sur les images $28\times28$ : utiliser soit :
>
> -   les deux premières composantes d’une PCA appliquée aux images ;
>
> -   les codes latents 2D extraits par le VAE après entraînement ;
>
> -   un sous-ensemble limité à deux classes, puis projeté en 2D.
>
> Observer la différence entre latent régularisé, ELBO, inversibilité et vraisemblance exacte dans cet espace 2D visualisable.

> **Modèle / méthode à utiliser**
>
> VAE dense ou convolutionnel léger ; RealNVP 2D avec quelques couches de couplage. Le Flow doit rester volontairement petit : deux à quatre couches de couplage suffisent pour cette activité.

> **5 éléments à évaluer**
>
> 1.  Qualité de reconstruction du VAE.
>
> 2.  Organisation du latent $z$ du VAE.
>
> 3.  Échantillons générés avec $z\sim\mathcal N(0,I)$.
>
> 4.  Vérification numérique de $f^{-1}(f(z))\approx z$.
>
> 5.  Log-vraisemblance calculée par le Flow.

> **5 questions clés**
>
> 1.  Quel est le rôle du terme reconstruction dans l’ELBO ?
>
> 2.  Quel est le rôle de $D_{\mathrm{KL}}(q_\phi(z\mid x)\|p(z))$ ?
>
> 3.  Pourquoi le VAE permet-il d’échantillonner plus naturellement qu’un AE classique ?
>
> 4.  Pourquoi RealNVP impose-t-il des transformations inversibles ?
>
> 5.  Quelle différence essentielle existe entre ELBO et vraisemblance exacte ?

## Charge de travail

- **Risque :** Moyen
- **Garde-fou recommandé :** VAE 2D + RealNVP uniquement dans un espace 2D.

## Consignes communes à tous les mini-projets

### Principes généraux 

Chaque mini-projet est conçu pour être réalisable en quelques heures et sert à **mettre en pratique les concepts vus pendant les deux semaines correspondantes**. L’objectif n’est pas d’obtenir le meilleur score possible, mais de comprendre le comportement, les hypothèses et les compromis des modèles.

-   Fashion-MNIST et MNIST servent de datasets fil rouge pour faciliter les comparaisons.

-   Les datasets synthétiques 2D sont privilégiés lorsque la visualisation des densités, champs de vecteurs ou trajectoires est essentielle.

-   Chaque mini-projet comporte exactement **5 éléments à évaluer** et **5 questions clés de réflexion**.

### Livrable commun 

Pour chaque mini-projet, remettre :

1.  un notebook reproductible ou un script clairement organisé ;

2.  les cinq éléments demandés dans la section **5 éléments à évaluer** ;

3.  des réponses courtes aux cinq questions clés ;

4.  une conclusion de 150 à 250 mots reliant les résultats aux concepts du cours.

> **À noter**
>
> **Important :** l’évaluation porte autant sur l’interprétation probabiliste des résultats que sur le fonctionnement du code. Il n’est pas demandé d’optimiser les modèles jusqu’à obtenir des performances de référence.

