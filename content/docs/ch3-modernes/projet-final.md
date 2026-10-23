---
title: Projet final
weight: 155
---

# Projet final : quel modèle génératif choisir ?

*Analyse du besoin · choix du modèle · preuve de concept · évaluation critique*

{{< telecharger href="pdf/projet-final.pdf" label="Télécharger l'énoncé du projet final (PDF)" >}}

## But du projet

> **Objectif du projet final**
>
> L’objectif n’est pas d’implémenter le modèle le plus complexe ni d’obtenir la meilleure performance possible.
>
> Le projet doit montrer que vous êtes capable de : 
>
> **comprendre un besoin → identifier les contraintes → choisir le bon modèle → justifier ce choix → le vérifier expérimentalement**
>
>
> La compétence finale évaluée est donc la capacité à **choisir et défendre une famille de modèles génératifs en fonction d’un problème donné**.

> **À retenir**
>
> Le projet final est une **synthèse** des compétences acquises de S1 à S14. Il ne s’agit pas d’introduire une nouvelle architecture ni de refaire un gros projet technique. Vous pouvez réutiliser et adapter du code provenant des mini-projets précédents.

## Dataset commun

> **Dataset**
>
> **Dataset conseillé : Fashion-MNIST**
>
> Fashion-MNIST contient des images en niveaux de gris de taille $28\times28$, réparties en 10 catégories de vêtements.
>
> Lien : <https://github.com/zalandoresearch/fashion-mnist>
>
> Tous les étudiants utilisent le même dataset afin que l’évaluation porte sur le **choix du modèle** et non sur les différences entre jeux de données.
>
> Pour limiter le coût, un sous-ensemble de 20 000 à 30 000 images peut être utilisé.

## Choisir un scénario

Chaque étudiant choisit **un seul scénario**. Le modèle n’est pas imposé : il doit être choisi et justifié.

> **Scénario A — Génération contrôlée**
>
> Une application doit générer un type précis de vêtement à la demande : chaussure, sac, pantalon, etc. On souhaite également disposer d’un espace latent permettant l’interpolation.
>
> **Question :** quelle famille de modèle est la plus adaptée à ce besoin ?

> **Scénario B — Vraisemblance calculable**
>
> On souhaite générer de nouvelles observations, mais il est également important de pouvoir calculer une vraisemblance explicite ou exacte des observations.
>
> **Question :** quelle famille de modèle permet le mieux de répondre à cette contrainte ?

> **Scénario C — Génération rapide**
>
> Une application interactive doit produire rapidement de nouvelles images. La qualité visuelle est importante et il n’est pas nécessaire de connaître explicitement $p_\theta(x)$.
>
> **Question :** quel modèle privilégier si la vitesse d’échantillonnage est une contrainte principale ?

> **Scénario D — Génération progressive et stable**
>
> On privilégie la stabilité de l’apprentissage et une bonne couverture de la distribution. Une génération plus lente est acceptable.
>
> **Question :** quelle famille correspond le mieux à ce compromis ?

> **À retenir**
>
> **Aucun scénario n’impose une réponse unique.** Un modèle différent de la solution la plus naturelle peut être retenu s’il répond aux contraintes du scénario, si le choix est techniquement justifié et si cette justification est ensuite vérifiée par une expérience adaptée.

## Familles de modèles disponibles

L’étudiant doit considérer au minimum trois familles avant de faire son choix.

| **Famille**      | **Vraisemblance**                                              | **Vitesse**       | **Contrôle**         | **Point d’attention**       |
|:-----------------|:---------------------------------------------------------------|:------------------|:---------------------|:----------------------------|
| Auto-régressif   | Exacte                                                         | Lente             | Possible             | Génération séquentielle     |
| VAE / CVAE       | Marginale souvent intractable ; apprentissage par ELBO         | Rapide            | Fort avec condition  | Qualité parfois plus lissée |
| Normalizing Flow | Exacte                                                         | Rapide ou modérée | Possible             | Contraintes d’inversibilité |
| GAN              | Non explicite                                                  | Très rapide       | Possible             | Instabilité / mode collapse |
| Diffusion / DDPM | Objectif de débruitage ; borne ou likelihood selon formulation | Lente             | Forte avec condition | Échantillonnage itératif    |

