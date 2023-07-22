class Negozio:
    """
    Classe per rappresentare un negozio.
    """

    def __init__(self, nome, categoria):
        """
        Inizializza un nuovo negozio con il nome e la categoria specificati.
        """
        self._nome = nome
        self._categoria = categoria
        self._inventario = {}

    def aggiungi_prodotto(self, nome, quantita, prezzo_unitario):
        """
        Aggiunge un prodotto all'inventario del negozio con il nome, la quantità e il prezzo unitario specificati.
        """
        if nome in self._inventario:
            self._inventario[nome]["quantita"] += quantita
        else:
            self._inventario[nome] = {"quantita": quantita, "prezzo_unitario": prezzo_unitario}

    def rimuovi_prodotto(self, nome, quantita):
        """
        Rimuove una quantità specificata di un prodotto dall'inventario del negozio.
        """
        if nome in self._inventario:
            if self._inventario[nome]["quantita"] >= quantita:
                self._inventario[nome]["quantita"] -= quantita
                if self._inventario[nome]["quantita"] == 0:
                    del self._inventario[nome]
            else:
                print("Quantità insufficiente disponibile per rimuovere il prodotto.")
        else:
            print("Il prodotto non è presente nell'inventario.")

    def ottieni_inventario(self):
        """
        Restituisce l'inventario del negozio.
        """
        return self._inventario

    def calcola_totale_vendite(self):
        """
        Calcola il totale delle vendite effettuate nel negozio.
        """
        totale = 0
        for prodotto, dettagli in self._inventario.items():
            totale += dettagli["quantita"] * dettagli["prezzo_unitario"]
        return totale


class Cliente:
    """
    Classe per rappresentare un cliente di un negozio.
    """

    def __init__(self, nome):
        """
        Inizializza un nuovo cliente con il nome specificato.
        """
        self._nome = nome
        self._carrello = {}

    def aggiungi_al_carrello(self, nome_prodotto, quantita):
        """
        Aggiunge un prodotto al carrello del cliente con il nome e la quantità specificati.
        """
        if nome_prodotto in self._carrello:
            self._carrello[nome_prodotto] += quantita
        else:
            self._carrello[nome_prodotto] = quantita

    def rimuovi_dal_carrello(self, nome_prodotto, quantita):
        """
        Rimuove una quantità specificata di un prodotto dal carrello del cliente.
        """
        if nome_prodotto in self._carrello:
            if self._carrello[nome_prodotto] >= quantita:
                self._carrello[nome_prodotto] -= quantita
                if self._carrello[nome_prodotto] == 0:
                    del self._carrello[nome_prodotto]
            else:
                print("Quantità insufficiente disponibile per rimuovere il prodotto dal carrello.")
        else:
            print("Il prodotto non è presente nel carrello.")

    def ottieni_carrello(self):
        """
        Restituisce il carrello del cliente.
        """
        return self._carrello

    def calcola_totale_acquisto(self, negozio):
        """
        Calcola il totale dell'acquisto del cliente presso il negozio specificato.
        """
        totale = 0
        for prodotto, quantita in self._carrello.items():
            if prodotto in negozio.ottieni_inventario():
                prezzo_unitario = negozio.ottieni_inventario()[prodotto]["prezzo_unitario"]
                totale += quantita * prezzo_unitario
            else:
                print(f"Il prodotto '{prodotto}' non è disponibile nel negozio.")
        return totale


def main():
    # Creazione di un'istanza del negozio
    mio_negozio = Negozio("Supermercato", "Alimentari")

    # Aggiunta di prodotti all'inventario del negozio con prezzo unitario
    mio_negozio.aggiungi_prodotto("Pasta", 10, 2.5)
    mio_negozio.aggiungi_prodotto("Riso", 5, 3.0)
    mio_negozio.aggiungi_prodotto("Latte", 8, 1.5)

    # Creazione di un'istanza del cliente
    io = Cliente("Mario")

    # Aggiunta di prodotti al carrello del cliente
    io.aggiungi_al_carrello("Pasta", 2)
    io.aggiungi_al_carrello("Latte", 3)

    # Rimozione di prodotti dal carrello del cliente
    io.rimuovi_dal_carrello("Pasta", 1)

    # Stampa dell'inventario del negozio
    inventario_negozio = mio_negozio.ottieni_inventario()
    print("Inventario del negozio:")
    for prodotto, dettagli in inventario_negozio.items():
        print(f"{prodotto}: {dettagli['quantita']}, Prezzo Unitario: {dettagli['prezzo_unitario']}")

    # Stampa del carrello del cliente
    carrello_cliente = io.ottieni_carrello()
    print("Carrello del cliente:")
    for prodotto, quantita in carrello_cliente.items():
        print(f"{prodotto}: {quantita}")

    # Calcolo del totale delle vendite del negozio
    totale_vendite = mio_negozio.calcola_totale_vendite()
    print(f"Totale delle vendite del negozio: {totale_vendite}")

    # Calcolo del totale dell'acquisto del cliente
    totale_acquisto = io.calcola_totale_acquisto(mio_negozio)
    print(f"Totale dell'acquisto del cliente: {totale_acquisto}")


if __name__ == "__main__":
    main()