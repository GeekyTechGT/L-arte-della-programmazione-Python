try:
    file = open("dati.txt", "r")
    contenuto = file.read()
    print(contenuto)
    file.close()
except FileNotFoundError:
    print("Il file non esiste.")
except PermissionError:
    print("Accesso negato al file.")
