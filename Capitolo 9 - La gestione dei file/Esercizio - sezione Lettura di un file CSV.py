import csv

# Apertura del file CSV in modalità lettura
with open('dati.csv', 'r') as file:
    # Creazione dell'oggetto reader CSV
    reader = csv.reader(file)

    # Iterazione sulle righe del file CSV
    for riga in reader:
        # Processa la riga
        print(riga)
