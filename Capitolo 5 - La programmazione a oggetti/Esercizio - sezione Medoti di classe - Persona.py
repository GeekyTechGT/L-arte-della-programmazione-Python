
class Persona:
    # Attributo di classe
    popolazione = 0

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        Persona.popolazione += 1

    def nome_completo(self):
        return f"{self.nome} {self.cognome}"

    @classmethod
    def resetta_popolazione(cls):
        cls.popolazione = 0

    @classmethod
    def da_stringa(cls, stringa):
        nome, cognome = stringa.split()
        return cls(nome, cognome)

# Creazione di istanze della classe Persona
persona1 = Persona("Mario", "Rossi")
persona2 = Persona("Luca", "Bianchi")

# Accesso all'attributo di classe
print("Popolazione:", Persona.popolazione)

# Utilizzo del metodo di classe per reimpostare la popolazione
Persona.resetta_popolazione()
print("Popolazione dopo il reset:", Persona.popolazione)

# Utilizzo del metodo di classe per creare un'istanza dalla stringa
persona3 = Persona.da_stringa("Giuseppe Verdi")
print("Nome completo della persona3:", persona3.nome_completo())
