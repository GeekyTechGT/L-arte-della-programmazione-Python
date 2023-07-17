import re

pattern = re.compile(r'\d{2}-\d{2}-\d{4}')


testo = "La data di oggi è 10-07-2023"

corrispondenza = pattern.search(testo)
if corrispondenza:
    print("Data trovata:", corrispondenza.group())
else:
    print("Nessuna data trovata.")

#output: Data trovata: 10-07-2023