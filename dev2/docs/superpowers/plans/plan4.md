# Plan 4

1. Dans `code/trajectory.py`, dans `evaluer`, **supprimer l'instruction
   `raise NotImplementedError(...)` en entier** (toutes ses lignes, parenthèse fermante comprise)
   et la **remplacer par l'implémentation**. Aucun `raise NotImplementedError` ne doit rester
   dans la fonction, et elle ne doit pas se terminer par `pass` ni par un `return None`.
   Suivre son docstring et son commentaire `Indice`.
   Ne pas modifier `test/`.

   1. **Garder le début existant** : `t = float(instant)` puis écrêtage à `0.0` si `t < 0`,
      ainsi que les commentaires `# Indice` / `# Tests`.
   2. **Écrêter aussi par le haut** : `t = min(t, profil.duree_totale)`. Après la fin, le profil
      est « arrivé » : vitesse nulle, position égale à la distance totale. Aucune exception.
   3. **Lire les paramètres du profil** (noms exacts à vérifier dans `ProfilTrapeze`) :
      accélération `a`, vitesse de crête, durée de montée, durée de plateau, durée totale,
      distance totale.
   4. **Trois phases**, selon la valeur de `t` :
      1. **Montée** (`t <= t_montee`) : `v = a·t`, `x = ½·a·t²` ;
      2. **Plateau** (`t_montee < t <= t_montee + t_plateau`) : `v = v_crete`,
         `x = x_montee + v_crete·(t − t_montee)` ;
      3. **Descente** (au-delà) : `τ = duree_totale − t` (temps restant),
         `v = a·τ`, `x = distance_totale − ½·a·τ²`.
   5. **Profil triangulaire** : si le plateau est de durée nulle, le même code doit
      fonctionner sans branche spéciale.
   6. **Terminer par un `return`** d'un `Echantillon` (position parcourue, vitesse), avec les
      champs et l'ordre définis dans sa déclaration.

Tests à faire passer : `test_evaluer_ecrete_avant_le_depart_et_apres_la_fin`, `test_vitesse_nulle_aux_deux_bouts`, `test_vitesse_maximale_respectee`.

## Pièges principaux

- La descente se calcule avec le **temps restant** `τ = duree_totale − t`, pas avec `t`.
- Sans l'écrêtage par le haut, `τ` devient négatif après la fin et la vitesse aussi.
- Si le test de vitesse maximale est strict, borner `v` avec `min(v, v_crete)`.

## Vérification

- `Select-String -Path code\trajectory.py -Pattern "'evaluer' a implementer"` ne doit plus rien renvoyer.
- Un échec `NotImplementedError` dans pytest signifie que le `raise` est toujours là : la modification n'a pas été appliquée.

