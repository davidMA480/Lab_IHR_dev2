# Plan 2

1. Dans `code\state_machine.py`, dans `Transitions.repondu`, **supprimer l'instruction
   `raise NotImplementedError(...)` en entier** (les 3 lignes, parenthèse fermante comprise)
   et la **remplacer par l'implémentation**. Aucun `raise NotImplementedError` ne doit rester
   dans la fonction, et elle ne doit pas se terminer par `pass` ni par un `return None`.
   Suivre son docstring et son commentaire `Indice`.
   Ne pas modifier `test/`.

   1. **Garder** la première ligne `self._exiger(Etat.CONFIRMATION_COMMANDE, Etat.CONFIRMATION_ACTION)`
      et le commentaire `# Indice` / `# Tests`.
   2. **Classer la réponse** avec les outils déjà présents dans le fichier (classificateur de
      réponse, listes de mots, constantes) : chercher d'abord comment `texte` est interprété
      ailleurs dans le code, ne pas réinventer la détection.
   3. **Ordre des vérifications** (c'est ce que dit l'`Indice`) :
      1. `SORTIE` d'abord, quel que soit l'état courant ;
      2. `INDECIS` ensuite : rester dans l'état courant et reposer la question ;
      3. puis seulement acceptation ou refus.
   4. **Acceptation** : avancer selon l'état courant (voir les autres méthodes de la classe).
   5. **Refus** : l'état courant décide où on va :
      - `CONFIRMATION_COMMANDE` → `ECOUTE`, jamais `INTERPRETATION` ;
      - `CONFIRMATION_ACTION` → `INTERPRETATION`, jamais `ECOUTE`.
   6. **Terminer par un `return`** d'une `Transition` (état atteint plus message à dire),
      construite comme dans les autres méthodes de la classe.

Tests à faire passer : `test_refus_en_confirmation_commande_renvoie_a_ecoute_jamais_a_interpretation`, `test_refus_en_confirmation_action_renvoie_a_interpretation_jamais_a_ecoute`.

## Vérification

- `Select-String -Path code\state_machine.py -Pattern "repondu' a implementer"` ne doit plus rien renvoyer.
- Un échec `NotImplementedError` dans pytest signifie q
