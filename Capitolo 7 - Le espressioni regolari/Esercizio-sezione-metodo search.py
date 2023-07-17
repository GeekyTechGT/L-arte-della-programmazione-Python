import re

testo = "La mia email è test@example.com"
pattern = re.compile(r'\w+@\w+\.\w+')
corrispondenza = pattern.search(testo)
if corrispondenza:
    print("Corrispondenza trovata:", corrispondenza.group())
else:
    print("Nessuna corrispondenza trovata.")

#output: Corrispondenza trovata: test@example.com