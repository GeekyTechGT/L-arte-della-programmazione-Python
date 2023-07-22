import re

testo = "Questo è un test con numeri: 123 e 456"
pattern = re.compile(r'\d+')
corrispondenze = pattern.findall(testo)
if corrispondenze:
    print("Corrispondenze trovate:", corrispondenze)
else:
    print("Nessuna corrispondenza trovata.")

#output: Corrispondenze trovate: ['123', '456']