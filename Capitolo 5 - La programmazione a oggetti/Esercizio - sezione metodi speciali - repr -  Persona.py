class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def __str__(self):
        return f"{self.nome} {self.cognome}, {self.eta} anni"

    def __repr__(self):
        return f"Persona('{self.nome}', '{self.cognome}', {self.eta})"

p = Persona("Mario", "Rossi", 30)
print(repr(p))  # stampa "Persona('Mario', 'Rossi', 30)"

p1 = repr(p)
print(p1)      # stampa "Persona('Mario', 'Rossi', 30)"
