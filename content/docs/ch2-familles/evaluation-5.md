---
title: 'Évaluation 5 : Énergie vs génération implicite'
weight: 105
---

# Évaluation 5 : Énergie vs génération implicite

**Mini-projet 5 — Semaines 9–10.** Ce mini-projet met en pratique les concepts vus en [semaine 9]({{< ref "/docs/ch2-familles/week09" >}}) et [semaine 10]({{< ref "/docs/ch2-familles/week10" >}}). Il est réalisable en quelques heures.

{{< telecharger href="pdf/mini-projet-5.pdf" label="Télécharger l'énoncé de l'évaluation 5 (PDF)" >}}

> **Description**
>
> Comparer un EBM, qui apprend une fonction d’énergie, et un GAN, qui apprend directement une procédure de génération implicite.

> **Dataset**
>
> **Dataset : mélange de 8 gaussiennes 2D.**
>
> Les centres sont placés régulièrement sur un cercle, par exemple 
>
> $$\mu_k = r \begin{pmatrix} \cos(2\pi k/8)\\ \sin(2\pi k/8) \end{pmatrix}, \qquad k=0,\ldots,7.$$
>
>
> Chaque observation est tirée autour d’un centre avec une petite covariance isotrope. Aucun téléchargement n’est nécessaire : le dataset est généré directement avec NumPy.
>
> Ce choix est préférable à Two Moons pour ce bloc, car les **8 modes distincts** permettent de voir immédiatement si un GAN couvre toute la distribution ou s’il ignore certains modes.

> **Problème à traiter**
>
> Apprendre (A) une fonction d’énergie $E_\theta(x)$ et visualiser son paysage, puis (B) un petit GAN 2D 
>
> $$z\rightarrow G_\theta(z)\rightarrow x.$$
>Comparer les régions d’énergie faible, les échantillons Langevin et les échantillons GAN.

> **Modèle / méthode à utiliser**
>
> Petit MLP comme fonction d’énergie. Utiliser des chaînes de Langevin courtes pour produire les échantillons négatifs ; une banque persistante de particules est recommandée mais optionnelle.
>
> Petit GAN composé de deux MLP, entraîné sur le même dataset. L’objectif reste qualitatif : visualiser le paysage d’énergie, la dynamique des échantillons et la couverture des modes.

> **5 éléments à évaluer**
>
> 1.  Carte du paysage d’énergie.
>
> 2.  Position des vraies données dans les régions d’énergie faible.
>
> 3.  Échantillons générés par Langevin.
>
> 4.  Échantillons produits par le GAN.
>
> 5.  Nombre de modes couverts parmi les 8 gaussiennes et répartition approximative des échantillons entre ces modes.

> **5 questions clés**
>
> 1.  Pourquoi une faible énergie correspond-elle à une configuration plausible ?
>
> 2.  À quoi sert la fonction de partition $Z(\theta)$ ?
>
> 3.  Pourquoi l’apprentissage d’un EBM nécessite-t-il de l’échantillonnage, et pourquoi des chaînes de Langevin courtes ne donnent-elles que des échantillons approximatifs ?
>
> 4.  Pourquoi un GAN peut-il générer sans calculer $p_\theta(x)$ ?
>
> 5.  Comment détecter un mode collapse lorsque la distribution réelle possède 8 modes ?

## Charge de travail

- **Risque :** Élevé
- **Garde-fou recommandé :** MLP 2D, nombre fixe de pas Langevin, GAN minimal.

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

