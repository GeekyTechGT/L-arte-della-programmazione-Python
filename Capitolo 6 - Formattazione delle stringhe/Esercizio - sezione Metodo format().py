name = "Alice"
age = 25
message = "Ciao, mi chiamo {} e ho {} anni.".format(name, age)
print(message) #Output: "Ciao, mi chiamo Alice e ho 25 anni."


pi = 3.14159265359
# Formattazione con 2 decimali
formatted_pi = "Valore di pi: {:.2f}".format(pi)
print(formatted_pi)  #output: Valore di pi: 3.14
# Formattazione con 4 decimali
formatted_pi = "Valore di pi: {:.4f}".format(pi)
print(formatted_pi)  #output: Valore di pi: 3.1416


# Allineamento a sinistra
print("Nome: {:<10} Età: {}".format(name, age))
# Allineamento a destra
print("Nome: {:>10} Età: {}".format(name, age))
# Allineamento centrato
print("Nome: {:^10} Età: {}".format(name, age))


# Indicizzazione degli argomenti
message = "Il mio nome è {0} e ho {1} anni.".format(name, age)
print(message)  #output: Il mio nome è Alice e ho 25 anni.
# Ripetizione degli argomenti
message = "Il mio nome è {0} e ho {1} anni. {0} è un bel nome!".format(\
name, age)
print(message)  #output: Il mio nome è Alice e ho 25 anni. Alice è un bel nome!
