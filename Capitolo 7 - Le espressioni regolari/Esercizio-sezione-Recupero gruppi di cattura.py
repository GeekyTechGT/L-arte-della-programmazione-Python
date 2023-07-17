import re

testo = "Il mio numero di telefono è (+123) 456-7890"
pattern = re.compile(r'\((\+\d+)\) (\d+-\d+)')
corrispondenza = pattern.search(testo)
if corrispondenza:
    indicativo = corrispondenza.group(1)
    numero_locale = corrispondenza.group(2)
    print("Indicativo internazionale:", indicativo)
    print("Numero locale:", numero_locale)
else:
    print("Nessuna corrispondenza trovata.")

"""
output:
Indicativo internazionale: +123
Numero locale: 456-7890
"""