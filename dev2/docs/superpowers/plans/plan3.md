# Plan 3

1. Dans `code/state_machine.py`, dans `signer`, **supprimer l'instruction
   `raise NotImplementedError(...)` en entier** (les 3 lignes, parenthèse fermante comprise)
   et la **remplacer par l'implémentation**. Aucun `raise NotImplementedError` ne doit rester
   dans la fonction, et elle ne doit pas se terminer par `pass` ni par un `return None`.
   Suivre son docstring et son commentaire `Indice`.
   Ne pas modifier `test/`.

   1. **Garder** le docstring et les commentaires `# Indice` / `# Tests`.
   2. **Vitesse linéaire** : positive si `is_forward` est vrai, négative sinon.
      `linear = linear_speed if is_forward else -linear_speed`
   3. **Vitesse angulaire** (REP-103 : antihoraire positif, horaire négatif) :
      négative si `is_clockwise` est vrai, positive sinon.
      `angular = -angular_speed if is_clockwise else angular_speed`
   4. **Terminer par** `return linear, angular` (tuple de deux `float`, dans cet ordre).
   5. Ne rien décider d'autre : pas de configuration, pas d'état, pas d'effet de bord.

Tests à faire passer : `test_signer_is_forward_vrai_rend_une_vitesse_lineaire_positive`, `test_signer_is_clockwise_vrai_rend_une_vitesse_angulaire_negative`.

## Piège principal

`is_clockwise` vrai donne un signe **négatif**, alors que `is_forward` vrai donne un signe **positif**.

## Vérification

- `Select-String -Path code\state_machine.py -Pattern "'signer' a implementer"` ne doit plus rien renvoyer.
- Un échec `NotImplementedError` dans pytest signifie que le `raise` est toujours là : la modification n'a pas été appliquée.
