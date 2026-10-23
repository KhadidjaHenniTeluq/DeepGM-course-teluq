---
title: 'Évaluation 2 : Maximum de vraisemblance et variable latente'
weight: 45
---

# Évaluation 2 : Maximum de vraisemblance et variable latente

**Mini-projet 2 — Semaines 3–4.** Ce mini-projet met en pratique les concepts vus en [semaine 3]({{< ref "/docs/ch1-fondements/week03" >}}) et [semaine 4]({{< ref "/docs/ch1-fondements/week04" >}}). Il est réalisable en quelques heures.

{{< telecharger href="pdf/mini-projet-2.pdf" label="Télécharger l'énoncé de l'évaluation 2 (PDF)" >}}

> **Description**
>
> Mettre en pratique MLE, log-vraisemblance, variables latentes et inférence à l’aide d’un exemple 2D totalement visualisable.

> **Dataset**
>
> Mélange synthétique de deux gaussiennes 2D. Aucun téléchargement n’est nécessaire.

> **Problème à traiter**
>
> Générer des observations selon 
>
> $$p(x)=0.5\,\mathcal N(\mu_1,\Sigma_1)+0.5\,\mathcal N(\mu_2,\Sigma_2),$$
>par exemple avec $\mu_1=(-2,0)$ et $\mu_2=(2,0)$. Ajuster d’abord une gaussienne unique, puis un mélange de deux gaussiennes et interpréter le posterior $p(z\mid x)$.

> **Modèle / méthode à utiliser**
>
> Utiliser un **Gaussian Mixture Model**, par exemple `sklearn.mixture.GaussianMixture`. La variable latente $z\in\{0,1\}$ représente la composante ayant généré chaque point.

> **5 éléments à évaluer**
>
> 1.  Estimation correcte des paramètres de la gaussienne ou des composantes.
>
> 2.  Calcul ou affichage de la log-vraisemblance.
>
> 3.  Comparaison gaussienne unique vs mélange de deux gaussiennes.
>
> 4.  Visualisation des deux composantes latentes.
>
> 5.  Calcul ou interprétation du posterior $p(z\mid x)$.

> **5 questions clés**
>
> 1.  Pourquoi maximise-t-on la log-vraisemblance plutôt que la vraisemblance brute ?
>
> 2.  Que représente ici la variable latente $z$ ?
>
> 3.  Pourquoi $z$ est-elle dite non observée ?
>
> 4.  Quelle différence existe entre apprendre les paramètres du modèle et inférer $z$ ?
>
> 5.  Pourquoi le calcul de $p(z\mid x)$ devient-il plus difficile avec un modèle latent profond ?

## Charge de travail

- **Risque :** Très faible
- **Garde-fou recommandé :** Utiliser `GaussianMixture` et imposer les visualisations.

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

