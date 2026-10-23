---
title: Laboratoire
weight: 1
---

# Laboratoire : semaine 1

*Rappels NN & Représentations*

> [!TIP]
> Cherchez chaque exercice **avant** d'ouvrir la solution. L'objectif est de relier les équations, les architectures et les choix de modélisation vus dans le support de la semaine.

## Exercice 1 — Identifier la représentation apprise

On considère trois systèmes :\
(a) un CNN qui transforme une image en un vecteur de 128 caractéristiques avant classification ;\
(b) un RNN qui lit une phrase et conserve un état caché final $h_T$ ;\
(c) un Transformer qui produit un vecteur contextuel pour chaque token.\
Pour chacun, indiquez où se trouve la représentation apprise et expliquez en une phrase ce qu’elle résume.

{{% details title="Voir la solution" open=false %}}
\(a\) Le vecteur de 128 caractéristiques constitue la représentation apprise : il résume des motifs visuels utiles à la tâche.\
(b) L’état caché $h_T$ est une représentation de la séquence telle qu’elle a été accumulée au fil du RNN.\
(c) Les vecteurs contextuels sont les représentations apprises : chaque token est représenté en fonction des autres tokens auxquels l’attention donne du poids.\
Idée centrale : une représentation n’est pas la donnée brute ; c’est une transformation apprise qui organise l’information utile.
{{% /details %}}

## Exercice 2 — Reconstruction ou génération ?

Classifiez chacune des opérations suivantes comme reconstruction ou génération.
1. Encoder une image $x$ en $z$ puis calculer $\hat{x} = \mathrm{decode}(z)$.
2. Tirer $z \sim p(z)$ puis produire $x_{\text{new}} = \mathrm{decode}(z)$.
3. Prendre une phrase observée et produire une version compressée puis reconstruite.
4. Produire une nouvelle image à partir d’un latent choisi sans image d’entrée.

{{% details title="Voir la solution" open=false %}}
1\. Reconstruction : le processus part d’une observation $x$ et cherche à la retrouver.
2. Génération : le processus part d’un échantillon latent et produit une nouvelle observation.
3. Reconstruction : une observation cible existe à l’entrée.
4. Génération : aucune observation cible n’est donnée en entrée.
La distinction essentielle est donc la provenance de l’information : reconstruire part d’un $x$ observé ; générer vise un nouvel $x$ plausible.
{{% /details %}}

## Exercice 3 — Mini-analyse d’un espace latent

Deux images $x_1$ et $x_2$ sont encodées en $z_1$ et $z_2$, avec $\|z_1 - z_2\|$ très faible. Peut-on conclure qu’elles sont sémantiquement similaires ? Donnez une réponse nuancée.

{{% details title="Voir la solution" open=false %}}
Pas automatiquement. Une proximité dans l’espace latent traduit la géométrie apprise par le modèle et la tâche d’entraînement. Elle peut correspondre à une similarité sémantique si l’apprentissage a organisé le latent dans ce sens, mais ce n’est pas garanti. Il faut vérifier empiriquement la structure du latent, par exemple avec des voisins, des interpolations ou des visualisations.
{{% /details %}}

---

Une fois le laboratoire terminé, testez-vous avec le [quiz de la semaine]({{< ref "quiz" >}}).
