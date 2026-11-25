# Spec

Le programme pilote la tortue turtlesim par commande vocale. Une commande
complète passe par quatre étapes : transcription, interprétation,
confirmation, exécution. À la fin, la tortue avance ou tourne selon ce que
l'utilisateur a dit et confirmé. Les arcs (vitesse linéaire et angulaire
combinées) doivent être testés contre les obstacles, et les trajectoires
doivent respecter la vitesse maximale avec une montée, un plateau et une
descente.

## Fonctions à implémenter

Chaque fonction se trouve dans le fichier indiqué et doit respecter son
docstring (Purpose, Inputs, Outputs) ainsi que ses commentaires `Indice`.
La suite `test/` doit passer en entier.

| Fonction | Fichier | Indice |
|---|---|---|
| `echantillonner_arc` | `code/arcs.py` | Intégrer x, y, theta par Euler explicite (modèle unicycle) et tester la collision avant chaque pas. |
| `Transitions.repondu` | `code/state_machine.py` | L'état courant décide où mène un refus ; traiter SORTIE et INDECIS d'abord. |
| `signer` | `code/state_machine.py` | Convention REP-103 : antihoraire positif, horaire négatif. |
| `evaluer` | `code/trajectory.py` | Trois phases : montée (a*t), plateau (vitesse de crête constante), descente (temps restant). |

## Règles

Ne faire que ce que le plan en cours demande.

Interdit :

- modifier les fichiers de `test/` ;
- changer la signature d'une fonction existante ;
- ajouter une dépendance.
