import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "code"))
from state_machine import signer, MachineDialogue, Etat
import trajectory, arcs

print("=== signer(1.0, 1.0, is_forward, is_clockwise) ===")
for fwd in (True, False):
    for cw in (False, True):
        print(f"  avance={fwd!s:5}  horaire={cw!s:5}  ->  (lineaire, angulaire) = {signer(1.0, 1.0, fwd, cw)}")

print("\n=== evaluer : profil trapezoidal, distance 2 m en 1 s ===")
p = trajectory.calculer_profil(distance=2.0, temps_total=1.0, acceleration_max=16.0, vitesse_max=3.0)
print(f"  montee {p.duree_montee:.3f} s | plateau {p.duree_plateau:.3f} s | crete {p.vitesse_crete:.3f} m/s")
for t in (-0.5, 0.0, 0.07, 0.3, 0.5, 0.9, 0.97, 1.0, 1.5):
    e = trajectory.evaluer(p, t)
    print(f"  t={t:5.2f} s   position={e.position:6.3f} m   vitesse={e.vitesse:6.3f} m/s")

print("\n=== echantillonner_arc : 2 m + virage de 60 deg en 1 s ===")
pl = trajectory.calculer_profil(distance=2.0, temps_total=1.0, acceleration_max=16.0, vitesse_max=3.0)
pa = trajectory.calculer_profil(distance=math.radians(60), temps_total=1.0, acceleration_max=16.0, vitesse_max=2.4)
r = arcs.echantillonner_arc((0.0, 0.0, 0.0), pl, 1.0, pa, 1.0, 1.0, 0.02, None, 0.1)
fin = r.echantillons[-1]
print(f"  sans obstacle : {len(r.echantillons)} echantillons, collision={r.collision}")
print(f"  pose finale   : x={fin.x:.3f}  y={fin.y:.3f}  theta={math.degrees(fin.theta):.1f} deg")
r2 = arcs.echantillonner_arc((0.0, 0.0, 0.0), pl, 1.0, pa, -1.0, 1.0, 0.02, None, 0.1)
print(f"  virage horaire : y final={r2.echantillons[-1].y:.3f} (negatif = a droite)")
obs = arcs.Obstacle(x=1.0, y=0.0, rayon=0.2)
pz = trajectory.calculer_profil(distance=0.0, temps_total=1.0, acceleration_max=16.0, vitesse_max=2.4)
r3 = arcs.echantillonner_arc((0.0, 0.0, 0.0), pl, 1.0, pz, 1.0, 1.0, 0.02, obs, 0.1)
c = r3.collision
print(f"  obstacle en (1.0, 0.0) rayon 0.2 : collision a t={c.instant:.2f} s, x={c.x:.3f}  ({len(r3.echantillons)} echantillons avant l'impact)")

print("\n=== repondu : dialogue de confirmation ===")
def machine():
    return MachineDialogue(mots_accord=["oui", "d'accord"], mots_refus=["non"], mots_sortie=["quitter"])
for reponse in ("oui", "non", "peut-etre", "non, quitter"):
    m = machine(); m.entendu("avance")
    t = m.repondu(reponse)
    print(f"  confirmation de COMMANDE, reponse {reponse!r:15} -> {m.etat.value:22} | {t.message}")
