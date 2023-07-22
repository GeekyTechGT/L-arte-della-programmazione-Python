class Automobile:
    # Attributi di classe
    num_ruote = 4
    car_count = 0

    def __init__(self, marca, modello, anno, colore, velocita_max):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.colore = colore
        self.velocita_max = velocita_max
        self.velocita_attuale = 0
        Automobile.car_count += 1
    
    def accelerare(self, velocita):
        if self.velocita_attuale + velocita > self.velocita_max:
            self.velocita_attuale = self.velocita_max
        else:
            self.velocita_attuale += velocita
    
    def frenare(self, velocita):
        if self.velocita_attuale - velocita < 0:
            self.velocita_attuale = 0
        else:
            self.velocita_attuale -= velocita
    
    def accendere_motore(self):
        print(f"{self.marca} {self.modello}: Motore acceso.")
    
    def spegnere_motore(self):
        print(f"{self.marca} {self.modello}: Motore spento.")

    
# Creazione di istanze della classe Automobile
auto1 = Automobile( marca="Fiat", modello="500", \
                    anno=2020,  colore="rosso", velocita_max=200)
auto2 = Automobile( marca="Fiat", modello="Tipo", \
                    anno=2020,  colore="bianco", velocita_max=220)

# Accesso agli attributi di classe
print("Numero di automobili create:", Automobile.car_count) 