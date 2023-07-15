"""File: DatabaseBuilder.py"""

import os
import sqlite3


class DatabaseBuilder:
    def __init__(self, database_name=None):
        """Costruttore.
        
        Args:
            database_name (str): Il nome del database.
        """
        self.database_name = database_name  # Nome del database
        self.database_rows = []  # Lista per memorizzare le righe del database

    def database_connect(self):
        """Questo metodo stabilisce la connessione al database SQLite."""
        self.connection = sqlite3.connect(self.database_name)  # Connettiti al database
        self.cursor = self.connection.cursor()  # Ottieni un cursore per eseguire query

    def create_table(self, header=None):
        """
        Questo metodo crea una tabella nel database utilizzando un'intestazione specificata.
        L'intestazione contiene i nomi delle colonne e i relativi tipi di dati.
        
        Args:
            header (list): L'intestazione contenente i nomi delle colonne e i relativi tipi di dati.
        """
        # Aggiungi l'estensione ".db" al nome del database se non è presente
        if not self.has_file_extension(self.database_name):
            database = self.database_name + '.db'
        else:
            database = self.database_name

        # Verifica se il database non esiste già
        if not os.path.exists(database):
            try:
                self.connection = sqlite3.connect(database)  # Crea una connessione al database
                self.cursor = self.connection.cursor()  # Ottieni un cursore per eseguire query

                # Costruzione della query CREATE TABLE
                query = f"CREATE TABLE {self.database_name} ("
                for column in header:
                    column_name, column_type = column
                    query += f"{column_name} {column_type},"

                query = query.rstrip(",") + ")"

                # Esecuzione della query
                self.cursor.execute(query)

            except sqlite3.Error as e:
                print("Error connecting to the database:", e)
        else:
            print("Database already exists")
            self.connection = sqlite3.connect(database)  # Connettiti al database esistente
            self.cursor = self.connection.cursor()  # Ottieni un cursore per eseguire query

        # Conferma delle modifiche al database
        self.connection.commit()

    def fetch_all(self):
        """Questo metodo esegue una query SQL per recuperare tutte le righe dal database."""
        # Costruzione della query
        query = "SELECT * FROM {database_name}".format(
            database_name=self.database_name)

        # Esecuzione della query
        self.cursor.execute(query)

        # Memorizzazione delle righe recuperate dal database
        self.database_rows = self.cursor.fetchall()

    def insert_elements(self, elements):
        """
        Questo metodo inserisce gli elementi forniti nel database.
        Se viene fornita una lista di elementi, verifica se ciascun elemento è già presente nel database.
        Se un elemento non è presente, viene inserito nel database utilizzando il metodo insert_element().
        
        Args:
            elements (list or tuple): Gli elementi da inserire nel database.
        """
        # Recupera tutte le righe dal database
        self.fetch_all()

        # Verifica se l'input 'elements' è di tipo list
        if isinstance(elements, list):
            for element in elements:
                # Verifica se l'elemento è già presente nel database
                if element not in self.database_rows:
                    print(f"L'elemento {str(element)} non è presente nel database: aggiungiamolo!")
                    # Inserisce l'elemento nel database utilizzando il metodo insert_element()
                    self.insert_element(element)
                else:
                    print(f"L'elemento {str(element)} è già presente nel database")
        else:
            print('Hai fornito un input di tipo non supportato!')

    def insert_element(self, row_values):
        """Questo metodo inserisce una singola riga di valori nel database.
        
        Args:
            row_values (tuple): I valori della riga da inserire nel database.
        """
        # Verifica se l'input 'elements' è di tipo tuple
        if isinstance(row_values, tuple):
            # Costruzione della query INSERT
            query = "INSERT INTO {} VALUES ({})".format(self.database_name, ",".join(["?"] * len(row_values)))
            # Esecuzione della query INSERT con i valori della riga
            self.cursor.execute(query, row_values)
            # Conferma delle modifiche al database
            self.connection.commit()
        else:
            print('Hai fornito un elemento di tipo non supportato!')

    def has_file_extension(self, filename):
        """
        Questo metodo verifica se una stringa ha un'estensione di file.
        Restituisce True se l'estensione è presente, False altrimenti.
        
        Args:
            filename (str): Il nome del file da controllare.
        
        Returns:
            bool: True se l'estensione è presente, False altrimenti.
        """
        # Controlla se la stringa termina con un'estensione di file
        # Ad esempio, ".db" indica che è presente un'estensione di file
        return '.' in filename and filename.rsplit('.', 1)[1].lower() != 'db'
