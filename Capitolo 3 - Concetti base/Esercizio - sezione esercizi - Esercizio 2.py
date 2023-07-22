def somma_numeri_pari(n):
    """
    Calcola la somma dei numeri pari da 1 a n.
    
    Args:
        n (int): Limite superiore dei numeri da sommare.
    
    Returns:
        int: La somma dei numeri pari da 1 a n.
    """
    somma = 0
    i = 1
    while i <= n:
        if i % 2 == 0:
            somma += i
        i += 1
    return somma

def conta_vocali(parola):
    """
    Conta il numero di vocali in una parola.
    
    Args:
        parola (str): Parola di cui contare le vocali.
    
    Returns:
        int: Il numero di vocali nella parola.
    """
    vocali = 'aeiouAEIOU'


    conteggio = 0
    for lettera in parola:
        if lettera in vocali:
            conteggio += 1
    return conteggio

# Esempio di utilizzo delle funzioni

# Task 1: Calcolare la somma dei numeri pari
numero_limite = 10
risultato_somma = somma_numeri_pari(numero_limite)
print(f"La somma dei numeri pari da 1 a {numero_limite} è: {risultato_somma}")

# Task 2: Contare il numero di vocali
parola_input = "OpenAI"
risultato_conteggio = conta_vocali(parola_input)
print(f"Il numero di vocali nella parola '{parola_input}' è: {risultato_conteggio}")
