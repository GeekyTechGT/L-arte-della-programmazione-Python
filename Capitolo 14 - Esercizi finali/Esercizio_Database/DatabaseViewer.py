"""File: DatabaseViewer.py"""

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTableView, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase


class DataBaseViewer(QMainWindow):
    def __init__(self, database_name=None):
        """Costruttore.

        Args:
            database_name (str): Il nome del database.
        """
        super().__init__()
        try:
            # Attributi
            self.database_name = database_name

            # Imposta l'icona della finestra
            self.setWindowIcon(QIcon("img/database.png"))

            # Imposta il titolo della finestra
            self.setWindowTitle("DataBase")

            # Imposta la geometria della finestra
            self.setGeometry(1000, 1000, 3000, 1000)

            # Crea un widget centrale
            self.central_widget = QWidget(self)

            # Crea un layout verticale per il widget centrale
            layout = QVBoxLayout(self.central_widget)

            # Crea il QTableView
            self.table_view = QTableView()

            # Aggiungi il QTableView al layout
            layout.addWidget(self.table_view)

            # Imposta il widget centrale come widget centrale della finestra
            self.setCentralWidget(self.central_widget)
        except:
            print("Errore identificato durante l'inizializzazione dell'oggetto!")
            return

    def set_database_name(self, name):
        """
        Questo metodo imposta il nome del database utilizzato dall'applicazione.

        Args:
            name (str): Il nome del database da impostare.
        """
        self.database_name = name

    def get_database_name(self):
        """
        Questo metodo restituisce il nome del database utilizzato dall'applicazione.

        Returns:
            str: Il nome del database.
        """
        return self.database_name

    def move_to_middle_of_screen(self):
        """
        Questo metodo permette di spostare la finestra principale nel centro del desktop.
        Recupera le dimensioni dello schermo e della finestra, dopodiché calcola la posizione in cui centrare la finestra.
        """
        # Ottiene il desktop dell'applicazione
        desktop = QApplication.desktop()

        # Ottiene la geometria dello schermo
        screen_rect = desktop.screenGeometry()

        # Ottiene la geometria della finestra
        window_rect = self.geometry()

        # Calcola la posizione (x,y) per il centro
        x = (screen_rect.width() - window_rect.width()) // 2
        y = (screen_rect.height() - window_rect.height()) // 2

        # Sposta la finestra nella posizione calcolata
        self.move(x, y)

    def add_database(self):
        """
        Questo metodo aggiunge un database SQLite alla finestra principale.
        Viene utilizzato il driver QSQLITE per creare un'istanza di QSqlDatabase
        e viene impostato il nome del database. Successivamente, il database viene aperto.
        """
        # Crea un'istanza di QSqlDatabase con il driver QSQLITE
        self.db = QSqlDatabase.addDatabase("QSQLITE")

        # Imposta il nome del database
        self.db.setDatabaseName(self.database_name)

        # Apre il database
        self.db.open()

    def create_model(self):
        """
        Questo metodo crea un modello QSqlTableModel e visualizza i dati all'interno di un QTableView.
        Il modello viene collegato al database self.db e la tabella viene impostata come il nome del database senza estensione.
        Successivamente, il modello viene selezionato per ottenere i dati dalla tabella.
        Infine, viene creato un'istanza di QTableView e il modello viene impostato come modello per la visualizzazione.
        """
        # Crea un'istanza di QSqlTableModel con il database self.db
        self.model = QSqlTableModel(None, self.db)

        # Imposta la tabella del modello come il nome del database senza estensione
        self.model.setTable(self.database_name.replace('.db', ''))

        # Seleziona il modello per ottenere i dati dalla tabella
        self.model.select()

        # Crea un'istanza di QTableView
        self.table_view = QTableView()

        # Imposta il modello come modello per la visualizzazione nel QTableView
        self.table_view.setModel(self.model)

    def print_model_content(self):
        """
        Questo metodo stampa i contenuti del modello QSqlTableModel.
        Itera su ogni cella del modello e stampa il dato contenuto.
        """
        # Ottiene il numero di righe e colonne del modello
        row_count = self.model.rowCount()
        column_count = self.model.columnCount()
        for row in range(row_count):
            for column in range(column_count):
                # Ottiene l'indice per una specifica cella nel modello
                index = self.model.index(row, column)
                # Ottiene il dato nella cella corrispondente all'indice
                data = self.model.data(index)
                # Stampa il dato
                print(data)

    def add_table_to_window(self):
        """
        Questo metodo aggiunge la vista tabellare QTableView come widget centrale della finestra principale
        e ne imposta le proprietà.
        """
        # Imposta la vista tabellare come widget centrale della finestra principale
        self.setCentralWidget(self.table_view)

        # Imposta le proprietà della vista tabellare
        self.set_table_properties()

    def set_table_properties(self):
        """
        Questo metodo imposta le proprietà della vista tabellare QTableView.
        Vengono impostate le etichette degli headers, lo stile degli headers, l'estensione dell'ultimo header,
        il comportamento di modifica, il comportamento di selezione delle righe, la modalità di scorrimento verticale
        e le dimensioni della vista tabellare.
        """
        # Imposta le etichette degli header con uno stile specifico
        self.table_view.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: lightblue; font-weight: bold; }")
        self.table_view.verticalHeader().setStyleSheet("QHeaderView::section { background-color: lightblue; font-weight: bold; }")

        # Imposta l'estensione dell'ultimo header
        self.table_view.horizontalHeader().setStretchLastSection(True)

        # Imposta il comportamento di modifica della vista tabellare a NoEditTriggers (disabilita la modifica)
        self.table_view.setEditTriggers(QTableView.NoEditTriggers)

        # Imposta il comportamento di selezione delle righe della vista tabellare a SelectRows (seleziona intere righe)
        self.table_view.setSelectionBehavior(QTableView.SelectRows)

        # Imposta la modalità di selezione della vista tabellare a SingleSelection (seleziona una singola riga alla volta)
       
