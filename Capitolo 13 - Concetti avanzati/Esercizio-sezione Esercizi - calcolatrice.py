class Calcolatrice:
    """
    Classe che rappresenta una calcolatrice.

    Metodi:
    - calcola: esegue un calcolo specifico utilizzando una lambda func-tion.
    """

    def calcola(self, operazione, a, b):
        """
        Esegue un calcolo specifico utilizzando una lambda function.

        Parametri:
        - operazione: una lambda function che rappresenta l'operazione da eseguire.
        - a: il primo operando.
        - b: il secondo operando.

        Ritorna:
        - Il risultato del calcolo.
        """
        return operazione(a, b)
def main():
    """
    Funzione principale che esegue un esempio di utilizzo di lambda function,
    classi e oggetti per eseguire calcoli con una calcolatrice.
    """
    calcolatrice = Calcolatrice()

    # Esempio di calcolo: somma di due numeri
    somma = lambda x, y: x + y
    risultato_somma = calcolatrice.calcola(somma, 5, 3)
    print("Risultato della somma:", risultato_somma)

    # Esempio di calcolo: prodotto di due numeri
    prodotto = lambda x, y: x * y
    risultato_prodotto = calcolatrice.calcola(prodotto, 4, 2)
    print("Risultato del prodotto:", risultato_prodotto)

if __name__ == "__main__":
    main()
