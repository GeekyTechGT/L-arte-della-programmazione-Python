class Libro:
    """
    Classe per rappresentare un libro.
    """

    def __init__(self, titolo, autore, anno_pubblicazione):
        """
        Inizializza un nuovo oggetto Libro con il titolo, l'autore e l'anno di pubblicazione specificati.

        Args:
            titolo (str): Il titolo del libro.
            autore (str): L'autore del libro.
            anno_pubblicazione (int): L'anno di pubblicazione del libro.
        """
        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione

    def __str__(self):
        """
        Restituisce una rappresentazione in formato stringa del libro.

        Returns:
            str: La stringa che rappresenta il libro nel formato "Titolo di Autore (Anno di pubblicazione)".
        """
        return f"{self.titolo} di {self.autore} ({self.anno_pubblicazione})"

inventario = []
dizionario_libri = {}
insieme_autori = set()
coda_vendite = []

# Aggiungiamo alcuni libri all'inventario
libro1 = Libro("Il signore degli anelli", "J.R.R. Tolkien", 1954)
libro2 = Libro("Harry Potter e la pietra filosofale", \
               "J.K. Rowling", 1997)
libro3 = Libro("1984", "George Orwell", 1949)

inventario.append(libro1)
inventario.append(libro2)
inventario.append(libro3)

# Aggiungiamo i libri al dizionario dei libri utilizzando 
# il titolo come chiave
dizionario_libri[libro1.titolo] = libro1
dizionario_libri[libro2.titolo] = libro2
dizionario_libri[libro3.titolo] = libro3

# Aggiungiamo gli autori all'insieme degli autori
insieme_autori.add(libro1.autore)
insieme_autori.add(libro2.autore)
insieme_autori.add(libro3.autore)

# Aggiungiamo una vendita alla coda delle vendite
coda_vendite.append(libro1)
coda_vendite.append(libro2)

# Stampiamo l'inventario dei libri
print("Inventario:")
for libro in inventario:
    print(libro)

# Stampiamo i libri nel dizionario dei libri
print("Dizionario dei libri:")
for libro in dizionario_libri.values():
    print(libro)

# Stampiamo gli autori
print("Autori:")
for autore in insieme_autori:
    print(autore)

# Effettuiamo la vendita di un libro dalla coda delle vendite
libro_venduto = coda_vendite.pop(0)
print("Libro venduto:", libro_venduto)

# Aggiorniamo l'inventario dopo la vendita
inventario.remove(libro_venduto)

# Verifichiamo l'aggiornamento dell'inventario
print("Nuovo inventario:")
for libro in inventario:
    print(libro)
