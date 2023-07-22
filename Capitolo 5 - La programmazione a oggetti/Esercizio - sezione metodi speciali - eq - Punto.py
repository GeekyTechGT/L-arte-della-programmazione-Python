class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Punto):
            return self.x == other.x and self.y == other.y
        return False

p1 = Punto(1, 2)
p2 = Punto(1, 2)
p3 = Punto(3, 4)

print(p1 == p2)  # stampa "True"
print(p1 == p3)  # stampa "False"
