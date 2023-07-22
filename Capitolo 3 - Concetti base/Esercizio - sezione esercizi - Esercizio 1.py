def stampa_numeri(n):
	"""
	Stampa i numeri da 1 a n.
	
	Args:
		n (int): Limite superiore dei numeri da stampare.
	"""
	print("Numeri da 1 a", n)
	i = 1
	while i <= n:
		print(i)
		i += 1

def stampa_numeri_pari(n):
	"""
	Stampa i numeri pari da 1 a n.
	
	Args:
		n (int): Limite superiore dei numeri da stampare.
	"""
	print("Numeri pari da 1 a", n)
	for i in range(1, n+1):
		if i % 2 == 0:
			print(i)

def calcola_fattoriale(n):
	"""
	Calcola il fattoriale di un numero.
	
	Args:
		n (int): Numero intero positivo.
	
	Returns:
		int: Il fattoriale del numero n.
	"""
	fattoriale = 1
	for i in range(1, n+1):
		fattoriale *= i
	return fattoriale


# Esempio di utilizzo delle funzioni

# Utilizzo del ciclo while
stampa_numeri(5)
print()

# Utilizzo del ciclo for e dell'istruzione if-else
stampa_numeri_pari(10)
print()

# Utilizzo del ciclo for e calcolo del fattoriale
numero = 6
risultato = calcola_fattoriale(numero)
print("Il fattoriale di", numero, "è", risultato)