> **À retenir**
>
> Ce tableau fournit des **repères pédagogiques** et non des lois universelles. Le choix doit être argumenté en fonction du scénario donné.

> **À retenir**
>
> **Faisabilité du scénario B.** Sur Fashion-MNIST, appliquer un Flow directement aux pixels discrets demande des précautions supplémentaires (déquantification, architecture inversible et gestion de la dimension). Pour ce projet, un Flow peut donc être appliqué à une **représentation continue de faible dimension**, par exemple une projection PCA ou des embeddings issus d’un encodeur. Un **modèle auto-régressif simple** est également un choix valide si la vraisemblance exacte sur les pixels est la priorité.

## Travail demandé

> **Travail demandé**
>
> Le projet comporte cinq étapes obligatoires.
>
> 1.  **Analyser le besoin.**
>
>     Identifier les contraintes importantes du scénario : génération contrôlée, vraisemblance calculable, vitesse de génération, stabilité, qualité/diversité et espace latent interprétable.
>
> 2.  **Comparer au moins trois familles.**
>
>     Construire un petit tableau comparatif et expliquer : 
>
>     $$\text{pourquoi choisir X} \qquad\text{et}\qquad \text{pourquoi ne pas choisir Y ou Z}.$$
>
>
> 3.  **Choisir un seul modèle.**
>
>     Le modèle peut être : 
>
>     **Auto-régressif · CVAE · RealNVP / Flow · GAN · DDPM / Diffusion**
>
>
> 4.  **Réaliser une preuve de concept simple.**
>
>     Le modèle doit être volontairement petit. Quelques époques ou un sous-ensemble des données suffisent. Le but est de vérifier le raisonnement, pas de rechercher l’état de l’art.
>
> 5.  **Vérifier le critère qui a motivé le choix.**
>
>     La propriété invoquée pour choisir le modèle doit être mesurée ou observée expérimentalement.

## Exemples de vérification

| **Modèle choisi** | **Raison principale**              | **Ce qu’il faut vérifier**                                                                                                                                                                                              |
|:------------------|:-----------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Auto-régressif    | Vraisemblance exacte               | Calculer la NLL / log-vraisemblance et mesurer le coût de la génération séquentielle.                                                                                                                                   |
| CVAE              | Génération contrôlée               | Conditionner sur une classe et vérifier que les images générées correspondent à la classe demandée.                                                                                                                     |
| Flow              | Vraisemblance calculable           | Calculer des log-vraisemblances et vérifier l’inversibilité dans l’espace continu utilisé.                                                                                                                              |
| GAN               | Échantillonnage rapide             | Mesurer le temps de génération et évaluer la diversité par une grille d’échantillons, la distribution des classes prédites par un classificateur de référence, ou une mesure simple de diversité entre images générées. |
| DDPM              | Génération progressive / stabilité | Montrer plusieurs étapes de débruitage et analyser la qualité ainsi que la diversité des échantillons obtenus.                                                                                                          |

## Contraintes techniques

-   L’entraînement doit pouvoir être réalisé sur un GPU standard ou, à défaut, sur un sous-ensemble raisonnable du dataset.

-   Les architectures doivent rester pédagogiques : réseaux légers, nombre d’époques limité et images à la résolution de Fashion-MNIST.

-   Les modèles pré-entraînés, APIs externes de génération d’images et grands modèles téléchargés ne sont pas autorisés comme **cœur de la preuve de concept**.

-   Les bibliothèques standard sont autorisées, à condition que le rapport explique clairement le mécanisme du modèle utilisé.

