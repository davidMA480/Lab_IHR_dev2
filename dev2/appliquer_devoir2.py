import re, sys, os
os.chdir(sys.argv[1])
IMPL = {
"arcs.py": '''    x, y, theta = (float(c) for c in pose_depart)
    nb_pas = math.ceil(duree_etape / resolution_s - 1e-9)
    echantillons = []
    for k in range(nb_pas + 1):
        instant = min(k * resolution_s, duree_etape)
        # Collision testee AVANT le pas : on n'integre jamais au-dela d'un impact.
        if _en_collision(x, y, obstacle, tolerance_collision):
            return ResultatArc(tuple(echantillons), Collision(instant, x, y))
        echantillons.append(EchantillonArc(instant, x, y, theta))
        if k == nb_pas:
            break
        dt = min((k + 1) * resolution_s, duree_etape) - instant
        v = sens_lineaire * evaluer(profil_lineaire, instant).vitesse
        w = sens_angulaire * evaluer(profil_angulaire, instant).vitesse
        x += v * math.cos(theta) * dt
        y += v * math.sin(theta) * dt
        theta += w * dt
    return ResultatArc(tuple(echantillons), None)
''',
"trajectory.py": '''    if t > profil.duree_totale:
        t = profil.duree_totale
    if profil.duree_totale <= 0.0:
        return Echantillon(position=profil.distance, vitesse=0.0)
    a = profil.acceleration
    crete = profil.vitesse_crete
    fin_montee = profil.duree_montee
    fin_plateau = profil.duree_montee + profil.duree_plateau
    if t <= fin_montee:
        vitesse = min(a * t, crete)
        position = 0.5 * a * t * t
    elif t <= fin_plateau:
        vitesse = crete
        position = 0.5 * a * fin_montee ** 2 + crete * (t - fin_montee)
    else:
        restant = profil.duree_totale - t
        vitesse = min(a * restant, crete)
        position = profil.distance - 0.5 * a * restant * restant
    return Echantillon(position=position, vitesse=vitesse)
''',
}
STATE_REPONDU = '''        reponse = interpreter_reponse(texte, self.mots_accord, self.mots_refus, self.mots_sortie)
        # SORTIE d'abord : "non, quitter" doit quitter, pas refuser.
        if reponse is Reponse.SORTIE:
            return self._aller(Etat.ARRET, "Mot de sortie entendu. Au revoir.")
        # INDECIS ensuite : on reste dans l'etat courant et on repose la question.
        if reponse is Reponse.INDECIS:
            return self._aller(self.etat, "Je n'ai pas compris. R\u00e9pondez par oui ou par non.")
        en_commande = self.etat is Etat.CONFIRMATION_COMMANDE
        if reponse is Reponse.ACCORD:
            if en_commande:
                return self._aller(Etat.INTERPRETATION, "Je traduis la commande.")
            return self._aller(Etat.EXECUTION, "J'ex\u00e9cute le plan.")
        # REFUS : c'est l'ETAT COURANT qui decide ou il mene.
        if en_commande:
            self.commande = ""
            return self._aller(Etat.ECOUTE, "D'accord. R\u00e9p\u00e9tez la commande.")
        self.plan = None
        return self._aller(Etat.INTERPRETATION, "D'accord. Je propose une autre traduction.")
'''
STATE_SIGNER = '''    linear = abs(linear_speed) if is_forward else -abs(linear_speed)
    angular = -abs(angular_speed) if is_clockwise else abs(angular_speed)
    return linear, angular
'''
PAT = r'^[ ]*# Indice.*?\n[ ]*# Tests.*?\n[ ]*raise NotImplementedError\((?:.|\n)*?\n[ ]*\)\n'
for fn, impl in IMPL.items():
    s = open(fn, encoding="utf-8").read()
    m = re.search(PAT, s, re.M)
    print(fn, bool(m))
    s = s[:m.start()] + impl + s[m.end():]
    open(fn, "w", encoding="utf-8").write(s)
s = open("state_machine.py", encoding="utf-8").read()
ms = list(re.finditer(PAT, s, re.M))
print("state_machine stubs", len(ms))
for m, rep in reversed(list(zip(ms, [STATE_REPONDU, STATE_SIGNER]))):
    s = s[:m.start()] + rep + s[m.end():]
open("state_machine.py", "w", encoding="utf-8").write(s)
d = open("dialogue_manager_node.py", encoding="utf-8").read()
old = "from state_machine import Action, Etat, MachineDialogue, Plan, action_depuis_config"
if old in d:
    d = d.replace(old, "from state_machine import Action, Etat, MachineDialogue, Plan, Transition, action_depuis_config")
    open("dialogue_manager_node.py", "w", encoding="utf-8").write(d)
    print("import Transition ajoute")
else:
    print("import deja corrige ou introuvable")
