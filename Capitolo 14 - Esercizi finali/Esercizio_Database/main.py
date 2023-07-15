"""File: main.py"""

# Importa i moduli
import sys  
import json  
from PyQt5.QtWidgets import QApplication
from DatabaseBuilder import DatabaseBuilder
from DatabaseViewer import DataBaseViewer

if __name__ == "__main__":
    app = QApplication([])

    # Leggi dati anagrafici da file (.json)
    filename = './dati/dati_anagrafici.json'
    elements = []
    with open(filename, "r") as f:
        # Carica il contenuto del file JSON
        dati_anagrafici = json.load(f)
        for element in dati_anagrafici:
            elements.append(tuple(element.values()))
   
    database_name = 'dati_anagrafici'
    database = database_name + '.db'

    # Crea database
    instance_db_builder = DatabaseBuilder(database_name)
    # Creo l'header del database (partendo dalle chiavi del dizionario dei dati)
    header = []
    for key in dati_anagrafici[0].keys():
        print(key)
        header.append((key,'TEXT'))
    instance_db_builder.create_table(header)
    instance_db_builder.insert_elements(elements)

    # Visualizza database
    window = DataBaseViewer(database) 
    window.add_database()
    window.create_model()
    window.add_table_to_window()
    window.move_to_middle_of_screen()
    window.show()  
    sys.exit(app.exec_())
    

        
