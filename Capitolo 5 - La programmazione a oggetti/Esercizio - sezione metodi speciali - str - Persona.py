class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def __str__(self):
        return f"{self.nome} {self.cognome}, {self.eta} anni"

p = Persona("Mario", "Rossi", 30)
print(p)  # output: "Mario Rossi, 30 anni"
