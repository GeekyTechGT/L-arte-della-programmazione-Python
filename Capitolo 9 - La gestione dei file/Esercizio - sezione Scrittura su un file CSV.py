import csv

# Dati da scrivere nel file CSV
dati = [
    ['Nome', 'Cognome', 'Età'],
    ['Mario', 'Rossi', 25],
    ['Laura', 'Verdi', 30]
]

# Apertura del file CSV in modalità scrittura
with open('output.csv', 'w', newline='') as file:
    # Creazione dell'oggetto writer CSV
    writer = csv.writer(file)

    # Scrittura dei dati nel file CSV
    writer.writerows(dati)