-   La réutilisation de code provenant des mini-projets S1–S14 est autorisée et encouragée si l’étudiant sait expliquer et adapter ce code au scénario choisi.

## 5 éléments à évaluer

> **5 éléments à évaluer**
>
> 1.  **Identification correcte des besoins — 20 %.**
>
> 2.  **Choix et justification du modèle — 30 %.**
>
>     Le choix doit être relié aux concepts du cours : 
>
>     $$\text{likelihood},\quad \text{latent},\quad \text{sampling},\quad \text{contrôle},\quad \text{stabilité}.$$
>
>
> 3.  **Preuve de concept fonctionnelle — 20 %.**
>
> 4.  **Évaluation du critère principal — 15 %.**
>
> 5.  **Analyse critique — 15 %.**

### Indicateurs de niveau 

-   **Excellent :** contraintes correctement hiérarchisées, comparaison nuancée, modèle choisi cohérent et vérification expérimentale directement alignée sur le besoin.

-   **Satisfaisant :** modèle fonctionnel et justification correcte, mais comparaison limitée ou évaluation partielle du critère principal.

-   **Insuffisant :** modèle entraîné sans justification claire, comparaison absente, ou métriques / résultats sans lien avec le scénario choisi.

## 5 questions finales

> **5 questions clés**
>
> 1.  Quel est le besoin principal de votre application et pourquoi influence-t-il le choix du modèle ?
>
> 2.  Pourquoi avez-vous choisi cette famille plutôt qu’au moins deux autres familles étudiées dans le cours ?
>
> 3.  Votre modèle permet-il de calculer une vraisemblance exacte, utilise-t-il une borne / un objectif probabiliste approché, ou définit-il principalement une procédure d’échantillonnage ?
>
> 4.  Comment votre modèle génère-t-il concrètement un nouvel échantillon ?
>
> 5.  Si l’on modifiait une contrainte du problème, par exemple exiger une vraisemblance exacte, une génération beaucoup plus rapide ou davantage de contrôle, changeriez-vous de modèle ? Pourquoi ?

## Livrables

> **Livrables**
>
> 1.  un notebook reproductible ou un script clairement organisé ;
>
> 2.  un rapport de **3 pages maximum** ;
>
> 3.  un tableau comparatif d’au moins trois familles avant le choix final ;
>
> 4.  quelques résultats expérimentaux : figures, générations ou mesures adaptées au scénario ;
>
> 5.  les réponses aux cinq questions finales ;

## Structure suggérée du rapport

1.  **Problème et contraintes** — environ un demi-page.

2.  **Comparaison des modèles et choix** — environ une page.

3.  **Expérience et résultats** — environ une page.

4.  **Analyse critique et conclusion** — environ un demi-page.

## Exemple de raisonnement attendu

> **Exemple**
>
> **Besoin :** générer une catégorie précise de vêtement et disposer d’un espace latent manipulable.
>
> L’étudiant identifie : 
>
> $$\text{contrôle} + \text{latent structuré}.$$
>
>
> Il compare ensuite plusieurs familles et peut conclure qu’un CVAE constitue un choix naturel.
>
> Il doit alors vérifier expérimentalement que : 
>
> $$y=\text{``sac''} \quad\Longrightarrow\quad \text{générations majoritairement cohérentes avec la classe ``sac''}.$$
>
>
> Le projet est évalué sur la cohérence : 
>
> **besoin → choix → expérience → conclusion**
>

## Synthèse

> **À retenir**
>
> Les mini-projets S1–S14 servent à apprendre **comment fonctionnent** les principales familles, y compris les modèles auto-régressifs, VAE, flows, GAN, EBM, diffusion et approches hybrides.
>
> Le projet final S15 vérifie une compétence différente : 
>
> **savoir choisir le modèle génératif adapté à un besoin donné**
>
>
> La qualité du raisonnement, de la justification et de l’analyse compte davantage que la quantité de code.
