class Persona:
    def __init__(self, nome, età):
        self._nome = nome
        self._età = età

    def get_nome(self):
        return self._nome

    def set_nome(self, nuovo_nome):
        self._nome = nuovo_nome

    def get_età(self):
        return self._età

    def set_età(self, nuova_età):
        if nuova_età > 0:
            self._età = nuova_età

# Creazione di un'istanza della classe Persona
persona = Persona("Mario", 30)

# Utilizzo dei metodi getter e setter
print(persona.get_nome())  # Output: "Mario"
persona.set_nome("Luigi")
print(persona.get_nome())  # Output: "Luigi"

print(persona.get_età())  # Output: 30
persona.set_età(35)
print(persona.get_età())  # Output: 35
persona.set_età(-5)  # La chiamata a set_età() non modificherà l'età perché il valore è negativo
print(persona.get_età())  # Output: 35
