import re

testo = "Ciao, come stai?"
pattern = re.compile(r'Ciao')
corrispondenza = pattern.match(testo)
if corrispondenza:
    print("Corrispondenza trovata:", corrispondenza.group())
else:
    print("Nessuna corrispondenza trovata.")

#output: Corrispondenza trovata: Ciao