class ValoreNonValidoError(Exception):
    """Eccezione personalizzata per un valore non valido."""

    def __init__(self, messaggio):
        self.messaggio = messaggio
        super().__init__(self.messaggio)

    def __str__(self):
        return f"ValoreNonValidoError: {self.messaggio}"

def controlla_valore(valore):
    if valore < 0:
        raise ValoreNonValidoError("Il valore non può essere negativo.")

# Esempio di utilizzo
try:
    valore_input = int(input("Inserisci un valore positivo: "))
    controlla_valore(valore_input)
    print("Valore valido!")
except ValoreNonValidoError as e:
    print(f"Errore: {e}")
