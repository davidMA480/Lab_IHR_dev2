import sys, os
os.chdir(sys.argv[1])
s = open("state_machine.py", encoding="utf-8").read()
CHANGES = [
 ('"Je n\'ai pas compris. R\u00e9pondez par oui ou par non."', '"R\u00e9pondez par oui ou par non."'),
 ('"Je traduis la commande."', '"Commande confirm\u00e9e. Interpr\u00e9tation en cours."'),
 ('"J\'ex\u00e9cute le plan."', '"Plan confirm\u00e9. Ex\u00e9cution."'),
 ('"D\'accord. R\u00e9p\u00e9tez la commande."', '"Commande annul\u00e9e. R\u00e9p\u00e9tez."'),
 ('"D\'accord. Je propose une autre traduction."', '"Plan refus\u00e9. Je propose une autre traduction."'),
]
for old, new in CHANGES:
    n = s.count(old)
    print(n, "x" if n != 1 else "ok", ascii(old)[:50])
    if n == 1:
        s = s.replace(old, new)
open("state_machine.py", "w", encoding="utf-8").write(s)
