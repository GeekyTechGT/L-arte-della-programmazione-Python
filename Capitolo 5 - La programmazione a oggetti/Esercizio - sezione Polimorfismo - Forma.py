class Forma:
    def calcola_area(self):
        pass

class Rettangolo(Forma):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
    
    def calcola_area(self):
        return self.base * self.altezza

class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio
    
    def calcola_area(self):
        return 3.14159 * self.raggio**2

def stampa_area(forma):
    print("L'area è:", forma.calcola_area())

rettangolo = Rettangolo(5, 3)
cerchio = Cerchio(4)

stampa_area(rettangolo)  # Stampa "L'area è: 15"
stampa_area(cerchio)    # Stampa "L'area è: 50.26544"


class Triangolo(Forma):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def calcola_area(self):
        return (self.base * self.altezza) / 2


triangolo = Triangolo(4, 8)
stampa_area(triangolo)    # Stampa "L'area è: 16"

