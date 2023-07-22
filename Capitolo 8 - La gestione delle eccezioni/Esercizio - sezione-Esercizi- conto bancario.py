class SaldoInsufficienteError(Exception):
    """Eccezione personalizzata per fondi insufficienti sul conto."""

    def __init__(self, saldo, importo):
        self.saldo = saldo
        self.importo = importo

    def __str__(self):
        return f"Saldo insufficiente! Saldo disponibile: {self.saldo}, Importo richiesto: {self.importo}"


class ImportoNonValidoError(Exception):
    """Eccezione personalizzata per importo di deposito o prelievo non valido."""

    def __init__(self, importo):
        self.importo = importo

    def __str__(self):
        return f"Importo non valido! Importo richiesto: {self.importo}"


class BankAccount:
    """
    Classe che rappresenta un conto bancario.
    """

    def __init__(self, saldo_iniziale=0):
        self.saldo = saldo_iniziale

    def deposito(self, importo):
        """
        Deposita l'importo specificato sul conto.
        Solleva ImportoNonValidoError se l'importo non è positivo.
        """

        if importo <= 0:
            raise ImportoNonValidoError(importo)

        self.saldo += importo
        print(f"Depositati {importo}. Nuovo saldo: {self.saldo}")

    def prelievo(self, importo):
        """
        Preleva l'importo specificato dal conto.
        Solleva ImportoNonValidoError se l'importo non è positivo.
        Solleva SaldoInsufficienteError se il saldo è inferiore all'importo richiesto.
        """

        if importo <= 0:
            raise ImportoNonValidoError(importo)

        if importo > self.saldo:
            raise SaldoInsufficienteError(self.saldo, importo)

        self.saldo -= importo
        print(f"Prelievo di {importo}. Nuovo saldo: {self.saldo}")


# Test del programma
conto = BankAccount(100)

try:
    conto.deposito(-50)
except ImportoNonValidoError as e:
    print(e)

try:
    conto.prelievo(200)
except SaldoInsufficienteError as e:
    print(e)

try:
    conto.prelievo(50)
except SaldoInsufficienteError as e:
    print(e)
except ImportoNonValidoError as e:
    print(e)




