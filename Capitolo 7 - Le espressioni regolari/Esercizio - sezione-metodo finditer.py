import re

testo = "Ciao mondo. Hello world."
pattern = re.compile(r'\b\w+\b')
corrispondenze = pattern.finditer(testo)
if corrispondenze:
    for corrispondenza in corrispondenze:
        print("Corrispondenza trovata:", corrispondenza.group())
else:
    print("Nessuna corrispondenza trovata.")


"""
Corrispondenza trovata: Ciao
Corrispondenza trovata: mondo
Corrispondenza trovata: Hello
Corrispondenza trovata: world
"""