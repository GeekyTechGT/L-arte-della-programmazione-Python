import csv

nome_file = "dati.csv"
delimitatore = ","
quoting = csv.QUOTE_ALL  # o csv.QUOTE_MINIMAL, 
                         # csv.QUOTE_NONNUMERIC, csv.QUOTE_NONE

with open(nome_file, "r") as file_csv:
    lettore_csv = csv.reader(file_csv, delimiter=delimitatore, \
                             quoting=quoting)
    for riga in lettore_csv:
        print(riga)




with open(nome_file, "r") as file_csv:
    lettore_csv = csv.reader(file_csv)
    
    # Lettura dell'header
    header = next(lettore_csv)
    print("Header:", header)
    
    # Lettura della prossima riga
    riga = next(lettore_csv)
    print("Prossima riga:", riga)
