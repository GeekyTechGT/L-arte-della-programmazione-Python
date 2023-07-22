import re

testo = "ciao ciao"
pattern = re.compile(r'(\b\w+\b) \1')
corrispondenza = pattern.search(testo)
if corrispondenza:
    parola_duplicata = corrispondenza.group()
    print("Parola duplicata trovata:", parola_duplicata)
else:
    print("Nessuna parola duplicata trovata.")

#output: Parola duplicata trovata: ciao ciao