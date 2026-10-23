---
title: 'Évaluation 3 : Génération auto-régressive vs reconstruction par autoencodeur'
weight: 65
---

# Évaluation 3 : Génération auto-régressive vs reconstruction par autoencodeur

**Mini-projet 3 — Semaines 5–6.** Ce mini-projet met en pratique les concepts vus en [semaine 5]({{< ref "/docs/ch2-familles/week05" >}}) et [semaine 6]({{< ref "/docs/ch2-familles/week06" >}}). Il est réalisable en quelques heures.

{{< telecharger href="pdf/mini-projet-3.pdf" label="Télécharger l'énoncé de l'évaluation 3 (PDF)" >}}

> **Description**
>
> Comparer la génération composante par composante d’un modèle auto-régressif à la reconstruction globale d’un autoencodeur.

> **Dataset**
>
> MNIST : images 28×28 de chiffres manuscrits. Pour réduire le coût, utiliser environ 10 000 images ou une résolution 14×14.
>
> Lien : <https://yann.lecun.com/exdb/mnist/>

> **Problème à traiter**
>
> Construire deux petits modèles : (A) un modèle auto-régressif sur MNIST binarisé, 
>
> $$p(x)=\prod_i p(x_i\mid x_{<i}),$$
>et (B) un autoencodeur 
>
> $$x\rightarrow z\rightarrow \hat{x}.$$
>Comparer surtout leurs mécanismes et non leur performance absolue.

> **Modèle / méthode à utiliser**
>
> Un MADE ou réseau masqué simple, et un autoencodeur dense ou convolutionnel léger.

> **5 éléments à évaluer**
>
> 1.  NLL du modèle auto-régressif.
>
> 2.  Temps de génération de plusieurs images auto-régressives.
>
> 3.  Erreur de reconstruction de l’autoencodeur.
>
> 4.  Visualisation de l’espace latent de l’autoencodeur.
>
> 5.  Test de génération en décodant des $z$ aléatoires.

> **5 questions clés**
>
> 1.  Pourquoi le modèle auto-régressif possède-t-il une vraisemblance calculable ?
>
> 2.  Pourquoi sa génération est-elle séquentielle ?
>
> 3.  Pourquoi l’autoencodeur peut-il reconstruire une image rapidement ?
>
> 4.  Pourquoi un excellent autoencodeur peut-il produire de mauvaises images avec $z\sim\mathcal N(0,I)$ ?
>
> 5.  Quelle limite de l’autoencodeur motive directement le VAE ?

## Charge de travail

- **Risque :** Élevé
- **Garde-fou recommandé :** MADE simplifié, images $14\times14$, 5 000 à 10 000 exemples.

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

