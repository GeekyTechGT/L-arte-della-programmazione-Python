import json

# Dati da scrivere nel file JSON
dati = {
    'nome': 'Mario Rossi',
    'età': 30,
    'indirizzo': 'Via Roma 123'
}

# Apertura del file JSON in modalità scrittura
with open('output.json', 'w') as file:
    # Scrittura dei dati JSON
    json.dump(dati, file)

