class Contatore:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        print(f"Il contatore è stato chiamato {self.count} volte.")

# Creazione di un'istanza della classe Contatore
counter = Contatore()

# Chiamata dell'istanza come se fosse una funzione
counter()  # Output: Il contatore è stato chiamato 1 volta.
counter()  # Output: Il contatore è stato chiamato 2 volte.
counter()  # Output: Il contatore è stato chiamato 3 volte.
