---
title: Laboratoire
weight: 1
---

# Laboratoire : semaine 14

*Hybridation & modèles modernes*

> [!TIP]
> Cherchez chaque exercice **avant** d'ouvrir la solution. L'objectif est de relier les équations, les architectures et les choix de modélisation vus dans le support de la semaine.

## Exercice 1 — Compression LDM

Une image $512 \times 512 \times 3$ est encodée dans un latent $64 \times 64 \times 4$.
1. Comparez le nombre de scalaires des deux représentations.
2. Calculez approximativement le facteur de réduction.

{{% details title="Voir la solution" open=false %}}
Image : $512 \cdot 512 \cdot 3 = 786\,432$ scalaires.\
Latent : $64 \cdot 64 \cdot 4 = 16\,384$ scalaires.\
Réduction $\approx 786432/16384 = 48$.\
Le nombre de scalaires de la représentation est donc réduit d’un facteur 48 dans cet exemple. Cela ne signifie pas que le coût total de calcul du modèle est automatiquement divisé par 48 : il dépend aussi du nombre de canaux, des blocs du réseau et des mécanismes d’attention.
{{% /details %}}

## Exercice 2 — Flow Matching linéaire

On suppose ici que $x_0$ est un échantillon de la distribution de base (bruit) et que $x_1$ est un échantillon de la distribution des données. On prend $x_0 = (0, 0)$, $x_1 = (2, 4)$ et le chemin $x_t = (1-t) x_0 + t x_1$.
1. Calculez $x_{0{,}25}$.
2. Donnez la vitesse cible $u_t = x_1 - x_0$.
3. Pourquoi cette cible est-elle facile à apprendre par régression ?

{{% details title="Voir la solution" open=false %}}
1\. $x_{0{,}25} = (1 - 0{,}25) \cdot (0, 0) + 0{,}25 \cdot (2, 4) = (0{,}5, 1)$.
2. $u_t = (2, 4)$, constant pour ce chemin linéaire.
3. Pour une paire $(x_0, x_1)$ et un temps $t$, la position $x_t$ et la vitesse cible sont directement calculables. Le réseau peut donc être entraîné par une MSE sur le champ de vitesse, sans devoir estimer explicitement une densité ou un score marginal compliqué.
{{% /details %}}

---

Une fois le laboratoire terminé, testez-vous avec le [quiz de la semaine]({{< ref "quiz" >}}).
