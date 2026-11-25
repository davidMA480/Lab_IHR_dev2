# Plan 1

1. Dans `code/arcs.py`, remplacer le `raise NotImplementedError` de `echantillonner_arc`
   en suivant son docstring et son commentaire `Indice`.
   Ne pas modifier `test/`.

   1. **Valider les entrées** : `resolution_s > 0`, `duree_etape >= 0`, `tolerance_collision >= 0`
      (`ValueError` sinon). Ne jamais lever à cause d'un obstacle absent.
   2. **Grille de temps par indice** : `t_k = k × resolution_s`, `k = 0..N`,
      `N = floor(duree_etape / resolution_s)`, plus un dernier échantillon à `t = duree_etape`
      si la grille ne le contient pas (pas final plus court). Pas d'accumulation de flottants.
   3. **Échantillon initial** `(0, x0, y0, θ0)` : tester la collision dès ce point.
   4. **Intégration pas à pas** sur chaque `[t_k, t_{k+1}]` :
      - `v = sens_lineaire × profil_lineaire(t_mid)` et `ω = sens_angulaire × profil_angulaire(t_mid)`,
        évalués au milieu de l'intervalle ;
      - si `|ω| > ε` : arc exact (`R = v/ω`, `x += R(sin(θ+ω·dt) − sin θ)`,
        `y −= R(cos(θ+ω·dt) − cos θ)`), sinon ligne droite ;
      - `θ += ω·dt`.
   5. **Test de collision** (seulement si `obstacle is not None`) :
      collision si `distance(pose, centre) <= rayon + tolerance_collision`.
      Tester chaque échantillon de l'arc, pas seulement le point final de l'étape.
   6. **Première collision** : arrêter la boucle dès qu'elle est détectée, conserver les
      échantillons jusqu'à ce point et renvoyer `ResultatArc` avec la collision.
   7. **Sans collision** : renvoyer tous les échantillons et `collision = None`.

Tests à faire passer : `test_arc_dont_le_segment_etait_libre_est_refuse`, `test_arc_entre_dans_l_obstacle_est_detecte`, `test_arc_frole_l_obstacle_sans_le_toucher`.

## Ce que chaque test vérifie

| Test | Comportement attendu | Point du plan |
|------|----------------------|---------------|
| `test_arc_entre_dans_l_obstacle_est_detecte` | L'arc traverse l'obstacle : une collision est renvoyée, c'est la première, les échantillons s'arrêtent là. | étapes 5 et 6 |
| `test_arc_dont_le_segment_etait_libre_est_refuse` | Le segment droit entre départ et arrivée est libre, mais l'arc courbe touche l'obstacle : il faut tester les échantillons de l'arc, pas la corde. | étapes 4 et 5 |
| `test_arc_frole_l_obstacle_sans_le_toucher` | L'arc passe près de l'obstacle sans entrer dans `rayon + tolerance_collision` : aucune collision. Attention au `<=` et à la tolérance. | étape 5 |

## Vérifications avant de lancer

- Relire le commentaire `Indice` dans `echantillonner_arc` : il prime sur ce plan s'il précise une convention (grille de temps, comparaison stricte ou non, forme de `ResultatArc`).
- Lancer d'abord les trois tests ciblés, puis toute la suite pour vérifier qu'aucune régression n'apparaît (sans toucher à `test/`).
- Si le test « frôle » échoue de peu, vérifier d'abord la comparaison (`<=` contre `<`) et l'ajout de `tolerance_collision` au rayon.
