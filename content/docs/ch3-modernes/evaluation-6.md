---
title: 'Évaluation 6 : Du score au modèle de diffusion'
weight: 125
---

# Évaluation 6 : Du score au modèle de diffusion

**Mini-projet 6 — Semaines 11–12.** Ce mini-projet met en pratique les concepts vus en [semaine 11]({{< ref "/docs/ch3-modernes/week11" >}}) et [semaine 12]({{< ref "/docs/ch3-modernes/week12" >}}). Il est réalisable en quelques heures.

{{< telecharger href="pdf/mini-projet-6.pdf" label="Télécharger l'énoncé de l'évaluation 6 (PDF)" >}}

> **Description**
>
> Construire un mini-DDPM afin de rendre concret le lien entre score, bruitage progressif, prédiction du bruit et génération inverse.

> **Dataset**
>
> MNIST. Utiliser un sous-ensemble d’environ 10 000 images pour garder l’entraînement léger.
>
> Lien : <https://yann.lecun.com/exdb/mnist/>

> **Problème à traiter**
>
> Visualiser le processus direct 
>
> $$x_0\rightarrow x_t\rightarrow x_T.$$
>
>
> Pendant l’entraînement, obtenir directement une version bruitée de $x_0$ : 
>
> $$x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1-\bar\alpha_t}\,\epsilon, \qquad \epsilon\sim\mathcal N(0,I).$$
>
>
> Entraîner ensuite un réseau à prédire 
>
> $$\epsilon_\theta(x_t,t)\approx\epsilon.$$
>
>
> Enfin, générer des images en partant de 
>
> $$x_T\sim\mathcal N(0,I)$$
>et en appliquant le processus inverse appris.

> **Modèle / méthode à utiliser**
>
> Petit U-Net ou réseau convolutionnel léger conditionné par un embedding du temps $t$.
>
> Pour conserver une activité de quelques heures, utiliser un sous-ensemble du dataset, un nombre réduit d’étapes de diffusion, par exemple $T\in[50,100]$, et un réseau volontairement léger.

> **5 éléments à évaluer**
>
> 1.  Visualisation du processus direct pour plusieurs valeurs de $t$.
>
> 2.  Courbe de la loss MSE sur le bruit.
>
> 3.  Qualité du débruitage à différents niveaux de bruit.
>
> 4.  Échantillons générés depuis $x_T\sim\mathcal N(0,I)$.
>
> 5.  Comparaison qualitative d’un schedule linéaire et d’un schedule cosinus.

> **5 questions clés**
>
> 1.  Que représente $t$ pour le réseau ?
>
> 2.  Pourquoi peut-on générer directement $x_t$ à partir de $x_0$ pendant l’entraînement ?
>
> 3.  Pourquoi le réseau prédit-il souvent $\epsilon$ plutôt que directement $x_0$ ?
>
> 4.  Quel lien existe entre le débruitage et le score ?
>
> 5.  Pourquoi l’échantillonnage DDPM est-il beaucoup plus lent qu’un GAN ?

## Charge de travail

- **Risque :** Très élevé
- **Garde-fou recommandé :** Sous-ensemble de MNIST, $T\in[50,100]$, U-Net très léger.

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

