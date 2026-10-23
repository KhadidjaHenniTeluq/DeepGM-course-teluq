---
title: 'Évaluation 7 : Génération dans un espace latent + Flow Matching'
weight: 145
---

# Évaluation 7 : Génération dans un espace latent + Flow Matching

**Mini-projet 7 — Semaines 13–14.** Ce mini-projet met en pratique les concepts vus en [semaine 13]({{< ref "/docs/ch3-modernes/week13" >}}) et [semaine 14]({{< ref "/docs/ch3-modernes/week14" >}}). Il est réalisable en quelques heures.

{{< telecharger href="pdf/mini-projet-7.pdf" label="Télécharger l'énoncé de l'évaluation 7 (PDF)" >}}

> **Description**
>
> Combiner compression latente et transport continu pour illustrer l’idée des modèles hybrides modernes sans entraîner un grand modèle.

> **Dataset**
>
> Fashion-MNIST.
>
> Lien : <https://github.com/zalandoresearch/fashion-mnist>

> **Problème à traiter**
>
> Entraîner d’abord un petit autoencodeur : 
>
> $$x\rightarrow z.$$
>
>
> Encoder ensuite les images du dataset afin d’obtenir des codes 
>
> $$z_1\sim p_{\mathrm{latent}}.$$
>
>
> Pour chaque code $z_1$, tirer indépendamment 
>
> $$z_0\sim\mathcal N(0,I),$$
>puis choisir 
>
> $$t\sim\mathcal U(0,1).$$
>
>
> Construire le point intermédiaire et sa vitesse cible : 
>
> $$z_t=(1-t)z_0+t z_1, \qquad u_t=z_1-z_0.$$
>
>
> Le réseau apprend alors 
>
> $$v_\theta(z_t,t)\approx u_t.$$
>
>
> Après intégration d’une ODE depuis un bruit initial, décoder le latent généré.

> **Modèle / méthode à utiliser**
>
> Petit autoencodeur + MLP pour $v_\theta(z_t,t)$.
>
> **Échantillonnage :** intégrer l’ODE 
>
> $$\frac{dz_t}{dt}=v_\theta(z_t,t), \qquad z(0)\sim\mathcal N(0,I),$$
>avec Euler explicite : 
>
> $$z_{t+\Delta t} = z_t+\Delta t\,v_\theta(z_t,t).$$
>
>
> Pour garder l’activité légère, utiliser un latent de dimension 2 ou 8 et environ 20 à 50 pas d’Euler. L’autoencodeur peut être fourni pré-entraîné si le temps de séance est limité.

> **5 éléments à évaluer**
>
> 1.  Erreur de reconstruction de l’autoencodeur.
>
> 2.  Dimension et visualisation de l’espace latent.
>
> 3.  Loss de Flow Matching $\|v_\theta(z_t,t)-u_t\|^2$.
>
> 4.  Visualisation des trajectoires de quelques points latents.
>
> 5.  Images obtenues après décodage des latents générés.

> **5 questions clés**
>
> 1.  Pourquoi est-il avantageux de générer dans l’espace latent plutôt que directement dans les pixels ?
>
> 2.  Que représentent $z_0$, $z_1$ et $z_t$ ?
>
> 3.  Quelle quantité le réseau de Flow Matching doit-il prédire ?
>
> 4.  Quelle différence fondamentale existe entre Flow Matching et DDPM ?
>
> 5.  En quoi ce mini-projet illustre-t-il une hybridation de plusieurs idées vues pendant le cours ?

## Charge de travail

- **Risque :** Moyen
- **Garde-fou recommandé :** AE pré-entraîné possible, latent 2 ou 8 dimensions, Euler 20 à 50 pas.

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

