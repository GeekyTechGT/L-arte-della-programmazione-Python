name = "Bob"
age = 30
message = f"Ciao, mi chiamo {name} e ho {age} anni."
print(message)  # Output: "Ciao, mi chiamo Bob e ho 30 anni."

name = "Alice"
age = 25

# Calcoli all'interno delle parentesi
message = f"Il mio nome è {name.upper()} e tra 10 anni avrò {age + 10} anni."

print(message)  #output: Il mio nome è ALICE e tra 10 anni avrò 35 anni.

# Chiamate di funzioni all'interno delle parentesi
def double(x):
    return x * 2

number = 5
result = f"Il doppio di {number} è {double(number)}."
print(result)  #output: Il doppio di 5 è 10.
