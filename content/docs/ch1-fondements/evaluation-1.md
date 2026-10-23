---
title: 'Évaluation 1 : Représentations apprises : classifier n’est pas générer'
weight: 25
---

# Évaluation 1 : Représentations apprises : classifier n’est pas générer

**Mini-projet 1 — Semaines 1–2.** Ce mini-projet met en pratique les concepts vus en [semaine 1]({{< ref "/docs/ch1-fondements/week01" >}}) et [semaine 2]({{< ref "/docs/ch1-fondements/week02" >}}). Il est réalisable en quelques heures.

{{< telecharger href="pdf/mini-projet-1.pdf" label="Télécharger l'énoncé de l'évaluation 1 (PDF)" >}}

> **Description**
>
> Entraîner un petit CNN discriminatif, extraire sa représentation interne et visualiser les embeddings afin de comprendre la différence entre représentation, classification et génération.

> **Dataset**
>
> Fashion-MNIST : images 28×28 en niveaux de gris, 10 classes de vêtements.
>
> Lien : <https://github.com/zalandoresearch/fashion-mnist>

> **Problème à traiter**
>
> Entraîner un petit CNN pour reconnaître les 10 catégories. Récupérer ensuite le vecteur de caractéristiques juste avant la couche de classification et projeter ces représentations en 2D avec PCA. Le but est d’observer si les classes se regroupent et d’expliquer pourquoi cette représentation n’est pas encore un modèle génératif.

> **Modèle / méthode à utiliser**
>
> Petit CNN : 
>
> $$28\times28 \rightarrow \mathrm{Conv} \rightarrow \mathrm{Conv} \rightarrow z \rightarrow \mathrm{Linear}(10).$$
>

> **5 éléments à évaluer**
>
> 1.  Accuracy du classificateur sur le jeu de test.
>
> 2.  Visualisation PCA des embeddings.
>
> 3.  Distance entre embeddings de deux exemples d’une même classe.
>
> 4.  Distance entre embeddings de classes différentes.
>
> 5.  Explication de la raison pour laquelle un latent arbitraire ne permet pas automatiquement de générer une image plausible.

> **5 questions clés**
>
> 1.  Où se trouve exactement la représentation apprise dans le CNN ?
>
> 2.  Deux images proches dans l’espace latent sont-elles forcément similaires sémantiquement ?
>
> 3.  Le CNN apprend-il $p(y\mid x)$, $p(x)$ ou $p(x,y)$ ?
>
> 4.  Pourquoi ce réseau est-il discriminatif et non génératif ?
>
> 5.  Que faudrait-il ajouter pour passer de $x\rightarrow z\rightarrow y$ à un mécanisme capable de produire un nouvel $x$ ?

## Charge de travail

- **Risque :** Faible
- **Garde-fou recommandé :** 3 à 5 époques de CNN suffisent.

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

