class Veicolo:
    """
    Classe per rappresentare un veicolo.
    """

    def __init__(self, targa, marca, modello, anno, tipo):
        """
        Inizializza un nuovo oggetto Veicolo con la targa, la marca, il modello, l'anno di produzione e il tipo specificati.

        Args:
            targa (str): La targa del veicolo.
            marca (str): La marca del veicolo.
            modello (str): Il modello del veicolo.
            anno (int): L'anno di produzione del veicolo.
            tipo (str): Il tipo di veicolo.
        """
        self.targa = targa
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.tipo = tipo

    def informazioni(self):
        """
        Restituisce una stringa con le informazioni del veicolo.

        Returns:
            str: Le informazioni del veicolo nel formato "Marca Modello (Anno), Tipo: TipoVeicolo".
        """
        return f"{self.marca} {self.modello} ({self.anno}), Tipo: {self.tipo}"


class Flotta:
    """
    Classe per rappresentare una flotta di veicoli.
    """

    def __init__(self):
        """
        Inizializza un nuovo oggetto Flotta con una lista vuota di veicoli.
        """
        self.veicoli = []

    def aggiungi_veicolo(self, veicolo):
        """
        Aggiunge un veicolo alla flotta.

        Args:
            veicolo (Veicolo): Il veicolo da aggiungere alla flotta.
        """
        self.veicoli.append(veicolo)

    def rimuovi_veicolo(self, targa):
        """
        Rimuove un veicolo dalla flotta in base alla targa.

        Args:
            targa (str): La targa del veicolo da rimuovere.
        """
        for veicolo in self.veicoli:
            if veicolo.targa == targa:
                self.veicoli.remove(veicolo)
                break

    def elenco_veicoli(self):
        """
        Stampa l'elenco dei veicoli nella flotta, mostrando le informazioni di ciascun veicolo.
        """
        for veicolo in self.veicoli:
            print(veicolo.informazioni())
            
# Creiamo la flotta di veicoli
flotta = Flotta()

# Aggiungiamo alcuni veicoli alla flotta
autobus1 = Veicolo("AB123CD", "Mercedes", "Tourismo", 2015, "Autobus")
camion1 = Veicolo("XY789ZA", "Scania", "R500", 2018, "Camion")
auto1 = Veicolo("EF456GH", "Toyota", "Corolla", 2020, "Auto")

flotta.aggiungi_veicolo(autobus1)
flotta.aggiungi_veicolo(camion1)
flotta.aggiungi_veicolo(auto1)

# Stampiamo l'elenco dei veicoli nella flotta
print("Elenco veicoli:")
flotta.elenco_veicoli()

# Rimuoviamo un veicolo dalla flotta
flotta.rimuovi_veicolo("XY789ZA")

# Stampiamo nuovamente l'elenco dei veicoli nella flotta
print("Nuovo elenco veicoli:")
flotta.elenco_veicoli()
