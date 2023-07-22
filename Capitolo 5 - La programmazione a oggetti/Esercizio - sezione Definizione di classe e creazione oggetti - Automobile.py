class Automobile:
    def __init__(self, marca, modello, anno, colore, velocita_max):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.colore = colore
        self.velocita_max = velocita_max
        self.velocita_attuale = 0
    
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


# Esempio di utilizzo delle classe Automobile

mia_auto = Automobile(marca="Ford", modello="Mustang", anno=2022, colore='rosso', velocita_max=260)
print(mia_auto.marca)  #output: Ford
mia_auto.accendere_motore()