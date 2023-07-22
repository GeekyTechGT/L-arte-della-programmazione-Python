# Classe genitore
class Animale:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età
    
    def fare_rumore(self):
        print("L'animale sta facendo rumore.")

# Classe figlia
class Cane(Animale):
    def __init__(self, nome, eta, razza):
        super().__init__(nome, eta)
        self.razza = razza
    
    def fare_rumore(self):
        print("Il cane sta abbaiando.")

mio_cane = Cane(nome="Fido", eta=3, razza="Labrador")

print(mio_cane.nome)   #output: Fido
