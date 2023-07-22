import json

# Apertura del file JSON in modalità lettura
with open('dati.json', 'r') as file:
    # Caricamento dei dati JSON
    dati = json.load(file)

    # Accesso ai dati (assicurati dell'esistenza delle chiavi)
    nome = dati['nome']
    età = dati['età']
    indirizzo = dati['indirizzo']
    print(f"nome:  {nome}")
    print(f"età: {età}")
    print(f"indirizzo: {indirizzo}")
