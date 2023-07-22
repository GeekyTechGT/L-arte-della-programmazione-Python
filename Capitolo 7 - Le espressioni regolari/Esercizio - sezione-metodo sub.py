import re

testo = "Ciao mondo. Hello world."
pattern = re.compile(r'Hello')
nuovo_testo = pattern.sub("Hi", testo)
print("Nuovo testo:", nuovo_testo)

#output: Nuovo testo: Ciao mondo. Hi world.